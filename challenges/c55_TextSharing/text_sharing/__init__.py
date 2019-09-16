import os

from flask import Flask


def create_app(testing=False):
    """
    This file will contain the application factory
    The application factory sets any configuration, registration, and
    other setup the application needs. Then, the application is returned.
    """
    # create and configure the app
    # The app needs to know where it's located to set up some paths
    # Using __name__ is a convenient way to tell it that
    # We also tell the app that the instance folder is located outside
    # the package. This folder will hold data that shouldn't be committed
    # to version control (secrets, database file, etc)
    app = Flask(
        __name__,
        instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'),
        instance_relative_config=True)

    if testing:
        app.config.from_object(testing)
    else:
        app.config.from_object("instance.config.DevelopmentConfig")

    # ensure the instance folder exists - Flask doesn't create automatically so
    # you need to tell it to be created
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # Register the database with the application
    from . import psql_db
    psql_db.init_app(app)

    # Register the `auth` blueprint with the app
    from . import users
    app.register_blueprint(users.bp)

    # Register the `snippet` blueprint with the app
    # The endpoint for the index view defined below will
    # be blog.index. Some of the authentication views
    # referred to a plain index endpoint. app.add_url_rule()
    # associates the endpoint name 'index' with the / url
    # so that url_for('index') or url_for('blog.index')
    # will both work, generating the same / URL either way.
    from . import snippets
    app.register_blueprint(snippets.bp)
    app.add_url_rule("/", endpoint="index")

    return app
