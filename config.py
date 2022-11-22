import os

from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_TPL = '%s://%s:%s@%s:%s/%s'


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_TPL % (config('DB_TYPE'), config(
        'DB_USER'), config('DB_PASSWORD'), config('DB_HOST'), config('DB_PORT'), config('DB_NAME'))
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    DEBUG = False


class Staging(Config):
    DEVELOPMENT = True
    DEBUG = True


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True


class Testing(Config):
    TESTING = True


config = {
    'development': Development,
    'testing': Testing,
    'default': Development
}
