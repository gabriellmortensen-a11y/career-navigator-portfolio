# Example — one requirement, end to end (synthetic)

**What this is:** a hand-built illustration of how data moves through the system, using an invented
person ("Dana", a logistics program manager) and an invented posting. **It is not system output.**
The *shapes* (field names, states, thresholds, the order of steps) are taken from the code at Live
`7322289`. The *content* is fictional, so nothing here is anyone's career record.

## 1. Evidence enters (Knowledge 02)

Dana writes on Add Evidence:

> At Northwind Freight I ran the carrier onboarding program. I cut onboarding from 21 days to 9 by
> moving document checks into a shared portal, and I trained 14 regional coordinators on it.

**Sentences are offered by rule; Dana ticks the spans.** The Change Document's contract checks, in
code, that every span is a verbatim substring:

```json
{
  "operation": "ADD",
  "supplied": {
    "role_id": "17",
    "locator": "evidence-chat-…",
    "text": "At Northwind Freight I ran the carrier onboarding program. I cut onboarding from 21 days to 9 by moving document checks into a shared portal, and I trained 14 regional coordinators on it.",
    "spans": [
      "I ran the carrier onboarding program",
      "I cut onboarding from 21 days to 9 by moving document checks into a shared portal",
      "I trained 14 regional coordinators on it"
    ]
  },
  "admission": {
    "ready": true,
    "missing_required": [],
    "problems": [],
    "missing_optional": [{"field": "occurred", "label": "…"}],
    "unknown_fields": []
  }
}
```

Dana presses Apply. The source, three claims and one story are written, all carrying `role_id = 17`.
A claim citing another role's source would be refused by PostgreSQL.

## 2. A posting is read (Applications 01)

The invented posting has the line: *"Experience improving partner onboarding processes, ideally with
self-service tooling."*

| Step | Kind | Result |
|---|---|---|
| Line label | Code | `ask` |
| "Is this a requirement?" | Jev | 0.93 (kept; < 0.5 would be set aside) |
| Employer-only names | Code | none to reword |
| Fact or requirement | Code | requirement (not degree, eligibility, location or bare years) |

## 3. Evidence is matched (Architecture 03)

| Step | Kind | Result |
|---|---|---|
| Nominators (best sentence, whole story, named terms) | Embeddings + code | Dana's onboarding story nominated by best sentence and whole story |
| "Is the story related?" | Jev | 0.88 (≥ 0.3) |
| "Does this sentence establish the requirement?" | Jev | "I cut onboarding from 21 days to 9 by moving document checks into a shared portal" → 0.71 |
| Verdict | Code | **direct** (≥ 0.5) → requirement **strong** |
| "Would a recruiter pass without it?" | Jev | 0.42 (not a deal-breaker even if it were missing) |

## 4. The résumé is written (Applications 03)

The selector sees `R1…Rn` and the numbered stories, and answers `{"numbers": [3, 1, 4]}`. Dana's
story is number 3. Code copies stories 3, 1 and 4 verbatim into the writer's prompt. The writer
never sees R1…Rn. The writer answers:

```json
{"bullets": [
  {"story": 3, "text": "Cut carrier onboarding from 21 to 9 days by moving document checks into a shared portal; trained 14 regional coordinators."}
]}
```

`story` must be one of the numbers sent. The bullet is stored with story 3's event id, under role 17,
in state `UNGROUNDED`.

## 5. What would be caught, and what would not

| If the writer had written… | What happens on Live |
|---|---|
| "…under role 22's evidence" | **Refused by the database** (composite foreign key) |
| `{"story": 9, …}` when only 3, 1 and 4 were sent | **Dropped** (schema enum) |
| "Led a company-wide onboarding transformation" | **Not caught at build time.** The agency check runs only inside Fix. A reviewer may report it |
| "Cut onboarding by 60%" (a figure Dana never stated) | **Not caught at build time** on this flow. The editor's gate would refuse it only if the *editor* introduced it |

This is why the design is described as controlled inputs plus attribution, and **not** as
hallucination-proof ([Case study 02](../../case-studies/02-preventing-unsupported-claims.md#results-and-limitations)).
