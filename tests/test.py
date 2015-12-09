from drone_tower import DroneTower, TowerCliError
import io
import os
import sys
import unittest


def skipEnv(*args):
    missing = []
    for arg in args:
        try:
            os.environ[arg]
        except:
            missing.append(arg)
    if missing:
        return unittest.skip(
            "environment variable undefined: {0}"
            .format(", ".join(missing)))
    return lambda func: func


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def tearDown(self):
        sys.stdin = sys.__stdin__

    def test_config_local(self):
        s = u"""\
{{
    "workspace": {{
        "path": "{path}"
    }},
    "vargs": {{
        "config": {{
            "username": "{username}",
            "password": "{password}",
            "host": "{host}",
            "verify_ssl": false
        }},
        "commands": [
            ["config"]
        ]
    }}
}}
"""
        sys.stdin = io.StringIO(s.format(
            path=self.path,
            username="user",
            password="secret",
            host="example.com"))
        DroneTower().run()

    @skipEnv('DRONE_TOWER_USERNAME',
             'DRONE_TOWER_PASSWORD',
             'DRONE_TOWER_HOST')
    def test_config_remote(self):
        s = u"""\
{{
    "workspace": {{
        "path": "{path}"
    }},
    "vargs": {{
        "config": {{
            "username": "{username}",
            "password": "{password}",
            "host": "{host}",
            "verify_ssl": false
        }},
        "commands": [
            ["config"],
            ["user", "list"]
        ]
    }}
}}
"""
        sys.stdin = io.StringIO(s.format(
            path=self.path,
            username=os.environ["DRONE_TOWER_USERNAME"],
            password=os.environ["DRONE_TOWER_PASSWORD"],
            host=os.environ["DRONE_TOWER_HOST"]))
        DroneTower().run()

    def test_config_failure(self):
        s = u"""\
{{
    "workspace": {{
        "path": "{path}"
    }},
    "vargs": {{
        "config": {{
            "username": "{username}",
            "password": "{password}",
            "host": "{host}",
            "verify_ssl": false
        }},
        "commands": [
            ["config"],
            ["user", "list"]
        ]
    }}
}}
"""
        sys.stdin = io.StringIO(s.format(
            path=self.path,
            username="user",
            password="password",
            host="example.com"))
        self.assertRaises(TowerCliError, lambda: DroneTower().run())


if __name__ == '__main__':
    unittest.main()
