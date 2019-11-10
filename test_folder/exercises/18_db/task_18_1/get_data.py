# -*- coding: utf-8 -*-

import sqlite3
import sys



my_in_arg = sys.argv
conn = sqlite3.connect('dhcp_snooping.db')


try:
	if my_in_arg[1]:
		try:
			if my_in_arg[2]:
				print("Information about devices with parameters:", my_in_arg[1], my_in_arg[2])
				result_str = 'select * from dhcp WHERE '+my_in_arg[1]+' GLOB "*'+my_in_arg[2]+'*"'
				for row in conn.execute(result_str):
					print(row)
			
		except sqlite3.OperationalError:
			print("This parameter is not supported. Supported parameters: mac, ip, vlan, intf,switch")
		except IndexError:
			print("Input needs 0 or 2 arguments")
except:
	print("Lines in dhcp table: ")	
	for row in conn.execute('select *from dhcp'):
		print(row)
		

