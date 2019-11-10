# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
import re
from pprint import pprint
import glob
import yaml
from graphviz import Digraph



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
			
	
	#pprint(final_result)	 
	return final_result




def generate_topology_from_cdp (list_of_files, save_to_filename=None):
	result = []
	for ffile in list_of_files:
		result.append(parse_sh_cdp_neighbors(ffile))
		
	with open (save_to_filename , "w") as f:
		yaml.dump(result, f)
		


def transform_topology (yaml_file):
	with open(yaml_file) as f:
		data = yaml.safe_load(f)
		dot = Digraph(comment="Network Map")
		for line in data:
			dot.node(line)
			
		"""
		dot.node('A', 'King Arthur')
		dot.node('B', 'Sir Bedevere the Wise')
		dot.node('L', 'Sir Lancelot the Brave')

		dot.edges(['AB', 'AL'])
		dot.edge('B', 'L', constraint='false')
		"""
		dot.render("test.gv", view = True)
		

if __name__ == "__main__":
	transform_topology("topology.yaml")
	
