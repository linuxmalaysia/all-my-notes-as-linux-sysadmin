---
okf_version: 0.1
type: knowledge-node
title: "Pemprosesan Teks Aluran, Saluran Paip, Editor CLI & Analisis Punca Utama (RCA)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu06", "grep", "sed", "awk", "cut", "sort", "uniq", "vim", "nano", "rca"]
tags: ["cu06", "linux", "noss", "grep", "sed", "awk", "vim", "nano", "rca", "standard-malaysia"]
description: "Panduan amali pemprosesan teks aluran menggunakan penapis Linux (grep, sed, awk, cut, sort, uniq), pengalihan I/O dan piping, penyuntingan fail konfigurasi menggunakan vim/nano, serta dokumentasi laporan RCA."
resource: "file:///manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md"
---

# Pemprosesan Teks Aluran, Saluran Paip, Editor CLI & Analisis Punca Utama (RCA)

## 🎯 Objektif Pembelajaran
Di akhir modul amali ini, pelatih dapat:
1. Menguasai alat penapis teks berprestasi tinggi (`grep` / `ripgrep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, `tr`) untuk menganalisis fail log sistem.
2. Mengaplikasikan pengalihan I/O (`>`, `>>`, `<`, `2>&1`, `|` piping, `tee`) dan pengurusan ralat aluran skrip Bash.
3. Menyunting fail konfigurasi pentadbiran menggunakan penyunting teks CLI (`vim` dan `nano`).
4. Menyediakan laporan Analisis Punca Utama (*Root Cause Analysis - RCA*) bagi insiden anomali sistem yang mematuhi standard ISO/IEC 27001 dan JDN/MAMPU.

> [!NOTE]
> Modul amali ini dipetakan kepada **NOSS CU06 (End-User Support & System Maintenance) - WA07: Resolve System Anomalies and Document RCA**. Edaran Linux rujukan merangkumi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Penapis Teks Berprestasi Tinggi (*Text Processing Utilities*)

#### A. carian Corak dengan `grep` / `ripgrep`
```bash
# Mencari ralat 'FAILED' dalam auth.log tanpa mengira huruf besar/kecil (-i) beserta nombor baris (-n)
grep -in "failed" /var/log/auth.log

# Mengira jumlah percubaan log masuk gagal
grep -c "Failed password" /var/log/auth.log
```

#### B. Pemprosesan Jalur & Pengasingan Medan (`cut`, `sort`, `uniq`, `wc`)
```bash
# Ekstrak senarai alamat IP daripada log percubaan SSH gagal, susun, dan kira frekuensi
grep "Failed password" /var/log/auth.log | cut -d' ' -f11 | sort | uniq -c | sort -nr
```

#### C. Editor Aluran & Bahasa Pemprosesan Corak (`sed` & `awk`)
```bash
# sed: Menggantikan teks secara aluran (contoh: tukar Port 22 ke 2222 dalam sshd_config)
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# awk: Menganalisis log dan memaparkan medan khusus (Contoh: Cetak Kolom 1 dan Kolom 5 dari log)
awk '{print $1, $5}' /var/log/syslog | head -n 10
```

---

### 2. Pengalihan Input/Output (I/O Redirection) & Saluran Paip (*Piping*)

| Operator | Penerangan & Kegunaan |
| :--- | :--- |
| `>` | Mengalih keluaran standard (stdout) ke fail (menimpa kandungan). |
| `>>` | Mengalih keluaran standard (stdout) ke fail secara tambahan (*append*). |
| `<` | Mengalih input standard (stdin) daripada fail. |
| `2>&1` | Mengalih ralat standard (stderr) ke saluran stdout. |
| `\|` | Saluran paip (*pipe*) - menyambungkan stdout arahan pertama ke stdin arahan kedua. |
| `tee` | Memaparkan stdout di skrin terminal serentak menulis ke fail. |

```bash
# Menyimpan ralat sistem secara bersama ke fail log dan skrin
sudo systemctl status nginx 2>&1 | tee /tmp/nginx_error_audit.log
```

---

### 3. Penyuntingan Fail Konfigurasi CLI (`vim` & `nano`)

#### A. Penyunting Teks `nano` (Mesra Pemula):
- `Ctrl + O`: Menyimpan fail (*WriteOut*).
- `Ctrl + X`: Keluar dari editor.
- `Ctrl + W`: Carian teks.

#### B. Penyunting Teks `vim` (Standard Pentadbir Sistem):
- **Mod Arahan (Command Mode)**:
  - `i`: Masuk ke Mod Sisipan (*Insert Mode*).
  - `dd`: Memadam satu baris.
  - `yy` / `p`: Menyalin baris / Menampal baris.
  - `/paten`: Carian teks ke hadapan.
- **Mod Ex / Terakhir (Ex Mode)**:
  - `:w`: Menyimpan fail.
  - `:q!`: Keluar tanpa menyimpan.
  - `:wq` / `:x`: Menyimpan dan keluar.

---

### 4. Penyediaan Laporan Analisis Punca Utama (*Root Cause Analysis - RCA*)

Apabila anomali sistem diselesaikan, pentadbir wajib menyediakan dokumen RCA berformat OKF v0.1:

#### Format Laporan RCA Standard JDN/MAMPU:
1. **Ringkasan Insiden**: Tarikh, masa, dan perkhidmatan yang terjejas.
2. **Kronologi Kejadian**: Urutan garis masa dikesan menerusi log (`journalctl`, `syslog`).
3. **Punca Utama (*Root Cause*)**: Hasil analisis pemprosesan teks log (`grep`/`awk`).
4. **Tindakan Pembaikan**: Langkah pembetulan amali yang diambil.
5. **Langkah Pencegahan**: CADANGAN automasi atau pengerasan keselamatan agar insiden tidak berulang.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Berjaya menapis dan menganalisis log menggunakan `grep`, `sed`, `awk`, `cut`, `sort`, dan `uniq`.
- [ ] Berjaya menggunakan operator pengalihan I/O (`>`, `>>`, `2>&1`, `|`, `tee`) dalam aluran skrip Bash.
- [ ] Berjaya menyunting fail konfigurasi sistem menggunakan `vim` dan `nano`.
- [ ] Mampu mendokumentasikan laporan RCA rasmi bagi insiden anomali sistem.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Tunjukkan satu arahan awk sebaris (one-liner) untuk mengira jumlah saiz pemindahan fail dalam log akses Nginx."*
2. *"Apakah perbezaan antara sed -i (in-place) dengan penyuntingan menerusi paip aluran?"*
3. *"Berikan templat laporan RCA (Root Cause Analysis) ringkas bagi insiden kegagalan perkhidmatan disebabkan kehabisan nod i-node pada sistem fail."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [GNU Sed User Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [GNU Awk User's Guide](https://www.gnu.org/software/gawk/manual/gawk.html)
- [Vim Cheat Sheet & Interactive Tutor](https://vim.rtorr.com/)
- [SRE Incident Management & RCA Guidelines by Google](https://sre.google/sre-book/postmortem-culture/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Sed & Awk (2nd Edition)** oleh Dale Dougherty & Arnold Robbins.
- **Learning the vi and Vim Editors** oleh Arnold Robbins & Elbert Hannah.
- **Analisis Log & RCA Sistem Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
