---
okf_version: 0.1
name: Bab 12 - Bahagian 1
topics: [linux, manual, references, chapter-12]
tags: [noss, dbp]
---
# Bab 12 - Bahagian 1

Untuk mengubah tetapan pencetak diimport (imported printer’s setting).
Anda tidak boleh mengubah tetapan (setting) secara terus. Anda harus mengatasi
pencetak (printer) tersebut. Anda hanya boleh mengatasi tetapan pencetak (printer
setting) yang telah diimport menggunakan alchemist library . Pencetak (printer) yang
diimport ada simbol di sebelahnya dalam jalur yang pertama dari senarai pencetak
(printer).
Untuk mengatasi pencetak (printer) tersebut, pilih pencetak (printer) itu dan pilih File >
Override Queue  dari menu menular ke bawah (pull down menu). Selepas mengatasi
pencetak (printer) tersebut, pencetak (printer) diimport asal akan mempunyai simbol di
sebelahnya dalam jajar pertama senarai pencetak (printer).
Klik di atas ikon pencetak (printer) tersebut dan klik edit pada menu di atas. Ia
mempunyai nilai sedia ada untuk diubah. Klik Apply dalam tetingkap Printer
Configuration Tools untuk menyimpan perubahan dan menghidupkan semula daemon.
20.2.3 Nama Dan Alias (Name And Alias)
Jika anda ingin menukar nama pencetak (printer), tukar nilai nama baris (Queue Name) di
dalam tab Names and Aliases. Klik OK untuk pergi semula ke tetingkap utama. Pencetak
(printer) tersebut akan bertukar namanya. Klik Apply untuk menyimpan perubahan dan
menghidupkan semula servis daemon pencetak (printer).

Gambar Rajah 173 : Skrin petukaran nama pencetak (printer)
Alias pencetak (printer) adalah nama pilihan lain untuk sesuatu pencetak (printer). Untuk
menambah alias pada pencetak (printer) sedia ada, tekan tab Add pada Names And
Aliases, masukkan nama alias nya. Klik OK lagi dan pergi semula ke tetingkap utama.
Klik Apply untuk menyimpan alias dan hidupkan semula daemon pencetak (printer).
Pencetak (printer) boleh mempunyai lebih dari satu alias.

20.2.4 Jenis Queue (Queue Type)
Gambar Rajah 174 : Skrin petukaran lokasi pencetak (printer)
• Tab Jenis Queue (queue type) menunjukkan jenis queue yang telah anda pilih semasa
menambah pencetak (printer) dan tetapannya (setting). Anda boleh mengubah queue
type atau cuma mengubah tetapannya sahaja. Selepas membuat perubahan, klik OK
untuk kembali ke Tetingkap Utama. Klik Apply untuk menyimpan queue type  dan
hidupkan semula daemon pencetak (printer). Berdasarkan queue mana yang dipilih
(Local Printer, Unix Printer LPD, Window Printer SMB dsbnya), ianya akan diaparkan
di tab queue type .

20.2.5 Pemandu Peranti (Driver )
Pemacu Tab (Tab driver) menunjukkan pemacu pencetak (printer drive) mana yang
sedang digunakan. Ini adalah senarai yang sama yang anda gunakan bila menambah
pencetak. Jika anda menukar pemacu pencetak (printer driver), klik OK untuk kembali
semula ke tetingkap utama. Klik Apply untuk menyimpan perubahan dan hidupkan
daemon pencetak (printer).
Jika anda mempunyai masalah mencetak, sila pilih pemacu (driver) lain dari senarai dan
cetakkan muka surat percubaan (test page). Sebahagian driver berfungsi lebih baik dari
yang lain.
20.2.5.1 Pilihan Terdapat Di Pemandu Peranti (Driver Options)
Gambar Rajah 175 : Skrin petukaran pilihan pemandu

Pilihan di tab Pilihan Pemacu (Driver options) memaparkan fungsi lanjutan pencetak
(printer). Pilihan adalah berbeza menurut pencetak (printer). Pilihlah biasa adalah
Prerender Postscript  harus dipilih jika anda mencetak huruf yang melangkaui huruf
ASCII seperti tulisan Jepun. Pilihan ini menyokong huruf tidak piawai Postscript supaya
ia dicetak dengan betul.
Jika pencetak (printer) tidak menyokong huruf yang cuba anda cetak, sila pilih pilihan ini.
Sebagai contoh, jika mencetak huruf Jepun kepada pencetak (printer) yang tidak
menyokong huruf Jepun, masa tambahan diperlukan untuk menjalankan fungsi ini.
Jangan pilihnya kecuali jika anda mempunyai masalah mencetak huruf dengan betul.
Convert Text to Postscript  dipilih secara tersedia. Jika pencetak (printer) anda boleh
mencetak teks biasa, cuba buang pilihan ini di masa mencetak teks biasa untuk
menyingkatkan masa percetakan. Saiz mukasurat (Page Size) membenarkan anda
mencetak saiz kertas pencetak (printer) anda seperti US Letter, US Legal, A3, A4.
Di atas adalah contoh umum yang mungkin anda perlu tukarkan. Terdapat banyak lagi
pilihan yang boleh anda perbaiki untuk mempercepatkan dan menaikkan kualiti pencetak
(printer) anda tetapi nilai tetapan tersedia (default setting) akan berfungsi dengan baik
dalam percetakan biasa.

PANDUAN PENGAJAR
Pelajaran 21: Set Aplikasi OpenOffice

Mukadimah:
Dalam pelajaran ini, anda akan diperkenalkan kepada set aplikasi OpenOffice. Aplikasi
yang sangat berguna ini pada mulanya dibangunkan oleh Sun Microsystems dan dikenali
sebagai StarOffice. Kini OpenOffice semakin matang dan mampu digunakan oleh
pengguna secara profesional.
Objektif:
1. Mengetahui asas set OpenOffice
2. Mengetahui ciri-ciri set OpenOffice
3. Mengenali aplikasi Writer dalam set OpenOffice
4. Mengenali aplikasi Calc dalam set OpenOffice
5. Mengenali aplikasi Impress dalam set OpenOffice
6. Mengenali aplikasi Draw dalam set OpenOffice

21 SET OPENOFFICE
21.1 Set OpenOffice
Red Hat Linux mempunyai beberapa fungsi untuk membantu pengguna untuk
menyediakan dan mengendalikan dokumen. Jika anda ingin menyediakan persembahan
slaid, menulis surat rasmi atau ingin membuka dokumen dari sesebuah lekatan e-mel (e-
mail link), maka jawapannya sudah tersedia di dalam set OpenOffice.
Set OpenOffice ialah satu gabungan aplikasi yang direka untuk menjimatkan masa dan
membantu pengguna di pejabat, sekolah atau di rumah. OpenOffice adalah aplikasi
automasi pejabat yang mengandungi pemproses perkataan (word processing), laman
lembaran (spreadsheet) dan utiliti persembahan (presentation utility). Aplikasi dalam Set
OpenOffice ini bersifat integrasi di mana anda boleh menyediakan dokumen dengan
menggunakan aplikasi pemproses perkataan (word proccessing) dan mencipta carta
menggunakan aplikasi laman lembaran (spreadsheet) dan juga slaid dari aplikasi
persembahan grafik (graphic presentation application).
OpenOffice memang senang digunakan dan membolehkan anda menguasai keseluruhan
aplikasi dan ia akan mempamerkan perubahan secara spontan semasa anda
menyuntingnya. Cara penyuntingan masa sebenar ini digelar “ Apa yang dilihat itu yang
diperoleh” (“What you see is what you get”).

21.2 Ciri-ciri OpenOffice
Set OpenOffice mengandungi beberapa aplikasi untuk mereka dan menyunting dokumen,
lembaran halaman (spreadsheet), persembahan perniagaan (business presentation) dan
hasil kerja grafik. Ini termasuk templat (templete), borang dan wizuri (wizard) yang
membolehkan anda mereka dokumen profesional asas dan persembahan perniagaan
dengan pantas .Jika anda pernah menggunakan atau menerima fail .doc or .xls, anda akan
memahami bahawa ia serupa dengan Set Microsoft Office. OpenOffice membolehkan
anda untuk membaca, menyunting dan mereka fail dalam beberapa format termasuk fail
yang serupa dengan format Microsoft Office.
Aplikasi OpenOffice Keserasian Fail Jenis dokumen
Writer .sxw, .sdw, .doc, .rtf, .txt,
.htm/.html
Surat rasmi, borang perniagaan,
kerja-kerja sekolah, resume,
berita, laporan.
Calc .sxc, .dbf, .xls, .sdc, .slk,
.csv, .htm/.html
Lembaran halaman, carta,
Jadual, graf, direktori, buku
alamat, bil, belanjawan,
pangkalan data kecil.
Impress .sxi, .ppt, .sxd, .sdd Persembahan perniagaan &
pembelajaran, persembahan web,
syarahan, persembahan slaid.
Draw .sxd, .sd a; eksport fail ke
beberapa format imej,
termasuk jpg, bmp, gif, png
Ilustrasi, lukisan bergaris, klip
seni, carta organisasi
Jadual 36 : Jenis-jenis aplikasi OpenOffice
Set OpenOffice mengandungi beberapa fungsi yang membolehkan anda mengendalikan
kerja untuk pembelajaran, perniagaan dan kegunaan di rumah. Bahagian seterusnya akan
menjelaskan bagaimana cara untuk menggunakan set OpenOffice.

21.3 OpenOffice writer
Menulis dokumen dengan OpenOffice adalah sama seperti pemproses perkataan yang
pernah anda gunakan. Pemproses perkataan (word processing) adalah seperti pengedit
teks di mana anda boleh menyunting, mereka dan mencetak dokumen tanpa tag
penyuntingan yang rumit atau kod. OpenOffice writer pemproses perkataan canggih di
mana terdapat fungsi WYSIWYG -apa yang anda lihat di tetingkap OpenOffice writer
adalah apa yang akan dapat saksikan selepas dokumen itu dicetak atau jika diberi kepada
orang lain untuk ditatap.
21.3.1 Tetingkap OpenOffice writer
Untuk memulakan OpenOffice dari panel meja kerja, pilih
main menu>office>OpenOffice writer.
Lembaran putih yang terdapat di tengah-tengah tetingkap adalah kawasan untuk
menyunting dokumen -inilah kawasan di mana anda boleh menaip teks. Di bahagian atas
tetingkap terdapat bar alat (toolbar) yang mengandungi pilihan untuk mengawal saiz
huruf, menyelaraskan teks dalam dokumen dan penyuntingan teks yang lain.
Text box digunakan untuk anda menaip lokasi yang tepat untuk dokumen di komputer
anda dan memuatkan dokumen itu ke ruang penyuntingan .Selain daripada itu, ada juga
butang untuk buka dokumen (open), simpan (save),cetak (print) dokumen dan juga  untuk
memulakan dokumen yang baru di mana anda akan membuka tetingkap (window ) baru
dengan dokumen yang kosong untuk anda menulis kandungan.

Gambar Rajah 176 : Paparan tetingkap program OpenOffice Writer
Di sebelah kiri tetingkap (window), terdapat bar alat (toolbar) dengan butang untuk
semak ejaan (spell checking), perkataan salah dinyatakan (automatic highlighting of
misspelled words), pencarian perkataan dan frasa (word & phrase searching),
Penyuntingan Mudah (convenient editing functions). Jika  anda mengarahkan tetikus di
atas butang bar alatan (toolbar), popup atau tooltip akan terpapar untuk keterangan
tentang fungsi butang itu. Anda juga boleh mendapatkan keterangan lanjut dengan
mengklik di help menu dan seterusnya di extended tips.

21.3.2 Cara menggunakan OpenOffice write
Anda boleh terus mula menaip text di ruang penyuntingan dokumen (document editing
area) dengan menggunakan tetapan tersedia (default settings).Untuk menyimpan teks ,
klik  di  butang Save .Anda boleh pilih jenis format fail yang akan disimpan dari menu
file type. Jenis fail tersedia (Default file type) adalah hanya untuk aplikasi OpenOffice.
Untuk fail yang ingin dihantar kepada pengguna Microsoft Office, atau anda ingin
menyunting fail dari pautan (link) email yang dihantar dalam format  Microsoft Words
.doc, anda boleh menyimpan  fail  itu dengan format Microsoft Word supaya ia dapat
dibuka oleh orang lain yang menggunakan Microsoft Word. Selain daripada
penyuntingan dokumen, anda boleh juga menambah objek  seperti  imej, ilustrasi, carta
dan jadual ke dalam dokumen.Untuk menambah imej, klik insert>graphics>from file dan
pilih imej dari pelayar file (pop-up file browser). Imej itu akan ditampal di mana anda
mengarahkan penunjuk tetikus dan anda juga boleh mengubah saiz imej.
Selepas mencipta dokumen baru, anda boleh menyimpan dalam format yang anda
inginkan. Selain dari
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
