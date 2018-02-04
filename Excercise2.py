#opening the commands.txt file for reading

with open("commands.txt", "r") as commands:
    commands_var = commands.readlines()
    trunk_list = []
    for each_element in commands_var:
        if each_element.startswith("switchport trunk allowed vlan"):
            trunk_list.append(each_element.strip("switchport trunk allowed vlan"))

chunks = [trunk_list[x:x+1] for x in range(0, len(trunk_list))]




