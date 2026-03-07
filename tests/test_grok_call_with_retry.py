import unittest
from unittest import mock

import grok


class _FakeCompletions:
    def __init__(self, result):
        self._result = result

    def create(self, **_kwargs):
        return self._result


class _FakeChat:
    def __init__(self, result):
        self.completions = _FakeCompletions(result)


class _FakeClient:
    def __init__(self, result):
        self.chat = _FakeChat(result)


class CallWithRetryTests(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
