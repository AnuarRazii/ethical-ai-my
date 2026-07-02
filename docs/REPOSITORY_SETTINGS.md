# Ethical AI MY – Repository Security and Governance Settings

**Version 1.1.0**  
**Tarikh Kuat Kuasa | Effective Date:** 2026-07-02  
**Penyelarasan | Alignment:** ONSA 2025, CPC, dan RMC (MCMC)  
**Repositori | Repository:** `AnuarRazii/ethical-ai-my`

Dokumen ini menetapkan baseline tetapan keselamatan dan tadbir urus repositori yang boleh diaudit, boleh diverifikasi, dan sesuai untuk operasi corporate-grade.

This document defines the repository security and governance settings baseline in an auditable, verifiable, and corporate-grade operating format.

---

## Jadual Kandungan | Table of Contents

1. [Tujuan dan Prinsip Normatif | Purpose and Normative Language](#1-tujuan-dan-prinsip-normatif--purpose-and-normative-language)
2. [Skop dan Kebolehgunaan | Scope & Applicability](#2-skop-dan-kebolehgunaan--scope--applicability)
3. [Peranan dan Akauntabiliti | Roles & Accountability](#3-peranan-dan-akauntabiliti--roles--accountability)
4. [Matriks Baseline Kawalan | Control Baseline Matrix](#4-matriks-baseline-kawalan--control-baseline-matrix)
5. [Kawalan RS-01 — Default Branch](#5-kawalan-rs-01--default-branch)
6. [Kawalan RS-02 — Release Immutability](#6-kawalan-rs-02--release-immutability)
7. [Kawalan RS-03 — DCO](#7-kawalan-rs-03--developer-certificate-of-origin-dco)
8. [Kawalan RS-04 — Rebase + Suggest Branch Update](#8-kawalan-rs-04--rebase--suggest-branch-update)
9. [Kawalan RS-05 — Line Comments + LFS in Archives](#9-kawalan-rs-05--line-comments--lfs-in-archives)
10. [Kawalan RS-06 — Standard Minimum Branch Protection / Ruleset](#10-kawalan-rs-06--standard-minimum-branch-protection--ruleset)
11. [Skrip Verifikasi Automatik (gh CLI) | Automated Verification Script (gh CLI)](#11-skrip-verifikasi-automatik-gh-cli--automated-verification-script-gh-cli)
12. [Proses Pengecualian / Waiver | Exception / Waiver Process](#12-proses-pengecualian--waiver--exception--waiver-process)
13. [Daftar Bukti Audit | Audit Evidence Register](#13-daftar-bukti-audit--audit-evidence-register)
14. [Tadbir Urus Dokumen | Document Governance](#14-tadbir-urus-dokumen--document-governance)
15. [Rujukan | References](#15-rujukan--references)

---

## 1. Tujuan dan Prinsip Normatif | Purpose and Normative Language

Dokumen ini menyokong pematuhan kepada ONSA 2025, CPC, dan RMC MCMC dengan membezakan kawalan yang **MUST** dipatuhi, **SHOULD** dilaksanakan secara kuat, dan **OPTIONAL** mengikut konteks teknikal.

This document supports alignment with ONSA 2025, CPC, and RMC MCMC by distinguishing controls that **MUST** be complied with, **SHOULD** be strongly implemented, and are **OPTIONAL** depending on technical context.

**Takrif | Definitions**
- **MUST** — wajib dipatuhi; sebarang pengecualian memerlukan waiver berjejak audit.
- **SHOULD** — sangat disyorkan; sebarang penolakan mesti direkodkan bersama rasional.
- **OPTIONAL** — boleh diaktifkan mengikut keperluan operasi tanpa menjejaskan baseline minimum.

---

## 2. Skop dan Kebolehgunaan | Scope & Applicability

Dokumen ini terpakai kepada repositori `AnuarRazii/ethical-ai-my` dan mana-mana fork dalaman atau salinan operasi yang menuntut baseline tadbir urus setara.

This document applies to the `AnuarRazii/ethical-ai-my` repository and any internal forks or operational copies that require an equivalent governance baseline.

- **Jenis repositori | Repository type:** Repositori awam; kawalan juga sesuai untuk repositori private dengan baseline yang sama.
- **Pelan GitHub | GitHub plan assumption:** Tetapan teras repositori berfungsi pada GitHub Free/Team; rulesets lanjutan, bypass governance, dan sesetengah audit controls mungkin lebih konsisten pada GitHub Team/Enterprise.
- **Konteks pemilikan | Ownership context:** Repositori ini ialah repositori milik pengguna (`user-owned repository`). Jika dipindahkan ke organisasi, rulesets peringkat organisasi dan peranan keselamatan native GitHub SHOULD digunakan.
- **Keutamaan pelaksanaan | Implementation preference:** GitHub **Rulesets SHOULD** diutamakan berbanding legacy branch protection apabila tersedia. Jika rulesets tidak tersedia atau tidak praktikal, legacy branch protection **MUST** memberi kawalan setara.
- **Peranan pemilik tetapan | Settings ownership roles:**
  - **Repo Admin** — melaksana tetapan repositori dan rulesets.
  - **Security Maintainer** — menyemak kawalan integriti, DCO, release immutability, dan status checks.
  - **Compliance Owner** — menyimpan bukti audit, meluluskan waiver, dan memacu semakan berkala.

---

## 3. Peranan dan Akauntabiliti | Roles & Accountability

Kawalan repositori ini mesti mempunyai pemilik yang jelas bagi pelaksanaan, verifikasi, dan bukti.

These repository controls must have explicit owners for implementation, verification, and evidence retention.

| Peranan | Role | Tanggungjawab Utama | Primary Responsibility |
|---|---|---|---|
| Repo Admin | Repo Admin | Ubah tetapan repositori, branch protection, rulesets, dan metadata | Change repository settings, branch protection, rulesets, and metadata |
| Security Maintainer | Security Maintainer | Sahkan status checks, DCO, immutability, dan integriti merge | Validate status checks, DCO, immutability, and merge integrity |
| Compliance Owner | Compliance Owner | Simpan bukti audit, pantau waiver, dan urus semakan berkala | Retain audit evidence, track waivers, and manage periodic review |

---

## 4. Matriks Baseline Kawalan | Control Baseline Matrix

| Control ID | Setting | Expected Value | Enforcement Method (Manual/Automated/Mixed) | Policy Level |
|---|---|---|---|---|
| RS-01 | Default branch | `main` | Mixed (`.github/settings.yml` + UI/API) | MUST |
| RS-02 | Release/tag immutability | Published releases and `v*` tags are not modified or deleted | Mixed (workflow + ruleset/UI) | MUST |
| RS-03 | Web commit sign-off | `web_commit_signoff_required = true` and DCO workflow active | Mixed (`.github/settings.yml` + workflow + UI/API) | MUST |
| RS-04 | Rebase merge | `allow_rebase_merge = true` | Mixed (`.github/settings.yml` + UI/API) | MUST |
| RS-04 | Suggest/update branch | `allow_update_branch = true` | Mixed (`.github/settings.yml` + UI/API) | MUST |
| RS-05A | PR line comments | Inline review comments available on changed lines | Platform default + process | MUST |
| RS-05B | Git LFS objects in archives | Enabled when LFS-tracked files are used | Manual/UI + repo config evidence | SHOULD |
| RS-06 | Branch protection / ruleset minimum standard | PR-only merge, required checks, up-to-date branch, stale review dismissal, ≥1 approval, no force-push, no deletion, conversation resolution | Mixed (Ruleset preferred; legacy protection acceptable) | MUST |

---

## 5. Kawalan RS-01 — Default Branch

### Requirement | Keperluan
Cawangan lalai repositori **MUST** ditetapkan kepada `main`.

The repository default branch **MUST** be set to `main`.

### Implementation | Pelaksanaan
- **UI:** `Settings` → `General` → `Default branch` → pilih `main`.
- **API:**
  ```bash
  gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
    --field default_branch=main
  ```
- **.github/settings.yml:**
  ```yaml
  repository:
    default_branch: main
  ```
- **Workflow:** Tiada workflow khusus; drift SHOULD dikesan melalui semakan berkala atau skrip verifikasi.

### Verification | Verifikasi
```bash
gh api /repos/AnuarRazii/ethical-ai-my --jq '.default_branch'
# Expected output: main
```

### Evidence | Bukti
- Output `gh api` disimpan dalam tiket perubahan, log audit, atau rekod semakan.
- Snapshot `.github/settings.yml` yang menunjukkan `default_branch: main`.

### Owner | Pemilik
**Repo Admin**

---

## 6. Kawalan RS-02 — Release Immutability

### Requirement | Keperluan
Tag keluaran dan release yang telah diterbitkan **MUST NOT** diubah atau dipadam selepas penerbitan. Ruleset tag untuk corak `v*` **SHOULD** dikuatkuasakan jika ciri tersedia.

Published release tags and releases **MUST NOT** be modified or deleted after publication. A tag ruleset for the `v*` pattern **SHOULD** be enforced when the feature is available.

### Implementation | Pelaksanaan
- **Workflow:** `.github/workflows/release-immutability.yml` **MUST** kekal aktif.
- **UI (Rulesets preferred):** `Settings` → `Rules` → `Rulesets` → cipta tag ruleset aktif untuk `refs/tags/v*` dengan sekatan `Restrict deletions` dan `Restrict updates`.
- **API (documented and supported endpoints only):**
  ```bash
  gh api /repos/AnuarRazii/ethical-ai-my/rulesets
  ```
  Gunakan endpoint supported GitHub REST untuk rulesets/tag protection yang tersedia pada pelan semasa.
- **Evidence source in repo:** Workflow snapshot mencipta jejak audit apabila violation berlaku.

### Verification | Verifikasi
```bash
gh api /repos/AnuarRazii/ethical-ai-my/rulesets \
  --jq '.[] | select(.target=="tag") | {name: .name, enforcement: .enforcement}'
# Expected output: at least one active tag ruleset relevant to v* releases
```

```bash
gh api /repos/AnuarRazii/ethical-ai-my/contents/.github/workflows/release-immutability.yml --jq '.path'
# Expected output: .github/workflows/release-immutability.yml
```

### Evidence | Bukti
- Output ruleset verification.
- Workflow file path and commit SHA.
- Audit issue URL or workflow run URL if a violation is triggered.

### Owner | Pemilik
**Security Maintainer** (implementation review) + **Repo Admin** (setting enforcement)

---

## 7. Kawalan RS-03 — Developer Certificate of Origin (DCO)

### Requirement | Keperluan
Semua sumbangan web-based **MUST** menambah sign-off automatik, dan semua komit dalam PR **MUST** lulus pemeriksaan DCO.

All web-based contributions **MUST** add sign-off automatically, and all PR commits **MUST** pass DCO verification.

### Implementation | Pelaksanaan
- **UI:** `Settings` → `General` → `Contributions` → aktifkan **Require contributors to sign off on web-based commits**.
- **API:**
  ```bash
  gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
    --field web_commit_signoff_required=true
  ```
- **.github/settings.yml:**
  ```yaml
  repository:
    web_commit_signoff_required: true
  ```
- **Workflow:** `.github/workflows/dco.yml` **MUST** kekal aktif sebagai required status check.

### Verification | Verifikasi
```bash
gh api /repos/AnuarRazii/ethical-ai-my --jq '.web_commit_signoff_required'
# Expected output: true
```

```bash
gh api /repos/AnuarRazii/ethical-ai-my/contents/.github/workflows/dco.yml --jq '.path'
# Expected output: .github/workflows/dco.yml
```

### Evidence | Bukti
- Output setting `web_commit_signoff_required`.
- Workflow path/commit SHA.
- PR check run showing `DCO Check / dco-check` as passing or required.

### Owner | Pemilik
**Security Maintainer**

---

## 8. Kawalan RS-04 — Rebase + Suggest Branch Update

### Requirement | Keperluan
`allow_rebase_merge` dan `allow_update_branch` **MUST** diaktifkan bagi mengekalkan sejarah yang kemas dan memastikan PR boleh dibawa ke base terkini dengan jelas.

`allow_rebase_merge` and `allow_update_branch` **MUST** be enabled to maintain clean history and allow PR branches to be brought up to date in a governed way.

### Implementation | Pelaksanaan
- **UI:** `Settings` → `General` → `Pull Requests` → aktifkan **Allow rebase merging** dan **Always suggest updating pull request branches**.
- **API:**
  ```bash
  gh api --method PATCH /repos/AnuarRazii/ethical-ai-my \
    --field allow_rebase_merge=true \
    --field allow_update_branch=true
  ```
- **.github/settings.yml:**
  ```yaml
  repository:
    allow_rebase_merge: true
    allow_update_branch: true
  ```
- **Workflow:** Tiada workflow khusus; verify melalui repo settings API.

### Verification | Verifikasi
```bash
gh api /repos/AnuarRazii/ethical-ai-my \
  --jq '{allow_rebase_merge, allow_update_branch}'
# Expected output: {"allow_rebase_merge":true,"allow_update_branch":true}
```

### Evidence | Bukti
- JSON output daripada `gh api`.
- Snapshot `.github/settings.yml`.

### Owner | Pemilik
**Repo Admin**

---

## 9. Kawalan RS-05 — Line Comments + LFS in Archives

### 9.1 RS-05A — Allow Comments on Individual Lines

#### Requirement | Keperluan
Keupayaan memberi ulasan pada baris individu dalam PR **MUST** tersedia untuk semakan kod dan audit teknikal.

The ability to comment on individual lines in PRs **MUST** remain available for code review and technical audit.

#### Implementation | Pelaksanaan
- **Platform default:** GitHub menyediakan inline review comments secara lalai pada tab `Files changed`.
- **Process:** Pengulas **SHOULD** menggunakan `Start a review` atau review comments berangkai untuk meninggalkan jejak audit yang sesuai.
- **UI:** Tiada toggle repositori khusus yang perlu diaktifkan dalam kebanyakan kes.

#### Verification | Verifikasi
```bash
gh api /repos/AnuarRazii/ethical-ai-my/pulls/comments?per_page=1 > /dev/null && echo "PASS: review comment API reachable"
# Expected output: PASS: review comment API reachable
```

#### Evidence | Bukti
- URL review comment pada PR.
- Screenshot tab `Files changed` yang menunjukkan inline comment capability jika diminta auditor.

#### Owner | Pemilik
**Security Maintainer**

### 9.2 RS-05B — Include Git LFS Objects in Archives

#### Requirement | Keperluan
Jika repositori menggunakan Git LFS, objek LFS dalam arkib **SHOULD** disertakan supaya muat turun ZIP/TAR kekal berguna untuk audit dan reproduksibiliti. Jika repositori tidak menggunakan LFS, kawalan ini menjadi **OPTIONAL** tetapi tetapan SHOULD kekal enabled.

If the repository uses Git LFS, LFS objects in archives **SHOULD** be included so ZIP/TAR downloads remain useful for audit and reproducibility. If the repository does not use LFS, this control becomes **OPTIONAL**, but the setting SHOULD remain enabled.

#### Implementation | Pelaksanaan
- **UI:** `Settings` → `General` → `Archives` → aktifkan **Include Git LFS objects in archives**.
- **Repo evidence:** `.gitattributes` atau `git lfs track` records SHOULD menunjukkan penggunaan LFS apabila berkenaan.
- **API:** Tiada field REST repositori yang konsisten didokumenkan untuk toggle ini; jangan andaikan endpoint yang tidak disahkan.

#### Verification | Verifikasi
```bash
git -C /home/runner/work/ethical-ai-my/ethical-ai-my lfs ls-files || true
# Expected output: list of tracked LFS files, or no output if LFS is not currently used
```

#### Evidence | Bukti
- Screenshot UI yang menunjukkan toggle diaktifkan.
- Output `git lfs ls-files` atau `.gitattributes` commit SHA jika LFS digunakan.

#### Owner | Pemilik
**Repo Admin**

---

## 10. Kawalan RS-06 — Standard Minimum Branch Protection / Ruleset

### Requirement | Keperluan
Untuk cawangan `main`, baseline minimum berikut **MUST** berkuat kuasa:
- require pull request before merge;
- required status checks;
- require branch to be up to date before merge;
- dismiss stale reviews;
- minimum approvals sekurang-kurangnya `1`;
- block force-push;
- block deletion; dan
- require conversation resolution.

For the `main` branch, the following minimum baseline **MUST** be enforced:
- require pull request before merge;
- required status checks;
- require branch to be up to date before merge;
- dismiss stale reviews;
- minimum approvals of at least `1`;
- block force-push;
- block deletion; and
- require conversation resolution.

### Implementation | Pelaksanaan
- **Rulesets preferred:** `Settings` → `Rules` → `Rulesets` → branch ruleset for `refs/heads/main`.
- **Legacy acceptable:** `.github/settings.yml` currently documents equivalent legacy branch protection and MAY remain as the fallback baseline.
- **Minimum expected settings:**
  - `required_status_checks.strict = true`
  - required checks include `DCO Check / dco-check`, `RZ1 Compliance Engine / compliance`, `RZ1 Security Enforcement / security-check`, `Release Immutability Guard / immutability-check`
  - `required_pull_request_reviews.required_approving_review_count >= 1`
  - `dismiss_stale_reviews = true`
  - `allow_force_pushes = false`
  - `allow_deletions = false`
  - `required_conversation_resolution = true`
- **User vs org note:** Untuk repositori pengguna, bypass approval biasanya dikawal secara manual oleh owner/admin. Untuk repositori organisasi, bypass lists SHOULD berada dalam ruleset berjejak audit.

### Verification | Verifikasi
```bash
gh api /repos/AnuarRazii/ethical-ai-my/branches/main/protection \
  --jq '{strict: .required_status_checks.strict, contexts: .required_status_checks.contexts, approvals: .required_pull_request_reviews.required_approving_review_count, dismiss_stale_reviews: .required_pull_request_reviews.dismiss_stale_reviews, allow_force_pushes: .allow_force_pushes.enabled, allow_deletions: .allow_deletions.enabled, conversation_resolution: .required_conversation_resolution.enabled}'
# Expected output: strict=true, approvals>=1, dismiss_stale_reviews=true, allow_force_pushes=false, allow_deletions=false, conversation_resolution=true, and required contexts present
```

```bash
gh api /repos/AnuarRazii/ethical-ai-my/rulesets \
  --jq '.[] | select(.target=="branch") | {name: .name, enforcement: .enforcement}'
# Expected output: active branch ruleset for main when rulesets are used
```

### Evidence | Bukti
- JSON output branch protection or ruleset evaluation.
- URL workflow runs for required checks.
- PR merge screen screenshot showing PR-only merge enforcement if requested.

### Owner | Pemilik
**Repo Admin** + **Compliance Owner**

---

## 11. Skrip Verifikasi Automatik (gh CLI) | Automated Verification Script (gh CLI)

Skrip di bawah memberi keputusan PASS/FAIL yang mudah dibaca auditor untuk tetapan teras repositori.

The script below provides auditor-friendly PASS/FAIL output for core repository settings.

```bash
#!/usr/bin/env bash
set -euo pipefail

REPO="AnuarRazii/ethical-ai-my"
FAILED=0

pass() { printf 'PASS | %-32s | expected=%-8s | actual=%s\n' "$1" "$2" "$3"; }
fail() { printf 'FAIL | %-32s | expected=%-8s | actual=%s\n' "$1" "$2" "$3"; FAILED=1; }
check() {
  local name="$1"
  local jq_expr="$2"
  local expected="$3"
  local actual
  actual=$(gh api "/repos/$REPO" --jq "$jq_expr")
  if [ "$actual" = "$expected" ]; then
    pass "$name" "$expected" "$actual"
  else
    fail "$name" "$expected" "$actual"
  fi
}

echo "Repository Governance Verification"
echo "Repo : $REPO"
echo "Time : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "---------------------------------------------"

check "default_branch" '.default_branch' 'main'
check "web_commit_signoff_required" '.web_commit_signoff_required' 'true'
check "allow_rebase_merge" '.allow_rebase_merge' 'true'
check "allow_update_branch" '.allow_update_branch' 'true'

echo "---------------------------------------------"
if [ "$FAILED" -eq 0 ]; then
  echo "OVERALL RESULT: PASS"
else
  echo "OVERALL RESULT: FAIL"
  exit 1
fi
```

**Contoh output | Example output**
```text
Repository Governance Verification
Repo : AnuarRazii/ethical-ai-my
Time : 2026-07-02T15:46:13Z
---------------------------------------------
PASS | default_branch                   | expected=main     | actual=main
PASS | web_commit_signoff_required      | expected=true     | actual=true
PASS | allow_rebase_merge               | expected=true     | actual=true
PASS | allow_update_branch              | expected=true     | actual=true
---------------------------------------------
OVERALL RESULT: PASS
```

---

## 12. Proses Pengecualian / Waiver | Exception / Waiver Process

Sebarang penyimpangan daripada kawalan **MUST** mempunyai waiver sementara, bersebab, dan boleh diaudit.

Any deviation from these controls **MUST** have a temporary, justified, and auditable waiver.

- **Pelulus | Approver:** Waiver hanya boleh diluluskan oleh **Compliance Owner** dan satu lagi pelulus bebas daripada **Repo Admin** atau **Security Maintainer**.
- **Tempoh maksimum | Maximum duration:** **24 jam** setiap waiver, melainkan insiden keselamatan aktif memerlukan peluasan rasmi baharu.
- **Rekod wajib | Required record:** Waiver **MUST** merekodkan control ID, sebab, risiko, mitigasi sementara, tarikh mula/tamat, pelulus, dan pautan tiket/issue.
- **Audit trail:** Waiver **MUST** direkodkan dalam issue atau change record yang boleh dirujuk auditor.
- **Post-incident review:** Jika waiver digunakan semasa insiden atau production hotfix, semakan pasca-insiden **MUST** disiapkan dalam masa **3 hari bekerja**.
- **Expiry handling:** Waiver yang tamat **MUST** ditutup secara eksplisit dan kawalan dipulihkan atau diganti dengan waiver baharu yang diluluskan.

---

## 13. Daftar Bukti Audit | Audit Evidence Register

Jadual ini merekodkan baseline verifikasi semasa dokumen ini dikeluarkan. Jika tarikh pelaksanaan asal lebih awal, rekod terdahulu MUST dirujuk dalam sejarah tetapan repositori, workflow run, atau tiket perubahan.

This table records the verification baseline at document release time. If the original implementation date is earlier, prior evidence MUST be cross-referenced from repository settings history, workflow runs, or change records.

| Control/Setting | Implemented By | Date Implemented | Verification Evidence (URL/command output/workflow run) | Verified By | Last Verified Date | Next Review Date |
|---|---|---|---|---|---|---|
| RS-01 Default branch = `main` | Repo Admin | 2026-07-02 | `gh api /repos/AnuarRazii/ethical-ai-my --jq '.default_branch'` | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-02 Release immutability workflow | Security Maintainer | 2026-07-02 | `.github/workflows/release-immutability.yml` commit SHA + workflow run URL | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-02 Tag immutability ruleset / protection | Repo Admin | 2026-07-02 | `gh api /repos/AnuarRazii/ethical-ai-my/rulesets` output | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-03 Web commit sign-off required | Repo Admin | 2026-07-02 | `gh api /repos/AnuarRazii/ethical-ai-my --jq '.web_commit_signoff_required'` | Security Maintainer | 2026-07-02 | 2026-10-02 |
| RS-03 DCO workflow active | Security Maintainer | 2026-07-02 | `.github/workflows/dco.yml` commit SHA + required check evidence | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-04 Rebase merge + update branch | Repo Admin | 2026-07-02 | `gh api /repos/AnuarRazii/ethical-ai-my --jq '{allow_rebase_merge, allow_update_branch}'` | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-05A Line comments capability | Security Maintainer | 2026-07-02 | PR review comment URL or `gh api /repos/AnuarRazii/ethical-ai-my/pulls/comments?per_page=1` | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-05B LFS in archives | Repo Admin | 2026-07-02 | UI screenshot + `git lfs ls-files` or `.gitattributes` evidence | Compliance Owner | 2026-07-02 | 2026-10-02 |
| RS-06 Branch protection / ruleset baseline | Repo Admin | 2026-07-02 | `gh api /repos/AnuarRazii/ethical-ai-my/branches/main/protection` and/or ruleset output | Compliance Owner | 2026-07-02 | 2026-10-02 |

---

## 14. Tadbir Urus Dokumen | Document Governance

| Item | Value |
|---|---|
| Document Title | Ethical AI MY – Repository Security and Governance Settings |
| Version | 1.1.0 |
| Effective Date | 2026-07-02 |
| Review Cycle | Quarterly |
| Approved By | Repository Owner / Compliance Owner |

### Log Perubahan Ringkas | Brief Change Log

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-07-02 | Initial repository settings guide with core manual and workflow controls |
| 1.1.0 | 2026-07-02 | Rewritten into audit-ready control format with TOC, scope, baseline matrix, ruleset minimum standard, verification script, waiver process, audit evidence register, and document governance |

---

## 15. Rujukan | References

- [`../.github/settings.yml`](../.github/settings.yml) — baseline repository settings as code
- [`../.github/workflows/dco.yml`](../.github/workflows/dco.yml) — DCO enforcement workflow
- [`../.github/workflows/release-immutability.yml`](../.github/workflows/release-immutability.yml) — release immutability workflow
- [`../GOVERNANCE.md`](../GOVERNANCE.md) — governance framework
- [`../SECURITY.md`](../SECURITY.md) — security baseline
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — contributor obligations and traceability
- [GitHub REST API — Repositories](https://docs.github.com/en/rest/repos/repos)
- [GitHub REST API — Branch Protection](https://docs.github.com/en/rest/branches/branch-protection)
- [GitHub REST API — Repository Rules](https://docs.github.com/en/rest/repos/rules)
- [Developer Certificate of Origin](https://developercertificate.org)
- [GitHub Settings App (probot/settings)](https://github.com/apps/settings)

---

**Ethical AI MY – Repository Security and Governance Settings**  
**Version 1.1.0**  
**Tarikh Kuat Kuasa | Effective Date: 2026-07-02**
