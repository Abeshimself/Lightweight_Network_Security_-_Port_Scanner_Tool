#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_ports(target_host, start_port=20, end_port=100):
    """
    A simple port scanner that checks open TCP ports on a target host.
    """
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[!] Error: Could not resolve hostname '{target_host}'.")
        sys.exit()

    print("=" * 50)
    print(f" Scanning target: {target_ip}")
    print(f" Time started:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Wait max 0.5 seconds per port
        
        # Attempt to connect to port
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            open_ports.append(port)
        
        s.close()

    print("-" * 50)
    print(f"Scan complete. Found {len(open_ports)} open port(s).")
    
    # Save simple log to file
    with open("scan_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] Scanned {target_ip}: Open ports = {open_ports}\n")


if __name__ == "__main__":
    # Scans localhost by default; change to target IP or domain as needed
    target = input("Enter target IP or domain (default: 127.0.0.1): ").strip()
    if not target:
        target = "127.0.0.1"
        
    scan_ports(target, start_port=20, end_port=100)