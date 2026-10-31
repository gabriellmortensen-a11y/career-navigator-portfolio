# Knowledge 04 — Incomplete information

*Knowledge 3.1 · describes Live `00eac95` (2026-10-31)*

**The question this answers:** what does the system do when the evidence does not say enough?

The design answer is **ask, label or leave it out. Never fill it in.** A gap stays visible as a gap
until the person supplies evidence or says there is none.

## States that are not "no"

Several states are stored explicitly so that *unknown* is never read as *absent*:

| State | Meaning | Where |
|---|---|---|
| `not_established` | The evidence on hand does not show it, which is not the same as the person lacking it | Chat assessments, living-résumé answers, interview answers |
| `unreviewed` | "Not a verdict" | Requirement readings |
| `confirmed_none` | The person said they have not done it. The only state that speaks to experience, and only on their word | Chat assessment |
| `not_done` → **Growth area** | A limit the person stated, kept on a separate list by its own press | Growth page |
| "missing — no verified evidence on your record yet" | A need of an interview answer that no verified claim shows. The coach asks about it; it never fills it with weaker material | Interview coach ([A-63](../evidence/03-claim-index.md#a-63)) |
| `interpreted_<pattern>` | A living-résumé answer to a situational question: an inference from recorded decisions, with how well they support it (strong, limited, mixed, none). Without a surviving citation it is "not established" | Living résumé ([A-114](../evidence/03-claim-index.md#a-114)) |
| `division` empty | A requirement line not read for several asks (a short line never is). A line read once is `whole` or `divided`, and its asks are `part` | Requirement readings ([A-05](../evidence/03-claim-index.md#a-05)) |

**A Growth area is never evidence.** A test, a text scan for the Growth table's name, asserts that
nothing in the résumé, apply, outreach or pipeline code reads it ([K-28](../evidence/03-claim-index.md#k-28)). Since 2026-10-29 a limit is offered for Growth on the turn
the person states it, once, and never again for what is already listed for that requirement; adding
it stays their own press ([A-108](../evidence/03-claim-index.md#a-108)). Since 2026-10-30 each Growth item can carry an action
plan: an outcome that would get them evidence, and milestones to it. Plans and milestones are never
evidence either. The plan call is never shown the record's text, but the boundary test names only
the Growth list's table (which holds the plans), not the milestones' table or the plan modules ([K-33](../evidence/03-claim-index.md#k-33)).

## Years are counted only from what the person said

Requirements like "5+ years of SQL" are split by rules into years, named tools ("or similar") and
how the tools were used. The rule for years is strict:
- They count only from stated numbers ("six years"), date ranges or "since 2019" **in the person's
  own words**.
- Spans across employers are summed.
- Employment dates are never used: "Five years of employment is never five years of a tool."

A shortfall is said plainly: "N of the M the posting asks for"
([K-26](../evidence/03-claim-index.md#k-26)).

**An inconsistency, stated.** Career Direction's role pages use a different rule. They sum dated
roles that Jev reads as that function and list undated roles without counting them. Two features
can therefore give different year counts for the same person ([D-14](../evidence/05-discrepancies.md#d-14)). (Until 2026-10-30
that reading was the *Tune my evidence* page, which was retired and its role readings kept on
Career Direction: [A-107](../evidence/03-claim-index.md#a-107).)

## What counts as a gap

A requirement the evidence shows only lightly, or not at all, is a **gap** only if a reader would
likely pass on the candidate without it:
1. Jev is asked per requirement whether a recruiter, and separately a hiring manager, would pass on
   someone who doesn't show it.
2. A missing requirement at ≥ 0.6 is a deal-breaker.
3. Everything else is "could be stronger", which is optional
   ([A-06](../evidence/03-claim-index.md#a-06)).

The product owner set this definition: a gap is only what a reader would pass on you without. In
the owner's words: "if that's the case, they're really not gaps" (`e718941`).

After a résumé exists, the model reviewers' actual reading overrides the estimate. What a model reviewer who said *no*
found short and called material becomes a gap for that reader
([A-07](../evidence/03-claim-index.md#a-07)).

Degree, years-as-a-fact, location and work eligibility are **facts to confirm**, not gaps:
- Citizenship, residency, visa and export-control lines are never sent to the reviewers.
- A missing degree reaches the reviewers labeled as a *risk*, "never a reason to decline".

The product owner set both rules after a review declined an above-typical résumé on exactly those
two grounds ([A-04](../evidence/03-claim-index.md#a-04)). Since 2026-10-27 a degree, or any other fact to confirm, is never a
gap on the résumé review either.

Two more rules decide what is *not* a gap, and how gaps are counted
([A-06](../evidence/03-claim-index.md#a-06), [A-78](../evidence/03-claim-index.md#a-78)):
- **A line about the role is never a gap.** Jev answers two questions about each line, once at
  Chart My Course, cached: does it describe the role rather than something a candidate could show?
  When both readings are low, the line leaves the gap queue.
- **Related gaps count as one, everywhere.** Since 2026-10-30 the opportunity page, the review page,
  the opportunities pane and the chat all count a theme as one gap. A gap whose saved story still
  reads light stays open; the chat says how many are still open and how many are still to talk
  through.

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
- **The interview coach asks what nothing verified shows.** Each answer has needs set by code from
  the role reading. A need with no verified claim is asked about, one question at a time
  ([A-63](../evidence/03-claim-index.md#a-63)). A reason for wanting the role is drafted from the record and labeled as
  inferred; with nothing to infer from, the coach says so, then asks ([A-68](../evidence/03-claim-index.md#a-68)).

## Silence on a shared record

The living résumé answers visitors from what the owner chose to share. What that record is silent on
is not a gap to volunteer:
- A posting sent to it is answered with strengths only. Anything the shared record doesn't cover is
  said only when the visitor asks about it, as not on the shared record, "which doesn't mean I have
  no experience with it". This is held by the policy and the answer's shape, not by code
  ([A-113](../evidence/03-claim-index.md#a-113)).
- A situational question is answered as an interpretation, with the strength of the pattern said;
  when the record can't predict it, the answer says so and suggests asking the owner
  ([A-114](../evidence/03-claim-index.md#a-114)).
- A personal question is answered only from what the owner explicitly said, and predictions
  (offers, relocation, pay) are left to the owner ([A-115](../evidence/03-claim-index.md#a-115)).

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
| Growth areas kept apart from evidence | Limited (the boundary test is a text scan) | [K-28](../evidence/03-claim-index.md#k-28) |
| Growth offered on the turn it is stated, once | Verified | [A-108](../evidence/03-claim-index.md#a-108) |
| Growth plans and milestones never evidence | Limited (the boundary test names the Growth list's table, which holds the plans, not the milestones' table or the plan modules) | [K-33](../evidence/03-claim-index.md#k-33) |
| A theme is one gap everywhere; a light save stays open | Verified | [A-78](../evidence/03-claim-index.md#a-78) |
| Interview answers ask for what nothing verified shows | Verified | [A-63](../evidence/03-claim-index.md#a-63) |
| A drafted reason labeled as inferred | Verified | [A-68](../evidence/03-claim-index.md#a-68) |
| Living résumé volunteers no gap | Limited (policy and shape, not code) | [A-113](../evidence/03-claim-index.md#a-113) |
| Situational questions as labeled interpretations | Verified | [A-114](../evidence/03-claim-index.md#a-114) |
| Personal questions and predictions | Limited | [A-115](../evidence/03-claim-index.md#a-115) |
| Requirement division at Chart My Course | Verified (registry test) | [A-05](../evidence/03-claim-index.md#a-05) |
| Tune my evidence | Superseded (replaced by Career Direction role pages, `a98124c`) | [A-107](../evidence/03-claim-index.md#a-107) |
| Career breaks asked, not inferred | Verified | [K-29](../evidence/03-claim-index.md#k-29) |
| Explicit not-established / unreviewed states | Verified | [K-30](../evidence/03-claim-index.md#k-30) |
| Unreadable postings held, not guessed | Verified | [A-36](../evidence/03-claim-index.md#a-36) |
