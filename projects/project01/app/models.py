from app import db
from app import login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship("Review", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"  


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(128))
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    pub_year = db.Column(db.String(64))
    reviews = db.relationship("Review", backref="book", lazy="dynamic")

'''
    def __repr__(self):
        return f"<Book {self.title}>"
'''


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String) 
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __repr__(self):
        return f"<Review {self.body}>"
