---
okf_version: 0.1
name: cu03-wa04-perform-core-server-configurations
title: "CU03 WA04: Perform Core Server Configurations"
timestamp: "2026-08-17T00:00:00Z"
type: skill
topics: ["noss", "cu03", "wa04", "systemd", "systemctl", "journalctl", "timedatectl", "chrony", "man"]
tags: ["noss", "cu03", "wa04", "systemd", "systemctl", "journalctl", "chrony", "timedatectl", "man"]
description: "Executes NOSS Work Activity K622-XXX-3:2026-C03 WA04: Perform Core Server Configurations including systemd service management, custom service units, journalctl audit logging, timedatectl/chrony time sync, and system man pages."
resource: "file:///.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md"
---

# CU03 WA04: Perform Core Server Configurations

## 🎯 Purpose & Scope
This skill guides AI agents and system administrators in executing core Linux server configurations mapped to Malaysian NOSS **K622-XXX-3:2026-C03 WA04**. Canonical reference environments are **Ubuntu 26.04 LTS "Quetzal"** and **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Execution Protocol & Commands

### 1. Systemd Service Unit Management (`systemctl`)
```bash
# Check status, start, stop, restart, and reload services
sudo systemctl status sshd
sudo systemctl start sshd
sudo systemctl stop sshd
sudo systemctl restart sshd
sudo systemctl reload sshd

# Enable or disable service auto-start at boot
sudo systemctl enable --now sshd
sudo systemctl disable sshd

# Mask unneeded or unsafe services
sudo systemctl mask telnet.service
```

### 2. Custom Unit File Creation (`/etc/systemd/system/myapp.service`)
```ini
[Unit]
Description=NOSS Core Application Service
After=network.target remote-fs.target
Wants=network-online.target

[Service]
Type=simple
User=nossapp
Group=nossapp
ExecStart=/usr/local/bin/myapp --config /etc/myapp/config.conf
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s

# JDN/MAMPU & ISO/IEC 27001 Hardening Directives
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
NoNewPrivileges=true
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
ReadWritePaths=/var/log/myapp /var/lib/myapp

[Install]
WantedBy=multi-user.target
```

```bash
# Register and launch custom unit
sudo useradd -r -s /sbin/nologin nossapp
sudo systemctl daemon-reload
sudo systemctl enable --now myapp.service
```

### 3. Journal Audit Logging (`journalctl`)
```bash
# Tail real-time service logs
sudo journalctl -u sshd -f

# Query error logs within specific timeframes
sudo journalctl -u myapp.service --since "2026-08-17 00:00:00" -p err..emerg

# Manage journal disk usage
sudo journalctl --disk-usage
sudo journalctl --vacuum-size=500M
```

### 4. Time Synchronization & Timezone (`timedatectl` & `chronyd`)
```bash
# Set timezone to Malaysia Standard Time
sudo timedatectl set-timezone Asia/Kuala_Lumpur
sudo timedatectl set-ntp true

# Chrony configuration (/etc/chrony/chrony.conf or /etc/chrony.conf)
# server my.pool.ntp.org iburst

# Verify Chrony NTP synchronization
sudo systemctl enable --now chronyd
chronyc sources -v
chronyc tracking
```

### 5. System Documentation Navigation (`man`, `apropos`, `whatis`, `plocate`)
```bash
# Search offline manual pages by keyword or section
man systemctl
man 5 fstab
man 8 useradd
apropos "systemctl"
whatis chronyd
whereis chronyc

# Rapid file lookup
sudo updatedb
plocate chrony.conf
```

---

## 🔒 Security & Compliance Safeguards
- **Service Minimisation:** Disable and mask unused legacy services (`telnet`, `rsh`, `rlogin`).
- **Least Privilege:** Run custom services under dedicated system accounts (`/sbin/nologin`).
- **ISO/IEC 27001 Auditability:** Enforce centralized journal logging and NTP time sync for accurate timestamping across server logs.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
