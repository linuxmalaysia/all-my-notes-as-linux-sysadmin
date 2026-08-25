---
okf_version: 0.1
type: knowledge-node
title: "Pentadbiran Pengguna, Kebenaran Fail & Kawalan Akses Endpoint Linux"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu05", "cu01", "panduan-amali", "manual-linux", "security"]
tags: ["cu05", "cu01", "linux", "noss", "amali", "users", "permissions", "acl", "faillock"]
description: "Panduan amali komprehesif pentadbiran pengguna, kumpulan, /etc/shadow, visudo, kebenaran fail chmod/chown, SUID/SGID/Sticky bit, POSIX ACL, faillock, FHS, dan penutupan sistem selamat."
resource: "file:///manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md"
---

# Pentadbiran Pengguna, Kebenaran Fail & Kawalan Akses Endpoint Linux

## 🎯 Objektif Pembelajaran

Menguasai pentadbiran pengguna dan kumpulan, kawalan kebenaran fail asas dan lanjutan (POSIX ACL & Bit Khas SUID/SGID/Sticky), pengukuhan dasar kata laluan (`faillock`), navigasi struktur FHS, pencarian fail, serta kawalan keselamatan fizikal/sesi terminal mengikut piawaian **NOSS CU05 & CU01** serta standard keselamatan **Jabatan Digital Negara (JDN) / MAMPU** dan **ISO/IEC 27001**.

> [!NOTE]
> Modul ini dipetakan daripada **Bab 4 (Pentadbiran Pengguna, Kebenaran & Pelayaran)** ke dalam Unit Kompetensi **CU05 (Kawalan Keselamatan Endpoint & Audit)** dan **CU01 (Aktiviti Asas Linux)** untuk edaran rasmi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 📐 1. Pentadbiran Pengguna & Kumpulan Sistem

### 1.1 Struktur Fail Konfigurasi Identiti

Dalam Linux, maklumat pengguna dan keselamatan disimpan dalam fail sistem teras:

- `/etc/passwd`: Menyimpan senarai akaun pengguna, UID, GID, direktori perumah, dan shell log masuk.
- `/etc/shadow`: Menyimpan kata laluan terdisi (*hashed password*) terenkripsi dengan algoritma SHA-512/Yescrypt, tarikh tamat tempoh, dan kawalan akses (hanya boleh dibaca oleh `root` atau kumpulan `shadow`).
- `/etc/group`: Menyimpan maklumat kumpulan pengguna dan senarai ahli.
- `/etc/gshadow`: Menyimpan maklumat keselamatan kumpulan dan kata laluan kumpulan.

### 1.2 Penciptaan dan Pengurusan Akaun Pengguna (`useradd`, `usermod`, `userdel`)

```bash
# Cipta kumpulan pentadbir atau projek baharu
sudo groupadd sysadmin_sec

# Cipta akaun pengguna baharu dengan direktori perumah dan shell Bash
sudo useradd -m -g sysadmin_sec -s /bin/bash -c "Ahmad Pengawas Sistem" ahmad

# Tetapkan kata laluan awal untuk pengguna
sudo passwd ahmad

# Tambahkan pengguna ke kumpulan tambahan (contohnya kumpulan sudo/wheel)
# Pada Ubuntu 26.04 LTS:
sudo usermod -aG sudo ahmad

# Pada AlmaLinux 10 / Fedora 43:
sudo usermod -aG wheel ahmad

# Semak identiti dan keahlian kumpulan pengguna
id ahmad
```

---

## 🔒 2. Polisi Kebolehan Keistimewaan Sistem (`visudo`) & Dasar Kata Laluan (`faillock`)

### 2.1 Konfigurasi Privilesej Pentadbir dengan `visudo`

Penggunaan log masuk terus sebagai `root` adalah **DILARANG** di bawah garis panduan JDN/MAMPU. Sebaliknya, pentadbiran MESTI dilaksanakan melalui `sudo` dengan audit log lengkap.

```bash
# Buka fail /etc/sudoers dengan selamat menggunakan visudo
sudo visudo
```

Tambah peraturan khusus keistimewaan minimum (*Principle of Least Privilege*):
```text
# Membenarkan kumpulan sysadmin_sec menjalankan arahan pentadbiran dengan pengesahan
%sysadmin_sec ALL=(ALL:ALL) ALL

# Membenarkan pentadbiran perkhidmatan tanpa kata laluan untuk akaun tertentu jika diperlukan
ahmad ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx
```

### 2.2 Perlindungan Brute-Force & Penguncian Akaun (`faillock`)

Untuk mematuhi standard ISO/IEC 27001, sistem perlu mengunci akaun secara automatik selepas percubaan log masuk gagal yang berturut-turut.

```bash
# Semak status log kegagalan akaun pengguna
sudo faillock --user ahmad

# Buka kunci akaun pengguna yang terkunci akibat percubaan kata laluan salah
sudo faillock --user ahmad --reset
```

Konfigurasi di `/etc/security/faillock.conf`:
```text
deny = 5
unlock_time = 900
fail_interval = 900
silent
```

---

## 📁 3. Kebenaran Fail Asas & Bit Khas (SUID, SGID, Sticky Bit)

### 3.1 Kebenaran Asas UGO (`chmod`, `chown`, `chgrp`, `umask`)

Kebenaran Linux berasaskan tiga entiti: **User (u)**, **Group (g)**, dan **Others (o)** dengan mod **Read (4)**, **Write (2)**, dan **Execute (1)**.

```bash
# Ubah pemilikan fail dan direktori kepada ahmad:sysadmin_sec
sudo chown ahmad:sysadmin_sec /srv/projek_sec/
sudo chown -R ahmad:sysadmin_sec /srv/projek_sec/

# Tetapkan kebenaran rwx untuk pemilik, r-x untuk kumpulan, dan tiada akses untuk yang lain (750)
sudo chmod 750 /srv/projek_sec/

# Tetapkan umask laluan keistimewaan selamat (027) dalam /etc/profile atau ~/.bashrc
umask 027
```

### 3.2 Bit Kebenaran Khas (SUID, SGID, Sticky Bit)

- **SUID (Set User ID - 4000 / `u+s`):** Melaksanakan fail binaan (*executable*) dengan hak keistimewaan pemilik fail (contoh: `/usr/bin/passwd`).
- **SGID (Set Group ID - 2000 / `g+s`):** Apabila ditetapkan pada direktori, semua fail baharu yang dicipta dalam direktori tersebut akan mewarisi kumpulan direktori asal.
- **Sticky Bit (1000 / `t`):** Apabila ditetapkan pada direktori kongsian (seperti `/tmp`), hanya pemilik fail sahaja yang boleh memadam fail mereka sendiri.

```bash
# Tetapkan SGID pada direktori projek kongsian
sudo chmod g+s /srv/projek_sec/

# Tetapkan Sticky Bit pada direktori kongsian umum
sudo chmod +t /srv/kongsi_awam/

# Cari fail dalam sistem yang mempunyai bit SUID ditetapkan (Audit Keselamatan)
find / -perm -4000 -type f -ls 2>/dev/null
```

---

## 🎛️ 4. Senarai Kawalan Akses POSIX (POSIX ACL - `getfacl` & `setfacl`)

Apabila kebenaran UGO tidak cukup fleksibel untuk menetapkan hak akses kepada berbilang pengguna atau kumpulan secara individu, POSIX Access Control Lists (ACL) digunakan.

```bash
# Semak ACL sedia ada pada fail/direktori
getfacl /srv/projek_sec/dokumen.pdf

# Berikan kebenaran membaca dan menulis kepada pengguna 'zarith' secara khusus
setfacl -m u:zarith:rw- /srv/projek_sec/dokumen.pdf

# Berikan kebenaran laluan (default ACL) supaya fail baharu mewarisi ACL secara automatik
setfacl -d -m u:zarith:rwx /srv/projek_sec/

# Padam semua tetapan ACL khusus pada fail
setfacl -b /srv/projek_sec/dokumen.pdf
```

---

## 🧭 5. Navigasi FHS, Pencarian Fail & Dokumentasi (`find`, `plocate`, `man-db`)

### 5.1 Hierarki Standard Sistem Fail (FHS)

- `/etc`: Fail konfigurasi sistem.
- `/var`: Data berubah (log `/var/log`, laman web `/var/www`).
- `/home`: Direktori perumah pengguna biasa.
- `/root`: Direktori perumah pengguna pentadbir.
- `/usr`: Binaan perisian dan pustaka pengguna (`/usr/bin`, `/usr/sbin`).

### 5.2 Alat Pencarian & Dokumentasi

```bash
# Kemas kini pangkalan data plocate
sudo updatedb

# Cari fail dengan pantas menggunakan plocate
plocate sudoers

# Cari fail menggunakan find mengikut saiz dan kriteria
find /var/log -type f -name "*.log" -mtime -7

# Capaian halaman panduan manual rasmi
man 5 shadow
man 8 usermod
```

---

## 🚪 6. Kawalan Keselamatan Sesi & Penutupan Selamat (`TMOUT`, `limits.conf`, `systemctl`)

### 6.1 Tamat Masa Sesi Shell Otomatik (`TMOUT`)

Bagi mengelakkan sesi terminal ditinggalkan tanpa kawalan fizikal, tetapkan pembolehubah `TMOUT` di `/etc/profile.d/timeout.sh`:

```bash
# Cipta fail skrip penguatkuasaan tamat masa sesi (15 minit / 900 saat)
cat << 'EOF' | sudo tee /etc/profile.d/timeout.sh
readonly TMOUT=900
export TMOUT
EOF
sudo chmod +x /etc/profile.d/timeout.sh
```

### 6.2 Pengurusan Had Sumber Pengguna (`/etc/security/limits.conf`)

Menghadkan bilangan proses maksima dan fail terbuka pengguna untuk mementingkan kestabilan sistem:
```text
# Mengurangkan risiko Serangan Penafian Perkhidmatan (DoS) berasaskan fork bomb dan kehabisan pemegang fail
*          hard    nproc          2048
ahmad      soft    nofile         4096
ahmad      hard    nofile         8192
```

### 6.3 Penutupan dan Ulang But Selamat

```bash
# Beritahu semua pengguna dan jadualkan penutupan sistem secara selamat
sudo shutdown -h +5 "Sistem akan ditutup untuk penyelenggaraan dalam masa 5 minit."

# Atau matikan sistem serta-merta menggunakan systemd
sudo systemctl poweroff

# Ulang but sistem serta-merta
sudo systemctl reboot
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya mencipta pengguna dan kumpulan mengikut penamaan standard NOSS.
- [ ] Mengesahkan bahawa fail `/etc/shadow` tidak boleh dibaca oleh pengguna biasa.
- [ ] Mampu mengonfigurasi privilesej `sudo` menggunakan `visudo`.
- [ ] Berjaya menetapkan kebenaran UGO, bit khas (SUID/SGID/Sticky Bit), dan POSIX ACL.
- [ ] Mampu memulihkan akaun yang terkunci dengan `faillock`.
- [ ] Mengonfigurasi `TMOUT` untuk keselamatan sesi terminal.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Apakah perbezaan mendalam antara algoritma enkrpsi SHA-512 dan Yescrypt dalam fail `/etc/shadow` pada Linux moden 2026?"*
2. *"Tunjukkan cara mengaudit keseluruhan fail binaan yang mempunyai bit SUID dan SGID serta cara menghapuskan bit keistimewaan yang tidak diperlukan."*
3. *"Tulis skrip Bash automatik untuk menyemak ketidakpatuhan kebenaran fail sistem mengikut penanda aras CIS Benchmark."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Ubuntu Server Security Handbook - User Management](https://ubuntu.com/server/docs/security-users)
- [AlmaLinux 10 Hardening Guide & PAM Faillock](https://wiki.almalinux.org/)
- [POSIX Access Control Lists in Linux - Red Hat Documentation](https://access.redhat.com/documentation/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **UNIX and Linux System Administration Handbook (5th Edition)** oleh Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley, Dan Mackin.
- **Linux Security Cookbook** oleh Daniel J. Barrett, Richard E. Silverman, Robert G. Byrnes.
- **Panduan Pentadbiran Sistem & Keselamatan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
