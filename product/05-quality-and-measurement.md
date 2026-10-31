# Product 05 — Quality and measurement

*Product 4.1 · describes Live `00eac95` (2026-10-31)*

## What is measured, and against what

| Question | Instrument | Ground truth | Status |
|---|---|---|---|
| Does a résumé show what this job asks for? | Two model reviewer seats (recruiter, hiring manager) read the finished page against the requirements, one row per requirement | The model personas' judgment, **not people** | Verified ([A-15](../evidence/03-claim-index.md#a-15)) |
| Would a reader pass on this candidate before a résumé exists? | Jev "would pass" per seat | Calibrated against those reviewer verdicts (84% vs a 74% baseline for the recruiter seat; 79% vs 58% for the hiring manager; 19 résumés) | Limited ([M-13](../evidence/04-metric-ledger.md#m-13)) |
| Is the page readable in a skim? | Deterministic measures: words per bullet, printed lines, bullets per role, summary length, tools per sentence | Thresholds, reported only | Verified (report) |
| Does the same text repeat? | Jev twin and summary-repeat questions | Thresholds tuned on 897 bullet pairs | Verified (label only) |
| Is each statement supported? | Assertion-level grounding + numeric monotonicity | A 9-case adversarial set (9/9) | **Measurement only; not on Live résumés** ([K-24](../evidence/03-claim-index.md#k-24)) |
| Does each summary sentence rest on its stories? (since 2026-10-28) | Jev reads each professional- and role-summary sentence against the stories it cites; code flags shape and copied wording | Jev's reading at 0.5 | Limited: **reported** on the review page, never gating ([A-84](../evidence/03-claim-index.md#a-84), [K-23](../evidence/03-claim-index.md#k-23)) |
| Does each interview or application answer line rest on its sources? (since 2026-10-25) | Jev reads each draft line against the exact words it cites | Jev's reading at 0.5 | Verified for the application chat ([A-73](../evidence/03-claim-index.md#a-73)); Limited for the coach ([A-64](../evidence/03-claim-index.md#a-64), [D-31](../evidence/05-discrepancies.md#d-31)); shown as footnotes and marks |
| Is a model swap safe? | Model check: replay real prompts, deterministic scores, noise floor | The current model's agreement with itself | Limited; not run on Live yet, and none of the stages governed since 2026-10-25 can be replayed ([P-07](../evidence/03-claim-index.md#p-07)) |
| What does it cost, how long does it take, what failed? | `model_execution` rows; per-phase run records; spend and failure pages; alerts | Measured tokens × listed prices | Verified ([P-03](../evidence/03-claim-index.md#p-03)) |

## Measurement discipline learned the hard way

These rules came from measurements that turned out to be wrong:

1. **A failed judgment is never a verdict.** In August, three runs of one job read 78%, 64% and
   70% because crashed validations were displayed as "missing". Coverage shown as 22 of 22
   re-scored to 10 covered and 12 partial (72% weighted) ([H-06](../evidence/03-claim-index.md#h-06)).
2. **No null model, no measurement.** An optimizer run accepted a "better" résumé policy on a
   difference of one major finding. Four blind readings of an *unchanged* artifact then ranged by
   up to 3 major findings. The acceptance was reversed ([M-26](../evidence/04-metric-ledger.md#m-26)).
3. **A lenient validator is worse than none.** The sentence-level validator called 48/48 statements
   established. Assertion-level grounding found 19/48. The accepted policy had manufactured causal
   claims ([M-25](../evidence/04-metric-ledger.md#m-25)).
4. **Repeatability comes from persistence, not determinism.** Re-judging the same inputs every run
   gave 16, then 2, then 7 established requirements on an unchanged posting. Persisting gated
   findings made an unchanged rerun take about 2 s at $0, with 21/21 identical
   ([M-34](../evidence/04-metric-ledger.md#m-34)). Today identical inputs reuse their first Jev
   reading and their first model verdict.
5. **Never combine measurements from different system states.** A local-model latency and a hosted
   one are not a speed-up. A reservation and a charge are not the same money. This portfolio's
   metric ledger keeps states apart ([Metric ledger](../evidence/04-metric-ledger.md)).
6. **Quote measured cost, never an estimate** ([Product 02 §11](02-principles.md#11-quote-measured-cost-never-an-estimate)).

## Controlled experiments that changed the design

All run on frozen inputs with pre-declared questions (2026-10-03 → 10-07). Details are in the
[metric ledger](../evidence/04-metric-ledger.md).

| Experiment | Result | What changed |
|---|---|---|
| Does the stored indexing score reproduce a top-3 evidence reference? | Exact set 21.3%, item recall 55% ([M-27](../evidence/04-metric-ledger.md#m-27)) | Showed the "relevance" score was requirement-to-taxonomy, not requirement-to-evidence |
| How deep must requirement ↔ evidence cosine go to keep the top 3? | Depth 27; deterministic floor 24 | Cosine became the first-stage retriever with a measured depth |
| Hosted reranker vs Jev on the same population | Reranker's rank correlation was only 0.365 with the dense ordering and 0.359 with the cascade; Jev needed depth 17 ([M-28](../evidence/04-metric-ledger.md#m-28)) | Jev's two frozen questions later became the reader and selector |
| Named-artifact routing | Routed result equaled the fallback on 47/47 pairs | **Not built**; kept as reporting only |
| Run Jev before the costly review? | 16.4% of 122 requirement × role pairs would have lost evidence | **Refuted** as designed |
| Reuse proven bullets across jobs | 0–1 writer calls saved, 13–60 s added | **Removed** |
| Frozen baseline + floor for rebuilds | Regressions 4 → 0; rebuild $0.072/154 s → $0.028/86 s | Adopted for the older writer path |

## Experiments and calibrations since 2026-10-25

These ran on Beta or on recorded Live readings, each on one account. They set a threshold or decided
whether a change shipped. Details and limits are in the ledger.

| Experiment | Result | What changed |
|---|---|---|
| A "polish" step after tightening each bullet | Meaning changed in 6 of 23 bullets at low reasoning and 8 at medium, different ones each time, none flagged ([M-64](../evidence/04-metric-ledger.md#m-64)) | **Closed** the same day: "Close the polish experiment" (my words; [A-97](../evidence/03-claim-index.md#a-97), [DEC-58](07-decision-log.md#dec-58)) |
| Bullets written as the finished line, on one run's fixed inputs | Same 20 bullets, same order, same printed lines; 3 writer calls where there were 6 ([M-63](../evidence/04-metric-ledger.md#m-63)) | **Adopted**, with the rule that writing changes may not cost bullets or change their order ([A-91](../evidence/03-claim-index.md#a-91), [DEC-57](07-decision-log.md#dec-57), [DEC-59](07-decision-log.md#dec-59)) |
| How many characters print on two lines, read off downloaded PDFs | Every bullet up to 228 characters printed on two lines; one of 244 printed on three, which the page estimate counted as two ([M-62](../evidence/04-metric-ledger.md#m-62)) | Only a bullet past 220 characters is shortened ([A-91](../evidence/03-claim-index.md#a-91)) |
| Summaries at low vs medium reasoning | 86 s vs 148 s and 174 s, comparable support per sentence, one posting ([M-61](../evidence/04-metric-ledger.md#m-61)) | **Adopted** for the summary planner and writers ([A-88](../evidence/03-claim-index.md#a-88), [DEC-55](07-decision-log.md#dec-55)) |
| The application chat on a five-question evaluation | Drafted from checked evidence or asked one focused question every time; its prose did not reach my own baseline answers ([M-72](../evidence/04-metric-ledger.md#m-72)) | Shipped as Limited; scored by a code rubric, not by people ([A-74](../evidence/03-claim-index.md#a-74)) |
| What a coaching message means, by Jev | Thresholds set on 106 messages ([M-73](../evidence/04-metric-ledger.md#m-73)) | Phrase lists replaced ([A-66](../evidence/03-claim-index.md#a-66), [DEC-43](07-decision-log.md#dec-43)) |
| A pasted application question vs an answer | Pasted questions read 0.41–0.54, answers and requests at most 0.07 ([M-74](../evidence/04-metric-ledger.md#m-74)) | New-question line lowered to 0.35; thin margin ([A-76](../evidence/03-claim-index.md#a-76), [DEC-65](07-decision-log.md#dec-65)) |
| Career Chat read routing and gap kinds | Lines set on 52 asks plus 11 ordinary messages, and on 187 reviewer gaps ([M-75](../evidence/04-metric-ledger.md#m-75)) | Shipped; Jev is stubbed in every test, so routing accuracy is not tested ([A-104](../evidence/03-claim-index.md#a-104)) |
| Completing an answer's outcome from other pieces of the same work | Borderline readings, about +1 s and +60% tokens on one replayed answer ([M-80](../evidence/04-metric-ledger.md#m-80)) | **Not adopted** ([A-119](../evidence/03-claim-index.md#a-119), [DEC-73](07-decision-log.md#dec-73)) |

Writing-quality measurements for résumés exist only on Beta, by my decision: "Its for testing
resume writing changes only" (my words; [A-98](../evidence/03-claim-index.md#a-98), [DEC-62](07-decision-log.md#dec-62)).

## Calibrating against the system's own readers, and the limit of that

The assessment's thresholds were tuned on my reviewed résumés against the model reviewers' verdicts
([M-13](../evidence/04-metric-ledger.md#m-13)–[M-15](../evidence/04-metric-ledger.md#m-15)):
- A missing requirement at ≥ 0.6 "would pass" predicts the reviewer's call better than always
  saying "forward".
- A lightly shown requirement is never a deal-breaker, because half of them (320 of 602) were
  written strong.
- A barely shown core requirement is called critical 91% of the time.

**This is model-versus-model agreement on one person's data.** It makes the product consistent with
itself, but it does not show what real recruiters do. Observability calls these seats "recruiter"
and "hiring manager", and the code once called them "the real recruiter". They are personas
([D-19](../evidence/05-discrepancies.md#d-19)).

## What is not measured

- **Interview and offer outcomes attributable to the product.** Status history records applications
  and outcomes, but nothing joins outcomes to the résumés or assessments, there is no control group,
  and the sample is one person. **No outcome claim is made in this portfolio.**
- **First-pass writer quality vs editor fixes.** The project rules require this. Today only cost per
  stage is separable ([P-17](../evidence/03-claim-index.md#p-17)).
- **Per-call latency** of the writer, selector, reviewers and summary calls, and the time of an
  interview-coach turn, which is not stored on the turn ([D-21](../evidence/05-discrepancies.md#d-21)).
- **Human-labeled accuracy of the current pipeline.** The earlier build had a 47-pair blind
  human-labeled evaluation set, and its sealed 56-pair holdout has no recorded result. The current
  pipeline has not been evaluated against human labels. The application chat's evaluation is scored
  by code against a rubric, not by people ([A-74](../evidence/03-claim-index.md#a-74)).
- **The quality of interview-coach drafts on Live**, and how often Career Chat routes a message to
  the right read ([A-104](../evidence/03-claim-index.md#a-104)).
- **How often an application-chat offer keeps their words but drops the named "it"**: rejections
  are only logged ([D-21](../evidence/05-discrepancies.md#d-21)).
- **Extension fill rate, connection-message use, MCP use** — no data.

## Feedback loops in operation

1. **Model routing:** model check replay → rule-based recommendation → a person switches →
   a new assignments version. A model named only in the seed file does not reach an existing
   database ([D-27](../evidence/05-discrepancies.md#d-27)).
2. **Assessment calibration:** predicted calls vs reviewer verdicts on the Assessment vs review page →
   thresholds updated by hand in code.
3. **Experiments → selective adoption:** cosine retrieval, Jev questions and the union of nominators
   came from the October experiments.
4. **Use → defects → source fixes:** most changes in October started from something I saw on a Live
   résumé or job. See the [decision log](07-decision-log.md) and [Case study 06](../case-studies/06-operating-the-human-agent-loop.md).
5. **Real outcomes → calibration:** **not connected yet** ([Roadmap](../ROADMAP.md)).
