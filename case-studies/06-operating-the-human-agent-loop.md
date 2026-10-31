# Case study 06 — Operating a product with an implementation agent

**One line:** Building with AI coding agents compressed the step from hypothesis to working
software to minutes. That made the product side of the loop the bottleneck: deciding, testing and
saying no. I built the process controls that let it run on a real production system without
breaking it.

**Audience notes.** *Product:* the human/agent loop as a way of working, and its failure modes.
*TPM:* release governance, incident response and turning operational feedback into product changes.
*Engineering:* what agents get wrong, and the guardrails that held.

---

## Context

I wrote none of Career Navigator's code. That was deliberate. The project was also an experiment in
what product development looks like when a product manager works with an implementation agent
almost in real time ([H-16](../evidence/03-claim-index.md#h-16)).

**Volume, as size not quality.** From 2026-10-03 to 10-24 the application received 683 non-merge
commits, 652 of them with a Claude co-author trailer ([M-31](../evidence/04-metric-ledger.md#m-31)).
The busiest days had 50–73 commits
([M-31](../evidence/04-metric-ledger.md#m-31)).

**The loop:**
1. I use the product on my real job search.
2. I notice something wrong or missing.
3. I describe the behavior I want and the constraints.
4. The agent investigates, proposes, implements and tests.
5. I check it on Beta.
6. It ships, or it doesn't.

## The problem: speed in both directions

Fast implementation has a mirror image: **fast regression.** Agents:
- reintroduced superseded rules from older documents;
- shipped changes I hadn't seen;
- once destroyed data;
- often proposed a "check that fixes it" instead of a fix.

In the earlier build I had to retire one rule twice ("I keep telling you that") and another only on
"the third time of asking" ([H-12](../evidence/03-claim-index.md#h-12)).

## My ownership

This case is about *my* side of the loop:
- deciding what gets built and what gets reverted;
- setting the rules agents must follow;
- running the release gate;
- interpreting incidents.

The agents wrote the scripts and tests that enforce those rules.

## Constraints

- **One production system, one person's real data, live use.** Live breakages cost me real
  applications.
- **A tiny, cheap host:** two cores, shared by Beta, Live and the database.
- **No team to review changes.** The controls had to work with one product owner and one agent.

## What went wrong, and what changed

| Date | What happened | Root cause | Change at the source |
|---|---|---|---|
| 2026-09-28 (earlier build) | A deploy override skipped the release proof and shipped untested code to the database I apply for jobs with | An override added as a hotfix path after Live broke, with no recorded owner decision behind it | Removed after 26 hours; the rule "never push to Live without the tests being complete, without my approval" ([H-11](../evidence/03-claim-index.md#h-11)) |
| 2026-10-02 | Change after change broke a 10,000-test legacy suite; a page-fitting pipeline rationed real evidence away | Accumulated machinery nobody could reason about | I had the approach deleted, "rather than parked"; then the **extraction** into a clean application with a sub-1,000-test target ([P-30](../evidence/03-claim-index.md#p-30)) |
| 2026-10-05 | While tenancy was being built, an agent's cleanup script deleted 17,183 rows across 50 tables, connected as schema owner, which bypasses row-level security | The runtime and maintenance roles could bypass row-level security | Forced RLS, a non-owner runtime role, explicit-account imports. Lost artifacts documented as lost; the tests that audit them are skipped, never re-pinned ([H-17](../evidence/03-claim-index.md#h-17)) |
| 2026-10-08 | A deploy restarted Live 3 s after I added a posting; its indexing vanished | Work accepted as an in-memory task | Durable background operations; deploys drain running work ([P-09](../evidence/03-claim-index.md#p-09)) |
| 2026-10-12/13 | Proposals to fix bad output with an automatic repair step | Catch-and-repair instinct | The project rule: **defects are fixed at their source**; one writer pass, one editor pass, no loops ([Product 02](../product/02-principles.md)) |
| 2026-10-14 | Several changes went straight to Live; I found labels shifting, status not saving, slow pages | No gate between "done" and "Live" | **Beta first**; Live deploys only from a branch of commits I approved after using them on Beta ([P-11](../evidence/03-claim-index.md#p-11)) |
| 2026-10-14 | Model spend was invisible: Jev recorded at $0, some calls unrecorded, failures erased by rollbacks | Each transport recorded itself differently, or not at all | Every call recorded at the governed boundary; spend and failure pages; alerts ([P-03](../evidence/03-claim-index.md#p-03), [P-18](../evidence/03-claim-index.md#p-18)) |
| 2026-10-19 | I'd asked for "no suite" pushes for speed; then reversed it | Speed over safety | **The full suite on the exact Live code before any Live deploy** |
| 2026-10-19 | Pages took 4–6 s while background work ran | Work threads in the web process on a 2-core host | A separate, lower-priority runner process ([M-29](../evidence/04-metric-ledger.md#m-29)) |
| 2026-10-21 | Beta and Live had diverged; each change needed two test runs | Parallel histories | Unified: the same code, schema and documents, with only the labs different. *Replaced on 2026-10-28, when I kept three Beta-only features off Live: Live is now its own cherry-picked line ([P-37](../evidence/03-claim-index.md#p-37), [DEC-50](../product/07-decision-log.md#dec-50))* |

## Alternatives considered

| Option | Why not |
|---|---|
| Review every diff myself | Not my role, and not where the value of the loop is. I review behavior on Beta instead |
| Let the agent deploy to Live when tests pass | Tests passed when the product was wrong; many defects were found only by use |
| Freeze features while hardening | Usage drove every important fix; freezing would have hidden the next defect |

## Decision and reasoning

**I govern behavior and gates; the agent governs code.** Concretely:

1. **Rules live where agents read them.** The project's agent instructions hold the product rules,
   each with its date and the words I used. The baseline's lesson was that "documents do not help if
   a session never looks at them" ([H-12](../evidence/03-claim-index.md#h-12)).
2. **Every rule has an enforcement point.** That might be a schema constraint, a contract test, a
   release script that stops at Beta, or a test that fails if a model is called in Chart My Course.
   (Since 2026-10-27 that test allows exactly one stated exception, which I chose:
   [A-05](../evidence/03-claim-index.md#a-05).)
   Prose alone wasn't enough.
3. **The release gate is a person using the product.** `ship.sh` stops at Beta: "the step between
   Beta and Live is a person opening the product".
4. **Disclosure over cosmetics.** Incidents are recorded in the commit that recovers from them,
   including the data-loss incident. Data that could not be restored is documented as lost, not
   re-created.

## Verification

- **Live deploys** come only from the `live-approved` branch, whose push history starts on
  2026-10-14 (75 pushes to 2026-10-25). That each push followed my use of the change on Beta is my
  account; git records the pushes, not the approvals. *Note, 2026-10-31: since 2026-10-28 Live
  deploys from a branch per release, rebuilt from Beta's approved commits by cherry-pick
  ([P-11](../evidence/03-claim-index.md#p-11), [P-37](../evidence/03-claim-index.md#p-37)).*
- **Deploys** back up the database, drain running work, publish governed documents with a snapshot,
  probe the site, and roll back automatically on failure ([P-10](../evidence/03-claim-index.md#p-10)).
- **Contract tests pin the rules:**
  - the governed model boundary;
  - tenancy;
  - the clean-room independence from the old codebase;
  - the role boundary;
  - "no model call" in the flows that must have none.
- **Last recorded full run:** 3,135 passed, 0 failed, 141 skipped (2026-10-21). Most of the 141 skips audit data lost on 2026-10-05; the rest need private
  files or tools not present ([M-30](../evidence/04-metric-ledger.md#m-30)). This run result is a session
  record, not a commit. *Note, 2026-10-31: the run for release 2026.10.1 is
  [M-79](../evidence/04-metric-ledger.md#m-79).*

## Results

- **No Live incident of the earlier kinds since the gates went in.** That rests on my own use, not a
  formal measure: no straight-to-Live changes, no lost accepted work, no invisible spend.
- **Features still shipped daily**, now through Beta, with the evidence chat, own interview questions,
  quick answers, Discover Jobs, apply kits, assess-first and gap themes all arriving in the ten days
  after the gates.
- **Review findings stay findings.** This portfolio's review turned up several defects:
  
  - an eligibility pattern that over-matches technical requirements;
    - the walkthrough using unchosen evidence;
  - two security and privacy findings, whose details are withheld from this public version until
    they are fixed.

  They are recorded with evidence, not quietly patched ([Discrepancies](../evidence/05-discrepancies.md)).

## Limitations

- **The loop still depends on me noticing.** Many defects surfaced only because I used the product
  daily. Without that, they would have shipped. Automated support checks on Live résumé text are not
  in place ([K-23](../evidence/03-claim-index.md#k-23)).
- **Agents still drift.** Stale "Beta only" comments, outdated documents and the README's legacy
  pipeline are visible in this review ([D-03](../evidence/05-discrepancies.md#d-03),
  [D-18](../evidence/05-discrepancies.md#d-18)).
- **One person is one reviewer.** No second human reviews behavior.

## What I learned about the loop

1. **The bottleneck moves to judgment.** When implementation is nearly free, the scarce skills are
   deciding what not to build, noticing when a fix is really a patch, and saying no to a passing
   test suite.
2. **Rules need a home and an enforcement point**, or an agent will helpfully undo them.
3. **Use beats tests for finding what matters.** Tests protect what you already understand. Daily use
   finds what you don't.
4. **Speed has to be spent on reversibility.** Branch-per-approval releases, durable work, automatic
   rollback and document snapshots are what made shipping this fast survivable.
