import unittest

from tests import test_integration
from tests import test_units

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTests(loader.loadTestsFromModule(test_integration))
suite.addTests(loader.loadTestsFromModule(test_units))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
