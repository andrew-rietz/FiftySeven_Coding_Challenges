from flask import Flask
from flask import g as flask_g
from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
from flask_migrate import Migrate
from flask_redis import FlaskRedis


# Set globals
db = SQLAlchemy()
migrate = Migrate()
# redis_store = FlaskRedis()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    with app.app_context():
        # Set global values
        # redis_store.endpoint = app.config['ENDPOINT']
        # redis_store.post_query = app.config['POST_QUERY']

        # Initialize globals
        # redis_store.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)

        # Register Blueprints
        from . import users
        app.register_blueprint(users.users_bp)
        # app.register_blueprint(admin.admin_bp)

        return app
