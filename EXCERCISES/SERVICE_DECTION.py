ip = input("Enter IP Address: ")
port = int(input("Enter Port: "))

print("\n========================================")
print("         SERVICE DETECTION              ")
print("========================================")

if port == 21:
    service = "FTP"
elif port == 22:
    service = "SSH"
elif port == 23:
    service = "Telnet"
elif port == 25:
    service = "SMTP"
elif port == 53:
    service = "DNS"
elif port == 80:
    service = "HTTP"
elif port == 110:
    service = "POP3"
elif port == 443:
    service = "HTTPS"
else:
    service = "Unknown"

print(f"Target IP : {ip}")
print(f"Port      : {port}")
print(f"Service   : {service}")
print("========================================")