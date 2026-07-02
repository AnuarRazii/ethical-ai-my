# REPOSITORY_SETTINGS.md – Panduan Tetapan Keselamatan dan Tadbir Urus Repositori  
# REPOSITORY_SETTINGS.md – Repository Security and Governance Settings Guide

**Ethical AI MY – Repository Security and Governance Settings**  
**Version:** 1.1.0  
**Tarikh Kuat Kuasa | Effective Date:** 2026-07-02  
**Kitaran Semakan | Review Cycle:** Suku Tahunan (Quarterly)

---

## 0) Jadual Kandungan | Table of Contents

1. [Pengenalan | Introduction](#1-pengenalan--introduction)  
2. [Skop & Kebolehgunaan | Scope & Applicability](#2-skop--kebolehgunaan--scope--applicability)  
3. [Kata Kunci Normatif | Normative Keywords](#3-kata-kunci-normatif--normative-keywords)  
4. [Peranan & Pemilikan Kawalan | Roles & Control Ownership](#4-peranan--pemilikan-kawalan--roles--control-ownership)  
5. [Control Baseline Matrix](#5-control-baseline-matrix)  
6. [Tetapan Terperinci | Detailed Settings](#6-tetapan-terperinci--detailed-settings)  
   - 6.1 [Default Branch](#61-default-branch)  
   - 6.2 [Release Immutability](#62-release-immutability)  
   - 6.3 [Developer Certificate of Origin (DCO)](#63-developer-certificate-of-origin-dco)  
   - 6.4 [Rebase Merge + Suggest Branch Update](#64-rebase-merge--suggest-branch-update)  
   - 6.5 [Line Comments + Git LFS in Archives](#65-line-comments--git-lfs-in-archives)  
7. [Standard Minimum Branch Protection / Ruleset](#7-standard-minimum-branch-protection--ruleset)  
8. [Automated Verification Script (gh CLI)](#8-automated-verification-script-gh-cli)  
9. [Proses Pengecualian (Waiver) | Exception Process](#9-proses-pengecualian-waiver--exception-process)  
10. [Audit Evidence Register](#10-audit-evidence-register)  
11. [Keserasian Pelan & Had Platform | Plan Compatibility & Platform Constraints](#11-keserasian-pelan--had-platform--plan-compatibility--platform-constraints)  
12. [Rujukan | References](#12-rujukan--references)  
13. [Document Governance & Change Log](#13-document-governance--change-log)

---

## 1) Pengenalan | Introduction

Dokumen ini mentakrifkan tetapan keselamatan dan tadbir urus repositori GitHub untuk **Ethical AI MY** secara audit-ready dan boleh diverifikasi.  
This document defines GitHub repository security and governance settings for **Ethical AI MY** in an audit-ready and verifiable manner.

Dokumen ini menyokong pematuhan kepada prinsip **ONSA 2025**, **CPC**, dan **RMC MCMC** melalui kombinasi tetapan UI, API, workflow automasi, dan konfigurasi `.github/settings.yml`.  
This document supports alignment with **ONSA 2025**, **CPC**, and **RMC MCMC** principles through UI/API settings, workflow automation, and `.github/settings.yml`.

---

## 2) Skop & Kebolehgunaan | Scope & Applicability

**Repositori | Repository:** `AnuarRazii/ethical-ai-my`  
**Model pemilikan | Ownership model:** User-owned repository (bukan organization-owned)  
**Keterlihatan | Visibility:** Public (rujuk tetapan semasa repo)

### Skop
Polisi ini terpakai kepada:
- cawangan lalai `main`,
- semua pull request ke cawangan terlindung,
- semua release/tag versi (`v*`),
- semua sumbangan kod (termasuk web-based commits).

This policy applies to:
- default branch `main`,
- all pull requests into protected branches,
- all version release tags (`v*`),
- all code contributions (including web-based commits).

---

## 3) Kata Kunci Normatif | Normative Keywords

- **MUST**: Keperluan wajib pematuhan.  
- **SHOULD**: Amalan sangat disyorkan; penyimpangan perlu justifikasi.  
- **OPTIONAL**: Pilihan berdasarkan keperluan operasi.

---

## 4) Peranan & Pemilikan Kawalan | Roles & Control Ownership

| Peranan | Tanggungjawab Utama |
|---|---|
| Repo Admin | Melaksanakan tetapan UI/API, rulesets, branch protection |
| Security Maintainer | Menyelenggara workflow keselamatan dan semakan status |
| Compliance Owner | Mengesahkan bukti audit, semakan berkala, waiver review |
| Release Manager | Tadbir tag/release dan rekod immutability |

---

## 5) Control Baseline Matrix

| Control ID | Setting | Expected Value | Enforcement Method | Policy Level |
|---|---|---|---|---|
| EAI-RS-001 | Default branch | `main` | Manual (sekali) + API verify | MUST |
| EAI-RS-002 | Release tag immutability | Tag `v*` tidak boleh update/delete | Ruleset/Tag protection + workflow guard | MUST |
| EAI-RS-003 | Web commit signoff | `web_commit_signoff_required=true` | `.github/settings.yml` + API | MUST |
| EAI-RS-004 | DCO commit validation | Semua commit PR ada `Signed-off-by:` sah | `dco.yml` status check | MUST |
| EAI-RS-005 | Rebase merge | `allow_rebase_merge=true` | `.github/settings.yml` + API | SHOULD |
| EAI-RS-006 | Suggest branch updates | `allow_update_branch=true` | `.github/settings.yml` + API | SHOULD |
| EAI-RS-007 | Inline line comments | Tersedia pada tab Files changed | Built-in GitHub behavior | MUST |
| EAI-RS-008 | LFS objects in archives | Enabled | UI setting + `.gitattributes` consistency | SHOULD |
| EAI-RS-009 | Required checks for main | DCO + immutability checks required | Branch protection / Ruleset | MUST |
| EAI-RS-010 | Force push & deletion guard | Disabled | Branch protection / Ruleset | MUST |

---

## 6) Tetapan Terperinci | Detailed Settings

## 6.1 Default Branch

### Requirement
- Cawangan lalai repositori **MUST** ditetapkan kepada `main`.

### Implementation
**UI:** Settings → General → Default branch → pilih `main`  
**API:**
```bash
gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
  --field default_branch=main
```

### Verification
```bash
gh api /repos/AnuarRazii/ethical-ai-my --jq '.default_branch'
# Expected: "main"
```

### Evidence
- Output command di atas
- Screenshot halaman Settings > General > Default branch

### Owner
- Repo Admin

---

## 6.2 Release Immutability

### Requirement
- Tag/release diterbitkan **MUST NOT** dipadam atau diubah SHA selepas publish.

### Implementation
1. **Ruleset (disyorkan)** untuk target `tag` pattern `refs/tags/v*`:
   - Restrict deletions = ON
   - Restrict updates = ON
2. Workflow `release-immutability.yml`:
   - audit event edit/delete release,
   - cipta isu audit jika pelanggaran,
   - rekod snapshot metadata tag/release.

**API contoh (legacy tag protection):**
```bash
gh api --method POST /repos/AnuarRazii/ethical-ai-my/tags/protection \
  --field pattern='v*'
```

> Nota: Legacy tag protection lebih terhad; Rulesets lebih menyeluruh jika tersedia.

### Verification
```bash
gh api /repos/AnuarRazii/ethical-ai-my/tags/protection
# Expected: pattern v* exists (legacy), atau semak rulesets aktif untuk refs/tags/v*
```

### Evidence
- URL ruleset/tag-protection
- URL workflow runs `release-immutability.yml`
- Isu audit (jika ada pelanggaran simulasi)

### Owner
- Release Manager + Security Maintainer

---

## 6.3 Developer Certificate of Origin (DCO)

### Requirement
- Semua commit dalam PR **MUST** ada trailer `Signed-off-by: Name <email>` yang sah.
- Web-based commit signoff **MUST** diaktifkan.

### Implementation
1. Workflow `.github/workflows/dco.yml` memeriksa semua commit PR.
2. Repository setting:
```yaml
repository:
  web_commit_signoff_required: true
```
3. API:
```bash
gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
  --field web_commit_signoff_required=true
```

### Verification
```bash
gh api /repos/AnuarRazii/ethical-ai-my --jq '.web_commit_signoff_required'
# Expected: true
```

### Remediation (Contributor Quick Fix)
**Commit terakhir:**
```bash
git commit --amend --signoff --no-edit
git push --force-with-lease
```

**Beberapa commit (interactive rebase):**
```bash
git rebase -i origin/main
# tandakan commit sebagai edit
git commit --amend --signoff --no-edit
git rebase --continue
git push --force-with-lease
```

### Evidence
- Status check `DCO Check / dco-check` hijau
- API output `web_commit_signoff_required=true`

### Owner
- Security Maintainer

---

## 6.4 Rebase Merge + Suggest Branch Update

### Requirement
- `allow_rebase_merge` **SHOULD** diaktifkan.
- `allow_update_branch` **SHOULD** diaktifkan.

### Implementation
```bash
gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
  --field allow_rebase_merge=true \
  --field allow_update_branch=true
```

`.github/settings.yml`:
```yaml
repository:
  allow_rebase_merge: true
  allow_update_branch: true
```

### Verification
```bash
gh api /repos/AnuarRazii/ethical-ai-my \
  --jq '{allow_rebase_merge,allow_update_branch}'
# Expected:
# {"allow_rebase_merge":true,"allow_update_branch":true}
```

### Evidence
- API output
- Screenshot Settings > Pull Requests

### Owner
- Repo Admin

---

## 6.5 Line Comments + Git LFS in Archives

### 6.5a Line Comments

#### Requirement
- Keupayaan ulasan pada baris individu PR **MUST** tersedia.

#### Implementation
- Tiada tetapan khas; ini ciri default GitHub PR review (tab **Files changed**).

#### Verification
- Buka PR → Files changed → hover line → ikon `+` untuk komen muncul.

#### Owner
- Repo Admin (monitoring only)

---

### 6.5b Include Git LFS Objects in Archives

#### Requirement
- LFS objects dalam arkib ZIP/TAR **SHOULD** diaktifkan jika repo guna LFS.

#### Implementation
UI: Settings → General → Archives → enable **Include Git LFS objects in archives**

`.gitattributes` mesti konsisten:
```gitattributes
*.bin filter=lfs diff=lfs merge=lfs -text
*.pdf filter=lfs diff=lfs merge=lfs -text
```

#### Verification
- Download Source Code ZIP dan sahkan objek LFS tidak tinggal pointer text sahaja.
- Semak fail `.gitattributes` wujud dan betul.

#### Owner
- Repo Admin + Security Maintainer

---

## 7) Standard Minimum Branch Protection / Ruleset

Untuk `main`, konfigurasi minimum berikut **MUST** aktif:

1. Require a pull request before merging  
2. Require approvals: minimum 1  
3. Dismiss stale pull request approvals when new commits are pushed  
4. Require status checks to pass before merging  
5. Require branches to be up to date before merging  
6. Required checks (minimum):  
   - `DCO Check / dco-check`  
   - `Release Immutability Guard / immutability-check`  
7. Require conversation resolution before merging  
8. Block force pushes (`allow_force_pushes: false`)  
9. Block deletions (`allow_deletions: false`)  
10. Admin bypass policy ditakrif dan direkod (jika dibenarkan)

---

## 8) Automated Verification Script (gh CLI)

> Jalankan dari terminal dengan akses `gh auth login` yang sah.

```bash
#!/usr/bin/env bash
set -euo pipefail

REPO="AnuarRazii/ethical-ai-my"
pass_count=0
fail_count=0

check() {
  local name="$1"
  local actual="$2"
  local expected="$3"

  if [[ "$actual" == "$expected" ]]; then
    echo "[PASS] $name => $actual"
    pass_count=$((pass_count+1))
  else
    echo "[FAIL] $name => actual: $actual | expected: $expected"
    fail_count=$((fail_count+1))
  fi
}

echo "== Ethical AI MY Repository Settings Verification =="
json="$(gh api /repos/$REPO)"

default_branch="$(jq -r '.default_branch' <<<"$json")"
web_signoff="$(jq -r '.web_commit_signoff_required' <<<"$json")"
allow_rebase="$(jq -r '.allow_rebase_merge' <<<"$json")"
allow_update_branch="$(jq -r '.allow_update_branch' <<<"$json")"

check "Default branch" "$default_branch" "main"
check "Web commit signoff required" "$web_signoff" "true"
check "Allow rebase merge" "$allow_rebase" "true"
check "Allow update branch" "$allow_update_branch" "true"

echo "== Summary =="
echo "PASS: $pass_count"
echo "FAIL: $fail_count"

if [[ "$fail_count" -gt 0 ]]; then
  exit 1
fi
```

---

## 9) Proses Pengecualian (Waiver) | Exception Process

### Requirement
Sebarang penyimpangan dari kawalan **MUST** melalui proses waiver rasmi.

### Rules
1. Waiver hanya boleh diluluskan oleh **Compliance Owner** + **Repo Admin**.
2. Tempoh maksimum waiver: **24 jam** (melainkan diluluskan semula secara bertulis).
3. Waiver **MUST** direkod dalam isu bertag:
   - `security`
   - `waiver`
   - `priority: high` (atau `critical` jika impak tinggi)
4. Selepas tamat incident:
   - post-incident review **MUST** siap dalam 5 hari bekerja,
   - root cause + tindakan pembetulan direkod.

---

## 10) Audit Evidence Register

| Control/Setting | Implemented By | Date Implemented | Verification Evidence (URL/Output) | Verified By | Last Verified Date | Next Review Date |
|---|---|---|---|---|---|---|
| DCO Workflow | GitHub Copilot Agent | 2026-07-02 | `.github/workflows/dco.yml` + workflow run URL |  |  |  |
| Release Immutability Workflow | GitHub Copilot Agent | 2026-07-02 | `.github/workflows/release-immutability.yml` + run URL |  |  |  |
| `.github/settings.yml` baseline | GitHub Copilot Agent | 2026-07-02 | file URL + commit URL |  |  |  |
| Default branch = main |  |  | `gh api ... --jq '.default_branch'` output |  |  |  |
| web_commit_signoff_required = true |  |  | `gh api ... --jq '.web_commit_signoff_required'` output |  |  |  |
| allow_rebase_merge = true |  |  | API output snapshot |  |  |  |
| allow_update_branch = true |  |  | API output snapshot |  |  |  |
| Tag/ruleset `v*` immutability |  |  | ruleset URL / tags protection API output |  |  |  |
| LFS objects in archives |  |  | settings screenshot + sample archive test |  |  |  |
| Branch protection minimum standard |  |  | ruleset/branch protection screenshot + API output |  |  |  |

---

## 11) Keserasian Pelan & Had Platform | Plan Compatibility & Platform Constraints

1. Sesetengah ciri Rulesets/advanced enforcement mungkin berbeza mengikut pelan GitHub atau jenis akaun.  
2. Untuk user-owned repo, beberapa kawalan enterprise-level mungkin tidak tersedia sepenuhnya.  
3. Jika Rulesets tidak tersedia, gunakan branch protection + workflow checks sebagai mitigasi minimum.  
4. Legacy tag protection API lebih sempit berbanding Rulesets; pilih Rulesets apabila tersedia.

---

## 12) Rujukan | References

- [GOVERNANCE.md](../GOVERNANCE.md)  
- [SECURITY.md](../SECURITY.md)  
- [CONTRIBUTING.md](../CONTRIBUTING.md)  
- [`.github/settings.yml`](../.github/settings.yml)  
- [`.github/workflows/dco.yml`](../.github/workflows/dco.yml)  
- [`.github/workflows/release-immutability.yml`](../.github/workflows/release-immutability.yml)  
- [GitHub REST API — Update a repository](https://docs.github.com/en/rest/repos/repos#update-a-repository)  
- [Developer Certificate of Origin](https://developercertificate.org)  
- [probot/settings GitHub App](https://github.com/apps/settings)

---

## 13) Document Governance & Change Log

**Document Owner:** Compliance Owner  
**Technical Maintainer:** Security Maintainer  
**Approved By:** _To be filled_  

### Versioning
- Current: **1.1.0**
- Previous: 1.0.0

### Change Log
- **1.1.0 (2026-07-02)**
  - Tambah Scope & Applicability
  - Tambah Normative Keywords (MUST/SHOULD/OPTIONAL)
  - Tambah Control Baseline Matrix
  - Standardkan format Requirement/Implementation/Verification/Evidence/Owner
  - Tambah minimum standard branch protection/ruleset
  - Tambah automated verification script (PASS/FAIL)
  - Tambah waiver process rasmi
  - Tambah audit evidence register berstruktur
  - Kemas kini document governance & review cycle

---

**Ethical AI MY – Repository Security and Governance Settings**  
**Version 1.1.0 | Effective Date: 2026-07-02**  
**Selaras dengan ONSA 2025, CPC, dan RMC MCMC**
