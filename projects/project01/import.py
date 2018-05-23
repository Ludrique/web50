'''
Imports books.csv into the application database.
'''
# CSV row strucutre: [ISBN, Author, Title, Year]
# USE BATCH ADD/COMMITS NEXT TIME!!

from app import db 
from app.models import Book 

import csv

with open("./data/books.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        isbn, author, title, pub_year = row 
        book = Book(isbn=isbn, author=author, title=title, pub_year=pub_year)
        db.session.add(book)
        db.session.commit()
        print(f'{isbn} commited')
