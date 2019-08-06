import unittest
import unittest.mock

from tests.context import password_validation

class PasswordValidationTests(unittest.TestCase):

    def setUp(self):
        self.users = password_validation.LoginSystem()

    def test_login_success(self):
        self.assertEqual(True, self.users.login("abc$123"))

    def test_login_fail(self):
        self.assertEqual(False, self.users.login("wrong_pw"))

if __name__ == "__main__":
    unittest.main()
