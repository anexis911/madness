# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
import textfsm
from tabulate import tabulate
from pprint import pprint



def parse_command_output (template, command_output):
	with open (template) as template, open (command_output) as output:
		result = {}
		n=1
		re_table = textfsm.TextFSM(template)
		header = re_table.header
		results = re_table.ParseText(output.read())
		for res in results:
			result[n] =dict(zip(header, res))
			n+=1
		return(result)



if __name__ == "__main__":
	pprint(parse_command_output('templates/sh_ip_int_br.template', 'output/sh_ip_int_br.txt'))
