# Lightweight Network Security & Port Scanner Tool

A beginner-friendly Python tool designed to perform basic network reconnaissance, scan TCP ports, detect active services, and log security scan results.

---

##  Project Overview

This project demonstrates core cybersecurity fundamentals, including:
- **Socket Programming:** Establishing direct TCP connections to target host IP addresses.
- **Port Reconnaissance:** Iterating through target port ranges to detect open listening ports.
- **Security Logging:** Automatically appending timestamped scan results to a log file (`scan_log.txt`).

---

##  Features

- **No Third-Party Dependencies:** Built using standard Python standard libraries (`socket`, `sys`, `datetime`).
- **Customizable Targets:** Scan local interface (`127.0.0.1`), LAN IP addresses, or domain names.
- **Port Range Control:** Easily adjust target port parameters.
- **Automated Alert/Scan Logging:** Records scan timestamps and open ports for security auditing.

---

##  Requirements & Setup

### Prerequisites
- Python 3.x installed on Windows, macOS, or Linux.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/network-port-scanner.git](https://github.com/YOUR_GITHUB_USERNAME/network-port-scanner.git)
