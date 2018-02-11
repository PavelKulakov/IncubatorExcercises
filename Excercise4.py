import re

access_template = ['switchport mode access', 'switchport access vlan {}', 'switchport nonegotiate','spanning-tree portfast','spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan {}']

while True:
    mode = input("Enter interface mode (access/trunk): ")
    if mode == "access":
        interface = input("Enter interface type and number: ")
        if re.findall("((?:(?:Fa|Gi|Eth)\d(?:\/*\d*){0,3})|(?:Po\d*))", interface, re.I):
            pass
        else:
            print("Please, enter valid value")
            continue
        vlan = input("Enter VLAN number: ")
        break
    elif mode == "trunk":
        interface = input("Enter interface type and number: ")
        if re.findall("((?:(?:Fa|Gi|Eth)\d(?:\/*\d*){0,3})|(?:Po\d*))", interface, re.I):
            pass
        else:
            print("Please, enter valid value")
            continue
        break
    else:
        print("Please, enter valid value: ")
        continue
