"""
Defines a `users` blueprint and its associated views

Views:
    register: registers a new user for the site
    login: logs a user into the site
    load_logged_in_user: checks for a user in the existing session, and attempts to load them
    logout: logs user out of the site and clears them from the session

Methods:
    login_required: defines a decorator function that requires a logged in user prior to
        execution of the decorated function / method.
"""
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for,
)
from werkzeug.security import (
    check_password_hash, generate_password_hash,
)

from text_sharing.psql_db import get_db

# Creates a blueprint named `users`
bp = Blueprint("users", __name__, url_prefix="/users")


# Associate the view with its blueprint using bp.route
# When Flask receives a request to /users/register, it will call the
# register view and use the returned value as the response
@bp.route("/register", methods=("GET", "POST"))
def register():
    """
    Checks user credentials from the registration form. Takes the username and
    password from the form, and queries against the DB. If a user is found,
    returns an error message. Otherwise, adds a new user to the database and stores
    their password hash.

    Redirects to the login form if successful. Otherwise redirects to the registration
    page.
    """
    if request.method == "POST":
        # `request.form` is a special dictionary that maps form
        # keys and their values
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif db.run_query(
                "SELECT id FROM users WHERE username = %s",
                (username,)
        ) is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.run_query(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                # Password is hashed for security
                (username, generate_password_hash(password))
            )
            # `redirect` generates a redirect response to the URL
            return redirect(url_for("users.login"))

        # `flash()` stores messages that can be retrieved when
        # rendering the template (HTML)
        flash(error)

    # `render_template()` renders a template containing the HTML
    return render_template("users/register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    """
    Checks user credentials from the login form. Takes the username and
    password from the login form, and queries against the DB. If a valid
    user is found, verifies that the password hash matches the expected value.

    If the inputs are valid, query the database for the associated
    user_id and store the information in g.user. Also set the session's
    user_id to the id of the user that just logged in.

    If user_id in the session is `None`, g.user is set to None
    """
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        db = get_db()
        error = None
        # Query the database for a user and return all columns
        # User is unique (primary key), so a single row is returned
        user = db.run_query(
            "SELECT * FROM users WHERE username = %s", (username,)
        )

        if not user:
            error = "Incorrect username."
        elif len(user) > 1:
            # Should never happen if users are added via register, but catch anyways
            error = "Duplicate users -- login failed"
        else:
            user = user[0]
            g.user = user

            # check_password_hash is a flask built-in
            if not check_password_hash(user["password"], password):
                error = "Incorrect password."

        if error is None:
            # session is a dictionary that stores data across requests
            # When validation succeeds, the user's `id` is stored in
            # a new session.
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

            # Now that the user's `id` is stored in the session,
            # it will be available on subsequent requests.
            # At the beginning of each request, if a user is logged in
            # their information should be loaded and available to views

        flash(error)

    return render_template("users/login.html")


# the `before_app_request` decorator registers a function that runs
# before the `view` function, no matter what URL is requested
@bp.before_app_request
def load_logged_in_user():
    """
    Checks user credentials from the session.
    If the inputs are valid, query the database for the associated
    user_id and store the information in g.user.

    If user_id in the session is `None`, g.user is set to None
    """
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        print(f"User ID: {user_id}")
        db = get_db()
        user = db.run_query(
            "SELECT * FROM users WHERE id = %s", (user_id,)
        )
        print(user)

        if user is None:
            g.user = None
        elif len(user) == 1:
            user = user[0]
            g.user = user


# To log out, you need to remove the user id from the session
@bp.route("/logout")
def logout():
    """ Logs the user out and removes their id from the session """
    session.clear()
    return redirect(url_for("index"))


def login_required(view):
    """
    Return a new view decorator function that wraps the original view
    it's applied to. The function checks if a user is loaded. If
    there is a user, the original view is called and normal
    operation continues. Otherwise redirects to the login page.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("users.login"))

        return view(**kwargs)

    return wrapped_view
