"""
this is the introduction to loop with python
"""

print("\n")

ip = int(input("Enter the target IP address: "))

print("\n")
# use the for loop to work it through
print("============================== PORT SCAN RESULT ============================= ")
print("\n")

for port  in range(20, 443):

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
    elif port == 443:
        service = "HTTPS"
    elif port == 80:
        service = "HTTP"

    elif port == 110:
        service = "POP3"
    else:
        service = "Unknown"

    print(f"port {port} n {service}")







print("===================================================")