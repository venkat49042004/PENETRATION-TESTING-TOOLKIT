import socket

def scan_ports(target_ip, port_range=100):
    open_ports = []
    print(f"[~] Scanning {target_ip} for open ports 1 to {port_range}")
    
    for port in range(1, port_range + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((target_ip, port)) == 0:
                    print(f"[+] Port {port} is OPEN")
                    open_ports.append(port)
        except KeyboardInterrupt:
            print("\n[!] Scan cancelled by user.")
            break
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
    
    return open_ports
