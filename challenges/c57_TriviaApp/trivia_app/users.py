"""Defines the routes for handling user registration / authentication"""
import functools
from . import db
from .models import User
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from flask import g as flask_g
from werkzeug.security import check_password_hash, generate_password_hash
from flask.views import View

# A blueprint is an object that allows defining application functions without
# requiring an application object ahead of time. Will register to the app later
bp = Blueprint(name='users', import_name=__name__, url_prefix="/users")

class BaseUserView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserLoginView(BaseUserView):
    methods = ["GET", "POST"]

    def register(self):
        if request.method == "POST":
            username = request.form.get("username", None)
            email = request.form.get("email", None)
            password = request.form.get("password", None)

            error = None
            if not username:
                error = "Username is required."
            elif not password:
                error = "Password is required."
            elif User.query.filter_by(username=username).first() is not None:
                error = f"User {username} is already registered."

            if error is None:
                hashed_pw = generate_password_hash(password)
                new_user = User(username=username, email=email, password=hashed_pw)
                db.session.add(new_user)
                db.session.commit()
                flash("Registration successful")
                return redirect(url_for("users.login"))

            flash(error)

        return self.render_template(context={})

    def login(self):
        # TODO
        pass

    def logout(self):
        # TODO
        pass
