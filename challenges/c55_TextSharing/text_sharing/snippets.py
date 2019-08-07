import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
)
from werkzeug.exceptions import abort

from text_sharing.users import login_required
from text_sharing.psql_db import get_db

# Creates a blueprint named `snippets`
# >>> The snippets are the main feature of our app, so it makes sense
# >>> that it's at the index
bp = Blueprint("snippets", __name__)


# Associate the view with its blueprint using bp.route
@bp.route("/")
def index():
    """Creates a """
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
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
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
    snippet = get_db().run_query(
        "SELECT s.id, title, body, created, author_id, username" +
        " FROM snippet s JOIN users u ON s.author_id = u.id" +
        " WHERE s.id = %s",
        (id,)
    )

    if snippet is None:
        # abort() will raise a special exception that returns a
        # HTTP status code. It takes an optional message to
        # show with the error, otherwise a default message is used
        # 404 == 'Not Found'
        # 403 = 'Forbidden'
        abort(404, f"Snippet id {id} doesn't exist.")
    elif len(snippet) > 1:
        error = "Duplicate snippets -- selection failed"
    else:
        snippet = snippet[0]

    # the `check_author` argument is defined so that the function
    # can be used to get a `post` without checking the author
    # This would be helpful if you wrote a view to show an individual
    # post on a page, where the user doesn't matter because they're
    # not modifying the post.
    if check_author and snippet["author_id"] != g.user["id"]:
        abort(403)

    return snippet


# Unlike the views we've written so far, the `update` function
# takes an argument, `id`, which corresponds to the
# `<int:id>` in the route. Flask will capture the id, make sure
# it's an int and pass it as the id argument. If you don't
# specify `int:` and instead do `<id>`, it will be a string.
@bp.route("/<int:id>/view", methods=("GET", "POST"))
def view(id):
    snippet = get_snippet(id, check_author=False)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
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

    return render_template("snippets/view.html", snippet=snippet)


@bp.route("/<int:id>/edit", methods=("GET", "POST"))
@login_required
def edit(id):
    snippet = get_snippet(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
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
    get_snippet(id)
    db = get_db()
    db.run_query("DELETE FROM snippet WHERE id = %s", (id,))
    return redirect(url_for("snippets.index"))
