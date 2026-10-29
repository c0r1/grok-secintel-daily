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


class CallWithRetryTests(unittest.TestCase):
    def test_request_includes_web_search_tool_by_default(self):
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='ok'))]
        )
        client = _FakeClient(response)

        with mock.patch.object(grok, 'MAX_RETRIES', 0), mock.patch.object(grok, 'log'):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.1, '[1/1]')

        self.assertEqual(result, 'ok')
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
            fake_time.time.return_value = 0.0
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.7, '[汇总]')

        self.assertEqual(result, 'ok')
        fake_time.sleep.assert_called_once_with(120.0)

    def test_retry_after_http_date_is_parsed(self):
        error = Exception('503 unavailable')
        retry_at = datetime.now(timezone.utc) + timedelta(seconds=90)
        error.response = SimpleNamespace(
            headers={'retry-after': format_datetime(retry_at, usegmt=True)}
        )

        delay = grok.get_retry_after_seconds(error)

        self.assertIsNotNone(delay)
        self.assertGreater(delay, 80)
        self.assertLessEqual(delay, 90)

    def test_permanent_client_error_is_not_retried(self):
        error = Exception('400 invalid request')
        error.status_code = 400
        client = _FakeClient([error])

        with mock.patch.object(grok, 'MAX_RETRIES', 2), mock.patch.object(grok, 'log'):
            result = grok.call_with_retry(client, grok.FAST_MODEL, 'prompt', 0.7, '[1/1]')

        self.assertIsNone(result)
        self.assertEqual(len(client.chat.completions.calls), 1)

    def test_parses_sse_string_response(self):
        response = "\n\n".join(
            [
                'data: {"choices":[{"delta":{"role":"assistant","content":""}}]}',
                'data: {"choices":[{"delta":{"content":"你"}}]}',
                'data: {"choices":[{"delta":{"content":"好"}}]}',
                'data: [DONE]',
            ]
        )
        client = _FakeClient(response)

        with mock.patch.object(grok, 'MAX_RETRIES', 0), mock.patch.object(grok, 'log'):
            content = grok.call_with_retry(client, 'grok-4.1-fast', 'prompt', 0.1, '[1/1]')

        self.assertEqual(content, '你好')

    def test_parses_sse_string_response_with_comment_preamble(self):
        response = "\n\n".join(
            [
                ': ping',
                'data: {"choices":[{"delta":{"content":"你"}}]}',
                'data: {"choices":[{"delta":{"content":"好"}}]}',
                'data: [DONE]',
            ]
        )
        client = _FakeClient(response)

        with mock.patch.object(grok, 'MAX_RETRIES', 0), mock.patch.object(grok, 'log'):
            content = grok.call_with_retry(client, 'grok-4.1-fast', 'prompt', 0.1, '[1/1]')

        self.assertEqual(content, '你好')

    def test_rejects_non_sse_string_response(self):
        client = _FakeClient('{"error":"blocked"}')

        with mock.patch.object(grok, 'MAX_RETRIES', 0), mock.patch.object(grok, 'log'):
            content = grok.call_with_retry(client, 'grok-4.1-fast', 'prompt', 0.1, '[1/1]')

        self.assertIsNone(content)

    def test_strips_think_block_from_sse_string_response(self):
        response = "\n\n".join(
            [
                'data: {"choices":[{"delta":{"content":"<think>\\n内部推理\\n</think>\\n正式内容"}}]}',
                'data: [DONE]',
            ]
        )
        client = _FakeClient(response)

        with mock.patch.object(grok, 'MAX_RETRIES', 0), mock.patch.object(grok, 'log'):
            content = grok.call_with_retry(client, 'grok-4.1-fast', 'prompt', 0.1, '[1/1]')

        self.assertEqual(content, '正式内容')

    def test_strips_unterminated_think_block(self):
        self.assertEqual(grok.sanitize_model_output('<think>\n内部推理'), '')

    def test_call_thinking_model_uses_single_summary_prompt(self):
        contents = ['draft-1', 'draft-2', 'draft-3']

        with mock.patch.object(grok, 'call_with_retry', return_value='summary-1') as retry_call, \
             mock.patch.object(grok, 'log'):
            result = grok.call_thinking_model(mock.Mock(), contents)

        self.assertEqual(result, 'summary-1')
        retry_call.assert_called_once()
        self.assertEqual(retry_call.call_args.kwargs['use_web_search'], False)
        self.assertEqual(retry_call.call_args.args[3], 0.7)
        prompt = retry_call.call_args.args[2]
        self.assertIn('【第 1 份内容】\ndraft-1', prompt)
        self.assertIn('【第 2 份内容】\ndraft-2', prompt)
        self.assertIn('【第 3 份内容】\ndraft-3', prompt)


if __name__ == '__main__':
    unittest.main()
