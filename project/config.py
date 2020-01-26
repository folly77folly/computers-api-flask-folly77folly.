import os

# for development
class Development:
    SECRET_KEY = os.urandom(16)
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_NAME = 'session'

# for development
class Production:
    SECRET_KEY = os.urandom(16)
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_NAME = 'session'

class Database:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pass@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False