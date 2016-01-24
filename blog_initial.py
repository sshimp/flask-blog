# flask-blog Controller

# imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

app.config.from_object(__name__) # looks for uppercase variables (?)

# function to connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
	return render_template('login.html') # connect to login page

@app.route('/main')
def main():
	return render_template('main.html') # connect to main page

if __name__ == '__main__':
	app.run(debug=True)



