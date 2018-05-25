# Routes
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy import or_

from app import app, db
from app.forms import LoginForm, RegistrationForm, BookSearchForm
from app.models import Book, Review, User

@app.route("/")
@app.route("/index")
@login_required
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    handle_authenicated()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    handle_authenicated()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("book_search"))
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/book_search", methods=["GET", "POST"])
@login_required
def book_search():
    form = BookSearchForm()
    if form.validate_on_submit():
        item = form.search_query.data
        books = search_books_for(item)
        if books:
            return render_template("book_search.html", form=form, books=books)
    return render_template("book_search.html", form=form)

@app.route("/book/<isbn>", methods=["GET"])
@login_required
def book_page(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    book_reviews = Review.query.filter_by(book_id=book.id)
    return render_template("book_page.html", book=book, book_reviews=book_reviews)


# Helpers
def handle_authenicated():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

def search_books_for(item):
    return Book.query.filter(or_(
        Book.isbn.contains(item),
        Book.author.contains(item),
        Book.pub_year.contains(item),
        Book.title.contains(item)
        )
    ).all()
