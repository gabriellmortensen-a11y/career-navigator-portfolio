# Product — how the system thinks and operates

**Section version: Product 4.1** (2026-10-31) · supersedes Product 4.0 (2026-10-25) and the Product
layer v3.0 (2026-07-08) · describes Live `00eac95` (2026-10-31) · see [COMPATIBILITY](../COMPATIBILITY.md)

The Product section answers: **why does Career Navigator exist, how should it decide, and how is it
run?** It owns the principles every other section must obey, the system architecture, model routing,
measurement and operations.

| # | Document | Answers |
|---|---|---|
| 01 | [Problem, users and my role](01-problem-users-and-role.md) | What problem, for whom, and who did what |
| 02 | [Principles](02-principles.md) | The rules the system follows, the failures they came from, and their named exceptions |
| 03 | [System architecture](03-system-architecture.md) | Components, boundaries, the four kinds of work, external services |
| 04 | [Model routing, cost and latency](04-model-routing-cost-latency.md) | Which model does what and why; what it costs; how long it takes |
| 05 | [Quality and measurement](05-quality-and-measurement.md) | What is measured, against what, and what is not measured |
| 06 | [Operations and privacy](06-operations-and-privacy.md) | Release process, deploy, background work, tenancy, privacy findings |
| 07 | [Decision log](07-decision-log.md) | Dated decisions, their triggers and what they replaced |

## What changed since Product 4.0

Product 4.1 adds content and corrects statements that became false. No principle was added or
removed; two have new named exceptions.

| Area | 4.0 (2026-10-25) said | 4.1 (2026-10-31) records |
|---|---|---|
| Beta and Live | Both run the same code; only the labs differ | Since 2026-10-28 Live is its own line, rebuilt from Beta's commits by cherry-pick, with its own migration copies and without three Beta-only evidence features ([P-37](../evidence/03-claim-index.md#p-37), [DEC-50](07-decision-log.md#dec-50)) |
| Assessment | No language model in Chart My Course | One stated exception, chosen by me: one small call reads a requirement line that lists several asks ([A-05](../evidence/03-claim-index.md#a-05), [DEC-47](07-decision-log.md#dec-47)) |
| Jev | Ranks, selects and decides states in assessment, discovery, interview evidence and de-duplication | Also reads what a coaching message means, picks the claims an interview or application answer may use, checks each draft line, routes Career Chat's reads and suggests portfolio links ([Product 02 §4](02-principles.md#4-jev-selects-models-reason-and-write)) |
| Writing passes | A draft and a tighten call per section | Bullets are drafted as finished lines; only a bullet past two printed lines gets a second call. Summaries are written once from a positioning brief, and a missing one can be written on a person's press after review ([Product 02 §5](02-principles.md#5-one-writer-pass-one-editor-pass-no-loops)) |
| Components | 45 capabilities in 6 flows | 66 capabilities in 9 flows; new: the interview coach, the application chat, Career Chat's read layer, Growth plans, the GitHub portfolio ([Product 03](03-system-architecture.md)) |
| Outside services | OpenAI, Anthropic, Jev, Tavily, Apify, ATS public APIs | Also GitHub's public API, read without credentials and outside the recorded call boundary ([P-36](../evidence/03-claim-index.md#p-36)) |
| Cost and time | A résumé ≈ $0.11 in model calls; median 207 s | A new, separate state after the 2026-10-29 speed route, side by side with the old one, not a trend ([M-60](../evidence/04-metric-ledger.md#m-60)) |

## What changed since Product 3.0

Product layer 3.0 (2026-07-08) was a vision and operating model written **before** any of the
software existed. It had 18 documents covering vision, principles, philosophy, engines, CareerOS,
workflows, AI reasoning, a PRFAQ, roadmap, ADRs, an incubation library, a decision log, a research
backlog and a glossary.

| 3.0 said | 4.0 records |
|---|---|
| "Most AI career products optimize generation. Career Navigator optimizes discovery." | Still the thesis. Discovery is now concrete: Chart My Course, gap conversations and the interview coach ([Applications](../applications/00-README.md)). (4.0 also named *Tune my evidence*, retired on 2026-10-30: [A-107](../evidence/03-claim-index.md#a-107).) |
| Five engines: Discovery, Knowledge, Learning, Reasoning, Navigation | Discovery, Knowledge and Reasoning exist as implemented capabilities. A **Learning engine** and the **Persona system** were never built ([D-24](../evidence/05-discrepancies.md#d-24)) |
| Verified evidence before any reasoning | Enforced by a single writer and the database ([Knowledge 02](../knowledge/02-admission-and-acceptance.md)) |
| Principles as aspirations | Principles as rules, each with the failure that created it and its named exceptions ([Product 02](02-principles.md)) |
| No operations, cost or measurement model | Governed model calls, a cost ledger, a release process, measured calibration and named measurement gaps (04–06) |
