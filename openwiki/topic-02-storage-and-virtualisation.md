---
okf_version: 0.2
type: documentation
title: "Topik 2: Pengurusan Storan, Partisi & Pengmayaan (CU02) — Dikemaskini 2026"
timestamp: "2026-08-17T00:00:00Z"
topics: ["storage", "virtualisation", "cu02", "gpt", "lvm2", "ext4", "xfs", "btrfs", "kvm"]
tags: ["linux", "storage", "virtualisation", "cu02", "partisi", "gdisk", "lvm", "luks2"]
description: "Silibus pengurusan storan fizikal/logikal (GPT, LVM2, EXT4/XFS/Btrfs, LUKS2) dan pengmayaan (KVM/QEMU/libvirt) Linux dipetakan kepada NOSS CU02."
resource: "file:///openwiki/topic-02-storage-and-virtualisation.md"
---

# Topik 2: Pengurusan Storan & Pengmayaan (CU02)

## Gambaran Keseluruhan (Overview)

Topik ini merangkumi pengurusan ruang storan fizikal dan logikal (*disk management*), skema partisi GPT moden, Pengurusan Volum Logikal (**LVM2**), sistem fail moden (**EXT4**, **XFS**, **Btrfs**), penyulitan **LUKS2**, serta infrastruktur pemayaan (*virtualisation*) berprestasi tinggi di persekitaran Linux. Topik ini dipetakan secara terus kepada piawaian **NOSS Level 3 (CU02: Virtualisation Infrastructure & Storage Management)**.

> **💡 Kemahiran Kognitif - Peningkatan Tahap Pengabstrakan:**
> Daripada sekadar "mencipta partisi dan format cakera" (spesifik) → fahami "bagaimana pangkalan data dan hipervisor menguruskan volum storan secara dinamis dan tersulit" (corak) → hayati "apakah peranan ketahanan data dan fleksibiliti storan dalam seni bina awan sovereign" (prinsip universal).

---

## Silibus Utama

### 1. Pengurusan Storan Fizikal & Jadual Partisi GPT

- Pemerhatian peranti blok: `lsblk`, `blkid`, `df -hT`
- Perbandingan MBR (Legacy) vs **GPT (GUID Partition Table)** moden
- Pembahagian partisi GPT menggunakan `gdisk` (interaktif) dan `parted` (skrip)

**📖 Baca Lanjut:** [manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md](../manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md)

### 2. Pengurusan Volum Logikal LVM2 (Logical Volume Management)

- Hierarki LVM2: *Physical Volume* (PV) ➔ *Volume Group* (VG) ➔ *Logical Volume* (LV)
- Arahan pembinaan: `pvcreate`, `vgcreate`, `lvcreate`
- Peluasan volum secara dalam talian (*online volume expansion*): `lvextend` dan `resize2fs` / `xfs_growfs`

**📖 Baca Lanjut:** [manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md](../manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md)

### 3. Sistem Fail Moden (EXT4, XFS, Btrfs) & Pautan Kekal `/etc/fstab`

- Perbandingan prestasi dan kegunaan EXT4 (Desktop/Linux am), XFS (Enterprise Pelayan AlmaLinux 10), dan Btrfs (Snapshot/Fedora 43)
- Arahan format: `mkfs.ext4`, `mkfs.xfs`, `mkfs.btrfs`
- Konfigurasi lekap kekal di `/etc/fstab` menggunakan `UUID` dan parameter `nofail`

**📖 Baca Lanjut:** [manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md](../manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md)

### 4. Penyulitan Storan Blok LUKS2 Pejabat

- Konfigurasi LUKS2 (`cryptsetup luksFormat --type luks2`)
- Pembukaan dan pemetaan volum tersulit di `/dev/mapper/`
- Pematuhan piawaian ISO/IEC 27001 & Pekeliling Am Jabatan Digital Negara (JDN) / MAMPU

**📖 Baca Lanjut:** [manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md](../manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md)

### 5. Infrastruktur Pemayaan (KVM Type-1 Hypervisor & Type-2 Desktop Products)

- Konsep **KVM (Kernel-based Virtual Machine)** sebagai **Hipervisor Jenis-1 (Type-1 / Bare-Metal)** yang terintegrasi secara langsung ke dalam isirung Linux, berbeza daripada produk Type-2 berasaskan OS hos seperti VirtualBox
- Pengurusan mesin maya tetamu (*Guest VMs*) menggunakan `QEMU`, `libvirt`, `virsh`, dan `virt-manager`
- Penyediaan rekod konfigurasi pemayaan dan pengasingan rangkaian maya (*virtual networks*)

**📖 Baca Lanjut:** [manual/cu02/cu02-wa01-keperluan-infrastruktur-pemayaan.md](../manual/cu02/cu02-wa01-keperluan-infrastruktur-pemayaan.md)

---

## Pemetaan NOSS & Agent Skills (NOSS Mapping)

| Kod NOSS | Nama Aktiviti Kerja | Status Modul & Skill |
|----------|----------------------|----------------------|
| **CU02-WA01** | Keperluan Infrastruktur Pemayaan & Storan | [Lihat Skill](../.agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md) |
| **CU02-WA02** | Pemasangan Hipervisor Jenis-2 | [Lihat Skill](../.agents/skills/cu02-wa02-install-type-2-hypervisor-platform/SKILL.md) |
| **CU02-WA03** | Penyebaran Mesin Maya Tetamu (VM) | [Lihat Skill](../.agents/skills/cu02-wa03-deploy-guest-virtual-machines-vm/SKILL.md) |
| **CU02-WA04** | Penyediaan Rekod Konfigurasi Pemayaan | [Lihat Skill](../.agents/skills/cu02-wa04-prepare-virtualisation-configuration-records/SKILL.md) |

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

Gunakan *prompt* berikut bersama AI (seperti ChatGPT, Claude, atau Gemini) untuk mendalami topik ini:
1. > "Bolehkah anda jelaskan perbezaan antara sistem fail EXT4, XFS, dan Btrfs dari segi sokongan saiz maksimum, kecekapan I/O, dan kebolehan salinan snapshot?"
2. > "Tuliskan skrip Bash untuk membina susunan LVM2 secara automatik berasaskan dua peranti blok baharu, memformatnya ke XFS, dan memasangnya ke /mnt/data dengan tetapan UUID dalam /etc/fstab."
3. > "Bagaimanakah cara meluaskan saiz Logical Volume (LV) LVM2 dan sistem fail XFS secara dalam talian (online expansion) tanpa perlu menghentikan mesin maya (VM)?"
4. > "Apakah perbezaan seni bina antara KVM (Kernel-based Virtual Machine) sebagai Type-1 Hypervisor dengan Type-2 Hypervisor seperti VirtualBox dalam persekitaran pelayan perusahaan?"

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi LVM2 Red Hat / AlmaLinux 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/)
- [Panduan GNU Parted & GPT Partition Table](https://www.gnu.org/software/parted/)
- [Dokumentasi Btrfs Wiki Documentation](https://btrfs.readthedocs.io/)
- [Dokumentasi KVM & Libvirt Virtualization](https://libvirt.org/)
- [Pekeliling Keselamatan ICT Jabatan Digital Negara (JDN) / MAMPU](https://www.jdn.gov.my/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

Jika anda ingin membina pemahaman yang lebih mendalam, berikut adalah senarai buku yang disyorkan:

**Bahasa Melayu:**
1. *Asas Pentadbiran Storan & Pelayan Linux* oleh Harisfazillah Jamel — Panduan amali pengurusan storan dan sistem fail dalam persekitaran Malaysia.
2. *Panduan Amali Virtualisasi KVM Linux* — Buku latihan amali mesin maya dan LVM.

**English (Antarabangsa):**
1. *UNIX and Linux System Administration Handbook, 5th Edition* oleh Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley, Dan Mackin — Kitab rujukan utama pentadbiran storan dan sistem.
2. *Storage Systems: Organization, Performance, Coding, Reliability, and Statistics* oleh Alexander Thomasian — Rujukan mendalam seni bina storan enterprise.
3. *Mastering KVM Virtualization* oleh Prasad Mukhedkar, Anil Vettattu, Humble Chirammal — Panduan lengkap hipervisor KVM dan libvirt.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
