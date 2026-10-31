# Where to inspect the work

*An index of this portfolio by kind of artifact. The linked documents describe Live `7322289`
(2026-10-24) unless they say otherwise.*

Each entry links to the exact file, section or anchor and says in one line what it shows. This page
adds nothing of its own: every number and status lives in [evidence/](evidence/00-README.md)
([one home per topic](COMPATIBILITY.md#one-home-per-topic)). The application's source is private;
the linked documents cite the file, test or commit each claim rests on
([how to read a citation](evidence/00-README.md)).

**Sections:** [Product overview](#product-overview) · [Architecture](#architecture) ·
[Decisions](#decisions) · [Security and authorization](#security-and-authorization) ·
[Testing and verification](#testing-and-verification) · [Observability](#observability) ·
[Integrations](#integrations) · [Case studies](#case-studies) ·
[Claims, metrics and discrepancies](#claims-metrics-and-discrepancies) · [Releases](#releases) ·
[Examples](#examples) · [Authorship](#authorship)

## Product overview

| Where | What it shows |
|---|---|
| [README → What works today](README.md#what-works-today) | Each capability on Live, what it means for the person, and its status |
| [Product 01 — Problem, users and my role](product/01-problem-users-and-role.md) | The problem, who it serves, why existing tools didn't fit, and who did what |
| [Product 02 — Principles](product/02-principles.md) | Eleven rules the system follows, the failure each came from, how each is enforced, and named exceptions |
| [Knowledge](knowledge/00-README.md) · [Product](product/00-README.md) · [Applications](applications/00-README.md) | The three versioned sections, each with a table of its documents and what changed since the earlier layer |
| [GLOSSARY](GLOSSARY.md) | Plain-language definitions of the terms used throughout |

## Architecture

| Where | What it shows |
|---|---|
| [Product 03 — System architecture](product/03-system-architecture.md) | The narrative: components, the four kinds of work, authority boundaries, external services, and where the architecture came from |
| [Architecture 00 — Index and legend](architecture/00-README.md) | The diagram list and the one legend: deterministic code, Jev, language-model call, human decision, persistence, external service |
| [Architecture 01 — Components and boundaries](architecture/01-components.md) | Processes, modules, the governed model boundary, the database and external services, plus a table of the boundaries the diagram encodes |
| [Architecture 02 — Evidence admission and acceptance](architecture/02-evidence-admission.md) | Every path into the career record and who decides |
| [Architecture 03 — Requirement analysis and evidence matching](architecture/03-requirement-analysis-and-matching.md) | Posting → requirements → stories → assessment, with no language model |
| [Architecture 04 — Résumé planning, writing and review](architecture/04-resume-flow.md) | What each stage sees; where the job's requirement text goes and where it never goes |
| [Architecture 05 — Discovery through application tracking](architecture/05-discovery-to-tracking.md) | Search → screen → assess → write → kit → fill → submit → status |
| [Architecture 06 — Measurement and feedback](architecture/06-measurement-and-feedback.md) | Call ledger, observability, model check, calibration, release loop |
| [Architecture 07 — Historical and planned](architecture/07-historical-and-planned.md) | Earlier generations (not current) and planned work (not built), kept apart |
| [Rendered diagrams](assets/diagrams/README.md) | SVG copies for viewers that don't render Mermaid; the Mermaid source in `architecture/` is authoritative |

## Decisions

| Where | What it shows |
|---|---|
| [Product 07 — Decision log](product/07-decision-log.md) | 36 dated decisions, `DEC-01` to `DEC-36`, each with its trigger and what it replaced. Every row has its own anchor, for example [`#dec-01`](product/07-decision-log.md#dec-01) |
| [Decision log → Before the baseline](product/07-decision-log.md#before-the-baseline-earlier-build-summarised) | DEC-01 to DEC-07: decisions from the earlier build that the current design rests on |
| [Decision log → Since the baseline](product/07-decision-log.md#since-the-baseline) | DEC-08 to DEC-36: decisions from 2026-10-02 to 2026-10-24 |
| [Decision log → Decisions still open](product/07-decision-log.md#decisions-still-open) | Four decisions recorded as open, not inferred |
| [EVOLUTION](EVOLUTION.md) | How the design got from the July 2026 layer documents to the current application |

**Owner decisions.** The log states that decisions not marked "owner" were proposed by the
implementing agent and accepted by me. Rows that open with **Owner:** are mine:
[DEC-04](product/07-decision-log.md#dec-04), [DEC-06](product/07-decision-log.md#dec-06),
[DEC-07](product/07-decision-log.md#dec-07), [DEC-08](product/07-decision-log.md#dec-08),
[DEC-16](product/07-decision-log.md#dec-16), [DEC-17](product/07-decision-log.md#dec-17),
[DEC-18](product/07-decision-log.md#dec-18), [DEC-20](product/07-decision-log.md#dec-20),
[DEC-21](product/07-decision-log.md#dec-21), [DEC-22](product/07-decision-log.md#dec-22),
[DEC-23](product/07-decision-log.md#dec-23), [DEC-26](product/07-decision-log.md#dec-26),
[DEC-28](product/07-decision-log.md#dec-28), [DEC-29](product/07-decision-log.md#dec-29),
[DEC-30](product/07-decision-log.md#dec-30), [DEC-31](product/07-decision-log.md#dec-31) and
[DEC-32](product/07-decision-log.md#dec-32). Two more rows quote my words inside the decision
([DEC-33](product/07-decision-log.md#dec-33), [DEC-35](product/07-decision-log.md#dec-35)), and
[DEC-36](product/07-decision-log.md#dec-36) was triggered in part by a near-duplicate bullet I spotted.

## Security and authorization

| Where | What it shows |
|---|---|
| [Product 03 → Two authority boundaries](product/03-system-architecture.md#two-authority-boundaries-enforced-by-the-database) | A job owns its demand universe and a role owns what may compose, both enforced by the database; forced row-level security on every non-shared table, with a runtime role that owns nothing |
| [Product 06 → Tenancy and privacy](product/06-operations-and-privacy.md#tenancy-and-privacy) | Separation between accounts enforced by the database, not by queries, and how prompts, model outputs, search queries, shared links, the ChatGPT connector, API keys and a person's own data are handled |
| [Architecture 01 → Boundaries the diagram encodes](architecture/01-components.md#boundaries-the-diagram-encodes) | Six boundaries, what enforces each, and the claim behind it |
| [Knowledge 02 — Admission and acceptance](knowledge/02-admission-and-acceptance.md) | Who may change the career record: proposal vs record, the single writer, every way in, and where the implementation and the rule still disagree |
| [Product 06 → Incidents and what changed](product/06-operations-and-privacy.md#incidents-and-what-changed) | Incidents, including the 2026-10-05 data loss, and the change made at the source for each |
| [D-02](evidence/05-discrepancies.md#d-02), [D-17](evidence/05-discrepancies.md#d-17) | Two open security and privacy findings, listed with their details withheld until fixed |

## Testing and verification

| Where | What it shows |
|---|---|
| [Case study 06 → Verification](case-studies/06-operating-the-human-agent-loop.md#verification) | Live deploys only from approved commits, deploys that back up and roll back, contract tests that pin the rules, and the last recorded full test run |
| [Product 06 → Release process](product/06-operations-and-privacy.md#release-process) and [Deploy](product/06-operations-and-privacy.md#deploy) | The release gate (full suite, Beta, the owner's use on Beta, Live) and each deploy step, with the deploy script's stated limits |
| [M-30 — Test suite](evidence/04-metric-ledger.md#m-30) | 209 test files and 3,167 test functions (static count); last recorded full run 3,135 passed, 0 failed, 141 skipped, with the limits of those figures |
| [M-49 — Test suite at extraction](evidence/04-metric-ledger.md#m-49) | 117 contracts on the extracted application's first day vs 10,541 in the earlier build |
| [M-48 — Legacy release suite](evidence/04-metric-ledger.md#m-48) | The earlier build's last release suite: 9,453 passed, 27 failed, each failure classified (historical) |
| [Evidence 03 — Claim index](evidence/03-claim-index.md) | Each claim's "Evidence" and "How verified" columns: the code, tests, commits or records it rests on, and how it was checked |
| [Product 05 — Quality and measurement](product/05-quality-and-measurement.md) | What is measured and against what, the controlled experiments that changed the design, and [what is not measured](product/05-quality-and-measurement.md#what-is-not-measured) |
| [Case study 03 → Verification](case-studies/03-evaluation-quality-latency-cost.md#verification-guarding-against-measuring-noise) | Guarding against measuring noise: an optimizer's acceptance reversed when evaluator variance exceeded the improvement |
| [Evidence 06 — Verification log](evidence/06-verification-log.md) | How this portfolio's evidence was gathered and checked: code and history, read-only Live telemetry, the career-evidence file, publication checks, an independent review, publication decisions, and what was not done |
| [Evidence 06 → Independent review](evidence/06-verification-log.md#5-independent-review-before-release) | A separate agent's review before release, and the factual errors, overclaims and unsourced numbers it found, all corrected |
| [Evidence 06 → Publication checks](evidence/06-verification-log.md#4-publication-checks-for-this-release) and [`tools/check.sh`](tools/check.sh) | The checks a release runs: links and anchors, Mermaid rendering, sensitive content and private terms, the career-evidence import shape, empty files |

## Observability

| Where | What it shows |
|---|---|
| [Product 06 → Monitoring](product/06-operations-and-privacy.md#monitoring) | Spend and failures by day, stage, model and account; alerts every 15 minutes; request logs with request and account ids; `/healthz` |
| [Architecture 06 — Measurement and feedback](architecture/06-measurement-and-feedback.md) | Every call recorded in one ledger, the readers built on it, the model-check and calibration loops, the release loop, and the gaps the diagram makes visible |
| [Product 04 — Model routing, cost and latency](product/04-model-routing-cost-latency.md) | Which model does what and why, [measured costs from Live telemetry](product/04-model-routing-cost-latency.md#what-things-cost-live-telemetry), latency, cost controls and their limits, and known measurement gaps |

## Integrations

| Where | What it shows |
|---|---|
| [Applications 06 → ChatGPT connector (MCP)](applications/06-sharing-and-integrations.md#chatgpt-connector-mcp) | OAuth 2.1 with PKCE, eight read-only tools under row-level security, a rate limit, and an audit that never keeps arguments or answers; its Live status stated precisely ([D-01](evidence/05-discrepancies.md#d-01)) |
| [Applications 06 → Share my career conversation](applications/06-sharing-and-integrations.md#share-my-career-conversation) | A public link, draft until activated, that answers only from what the owner chose to share |
| [Applications 04 → Apply kit and browser extension](applications/04-discovery-to-application.md#3-apply-kit-and-browser-extension) | Greenhouse questions read from the public endpoint, code deciding each question's source, and an extension that fills forms and never submits |
| [Product 03 → External services](product/03-system-architecture.md#external-services) | Each outside service, what it is used for, and its boundary |

## Case studies

Each case study covers the problem, my ownership, constraints, alternatives, the decision,
implementation, verification, results and limitations, and what changed after learning from use
([index](case-studies/00-README.md)).

| Case study | Best for |
|---|---|
| [01 — Building a governed career evidence system](case-studies/01-governed-career-evidence.md) | Product judgment on trust; data architecture |
| [02 — Preventing unsupported claims in tailored résumés](case-studies/02-preventing-unsupported-claims.md) | AI product design; technical depth |
| [03 — Making evaluation trustworthy, fast and cheap](case-studies/03-evaluation-quality-latency-cost.md) | Quality, cost and latency trade-offs |
| [04 — Connecting job discovery to application execution](case-studies/04-connecting-discovery-to-application.md) | End-to-end workflow; automation boundaries |
| [05 — Designing gap conversations that produce useful evidence](case-studies/05-gap-conversations-that-produce-evidence.md) | Conversational UX with integrity constraints |
| [06 — Operating a product with an implementation agent](case-studies/06-operating-the-human-agent-loop.md) | TPM / delivery; working with AI coding agents |

## Claims, metrics and discrepancies

| Where | What it shows |
|---|---|
| [Evidence 03 — Claim index](evidence/03-claim-index.md) | 116 claims with status, evidence and how each was verified; each has an anchor by ID, for example [`#k-01`](evidence/03-claim-index.md#k-01) |
| [Evidence 04 — Metric ledger](evidence/04-metric-ledger.md) | Every published number with its definition, sample, period, source, kind, system state and limits; an [index](evidence/04-metric-ledger.md#index) and an anchor per entry, for example [`#m-01`](evidence/04-metric-ledger.md#m-01) |
| [Evidence 05 — Discrepancies](evidence/05-discrepancies.md) | 24 places where documents, comments or rules disagree with the code at Live `7322289`, for example [`#d-01`](evidence/05-discrepancies.md#d-01) |
| [Evidence 01 — Baseline](evidence/01-baseline.md) | The earlier retrospective, which commit it describes, how this portfolio uses it, and its limitations |
| [Evidence 02 — Source inventory](evidence/02-source-inventory.md) | Every source, how it was accessed, what rests on it, and what was deliberately not used |
| [Evidence 00 — How to read a citation](evidence/00-README.md) | ID prefixes (`K-`, `P-`, `A-`, `H-` claims; `M-` metrics; `D-` discrepancies) and what file paths and hashes refer to |

## Releases

| Where | What it shows |
|---|---|
| [CHANGELOG](CHANGELOG.md) | Each portfolio release: what it pins, what was added, and what was verified for it |
| [COMPATIBILITY → Versions](COMPATIBILITY.md#versions) | Calendar-versioned portfolio releases, the section versions and application commit each pins, and the version rules |
| [COMPATIBILITY → Status vocabulary](COMPATIBILITY.md#status-vocabulary) | What *Verified*, *Limited*, *Experimental*, *Planned* and *Superseded* mean, and the minimum evidence for each |
| [ROADMAP](ROADMAP.md) | Future work, kept apart from the description of the current system |

## Examples

| Where | What it shows |
|---|---|
| [Examples index](assets/examples/README.md) | Every example is verbatim system text with no personal data, aggregate telemetry, or synthetic; and why there are no screenshots |
| [resume-flow-prompts.md](assets/examples/resume-flow-prompts.md) | Verbatim governed policy text: the selector answers with numbers only, the writer's template has no slot for requirements, bullets carry their story number |
| [model-assignment-excerpt.md](assets/examples/model-assignment-excerpt.md) | Model routing as a versioned document, each choice with its evidence and sample size |
| [resume-run-phases.json](assets/examples/resume-run-phases.json) | Per-phase cost, time and calls of a résumé run (aggregate Live telemetry, 32 runs, one account) |
| [synthetic-evidence-walkthrough.md](assets/examples/synthetic-evidence-walkthrough.md) | One requirement from evidence entry to an attributed bullet, with an invented person and posting, and what would or would not be caught |
| [career-evidence/](career-evidence/README.md) | The portfolio's learnings as an importable career-evidence file: 39 statements under one role, each derived from claims and metrics here |

## Authorship

I'm the product owner, and I wrote none of the code. I identified the problems, defined behavior
and constraints, challenged designs, tested the product on a real job search, chose experiments,
accepted or reverted changes, and ran the release gate. Claude Code agents proposed designs,
implemented changes, wrote the code and tests, and ran investigations and measurements. In the
decision log, decisions marked "owner" are mine and the rest were proposed by the implementing
agent and accepted by me ([see above](#decisions)). The commit history is consistent with this
split but can't prove who typed what
([Product 01 → My role](product/01-problem-users-and-role.md#my-role),
[M-31](evidence/04-metric-ledger.md#m-31)). The investigations behind this portfolio were run by
Claude Code agents at my direction ([Evidence 06](evidence/06-verification-log.md)).
