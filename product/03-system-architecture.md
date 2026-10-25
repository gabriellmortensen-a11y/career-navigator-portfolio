# Product 03 — System architecture

*Product 4.0 · describes Live `7322289` (2026-10-24) · diagrams in [architecture/](../architecture/00-README.md)*

## Shape of the system

Career Navigator is one Python web application (FastAPI with server-rendered pages) backed by one
PostgreSQL database per environment. A separate background runner process handles the slow work. It
runs on a single small Linux host that serves **Beta** and **Live** as two services, each with its
own database. Both run the same code. Only the experimental labs differ ([P-11](../evidence/03-claim-index.md#p-11)).

```text
browser ──► web process (enqueue only) ──► background_operation rows ──► runner process (niced)
   │              │                                                         │
   │              └── PostgreSQL (row-level security, one DB per env) ◄─────┘
   │                                                                       │
Chrome extension (fills forms, never submits)          external services: OpenAI, Anthropic,
                                                       Jev, Tavily, Apify, ATS public APIs
```

The component diagram with every boundary is [Architecture 01](../architecture/01-components.md).

## Components and what each owns

| Component | Owns | Never does |
|---|---|---|
| **Career record** (`app/evidence`, `app/authority`) | Roles, sources, claims, stories; the Change Document writer | Accept a write that is not a Change Document; let two roles share a row |
| **Job intake and analysis** (`app/pipeline`) | Reading postings, requirement sifting and rewording, fingerprints, story retrieval and Jev reading, the assessment | Call a language model ([A-05](../evidence/03-claim-index.md#a-05)) |
| **Gap conversations** (`app/evidence/chat`, `discovery`, `job_gaps`, `themes`) | Asking about gaps, deciding stops in code, proposing one consolidated addition | Save without a person's press and a role the person confirmed |
| **Résumé** (`app/resume`) | Selection, the recruiter-selects writing flow, page fit, reviews, editor, Fix, person edits | Show the writer the requirements; loop writer ↔ reviewer |
| **Discovery and apply** (`app/discovery`, `app/apply`, `extension/`) | Searching sources, screening, queues, kits, browser fill | Submit an application; use a credential or work around a refusal |
| **Journey** (`app/journey`) | Statuses, activity, company research, interview preparation, Change Course, work fit | Treat an earlier conclusion as evidence |
| **Sharing and integrations** (`app/sharing`, `app/mcp_beta`) | Scoped public conversation links; read-only ChatGPT connector | Write to the record; read outside the owner's chosen scope |
| **Governance** (`app/governance`, `app/documents`) | The only path to any model, Jev, embedding, search or scrape call; governed policy documents; model assignments; cost | Call an unpriced model, fall back silently, or run an undeclared stage ([P-01](../evidence/03-claim-index.md#p-01)) |
| **Operations** (`app/operations`, `scripts/deploy.sh`) | Durable background work, the runner, deploy with backup, drain and rollback | Lose accepted work on restart ([P-09](../evidence/03-claim-index.md#p-09)) |
| **Observability** (`app/observability`, `app/capabilities`) | Spend, failures, flow charts, assessment-vs-review | Show career text ([P-13](../evidence/03-claim-index.md#p-13)) |

## Four kinds of work, kept distinct

Every step is one of these four kinds. The diagrams mark which kind each step is.

1. **Deterministic code**: parsing, rules, thresholds, fingerprints, gates, page fit.
2. **Jev questions**: a probability model asked fixed, typed questions ("does this sentence
   establish this requirement?"). Used to rank, select, filter and decide states. About $0.042 per
   million input tokens.
3. **Language-model calls**: writing and reasoning only. These are the selector and writer of the
   résumé flow, the chat, interview stages, the research brief, the reviewers and the editor. Each
   runs under a governed, versioned policy document.
4. **Human decisions**: approving evidence, picking a role, pressing Write, accepting a kit answer,
   submitting the application.

The capability registry declares 45 capabilities in 6 flows. Each declares its owner function, the
stages it records and its gate. Tests check every declaration against the code
([P-06](../evidence/03-claim-index.md#p-06)).

| Kind | Capabilities |
|---|---:|
| Code rules | 18 |
| Jev | 12 |
| Language model | 10 |
| Embeddings | 4 |
| Outside service | 1 |

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
| OpenAI (gpt-5-mini; embeddings) | Résumé selector, writer, reviewers, editor; most governed stages; all embeddings | Governed stage + priced model + recorded call |
| Anthropic (Claude Haiku 5.5) | Chat, interview stages, research brief, claim extraction | Same; prompt caching on |
| Jev (TypeSafe) | Every ranking, selection and state probability | Fixed questions in code, cached by context hash |
| Tavily | Company research sources; part of job discovery | ≤4 searches per research run; per-month cap for discovery |
| Apify (career-site index) | Job discovery from hosted career-site data | Admin account only, own monthly cap |
| ATS public APIs, employer pages | Job discovery and application questions | No credentials; robots.txt honoured for non-ATS pages |

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
