# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

my_input_1 = input("Введите сеть IP и маску в формате n.n.n.n/n ")
ip= my_input_1[0:-3].split(".")
ip.insert(3, "0")
print(ip)
mk= my_input_1[-3:]


mask_dictionary = {
"/32": "255.255.255.255",
"/31": "255.255.255.254",
"/30": "255.255.255.252",
"/29": "255.255.255.248",
"/28": "255.255.255.240",
"/27": "255.255.255.224",
"/26": "255.255.255.192",
"/25": "255.255.255.128",
"/24": "255.255.255.000",
"/23": "255.255.254.000",
"/22": "255.255.252.000",
"/21": "255.255.248.000",
"/20": "255.255.240.000",
"/19": "255.255.224.000",
"/18": "255.255.192.000",
"/17": "255.255.128.000",
"/16": "255.255.000.000",
"/15": "255.254.000.000",
"/14": "255.252.000.000",
"/13": "255.248.000.000",
"/12": "255.240.000.000",
"/11": "255.224.000.000",
"/10": "255.192.000.000",
"/9": "255.128.000.000",
"/8": "255.000.000.000",
"/7": "254.000.000.000",
"/6": "252.000.000.000",
"/5": "248.000.000.000",
"/4": "240.000.000.000",
"/3": "224.000.000.000",
"/2": "192.000.000.000",
"/1": "128.000.000.000",
"/0": "000.000.000.000",
}

nmk = mask_dictionary[mk].split(".")



nt_template = '''
Network:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}

'''
mask_template = '''
Mask:
{}
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}

'''

print(nt_template.format(ip[0],ip[1],ip[2],ip[3],int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print("-"*50)
print(mask_template.format(mk,nmk[0],nmk[1],nmk[2],nmk[3],int(nmk[0]),int(nmk[1]),int(nmk[2]),int(nmk[3])))

