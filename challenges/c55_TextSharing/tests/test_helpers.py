import io
import os
import sys
import unittest
from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import text_sharing
from text_sharing import create_app, psql_db


@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class BaseFlaskTest(unittest.TestCase):
    """Establishes create_app, setUp, and tearDown methods to be inherited by other test classes"""

    def setUp(self):
        self.app = create_app(testing="instance.config.TestConfig")

        # create a test client
        self.client = self.app.test_client()
        self.app.testing = True

        self.app_context = self.app.app_context()
        # psql_db.init_app(self.app)
        with captured_output():
            with self.app_context:
                self.db = psql_db.get_db()
                self.db.load_schema()

    def tearDown(self):
        with captured_output():
            self.db.clear_schema()
            self.db.close_connection()

class HelloWorldTest(BaseFlaskTest):
    """Basic 'hello world' test to make sure that test setup is working"""
    def test_home_status_code(self):
        result = self.client.get('/hello')
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        result = self.client.get('/hello')
        self.assertEqual(result.data.decode('UTF-8'), "Hello, World!")

if __name__ == "__main__":
    unittest.main(verbosity=3)
