# Evidence 04 — Metric ledger

*Every number the portfolio publishes, with its definition, sample, period, source and kind. Read the rules first. Release 2026.10.1 (describes Live `00eac95`, 2026-10-31) adds M-60 … M-81.*

## Rules

1. **Never combine numbers from different system states.** Each entry names its system (earlier build, current Live, Beta, local). Figures from different states are not a trend, even when they sit side by side.
2. **Kinds are kept apart:** *telemetry* (the product's own records), *controlled experiment* (frozen inputs, pre-declared question), *measured run* (one run, reported in a commit), *replay* (real inputs re-run), *session record* (measured in a working session and recorded in project notes, not in a commit or document), *owner-reported* (my recollection, uncorroborated).
3. **Counts are size, not quality** (commits, tests, lines).
4. **Costs are measured charges** from the call ledger (`model_execution.cost_usd`: tokens × listed price), never reservations or estimates. No invoice is used.
5. **Model personas are not people.** Where a metric uses the app's "recruiter" and "hiring manager" reviewer seats as the reference, it says so.
6. **Live telemetry here is read-only aggregate data from one account (mine)**, queried on 2026-10-25 (release 2026.10.0) and on 2026-10-31 (release 2026.10.1); each entry's source says which. No record text was read. Usage by any other account is not reported; answers given to visitors of my living-résumé links are reported only as aggregates.

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
| [M-22](#m-22) | Cost/latency | Evidence reading vs exhaustive review | 1,164 → 68 judgments, 105 → 15 calls, 267 → 46.1 s, $0.4507 → $0.0385 per posting |
| [M-23](#m-23) | Evidence reading | Jev vs cosine at keeping directly relevant evidence | Jev's top 4 kept 461 of 531 direct pieces vs cosine's 413; Jev's sure cases agreed with the model reader 93% |
| [M-24](#m-24) | Evidence reading | Jev stability on a repeated input | 0.45–0.54 across 11 runs (flips at 0.5) |
| [M-25](#m-25) | Grounding | Sentence-level vs assertion-level grounding | Old validator: 48/48 statements established; assertion-level: 19/48 fully established; adversarial set 9/9 correct after two bug fixes |
| [M-26](#m-26) | Evaluation | Evaluator variance on an unchanged artifact | Major findings ranged by up to 3 across four blind readings (7,7,6,5 and 6,8,5,5; declared tolerance ±3); an optimizer acceptance inside that noise was reversed |
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
| [M-40](#m-40) | Experiments | Named-artifact certainty routing | Routed result equaled the fallback on 47 of 47 pairs; precision 2/2, recall 2/3 |
| [M-41](#m-41) | Résumé quality | Repeat-detection thresholds | Shared facts: 22 within-role sentence pairs at cosine ≥ 0.70, repeats read 0.86–0.94 and different work ≤ 0.84 (threshold 0.85); twin bullets: repeats 0.75–0.81, different ≤ 0.66 (threshold 0.75) |
| [M-42](#m-42) | Historical evaluation | Human-labeled evaluation set (earlier build) | Eval Set v1: 47 blind human-judged pairs, baseline 37/47 (78.7%) → 38/47 (80.9%); a sealed 56-pair holdout has no recorded result |
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
| [M-60](#m-60) | Résumé cost/time | Résumé cost and time on Live after the speed route | 17 runs: cost mean $0.160, median $0.128 (min $0.103, max $0.278); time mean 214 s, median 210 s (min 165 s, max 304 s); per run: selector $0.0130, bullet writer $0.0135, summaries $0.0222 |
| [M-61](#m-61) | Résumé time | Summary time at low vs medium reasoning | 86 s at low vs 148 s and 174 s at medium, with comparable Jev support per sentence (one posting) |
| [M-62](#m-62) | Résumé output | Characters that fit two printed lines | Every bullet up to 228 characters printed on two lines; one of 244 printed on three, which the page measure counted as two → limit 220 |
| [M-63](#m-63) | Résumé output | Finished-line bullets on fixed inputs | Same 20 bullets, same order, same 40 printed lines; 3 writer calls where there were 6 |
| [M-64](#m-64) | Résumé quality | Polish experiment: meaning changed | 6 of 23 bullets at low reasoning, 8 at medium, different ones each time; none flagged |
| [M-65](#m-65) | Résumé quality | A summary over the page's cap | 538 characters against a 520 cap; the page dropped the third sentence |
| [M-66](#m-66) | Latency | Citation re-reading before caching | About 1,100 (requirement, line) Jev pairs and 60–130 s per view; 3,276 readings in three views |
| [M-67](#m-67) | Job analysis | Requirement division on Live | 21 calls: 19 on Claude Haiku 5.5 ($0.0244, median 9.4 s), 2 on gpt-5-mini ($0.0140, median 30.1 s); 190 lines read as one ask, 145 divided into 416 asks |
| [M-68](#m-68) | Model routing | Models used on Live by the new stages | Application chat 19 Haiku + 1 gpt-5-mini; application question 6 Haiku; role understanding 8 Haiku; requirement division 19 Haiku + 2 gpt-5-mini; living résumé 71 Haiku; evidence chat incl. coach 170 Haiku; résumé summaries 136 gpt-5-mini; career journey 1 gpt-5-mini; Growth plan and chat: no Live calls |
| [M-69](#m-69) | Living résumé | Answer cost on Live | 14 visitor answers: mean model-call cost $0.00066, highest $0.0015 (with a posting $0.0008–0.0015); 5 owner previews, highest $0.0018; mean 2–8 s per kind |
| [M-70](#m-70) | Career Chat | Career Chat reads on Live | 40 chat turns, 1 read the account; 336 routing questions to Jev, $0.0071 in all, median 0.2 s each |
| [M-71](#m-71) | Application chat | Application chat on Live | 20 writer calls (19 Haiku, 1 gpt-5-mini), $0.029 in all, median 9.3 s per call; 6 question readings (Haiku), $0.005 |
| [M-72](#m-72) | Application chat | Application chat evaluation | 5 questions, 10 code-scored criteria; measured spend $0.5036 (nine evaluation runs and calibration) and $0.1311 (second story); a first turn 30–70 s |
| [M-73](#m-73) | Interview coach | Meaning questions calibration | 106 messages; "Let's come back to this" read 0.90 as leaving vs a story with "moved on" 0.32 |
| [M-74](#m-74) | Application chat | Pasted application questions | Pasted questions 0.41–0.54; answers and requests 0.07 or less; a question about a draft 0.21 (Beta); new-question line 0.45 → 0.35 |
| [M-75](#m-75) | Career Chat | Read-layer calibration | Routing lines set on 52 asks and 11 ordinary messages; note readings on the 187 gaps of Beta's rejected opportunities |
| [M-76](#m-76) | Latency | Counting gaps for 71 résumés | 86 s to build every review view, so counts are kept |
| [M-77](#m-77) | Interview coach | An introduction drafted from 35 pieces | 35 record pieces in one introduction, before claims-only answers |
| [M-78](#m-78) | Gap conversations | Page said 4 gaps, chat said 2 | 4 vs 2: two of the four were one theme, and a just-saved story still read light |
| [M-79](#m-79) | Engineering size | Test suite at the described commit | Full run on `00eac95`: 3,926 passed, 142 skipped, 0 failed in 652 s; 3,548 test functions in 230 files (static) |
| [M-80](#m-80) | Living résumé | Same-work outcome completion | About +1 s and +60% tokens, with borderline readings; not adopted |
| [M-81](#m-81) | Growth | Growth suggestions on Beta | One call for 15 Growth items, $0.0027 (Haiku) |
| [M-82](#m-82) | Living résumé | Portfolio documents a visitor asks about | "Case study 1": 18th of 55 by content, 2nd by name, Jev 0.90–0.92; 4 of 4 document requests answered from the document; $0.0011–0.0017 an answer |

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
| Source | `app/pipeline/assessment.py` (`NOTICED`); commit `6026681` |
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

*Describes the summary path superseded on Live on 2026-10-28 ([A-101](03-claim-index.md#a-101)); Live summaries are now written to the page's own character cap ([M-65](#m-65)).*

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
| Value | 1,164 → 68 judgments, 105 → 15 calls, 267 → 46.1 s, $0.4507 → $0.0385 per posting |
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
| Value | Major findings ranged by up to 3 across four blind readings (7,7,6,5 and 6,8,5,5; declared tolerance ±3); an optimizer acceptance inside that noise was reversed |
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
| Value | Routed result equaled the fallback on 47 of 47 pairs; precision 2/2, recall 2/3 |
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
### M-42 — Human-labeled evaluation set (earlier build)

| Field | |
|---|---|
| Value | Eval Set v1: 47 blind human-judged pairs, baseline 37/47 (78.7%) → 38/47 (80.9%); a sealed 56-pair holdout has no recorded result |
| Definition / denominator | Agreement of the obligation gate with human labels |
| Sample | 47 pairs |
| Period | 2026-09-25 |
| Source | beta4 commits `10a7501`, `8f9baa0`; ledger SYS-007, SYS-008, LAT-080 |
| Kind | Human-labeled experiment |
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
| Source | `app/evidence/themes.py` comment; commit `294d859` |
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
| Limits | The constraint codified existing behavior. |

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

<a id="m-60"></a>
### M-60 — Résumé cost and time on Live after the speed route

| Field | |
|---|---|
| Value | 17 complete runs: cost mean $0.160, median $0.128 (min $0.103, max $0.278); time mean 214 s, median 210 s (min 165 s, max 304 s). Per run, by stage: selector $0.0130 (5.1 calls), bullet writer $0.0135 (3.8 calls), summaries (`resume_summary_tool`) $0.0222 (6.5 calls) |
| Definition / denominator | Run figures: `resume_generation_run.cost_usd` (the run ledger, as M-04) and `seconds` of runs in state complete. Stage figures: sum of `model_execution.cost_usd` and count of rows per stage, keyed to each run by `input_artifact->>'selection_run'`, ÷ runs |
| Sample | 17 complete runs (one account); no run ended in another state |
| Period | 2026-10-30 00:58:52 UTC (Live deploy of `77acb9c`, from the host's deploy history) → 2026-10-31 |
| Source | Read-only query on the production host, 2026-10-31 |
| Kind | Telemetry |
| System state | Live `77acb9c` … `00eac95`: bullets written as their finished line, summaries from a positioning brief at low reasoning, started beside the bullets ([A-11](03-claim-index.md#a-11), [A-82](03-claim-index.md#a-82), [A-88](03-claim-index.md#a-88)) |
| Limits | A different system state from M-04/M-05 (mean $0.187 / median $0.198; median 207 s): side by side, not a trend (rule 1). The run cost is an upper bound for the same reason as M-04 ([D-21](05-discrepancies.md#d-21)). I asked for half the time and the cost; M-05 and M-60 are different system states, and neither shows the run time halved. Per-call seconds are not recorded for these stages ([P-17](03-claim-index.md#p-17)). |

<a id="m-61"></a>
### M-61 — Summary time at low vs medium reasoning

| Field | |
|---|---|
| Value | 86 s at low reasoning vs 148 s and 174 s at medium. Jev support per sentence of the professional summary .51 / .89 / .69 at low vs .62 / .89 / .48 and .60 / .89 / .48 at medium; every role summary supported, no flag, within the page's cap, with about a third of the reasoning |
| Definition / denominator | Time of the summary steps (planner and writers) in one résumé run; Jev's support reading of each of the professional summary's three sentences |
| Sample | 1 run at low vs 2 runs at medium, one posting |
| Period | 2026-10-29 |
| Source | Commit `85de28a`; `app/resume/main_summary.py` (`EFFORT` comment) |
| Kind | Measured run |
| System state | Beta (data refreshed from Live) |
| Limits | n = 3, one posting. Summary time only, not a whole-résumé time; Live runs since are in [M-60](#m-60). |

<a id="m-62"></a>
### M-62 — Characters that fit two printed lines

| Field | |
|---|---|
| Value | Every bullet of up to 228 characters printed on two lines; one of 244 printed on three, which the page measure (122 characters a line) counted as two → threshold 220 characters. Earlier, the page measure matched the print for all 56 bullets of three résumés |
| Definition / denominator | Printed lines of each bullet in downloaded PDF résumés against its length in characters |
| Sample | 78 bullets in four downloaded résumés; earlier 56 bullets in three |
| Period | 2026-10-29 |
| Source | Commits `7411d3f`, `77acb9c`; `app/resume/recruiter_flow.py` (`TWO_LINES` comment) |
| Kind | Measured run (downloaded PDFs) |
| System state | Beta |
| Limits | One person's résumé template and font. 220 is the design limit taken from it ([A-91](03-claim-index.md#a-91)). |

<a id="m-63"></a>
### M-63 — Finished-line bullets on fixed inputs

| Field | |
|---|---|
| Value | The same 20 bullets in the same order and the same 40 printed lines; 3 writer calls where there were 6 |
| Definition / denominator | One earlier run's inputs written again with bullets drafted as their finished line and only bullets past two printed lines shortened |
| Sample | One run's inputs |
| Period | 2026-10-29 |
| Source | Commit `7411d3f` |
| Kind | Replay |
| System state | Beta |
| Limits | One résumé. Shows no bullet lost or reordered and fewer calls; says nothing about wording quality. |

<a id="m-64"></a>
### M-64 — Polish experiment: meaning changed

| Field | |
|---|---|
| Value | Meaning changed in 6 of 23 bullets at low reasoning and 8 at medium, different bullets each time; none flagged as unclear. An earlier expanding instruction grew one bullet from 29 to 62 words |
| Definition / denominator | Bullets whose polished copy said something different from the kept text ÷ bullets in the run |
| Sample | One run's 23 bullets, at two reasoning levels |
| Period | 2026-10-29 |
| Source | Commits `61362ff`, `f23ed14` |
| Kind | Replay |
| System state | Beta |
| Limits | One résumé; "meaning changed" was judged in the working session. The experiment was closed ([A-97](03-claim-index.md#a-97)). |

<a id="m-65"></a>
### M-65 — A summary over the page's cap

| Field | |
|---|---|
| Value | 538 characters against a 520-character cap; the page dropped the third sentence |
| Definition / denominator | Length of one professional summary against the writing policy's `executive_summary.max_chars` |
| Sample | One run |
| Period | 2026-10-28 |
| Source | Commit `29754f5` |
| Kind | Measured run |
| System state | Beta |
| Limits | One example; it is why the summary is now written to the page's own cap. |

<a id="m-66"></a>
### M-66 — Citation re-reading before caching

| Field | |
|---|---|
| Value | About 1,100 (requirement, line) Jev pairs per view and 60–130 s per view; 3,276 readings in three views |
| Definition / denominator | Jev readings asked to re-cite reworded lines when a review page was opened, before the readings were cached on their own committed session |
| Sample | One review with every line reworded |
| Period | 2026-10-30 |
| Source | Commit `458864a` |
| Kind | Measured run (a Live observation recorded in a commit) |
| System state | Live, before `458864a` |
| Limits | One review. Fixed at the source: readings are now kept ([A-93](03-claim-index.md#a-93)). |

<a id="m-67"></a>
### M-67 — Requirement division on Live

| Field | |
|---|---|
| Value | 21 `requirement_division` calls: 19 on Claude Haiku 5.5 ($0.0244 in all, median 9.4 s), 2 on gpt-5-mini ($0.0140, median 30.1 s, before the assignment was set). `job_demand.division`: 190 lines read as one ask (`whole`), 145 lines divided (`divided`), 416 asks from divided lines (`part`) |
| Definition / denominator | `model_execution` rows with stage `requirement_division` by model: count, sum of `cost_usd`, median `seconds`. `job_demand` rows by `division` where it is set |
| Sample | All calls and all read lines of one account |
| Period | Since 2026-10-25 (the stage reached Live with `a41a455`, deployed 2026-10-27 19:47 UTC) → 2026-10-31 |
| Source | Read-only query on the production host, 2026-10-31 |
| Kind | Telemetry |
| System state | Live |
| Limits | Single user. The two gpt-5-mini calls are the seed-assignment gap ([D-27](05-discrepancies.md#d-27)). |

<a id="m-68"></a>
### M-68 — Models used on Live by the new stages

| Field | |
|---|---|
| Value | `application_chat` 19 Claude Haiku 5.5 + 1 gpt-5-mini; `application_question` 6 Haiku; `role_understanding` 8 Haiku; `requirement_division` 19 Haiku + 2 gpt-5-mini (M-67); `career_conversation` 71 Haiku; `evidence_chat` (coach turns included) 170 Haiku; `resume_summary_tool` 136 gpt-5-mini; `career_journey` 1 gpt-5-mini; `growth_plan` and `growth_chat`: no Live calls yet |
| Definition / denominator | `model_execution` rows by stage and `model` |
| Sample | All calls of one account |
| Period | 2026-10-25 → 2026-10-31 |
| Source | Read-only query on the production host, 2026-10-31 |
| Kind | Telemetry |
| System state | Live |
| Limits | Single user. Shows the model each stage actually ran on, which the seed alone does not settle ([D-27](05-discrepancies.md#d-27)). The Growth stages' model on Live is unverified until they are called. |

<a id="m-69"></a>
### M-69 — Living-résumé answer cost on Live

| Field | |
|---|---|
| Value | 14 answers through links (not owner previews): mean model-call cost $0.00066, highest $0.0015; with a posting $0.0008–0.0015. Owner previews: 5, highest $0.0018 (with a posting). Mean time 2–8 s per kind of answer. All `career_conversation` calls since 2026-10-25: 71, $0.0434 in all (mean $0.0006), all Claude Haiku |
| Definition / denominator | `shared_conversation_turn` rows joined to their `model_execution` row: count, mean `cost_usd` and mean `seconds`, by preview, basis and whether a posting was sent |
| Sample | 14 visitor answers and 5 owner previews on one account's links |
| Period | 2026-10-30 23:00 UTC, some hours before the rename (`4555460`, authored 2026-10-31 06:29 UTC) → 2026-10-31; stage totals from 2026-10-25 |
| Source | Read-only query on the production host, 2026-10-31 |
| Kind | Telemetry |
| System state | Live (posting answers in a résumé's shape, Claude Haiku) |
| Limits | Visitors are third parties: aggregates only, no text. Small sample. [M-44](#m-44) ($0.0047) was the earlier engine: not a trend. |

<a id="m-70"></a>
### M-70 — Career Chat reads on Live

| Field | |
|---|---|
| Value | 40 chat turns, 1 of which read the account; 336 `chat_reads_route` Jev questions recorded, $0.0071 in all, median 0.2 s each |
| Definition / denominator | `evidence_chat_turn` rows with a `reads` entry ÷ all turns; `model_execution` rows with stage `chat_reads_route` (cache hits write no row) |
| Sample | One account's chat turns |
| Period | Since the Live deploy of `88123b4` (2026-10-28 18:45 UTC) → 2026-10-31 |
| Source | Read-only query on the production host, 2026-10-31 |
| Kind | Telemetry |
| System state | Live |
| Limits | Single user, three days. Routing accuracy is not measured ([A-104](03-claim-index.md#a-104)). |

<a id="m-71"></a>
### M-71 — Application chat on Live

| Field | |
|---|---|
| Value | 20 writer calls (19 Claude Haiku, 1 gpt-5-mini), $0.029 in all, median 9.3 s per call; 6 question readings (Haiku), $0.005 |
| Definition / denominator | `model_execution` rows with stages `application_chat` and `application_question`: count, sum of `cost_usd`, median `seconds` |
| Sample | One account |
| Period | 2026-10-27 (first Live call) → 2026-10-31 |
| Source | Read-only query on the production host, 2026-10-31 |
| Kind | Telemetry |
| System state | Live |
| Limits | Single user. Excludes the Jev readings and embeddings an answer also uses. |

<a id="m-72"></a>
### M-72 — Application chat evaluation

| Field | |
|---|---|
| Value | Five questions on two employers' opportunities, scored by code on ten criteria. Measured spend $0.5036 (nine evaluation runs and calibration) and $0.1311 (second story). In the last run every case drafted from checked evidence or asked one focused question; an answer limited to 600 characters came back at 701, then 441, then 519 characters; a 400–600-word answer went from 151 words to 273 fully supported words. A first turn on a question takes 30–70 s |
| Definition / denominator | Per-criterion pass/fail by a code rubric (`app/apply/rubric.py`); spend is the sum of `cost_usd` of the runs |
| Sample | 5 questions; nine runs plus a second story |
| Period | 2026-10-27 |
| Source | `experiments/application_chat_log.md` (commits `22451ca`, `36d9211`) |
| Kind | Controlled experiment |
| System state | Beta copy of one Live account; the nine evaluation runs on gpt-5-mini (the assignment was not in force), the second story on Claude Haiku |
| Limits | One account's record; a code rubric, not people. The log's own words: "Not yet at the baselines' prose quality". |

<a id="m-73"></a>
### M-73 — Meaning questions calibration

| Field | |
|---|---|
| Value | Thresholds set against 106 messages; "Let's come back to this" read 0.90 as leaving, a story with "moved on" in it 0.32 |
| Definition / denominator | Jev's probability for each meaning question on each message, against the meaning the message had |
| Sample | 106 messages from one account (its Live messages and varied phrasings) |
| Period | 2026-10-26/27 |
| Source | Commit `0018434`; `tests/journey/test_heard.py` (`BETA` fixed data) |
| Kind | Controlled experiment (calibration) |
| System state | Beta |
| Limits | One account's phrasing. The `heard.py` docstring gives older readings for the same two messages ([D-32](05-discrepancies.md#d-32)). |

<a id="m-74"></a>
### M-74 — Pasted application questions

| Field | |
|---|---|
| Value | Pasted form questions read 0.41–0.54 as a new question; answers and requests 0.07 or less; a question about a draft 0.21 (Beta). The line moved from 0.45 to 0.35 |
| Definition / denominator | Jev's stored "new question" reading on application-chat messages |
| Sample | Every stored reading of Live application chats (one account) plus one Beta calibration message |
| Period | 2026-10-30 |
| Source | Commit `8d92b75`; `tests/journey/test_heard.py` (`LIVE_QUESTIONS`) |
| Kind | Telemetry recorded in a commit |
| System state | Live (readings), Beta (one calibration) |
| Limits | One account; the margin above the line is thin ([A-76](03-claim-index.md#a-76)). |

<a id="m-75"></a>
### M-75 — Read-layer calibration

| Field | |
|---|---|
| Value | Routing lines set on 52 asks phrased as people ask them and 11 ordinary messages, each line under its lowest real ask and above what it should not read; note readings set on the 187 gaps of Beta's rejected opportunities |
| Definition / denominator | Jev's probability per read operation's question on each message; per kind question on each reviewer note |
| Sample | 52 + 11 messages; 187 reviewer gaps |
| Period | 2026-10-28 |
| Source | `app/reads/route.py` and `app/reads/analysis.py` comments; commits `eb73d50`, `73416a8`, `c555871` |
| Kind | Controlled experiment (calibration) |
| System state | Beta (one account) |
| Limits | Calibrated once; Jev is stubbed in every test ([A-104](03-claim-index.md#a-104)). |

<a id="m-76"></a>
### M-76 — Counting gaps for 71 résumés

| Field | |
|---|---|
| Value | 86 s to build every review view for 71 résumés, which is why each job's gap count is kept |
| Definition / denominator | Wall-clock time to build the review views from which the gap counts come |
| Sample | 71 résumés |
| Period | 2026-10-27 |
| Source | Commit `05abced`; `app/journey/standing.py` docstring |
| Kind | Measured run |
| System state | Beta |
| Limits | One account's résumés. Pages can still pay at render on a cache miss ([D-35](05-discrepancies.md#d-35)). |

<a id="m-77"></a>
### M-77 — An introduction drafted from 35 pieces

| Field | |
|---|---|
| Value | One introduction drafted from 35 pieces of the record, including leftover test text |
| Definition / denominator | Record pieces the coaching call drew on for one draft |
| Sample | One Live coaching conversation |
| Period | 2026-10-25 |
| Source | Commit `291517d` |
| Kind | Measured run (a Live observation recorded in a commit) |
| System state | Live, before claims-only answers |
| Limits | One case; it motivated [A-63](03-claim-index.md#a-63). |

<a id="m-78"></a>
### M-78 — Page said 4 gaps, chat said 2

| Field | |
|---|---|
| Value | The opportunity page said 4 gaps while the chat said "2 gaps to go": two of the four were one theme, and a just-saved story still read light |
| Definition / denominator | Gap count on the page vs the chat for one opportunity |
| Sample | One opportunity |
| Period | 2026-10-30 |
| Source | Commit `798fbf9` |
| Kind | Measured run (a Live observation recorded in a commit) |
| System state | Live, before `798fbf9` |
| Limits | One case; it motivated [A-78](03-claim-index.md#a-78). |

<a id="m-79"></a>
### M-79 — Test suite at the described commit

| Field | |
|---|---|
| Value | Full suite on the Live code `00eac95`: 3,926 passed, 142 skipped, 0 failed in 652 s (the runs before, on `821b151`: 3,920 passed; on `79658ad`: 3,919 passed; each 142 skipped, 0 failed). Static count: 3,548 test functions in 230 files at `00eac95` (3,541 at `79658ad`; 3,167 in 209 at `7322289`) |
| Definition / denominator | The suite's own pass/skip/fail result; static count of `def test_` under `tests/`, parametrization not expanded |
| Sample | — |
| Period | 2026-10-31, before the deploy of `00eac95` |
| Source | Session record (run); `tests/` (count) |
| Kind | Session record + count |
| System state | Local suite on the exact Live code |
| Limits | Counts are size, not quality (rule 3). Functions ≠ collected cases. Many tests stand in for the model and Jev; some test summary code no Live path calls ([D-26](05-discrepancies.md#d-26)). Skip reasons not re-audited since [M-30](#m-30). |

<a id="m-80"></a>
### M-80 — Same-work outcome completion

| Field | |
|---|---|
| Value | Adding a story's outcome from other pieces of the same work gave borderline readings at about +1 s and +60% tokens; not adopted |
| Definition / denominator | Time and tokens of one living-résumé answer with and without the completion step |
| Sample | One Live answer, reproduced exactly |
| Period | 2026-10-31 |
| Source | Commit `b8d8cf2` |
| Kind | Replay |
| System state | One Live answer's inputs, replayed (the commit does not say on which system) |
| Limits | One answer ([A-119](03-claim-index.md#a-119)). |

<a id="m-81"></a>
### M-81 — Growth suggestions on Beta

| Field | |
|---|---|
| Value | One Suggest action plans call for 15 Growth items, $0.0027 (Claude Haiku) |
| Definition / denominator | `model_execution.cost_usd` of the one `growth_plan` call |
| Sample | One call |
| Period | 2026-10-30 |
| Source | Session record |
| Kind | Session record |
| System state | Beta |
| Limits | One call. No Live call yet ([M-68](#m-68)). |

<a id="m-82"></a>
### M-82 — Portfolio documents a visitor asks about

| Field | |
|---|---|
| Value | **Calibration:** for "Can you summerize case study 1?" its document ranked 18th of 55 by content and 2nd by name; Jev read it 0.90, and 0.92 for the follow-up "I want you to summerize it."; every case study read 0.56–0.76 for "the case studies"; no document read above 0.04 for a question about what I built at a past employer; documents outside both short lists read 0.51–0.68 at worst. **Replay:** of four requests for a portfolio document, before the change none was answered from the document (the answers said they couldn't show or summarize it); after it, 4 of 4 were ("the case studies" summarized all six), and the control question drew no portfolio. $0.0011–0.0017 a model answer; $0.022 for the whole validation, Jev and embeddings included |
| Definition / denominator | Ranks by cosine of the message (with the one before it) to each document's name, and to its sections' stored vectors; Jev's probability for `portfolio.ASKS_ABOUT`; an answer counts as from the document when its cited portfolio artifacts are that document's parts |
| Sample | One portfolio (55 public documents); six messages for calibration; a seven-message Live conversation replayed twice |
| Period | 2026-10-31 |
| Source | Commits `d6e7c36`, `00eac95` (`app/portfolio.py` comment); session record of the Beta runs |
| Kind | Calibration and replay |
| System state | Beta, with the owner's portfolio |
| Limits | One portfolio and one conversation. The thresholds are set on these readings, not tested on another portfolio. |

