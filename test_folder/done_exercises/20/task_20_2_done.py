# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed
import netmiko
import logging
import yaml
import time
from datetime import datetime

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(format = '%(threadName)s %(name)s %(levelname)s: %(message)s', level = logging.INFO)
start_msg = '===> {} Connection: {}'
received_msg = '<=== {} Received: {}'


def send_show( dev_dict, command):
	ip = dev_dict['ip']
	logging.info(start_msg.format(datetime.now().time(), ip))
	try:
		with netmiko.ConnectHandler(**dev_dict) as ssh:
			ssh.enable()
			result = ssh.send_command(command)
			logging.info(received_msg.format(datetime.now().time(), ip))
		return{ip: result}
	except netmiko.NetMikoAuthenticationException as err:
		logging.warning(err)



def send_show_command_to_devices (devices, command, filename, limit=3):
	final_result =[]
	with ThreadPoolExecutor(max_workers = limit) as executor:
		futures = []
		for device in devices:
			futures.append(executor.submit(send_show, device, command))
		for f in as_completed(futures):
			print(f.result())
			final_result.append(f.result())
	pprint(final_result)
	with open (filename, 'w') as f:
		yaml.dump(final_result, f)



if __name__ == "__main__":
	command = 'sh ip int br'
	with open('devices.yaml') as f:
		devices = yaml.load(f, Loader=yaml.FullLoader)
	send_show_command_to_devices(devices, command, 'my_result.yaml')
	
