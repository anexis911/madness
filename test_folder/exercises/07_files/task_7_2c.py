# -*- coding: utf-8 -*-
import sys
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
comm_list = sys.argv
ignore = ['duplex', 'alias', 'Current configuration']



with open (comm_list[1]) as config, open (comm_list[2], "w") as dest:
	for line in config:
		if not (line.startswith(ignore[2]) or line.startswith(ignore[1]) or line.startswith(" "+ignore[0])):
				
				dest.write(line)
