# Evidence 05 — Discrepancies between documentation and behavior

*Where the application's own documents, comments, rules or earlier designs say one thing and the code at Live `00eac95` (2026-10-31) does another. D-01 … D-24 were found during the 2026.10.0 review (2026-10-25) and re-checked against Live `79658ad` for this release; D-25 … D-39 were found during the 2026.10.1 review (2026-10-31). None was fixed as part of this work: the portfolio records them; fixing each is a product decision.*

| ID | Stated | Actual | Status |
|---|---|---|---|
| [D-01](#d-01) | Seven comments and the server's own name say the ChatGPT (MCP) connector is "never on Live" / "Beta". | The connector is mounted on Live: `MCP_ORIGINS` includes Live's origin and a test asserts Live works. A read-only probe on the host (2026-10… | Open (documentation lag; decision was made at unification) |
| [D-02](#d-02) | A security or privacy finding from this review (details withheld from the public version until fixed). | Withheld until fixed. Recorded privately on 2026-10-25 with its evidence and a proposed source fix. | Open — withheld until fixed |
| [D-03](#d-03) | README pipeline: "source → body → exactly one authoritative role" and "writing → grounding validation → final application resume → independe… | New evidence writes no Body/Atom (legacy only). On Live, grounding validation and the independent evaluator run only from measurement code; … | Open (documentation lag) |
| [D-04](#d-04) | `docs/test-inventory.md` (525 tests), `docs/backlog/import-a-resume.md` ("Not built"), `docs/known-defects.md` (2026-10-07), story V2-1065 (… | 3,542 test functions in 230 files (static count at `00eac95`, M-79); the importer shipped 2026-10-05; the optimizer was built the day it was… | Open (stale documents) |
| [D-05](#d-05) | The importer's docstring: approval is "a POST behind a button on a page that showed the whole proposal first". | Accept as is on a brought résumé records it as evidence with no proposal page. | Open |
| [D-06](#d-06) | `stories.glue` docstring: "Proposes; writes nothing". | It applies COMPOSE changes and retires fragments. | Open (docstring) |
| [D-07](#d-07) | The capability registry says "a prompt holding the requirements is refused"; the writer's context package declares `demands`/`posting` forbi… | The declaration is never checked in the recruiter flow (each call is recorded as one undivided part); the only enforcement is a substring gu… | Open |
| [D-08](#d-08) | Writing policy V13/V14 attaches relation- and agency-preservation checks to bullets and summaries. | Neither check runs on recruiter-flow output; they run only in the older flow and inside Fix. | Open |
| [D-09](#d-09) | Project rule: "one writer pass, one editor pass, no loops"; the registry labels the flow "One writer pass, one editor pass". | Bullets are drafted as finished lines, and only a bullet longer than two printed lines gets a second, tightening call. Summaries are planned… | Open — design decision to record |
| [D-10](#d-10) | Project rule: "Ranking, selecting, filtering and deciding a state are Jev's job." | Language models still select or decide in six places: story selection for résumé bullets (by the owner's design of the recruiter-selects flo… | Open — partly deliberate |
| [D-11](#d-11) | Application facts are "current facts" about the person (eligibility, availability, logistics). | The pattern also matches technical requirements such as high availability, on-call incident response and export-control compliance programs,… | Open — defect |
| [D-12](#d-12) | The walkthrough docstring: its evidence is what "Jev chose". | It reads the preparation's stored input, which holds the cosine candidate pool; Jev's chosen set is passed to the preparation call but never… | Open — defect |
| [D-13](#d-13) | Discover's "Already applied" is a decision about an opening. | It writes no opportunity status event, so the activity card misses it (the kit and extension do write one). | Open — defect |
| [D-14](#d-14) | Years toward a requirement count only from what the person said (gap chat). | Career Direction's role pages (the reading Tune my evidence used; the page itself was retired on 2026-10-30, A-107) sum dated roles that Jev… | Open — inconsistency |
| [D-15](#d-15) | *Ask your record*: "Code narrows and never widens." | When the model returns neither field, the fallback is "sufficient". | Open — defect |
| [D-16](#d-16) | `CE_MODEL_PROVIDER` selects the provider; a global spend ceiling bounds spend; `reserved_usd` records holds. | No code reads `CE_MODEL_PROVIDER` (routing is by model-name prefix); the ceiling binds only on calls that declare an estimate; `reserved_usd… | Open (configuration debt) |
| [D-17](#d-17) | A security or privacy finding from this review (details withheld from the public version until fixed). | Withheld until fixed. Recorded privately on 2026-10-25 with its evidence and a proposed source fix. | Open — withheld until fixed |
| [D-18](#d-18) | Code comments call the career world, work fit, discovery modules and first-five journeys "Beta only" / "an experiment on Beta". | All are switched on for Live; only the Experience Labs and Claude research search remain Beta-only. | Open (documentation lag) |
| [D-19](#d-19) | `assessment.py` refers to "the real recruiter and hiring manager". | These are the app's model reviewer personas, not people; calibration is model-vs-model and not joined to real outcomes. | Open (wording) — named in every metric that uses them |
| [D-20](#d-20) | `provenance.py`: every prompt that carries earlier text labels it there. | The apply-kit answer drafts, the living résumé and the application chat label earlier text their own way and are outside the tested rule. | Open |
| [D-21](#d-21) | A résumé run's recorded cost is its cost; stage latency is recorded per call. | Run cost is an account-wide before/after ledger difference (concurrent work inflates it: mean $0.187 vs $0.11 in attributable résumé calls);… | Open — measurement gap |
| [D-22](#d-22) | ORM models declare single-column natural keys. | The database enforces per-account keys (15 constraints re-scoped); the `account_id` column is in no model. | Open (model/schema drift) |
| [D-23](#d-23) | Headers in `career_switch.py` and `requirement_filter.py` say Jev costs $0. | Jev has been priced at $0.042 per million input tokens since 2026-10-14. | Open (comments) |
| [D-24](#d-24) | The 2026-07-08 Application layer described cover letters, executive biography, outreach, networking, application packages, promotion packets… | Of those, only résumés, interview preparation and opportunity analysis were built as products; cover letters exist only as drafted answers i… | Historical — superseded scope |
| [D-25](#d-25) | The résumé flow's own descriptions: the `recruiter_flow.py` module docstring says every section (the executive summary, each role's summary,… | Only bullets go through the four steps, and only bullets over 220 characters are tightened (A-91). Both summaries come from the positioning … | Open (documentation lag) |
| [D-26](#d-26) | The summary tests count toward the suite as tests of the résumé flow: `tests/resume/test_summary_tool.py` and the summary tests in `tests/re… | Most of them exercise the four-step summary branch of `recruiter_flow.section` and `summary_tool.write`, which no Live path has called since… | Open (test debt) |
| [D-27](#d-27) | The `model_assignments` seed names Claude Haiku for six stages added since 2026-10-25 (requirement division, application question, applicati… | The assignments document is created from the seed only where none exists and is "never republished from the seed file afterwards"; a seed ch… | Open (configuration: the seed and each database diverge by design) |
| [D-28](#d-28) | Product 03: governance is "the only path to any model, Jev, embedding, search or scrape call"; every such call writes a `model_execution` ro… | The GitHub portfolio reads GitHub's public API directly through `httpx` and writes no `model_execution` row; the capability `portfolio_read`… | Open (documentation and measurement gap) |
| [D-29](#d-29) | `docs/chat-read-access.md` on Live: career themes and major outcomes are kept apart by design at `/evidence/themes` and `/evidence/outcomes`… | On Live those pages, their models and that test don't exist (A-100); the document is Beta's, copied unchanged. | Open (documentation lag) |
| [D-30](#d-30) | Settings › Portfolio offers three uses for an approved repository, one of them "Career Navigator, for my preparation". | Nothing reads that level: such a repository's artifacts are read and stored but used nowhere. Only `sharing == "public"` is ever queried (A-… | Open — product gap |
| [D-31](#d-31) | CLAUDE.md: "Reviewers, editors and checks may detect and report a defect. Nothing may rely on them to repair it." | In the interview coach, approving a draft that the Jev line check reads as unsupported marks the draft stale and the coach writes it again (… | Open — design decision to record |
| [D-32](#d-32) | The coach's own descriptions: the capability registry labels coach routing (`coach_route`) as rules, "By the words of the message", and the … | `coach.mode` routes on Jev's readings of what the message means since `0018434` (A-66). The line check reads the cited claims' words against… | Open (documentation lag) |
| [D-33](#d-33) | Commit `0018434`: what a message means is "never matched against phrase lists"; code reads only "the app's own messages, dates, footnote num… | Word lists still read the person's words when a dispute must be pinned to one line: words for both or all, for first or second, for footnote… | Open (minor) |
| [D-34](#d-34) | The `JobStatement` docstring: the person's words are kept "for this opportunity and read again by its preparation"; the table has a `turn_id… | `turn_id` is never written (the only writer passes none), so a statement cannot be traced to its turn. The application chat reads stated rea… | Open (provenance gap and docstring lag) |
| [D-35](#d-35) | The opportunities pane's design (`05abced`): gap counts are kept so pages don't pay for counting (M-76). | Page renders call `job_gaps.counted` → `themes.group`, which embeds the gap texts and asks Jev about close pairs (paid calls) on an in-process cache miss. If … | Open (cost and consistency) |
| [D-36](#d-36) | The evidence chat reports, beside every proposal, any figure the person never said (K-25). | Offers made in the application chat are stored with no findings: the figure check is not run on them. Only the check that the named version … | Open (minor) |
| [D-37](#d-37) | `career_journey.py`: the journey is written from "every story of it a résumé may use (not retired, not flagged)". | It leaves out only stories the person flagged, not those the deterministic reading flags; the résumé flow leaves out both (K-17, A-86). | Open — defect |
| [D-38](#d-38) | Commit `61362ff` (closing the polish experiment): "the summary writer's changes stay on Beta, unpromoted". | Those summary-prompt changes are in Live's `resume_summary_tool_v1.md`: Live was rebuilt from Beta's commits by cherry-pick (P-37), and the … | Open (record lag) |
| [D-39](#d-39) | Starting a round preparation, Quick answers and the guided walkthrough are current interview features (A-52–A-54 in release 2026.10.0); thei… | Their only entry points were in the "Navigate the interview" card, which was removed on 2026-10-25 so the interview coach leads Interview Pr… | Open — product gap (keep, link again or retire) |

## Details

<a id="d-01"></a>
### D-01

- **Stated:** Seven comments and the server's own name say the ChatGPT (MCP) connector is "never on Live" / "Beta".
- **Actual:** The connector is mounted on Live: `MCP_ORIGINS` includes Live's origin and a test asserts Live works. A read-only probe on the host (2026-10-25) got 200 from the OAuth discovery endpoint and 401 from `/mcp`.
- **Evidence:** `app/config.py`, `app/web/main.py`, `app/mcp_beta/*`, `tests/mcp_beta/test_isolation.py`; commit `6c2723c` (2026-10-20, 23:01 PT). Comments unchanged at `79658ad`.
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
- **Actual:** 3,542 test functions in 230 files (static count at `00eac95`, [M-79](04-metric-ledger.md#m-79)); the importer shipped 2026-10-05; the optimizer was built the day it was backlogged; `docs/reliability/` does not exist.
- **Evidence:** Static count; commits `fb2caa7`, `cf27ec8`. `docs/` unchanged since 2026-10-24 apart from a new `docs/chat-read-access.md` ([D-29](#d-29)).
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
- **Actual:** The declaration is never checked in the recruiter flow (each call is recorded as one undivided part); the only enforcement is a substring guard, which no test exercises. A unit test of prompt construction does assert the requirements are absent. The summary writer added on 2026-10-28 has its own guard, which a test exercises; the bullet writer's still has none ([A-12](03-claim-index.md#a-12), [A-83](03-claim-index.md#a-83)).
- **Evidence:** `app/capabilities.py`; `app/context/packages.py`; `app/resume/recruiter_flow.py`; `tests/resume/test_recruiter_flow.py`; `app/resume/main_summary.py` (`written`, `role_written`); `tests/resume/test_main_summary.py` (`test_a_writer_message_carrying_a_requirement_is_refused`).
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
- **Actual:** Bullets are drafted as finished lines, and only a bullet longer than two printed lines gets a second, tightening call. Summaries are planned, restated in plain words, briefed and written once, never rewritten or replaced. Editor corrections still get a verify read. Fix (person-pressed) rewrites lines up to twice and re-reviews; a missing summary can be written on its own from a person-pressed button, without a new review. The rule is interpreted, not literal.
- **Evidence:** `CLAUDE.md`; `app/resume/recruiter_flow.py`; `app/resume/main_summary.py`; `app/resume/editor_review.py`; `app/resume/repair.py`; `app/operations.py` (`review.summary`); commits `77acb9c`, `ba6f332`, `62d4327`, `caa6460` ([A-11](03-claim-index.md#a-11), [A-84](03-claim-index.md#a-84), [A-90](03-claim-index.md#a-90)).
- **Status:** Open — design decision to record

<a id="d-10"></a>
### D-10

- **Stated:** Project rule: "Ranking, selecting, filtering and deciding a state are Jev's job."
- **Actual:** Language models still select or decide in six places: story selection for résumé bullets (by the owner's design of the recruiter-selects flow), the gap-panel "closes the gap" judgment, concept indexing, What's Next's fix kind deciding whether a shortfall counts as a gap, whether a posting line holds several asks (the owner's stated exception, 2026-10-27, [A-05](03-claim-index.md#a-05)), and an application question's kind (evidence, motivation, judgment, reflection or mixed), which code then uses to route the answer. The professional summary's stories are now classed by Jev first; the summary planner then chooses which of those each assertion cites.
- **Evidence:** `app/resume/recruiter_flow.py`; `app/evidence/guided_add.py`; `app/pipeline/ingestion.py`; `app/evidence/job_gaps.py`; `app/pipeline/requirement_division.py` (`a41a455`); `app/apply/assist.py`, `app/documents/seeds/application_question_v1.md`; `app/resume/main_summary.py` (`classified`, `ba6f332`).
- **Status:** Open — partly deliberate

<a id="d-11"></a>
### D-11

- **Stated:** Application facts are "current facts" about the person (eligibility, availability, logistics).
- **Actual:** The pattern also matches technical requirements such as high availability, on-call incident response and export-control compliance programs, which are then never sent to reviewers. A second classifier used by the assessment disagrees with it on several phrasings (remote teams, hybrid cloud, certification programs). Since 2026-10-27 the second classifier also decides which lines the résumé review counts as gaps, so the disagreement reaches the review page's gap count too.
- **Evidence:** `app/resume/requirement_kinds.py`; `app/pipeline/demand_index.py` (`is_structural`); `app/evidence/job_gaps.py` (`of_view`); `tests/jobs/test_not_this_postings_asks.py`; commit `728f903`.
- **Status:** Open — defect

<a id="d-12"></a>
### D-12

- **Stated:** The walkthrough docstring: its evidence is what "Jev chose".
- **Actual:** It reads the preparation's stored input, which holds the cosine candidate pool; Jev's chosen set is passed to the preparation call but never saved. Since 2026-10-25 no page links to the walkthrough ([D-39](#d-39)).
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
- **Actual:** Career Direction's role pages (the reading Tune my evidence used; the page itself was retired on 2026-10-30, [A-107](03-claim-index.md#a-107)) sum dated roles that Jev reads as that function; the two can disagree for the same person.
- **Evidence:** `app/evidence/requirement_parts.py`; `app/evidence/tune.py`; `app/web/tune.py` (`retired`); commit `a98124c`.
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
- **Actual:** The apply-kit answer drafts, the living résumé and the application chat label earlier text their own way and are outside the tested rule.
- **Evidence:** `app/context/provenance.py`; `app/apply/kit.py`; `app/career_conversation.py`; `app/apply/assist.py`; `app/documents/seeds/application_chat_v1.md`.
- **Status:** Open

<a id="d-21"></a>
### D-21

- **Stated:** A résumé run's recorded cost is its cost; stage latency is recorded per call.
- **Actual:** Run cost is an account-wide before/after ledger difference (concurrent work inflates it: mean $0.187 vs $0.11 in attributable résumé calls); per-call seconds are NULL for the writer, selector and reviewer stages, and for the summary calls added on 2026-10-28, whose step times are kept only in the run's phases. Interview-coach turns store no wall-clock seconds on the turn (the application chat stores them), and the application chat's rejections of a named version of what the person told (`stands_alone`) are only logged, so their rate cannot be measured.
- **Evidence:** `app/resume/pipeline.py`, `app/resume/drafting.py` (`_spend`); `app/resume/main_summary.py`; `app/journey/coach.py`; `app/apply/assist.py`; Live telemetry 2026-10-21..24 and 2026-10-31.
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
- **Actual:** Of those, only résumés, interview preparation and opportunity analysis were built as products; cover letters exist only as drafted answers inside Greenhouse apply kits; networking exists only as connections import and a message draft. Since then, application answers are also written in the application chat (2026-10-27), and Growth action plans (2026-10-30) suggest outcomes and milestones for stated limits; neither is a learning engine.
- **Evidence:** Predecessor `application/` documents; current code; `app/apply/assist.py`; `app/evidence/growth_plans.py`.
- **Status:** Historical — superseded scope

<a id="d-25"></a>
### D-25

- **Stated:** The résumé flow's own descriptions: the `recruiter_flow.py` module docstring says every section (the executive summary, each role's summary, each role's bullets) is written in the same four steps and "the writer tightens exactly what was kept"; the `main_summary.py` docstring says only the professional summary changes and the role summaries "stay the summary tool's", in three sentences of who, how they operate and how the career progressed; the capability registry (`summary_tool`), the context declaration (`resume_summary_tool`), the seed registration and the `test_main_summary.py` docstring and two test names say the summary is placed only when Jev supports every sentence, otherwise the summary tool's stays; the run trace says "the writer writes the summaries, then the bullets".
- **Actual:** Only bullets go through the four steps, and only bullets over 220 characters are tightened ([A-91](03-claim-index.md#a-91)). Both summaries come from the positioning tool ([A-82](03-claim-index.md#a-82), [A-85](03-claim-index.md#a-85)), in the parts who and the problems they solve, scope, current work, and are placed as written ([A-84](03-claim-index.md#a-84)); `summary_tool.write` has no caller; the tests check the `accepted` label. The bullets come first and the summaries are written beside them, with their counts in the enrichment phase.
- **Evidence:** `app/resume/recruiter_flow.py` (module docstring); `app/resume/main_summary.py` (docstring, `PARTS`); `app/capabilities.py` (`summary_tool`); `app/context/packages.py` (`resume_summary_tool`); `app/documents/seed.py`; `tests/resume/test_main_summary.py`; `app/models/resume_generation.py` (`RECRUITER_LABELS`); `app/web/templates/partials/resume_trace_rows.html`; commits `ba6f332`, `2ac4c41`, `62d4327`, `77acb9c`.
- **Status:** Open (documentation lag)

<a id="d-26"></a>
### D-26

- **Stated:** The summary tests count toward the suite as tests of the résumé flow: `tests/resume/test_summary_tool.py` and the summary tests in `tests/resume/test_recruiter_flow.py`.
- **Actual:** Most of them exercise the four-step summary branch of `recruiter_flow.section` and `summary_tool.write`, which no Live path has called since 2026-10-28 ([A-101](03-claim-index.md#a-101)). The suite's size overstates its coverage of live behavior.
- **Evidence:** `tests/resume/test_summary_tool.py`; `tests/resume/test_recruiter_flow.py` (`test_the_writer_sees_stories_and_its_own_draft_never_the_recruiter`, `test_a_tightened_summary_fits_the_readability_check_by_its_shape`); no caller of the summary kinds of `section()` or of `summary_tool.write` at `79658ad`.
- **Status:** Open (test debt)

<a id="d-27"></a>
### D-27

- **Stated:** The `model_assignments` seed names Claude Haiku for six stages added since 2026-10-25 (requirement division, application question, application chat, role understanding, Growth plan, Growth chat), and a test asserts Haiku for both Growth stages.
- **Actual:** The assignments document is created from the seed only where none exists and is "never republished from the seed file afterwards"; a seed change reaches an existing database only when someone sets it in Admin › Models. On Live the first calls of two new stages ran on gpt-5-mini before the assignment was set by hand: 1 of 20 application-chat calls and 2 of 21 requirement-division calls ([M-68](04-metric-ledger.md#m-68), [M-67](04-metric-ledger.md#m-67)). The résumé summaries and the career journey have no assignment and run on the default model, gpt-5-mini on Live. The Growth stages had no Live call by 2026-10-31, so their Live model is unverified; the test reads the seed, not the document in force.
- **Evidence:** `app/governance/models.py` (`ensure_seeded`); `app/documents/seeds/model_assignments_v1.md`; `experiments/application_chat_log.md` (the assignment "never reached the document in force"); `tests/evidence/test_growth_plans.py::test_the_policy_asks_for_evidence_and_small_milestones_and_both_calls_are_haiku`; read-only Live query 2026-10-31.
- **Status:** Open (configuration: the seed and each database diverge by design)

<a id="d-28"></a>
### D-28

- **Stated:** Product 03: governance is "the only path to any model, Jev, embedding, search or scrape call"; every such call writes a `model_execution` row ([P-03](03-claim-index.md#p-03)).
- **Actual:** The GitHub portfolio reads GitHub's public API directly through `httpx` and writes no `model_execution` row; the capability `portfolio_read` declares only the `embedding` stage. The reads are free and carry no credential. Discover's ATS reads, by contrast, are recorded as `job_board_fetch` ([P-36](03-claim-index.md#p-36)).
- **Evidence:** `app/portfolio.py` (`_get`); `app/capabilities.py` (`portfolio_read`); `app/discovery/fetch.py` (`STAGE`); Live telemetry 2026-10-31 (`job_board_fetch` rows present, no GitHub rows).
- **Status:** Open (documentation and measurement gap)

<a id="d-29"></a>
### D-29

- **Stated:** `docs/chat-read-access.md` on Live: career themes and major outcomes are kept apart by design at `/evidence/themes` and `/evidence/outcomes`, enforced by `tests/structural/test_evidence_backend_boundary.py`.
- **Actual:** On Live those pages, their models and that test don't exist ([A-100](03-claim-index.md#a-100)); the document is Beta's, copied unchanged.
- **Evidence:** `docs/chat-read-access.md`; `tests/structural/` holds only `test_authority_boundaries.py` at `79658ad`; commit `8edc02a`.
- **Status:** Open (documentation lag)

<a id="d-30"></a>
### D-30

- **Stated:** Settings › Portfolio offers three uses for an approved repository, one of them "Career Navigator, for my preparation".
- **Actual:** Nothing reads that level: such a repository's artifacts are read and stored but used nowhere. Only `sharing == "public"` is ever queried ([A-122](03-claim-index.md#a-122)).
- **Evidence:** `app/models/portfolio.py` (`SHARING`, `SHARING_LABEL`); `app/portfolio.py` (`served`).
- **Status:** Open — product gap

<a id="d-31"></a>
### D-31

- **Stated:** CLAUDE.md: "Reviewers, editors and checks may detect and report a defect. Nothing may rely on them to repair it."
- **Actual:** In the interview coach, approving a draft that the Jev line check reads as unsupported marks the draft stale and the coach writes it again ([A-64](03-claim-index.md#a-64)). The application chat, by contrast, only reports unsupported lines ([A-73](03-claim-index.md#a-73)).
- **Evidence:** `app/journey/coach.py` (`prepare`); `tests/journey/test_verified_answers.py::test_approving_an_answer_with_an_untraced_line_rewrites_it`; commit `c91793c` (2026-10-25).
- **Status:** Open — design decision to record

<a id="d-32"></a>
### D-32

- **Stated:** The coach's own descriptions: the capability registry labels coach routing (`coach_route`) as rules, "By the words of the message", and the `coach.mode` docstring says "by code"; `UNGOVERNED_STAGES["interview_coach_line"]` says Jev is asked "about one posting line and one line of a draft"; the `heard.py` docstring gives readings for two calibration messages; the `rounds.py` docstring says "Reading their words is code's".
- **Actual:** `coach.mode` routes on Jev's readings of what the message means since `0018434` ([A-66](03-claim-index.md#a-66)). The line check reads the cited claims' words against the draft line (and, for reason lines, whether it is a fair inference); no posting line is read. The calibration readings in the commit and the test's fixed data differ from the docstring's ([M-73](04-metric-ledger.md#m-73)). In rounds, an interview's outcome and the next interview's kind are Jev's readings, dates are code's, and who the next interview is with is the coaching model's reading, shown on the card for Save.
- **Evidence:** `app/capabilities.py` (`coach_route`); `app/journey/coach.py` (`mode`); `app/governance/execution.py`; `app/journey/heard.py`; `app/journey/rounds.py`; commits `0018434`, `291517d`, `a81cf41`.
- **Status:** Open (documentation lag)

<a id="d-33"></a>
### D-33

- **Stated:** Commit `0018434`: what a message means is "never matched against phrase lists"; code reads only "the app's own messages, dates, footnote numbers, the question mark".
- **Actual:** Word lists still read the person's words when a dispute must be pinned to one line: words for both or all, for first or second, for footnote, line, sentence or claim, overlap with a role's name, and "previous" or "latest" message or draft.
- **Evidence:** `app/journey/coach.py` (`_BOTH`, `_PICK`, `_POINTS`, `_chosen_option`); `app/journey/answer.py` (`_WHICH`).
- **Status:** Open (minor)

<a id="d-34"></a>
### D-34

- **Stated:** The `JobStatement` docstring: the person's words are kept "for this opportunity and read again by its preparation"; the table has a `turn_id` column.
- **Actual:** `turn_id` is never written (the only writer passes none), so a statement cannot be traced to its turn. The application chat reads stated reasons from every opportunity, not only this one (deliberate, `7518723`), which the docstring does not say ([A-70](03-claim-index.md#a-70)).
- **Evidence:** `app/models/journey.py` (`JobStatement`); `app/evidence/chat.py` (the call to `keep_words`); `app/apply/assist.py`; commits `05b0624`, `7518723`.
- **Status:** Open (provenance gap and docstring lag)

<a id="d-35"></a>
### D-35

- **Stated:** The opportunities pane's design (`05abced`): gap counts are kept so pages don't pay for counting ([M-76](04-metric-ledger.md#m-76)).
- **Actual:** Page renders call `job_gaps.counted` → `themes.group`, which embeds the gap texts and asks Jev about close pairs not already answered (paid `embedding` and Jev calls) on an in-process cache miss. If the grouping fails it is logged and each requirement counts as its own gap, so the page can show a different count from the chat without saying why ([A-78](03-claim-index.md#a-78)).
- **Evidence:** `app/evidence/job_gaps.py`; `app/evidence/themes.py`; `app/journey/standing.py`; commits `05abced`, `798fbf9`.
- **Status:** Open (cost and consistency)

<a id="d-36"></a>
### D-36

- **Stated:** The evidence chat reports, beside every proposal, any figure the person never said ([K-25](03-claim-index.md#k-25)).
- **Actual:** Offers made in the application chat are stored with no findings: the figure check is not run on them. Only the check that the named version keeps every word they said guards the text ([A-75](03-claim-index.md#a-75)). The interview coach's offers do get the figure check.
- **Evidence:** `app/apply/assist.py` (`_stored`, `stands_alone`); `app/evidence/chat.py` (`check`).
- **Status:** Open (minor)

<a id="d-37"></a>
### D-37

- **Stated:** `career_journey.py`: the journey is written from "every story of it a résumé may use (not retired, not flagged)".
- **Actual:** It leaves out only stories the person flagged, not those the deterministic reading flags; the résumé flow leaves out both ([K-17](03-claim-index.md#k-17), [A-86](03-claim-index.md#a-86)).
- **Evidence:** `app/evidence/career_journey.py` (`roles`); `app/evidence/instance_gap.py` (`is_flagged`).
- **Status:** Open — defect

<a id="d-38"></a>
### D-38

- **Stated:** Commit `61362ff` (closing the polish experiment): "the summary writer's changes stay on Beta, unpromoted".
- **Actual:** Those summary-prompt changes are in Live's `resume_summary_tool_v1.md`: Live was rebuilt from Beta's commits by cherry-pick ([P-37](03-claim-index.md#p-37)), and the seed is identical on Live `79658ad` and Beta. The prompt was rewritten again by `7411d3f` and `77acb9c`.
- **Evidence:** `app/documents/seeds/resume_summary_tool_v1.md` (identical at Live `79658ad` and Beta `c1befd7`); commits `61362ff`, `7411d3f`, `77acb9c`.
- **Status:** Open (record lag)

<a id="d-39"></a>
### D-39

- **Stated:** Starting a round preparation, Quick answers and the guided walkthrough are current interview features ([A-52](03-claim-index.md#a-52)–[A-54](03-claim-index.md#a-54) in release 2026.10.0); their routes are still served, and Quick answers is still listed among the page's children.
- **Actual:** Their only entry points were in the "Navigate the interview" card, which was removed on 2026-10-25 so the interview coach leads Interview Prep ([A-71](03-claim-index.md#a-71)). No page posts to or links to them, except the quick-answer chat's own way back. An earlier preparation still shows.
- **Evidence:** `app/web/templates/journey.html`; `app/web/journey.py`; `app/web/walkthrough.py`; `app/web/nav.py` (`CHILDREN`); commit `2c05495`.
- **Status:** Open — product gap (keep, link again or retire)
