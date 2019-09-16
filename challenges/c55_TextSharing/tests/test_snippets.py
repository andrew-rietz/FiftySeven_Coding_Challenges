import os
import sys
import unittest
import psycopg2
import werkzeug.exceptions
from werkzeug.exceptions import abort

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import test_helpers
from test_helpers import captured_output, BaseFlaskTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import text_sharing
from text_sharing import snippets, users

def login_user(client=None, username="test"):
    client.post(
        "/users/login",
        data={"username": username, "password": "test"}
    )

class BaseSnippetTest(BaseFlaskTest):
    def setUp(self):
        with captured_output():
            super().setUp()
            self.client.post(
                "/users/register",
                data={"username": "test", "password": "test"}
            )
            self.client.post(
                "/users/register",
                data={"username": "test2", "password": "test"}
            )
            self.db.run_query(
                "INSERT INTO snippet (title, body, author_id) VALUES (%s, %s, %s)",
                ("test_title1", "test_body1", 1)
            )
            self.db.run_query(
                "INSERT INTO snippet (title, body, author_id) VALUES (%s, %s, %s)",
                ("test_title2", "test_body2", 1)
            )

class IndexTests(BaseSnippetTest):
    def test__snippets_exist(self):
        with captured_output():
            result = self.client.get("/")
            snippets_exist = (b'test_title2' in result.data) and (b'test_title1' in result.data)
        self.assertTrue(snippets_exist)

class CreateSnippetTests(BaseSnippetTest):
    def test__not_logged_in(self):
        result = self.client.get("/create")
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/users/login"
        self.assertEqual(redirect_url, expected_url)

    def test__get_status_code_200(self):
        with captured_output():
            login_user(self.client)
            result = self.client.get("/create")
        self.assertEqual(200, result.status_code)

    def test__get_render_create_html(self):
        with captured_output():
            login_user(self.client)
            result = self.client.get("/create")
        self.assertIn(b'New Post', result.data)

    def test__post_no_title(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/create",
                data={"title": None, "body": "test"}
            )
        self.assertIn(b'Title is required.', result.data)

    def test__post_success_status(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/create",
                data={"title": "test", "body": "test"},
                follow_redirects=True
            )
        self.assertEqual(200, result.status_code)

    def test__post_success(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/create",
                data={"title": "test", "body": "test"}
            )
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/"
        self.assertEqual(redirect_url, expected_url)

class ViewSnippetTests(BaseSnippetTest):
    def test__get_status_code_200(self):
        with captured_output():
            login_user(self.client)
            result = self.client.get("/1/view")
        self.assertEqual(200, result.status_code)

    def test__get_render_view_html(self):
        with captured_output():
            login_user(self.client)
            result = self.client.get("/1/view")
        self.assertIn(b'test_title1', result.data)

    def test__post_no_snippet(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/999/view",
            )
        self.assertEqual(404, result.status_code)

    def test__post_success_status(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/1/view",
                follow_redirects=True
            )
        self.assertEqual(200, result.status_code)

    def test__post_success(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/1/view",
            )
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/"
        self.assertEqual(redirect_url, expected_url)

class GetSnippetTests(BaseSnippetTest):
    def test__snippet_doesnt_exist(self):
        with captured_output():
            with self.assertRaises(werkzeug.exceptions.NotFound):
                # abort 404 == NotFound
                with self.app_context:
                    snippets.get_snippet("999")

    def test__valid_snippet_no_check_author(self):
        with captured_output():
            with self.app_context:
                with self.client.session_transaction() as sess:
                    sess["user_id"] = "2"
                with self.app.test_request_context() as trc:
                    trc.session = sess
                    users.load_logged_in_user()
                    snippet = snippets.get_snippet("1", check_author=False)
        self.assertEqual("test_title1", snippet["title"])

    def test__valid_snippet_check_author_passes(self):
        with captured_output():
            with self.app_context:
                with self.client.session_transaction() as sess:
                    sess["user_id"] = "1"
                with self.app.test_request_context() as trc:
                    trc.session = sess
                    users.load_logged_in_user()
                    snippet = snippets.get_snippet("1", check_author=True)
        self.assertEqual("test_title1", snippet["title"])

    def test__valid_snippet_check_author_fails(self):
        with captured_output():
            with self.app_context:
                with self.client.session_transaction() as sess:
                    sess["user_id"] = "2"
                with self.assertRaises(werkzeug.exceptions.Forbidden):
                    # abort 403 == Forbidden
                    with self.app.test_request_context() as trc:
                        trc.session = sess
                        users.load_logged_in_user()
                        snippets.get_snippet("1", check_author=True)

class EditSnippetTests(BaseSnippetTest):
    def test__not_logged_in(self):
        result = self.client.get("/1/edit")
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/users/login"
        self.assertEqual(redirect_url, expected_url)

    def test__get_status_code_200(self):
        with captured_output():
            login_user(self.client)
            result = self.client.get("/1/edit")
        self.assertEqual(200, result.status_code)

    def test__get_render_edit_html(self):
        with captured_output():
            login_user(self.client)
            result = self.client.get("/1/edit")
        self.assertIn(b'Edit "test_title1"', result.data)

    def test__edit_no_title(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/1/edit",
                data={"title": None, "body": "test"}
            )
        self.assertIn(b'Title is required.', result.data)

    def test__edit_success_status(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/1/edit",
                data={"title": "test", "body": "test"},
                follow_redirects=True
            )
        self.assertEqual(200, result.status_code)

    def test__edit_success(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post(
                "/1/edit",
                data={"title": "test", "body": "test"}
            )
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/"
        self.assertEqual(redirect_url, expected_url)

class DeleteSnippetTests(BaseSnippetTest):
    def test__not_logged_in(self):
        result = self.client.post("/1/delete")
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/users/login"
        self.assertEqual(redirect_url, expected_url)

    def test__delete_snippet_success(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post("/1/delete")
        redirect_url = result.headers.get("location")
        expected_url = "http://localhost/"
        self.assertEqual(redirect_url, expected_url)

    def test__delete_snippet_doesnt_exist_returns_404(self):
        with captured_output():
            login_user(self.client)
            result = self.client.post("/999/delete")
        self.assertEqual(404, result.status_code)

    def test__delete_snippet_wrong_author_returns_403(self):
        with captured_output():
            login_user(self.client, "test2")
            result = self.client.post("/1/delete")
        self.assertEqual(403, result.status_code)

if __name__ == "__main__":
    unittest.main(verbosity=3)
