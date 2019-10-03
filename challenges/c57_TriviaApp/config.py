"""Flask config file"""
import os

class BaseConfig(object):
    """Base config class"""
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL')
    ENDPOINT = os.environ.get("ENDPOINT")
    POST_QUERY = os.environ.get("POST_QUERY")

class DevelopmentConfig(BaseConfig):
    """Settings for our development config"""
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(BaseConfig):
    """Settings for our development config"""
    TESTING = True
