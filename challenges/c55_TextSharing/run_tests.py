import unittest

from tests import test_db, test_helpers, test_snippets, test_users

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTests(loader.loadTestsFromModule(test_db))
suite.addTests(loader.loadTestsFromModule(test_helpers))
suite.addTests(loader.loadTestsFromModule(test_snippets))
suite.addTests(loader.loadTestsFromModule(test_users))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
