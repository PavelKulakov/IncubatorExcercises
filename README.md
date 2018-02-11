You can find below initial conditions of the excercises presented in the repository:



Exercise 1:

Your program should ask two inputs from the user:

“Enter Ip address:”
“Enter subnet mask in decimal format:”
Program should:

Check the validity of ip address. If address is invalid, it should generate the error “Invalid IP address format” and prompt again “Enter ip address:”
Check the validity of the subnet mask. If subnet mask is not in decimal format or incorrect, then generate the error “Subnet mask is invalid” and prompt again “Enter subnet mask in decimal format”
The program should present the ip address in the binary formal like in example below (each number in decimal ip address has it’s own row of width 10 symbols).
Your program should print the network address and broadcast address for the given ip

======================================================================================

Exercise 2:

Your program should read the content of the file commands.txt which contains list of different commands(
each command is in a new line). Your program should look only for commands "switchport trunk allowed vlan ..."  all other commands should be ignored. (Example of the good command “switchport trunk allowed vlan 1,3,5,11,25,111,23,8”.)

Your program should:

1. print list of all common vlans in all commands, i.e. any good command from commands.txt contains this vlan
2. print list of all unique vlans, i.e for any vlan number from this list there should be only one command in the commands.txt file containing this vlan.
3. the output lists should not contains duplicated entries and should be sorted in ascending order.

======================================================================================

Excercise3:

your program should read information from the file ShowIpRoute.txt (the file contains only output of “show ip route”) and for each entry of dynamic routing protocol presented in the file you need to print the output like:

Protocol:	
Prefix:	
AD/Metric:	
Next-Hop:	
Last update:	
Outbound interface:

======================================================================================

Exercise 4:


You are given the following templates (just put them as it is in your script):

access_template = ['switchport mode access',

'switchport access vlan {}',

'switchport nonegotiate',

'spanning-tree portfast',

'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

'switchport mode trunk',

'switchport trunk allowed vlan {}']

Your program should ask:

‘Enter interface mode (access/trunk):’
‘Enter interface type and number:’
For access interfaces, script should request “Enter VLAN number”. For trunk interface, script should request list of allowed vlans “Enter allowed VLANs:”.
Your script should print the configuration depends on the input.

======================================================================================