import unittest
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from types import SimpleNamespace
from unittest import mock

import grok


class _FakeCompletions:
    def __init__(self, result):
        self._outcomes = list(result) if isinstance(result, list) else [result]
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        outcome = self._outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


class _FakeChat:
    def __init__(self, result):
        self.completions = _FakeCompletions(result)


class _FakeClient:
    def __init__(self, result):
        self.chat = _FakeChat(result)


class _FakeStream:
    def __init__(self, pieces):
        self._chunks = [
            SimpleNamespace(
                choices=[SimpleNamespace(delta=SimpleNamespace(content=piece))]
            )
            for piece in pieces
        ]

    def __iter__(self):
        return iter(self._chunks)


class CallWithRetryTests(unittest.TestCase):
    def test_request_includes_web_search_tool_by_default(self):
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='ok'))]
        )
        client = _FakeClient(response)

        with mock.patch.object(grok, 'MAX_RETRIES', 0), mock.patch.object(grok, 'log'):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.1, '[1/1]')

        self.assertEqual(result, 'ok')
        self.assertTrue(client.chat.completions.calls[0]['stream'])
        self.assertEqual(
            client.chat.completions.calls[0]['extra_body'],
            {'tools': [{'type': 'web_search'}]},
        )

    def test_retry_respects_server_retry_after_body(self):
        error = Exception('524 timeout')
        error.body = {'retry_after': 120}
        error.status_code = 524
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='ok'))]
        )
        client = _FakeClient([error, response])

        with mock.patch.object(grok, 'MAX_RETRIES', 1), \
             mock.patch.object(grok, 'time') as fake_time, \
             mock.patch.object(grok, 'log'):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.1, '[1/1]')

        self.assertEqual(result, 'ok')
        fake_time.sleep.assert_called_once_with(120)

    def test_retry_respects_server_retry_after_header_date(self):
        error = Exception('Rate limited')
        future_time = datetime.now(timezone.utc) + timedelta(seconds=65)
        error.response = SimpleNamespace(
            headers={'retry-after': format_datetime(future_time)}
        )
        error.status_code = 429
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='ok'))]
        )
        client = _FakeClient([error, response])

        with mock.patch.object(grok, 'MAX_RETRIES', 1), \
             mock.patch.object(grok, 'time') as fake_time, \
             mock.patch.object(grok, 'log'):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.1, '[1/1]')

        self.assertEqual(result, 'ok')
        # Should sleep for roughly 65 seconds (allowing a tiny delta for test execution time)
        called_delay = fake_time.sleep.call_args[0][0]
        self.assertTrue(60 <= called_delay <= 65)

    def test_retry_respects_server_retry_after_header_seconds(self):
        error = Exception('Rate limited')
        error.response = SimpleNamespace(
            headers={'retry-after': '45'}
        )
        error.status_code = 429
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='ok'))]
        )
        client = _FakeClient([error, response])

        with mock.patch.object(grok, 'MAX_RETRIES', 1), \
             mock.patch.object(grok, 'time') as fake_time, \
             mock.patch.object(grok, 'log'):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.1, '[1/1]')

        self.assertEqual(result, 'ok')
        fake_time.sleep.assert_called_once_with(45)

    def test_retry_falls_back_to_jittered_exponential_backoff_on_generic_error(self):
        error = Exception('Generic error')
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='ok'))]
        )
        client = _FakeClient([error, response])

        with mock.patch.object(grok, 'MAX_RETRIES', 1), \
             mock.patch.object(grok, 'time') as fake_time, \
             mock.patch.object(grok, 'log'), \
             mock.patch('random.uniform', return_value=3.5):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.1, '[1/1]')

        self.assertEqual(result, 'ok')
        fake_time.sleep.assert_called_once_with(3.5)