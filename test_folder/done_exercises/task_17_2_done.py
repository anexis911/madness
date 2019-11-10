# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint
#import glob
import csv


def parse_sh_cdp_neighbors (in_command):
	with open ("sh_cdp_n_sw1.txt") as f:
		in_comm_match = re.search(r'(\S+)>', in_command)
		intff = in_comm_match.group(1)
		final_result = {}
		result={}
		for line in f:
			line = line.strip()
			match_1 = re.search(r'(\S+)>', line)
			match_2 = re.search(r'(\S+) +(\S+ \d/\d) +\S+ .+(\S\S\S+ \d/\d)', line)
			if match_1:
				r_int = match_1.group(1)
			elif match_2:
				dev_id, loc_intf, port_id = match_2.groups()
				r_dict={}
				r_dict[loc_intf] = port_id
				result[dev_id] = r_dict
		final_result[intff] = result	
	
	pprint(final_result)	 
	return result




if __name__ == "__main__":
	with open ("sh_cdp_n_sw1.txt") as f:
		comm_line = next(f)
		comm_line_1 = next(f)
		parse_sh_cdp_neighbors(comm_line_1)
	

