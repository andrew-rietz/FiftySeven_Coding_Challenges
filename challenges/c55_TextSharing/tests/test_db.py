import os
import sys
import unittest
import psycopg2

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import test_helpers
from test_helpers import captured_output, BaseFlaskTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import text_sharing
from text_sharing import psql_db

class PSQLDatabaseTest(BaseFlaskTest):
    """Tests the methods of the PSQLDatabase Class"""

    def test__open_new_connection(self):
        # Open connections have a 'closed' value of zero
        self.db.conn = None
        with captured_output():
            self.db.open_connection()
        self.assertEqual(self.db.conn.closed, 0)

    def test__open_existing_connection(self):
        # Open connections have a 'closed' value of zero
        with captured_output():
            self.db.open_connection()
        self.assertEqual(self.db.conn.closed, 0)

    def test__close_connection(self):
        with captured_output():
            self.db.close_connection()
        self.assertEqual(self.db.conn.closed, 1)

    def test__load_schema(self):
        actual_tables = []
        expected_tables = ['users', 'snippet']
        with captured_output():
            self.db.open_connection()
            cur = self.db.conn.cursor()
            for table in expected_tables:
                cur.execute(
                    "select exists(select * from information_schema.tables " +
                    "where table_name=%s)", (table,)
                )
                actual_tables.append(cur.fetchone()[0])
        self.assertEqual(True, all(actual_tables))

    def test__clear_schema(self):
        actual_tables = []
        with captured_output():
            self.db.clear_schema()
            self.db.open_connection()
            cur = self.db.conn.cursor()
            cur.execute(
                "SELECT table_name FROM information_schema.tables " +
                "WHERE table_schema = 'public'"
            )
            for table in cur.fetchall():
                actual_tables.append(table)
        self.assertEqual([], actual_tables)

    def test__run_query__insert(self):
        with captured_output():
            self.db.run_query(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                ("un1", "pw1")
            )
            cur = self.db.conn.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username='un1'"
            )
            result = cur.fetchall()
        self.assertEqual(len(result), 1)

    def test__run_query__select(self):
        with captured_output():
            self.db.open_connection()
            cur = self.db.conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                ("un1", "pw1")
            )
            result = self.db.run_query(
                "SELECT * FROM users WHERE username=%s", ("un1", )
            )
        self.assertEqual(len(result), 1)

class DatabaseFunctionsTests(BaseFlaskTest):
    """Tests the global functions in the module"""

    def test__get_db(self):
        fresh_db = None
        with captured_output():
            with self.app_context:
                fresh_db = psql_db.get_db()
                fresh_db.load_schema()
        self.assertIsNotNone(self.db)

    def test__close_db(self):
        # the close_db method interacts with Flask's g object, which lives
        # within the request_context rather than the app_context
        with captured_output():
            with self.app.test_request_context() as trc:
                trc.g.db = psql_db.get_db()
                trc.g.db.open_connection()
                psql_db.close_db()

        self.assertNotEqual(self.db.conn.closed, 0)

class CliFunctionTest(BaseFlaskTest):
    def test__init_db_command(self):
        runner = self.app.test_cli_runner()
        with captured_output():
            result = runner.invoke(args="init-db")

        self.assertIn("Initialized the database.", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=3)
