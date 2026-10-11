# 🌐 Simple Ping Checker

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![ping3](https://img.shields.io/badge/ping3-latest-green)

A command-line network diagnostic tool for pinging IPv4, IPv6, and domain targets with real-time timestamps, latency statistics, and quiet mode.

---

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Commands](#-commands)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgments](#-acknowledgments)

---

## 📖 About the Project

Simple Ping Checker is a lightweight Python CLI tool that sends ICMP ping requests to IPv4 addresses, IPv6 addresses, or domain names. It provides real-time output with timestamps, DNS resolution for domains, and a summary with latency statistics after each run.

The tool is designed for quick network diagnostics from the terminal — no configuration files, no complex setup. Just run and ping.

---

## ❓ Why This Project?

Most ping tools offer limited output and no built-in statistics. This project solves that by providing:

- **Timestamped output** for correlating ping results with network events
- **Latency statistics** (min/avg/max) without needing external tools
- **Quiet mode** for scripting and automation
- **DNS resolution display** so you know exactly which IP a domain resolves to
- **Continuous mode** for long-running network monitoring
- **Full input validation** to prevent errors from bad input

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **IPv4 Ping** | Ping IPv4 addresses with full format validation |
| **IPv6 Ping** | Ping IPv6 addresses with format validation |
| **Domain Ping** | Ping domain names with DNS resolution display |
| **Quiet Mode** | Suppress per-packet output, show only summary statistics |
| **Latency Statistics** | Min/Avg/Max latency after each ping run |
| **Timeout Config** | Custom timeout in seconds (default: 4s) |
| **Continuous Mode** | Ping until Ctrl+C (set count to 0) |
| **TTL Control** | Set time-to-live on outgoing packets |
| **Timestamps** | Full `YYYY-MM-DD HH:MM:SS` timestamp on each reply |
| **Input Validation** | Validates IPs, domains, sizes, counts, timeouts, and TTLs |
| **Packet Size Control** | Custom ICMP payload size (default: 54 bytes) |
| **Source IP** | Optional source IP binding for multi-interface systems |

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.7+ |
| Ping Library | [ping3](https://github.com/kyan001/ping3) |
| DNS Resolution | `socket.gethostbyname` (stdlib) |
| IP Validation | `ipaddress` (stdlib) |

---

## 📁 Project Structure

```
Simple-ping-checker/
├── app.py                          # Main entry point with menu
├── LICENSE                         # MIT License
├── README.md                       # This file
├── requirements.txt                # Python dependencies
└── pings/
    ├── __init__.py                 # Package init
    ├── utils.py                    # Shared ping logic, DNS, timestamps
    ├── simple_ip_ping.py           # IPv4 ping module
    ├── simple_ipv6_ping.py         # IPv6 ping module
    └── simple_domain_ping.py       # Domain ping module
```

---

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/Marsh-Edge/Simple-ping-checker.git
cd Simple-ping-checker
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Or install dependencies directly:

```bash
pip install ping3 colorama
```

3. **Run the application**

```bash
python app.py
```

> **Note:** On Linux/macOS, you may need `sudo` for ICMP ping to work without root privileges. On Windows, no special privileges are required.

---

## 🚀 Usage

### Starting the Tool

```bash
python app.py
```

You will see the main menu:

```
===== Simple Ping Checker =====
1) IPv4 Ping
2) Domain Ping
3) IPv4 Ping (Quiet Mode)
4) Domain Ping (Quiet Mode)
5) IPv6 Ping
6) IPv6 Ping (Quiet Mode)

Choose an option (1-6):
```

### Example: IPv4 Ping

```
Choose an option (1-6): 1

Enter your source IP (DEFAULT YOUR IP) :
Enter your destination IP (DO NOT ENTER DOMAIN LIKE 'google.com'): 8.8.8.8
Enter packet size in bytes (DEFAULT 54) : 54
Enter packet count (0 for continuous, DEFAULT 4) : 4
Enter timeout in seconds (DEFAULT 4) : 4
Enter TTL (DEFAULT OS: 64 on Linux/macOS, 128 on Windows) :

Your source IP is : DEFAULT
Your destination IP is : 8.8.8.8
Your packet size is : 54
Your packet count is : 4

[2026-07-18 14:32:05] Reply from 8.8.8.8: bytes=54 time=12.3ms
[2026-07-18 14:32:05] Reply from 8.8.8.8: bytes=54 time=11.8ms
[2026-07-18 14:32:06] Reply from 8.8.8.8: bytes=54 time=15.7ms
[2026-07-18 14:32:06] Reply from 8.8.8.8: bytes=54 time=11.2ms

--- Ping Statistics ---
4 transmitted, 4 received, 0 lost (0.0% loss)
Min/Avg/Max = 11.2 / 12.8 / 15.7 ms
```

### Example: Domain Ping with DNS Resolution

```
Choose an option (1-6): 2

Enter your domain (DO NOT ENTER IP LIKE '8.8.8.8' or 'fd00::1'): google.com
...

Resolved: google.com -> 142.250.80.46

[2026-07-18 14:33:10] Reply from google.com: bytes=54 time=10.5ms
...
```

### Example: Quiet Mode

```
Choose an option (1-6): 3
...

(No per-packet output)

--- Ping Statistics ---
4 transmitted, 4 received, 0 lost (0.0% loss)
Min/Avg/Max = 11.2 / 12.8 / 15.7 ms
```

### Example: Continuous Mode

```
Enter packet count (0 for continuous, DEFAULT 4) : 0

(Continuous pinging until Ctrl+C)

[2026-07-18 14:34:00] Reply from 8.8.8.8: bytes=54 time=12.1ms
[2026-07-18 14:34:01] Reply from 8.8.8.8: bytes=54 time=11.9ms
^C
Stopped by user.

--- Ping Statistics ---
12 transmitted, 12 received, 0 lost (0.0% loss)
Min/Avg/Max = 10.5 / 12.3 / 15.2 ms
```

---

## ⌨️ Commands

| Option | Mode | Description |
|--------|------|-------------|
| `1` | IPv4 Ping | Ping an IPv4 address with full output |
| `2` | Domain Ping | Ping a domain name with DNS resolution |
| `3` | IPv4 Quiet | IPv4 ping with summary-only output |
| `4` | Domain Quiet | Domain ping with summary-only output |
| `5` | IPv6 Ping | Ping an IPv6 address with full output |
| `6` | IPv6 Quiet | IPv6 ping with summary-only output |

### Input Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Source IP | Your IP | Optional source IP for multi-interface systems |
| Destination | — | Target IP or domain (validated per mode) |
| Packet Size | 54 bytes | ICMP payload size |
| Packet Count | 4 | Number of pings (`0` = continuous) |
| Timeout | 4 seconds | Wait time per ping |
| TTL | OS default | Time-to-live (64 Linux/macOS, 128 Windows) |

---

## 🗺 Roadmap

### Completed

- [x] IPv4 ping with validation
- [x] Domain ping with validation
- [x] Quiet/summary mode with latency statistics
- [x] User-configurable timeout
- [x] Continuous/loop mode (count = 0)
- [x] DNS resolution display for domains
- [x] Timestamps on all ping output
- [x] TTL option
- [x] IPv6 ping support

### Upcoming

- [ ] Colored terminal output (green for success, red for failure)
- [ ] Export results to CSV/TXT
- [ ] Batch ping from file (multi-target)
- [ ] Ping interval control
- [ ] Auto-detect IP vs domain

---

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes input validation where applicable.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Edge Quantum**

- GitHub: [Marsh-Edge](https://github.com/Marsh-Edge)

---

## 🙏 Acknowledgments

- [ping3](https://github.com/kyan001/ping3) — The Python ping library that powers the ICMP functionality
