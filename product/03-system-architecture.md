# Product 03 — System architecture

*Product 4.1 · describes Live `00eac95` (2026-10-31) · diagrams in [architecture/](../architecture/00-README.md)*

## Shape of the system

Career Navigator is one Python web application (FastAPI with server-rendered pages) backed by one
PostgreSQL database per environment. A separate background runner process handles the slow work. It
runs on a single small Linux host that serves **Beta** and **Live** as two services, each with its
own database ([P-11](../evidence/03-claim-index.md#p-11)).

**Beta and Live are no longer the same code.** From 2026-10-21 to 10-27 they were: one code base,
schema and set of documents, with only the experimental labs different. On 2026-10-28 I decided:
"Leave the evidence timeline, career themes, and major outcomes off of live." (my words, `88123b4`;
[DEC-50](07-decision-log.md#dec-50)). Since then Live is deployed from its own branch, rebuilt from Beta's commits by
cherry-pick. A migration whose parent exists only on Beta goes to Live as its own copy, after Live's
head ([P-37](../evidence/03-claim-index.md#p-37)). Every feature reached Beta first; Live adds its own migration copies
and adaptations ([P-11](../evidence/03-claim-index.md#p-11), [P-37](../evidence/03-claim-index.md#p-37)).

```text
browser ──► web process (enqueue only) ──► background_operation rows ──► runner process (niced)
   │              │                                                         │
   │              └── PostgreSQL (row-level security, one DB per env) ◄─────┘
   │                                                                       │
Chrome extension (fills forms, never submits)          external services: OpenAI, Anthropic,
Navi rail (the chat beside every page)                 Jev, Tavily, Apify, ATS public APIs,
                                                       GitHub public API
```

The component diagram with every boundary is [Architecture 01](../architecture/01-components.md).

## Components and what each owns

| Component | Owns | Never does |
|---|---|---|
| **Career record** (`app/evidence`, `app/authority`) | Roles, sources, claims, stories; the Change Document writer | Accept a write that is not a Change Document; let two roles share a row |
| **Job intake and analysis** (`app/pipeline`) | Reading postings, requirement sifting and rewording, fingerprints, story retrieval and Jev reading, the assessment; since 2026-10-27 dividing a line that lists several asks, and applying a gap's saved story to its job at Save ([A-81](../evidence/03-claim-index.md#a-81)) | Call a language model, except the one stated exception: one call per line that looks like several asks, at Chart My Course ([A-05](../evidence/03-claim-index.md#a-05)) |
| **Gap conversations and Growth** (`app/evidence/chat`, `discovery`, `job_gaps`, `themes`, `growth_areas`, `growth_plans`, `growth_chat`) | Asking about gaps, deciding stops in code, proposing one consolidated addition; Growth action plans and Navi on Growth ([A-109](../evidence/03-claim-index.md#a-109), [A-110](../evidence/03-claim-index.md#a-110)) | Save without a person's press and a role the person confirmed |
| **Career Chat reads** (`app/reads`, since 2026-10-28) | 14 read-only operations Jev routes and code runs, with counts and whose each record is ([A-102](../evidence/03-claim-index.md#a-102)) | Write anything; read what is listed as never read ([P-33](../evidence/03-claim-index.md#p-33)) |
| **Résumé** (`app/resume`) | Selection, the recruiter-selects bullet flow, professional and role summaries from a positioning brief (`main_summary`), page fit, reviews, editor, Fix, writing a missing summary, person edits, citations re-read for changed lines (`line_citations`) | Show the bullet writer the requirements, or the summary writers the posting; loop writer ↔ reviewer |
| **Discovery and apply** (`app/discovery`, `app/apply`, `extension/`) | Searching sources, screening, queues, kits, questions the person adds by hand, the application chat (`app/apply/assist.py`, [A-73](../evidence/03-claim-index.md#a-73)), browser fill | Submit an application; use a credential or work around a refusal |
| **Journey** (`app/journey`) | Statuses, activity, company research, the interview coach (`coach`, `answer`, `heard`, `role_model`, `rounds`), the Upcoming card (`upcoming`), opportunity labels (`standing`), Change Course, work fit | Treat an earlier conclusion as evidence |
| **Sharing and integrations** (`app/sharing`, `app/career_conversation.py`, `app/portfolio.py`, `app/mcp_beta`) | The living résumé (public links, scoped by the owner); the GitHub portfolio behind it ([A-120](../evidence/03-claim-index.md#a-120)); read-only ChatGPT connector | Write to the record; read outside the owner's chosen scope; treat a portfolio artifact as evidence ([K-34](../evidence/03-claim-index.md#k-34)) |
| **Governance** (`app/governance`, `app/documents`) | The only path to any model, Jev, embedding, search or scrape call; governed policy documents; model assignments; cost. Plain public reads (ATS boards, GitHub) go around it: ATS reads are recorded, GitHub reads are not ([P-36](../evidence/03-claim-index.md#p-36), [D-28](../evidence/05-discrepancies.md#d-28)) | Call an unpriced model, fall back silently, or run an undeclared stage ([P-01](../evidence/03-claim-index.md#p-01)) |
| **Operations** (`app/operations`, `scripts/deploy.sh`) | Durable background work, the runner, deploy with backup, drain and rollback; new kinds of work for a missing summary, a portfolio refresh, Growth suggestions and opportunity labels | Lose accepted work on restart ([P-09](../evidence/03-claim-index.md#p-09)) |
| **Navi rail** (`app/static/rail.js`, `_base.html`) | The chat beside or over every page, opened by a tab for that page's own chat ([A-105](../evidence/03-claim-index.md#a-105), [A-106](../evidence/03-claim-index.md#a-106)) | Send anything just by opening |
| **Observability** (`app/observability`, `app/capabilities`) | Spend, failures, flow charts, assessment-vs-review | Show career text ([P-13](../evidence/03-claim-index.md#p-13)) |

## Four kinds of work, kept distinct

Every step is one of these four kinds. The diagrams mark which kind each step is.

1. **Deterministic code**: parsing, rules, thresholds, fingerprints, gates, page fit.
2. **Jev questions**: a probability model asked fixed, typed questions ("does this sentence
   establish this requirement?"). Used to rank, select, filter and decide states. About $0.042 per
   million input tokens.
3. **Language-model calls**: writing and reasoning. These are the selector and writer of the résumé
   flow, the summary planner and writers, the career journey, the chat and the interview coach, the
   role reading, the application question reader and writer, Growth plans and Navi on Growth, the
   living résumé, the research brief, the reviewers and the editor. Each runs under a governed,
   versioned policy document. Two of them classify rather than write: the reading of a line that
   lists several asks, and an application question's kind ([D-10](../evidence/05-discrepancies.md#d-10)).
4. **Human decisions**: approving evidence, picking a role, pressing Write, accepting a kit answer,
   submitting the application.

The capability registry declares 66 capabilities in 9 flows (45 in 6 at Product 4.0). The new flows
are the interview coach, help preparing an application, and Growth plans; the share flow is now the
living résumé. Each capability declares its owner function, the stages it records and its gate.
Tests check every declaration against the code ([P-06](../evidence/03-claim-index.md#p-06)). Some declarations still describe
the code before it changed ([D-25](../evidence/05-discrepancies.md#d-25), [D-32](../evidence/05-discrepancies.md#d-32)).

| Kind | Capabilities |
|---|---:|
| Code rules | 23 |
| Jev | 19 |
| Language model | 18 |
| Embeddings | 4 |
| Outside service | 2 |

## Two authority boundaries, enforced by the database

1. **A job owns its demand universe.** The chain is job → requirements → fingerprint → index →
   candidates. An index is bound to the requirement set it was built from, and a mismatch fails
   closed. There is no ambient "current" index. This rule came from a defect in the earlier build:
   retrieval accepted a job id and ignored it, so six jobs returned one identical set of 1,775
   relationships ([P-30](../evidence/03-claim-index.md#p-30)).
2. **A role owns what may compose.** Composite foreign keys enforce it
   ([K-01](../evidence/03-claim-index.md#k-01)).

Every non-shared table is protected by forced **row-level security** keyed to the account. The
runtime database role owns nothing ([P-12](../evidence/03-claim-index.md#p-12)).

## External services

| Service | Used for | Boundary |
|---|---|---|
| OpenAI (gpt-5-mini; embeddings) | Résumé selector, writer, summaries and career journey, reviewers, editor; most governed stages; all embeddings | Governed stage + priced model + recorded call |
| Anthropic (Claude Haiku 5.5) | Chat and interview coach, interview stages, role reading, application question and chat, requirement division, Growth plans and Navi on Growth (by the seed assignment; no Live call yet, [M-68](../evidence/04-metric-ledger.md#m-68)), the living résumé, research brief, claim extraction | Same; prompt caching on. Which stages ran on which model on Live: [M-68](../evidence/04-metric-ledger.md#m-68) |
| Jev (TypeSafe) | Rankings, selections and state probabilities, with the exceptions named in [D-10](../evidence/05-discrepancies.md#d-10) | Fixed questions in code, cached by context hash |
| Tavily | Company research sources; part of job discovery | ≤4 searches per research run; per-month cap for discovery |
| Apify (career-site index) | Job discovery from hosted career-site data | Admin account only, own monthly cap |
| ATS public APIs, employer pages | Job discovery and application questions | No credentials; robots.txt honored for non-ATS pages |
| GitHub public API | The portfolio: public repositories the owner approves | No credentials; files that could hold secrets never fetched ([P-34](../evidence/03-claim-index.md#p-34)); repository text untrusted ([P-35](../evidence/03-claim-index.md#p-35)); reads not recorded ([P-36](../evidence/03-claim-index.md#p-36)) |

## Where the architecture came from

None of this was designed up front. The capability architecture of the earlier build was
reconstructed from its code about 100 commits in. The current application was **extracted** on
2026-10-03 under a governing rule: "Migrate only capabilities and data whose authority and purpose
are understood. Do not copy the application and then try to remove the slop."
- 5 capabilities were re-implemented.
- 6 data sets were imported as data only.
- 5 were kept as reference only.
- 7 were rejected.

A clean-room test boots the application with the old system's imports made to fail
([P-30](../evidence/03-claim-index.md#p-30); [Evolution](../EVOLUTION.md)).
