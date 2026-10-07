---
name: solusi-pangkalan-data-ha
description: Kemahiran mereka bentuk dan menyebarkan Solusi Pangkalan Data Kebolehseediaan
  Tinggi Enterprise (MariaDB Galera + MaxScale lwn. PostgreSQL HA + Pgpool-II) mengikut
  standard NOSS CU03 / WA05.
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
okf_version: '0.2'
spec_version: '0.2'
status: stable
stale_after: '2027-12-31'
generated:
  by: NOSS Linux Malaysia / Harisfazillah Jamel
  at: '2026-10-02T08:46:00Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
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
type: agent_skill
title: solusi-pangkalan-data-ha
---

# Kemahiran AI: Solusi Pangkalan Data Kebolehseediaan Tinggi Enterprise (MariaDB Galera + MaxScale vs PostgreSQL HA + Pgpool-II)

## 📌 Gambaran Keseluruhan

Kemahiran ini membimbing ejen AI dalam mereka bentuk, mengkonfigurasi, dan menyebarkan seni bina pangkalan data kebolehseediaan tinggi (High Availability - HA) gred enterprise menggunakan proksi Lapisan 7 (L7 SQL-aware proxies) berasaskan **NOSS CU03 WA05**.

---

## 🛠️ Modul 1: MariaDB Galera Cluster + MaxScale

### 1.1 Konfigurasi WSREP Galera (`/etc/my.cnf.d/galera.cnf`)

```ini
[mysqld]
binlog_format=ROW
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2

# Tetapan asas ketahanan data ACID (1 = flushed on commit)
innodb_flush_log_at_trx_commit=1

# WSREP Provider Settings
wsrep_on=ON
wsrep_provider=/usr/lib64/galera-4/libgalera_smm.so
wsrep_cluster_name="mariadb_ha_cluster"
wsrep_cluster_address="gcomm://10.0.1.11,10.0.1.12,10.0.1.13"

# Node Configuration
wsrep_node_address="10.0.1.11"
wsrep_node_name="db-node-01"
wsrep_sst_method=mariabackup
wsrep_sst_auth="sstuser:<SECURE_SST_PASSWORD>"
```

### 1.2 Konfigurasi MaxScale (`/etc/maxscale.cnf`)

```ini
[maxscale]
threads=auto

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

[Galera-Monitor]
type=monitor
module=galeramon
servers=db-node-1, db-node-2, db-node-3
user=maxscale
password=<MAXSCALE_PASSWORD>
monitor_interval=2000ms
disable_master_failback=1

[Read-Write-Service]
type=service
router=readwritesplit
servers=db-node-1, db-node-2, db-node-3
user=maxscale
password=<MAXSCALE_PASSWORD>

[Read-Write-Listener]
type=listener
service=Read-Write-Service
protocol=MariaDBClient
port=3306
```

---

## 🛠️ Modul 2: PostgreSQL Streaming Replication + Pgpool-II Watchdog

### 2.1 Konfigurasi Pgpool-II (`/etc/pgpool-II/pgpool.conf`)

```ini
listen_addresses = '*'
port = 9999
pcp_port = 9898

backend_clustering_mode = 'streaming_replication'
master_slave_mode = on
master_slave_sub_mode = 'stream'

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

num_init_children = 32
max_pool = 4
connection_cache = on

load_balance_mode = on
health_check_period = 5
health_check_timeout = 5
health_check_max_retries = 3
health_check_user = 'pgpool'
health_check_password = '<PGPOOL_PASSWORD>'
health_check_database = 'postgres'

failover_command = '/etc/pgpool-II/failover.sh %d %h %p %D %m %H %M %P'
follow_primary_command = '/etc/pgpool-II/follow_primary.sh %d %h %p %D %m %H %M %P'

use_watchdog = on
wd_hostname = '10.0.2.21'
wd_port = 9000
delegate_IP = '10.0.2.100'
wd_lifecheck_method = 'heartbeat'
wd_interval = 2
wd_auth_key = '<WATCHDOG_SECRET_KEY>'
```

### 2.2 Skrip Failover Automatik (`/etc/pgpool-II/failover.sh`)

```bash
#!/usr/bin/env bash
FAILED_NODE_ID="$1"
FAILED_HOST="$2"
NEW_MASTER_ID="$5"
NEW_MASTER_HOST="$6"
OLD_PRIMARY_ID="$8"

LOGFILE="/var/log/pgpool/failover.log"
PGHOME="${PGHOME:-/usr/lib/postgresql/15}"
PGDATA="${PGDATA:-/var/lib/postgresql/15/main}"

echo "[$(date)] Cetusan kegagalan beralih. Nod Gagal: ${FAILED_NODE_ID} (${FAILED_HOST}). Utama Lama: ${OLD_PRIMARY_ID}" >> "$LOGFILE"

if [ "$FAILED_NODE_ID" -eq "$OLD_PRIMARY_ID" ]; then
    echo "[$(date)] Memajukan nod Penantian ${NEW_MASTER_ID} (${NEW_MASTER_HOST}) kepada Utama..." >> "$LOGFILE"
    ssh -i /var/lib/postgresql/.ssh/id_rsa postgres@"${NEW_MASTER_HOST}" \
        "${PGHOME}/bin/pg_ctl promote -D ${PGDATA}"
    if [ $? -eq 0 ]; then
        echo "[$(date)] Berjaya memajukan nod ${NEW_MASTER_HOST} kepada Utama." >> "$LOGFILE"
        exit 0
    else
        echo "[$(date)] RALT: Gagal memajukan nod ${NEW_MASTER_HOST}!" >> "$LOGFILE"
        exit 1
    fi
else
    echo "[$(date)] Nod gagal ${FAILED_NODE_ID} ialah nod Penantian. Tiada pemajuan diperlukan." >> "$LOGFILE"
    exit 0
fi
```

### 2.3 Skrip Penyelarasan Semula Standby (`/etc/pgpool-II/follow_primary.sh`)

```bash
#!/usr/bin/env bash
set -e

DETACHED_NODE_ID="$1"
DETACHED_HOST="$2"
NEW_MASTER_ID="$5"
NEW_MASTER_HOST="$6"
OLD_PRIMARY_ID="$8"

LOGFILE="/var/log/pgpool/follow_primary.log"
PGHOME="${PGHOME:-/usr/lib/postgresql/15}"
PGDATA="${PGDATA:-/var/lib/postgresql/15/main}"

echo "[$(date)] Menjalankan follow_primary bagi nod ${DETACHED_NODE_ID} (${DETACHED_HOST}) menyertai ${NEW_MASTER_HOST}..." >> "$LOGFILE"

if [ "$DETACHED_NODE_ID" -eq "$OLD_PRIMARY_ID" ]; then
    echo "[$(date)] Menghentikan bekas Utama ${DETACHED_HOST} sebelum penyelarasan semula..." >> "$LOGFILE"
    if ! ssh -i /var/lib/postgresql/.ssh/id_rsa postgres@"${DETACHED_HOST}" \
        "${PGHOME}/bin/pg_ctl stop -m immediate -D ${PGDATA}"; then
        echo "[$(date)] RALT: Gagal menghentikan perkhidmatan pada ${DETACHED_HOST}" >> "$LOGFILE"
        exit 1
    fi
fi

echo "[$(date)] Eksekusi pg_rewind pada ${DETACHED_HOST}..." >> "$LOGFILE"
if ! ssh -i /var/lib/postgresql/.ssh/id_rsa postgres@"${DETACHED_HOST}" \
    "${PGHOME}/bin/pg_rewind --target-pgdata=${PGDATA} --write-recovery-conf --source-server='host=${NEW_MASTER_HOST} port=5432 user=postgres'"; then
    echo "[$(date)] RALT: pg_rewind gagal pada ${DETACHED_HOST}" >> "$LOGFILE"
    exit 1
fi

if ! ssh -i /var/lib/postgresql/.ssh/id_rsa postgres@"${DETACHED_HOST}" \
    "${PGHOME}/bin/pg_ctl start -D ${PGDATA}"; then
    echo "[$(date)] RALT: Gagal memulakan semula PostgreSQL pada ${DETACHED_HOST}" >> "$LOGFILE"
    exit 1
fi

sleep 3
if ! ssh -i /var/lib/postgresql/.ssh/id_rsa postgres@"${DETACHED_HOST}" \
    "${PGHOME}/bin/pg_isready -h localhost -p 5432"; then
    echo "[$(date)] RALT: Nod ${DETACHED_HOST} belum sedia untuk sambungan" >> "$LOGFILE"
    exit 1
fi

pcp_attach_node -w -h localhost -p 9898 -U pgpool "${DETACHED_NODE_ID}"

echo "[$(date)] Selesai penyelarasan semula dan penempelan nod ${DETACHED_HOST} ke Pgpool-II." >> "$LOGFILE"
exit 0
```

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bagaimanakah cara mengkonfigurasikan SSL/TLS pada komunikasi backend antara Pgpool-II dan PostgreSQL?"*
2. *"Jelaskan kaedah menguji beban (load testing) menggunakan pgbench melalui VIP Pgpool-II."*
3. *"Apakah langkah-langkah menangani split-brain pada Galera Cluster jika 2 nod terpisah daripada rangkaian?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi MariaDB MaxScale](https://mariadb.com/kb/en/maxscale/)
- [Dokumentasi Pgpool-II](https://www.pgpool.net/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **High Availability MySQL & MariaDB** oleh Charles Bell.
- **PostgreSQL High Performance** oleh Gregory Smith.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
