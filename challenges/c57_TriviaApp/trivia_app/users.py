"""Defines the routes for handling user registration / authentication"""
from .models import User


@app.route("/users")
def hello():
    return "Hello, Users"
