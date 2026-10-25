# Product 04 — Model routing, cost and latency

*Product 4.0 · describes Live `7322289` (2026-10-24) · every figure is in the [metric ledger](../evidence/04-metric-ledger.md)*

## How a call gets its model

Every model call goes through one governed boundary ([P-01](../evidence/03-claim-index.md#p-01)):
1. **The stage must be governed.** It needs a promoted policy-document version, or a declared
   exemption with a written reason. There are 22 exemptions, mostly Jev questions, embeddings, search
   and scraping.
2. **The model is chosen in a fixed order:** the caller's explicit model (tests and experiments) →
   the task's entry in the governed `model_assignments` document → the policy's own model → the
   application default (gpt-5-mini) ([P-02](../evidence/03-claim-index.md#p-02)).
3. **Unpriced models are refused** before anything is sent. There are no fallbacks.
4. **Every call writes a row** recording stage, policy version, model, tokens (cached and reasoning
   separately), cost, seconds, outcome and context hash. Failures are written on their own
   transaction, so they survive the caller's rollback. Prompts are not stored, only their hash and
   sizes ([P-03](../evidence/03-claim-index.md#p-03)).

Changing a task's model on **Admin › Models** writes a new version of the assignments document,
recording who changed it and why. The recommended model is starred with the evidence for it.

## Which model does what, and why

| Work | Model | Evidence for the choice |
|---|---|---|
| Résumé selector, writer, reviewers, editor, competencies, next actions | gpt-5-mini | Résumé trial (2026-10-19). Haiku was about half the cost, but reviewers counted fewer relevant accomplishments on 4 of 6 postings and found 2–4 grammar slips. Sonnet was about 3× the cost. The reviewer is held constant so verdicts stay comparable ([M-20](../evidence/04-metric-ledger.md#m-20)) |
| Evidence chat, interview stages, research brief, expectation checks, claim extraction | Claude Haiku 5.5 | Replay of real calls. Chat 8 s vs 13 s at about half the cost; evidence answers 4 s vs 7 s at about a quarter; claim extraction about a tenth of the cost with every claim kept ([M-19](../evidence/04-metric-ledger.md#m-19)) |
| Concept indexing | gpt-5-mini | Haiku tagged 2 of the 21 concepts gpt-5-mini tagged: far too strict |
| Relationship review / demand reading (older flow) | gpt-5-mini | Haiku stricter (55% / 62% agreement). Switching would change match counts everywhere, which is a product decision, not a cost one |
| Ranking, selection, state | Jev | Cheaper and more stable than a model judge. Kept more directly relevant evidence than cosine on 309 logged readings ([M-23](../evidence/04-metric-ledger.md#m-23)) |
| Independent quality evaluator | gpt-5 (fixed) | Used only in measurement |

**Model check** turns this into a repeatable process ([P-07](../evidence/03-claim-index.md#p-07)):
1. Replay real recent prompts through candidate models under a spending cap.
2. Score deterministically against the current model's own noise floor.
3. Recommend the cheapest model within 0.10.
4. Switch nothing until a person presses "Use this".

Two limits: it has not yet been run on Live, and résumé stages cannot be replayed, so résumé model
choice still rests on the one trial.

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

**Earlier figures (different system states).** The first one-button résumé of the extracted application (2026-10-04)
cost $0.25 and took 868 s, of which grounding was 493.5 s. Exhaustive per-piece model review of a
posting cost $0.45 and 267 s. Reading six pieces per requirement once cut that to $0.04 and 46 s
([M-22](../evidence/04-metric-ledger.md#m-22)). Jev and stories then replaced the model reading
entirely. **These figures belong to different system states and are not one trend.**

## Latency

| Path | Time | Note |
|---|---|---|
| Résumé run | median 207 s | The writing phase averages 86.5 s; the two-seat review 66.5 s ([M-05](../evidence/04-metric-ledger.md#m-05)) |
| Evidence chat call | p50 11.5 s | Haiku; replies stream, but the model thinks before writing |
| Jev question | p50 0.31–1.10 s | Depends on the question; run 32 at a time ([M-59](../evidence/04-metric-ledger.md#m-59)) |
| Opportunity page while background work ran | 4–6 s → separate runner | ~1 s expected; no measured "after" figure ([M-29](../evidence/04-metric-ledger.md#m-29)) |

**Things done for latency:**
- résumé sections are written in parallel;
- Jev questions run 32 at a time;
- background work moved into its own lower-priority process;
- prompt caching on Claude calls;
- low reasoning effort for plain chat questions (about 45% less time across 13 replayed turns).

## Cost controls, and their honest limits

- **Paid surfaces have their own caps.** Each share link has a spend cap, each discovery source a
  monthly cap, and each model check an admin cap, all checked before the call.
- **The global ceiling only binds on declared estimates.** Most stages declare none, so the real
  bounds are the per-surface caps above plus a daily alert ([P-08](../evidence/03-claim-index.md#p-08),
  [D-16](../evidence/05-discrepancies.md#d-16)).
- **Exact limits are deliberately not published**, so they can't be used to maximise someone
  else's cost.

## Known measurement gaps

- **Per-call seconds** are not recorded for the writer, the selector or the reviewers. Latency for
  those stages exists only per phase ([P-17](../evidence/03-claim-index.md#p-17)).
- **The run total** is an account-wide ledger difference, so it is inflated by concurrent work
  ([D-21](../evidence/05-discrepancies.md#d-21)).
