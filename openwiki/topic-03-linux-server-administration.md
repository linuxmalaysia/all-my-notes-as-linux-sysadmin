---
name: topic-03-linux-server-administration
description: Silibus pentadbiran pelayan Linux (Apache, SSH, Samba) dipetakan kepada NOSS CU03.
tags:
  - linux
  - server
  - cu03
---

# Topik 3: Pentadbiran Pelayan Linux (CU03)

## Overview (Gambaran Keseluruhan)
Pusat utama ekosistem Linux adalah pelayannya (Server). Topik ini menerangkan tentang proses perkhidmatan (*services*) dan peranan pelayan. Ia merupakan pemetaan langsung daripada **CU03 (Server Setup)**.

## Silibus Utama
1. **Pemasangan OS Pelayan (Server OS)**: 
   - Membezakan edisi Desktop vs Server (tiada GUI, dikawal CLI penuh).
   - *Static IP Configuration* menggunakan Netplan (Ubuntu) atau NetworkManager (RHEL).
2. **Remote Access & SSH**:
   - Pemasangan `openssh-server`.
   - Log masuk jarak jauh dan penggunaan kunci (SSH Keys) `/home/user/.ssh/authorized_keys`.
3. **Penyedia Khidmat (Service Roles)**:
   - **Web Server**: Apache (`httpd` / `apache2`) atau Nginx.
   - **File Sharing**: Samba (SMB) untuk Windows, NFS untuk persekitaran Linux.
   - **Database**: MariaDB / MySQL.

## Pemetaan NOSS (NOSS Mapping)
Silibus ini memandu kemahiran Ejen AI berikut:
- `cu03-wa04-perform-core-server-configurations`
- `cu03-wa05-implement-server-roles-and-services`
