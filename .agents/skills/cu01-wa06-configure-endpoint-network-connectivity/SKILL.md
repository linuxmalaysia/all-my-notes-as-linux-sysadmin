---
name: cu01-wa06-configure-endpoint-network-connectivity
description: "Executes NOSS Work Activity: Configure Endpoint Network Connectivity (NetworkManager, nmcli, iproute2, Static IP, DHCP, Wi-Fi, DNS)"
topics: [noss, cu01, wa06, networking, networkmanager]
tags: [cu01, wa06, nmcli, ip, dhcp, wifi, dns, endpoint]
okf_version: 0.1
type: skill
---

# Configure Endpoint Network Connectivity

*Executes NOSS standard K622-XXX-3:2026-C01 WA06*

## Overview

This skill provides procedural execution steps for configuring wired (Ethernet) and wireless (Wi-Fi) network connections on Linux desktop endpoints using NetworkManager (`nmcli`), `iproute2` (`ip`), and `systemd-resolved` according to NOSS Level 3 standards.

## Procedure

### 1. Network Interface Inspection

```bash
ip -c a
ip route show
nmcli device status
```

### 2. Static IPv4 Configuration (`nmcli`)

```bash
sudo nmcli connection add type ethernet con-name "Static-LAN" ifname eth0 ip4 192.168.1.150/24 gw4 192.168.1.1
sudo nmcli connection modify "Static-LAN" ipv4.dns "192.168.1.10 8.8.8.8"
sudo nmcli connection modify "Static-LAN" ipv4.method manual
sudo nmcli connection up "Static-LAN"
```

### 3. Dynamic DHCP Configuration

When switching an existing connection profile from static to dynamic DHCP, clear static parameters:

```bash
sudo nmcli connection modify "Static-LAN" ipv4.addresses "" ipv4.gateway "" ipv4.dns ""
sudo nmcli connection modify "Static-LAN" ipv4.method auto
sudo nmcli connection up "Static-LAN"
```

### 4. Wi-Fi Connection (WPA2/WPA3 Personal & Enterprise)

```bash
nmcli radio wifi on
nmcli device wifi list

# WPA2/WPA3 Personal (interactive password prompt):
sudo nmcli --ask device wifi connect "Pejabat_WiFi"
```

### 5. DNS Verification

```bash
resolvectl status
dig www.jdn.gov.my
```

## Security & Governance

- Secure Wi-Fi with WPA2/WPA3 Enterprise authentication.
- Restrict connection profile read permissions (`/etc/NetworkManager/system-connections/` to `600`).
- Comply with ISO/IEC 27001 and JDN/MAMPU network access control guidelines.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
