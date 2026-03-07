import unittest
from datetime import datetime
from unittest import mock
from zoneinfo import ZoneInfo

import grok


class BuildClientTests(unittest.TestCase):
    def test_main_uses_plain_user_agent_for_openai_client(self):
        fake_now = datetime(2026, 3, 7, 7, 0, 0, tzinfo=ZoneInfo('Asia/Shanghai'))
        fake_client = object()

        with mock.patch.object(grok, 'OpenAI', return_value=fake_client) as openai_ctor, \
             mock.patch.object(grok, 'get_now', return_value=fake_now), \
             mock.patch.object(grok, 'is_dry_run', return_value=False), \
             mock.patch.object(grok, 'load_env_config', return_value=('sk-test', 'https://example.com/v1')), \
             mock.patch.object(grok, 'load_prompt_template', return_value='prompt'), \
             mock.patch.object(grok, 'sequential_call_grok_fast', return_value=['draft']), \
             mock.patch.object(grok, 'call_thinking_model', return_value='report'), \
             mock.patch.object(grok, 'inject_generated_time', return_value='report'), \
             mock.patch.object(grok, 'save_to_file', return_value='outputs/2026/03/2026-03-07.md'), \
             mock.patch.object(grok, 'save_latest', return_value='LATEST.md'), \
             mock.patch.object(grok, 'log'):
            grok.main()

        openai_ctor.assert_called_once_with(
            api_key='sk-test',
            base_url='https://example.com/v1',
            timeout=grok.API_TIMEOUT,
            default_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'},
        )


if __name__ == '__main__':
    unittest.main()
