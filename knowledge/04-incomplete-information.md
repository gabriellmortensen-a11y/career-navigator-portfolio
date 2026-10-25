# Knowledge 04 — Incomplete information

*Knowledge 3.0 · describes Live `7322289` (2026-10-24)*

**The question this answers:** what does the system do when the evidence does not say enough?

The design answer is **ask, label or leave it out. Never fill it in.** A gap stays visible as a gap
until the person supplies evidence or says there is none.

## States that are not "no"

Several states are stored explicitly so that *unknown* is never read as *absent*:

| State | Meaning | Where |
|---|---|---|
| `not_established` | The evidence on hand does not show it, which is not the same as the person lacking it | Chat assessments, shared conversations, interview answers |
| `unreviewed` | "Not a verdict" | Requirement readings |
| `confirmed_none` | The person said they have not done it. The only state that speaks to experience, and only on their word | Chat assessment |
| `not_done` → **Growth area** | A limit the person stated, kept on a separate list by its own press | Growth page |

**A Growth area is never evidence.** A test asserts that nothing in the résumé, apply, outreach or
pipeline code reads it ([K-28](../evidence/03-claim-index.md#k-28)).

## Years are counted only from what the person said

Requirements like "5+ years of SQL" are split by rules into years, named tools ("or similar") and
how the tools were used. The rule for years is strict:
- They count only from stated numbers ("six years"), date ranges or "since 2019" **in the person's
  own words**.
- Spans across employers are summed.
- Employment dates are never used: "Five years of employment is never five years of a tool."

A shortfall is said plainly: "N of the M the posting asks for"
([K-26](../evidence/03-claim-index.md#k-26)).

**An inconsistency, stated.** *Tune my evidence* uses a different rule. It sums dated roles that Jev
reads as that function and lists undated roles without counting them. Two features can therefore
give different year counts for the same person ([D-14](../evidence/05-discrepancies.md#d-14)).

## What counts as a gap

A requirement the evidence shows only lightly, or not at all, is a **gap** only if a reader would
likely pass on the candidate without it:
1. Jev is asked per requirement whether a recruiter, and separately a hiring manager, would pass on
   someone who doesn't show it.
2. A missing requirement at ≥ 0.6 is a deal-breaker.
3. Everything else is "could be stronger", which is optional
   ([A-06](../evidence/03-claim-index.md#a-06)).

The product owner set this definition: "if they wouldn't pass on you, they're really not gaps."

After a résumé exists, the model reviewers' actual reading overrides the estimate. What a model reviewer who said *no*
found short and called material becomes a gap for that reader
([A-07](../evidence/03-claim-index.md#a-07)).

Degree, years-as-a-fact, location and work eligibility are **facts to confirm**, not gaps:
- Citizenship, residency, visa and export-control lines are never sent to the reviewers.
- A missing degree reaches the reviewers labelled as a *risk*, "never a reason to decline".

The product owner set both rules after a review declined an above-typical résumé on exactly those
two grounds ([A-04](../evidence/03-claim-index.md#a-04)).

## Asking instead of assuming

- **Guided gap discovery** asks one question per turn. *Code* decides that a dimension (years,
  tools, use) is answered, and *code* decides when to stop. The model's own claim that something was
  answered is not trusted. When the person says "that's all", the requirement is recorded as
  reviewed and is never treated as a declined answer to the others
  ([A-08](../evidence/03-claim-index.md#a-08)).
- **The chat's policy:** "What they didn't do or can't say is a limit, never a fact … never invent
  the missing part."
- **Missing results go to the person.** After a résumé is written, a story with no stated result or
  a role with no stated scope becomes a "What to do next" action. Nothing is inferred
  ([P-31](../evidence/03-claim-index.md#p-31)).

## Career breaks

The rules for career breaks ([K-29](../evidence/03-claim-index.md#k-29)):
- A break is detected deterministically: ≥ 10 years with no dated paid role.
- Undated roles are never read as unemployment.
- Chart My Course **asks** before a build; the reason for a break is never asked for.
- Only a confirmed break changes recency, rendering or what reviewers are told.

Gaps shorter than ten years are not surfaced at all. That is a known limit, not a feature.

## Unreadable job postings

The same principle applies on the job side. A posting that cannot be read is never guessed at:
- **Save anyway** keeps the title, company and link under **Needs details**, with no requirements.
- A **paste box** asks for the text.
- Nothing is assessed or written until the text exists
  ([A-36](../evidence/03-claim-index.md#a-36)).

## Where the implementation widens instead of narrowing

*Ask your record* narrows "sufficient" to "partial" when gaps are named. However, when the model
returns neither field, the fallback is "sufficient", which widens. That contradicts the adjacent
comment "Code narrows and never widens" ([D-15](../evidence/05-discrepancies.md#d-15)).

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Years only from stated numbers or dates | Verified | [K-26](../evidence/03-claim-index.md#k-26) |
| Gap = a reader would pass (Jev + thresholds) | Limited (calibrated on one account against model reviewers) | [A-06](../evidence/03-claim-index.md#a-06) |
| Eligibility never screened; degree as risk | Verified | [A-04](../evidence/03-claim-index.md#a-04) |
| Growth areas kept apart from evidence | Verified | [K-28](../evidence/03-claim-index.md#k-28) |
| Career breaks asked, not inferred | Verified | [K-29](../evidence/03-claim-index.md#k-29) |
| Explicit not-established / unreviewed states | Verified | [K-30](../evidence/03-claim-index.md#k-30) |
| Unreadable postings held, not guessed | Verified | [A-36](../evidence/03-claim-index.md#a-36) |
