# -*- coding: utf-8 -*-

import sqlite3
import os

db_filename = 'dhcp_snooping.db'
db_exists = os.path.exists(db_filename)



def connect_to_db (file_db):
	conn = sqlite3.connect(file_db)
	return conn



conn = connect_to_db('dhcp_snooping.db')
if not db_exists:
	print('Создаю базу данных...')
	with open ('dhcp_snooping_schema.sql', 'r') as f:
		schema = f.read()
	conn.executescript(schema)
	print('Готово')
else:
	print("База уже существует")
	
