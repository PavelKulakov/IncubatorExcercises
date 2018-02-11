import re
from itertools import islice

"Creating list objects for future usage"""

protocol = []
prefix = []
admetric = []
nexthop = []
lastupdate = []
outintf = []

"""Opening a RIB text file in read mode"""

with open("ShowIpRoute.txt", "r") as rib:

    """We create 'for' loop which reads file from 16th line (beginning of RIB itself), using itertools islice method.
    Then we create separate regex values for each corresponding meaning (Protocol, Prefix, Next-hop, etc.)
    Firstly, we handle protocol regex values to convert dynamic protocol abbreviations (O, OE1, B, D, etc)
    into actual protocol names and also to filter local, connected and static routes. Then, we handle other regexes,
    appending them to corresponding list objects created earlier"""

    for line in islice(rib, 15, None):
        protoregex = re.findall("^(O E1|O E2|O IA|O N1|O N2|O|B|D|EX|i|su|R|L|S|C)", line)
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
        elif "EX" in protoregex:
            protocol.append("EIGRP external")
        elif "i" in protoregex:
            protocol.append("IS-IS")
        elif "su" in protoregex:
            protocol.append("IS-IS summary")
        elif "R" in protoregex:
            protocol.append("RIP")
        elif "L" or "C" or "S" in protoregex:
            continue
        prefregex = re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}|$", line)[0]
        nhregex = re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}|$", line)[1]
        adregex = re.findall("\[(\d+\/\d+)\]|$", line)[0]
        updregex = re.findall("((?:\d+d\d+h)|(?:\d+\:\d+\:\d+))|$", line)[0]
        intfregex = re.findall("((?:\w*Ethernet\d(?:\/*\d*){0,3})|(?:Port-channel\d*)|(?:Serial\d(?:\/*\d*){0,3})|(?:Dialer\d*)|(?:Cellular\d*)(?:Tunnel\d*)|(?:Null0))|$", line)[0]
        prefix.append(prefregex)
        nexthop.append(nhregex)
        admetric.append(adregex)
        lastupdate.append(updregex)
        outintf.append(intfregex)

"""Creating a separate file for outputs to improve their readability. Appending each value to this file using print function in 'for' loop"""

with open("RIB_output.txt", "w") as rib_output:
    for x in range(0, len(protocol)):
        print("Protocol: ", protocol[x], file=rib_output)
        print("Prefix: ", prefix[x], file=rib_output)
        print("AD/Metric: ", admetric[x], file=rib_output)
        print("Next-Hop: ", nexthop[x], file=rib_output)
        print("Last update: ", lastupdate[x], file=rib_output)
        print("Outbound interface: ", outintf[x],file=rib_output)
        print("\n==================================================\n", file=rib_output)


