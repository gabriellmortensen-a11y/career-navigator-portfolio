# Evidence 05 — Discrepancies between documentation and behaviour

*Where the application's own documents, comments, rules or earlier designs say one thing and the code at Live `7322289` does another. Found during this portfolio's review (2026-10-25). None was fixed as part of this work: the portfolio records them; fixing each is a product decision.*

| ID | Stated | Actual | Status |
|---|---|---|---|
| [D-01](#d-01) | Seven comments and the server's own name say the ChatGPT (MCP) connector is "never on Live" / "Beta". | The connector is mounted on Live: `MCP_ORIGINS` includes Live's origin and a test asserts Live works. A read-only probe on the host (2026-10… | Open (documentation lag; decision was made at unification) |
| [D-02](#d-02) | A security or privacy finding from this review (details withheld from the public version until fixed). | Withheld until fixed. Recorded privately on 2026-10-25 with its evidence and a proposed source fix. | Open — withheld until fixed |
| [D-03](#d-03) | README pipeline: "source → body → exactly one authoritative role" and "writing → grounding validation → final application resume → independe… | New evidence writes no Body/Atom (legacy only). On Live, grounding validation and the independent evaluator run only from measurement code; … | Open (documentation lag) |
| [D-04](#d-04) | `docs/test-inventory.md` (525 tests), `docs/backlog/import-a-resume.md` ("Not built"), `docs/known-defects.md` (2026-10-07), story V2-1065 (… | 3,167 test functions; the importer shipped 2026-10-05; the optimiser was built the day it was backlogged; `docs/reliability/` does not exist… | Open (stale documents) |
| [D-05](#d-05) | The importer's docstring: approval is "a POST behind a button on a page that showed the whole proposal first". | Accept as is on a brought résumé records it as evidence with no proposal page. | Open |
| [D-06](#d-06) | `stories.glue` docstring: "Proposes; writes nothing". | It applies COMPOSE changes and retires fragments. | Open (docstring) |
| [D-07](#d-07) | The capability registry says "a prompt holding the requirements is refused"; the writer's context package declares `demands`/`posting` forbi… | The declaration is never checked in the recruiter flow (each call is recorded as one undivided part); the only enforcement is a substring gu… | Open |
| [D-08](#d-08) | Writing policy V13/V14 attaches relation- and agency-preservation checks to bullets and summaries. | Neither check runs on recruiter-flow output; they run only in the older flow and inside Fix. | Open |
| [D-09](#d-09) | Project rule: "one writer pass, one editor pass, no loops"; the registry labels the flow "One writer pass, one editor pass". | Each section has a draft call and a tighten call; editor corrections get a verify read; Fix (person-pressed) rewrites up to twice and re-rev… | Open — design decision to record |
| [D-10](#d-10) | Project rule: "Ranking, selecting, filtering and deciding a state are Jev's job." | Language models still select or decide in four places: story selection for the résumé (by the owner's design of the recruiter-selects flow),… | Open — partly deliberate |
| [D-11](#d-11) | Application facts are "current facts" about the person (eligibility, availability, logistics). | The pattern also matches technical requirements such as high availability, on-call incident response and export-control compliance programs,… | Open — defect |
| [D-12](#d-12) | The walkthrough docstring: its evidence is what "Jev chose". | It reads the preparation's stored input, which holds the cosine candidate pool; Jev's chosen set is passed to the preparation call but never… | Open — defect |
| [D-13](#d-13) | Discover's "Already applied" is a decision about an opening. | It writes no opportunity status event, so the activity card misses it (the kit and extension do write one). | Open — defect |
| [D-14](#d-14) | Years toward a requirement count only from what the person said (gap chat). | Tune my evidence sums dated roles that Jev reads as that function; the two can disagree for the same person. | Open — inconsistency |
| [D-15](#d-15) | *Ask your record*: "Code narrows and never widens." | When the model returns neither field, the fallback is "sufficient". | Open — defect |
| [D-16](#d-16) | `CE_MODEL_PROVIDER` selects the provider; a global spend ceiling bounds spend; `reserved_usd` records holds. | No code reads `CE_MODEL_PROVIDER` (routing is by model-name prefix); the ceiling binds only on calls that declare an estimate; `reserved_usd… | Open (configuration debt) |
| [D-17](#d-17) | A security or privacy finding from this review (details withheld from the public version until fixed). | Withheld until fixed. Recorded privately on 2026-10-25 with its evidence and a proposed source fix. | Open — withheld until fixed |
| [D-18](#d-18) | Code comments call the career world, work fit, discovery modules and first-five journeys "Beta only" / "an experiment on Beta". | All are switched on for Live; only the Experience Labs and Claude research search remain Beta-only. | Open (documentation lag) |
| [D-19](#d-19) | `assessment.py` refers to "the real recruiter and hiring manager". | These are the app's model reviewer personas, not people; calibration is model-vs-model and not joined to real outcomes. | Open (wording) — named in every metric that uses them |
| [D-20](#d-20) | `provenance.py`: every prompt that carries earlier text labels it there. | The apply-kit answer drafts and the public career conversation label earlier text their own way and are outside the tested rule. | Open |
| [D-21](#d-21) | A résumé run's recorded cost is its cost; stage latency is recorded per call. | Run cost is an account-wide before/after ledger difference (concurrent work inflates it: mean $0.187 vs $0.11 in attributable résumé calls);… | Open — measurement gap |
| [D-22](#d-22) | ORM models declare single-column natural keys. | The database enforces per-account keys (15 constraints re-scoped); the `account_id` column is in no model. | Open (model/schema drift) |
| [D-23](#d-23) | Headers in `career_switch.py` and `requirement_filter.py` say Jev costs $0. | Jev has been priced at $0.042 per million input tokens since 2026-10-14. | Open (comments) |
| [D-24](#d-24) | The 2026-07-08 Application layer described cover letters, executive biography, outreach, networking, application packages, promotion packets… | Of those, only résumés, interview preparation and opportunity analysis were built as products; cover letters exist only as drafted answers i… | Historical — superseded scope |

## Details

<a id="d-01"></a>
### D-01

- **Stated:** Seven comments and the server's own name say the ChatGPT (MCP) connector is "never on Live" / "Beta".
- **Actual:** The connector is mounted on Live: `MCP_ORIGINS` includes Live's origin and a test asserts Live works. A read-only probe on the host (2026-10-25) got 200 from the OAuth discovery endpoint and 401 from `/mcp`.
- **Evidence:** `app/config.py`, `app/main.py`, `app/mcp_beta/*`, `tests/mcp_beta/test_isolation.py`; commit `6c2723c` (2026-10-20, 23:01 PT).
- **Status:** Open (documentation lag; decision was made at unification)

<a id="d-02"></a>
### D-02

- **Stated:** A security or privacy finding from this review (details withheld from the public version until fixed).
- **Actual:** Withheld until fixed. Recorded privately on 2026-10-25 with its evidence and a proposed source fix.
- **Evidence:** Recorded privately.
- **Status:** Open — withheld until fixed

<a id="d-03"></a>
### D-03

- **Stated:** README pipeline: "source → body → exactly one authoritative role" and "writing → grounding validation → final application resume → independent quality evaluation".
- **Actual:** New evidence writes no Body/Atom (legacy only). On Live, grounding validation and the independent evaluator run only from measurement code; résumés come from the recruiter-selects flow.
- **Evidence:** `app/evidence/change.py`; `app/resume/recruiter_flow.py`; `app/pipeline/baseline.py`.
- **Status:** Open (documentation lag)

<a id="d-04"></a>
### D-04

- **Stated:** `docs/test-inventory.md` (525 tests), `docs/backlog/import-a-resume.md` ("Not built"), `docs/known-defects.md` (2026-10-07), story V2-1065 ("not started"); `docs/reliability/` referenced in planning.
- **Actual:** 3,167 test functions; the importer shipped 2026-10-05; the optimiser was built the day it was backlogged; `docs/reliability/` does not exist.
- **Evidence:** Static count; commits `fb2caa7`, `cf27ec8`.
- **Status:** Open (stale documents)

<a id="d-05"></a>
### D-05

- **Stated:** The importer's docstring: approval is "a POST behind a button on a page that showed the whole proposal first".
- **Actual:** Accept as is on a brought résumé records it as evidence with no proposal page.
- **Evidence:** `app/evidence/resume_import.py`; `app/evidence/guided_add.py` (`record_the_resume`).
- **Status:** Open

<a id="d-06"></a>
### D-06

- **Stated:** `stories.glue` docstring: "Proposes; writes nothing".
- **Actual:** It applies COMPOSE changes and retires fragments.
- **Evidence:** `app/pipeline/stories.py`.
- **Status:** Open (docstring)

<a id="d-07"></a>
### D-07

- **Stated:** The capability registry says "a prompt holding the requirements is refused"; the writer's context package declares `demands`/`posting` forbidden.
- **Actual:** The declaration is never checked in the recruiter flow (each call is recorded as one undivided part); the only enforcement is a substring guard, which no test exercises. A unit test of prompt construction does assert the requirements are absent.
- **Evidence:** `app/capabilities.py`; `app/context/packages.py`; `app/resume/recruiter_flow.py`; `tests/resume/test_recruiter_flow.py`.
- **Status:** Open

<a id="d-08"></a>
### D-08

- **Stated:** Writing policy V13/V14 attaches relation- and agency-preservation checks to bullets and summaries.
- **Actual:** Neither check runs on recruiter-flow output; they run only in the older flow and inside Fix.
- **Evidence:** `app/resume/writing_policy.py`; `app/resume/recruiter_flow.py`.
- **Status:** Open

<a id="d-09"></a>
### D-09

- **Stated:** Project rule: "one writer pass, one editor pass, no loops"; the registry labels the flow "One writer pass, one editor pass".
- **Actual:** Each section has a draft call and a tighten call; editor corrections get a verify read; Fix (person-pressed) rewrites up to twice and re-reviews. The rule is interpreted, not literal.
- **Evidence:** `CLAUDE.md`; `app/resume/recruiter_flow.py`; `app/resume/editor_review.py`; `app/resume/repair.py`.
- **Status:** Open — design decision to record

<a id="d-10"></a>
### D-10

- **Stated:** Project rule: "Ranking, selecting, filtering and deciding a state are Jev's job."
- **Actual:** Language models still select or decide in four places: story selection for the résumé (by the owner's design of the recruiter-selects flow), the gap-panel "closes the gap" judgement, concept indexing, and What's Next's fix kind deciding whether a shortfall counts as a gap.
- **Evidence:** `app/resume/recruiter_flow.py`; `app/evidence/guided_add.py`; `app/pipeline/ingestion.py`; `app/evidence/job_gaps.py`.
- **Status:** Open — partly deliberate

<a id="d-11"></a>
### D-11

- **Stated:** Application facts are "current facts" about the person (eligibility, availability, logistics).
- **Actual:** The pattern also matches technical requirements such as high availability, on-call incident response and export-control compliance programs, which are then never sent to reviewers. A second classifier used by the assessment disagrees with it on several phrasings (remote teams, hybrid cloud, certification programs).
- **Evidence:** `app/resume/requirement_kinds.py`; `app/pipeline/demand_index.py`; `tests/jobs/test_not_this_postings_asks.py`.
- **Status:** Open — defect

<a id="d-12"></a>
### D-12

- **Stated:** The walkthrough docstring: its evidence is what "Jev chose".
- **Actual:** It reads the preparation's stored input, which holds the cosine candidate pool; Jev's chosen set is passed to the preparation call but never saved.
- **Evidence:** `app/journey/walkthrough.py`; `app/journey/prep.py`.
- **Status:** Open — defect

<a id="d-13"></a>
### D-13

- **Stated:** Discover's "Already applied" is a decision about an opening.
- **Actual:** It writes no opportunity status event, so the activity card misses it (the kit and extension do write one).
- **Evidence:** `app/discovery/queue.py`; `app/apply/kit.py`.
- **Status:** Open — defect

<a id="d-14"></a>
### D-14

- **Stated:** Years toward a requirement count only from what the person said (gap chat).
- **Actual:** Tune my evidence sums dated roles that Jev reads as that function; the two can disagree for the same person.
- **Evidence:** `app/evidence/requirement_parts.py`; `app/evidence/tune.py`.
- **Status:** Open — inconsistency

<a id="d-15"></a>
### D-15

- **Stated:** *Ask your record*: "Code narrows and never widens."
- **Actual:** When the model returns neither field, the fallback is "sufficient".
- **Evidence:** `app/evidence/answer.py`.
- **Status:** Open — defect

<a id="d-16"></a>
### D-16

- **Stated:** `CE_MODEL_PROVIDER` selects the provider; a global spend ceiling bounds spend; `reserved_usd` records holds.
- **Actual:** No code reads `CE_MODEL_PROVIDER` (routing is by model-name prefix); the ceiling binds only on calls that declare an estimate; `reserved_usd` is never written.
- **Evidence:** `app/governance/provider.py`; `app/governance/execution.py`.
- **Status:** Open (configuration debt)

<a id="d-17"></a>
### D-17

- **Stated:** A security or privacy finding from this review (details withheld from the public version until fixed).
- **Actual:** Withheld until fixed. Recorded privately on 2026-10-25 with its evidence and a proposed source fix.
- **Evidence:** Recorded privately.
- **Status:** Open — withheld until fixed

<a id="d-18"></a>
### D-18

- **Stated:** Code comments call the career world, work fit, discovery modules and first-five journeys "Beta only" / "an experiment on Beta".
- **Actual:** All are switched on for Live; only the Experience Labs and Claude research search remain Beta-only.
- **Evidence:** `app/config.py` and module headers; Live switches (2026-10-25).
- **Status:** Open (documentation lag)

<a id="d-19"></a>
### D-19

- **Stated:** `assessment.py` refers to "the real recruiter and hiring manager".
- **Actual:** These are the app's model reviewer personas, not people; calibration is model-vs-model and not joined to real outcomes.
- **Evidence:** `app/pipeline/assessment.py`; `app/resume/coverage_review.py`.
- **Status:** Open (wording) — named in every metric that uses them

<a id="d-20"></a>
### D-20

- **Stated:** `provenance.py`: every prompt that carries earlier text labels it there.
- **Actual:** The apply-kit answer drafts and the public career conversation label earlier text their own way and are outside the tested rule.
- **Evidence:** `app/context/provenance.py`; `app/apply/kit.py`; `app/career_conversation.py`.
- **Status:** Open

<a id="d-21"></a>
### D-21

- **Stated:** A résumé run's recorded cost is its cost; stage latency is recorded per call.
- **Actual:** Run cost is an account-wide before/after ledger difference (concurrent work inflates it: mean $0.187 vs $0.11 in attributable résumé calls); per-call seconds are NULL for the writer, selector and reviewer stages.
- **Evidence:** `app/resume/pipeline.py`, `app/resume/drafting.py` (`_spend`); Live telemetry 2026-10-21..24.
- **Status:** Open — measurement gap

<a id="d-22"></a>
### D-22

- **Stated:** ORM models declare single-column natural keys.
- **Actual:** The database enforces per-account keys (15 constraints re-scoped); the `account_id` column is in no model.
- **Evidence:** `app/models/evidence.py`, `app/models/chronology.py`; migration `f1b6c284a9e3`.
- **Status:** Open (model/schema drift)

<a id="d-23"></a>
### D-23

- **Stated:** Headers in `career_switch.py` and `requirement_filter.py` say Jev costs $0.
- **Actual:** Jev has been priced at $0.042 per million input tokens since 2026-10-14.
- **Evidence:** `app/journey/career_switch.py`; `app/pipeline/requirement_filter.py`; `app/governance/jev.py`.
- **Status:** Open (comments)

<a id="d-24"></a>
### D-24

- **Stated:** The 2026-07-08 Application layer described cover letters, executive biography, outreach, networking, application packages, promotion packets, performance reviews and a learning engine.
- **Actual:** Of those, only résumés, interview preparation and opportunity analysis were built as products; cover letters exist only as drafted answers inside Greenhouse apply kits; networking exists only as connections import and a message draft.
- **Evidence:** Predecessor `application/` documents; current code.
- **Status:** Historical — superseded scope

