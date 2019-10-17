# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

with open ("config_sw1.txt") as config, open ("config_sw1_cleared.txt", "w") as dest:
	for line in config:
		if not (line.startswith(ignore[2]) or line.startswith(ignore[1]) or line.startswith(" "+ignore[0])):
				print (line.strip())
				dest.write(line)

