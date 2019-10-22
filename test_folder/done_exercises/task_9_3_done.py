# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

acces_result = {}
trunk_result = {}
def get_int_vlan_map (input_file):
	with open (input_file) as f:
		
		for line in f:
			if "FastEthernet" in line:
				intf = line.split()[1]
				
			if "access" in line:
				new_ac_line = line.split()
				
				for word_l in new_ac_line:
					if word_l[-1].isdigit():
						acces_result[intf]=word_l
			if "trunk" in line:
				new_tr_line = line.split()
				
				for word_l in new_tr_line:
					if word_l[-1].isdigit():
						trunk_result[intf] = word_l
					
				
				
		
		print(acces_result, trunk_result)
				
get_int_vlan_map("config_sw1.txt")
