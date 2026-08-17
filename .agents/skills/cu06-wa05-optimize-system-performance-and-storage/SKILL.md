---
okf_version: 0.1
name: cu06-wa05-optimize-system-performance-and-storage
title: "CU06 WA05: Optimize System Performance and Storage"
timestamp: "2026-08-17T00:00:00Z"
type: skill
topics: ["noss", "cu06", "wa05", "ps", "top", "htop", "vmstat", "iostat", "nice", "renice", "kill", "cgroups"]
tags: ["noss", "cu06", "wa05", "ps", "top", "htop", "vmstat", "iostat", "nice", "renice", "kill", "cgroups"]
description: "Executes NOSS Work Activity K622-XXX-3:2026-C06 WA05: Optimize System Performance and Storage including process monitoring, CPU/Memory/IO diagnostics, POSIX signal handling, nice/renice priority tuning, and cgroups v2 resource controls."
resource: "file:///.agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md"
---

# CU06 WA05: Optimize System Performance and Storage

## 🎯 Purpose & Scope
This skill guides AI agents and system administrators in executing system optimization, process monitoring, and resource management mapped to Malaysian NOSS **K622-XXX-3:2026-C06 WA05**. Canonical reference environments are **Ubuntu 26.04 LTS "Quetzal"** and **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Execution Protocol & Commands

### 1. Process & System Resource Monitoring (`ps`, `top`, `htop`)
```bash
# Detailed static process listing and tree views
ps aux
ps axjf
ps aux --sort=-%mem | head -n 10
ps aux --sort=-%cpu | head -n 10

# Real-time interactive process monitoring
top
htop
```

### 2. Memory, CPU & I/O Diagnostics (`uptime`, `free`, `vmstat`, `iostat`)
```bash
# Load average and memory usage
uptime
free -h

# Virtual memory statistics (interval 1s, count 5)
vmstat 1 5

# Disk I/O performance and process I/O breakdown
iostat -xz 1 5
sudo pidstat -d 1 5
```

### 3. POSIX Signal Handling & Process Termination (`kill`, `killall`, `pkill`)
```bash
# Graceful termination SIGTERM (15)
kill -15 <PID>

# Forceful termination SIGKILL (9)
kill -9 <PID>

# Configuration reload SIGHUP (1)
sudo kill -1 <PID>

# Terminate processes by name
sudo killall -15 nginx
sudo pkill -f "python3 script.py"
```

### 4. Process Priority & I/O Scheduling (`nice`, `renice`, `ionice`)
```bash
# Launch process with high CPU priority (nice value -10)
sudo nice -n -10 /usr/local/bin/heavy-data-process.sh

# Launch background task with low CPU priority (nice value 15)
nice -n 15 /usr/local/bin/backup.sh &

# Modify priority of a running process
sudo renice -n 5 -p <PID>

# Set I/O scheduling class to Idle (Class 3)
sudo ionice -c 3 /usr/local/bin/backup-job.sh
```

### 5. Resource Control with Control Groups v2 (`cgroups v2` & `systemd-run`)
```bash
# Execute process within cgroups v2 scope with memory and CPU caps
sudo systemd-run --scope -p MemoryMax=500M -p CPUQuota=50% /usr/local/bin/heavy-app
```

---

## 🔒 Security & Performance Hardening
- **Anti-Fork Bomb Limits:** Enforce maximum process limits in `/etc/security/limits.conf` (`nproc` & `nofile`).
- **Anomalous Process Sweeps:** Regularly audit processes originating from `/tmp` or `/dev/shm` for unapproved crypto-miners.
- **Graceful Termination Policy:** Always issue `SIGTERM (15)` before escalating to `SIGKILL (9)` to prevent database and file system corruption.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
