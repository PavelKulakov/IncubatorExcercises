import re

"""Defining the initial variables"""

access_template = ['switchport mode access', 'switchport access vlan {}', 'switchport nonegotiate','spanning-tree portfast','spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan {}']

"""Defining a printing function for value warnings"""


def value_warning():
    print("Please, enter valid values")


"""Defining a function for access mode switchport configuration:
    1. The function checks the validity of entered interface type and number using regex
    2. It also checks if an entered access VLAN number is a number between 1 and 4096
    3. When all the checks are done it replaces {} symbol in the initial template with a VLAN number"""


def access():
    while True:
        interface = input("Enter interface type and number: ")
        vlan = input("Enter VLAN number: ")
        try:
            if re.findall("((?:(?:(?:Fa|Gi)\d+$)|(?:(?:Fa|Gi)(?:\d+\/\d+){1,3}))|(?:Po\d+))", interface, re.I) and 1 <= int(vlan) <= 4096:
                pass
            else:
                value_warning()
                continue
        except ValueError:
            value_warning()
            continue
        access_template[1] = access_template[1].replace("{}", vlan)
        print("\nInterface", interface)
        for x in range(0, len(access_template)):
            print(access_template[x])
        break


"""Defining a function for trunk mode switchport configuration:
    1. The function checks the validity of entered interface type and number using regex
    2. It also checks if an entered trunk allowed VLANs are valid
    3. When all the checks are done it replaces {} symbol in the initial template with a allowed VLANs number"""


def trunk():
    interface = input("Enter interface type and number: ")
    vlans = input("Enter allowed VLANs: ")
    if re.findall("((?:(?:(?:Fa|Gi)\d+$)|(?:(?:Fa|Gi)(?:\d+\/\d+){1,3}))|(?:Po\d+))", interface, re.I):
        try:
            for each_vlan in vlans.split(","):
                if 1 <= int(each_vlan) <= 4096:
                    continue
                else:
                    value_warning()
                    return trunk()
        except ValueError:
            value_warning()
            return trunk()
        pass
    else:
        value_warning()
        return trunk()
    trunk_template[2] = trunk_template[2].replace("{}", vlans)
    print("\nInterface", interface)
    for y in range(0, len(trunk_template)):
        print(trunk_template[y])


"""This part of a program ask user for an interface mode he wants to configure 
and applies access/trunk template accordingly"""


while True:
    mode = input("Enter interface mode (access/trunk): ")
    if mode == "access":
        access()
        break
    elif mode == "trunk":
        trunk()
        break
    else:
        value_warning()
        continue
