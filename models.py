from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///books.db'
db= SQLAlchemy(app)

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    created= db.Column('Created', db.DateTime,default=datetime.datetime)
    book_name=db.Column('Name of the book',db.String())
    date_published = db.Column('Date Published',db.String())
    genre = db.Column('Genre',db.String())
    date_sold = db.Column('Genre',db.String())
    number_of_pages = db.Column('Number of Pages',db.Integer)
    date_sold = db.Column('Date Sold',db.String())
    language = db.Column('Language',db.String())
    description = db.Column('Description',db.Text)

#finish creating the fields here, before setting the site again
    def __repr__(self):
        return f'''<Book(Name:{self.book_name}
                Created:{self.created}
                '''


