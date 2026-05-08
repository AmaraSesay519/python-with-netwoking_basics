import socket

ip = (input("Enter target IP: "))

print(f"\nScanning {ip}...\n")

for port in range(20, 1025):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    if result == 0:

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

        print(f"[OPEN] Port {port} 'n {service}")
    s.close()