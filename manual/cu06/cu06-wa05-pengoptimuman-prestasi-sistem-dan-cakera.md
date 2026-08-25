---
okf_version: 0.2
type: knowledge-node
title: "Pengoptimuman Prestasi Sistem, Pemantauan Proses & Kawalan Sumber"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu06", "wa05", "ps", "top", "htop", "vmstat", "iostat", "nice", "renice", "kill", "cgroups"]
tags: ["cu06", "prestasi", "proses", "ps", "top", "htop", "vmstat", "iostat", "nice", "renice", "kill", "cgroups", "amali"]
description: "Panduan amali pemantauan proses sistem, analisis penggunaan CPU/memori/I-O, kawalan keutamaan nice/renice, penamatan isyarat proses SIGTERM/SIGKILL, dan pengurusan sumber cgroups v2."
resource: "file:///manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md"
---

# Pengoptimuman Prestasi Sistem, Pemantauan Proses & Kawalan Sumber

## 🎯 Objektif Pembelajaran

Di akhir modul amali ini, pelatih TVET/NOSS akan dapat:

1. Memantau dan menganalisis status proses sistem secara deskriptif dan interaktif menggunakan `ps aux`, `top`, `htop`, dan `pidstat`.
2. Menganalisis prestasi pemprosesan CPU, memori maya, dan statistik I/O cakera menggunakan `vmstat`, `iostat`, `free -h`, dan `uptime`.
3. Mengurus dan mengawal kitaran hayat proses termasuk hantar isyarat penamatan POSIX (`SIGTERM`, `SIGKILL`, `SIGHUP`) menggunakan `kill`, `killall`, dan `pkill`.
4. Melaraskan keutamaan penjadualan CPU proses (*nice value*) menggunakan `nice`, `renice`, dan keutamaan I/O `ionice`.
5. Melaksanakan kawalan dan penghadan sumber sistem (*resource limits*) melalui `cgroups v2` dan `systemd-run`.

> [!NOTE]
> Modul ini dipetakan secara terus kepada standard NOSS **K622-XXX-3:2026-C06 (End-User Support & System Maintenance) WA05: Perform System Optimisation and Disk Management**. Persekitaran rujukan utama ialah **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Keperluan Awal & Pra-Syarat

- Persekitaran Linux beroperasi pada **Ubuntu 26.04 LTS** atau **AlmaLinux 10**.
- Akses terminal dengan hak pentadbir (`sudo`).
- Pakej perisian terpasang: `procps`, `psmisc`, `sysstat`, `htop`, `util-linux`.

---

### 2. Pemantauan & Analisis Status Proses Sistem

#### A. Pemeriksaan Statik Menggunakan `ps`

```bash
# Paparkan kesemua proses sistem yang sedang berjalan secara terperinci
ps aux

# Paparkan struktur pokok (hierarchy tree) proses
ps axjf
# atau
pstree -p

# Filter proses khusus (contoh: proses nginx atau sshd)
ps aux | grep sshd

# Urutkan proses mengikut penggunaan memori (%MEM) atau CPU (%CPU) tertinggi
ps aux --sort=-%mem | head -n 10
ps aux --sort=-%cpu | head -n 10
```

#### B. Pemantauan Masa Nyata Menggunakan `top` dan `htop`

```bash
# Jalankan pemantauan masa nyata standard
top

# Kunci navigasi penting dalam top:
# Press 'P' -> Urutkan mengikut penggunaan CPU
# Press 'M' -> Urutkan mengikut penggunaan Memori
# Press 'k' -> Masukkan PID untuk menamatkan proses secara interaktif
# Press 'q' -> Keluar dari top

# Pemantauan masa nyata berkuasa tinggi berasaskan teks/interaktif
htop
```

---

### 3. Analisis Kesihatan Memori, CPU & I/O Cakera

#### A. Analisis Memori & Beban Purata (`free` & `uptime`)

```bash
# Semak beban purata sistem (1 minit, 5 minit, 15 minit)
uptime

# Semak ruang memori Fizikal dan Swap dalam unit yang mudah dibaca (human-readable)
free -h
```

#### B. Analisis Memori Maya & Isirung (`vmstat`)

```bash
# Paparkan statistik memori maya, swap in/out, IO, dan konteks CPU setiap 1 saat sebanyak 5 kali
vmstat 1 5
```

*Petunjuk Penting vmstat:*
- `r`: Jumlah proses yang menunggu giliran CPU (run queue).
- `b`: Jumlah proses terhalang dalam ketersediaan I/O (blocked).
- `si` / `so`: Swap-in dan Swap-out. Sekiranya angka ini sentiasa tinggi, sistem mengalami kekurangan memori RAM fizikal (*thrashing*).

#### C. Analisis Prestasi I/O Peranti Storan (`iostat` & `pidstat`)

```bash
# Menganalisis kadar pembacaan/penulisan I/O cakera secara terperinci
iostat -xz 1 5

# Semak kegunaan I/O mengikut proses spesifik
sudo pidstat -d 1 5
```

---

### 4. Pengurusan Isyarat POSIX & Penamatan Proses

Proses berkomunikasi dengan isirung kernel melalui **Isyarat POSIX (POSIX Signals)**.

#### A. Jadual Isyarat Utama POSIX

| Nombor Isyarat | Nama Isyarat | Penerangan & Tindakan |
| :---: | :--- | :--- |
| **1** | `SIGHUP` | Hangup - Digunakan untuk mengarahkan daemon memuat semula konfigurasi tanpa restart. |
| **2** | `SIGINT` | Interrupt - Dihantar apabila pengguna menekan `Ctrl + C`. |
| **9** | `SIGKILL` | Kill - Penamatan paksa sertamerta oleh kernel. **TIDAK BOLEH** ditangkap atau diabaikan oleh proses. |
| **15** | `SIGTERM` | Terminate - Isyarat penamatan anggun (graceful shutdown) lalai. Membolehkan proses menyimpan data dan menutup pautan. |

#### B. Operasi Penamatan Proses (`kill`, `killall`, `pkill`)

```bash
# Hantar isyarat penamatan anggun SIGTERM (15) berdasarkan PID
kill -15 4821

# Hantar isyarat henti paksa SIGKILL (9) jika proses tidak bertindak balas
kill -9 4821

# Hantar isyarat muat semula SIGHUP (1) kepada daemon
sudo kill -1 1024

# Menamatkan semua proses mengikut nama aplikasi
sudo killall -15 nginx
sudo pkill -f "python3 script.py"
```

---

### 5. Penalaan Keutamaan CPU & I/O (`nice`, `renice`, `ionice`)

#### A. Penalaan Keutamaan CPU (`nice` & `renice`)

Skala nilai *nice* adalah dari **-20 (Keutamaan Tertinggi)** hingga **19 (Keutamaan Terendah)**. Nilai lalai ialah **0**.

```bash
# Jalankan skrip baru dengan keutamaan CPU yang lebih tinggi (nilai nice -10) - Perlu sudo
sudo nice -n -10 /usr/local/bin/heavy-data-process.sh

# Jalankan proses latar belakang dengan keutamaan rendah (nilai nice 15)
nice -n 15 /usr/local/bin/backup.sh &

# Ubah keutamaan proses yang SEDANG berjalan mengikut PID
sudo renice -n 5 -p 4821
```

#### B. Penalaan Keutamaan I/O Cakera (`ionice`)

Class I/O: 1 (Realtime), 2 (Best-effort), 3 (Idle).

```bash
# Jalankan proses sandaran dengan kelas I/O Idle (hanya guna cakera apabila I/O kosong)
sudo ionice -c 3 /usr/local/bin/backup-job.sh
```

---

### 6. Kawalan Sumber Sistem Melalui Control Groups v2 (`cgroups v2`)

Dalam persekitaran Linux moden 2026, `cgroups v2` disepadukan secara langsung dengan `systemd` untuk mengehadkan penggunaan CPU dan memori aplikasi bagi mengelakkan sistem daripada tergantung (*system freeze*).

#### A. Membataskan Sumber Menggunakan `systemd-run`

```bash
# Jalankan aplikasi berat dengan had memori maksimum 500MB dan CPU maksimum 50%
sudo systemd-run --scope -p MemoryMax=500M -p CPUQuota=50% /usr/local/bin/heavy-app
```

#### B. Membataskan Sumber Melalui Unit Drop-in Override (`/etc/systemd/system/myapp.service.d/override.conf`)

```ini
[Service]
MemoryMax=1G
MemoryHigh=800M
CPUQuota=200%  # Mengehadkan penggunaan maksimum kepada 2 teras CPU
IOWeight=50
```

```bash
# Muat semula konfigurasi dan laksanakan
sudo systemctl daemon-reload
sudo systemctl restart myapp.service
```

---

## 🔒 Pengerasan Keselamatan & Pematuhan JDN / MAMPU

1. **Perlindungan Terhadap DoS & Fork Bomb:** Tetapkan had maksimum proses per pengguna dalam `/etc/security/limits.conf` (`nproc` & `nofile`) bagi menghalang serangan pengeluaran sumber (*resource exhaustion*).
2. **Pengawasan Proses Luar Biasa:** Pantau proses bermula dari `/tmp` atau `/dev/shm` yang kerap digunakan oleh malwer untuk melakukan perlombongan kripto (*crypto-mining*).
3. **Pemberhentian Paksa Anggun:** Sentiasa amalkan penamatan isyarat `SIGTERM (15)` terlebih dahulu sebelum menggunakan `SIGKILL (9)` bagi mengelakkan kerosakan fail pangkalan data dan sistem fail.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya memeriksa status dan menyusun proses mengikut penggunaan sumber menggunakan `ps aux`, `top`, dan `htop`.
- [ ] Berjaya menganalisis statistik kesihatan memori maya dan I/O menggunakan `vmstat`, `iostat`, dan `free -h`.
- [ ] Berjaya menamatkan proses terhang menggunakan isyarat `SIGTERM (15)` dan `SIGKILL (9)`.
- [ ] Berjaya melaraskan nilai *nice* proses dengan `nice` dan `renice`.
- [ ] Berjaya melaksanakan had penggunaan sumber CPU dan memori menggunakan `cgroups v2` atau `systemd-run`.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Apakah tanda-tanda awal memory thrashing dalam laporan vmstat dan bagaimanakah parameter sysctl vm.swappiness boleh dilaras untuk mengurangkannya?"*
2. *"Tunjukkan cara menulis skrip Shell Bash automatik untuk mengesan dan menamatkan proses yang menggunakan CPU melebihi 90% selama lebih daripada 10 minit."*
3. *"Jelaskan perbezaan mekasnisme kawalan sumber cgroups v1 dan cgroups v2 dari segi seni bina unified hierarchy dalam kernel Linux moden."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Linux Kernel Documentation - Control Groups v2](https://docs.kernel.org/admin-guide/cgroup-v2.html)
- [Ubuntu Performance Tuning & Diagnostics Guide](https://ubuntu.com/server/docs)
- [AlmaLinux 10 System Performance & Monitoring Tools](https://wiki.almalinux.org/)
- [Brendan Gregg's Linux Performance Tools & BPF](https://www.brendangregg.com/linuxperf.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Systems Performance: Enterprise and the Cloud (2nd Edition)** oleh Brendan Gregg.
- **Linux Observability with BPF** oleh David Calavera & Lorenzo Fontana.
- **Pengoptimuman & Diagnostik Prestasi Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
