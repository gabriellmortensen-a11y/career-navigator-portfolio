# Product — how the system thinks and operates

**Section version: Product 4.0** (2026-10-25) · supersedes the Product layer v3.0 (2026-07-08) ·
describes Live `7322289` (2026-10-24) · see [COMPATIBILITY](../COMPATIBILITY.md)

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

## What changed since Product 3.0

Product layer 3.0 (2026-07-08) was a vision and operating model written **before** any of the
software existed. It had 18 documents covering vision, principles, philosophy, engines, CareerOS,
workflows, AI reasoning, a PRFAQ, roadmap, ADRs, an incubation library, a decision log, a research
backlog and a glossary.

| 3.0 said | 4.0 records |
|---|---|
| "Most AI career products optimize generation. Career Navigator optimizes discovery." | Still the thesis. Discovery is now concrete: Chart My Course, gap conversations and Tune my evidence ([Applications](../applications/00-README.md)) |
| Five engines: Discovery, Knowledge, Learning, Reasoning, Navigation | Discovery, Knowledge and Reasoning exist as implemented capabilities. A **Learning engine** and the **Persona system** were never built ([D-24](../evidence/05-discrepancies.md#d-24)) |
| Verified evidence before any reasoning | Enforced by a single writer and the database ([Knowledge 02](../knowledge/02-admission-and-acceptance.md)) |
| Principles as aspirations | Principles as rules, each with the failure that created it and its named exceptions ([Product 02](02-principles.md)) |
| No operations, cost or measurement model | Governed model calls, a cost ledger, a release process, measured calibration and named measurement gaps (04–06) |
