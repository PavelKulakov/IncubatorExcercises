import re

#Checking the validity of ip address(using regex)

while True:
    ip_addr = input("\nEnter Ip address: ")
    if re.match("^(([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-5]{2})\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5]{2})\.){2}(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5]{2}))$",ip_addr):
        break
    else:
        print("Invalid IP address format")
        continue

#Checking the validity of subnet mask

while True:
    try:
        subnet_mask = int(input("Enter subnet mask in decimal format: "))
    except ValueError:
        print("Subnet mask is invalid")
        continue
    if (subnet_mask <= 32) and (subnet_mask >= 2):
        break
    elif subnet_mask == 1:
        print("Wow! Seems like you have a really huge broadcast domain!")
        break
    else:
        print("Subnet mask is invalid")
        continue

#IP address binary format presentation

ip_addr_bin = []
ip_addr_dec = ip_addr.split('.')

for dec_octet in ip_addr_dec:
    bin_octet = bin(int(dec_octet)).split("b")[1]
    if len(bin_octet) < 8:
        bin_octet_zeros = bin_octet.zfill(8)
        ip_addr_bin.append(bin_octet_zeros)
    else:
        ip_addr_bin.append(bin_octet)

#Printing IP address in decimal and binary formats

print("\n{0:^8}{1:^10}{2:^10}{3:^10}".format(ip_addr_dec[0], ip_addr_dec[1], ip_addr_dec[2], ip_addr_dec[3]))
print("{0} {1} {2} {3}".format(ip_addr_bin[0], ip_addr_bin[1], ip_addr_bin[2], ip_addr_bin[3]))


#Converting subnet mask from CIDR decimal notation into binary format

subnet_mask_bin = "1" * subnet_mask + "0" * (32-subnet_mask)

#Converting ip address into the same format

ip_addr_bin_string = "".join(ip_addr_bin)

#Presenting network and broadcast address in binary format by combining binary IP and binary network mask from user input

network_addr_bin = ip_addr_bin_string[:subnet_mask] + "0" * (32-subnet_mask)
broadcast_addr_bin = ip_addr_bin_string[:subnet_mask] + "1" * (32-subnet_mask)

#Converting network and broadcast addresses into the list of octets, each of octets is converted to decimal

network_addr_octets = []
for octet in range(0, len(network_addr_bin), 8):
    network_addr_octet = network_addr_bin[octet:octet+8]
    network_addr_octets.append(str(int(network_addr_octet, 2)))

#Converting network address into the string format

network_addr_dec = ".".join(network_addr_octets)

#Doing the same manipulations for broadcast address:

broadcast_addr_octets = []
for octet in range(0,len(broadcast_addr_bin),8):
    broadcast_addr_octet = broadcast_addr_bin[octet:octet+8]
    broadcast_addr_octets.append(str(int(broadcast_addr_octet, 2)))

broadcast_addr_dec = ".".join(broadcast_addr_octets)

#Printing borh the network and broadcast addresses in decimal format

print("\nnetwork address: ", network_addr_dec+"/"+str(subnet_mask))
print("broadcast address: ", broadcast_addr_dec+"/"+str(subnet_mask))








