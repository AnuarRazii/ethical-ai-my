---
name: claude-api
description: >
  Expert guide for integrating and using the Anthropic Claude API within
  Ardoop Technologies projects — covering authentication, message construction,
  model selection, Human-in-the-Loop (HITL) governance wrappers, streaming,
  cost optimisation, and Malaysian regulatory alignment (ONSA 2025, PDPA,
  CPC, RMC). Use this skill whenever the user wants to call the Claude API,
  build an AI-powered feature, set up a governance layer around an LLM call,
  write or improve a prompt template, handle API errors or rate limits, test
  API responses, or integrate Claude into a Python / JavaScript workflow.
  Also trigger for any mention of: Anthropic SDK, claude-sonnet, claude-haiku,
  messages endpoint, tokens, system prompt, streaming, HITL wrapper,
  AI governance API, or Arbiey / Ardoop AI RZ1 backend integration.
---

# Claude API Skill — Ardoop Technologies

**Owner:** Anuar Bin Mohd Khai Razi (Anuar Razii)  
**Scope:** All Claude API integrations across Ardoop Technologies, Arbiey AI, and Ardoop AI RZ1  
**Compliance:** MCMC ONSA 2025 · PDPA 2010 · CPC · RMC (Jun 2026)  
**Principle:** Human-in-the-Loop (HITL) is mandatory for all official AI outputs

---

## 1 · Core API Pattern

```python
import anthropic

client = anthropic.Anthropic(api_key="ANTHROPIC_API_KEY")

response = client.messages.create(
    model="claude-sonnet-4-6",      # default — see §4 for model guide
    max_tokens=1024,
    system="You are …",             # always provide a system prompt
    messages=[
        {"role": "user", "content": "…"}
    ]
)
print(response.content[0].text)
```

**JavaScript equivalent:**

```js
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();
const msg = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "…" }],
});
console.log(msg.content[0].text);
```

---

## 2 · HITL Governance Wrapper (Mandatory for Official Outputs)

All outputs marked as *official* (letters, certificates, governance docs,
public posts) **must** pass through this wrapper before delivery.

```python
def hitl_wrap(raw_output: str, context: str, reviewer: str = "Anuar Razii") -> dict:
    """
    Flags AI output for human review before release.
    Returns a structured review packet.
    """
    return {
        "status": "PENDING_HUMAN_REVIEW",
        "reviewer": reviewer,
        "context": context,
        "ai_output": raw_output,
        "governance": {
            "model_used": "claude-sonnet-4-6",
            "compliance": ["ONSA_2025", "PDPA_2010", "CPC", "RMC"],
            "hitl_required": True,
        },
    }

# Usage
result = client.messages.create(model="claude-sonnet-4-6", max_tokens=512,
    messages=[{"role":"user","content": prompt}])
packet = hitl_wrap(result.content[0].text, context="LinkedIn post draft")
# → show packet["ai_output"] to Anuar for approval before publishing
```

---

## 3 · System Prompt Template (Ardoop / Arbiey)

```
You are an AI assistant operating under the Ardoop Technologies AI
Governance Framework. Your outputs must be:
- Factually accurate and verifiable
- Ethically grounded (Fairness, Transparency, Accountability, Privacy, Benefit)
- Aligned with MCMC ONSA 2025, CPC, and RMC Malaysia
- Free of hallucinated credentials or unverifiable claims
- Bilingual-aware (Bahasa Malaysia Rasmi / English) when relevant

Human-in-the-Loop oversight applies to all official outputs.
Never claim authority beyond what is stated in the user's verified profile.
```

---

## 4 · Model Selection Guide

| Use Case | Model | Why |
|---|---|---|
| Governance docs, profiling, analysis | `claude-sonnet-4-6` | Best balance quality/cost |
| Quick classification, routing | `claude-haiku-4-5-20251001` | Fast, cheap |
| Complex reasoning, policy review | `claude-opus-4-6` | Highest capability |
| Daily Buddy AI / Arbiey AI chat | `claude-sonnet-4-6` | Responsive + nuanced |

---

## 5 · Streaming (for real-time UI)

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

---

## 6 · Multi-turn Conversation

```python
history = []

def chat(user_msg: str) -> str:
    history.append({"role": "user", "content": user_msg})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are Arbiey, a compassionate AI daily companion...",
        messages=history,
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply
```

---

## 7 · Error Handling & Retry

```python
import time
from anthropic import RateLimitError, APIConnectionError

def safe_call(prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            r = client.messages.create(
                model="claude-sonnet-4-6", max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            return r.content[0].text
        except RateLimitError:
            wait = 2 ** attempt
            print(f"Rate limit — waiting {wait}s…")
            time.sleep(wait)
        except APIConnectionError as e:
            print(f"Connection error: {e}")
            break
    return "[ERROR: API unavailable]"
```

---

## 8 · Token & Cost Awareness

```python
# Always check token usage
response = client.messages.create(…)
usage = response.usage
print(f"Input: {usage.input_tokens} | Output: {usage.output_tokens}")

# Rough cost estimate (Sonnet 4.6 pricing, subject to change)
# Input:  ~$3 / 1M tokens
# Output: ~$15 / 1M tokens
cost_usd = (usage.input_tokens * 3 + usage.output_tokens * 15) / 1_000_000
print(f"Estimated cost: ${cost_usd:.6f}")
```

---

## 9 · Malaysian Regulatory Checklist

Before deploying any Claude API integration under Ardoop Technologies:

- [ ] System prompt explicitly states HITL requirement
- [ ] No raw PII passed to API without PDPA consent
- [ ] Outputs for children/minors comply with CPC
- [ ] Risk-reduction measures per RMC applied
- [ ] Bilingual output available for public-facing features
- [ ] Audit log maintained (model used, timestamp, reviewer)
- [ ] `ethical-ai-my` governance principles referenced in design doc

---

## 10 · Quick Reference

| Item | Value |
|---|---|
| API base | `https://api.anthropic.com` |
| Messages endpoint | `POST /v1/messages` |
| Auth header | `x-api-key: <your-key>` |
