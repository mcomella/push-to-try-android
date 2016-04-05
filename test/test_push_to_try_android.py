import json
import os
import unittest

PATH_TO_CONFIG = os.path.dirname(os.path.realpath(__file__)) + '/../config.json'

class TestPushToTry(unittest.TestCase):

    def test_config_format(self):
        with open(PATH_TO_CONFIG, 'r') as f:
            config = json.load(f)
            self.assertIsNotNone(config)

if __name__ == '__main__':
    unittest.main()
