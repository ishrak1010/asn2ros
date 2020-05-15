import os

name = input("Enter AS Number: ")

os.system("whois -h whois.radb.net -- '-i origin AS" + name + "' | grep ^route > " + name + ".txt")

list_name = input("Enter address-list name: ")

handle = open(name + ".txt")

print("/ip firewall address-list")

for line in handle :
    if "route6:" in line:
        continue
    else:
        line = line.split()
        address= line[1]
        print("add list=" + list_name, "address=" + address)

