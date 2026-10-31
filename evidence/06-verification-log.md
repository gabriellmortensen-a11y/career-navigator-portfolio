# Evidence 06 — Verification log

How the evidence behind release **2026.10.0** was gathered and checked (2026-10-25), and which
publication checks it passed. Investigations were run by Claude Code agents at my direction. Every
step was read-only, and no model or API spend was incurred to produce this portfolio.

## 1. Code and history

| Scope | Method | Result |
|---|---|---|
| Current system | A read-only export of Live commit `7322289` (2026-10-24), plus `git log` / `git show`. Five investigations (evidence governance; job analysis and résumé; discovery, apply and interview; measurement and operations; chronology since the baseline) each cited `file:line` and commits | Claims `K-`, `P-`, `A-`; discrepancies `D-01`–`D-23` |
| Beta parity | Tree hash of Beta `2a5f749` compared with Live `7322289` | Identical trees |
| Baseline | Digest of the 2026-09-30 package, plus hash and quote checks | 113/113 hashes exist; 73/73 quoted figures match (see [01-baseline](01-baseline.md)) |
| Test surface | Static count of `def test_` under `tests/` at `7322289` | 3,167 functions in 209 files (not run) |

**Figures re-read directly in their source commits by the portfolio author:**

| Commit | Figure |
|---|---|
| `8bedc4c`, `2068a41` | Evidence reading: 1,164 → 68 judgements; 105 → 15 calls; 267 → 46.1 s; $0.4507 → $0.0385 |
| `d897201` | Jev top 4: 461 of 531 vs cosine 413; 93% agreement on 309 readings |
| `766061f` | 84% / 74% and 79% / 58% on 19 reviewed résumés; 320 of 602 light written strong |
| `4c984f8` | Pages at 4–6 s instead of ~1 s on a 2-core host |
| `e801ffa` | 578 found → 34 close → 8 read |
| `2d3482b` | 73% / 96% of summaries over the limit |
| `2cd7811` | 868 s, $0.2541, 31 calls; grounding 493.5 s |
| `5a8456a` | About 45% less time at low effort on 13 replayed turns |
| `a072e68` | $0.0047 per shared-link question |
| `ea06f2f` | 13 requirements → 1 theme; 10 → 4 |

**Code re-read directly:**
- the writer-prompt guard and the `UNGROUNDED` storage in `app/resume/recruiter_flow.py`;
- `role_key` in `app/authority/role_boundary.py`;
- the importer's role matching, locators and accepted formats (`app/evidence/resume_import.py`,
  `resume_reading.py`);
- the Change Document `inspect` return shape;
- the `_spend` cost definition (`app/resume/drafting.py`);
- the two governed résumé prompts and the model-assignments seed.

## 2. Live telemetry (read-only)

All queries ran on the production host as a read-only transaction
(`default_transaction_read_only=on`). They returned aggregates only, and no record text was
selected. Definitions, with `:owner` standing for my account:

| Metric | Definition |
|---|---|
| [M-03](04-metric-ledger.md#m-03) | `sum(cost_usd)` from `model_execution` where `account_id = :owner` and stage is one of the six résumé writing and review stages, `ran_at` in [2026-10-21, 2026-10-25) UTC, ÷ complete `resume_generation_run` rows started in the same window |
| [M-04](04-metric-ledger.md#m-04)–[M-07](04-metric-ledger.md#m-07) | Mean, median, min and max of `cost_usd` and `seconds`, and per-phase JSON fields, over complete `resume_generation_run` rows of `:owner` in the window (and before 2026-10-14 for M-06) |
| [M-08](04-metric-ledger.md#m-08) | `job_status_event` rows of `:owner` with `to_status = 'applied'`, excluding undo rows and rows undone; for each event, distinct jobs within the next 40/60/90/120/180 minutes; the maximum per window; distinct jobs per Pacific day |
| [M-10](04-metric-ledger.md#m-10), [M-11](04-metric-ledger.md#m-11) | `discovery_run.summary` fields (found, new, close, assessed, recommended) and `cost_usd` for `:owner`; `discovery_opening` counts |
| [M-21](04-metric-ledger.md#m-21) | `model_execution` stage `evidence_chat`, model, `count`, `sum(cost_usd)`, percentiles of `seconds`, in the window |
| [M-51](04-metric-ledger.md#m-51) | `job_preparation_run` complete rows of `:owner` started in the window: `count`, distinct jobs, mean and median `cost_usd`, mean `seconds` |
| [P-07](03-claim-index.md#p-07) | `count(*)` of `model_check` (0) |
| [P-17](03-claim-index.md#p-17), [D-21](05-discrepancies.md#d-21) | Rows with `seconds IS NULL` by résumé stage in the window |

**Other read-only checks on the host:**
- **Feature switches:** names and values from the production configuration, with secret-bearing
  keys excluded.
- **MCP probe:** two unauthenticated loopback requests. The OAuth discovery endpoint returned 200,
  and `/mcp` returned 401.
- **Import alignment:** one role row of my account (employer, title, start) and a count of existing
  import locators, which was 0.

## 3. The career-evidence file

`tools/check_import.py` ran Career Navigator's own reader (`app/evidence/resume_reading.py` at
`7322289`) on [career-navigator-learnings.txt](../career-evidence/career-navigator-learnings.txt).

| Field | Result |
|---|---|
| Roles | 1 |
| Employer | `Career Navigator (Independent)` |
| Title | `Founder / Product Leader` |
| Start | `2026-04` |
| Bullets | 39 |
| Unplaced lines | 0 |

**Passed.**

## 4. Publication checks for this release

| Check | Tool | Result |
|---|---|---|
| Every relative link and image resolves; every `#anchor` matches a heading or explicit anchor | `tools/check_links.py` | **Passed** (see the release run below) |
| Every Mermaid diagram renders | `tools/check_mermaid.sh` (mermaid-cli 12.0.0) | **Passed**: 9 of 9 |
| No credentials, private keys, emails, phone numbers, IP addresses, server paths, database URLs, environment files or the connections export; no unfinished-work markers | `tools/scan_sensitive.py` | **Passed**: 0 findings |
| No private term: employer and company names from my career record and job search, my email, the host address, persona names, session-link prefixes (a 57-term list kept **outside** the repository) | `tools/scan_sensitive.py` with `PRIVATE_TERMS` | **Passed**: 0 findings |
| No internal record identifiers (run, job, review, turn or account numbers) | `grep` | **Passed** |
| No empty files | `tools/check.sh` | **Passed** |

Five generic words were removed from the private list because they matched legitimate text:
- a placeholder company name;
- the earlier build's internal name;
- the names of an applicant-tracking system and two model providers, used here as vendors.

**Release run (2026-10-25):** `tools/check.sh` with `MMDC`, `PRIVATE_TERMS` and `APP_SRC` set, run
after the review corrections below. All sections passed. An earlier run had passed too, but a late
edit then added a link to a metric not yet generated. The independent review caught it, which is why
the final run comes last.

## 5. Independent review before release

A separate Claude Code agent, not the one that wrote the portfolio, reviewed it against the code
snapshot and git history. It spot-checked 68 claims; 59 held as written. It also re-checked every
count. Everything it found was corrected before release:

| Kind | Found | Examples of what changed |
|---|---:|---|
| Factual errors | 17 | Two retired rules had been merged into one; the summary limit is "at most" 3 × 15 words, not fixed counts; forced row-level security was built alongside the data-loss incident, not because of it; wrong commit and test references in three claims; a weighted coverage figure described as accuracy |
| Overclaims | 13 | "Every rank and state goes to Jev" now names its exceptions; "person-picked role" became "confirmed role (guess preselected)"; "real review" became "the model reviewers' verdicts"; a cost "reduction" claim was removed; the learnings file now separates decisions I originated from agent proposals I accepted |
| Provenance gaps | 13 numbers | Each now has a metric-ledger entry (M-52–M-59) or was reworded |
| Clarity | — | [GLOSSARY.md](../GLOSSARY.md) added and linked from the README |

## 6. Publication decisions (2026-10-25)

I decided the following before the repository was made public:

1. **Public repository.**
2. **Two open security and privacy findings are withheld** ([D-02](05-discrepancies.md#d-02),
   [D-17](05-discrepancies.md#d-17)). Their details are recorded privately and will be published
   when they are fixed. The production hostname is left out for the same reason.
3. **My own job-search throughput figures stay**
   ([M-08](04-metric-ledger.md#m-08), [M-10](04-metric-ledger.md#m-10)).
4. **All rights reserved** ([LICENSE](../LICENSE)).
5. **Release checks:** `tools/check.sh` is run with `PRIVATE_TERMS` pointing at the private denylist,
   which is kept outside the repository.
6. **Commit metadata:** a GitHub noreply author address, as the baseline's publication audit
   recommends. The 2026.10.0 release was a single commit; later changes are added as further
   commits with the same author and no session or tool links in their messages.

## 7. What was not done

- **No test suite run.** The suite needs the private corpus database. The last recorded full run
  (2026-10-21) is cited as a session record ([M-30](04-metric-ledger.md#m-30)).
- **No application pages rendered and no screenshots taken.** Real pages show a real career record.
- **No model, search or scraping call made.** No spend.
- **No defect fixed in the application.** Findings are recorded in [discrepancies](05-discrepancies.md).
