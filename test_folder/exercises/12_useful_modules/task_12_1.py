# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
my_ip_list = ["172.48.131.33", "44.123.22.12", "8.8.8.8"]


def ping_ips(ip):
	
	result = subprocess.run("ping {} -c2 -n".format(ip), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	if result.returncode ==0:
		return True
	else:
		return False
	
def allowed_ip_adr(ip_list):
	allowed_ips = []
	not_allowed_ips=[]
	for ip in ip_list:
		print("pinging",ip)
		if ping_ips(ip) == True:
			allowed_ips.append(ip)
		else:
			not_allowed_ips.append(ip)
	#return (allowed_ips, not_allowed_ips)
	print("allowed IPs: " +str(allowed_ips), "Not Allowed IP's :"+str(not_allowed_ips))
	
allowed_ip_adr(my_ip_list)
