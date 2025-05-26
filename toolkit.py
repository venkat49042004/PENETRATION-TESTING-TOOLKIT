from modules import port_scanner, brute_forcer

print("1. Port Scanner")
print("2. SSH Brute Forcer")
choice = input("Choose a module: ")

if choice == '1':
    ip = input("Enter target IP: ")
    ports = port_scanner.scan_ports(ip)
    print("Open Ports:", ports)

elif choice == '2':
    ip = input("Enter SSH IP: ")
    user = input("Enter username: ")
    wordlist = input("Enter path to password list: ")
    brute_forcer.brute_force_ssh(ip, user, wordlist)
