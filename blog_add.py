# flask-blog Controller

# imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3
from functools import wraps

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

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first!')
			return redirect(url_for('login'))
	return wrap

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
@login_required # added "decorator" to main function
def main():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('main.html', posts=posts) # connect to main page

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out!')
	return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
@login_required
def add():
	title = request.form['title']
	post = request.form['post']
	if not title or not post:
		flash("All fields are required! Please try again...")
		return(redirect(url_for('main')))
	else:
		g.db = connect_db()
		g.db.execute('insert into posts (title, post) values (?,?)', \
			[request.form['title'], request.form['post']])
		g.db.commit()
		g.db.close()
		flash('New entry successfully posted!')
		return(redirect(url_for('main')))

if __name__ == '__main__':
	app.run(debug=True)



