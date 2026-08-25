---
okf_version: 0.2
type: knowledge-node
title: "CU01-WA06: Konfigurasi Sambungan Rangkaian Endpoint Linux"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu01", "wa06", "rangkaian", "networkmanager", "iproute2"]
tags: ["cu01", "wa06", "nmcli", "ip", "dhcp", "wifi", "dns", "endpoint"]
description: "Panduan amali NOSS CU01-WA06 bagi konfigurasi NetworkManager, IP statik, DHCP, Wi-Fi, dan DNS pada sistem endpoint Linux."
resource: "file:///manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md"
---

# CU01-WA06: Konfigurasi Sambungan Rangkaian Endpoint Linux

## 🎯 Objektif Pembelajaran

Menguasai prosedur amali pengurusan dan konfigurasi sambungan rangkaian berwayar (*Ethernet*) dan tanpa wayar (*Wi-Fi*) pada sistem endpoint Linux mengikut piawaian **NOSS Tahap 3 (CU01-WA06)**.

Setelah menyempurnakan modul ini, pelajar akan dapat:

1. Menguruskan antara muka (*interface*) rangkaian menggunakan perkakas **NetworkManager** (`nmcli`, `nmtui`) dan **iproute2** (`ip`).
2. Konfigurasi alamat IP secara dinamik (**DHCP**) dan statik (**Static IP**) mengikut skema IPv4 serta penetapan asas IPv6 (SLAAC / DHCPv6).
3. Menyambungkan endpoint ke rangkaian tanpa wayar (*Wi-Fi*) dengan protokol keselamatan WPA2/WPA3-Personal dan WPA2/WPA3-Enterprise.
4. Menganalisis dan melakukan penyelesaian masalah (*troubleshooting*) rute (*routing*), resolusi nama DNS, dan ujian ketercapaian pelayan.

---

## 🛠️ Garis Panduan Amali & Prosedur Kerja

### 1. Diagnostik Rangkaian Asas (`iproute2` & Tools)

Sebelum membuat sebarang perubahan konfigurasi, lakukan semakan antara muka dan status semasa:

```bash
# 1. Senaraikan semua antara muka rangkaian dan alamat IP
ip addr show
# atau ringkas:
ip -c a

# 2. Senaraikan jadual hala tuju (routing table) dan laluan lalai (default gateway)
ip route show

# 3. Uji ketercapaian rangkaian tempatan dan internet
ping -c 4 192.168.1.1
ping -c 4 8.8.8.8
```

---

### 2. Konfigurasi NetworkManager Menggunakan CLI (`nmcli`)

NetworkManager ialah perkhidmatan standard pada **Ubuntu 26.04 LTS**, **AlmaLinux 10**, dan **Fedora 43**.

#### A. Semakan Status Sambungan

```bash
# Senaraikan peranti fizikal dan status ketersambungan
nmcli device status

# Senaraikan profil sambungan yang wujud
nmcli connection show
```

#### B. Konfigurasi Alamat IP Statik (Berwayar / Ethernet)

Untuk peranti pejabat yang memerlukan alamat IP tetap:

```bash
# 1. Cipta profil sambungan IP statik baharu bernama 'Pejabat-Statik' pada antaramuka eth0 (atau enp0s3)
sudo nmcli connection add type ethernet con-name "Pejabat-Statik" ifname eth0 \
  ip4 192.168.1.150/24 gw4 192.168.1.1

# 2. Menetapkannya pelayan DNS (contoh: DNS Jabatan / Cloudflare / Google)
sudo nmcli connection modify "Pejabat-Statik" ipv4.dns "192.168.1.10 8.8.8.8"

# 3. Tukar mod carian IPv4 kepada manual
sudo nmcli connection modify "Pejabat-Statik" ipv4.method manual

# 4. Aktifkan sambungan baharu
sudo nmcli connection up "Pejabat-Statik"
```

#### C. Konfigurasi Sambungan DHCP (Dinamik)

Apabila menukar profil sambungan daripada IP statik kepada DHCP dinamik, padamkan parameter statik terlebih dahulu:

```bash
# 1. Padamkan penetapan alamat IP statik, gateway, dan DNS lama
sudo nmcli connection modify "Pejabat-Statik" ipv4.addresses "" ipv4.gateway "" ipv4.dns ""

# 2. Tukar mod carian IPv4 kepada automatik (DHCP)
sudo nmcli connection modify "Pejabat-Statik" ipv4.method auto

# 3. Aktifkan semula sambungan
sudo nmcli connection up "Pejabat-Statik"
```

---

### 3. Sambungan Rangkaian Tanpa Wayar (Wi-Fi)

```bash
# 1. Pastikan peranti Wi-Fi diaktifkan
nmcli radio wifi on

# 2. Imbas SSID Wi-Fi yang wujud berhampiran
nmcli device wifi list

# 3. Menyambung ke SSID Wi-Fi WPA2/WPA3-Personal dengan meminta kata laluan secara interaktif
sudo nmcli device wifi connect "Wi-Fi_Pejabat" --ask
```

---

### 4. Konfigurasi DNS & Resolusi Nama (`/etc/resolv.conf` & systemd-resolved)

Pada sistem moden dengan `systemd-resolved`:

```bash
# 1. Semak status resolusi DNS semasa
resolvectl status

# 2. Menguji kelajuan dan ketepatan carian nama domain (DNS lookup)
dig www.jdn.gov.my
nslookup www.gov.my
```

---

## 🔒 Pematuhan Keselamatan JDN / MAMPU & ISO/IEC 27001

1. **Penyulitan Wi-Fi Enterprise:** Elakkan penggunaan rangkaian Wi-Fi terbuka tanpa penyulitan di persekitaran kerajaan. Wajibkan standard WPA2-Enterprise / WPA3.
2. **Kawalan Profil Rangkaian:** Pastikan fail konfigurasi di `/etc/NetworkManager/system-connections/` dilindungi dengan kebenaran cap jari fail `600` (hanya `root` boleh membaca kata laluan Wi-Fi/IP).
3. **Pemberhentian Perkhidmatan Tidak Selamat:** Matikan antara muka tanpa wayar jika tidak digunakan (`nmcli radio wifi off`) pada pelayan atau endpoint sensitif.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya mengenal pasti nama antaramuka rangkaian menggunakan `ip addr` dan `nmcli dev`.
- [ ] Berjaya mengkonfigurasi Alamat IP Statik dan Gateway menggunakan `nmcli`.
- [ ] Berjaya imbas dan menyambung peranti ke Wi-Fi bersekuriti.
- [ ] Berjaya menjalankan diagnostik resolusi DNS menggunakan `ping`, `dig`, dan `resolvectl`.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bandingkan perbezaan seni bina antara NetworkManager, Netplan (Ubuntu), dan systemd-networkd dalam pentadbiran Linux."*
2. *"Tuliskan skrip Bash penyelesaian masalah rangkaian yang menguji ping gateway, resolusi DNS, dan port HTTP/HTTPS secara automatik."*
3. *"Bagaimanakah cara mengkonfigurasi pengikatan rangkaian (network bonding / team) untuk toleransi kelemahan (fault tolerance) di Linux?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Rasmi NetworkManager](https://networkmanager.dev/docs/)
- [Panduan Rangkaian Ubuntu 26.04 LTS](https://ubuntu.com/server/docs/network-configuration)
- [Rujukan iproute2 Linux Documentation](https://wiki.linuxfoundation.org/networking/iproute2)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Linux Networking Cookbook** oleh Carla Schroder.
- **UNIX and Linux System Administration Handbook, 5th Edition** oleh Evi Nemeth et al.
- **Panduan Rangkaian & Pentadbiran Sistem Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
