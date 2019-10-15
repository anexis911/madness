# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

try:
	ip = input("Введите айпи адрес: ")
	first_byte = int(ip.split(".")[0])
	ip_list = ip.split(".")
	tsikl = True
	if ip.replace(".","").isdigit():
		tsikl= True
	else:
		tsikl = False
	
	
	for list_str in  ip_list:
		if int(list_str) >256:
			tsikl = False
			break
		elif len(list_str) >= 4:
			tsikl = False
			break
		else:
			pass
	if tsikl == False:
		print ("Неправильный IP-адрес")
	else:
		if first_byte in list(range(1, 224)):
			print("Ваш IP типа unicast")
			
		elif first_byte in list(range(224, 240)):
			print("Ваш IP типа multicast")
			
		elif ip == "255.255.255.255":
			print("Ваш IP типа local broadcast")
			
		elif ip == "0.0.0.0":
			print("Ваш IP типа unassigned")
			
		else:
			print("Ваш IP типа unused")
			
		
			
			
except ValueError:
	print("Неправильный IP-адрес")


