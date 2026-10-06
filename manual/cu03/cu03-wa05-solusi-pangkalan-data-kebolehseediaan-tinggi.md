---
okf_version: '0.2'
type: reference
title: 'Solusi Pangkalan Data Kebolehseediaan Tinggi Enterprise: MariaDB Galera +
  MaxScale lwn. PostgreSQL HA + Pgpool-II'
timestamp: '2026-08-17T00:00:00Z'
topics:
- noss-linux
- cu03
- wa05
- mariadb-galera
- maxscale
- postgresql-ha
- pgpool-ii
tags:
- cu03
- wa05
- database-ha
- mariadb
- postgresql
- maxscale
- pgpool-ii
description: Kertas Reka Bentuk Teknikal dan Cetak Biru Penyebaran Solusi Pangkalan
  Data Kebolehseediaan Tinggi Enterprise merangkumi MariaDB Galera Cluster bersama
  MaxScale serta PostgreSQL HA bersama Pgpool-II.
resource: file:///manual/cu03/cu03-wa05-solusi-pangkalan-data-kebolehseediaan-tinggi.md
spec_version: '0.2'
status: stable
stale_after: '2027-12-31'
generated:
  by: NOSS Linux Malaysia / Harisfazillah Jamel
  at: '2026-10-02T08:45:00Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
- id: mariadb-galera-docs
  title: MariaDB Galera Cluster & MaxScale Documentation
  author: MariaDB Corporation
  url: https://mariadb.com/kb/en/maxscale/
  resource: https://mariadb.com/kb/en/maxscale/
- id: pgpool2-docs
  title: Pgpool-II Documentation & Watchdog Tutorial
  author: Pgpool Global Development Group
  url: https://www.pgpool.net/mediawiki/index.php/Main_Page
  resource: https://www.pgpool.net/mediawiki/index.php/Main_Page
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: Google Cloud Data Analytics
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- id: redlinesoft-attested-computations
  title: Attested Computations in Open Knowledge Format (OKF v0.2)
  author: RedLineSoft
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
  resource: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: dsom-okf-v02-adoption-skill
  title: OKF v0.2 Adoption Engineer Skill Standard
  author: Deep State of Mind (DSOM)
  url: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
  resource: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
---

# Solusi Pangkalan Data Kebolehseediaan Tinggi Enterprise: MariaDB Galera + MaxScale lwn. PostgreSQL HA + Pgpool-II

> **Tajuk Dokumen:** Cetak Biru Reka Bentuk Teknikal & Penyebaran Perbandingan: Kluster MariaDB Galera + MaxScale lwn. Kebolehseediaan Tinggi (HA) PostgreSQL (Penyalinan Penyiaran Fizikal Tempatan) + Pgpool-II
> **Versi Dokumen:** 3.0
> **Audiens Sasaran:** Arkitek Sistem, Pentadbir Pangkalan Data (DBA), Jurutera DevOps, Ketua Infrastruktur
> **Unit Kompetensi NOSS:** CU03 (Pentadbiran & Perkhidmatan Pelayan Linux) — WA05 (Pelaksanaan Peranan dan Servis Pelayan)

---

## 1. Ringkasan Eksekutif

Dokumen ini menyajikan cetak biru teknikal komprehensif bagi dua seni bina pangkalan data sumber terbuka gred enterprise berpengecasan Kebolehseediaan Tinggi (High Availability - HA) yang memanfaatkan proksi sedar-SQL Lapisan 7 (Layer 7):

1. **Kluster MariaDB Galera bersama MaxScale** (Proksi pangkalan data Lapisan 7 sedar-SQL).
2. **Kebolehseediaan Tinggi PostgreSQL (Penyalinan Penyiaran Fizikal Tempatan / Native Physical Streaming Replication)** bersama **Pgpool-II** (Proksi pangkalan data Lapisan 7 sedar-SQL, pengumpul sambungan / connection pooler, dan pengatur kegagalan beralih / failover orchestrator dengan Watchdog HA).

Kedua-dua seni bina menyediakan toleransi kelemahan (fault tolerance), kegagalan beralih tanpa gangguan masa henti (zero-downtime failover), kebolehskalaan bacaan, pengumpulan sambungan, serta pemisahan baca-tulis telus pada satu port pangkalan data tunggal. Reka bentuk ini memanfaatkan Pgpool-II untuk mengurus sambungan pelanggan PostgreSQL, penghalaan pertanyaan, pemantauan kesihatan, dan pemajuan nod tanpa memerlukan enjin konsensus pihak ketiga seperti `etcd` atau proksi TCP berasingan seperti HAProxy.

---

## 2. Seni Bina 1: Kluster MariaDB Galera bersama MaxScale

### 2.1 Gambaran Keseluruhan Seni Bina

Kluster MariaDB Galera ialah kluster penyalinan berasaskan multi-master dan terseganti (synchronous replication) berasaskan API *Write-Set Replication* (WSREP). MaxScale bertindak sebagai proksi pintar Lapisan 7 yang sedar-SQL untuk mengagihkan trafik berdasarkan konteks pertanyaan (memisahkan operasi baca dan tulis), melaksanakan semakan kesihatan pelayan, dan mengendalikan kegagalan beralih secara telus.

```
                     +-------------------+
                     |  Lapisan Aplikasi |
                     +---------+---------+
                               |
                               | (Protokol MySQL)
                               v
                     +-------------------+
                     | MariaDB MaxScale  |
                     | (Proksi SQL L7)   |
                     +----+---------+----+
                          |         |
         +----------------+         +----------------+
         | (Tulis / Baca)           | (Baca)         |
         v                          v                v
+-----------------+        +-----------------+  +-----------------+
|  Nod MariaDB 1  |<======>|  Nod MariaDB 2  |<=|  Nod MariaDB 3  |
| (Galera Master) |  wsrep | (Galera Master) |  | (Galera Master) |
+-----------------+        +-----------------+  +-----------------+
```

### 2.2 Komponen Teras & Tanggungjawab

* **Pelayan MariaDB (bersama Pustaka Galera):** Menyediakan penyalinan terseganti multi-master, memastikan kesemua nod mengandungi keadaan data yang identikal sebaik sahaja komit transaksi berlaku.
* **Enjin Galera WSREP:** Mengendalikan penyalinan berasaskan pensijilan (certification-based replication), komunikasi kumpulan (melalui protokol EVS), serta pemindahan keadaan data (SST/IST).
* **MariaDB MaxScale:**
  * **Modul ReadWriteSplit:** Menganalisis penyataan SQL yang masuk, menghantar arahan `INSERT`/`UPDATE`/`DELETE` dan transaksi eksplisit ke sasaran penulisan utama sambil mengimbangkan beban pertanyaan `SELECT` merentas semua nod bacaan yang sedia ada.
  * **Pemantau Galera (`galeramon`):** Memantau topologi kluster, status penyelarasan nod (`wsrep_local_state_comment`), dan status komponen utama secara berterusan.

### 2.3 Logik Penghalaan Trafik & Kegagalan Beralih (Failover)

* **Komit Terseganti (Synchronous Commit):** Transaksi disahkan berasaskan pensijilan di kesemua nod kluster sebelum proses komit diselesaikan.
* **Pemisahan Baca-Tulis:** MaxScale menganalisis sintaks SQL. Transaksi eksplisit (`BEGIN...COMMIT`) dan penyataan penulisan diarahkan secara khusus ke satu nod penulisan utama yang ditetapkan (bagi mengelakkan kebuntuan Galera / konflik pensijilan di bawah beban konkurensi tinggi).
* **Kegagalan Beralih (Failover):** Jika nod penulisan utama mengalami kegagalan, MaxScale mengalihkan pertanyaan penulisan secara serta-merta ke nod Galera lain yang terselaras tanpa sebarang gangguan masa henti kepada aplikasi yang terhubung.

### 2.4 Konfigurasi Garis Panduan Asas

#### A. Konfigurasi MariaDB Galera (`/etc/my.cnf.d/galera.cnf`)

```ini
[mysqld]
binlog_format=ROW
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2
innodb_flush_log_at_trx_commit=0

# WSREP Provider Settings
wsrep_on=ON
wsrep_provider=/usr/lib64/galera-4/libgalera_smm.so
wsrep_cluster_name="mariadb_ha_cluster"
wsrep_cluster_address="gcomm://10.0.1.11,10.0.1.12,10.0.1.13"

# Node Configuration
wsrep_node_address="10.0.1.11"
wsrep_node_name="db-node-01"
wsrep_sst_method=mariabackup
wsrep_sst_auth="sstuser:SecurePassword123!"
```

#### B. Konfigurasi MaxScale (`/etc/maxscale.cnf`)

```ini
[maxscale]
threads=auto

# Server Definitions
[db-node-1]
type=server
address=10.0.1.11
port=3306
protocol=MariaDBBackend

[db-node-2]
type=server
address=10.0.1.12
port=3306
protocol=MariaDBBackend

[db-node-3]
type=server
address=10.0.1.13
port=3306
protocol=MariaDBBackend

# Galera Monitor
[Galera-Monitor]
type=monitor
module=galeramon
servers=db-node-1, db-node-2, db-node-3
user=maxscale
password=MaxScalePassword123!
monitor_interval=2000ms
disable_master_failback=1

# Read-Write Split Router Service
[Read-Write-Service]
type=service
router=readwritesplit
servers=db-node-1, db-node-2, db-node-3
user=maxscale
password=MaxScalePassword123!

# Listener
[Read-Write-Listener]
type=listener
service=Read-Write-Service
protocol=MariaDBClient
port=3306
```

---

## 3. Seni Bina 2: Kebolehseediaan Tinggi PostgreSQL (Penyalinan Penyiaran Tempatan) bersama Pgpool-II

### 3.1 Gambaran Keseluruhan Seni Bina

Seni bina ini mengguna pakai Penyalinan Penyiaran Fizikal Tempatan (Physical Streaming Replication - Utama-Penantian / Primary-Standby) PostgreSQL yang diintegrasikan bersama Pgpool-II sebagai proksi Lapisan 7 sedar-SQL. Pgpool-II beroperasi dalam mod `master_slave_mode` dengan sub-mod `stream`, menyediakan pengumpulan sambungan pelanggan, pemisahan pertanyaan baca-tulis automatik pada port hadapan tunggal (9999 atau 5432), semakan kesihatan automatik, dan pengatur kegagalan beralih kluster aktif.

Bagi menghapuskan titik kegagalan tunggal (SPOF) pada lapisan proksi, nod-nod Pgpool-II menjejaskan protokol Watchdog, mengekalkan IP Maya (Virtual IP - VIP) yang dikongsi merentas berbilang instans Pgpool-II.

```
                      +--------------------+
                      |  Lapisan Aplikasi  |
                      +---------+----------+
                                |
                                | (Protokol PgSQL - VIP: 10.0.2.100:9999)
                                v
                     +----------------------+
                     |  Pgpool-II (Aktif)   | <--- Watchdog Heartbeat ---> Pgpool-II (Penantian)
                     | (Proksi L7 / Pooler) |
                     +---+--------------+---+
                         |              |
         +---------------+              +---------------+
         | (Tulis / Baca)                               | (Baca)
         v                                              v
+-------------------+   Physical Streaming     +-------------------+
|  Nod PostgreSQL 1 |<========================>|  Nod PostgreSQL 2 |
|  (Utama / Tulis)  |   (WAL Sender / Slot)    |  (Replika Standby)|
+-------------------+                          +-------------------+
```

### 3.2 Komponen Teras & Tanggungjawab

* **Enjin PostgreSQL:** Menjalankan Penyalinan Penyiaran Fizikal tempatan (menggunakan slot penyalinan utama dan penyalinan WAL).
* **Pelayan Proksi Pgpool-II:**
  * **Penganalisis Pertanyaan L7 & Pengimbang Beban:** Memintas pertanyaan PostgreSQL. Menghala penyataan `INSERT`, `UPDATE`, `DELETE`, DDL, dan transaksi eksplisit (`BEGIN...COMMIT`) ke bahagian belakang Primary PostgreSQL. Mengimbangkan beban pertanyaan `SELECT` baca sahaja merentas kesemua nod bahagian belakang yang sihat.
  * **Pengumpulan Sambungan (Connection Pooling):** Mengekalkan kolam sambungan berterusan di sebelah pelayan untuk mengelakkan beban lebihan sambungan PostgreSQL.
  * **Semakan Kesihatan & Kegagalan Beralih Automatik:** Memantau nod bahagian belakang secara berterusan. Mencetuskan skrip kegagalan beralih tersuai (`failover.sh`) apabila nod Utama mengalami kegagalan untuk memajukan nod pangkalan data penantian (Standby).
  * **Pgpool Watchdog:** Menyelaras keadaan nod dalaman merentas berbilang instans Pgpool-II dan mengurus IP Maya (VIP) terapung menggunakan mekanisme `arping` / `keepalived`.

### 3.3 Logik Penghalaan Trafik & Kegagalan Beralih (Failover)

* **Titik Hujung Aplikasi Teragih:** Aplikasi terhubung ke Pgpool-II melalui satu port tunggal (contohnya, 9999 atau 5432).
* **Pemprosesan Pertanyaan:**
  * Penyataan penulisan $\rightarrow$ Diarah terus ke Backend 0 (Utama / Primary).
  * Penyataan baca sahaja $\rightarrow$ Diagihkan antara Backend 0 (Utama) dan Backend 1/2 (Replika Penantian) mengikut pemberat beban yang dikonfigurasikan.
* **Kitaran Kegagalan Beralih Automatik:**
  1. Jika Pgpool-II mengesan nod Utama tidak dapat dicapai (selepas melebihi `health_check_max_retries`), ia mengeksekusi `failover_command`.
  2. Skrip terhubung ke nod Penantian (Standby) yang ditetapkan dan mengeksekusi `pg_ctl promote` (atau mencipta fail pemicu).
  3. Pgpool-II mengemas kini jadual status nod dalamannya, menandakan nod Utama lama sebagai terhenti (*down*), memajukan nod Penantian kepada status Utama dalam peta bahagian belakang Pgpool, dan meneruskan penghalaan transaksi tanpa perlu memulakan semula (*restart*) proksi.

### 3.4 Konfigurasi Garis Panduan Asas

#### A. Konfigurasi Utama PostgreSQL (`postgresql.conf`)

```ini
# Network & Connections
listen_addresses = '*'
port = 5432
max_connections = 250
shared_buffers = 4GB

# Replication Parameters
wal_level = replica
max_wal_senders = 10
max_replication_slots = 10
hot_standby = on
hot_standby_feedback = on

# Archive Parameters
archive_mode = on
archive_command = 'test ! -f /var/lib/postgresql/wal_archive/%f && cp %p /var/lib/postgresql/wal_archive/%f'
```

#### B. Konfigurasi Pgpool-II (`/etc/pgpool-II/pgpool.conf`)

```ini
# Network Settings
listen_addresses = '*'
port = 9999
pcp_port = 9898

# Operating Mode
backend_clustering_mode = 'streaming_replication'
master_slave_mode = on
master_slave_sub_mode = 'stream'

# Backend Database Nodes
backend_hostname0 = '10.0.2.11'
backend_port0 = 5432
backend_weight0 = 1
backend_flag0 = 'ALLOW_TO_FAILOVER'

backend_hostname1 = '10.0.2.12'
backend_port1 = 5432
backend_weight1 = 1
backend_flag1 = 'ALLOW_TO_FAILOVER'

backend_hostname2 = '10.0.2.13'
backend_port2 = 5432
backend_weight2 = 1
backend_flag2 = 'ALLOW_TO_FAILOVER'

# Connection Pooling Settings
num_init_children = 32
max_pool = 4
connection_cache = on

# Load Balancing (Read-Write Splitting)
load_balance_mode = on
ignore_leading_white_space = on
white_function_list = ''
black_function_list = 'nextval,currval,lastval,setval'

# Health Check Settings
health_check_period = 5
health_check_timeout = 5
health_check_max_retries = 3
health_check_user = 'pgpool'
health_check_password = 'PgpoolPassword123!'
health_check_database = 'postgres'

# Failover Script Command
failover_command = '/etc/pgpool-II/failover.sh %d %h %p %D %m %H %M %P'

# Watchdog Settings (High Availability for Pgpool itself)
use_watchdog = on
wd_hostname = '10.0.2.21'
wd_port = 9000
delegate_IP = '10.0.2.100'
wd_lifecheck_method = 'heartbeat'
wd_interval = 2
wd_auth_key = 'WatchdogSecretKey'

other_pgpool_hostname0 = '10.0.2.22'
other_pgpool_port0 = 9000
other_wd_port0 = 9000
```

#### C. Skrip Failover Pgpool (`/etc/pgpool-II/failover.sh`)

Dikeksekusi secara automatik oleh Pgpool-II apabila nod bahagian belakang mengalami kegagalan.

```bash
#!/usr/bin/env bash
# Parameter yang dihantar oleh Pgpool-II:
# %d = ID nod gagal, %h = hos gagal, %p = port gagal, %D = direktori data gagal
# %m = ID nod master baharu, %H = hos master baharu, %M = ID nod master lama, %P = ID nod utama lama

FAILED_NODE_ID="$1"
FAILED_HOST="$2"
NEW_MASTER_ID="$5"
NEW_MASTER_HOST="$6"
OLD_PRIMARY_ID="$8"

LOGFILE="/var/log/pgpool/failover.log"

echo "[$(date)] Cetusan kegagalan beralih. Nod Gagal: ${FAILED_NODE_ID} (${FAILED_HOST}). Utama Lama: ${OLD_PRIMARY_ID}" >> "$LOGFILE"

# Hanya lakukan pemajuan (promotion) jika nod yang gagal merupakan nod Utama
if [ "$FAILED_NODE_ID" -eq "$OLD_PRIMARY_ID" ]; then
    echo "[$(date)] Memajukan nod Penantian ${NEW_MASTER_ID} (${NEW_MASTER_HOST}) kepada Utama..." >> "$LOGFILE"

    # Eksekusi arahan pemajuan melalui SSH pada sasaran master baharu
    ssh -o StrictHostKeyChecking=no -i /var/lib/postgresql/.ssh/id_rsa postgres@"${NEW_MASTER_HOST}" \
        "/usr/lib/postgresql/15/bin/pg_ctl promote -D /var/lib/postgresql/15/main"

    if [ $? -eq 0 ]; then
        echo "[$(date)] Berjaya memajukan nod ${NEW_MASTER_HOST} kepada Utama." >> "$LOGFILE"
        exit 0
    else
        echo "[$(date)] RALT: Gagal memajukan nod ${NEW_MASTER_HOST}!" >> "$LOGFILE"
        exit 1
    fi
else
    echo "[$(date)] Nod gagal ${FAILED_NODE_ID} ialah nod Penantian (Standby). Tiada pemajuan diperlukan." >> "$LOGFILE"
    exit 0
fi
```

---

## 4. Matriks Perbandingan Seni Bina Komprehensif

| Dimensi | Kluster MariaDB + MaxScale | PostgreSQL HA (Streaming Repl.) + Pgpool-II |
| :--- | :--- | :--- |
| **Jenis Penyalinan** | Terseganti / Synchronous (WSREP berasaskan pensijilan) | Penyalinan Penyiaran Fizikal Asinkronus atau Terseganti |
| **Keupayaan Multi-Master** | Aktif-Aktif (Keupayaan penulisan Multi-Master) | Aktif-Pasif (Satu Utama / Primary, Berbilang Replika Standby) |
| **Peringkat Proksi** | Lapisan 7 / Layer 7 (Sedar Protokol SQL) | Lapisan 7 / Layer 7 (Sedar Protokol SQL) |
| **Penghalaan Baca-Tulis** | Analisis penyataan SQL tempatan pada port tunggal (3306) | Analisis penyataan SQL tempatan pada port tunggal (9999 / 5432) |
| **Pengumpulan Sambungan Binaan Dalam** | Ya (penapis `connection_pool`) | Ya (Pengurus kolam sambungan anak tempatan) |
| **Pengaturan Kegagalan Beralih (Failover)** | Modul `galeramon` MaxScale | Skrip eksekusi `failover_command` Pgpool-II |
| **Kebolehseediaan Tinggi Proksi** | Redundansi MaxScale (Keepalived / Corosync) | Protokol Watchdog Pgpool-II Tempatan bersama VIP Terapung |
| **Kebergantungan Luaran** | Tiada (Protokol WSREP binaan dalam) | Tiada (Tiada enjin DCS seperti `etcd` atau Consul diperlukan) |
| **Potensi Kehilangan Data (RPO)** | Hampir Sifar ($RPO = 0$) | $RPO = 0$ (Penyalinan terseganti) / $RPO > 0$ (Mod asinkronus) |
| **Masa Pemulihan (RTO)** | $< 5$ saat | $< 10 - 15$ saat (Masa henti semakan kesihatan + pemajuan skrip) |
| **Risiko Kebuntuan (Deadlock)** | Sederhana jika penulisan mengenai berbilang nod serentak | Sifar (Kesemua penulisan diarahkan secara tegar ke nod Utama tunggal) |

---

## 5. Pertimbangan Operasi & Amalan Terbaik

### 5.1 Mencegah Senario Otak-Terpisah (Split-Brain)

* **MariaDB Galera:** Memerlukan penyebaran minimum 3 nod. Galera menggunakan pengundian kuorum berpemberat EVS; nod terpencil secara automatik memasuki keadaan bukan-utama (non-primary) bagi mengelakkan penulisan otak-terpisah.
* **PostgreSQL + Pgpool-II Watchdog:** Sebarkan bilangan nod Pgpool-II ganjil (minimum 3 instans) yang menjalankan Watchdog. Watchdog memerlukan undian majoriti ($N/2 + 1$) sebelum menetapkan IP Maya (VIP) atau mencetuskan arahan kegagalan beralih, memastikan pembahagian rangkaian tidak menghasilkan pemajuan utama otak-terpisah.

### 5.2 Strategi Sandaran & Pemulihan Bencana

* **Kluster MariaDB:** Gunakan `mariabackup` untuk sandaran fizikal tanpa sekat (*non-blocking*) yang dieksekusi pada nod bacaan penantian. Tetapkan `wsrep_desync=ON` pada nod sandaran semasa eksekusi untuk mengasingkan I/O sandaran daripada trafik penyalinan Galera.
* **PostgreSQL HA:** Sebarkan `pgBackRest` atau `WAL-G` digabungkan dengan pengarkiban WAL berterusan. Eksekusi sandaran fizikal secara terus terhadap nod pangkalan data penantian bagi mengelakkan impak CPU dan I/O cakera pada nod Utama.

### 5.3 Pengoptimuman Pengurusan Sambungan

* **MariaDB / MaxScale:** Laraskan penapis kolam sambungan MaxScale dan tetapkan had pelayan belakang (`maxconn`) supaya sejajar dengan parameter `max_connections` MariaDB.
* **PostgreSQL / Pgpool-II:** Penalaan parameter `num_init_children` dan `max_pool` Pgpool secara teliti. Jumlah sambungan hadapan dari Pgpool ke PostgreSQL adalah bersamaan dengan:
  $$\text{Jumlah Sambungan} = \text{num\_init\_children} \times \text{max\_pool}$$
  Pastikan hasil darab ini tidak melebihi parameter `max_connections` yang dikonfigurasikan pada PostgreSQL.

---

## 6. Syor & Kerangka Kerja Keputusan

### Pilih Kluster MariaDB Galera + MaxScale jika:
* Anda memerlukan seni bina Aktif-Aktif di mana mana-mana nod pangkalan data boleh menerima penulisan semasa tetingkap penyelenggaraan bergilir (*rolling maintenance*).
* Beban kerja anda memerlukan penyalinan pensijilan terseganti merentas kesemua enjin storan nod secara terus dari kotak (*out-of-the-box*).
* Anda lebih gemar enjin penghalaan SQL MaxScale yang ringan dan modular.

### Pilih PostgreSQL (Penyalinan Penyiaran) + Pgpool-II jika:
* Anda mahukan solusi Lapisan 7 serba-boleh yang menyediakan Pemisahan Baca-Tulis, Pengumpulan Sambungan, dan Kegagalan Beralih HA dalam satu lapisan proksi tunggal.
* Anda memerlukan ciri-ciri canggih PostgreSQL (`JSONB`, `PostGIS`, sambungan/extensions) tanpa keperluan infrastruktur konsensus luaran (`etcd`, `Consul`).
* Anda mahukan redundansi proksi tempatan melalui Pgpool-II Watchdog tanpa perlu mengkonfigurasi perisian pengklusteran peringkat OS tambahan.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Berikan panduan langkah demi langkah untuk menguji senario failover automatik pada Pgpool-II Watchdog menggunakan arahan pcp_watchdog_info."*
2. *"Tunjukkan contoh Playbook Ansible untuk mengautomasikan penyebaran 3-nod MariaDB Galera Cluster bersama MaxScale pada AlmaLinux 10."*
3. *"Apakah langkah penalaan prestasi kernel Linux (sysctl) terbaik untuk mengendalikan beban pangkalan data PostgreSQL berprestasi tinggi?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
* [Dokumentasi Rasmi MariaDB MaxScale](https://mariadb.com/kb/en/maxscale/)
* [Dokumentasi Rasmi Pgpool-II Wiki](https://www.pgpool.net/mediawiki/index.php/Main_Page)
* [Panduan Penyalinan Penyiaran PostgreSQL](https://www.postgresql.org/docs/current/warm-standby.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
* **High Availability MySQL & MariaDB** oleh Charles Bell, Sveta Smirnova, dan Patrick Galbraith.
* **PostgreSQL High Performance** oleh Gregory Smith.
* **Panduan Praktikal Kebolehseediaan Tinggi Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
