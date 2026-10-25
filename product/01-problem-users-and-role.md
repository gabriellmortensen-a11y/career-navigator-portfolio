# Product 01 — Problem, users and my role

*Product 4.0 · describes Live `7322289` (2026-10-24)*

## The problem

Writing a résumé is not the hard part of representing a career. The hard part is understanding
three things:
- everything you have done;
- what you can actually show;
- which of it matters for this particular opening.

I had a long career with overlapping kinds of work. A normal résumé reduced it to a handful of
bullets. For every new job I was, in effect, reconstructing my career from memory:
- What have I done that answers this?
- Do I actually have evidence for it?
- Is there something relevant I've forgotten?

That is the problem Career Navigator exists to solve. It was built for me first, because I had the
problem and could test it on a real job search. As it started working, I made it usable by other
people ([H-10](../evidence/03-claim-index.md#h-10)).

The bet has not changed since the first version:

> The bottleneck isn't generating a career artifact. It's building a durable understanding of the
> person that the artifact can be grounded in.

The résumé is the first useful output and the most demanding test of that understanding. It is not
the product.

## Who it serves

| User | Need | What serves it today |
|---|---|---|
| **A job seeker with a long or varied career** | Show the right evidence for each opening, without reconstructing the career every time | Career record → Chart My Course → gap chat → résumé → apply kit ([Applications](../applications/00-README.md)) |
| **Someone changing careers** | See what their evidence already establishes toward another occupation | Change Course and "careers near my profession" (O*NET-based, no language model) ([A-58](../evidence/03-claim-index.md#a-58)) |
| **Someone unsure what they want** | A starting point tied to everyday words, not job titles | Problem-first journeys and the work-fit survey ([A-57](../evidence/03-claim-index.md#a-57), [A-59](../evidence/03-claim-index.md#a-59)) |
| **A recruiter, hiring manager or contact** (indirect) | A truthful, skimmable picture of the candidate | Résumés written only from the person's evidence; a shareable career conversation scoped by the owner ([A-55](../evidence/03-claim-index.md#a-55)) |

**Usage, stated plainly.** Live is multi-user, with accounts, invitations and row-level security.
The current application's measured usage, however, is overwhelmingly my own job search. The figures
in this portfolio come from that one account, and none of them should be read as adoption. Other
accounts exist, but none of their data is used in any measurement here.

## Why existing tools didn't fit

I wanted a system that understands my career through evidence, notices what's missing when an
opening exposes a gap, and represents me accurately from what it actually knows. I did not want an
AI résumé writer that takes a thin profile and makes the wording sound better.

That ruled out the two common patterns:
- **Generate from a profile.** This makes unsupported claims cheap. Nothing stops "supported" from
  becoming "led".
- **Keyword-match a résumé to a posting.** This rewards copying the posting's words, not showing the
  work.

## My role

**I am the product owner. I did not write the code.** That was intentional. Career Navigator was
also an experiment in what product development looks like when a product manager works with an
implementation agent almost in real time ([H-16](../evidence/03-claim-index.md#h-16)).

| I did | Claude Code agents did |
|---|---|
| Identified the problems, from my own use and from what the product showed me | Inspected the repository and proposed designs |
| Defined behaviour and constraints, and wrote the rules agents must follow | Implemented changes, wrote code and tests |
| Challenged assumptions and proposed designs | Ran investigations and measurements |
| Tested the real product on a real job search, daily | Surfaced findings, including their own errors |
| Interpreted failures and measurements | Deployed to Beta and, with my approval, to Live |
| Decided which experiments to run, and accepted or rejected approaches | |
| Decided what to build, change, revert or delete next | |

**What the repository shows** (consistent with this split, though it cannot prove who typed what):
- **Co-author trailers:** 652 of the 683 non-merge commits since 2026-10-03 carry a Claude
  co-author trailer ([M-31](../evidence/04-metric-ledger.md#m-31)).
- **Recorded decisions:** commit messages record my decisions in my words, for example "decided by
  the person whose product it is", "product owner, 2026-10-22" and "Asked 2026-10-12: …". By a rough
  text search, about 112 of 621 distinct messages cite a decision or request of mine.
- **Defects found through use:** many defects were found by using the product rather than by
  tests. Examples: a duplicate bullet I noticed on a Live résumé, conflicting verdicts on one job,
  and rejections filed under the wrong status.

**What the loop compressed.** Normally the step from hypothesis to working implementation goes
through handoffs and sprints. Here it took minutes to hours:
1. Have an idea and get it implemented.
2. Use it on a real application.
3. Find that the assumption or the implementation was wrong.
4. Change the design.

The cost of that speed is that agents also reintroduce old ideas quickly. The process controls in
[Case study 06](../case-studies/06-operating-the-human-agent-loop.md) exist because of that.

## What "working" means here

| Capability | Status |
|---|---|
| Career record with an enforced role boundary, one governed writer, provenance | Verified; automatic story composition limited ([Knowledge](../knowledge/00-README.md)) |
| Job analysis, assessment and gap definition with no language-model call | Verified ([A-05](../evidence/03-claim-index.md#a-05)) |
| Gap conversations that produce evidence the person approves | Verified ([A-08](../evidence/03-claim-index.md#a-08)) |
| Résumé writing from selected evidence, with the writer withheld from requirements | Verified; the withholding itself is limited verification ([A-11](../evidence/03-claim-index.md#a-11), [A-12](../evidence/03-claim-index.md#a-12)) |
| Job discovery → assessment → apply kit → browser fill → status tracking | Verified; extension limited ([Applications 04](../applications/04-discovery-to-application.md)) |
| Company research and interview preparation from chosen evidence | Verified; walkthrough has a known defect ([Applications 05](../applications/05-research-and-interview-prep.md)) |
| Outcome measurement (interviews, offers) attributable to the product | **Not established.** No controlled evidence exists ([Product 05](05-quality-and-measurement.md#what-is-not-measured)) |
