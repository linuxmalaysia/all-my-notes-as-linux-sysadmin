---
okf_version: 0.1
type: documentation
title: "topic-02-storage-and-virtualisation"
timestamp: "2026-08-16T08:43:42Z"
topics: ["storage", "virtualisation", "cu02"]
tags: ["linux", "storage", "virtualisation", "cu02"]
description: "Silibus pengurusan storan dan mesin maya (KVM) Linux dipetakan kepada NOSS CU02."
resource: "file:///openwiki/topic-02-storage-and-virtualisation.md"
---

# Topik 2: Pengurusan Storan & Pengmayaan (CU02)

## Overview (Gambaran Keseluruhan)
Topik ini meliputi pengurusan ruang storan keras (disk management) serta pengenalan kepada konsep infrastruktur maya di persekitaran Linux. Ia dipetakan daripada **CU02 (Virtualisation Infrastructure)**.

## Silibus Utama
1. **Pengurusan Storan Fizikal & Logikal**:
   - Arahan pemerhatian storan: `lsblk`, `df -h`, `du -sh`
   - Pemisahan cakera (Partitioning): `fdisk`, `parted`
   - Membina sistem fail (Filesystem): `mkfs.ext4`, `mkfs.xfs`
   - LVM (Logical Volume Management): `pvcreate`, `vgcreate`, `lvcreate`
2. **Mounting & Fstab**:
   - Pemasangan storan manual: `mount` dan `umount`
   - Tetapan kekal di `/etc/fstab`
3. **Pengmayaan (Virtualisation)**:
   - Hypervisor Type-2 & KVM (Kernel-based Virtual Machine).
   - Penggunaan QEMU, `libvirt`, dan Virtual Machine Manager.

## Pemetaan NOSS (NOSS Mapping)
Silibus ini adalah persediaan kepada kemahiran Ejen AI:
- `cu02-wa02-install-type-2-hypervisor-platform`
- `cu02-wa03-deploy-guest-virtual-machines-vm`

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
