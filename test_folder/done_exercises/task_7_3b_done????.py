# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


with open ("CAM_table.txt") as config:
	user_inp = input("Input your port: ")
	for line in config:	
		if ("Gi0/"+user_inp) in line:
			print(line.strip())
		
				
	
