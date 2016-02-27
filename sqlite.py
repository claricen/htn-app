#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module that contains functions for sqlite and flask interactions
"""

from flask import Flask
from flask import g

import sqlite3

DATABASE = 'database.db'

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())