# Product 02 — Principles, and where each came from

*Product 4.0 · describes Live `7322289` (2026-10-24)*

Each principle below is a rule the system now follows. For each one, the table records the failure
it answers and how it is enforced. Where the implementation does not yet fully honour a rule, the
exception is named.

## 1. A model may propose; only a person may approve

| | |
|---|---|
| **Came from** | Conversations and model output were becoming career "facts" without anyone saying they were true. In August 2026, a stored enrichment turned out to be the exact concatenation of seven answers, one of them a retraction ([H-03](../evidence/03-claim-index.md#h-03)). |
| **Enforced by** | One writer, Change Documents with a deterministic contract, and refusals kept with their reason ([K-10](../evidence/03-claim-index.md#k-10)). |
| **Exceptions, named** | Story composition is automatic. A brought résumé is recorded on "Accept as is" without its proposal page ([Knowledge 02](../knowledge/02-admission-and-acceptance.md#where-the-implementation-and-the-rule-still-disagree)). |

## 2. Evidence from different jobs never composes into one claim

| | |
|---|---|
| **Came from** | The September build established requirements by combining two or three unrelated roles. Each claim was true in parts and not true of any single piece of work ([H-07](../evidence/03-claim-index.md#h-07)). |
| **Enforced by** | PostgreSQL composite foreign keys on evidence and on résumé bullets ([K-01](../evidence/03-claim-index.md#k-01), [K-02](../evidence/03-claim-index.md#k-02)). |

## 3. Defects are fixed at their source, never papered over

| | |
|---|---|
| **Came from** | On 2026-10-12, Live résumés lost their summaries to a check that refused them. The first fix was an automatic repair phase after the build. It was removed the same day after I asked to "prevent the problems without another writing session or more model calls". The next day I set the rule: a defect "should not be … introduced at all", and "Defects always fixed, not papered over with a fix." |
| **Enforced by** | The project rules (2026-10-13). Reviewers and checks may detect and report. A fix changes the producing stage's input, its output shape, or what it may select. |
| **Examples** | Summaries over the length limit were fixed by giving the writer a sentence shape: 73% and 96% over the limit became 0 of 20 ([M-17](../evidence/04-metric-ledger.md#m-17)). Bullets stored against the wrong story were fixed by a schema enum, not a post-hoc matcher ([A-13](../evidence/03-claim-index.md#a-13)). |
| **Exceptions, named** | Fix is a person-pressed repair button and is called a catch-and-repair step ([A-17](../evidence/03-claim-index.md#a-17)). Excluding flagged stories is a filter that I chose deliberately on evidence ([K-17](../evidence/03-claim-index.md#k-17)). |

## 4. Jev selects; models reason and write

| | |
|---|---|
| **Came from** | Model judges kept "filling in gaps where evidence should be". A probability model asked fixed, typed questions (Jev) was cheaper, more stable and, on logged readings, kept more of the directly relevant evidence ([M-23](../evidence/04-metric-ledger.md#m-23)). On 2026-10-12 I said: "A model call should only be used for reasoning situations, not if it meets a rank or if it's a state. Jev should be used for that." |
| **Enforced by** | Story reading, assessment, discovery screening, interview evidence and de-duplication all use Jev with thresholds in code. A registry test and a code search show no model capability in Chart My Course or Quick add; call-tripping tests forbid model calls in Change Course and the journeys ([P-06](../evidence/03-claim-index.md#p-06)). |
| **Exceptions, named** | A language model still selects stories in the recruiter-selects résumé flow. That is my own design: I reproduced by hand what I wanted and asked for exactly that. Models also still decide in three other places: the gap-panel verdict, concept indexing, and What's Next's fix kind ([D-10](../evidence/05-discrepancies.md#d-10)). |

## 5. One writer pass, one editor pass, no loops

| | |
|---|---|
| **Came from** | Writer → reviewer → writer cycles made quality depend on the last pass and made cost and time unbounded. |
| **Enforced by** | There is no regeneration after review. Reviewers report. The single editor pass changes wording only, through a code gate ([A-16](../evidence/03-claim-index.md#a-16)). |
| **Exceptions, named** | Each section has a *draft* call and a *tighten* call, editor corrections get a verify read, and Fix can rewrite up to twice when a person presses it. The rule is interpreted, not literal ([D-09](../evidence/05-discrepancies.md#d-09)). |

## 6. Gaps are what a reader would pass on, not everything short

| | |
|---|---|
| **Came from** | One job showed 15 "gaps" while both model reviewers said yes ([M-58](../evidence/04-metric-ledger.md#m-58)). My words: "if they wouldn't pass on you, they're really not gaps." |
| **Enforced by** | Jev "would pass" per reader seat, with thresholds calibrated against reviewer verdicts. The model reviewers' actual reading overrides the estimate ([A-06](../evidence/03-claim-index.md#a-06), [A-07](../evidence/03-claim-index.md#a-07)). |

## 7. Unknown is never "no"; nothing is invented to fill a gap

| | |
|---|---|
| **Came from** | Early systems scored a failed judgement as a verdict and reported 22 of 22 covered where a re-score found 10 covered and 12 partial (72% weighted) ([H-06](../evidence/03-claim-index.md#h-06)). |
| **Enforced by** | Explicit `not_established`, `unreviewed` and `confirmed_none` states. Years are counted only from what the person said. Career breaks are asked about. Unreadable postings are held, not guessed ([Knowledge 04](../knowledge/04-incomplete-information.md)). |

## 8. Never screen people on eligibility

| | |
|---|---|
| **Came from** | A review declined an above-typical résumé over citizenship and a degree. I've been interviewed for plenty of roles that "required" a degree I don't have. |
| **Enforced by** | Eligibility lines never reach the reviewers, and a degree is a visible risk, not a blocker ([A-04](../evidence/03-claim-index.md#a-04)). |
| **Known defect** | The eligibility pattern over-matches some technical requirements ([D-11](../evidence/05-discrepancies.md#d-11)). |

## 9. More evidence on the page beats a more selective picker

| | |
|---|---|
| **Came from** | An experiment told the story picker which stories strongly show each requirement. Résumés fell from 18–20 bullets to 10–13, and the reviewers found no gain. It was reverted in 23 minutes ([M-18](../evidence/04-metric-ledger.md#m-18)). |
| **Applied as** | Résumé changes are judged first by bullet and story count, then by what reviewers find. Nothing narrows what the picker may choose. |

## 10. Everything goes to Beta first; Live only after I've looked

| | |
|---|---|
| **Came from** | On 2026-10-14 many changes went straight to Live, and I found problems there: labels shifting after edits, status not saving, slow pages. |
| **Enforced by** | `ship.sh` stops at Beta. Live deploys only from a branch of approved commits, and only after the full suite passes on that exact code ([P-11](../evidence/03-claim-index.md#p-11)). |

## 11. Quote measured cost, never an estimate

| | |
|---|---|
| **Came from** | A chat turn was once described as costing $0.02. That was the estimate passed to a spend check; the measured cost was about $0.004 ([M-21](../evidence/04-metric-ledger.md#m-21)). In the earlier build, worst-case holds ran 9.2× actual charges ([M-32](../evidence/04-metric-ledger.md#m-32)). |
| **Applied as** | Every figure in this portfolio comes from the call ledger or a recorded run, with its definition. |
