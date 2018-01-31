import re

#Checking the validity of ip address(using regex)

while True:
    ip_addr = input("Enter Ip address: ")
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







