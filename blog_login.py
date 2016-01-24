# flask-blog Controller

# imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'g\x8b\xcd\xed\xb4\x1f\xa9\x83\xa3G\x08!\xdc\xd7\xfe\x88\xbf\x93J\xf9\xec\xc0\xfe'

app = Flask(__name__)

app.config.from_object(__name__) # looks for uppercase variables (?)

# function to connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid credentials. Please try again.'
			flash('Invalid credentials. Please try again.')
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html') # connect to login page

@app.route('/main')
def main():
	return render_template('main.html') # connect to main page

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out!')
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)



