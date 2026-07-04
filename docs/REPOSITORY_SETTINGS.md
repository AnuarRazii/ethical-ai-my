# REPOSITORY_SETTINGS.md – Panduan Tetapan Keselamatan dan Tadbir Urus Repositori

**Ethical AI MY – Corporate-Grade Repository Governance Settings**

---

## Pengenalan | Introduction

Dokumen ini menerangkan semua tetapan keselamatan dan tadbir urus repositori yang diperlukan untuk **Ethical AI MY**. Tetapan ini memastikan pematuhan terhadap prinsip ONSA 2025, CPC, dan RMC MCMC.

This document describes all required repository security and governance settings for **Ethical AI MY**. These settings ensure compliance with ONSA 2025, CPC, and RMC MCMC principles.

> **Nota Automasi | Automation Note:**  
> Sebahagian tetapan dikuatkuasakan secara automatik melalui GitHub Actions workflows dan fail `.github/settings.yml`.  
> Some settings are automatically enforced via GitHub Actions workflows and `.github/settings.yml`.

---

## Ringkasan Status Tetapan | Settings Status Summary

| # | Tetapan | Kaedah Pelaksanaan | Status Automasi |
|---|---------|-------------------|----------------|
| 1 | Default branch: `main` | GitHub UI / API | ⚙️ Manual (sekali sahaja) |
| 2 | Release Immutability | Workflow + UI | ✅ Dikuatkuasakan oleh `release-immutability.yml` |
| 3 | DCO — Web-based contributions | Workflow + `.github/settings.yml` | ✅ Dikuatkuasakan oleh `dco.yml` + setting |
| 4 | Enable Rebase + Suggest Branch Update | `.github/settings.yml` + UI | ⚙️ Memerlukan probot/settings atau UI |
| 5 | Line Comments + LFS in Archives | GitHub UI | ⚙️ Manual (sekali sahaja) |

---

## Bahagian 1: Default Branch

### Keperluan | Requirement
Cawangan lalai mestilah `main`.

### Pelaksanaan Manual | Manual Steps

**GitHub UI:**
1. Pergi ke **Settings** → **General** → **Default branch**
2. Klik ikon pensel di sebelah nama cawangan semasa
3. Pilih atau taip `main`
4. Klik **Update**
5. Sahkan dengan klik **I understand, update the default branch**

**Pengesahan | Verification:**
```bash
gh api /repos/AnuarRazii/ethical-ai-my --jq '.default_branch'
# Output yang dijangka: "main"
```

**API (jika diperlukan):**
```bash
gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
  --field default_branch=main
```

---

## Bahagian 2: Release Immutability (Kebolehubahsuaian Keluaran)

### Keperluan | Requirement
Semua tag dan keluaran (releases) yang telah diterbitkan tidak boleh diubah, dipadam, atau ditarik balik selepas penerbitan.

### Pelaksanaan Automatik | Automatic Enforcement
Workflow **`release-immutability.yml`** secara automatik:
- Mengesan sebarang cubaan untuk mengedit atau memadamkan keluaran yang telah diterbitkan
- Mencipta isu audit dengan label `security` dan `priority: critical`
- Menyimpan rekod SHA tag setiap kali keluaran baharu diterbitkan

### Pelaksanaan Manual — Tag Protection Rules | Manual Steps — Tag Protection Rules

**GitHub UI (Disyorkan):**
1. Pergi ke **Settings** → **Rules** → **Rulesets**
2. Klik **New ruleset** → **New branch or tag ruleset**
3. Tetapkan:
   - **Ruleset Name:** `Release Tag Immutability`
   - **Target:** Tags
   - **Target pattern:** `v*` (semua tag versi)
4. Di bawah **Rules**, aktifkan:
   - ✅ **Restrict deletions** — Halang pemadaman tag
   - ✅ **Restrict updates** — Halang perubahan SHA tag
   - ✅ **Restrict creation** (pilihan) — Hadkan siapa boleh mencipta tag
5. Di bawah **Bypass**, tambah pengecualian jika perlu (tidak digalakkan)
6. Klik **Create**

**API:**
```bash
# Buat tag protection rule
gh api --method POST /repos/AnuarRazii/ethical-ai-my/tags/protection \
  --field pattern="v*"

# Atau via rulesets API (lebih komprehensif)
gh api --method POST /repos/AnuarRazii/ethical-ai-my/rulesets \
  --field name="Release Tag Immutability" \
  --field target="tag" \
  --field enforcement="active" \
  --field "conditions[ref_name][include][]=refs/tags/v*" \
  --field "rules[]=type:deletion" \
  --field "rules[]=type:update"
```

**Pengesahan | Verification:**
```bash
# Senarai tag protection rules
gh api /repos/AnuarRazii/ethical-ai-my/tags/protection
```

---

## Bahagian 3: Developer Certificate of Origin (DCO)

### Keperluan | Requirement
Semua sumbangan, terutama yang melalui editor web GitHub, mesti mengandungi tanda tangan DCO yang sah (`Signed-off-by:`).

### Pelaksanaan Automatik | Automatic Enforcement

**Workflow DCO (`dco.yml`):**
- Memeriksa semua komit dalam PR untuk kehadiran `Signed-off-by:` yang sah
- Menolak PR yang tidak mematuhi
- Meninggalkan komen pembantu dengan arahan pembetulan

**Tetapan Web Commit Sign-off:**

**GitHub UI:**
1. Pergi ke **Settings** → **General** → **Contributions**
2. Cari bahagian **"Contributions"** atau **"Pull Requests"**
3. Aktifkan ✅ **"Require contributors to sign off on web-based commits"**
4. Klik **Save**

> Ini akan memastikan editor web GitHub secara automatik menambahkan:
> `Signed-off-by: Nama Pengguna <emel@contoh.com>`
> kepada setiap komit yang dibuat melalui antara muka web.

**API:**
```bash
gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
  --field web_commit_signoff_required=true
```

**Tetapan dalam `.github/settings.yml`:**
```yaml
repository:
  web_commit_signoff_required: true
```

**Pengesahan | Verification:**
```bash
gh api /repos/AnuarRazii/ethical-ai-my --jq '.web_commit_signoff_required'
# Output yang dijangka: true
```

---

## Bahagian 4: Enable Rebase + Always Suggest Updating Branches

### Keperluan | Requirement
- Rebase merge mesti diaktifkan untuk mengekalkan sejarah Git yang bersih
- GitHub mesti sentiasa mencadangkan kemas kini cawangan PR kepada base terkini

### Pelaksanaan Manual | Manual Steps

**GitHub UI:**
1. Pergi ke **Settings** → **General** → **Pull Requests**
2. Di bawah **Allow rebase merging**:
   - ✅ Aktifkan **Allow rebase merging**
3. Di bawah **Always suggest updating pull request branches**:
   - ✅ Aktifkan **Always suggest updating pull request branches**
4. Klik **Save**

**API:**
```bash
gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
  --field allow_rebase_merge=true \
  --field allow_update_branch=true
```

**Tetapan dalam `.github/settings.yml`:**
```yaml
repository:
  allow_rebase_merge: true
  allow_update_branch: true
```

**Pengesahan | Verification:**
```bash
gh api /repos/AnuarRazii/ethical-ai-my \
  --jq '{allow_rebase_merge, allow_update_branch}'
# Output yang dijangka:
# {
#   "allow_rebase_merge": true,
#   "allow_update_branch": true
# }
```

---

## Bahagian 5: Allow Comments on Individual Lines + LFS in Archives

### 5a. Allow Comments on Individual Lines (Ulasan pada Baris Individu)

### Keperluan | Requirement
Pengulas PR mesti boleh membuat ulasan pada baris kod individu (inline comments).

### Maklumat | Information
Fungsi ini adalah **lalai** (enabled by default) dalam semua repositori GitHub dan tidak boleh dilumpuhkan melalui tetapan biasa. Ia adalah sebahagian daripada ciri semakan PR GitHub.

Jika ciri ini kelihatan tidak berfungsi, semak:
- Jenis semakan: Pastikan menggunakan **"Start a review"** bukan hanya komen biasa
- Perbezaan: Ulasan baris hanya tersedia pada paparan **"Files changed"** tab

### 5b. Git LFS Objects in Archives

### Keperluan | Requirement
Fail-fail yang disimpan dalam Git LFS mesti disertakan apabila pengguna memuat turun arkib repositori (ZIP/TAR.GZ).

### Pelaksanaan Manual | Manual Steps

**GitHub UI:**
1. Pergi ke **Settings** → **General** → **Archives**
2. Cari bahagian **"Archives"**
3. Aktifkan ✅ **"Include Git LFS objects in archives"**
4. Klik **Save**

> **Nota:** Tetapan ini memerlukan Git LFS diaktifkan untuk repositori.
> Jika belum diaktifkan, pergi ke **Settings** → **General** → **Archives** → **Git LFS** dan aktifkan.

**Pengesahan melalui .gitattributes:**
Pastikan fail `.gitattributes` mengandungi entri yang betul untuk fail LFS:
```
# Git LFS tracking
*.bin filter=lfs diff=lfs merge=lfs -text
*.pdf filter=lfs diff=lfs merge=lfs -text
```

---

## Senarai Semak Pengesahan Lengkap | Complete Verification Checklist

Gunakan senarai semak ini selepas melaksanakan semua tetapan:

### Tetapan GitHub UI
- [ ] **1. Default branch** — Ditetapkan kepada `main`
- [ ] **2. Tag Protection Rule** — Corak `v*` dilindungi daripada pemadaman dan kemas kini
- [ ] **3. Web commit sign-off** — `web_commit_signoff_required` diaktifkan
- [ ] **4a. Rebase merging** — `allow_rebase_merge` diaktifkan
- [ ] **4b. Suggest branch update** — `allow_update_branch` diaktifkan
- [ ] **5a. Line comments** — Tersedia secara lalai (tiada tindakan diperlukan)
- [ ] **5b. LFS in archives** — `Include Git LFS objects in archives` diaktifkan

### Tetapan Automatik (Workflows)
- [ ] **`dco.yml`** — Hadir dalam `.github/workflows/` ✅
- [ ] **`release-immutability.yml`** — Hadir dalam `.github/workflows/` ✅
- [ ] **`.github/settings.yml`** — Hadir dan dikonfigurasi ✅
- [ ] **`compliance.yml`** — Dikemas kini untuk memerlukan fail baharu ✅

### Pengesahan Branch Protection
- [ ] **Status check wajib** — `DCO Check / dco-check` diperlukan
- [ ] **Status check wajib** — `Release Immutability Guard / immutability-check` diperlukan
- [ ] **Kelulusan PR** — Sekurang-kurangnya 1 kelulusan diperlukan
- [ ] **Stale review dismissal** — Diaktifkan
- [ ] **Force push dihalang** — `allow_force_pushes: false`
- [ ] **Branch deletion dihalang** — `allow_deletions: false`

---

## Pemasangan probot/settings App (Disyorkan) | Installing probot/settings App (Recommended)

Untuk membolehkan `.github/settings.yml` dikuatkuasakan secara automatik:

1. Pergi ke: https://github.com/apps/settings
2. Klik **Install**
3. Pilih **Only select repositories** → `ethical-ai-my`
4. Klik **Install**

Selepas pemasangan, setiap push ke `main` akan menyegerakkan tetapan repositori dengan kandungan `.github/settings.yml`.

---

## Rekod Audit Pelaksanaan | Implementation Audit Record

| Tetapan | Dilaksanakan Oleh | Tarikh | Kaedah | Disahkan Oleh |
|---------|-----------------|--------|--------|--------------|
| DCO Workflow | GitHub Copilot Agent | 2026-07-02 | Commit workflow | |
| Release Immutability Workflow | GitHub Copilot Agent | 2026-07-02 | Commit workflow | |
| `.github/settings.yml` | GitHub Copilot Agent | 2026-07-02 | Commit file | |
| Default branch: main | | | GitHub UI/API | |
| Web commit sign-off required | | | GitHub UI/API | |
| Allow rebase merge | | | GitHub UI/API | |
| Allow update branch | | | GitHub UI/API | |
| Tag protection rules | | | GitHub UI/API | |
| LFS in archives | | | GitHub UI | |

---

## Rujukan | References

- [GOVERNANCE.md](../GOVERNANCE.md) — Model Tadbir Urus
- [SECURITY.md](../SECURITY.md) — Piawaian Keselamatan
- [CONTRIBUTING.md](../CONTRIBUTING.md) — Panduan Sumbangan
- [`.github/settings.yml`](../.github/settings.yml) — Konfigurasi Tetapan Repositori
- [`.github/workflows/dco.yml`](../.github/workflows/dco.yml) — Workflow Penguatkuasaan DCO
- [`.github/workflows/release-immutability.yml`](../.github/workflows/release-immutability.yml) — Workflow Kebolehubahsuaian Keluaran
- [GitHub REST API — Repository Settings](https://docs.github.com/en/rest/repos/repos#update-a-repository)
- [Developer Certificate of Origin](https://developercertificate.org)
- [probot/settings GitHub App](https://github.com/apps/settings)

---

**Ethical AI MY – Repository Security and Governance Settings**

*Versi 1.0 | Tarikh Kuat Kuasa: 2026-07-02*

*Selaras dengan ONSA 2025, CPC, dan RMC MCMC*
