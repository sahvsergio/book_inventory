# !/usr/bin/env/python


from crypt import methods
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from models import db, Book, app

#create instance of Flask


#create routes(visible parts of the site- urls)

@app.route('/')#decorator
def index():
    return render_template('index.html')

@app.route('/addbook',methods=['GET','POST'])
def add_book():
    print(request.form)
    return render_template('addbook.html')



if __name__ =='__main__':#if it were to be exported to a diffent filem then the --main .- would be the name of the file it is exported to
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')#making the app run, you just need to run the app.py file on the terminal

    