---
okf_version: 0.1
name: Bab 13 - Bahagian 1
topics: [linux, manual, references, chapter-13]
tags: [noss, dbp]
---
# Bab 13 - Bahagian 1

Gambar Rajah 179 : Penambahan graf dalam program OpenOffice Calc
Graf akan diwujudkan di dalam tetingkap lembaran (spreadsheet window). Anda boleh
juga mengalihkan graf tersebut di mana jua di atas skrin lembaran untuk dicetak atau
anda boleh juga menyimpan graf tersebut sebagai objek yang boleh digabung dengan
dokumen OpenOffice writer atau persembahan slaid OpenOffice impress.
21.5 OpenOffice Impress
Kesan visual membolehkan anda menarik perhatian penonton. OpenOffice impress
adalah perisian bantuan paparan grafik yang membolehkan anda mencipta paparan yang
menarik.

21.5.1 Menggunakan OpenOffice Impress
Untuk memulakan OpenOffice impress dari panel desktop, pilih main menu> office>
OpenOffice impress. Untuk shell prom pula ,taipkan ooimpress.
Bila anda memulakan OpenOffice impress, Autopilot akan  memaparkan skrin
penyediaan persembahan. Ia akan meminta dari anda informasi asas tentang persembahan
yang anda ingin menciptakan .Anda  boleh memilih jenis slaid  di mana ia akan
digunakan ( plain paper,transparent paper for overhead projector, slaids ,display
monitor) dan kesan visual yang anda inginkan semasa dipersembahkan melalui komputer.
Gambar Rajah 180 : Skrin bagi program OpenOffice Impress
Selepas membuat pilihan, anda boleh memilih jenis slaid yang ingin menciptakan. Anda
boleh memilih dari  slaid tersedia (pre-formatted slaid) dari senarai atau mulakan dengan

slaid kosong dan kemudian menciptanya .Untuk mencipta slaid baru, klik insert slaid«di
floating toolbar , sebuah pop-up window akan dipaparkan di mana anda boleh memilih
susun atur untuk slaid baru tersebut. Anda boleh mengadakan seberapa banyak slaid yang
anda inginkan.
Gambar Rajah 181 : Membuat slaid baru dalam program OpenOffice Impress
Hendak menonton persembahan? Anda boleh menonton pra tonton (preview) dengan
memilih Slide show> slide show  dari menu tarik ke bawah (pull down menu).
Persembahan itu boleh di pra tonton secara skrin penuh, di mana anda klik untuk ke slaid
seterusnya sehingga ke slaid akhir atau tekan ESC untuk berhenti serta merta.

21.5.2 Menyimpan Persembahan
Persembahan boleh disimpan dalam beberapa format. Anda boleh menyimpan dalam
format OpenOffice impress (contohnya, failku.sxi), format Microsoft Powerpoint (*.ppt)
atau format Starimpress (*.sdd). Selain daripada itu, anda boleh mencetak persembahan
di atas kertas biasa atau format kertas lut sinar dengan mengklik  file>print dari menu
file. Untuk keterangan lanjut mengenai OpenOffice impress, klik File> help> contents
dari pelayar help.
21.6 OpenOffice draw
Jikalau anda ingin mencipta graf untuk dokumen dan persembahan, anda boleh
menggunakan OpenOffice draw. Gunakan tetikus sebagai pen atau berus cat. OpenOffice
draw membolehkan anda membuat ilustrasi dan menyimpan dalam format yang boleh
anda tambah pada dokumen yang ingin anda cetak, memapar di laman web atau dipaut
ke e-mel (attachment).
Untuk memulakan OpenOffice draw dari panel meja kerja, klik Main menu> office>
OpenOffice draw. Di shell prom pula, taipkan oodraw.

Gambar Rajah 182 : Skrin bagi program OpenOffice Draw
Jikalau anda biasa dengan perisian ilustrasi dan grafik yang lain (misalnya GIMP), anda
akan dapati OpenOffice Draw mempunyai sebahagian dari fungsi tersebut.
Ia juga mengandungi toolbar untuk mencipta garis lurus & garis lenggok, bentuk asas
seperti segi empat dan bulatan, objek 3D seperti kon dan kiub dan sebagainya. Anda juga
boleh mewarnakan imej  dengan menggunakan Area style/filling  di menu tarik ke bawah
di toolbar utama. Anda juga boleh menambah teks ke dalam ilustrasi. OpenOffice draw
juga membolehkan anda membuka dan mengimport imej serta  membuat perubahan
dengan peralatan yang sedia ada.
Setelah selesai dengan perubahan ilustrasi atau imej, anda boleh menyimpan fail dalam
format fail asal atau eksport kerja anda ke format universal  seperti  .jpg atau  .png.

PANDUAN PENGAJAR
Pelajaran 22: Sambungan Ke Internet

Mukadimah:
Dalam pelajaran ini, anda akan mempelajari kaedah sambungan ke Internet menggunakan
beberapa kaedah sambungan yang biasanya digunakan seperti modem, ISDN dan xDSL.
Selain itu anda juga akan diperkenalkan kepada aplikasi disk druid dan kppp dialer yang
sangat berguna.
Objektif:
1. Mengenali jenis sambungan ke Internet yang biasa digunakan oleh pengguna dan
kaedah penetapannya
2. Mengetahui kepenggunaan wizard disk druid
3. Mengetahui penetapan modem
4. Mengetahui kepenggunaan dan penetapan kppp dialer

22 SAMBUNGAN  KE INTERNET
22.1 Jenis sambungan Internet
22.1.1 Sambungan ISDN
ISDN (Internet Services Digital Network) menggunakan talian telekomunikasi digital
yang laju dan bermutu tinggi berbanding dengan menggunakan sambungan modem
analog. Talian khas ini harus dipasang oleh syarikat telekomunikasi.
22.1.2 Sambungan Modem
Sambungan modem di mana modem di gunakan untuk membuat sambungan ke Internet
melalui talian telefon. Data digital akan ditukar ke isyarat analog  dan dihantar melalui
talian telefon.
22.1.3 Sambungan xDSL
xDSL (Digital Subsciber Line or Loop) menggunakan penyiaran berkelajuan tinggi
melalui talian telefon. Terdapat beberapa jenis DSL seperti ADSL, IDSL dan  SDSL.
Di Linux, sambungan ke Internet melalui talian Sesiri, Point-To-Point (PPP) atau Eternet
xDSL adalah begitu mudah.
Protokol Point-to-Point (PPP) adalah suatu piawaian untuk sambungan ke Internet
melalui talian dail. Ini adalah cara sambungan yang paling biasa (di Malaysia) ke
Internet sebagai sebahagian dari rangkaian ISP
Mula-mula anda harus  menyediakan perkakasan seperti modem luaran sama ada serial
atau usb. Selepas itu, anda perlu memberi informasi tentang Pembekal Perkhidmatan
Internet (ISP) yang anda gunakan, seperti maklumat nombor untuk didail , kata pengguna
dan kata laluan (login id and password). Selepas selesai menyediakan perkakasan  dan

mengkonfigurasi maklumat, anda boleh membuat sambungan  ke Internet untuk
menghantar dan menerima E-mel, melayari  WWW dan juga berceloteh.
Red Hat Linux ada menyediakan beberapa alat bantuan untuk memudahkan konfigurasi.
Hanya dengan mengikuti langkah-langkah berikut dan anda boleh melayari web!
22.2 Wizard Sambungan Internet
Gambar Rajah 183 : Langkah-langkah untuk membuka program konfigurasi Internet

22.2.1 Internet Druid
Di Red Hat, aplikasi Internet Druid  boleh digunakan untuk menkonfigurasi sambungan
Internet. Tetapi anda  harus menjalankan sistem X Windows  dan mempunyai
keistimewaan umbi. Untuk memulakan aplikasi Internet Druid, ikuti langkah-langkah
berikut:
1. Di meja kerja GNOME, pilih Main menu > programs > system > Internet
configuration  wizard
2. Di meja kerja KDE , pilih Main menu > System > Internet Configuration Wizard.
3. Di Shell prom, taipkan Internet-druid (contoh di Xterm atau Terminal GNOME).
Gambar Rajah 184 : Skrin pemilihan jenis perkakasan penyambungan Internet

ISP anda mungkin mempunyai konfigurasi yang lain daripada apa yang disebut di atas.
Sebelum sambungan, periksa ISP anda untuk arahan unik yang sedia ada, termasuk
informasi berikut:
/checkbldNombor telefon untuk modem yang di mana disambung ke ISP anda.
/checkbldKata pengguna (login) dan juga kata laluan (password) untuk akaun ISP.
/checkbldAlamat “gateway” (Gateway address) untuk beberapa ISP kena dimasukkan ,
manakala ada yang secara automatik akan diset “gateway address” apabila anda log
masuk (login).
/checkbldKemasukan DNS (DNS Entries) : DNS bermaksud “Domain Name Sistem”. DNS
adalah seperti peta jalan untuk Internet. Ini akan di set kan secara  automatik apabila
anda “login”.
Di Malaysia, sambungan ke Internet yang paling banyak digunakan adalah modem dan
juga xDSL (broadcast).
22.3 Konfigurasi Modem
Modem boleh digunakan untuk membuat konfigurasi sambungan Internet melalui talian
telefon yang  aktif. Anda juga perlu ada akaun ISP.
Modem menukarkan data analog  kepada digital di mana ia dapat dihantar melalui talian
telefon  biasa. Jenis-jenis modem adalah:
22.3.1 Modem Perisian Dalaman
Modem ini tidak mempunyai litar liang serial (serial port circuitry). Terdapat driver
Linux untuk modem perisian dalaman bagi beberapa model sahaja. Anda boleh ke
http://www.linmodems.org untuk keterangan lanjut. Cuba untuk  mengelakkan daripada
menggunakan modem perisian  di Linux.

22.3.2 Modem Luaran
Modem ini menggunakan liang serial. Linux akan mengesan modem jenis ini secara
automatik dan membuat semua konfigurasi tentang perkakasan ini.
22.3.3 Modem USB
Modem yang disambung melalui liang usb adalah popular sekarang. Modem USB yang
menggunakan ‘Communication Device Class Abstract Control Modem (CDC0ACM)
protocol’ akan berfungsi dengan  isirung (kernel) Linux 2.4.x.
Untuk menambah sambungan modem, ikut langkah-langkah berikut:
1. Pilih modem sambungan dari jadual jenis peranti (device type list), klik Forward.
2. Jika ada modem yang telah tersedia dikonfigurasikan dalam senarai perkakasan (di
tab hardware), Network Administration Tool akan membuat andaian bahawa anda
ingin menggunakannya untuk membuat sambungan Internet. Jika tiada modem yang
telah dikonfigurasi, ia akan mengesan modem lain di sistem. Ini akan mengambil
sedikit masa.
3. Sila buat konfigurasi untuk  kadar baud baud rate , kawalan aliran flow control ,
bahana modem modem volume . Jikalau anda tidak  mengetahui nilainya, biarkan
dalam keadaan tersedia (default). Kalau anda tidak mempunyai pendail tona  (touch-
tone dialling), buangkan tanda pilihan (uncheck).

Gambar Rajah 185 : Skrin pemilihan jenis modem
4. Klik forward.
5. Memberi maklumat tentang akaun ISP. Kalau anda tidak mengetahui, hubungilah ISP
anda. Klik forward.

Gambar Rajah 186 : Skrin pemilihan Pemberi Perkhidmatan Internet (ISP)
6. Di muka create dialup, klik apply.
Selepas menambah modem, anda boleh mengubahsuai konfigurasi dengan memilih
peranti tersebut yakni modem dari senarai peranti dan selepas itu mengklik Edit.
Contohnya, selepas peranti ditambah, ia di konfigurasi untuk tidak dimulakan masa
komputer dihidupkan (boot time) secara tersedia. Anda boleh mengubahsuai  konfigurasi
tersebut. Tetapan (setting) lain seperti PPP, kata pengguna (login name), kata laluan
(password) dan sebagainya boleh juga diubahsuai.
Selepas peranti  ditambah, ia masih tidak aktif dan digambarkan dengan status tidak aktif
(inactive status). Untuk mengaktifkan sambungan PPP, pilih Start Menu > System

Settings> Network . Untuk mengaktifkan peranti, pilih peranti dari senarai peranti dan
klik butang Activate.
Gambar Rajah 187 : Mengaktifkan modem melalui tetingkap konfigurasi rangkaian
22.4 Pendail KDE PPP Dialer
Anda boleh menggunakan satu lagi wiza
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
