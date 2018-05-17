from flask import render_template, redirect
from flask_login import current_user, login_user
from user import User
import application
from forms import LoginForm

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    check_if_authenticated()
    attempt_login()
    return render_template("login.html", title="Sign In", form=form)

# Helpers
def check_if_authenticated():
    if current_user.is_authenticated:
        return redirect(url_for("/"))

def attempt_login():
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data)
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("/"))
    




