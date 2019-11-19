# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
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
