
my_input_1 = input("Введите режим работы интерфейса access: ")
my_input_2 = input("Введите тип и номер интерфейса: ")
my_input_3 = input("Введите номер влан(ов): ")
my_dict= {"access": "switchport mode access\nswitchport access vlan {}\nswitchport nonegotiate\nspanning-tree portfast\nspanning-tree bpduguard enable",
"trunk":"switchport trunk encapsulation dot1q\nswitchport mode trunk\nswitchport trunk allowed vlan {}\n"

}
print("Interface: " + my_input_2)
working_string = my_dict.get(my_input_1)


print(working_string.format(my_input_3))
