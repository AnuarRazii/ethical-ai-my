# CONTRIBUTING.md – Panduan Sumbangan

**Ethical AI MY – Garis Panduan Sumbangan Profesional**

---

## Pengenalan | Introduction

Terima kasih kerana berminat menyumbang kepada **Ethical AI MY**. Repositori ini adalah rujukan awam untuk tadbir urus AI yang bertanggungjawab di Malaysia, selaras dengan prinsip ONSA 2025, CPC, dan RMC MCMC.

Thank you for your interest in contributing to **Ethical AI MY**. This repository serves as a public reference for responsible AI governance in Malaysia, aligned with ONSA 2025, CPC, and RMC MCMC principles.

Semua sumbangan mesti mencerminkan **aliran kerja profesional**, **tadbir urus gred-korporat**, dan **Prinsip Tatacara Kerja Etika AI Malaysia** — termasuk Keadilan, Ketelusan, Akauntabiliti, Privasi, dan Manfaat.

All contributions must reflect **professional workflow**, **corporate-grade governance**, and the **Malaysian Ethical AI Code of Practice Principles** — encompassing Fairness, Transparency, Accountability, Privacy, and Benefit.

---

## Jadual Kandungan | Table of Contents

1. [Kod Tatalaku | Code of Conduct](#1-kod-tatalaku--code-of-conduct)
2. [Jenis Sumbangan | Types of Contributions](#2-jenis-sumbangan--types-of-contributions)
3. [Persediaan Persekitaran | Environment Setup](#3-persediaan-persekitaran--environment-setup)
4. [Aliran Kerja Sumbangan | Contribution Workflow](#4-aliran-kerja-sumbangan--contribution-workflow)
5. [Piawaian Komit | Commit Standards](#5-piawaian-komit--commit-standards)
6. [Keperluan Dokumentasi | Documentation Requirements](#6-keperluan-dokumentasi--documentation-requirements)
7. [Penjajaran Etika | Ethical Alignment](#7-penjajaran-etika--ethical-alignment)
8. [Proses Semakan | Review Process](#8-proses-semakan--review-process)
9. [Kebolehkesanan dan Auditabiliti | Traceability and Auditability](#9-kebolehkesanan-dan-auditabiliti--traceability-and-auditability)
10. [Pengurusan Isu | Issue Management](#10-pengurusan-isu--issue-management)
11. [Atribusi dan Lesen | Attribution and Licensing](#11-atribusi-dan-lesen--attribution-and-licensing)
12. [Hubungi Kami | Contact Us](#12-hubungi-kami--contact-us)

---

## 1. Kod Tatalaku | Code of Conduct

Dengan menyumbang, anda bersetuju untuk mematuhi [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md). Tingkah laku yang tidak diterima hendaklah dilaporkan kepada penjaga repositori.

By contributing, you agree to abide by our [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md). Unacceptable behaviour should be reported to the repository maintainers.

---

## 2. Jenis Sumbangan | Types of Contributions

Kami mengalu-alukan pelbagai jenis sumbangan:

We welcome the following types of contributions:

| Jenis | Penerangan | Label Isu |
|-------|-----------|-----------|
| **Pembetulan Pepijat** | Membetulkan ralat dalam dokumentasi atau kod | `bug` |
| **Peningkatan Ciri** | Cadangan atau penambahan ciri baharu | `enhancement` |
| **Kerangka Etika** | Penambahbaikan prinsip atau garis panduan etika | `ethics` |
| **Tadbir Urus** | Kemas kini model atau mekanisme tadbir urus | `governance` |
| **Keselamatan** | Laporan kerentanan atau cadangan penambahbaikan | `security` |
| **Pematuhan** | Isu pematuhan, audit, dan kebolehkesanan | `compliance` |
| **Dokumentasi** | Kemas kini, terjemahan, atau penjelasan dokumentasi | `documentation` |
| **Kajian** | Kajian, penyelidikan, atau analisis berkaitan AI etika | `research` |

---

## 3. Persediaan Persekitaran | Environment Setup

### Prasyarat | Prerequisites

- Git ≥ 2.40
- Akaun GitHub yang aktif dan disahkan
- Pengetahuan asas tentang Markdown, JSON, dan YAML
- Kebiasaan dengan prinsip Etika AI Malaysia

### Langkah Persediaan | Setup Steps

```bash
# 1. Fork repositori ini di GitHub
# Fork this repository on GitHub

# 2. Klon fork anda | Clone your fork
git clone https://github.com/<your-username>/ethical-ai-my.git
cd ethical-ai-my

# 3. Tambah upstream remote | Add upstream remote
git remote add upstream https://github.com/AnuarRazii/ethical-ai-my.git

# 4. Sahkan remote | Verify remotes
git remote -v
```

---

## 4. Aliran Kerja Sumbangan | Contribution Workflow

### 4.1 Buat Isu Dahulu | Open an Issue First

**Sebelum** memulakan sebarang kerja, buka isu GitHub menggunakan templat yang sesuai:

**Before** starting any work, open a GitHub Issue using the appropriate template:

- 🐛 [Laporan Pepijat](https://github.com/AnuarRazii/ethical-ai-my/issues/new?template=bug_report.md)
- ✨ [Permintaan Ciri](https://github.com/AnuarRazii/ethical-ai-my/issues/new?template=feature_request.md)
- ⚖️ [Kebimbangan Etika](https://github.com/AnuarRazii/ethical-ai-my/issues/new?template=ethics_concern.md)
- 🔒 [Laporan Keselamatan](https://github.com/AnuarRazii/ethical-ai-my/issues/new?template=security_report.md)
- 🏛️ [Semakan Tadbir Urus](https://github.com/AnuarRazii/ethical-ai-my/issues/new?template=governance_review.md)
- 📋 [Isu Pematuhan/Audit](https://github.com/AnuarRazii/ethical-ai-my/issues/new?template=compliance_audit.md)

### 4.2 Konvensyen Penamaan Cawangan | Branch Naming Convention

Gunakan format berikut untuk nama cawangan. Format ini memastikan kebolehkesanan penuh dari cawangan ke isu:

Use the following format for branch names. This ensures full traceability from branch to issue:

```
<type>/<issue-number>-<short-description>
```

| Jenis | Bila Digunakan |
|-------|----------------|
| `fix/` | Pembetulan pepijat |
| `feat/` | Ciri baharu |
| `ethics/` | Penjajaran etika atau prinsip |
| `governance/` | Kemas kini tadbir urus |
| `security/` | Pembetulan keselamatan |
| `compliance/` | Pematuhan dan audit |
| `docs/` | Dokumentasi sahaja |
| `chore/` | Penyelenggaraan repositori |

**Contoh | Examples:**
```bash
git checkout -b fix/42-correct-fairness-definition
git checkout -b feat/17-add-bias-detection-guide
git checkout -b ethics/88-update-privacy-principle
git checkout -b docs/101-translate-governance-bm
```

### 4.3 Aliran Kerja Git | Git Workflow

```bash
# Sentiasa mulakan dari main yang terkini
# Always start from an up-to-date main
git fetch upstream
git checkout main
git merge upstream/main

# Buat cawangan baharu menggunakan konvensyen di atas
# Create a new branch using the convention above
git checkout -b fix/42-correct-fairness-definition

# Buat perubahan anda | Make your changes
# ...

# Tambah perubahan | Stage changes
git add <files>

# Komit menggunakan format konvensional | Commit using conventional format
git commit -m "fix(ethics): correct fairness definition for demographic parity"

# Tolak ke fork anda | Push to your fork
git push origin fix/42-correct-fairness-definition

# Buka Pull Request di GitHub | Open a Pull Request on GitHub
```

---

## 5. Piawaian Komit | Commit Standards

### Format Mesej Komit | Commit Message Format

Kami menggunakan **Conventional Commits** untuk memastikan kebolehkesanan dan auditabiliti:

We use **Conventional Commits** to ensure traceability and auditability:

```
<type>(<scope>): <short description>

[optional body]

[optional footer: refs #issue-number]
```

### Jenis Komit | Commit Types

| Jenis | Keterangan |
|-------|------------|
| `feat` | Ciri baharu |
| `fix` | Pembetulan pepijat |
| `docs` | Perubahan dokumentasi |
| `ethics` | Perubahan prinsip atau kerangka etika |
| `governance` | Kemas kini model tadbir urus |
| `security` | Pembetulan atau peningkatan keselamatan |
| `compliance` | Perubahan berkaitan pematuhan |
| `chore` | Penyelenggaraan, konfigurasi |
| `refactor` | Penstrukturan semula tanpa perubahan fungsi |

### Skop Komit | Commit Scopes

`ethics`, `governance`, `security`, `privacy`, `fairness`, `transparency`, `accountability`, `benefit`, `docs`, `ci`, `api`, `scripts`

### Contoh | Examples

```
feat(governance): add traceability matrix for stakeholder decisions

Implements a structured decision log format aligned with GOVERNANCE.md
Section 4, enabling full audit trails for cross-stakeholder issues.

refs #23
```

```
fix(ethics): correct accountability definition to include corrective procedures

The previous definition omitted corrective action procedures as required
by ETHICS.md Section 3. Updated to include all five implementation
requirements.

refs #67
```

### Peraturan Mesej Komit | Commit Message Rules

- Guna bahasa Inggeris untuk mesej komit (untuk kebolehkesanan antarabangsa)
- Tajuk tidak melebihi 72 aksara
- Guna kata kerja imperatif ("add", "fix", "update"), bukan past tense
- Sentiasa rujuk nombor isu dalam footer
- Jangan akhiri tajuk dengan noktah

---

## 6. Keperluan Dokumentasi | Documentation Requirements

Semua perubahan **mesti** disertakan dengan dokumentasi yang mencukupi. Ini adalah keperluan tadbir urus, bukan pilihan.

All changes **must** be accompanied by adequate documentation. This is a governance requirement, not optional.

### Senarai Semak Dokumentasi | Documentation Checklist

- [ ] **Penerangan perubahan** yang jelas dalam Pull Request
- [ ] **Kemas kini dokumen berkaitan** (ETHICS.md, GOVERNANCE.md, dll.) jika berkenaan
- [ ] **Komentar dalam kod** untuk perubahan teknikal yang kompleks
- [ ] **Rujukan kepada prinsip etika** yang berkaitan
- [ ] **Rekod jejak perubahan** dalam RELEASE_NOTES.md jika perubahan signifikan
- [ ] **Atribusi sumber** jika menggunakan bahan luaran

### Standard Dokumentasi | Documentation Standards

- Gunakan Markdown dengan tajuk hierarki yang jelas
- Tulis dalam dwibahasa (Bahasa Malaysia dan Bahasa Inggeris) jika memungkinkan
- Dokumentasi dasar mesti mengandungi nombor versi dan tarikh kuat kuasa
- Sertakan rujukan silang kepada dokumen berkaitan

---

## 7. Penjajaran Etika | Ethical Alignment

Setiap sumbangan mesti dinilai terhadap lima prinsip teras Ethical AI MY:

Every contribution must be assessed against the five core Ethical AI MY principles:

### Prinsip Penilaian | Assessment Principles

| # | Prinsip | Soalan Panduan |
|---|---------|----------------|
| 1 | **Keadilan (Fairness)** | Adakah perubahan ini memastikan layanan saksama? Adakah ia mengurangkan berat sebelah? |
| 2 | **Ketelusan (Transparency)** | Adakah perubahan ini meningkatkan kejelasan? Adakah jejak audit tersedia? |
| 3 | **Akauntabiliti (Accountability)** | Adakah tanggungjawab ditetapkan dengan jelas? Adakah mekanisme pembetulan wujud? |
| 4 | **Privasi (Privacy)** | Adakah data peribadi dilindungi? Adakah had data dipatuhi? |
| 5 | **Manfaat (Benefit)** | Adakah perubahan ini memberi impak positif? Adakah risiko telah dinilai? |

Semua penyumbang mesti mendokumentasikan penjajaran etika dalam templat Pull Request.

All contributors must document ethical alignment in the Pull Request template.

---

## 8. Proses Semakan | Review Process

### Peringkat Semakan | Review Stages

```
Isu Dibuka → Pengesahan → Pembangunan → PR Dibuka → Semakan Kod → Semakan Etika → Semakan Tadbir Urus → Cantum
Issue Opened → Validation → Development → PR Opened → Code Review → Ethics Review → Governance Review → Merge
```

### SLA Semakan | Review SLA

| Jenis Perubahan | Masa Semakan Sasaran |
|-----------------|---------------------|
| Pembetulan pepijat dokumentasi | 3 hari bekerja |
| Peningkatan dokumentasi | 5 hari bekerja |
| Perubahan prinsip etika | 10 hari bekerja |
| Kemas kini model tadbir urus | 14 hari bekerja |
| Perubahan keselamatan kritikal | 24 jam |

### Kriteria Kelulusan | Approval Criteria

Sebuah PR dianggap sedia untuk digabungkan apabila:

A PR is considered ready to merge when:

- [ ] Sekurang-kurangnya **1 ulasan kelulusan** daripada penjaga
- [ ] Semua **semakan CI** lulus
- [ ] **Penjajaran etika** didokumentasikan dan diluluskan
- [ ] **Piawaian dokumentasi** dipenuhi
- [ ] **Tiada konflik cantum** yang belum diselesaikan
- [ ] **Atribusi** disahkan dan betul

### Proses Semakan Etika | Ethics Review Process

Untuk perubahan yang mempengaruhi prinsip etika atau dasar tadbir urus, semakan tambahan diperlukan:

For changes affecting ethical principles or governance policy, additional review is required:

1. Penilai akan menilai sumbangan terhadap [ETHICS.md](./ETHICS.md)
2. Sebarang konflik etika mesti didokumentasikan dan diselesaikan
3. Keputusan semakan etika direkodkan dalam ulasan PR untuk audit trail

---

## 9. Kebolehkesanan dan Auditabiliti | Traceability and Auditability

Kebolehkesanan adalah teras kepada tadbir urus gred-korporat. Setiap perubahan mestilah boleh dijejaki dari asal usul hingga pelaksanaan.

Traceability is core to corporate-grade governance. Every change must be traceable from origin to implementation.

### Matriks Kebolehkesanan | Traceability Matrix

```
Keperluan → Isu → Cawangan → Komit → PR → Cantum → Catatan Keluaran
Requirement → Issue → Branch → Commit → PR → Merge → Release Notes
```

### Rekod Audit Wajib | Mandatory Audit Records

Setiap sumbangan signifikan mesti mengandungi:

Every significant contribution must contain:

| Elemen | Lokasi | Tujuan |
|--------|--------|--------|
| Nombor Isu | Nama cawangan, mesej komit, penerangan PR | Rujukan silang |
| ID Penyumbang | Mesej komit Git, metadata PR | Akauntabiliti |
| Tarikh dan Masa | Metadata komit Git | Jejak temporal |
| Penilai | Ulasan PR GitHub | Pengawasan |
| Keputusan Semakan Etika | Ulasan PR | Penjajaran prinsip |
| Versi Dokumen | Fail yang diubah | Versioning |

### Konvensyen Versi | Version Convention

Dokumen dasar menggunakan format: `vMAJOR.MINOR.PATCH | YYYY-MM-DD`

- **MAJOR**: Perubahan asas kepada prinsip atau model tadbir urus
- **MINOR**: Penambahan ciri atau perluasan skop
- **PATCH**: Pembetulan, penjelasan, atau kemas kini kecil

---

## 10. Pengurusan Isu | Issue Management

### Templat Isu | Issue Templates

Kami menyediakan templat isu yang komprehensif untuk memastikan maklumat yang mencukupi bagi kebolehkesanan dan pengurusan:

We provide comprehensive issue templates to ensure sufficient information for traceability and management:

| Templat | Guna Untuk |
|---------|-----------|
| 🐛 Laporan Pepijat | Melaporkan pepijat atau ralat |
| ✨ Permintaan Ciri | Mencadangkan ciri baharu |
| ⚖️ Kebimbangan Etika | Melaporkan isu penjajaran etika |
| 🔒 Laporan Keselamatan | Melaporkan kerentanan keselamatan |
| 🏛️ Semakan Tadbir Urus | Mencadangkan semakan dasar atau model |
| 📋 Isu Pematuhan/Audit | Melaporkan isu pematuhan atau jurang audit |

### Label Isu | Issue Labels

| Label | Warna | Keterangan |
|-------|-------|------------|
| `bug` | Merah | Pepijat atau ralat |
| `enhancement` | Biru | Peningkatan atau ciri baharu |
| `ethics` | Ungu | Berkaitan prinsip etika |
| `governance` | Emas | Berkaitan tadbir urus |
| `security` | Oren Gelap | Isu keselamatan |
| `compliance` | Hijau Tua | Isu pematuhan dan audit |
| `documentation` | Biru Muda | Kemas kini dokumentasi |
| `priority: critical` | Merah Gelap | Memerlukan tindakan segera |
| `priority: high` | Oren | Keutamaan tinggi |
| `priority: medium` | Kuning | Keutamaan sederhana |
| `priority: low` | Hijau | Keutamaan rendah |
| `status: under-review` | Abu-abu | Sedang disemak |
| `status: approved` | Hijau Terang | Diluluskan untuk pelaksanaan |
| `status: blocked` | Merah | Disekat oleh halangan |

---

## 11. Atribusi dan Lesen | Attribution and Licensing

### Lesen | License

Semua sumbangan kepada repositori ini dilesen di bawah **Creative Commons Attribution 4.0 International (CC BY 4.0)** melainkan dinyatakan sebaliknya.

All contributions to this repository are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)** unless otherwise stated.

Dengan menyerahkan sumbangan, anda bersetuju bahawa:

By submitting a contribution, you agree that:

1. Anda adalah pengarang asal atau mempunyai kebenaran untuk menyumbang bahan tersebut
2. Anda memberi kebenaran untuk menerbitkan bahan tersebut di bawah CC BY 4.0
3. Semua bahan luaran yang digunakan telah diatribusikan dengan betul

### Keperluan Atribusi | Attribution Requirements

- Sertakan atribusi dalam badan PR jika menggunakan bahan daripada sumber luar
- Rujuk [ATTRIBUTION.md](./ATTRIBUTION.md) untuk panduan atribusi terperinci
- Elakkan bahan berhak cipta tanpa kebenaran eksplisit

---

## 12. Hubungi Kami | Contact Us

### Saluran Komunikasi | Communication Channels

| Tujuan | Saluran |
|--------|---------|
| Soalan umum | [GitHub Discussions](https://github.com/AnuarRazii/ethical-ai-my/discussions) |
| Laporan pepijat / cadangan | [GitHub Issues](https://github.com/AnuarRazii/ethical-ai-my/issues) |
| Laporan keselamatan sensitif | Rujuk [SECURITY.md](./SECURITY.md) |
| Pelanggaran Kod Tatalaku | Rujuk [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) |

### Penjaga Repositori | Repository Maintainers

- **@AnuarRazii** – Penjaga Utama / Lead Maintainer

---

## Rujukan | References

- [ETHICS.md](./ETHICS.md) – Kerangka Etika / Ethical Framework
- [GOVERNANCE.md](./GOVERNANCE.md) – Model Tadbir Urus / Governance Model
- [SECURITY.md](./SECURITY.md) – Piawaian Keselamatan / Security Standards
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) – Kod Tatalaku / Code of Conduct
- [ATTRIBUTION.md](./ATTRIBUTION.md) – Keperluan Atribusi / Attribution Requirements
- [RELEASE_NOTES.md](./RELEASE_NOTES.md) – Nota Keluaran / Release Notes

---

**Ethical AI MY – Panduan Sumbangan Profesional**

*Versi 1.0 | Tarikh Kuat Kuasa: 2026-07-02*

*Selaras dengan ONSA 2025, CPC, dan RMC MCMC*
