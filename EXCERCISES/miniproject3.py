import socket

# User input
ipaddress = input("Enter IP Address: ")

print(f"\nScanning {ipaddress} ...\n")

# Counter for open ports
open_ports = 0

# Scan ports
for port in range(1, 1025):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((ipaddress, port))

    if result == 0:

        open_ports += 1

        if port == 21:
            service = "FTP"
        elif port == 22:
            service = "SSH"
        elif port == 80:
            service = "HTTP"
        elif port == 443:
            service = "HTTPS"
        else:
            service = "Unknown"

        print(f"[OPEN] Port {port} → {service}")

    s.close()

print("\nScan complete")
print(f"Total open ports: {open_ports}")