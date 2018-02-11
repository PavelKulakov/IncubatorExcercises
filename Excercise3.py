import re
from itertools import islice

protocol = []
prefix = []
admetric = []
nexthop = []
lastupdate = []
outintf = []


with open("ShowIpRoute.txt", "r") as rib:
    for line in islice(rib, 12, None):
        protoregex = re.findall("^(O E1|O E2|O IA|O N1|O N2|O|B|D|L|C|S|EX|i|su)", line)
        prefregex = re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}|$", line)[0]
        nhregex = re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}|$", line)[1]
        adregex = re.findall("\[(\d+\/\d+)\]|$", line)[0]
        updregex = re.findall("((?:\d\w\d+\w)|(?:\d+\:\d+\:\d+))|$", line)[0]
        prefix.append(prefregex)
        nexthop.append(nhregex)
        admetric.append(adregex)
        lastupdate.append(updregex)
        if "O" in protoregex:
            protocol.append("OSPF")
        elif "O E1" in protoregex:
            protocol.append("OSPF external type 1")
        elif "O E2" in protoregex:
            protocol.append("OSPF external type 2")
        elif "O IA" in protoregex:
            protocol.append("OSPF inter-area")
        elif "O N1" in protoregex:
            protocol.append("OSPF NSSA external type 1")
        elif "O N2" in protoregex:
            protocol.append("OSPF NSSA external type 2")
        elif "B" in protoregex:
            protocol.append("BGP")
        elif "D" in protoregex:
            protocol.append("EIGRP")
        elif "L" in protoregex:
            protocol.append("local")
        elif "C" in protoregex:
            protocol.append("connected")
        elif "S" in protoregex:
            protocol.append("static")
        elif "EX" in protoregex:
            protocol.append("EIGRP external")
        elif "i" in protoregex:
            protocol.append("IS-IS")
        elif "su" in protoregex:
            protocol.append("IS-IS summary")

print(protocol)
print(prefix)
print(admetric)
print(nexthop)
print(lastupdate)

"""for line in islice(rib, 12, None):
        print(line)
        print("\nProtocol: ", protocol[0])
        print("\nPrefix: ", prefix[0])
        print("\nNext-Hop: ", nexthop[0])"""




"""for each_route in protocol:
    print("\nProtocol: ", each_route)
for each_route in prefix:
    print("\nPrefix: ", each_route[0])
for each_route in nexthop:
    print("\nNext-Hop: ", each_route[0])
"""
"""print("AD/Metric:\n")
print("Next-Hop:\n")
print("Last update:\n")
print("Outbound interface:\n")"""



