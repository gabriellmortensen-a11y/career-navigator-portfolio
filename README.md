# Career Navigator — product portfolio

**Gabriel Mortensen · product owner** · Portfolio release **2026.10.1** (2026-10-31) · describes the live application as of 2026-10-31 (commit `00eac95`)

Career Navigator helps a job seeker do three things:
1. turn a long, messy career into **evidence they approve**;
2. see what a specific job asks for that their evidence does or doesn't show;
3. close the gaps that matter, then **write, apply and prepare from that evidence alone**.

It runs in production beside a Beta environment where every change is tried first. I built it
for my own job search first, and it's still mostly my own record it's tested on.

> The bottleneck isn't generating a career artifact. It's building a durable understanding of the
> person that the artifact can be grounded in.

## The problem

Writing a résumé isn't the hard part. Remembering everything you've done, knowing what you can
actually show, and choosing what matters for *this* opening is. AI résumé tools mostly solve the easy
part. They make thin profiles sound better, which makes unsupported claims cheap: "supported the
migration" becomes "led the migration", and the posting's own phrases come back as experience. I
wanted the opposite: **discovery before representation, and nothing on the page the person can't
defend in an interview.**

## My role

**I'm the product owner, and I wrote none of the code. That was intentional.** The project was also
an experiment in building a real product with an AI implementation agent (Claude Code), almost in
real time.

| I did | The agents did |
|---|---|
| Identified problems from daily use | Implemented changes |
| Defined behavior and constraints | Wrote code and tests |
| Challenged designs | Ran investigations and measurements |
| Tested on a real job search | Reported their findings and their own mistakes |
| Read failures and measurements | |
| Chose experiments and approved spend | |
| Accepted or reverted changes | |
| Ran the release gate | |

Of the 683 non-merge commits from 2026-10-03 to 2026-10-24, 652 carry an agent co-author trailer. That is size,
not quality ([details and evidence](product/01-problem-users-and-role.md#my-role)).

## What works today

Everything in this table runs on Live. Each row links to the document that describes it; statuses
are defined in [COMPATIBILITY](COMPATIBILITY.md#status-vocabulary).

| Capability | What it means for the person | Status |
|---|---|---|
| **Governed career record** | Nothing becomes "true" without the person's press, with two named exceptions. Evidence from two jobs can never merge into one claim, and the database refuses it | Verified; automatic story composition limited ([Knowledge](knowledge/00-README.md)) |
| **Chart My Course** | Each requirement is marked strong, light or missing. A *gap* is only what a recruiter or hiring-manager persona would likely pass on, and related requirements count as one gap. Code, embeddings and Jev decide, with one stated exception: a long line listing several asks is divided by one small model call | Verified; calibration limited ([Applications 01](applications/01-job-analysis-and-assessment.md)) |
| **Gap conversations and Growth** | A chat that asks about related gaps as one theme, stops when code says the requirement is answered, and proposes one addition saved to a role the person confirms. A gap they can't close yet can become a Growth item with an action plan whose outcome would produce evidence | Verified; themes, requirement parts and the Growth boundary test limited ([Applications 02](applications/02-gap-conversations.md)) |
| **Résumés from evidence only** | A recruiter persona picks stories by number, and each bullet is written as its finished line from those stories alone. The summaries are written from a positioning brief, and their writers never see the posting. Each bullet names its source story, and a line's citations follow its words | Verified; summary isolation and findings limited; named residual risks ([Applications 03](applications/03-resume-planning-writing-review.md)) |
| **Discovery → application** | Searches ATS public APIs from the person's own professions; screens with evidence; holds unreadable postings; builds Greenhouse apply kits; an application chat drafts each answer from checked evidence; a browser extension (developer-mode install) fills forms and **never submits** | Verified; extension limited ([Applications 04](applications/04-discovery-to-application.md)) |
| **Interview coach** | Reads the role from the posting alone, then coaches each interview from verified claims only. Every line of a draft has a footnote showing the words it rests on; bounded company research sits beside it | Verified; footnotes and reading what a message means limited ([Applications 05](applications/05-research-and-interview-prep.md)) |
| **Navi, the chat on every page** | Opens beside any page, for that page, and can read the person's own account (opportunities, reviews, résumés sent) through read-only operations | Verified; rail behavior and read thresholds limited ([Applications 07](applications/07-navi-and-career-chat.md)) |
| **Living résumé** | A public link that answers about the person's career from what they chose to share, turns a pasted posting into a résumé-shaped answer, labels interpretations as interpretations, and can show approved GitHub portfolio documents apart from the evidence, summarizing one when asked; plus a read-only ChatGPT connector | Verified; strengths-only and pronoun rules limited ([Applications 06](applications/06-sharing-and-integrations.md)) |

## The decisions that shaped it

1. **Put rules where they can't be argued with.** The role boundary, tenancy and the single evidence
   writer live in the database schema and contract tests. Every time a rule lived only in prompts or
   prose, an agent eventually undid it ([Case study 01](case-studies/01-governed-career-evidence.md)).
2. **Fix defects at the source, never paper over them.** I rejected an automatic "repair" step the
   day it shipped. Overlong summaries were fixed by changing the writer's output shape, and
   mis-attributed bullets by a schema ([Product 02](product/02-principles.md)).
3. **Separate selection from writing.** The job's requirements go to the selector, never to the
   bullet writer. The summaries are planned by a model that reads the posting, but written by one
   that only ever sees the plan ([Case study 02](case-studies/02-preventing-unsupported-claims.md)).
4. **A probability model selects; language models only reason and write.** Ranks and states moved to
   fixed yes/no questions to Jev, a hosted probability model, with thresholds in code. Six named
   places still use a language model, the résumé selector among them
   ([D-10](evidence/05-discrepancies.md#d-10)). Against embedding similarity,
   Jev kept more of the directly relevant evidence on logged readings
   ([Case study 03](case-studies/03-evaluation-quality-latency-cost.md)).
5. **Automate up to a decision, then stop.** Assess before writing; never auto-submit
   ([Case study 04](case-studies/04-connecting-discovery-to-application.md)).
6. **A gap is what a reader would act on.** Everything else is optional. The model reviewers' actual verdicts override the estimate ([Case study 05](case-studies/05-gap-conversations-that-produce-evidence.md)).
7. **Beta before Live; Live only after I've used it.** A single small host, one production system,
   and an agent that ships fast in both directions
   ([Case study 06](case-studies/06-operating-the-human-agent-loop.md)).

## Verified results, with their limits

| Result | Measure | Limit |
|---|---|---|
| The step that turns raw evidence into standard career statements was mostly citing text the system had put into its own prompt. After the fix, prompt-sourced citations fell **49.47% → 3.62%** of proposals and the share accepted rose **19.65% → 45.65%** | Before/after on 8 real evidence records, reproduced by a second instrument | Earlier build (2026-08-13); one run per arm ([M-01](evidence/04-metric-ledger.md#m-01), [M-02](evidence/04-metric-ledger.md#m-02)) |
| Reading evidence for one posting: **1,164 → 68 judgments, 267 → 46 s, $0.45 → $0.04** | Same posting, before and after | One posting (2026-10-05) ([M-22](evidence/04-metric-ledger.md#m-22)) |
| On 309 logged readings, Jev kept **461 of 531** directly relevant pieces vs embedding similarity's **413** | Offline comparison | The reference is a model's verdicts ([M-23](evidence/04-metric-ledger.md#m-23)) |
| A résumé run costs a median **$0.128** (mean $0.160) and takes a median **210 s** | Live telemetry, 17 résumés since the speed route reached Live (2026-10-30 → 10-31) | One account; a different system from the row below, so the two are not a trend ([M-60](evidence/04-metric-ledger.md#m-60)) |
| Before the summaries were rebuilt (2026-10-28), a résumé cost **≈ $0.11** in writing and review model calls; median **207 s**; **17.6** bullets on average | Live telemetry, 32 résumés (2026-10-21 → 10-24) | One account. Assessing a job costs ≈ $0.02 per run (an upper bound) on top ([M-03](evidence/04-metric-ledger.md#m-03), [M-05](evidence/04-metric-ledger.md#m-05), [M-07](evidence/04-metric-ledger.md#m-07), [M-51](evidence/04-metric-ledger.md#m-51)) |
| Summaries over the readability limit: **73% / 96% → 0 of 20** after the writer's output shape changed | Replay | That summary path was replaced on 2026-10-28 ([M-17](evidence/04-metric-ledger.md#m-17), [A-101](evidence/03-claim-index.md#a-101)) |
| A living-résumé answer costs about **$0.0007** in model calls | Live telemetry, 14 answers through links | One account's links; visitors are counted, never identified ([M-69](evidence/04-metric-ledger.md#m-69)) |
| Job discovery: 18 runs, 297 openings, 92 assessed, 54 recommended, **$1.86** in total | Live telemetry | My account; recommendation isn't a hiring outcome ([M-10](evidence/04-metric-ledger.md#m-10)) |
| Up to **13 applications in 40 minutes** recorded | Status telemetry | Throughput, not success; "21 in 40 minutes" is not corroborated ([M-08](evidence/04-metric-ledger.md#m-08), [M-09](evidence/04-metric-ledger.md#m-09)) |

**What I don't claim:**
- **Interview or offer outcomes caused by the product.** There's no control group and one user.
- **That résumés are hallucination-proof.** No code checks Live résumé bullets against the evidence,
  and Jev's reading of each summary sentence is reported, never enforced; the controls are on the inputs ([details](applications/03-resume-planning-writing-review.md#residual-risks)).
- **That the "recruiter" calibration predicts people.** It's agreement with model personas
  ([Product 05](product/05-quality-and-measurement.md#what-is-not-measured)).

## Reading paths

**Hiring manager, about 15 minutes:**
1. This page.
2. [Problem, users and my role](product/01-problem-users-and-role.md).
3. [Case study 02: Preventing unsupported claims](case-studies/02-preventing-unsupported-claims.md).
4. [Case study 06: Operating the human/agent loop](case-studies/06-operating-the-human-agent-loop.md).
5. [Principles](product/02-principles.md).

**Technical reviewer, about an hour:**
1. [System architecture](product/03-system-architecture.md) and the [diagrams](architecture/00-README.md).
2. [Résumé flow: what each stage sees](applications/03-resume-planning-writing-review.md).
3. [Evidence admission](knowledge/02-admission-and-acceptance.md).
4. [Model routing, cost and latency](product/04-model-routing-cost-latency.md).
5. [Quality and measurement](product/05-quality-and-measurement.md).
6. [Interview coach](architecture/08-interview-coach.md) and [Navi's read layer](applications/07-navi-and-career-chat.md): where a model is shown only what was verified or read for it.
7. [Discrepancies](evidence/05-discrepancies.md): where the code and its own documents disagree.

**TPM / delivery:** [Case study 06](case-studies/06-operating-the-human-agent-loop.md) →
[Operations and privacy](product/06-operations-and-privacy.md) →
[Decision log](product/07-decision-log.md) → [Evolution](EVOLUTION.md).

**Looking for a specific artifact:** [INSPECT](INSPECT.md) lists where each kind of work can be inspected, linked to the exact section.

## How this portfolio is organized

| Folder | What's in it |
|---|---|
| [knowledge/](knowledge/00-README.md) | **Knowledge 3.1**: what is true about the person and how the system knows |
| [product/](product/00-README.md) | **Product 4.1**: why, principles, architecture, routing, measurement, operations, decisions |
| [applications/](applications/00-README.md) | **Applications 5.0**: what the person experiences, end to end |
| [case-studies/](case-studies/00-README.md) | Six case studies: problem, decision, alternatives, verification, limits, learning |
| [architecture/](architecture/00-README.md) | Eleven diagrams that separate code, Jev, model calls, human decisions, storage and external services |
| [evidence/](evidence/00-README.md) | Baseline, sources, **claim index**, **metric ledger**, discrepancies, verification log |
| [EVOLUTION.md](EVOLUTION.md) · [ROADMAP.md](ROADMAP.md) · [CHANGELOG.md](CHANGELOG.md) · [COMPATIBILITY.md](COMPATIBILITY.md) · [GLOSSARY.md](GLOSSARY.md) | History, future work (kept apart), releases, how the sections relate, terms |
| [career-evidence/](career-evidence/README.md) | These learnings as an importable career-evidence file |

Unfamiliar terms (Jev, ATS, row-level security, `UNGROUNDED`…) are defined in the
[glossary](GLOSSARY.md). **Status vocabulary** used throughout: *Verified*, *Limited*, *Experimental*, *Planned*,
*Superseded* ([definitions](COMPATIBILITY.md#status-vocabulary)). The application's source is private. Every claim here cites the file, test or commit it rests on, so it
can be walked through on request.

© 2026 Gabriel Mortensen. All rights reserved; see [LICENSE](LICENSE).
