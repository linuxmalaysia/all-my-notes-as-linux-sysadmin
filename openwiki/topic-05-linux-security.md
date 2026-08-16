---
name: topic-05-linux-security
description: Silibus keselamatan OS Linux (Kebenaran fail, Firewall, Polisi) dipetakan kepada NOSS CU05.
tags:
  - linux
  - security
  - cu05
topics:
  - Firewalls
  - File Permissions
  - Mandatory Access Control
---

# Topik 5: Keselamatan Linux (CU05)

## Overview (Gambaran Keseluruhan)
Keselamatan merangkumi sekatan pengguna, perlindungan sistem fail, dan dinding api (firewall) pada tahap pelayan. Ia dipetakan secara eksklusif daripada **CU05 (User Account and Permissions Audits / Security Lockdowns)**.

## Silibus Utama
1. **Pengurusan Pengguna & Kumpulan (User & Group Management)**:
   - `useradd`, `usermod`, `groupadd`, fail `/etc/passwd` dan `/etc/shadow`.
2. **Kebenaran Sistem Fail (File Permissions & Ownership)**:
   - Konsep UGO (User, Group, Others).
   - Pengubahsuaian dengan `chmod` dan `chown`.
   - Konsep SUID, SGID, dan Sticky Bit.
3. **Dinding Api (Firewall & Port Security)**:
   - Konfigurasi Uncomplicated Firewall (`ufw`) di Ubuntu.
   - Konfigurasi `firewalld` di sistem berasaskan Red Hat.
4. **Sistem Kawalan Mandatori (MAC)**:
   - Pengenalan kepada SELinux (Enforcing, Permissive, Disabled).
   - Pengenalan kepada AppArmor.

## Pemetaan NOSS (NOSS Mapping)
Silibus ini memandu kemahiran Ejen AI berikut:
- `cu05-wa01-perform-user-account-and-permission-audits`
- `cu05-wa03-configure-client-firewall-profiles`
