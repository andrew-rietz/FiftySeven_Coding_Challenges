import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_strength_indicator import password_strength_indicator

class PasswordValidatorTests(unittest.TestCase):
    """Tests the password_validator function"""

    def test__spaces_returns_None(self):
        self.assertEqual(None, password_strength_indicator.password_validator("s p a c e s"))

    def test__five_characters__only_numbers__returns_1(self):
        self.assertEqual(1, password_strength_indicator.password_validator("12345"))

    def test__less_than_8_chars__only_alpha__returns_2(self):
        self.assertEqual(2, password_strength_indicator.password_validator("abcdefg"))

    def test__less_than_8_chars__mixed_alphanum_and_special__returns_2(self):
        self.assertEqual(2, password_strength_indicator.password_validator("abc123!"))

    def test__at_least_8_chars__mixed_alphanum__returns_3(self):
        self.assertEqual(3, password_strength_indicator.password_validator("abcd1234"))

    def test__more_than_8_chars__mixed_alphanum_and_special__returns_4(self):
        self.assertEqual(4, password_strength_indicator.password_validator("1337h@xor!"))


if __name__ == "__main__":
    unittest.main()
