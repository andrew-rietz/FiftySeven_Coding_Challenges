from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

# Globally accessible libraries
db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    # Initialize Plugins
    db.init_app(app)
    migrate = Migrate(app, db)

    # @app.route("/hello")
    # def hello():
    #     return "Hello, Trivia World!"

    with app.app_context():
        # Imports


        # Create tables for our models
        db.create_all()

        # Include our Routes


        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        return app
