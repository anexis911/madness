# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
import yaml
from pprint import pprint
import netmiko

command = 'sh ip int br'


def send_show_command (device):
	try:
		with netmiko.ConnectHandler (**device) as ssh:
			ssh.enable()
			result =ssh.send_command(command)
			return result
	except netmiko.NetMikoAuthenticationException as err:
		print("Oops, we've got an exception here!", err)
with open ('devices.yaml') as f:
	data = yaml.safe_load(f)
	result = []
	for line_dict in data:
		result.append(send_show_command(line_dict))
	
	pprint(result)
