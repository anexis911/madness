# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции send_commands, всегда будет передаваться только один из аргументов show, config.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

Пример работы функции:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: send_commands(r1, config=['username user5 password pass5', 'username user6 password pass6'])
Out[15]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#'
'''
import yaml
from pprint import pprint
import netmiko
import re
commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'


def send_commands(device, show_or_config):
	if type(show_or_config) == list:
		result = send_config_commands(device, show_or_config)
		return result
	else:
		result = send_show_command(device, show_or_config)
		return result
	
	


def send_show_command (device, command):
	try:
		with netmiko.ConnectHandler (**device) as ssh:
			print('Connecting to:', device['ip'])
			ssh.enable()
			result =ssh.send_command(command)
			
			return result
	except netmiko.NetMikoAuthenticationException as err:
		print("Oops, we've got an exception here!", err)
	except netmiko.ssh_exception.NetMikoTimeoutException as err:
		print("Oops, we've got an exception here!", err)
		



def send_config_commands (device, commands, verbose=True):
	try:
		result = {}
		if verbose:
			print("Connecting to:", device['ip'])
		with netmiko.ConnectHandler (**device) as ssh:
			ssh.enable()
			for command in commands:
				cfg = ssh.send_config_set(command)
				match = re.search(r'% (\D+[.:])', cfg)
				if match:
					print('Error occured while doing command:', command, ' Reason: ', match.groups())
				
				result[command] = cfg
		return result
	except netmiko.NetMikoAuthenticationException as err:
		print("Oops, we've got an exception here!", err)
	except netmiko.ssh_exception.NetMikoTimeoutException as err:
		print("Oops, we've got an exception here!", err)
		
		
		
with open ('devices.yaml') as f:
	data = yaml.safe_load(f)
	result = []
	for line_dict in data:
		result.append(send_commands(line_dict, commands))
	
	pprint(result)
		
