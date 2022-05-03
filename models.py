from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///books.db'
db= SQLAlchemy(app)

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)#primary key
    created= db.Column('Created',db.DateTime, default = datetime.datetime.now)#timestamp when the item was created
    book_name=db.Column('Name of the book',db.String())
    date_published = db.Column('date_published', db.String())
    genre = db.Column('Genre',db.String())
    date_sold = db.Column('Genre',db.String())
    number_of_pages = db.Column('Number of Pages',db.String())
    date_sold = db.Column('Date Sold',db.String())
    language = db.Column('Language',db.String())
    description = db.Column('Description',db.Text)
    isbn=db.Column('ISBN', db.String())
    


#finish creating the fields here, before setting the site again
    def __repr__(self):
        return f'''
            Book Name:{self.book_name}
            Created:{self.created}
            Date Published :{self.date_published}
            Genre:{self.genre}
            Date Sold:{self.date_sold}
            Language: {self.language}
            Description: {self.description}
            Number of pages:{self.date_sold}
                
                )
                '''

