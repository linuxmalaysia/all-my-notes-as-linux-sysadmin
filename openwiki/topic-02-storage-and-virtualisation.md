---
name: topic-02-storage-and-virtualisation
description: Silibus pengurusan storan dan mesin maya (KVM) Linux dipetakan kepada NOSS CU02.
tags:
  - linux
  - storage
  - virtualisation
  - cu02
topics:
  - Disk Partitioning
  - Virtual Machines
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
