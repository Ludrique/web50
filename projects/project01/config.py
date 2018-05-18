import os
import app.secrets as secrets
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Check for environment variable
    if not secrets.DATABASE_URL:
        raise RuntimeError("DATABASE_URL is not set")
    # Configure session to use filesystem
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SECRET_KEY = "you-will-never-guess"
    # Session(app)

    # Set up database
    # engine = create_engine(secrets.DATABASE_URL)
    # db = scoped_session(sessionmaker(bind=engine))
    SQLALCHEMY_DATABASE_URI = secrets.DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False