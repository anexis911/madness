# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']



with open ("config_sw1.txt") as config:
	for line in config:
		if not line.startswith("!"):
			if not (line.startswith(ignore[2]) or line.startswith(ignore[1]) or line.startswith(" "+ignore[0])):
				print (line.strip())
			
				
		
			

