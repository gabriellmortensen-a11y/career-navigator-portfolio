# Evolution — from the layer documents to the current application

This is the story from the July 2026 documents, through the earlier build that the 2026-09-30
retrospective described (the **baseline**), to Live `7322289` (2026-10-24). Every dated claim links
to the [claim index](evidence/03-claim-index.md) or [metric ledger](evidence/04-metric-ledger.md).
The diagrammatic version is [Architecture 07](architecture/07-historical-and-planned.md).

> **The premise never changed:** the bottleneck isn't generating a career artifact; it's building a
> durable understanding of the person that the artifact can be grounded in. The implementation
> changed almost completely, roughly four times.

## At a glance

| Period | System | What it believed | What it learned |
|---|---|---|---|
| 2026-07-08 | Three layer documents | Discovery before representation; verified knowledge; human validation | — (no software yet) |
| 07-17 → 08-06 | Predecessor: Markdown libraries in git, an Open WebUI front end | Truth lives in files a person edits | Slow (~183 s per run), single-user, never deployed ([H-02](evidence/03-claim-index.md#h-02)) |
| 08-06 → 09-29 | Earlier build ("beta4"): web app, then hosted multi-user Live | A model may propose; only a person may approve | Measurement kept contradicting the product; evidence was being manufactured across roles; rules in prose kept being undone |
| **09-29** | **Baseline** (`38f4bbf`) | Bounded Fit, capability addresses, one-press "Express" résumé | — |
| 10-03 → 10-24 | Current application (extracted) | Authority in the schema; Jev selects, models write; fix at the source; assess before writing | This portfolio |

## 1. Before software: the layer documents (2026-07-08)

Three layers, each with its own version ([H-01](evidence/03-claim-index.md#h-01)):

| Layer | Version | Question | Contents |
|---|---|---|---|
| Knowledge ("CareerOS") | 2.2 | What is true? | Markdown libraries of one career: profile, timeline, 14 project write-ups, metrics, stories, bullets |
| Product | 3.0 | How should the system think? | 18 documents: vision, principles, five engines (Discovery, Knowledge, Learning, Reasoning, Navigation), a PRFAQ, roadmap, ADRs |
| Application | 3.0 | How should the user experience it? | 14 artifact standards, from résumés to promotion packets |

Two ideas from these documents survive today: **"Most AI career products optimize generation.
Career Navigator optimizes discovery"**, and every artifact must be "interview-defensible and
traceable to verified evidence". Most of the Application layer was never built: no executive
biography, promotion packet, performance-review support, Learning engine or Persona system
([D-24](evidence/05-discrepancies.md#d-24)).

## 2. The predecessor (2026-07-17 → 08-06)

A single-user "career operating system" ([H-02](evidence/03-claim-index.md#h-02)):
- Markdown libraries in git were the source of truth.
- A FastAPI service posed as a chat backend behind Open WebUI.
- Approving a change wrote Markdown and made a git commit.
- Generation ran on a local model.

It was never deployed. Semantic runs took about 183 s. The knowledge model was reshaped about five
times in six days. The new build started on 2026-08-06 while the predecessor was still being
committed to, and no code was carried across.

## 3. The earlier build, up to the baseline (2026-08-06 → 09-29)

Condensed from the baseline's architecture generations G1–G11. Each step is approach → failure →
response.

1. **Proposals as the only intake** (08-06). Truthfulness was enforced "in code, not only in
   prompts", and chat could only create pending proposals. The rule "a model may propose; only a
   person may approve" entered the agent instructions and never left
   ([H-03](evidence/03-claim-index.md#h-03)).
2. **Measurement started contradicting the product** (08-11 → 08-17):
   - Four deterministic validators judging support scored at chance (5–7 of 17); a model validator
     scored 13/17 ([M-33](evidence/04-metric-ledger.md#m-33)).
   - Coverage displayed as 22 of 22 re-scored to 10 covered and 12 partial (72% weighted), and three runs of one job read 78, 64 and 70%
     because failures were shown as verdicts ([H-06](evidence/03-claim-index.md#h-06)).
   - **QC-1:** the canonicalization step was citing context the system had put into its own prompt.
     The fix cut prompt-sourced citations from **49.47% to 3.62%** and raised admission yield from
     **19.65% to 45.65%** ([M-01](evidence/04-metric-ledger.md#m-01), [M-02](evidence/04-metric-ledger.md#m-02)).
   - Rules followed: no paid calls in tests; a failed judgement is never a verdict.
3. **The architecture was discovered, not designed** (08-10). It was reconstructed from code about
   100 commits in. The agent instructions grew to 1,030 lines, which is size, not quality ([M-50](evidence/04-metric-ledger.md#m-50)).
4. **Retrieval went through seven generations.** One failure kept recurring: evidence with no index
   entry became invisible.
5. **Hosted, multi-user Live** arrived on 2026-09-06, with sign-in and PostgreSQL. Real users were
   recorded from 09-21 ([H-10](evidence/03-claim-index.md#h-10)). Where inference ran oscillated six
   times ([H-13](evidence/03-claim-index.md#h-13)).
6. **The human acceptance gate was retired** (09-10). I decided it assigned to a person work the
   system is supposed to do ([H-09](evidence/03-claim-index.md#h-09)).
7. **Repeatability came from persistence** (09-17). Re-judging every run gave 16, 2 and 7 ([M-34](evidence/04-metric-ledger.md#m-34)) established
   requirements on an unchanged posting. Persisting gated findings made an unchanged rerun identical
   (21/21) at $0 ([M-34](evidence/04-metric-ledger.md#m-34)).
8. **The judged unit changed five times**, each move for cost, reproducibility or stability. None was
   recorded as an accuracy gain ([H-14](evidence/03-claim-index.md#h-14)).
9. **Bounded Fit** (09-24 → 09-29). Requirements were being "established" by combining unrelated
   roles, so answers were forced to come from one coherent body of work. It "became the product
   through use" ([H-07](evidence/03-claim-index.md#h-07)).
10. **Release discipline was learned the hard way.**
    - A deploy override shipped untested code and was removed after 26 hours
      ([H-11](evidence/03-claim-index.md#h-11)).
    - Agents revived rules I had retired: one I retired twice, another only on "the third time of
      asking"
      ([H-12](evidence/03-claim-index.md#h-12)).

## 4. The baseline (2026-09-29, `38f4bbf`)

At the baseline, a job opened on the Bounded Fit page. One "Express" press grouped evidence, re-ran
fit, drafted bullets and wrote a résumé. Retrieval routed through embedded capability statements to
at most three bodies of work. All inference was hosted. The retrospective found 11 open
contradictions between documents and code. The most important was that a derived "capability" was
in places used as evidence ([H-18](evidence/03-claim-index.md#h-18)).

## 5. The last three days of the earlier build (09-30 → 10-02)

Twenty-three commits, all on the résumé path. Each change tripped the 10,000-test legacy suite: one
commit reported 9,453 passed and 27 failed ([M-48](evidence/04-metric-ledger.md#m-48)), and five commits existed only to classify failures caused
by the commit before. On 10-02 I had the Staged Planner's page-fitting stages deleted, "rather than
parked", and page rationing turned off on Beta. The experiments that defined the next architecture
(V2-1033…1061) were never committed.

## 6. The extraction (2026-10-03)

The governing rule: **"Migrate only capabilities and data whose authority and purpose are
understood. Do not copy the application and then try to remove the slop."**
([P-30](evidence/03-claim-index.md#p-30))

- **Why:**
  - an authority defect: retrieval accepted a job id and ignored it, so six jobs returned one
    identical set of relationships;
  - velocity: about 10,000 contract tests against a target of under 1,000.
- **How:**
  - a new repository and PostgreSQL from day one;
  - two authority boundaries in the schema (a job owns its requirements; a role owns what may
    compose);
  - one governed boundary for model calls with no fallbacks.
- **What was kept:**

  | Disposition | Count |
  |---|---:|
  | Capabilities re-implemented | 5 |
  | Data sets imported as data only | 6 |
  | Kept as reference only | 5 |
  | Rejected | 7 |

- **Proof:**
  - four verification jobs reproduced exactly on independently written routing;
  - 117 contracts ran in 3.16 s, against 10,541 before ([M-49](evidence/04-metric-ledger.md#m-49));
  - a clean-room test boots the application with the old system's imports made to fail.
- **Measured the same day:** an optimiser's "improvement" turned out to be inside evaluator noise (readings of an unchanged résumé ranged by up to 3 major findings), and was
  reversed ([M-26](evidence/04-metric-ledger.md#m-26)).

## 7. Since the extraction (2026-10-03 → 10-24)

| Phase | Dates | What changed |
|---|---|---|
| Product from pipeline | 10-04 → 10-05 | One-button résumé; Change Documents as the only evidence writer ([K-10](evidence/03-claim-index.md#k-10)); accounts; **forced row-level security, built the same day an agent's script running as schema owner deleted 17,183 rows** ([H-17](evidence/03-claim-index.md#h-17)); exhaustive review replaced by six pieces read once ([M-22](evidence/04-metric-ledger.md#m-22)); deploy by named commit |
| Review-centred job flow | 10-06 → 10-07 | Résumé review against a posting; What's Next; "relevance is not sufficiency"; Chart My Course |
| Journey, world, connections | 10-08 → 10-10 | My Journey; durable background work ([P-09](evidence/03-claim-index.md#p-09)); career world; LinkedIn import; Change Course with zero model calls ([A-58](evidence/03-claim-index.md#a-58)) |
| New users; Jev over model calls | 10-10 → 10-12 | First five minutes; "Jev selects" ([M-23](evidence/04-metric-ledger.md#m-23)); requirement sift; prevention without extra calls |
| **Stories + recruiter-selects** | 10-13 → 10-14 | Fragments glued into stories ([K-06](evidence/03-claim-index.md#k-06)); the project rules (fix at the source; Jev selects; one writer, one editor); the recruiter-selects résumé flow ([A-11](evidence/03-claim-index.md#a-11)); flagged evidence excluded |
| **Beta before Live** | 10-14 | Live deploys only from approved commits ([P-11](evidence/03-claim-index.md#p-11)); every call recorded and priced ([P-03](evidence/03-claim-index.md#p-03)) |
| Evidence chat | 10-14 → 10-16 | "Tell your record": propose, then Save ([K-13](evidence/03-claim-index.md#k-13)) |
| Interview, research, runner, routing | 10-19 → 10-20 | Own questions; Jev-chosen interview evidence; company research; separate runner; eligibility never screened ([A-04](evidence/03-claim-index.md#a-04)); per-task models ([M-19](evidence/04-metric-ledger.md#m-19)) |
| **Discovery to apply** | 10-20 → 10-21 | Discover Jobs ([A-30](evidence/03-claim-index.md#a-30)); apply kits and extension ([A-38](evidence/03-claim-index.md#a-38)); career-site index pilot |
| Beta and Live unified | 10-21 | One code base, schema and set of documents; only the labs differ |
| Tune and gap chat | 10-21 → 10-22 | Tune my evidence; guided gap discovery with code-decided stops ([A-08](evidence/03-claim-index.md#a-08)); prompt caching |
| **Assess first** | 10-22 → 10-24 | Nothing writes a résumé without the Write press ([A-37](evidence/03-claim-index.md#a-37)); gap = what a reader would pass on ([A-06](evidence/03-claim-index.md#a-06)); a real reading overrides the estimate; themes; bullets bound to stories by schema ([A-13](evidence/03-claim-index.md#a-13)) |

## 8. What changed most since the baseline

| Area | Baseline (2026-09-29) | Now (2026-10-24) |
|---|---|---|
| **Where rules live** | Mostly prose in a 1,030-line instruction file; enforcement uneven | Schema constraints, contract tests, a governed call boundary, release scripts; short project rules |
| **Unit of evidence** | Bodies of work routed through capability addresses | Stories (glued fragments) within one role, enforced by foreign keys |
| **Who judges evidence** | Model judges, persisted for repeatability | Jev for ranks and states, with four named exceptions; no language model in assessment ([A-05](evidence/03-claim-index.md#a-05)) |
| **Résumé writing** | Express: one press from analysis to an admitted résumé, with repair | Assess first; Write is its own press; recruiter selects by number; the writer never sees requirements; bullets bound to stories |
| **Gaps** | Coverage findings | Only what a reader would pass on, asked as themes, tracked per requirement by code |
| **Beyond the résumé** | Discovery and Growth pages inside the fit flow | Job discovery across ATSs, apply kits, browser fill, status tracking, company research, interview prep, shareable conversations, a ChatGPT connector |
| **Operations** | Hosted Live with a release suite and a removed override | Beta before Live, approved-commit branch, durable work, separate runner, backups, document snapshots, automatic rollback |
| **Measurement** | Ledger reservations vs charges; persisted findings | Every call recorded and priced; capability registry; assessment vs review; measured costs only |

## 9. What stayed constant

- A model may propose; only a person may approve.
- Unknown is never "no"; nothing is invented to fill a gap.
- Discovery before representation: the résumé is a test of the record, not the product.
- The working method: I decide and test; implementation agents build. The agents keep needing
  guardrails because they are fast in both directions ([Case study 06](case-studies/06-operating-the-human-agent-loop.md)).
