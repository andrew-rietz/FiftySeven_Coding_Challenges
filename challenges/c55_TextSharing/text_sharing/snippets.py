"""
Defines a `snippets` blueprint and its associated views, including CRUD views

Views:
    index: defines the main page of the site, dispays recent snippets
    create [login required]: create a new snippet
    view: view a snippet
    edit [login required]: edit a snippet
    delete [login required]: delete a snippet

Methods:
    login_required: defines a decorator function that requires a logged in user prior to
        execution of the decorated function / method.
"""
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
)
from werkzeug.exceptions import abort

from text_sharing.users import login_required
from text_sharing.psql_db import get_db

# Creates a blueprint named `snippets`
bp = Blueprint("snippets", __name__)


# Associate the view with its blueprint using bp.route
# The snippets are the main feature of our app, so it makes sense that it's at the index
@bp.route("/")
def index():
    """Queries database for all snippets, which are passed to index.html and displayed"""

    db = get_db()
    snippets = db.run_query(
        "SELECT s.id, title, body, created, author_id, username"
        " FROM snippet s JOIN users u ON s.author_id = u.id"
        " ORDER BY created DESC"
    )
    if not snippets:
        snippets = []
    return render_template("snippets/index.html", snippets=snippets)

@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Displays the view for creating a new snippet. Requires a logged in user.

    User will enter a title and body for the snippet. Title is reqired. The
    values are then stored in the database and associated with the logged in user.
    """

    if request.method == "POST":
        title = request.form.get("title", None)
        body = request.form.get("body", None)
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.run_query(
                "INSERT INTO snippet (title, body, author_id)" +
                " VALUES (%s, %s, %s)",
                (title, body, g.user["id"])
            )
            return redirect(url_for("snippets.index"))

    return render_template("snippets/create.html")

def get_snippet(id, check_author=True):
    """Queries the database for a specific snippet, based on the snippet id.

    This function is designed as a helper function for the 'view', 'edit', and
    'delete' views defined below. Each of the views will reference a specific snippet
    and the associated snippet id will be fed to this function.

    Throws errors if the snippet doesn't exist or if there are duplicate snippets.
    Also has an argument that governs whether the author id needs to match the id of
    the logged in user.

    Args:
        id (int): database id number for the snippet
        check_author (bool): optional input that govens whether the author id needs to match
            the id of the logged in user before return a snippet

    Returns:
        snippet (RealDictCursor): a snippet from the database
    """
    snippet = get_db().run_query(
        "SELECT s.id, title, body, created, author_id, username" +
        " FROM snippet s JOIN users u ON s.author_id = u.id" +
        " WHERE s.id = %s",
        (id,)
    )

    if snippet is None:
        # abort() will raise a special exception that returns a
        # HTTP status code. 404 == 'Not Found'
        abort(404, f"Snippet id {id} doesn't exist.")
    elif len(snippet) > 1:
        # should never happen, but...
        abort(404, f"Duplicate snippets with id {id}.")
    else:
        snippet = snippet[0]

    if check_author and snippet["author_id"] != g.user["id"]:
        abort(403)

    return snippet


# function takes an argument, `id`, which corresponds to the
# `<int:id>` in the route. Flask will capture the id, make sure
# it's an int and pass it as the id argument
@bp.route("/<int:id>/view", methods=("GET", "POST"))
def view(id):
    """
    Displays the entirety of a snippet for the end user to view. Also has a
    POST request option, where the user can click an 'edit' button to edit the
    snippet.

    Args:
        id (int): database id number for the snippet
    """
    snippet = get_snippet(id, check_author=False)

    if request.method == "POST":
        db = get_db()
        db.run_query(
            "UPDATE snippet SET title = %s, body = %s" +
            " WHERE id = %s",
            (snippet["title"], snippet["body"], id)
        )
        return redirect(url_for("snippets.index"))

    return render_template("snippets/view.html", snippet=snippet)


@bp.route("/<int:id>/edit", methods=("GET", "POST"))
@login_required
def edit(id):
    """
    Displays the entirety of a snippet for the end user to edit. Requires a logged
    in user

    Args:
        id (int): database id number for the snippet
    """
    snippet = get_snippet(id)

    if request.method == "POST":
        title = request.form.get("title", None)
        body = request.form.get("body", None)
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.run_query(
                "UPDATE snippet SET title = %s, body = %s" +
                " WHERE id = %s",
                (title, body, id)
            )
            return redirect(url_for("snippets.index"))

    return render_template("snippets/edit.html", snippet=snippet)

@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """
    Deletes a snippet from the database. Requires a logged in user

    Args:
        id (int): database id number for the snippet
    """
    # First query db to make sure snippet exists. get_snippet aborts unless a snippet is found
    get_snippet(id)
    db = get_db()
    db.run_query("DELETE FROM snippet WHERE id = %s", (id,))
    return redirect(url_for("snippets.index"))
