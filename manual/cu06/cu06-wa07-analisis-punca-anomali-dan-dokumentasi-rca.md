---
okf_version: 0.1
type: knowledge-node
title: "Pemprosesan Teks Aluran, Saluran Paip, Editor CLI & Analisis Punca Utama (RCA)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu06", "grep", "sed", "awk", "cut", "sort", "uniq", "vim", "neovim", "nano", "sudoedit", "visudo", "rca"]
tags: ["cu06", "linux", "noss", "grep", "sed", "awk", "vim", "neovim", "nano", "sudoedit", "visudo", "rca", "standard-malaysia"]
description: "Panduan amali pemprosesan teks aluran menggunakan penapis Linux (grep, sed, awk, cut, sort, uniq), pengalihan I/O dan piping, penyuntingan fail konfigurasi selamat menggunakan Vim/Neovim, GNU Nano, sudoedit/visudo, serta dokumentasi laporan RCA."
resource: "file:///manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md"
---

# Pemprosesan Teks Aluran, Saluran Paip, Editor CLI & Analisis Punca Utama (RCA)

## 🎯 Objektif Pembelajaran

Di akhir modul amali ini, pelatih dapat:
1. Menguasai alat penapis teks berprestasi tinggi (`grep` / `ripgrep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, `tr`) untuk menganalisis fail log sistem.
2. Mengaplikasikan pengalihan I/O (`>`, `>>`, `<`, `2>&1`, `|` piping, `tee`) dan pengurusan ralat aluran skrip Bash.
3. Menyunting fail konfigurasi pentadbiran menggunakan penyunting teks CLI (**Vim / Neovim** dan **GNU Nano**) serta amalan penyuntingan selamat (`sudoedit`, `visudo`).
4. Menyediakan laporan Analisis Punca Utama (*Root Cause Analysis - RCA*) bagi insiden anomali sistem yang mematuhi standard ISO/IEC 27001 dan JDN/MAMPU.

> [!NOTE]
> Modul amali ini dipetakan kepada **NOSS CU06 (End-User Support & System Maintenance) - WA07: Resolve System Anomalies and Document RCA**. Edaran Linux rujukan merangkumi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Penapis Teks Berprestasi Tinggi (*Text Processing Utilities*)

#### A. Carian Corak dengan `grep` / `ripgrep`

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

### 3. Penyuntingan Fail Konfigurasi Terminal CLI & Amalan Keselamatan

Penyuntingan fail konfigurasi sistem memerlukan pemahaman mendalam tentang mod operasi editor CLI serta amalan keselamatan penyuntingan berhak milik `root`.

#### A. GNU Nano (Penyunting Teks Mudah & Pantas)

GNU Nano merupakan penyunting teks CLI lalai bagi kebanyakan edaran Linux.

- **Pintasan Papan Kekunci Utama**:
  - `Ctrl + O`: Menyimpan fail (*WriteOut*).
  - `Ctrl + X`: Keluar dari editor.
  - `Ctrl + W`: Carian teks (*Where Is*).
  - `Ctrl + \`: Carian dan penggantian teks (*Replace*).
  - `Ctrl + K`: Memotong (*cut*) baris semasa.
  - `Ctrl + U`: Menampal (*uncut*) baris.
  - `Alt + G` / `Ctrl + _`: Lompat ke nombor baris tertentu.

- **Konfigurasi Penyesuaian `~/.nanorc`**:
  ```ini
  # Menandakan nombor baris dan mengaktifkan penyerlahan sintaks
  set linenumbers
  set softwrap
  set tabsize 4
  set tabstospaces
  include "/usr/share/nano/*.nanorc"
  ```

#### B. Vim / Neovim (Penyunting Teks Terminal Lanjutan Pentadbir Sistem)

Vim (*Vi Improved*) dan Neovim (`nvim`) adalah standard industri untuk pengaturcaraan dan pentadbiran sistem Linux.

- **4 Mod Operasi Utama Vim**:
  1. **Mod Arahan / Normalkan (Command / Normal Mode)**: Mod sedia ada selepas membuka Vim (`Esc` untuk kembali ke mod ini).
     - Pergerakan kursor: `h` (kiri), `j` (bawah), `k` (atas), `l` (kanan), `w` (perkataan seterusnya), `b` (perkataan sebelumnya), `0` (awal baris), `$` (akhir baris), `gg` (awal fail), `G` (akhir fail).
     - Penyuntingan asas: `x` (padam aksara), `dd` (padam/potong satu baris), `yy` (salin baris), `p` (tampal selepas kursor), `u` (undo), `Ctrl + r` (redo).
  2. **Mod Sisipan (Insert Mode)**: Ditekan `i` (sisip sebelum kursor), `a` (sisip selepas kursor), `o` (buka baris baharu di bawah), `O` (buka baris baharu di atas).
  3. **Mod Visual (Visual Mode)**: Ditekan `v` (pilihan aksara), `V` (pilihan baris), `Ctrl + v` (pilihan blok lajur). Digunakan untuk menyalin/memadam blok teks.
  4. **Mod Ex / Terakhir (Ex / Command-line Mode)**: Ditekan `:` daripada Mod Arahan.
     - `:w` (simpan), `:q` (keluar), `:wq` atau `:x` (simpan dan keluar), `:q!` (keluar tanpa simpan).
     - `:set nu` (papar nombor baris), `:set nonu` (sorok nombor baris).

- **Carian & Penggantian Expression Teratur (Regex Search & Replace)**:
  Dalam Mod Ex, gunakan sintaks `%s/corak_asal/teks_baharu/g`:
  ```vim
  " Menggantikan semua perkataan 'temp' kepada 'tmp' dalam keseluruhan fail:
  :%s/temp/tmp/g

  " Menggantikan 'Port 22' kepada 'Port 2222' secara interaktif dengan pengesahan (c):
  :%s/Port 22/Port 2222/gc
  ```

- **Perekaman & Pelaksanaan Makro Vim**:
  - `qa`: Mula merekod makro ke dalam daftar `a`.
  - *(Laksanakan siri arahan penyuntingan)*.
  - `q`: Hentikan rakaman.
  - `@a`: Jalankan makro dalam daftar `a`.
  - `5@a`: Jalankan makro sebanyak 5 kali berturut-turut.

#### C. Amalan Keselamatan Penyuntingan Fail Konfigurasi Sistem (`sudoedit` & `visudo`)

Menggunakan `sudo vim` atau `sudo nano` secara terus menjalankan keseluruhan proses penyunting teks sebagai pengguna `root`. Ini mendedahkan sistem kepada risiko keistimewaan editor berlebihan (*excessive editor privilege*), contohnya melalui keupayaan *shell escape* dalam Vim (`:sh` atau `:!bash`) yang membuka kelompang `root` tanpa kawalan audit log yang jelas.

- **Menggunakan `sudoedit` (`sudo -e`)**:
  `sudoedit` melancarkan persekitaran penyunting teks di bawah akaun pengguna biasa yang tidak berkeistimewaan (*unprivileged user*) untuk menyunting salinan sementara fail. Hanya komponen `sudo` yang berkeistimewaan akan menyalin semula fail sementara itu ke lokasi sistem sasaran selepas penyuntingan diselesaikan dan fail disimpan dengan selamat.
  ```bash
  # Menyunting fail konfigurasi Rangkaian Netplan secara selamat
  sudoedit /etc/netplan/01-netcfg.yaml
  ```

- **Menggunakan `visudo` untuk Pengurusan Sudoers**:
  `visudo` mengunci fail `/etc/sudoers` secara eksklusif semasa penyuntingan dan mengesahkan sintaks secara automatik sebelum menyimpan perubahan bagi mengelakkan ralat sintaks yang boleh menyebabkan kebuntuan akses root sistem (*lockout*).
  ```bash
  # Menyunting fail sudoers dengan semakan sintaks automatik
  sudo visudo

  # Mengesahkan sintaks fail sudoers tanpa membuat perubahan
  sudo visudo -c
  ```

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
- [ ] Berjaya menyunting fail konfigurasi sistem menggunakan `vim` / `nvim` (mod operasi, regex `%s/old/new/g`, makro) dan `nano` (`.nanorc`).
- [ ] Berjaya mengamalkan penyuntingan selamat sistem menggunakan `sudoedit` dan `visudo`.
- [ ] Mampu mendokumentasikan laporan RCA rasmi bagi insiden anomali sistem.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Tunjukkan satu arahan awk sebaris (one-liner) untuk mengira jumlah saiz pemindahan fail dalam log akses Nginx."*
2. *"Bagaimanakah cara membina regex Vim untuk menggantikan semua baris ulasan (#) dalam fail sshd_config secara pukal?"*
3. *"Mengapakah penggunaan sudoedit lebih selamat berbanding sudo vim dari sudut risiko shell escape dan prinsip keselamatan least privilege?"*

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
