# Product 02 — Principles, and where each came from

*Product 4.1 · describes Live `00eac95` (2026-10-31)*

Each principle below is a rule the system now follows. For each one, the table records the failure
it answers and how it is enforced. Where the implementation does not yet fully honor a rule, the
exception is named.

## 1. A model may propose; only a person may approve

| | |
|---|---|
| **Came from** | Conversations and model output were becoming career "facts" without anyone saying they were true. In August 2026, a stored enrichment turned out to be the exact concatenation of seven answers, one of them a retraction ([H-03](../evidence/03-claim-index.md#h-03)). |
| **Enforced by** | One writer, Change Documents with a deterministic contract, and refusals kept with their reason ([K-10](../evidence/03-claim-index.md#k-10)). |
| **Exceptions, named** | Story composition is automatic. A brought résumé is recorded on "Accept as is" without its proposal page ([Knowledge 02](../knowledge/02-admission-and-acceptance.md#where-the-implementation-and-the-rule-still-disagree)). |
| **Since 4.0** | The interview coach and the application chat now *offer* the person's own words for their record by code, and a disputed line becomes a correction to that exact text. Each still waits for their Save ([A-65](../evidence/03-claim-index.md#a-65), [A-69](../evidence/03-claim-index.md#a-69), [A-75](../evidence/03-claim-index.md#a-75)). Career Chat reads the account and writes nothing ([A-102](../evidence/03-claim-index.md#a-102)). |

## 2. Evidence from different jobs never composes into one claim

| | |
|---|---|
| **Came from** | The September build established requirements by combining two or three unrelated roles. Each claim was true in parts and not true of any single piece of work ([H-07](../evidence/03-claim-index.md#h-07)). |
| **Enforced by** | PostgreSQL composite foreign keys on evidence and on résumé bullets ([K-01](../evidence/03-claim-index.md#k-01), [K-02](../evidence/03-claim-index.md#k-02)). |

## 3. Defects are fixed at their source, never papered over

| | |
|---|---|
| **Came from** | On 2026-10-12, Live résumés lost their summaries to a check that refused them. The first fix was an automatic repair phase after the build. It was removed the same day after I asked to "prevent the problems without another writing session or more model calls". The next day I set the rule that a defect should not be introduced in the first place: "Defects always fixed, not papered over with a fix." (my words, in the project rules, `CLAUDE.md`) |
| **Enforced by** | The project rules (2026-10-13). Reviewers and checks may detect and report. A fix changes the producing stage's input, its output shape, or what it may select. |
| **Examples** | Summaries over the length limit were fixed by giving the writer a sentence shape: 73% and 96% over the limit became 0 of 20 ([M-17](../evidence/04-metric-ledger.md#m-17)). That shape no longer writes Live summaries: since 2026-10-28 they come from a positioning brief, and the professional summary has three required fields, asked for at the page's own character cap; a summary over the cap is flagged, not cut ([A-82](../evidence/03-claim-index.md#a-82), [A-101](../evidence/03-claim-index.md#a-101)). Bullets stored against the wrong story were fixed by a schema enum, not a post-hoc matcher ([A-13](../evidence/03-claim-index.md#a-13)). When a summary came out short of support, I asked for it to be placed as written with what was found shown, not swapped for a backup: "I dont ever want the default summaries to be a backup" (my words, `62d4327`; [DEC-53](07-decision-log.md#dec-53)). |
| **Exceptions, named** | Fix is a person-pressed repair button and is called a catch-and-repair step ([A-17](../evidence/03-claim-index.md#a-17)). A person-pressed red button writes one *missing* summary after the review, and nothing is reviewed again ([A-90](../evidence/03-claim-index.md#a-90), [DEC-56](07-decision-log.md#dec-56)). Excluding flagged stories is a filter that I chose deliberately on evidence ([K-17](../evidence/03-claim-index.md#k-17)). |
| **Known defect** | In the interview coach, approving a draft whose line Jev reads as unsupported makes the coach write it again: a check that triggers a rewrite ([D-31](../evidence/05-discrepancies.md#d-31)). |

## 4. Jev selects; models reason and write

| | |
|---|---|
| **Came from** | Model judges kept filling in gaps where evidence should have been. A probability model asked fixed, typed questions (Jev) was cheaper, more stable and, on logged readings, kept more of the directly relevant evidence ([M-23](../evidence/04-metric-ledger.md#m-23)). On 2026-10-12 I said: "A model call should only be used for reasoning situations, not if it meets a rank or if it's a state. Jev should be used for that." |
| **Enforced by** | Story reading, assessment, discovery screening, interview evidence and de-duplication all use Jev with thresholds in code. Since 2026-10-25 Jev also picks the claims an interview or application answer may use, checks each draft line against its sources, and orders the coach's topics ([A-63](../evidence/03-claim-index.md#a-63), [A-64](../evidence/03-claim-index.md#a-64), [A-73](../evidence/03-claim-index.md#a-73)). Since 2026-10-26 it reads what a coaching or application-chat message means, in place of phrase lists: "Hard coded signals are a failure" (my words, `0018434`; [A-66](../evidence/03-claim-index.md#a-66), [DEC-43](07-decision-log.md#dec-43)). It routes Career Chat's reads ([A-102](../evidence/03-claim-index.md#a-102)), classes the professional summary's stories against the posting's needs ([A-82](../evidence/03-claim-index.md#a-82)) and suggests links from portfolio artifacts to evidence ([K-34](../evidence/03-claim-index.md#k-34)). A registry test shows no model capability in Quick add, and exactly one in Chart My Course (below); call-tripping tests forbid model calls in Change Course and the journeys ([P-06](../evidence/03-claim-index.md#p-06)). |
| **Exceptions, named** | A language model still selects stories in the recruiter-selects résumé flow. That is my own design: I reproduced by hand what I wanted and asked for exactly that. Models also still decide in five other places: the gap-panel verdict, concept indexing, What's Next's fix kind, an application question's kind, and whether a requirement line holds several asks ([D-10](../evidence/05-discrepancies.md#d-10)). The last is a stated exception I chose on 2026-10-27: "one small call" over rules, at Chart My Course, and code keeps an ask only if it is made of the line's own words ([A-05](../evidence/03-claim-index.md#a-05), [DEC-47](07-decision-log.md#dec-47)). A few word lists still read the person's words when a dispute names "both" or "the first" ([D-33](../evidence/05-discrepancies.md#d-33)). |

## 5. One writer pass, one editor pass, no loops

| | |
|---|---|
| **Came from** | Writer → reviewer → writer cycles made quality depend on the last pass and made cost and time unbounded. |
| **Enforced by** | There is no regeneration after review. Reviewers report. The single editor pass changes wording only, through a code gate ([A-16](../evidence/03-claim-index.md#a-16)). Since 2026-10-29 each bullet is drafted as its finished line; only a bullet longer than two printed lines gets a second, shortening call ([A-91](../evidence/03-claim-index.md#a-91), [DEC-59](07-decision-log.md#dec-59)). Summaries are planned, restated in plain words, briefed and written once, never rewritten or replaced ([A-82](../evidence/03-claim-index.md#a-82), [A-84](../evidence/03-claim-index.md#a-84)). |
| **Exceptions, named** | The shortening call for long bullets, the editor corrections' verify read, and Fix, which can rewrite up to twice when a person presses it. A missing summary can be written after the review from a person-pressed button, without a new review ([A-90](../evidence/03-claim-index.md#a-90)). The rule is interpreted, not literal ([D-09](../evidence/05-discrepancies.md#d-09)). |

## 6. Gaps are what a reader would pass on, not everything short

| | |
|---|---|
| **Came from** | One job showed 15 "gaps" while both model reviewers said yes ([M-58](../evidence/04-metric-ledger.md#m-58)). A gap is only what a reader would pass on you without. My words: "if that's the case, they're really not gaps" (`e718941`). |
| **Enforced by** | Jev "would pass" per reader seat, with thresholds calibrated against reviewer verdicts. The model reviewers' actual reading overrides the estimate ([A-06](../evidence/03-claim-index.md#a-06), [A-07](../evidence/03-claim-index.md#a-07)). |

## 7. Unknown is never "no"; nothing is invented to fill a gap

| | |
|---|---|
| **Came from** | Early systems scored a failed judgment as a verdict and reported 22 of 22 covered where a re-score found 10 covered and 12 partial (72% weighted) ([H-06](../evidence/03-claim-index.md#h-06)). |
| **Enforced by** | Explicit `not_established`, `unreviewed` and `confirmed_none` states. Years are counted only from what the person said in the gap chat. Career breaks are asked about. Unreadable postings are held, not guessed ([Knowledge 04](../knowledge/04-incomplete-information.md)). The interview coach asks about a need nothing verified shows instead of filling it ([A-63](../evidence/03-claim-index.md#a-63)). |
| **Known inconsistency** | Career Direction's role pages count years from dated roles Jev reads as that function, so the two can disagree ([D-14](../evidence/05-discrepancies.md#d-14)). |

## 8. Never screen people on eligibility

| | |
|---|---|
| **Came from** | A review declined an above-typical résumé over citizenship and a degree. I've been interviewed for plenty of roles that "required" a degree I don't have. |
| **Enforced by** | Eligibility lines never reach the reviewers, and a degree is a visible risk, not a blocker ([A-04](../evidence/03-claim-index.md#a-04)). Since 2026-10-27 a degree is never a gap on the résumé review either ([A-06](../evidence/03-claim-index.md#a-06)). |
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
| **Enforced by** | `ship.sh` stops at Beta. Live deploys only from a branch of approved commits, and only after the full suite passes on that exact code ([P-11](../evidence/03-claim-index.md#p-11)). Since 2026-10-28 that branch is rebuilt for each release from Beta's commits by cherry-pick (`live-chat-reads`, `live-summaries`, `live-kept`), because Live leaves out three Beta-only features ([P-37](../evidence/03-claim-index.md#p-37)). |

## 11. Quote measured cost, never an estimate

| | |
|---|---|
| **Came from** | A chat turn was once described as costing $0.02. That was the estimate passed to a spend check; the measured cost was about $0.004 ([M-21](../evidence/04-metric-ledger.md#m-21)). In the earlier build, worst-case holds ran 9.2× actual charges ([M-32](../evidence/04-metric-ledger.md#m-32)). |
| **Applied as** | Every figure in this portfolio comes from the call ledger or a recorded run, with its definition. |
