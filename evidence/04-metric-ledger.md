# Evidence 04 — Metric ledger

*Every number the portfolio publishes, with its definition, sample, period, source and kind. Read the rules first.*

## Rules

1. **Never combine numbers from different system states.** Each entry names its system (earlier build, current Live, Beta, local). Figures from different states are not a trend, even when they sit side by side.
2. **Kinds are kept apart:** *telemetry* (the product's own records), *controlled experiment* (frozen inputs, pre-declared question), *measured run* (one run, reported in a commit), *replay* (real inputs re-run), *session record* (measured in a working session and recorded in project notes, not in a commit or document), *owner-reported* (my recollection, uncorroborated).
3. **Counts are size, not quality** (commits, tests, lines).
4. **Costs are measured charges** from the call ledger (`model_execution.cost_usd`: tokens × listed price), never reservations or estimates. No invoice is used.
5. **Model personas are not people.** Where a metric uses the app's "recruiter" and "hiring manager" reviewer seats as the reference, it says so.
6. **Live telemetry here is read-only aggregate data from one account (mine)**, queried on 2026-10-25. No record text was read. Usage by any other account is not reported.

## Index

| ID | Group | Metric | Value |
|---|---|---|---|
| [M-01](#m-01) | Evidence quality (historical) | Prompt contamination in evidence canonicalization | 49.47% → 3.62% of proposals |
| [M-02](#m-02) | Evidence quality (historical) | Admission yield of the canonicalization funnel | 19.65% → 45.65% (commit rounds to 20% → 46%) |
| [M-03](#m-03) | Résumé cost | Language-model cost of writing and reviewing one résumé | ≈ $0.11 per résumé ($3.59 / 32): selector + writer ≈ $0.06 ($1.94), two-seat review ≈ $0.03 ($0.97), editor, competencies and next actions ≈ $0.02 |
| [M-04](#m-04) | Résumé cost | Recorded cost per résumé run (run ledger) | mean $0.187, median $0.198 (min $0.083, max $0.284) |
| [M-05](#m-05) | Résumé time | Wall-clock time of a résumé run | median 207 s, mean 215 s; the bullets phase averages 86.5 s and the two-seat review 66.5 s |
| [M-06](#m-06) | Résumé cost | Run-ledger cost before the recruiter-selects flow | mean $0.105, median $0.073 |
| [M-07](#m-07) | Résumé output | Bullets per résumé | mean 17.6 (min 9, max 30) |
| [M-08](#m-08) | Workflow throughput | Applications recorded in a session | 13 jobs within 38.6 min (densest 40-min window); 16 in one evening; 44 jobs moved to Applied between 2026-10-09 and 10-24 |
| [M-09](#m-09) | Workflow throughput | 21 applications in about 40 minutes | Not corroborated |
| [M-10](#m-10) | Discovery | Discover funnel on Live | 18 runs: 4,290 found (incl. repeats across runs), 297 openings stored, 92 assessed against evidence, 54 recommended, 59 saved as opportunities; $1.86 total ($0–0.064 per ordinary run; $1.27 for the run that included the paid career-site index) |
| [M-11](#m-11) | Discovery | Reach before and after widening sources | Before: 578 found → 34 close → 8 read. After (next comparable manual run): 338 found → 60 close → 30 read → 21 recommended, $0.048 |
| [M-12](#m-12) | Discovery | Hosted career-site index pilot | 2 title-led searches: 40 jobs, 0 overlap with existing sources, 37 close, 10 recommended (~$0.05 per relevant job); 25 of 40 on systems the other sources cannot read; responsibility-led searches returned 1 and 0 jobs |
| [M-13](#m-13) | Assessment calibration | Would-a-reader-pass call vs reviewer verdict | Recruiter seat right 84% (always-forward baseline 74%); hiring-manager seat 79% (58%) |
| [M-14](#m-14) | Assessment calibration | Chance a requirement is called a critical weakness | missing 76% (n=75); light but core and < 0.1: 91% (32); light < 0.2: 48% (258); < 0.3: 35% (222); other light: 24% (343); strong: 10% |
| [M-15](#m-15) | Assessment calibration | Lightly shown requirements written strong | 320 of 602 |
| [M-16](#m-16) | Job analysis | Posting lines that are not requirements | 143 of 500 (29%) set aside by Jev; all junk on inspection |
| [M-17](#m-17) | Résumé quality | Summaries over the readability limit | 73% of executive summaries and 96% of role summaries → 0 of 20 each after the shape change |
| [M-18](#m-18) | Résumé quality | Bullets after narrowing the story picker (experiment) | 18–20 → 10–13 bullets, no gain the reviewers found |
| [M-19](#m-19) | Model routing | Haiku 5.5 vs gpt-5-mini on short tasks (replay) | Chat: 8 s vs 13 s at about half the cost (6 chats); evidence answers 4 s vs 7 s at about a quarter (5); claim extraction about a tenth of the cost with every claim kept (6); concept indexing: Haiku tagged 2 of 21 concepts (10 calls); relationship review same verdict on 55% of 105 pieces; demand reading 62% of 37 |
| [M-20](#m-20) | Model routing | Résumé trial | Haiku at high effort ≈ half the cost, but reviewers counted fewer relevant accomplishments on 4 of 6 postings; Haiku's résumés carried 2–4 grammar slips where gpt-5-mini's had none; Sonnet ≈ 3× the cost |
| [M-21](#m-21) | Cost | Evidence-chat turn cost | Mean $0.0033 per call (108 calls, p50 11.5 s); Beta measurement on the caching day: $0.003–0.005 → $0.0017–0.0023 per turn, about 13k of 25k tokens read from cache. An earlier quote of "$0.02 a turn" was the estimate passed to the spend check; measured cost was about $0.004 |
| [M-22](#m-22) | Cost/latency | Evidence reading vs exhaustive review | 1,164 → 68 judgements, 105 → 15 calls, 267 → 46.1 s, $0.4507 → $0.0385 per posting |
| [M-23](#m-23) | Evidence reading | Jev vs cosine at keeping directly relevant evidence | Jev's top 4 kept 461 of 531 direct pieces vs cosine's 413; Jev's sure cases agreed with the model reader 93% |
| [M-24](#m-24) | Evidence reading | Jev stability on a repeated input | 0.45–0.54 across 11 runs (flips at 0.5) |
| [M-25](#m-25) | Grounding | Sentence-level vs assertion-level grounding | Old validator: 48/48 statements established; assertion-level: 19/48 fully established; adversarial set 9/9 correct after two bug fixes |
| [M-26](#m-26) | Evaluation | Evaluator variance on an unchanged artifact | Major findings ranged by up to 3 across four blind readings (7,7,6,5 and 6,8,5,5; declared tolerance ±3); an optimiser acceptance inside that noise was reversed |
| [M-27](#m-27) | Retrieval experiments | Requirement × role top-3 reproduction | Indexing score reproduced the reference exactly in 21.3% (item recall 55.0%); requirement↔evidence cosine needed depth 27 for lossless top-3; deterministic floor 24 (765 slots vs 1,142) |
| [M-28](#m-28) | Retrieval experiments | Hosted reranker vs Jev on the same population | Voyage reranker: depth 22, rank correlation 0.365 with the dense ordering and 0.359 with the cascade, $0.0028, p50 185 ms; Jev: depth 17 (17–22 over tie orders), p50 146 ms, $0.0223 |
| [M-29](#m-29) | Latency | Page load while background work ran | 4–6 s instead of ~1 s per opportunity page |
| [M-30](#m-30) | Engineering size | Test suite | 209 files, 3,167 test functions (static); last recorded full run 3,135 passed / 0 failed / 141 skipped |
| [M-31](#m-31) | Engineering size | Commits and co-authorship | 683 non-merge commits from 2026-10-03 to 10-24, 652 (95.5%) with a Claude co-author trailer; busiest days 73, 62, 56 and 50 non-merge commits; by a rough text search about 112 of 621 distinct messages cite a decision or request of the owner |
| [M-32](#m-32) | Historical cost | Reservations vs charges | $113.66 reserved vs $12.39 charged (9.2×) over 14,377 requests |
| [M-33](#m-33) | Historical quality | Deterministic validators vs a model validator at judging support | 5, 5, 6 and 7 of 17 (chance ≈ 6) vs 13/17 |
| [M-34](#m-34) | Historical repeatability | Persisting gated findings | Re-judging every run gave 16, then 2, then 7 established requirements on an unchanged posting; persisting gated findings raised pair agreement 170 → 197 of 248, and an unchanged rerun took ~2 s at $0 with 21/21 identical |
| [M-35](#m-35) | Résumé cost/latency (earlier flow) | First one-button résumé of the extracted application | 868 s, $0.2541, 31 calls; grounding alone 493.5 s (two thirds of the generation) |
| [M-36](#m-36) | Latency | Chat effort for plain questions | About 45% less time at low reasoning effort, with answers judged as good on questions (wrong once on a hard correction, which keeps medium effort) |
| [M-37](#m-37) | Experiments | Jev filter before the costly relationship review | 16.4% of 122 requirement × role pairs would have lost evidence; projected saving ~$1.03 per $1.11 review |
| [M-38](#m-38) | Experiments | Frozen baseline + coverage floor for rebuilds | Regressions 4 → 0; rebuild $0.072 / 154 s → $0.028 / 86 s |
| [M-39](#m-39) | Experiments | Reusing proven bullets across jobs | 0–1 writer calls saved, 13–60 s added |
| [M-40](#m-40) | Experiments | Named-artifact certainty routing | Routed result equalled the fallback on 47 of 47 pairs; precision 2/2, recall 2/3 |
| [M-41](#m-41) | Résumé quality | Repeat-detection thresholds | Shared facts: 22 within-role sentence pairs at cosine ≥ 0.70, repeats read 0.86–0.94 and different work ≤ 0.84 (threshold 0.85); twin bullets: repeats 0.75–0.81, different ≤ 0.66 (threshold 0.75) |
| [M-42](#m-42) | Historical evaluation | Human-labelled evaluation set (earlier build) | Eval Set v1: 47 blind human-judged pairs, baseline 37/47 (78.7%) → 38/47 (80.9%); a sealed 56-pair holdout has no recorded result |
| [M-43](#m-43) | Résumé quality (older flow) | Bullets with phrases copied from the requirement | 2 of 220 on Live; 52 of 265 on Beta |
| [M-44](#m-44) | Cost | Shared-link question cost | About $0.0047 per question |
| [M-45](#m-45) | Gap conversations | Gap themes | 13 related compliance requirements → 1 theme; 11 growth requirements → 3; 10 requirements on a third posting → 4 |
| [M-46](#m-46) | Gap conversations | One job's gap record reconciled | 16 gaps: 12 reviewed (7 with new evidence, 5 with no more to add), 1 in progress, 3 still to explore |
| [M-47](#m-47) | Gap conversations | Paid test of a full gap conversation | $0.020 for a full run that found four defects (fields not nested, draft holding only the last turn's facts, question appended twice, facts restated on reopen) |
| [M-48](#m-48) | Engineering size (historical) | Legacy release suite at the end of the earlier build | 9,453 passed / 27 failed, each failure classified |
| [M-49](#m-49) | Engineering size | Test suite at extraction vs the earlier build | 117 contracts in 3.16 s vs 10,541 in the earlier build |
| [M-50](#m-50) | Engineering size (historical) | Agent-instruction file size in the earlier build | 130 → 1,030 lines across 55 commits |
| [M-51](#m-51) | Assessment cost | Cost of preparing and assessing a job (Chart My Course) | mean $0.0198, median $0.0148, mean 53.7 s per preparation run |
| [M-52](#m-52) | Evidence model | Evidence count after story composition | 176 "evidence pieces" → 86 examples on one account |
| [M-53](#m-53) | Evidence model | Splitting already-glued stories (experiment) | 20 strong requirements became light and 3 became stronger, over 63 jobs |
| [M-54](#m-54) | Evidence model | Role agreement before the bullet constraint | 0 disagreements across 12,440 candidates, 46 selections and 34 bullets |
| [M-55](#m-55) | Operations | Data-loss incident | 17,183 rows across 50 tables deleted; suite went from 1,298 passed / 1 failed to 1,182 passed / 84 failed / 19 errors; 215 of 221 retired events would have been re-indexed by the re-import |
| [M-56](#m-56) | Résumé quality | Bullets matched to stories by position | 17 bullets written from 15 stories; every bullet after the first split was stored against the wrong story |
| [M-57](#m-57) | Résumé quality | Strong evidence written weakly | About 1 in 6 requirements assessed strong came out partial or absent on the reviewed résumé |
| [M-58](#m-58) | Gap conversations | Gap list vs reviewer verdicts (before the gap redefinition) | One job showed 15 gaps while both model reviewers would advance the candidate |
| [M-59](#m-59) | Latency | Jev question latency | p50 0.31–1.10 s depending on the question (e.g. 0.31 s repeat labels, 0.34 s interview evidence, 1.10 s story reading); Jev runs up to 32 questions at a time |

## Entries

<a id="m-01"></a>
### M-01 — Prompt contamination in evidence canonicalization

| Field | |
|---|---|
| Value | 49.47% → 3.62% of proposals |
| Definition / denominator | Proposals whose citation was traceable to the Career Story summary the prompt itself supplied ÷ all proposals (141/285 → 5/138) |
| Sample | 8 real projections, one run per arm, paired before/after |
| Period | 2026-08-13 |
| Source | beta4 commit `4e8e3e0` (QC-1) body; Observatory fixture `tests/fixtures/qc1.py` at `dd881b7` (re-summed 2026-10-25) |
| Kind | Controlled before/after run, reproduced by a second instrument |
| System state | Earlier build (beta4), Beta data read-only, local models |
| Limits | One run per arm; counts differ ~20% between runs while rates differ 0.1–0.3 pp, so rates are the robust figure. Historical system. |

<a id="m-02"></a>
### M-02 — Admission yield of the canonicalization funnel

| Field | |
|---|---|
| Value | 19.65% → 45.65% (commit rounds to 20% → 46%) |
| Definition / denominator | Admitted ÷ proposals (56/285 → 63/138). "Admission" here is the canonicalization funnel, not résumé admission |
| Sample | Same 8 projections |
| Period | 2026-08-13 |
| Source | Same as M-01 |
| Kind | Controlled before/after run |
| System state | Earlier build |
| Limits | Same as M-01. Never conflate with résumé admission. |

<a id="m-03"></a>
### M-03 — Language-model cost of writing and reviewing one résumé

| Field | |
|---|---|
| Value | ≈ $0.11 per résumé ($3.59 / 32): selector + writer ≈ $0.06 ($1.94), two-seat review ≈ $0.03 ($0.97), editor, competencies and next actions ≈ $0.02 |
| Definition / denominator | Sum of `model_execution.cost_usd` for the owner's account over the stages resume_flow_writer, resume_recruiter_select, resume_coverage_review, resume_editor_review, resume_competencies, whats_next_actions ÷ complete résumé runs in the window |
| Sample | 32 complete runs (one account) |
| Period | 2026-10-21 00:00 → 2026-10-25 00:00 UTC |
| Source | Live `model_execution` + `resume_generation_run`, read-only aggregate query 2026-10-25 |
| Kind | Telemetry |
| System state | Live `7322289`-era code (recruiter-selects flow) |
| Limits | Excludes Jev reading shared with assessment (stories_establishes $1.02 for the account in the window), embeddings and posting preparation; coverage-review cost includes re-reviews after person edits. Single user. |

<a id="m-04"></a>
### M-04 — Recorded cost per résumé run (run ledger)

| Field | |
|---|---|
| Value | mean $0.187, median $0.198 (min $0.083, max $0.284) |
| Definition / denominator | `resume_generation_run.cost_usd`: account-wide before/after difference of the call ledger across the run |
| Sample | 32 complete runs |
| Period | 2026-10-21 → 10-24 |
| Source | Live `resume_generation_run`, read-only |
| Kind | Telemetry |
| System state | Live |
| Limits | Upper bound: concurrent work on the same account (other builds, chat, discovery) is included (D-21). Do not quote as the cost of a résumé. |

<a id="m-05"></a>
### M-05 — Wall-clock time of a résumé run

| Field | |
|---|---|
| Value | median 207 s, mean 215 s; the bullets phase averages 86.5 s and the two-seat review 66.5 s |
| Definition / denominator | Sum of phase seconds per complete run |
| Sample | 32 complete runs |
| Period | 2026-10-21 → 10-24 |
| Source | Live `resume_generation_run.phases` |
| Kind | Telemetry |
| System state | Live |
| Limits | Includes queueing inside phases; per-call seconds are not recorded for writer/selector/reviewer calls (D-21). |

<a id="m-06"></a>
### M-06 — Run-ledger cost before the recruiter-selects flow

| Field | |
|---|---|
| Value | mean $0.105, median $0.073 |
| Definition / denominator | As M-04 |
| Sample | 25 complete runs |
| Period | 2026-10-06 → 10-13 |
| Source | Live `resume_generation_run` |
| Kind | Telemetry |
| System state | Earlier flows of the current app |
| Limits | Different system state from M-03/M-04 — not comparable as a trend. |

<a id="m-07"></a>
### M-07 — Bullets per résumé

| Field | |
|---|---|
| Value | mean 17.6 (min 9, max 30) |
| Definition / denominator | Bullets written by the recruiter-selects flow per complete run |
| Sample | 32 complete runs |
| Period | 2026-10-21 → 10-24 |
| Source | Live `resume_generation_run.phases` (bullets phase) |
| Kind | Telemetry |
| System state | Live |
| Limits | One person's career; number of roles varies. |

<a id="m-08"></a>
### M-08 — Applications recorded in a session

| Field | |
|---|---|
| Value | 13 jobs within 38.6 min (densest 40-min window); 16 in one evening; 44 jobs moved to Applied between 2026-10-09 and 10-24 |
| Definition / denominator | Distinct jobs moved to status Applied (undo events excluded), by the time the person recorded the status |
| Sample | 45 status events, one account |
| Period | 2026-10-09 → 10-24 |
| Source | Live `job_status_event`, read-only |
| Kind | Telemetry |
| System state | Live |
| Limits | Status time is when the person marked it, not when the employer received it. Throughput only — says nothing about interviews or offers. Status history before 2026-10-08 is undated. |

<a id="m-09"></a>
### M-09 — 21 applications in about 40 minutes

| Field | |
|---|---|
| Value | Not corroborated |
| Definition / denominator | Owner-reported session |
| Sample | — |
| Period | 2026-10 (owner recollection) |
| Source | Owner report |
| Kind | Owner-reported |
| System state | Live |
| Limits | Status telemetry shows at most 13 in any 40-minute window and 16 in one evening (M-08). Applications may have been submitted before being recorded; the claim is kept only as owner-reported. |

<a id="m-10"></a>
### M-10 — Discover funnel on Live

| Field | |
|---|---|
| Value | 18 runs: 4,290 found (incl. repeats across runs), 297 openings stored, 92 assessed against evidence, 54 recommended, 59 saved as opportunities; $1.86 total ($0–0.064 per ordinary run; $1.27 for the run that included the paid career-site index) |
| Definition / denominator | Run summaries: found → close (embedding ≥ 0.5, capped at 60) → assessed (Jev on requirement lines) → recommended (rules) |
| Sample | 18 runs, one account, 2 search profiles |
| Period | 2026-10-20 → 2026-10-25 |
| Source | Live `discovery_run`, `discovery_opening`, read-only |
| Kind | Telemetry |
| System state | Live |
| Limits | Close saturates at the 60 cap. Recommendation is not a hiring outcome. |

<a id="m-11"></a>
### M-11 — Reach before and after widening sources

| Field | |
|---|---|
| Value | Before: 578 found → 34 close → 8 read. After (next comparable manual run): 338 found → 60 close → 30 read → 21 recommended, $0.048 |
| Definition / denominator | As M-10 |
| Sample | One run each |
| Period | 2026-10-20 |
| Source | Commit `e801ffa` (before); Live `discovery_run` 6 and 7 (both verified in telemetry) |
| Kind | Telemetry, uncontrolled before/after |
| System state | Live |
| Limits | Not a controlled comparison: the same change raised the read cap from 8 to 30 per run, "close" is capped at 60, and "found" fell; different queries and days. Shows the funnel's shape, not the effect of new sources. |

<a id="m-12"></a>
### M-12 — Hosted career-site index pilot

| Field | |
|---|---|
| Value | 2 title-led searches: 40 jobs, 0 overlap with existing sources, 37 close, 10 recommended (~$0.05 per relevant job); 25 of 40 on systems the other sources cannot read; responsibility-led searches returned 1 and 0 jobs |
| Definition / denominator | Pilot on a copy of the owner's account |
| Sample | 6 searches, 69 jobs, $0.888 billed of $1 approved |
| Period | 2026-10-21 |
| Source | Session record; "10 recommended in 40" and the responsibility-led result are also recorded in `app/discovery/indexed.py` comments |
| Kind | Session record (partly corroborated in code) |
| System state | Beta |
| Limits | Small pilot; one person's targets; supported the admin-only, title-led design. |

<a id="m-13"></a>
### M-13 — Would-a-reader-pass call vs reviewer verdict

| Field | |
|---|---|
| Value | Recruiter seat right 84% (always-forward baseline 74%); hiring-manager seat 79% (58%) |
| Definition / denominator | Jev "would pass" with missing at ≥ 0.6 vs the coverage reviewers' advance yes/no on the same job |
| Sample | 19 reviewed résumés, one account |
| Period | 2026-10-23 |
| Source | Commit `766061f`; `app/pipeline/assessment.py` constants |
| Kind | Offline replay on Live data |
| System state | Live data |
| Limits | The "reviewers" are the app's model personas, not people; not joined to hiring outcomes; one account. |

<a id="m-14"></a>
### M-14 — Chance a requirement is called a critical weakness

| Field | |
|---|---|
| Value | missing 76% (n=75); light but core and < 0.1: 91% (32); light < 0.2: 48% (258); < 0.3: 35% (222); other light: 24% (343); strong: 10% |
| Definition / denominator | Reviewer coverage partial/absent and marked critical, by assessment fit |
| Sample | 55 reviewed résumés, one account |
| Period | 2026-10-23/24 |
| Source | `app/pipeline/assessment.py` (`NOTICED`); commit `53798d6` |
| Kind | Offline replay on Live data |
| System state | Live data |
| Limits | Same as M-13. |

<a id="m-15"></a>
### M-15 — Lightly shown requirements written strong

| Field | |
|---|---|
| Value | 320 of 602 |
| Definition / denominator | Light at assessment vs strong in the reviewers' reading of the written résumé |
| Sample | 19 résumés |
| Period | 2026-10-22/23 |
| Source | Commit `766061f` |
| Kind | Offline replay |
| System state | Live data |
| Limits | Same as M-13; this is why "light" is never a deal-breaker. |

<a id="m-16"></a>
### M-16 — Posting lines that are not requirements

| Field | |
|---|---|
| Value | 143 of 500 (29%) set aside by Jev; all junk on inspection |
| Definition / denominator | Jev "is this a requirement?" < 0.5 |
| Sample | 500 lines from 16 postings |
| Period | 2026-10-12 |
| Source | `app/pipeline/requirement_filter.py`; commit `4452c6d` |
| Kind | Inspection |
| System state | Live data |
| Limits | One inspector; no recall estimate. |

<a id="m-17"></a>
### M-17 — Summaries over the readability limit

| Field | |
|---|---|
| Value | 73% of executive summaries and 96% of role summaries → 0 of 20 each after the shape change |
| Definition / denominator | Summaries over the readability threshold. Before: ten Live days asking for one text "of at most N words". After: replay asking for at most 3 sentences of at most 15 words (2 for a role summary), requested in the prompt |
| Sample | Live 10 days; 20 + 20 replay |
| Period | 2026-10-22 |
| Source | Commit `2d3482b`; `app/resume/recruiter_flow.py` |
| Kind | Before/after replay |
| System state | Live data |
| Limits | Shape still prompt-enforced. |

<a id="m-18"></a>
### M-18 — Bullets after narrowing the story picker (experiment)

| Field | |
|---|---|
| Value | 18–20 → 10–13 bullets, no gain the reviewers found |
| Definition / denominator | Bullet count on three Beta résumés |
| Sample | 3 résumés |
| Period | 2026-10-23 |
| Source | Beta commits `4e4f206` → `4c2f06d` |
| Kind | Small A/B |
| System state | Beta |
| Limits | Reverted; never on Live. |

<a id="m-19"></a>
### M-19 — Haiku 5.5 vs gpt-5-mini on short tasks (replay)

| Field | |
|---|---|
| Value | Chat: 8 s vs 13 s at about half the cost (6 chats); evidence answers 4 s vs 7 s at about a quarter (5); claim extraction about a tenth of the cost with every claim kept (6); concept indexing: Haiku tagged 2 of 21 concepts (10 calls); relationship review same verdict on 55% of 105 pieces; demand reading 62% of 37 |
| Definition / denominator | Replay of real recent calls; agreement with gpt-5-mini, which is not ground truth |
| Sample | 50 real calls |
| Period | 2026-10-19 |
| Source | `app/documents/seeds/model_assignments_v1.md` (`why` lines) |
| Kind | Replay experiment |
| System state | Copy of Live |
| Limits | Very small samples; recorded as the evidence behind each assignment. |

<a id="m-20"></a>
### M-20 — Résumé trial

| Field | |
|---|---|
| Value | Haiku at high effort ≈ half the cost, but reviewers counted fewer relevant accomplishments on 4 of 6 postings; Haiku's résumés carried 2–4 grammar slips where gpt-5-mini's had none; Sonnet ≈ 3× the cost |
| Definition / denominator | Same reviewer for all |
| Sample | 6 postings |
| Period | 2026-10-19 |
| Source | `app/documents/seeds/model_assignments_v1.md`; trial branch `anthropic-trial` |
| Kind | Experiment (single runs) |
| System state | Copy of Live (dropped after) |
| Limits | Single runs are noisy; the trial database was dropped, so only the recorded conclusions remain. |

<a id="m-21"></a>
### M-21 — Evidence-chat turn cost

| Field | |
|---|---|
| Value | Mean $0.0033 per call (108 calls, p50 11.5 s); Beta measurement on the caching day: $0.003–0.005 → $0.0017–0.0023 per turn, about 13k of 25k tokens read from cache. An earlier quote of "$0.02 a turn" was the estimate passed to the spend check; measured cost was about $0.004 |
| Definition / denominator | `model_execution.cost_usd` for stage evidence_chat (Haiku) |
| Sample | 108 Live calls; Beta probe |
| Period | 2026-10-21 → 10-24 (Live; the window opens on the day caching shipped); 2026-10-21 (Beta) |
| Source | Live telemetry; session record for the Beta probe; commits `95c0297`, `f9332c7` |
| Kind | Telemetry + session record |
| System state | Live / Beta |
| Limits | Live mean includes long gap-discovery turns; the $0.02 figure seen in code is an estimate passed to the ceiling check, never a cost. |

<a id="m-22"></a>
### M-22 — Evidence reading vs exhaustive review

| Field | |
|---|---|
| Value | 1,164 → 68 judgements, 105 → 15 calls, 267 → 46.1 s, $0.4507 → $0.0385 per posting |
| Definition / denominator | Old: every candidate judged by a model; new: six pieces per demand, read once, eight calls in parallel |
| Sample | 1 posting |
| Period | 2026-10-05 |
| Source | Commits `8bedc4c`, `2068a41` |
| Kind | Measured run |
| System state | Local / then Live |
| Limits | One posting; later replaced by Jev ranking and stories. |

<a id="m-23"></a>
### M-23 — Jev vs cosine at keeping directly relevant evidence

| Field | |
|---|---|
| Value | Jev's top 4 kept 461 of 531 direct pieces vs cosine's 413; Jev's sure cases agreed with the model reader 93% |
| Definition / denominator | Direct pieces per the model reader's verdicts |
| Sample | 309 Live readings |
| Period | 2026-10-12 |
| Source | Commit `d897201` |
| Kind | Offline comparison |
| System state | Live data |
| Limits | Reference is a model's verdicts, not human labels. |

<a id="m-24"></a>
### M-24 — Jev stability on a repeated input

| Field | |
|---|---|
| Value | 0.45–0.54 across 11 runs (flips at 0.5) |
| Definition / denominator | Repeated identical question |
| Sample | 1 input × 11 |
| Period | 2026-10-21 |
| Source | Commit `346d751` |
| Kind | Probe |
| System state | Beta |
| Limits | Led to reusing the first stored reading for identical inputs. |

<a id="m-25"></a>
### M-25 — Sentence-level vs assertion-level grounding

| Field | |
|---|---|
| Value | Old validator: 48/48 statements established; assertion-level: 19/48 fully established; adversarial set 9/9 correct after two bug fixes |
| Definition / denominator | Statements in 5 artifacts; frozen adversarial cases |
| Sample | 48 statements; 9 cases |
| Period | 2026-10-03 |
| Source | `docs/measurement-calibration.md`; commit `335e8d4` |
| Kind | Measured experiment |
| System state | Local |
| Limits | Tiny n; one job. |

<a id="m-26"></a>
### M-26 — Evaluator variance on an unchanged artifact

| Field | |
|---|---|
| Value | Major findings ranged by up to 3 across four blind readings (7,7,6,5 and 6,8,5,5; declared tolerance ±3); an optimiser acceptance inside that noise was reversed |
| Definition / denominator | 4 blind readings × 2 artifacts |
| Sample | 8 readings |
| Period | 2026-10-03 |
| Source | Commit `335e8d4`; `docs/measurement-calibration.md` |
| Kind | Repeated measurement |
| System state | Local |
| Limits | n = 4 per artifact. |

<a id="m-27"></a>
### M-27 — Requirement × role top-3 reproduction

| Field | |
|---|---|
| Value | Indexing score reproduced the reference exactly in 21.3% (item recall 55.0%); requirement↔evidence cosine needed depth 27 for lossless top-3; deterministic floor 24 (765 slots vs 1,142) |
| Definition / denominator | 47 contested pairs; a gpt-5-mini top-3 reference (not ground truth) |
| Sample | 1 frozen posting |
| Period | 2026-10-03 |
| Source | `docs/vector-ranking-check.md`, `docs/direct-evidence-similarity.md`, `docs/p99-candidate-reduction.md` |
| Kind | Controlled offline experiments |
| System state | Local |
| Limits | One posting; reference is a model's ranking. |

<a id="m-28"></a>
### M-28 — Hosted reranker vs Jev on the same population

| Field | |
|---|---|
| Value | Voyage reranker: depth 22, rank correlation 0.365 with the dense ordering and 0.359 with the cascade, $0.0028, p50 185 ms; Jev: depth 17 (17–22 over tie orders), p50 146 ms, $0.0223 |
| Definition / denominator | Depth needed to keep all three reference pieces |
| Sample | 47 pairs |
| Period | 2026-10-03 |
| Source | `docs/hosted-reranker-experiment.md`, `docs/jev-reranker-experiment.md` |
| Kind | Controlled offline experiments |
| System state | Local |
| Limits | Experiment questions pre-registered in code; nothing promoted from these documents directly. |

<a id="m-29"></a>
### M-29 — Page load while background work ran

| Field | |
|---|---|
| Value | 4–6 s instead of ~1 s per opportunity page |
| Definition / denominator | Observed on Live while Chart My Course ran in the web process |
| Sample | Observation |
| Period | 2026-10-19 |
| Source | Commit `4c984f8` |
| Kind | Observation |
| System state | Live |
| Limits | No "after" figure recorded. |

<a id="m-30"></a>
### M-30 — Test suite

| Field | |
|---|---|
| Value | 209 files, 3,167 test functions (static); last recorded full run 3,135 passed / 0 failed / 141 skipped |
| Definition / denominator | Static count at `7322289`; run result from the unification session |
| Sample | — |
| Period | 2026-10-21 (run); 2026-10-25 (count) |
| Source | `tests/`; session record |
| Kind | Count + session record |
| System state | Local suite |
| Limits | Functions ≠ collected cases. Most of the 141 skips audit historical data lost on 2026-10-05; the rest need private files or tools not present in the checkout. |

<a id="m-31"></a>
### M-31 — Commits and co-authorship

| Field | |
|---|---|
| Value | 683 non-merge commits from 2026-10-03 to 10-24, 652 (95.5%) with a Claude co-author trailer; busiest days 73, 62, 56 and 50 non-merge commits; by a rough text search about 112 of 621 distinct messages cite a decision or request of the owner |
| Definition / denominator | `git log 7322289` |
| Sample | — |
| Period | 2026-10-03 → 10-24 |
| Source | Git |
| Kind | Count |
| System state | Repository |
| Limits | Size, not quality; trailers record co-authorship, not the split of work. |

<a id="m-32"></a>
### M-32 — Reservations vs charges

| Field | |
|---|---|
| Value | $113.66 reserved vs $12.39 charged (9.2×) over 14,377 requests |
| Definition / denominator | Worst-case hold before sending vs reconciled charge |
| Sample | 14,377 requests |
| Period | ≈ 2026-09-10 |
| Source | beta4 `inference_budget.py:240-252`; ledger SYS-053 |
| Kind | Telemetry (historical) |
| System state | Earlier build |
| Limits | Not a bill. |

<a id="m-33"></a>
### M-33 — Deterministic validators vs a model validator at judging support

| Field | |
|---|---|
| Value | 5, 5, 6 and 7 of 17 (chance ≈ 6) vs 13/17 |
| Definition / denominator | Agreement with frozen labels |
| Sample | 17 cases |
| Period | 2026-08-11 |
| Source | beta4 commit `6a88ea8`; ledger EAR-060 |
| Kind | Measured experiment |
| System state | Earlier build, local models |
| Limits | Small n. |

<a id="m-34"></a>
### M-34 — Persisting gated findings

| Field | |
|---|---|
| Value | Re-judging every run gave 16, then 2, then 7 established requirements on an unchanged posting; persisting gated findings raised pair agreement 170 → 197 of 248, and an unchanged rerun took ~2 s at $0 with 21/21 identical |
| Definition / denominator | Agreement across runs |
| Sample | 248 pairs |
| Period | 2026-09-17 |
| Source | beta4 commit `3dd55f1`; ledger SYS-018, LAT-055 (sanitized) |
| Kind | Measured runs |
| System state | Earlier build, Live and Beta |
| Limits | Mixed states; quoted as recorded. |

<a id="m-35"></a>
### M-35 — First one-button résumé of the extracted application

| Field | |
|---|---|
| Value | 868 s, $0.2541, 31 calls; grounding alone 493.5 s (two thirds of the generation) |
| Definition / denominator | One run of the then-current pipeline (warm cache) |
| Sample | 1 posting |
| Period | 2026-10-04 |
| Source | Commit `2cd7811`; `app/resume/drafting.py` comment |
| Kind | Measured run |
| System state | Local / earlier flow |
| Limits | Different system state from M-03/M-05; not a trend. |

<a id="m-36"></a>
### M-36 — Chat effort for plain questions

| Field | |
|---|---|
| Value | About 45% less time at low reasoning effort, with answers judged as good on questions (wrong once on a hard correction, which keeps medium effort) |
| Definition / denominator | Replay of real chat turns at low vs medium effort |
| Sample | 13 turns |
| Period | 2026-10-23 |
| Source | Commit `5a8456a` |
| Kind | Replay |
| System state | Live turns replayed |
| Limits | Small sample. |

<a id="m-37"></a>
### M-37 — Jev filter before the costly relationship review

| Field | |
|---|---|
| Value | 16.4% of 122 requirement × role pairs would have lost evidence; projected saving ~$1.03 per $1.11 review |
| Definition / denominator | Requirement × role pairs whose only supporting evidence the filter would have removed |
| Sample | 122 requirement × role pairs |
| Period | 2026-10-04 |
| Source | `docs/review-filter-economics.md`; commit `c8943e1` |
| Kind | Controlled offline experiment |
| System state | Local |
| Limits | Refuted as designed; the review it costed was later replaced outright. |

<a id="m-38"></a>
### M-38 — Frozen baseline + coverage floor for rebuilds

| Field | |
|---|---|
| Value | Regressions 4 → 0; rebuild $0.072 / 154 s → $0.028 / 86 s |
| Definition / denominator | Requirements whose coverage fell on a rebuild |
| Sample | 1 posting, 4 rebuilds |
| Period | 2026-10-07 |
| Source | `docs/unified-resume-review.md`; commits `69bcaae` → `6b6eb1a` |
| Kind | Controlled experiment |
| System state | Beta persona |
| Limits | Adopted for the older writer path, which Live no longer runs. |

<a id="m-39"></a>
### M-39 — Reusing proven bullets across jobs

| Field | |
|---|---|
| Value | 0–1 writer calls saved, 13–60 s added |
| Definition / denominator | Calls and wall clock with vs without reuse |
| Sample | Small set of rebuilds |
| Period | 2026-10-07 |
| Source | `docs/projection-reuse-experiment.md`; commits `60062a9` → `9391b5f` |
| Kind | Controlled experiment |
| System state | Local |
| Limits | Feature removed and its table dropped. |

<a id="m-40"></a>
### M-40 — Named-artifact certainty routing

| Field | |
|---|---|
| Value | Routed result equalled the fallback on 47 of 47 pairs; precision 2/2, recall 2/3 |
| Definition / denominator | Pairs where routing changed the outcome |
| Sample | 47 pairs |
| Period | 2026-10-03 |
| Source | `docs/deterministic-certainty-routing.md`; commit `2561e63` |
| Kind | Controlled offline experiment |
| System state | Local |
| Limits | Not built; kept as reporting (named tools and credentials coverage). |

<a id="m-41"></a>
### M-41 — Repeat-detection thresholds

| Field | |
|---|---|
| Value | Shared facts: 22 within-role sentence pairs at cosine ≥ 0.70, repeats read 0.86–0.94 and different work ≤ 0.84 (threshold 0.85); twin bullets: repeats 0.75–0.81, different ≤ 0.66 (threshold 0.75) |
| Definition / denominator | Jev same-accomplishment / "would a recruiter think the second repeats the first?" |
| Sample | 83 stories, 363 sentences; 897 bullet pairs from the last 10 résumés |
| Period | 2026-10-24 |
| Source | `app/resume/overlap.py`, `app/resume/summary_cover.py`; commit `7322289` |
| Kind | Threshold calibration on Live data |
| System state | Live data |
| Limits | One record; post-deploy effect not yet measured. |

<a id="m-42"></a>
### M-42 — Human-labelled evaluation set (earlier build)

| Field | |
|---|---|
| Value | Eval Set v1: 47 blind human-judged pairs, baseline 37/47 (78.7%) → 38/47 (80.9%); a sealed 56-pair holdout has no recorded result |
| Definition / denominator | Agreement of the obligation gate with human labels |
| Sample | 47 pairs |
| Period | 2026-09-25 |
| Source | beta4 commits `10a7501`, `8f9baa0`; ledger SYS-007, SYS-008, LAT-080 |
| Kind | Human-labelled experiment |
| System state | Earlier build |
| Limits | One-pair difference; v1 later judged to measure the wrong thing; no equivalent for the current pipeline. |

<a id="m-43"></a>
### M-43 — Bullets with phrases copied from the requirement

| Field | |
|---|---|
| Value | 2 of 220 on Live; 52 of 265 on Beta |
| Definition / denominator | Runs of ≥ 2 words copied from the requirement the bullet answered |
| Sample | 485 bullets |
| Period | 2026-10-12 |
| Source | `app/resume/borrowed.py` comment; commit `9dd2354` |
| Kind | Count |
| System state | Live and Beta (older writer, which saw requirement text) |
| Limits | Beta hits concentrated in one test account; the check became unnecessary once the writer stopped seeing requirements. |

<a id="m-44"></a>
### M-44 — Shared-link question cost

| Field | |
|---|---|
| Value | About $0.0047 per question |
| Definition / denominator | `model_execution` cost of one answer |
| Sample | Development runs |
| Period | 2026-10-05 |
| Source | Commit `a072e68` |
| Kind | Measured |
| System state | Earlier version of the share link |
| Limits | Small sample; the conversation link (2026-10-22) uses a similar single call. |

<a id="m-45"></a>
### M-45 — Gap themes

| Field | |
|---|---|
| Value | 13 related compliance requirements → 1 theme; 11 growth requirements → 3; 10 requirements on a third posting → 4 |
| Definition / denominator | Average-link grouping at Jev ≥ 0.5 over cosine-near pairs |
| Sample | 8 jobs, one account |
| Period | 2026-10-24 |
| Source | `app/evidence/themes.py` comment; commit `ea06f2f` |
| Kind | Measured |
| System state | Live data |
| Limits | Few jobs; tests stub Jev. |

<a id="m-46"></a>
### M-46 — One job's gap record reconciled

| Field | |
|---|---|
| Value | 16 gaps: 12 reviewed (7 with new evidence, 5 with no more to add), 1 in progress, 3 still to explore |
| Definition / denominator | Discovery ledger read from the turns |
| Sample | 1 job |
| Period | 2026-10-22 |
| Source | Session record (Live reconciliation) |
| Kind | Session record |
| System state | Live |
| Limits | One job; illustrative, not a rate. |

<a id="m-47"></a>
### M-47 — Paid test of a full gap conversation

| Field | |
|---|---|
| Value | $0.020 for a full run that found four defects (fields not nested, draft holding only the last turn's facts, question appended twice, facts restated on reopen) |
| Definition / denominator | Beta run under an approved budget |
| Sample | 1 run |
| Period | 2026-10-22 |
| Source | Session record; fixes in the evidence-chat policy and `app/evidence/discovery.py` |
| Kind | Session record |
| System state | Beta |
| Limits | Single run. |

<a id="m-48"></a>
### M-48 — Legacy release suite at the end of the earlier build

| Field | |
|---|---|
| Value | 9,453 passed / 27 failed, each failure classified |
| Definition / denominator | Full legacy release suite |
| Sample | One run |
| Period | 2026-09-30 |
| Source | beta4 commit `90cf2d1` |
| Kind | Measured run (commit message) |
| System state | Earlier build |
| Limits | Size and churn evidence, not quality. |

<a id="m-49"></a>
### M-49 — Test suite at extraction vs the earlier build

| Field | |
|---|---|
| Value | 117 contracts in 3.16 s vs 10,541 in the earlier build |
| Definition / denominator | Full suite of the extracted application on day one |
| Sample | One run |
| Period | 2026-10-03 |
| Source | Commit `461a0e7`; `docs/migration-report.md` |
| Kind | Measured run |
| System state | Local |
| Limits | The suite has since grown to 3,167 test functions (M-30); the "under 1,000" goal was not kept. |

<a id="m-50"></a>
### M-50 — Agent-instruction file size in the earlier build

| Field | |
|---|---|
| Value | 130 → 1,030 lines across 55 commits |
| Definition / denominator | Lines in the project's agent instructions |
| Sample | — |
| Period | 2026-08-10 → 09-29 |
| Source | Baseline ledger NUM-060 |
| Kind | Count |
| System state | Earlier build |
| Limits | Size, not quality; the current project rules file is short by design. |

<a id="m-51"></a>
### M-51 — Cost of preparing and assessing a job (Chart My Course)

| Field | |
|---|---|
| Value | mean $0.0198, median $0.0148, mean 53.7 s per preparation run |
| Definition / denominator | `job_preparation_run.cost_usd` (account-wide ledger difference across the run) and seconds |
| Sample | 89 complete runs on 29 jobs, one account |
| Period | 2026-10-21 → 10-24 |
| Source | Live `job_preparation_run`, read-only |
| Kind | Telemetry |
| System state | Live |
| Limits | Upper-bound definition as M-04; Jev reading dominates. Jobs were prepared about 3.1 times each in the window (89 runs on 29 jobs). Not additive with M-03: M-03 excludes the Jev story reading that assessment pays for. |

<a id="m-52"></a>
### M-52 — Evidence count after story composition

| Field | |
|---|---|
| Value | 176 "evidence pieces" → 86 examples on one account |
| Definition / denominator | Distinct non-retired stories with a current document, before vs after fragments were glued |
| Sample | One account |
| Period | 2026-10-13 (observed 2026-10-19) |
| Source | Commit `5db5ab3` |
| Kind | Measured count |
| System state | Live |
| Limits | One record; nothing deleted — merged fragments count once. |

<a id="m-53"></a>
### M-53 — Splitting already-glued stories (experiment)

| Field | |
|---|---|
| Value | 20 strong requirements became light and 3 became stronger, over 63 jobs |
| Definition / denominator | Requirement strength before vs after splitting merged stories, on a rolled-back Beta session |
| Sample | 63 jobs |
| Period | 2026-10-23 |
| Source | Session record |
| Kind | Session record |
| System state | Beta (copy of Live data) |
| Limits | Rejected; not in a commit or document. |

<a id="m-54"></a>
### M-54 — Role agreement before the bullet constraint

| Field | |
|---|---|
| Value | 0 disagreements across 12,440 candidates, 46 selections and 34 bullets |
| Definition / denominator | Rows whose cited evidence belonged to a different role than the bullet |
| Sample | One database |
| Period | 2026-10-07 |
| Source | Migration `c5e1a9d47b20` docstring; commit `9dd1a46` |
| Kind | Database check |
| System state | Local corpus |
| Limits | The constraint codified existing behaviour. |

<a id="m-55"></a>
### M-55 — Data-loss incident

| Field | |
|---|---|
| Value | 17,183 rows across 50 tables deleted; suite went from 1,298 passed / 1 failed to 1,182 passed / 84 failed / 19 errors; 215 of 221 retired events would have been re-indexed by the re-import |
| Definition / denominator | Rows removed by a cleanup script connected as the schema owner; suite results before and after |
| Sample | Whole local database |
| Period | 2026-10-05 |
| Source | Commit `fb2caa7`; `docs/historical-provenance.md` |
| Kind | Incident record |
| System state | Local corpus database |
| Limits | Frozen measurement artifacts were lost permanently and are documented as lost. |

<a id="m-56"></a>
### M-56 — Bullets matched to stories by position

| Field | |
|---|---|
| Value | 17 bullets written from 15 stories; every bullet after the first split was stored against the wrong story |
| Definition / denominator | Bullets vs stories in one production run |
| Sample | 1 run |
| Period | 2026-10-24 |
| Source | Commit `7322289` |
| Kind | Defect record |
| System state | Live |
| Limits | Fixed by the story-number schema in the same commit. |

<a id="m-57"></a>
### M-57 — Strong evidence written weakly

| Field | |
|---|---|
| Value | About 1 in 6 requirements assessed strong came out partial or absent on the reviewed résumé |
| Definition / denominator | Assessment strength vs the model reviewers' coverage reading of the written résumé |
| Sample | Reviewed résumés (count not stated) |
| Period | 2026-10-23 |
| Source | Beta commit `4e4f206` (not in Live history) |
| Kind | Replay |
| System state | Live data, Beta commit |
| Limits | The attempted fix was reverted (M-18); the figure is not computed by any Live code. |

<a id="m-58"></a>
### M-58 — Gap list vs reviewer verdicts (before the gap redefinition)

| Field | |
|---|---|
| Value | One job showed 15 gaps while both model reviewers would advance the candidate |
| Definition / denominator | Gaps listed vs the reviewers' advance verdicts |
| Sample | 1 job |
| Period | 2026-10-23 |
| Source | Session record (owner report that prompted the change) |
| Kind | Owner-reported observation |
| System state | Live |
| Limits | Single example; the trigger for "a gap is what a reader would pass on". |

<a id="m-59"></a>
### M-59 — Jev question latency

| Field | |
|---|---|
| Value | p50 0.31–1.10 s depending on the question (e.g. 0.31 s repeat labels, 0.34 s interview evidence, 1.10 s story reading); Jev runs up to 32 questions at a time |
| Definition / denominator | `model_execution.seconds` by Jev stage |
| Sample | Thousands of calls per stage |
| Period | 2026-10-21 → 10-24 |
| Source | Live `model_execution`, read-only |
| Kind | Telemetry |
| System state | Live |
| Limits | Network latency to a hosted service; varies by load. |

