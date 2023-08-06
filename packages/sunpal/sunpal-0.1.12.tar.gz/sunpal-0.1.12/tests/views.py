import os
import sunpal
import unittest

api_key = os.environ.get("API_KEY_SUNPAL")
site = "sunwise-test"
sunpal.configure(api_key, site)


class TestCases(unittest.TestCase):
    def test_retrieve_views(self):
        entries = sunpal.Interactive.retrieve_views(
            "f0343240-dc16-4467-8476-b825059b484f"
        )

        for entry in entries:
            print(entry.view)

        self.assertTrue(True, True)

    def test_restart_views(self):
        sunpal.Interactive.restart_views("f0343240-dc16-4467-8476-b825059b484f")
        self.assertTrue(True, True)


if __name__ == "__main__":
    unittest.main()
