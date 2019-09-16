import os
import sys
import unittest
import psycopg2
from flask import Flask

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import test_helpers
from test_helpers import captured_output, BaseFlaskTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import text_sharing
from text_sharing import users

class RegisterTests(BaseFlaskTest):

    def test__register_get_status(self):
        result = self.client.get("/users/register")
        self.assertEqual(200, result.status_code)

    def test__register_get_url(self):
        result = self.client.get("/users/register")
        redirect_url = result.headers.get("location)")
        self.assertIsNone(redirect_url)

    def test__register_no_username(self):
        with captured_output():
            result = self.client.post(
                "/users/register",
                data={"password": "test"},
                follow_redirects=True,
            )
        self.assertIn(b'Username is required.', result.data)

    def test__register_no_password(self):
        with captured_output():
            result = self.client.post(
                "/users/register",
                data={"username": "test"},
                follow_redirects=True,
            )
        self.assertIn(b'Password is required.', result.data)

    def test__register_already_registered(self):
        with captured_output():
            result = self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"},
                follow_redirects=True,
            )
            result = self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"},
                follow_redirects=True,
            )
        self.assertIn(b'User test is already registered.', result.data)

    def test__register_post_status_success(self):
        with captured_output():
            result = self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"},
                follow_redirects=True
            )
        self.assertEqual(200, result.status_code)

    def test__register_post_url(self):
        with captured_output():
            result = self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"},
            )
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/users/login"
        self.assertEqual(redirect_url, expected_url)

class LoginTests(BaseFlaskTest):

    def setUp(self):
        with captured_output():
            super().setUp()
            self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"}
            )

    def test__login_get_status(self):
        result = self.client.get("/users/login")
        self.assertEqual(200, result.status_code)

    def test__login_get_url(self):
        result = self.client.get("/users/login")
        redirect_url = result.headers.get("location)")
        self.assertIsNone(redirect_url)

    def test__login_wrong_username(self):
        with captured_output():
            result = self.client.post(
                "/users/login",
                data={"username": "test_wrong", "password": "test"},
                follow_redirects=True,
            )
        self.assertIn(b'Incorrect username.', result.data)

    def test__login_wrong_password(self):
        with captured_output():
            result = self.client.post(
                "/users/login",
                data={"username": "test", "password": "test_wrong"},
                follow_redirects=True,
            )
        self.assertIn(b'Incorrect password.', result.data)

    def test__login_post_status_success(self):
        with captured_output():
            result = self.client.post(
                "/users/login",
                data={"username": "test", "password": "test"},
                follow_redirects=True
            )
        self.assertEqual(200, result.status_code)

    def test__login_post_url(self):
        with captured_output():
            result = self.client.post(
                "/users/login",
                data={"username": "test", "password": "test"},
            )
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/"
        self.assertEqual(redirect_url, expected_url)

class LoadLoggedInTest(BaseFlaskTest):
    def setUp(self):
        super().setUp()
        with captured_output():
            self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"},
                follow_redirects=True,
            )
            self.client.post(
                "/users/login",
                data={"username": "test", "password": "test"},
                follow_redirects=True,
            )

    def test__user_is_test(self):
        with captured_output():
            with self.client.session_transaction() as sess:
                sess["user_id"] = "1"
            with self.app.test_request_context("/") as trc:
                trc.session = sess
                users.load_logged_in_user()
                g_user = trc.g.get("user")
        self.assertEqual("test", g_user.get("username"))

    def test__user_is_None(self):
        with captured_output():
            with self.client.session_transaction() as sess:
                sess.pop("user_id", None)
            with self.app.test_request_context("/") as trc:
                trc.session = sess
                users.load_logged_in_user()
                g_user = trc.g.get("user", None)
        self.assertEqual(None, g_user)

class LogoutTest(BaseFlaskTest):
    def setUp(self):
        super().setUp()
        with captured_output():
            self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"}
            )
            self.client.post(
                "/users/login",
                data={"username": "test", "password": "test"}
            )

    def test__logout_redirects_to_index(self):
        with self.app.test_request_context("/users/login"):
            result = users.logout()
        redirect_url = result.headers.get("location")
        expected_url = "/"
        self.assertEqual(redirect_url, expected_url)

class LoginRequiredTests(LoadLoggedInTest):
    def test__user_is_test(self):
        with captured_output():
            with self.app.test_request_context("/create") as trc:
                trc.g.user = self.db.run_query(
                    "SELECT * FROM users WHERE id = %s", (1,)
                )[0]
                g_user = trc.g.user
        self.assertEqual("test", g_user.get("username"))

    def test__user_is_None(self):
        with captured_output():
            with self.app.test_request_context("/create") as trc:
                trc.g.user = None
                g_user = trc.g.user
        self.assertEqual(None, g_user)

if __name__ == "__main__":
    unittest.main(verbosity=3)
