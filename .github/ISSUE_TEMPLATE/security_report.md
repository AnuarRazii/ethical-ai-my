---
name: "🔒 Laporan Keselamatan | Security Report"
about: "Laporkan kerentanan keselamatan atau isu perlindungan | Report a security vulnerability or protection issue"
title: '[SECURITY] '
labels: 'security'
assignees: 'AnuarRazii'

---

<!--
⚠️ AMARAN PENTING | IMPORTANT WARNING ⚠️

Jika ini adalah kerentanan keselamatan yang KRITIKAL atau SENSITIF yang boleh mendedahkan data
atau mengancam keselamatan sistem secara serius, JANGAN lapor secara awam di sini.
Hubungi penjaga secara peribadi terlebih dahulu melalui kaedah yang dinyatakan dalam SECURITY.md.

If this is a CRITICAL or SENSITIVE security vulnerability that could expose data or
seriously threaten system security, DO NOT report publicly here.
Contact maintainers privately first through methods described in SECURITY.md.

Untuk kerentanan yang tidak kritikal atau cadangan peningkatan keselamatan,
templat ini sesuai digunakan.

For non-critical vulnerabilities or security improvement suggestions,
this template is appropriate.
-->

## 📋 Maklumat Kebolehkesanan | Traceability Information

| Medan | Nilai |
|-------|-------|
| **Tarikh Laporan** | <!-- YYYY-MM-DD --> |
| **Dilaporkan Oleh** | <!-- @username atau "Tanpa Nama / Anonymous" --> |
| **Komponen Terjejas** | <!-- API / Scripts / Dokumentasi / Konfigurasi / Lain-lain --> |
| **Versi Terjejas** | <!-- e.g., v1.0 --> |
| **CVE (jika ada)** | <!-- CVE-YYYY-NNNNN atau "Belum ditentukan" --> |

---

## 🔴 Tahap Keterukan | Severity Level

- [ ] 🔴 **Kritikal (CVSS 9.0–10.0)** – Pendedahan data serius atau kompromi sistem penuh
- [ ] 🟠 **Tinggi (CVSS 7.0–8.9)** – Impak signifikan, boleh dieksploitasi dari jarak jauh
- [ ] 🟡 **Sederhana (CVSS 4.0–6.9)** – Impak terhad, memerlukan syarat tertentu
- [ ] 🟢 **Rendah (CVSS 0.1–3.9)** – Impak minimum, sukar dieksploitasi
- [ ] ℹ️ **Maklumat** – Cadangan peningkatan keselamatan sahaja

---

## 🔍 Penerangan Kerentanan | Vulnerability Description

Berikan penerangan yang jelas tentang isu keselamatan yang ditemui.
Provide a clear description of the security issue found.

### Jenis Kerentanan | Vulnerability Type

- [ ] Pendedahan data sensitif | Sensitive data exposure
- [ ] Kawalan akses tidak mencukupi | Insufficient access control
- [ ] Pengesahan input tidak sah | Improper input validation
- [ ] Suntikan (SQL, XSS, dll.) | Injection (SQL, XSS, etc.)
- [ ] Kerentanan pergantungan | Dependency vulnerability
- [ ] Konfigurasi tidak selamat | Insecure configuration
- [ ] Kelemahan kriptografi | Cryptographic weakness
- [ ] Lain-lain | Other: ___________

### Penerangan Terperinci | Detailed Description

---

## 🔁 Langkah Pengeksploitasian | Exploitation Steps

*Sila berhati-hati — hanya sertakan maklumat yang mencukupi untuk mengesahkan isu, bukan panduan pengeksploitasian penuh.*
*Please be careful — only include enough information to verify the issue, not a full exploitation guide.*

1. 
2. 
3. 

---

## 💥 Potensi Impak | Potential Impact

Apakah yang boleh berlaku jika kerentanan ini dieksploitasi?
What could happen if this vulnerability is exploited?

- [ ] Pendedahan data peribadi / Personal data exposure
- [ ] Akses tanpa kebenaran / Unauthorized access
- [ ] Gangguan perkhidmatan / Service disruption
- [ ] Manipulasi data / Data manipulation
- [ ] Impak reputasi / Reputational impact
- [ ] Pelanggaran pematuhan | Compliance violation (PDPA, ONSA 2025, dll.)

**Penerangan Impak | Impact Description:**

---

## 🌍 Persekitaran dan Konteks | Environment and Context

| Medan | Nilai |
|-------|-------|
| **Sistem Operasi** | |
| **Persekitaran** | <!-- Pembangunan / Ujian / Pengeluaran --> |
| **Konfigurasi** | |
| **Versi Kebergantungan** | |

---

## 🔗 Penjajaran dengan Piawaian Keselamatan | Alignment with Security Standards

Adakah isu ini berkaitan dengan bahagian SECURITY.md yang spesifik?
Does this issue relate to a specific section of SECURITY.md?

- [ ] Perlindungan Data dan Enkripsi | Data Protection and Encryption
- [ ] Kawalan Akses dan Pengesahan | Access Control and Authentication
- [ ] Keselamatan Sistem dan Pengurusan Kerentanan | System Security and Vulnerability Management
- [ ] Integriti Model dan Data | Model and Data Integrity
- [ ] Keselamatan Infrastruktur | Infrastructure Security
- [ ] Tindak Balas Insiden | Incident Response

**Rujukan Bahagian | Section Reference:**

---

## 💡 Pembetulan yang Dicadangkan | Suggested Fix

Jika anda mempunyai cadangan untuk menyelesaikan kerentanan ini, sila kongsikan.
If you have suggestions to fix this vulnerability, please share them.

---

## 📎 Bukti dan Artifak | Evidence and Artifacts

```
[Tampal bukti teknikal di sini — elakkan maklumat eksploitasi yang lengkap]
[Paste technical evidence here — avoid complete exploitation details]
```

---

## ⏰ Garis Masa Pendedahan | Disclosure Timeline

| Tarikh | Peristiwa |
|--------|----------|
| | Kerentanan ditemui |
| | Laporan dihantar |
| | Sasaran pembetulan (cadangan) |
| | Sasaran pendedahan awam (cadangan) |

---

## 📜 Rekod Audit Keselamatan | Security Audit Record

*Bahagian ini untuk kegunaan penjaga repositori. | This section is for maintainer use.*

| Medan | Nilai |
|-------|-------|
| **Tarikh Diterima** | |
| **Petugas Keselamatan** | |
| **ID Kerentanan** | SEC-YYYY-### |
| **Status** | [ ] Baharu [ ] Dalam Siasatan [ ] Disahkan [ ] Pembetulan Dalam Proses [ ] Selesai [ ] Ditolak |
| **CVSS Score** | |
| **Tarikh Pembetulan Dirancang** | |
| **PR Pembetulan** | |
| **Nota Keselamatan** | |

---

## ✔️ Senarai Semak Pelapor | Reporter Checklist

- [ ] Saya telah membaca [SECURITY.md](../../SECURITY.md)
- [ ] Ini bukan kerentanan kritikal yang memerlukan laporan peribadi
- [ ] Saya tidak akan mendedahkan butiran ini secara awam sebelum pembetulan tersedia
- [ ] Laporan ini dibuat dengan niat baik
- [ ] Saya bersetuju untuk bekerjasama dalam proses pengesahan dan pembetulan

---

*Ethical AI MY menghargai penyelidik keselamatan yang bertanggungjawab. Laporan anda membantu melindungi semua pengguna.*
*Ethical AI MY appreciates responsible security researchers. Your report helps protect all users.*

*Rujukan: [CONTRIBUTING.md](../CONTRIBUTING.md) | [SECURITY.md](../../SECURITY.md)*
