# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''
import re
from pprint import pprint
import glob
import csv


sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)






def parse_sh_version (in_file):
	with open (in_file) as f:
		result=[]
		for line in f:
			line = line.strip()
			match_1 = re.search(r'Cisco .+Software \S+, Version (?P<vers>\S+)', line)
			match_2 = re.search(r'uptime is (?P<time>\S.+)', line)
			match_3 = re.search(r'image file is (?P<file>\S+)', line)
			if match_1:
				result.append(match_1.group("vers"))
			elif match_2:
				result.append(match_2.group("time"))
			elif match_3:
				result.append(match_3.group("file"))
	#print(result)		 
	return result



def write_inventory_to_csv (data_filenames, csv_filename):
	headers = ['hostname', 'ios', 'uptime', 'image']
	result = []
	for ffile in data_filenames:
		result_list = (parse_sh_version(ffile))
		result_list.insert(0, ffile)
		#print(result_list)
		result.append(list(zip(headers, result_list)))
		
	
	with open (csv_filename , "w") as f:
		writer = csv.writer(f, quoting = csv.QUOTE_NONNUMERIC)
		writer.writerow(result)
			
	
		
	




if __name__ == "__main__":
	write_inventory_to_csv(sh_version_files, "routers_inventory.csv")
	"""with open ("routers_inventory.csv") as f:
		reader = csv.reader(f)
		for line in reader:
			print(line)
	"""


