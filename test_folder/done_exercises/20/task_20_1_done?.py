# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import netmiko
import logging

ip = ['192.168.100.2', '8.8.8.8', '17.22.121.11']



def ping_one_ip(ip):
	result = subprocess.run('ping {} -c 3 -n'.format(ip), shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
	if result.returncode ==0:
		return True
	else:
		return False
		
		
def ping_ip_addresses (ip_list, limit=3):
	reachable_ip=[]
	unreachable_ip=[]
	for one_ip in ip_list:
		with ThreadPoolExecutor(max_workers=limit) as executor:
			result = executor.submit(ping_one_ip, one_ip)
			for f in as_completed([result]):
				if f.result() == True:
					reachable_ip.append(one_ip)
				else:
					unreachable_ip.append(one_ip)
	return (reachable_ip+unreachable_ip)
			

			
if __name__ == "__main__":
	pprint(ping_ip_addresses(ip))
	
