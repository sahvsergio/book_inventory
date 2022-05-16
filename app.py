# !/usr/bin/env/python


from crypt import methods
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from models import db, Book, app, Flask


#create instance of Flask


#create routes(visible parts of the site- urls)

@app.route('/')#decorator
def index():
    books=Book.query.all()
    return render_template('index.html', books=books)

@app.route('/book/<id>')
def book(id):
    book=Book.query.get_or_404(id)
    return render_template('book.html', book=book) #book=book.id


@app.route('/addbook', methods=['GET', 'POST'])
def add_book():
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
        return redirect(url_for('index'))
    
    return render_template('edit-book.html',book=book)



@app.route('/delete/<id>')
def delete_book(id):
    book=Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error),404




if __name__ =='__main__':#if it were to be exported to a diffent filem then the --main .- would be the name of the file it is exported to
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')#making the app run, you just need to run the app.py file on the terminal


    