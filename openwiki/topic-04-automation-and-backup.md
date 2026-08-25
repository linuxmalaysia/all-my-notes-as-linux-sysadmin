---
okf_version: 0.1
type: documentation
title: "Topik 4: Automasi Skrip, Sandaran Data & Pemulihan Sistem (CU04)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["bash-scripting", "backup", "recovery", "cu04", "tar", "rsync", "zstd", "cron", "systemd-timer"]
tags: ["linux", "backup", "scripting", "cu04", "recovery", "zstd", "rsync", "noss"]
description: "Silibus automasi skrip Bash, pengarkiban dan pemampatan tar/zstd, penyegerakan rsync, automasi berkala cron/systemd-timer, dan pemulihan data dipetakan kepada NOSS CU04."
resource: "file:///openwiki/topic-04-automation-and-backup.md"
---

# Topik 4: Automasi Skrip, Sandaran Data & Pemulihan Sistem (CU04)

## 📌 Overview (Gambaran Keseluruhan)
Sistem Linux terkenal dengan keupayaan automasi dan keutuhan integriti data. Topik ini merangkumi pengarkiban moden, penyegerakan direktori pintar, automasi pemasa berjadual, serta strategi pemulihan data dan bencana. Dipetakan daripada **NOSS CU04 (Backup & Recovery Tools)**.

---

## 📚 Silibus Utama
1. **Pengarkiban & Pemampatan Data Moden (Archiving & Compression)**:
   - Utiliti pengarkiban `tar`.
   - Pemampat moden berprestasi tinggi `zstd` (*Zstandard multi-threaded*), `xz`, `gzip`, dan `bzip2`.
   - Menjalankan penyulitan arkib tersulit `gpg` (AES-256) mengikut garis panduan JDN/MAMPU.
2. **Penyegerakan Data Pintar (Incremental Synchronization)**:
   - Penggunaan `rsync` untuk penyegerakan direktori tempatan dan rangkaian (`rsync -avzP --delete-after`).
   - Penerapan Strategi Sandaran **3-2-1** (3 salinan, 2 media, 1 offsite) & pematuhan ISO/IEC 27001.
3. **Automasi Penjadualan Tugasan (Job Scheduling)**:
   - Automasi `cron` dan penyuntingan jadual menerusi `crontab -e`.
   - Automasi moden berasaskan unit `systemd.service` dan `systemd.timer`.
4. **Pemulihan Data & Verifikasi Integriti (Recovery & Verification)**:
   - Pengesahan integriti checksum cryptographic `sha256sum`.
   - Pengekstrakan data terpilih (*selective restoration*) daripada arkib termampat.
   - Prosedur dan alur kerja pemulihan bencana sistem *bare-metal*.

---

## 🗺️ Pemetaan Modul Amali & Kemahiran AI (NOSS Mapping)

Silibus ini memandu modul amali di `manual/cu04/` dan kemahiran AI di `.agents/skills/`:

- `manual/cu04/cu04-wa01-persediaan-alatan-sandaran-dan-pemulihan.md` ➔ `.agents/skills/cu04-wa01-prepare-backup-recovery-tools/`
- `manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md` ➔ `.agents/skills/cu04-wa02-perform-local-backup-operations/`
- `manual/cu04/cu04-wa03-sandaran-berasaskan-rangkaian.md` ➔ `.agents/skills/cu04-wa03-perform-network-based-backup/`
- `manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md` ➔ `.agents/skills/cu04-wa04-restore-endpoint-data/`
- `manual/cu04/cu04-wa05-pemulihan-bare-metal-endpoint.md` ➔ `.agents/skills/cu04-wa05-perform-endpoint-bare-metal-recovery/`

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Apakah perbezaan kelajuan dan kecekapan nisbah mampatan antara tar -I zstd berbanding tar -czvf bagi fail bersaiz besar?"*
2. *"Bagaimanakah cara membina skrip Bash automasi sandaran rsync yang menghantar makluman kegagalan terus ke log systemd journalctl?"*
3. *"Tunjukkan kaedah mengesahkan fail sha256sum secara berkelompok sebelum melancarkan proses pemulihan data pelayan."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [GNU Tar Official Manual](https://www.gnu.org/software/tar/manual/)
- [Zstandard Compression Algorithm Guide](https://facebook.github.io/zstd/)
- [Rsync Documentation & User Manual](https://rsync.samba.org/)
- [Systemd Timers Documentation](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Administration Handbook** oleh Evi Nemeth et al.
- **Automating Linux with Bash and Python** oleh R. W.
- **Panduan Praktikal Sandaran & Automasi Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
