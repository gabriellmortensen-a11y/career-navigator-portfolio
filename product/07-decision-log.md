# Product 07 — Decision log

*Product 4.0 · decisions since the 2026-09-29 baseline, plus the earlier ones the current design rests on*

Each entry gives the decision, its trigger and what it replaced. Unless marked "owner", decisions
were proposed by the implementing agent and accepted by me. Dates are from git. Where my own words
are quoted, they come from the commit or rule that records them.

## Before the baseline (earlier build, summarised)

| Date | Decision | Trigger | Replaced |
|---|---|---|---|
| 2026-08 | A model may propose; only a person may approve (in the agent rules from their first version) | Conversations becoming "knowledge" without acceptance | Free model writes to the record ([H-03](../evidence/03-claim-index.md#h-03)) |
| 2026-08-13 | Fix canonicalization's prompt contamination | 141 of 285 proposals cited text the system itself had put into the prompt | — ([M-01](../evidence/04-metric-ledger.md#m-01)) |
| 2026-08-14 | A failed judgement is never a verdict | Coverage swinging 78/64/70% across runs | Failures displayed as "missing" ([H-06](../evidence/03-claim-index.md#h-06)) |
| 2026-09-10 | **Owner:** retire the human acceptance gate before résumé generation | It assigned to a person work the system is supposed to do | Per-résumé evidence ranking by hand ([H-09](../evidence/03-claim-index.md#h-09)) |
| 2026-09-17 | Persist gated findings | 0 of 17 requirements worded the same twice across 31 runs | Re-deriving every run ([M-34](../evidence/04-metric-ledger.md#m-34)) |
| 2026-09-24 → 29 | **Owner:** answer from one coherent body of work ("Bounded Fit"); it became the product through use | Requirements "established" by combining unrelated roles | Job Fit ([H-07](../evidence/03-claim-index.md#h-07)) |
| 2026-09-29 | **Owner:** never push to Live without complete tests and my approval | A deploy override shipped untested code | The override ([H-11](../evidence/03-claim-index.md#h-11)) |

## Since the baseline

| Date | Decision | Trigger | Replaced |
|---|---|---|---|
| 2026-10-02 | **Owner:** delete the Staged Planner's post-draft stages ("the approach was wrong, so the code is deleted rather than parked"); stop page rationing on Beta | Each change broke the 10,000-test legacy suite; pages rationed real evidence away | Page-fitting machinery |
| 2026-10-03 | **Extract a clean application**: migrate only what is understood; PostgreSQL from day one; the role boundary in the schema; no runtime fallback to the old system | Retrieval in the old system ignored the job id; ~10,000 contract tests slowed every change | The earlier codebase ([P-30](../evidence/03-claim-index.md#p-30)) |
| 2026-10-03 | Reverse an optimiser's acceptance | Evaluator noise (readings ranged by up to 3 major findings) exceeded the improvement | The optimiser run's accepted policy ([M-26](../evidence/04-metric-ledger.md#m-26)) |
| 2026-10-05 | Database-enforced multi-tenancy (forced RLS, non-owner runtime role, explicit-account imports) | A second person needed their own record; during the work an agent's cleanup script, running as schema owner, deleted 17,183 rows | The inventory's REJECT of multi-tenancy ([H-17](../evidence/03-claim-index.md#h-17)) |
| 2026-10-05 | Six pieces per requirement, read once | Exhaustive review: 1,164 judgements, $0.45, 267 s per posting | Exhaustive relationship review ([M-22](../evidence/04-metric-ledger.md#m-22)) |
| 2026-10-05 | Deploy by pulling a named commit; ship stops at Beta | A half-finished change once reached production by file sync | rsync deploys |
| 2026-10-08 | Durable background operations | A restart erased accepted work | In-memory tasks ([P-09](../evidence/03-claim-index.md#p-09)) |
| 2026-10-09 | Change Course uses O*NET's expert relations, with zero model calls | Computed similarity "put physicians beside nurses" | — ([A-58](../evidence/03-claim-index.md#a-58)) |
| 2026-10-12 | **Owner:** "A model call should only be used for reasoning situations, not if it meets a rank or if it's a state. Jev should be used for that." | Model judges filling gaps where evidence should be | Model reading of clear cases ([M-23](../evidence/04-metric-ledger.md#m-23)) |
| 2026-10-12 | **Owner:** prevent defects without extra calls; remove the automatic repair phase the same day it shipped | Summaries lost to refusals | Automatic post-build repair ([A-17](../evidence/03-claim-index.md#a-17)) |
| 2026-10-13 | **Owner rules:** fix defects at the source; filtering isn't a fix; Jev selects, models write; one writer pass, one editor pass, no loops | Repeated catch-and-repair proposals | — ([Product 02](02-principles.md)) |
| 2026-10-13 | **Stories**: glue fragments of the same work within a role; one bullet per story | Evidence missed "at the seams" between fragments | Per-piece model reading ([K-06](../evidence/03-claim-index.md#k-06)) |
| 2026-10-13/14 | **Owner:** the recruiter-selects résumé flow, "the product owner's four steps for every section"; never pass the writer text of what to write from the selector | My own manual experiment beat every engineered variant | Older bullet writer, summary writers, review editor ([A-11](../evidence/03-claim-index.md#a-11)) |
| 2026-10-14 | **Owner:** flagged stories are not used ("If its flagged it shouldn't be used. We have proof now on why.") | A Live résumé opened a role with a flagged belief-statement | The 2026-10-07 "reading, not a gate" decision ([K-17](../evidence/03-claim-index.md#k-17)) |
| 2026-10-14 | **Owner:** everything through Beta first | Direct-to-Live changes broke things in use | Direct deploys ([P-11](../evidence/03-claim-index.md#p-11)) |
| 2026-10-19 | **Owner:** never screen on citizenship; a degree is a risk, not a blocker | Both reviewers declined an above-typical résumé on those grounds | Reviewers seeing eligibility lines ([A-04](../evidence/03-claim-index.md#a-04)) |
| 2026-10-19 | Separate runner process | Pages at 4–6 s during background work | Threads in the web process ([M-29](../evidence/04-metric-ledger.md#m-29)) |
| 2026-10-20 | Per-task models in a governed document; Haiku for short tasks; gpt-5-mini kept for résumé work | A budget-capped trial on a copy of Live | One default model ([M-19](../evidence/04-metric-ledger.md#m-19), [M-20](../evidence/04-metric-ledger.md#m-20)) |
| 2026-10-20 | **Owner:** discovery profiles only from my own record ("stick to my evidence and professions"); apply kits never submit | Suggestions drawn from saved jobs | — ([A-30](../evidence/03-claim-index.md#a-30), [A-38](../evidence/03-claim-index.md#a-38)) |
| 2026-10-20 | Keep Tavily for company research; Claude web search stays Beta-only | Small Beta comparison: staler sources, missed the official site, higher cost | — ([A-51](../evidence/03-claim-index.md#a-51)) |
| 2026-10-21 | **Owner:** Beta and Live unified ("get parity between the two so only one test needs to happen") | Two diverging histories doubled testing | Separate Beta branch |
| 2026-10-22 | **Owner:** assess first; nothing writes a résumé without the Write press ("There should be a gate for review before doing it") | Discovery and charting were writing résumés automatically | One-press Chart My Course ([A-37](../evidence/03-claim-index.md#a-37)) |
| 2026-10-22 | **Owner:** the chat confirms the role before saving ("it should confirm what role it was with, even if it thinks it knows") | An addition filed under the chat's guess | — ([K-13](../evidence/03-claim-index.md#k-13)) |
| 2026-10-23 | **Owner:** a gap is only what a reader would likely pass on | "Both approve but 15 gaps" | Gap = anything short ([A-06](../evidence/03-claim-index.md#a-06)) |
| 2026-10-23 | **Owner:** "a real reading should over ride, thats common sense right?" | Estimate and review disagreed on one job | Estimate-only gaps ([A-07](../evidence/03-claim-index.md#a-07)) |
| 2026-10-23 | Reject the selector-narrowing experiment (23 minutes on Beta); **owner:** "whatever gives the most bullets" | 18–20 → 10–13 bullets, no reviewer gain | — ([M-18](../evidence/04-metric-ledger.md#m-18)) |
| 2026-10-23 | Reject splitting glued stories | 20 strong requirements became light over 63 jobs | — ([K-07](../evidence/03-claim-index.md#k-07)) |
| 2026-10-23 | Related gaps as themes, each requirement still tracked; **owner:** "it needs to be a general thing so it works beyond just sox" | A 13-requirement compliance cluster asked as 13 gaps | One gap per turn ([A-09](../evidence/03-claim-index.md#a-09)) |
| 2026-10-24 | Bullets name their story by schema; shared sentences reach the writer once | 17 bullets from 15 stories stored by position; **owner** spotted a near-duplicate bullet | Position matching ([A-13](../evidence/03-claim-index.md#a-13), [A-14](../evidence/03-claim-index.md#a-14)) |

## Decisions still open

These are recorded as open, not inferred:
- **Grounding on Live.** Whether to restore an automated support check on Live résumés, as
  measurement or as a gate, now that the input-side design carries the load ([K-23](../evidence/03-claim-index.md#k-23)).
- **Narrow model selection.** Whether story selection and the gap-panel judgement should move to
  Jev ([D-10](../evidence/05-discrepancies.md#d-10)).
- **Two open security and privacy findings.** How to fix them at the source (details withheld from
  this public version until fixed; [D-02](../evidence/05-discrepancies.md#d-02), [D-17](../evidence/05-discrepancies.md#d-17)).
- **Real outcomes.** Whether to connect real outcomes (status history) to the assessment
  calibration ([Roadmap](../ROADMAP.md)).
