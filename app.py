# !/usr/bin/env/python


from crypt import methods
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash
from models import db, Book, app, Flask


#create instance of Flask


#create routes(visible parts of the site- urls)

@app.route('/')#decorator
def index():
    """creates the homepage for the app"""
    books=Book.query.all()
    total_books=len(books)
    
    return render_template('index.html', books=books, total_books=total_books)

@app.route('/book/<id>')
def book(id):
    """Creates the view for the app"""
    book=Book.query.get_or_404(id)
    book_length=Book.query.all()
    
    
    return render_template('book.html', book=book, book_length=book_length)


@app.route('/addbook', methods=['GET', 'POST'])
def add_book():
    """Creates the route to create new books on the app and adds it to the database"""
    
    if request.form:
        new_book = Book(book_name=request.form['book_name'],
                        isbn=request.form['ISBN'],
                        date_published=request.form['date_pusblished'],
                        genre=request.form['genre'],
                        date_sold=request.form['date_sold'],
                        number_of_pages=request.form['number_of_pages'],
                        language=request.form['language'],
                        description=request.form['description'],
                        )
        db.session.add(new_book)
        db.session.commit()
       
        
        return redirect(url_for('index'))
    return render_template('addbook.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_book(id):
    """Edits the book information both in the app and database"""
    book=Book.query.get(id)
    
    if request.form:
        book.book_name=request.form['book_name']
        book.isbn = request.form['ISBN']
        book.date_published = request.form['date_pusblished']
        book.genre = request.form['genre']
        book.date_sold = request.form['date_sold']
        book.number_of_pages = request.form['number_of_pages']
        book.language = request.form['language']
        book.description = request.form['description']
        
        db.session.commit()
        
        flash('The book was successfully edited to the database')
        return redirect(url_for('index'))
    
    return render_template('edit-book.html')



@app.route('/delete/<id>')
def delete_book(id):
    """deletes books from the database and from the  app """
    book=Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors-non existant pages"""
    return render_template('404.html', msg=error),404






if __name__ =='__main__':#if it were to be exported to a diffent filem then the --main .- would be the name of the file it is exported to
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')#making the app run, you just need to run the app.py file on the terminal


    