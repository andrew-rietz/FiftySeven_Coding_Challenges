import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from computing_statistics.computing_statistics import StatsCalculator

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class StatsCalculatorTests(unittest.TestCase):
    """Tests the StatsCalculator class"""

    def setUp(self):
        self.calc = StatsCalculator()
        self.calc.population = [100, 200, 1000, 300]

    def test__population_is_2_4_6_8(self):
        self.calc.population = []
        self.calc.add_to_pop([2, "4", 6, "8"])
        self.assertEqual([2, 4, 6, 8], self.calc.population)

    def test__population_not_changed(self):
        self.calc.add_to_pop(["a", "b"])
        self.assertEqual([100, 200, 1000, 300], self.calc.population)

    def test__population_add_800(self):
        self.calc.add_to_pop(["800"])
        self.assertEqual([100, 200, 1000, 300, 800], self.calc.population)

    def test__min_is_100(self):
        self.assertEqual(100, self.calc.min())

    def test__max_is_1000(self):
        self.assertEqual(1000, self.calc.max())

    def test__mean_is_400(self):
        self.assertEqual(400, self.calc.mean())

    def test__stddev_is_353_55(self):
        self.assertEqual(353.55, round(self.calc.stddev(),2))

    def test_summary_is_success(self):
        expected_output = (
            "The average is 400.00.\n" +
            "The minimum is 100.00.\n" +
            "The maximum is 1,000.00.\n" +
            "The standard deviation is 353.55."
        )
        self.assertEqual(expected_output, self.calc.summary())



if __name__ == "__main__":
    unittest.main(verbosity=3)
