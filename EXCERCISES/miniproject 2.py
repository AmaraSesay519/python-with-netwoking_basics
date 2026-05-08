"""
This is a smart port Identifier program version 1
"""
print("\n\n")
# get the user input
ip = input("Enter the IP address: ")
subnet = input("Enter the subnet mask: ")
port = int(input("Enter the port number: "))

# condition to check
if port == 21:
    service = "FTP"

elif port == 22:
    service = "SSH"
    status = "Recognized"
elif port == 23:
    service = "Telnet"
    status = "Recognized"
elif port == 25:
    service = "SMTP"
    status = "Recognized"
elif port == 53:
    service = "DNS"
    status = "Recognized"
elif port == 443:
    service = "HTTPS"
    status = "Recognized"
elif port == 80:
    service = "HTTP"
    status = "Recognized"
elif port == 110:
    service = "POP3"
    status = "Recognized"

else:
    status = "Port number not recognized"
print("\n\n")

# output
print("==================================================================")
print("                         SCAN RESULT                              ")
print("==================================================================")
print(f"Target IP : {ip}")
print(f"subnet mask: {subnet}")
print(f"port: {port}")
print(f"service: {service} ")
print(f"status: {status} ")

"""
below is to answer the test  questions

Q1.  this if condition runs when the condition is true , while the elif condition runs when you have 
multiple conditions if the first condition fail the second  condition will runs .

Q2.the program will excuted the first condition only.

Q3. port = int(input("Enter the port number: "))
if port == 443:
    service = "HTTPS"
   
else:
    service = "Not HTTPS"

Q4 port = int(input("Enter the port number: "))
if port == 80:
    print("HTTP) 
"""
