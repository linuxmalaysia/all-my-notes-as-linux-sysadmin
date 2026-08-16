---
okf_version: 0.1
name: Bab 6 - Bahagian 2
topics: [linux, manual, references, chapter-6]
tags: [noss, dbp]
---
# Bab 6 - Bahagian 2

anda boleh aksesnya.
Di sini ada beberapa langkah untuk akses cakera padat (CD-ROM):
Langkah 1     Penggunaan arahan “mount” untuk melampirkan cakera padat (CD-ROM)
kepada direktori sub dibina dalam Langkah 1:
# mount /dev/cdrom /mnt/cdrom
atau

# mount  /dev/hdb   /mnt/cdrom   (jika CD ROM anda dilampirkan ke
sistem sebagai ‘slave drive’ pada IDE kedua, guna /dev/hdb).
Nota: Nama alat bagi cakera padat (CD ROM) anda adalah /dev /hdb. Jika
cakera padat (CD ROM) dilampirkan ke ‘Master Drive’ atau ‘Master
Dirve pada IDE kedua, kemudian nama alat tersebut perlu menjadi
/dev/hdc.
Langkah 2 Ubah direktori ke dalam sub-direktori, dan anda boleh akses
kandungan dalam cakera padat (CD ROM):
#  ls /mnt/cdrom
Langkah 3 Cakera padat (CD ROM) adalah cakera baca sahaja (read-only), anda tidak
boleh menulis atau mengubah kandungannya. Selepas anda sudah menggunakannya, anda
perlu tidak memasangnya sebelum anda boleh mengeluarkan CD ROM tersebut dari
pemacu cakera liut (floppy disk drive) CD ROM.
# umount /mnt/cdrom
atau
# umount /dev/hdb
# eject
Nota: Butang ‘eject’ pada pemacu cakera padat (CD ROM drive) tidak akan
mengeluarkan cakera padat jika anda tidak ‘unmounted’ CD ROM dari sistem.

PANDUAN PENGAJAR
Pelajaran 16 : Teks Editor

Mukadimah:
Dalam pelajaran ini, anda akan diperkenalkan kepada teks editor popular dan berguna
dalam Linux. Teks editor sangat berguna terutamanya apabila anda bekerja di
persekitaran shell.
Objektif:
1. Mengenali teks editor emacs
2. Mengenali teks editor vim
3. Mengenali teks editor pico

16 MENGAPA TEKS EDITOR
16.1 Pengenalan Teks Editor
Mereka yang biasa dengan antara muka (interface) grafik Windows dan program moden
yang lain, akan berasa pelik apabila menggunakan teks editor. Walaupun Linux
mempunyai keupayaan grafik (kebanyakkannya aras rendah), pentadbir masih
memerlukan fail konfigurasi dengan teks. Oleh itu, pengguna harus tahu bagaimana untuk
menukar fail konfigurasi teks sistem (seperti /etc/rc.config) supaya Red Hat Linux
bekerja mengikut cara yang kita mahu.
Terdapat banyak editor yang diselitkan dalam pecahan Linux dan jadual berikut
menyenaraikan beberapa yang popular. Alatan yang disebut di sini adalah program
interaktif yang membolehkan kita sebagai pengguna Linux masukkan teks,
menggerakkan anak panah (cursor), membuka menu dan menyimpan atau mencetak fail.
Program-program berbeza dari jenis fail dan tampungan saiz fail berbeza, terhad melebihi
150MB dan kurang daripada 200,000 aksara (charactors).
Arahan Ulasan
Bluefish Editor HTML
Emacs Editor GNU Emacs untuk konsol dan X11
jed, xjed Editor pengatur cara untuk konsol dan X11
joe, jmacs, jpico, jstar Editor Joe dan kesesuaian editor lain mengikut Joe
Jove Editor Emacs Jonathan
Kedit Teks Editor untuk KDE
Lyx Editor Latex berdasarkan WYSIWYG untuk X11
Nvi Editor klon vi dari Berkeley
Pico Editor fail untuk 200 baris sahaja
Red Editor baca sahaja
Sed Editor aluran

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
