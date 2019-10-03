"""Defines the routes for handling user registration / authentication"""
from flask import current_app as app
from . import db
from .models import User
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask import g as flask_g
from flask import session as flask_session
from flask.views import View
from werkzeug.security import check_password_hash, generate_password_hash


# A blueprint is an object that allows defining application functions without
# requiring an application object ahead of time. Will register to the app later
users_bp = Blueprint(name='users', import_name=__name__, url_prefix="/users")

class BaseUserView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

    def get_objects(self):
        raise NotImplementedError()

class Users(BaseUserView):
    methods = ["GET", "POST"]

    @classmethod
    def get_template_name(self):
        return "users/login.html"

    def get_objects(self):
        return User.query.all()

    def register(self):
        if request.method == "POST":
            username = request.form.get("username", None)
            email = request.form.get("email", None)
            password = request.form.get("password", None)

            error = None
            if not email:
                error = "Email is required."
            elif not username:
                error = "Username is required."
            elif not password:
                error = "Password is required."
            elif User.query.filter_by(username=username).first() is not None:
                error = f"User {username} is already registered."

            if error is None:
                hashed_pw = generate_password_hash(password)
                new_user = User(username=username, email=email, password=hashed_pw)

                # The session here is not the Flask session, but the Flask-SQLAlchemy one.
                # It is essentially a beefed up version of a database transaction.
                db.session.add(new_user)
                db.session.commit()
                flash("Registration successful")
                return redirect(url_for("users.login"))

            flash(error)

        return self.render_template(context={})

    def login(self):
        if request.method == "POST":
            username = request.form.get("username", None)
            password = request.form.get("password", None)

            error = None
            if not username:
                error = "Username is required."
            elif not password:
                error = "Password is required."
            else:
                user = User.query.filter_by(username=username).first()
                if user is None or not check_password_hash(user["password"], password):
                    error = "Incorrect username or password."

            if error is None:
                flask_session.clear()
                flask_session["user_id"] = user["id"]
                flash("Registration successful")
                return redirect(url_for("index"))

            flash(error)

        return self.render_template(context={})

    def logout(self):
        flask_session.clear()
        return redirect(url_for("index"))

app.add_url_rule('/users/login', view_func=Users.as_view('users'))
