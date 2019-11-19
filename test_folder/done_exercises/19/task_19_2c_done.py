# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''
import yaml
from pprint import pprint
import netmiko
import re
# списки команд с ошибками и без:
commands_with_errors = ['logging 0255.255.1', 'logging', 'sh i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands



def send_config_commands (device, verbose=True):
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
					my_inp = input("Продолжать выполнять команды? [y]/n: ")
					if my_inp == 'n':
						break
				
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
		result.append(send_config_commands(line_dict))
	
	pprint(result)
