from itertools import chain                                                         #importing all necessary modules
import re
import sys

with open("commands.txt", "r") as commands:                                         #opening the file in read mode
    commands_var = commands.readlines()                                             #reading the file using built-in readlines() method
    trunk_list = []                                                                 #defining a container for all 'switchport trunk' lines

    for each_element in commands_var:                                               #'for' loop is used to go over all lines in a file
        if each_element.startswith("switchport trunk allowed vlan"):                #if statement to work with only desired 'switchport..' commands
            each_element = each_element.strip("switchport trunk allowed vlan,\n")   #cutting the 'switchport trunk allowed vlan' text part
            trunk_list.append(set(each_element.split(",")))                         #appending every line to a big list and making each line a set for future intersection usage

    if re.search("switchport trunk allowed vlan", "".join(commands_var)) is None:   #if statement in case there are no 'switchport trunk..' lines in a file
            sys.exit("Line 'switchport trunk allowed vlan' was not found")

    common_vlans = list(set.intersection(*trunk_list))                              #using set.intersection method to find common vlans and transforming common_vlans variable back to list type               #
    unique_vlans = []
    for each_element in trunk_list:                                                 #'for' loop is used to handle each element in trunk_list
        list_union = list(chain(*trunk_list))                                       #defining a big list instead of pack of small lists
        for x in each_element:                                                      #'for' loop is used to handle every single vlan number in each element of trunk_list
            list_union.remove(x)                                                    #removing redundant vlan numbers
        set_union = set(list_union)                                                 #transforming the result of removal into a set
        unique_vlans.append(set(each_element) - set_union)                          #finding the difference between this result and an element in the initial list and appending it to a new list

    unique_vlans = chain(*unique_vlans)                                             #creating a big continious list instead of pack of small lists

    unique_vlans = [int(x) for x in unique_vlans]                                   #transforming list elements in unique_vlans and common_vlans
    common_vlans = [int(x) for x in common_vlans]                                   #lists to int type (for correct sorted() function usage)

    print("List_1 =", sorted(common_vlans))                                         #printing the results in ascending order
    print("List_2 =", sorted(unique_vlans))







