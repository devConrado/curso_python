#!/usr/bon/python3

from pymongo import MongoClient

try:
	con = MongoClient()
	db = con['projeto']
	print('Conectado!')
except Exception as e:
	print(e)
