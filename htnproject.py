#!/usr/bin/python

"""
    A simple application that uses sqlite3 and flaskr to show user info.
    Based on the Flaskr example from the Flask site.
"""

import os
import sqlite3
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from contextlib import closing

#configuration
DATABASE = '/database/htn.db'
DEBUG = True
SECRET_KEY='development key',
USERNAME='admin',
PASSWORD='default'

# creating application
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'htn.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    print "Opened database successfully"
    return rv

def init_db():
    """Initializes the database."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_index():
    db = get_db()
    return "Hi, this is my backend dev application for Hack the North 2016 :)"

@app.route('/users', methods=['GET'])
def show_all_users():
    cur = g.db.execute('SELECT * FROM Person')
    entries = cur.fetchall()
    print str(entries).strip('[]')
    return str(entries).strip('[]')

@app.route('/skills', methods=['GET'])
def show_all_skills():
    cur = g.db.execute('SELECT * FROM skills')
    entries = cur.fetchall()
    print str(entries).strip('[]')
    return str(entries).strip('[]')

def add_users(file):
    with open(file, "r") as f:
        data = json.load(f)
        parse_data(data)

def parse_data(data):
    """
    Args:
        data: a dictionary from json.load of user data
    """
    
    userdata = None
    primary_key = 0 ##change this later?

    for user in data[:3]:
        name = user["name"]
        email = user["email"]
        company = user["company"]
        latitude = user["latitude"]
        longitude = user["longitude"]
        phone = user["phone"]
        picture = user["picture"]
        skills = user["skills"]

        db = get_db()
        db.execute("INSERT INTO Person (name, email, company, latitude, longitude, phone, picture) \
                     VALUES (?, ?, ?, ?, ?, ?, ?)", (name, email, company, latitude, longitude, phone, picture))
        for skill in skills:
            pk = db.execute("SELECT id FROM Person WHERE email = '%s'" % email).fetchone()
            db.execute("INSERT INTO Skills (name, rating, person) VALUES (?, ?, ?)", (skill["name"], skill["rating"], pk[0]))

        db.commit()

        


# @app.route('/user/', methods=['GET', 'PUT'])
# def show_user():
#     cur = db.execute('select title, text from entries order by id desc')
#     entries = cur.fetchall()
#     return render_template('show_entries.html', entries=entries)


# @app.cli.command('initdb')
# def initdb_command():
#     """Creates the database tables."""
#     init_db()
#     print('Initialized the database.')





# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()


# @app.route('/add', methods=['POST'])
# def add_entry():
#     if not session.get('logged_in'):
#         abort(401)
#     db = get_db()
#     db.execute('insert into entries (title, text) values (?, ?)',
#                [request.form['title'], request.form['text']])
#     db.commit()
#     flash('New entry was successfully posted')
#     return redirect(url_for('show_entries'))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif request.form['password'] != app.config['PASSWORD']:
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('show_entries'))
#     return render_template('login.html', error=error)


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('show_entries'))

if __name__ == '__main__':
    init_db()
    with app.app_context():
        add_users('uploader/users.json')
    app.run()