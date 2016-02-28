#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import json

import sqlite3
from contextlib import closing

#from htnproject import connect_db, init_db, get_db, before_request, teardown_request

class UserUploader(object):
	""" 
	Takes a json file of specified user info and puts it into a class for uploading to database
	"""

	def __init__(self, filename):
		"""Initializes class
		"""

		self.filename = filename

	def upload(self):
		with open(self.filename, "r") as f:
			data = json.load(f)
			self.parse_data(data)

	def parse_data(self, data):
		"""
		Args:
			data: a dictionary from json.load of user data
		"""
		userdata = None
		primary_key = 0 ##change this later?

		for user in data[:3]:
			print user, ('\n')
			#return user ## dictionary with data

	def get_pk(self):
		"""
		The primary key is an integer identifying a certain user. Returns the number of users in the database.
		"""
		pass

				

	def create_user(self, userdata):
		"""
		Creates a user object to export the data to the database.
		"""
		pass

		# Checks to see if user already exists (based on email) before uploading
		if self.check_User(userdata.email):
			print "The individual %s already exists in the database." % userdata.email
		else:
			kwargs = userdata.build_kwargs()
			#User(g, **kwargs).upload() ## Not final function name
			# Function here to upload to the database

	def check_User(self, email):
		"""
		Checks to see if the user is stored in the database already
		"""
		print email
		return False ## Just return this until database is set up


class UserData(object):
	"""
	A container class used to store user information before uploading to the database
	"""

	def __init__(self, name, email, latitude, longitude):
		"""
		Initializes the class. Dictionary used for storing keyword arguments.

		Args:
			name (str): name of the user
			email (str): user's email (unique)
			latitude (int)
			longitude (int)
		"""
		self.name = name
		self.email = email
		self.latitude = latitude
		self.longitude = longitude

		def add_key(self, k, v):
			"""
			Adds a new key-value pair of user data to the class.
			"""
			self.dict[k] = v

		def build_kwargs(self):
			"""
			Converts data stored in the dictionary to be used as a kwargs argument for user class.

			Returns: the kwargs dict
			"""
			## not sure if this function is necessary since I originally used a dict...
			return self.dict


if __name__ == "__main__":
	UserUploader("users.json").upload()
