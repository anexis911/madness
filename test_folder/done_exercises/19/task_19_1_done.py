# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import yaml
from pprint import pprint
from netmiko import ConnectHandler

command = 'sh ip int br'


def send_show_command (device):
	with ConnectHandler (**device) as ssh:
		ssh.enable()
		result =ssh.send_command(command)
		return result
	
with open ('devices.yaml') as f:
	data = yaml.safe_load(f)
	result = []
	for line_dict in data:
		result.append(send_show_command(line_dict))
	
	pprint(result)
