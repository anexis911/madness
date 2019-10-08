# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
new_set_command1= set(command1.split()[-1].replace(",", ""))
new_set_command2= set(command2.split()[-1].replace(",", ""))
resultset = list(new_set_command1.intersection(new_set_command2))
print(sorted(resultset))

