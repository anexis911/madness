# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import re
from pprint import pprint
import glob
import yaml



sh_cdp_files = glob.glob('sh_cdp_n*')
#print(sh_cdp_files)

def parse_sh_cdp_neighbors (in_file):
	with open (in_file) as f:
		final_result = {}
		result={}
		for line in f:
			line = line.strip()
			
			match_1 = re.search(r'(\S+)>', line)
			in_comm_match = re.search(r'(\S+)>', line)
			match_2 = re.search(r'(\S+) +(\S+ \d/\d) +\S+ .+(\S\S\S+ \d/\d)', line)
			if in_comm_match:
				intff = in_comm_match.group(1)
			elif match_1:
				r_int = match_1.group(1)
			elif match_2:
				dev_id, loc_intf, port_id = match_2.groups()
				r_dict={}
				r_dict[loc_intf] = port_id
				result[dev_id] = r_dict
				final_result[intff] = result
			
	
	pprint(final_result)	 
	return final_result

#parse_sh_cdp_neighbors("sh_cdp_n_r2.txt")


def generate_topology_from_cdp (list_of_files, save_to_filename=None):
	result = []
	for ffile in list_of_files:
		result.append(parse_sh_cdp_neighbors(ffile))
		
	with open (save_to_filename , "w") as f:
		yaml.dump(result, f)
		

if __name__ == "__main__":
	generate_topology_from_cdp(sh_cdp_files, "topology.yaml")
	

