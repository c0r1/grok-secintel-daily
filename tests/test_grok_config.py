import os
import unittest
from unittest import mock

import grok


class LoadEnvConfigTests(unittest.TestCase):
    def test_reads_api_key_and_base_url_from_environment(self):
        env = {
            'XAI_API_KEY': 'sk-from-env',
            'XAI_BASE_URL': 'https://gateway.example/v1',
        }

        with mock.patch.dict(os.environ, env, clear=False):
            api_key, base_url = grok.load_env_config()

        self.assertEqual(api_key, 'sk-from-env')
        self.assertEqual(base_url, 'https://gateway.example/v1')


if __name__ == '__main__':
    unittest.main()
