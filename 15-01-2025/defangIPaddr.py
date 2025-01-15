'''1108. Defanging an IP Address
Easy
Topics
Companies
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".'''

# 35ms


def defangIPaddr(address):
    address =  address.replace(".", "[.]")

    return address


# 49ms
def defangIPaddr2(address):
    return "[.]".join(address.split("."))


print(defangIPaddr2("1.1.1.1"))
