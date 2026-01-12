# Linux Intrusion Detection Lab

This Project simulates real-world brute-force SSH attacks using Kali Linux and Ubuntu Server in an isolated lab environment

## Features
- Parses authentication logs from /var/log/auth.log
- Detects repeated failed SSH login attempts
- Tracks attack duration per IP
- Automatically blocks attackers using UFW firewall rules

## Tools Used
- Kali Linux (Attacker)
- Ubuntu Server (Victim)
- Hydra, Nmap, SSH
- Python 3
- UTM on Apple Silicon (M2 Pro)

# Sample Output
--- Intrusion Detection Report---

ALERT: 192.168.64.3
Attempts: 5
First Seen: 2026-01-11 05:29:46.541707+00:00
Last Seen: 2026-01-11 05:29:46.588486+00:00
Duration: 0:00:00.046779

## Skills Demonstrated
- Linux log analysis
- Python automation for intrusion detection
- Network attack simulation
- Incident response and firewall mitigation
