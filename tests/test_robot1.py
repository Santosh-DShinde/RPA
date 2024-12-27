import unittest
from robot1 import automate_browser

class TestRobot1(unittest.TestCase):
    def test_browser_automation(self):
        try:
            automate_browser()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Automation failed: {e}")

if __name__ == "__main__":
    unittest.main()