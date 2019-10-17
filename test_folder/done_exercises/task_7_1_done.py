# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
my_template = '''
Protocol:			{protocol}
Prefix:				{prefix}
AD/Metric:			{ad_metric}
Next-Hop:			{next_hop}
Last update:			{last_update}
Outbound Interface:		{outb_interface}

'''

with open("ospf.txt") as config:
	for line in config:
		new_info = list(line.replace("[","").replace("]",'').replace("via",'').split())
		print(my_template.format(protocol="OSPF",prefix=new_info[1],ad_metric=new_info[2],next_hop=new_info[3],last_update=new_info[4],outb_interface=new_info[5]))



