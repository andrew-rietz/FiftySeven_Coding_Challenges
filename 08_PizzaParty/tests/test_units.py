import unittest
import unittest.mock

from tests.context import pizza_party

class PizzaPartyTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["3", "2", "6"]
        self.pizza_calc = pizza_party.PizzaCalc()

    def test_people_is_3(self):
        self.assertEqual(3, self.pizza_calc.people)

    def test_pizzas_is_2(self):
        self.assertEqual(2, self.pizza_calc.pizzas)

    def test_slices_per_pizza_is_4(self):
        self.assertEqual(6, self.pizza_calc.slices_per_pizza)

if __name__ == "__main__":
    unittest.main()
