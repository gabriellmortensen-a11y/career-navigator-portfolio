# Case study 03 — Making evaluation trustworthy, fast and cheap

**One line:** Judging "does this evidence show this requirement?" moved in three steps:
1. from model judges reviewing every candidate, which was slow, costly and unstable;
2. to a few pieces read once;
3. to a probability model answering fixed questions.

I insisted on quoting measured costs, never estimates, and on checking improvements against a noise
floor wherever one could be measured.

**Audience notes.** *Product:* why the cheapest path also agreed better with the reference. *Technical:*
experiment design, noise floors, routing evidence. *TPM:* cost and latency as first-class
requirements, with named measurement gaps.

---

## Customer problem and context

Every useful thing the product does rests on one judgement repeated thousands of times: **does this
piece of the person's evidence establish this requirement?** It drives the assessment, the gap list,
which stories reach a résumé, interview prep and job screening.

In early October 2026 that judgement was a language-model call per candidate:
- One posting took **1,164 judgements, 105 calls, 267 s and $0.45**
  ([M-22](../evidence/04-metric-ledger.md#m-22)).
- The verdicts were unstable. The same input could flip between runs.
- The earlier build had already shown how misleading unstable verdicts are. Three runs of one job
  read 78%, 64% and 70%, because crashed judgements were displayed as "missing"
  ([H-06](../evidence/03-claim-index.md#h-06)).

A person applying to many jobs needs this to be fast, cheap and stable, or the product is unusable.

## My ownership

- **I set the rule** that a model call is for reasoning and writing, never for ranking or deciding
  a state: "A model call should only be used for reasoning situations, not if it meets a rank or if
  it's a state. Jev should be used for that."
- **I set the evidence bar for model changes:** a budget-capped trial on a copy of Live. I then
  approved Haiku for short tasks and rejected Sonnet for résumés on cost
  ([M-19](../evidence/04-metric-ledger.md#m-19), [M-20](../evidence/04-metric-ledger.md#m-20)).
- **I approve every paid experiment in advance**, at any amount, and refuse quoted estimates as
  costs.
- I did not design the experiments' statistics. The agents did, and I accepted or rejected the
  conclusions.

## Constraints

- **Cost per action in cents.** I pay for every call, and I'm the heaviest user.
- **Interactive latency** for chat and pages; minutes, not tens of minutes, for a résumé.
- **No model judge per evidence piece.** Model judges "fill in gaps where evidence should be".
- **Measurements must be reproducible**, or at least their noise must be known.

## Alternatives considered

| Approach | Measured result | Fate |
|---|---|---|
| Exhaustive model review of every candidate | 1,164 judgements, $0.45, 267 s per posting | Replaced |
| Deterministic and lexical validators (earlier build) | 5–7 of 17 correct, about chance; a model validator got 13/17 ([M-33](../evidence/04-metric-ledger.md#m-33)) | Rejected |
| A hosted joint reranker (Voyage) | Rank correlation only 0.365 with the dense ordering and 0.359 with the cascade; depth 22 to keep the reference top 3 ([M-28](../evidence/04-metric-ledger.md#m-28)) | Not promoted |
| Jev, a probability model asked two fixed, pre-registered questions | Depth 17 on the same population; p50 146 ms ([M-28](../evidence/04-metric-ledger.md#m-28)) | Became the reader and selector |
| Named-artifact routing | Routed result equalled the fallback on 47/47 pairs ([M-40](../evidence/04-metric-ledger.md#m-40)) | Not built |
| A Jev filter before the costly review | 16.4% of 122 requirement × role pairs would have lost evidence ([M-37](../evidence/04-metric-ledger.md#m-37)) | Refuted |

The experiments shared one discipline. Each question was fixed in code before any score was seen,
using wording authored for a different, earlier measurement. The declared primary signal could not
be swapped for the better-looking one afterwards. The reference was a model's top 3, not ground
truth, and every write-up says so.

## Decision and reasoning

The judgement was rebuilt in three steps; the first two were measured.

1. **Read less, once** (2026-10-05). Six pieces per requirement, read once, eight calls in parallel:
   **1,164 → 68 judgements, 105 → 15 calls, 267 → 46.1 s, $0.4507 → $0.0385** on the same posting
   ([M-22](../evidence/04-metric-ledger.md#m-22)).
2. **Let Jev decide the clear cases** (2026-10-12). Cosine takes 24 candidates and Jev scores them.
   Clear cases are decided without a model; the model reasons only about the in-between. On 309
   logged readings, Jev's top 4 kept **461 of 531** directly relevant pieces against cosine's
   **413**, and its sure cases agreed with the model reader **93%** of the time
   ([M-23](../evidence/04-metric-ledger.md#m-23)).
3. **Read stories, not fragments** (2026-10-13). Retrieval nominates whole stories three ways and
   Jev reads them sentence by sentence. The per-piece model judge left the Live path entirely
   ([P-19](../evidence/03-claim-index.md#p-19)).

**Stability came from reuse, not hope.** One Jev input read 0.45–0.54 across 11 runs, flipping at
the 0.5 threshold ([M-24](../evidence/04-metric-ledger.md#m-24)). Identical inputs now reuse their
first stored reading. Model verdicts are reused by context hash and editor verdicts by line text.
This echoes the earlier build's lesson: repeatability comes from persistence, not determinism
([M-34](../evidence/04-metric-ledger.md#m-34)).

**Model routing became a governed decision, not a code constant** ([P-02](../evidence/03-claim-index.md#p-02)):

| Task | Model | Basis |
|---|---|---|
| Short tasks: chat, interview stages, research brief, claim extraction | Claude Haiku | Comparable answers on replays, faster and cheaper (chat 8 s vs 13 s, about half the cost) |
| Résumé work | gpt-5-mini | Haiku counted fewer relevant accomplishments on 4 of 6 postings; Sonnet about 3× the cost |
| Reviewer | gpt-5-mini, held constant | "So every résumé's verdict can be compared with every other's" |

Each choice and its reason live in a versioned document. A model check can replay real prompts
through candidates and recommends without switching ([P-07](../evidence/03-claim-index.md#p-07)).

## Implementation

- **One governed boundary** for every call. No fallbacks. Unpriced models refused. Every call
  recorded with tokens (cached and reasoning separately), cost, seconds and outcome
  ([P-01](../evidence/03-claim-index.md#p-01), [P-03](../evidence/03-claim-index.md#p-03)).
- **Jev calls priced** from the tokens it reports. They had been recorded at $0 until 2026-10-14
  ([P-18](../evidence/03-claim-index.md#p-18)).
- **Prompt caching** for Claude calls. Chat sends stable context first. Cost accounting counts cache
  writes and reads ([P-04](../evidence/03-claim-index.md#p-04)).
- **Latency work:**
  - résumé sections in parallel;
  - Jev questions 32 at a time;
  - a separate, lower-priority runner process, after background work pushed pages to 4–6 s
    ([M-29](../evidence/04-metric-ledger.md#m-29));
  - low reasoning effort for plain chat questions, about 45% less time
    ([M-36](../evidence/04-metric-ledger.md#m-36)).

## Verification: guarding against measuring noise

The most important evaluation result in this project was a **reversal**:
1. An unattended optimisation loop accepted a "better" résumé policy on a one-major-finding
   difference.
2. Four blind readings of an *unchanged* artifact ranged by **up to 3 major findings**
   ([M-26](../evidence/04-metric-ledger.md#m-26)).
3. The sentence-level validator had passed **48/48** statements. Assertion-level grounding found
   **19/48** fully established, and the accepted policy had manufactured causal claims
   ([M-25](../evidence/04-metric-ledger.md#m-25)).
4. The acceptance was reversed, and constitutional gates now come before quality comparisons.

## Results

| Measure | Value | Basis |
|---|---|---|
| Language-model cost of a résumé | ≈ $0.11 | 32 Live résumés ([M-03](../evidence/04-metric-ledger.md#m-03)) |
| Résumé wall clock | median 207 s | Same ([M-05](../evidence/04-metric-ledger.md#m-05)) |
| Evidence-chat call | mean $0.0033, p50 11.5 s | 108 Live calls ([M-21](../evidence/04-metric-ledger.md#m-21)) |
| Chart My Course | No language-model calls | Jev + embeddings + code ([A-05](../evidence/03-claim-index.md#a-05)) |

**The cheapest path also agreed better with the reference available.** Jev kept more of the
directly relevant evidence than embedding similarity did, measured against a model reader's
verdicts. Removing per-piece model judges also removed one place a model could supply support the
evidence didn't have. That effect was not measured separately.

## Limitations

- **The references are models.** Experiments compare against a model's top 3 or a model reader's
  verdicts. The assessment is calibrated against model reviewer personas. None of it is validated
  against human recruiters ([D-19](../evidence/05-discrepancies.md#d-19)).
- **Measurement gaps:**
  - per-call seconds are not recorded for the writer, selector and reviewers;
  - the run total is an account-wide ledger difference, inflated by concurrent work ($0.19 recorded
    vs $0.11 attributable) ([D-21](../evidence/05-discrepancies.md#d-21));
  - first-pass writer quality vs editor fixes, which the project rules require, is not yet measured
    ([P-17](../evidence/03-claim-index.md#p-17)).
- **Small samples.** The model-routing evidence rests on single runs and small replays. The trial
  database was dropped, so only its recorded conclusions remain.
- **The shipped combination** (cosine + Jev + stories) has not itself been re-measured against the
  October reference set.

## What changed after learning from use

1. **"Quote measured, never estimated"** became a rule after I was told a chat turn cost $0.02.
   That was the estimate passed to a spend check; it measured about $0.004 ([M-21](../evidence/04-metric-ledger.md#m-21)). The earlier build's
   reservations had run 9.2× actual charges ([M-32](../evidence/04-metric-ledger.md#m-32)).
2. **"No null model, no measurement"** stopped an optimiser from shipping noise.
3. **The cost conversation changed from "which model is cheapest" to "which decisions need a model
   at all".** The biggest savings came from removing model calls from ranking and state decisions,
   not from swapping models.
