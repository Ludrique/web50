import os

from flask import Flask, session, render_template
from flask_login import LoginManager
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from secrets import DATABASE_URL

app = Flask(__name__)

# Check for environment variable
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

# Configure Login
login = LoginManager(app)

@app.route("/")
def index():
    user = {"username": "World"}
    return render_template("index.html", title="Home", user=user)

