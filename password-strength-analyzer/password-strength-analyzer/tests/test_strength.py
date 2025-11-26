import unittest
from src.analyzer.strength import PasswordStrengthAnalyzer

class TestPasswordStrengthAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = PasswordStrengthAnalyzer()

    def test_strong_password(self):
        password = "Str0ngP@ssw0rd!"
        strength = self.analyzer.analyze_password(password)
        self.assertGreaterEqual(strength['score'], 3)

    def test_weak_password(self):
        password = "12345"
        strength = self.analyzer.analyze_password(password)
        self.assertLess(strength['score'], 3)

    def test_medium_password(self):
        password = "Password123"
        strength = self.analyzer.analyze_password(password)
        self.assertEqual(strength['score'], 2)

    def test_empty_password(self):
        password = ""
        strength = self.analyzer.analyze_password(password)
        self.assertEqual(strength['score'], 0)

    def test_password_with_common_patterns(self):
        password = "qwerty"
        strength = self.analyzer.analyze_password(password)
        self.assertLess(strength['score'], 3)

if __name__ == '__main__':
    unittest.main()