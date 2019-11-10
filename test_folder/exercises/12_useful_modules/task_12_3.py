# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
from tabulate import tabulate

reach_ip = ["10.1.1.1", "10.1.1.2"]
unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
#print(tabulate(reach_ip))


def print_ip_table (re_tabl, unr_tabl):
	result_tabl={}
	result_tabl["Reachable"]=reach_ip
	result_tabl["Unreachable"]=unreach_ip
	
	print(tabulate(result_tabl, headers = "keys"))
	
print_ip_table(reach_ip, unreach_ip)
