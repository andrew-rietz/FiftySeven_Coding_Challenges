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
# Like the application object, this needs to know where it's
# defined, so we pass in __name__ as the second argument
# `url_prefix` will be prepended to all URLs associated with
# the blueprint
bp = Blueprint("users", __name__, url_prefix="/users")


# Associate the view with its blueprint using bp.route
# When Flask receives a request to /users/register, it will call the
# register view and use the returned value as the response
@bp.route("/register", methods=("GET", "POST"))
def register():
    """
    Checks inputs from the login form
    CHECKS:
    - username has a value
    - password has a value
    - username is new (does not exist in database)

    SUCCESS:
    - user added to database
    - database saved (commit)
    - redirects to the login

    FAILURE:
    - tracks errors and passes to "flash"
    - renders the register HTML
    """
    if request.method == "POST":
        # `request.form` is a special dictionary that maps form
        # keys and their values
        username = request.form["username"]
        password = request.form["password"]
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
    Checks inputs from the login form
    CHECKS:
    - username exists in database
    - hashed password matches database password hash

    SUCCESS:
    - logs in user
    - stores their id in a cookie
    - redirects to the index

    FAILURE:
    - tracks errors and passes to "flash"
    - renders the login HTML
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
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
            error = "Duplicate users -- login failed"
        else:
            user = user[0]
            g.user = user

            if not check_password_hash(user["password"], password):
                error = "Incorrect password."

        if error is None:
            # session is a dictionary that stores data across requests
            # When validation succeeds, the user's `id` is stored in
            # a new session as a cookie. Flask securely signs
            # cookies so they can't be tampered with
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

            # Now that the user's `id` is stored in the session,
            # it will be available on subsequent requests.
            # At the beginning of each request, if a user is logged in
            # their information should be loaded and available to
            # views

        flash(error)

    return render_template("users/login.html")


# the `before_app_request` decorator registers a function that runs
# before the `view` function, no matter what URL is requested
@bp.before_app_request
def load_logged_in_user():
    """
    Checks inputs from the login form
    CHECKS:
    - user_id is stored as a cookie in the session

    SUCCESS:
    - queries the database for the user_id
    - stores the user data in g.user

    FAILURE:
    - g.user is set to None
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

# Create a new decorator `login_required` that can be applied
# to other functions
def login_required(view):
    """
    Return a new view function that wraps the original view
    it's applied to.

    CHECKS:
    - user is loaded (not None)

    SUCCESS:
    - original view is called and continues normally

    FAILURE:
    - redirects to the login page
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("users.login"))

        return view(**kwargs)

    return wrapped_view
