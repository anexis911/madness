# -*- coding: utf-8 -*-
'''
Задание 22.2

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding и записать его в файл templates/sh_ip_dhcp_snooping.template

Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 22.1.
'''
import textfsm
from tabulate import tabulate



def parse_command_output (template, command_output):
	with open (template) as template, open (command_output) as output:
		re_table = textfsm.TextFSM(template)
		header = re_table.header
		result = re_table.ParseText(output.read())
		print(tabulate(result, headers = header))



if __name__ == "__main__":
	parse_command_output('templates/sh_ip_dhcp_snooping.template', 'output/sh_ip_dhcp_snooping.txt')
