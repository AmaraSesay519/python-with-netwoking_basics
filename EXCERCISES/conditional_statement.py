# This is a detection logic program using python with networking

# get user input
print("\n")

ipaddress = input("Enter the IP address: ")
subnet_mask = input("Enter the subnet mask: ")
port = int(input("Enter the port: "))


print("\n=====================================================")
print("         SERVICE DETECTION              ")
print("=======================================================")


# condition to check
if port == 80:

   # print("====================================================")
    service = "HTTP services detected"
    #print("====================================================")

elif port == 443:

    #print("====================================================")
    service = "HTTPS services detected"
    #print("====================================================")


elif port == 21:

    #print("====================================================")
    service = "FTP detected"
    #print("====================================================")

elif port == 22:

    #print("======================================================")
    service = "SSH detected"
    #print("=====================================================")

elif port == 23:

    #print("======================================================")
    service = "Teline services detected"
    #print("======================================================")

elif port == 25:

   # print("=====================================================")
    service = "SMTP service detected"
    #print("======================================================")

elif port == 53:

   # print("====================================================")
    service = "DNS service detected"
    #print("======================================================")

elif port == 110:

    #print("======================================================")
    service = "POP3 service detected"
else:

    #print("====================================================")
    service = "Port number not recognized"
   #print("====================================================")

#output of the project

print(f"Target IP : {ipaddress}")
print(f"subnetmask : {subnet_mask}")
print(f"Port      : {port}")
print(f"Service   : {service}")
print("========================================")