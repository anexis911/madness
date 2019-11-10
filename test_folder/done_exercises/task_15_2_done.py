# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re
from pprint import pprint

def sh_ip_int_br (configtxt):
	
	with open (configtxt) as f:
		result=[]
		regex = r'(?P<intf>\S+) +(?P<ip>\d+.\d+.\d+.\d+|unassigned) +\S+ \S+ +(?P<status>\S+ \S+|\S+) +(?P<protocol>\S+)'
		for line in f:
			match = re.search(regex, line)
			
			if match:
				
				intf,ip,status, protocol = match.groups()
				result.append(match.groups())
					
		
	#print(result)		
	return result


if __name__ == "__main__":
	result =sh_ip_int_br("sh_ip_int_br.txt")
	pprint(result)

	

