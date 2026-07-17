# Ethical AI MY – v1.0 Reference Release

**Open, Auditable, Non-Mandatory Reference for Ethical AI in Malaysia**

---

## Hotfix: v1.0.1 — RZ1 SHA Pin Enforcement (2026-07-02)

**Hotfix reference:** `hotfix/rz1-sha-pin-enforcement-audit`
**Applied by:** Anuar Razii \<anuarrazii@outlook.my\>
**Governance engines affected:** RZ1 Compliance Engine, RZ1 Validate, CodeQL Security Analysis, RZ1 Security Enforcement, DCO Check, Release Immutability Guard

### Issue Identified

All six GitHub Actions workflow files were referencing actions using version tags (`@v4`, `@v7`, `@v3`) instead of full commit SHAs. The repository enforces a policy requiring every action reference to use a pinned full-length commit SHA. This caused immediate `startup` failures across all RZ1 governance engines.

**Error logged:** `The action actions/checkout@v4 is not allowed because all actions must be pinned to a full-length commit SHA.`

### Affected Workflows (prior to fix)

| Workflow file | Action | Tag (blocked) | SHA pin (applied) |
|---|---|---|---|
| `compliance.yml` | `actions/checkout` | `@v4` | `@34e114876b0b11c390a56381ad16ebd13914f8d5` |
| `RZ1-validate.yml` | `actions/checkout` | `@v4` | `@34e114876b0b11c390a56381ad16ebd13914f8d5` |
| `codeql.yml` | `actions/checkout` | `@v4` | `@34e114876b0b11c390a56381ad16ebd13914f8d5` |
| `codeql.yml` | `github/codeql-action/init` | `@v3` | `@411c4c9a36b3fca4d674f06b6396b2c6d23522c6` |
| `codeql.yml` | `github/codeql-action/analyze` | `@v3` | `@411c4c9a36b3fca4d674f06b6396b2c6d23522c6` |
| `security.yml` | `actions/checkout` | `@v4` | `@34e114876b0b11c390a56381ad16ebd13914f8d5` |
| `dco.yml` | `actions/checkout` | `@v4` | `@34e114876b0b11c390a56381ad16ebd13914f8d5` |
| `dco.yml` | `actions/github-script` | `@v7` | `@f28e40c7f34bde8b3046d885e986cb6290c5673b` |
| `release-immutability.yml` | `actions/checkout` | `@v4` | `@34e114876b0b11c390a56381ad16ebd13914f8d5` |
| `release-immutability.yml` | `actions/github-script` | `@v7` | `@f28e40c7f34bde8b3046d885e986cb6290c5673b` |

### Resolution

SHA pins applied via PR #10 (merged `2026-07-02T16:21:36Z`, merge commit `083d0fbb0532babb12ec192059042fc267350f65`). All RZ1 governance engines restored to **green** status immediately after merge.

### Audit Trail

- **Detected at:** `d5cb904972a84211f4e3ba6f4ed2299121ca27fe` — 4 workflows failing
- **Fixed at:** `083d0fbb0532babb12ec192059042fc267350f65` — all workflows passing
- **Hotfix commit:** this record — confirmed by `Signed-off-by: Anuar Razii <anuarrazii@outlook.my>`
- **Governance framework:** ONSA 2025 | CPC | RMC (MCMC, eff. 1 Jun 2026)

---

## Release Summary

Ethical AI MY v1.0 represents the initial comprehensive reference release for responsible and ethical AI development in Malaysia. This release includes:

### Core Policy Documents
- **ETHICS.md** – Fundamental ethical principles (Fairness, Transparency, Accountability, Privacy, Benefit)
- **GOVERNANCE.md** – Non-centralized governance model and stakeholder roles
- **SECURITY.md** – Security standards and risk management framework
- **CODE_OF_CONDUCT.md** – Community guidelines and standards
- **ATTRIBUTION.md** – Recognition and citation framework
- **FINAL_INTENT.md** – Statement of purpose and long-term vision

### Supporting Materials
- **README.md** – Comprehensive documentation and navigation
- **LICENSE** – Creative Commons Attribution 4.0 International
- **index.html** – Landing page for GitHub Pages
- **ethical-ai-my-archive-bilingual.html** – Single-page bilingual archive (English/Malay)
- **ethical-ai-my-diagram-monochrome-bilingual.svg** – Governance model diagram

### GitHub Templates
- Pull Request Template
- Bug Report Issue Template
- Feature Request Issue Template

---

## Key Features

### ✓ Open
All materials are publicly available under CC BY 4.0 license.

### ✓ Auditable
Complete documentation of frameworks, governance, and decision-making processes.

### ✓ Non-Mandatory
Reference guidance, not regulation. Organizations adapt according to their context.

### ✓ Comprehensive
Addresses ethics, governance, security, community standards, and attribution.

### ✓ Bilingual
Core materials available in English and Malay (Bahasa Melayu).

### ✓ Accessible
Single-page archive for printing, offline access, and broad accessibility.

---

## Release Contents

```
ethical-ai-my/
├── index.html
├── README.md
├── LICENSE (CC BY 4.0)
├── ETHICS.md
├── GOVERNANCE.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── ATTRIBUTION.md
├── FINAL_INTENT.md
├── ethical-ai-my-archive-bilingual.html
├── ethical-ai-my-diagram-monochrome-bilingual.svg
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

---

## Getting Started

### For Developers
1. Review ETHICS.md for ethical principles
2. Study SECURITY.md for technical requirements
3. Implement according to your AI system context

### For Organizations
1. Examine GOVERNANCE.md for governance structures
2. Review CODE_OF_CONDUCT.md for team guidelines
3. Establish alignment with your AI strategy

### For Researchers
1. Access ethical-ai-my-archive-bilingual.html for comprehensive references
2. Consult ATTRIBUTION.md for citation practices
3. Contribute findings to expand the reference

### For Communities
1. Read CODE_OF_CONDUCT.md for participation guidelines
2. Review contribution process
3. Engage in discussions and provide feedback

---

## Version Information

- **Version:** 1.0
- **Release Type:** Reference Release
- **Release Date:** 2026-06-01
- **Status:** Published & Open
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Language:** English (Primary), Malay (Bilingual)

---

## Core Ethical Principles

### Fairness
Equitable treatment and outcomes across all stakeholders and demographics.

### Transparency
Documented, understandable AI systems open to scrutiny.

### Accountability
Clear responsibility for system behavior and outcomes.

### Privacy
Protection of personal data throughout the system lifecycle.

### Benefit
Positive contribution to individual wellbeing and society.

---

## Governance Model

**Non-centralized, autonomous stakeholder decision-making** maintained through:
- Shared ethical principles
- Transparent communication
- Mutual accountability
- Collaborative problem-solving

---

## Downloads & Access

### Primary Repository
https://github.com/AnuarRazii/ethical-ai-my

### Key Links
- **Full Documentation:** README.md
- **Landing Page:** index.html
- **Bilingual Archive:** ethical-ai-my-archive-bilingual.html
- **Governance Diagram:** ethical-ai-my-diagram-monochrome-bilingual.svg

---

## Contributing

We welcome contributions! Please:

1. Review CODE_OF_CONDUCT.md
2. Follow .github/PULL_REQUEST_TEMPLATE.md
3. Ensure alignment with ETHICS.md
4. Update ATTRIBUTION.md as needed

---

## Support & Feedback

- **Issues:** Open an issue using provided templates
- **Discussions:** Engage in community discussions
- **Feedback:** All feedback welcome through GitHub issues

---

## Acknowledgments

This reference release represents the collective effort of the AI ethics community, stakeholder feedback, and the commitment to responsible AI development in Malaysia.

---

## License

This work is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

You are free to:
- Share, copy, and redistribute
- Adapt, remix, transform, and build upon

Under the terms of:
- Attribution – Credit the original work
- No additional restrictions – No legal terms limiting others

For full license details, see LICENSE file.

---

## Statement of Intent

Ethical AI MY is established as an open, auditable, non-mandatory reference for responsible AI development. It represents a collective commitment to:

- **Ethical alignment** – Shared principles guiding development
- **Transparent governance** – Open decision-making processes
- **Stakeholder voice** – All affected parties represented
- **Continuous improvement** – Evolution based on learning

---

## Next Steps

### Immediate (v1.0+)
- Community feedback and improvement
- Integration into development practices
- Translation to additional languages
- Case studies and implementation guides

### Medium-term (v1.1+)
- Expanded security guidance
- Industry-specific adaptations
- Tool and framework integration
- Educational resources

### Long-term (2+ years)
- Widespread adoption across Malaysia
- Integration into policy and regulation
- International collaboration
- Demonstrated impact on AI development

---

## Questions?

Visit the GitHub repository for complete documentation:
https://github.com/AnuarRazii/ethical-ai-my

---

**Ethical AI MY – Reference Release v1.0**

*"Open. Auditable. Non-Mandatory. For Ethical AI in Malaysia."*

**Release Date:** 2026-06-01
**Status:** Published & Available
**License:** CC BY 4.0