# -*- coding: utf-8 -*-

import sqlite3
import yaml
import glob
import sys
import re

query = 'INSERT into switches values (?, ?)'
query2 = 'INSERT into dhcp values (?, ?, ?, ?, ?)'
conn = sqlite3.connect('dhcp_snooping.db')
sh_version_files = glob.glob('*_dhcp_snooping*')





def yaml_file_dict(in_file):
	with open(in_file) as f:
		data = yaml.safe_load(f)
		nd = data.values()
		for l in nd:
			res = list(zip(l.keys(), l.values()))
		
		return res
		
		

def parse_txt_file(in_file):
	result = []
	switch_numb = str(in_file)[0:3]
	with open (in_file) as f:
		for line in f:
			my_match = re.search(r'(?P<mac>\S+) +(?P<ip>\d+.\d+.\d+.\d+) +\S+ +\S+ +(?P<vlan>\S+) +(?P<intf>\S+)', line)
			if my_match:
				result_list=[]
				mac, ip, vlan, intf = my_match.group("mac", "ip", "vlan", "intf")
				result_list.append(mac), result_list.append(ip), result_list.append(vlan)
				result_list.append(intf), result_list.append(switch_numb)
				result.append(result_list)
		
	return result

try:
	
	my_except = []
	my_data = yaml_file_dict('switches.yml')
	print("Добавляю данные в таблицу switches...")
	for row in my_data:
		my_except.append(row)
		conn.execute(query, row)
		
		
	conn.commit()
	for row in conn.execute('select * from switches'): #optional
		print ("Добавлено :", row)
	
except sqlite3.OperationalError :
	print('База данных не существует. Перед добавлением данных, ее надо создать')
except sqlite3.IntegrityError as err2 :
	print('При добавлении данных: ', my_except, 'Возникла ошибка: ', err2)
	

try:
	print("Добавляю данные в таблицу dhcp...")
	for ffile in sh_version_files:
		my_except = []
		txt_data_list = parse_txt_file(ffile)
		for sm_list in txt_data_list:
			my_except.append(sm_list)
			conn.execute(query2, sm_list)
			conn.commit()
			#for row in conn.execute('select * from dhcp'):
				#print ("Добавлено :", txt_data_list)
		

except sqlite3.OperationalError :
	print('База данных не существует. Перед добавлением данных, ее надо создать')
except sqlite3.IntegrityError as err2 :
	print('При добавлении данных: ', my_except, 'Возникла ошибка: ', err2)
	
conn.close()
	


