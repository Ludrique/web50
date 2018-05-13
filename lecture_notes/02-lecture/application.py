import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    is_new_year = now.month == 5 and now.day == 12 
    return render_template(
        "index.html", 
        is_new_year=is_new_year
    )
