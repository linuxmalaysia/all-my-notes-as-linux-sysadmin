---
name: "dsom-infrastructure-playbook-documenter"
okf_version: 0.1
type: skill
title: "DSOM Infrastructure Playbook Authoring & Automated Idempotency Gate (Rule 32.43 & Rule 32.44)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["ansible", "playbook", "idempotency", "cop", "dsom", "ai-forge"]
tags: ["ansible", "playbook", "validation", "idempotence", "redhat-cop", "zen-of-ansible"]
description: "Garis panduan dan kemahiran AI bagi penulisan, penyesuaian, pengesahan, dan audit Ansible Playbook berteraskan 5-Tier Validation Ladder, Idempotence Assertion, serta Red Hat CoP Good Practices."
resource: "file:///.agents/skills/dsom-infrastructure-playbook-documenter/SKILL.md"
---

# 🤖 DSOM Infrastructure Playbook Authoring & Automated Idempotency Gate

## 📌 Pengenalan & Kerangka Tadbir Urus
Kemahiran ini mentakrifkan piawaian penulisan, semakan, dan pautan automasi Ansible Playbook mengikut **Rule 32.43** (*Automated Ansible Playbook Validation Ladder & Idempotence Assertion Standard*) dan **Rule 32.44** (*Ansible Community AI-Forge & Red Hat CoP Automation Good Practices Standard*).

---

## 🪜 Fasa 4l: The 5-Tier Ascending Cost Validation Ladder (Rule 32.43)

Apabila Ejen AI menjana atau mengemaskini Playbook/Role Ansible, kod MESTI melepasi 5 tingkat pengesahan:

1. **Tier 1 (YAML Static Lint):** Semakan sintaks YAML asas (ms/sub-saat).
2. **Tier 2 (Ansible Syntax Check):** Execution `ansible-playbook <playbook.yml> --syntax-check` untuk mengesahkan blok task, struktur YAML, dan rujukan pemboleh ubah.
3. **Tier 3 (Ansible-Lint Production Profile):** Strict linting `ansible-lint --profile production` (penguatkuasaan Fully Qualified Collection Names `ansible.builtin.*`, nama tugas berhuruf besar, ketiadaan bare shell/command).
4. **Tier 4 (Check Mode / Dry Run):** `ansible-playbook --check --diff` terhadap inventori ujian untuk mengesan sebarang ralat runtime dan variasi konfigurasi tanpa mengubah sistem.
5. **Tier 5 (Two-Pass Execution & Idempotence Assertion):**
   - *Pass 1 (Converge):* Pelaksanaan pertama untuk mencapai keadaan yang diingini.
   - *Pass 2 (Assert Idempotency):* Pelaksanaan kedua mesti menghasilkan `changed=0, failed=0`. Sebarang `changed > 0` menandakan regresi prosedur yang mesti dibetulkan.

---

## 🛡️ Deterministic Pre-Execution Code Gates (Fast-Fail)
- **Modul FQCN:** Wajib menggunakan nama koleksi penuh (contoh: `ansible.builtin.package`, `ansible.builtin.service`, `ansible.builtin.copy`).
- **Garda Impotensi Task:** Prosedur bare `ansible.builtin.shell` atau `ansible.builtin.command` DILARANG sama sekali melainkan disertakan dengan penanda `creates`, `removes`, atau `changed_when`.
- **Pengurusan Rahsia:** Dilarang menggunakan kata laluan/kunci teks biasa. Task yang mengendalikan rahsia wajib menggunakan `no_log: true`.

---

## 📜 Fasa 4m: Red Hat CoP Authoring & Zen of Ansible Review Protocol (Rule 32.44)

### 1. Falsafah Zen of Ansible
- *Ansible bukan Python:* Elakkan pemprosesan gelung Jinja2 yang kompleks atau pemprosesan skrip dalam arahan task.
- *Playbook bukan program:* Elakkan rantaian `when` yang terlalu dalam dan penyalahgunaan aliran kawalan.
- *Isytihar (Declarative) melebihi Arahan (Imperative):* Utamakan modul khas berbanding `command`/`shell`/`raw`.

### 2. Standard Gaya Penulisan Red Hat CoP (14-Point Invariants)
1. Indentasi 2 ruang, sambungan fail `.yml` (bukan `.yaml`).
2. Format kamus YAML bagi argumen modul (bukan format rentetan `key=value`).
3. Nilai boolean `true`/`false` berhuruf kecil.
4. Penggunaan FQCN `ansible.builtin.*` untuk semua modul.
5. Nama task, play, dan block menggunakan ragam perintah berhuruf besar (*Imperative mood*, contoh: `Ensure nginx is installed`).
6. Parameter `state:` dinyatakan secara eksplisit (`present`, `absent`, `started`, `restarted`).
7. Penggunaan binaan moden `loop:` berbanding `with_*` yang telah lapuk.
8. Penetapan `failed_when:` dengan syarat status spesifik berbanding `ignore_errors: true`.
9. Awalan pemboleh ubah role (`<role_name>_...` bagi pemboleh ubah luaran, `__<role_name>_...` bagi pemstelar dalaman).
10. Pengepala fail konfigurasi: `{{ ansible_managed | comment }}` pada bahagian atas fail templat Jinja2.
11. Gaya `snake_case` untuk nama fail, pemboleh ubah, dan role.
12. Notasi fakta moden: `ansible_facts['...']` menggunakan kurungan siku berbanding pemboleh ubah terus.

---

## 📊 Matriks Semakan 14-Kategori CoP (Review Checklist)
Setiap penilaian kod Playbook mesti menilai 14 kategori berikut:
1. **YAML Style** (Indentasi, format dictionary)
2. **Naming Conventions** (Imperative, capitalized)
3. **Module Usage** (FQCN, declarative over shell)
4. **Task Structure** (Descriptive, minimal nesting)
5. **Handlers** (Triggering logic)
6. **Templates** (Jinja2 header `ansible_managed`)
7. **Variables** (Role prefixing, snake_case)
8. **Playbook Structure** (Imports/includes)
9. **Inventory** (Group vars, host vars separation)
10. **Error Handling** (failed_when, block/rescue)
11. **Idempotency** (creates/removes/changed_when, changed=0 on run 2)
12. **Argument Specs** (meta/argument_specs.yml)
13. **Tags** (Granular execution tags)
14. **Platform Support** (OS distribution branching via `ansible_facts['os_family']`)

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
