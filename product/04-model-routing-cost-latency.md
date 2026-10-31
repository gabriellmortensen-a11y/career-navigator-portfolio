# Product 04 — Model routing, cost and latency

*Product 4.1 · describes Live `00eac95` (2026-10-31) · every figure is in the [metric ledger](../evidence/04-metric-ledger.md)*

## How a call gets its model

Every model call goes through one governed boundary ([P-01](../evidence/03-claim-index.md#p-01)):
1. **The stage must be governed.** It needs a promoted policy-document version, or a declared
   exemption with a written reason. There are 32 exemptions, mostly Jev questions, embeddings, search
   and scraping. The ten added since Product 4.0 are all Jev questions: the coach's claims, line
   checks, meaning and topic order; the application chat's story, likes and line checks; Career
   Chat's read routing and findings; and portfolio link suggestions.
2. **The model is chosen in a fixed order:** the caller's explicit model (tests and experiments) →
   the task's entry in the governed `model_assignments` document → the policy's own model → the
   application default (gpt-5-mini) ([P-02](../evidence/03-claim-index.md#p-02)).
3. **Unpriced models are refused** before anything is sent. There are no fallbacks. The summary
   path repeats the *same* call, up to three tries, when the provider fails on its side; that is a
   retry, not a fallback ([A-89](../evidence/03-claim-index.md#a-89)).
4. **Every call writes a row** recording stage, policy version, model, tokens (cached and reasoning
   separately), cost, seconds, outcome and context hash. Failures are written on their own
   transaction, so they survive the caller's rollback. Prompts are not stored, only their hash and
   sizes ([P-03](../evidence/03-claim-index.md#p-03)).

Changing a task's model on **Admin › Models** writes a new version of the assignments document,
recording who changed it and why. The recommended model is starred with the evidence for it.

**A seed assignment does not reach an existing database.** The assignments document is created from
the seed file only where none exists; after that Admin › Models owns it. Six tasks added to the seed
since Product 4.0 name Claude Haiku. On Live, the first calls of two of them ran on the default model
until the assignment was set by hand ([D-27](../evidence/05-discrepancies.md#d-27), [M-68](../evidence/04-metric-ledger.md#m-68)).

## Which model does what, and why

| Work | Model | Evidence for the choice |
|---|---|---|
| Résumé selector, writer, reviewers, editor, competencies, next actions | gpt-5-mini | Résumé trial (2026-10-19). Haiku was about half the cost, but reviewers counted fewer relevant accomplishments on 4 of 6 postings and found 2–4 grammar slips. Sonnet was about 3× the cost. The reviewer is held constant so verdicts stay comparable ([M-20](../evidence/04-metric-ledger.md#m-20)) |
| Résumé summaries (planner, plain words, brief, writers) and the career journey | gpt-5-mini, the application default | No assignment names these stages, so they take the default. On Live every call of both ran on gpt-5-mini ([M-68](../evidence/04-metric-ledger.md#m-68)) |
| Evidence chat, interview stages, research brief, expectation checks, claim extraction | Claude Haiku 5.5 | Replay of real calls. Chat 8 s vs 13 s at about half the cost; evidence answers 4 s vs 7 s at about a quarter; claim extraction about a tenth of the cost with every claim kept ([M-19](../evidence/04-metric-ledger.md#m-19)) |
| Role reading, application question and chat, requirement division, Growth plan and Navi on Growth (new since Product 4.0); interview coach turns and the living résumé (both use the evidence chat's assignment) | Claude Haiku 5.5 | The new ones are assigned in the seed as short reading tasks like those above, or by my instruction for Growth ("Use haiku for it", `1ea9a97`). Only the application chat's choice cites a measurement, an evaluation on one account ([M-72](../evidence/04-metric-ledger.md#m-72)). On Live every coach turn, role reading, question reading and living-résumé answer ran on Haiku; one application-chat call and two requirement-division calls ran on gpt-5-mini before their assignment was set; Growth has made no Live call yet ([M-68](../evidence/04-metric-ledger.md#m-68), [D-27](../evidence/05-discrepancies.md#d-27)) |
| Concept indexing | gpt-5-mini | Haiku tagged 2 of the 21 concepts gpt-5-mini tagged: far too strict |
| Relationship review / demand reading (older flow) | gpt-5-mini | Haiku stricter (55% / 62% agreement). Switching would change match counts everywhere, which is a product decision, not a cost one |
| Ranking, selection, state | Jev | Cheaper and more stable than a model judge. Kept more directly relevant evidence than cosine on 309 logged readings ([M-23](../evidence/04-metric-ledger.md#m-23)). Since Product 4.0 also: the coach's reading of what a message means, claim selection and line checks for interview and application answers, Career Chat's read routing, portfolio link suggestions |
| Independent quality evaluator | gpt-5 (fixed) | Used only in measurement |

**Model check** turns this into a repeatable process ([P-07](../evidence/03-claim-index.md#p-07)):
1. Replay real recent prompts through candidate models under a spending cap.
2. Score deterministically against the current model's own noise floor.
3. Recommend the cheapest model within 0.10.
4. Switch nothing until a person presses "Use this".

Three limits: it has not yet been run on Live; résumé stages cannot be replayed, so résumé model
choice still rests on the one trial; and none of the eight stages governed since Product 4.0 can be
replayed either. The role reading's assignment itself says "run a model check to confirm".

## What things cost (Live telemetry)

| What | Cost | Basis |
|---|---|---|
| Writing and reviewing one résumé (language-model calls) | **≈ $0.11** | 32 résumés, 2026-10-21 → 10-24 ([M-03](../evidence/04-metric-ledger.md#m-03)) |
| — the selector's and writer's share | ≈ $0.06 | Same ([M-03](../evidence/04-metric-ledger.md#m-03) breakdown) |
| — the two-seat review's share | ≈ $0.03 | Same |
| Recorded run total (upper bound) | mean $0.19 | Includes concurrent account spend; not a per-résumé cost ([M-04](../evidence/04-metric-ledger.md#m-04)) |
| Preparing and assessing a job (Chart My Course) | mean $0.02, median $0.015; mean 54 s | 89 runs on 29 jobs; same upper-bound caveat ([M-51](../evidence/04-metric-ledger.md#m-51)) |
| One evidence-chat call (Haiku, cached) | mean $0.0033 | 108 calls ([M-21](../evidence/04-metric-ledger.md#m-21)) |
| One ordinary discovery run | $0.016–0.064 | 18 runs ([M-10](../evidence/04-metric-ledger.md#m-10)) |
| Company research | ≤ 4 searches + one Haiku brief | Code bound |

**Since Product 4.0 (Live telemetry, read 2026-10-31).** Each row is its own system state; none
continues a row above as a trend.

| What | Cost | Basis |
|---|---|---|
| Résumé run after the speed route (recorded run total, upper bound) | mean $0.160, median $0.128 | 17 runs from the Live deploy of `77acb9c` to 2026-10-31 ([M-60](../evidence/04-metric-ledger.md#m-60)). Compare with [M-04](../evidence/04-metric-ledger.md#m-04) side by side only: the flow changed |
| — selector, bullet writer and summaries per run | about $0.013, $0.0135 and $0.022 | Same runs, by stage ([M-60](../evidence/04-metric-ledger.md#m-60)) |
| Reading lines that list several asks (Chart My Course) | $0.0244 for 19 Haiku calls | Since its Live deploy ([M-67](../evidence/04-metric-ledger.md#m-67)) |
| Application chat | $0.029 for 20 writer calls; $0.005 for 6 question readings | Since 2026-10-27 ([M-71](../evidence/04-metric-ledger.md#m-71)) |
| One living-résumé answer | mean $0.00066 per model call | 14 answers through links, not my previews ([M-69](../evidence/04-metric-ledger.md#m-69)) |
| Career Chat's read routing | $0.0071 for 336 Jev questions | Since its Live deploy; cache hits write no row ([M-70](../evidence/04-metric-ledger.md#m-70)) |
| Suggesting Growth plans (Beta) | $0.0027 for one call covering 15 items | Session record ([M-81](../evidence/04-metric-ledger.md#m-81)) |

**Earlier figures (different system states).** The first one-button résumé of the extracted application (2026-10-04)
cost $0.25 and took 868 s, of which grounding was 493.5 s. Exhaustive per-piece model review of a
posting cost $0.45 and 267 s. Reading six pieces per requirement once cut that to $0.04 and 46 s
([M-22](../evidence/04-metric-ledger.md#m-22)). Jev and stories then replaced the model reading
entirely. **These figures belong to different system states and are not one trend.**

## Latency

| Path | Time | Note |
|---|---|---|
| Résumé run | median 207 s | The writing phase averages 86.5 s; the two-seat review 66.5 s ([M-05](../evidence/04-metric-ledger.md#m-05)). Before the summary rebuild |
| Résumé run after the speed route | mean 214 s, median 210 s | 17 Live runs ([M-60](../evidence/04-metric-ledger.md#m-60)). I asked for half the time and cost ([DEC-55](07-decision-log.md#dec-55)); M-60 does not show the run time halved; M-05 is a different system state |
| Summaries at low vs medium reasoning | 86 s vs 148 s and 174 s, comparable support per sentence | One Beta comparison on one posting ([M-61](../evidence/04-metric-ledger.md#m-61)) |
| Reading a line that lists several asks | median 9.4 s per call | Haiku, on Live ([M-67](../evidence/04-metric-ledger.md#m-67)) |
| Application-chat writer call | median 9.3 s | On Live ([M-71](../evidence/04-metric-ledger.md#m-71)) |
| Evidence chat call | p50 11.5 s | Haiku; replies stream, but the model thinks before writing |
| Jev question | p50 0.31–1.10 s | Depends on the question; run 32 at a time ([M-59](../evidence/04-metric-ledger.md#m-59)) |
| Opportunity page while background work ran | 4–6 s → separate runner | ~1 s expected; no measured "after" figure ([M-29](../evidence/04-metric-ledger.md#m-29)) |

**Things done for latency:**
- résumé sections are written in parallel;
- Jev questions run 32 at a time;
- background work moved into its own lower-priority process;
- prompt caching on Claude calls;
- low reasoning effort for plain chat questions (about 45% less time across 13 replayed turns);
- the summaries' Jev matching and plain words start beside the bullets, and the summary planner and
  writers run at low reasoning ([A-88](../evidence/03-claim-index.md#a-88), [M-61](../evidence/04-metric-ledger.md#m-61));
- plain words are kept and never asked for again ([A-87](../evidence/03-claim-index.md#a-87));
- only a bullet past two printed lines gets a second call; on one replayed résumé that meant 3 writer
  calls where there had been 6, with the same bullets ([A-91](../evidence/03-claim-index.md#a-91), [M-63](../evidence/04-metric-ledger.md#m-63));
- opportunity pages read only the Jev answers they ask for;
- opportunity labels are counted once and kept, because counting 71 résumés' review views took 86 s
  ([A-79](../evidence/03-claim-index.md#a-79), [M-76](../evidence/04-metric-ledger.md#m-76)).

## Cost controls, and their honest limits

- **Paid surfaces have their own caps.** Each share link has a spend cap, each discovery source a
  monthly cap, and each model check an admin cap, all checked before the call.
- **The global ceiling only binds on declared estimates.** Most stages declare none, so the real
  bounds are the per-surface caps above plus a daily alert ([P-08](../evidence/03-claim-index.md#p-08),
  [D-16](../evidence/05-discrepancies.md#d-16)).
- **Exact limits are deliberately not published**, so they can't be used to maximize someone
  else's cost.

## Known measurement gaps

- **Per-call seconds** are not recorded for the writer, the selector, the reviewers or the summary
  calls. Latency for those stages exists only per phase; the summary steps keep theirs in the run's
  phases ([P-17](../evidence/03-claim-index.md#p-17)). An interview-coach turn stores no time on the turn either ([D-21](../evidence/05-discrepancies.md#d-21)).
- **The run total** is an account-wide ledger difference, so it is inflated by concurrent work
  ([D-21](../evidence/05-discrepancies.md#d-21)).
- **GitHub reads are not recorded.** They are free and need no credential, but they go around the
  governed call boundary ([D-28](../evidence/05-discrepancies.md#d-28)).
- **Career Chat's routing** asks up to 14 Jev questions in turn on a message; what that adds to a
  chat turn's time is not measured ([A-104](../evidence/03-claim-index.md#a-104)).
