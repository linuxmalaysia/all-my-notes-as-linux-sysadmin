---
okf_version: 0.1
name: Bab 11 - Bahagian 1
topics: [linux, manual, references, chapter-11]
tags: [noss, dbp]
---
# Bab 11 - Bahagian 1

Gambar Rajah 164 : xpdf Beroperasi
Halaman utama xpdf mempunyai informasi tentang pilihan xpdf. Untuk melihat halaman
utama, type man xpdf di shell.
19.3.1 Untuk memancar fail PDF dengan xpdf:
1. Di meja kerja, pilih main menu > graphics > xpdf. Anda juga boleh terus ke xpdf
dengan type xpdf di shell.
2. Klik-kanan di skrin xpdf untuk melihat pilihan.
3. Pilih open untuk melihat senarai fail.
4. Pilih dokumen PDF yang anda ingin untuk pancar dan klik buka (open).
Adobe Acrobat Reader adalah lagi satu pemancar PDF yang popular. Walaupun ia tidak

berada di Red Hat Linux secara asasnya, anda boleh memuat turun aplikasi ini melalui
halaman web rasmi Adobe di http://www.adobe.com/. Anda boleh dapatkan link
untuknya di meja kerja apabila anda log masuk (login) ke sistem. Klik berganda pada
perisian pemuat tersebut dan ia akan secara automatik memuat turun Adobe Acrobat
Reader ke sistem anda.

PANDUAN PENGAJAR
Pelajaran 20: Konfigurasi Pencetak (printer)

Mukadimah:
Dalam pelajaran ini, anda akan diperkenalkan kepada proses percetakan dalam Linux.
Sebelum ini ramai beranggapan konfigurasi pencetak (printer) amat sukar dilakukan
dalam Linux, namun tanggapan itu semakin pudar. Oleh itu diharapkan pelajaran ini akan
lebih memberikan pemahaman terhadap konfigurasi pencetak (printer) dalam Linux.
Objektif:
1. Mengenali cara dan alatan konfigurasi pencetak (printer)
2. Mengenali kaedah menambah pencetak (printer) setempat (local printer)

20 KONFIGURASI PENCETAK (PRINTER CONFIGURATION)
20.1 Alatan Mengkonfigurasi Pencetak (printer)
Sebelum anda memulakan penggunaan komputer untuk mengeluarkan dokumen, anda
harus menyediakan pencetak (printer) anda dahulu. Di sini, kami akan menunjukkan anda
kaedah konfigurasi, menguji dan mengubahsuai pencetak (printer) sambungan terus ke
komputer dengan arahan printconf. (Untuk mengetahui cara konfigurasi pencetak
(printer) selain dari sambungan terus ke komputer, membentuk alias pencetak (printer)
dan sebagainya, klik butang help selepas anda melarikan aplikasi printconf)
Red Hat Linux disediakan dengan dua sistem percetakan yakni LPRng dan CUPS. LRPng
adalah sistem yang tersedia digunakan. Adalah digalakkan pengguna baru menggunakan
sistem percetakan tersedia digunakan iaitu LRPng.
Untuk menggunakan Alatan konfigurasi Pencetak (printer), anda harus mempunyai
kelebihan sebagai pengguna akar (root user). Anda boleh melancarkannya dengan salah
satu cara di bawah.
1. Dalam meja kerja grafik, klik Main Menu > System Settings > Printing
2. Dalam shell prompt (contohnya di terminal arahan) taipkan redhat-config-
printer untuk memulakan versi grafik.

Gambar Rajah 165 : Skrin konfigurasi pencetak (printer)
Jika anda ingin menambah pencetak (printer) tanpa menggunakan Alatan Konfigurasi
Pencetak (Printer Configuration Tool), sunting fail /etc/printcap.local. Jangan bimbang
jika penetapan yang anda lakukan di dalam /etc/printcap.local tidak dipaparkan di dalam
Alatan Konfigurasi Pencetak (Printer Configuration Tool) namun ia akan tetap diketahui
oleh  daemon pencetak (printer).
Di dalam Linux, untuk menambahkan pencetak (printer) adalah menambahkan baris
pencetak (printer queue) baru.
Baris pencetak (Print queue) boleh didefinisikan sebagai tempat di mana tugas mencetak
disenaraikan sedia untuk dicetak. Lima jenis queue pencetak (print queue) iaitu :-

Gambar Rajah 166 : Jenis penyenaraian pencetak (printer)

20.1.1 Local Printer
Pencetak (printer) di sambung secara terus pada komputer anda melalui parallel atau port
USB. Di dalam senarai utama pencetak (printer), Jenis queue (Queue Type) untuk
pencetak tempatan (local printer) disetkan kepada LOCAL.
20.1.2 Unix Printer (Ipd Spool)
Pencetak (printer) disambung pada sistem UNIX yang berbeza yang boleh dicapai
melalui rangkaian TCP/IP (atau contohnya, pencetak (printer) disambung kepada sistem
Linux RED HAT yang lain di dalam rangkaian anda). Di dalam senarai utama pencetak
(printer), jenis queue (queue type) untuk kawalan pencetak (printer control) UNIX diset
kepada LPD.
20.1.3 Windows Printer (SMB)
Pencetak (printer) disambung pada sistem yang berbeza di mana pencetak (printer)
dikongsi melalui rangkaian SMB (sebagai contoh, pencetak (printer) disambung kepada
mesin Microsoft Windows). Di dalam senarai utama pencetak (printer), jenis queue
(queue type) untuk kawalan pencetak (printer control) Windows diset kepada SMB.
20.1.4 Novel Printer (NCP Queue)
Pencetak (printer) disambung kepada sistem yang berbeza di mana menggunakan
teknologi rangkaian Novell¶s NetWare. Di dalam senarai utama pencetak (printer), jenis
queue (queue type) untuk kawalan pencetak (printer control) Novell diset kepada NCP.

20.1.5 JetDirect Printer
Pencetak (printer) disambungkan secara terus kepada rangkaian melalui kad
rangkaiannya sendiri (network card) dan bukan kepada komputer. Di dalam senarai
utama pencetak (printer), jenis queue (queue type) untuk pencetak (printer) JetDirect
diset kepada JetDirect.
daemon – Ini adalah program yang menjalankan sebahagian daripada tugas pengguna.
Walaupun ia hanya boleh menjalankan fungsi tertentu (seperti menguruskan baris
pencetak (print queue)), ia tidak boleh dimatikan selepas ia menjalankan tugas
tersebut. Tidak seperti arahan biasa yang boleh dimatikan selepas ia dilakukan,
daemons sentiasa aktif, menunggu untuk arahan yang lain atau data.

20.2 Menambah Pencetak Setempat (Local Printer)
Untuk menambah pencetak setempat (local printer) seperti seseorang menyambungkan
kepada port parallel atau port USB komputer anda, hanya ikut langkah mudah seperti
yang tertera di sini:
1) Klik butang New pada tetingkap Printer Configuration Tool utama. Tetingkap yang
tertera dibawah akan muncul. Klik Forward untuk diproses.
Gambar Rajah 167 : Paparan skrin penambahan pencetak (printer)

2) Masukkan nama unik untuk pencetak (printer) di dalam medan teks Queue Name.
Nama pencetak (printer) tidak boleh mengandungi ruang dan mestilah bermula
dengan huruf a sehingga z, atau A sehingga Z.
Gambar Rajah 168 : Skrin penetapan nama dan jenis pencetak (printer)
3) Printer Configuration Tool  akan cuba untuk mengesan peranti pencetak (printer
device) anda dan memaparkannya. Jika peranti pencetak (printer device) tidak
dipaparkan, klik Custom Device. Taip nama peranti pencetak (printer device) anda
dan klik OK untuk menambahkannya ke dalam senarai peranti pencetak (printer
device). Selepas memilih peranti pencetak (printer device) anda, klik Forward.

Gambar Rajah 169 : Skrin bagi mengkonfigurasi pencetak setempat (local printer)
4) Seterusnya, Printer Configuration Tool  akan cuba untuk mengesan pencetak
(printer) yang mana disambungkan ke peranti pencetak (printer device) yang anda
pilih. Jika anda mengkonfigurasikan pencetak setempat (local printer) dan model
tersebut dikesan secara automatik, pemacu (driver) yang dicadangkan secara
automatik dipilih dan ditandakan dengan asterisk (*). Jika ia mengesan pemacu
(driver) yang salah atau tidak dapat mengesan sebarang pencetak (printer), anda
boleh pilih salah satu secara manual. Pencetak (printer) dikategorikan berdasarkan
kepada pengilang atau jenama. Klik anak panah di sebelah pengilang untuk
pencetak (printer) anda. Cari pencetak (printer) anda dari senarai selebihnya, dan
klik anak panah di bawah nama pencetak (printer). Senarai pemacu (driver) untuk
pencetak (printer) anda akan keluar.

Gambar Rajah 170 : pemilihan jenis pemandu pencetak (printer)
5) Pilih salah satu. Jika anda tidak tahu yang mana satu yang akan digunakan, pilih
yang pertama di dalam senarai. Jika anda mempunyai masalah menggunakan
pemacu (driver) tersebut, edit konfigurasi pencetak (printer) di dalam printconf dan
pilih pemacu (driver) yang berbeza.

Gambar Rajah 171 : Skrin penyelesaian penambahan pencetak (printer)
6) Langkah terakhir adalah untuk mengesahkan pencetak (printer) anda. Klik Apply
jika ini adalah pencetak (printer) yang anda mahu tambah. Klik Back jika anda perlu
mengubah konfigurasi pencetak (printer) anda.
7) Pencetak (printer) baru akan muncul di dalam senarai pencetak (printer) di
tetingkap utama. Klik butang Apply di tetingkap (window) untuk menyimpan
perubahan anda pada fail konfigurasi /etc/printcap dan hidupkan semula daemon
pencetak (lpd). Selepas melakukan perubahan, cetak muka surat percubaan untuk
memastikan konfigurasi adalah betul.

Gambar Rajah 172 : Nama pencetak (printer) yang baru dipaparkan dalam skrin konfigurasi
pencetak (printer configuration)
20.2.1 Pencetak (printer) Mukasurat Percubaan
Selepas anda mengkonfigurasi pencetak (printer) anda, anda harus mencetak muka surat
percubaan untuk memastikan pencetak (printer) berfungsi dengan lancar. Untuk
mencetak muka surat percubaan, pilih pencetak (printer) yang anda mahu dari senarai dan
pilih Test > Print US Letter Postscript Test Page, Print A4 Postscript Test Page , atau
Print ASCII Test Page  dari menu menular ke bawah (pull down menu). Jika pencetak
(printer) anda tidak menyokong percetakan Postscript, pilih untuk mencetak muka surat
percubaan ASCII.
20.2.2 Mengubah Pencetak (printer) Sediaada
Untuk memadam atau membuang pencetak (printer) sedia ada . Pilih pencetak
(printer) dan klik butang Delete di atas toolbar. Pencetak (printer) tersebut akan
dipadamkan atau dibuang dari senarai pencetak (printer). Klik Apply untuk menyimpan
perubahan dan hidupkan semula daemon pencetak (printer).

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
