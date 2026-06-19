# Basic Network Sniffer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scapy](https://img.shields.io/badge/Scapy-2.5%2B-green.svg)](https://scapy.net/)
[![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)]()

**CodeAlpha Cyber Security Internship Project**

A beginner-friendly Python application that captures and analyzes live network traffic using the Scapy library. This project helps you understand how data flows across a network and how common protocols like TCP, UDP, and ICMP work at the packet level.

---

## Project Description

Network sniffing is a fundamental skill in cybersecurity. Security professionals use packet capture tools to monitor traffic, detect suspicious activity, troubleshoot network issues, and investigate security incidents.

This project implements a **Basic Network Sniffer** that listens to live network traffic on your machine and displays essential information from each captured packet:

- **Source IP Address** — where the packet originated
- **Destination IP Address** — where the packet is headed
- **Protocol Type** — whether the packet uses TCP, UDP, or ICMP
- **Packet Summary** — a concise description of the packet contents

Built with Python and Scapy, the tool is designed to be simple, well-commented, and easy for beginners to read and extend.

---

## Features

- **Live Packet Capture** — Captures network packets in real time from your network interface
- **Source IP Display** — Shows the IP address that sent each packet
- **Destination IP Display** — Shows the IP address that receives each packet
- **Protocol Detection** — Identifies TCP, UDP, and ICMP protocols automatically
- **Packet Summary** — Displays a human-readable summary of each captured packet
- **Packet Counter** — Tracks and displays the total number of captured packets
- **Welcome Banner** — Prints a clear welcome message when the program starts
- **Graceful Error Handling** — Handles missing dependencies, permission errors, and Ctrl+C cleanly
- **Beginner-Friendly Code** — Well-commented source code suitable for learning

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming language |
| Scapy | Packet capture and network analysis |
| Npcap / libpcap | Low-level packet capture driver |

---

## Prerequisites

Before running this project, make sure you have:

1. **Python 3.8 or higher** — [Download Python](https://www.python.org/downloads/)
2. **Npcap** (Windows) or **libpcap** (Linux/macOS) — required for packet capture
   - Windows: Download and install [Npcap](https://npcap.com/#download) (check "Install Npcap in WinPcap API-compatible Mode")
   - Linux: `sudo apt install libpcap-dev` (Debian/Ubuntu)
   - macOS: libpcap is usually pre-installed

---

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/MalaikaRizwan/CodeAlpha_Basic_Network_Sniffer.git
cd CodeAlpha_Basic_Network_Sniffer
```

### Step 2: Create a virtual environment (recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

> **Note:** If `pip` is not recognized, always use `python -m pip` instead.

---

## Usage

> **Important:** Packet capture requires elevated privileges. You must run the program as Administrator on Windows or with `sudo` on Linux/macOS.

### Windows (Run as Administrator)

1. Open **PowerShell** or **Command Prompt** as **Administrator**
2. Navigate to the project folder:
   ```powershell
   cd CodeAlpha_Basic_Network_Sniffer
   ```
3. Activate the virtual environment (if using one):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. Run the sniffer:
   ```powershell
   python network_sniffer.py
   ```

### Linux/macOS

```bash
sudo python3 network_sniffer.py
```

### Stopping the Sniffer

Press **Ctrl+C** to stop capturing. The program will display the total number of packets captured.

---

## Sample Output

```
============================================================
       BASIC NETWORK SNIFFER - CodeAlpha Project
============================================================
  Capturing live network packets...
  Press Ctrl+C to stop the sniffer.
============================================================

[Packet #1]
  Source IP      : 192.168.100.117
  Destination IP : 151.101.128.223
  Protocol       : TCP
  Summary        : Ether / IP / TCP 192.168.100.117:55654 > 151.101.128.223:https PA / Raw
------------------------------------------------------------
[Packet #2]
  Source IP      : 192.168.100.117
  Destination IP : 8.8.8.8
  Protocol       : UDP
  Summary        : Ether / IP / UDP 192.168.100.117:53421 > 8.8.8.8:domain
------------------------------------------------------------

[INFO] Sniffer stopped. Total packets captured: 2
       Thank you for using Basic Network Sniffer!
```

---

## Project Structure

```
CodeAlpha_Basic_Network_Sniffer/
├── network_sniffer.py    # Main sniffer script
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `pip is not recognized` | Use `python -m pip install -r requirements.txt` |
| `Scapy is not installed` | Run `python -m pip install scapy` |
| `Permission denied` | Run as Administrator (Windows) or with `sudo` (Linux) |
| `Network interface error` | Install Npcap (Windows) or libpcap (Linux) |
| No packets appearing | Generate traffic by opening a browser or pinging a website |

---

## Ethical Use Disclaimer

This tool is intended for **educational purposes only** as part of the CodeAlpha Cyber Security Internship. Only capture network traffic on networks you own or have explicit permission to monitor. Unauthorized packet sniffing may violate laws and policies.

---

## Conclusion

The **Basic Network Sniffer** project provides hands-on experience with one of the core tools in cybersecurity — packet analysis. By building and running this sniffer, you learn:

- How network packets are structured and transmitted
- How to identify source and destination addresses in traffic
- How common protocols (TCP, UDP, ICMP) appear in captured data
- How to use Python and Scapy for network security tasks

This project serves as a solid foundation for more advanced topics such as intrusion detection, traffic analysis, and ethical hacking. As you continue your cybersecurity journey with CodeAlpha, the skills gained here will help you understand how attackers reconnaissance networks and how defenders monitor and protect them.

---

## Author

**Malaika Rizwan**

Developed as part of the **CodeAlpha Cyber Security Internship Program**.

- GitHub: [MalaikaRizwan](https://github.com/MalaikaRizwan)
- Website: [www.codealpha.tech](https://www.codealpha.tech)

---

## License

This project is created for educational purposes under the CodeAlpha Internship Program.
