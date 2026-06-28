---
name: claude-api
version: "3.0"
classification: RESTRICTED — ARDOOP TECHNOLOGIES INTERNAL
hitl_required: true
last_reviewed: "2026-06-29"
reviewer: "Anuar Bin Mohd Khai Razi"
compliance: ["MCMC_ONSA_2025", "PDPA_2010", "CPC", "RMC_JUN_2026"]
---

# Claude API Skill — Ardoop Technologies

| Field | Value |
|-------|-------|
| **Pemilik** | Anuar Bin Mohd Khai Razi · anuarrazii@outlook.my |
| **Skop** | Semua integrasi Claude API merentas Ardoop Technologies, Arbiey AI, Ardoop AI RZ1 |
| **Pematuhan** | MCMC ONSA 2025 · PDPA 2010 · CPC · RMC (Jun 2026) |
| **Prinsip** | Human-in-the-Loop (HITL) adalah WAJIB untuk semua output rasmi |
| **ORCID** | 0009-0005-7085-054X |

> © 2026 Anuar Bin Mohd Khai Razi. Hak Cipta Terpelihara.

---

## ⛔ BAHAGIAN 0 — GARIS KASAR TAHAP TERTINGGI (HARD LINES)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                   🚫 HARD LINES — TIDAK BOLEH DILANGGAR                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  HL-01  API key TIDAK BOLEH dicommit ke mana-mana repositori dalam          ║
║         apa jua keadaan — plaintext, base64, dalam komen, atau history.     ║
║                                                                              ║
║  HL-02  Data peribadi (nama, IC, alamat, telefon, data kesihatan)           ║
║         TIDAK BOLEH dihantar ke Claude API tanpa kebenaran PDPA bertulis.   ║
║                                                                              ║
║  HL-03  Output AI TIDAK BOLEH diterbitkan sebagai output rasmi Ardoop       ║
║         Technologies tanpa melalui HITL checkpoint yang disahkan.           ║
║                                                                              ║
║  HL-04  Model AI TIDAK BOLEH membuat keputusan muktamad yang melibatkan     ║
║         hak manusia, reputasi, atau undang-undang tanpa kelulusan manusia.  ║
║                                                                              ║
║  HL-05  Aplikasi pihak ketiga (StackBlitz, Bolt, Lovable, dsb.) TIDAK       ║
║         BOLEH mempunyai akses penuh kepada repositori yang mengandungi      ║
║         secrets, kunci API, atau data sensitif.                              ║
║                                                                              ║
║  HL-06  Prompt injection dari sumber luar (GitHub issues, PR komen,         ║
║         input pengguna) TIDAK BOLEH dihantar terus ke LLM tanpa sanitasi.  ║
║                                                                              ║
║  HL-07  Kandungan melibatkan kanak-kanak TIDAK BOLEH diproses oleh AI       ║
║         tanpa lapisan pematuhan CPC yang lengkap dan eksplisit.             ║
║                                                                              ║
║  HL-08  Agent AI TIDAK BOLEH diberi kebenaran contents:write ke             ║
║         repositori utama (main/production) tanpa HITL gate aktif.           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🔒 BAHAGIAN 0B — DASAR KERAS TAHAP TERTINGGI (HARD POLICIES)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                   🔒 HARD POLICIES — WAJIB DIKUATKUASAKAN                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  HP-01  KEBENARAN MINIMUM (Least Privilege)                                  ║
║         Setiap integrasi API mesti bermula dengan kebenaran paling           ║
║         terhad. Tambah kebenaran hanya apabila diperlukan dan didokumen.    ║
║                                                                              ║
║  HP-02  AUDIT TRAIL WAJIB                                                   ║
║         Setiap panggilan API rasmi mesti log: model, timestamp UTC,         ║
║         context, token count, dan nama penyemak HITL.                       ║
║                                                                              ║
║  HP-03  PUSINGAN KUNCI BERKALA                                               ║
║         ANTHROPIC_API_KEY mesti dipusingkan sekurang-kurangnya setiap       ║
║         90 hari atau serta-merta selepas sebarang pendedahan yang disyaki.  ║
║                                                                              ║
║  HP-04  PENGASINGAN PERSEKITARAN                                             ║
║         Kunci API dev, staging, dan production mesti berbeza.               ║
║         Jangan guna kunci production dalam persekitaran ujian.              ║
║                                                                              ║
║  HP-05  SEMAKAN LINTANG (Cross-Review)                                       ║
║         Output AI yang melibatkan reputasi Ardoop Technologies mesti        ║
║         disemak oleh Anuar Razii sebelum diterbitkan — tiada pengecualian.  ║
║                                                                              ║
║  HP-06  TAMAT TEMPOH TOKEN                                                   ║
║         Gunakan fine-grained GitHub tokens dengan tarikh tamat tempoh.      ║
║         Token tanpa tarikh tamat tempoh adalah dilarang dalam CI/CD.        ║
║                                                                              ║
║  HP-07  RANTAI KESELAMATAN BERTERUSAN                                        ║
║         Secret scanning + CodeQL + HITL gate mesti AKTIF dalam semua        ║
║         repositori yang menggunakan Claude API.                              ║
║                                                                              ║
║  HP-08  TIADA AKSES TERUS KE PRODUCTION                                      ║
║         Agent AI TIDAK BOLEH push terus ke branch main. Semua perubahan     ║
║         mesti melalui Pull Request + HITL.                                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🛡️ BAHAGIAN 0C — IRINGAN KESELAMATAN KUKUH (SECURITY ESCORT)

```python
import os, re, hashlib, datetime, logging

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s [ARDOOP-SEC] %(message)s')
logger = logging.getLogger("ardoop.security")

SENSITIVE_PATTERNS = [
    r'\b\d{6}-\d{2}-\d{4}\b',           # IC number
    r'\b01[0-9]-?\d{7,8}\b',            # MY phone number
    r'\bsk-ant-[a-zA-Z0-9\-_]{20,}\b',  # Anthropic key
    r'\bghp_[a-zA-Z0-9]{36}\b',         # GitHub PAT
    r'\bghx_[a-zA-Z0-9]{36}\b',         # GitHub App token
    r'(?i)(password|kata\s*laluan)\s*[:=]\s*\S+',
    r'(?i)(api[_-]?key|secret|token)\s*[:=]\s*["\']?\S+["\']?',
]

class SecurityEscort:
    """Iringan keselamatan untuk semua integrasi Claude API."""

    def __init__(self, context: str, reviewer: str = "Anuar Bin Mohd Khai Razi"):
        self.context = context
        self.reviewer = reviewer
        self.session_id = hashlib.sha256(
            f"{context}{datetime.datetime.utcnow().isoformat()}".encode()
        ).hexdigest()[:16]
        self._cleared = False

    def scan_input(self, text: str) -> dict:
        """Imbas input untuk corak sensitif sebelum hantar ke API."""
        threats = []
        for pattern in SENSITIVE_PATTERNS:
            if re.search(pattern, text):
                threats.append(pattern)
        if threats:
            logger.critical(f"[{self.session_id}] INPUT SCAN GAGAL — {len(threats)} ancaman")
            return {"cleared": False, "threats": threats}
        self._cleared = True
        logger.info(f"[{self.session_id}] Input scan lulus")
        return {"cleared": True, "threats": []}

    def verify_api_key(self) -> bool:
        """Sahkan kunci API wujud dan sah."""
        key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not key or len(key) < 20 or key == "ANTHROPIC_API_KEY":
            logger.critical(f"[{self.session_id}] API key tidak sah atau placeholder!")
            return False
        logger.info(f"[{self.session_id}] API key disahkan")
        return True

    def hitl_wrap(self, ai_output: str, model: str = "claude-sonnet-4-6",
                  input_tokens: int = 0, output_tokens: int = 0) -> dict:
        """Bungkus output AI dengan metadata HITL untuk semakan manusia."""
        now_utc = datetime.datetime.utcnow()
        return {
            "status": "PENDING_HUMAN_REVIEW",
            "session_id": self.session_id,
            "reviewer": self.reviewer,
            "timestamp_utc": now_utc.isoformat() + "Z",
            "timestamp_myt": (now_utc + datetime.timedelta(hours=8)
                              ).strftime('%Y-%m-%d %H:%M MYT'),
            "context": self.context,
            "ai_output": ai_output,
            "governance": {
                "model_used": model,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "compliance": ["ONSA_2025", "PDPA_2010", "CPC", "RMC"],
                "hitl_required": True,
                "hard_lines_version": "3.0",
            },
        }

    def approve(self, approved: bool, notes: str = "") -> dict:
        """Rekod keputusan kelulusan HITL."""
        decision = {
            "session_id": self.session_id,
            "approved": approved,
            "reviewed_by": self.reviewer,
            "reviewed_at_utc": datetime.datetime.utcnow().isoformat() + "Z",
            "notes": notes,
            "status": "APPROVED" if approved else "REJECTED",
        }
        logger.info(f"[{self.session_id}] HITL: {decision['status']}")
        return decision
```

---

## 1 · Core API Pattern

### Python

```python
import anthropic

client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env var

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain HITL governance in 3 bullet points."}
    ]
)
print(message.content[0].text)
```

### JavaScript

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic(); // Uses ANTHROPIC_API_KEY env var

const message = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Explain HITL governance in 3 bullet points." }
  ]
});
console.log(message.content[0].text);
```

---

## 2 · HITL Governance Wrapper

```python
from security_escort import SecurityEscort

escort = SecurityEscort(context="LinkedIn post draft")

# 1. Scan input
scan = escort.scan_input(user_prompt)
if not scan["cleared"]:
    raise ValueError(f"Input ditolak: {scan['threats']}")

# 2. Call Claude API
result = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=512,
    messages=[{"role": "user", "content": user_prompt}]
)

# 3. Wrap with HITL
packet = escort.hitl_wrap(
    ai_output=result.content[0].text,
    model="claude-sonnet-4-6",
    input_tokens=result.usage.input_tokens,
    output_tokens=result.usage.output_tokens
)
# packet["status"] == "PENDING_HUMAN_REVIEW" — must be approved before publish

# 4. Human approval (Anuar Razii)
decision = escort.approve(approved=True, notes="Content verified, tone OK")
```

---

## 3 · System Prompt Template

```
You are an AI assistant for Ardoop Technologies, operating under:
- MCMC ONSA 2025 compliance
- PDPA 2010 data protection
- Children Protection Code (CPC)
- RMC (effective June 2026)

HITL Directive: All official outputs require human review before publication.
Language: Respond in Bahasa Malaysia unless English is explicitly requested.
Owner: Anuar Bin Mohd Khai Razi (ORCID: 0009-0005-7085-054X)

Hard constraints:
- Never output personal data (IC, phone, address) without PDPA clearance
- Never make final legal/reputational decisions
- Always flag content involving children for CPC review
- Always include governance metadata in structured outputs
```

---

## 4 · Model Selection Guide

| Kes Penggunaan | Model | Sebab |
|----------------|-------|-------|
| Governance docs, profiling | `claude-sonnet-4-6` | Kualiti/kos terbaik |
| Klasifikasi pantas, routing | `claude-haiku-4-5-20251001` | Pantas, murah |
| Penaakulan kompleks, dasar | `claude-opus-4-6` | Keupayaan tertinggi |
| Arbiey AI daily chat | `claude-sonnet-4-6` | Responsif + bernuansa |
| Security audit, kod review | `claude-opus-4-6` | Penaakulan mendalam |

---

## 5 · Streaming

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

---

## 6 · Multi-turn Conversation

```python
conversation = []

def chat(user_msg: str) -> str:
    conversation.append({"role": "user", "content": user_msg})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are Arbiey AI, assistant for Ardoop Technologies.",
        messages=conversation
    )
    assistant_msg = response.content[0].text
    conversation.append({"role": "assistant", "content": assistant_msg})
    return assistant_msg
```

---

## 7 · Error Handling & Retry

```python
import time
import anthropic

def call_with_retry(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                messages=messages
            )
        except anthropic.RateLimitError:
            wait = 2 ** attempt
            logger.warning(f"Rate limited. Retry in {wait}s...")
            time.sleep(wait)
        except anthropic.APIConnectionError:
            logger.error("Connection error. Retry in 5s...")
            time.sleep(5)
        except anthropic.APIStatusError as e:
            logger.error(f"API error {e.status_code}: {e.message}")
            raise
    raise RuntimeError("Max retries exceeded")
```

---

## 8 · Token & Cost Awareness

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
)

usage = response.usage
print(f"Input tokens:  {usage.input_tokens}")
print(f"Output tokens: {usage.output_tokens}")

# Cost estimation (approximate, check current pricing)
INPUT_COST_PER_1K = 0.003   # Sonnet input
OUTPUT_COST_PER_1K = 0.015  # Sonnet output
estimated_cost = (
    (usage.input_tokens / 1000) * INPUT_COST_PER_1K +
    (usage.output_tokens / 1000) * OUTPUT_COST_PER_1K
)
print(f"Estimated cost: ${estimated_cost:.4f}")
```

---

## 9 · Senarai Semak Regulasi Malaysia

```
┌─────────────────────────────────────────────────────────────┐
│  SENARAI SEMAK PRA-PENEMPATAN (Pre-Deployment Checklist)    │
├─────────────────────────────────────────────────────────────┤
│  [ ] ONSA 2025 — Pendaftaran sistem AI jika berkenaan       │
│  [ ] PDPA 2010 — Data peribadi tidak diproses tanpa izin    │
│  [ ] CPC — Kandungan kanak-kanak dilindungi sepenuhnya      │
│  [ ] RMC — Pematuhan kod multimedia (berkuat kuasa Jun 2026)│
│  [ ] HITL — Gate kelulusan manusia aktif                    │
│  [ ] Secret Scanning — Tiada kunci/token dalam kod          │
│  [ ] CodeQL — Tiada kelemahan keselamatan kritikal          │
│  [ ] Audit Trail — Logging lengkap untuk setiap panggilan   │
└─────────────────────────────────────────────────────────────┘
```

---

## 10 · Rujukan Pantas

```
┌────────────────────────────────────────────────────────────────┐
│  RUJUKAN PANTAS (Quick Reference)                              │
├────────────────────────────────────────────────────────────────┤
│  API Base:    https://api.anthropic.com                        │
│  Docs:        https://docs.anthropic.com                       │
│  SDK Python:  pip install anthropic                             │
│  SDK JS:      npm install @anthropic-ai/sdk                    │
│  Key env var: ANTHROPIC_API_KEY                                │
│  HITL gate:   PENDING_HUMAN_REVIEW → APPROVED/REJECTED        │
│  Rotation:    Every 90 days or on suspected exposure           │
│  Owner:       Anuar Bin Mohd Khai Razi                         │
│  ORCID:       0009-0005-7085-054X                              │
└────────────────────────────────────────────────────────────────┘
```

---

## 11 · GitHub Actions CI Integration

| Job | Fungsi | Trigger |
|-----|--------|---------|
| `governance-check` | Audit .md dengan Claude Haiku | Push / PR |
| `generate-pdf-report` | Jana PDF dengan Sonnet + ReportLab | Push ke main |
| `hitl-gate` | Tunggu kelulusan manual Anuar | Semua PR |

**Setup:**
- `ANTHROPIC_API_KEY` dalam Repository Secrets
- Environment `hitl-review` dikonfigurasi
- Kebenaran: `contents: read` + `pull-requests: write` sahaja

---

## 12 · PDF Pipeline (Standalone)

```bash
# Install dependencies
pip install anthropic reportlab

# Flow:
# SecurityEscort.scan_input() → Claude generate → hitl_wrap() → Anuar approve → ReportLab PDF
```

**Aliran:**
`SecurityEscort.scan_input()` → Claude jana → `hitl_wrap()` → Kelulusan Anuar → ReportLab PDF

---

## 13 · Semakan Lintang Siap Guna (Cross-Review)

```
┌─────────────────────────────────────────────────────────────────┐
│  SEMAKAN LINTANG (Cross-Review Protocol)                        │
├─────────────────────────────────────────────────────────────────┤
│  1. AI generates output                                         │
│  2. SecurityEscort.scan_input() — check for sensitive data      │
│  3. hitl_wrap() — package with governance metadata              │
│  4. Status: PENDING_HUMAN_REVIEW                                │
│  5. Anuar Razii reviews and approves/rejects                    │
│  6. If APPROVED: publish/deploy                                 │
│  7. If REJECTED: return to step 1 with feedback                 │
│  8. Audit log: all decisions recorded with timestamp            │
└─────────────────────────────────────────────────────────────────┘
```

---

> **Skill versi 3.0** — 🫡 HITL Directive — Penaakulan Lanjutan Dasar
>
> © 2026 Anuar Bin Mohd Khai Razi · Ardoop Technologies · ORCID: 0009-0005-7085-054X
>
> Terakhir disemak: 29 Jun 2026 · Penyemak: Anuar Bin Mohd Khai Razi
