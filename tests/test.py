from drone_tower import DroneTower
import io
import os
import sys
import unittest


class TestDroneTower(unittest.TestCase):

    def setUp(self):
        self.stdin = sys.stdin

    def tearDown(self):
        sys.stdin = self.stdin

    def test_config(self):
        sys.stdin = io.StringIO(u"""\
{{
    "workspace": {{
        "path": "{path}"
    }},
    "vargs": {{
        "config": {{
            "username": "drone",
            "password": "5uper5ecret",
            "host": "127.0.0.1:10443",
            "verify_ssl": false
        }},
        "commands": [
            ["config"],
            ["user", "list"]
        ]
    }}
}}
""".format(path=os.path.dirname(os.path.realpath(__file__))))
        DroneTower().run()

if __name__ == '__main__':
    unittest.main()
