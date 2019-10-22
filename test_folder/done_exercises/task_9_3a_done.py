# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
acces_result = {}
trunk_result = {}
eth_1_list = {}
def get_int_vlan_map (input_file):
	with open (input_file) as f:
		
		for line in f:
			if "FastEthernet" in line:
				intf = line.split()[1]
				eth_1_list[intf] = 1
				
			if "access" in line:
				new_ac_line = line.split()
				
				for word_l in new_ac_line:
					if word_l[-1].isdigit():
						acces_result[intf]=word_l
			
			if "trunk" in line:
				new_tr_line = line.split()
				
				for word_l in new_tr_line:
					if word_l[-1].isdigit():
						trunk_result[intf] = word_l
					
				
				
		
		
		new_ac, new_tr, new_eth  = set(acces_result.keys()), set(trunk_result.keys()), set(eth_1_list.keys())
		res_set = (new_eth - new_ac - new_tr)
		for key_val in res_set:
			acces_result[key_val] = 1
		print(acces_result, trunk_result)
				
get_int_vlan_map("config_sw2.txt")
