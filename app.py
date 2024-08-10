from flask import Flask, render_template, flash, session, request, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
from flask_login import LoginManager, login_manager
import yaml 
import os

app = Flask(__name__)
Bootstrap(app)
CKEditor(app)

#Configure DB
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/play/')
def play():
    deckChoice = None
    deck1 = "Harry Potter"
    deck2 = "Roald Dahl"
    deck3 = "Sports Cars"
    return render_template("play.html", deckChoice=deckChoice, deck1=deck1, deck2=deck2, deck3=deck3)

@app.route('/learn/')
def learn():
    return render_template("learn.html")

@app.route('/trumpopedia/', methods=['GET','POST'])
def trumpopedia():
    return render_template("trumpopedia.html")

@app.route('/register/')
def register():
    return render_template()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/logout/')
def logout():
    return render_template()

# invoke /call the main class
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3500)
