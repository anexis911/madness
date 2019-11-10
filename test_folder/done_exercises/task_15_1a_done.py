# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
from pprint import pprint

def get_ip_from_cfg (configtxt):
	
	with open (configtxt) as f:
		result={}
		
		for line in f:
			if line.startswith("interface"):
				intf = line.split()[-1]
				
			
			if line.startswith(" ip address"):
				match = re.search(r' ip address (?P<ipadr>\S+) +(?P<mask>\S+)',line)
				if match:
					ipadr, mask = match.groups()
					result[intf]={}
					result[intf]["ipadr"] = ipadr
					result[intf]["mask"] = mask
		
	#print(result)		
	return result
	

if __name__ == "__main__":
	result =get_ip_from_cfg("config_r1.txt")
	pprint(result)

	

