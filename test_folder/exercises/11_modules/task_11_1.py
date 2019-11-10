# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


import sys

command_output = sys.argv[1]





def parse_cdp_neighbors(command_output):
	result_dict={}
	
	with open ("sh_cdp_n_sw1.txt") as f:
		try:
			
			for line in f:
				
				if "Eth" in line:
					line = line.strip()
					my_list = line.split()
					
					result_dict[my_list[0]]=my_list[1:]
					#print(my_list)
				
				
				#if command_output in result_dict.keys():
					
			
			res_dictt = dict(zip(result_dict.keys(), result_dict.values()))
			print(res_dictt)
			
		except KeyError:
			print("1")	
		

parse_cdp_neighbors(command_output)

