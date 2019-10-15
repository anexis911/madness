# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
finished = False
while not finished:
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
			continue
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
			finished = True
	except ValueError:
		print ("Неправильный IP-адрес")
			
		
			

