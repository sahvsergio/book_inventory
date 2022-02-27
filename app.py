

# #import flask
from flask import Flask,render_template
from flask import url_for
#create instance of Flask
app= Flask(__name__)

#create routes(visible parts of the site- urls)

@app.route('/')#decorator
def index():
    return render_template('index.html')

@app.route('/addbook')
def add_book():
    return render_template('addbook.html')



if __name__ =='__main__':#if it were to be exported to a diffent filem then the --main .- would be the name of the file it is exported to
    app.run(debug=True, port=8000, host='127.0.0.1')#making the app run, you just need to run the app.py file on the terminal
