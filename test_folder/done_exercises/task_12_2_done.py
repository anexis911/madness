# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
from ipaddress import ip_address
def making_ips_list_from_line(line):
	result_ip_list =[]
	try:
		
		result_ip_list.append(ip_address(line))
	except ValueError:
		line = line.split(".")
		if "-" in str(line[-1]):
			last_host_list = list(range(int(line[-1].split("-")[0]),int(line[-1].split("-")[-1])+1))
			for ip_range in last_host_list:
				result_line = line[0:3]
				result_line.append(ip_range)
				itogo= ("".join(str(result_line)).replace(",",".").replace("'","").replace("[","").replace("]","").replace(" ",""))
				
				result_ip_list.append(ip_address(itogo))
				
		if "-" in str(line[-4]):
			fth_ip_oct = line[3].split('-')[0]
			sec_ip_oct = line[-1]
			last_host_list = list(range(int(fth_ip_oct), int(sec_ip_oct)+1))
			for ip_range in last_host_list:
				result_line = line[0:3]
				result_line.append(ip_range)
				itogo= ("".join(str(result_line)).replace(",",".").replace("'","").replace("[","").replace("]","").replace(" ",""))
				
				result_ip_list.append(ip_address(itogo))
			
			
	#print(result_ip_list)
	

def convert_ranges_to_ip_list (ip_list):
	
	for ip_mean in ip_list:
		making_ips_list_from_line(ip_mean)
		
		



ip_listt= ['8.8.4.4', '1.1.1.1-12', '172.21.41.128-172.21.41.132']
convert_ranges_to_ip_list(ip_listt)
