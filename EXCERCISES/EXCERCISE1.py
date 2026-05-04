# this is a project that takes the user input and print it on the console
print("\n\n")

# get user details
ipaddress = input("Enter ip address: ")
print("\n")
print("Target locked:" ,ipaddress)

print("\n\n")

#EXCERCISE 2
ip = input("Enter ip address to check: ")
print("\n")
subnet_mask = input("Enter subnet mask: ")

print("\n")
port = int(input("Enter port: "))

print("\n")
print("Attempting to connect to")
print(ip,":",subnet_mask ,":",port)

#EXCERCISE 3
print("\n")
# get multiple ports from the user
ports1 = int(input("Enter the first ports: "))
print("\n")
port2 = int(input("Enter second port: "))
print("\n")
port3 = int(input("Enter third  port: "))
port4 = int(input("Enter forth  port: "))


print("\n")
# stores the ports in a list
ports = [ports1, port2, port3, port4]

print("Commons ports:",ports)


print("\n")
print("=========================================================")

