class BaseConfig(object):
    SECRET_KEY = 'z2v(bgmv3nsbd3fc7tb+up_4)xsey4ka=%$fp4kpaz&=(4b0@h'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_test.sqlite3'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
