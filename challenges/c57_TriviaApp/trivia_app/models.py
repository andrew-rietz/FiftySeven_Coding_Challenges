"""Defines the database for the app"""

from . import db
from sqlalchemy.dialects.postgresql import JSON
from flask import current_app, g
from flask.cli import with_appcontext
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Serial, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Serial, primary_key=True)
    author_id = db.Column(db.Serial, db.ForeignKey("users.id"), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited = db.Column(db.DateTime, nullable=True)
    prompt = db.Column(db.Text, nullable=False)
    distractors = db.Column(db.JSON, nullable=False)
