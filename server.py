"""
This is a Flask server that will help to do testing on 9.01X course
materials. 
"""

import sqlite3 
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# create application 
app = Flask(__name__)

#Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE = './survey.db',
	DEBUG = False,
	# add this later in a config file: SECRET_KEY = 'development key'
	# add this later in a config file: USERNAME = 'admin'
	# add this later in a config file: PASSWORD = 'default'
))

def connect_db():
	"""Connects to a specific database, specified in parens"""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Roq
	return rv


def init_db(): 
	"""Creates tables within the database"""
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f: 
			db.cursor().execturescript(f.read())
		db.commit()

def get_db(): 
	"""Opens a new database connection if there isn't one yet"""

	if not hasattr(g,'sqlite'): 
		g.sqlite_db = connect_db()
	return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
	"""Closes the db at the end of the connection""" 
	if hasattr(g, 'sqlite_db'): 
		g.sqlite_db.close()

@app.route('/')
def home():
	print "I'm here!!"
	return render_template('home.html')

@app.route('/add', methods=['POST'])
def add_entry():
    pass


if __name__ == '__main__':
    #init_db()
    app.run()


