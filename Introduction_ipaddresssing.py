"""
THIS IS THE INTRODUCTION TO PYTHON WITH NETWORKING
"""
print("\n\n")
ip_address = "192.168.1.1"
port = 80

print(ip_address)
print(port)

# get the user input
ip_address = input("Enter IP Address: ")
port = int(input("Enter port: "))

print("\n ========================================= \n")

print("IP Address: ", ip_address)
print("Port: ", port)

print("========================================= \n")


"""
the common data types used 
"""
print("\n\n")

ip = "8.8.8.8" #string
port = 53 # integer
ports = [21,22,80, 80] # list

print(ip)
print("\n")
print(port)
print("\n")
print(ports)

print("======================================")

ip = input("Enter IP Address: ")
port = int(input("Enter port: "))
print("\n")
print(f"Scanning {ip} on port {port}......")
print("\n")
