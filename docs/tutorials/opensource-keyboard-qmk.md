---
okf_version: 0.1
type: tutorial
title: "Tutorial Interaktif: Eksplorasi Papan Kekunci Sumber Terbuka (QMK & OSHW)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["opensource-keyboard", "qmk-firmware", "qmk-configurator", "oshw", "open-source-hardware", "input-devices"]
tags: ["qmk", "oshw", "keyboard", "tutorial", "custom-keyboard", "firmware", "linux"]
description: "Panduan amali dan interaktif meneroka papan kekunci sumber terbuka (Open-Source Hardware), firmawer QMK, dan mereka bentuk susun atur kekunci tersuai menggunakan QMK Configurator di Linux."
resource: "file:///docs/tutorials/opensource-keyboard-qmk.md"
---

# Tutorial Interaktif: Eksplorasi Papan Kekunci Sumber Terbuka (QMK & OSHW)

## 🌟 Objektif Pembelajaran

Dalam tutorial amali ini, anda akan:
1. **Memahami Konsep Perkakasan Sumber Terbuka (OSHW):** Bagaimana reka bentuk fizikal, skematik PCB, fail CAD, dan *Bill of Materials* (BOM) dikongsi secara bebas.
2. **Mengenali Ekosistem QMK (Quantum Mechanical Keyboard):** Memahami peranan QMK Firmware, QMK Configurator, QMK Toolbox, dan komuniti [qmk.fm](https://qmk.fm/).
3. **Mereka Bentuk Papan Kekunci Tersuai (Custom Keyboard Layout):** Menggunakan QMK Configurator secara interaktif untuk mencipta lapisan kekunci (*layers*), makro, dan *keycodes* khas.
4. **Menyediakan Persekitaran Linux untuk Flashing:** Mengkonfigurasi peraturan `udev` pada edaran Linux (Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10) bagi membolehkan pemprosesan firmawer peranti USB dengan selamat.

---

## 🛠️ Modul 1: Apa itu Perkakasan Sumber Terbuka (Open-Source Hardware - OSHW)?

**Perkakasan Sumber Terbuka (OSHW)** ialah satu gerakan sosial dan teknologi di mana reka bentuk perkakasan fizikal—seperti skematik litar, fail reka bentuk berbantu komputer (CAD), papan litar bertercetak (PCB layout), dan senarai bahan ramuan (*Bill of Materials* - BOM)—disediakan secara awam supaya sesiapa sahaja boleh mempelajari, mengubah suai, membina, dan mengedarkannya semula.

```
       [ Skematik Litar PCB ]  +  [ Fail 3D CAD Kesing ]
                                 │
                                 ▼
                     [ Bill of Materials (BOM) ]
                                 │
                                 ▼
               [ Lesen Sumber Terbuka (OSHW / CERN / TAPR) ]
                                 │
                                 ▼
         ┌──────────────────────────────────────────────┐
         │ Pengguna Bebas Menyemak, Membina, Ubah Suai &│
         │          Mengedarkan Perkakasan Fizikal      │
         └──────────────────────────────────────────────┘
```

Pergerakan ini memberikan kebebasan penuh kepada komuniti pengkomputeran dan peminat *custom keyboard* untuk membina perkakasan sendiri tanpa bergantung kepada kunci (*lock-in*) vendor proprietari.

---

## 🎹 Modul 2: Apakah itu QMK Firmware?

**QMK (Quantum Mechanical Keyboard)** ialah sebuah komuniti sumber terbuka yang berteraskan pembangunan peranti input komputer. Komuniti ini merangkumi pelbagai jenis peranti input seperti papan kekunci mekanikal, tetikus, dan peranti MIDI.

Kumpulan kolaborator utama memelihara:
- **QMK Firmware:** Komponen tegar (*firmware*) berasaskan C untuk mikropengawal (seperti ATmega32U4, RP2040, STM32).
- **QMK Configurator:** Antara muka web visual untuk mereka bentuk susun atur (*layout*) tanpa perlu menulis kod C secara manual.
- **QMK Toolbox:** Utiliti GUI untuk muat naik (*flashing*) firmawer ke peranti.
- **qmk.fm & Dokumentasi Rasmi:** Pusat rujukan komuniti di [docs.qmk.fm](https://docs.qmk.fm/).

---

## 🚀 Modul 3: Latihan Amali Interaktif — Mereka Bentuk Papan Kekunci di QMK Configurator

Latihan ini direka untuk menyemarakkan semangat anda dalam meneroka keupayaan pengaturcaraan papan kekunci fizikal secara grafik!

### Langkah 1: Buka QMK Configurator
Buka pelayar web pilihan anda (seperti Mozilla Firefox atau Chromium di Linux) dan layari:
👉 **[https://config.qmk.fm](https://config.qmk.fm)**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          QMK CONFIGURATOR                               │
│  Keyboard: [ Keychron / V1              ▼ ]   Layout: [ ANSI        ▼ ] │
│  Keymap Name: [ my_custom_keyboard_v1                                ] │
└─────────────────────────────────────────────────────────────────────────┘
```

### Langkah 2: Pilih Model Papan Kekunci
1. Pada ruangan **Keyboard**, pilih papan kekunci kegemaran atau sasaran anda (contohnya `keychron/v1/ansi`, `clueboard/66/rev2`, atau `crkbd` / Corne Split Keyboard).
2. Perhatikan paparan visual susun atur kekunci (*keyboard layout*) yang muncul di skrin.

### Langkah 3: Meneroka & Mereka Bentuk Lapisan Kekunci (Layers)
Papan kekunci QMK menyokong konsep **Lapisan (Layers)**. Lapisan 0 ialah lapisan asas (huruf standard). Lapisan 1 dan 2 boleh diaktifkan menggunakan kekunci fungsi khas untuk mengakses simbol, pad nombor, kawalan media, atau navigasi anak panah!

1. **Memilih Lapisan 0 (Base Layer):**
   - Tetapkan susun atur huruf standard (QWERTY / DVORAK / COLEMAK).
2. **Pindah ke Lapisan 1 (Layer 1 - Symbol & Navigation):**
   - Klik pada butang **Layer 1**.
   - Pada bahagian bawah panel *Keycodes*, pilih kategori **Quantum** atau **Layer Switching**.
   - Heret (*drag and drop*) kekunci `MO(1)` (Momentary Switch Layer 1) ke kekunci `Caps Lock` atau `Space` pada Lapisan 0.
   - Pada Lapisan 1, gantikan kekunci `H, J, K, L` dengan anak panah `LEFT, DOWN, UP, RIGHT` (gaya Vim editor!).
3. **Menambah Kawalan Kecerahan & Media:**
   - Letakkan `KC_MUTE`, `KC_VOLU`, `KC_VOLD`, dan kawalan lampu RGB pada Lapisan 1.

### Langkah 4: Mengeksport & Membina Firmawer
1. Klik butang **Save Preset** atau **Export JSON** untuk menyimpan fail reka bentuk `.json` anda sebagai sandaran.
2. Klik butang **Compile** (ikon tukul/dapur binaan). Beruang QMK akan mula memasak (*compiling*) firmawer anda di awan!
3. Setelah selesai, klik **Download Firmware** untuk memuat turun fail binari (`.hex`, `.bin`, atau `.uf2`).

---

## 💻 Modul 4: Persediaan Persekitaran Linux (Ubuntu / Fedora / AlmaLinux) untuk Flashing

Untuk memasukkan firmawer baharu ke dalam peranti tanpa memerlukan akses `sudo` setiap kali, kita perlu menetapkan peraturan `udev` khas untuk peranti USB QMK.

### Langkah 1: Pasang Utiliti & Peraturan Udev QMK
Buka Terminal Linux anda dan laksanakan arahan berikut:

```bash
# Kemaskini repositori pakej
sudo apt update || sudo dnf check-update

# Pasang git dan python3
sudo apt install -y git python3-pip || sudo dnf install -y git python3-pip

# Muat turun peraturan udev rasmi QMK
cat << 'EOF' | sudo tee /etc/udev/rules.d/50-qmk.rules
# QMK / DFU / Caterpillar Bootloaders
SUBSYSTEMS=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ff4", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ff0", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="0478", MODE="0666"
# Raspberry Pi RP2040 Bootloader (UF2)
SUBSYSTEMS=="usb", ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="0003", MODE="0666"
EOF

# Muat semula peraturan udev
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### Langkah 2: Flashing menggunakan QMK CLI atau QMK Toolbox
Di Linux, anda boleh menggunakan **QMK CLI** secara terus melalui sokongan Python:

```bash
# Pasang QMK CLI melalui pip/uv
python3 -m pip install --user qmk

# Sahkan pemasangan QMK CLI
qmk --version

# Muat naik firmawer ke papan kekunci dalam mod bootloader
# (Tekan butang Reset pada papan kekunci mekanikal anda)
qmk flash my_custom_keyboard.hex
```

---

## 🎯 Kesimpulan & Cabaran Amali Komuniti

Dengan menguasai QMK dan OSHW, anda bukan sahaja sekadar pengguna papan kekunci, malah anda adalah **pereka bentuk perkakasan dan perisian** bagi stesen kerja pengkomputeran anda sendiri!

**🔥 Cabaran Amali Kreatif:**
1. Reka satu susun atur kekunci di QMK Configurator yang mempunyai kekunci makro pintasan untuk arahan terminal Linux popular (seperti `sudo apt update && sudo apt upgrade -y`).
2. Eksport fail JSON konfigurasi anda dan kongsi bersama komuniti peminat Linux & OSHW tempatan!

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

Gunakan *prompt* berikut bersama AI untuk mendalami topik ini:
1. > "Tunjukkan contoh skrip C firmawer QMK untuk menetapkan fungsi 'Tap-Dance' di mana menekan kekunci A sekali menghasilkan huruf 'a', manakala menekan dua kali dengan pantas menghasilkan simbol '@'."
2. > "Bagaimanakah cara menambah sokongan paparan skrin OLED (SSD1306) dan pemutar berputar (rotary encoder) pada papan kekunci split tersuai dalam QMK Firmware?"
3. > "Jelaskan perbezaan antara mikropengawal AVR ATmega32U4 dan RP2040 dari segi memori flash, prestasi, dan keserasian dengan QMK Firmware."

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Rasmi QMK Firmware](https://docs.qmk.fm/)
- [QMK Configurator Web App](https://config.qmk.fm/)
- [Pernyataan Rasmi Open Source Hardware Association (OSHWA)](https://www.oshwa.org/definition/)
- [Repositori Kod Sumber QMK Firmware di GitHub](https://github.com/qmk/qmk_firmware)
- [Panduan Peraturan Udev Linux untuk QMK](https://docs.qmk.fm/cli_installation#udev-rules)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

1. *Building Custom Mechanical Keyboards: Design, Assembly, and Firmware Programming* — Panduan komprehensif membina papan kekunci mekanikal fizikal dari awal.
2. *Open-Source Hardware Documentation and Licensing* oleh OSHWA — Panduan pelesenan dan pembuatan dokumen fizikal OSHW.
3. *Practical Electronics for Inventors, 4th Edition* oleh Paul Scherz & Simon Monk — Rujukan asas rekabentuk litar elektronik dan mikropengawal.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
