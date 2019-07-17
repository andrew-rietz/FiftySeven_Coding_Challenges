import unittest
import unittest.mock

from tests.context import rectangular_area

class RectangularAreaTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["10", "20"]
        self.rectangle_calc = rectangular_area.Calculator()

    def test_length_is_10(self):
        self.assertEqual(10, self.rectangle_calc.len)

    def test_width_is_20(self):
        self.assertEqual(20, self.rectangle_calc.width)


if __name__ == "__main__":
    unittest.main()
