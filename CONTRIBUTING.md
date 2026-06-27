# Contributing to Ethical AI MY

**Tatacara Kerja Etika AI Malaysia — Ethical AI Governance Framework**

Thank you for your interest in contributing to Ethical AI MY. This document outlines the process, standards, and expectations for contributing to this project. All contributions must align with our ethical principles and governance framework.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Development Workflow](#development-workflow)
4. [Commit Standards](#commit-standards)
5. [Pull Request Process](#pull-request-process)
6. [Issue Reporting](#issue-reporting)
7. [Documentation Standards](#documentation-standards)
8. [Ethical Alignment Requirements](#ethical-alignment-requirements)
9. [Attribution and Licensing](#attribution-and-licensing)
10. [Contact and Support](#contact-and-support)

---

## Code of Conduct

All contributors must read and adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before participating. We are committed to fostering a welcoming, respectful, and inclusive environment.

---

## How to Contribute

### Types of Contributions Welcome

- **Documentation improvements** – Clarifications, corrections, bilingual additions
- **Policy proposals** – Governance framework enhancements
- **Ethical framework refinements** – Expansions or updates to ethical principles
- **Security enhancements** – Identification and resolution of security issues
- **Community engagement** – Discussions, translations, accessibility improvements
- **Bug reports** – Issues in documentation, structure, or code

### Before You Start

1. Review existing [issues](../../issues) and [pull requests](../../pulls) to avoid duplication
2. Read the relevant policy documents ([ETHICS.md](ETHICS.md), [GOVERNANCE.md](GOVERNANCE.md))
3. Open an issue to discuss significant changes before implementing them
4. Ensure you have the authority to contribute the proposed content

---

## Development Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/ethical-ai-my.git
cd ethical-ai-my
```

### 2. Create a Feature Branch

Use a descriptive branch name following this convention:

```
docs/update-ethics-framework
fix/security-section-clarity
feat/governance-proposal-template
policy/data-privacy-amendment
```

```bash
git checkout -b docs/your-descriptive-branch-name
```

### 3. Make Your Changes

- Keep changes focused and minimal in scope
- Update relevant documentation if applicable
- Ensure all changes align with our ethical principles

### 4. Commit Your Changes

Sign your commits with DCO (Developer Certificate of Origin):

```bash
git commit -s -m "docs: update ethics framework section 3"
```

The `-s` flag adds a `Signed-off-by` trailer to your commit, certifying that you have the right to submit your contribution under the project's license.

### 5. Submit a Pull Request

Push your branch and open a pull request using the provided template.

---

## Commit Standards

### Commit Message Format

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
Signed-off-by: Your Name <your.email@example.com>
```

### Commit Types

| Type       | Description                                       |
|------------|---------------------------------------------------|
| `feat`     | New feature or framework addition                 |
| `fix`      | Correction or bug fix                             |
| `docs`     | Documentation changes only                        |
| `policy`   | Policy or governance framework changes            |
| `security` | Security-related improvements                     |
| `refactor` | Restructuring without changing meaning            |
| `chore`    | Maintenance tasks, CI updates                     |

### DCO Sign-Off Requirement

All commits must include a `Signed-off-by` line. By signing off, you certify:

> By making a contribution to this project, I certify that:
> (a) the contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or
> (b) the contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications; or
> (c) the contribution was provided directly to me by some other person who certified (a), (b) or (c) and I have not modified it.

---

## Pull Request Process

### PR Requirements

1. Use the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md)
2. Link to the relevant issue(s)
3. Ensure all checklist items are addressed
4. Obtain at least one reviewer approval before merging
5. Keep PRs focused — one logical change per PR

### Merge Strategy

This repository uses **squash merging** for a clean commit history. Ensure your PR title follows the commit message format above, as it becomes the squash commit message.

### Review Process

- Reviewers assess ethical alignment, documentation quality, and correctness
- Address all review comments constructively
- Keep PR branches up to date with `main`
- PRs are automatically closed if the linked issue is resolved

### Branch Deletion

Merged branches are automatically deleted. Ensure you do not have uncommitted work on the PR branch before merging.

---

## Issue Reporting

### Creating Issues

Use the appropriate issue template:

- **Bug Report** – For errors, inaccuracies, or broken functionality
- **Feature Request** – For new framework additions or enhancements
- **Documentation Improvement** – For clarity and accuracy improvements
- **Governance Proposal** – For policy and governance changes

### Issue Guidelines

- Provide complete information using the template
- Include steps to reproduce for bug reports
- Reference related documents or sections
- Remain respectful and constructive

---

## Documentation Standards

### Language

This project is bilingual (English and Malay). Significant changes should ideally be reflected in both languages.

### Formatting

- Use Markdown for all documentation
- Use ATX-style headings (`#`, `##`, `###`)
- Use numbered lists for sequential steps, bullet lists for non-sequential items
- Include a document version and date at the bottom of policy documents

### Structure

Policy documents should follow this structure:
1. Title and subtitle
2. Overview/Purpose
3. Core content with numbered sections
4. Implementation guidance
5. Version and date footer

---

## Ethical Alignment Requirements

All contributions must demonstrate alignment with our core ethical principles:

| Principle       | Requirement                                                   |
|-----------------|---------------------------------------------------------------|
| **Fairness**    | Promotes equitable treatment of all stakeholders              |
| **Transparency**| Improves clarity, auditability, and documentation             |
| **Accountability** | Strengthens responsibility and governance mechanisms       |
| **Privacy**     | Protects personal data and confidentiality                    |
| **Benefit**     | Contributes to positive societal impact                       |

Contributions that conflict with these principles will not be accepted.

---

## Attribution and Licensing

### Licensing

All contributions are released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). By contributing, you agree to these terms.

### Attribution

Significant contributors will be acknowledged in [ATTRIBUTION.md](ATTRIBUTION.md). Please include your name, affiliation (optional), and contribution description when opening a pull request.

### Intellectual Property

- Ensure you have the right to contribute all submitted content
- Do not submit content that infringes on third-party intellectual property
- Clearly attribute any third-party content, quotes, or references

---

## Contact and Support

- **Issues:** Open a [GitHub Issue](../../issues)
- **Discussions:** Join our [GitHub Discussions](../../discussions)
- **Security concerns:** Follow [SECURITY.md](SECURITY.md) reporting procedures
- **General enquiries:** Contact maintainers via the repository

---

**Ethical AI MY – Contributing to Responsible AI Governance in Malaysia**

*Framework: ONSA 2025 | CPC | RMC (MCMC, eff. 1 Jun 2026)*  
*Version 1.0 | 2026-06-01*
