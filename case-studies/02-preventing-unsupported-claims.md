# Case study 02 — Preventing unsupported claims in tailored résumés

**One line:** Instead of catching overreach after a model writes, I changed what the writer is
allowed to see. Selection is done on the job's requirements; writing is done from the selected
evidence only; each bullet is bound to its source by a schema.

**Audience notes.** *Product:* the trade between tailoring and truthfulness. *Technical:* exactly
what each stage receives, and the residual risks. *TPM:* how the "fix it at the source" rule changed
the roadmap.

---

## Customer problem and context

A tailored résumé has to do two things that pull against each other:
- speak to what this job asks for;
- say nothing the person can't back up.

The common approach gives the writer the posting and the person's history and asks for a
"tailored" résumé. It produces confident, relevant text, and it also produces "led" where the
evidence says "supported", figures nobody stated, and the posting's own phrases presented as
experience.

The earlier flow in this product took that approach and then tried to *catch* the problems. The
writer saw each requirement it was answering. Five checks ran afterwards:
- relation and agency preservation;
- phrases copied from the posting;
- named tools claimed but missing;
- conflicting figures;
- optional assertion-level grounding.

On Beta, 52 of 265 bullets carried phrases copied from the requirement, nearly all on one test
account; on Live it was 2 of 220 ([M-43](../evidence/04-metric-ledger.md#m-43)). Grounding alone took 493.5 s of a 14-minute
generation ([M-35](../evidence/04-metric-ledger.md#m-35)). Each catch either dropped a line or
triggered another rewrite.

## My ownership

- **I set the rule** (2026-10-13): defects are fixed at the stage that produces them. A later step
  that notices and rewrites is not a fix. Reviewers and checks may detect and report.
- **I designed the replacement flow by doing it by hand.** I played recruiter and writer myself,
  section by section, and that beat every engineered variant the agents had built. My instruction
  was to reproduce exactly those four steps, and never to pass the writer the recruiter's text about
  what to write ([A-11](../evidence/03-claim-index.md#a-11)).
- **I judged changes by bullets, not by elegance.** A more selective picker produced shorter résumés
  with no reviewer gain, so it was reverted ([A-21](../evidence/03-claim-index.md#a-21)).
- **I found the defects that drove the last changes by reading Live résumés:**
  - a flagged belief-statement leading a role;
  - eligibility-based declines;
  - a near-duplicate bullet.

## Constraints

- **One writer pass, one editor pass, no loops.** No regeneration after review
  ([Product 02 §5](../product/02-principles.md#5-one-writer-pass-one-editor-pass-no-loops)).
- **No extra model calls in the build to prevent problems.** Prevention had to come from inputs and
  shapes ([A-17](../evidence/03-claim-index.md#a-17)).
- **Most bullets wins.** A résumé with fewer bullets reads as less evidence
  ([M-18](../evidence/04-metric-ledger.md#m-18)).
- **About ten cents and a few minutes per résumé**, for someone applying to many jobs
  ([M-03](../evidence/04-metric-ledger.md#m-03), [M-05](../evidence/04-metric-ledger.md#m-05)).

## Alternatives considered

| Option | Outcome |
|---|---|
| Writer sees requirements; checks catch overreach | The older flow. Detection was real, but the defects were still produced, and grounding dominated run time ([A-20](../evidence/03-claim-index.md#a-20)) |
| Automatic repair phase after review | Shipped and removed the same day (2026-10-12): it was catch-and-repair, with extra calls on every build |
| Content plan with labeled story parts and evidence-isolated writing | Built on a branch (12 commits); superseded before deployment by the simpler flow |
| Tell the selector which requirement each story shows, and how strongly | Tried on Beta. Bullets fell from 18–20 to 10–13 with no reviewer gain. Reverted in 23 minutes ([M-18](../evidence/04-metric-ledger.md#m-18)) |
| **Recruiter selects by number; writer writes only from what was selected** | **Chosen** |

## Decision and reasoning

**Selection is where the job belongs. Writing is where the evidence belongs.** Keep the two apart.

- **The selector**, a model playing a recruiter, sees the job title, every requirement, and the
  candidate stories numbered. It answers **numbers only**.
- **Code copies the chosen stories verbatim** into the writer's prompt.
- **The writer** sees those stories and its own draft. It never sees the requirements, the posting
  or anything the selector wrote. It is not given the posting's phrasing to borrow.
- **Each bullet must name the story it came from.** The API holds the answer to a schema whose story
  number is an enum of the stories it was given ([A-13](../evidence/03-claim-index.md#a-13)).
- **The database refuses** a bullet that cites another role's evidence
  ([K-02](../evidence/03-claim-index.md#k-02)).
- **Reviewers and the editor report**; they don't rewrite. The one editor pass may only change
  wording, through a code gate: no new figure or name, no negation change, ≤ 6 words
  ([A-16](../evidence/03-claim-index.md#a-16)).

The stage-by-stage table, with what each stage receives, is in
[Applications 03](../applications/03-resume-planning-writing-review.md#stage-by-stage-what-each-stage-receives).

## Implementation

Four calls per section, sections in parallel:

| Step | Who | Gets | Answers |
|---|---|---|---|
| 1 | Selector | Requirements + numbered stories | The story numbers to use |
| 2 | Writer | The picked stories (copied by code) | A draft, each bullet tagged `{story n}` |
| 3 | Selector | Requirements + numbered draft pieces | The piece numbers to keep |
| 4 | Writer | The kept pieces only | The tightened final text |

Then code assembles, fits the page against the printed PDF, and runs the reviewers.

*Note, 2026-10-31: since 2026-10-29 this flow writes bullets only. Each bullet is drafted as its
finished line, and step 4 runs only for a bullet longer than two printed lines
([A-91](../evidence/03-claim-index.md#a-91)). Since 2026-10-28 the summaries are written separately, from a positioning brief
([A-82](../evidence/03-claim-index.md#a-82), [A-101](../evidence/03-claim-index.md#a-101)).*

Defects found in use were fixed at the stage that produced them:

| Observed (date) | Producing stage | Change |
|---|---|---|
| A flagged belief-statement opened a role (10-13) | Selection input | Flagged stories removed before the selector sees them; the person can override ([K-17](../evidence/03-claim-index.md#k-17)) |
| 73% of executive and 96% of role summaries over the readability limit (10-22) | Writer output shape | At most 3 sentences of at most 15 words (2 for a role summary) instead of one text "of at most N words": **0 of 20** over on replay ([M-17](../evidence/04-metric-ledger.md#m-17)). *Superseded on 2026-10-28 by summaries from a positioning brief ([A-101](../evidence/03-claim-index.md#a-101))* |
| 17 bullets from 15 stories, so every bullet after the first split was stored against the wrong story (10-24, [M-56](../evidence/04-metric-ledger.md#m-56)) | Writer output shape | The story number moved into the schema |
| The same fact written twice because two stories said it (10-24) | Writer input | Sentences two stories share reach the writer once (cosine ≥ 0.70, then Jev ≥ 0.85) ([A-14](../evidence/03-claim-index.md#a-14)) |
| Both reviewers declined an above-typical résumé on citizenship and a degree (10-19) | Reviewer input | Eligibility lines never sent; education labeled a risk ([A-04](../evidence/03-claim-index.md#a-04)) |

## Verification

- **Unit test:** no writer prompt contains the requirements, and unselected or unkept text is never
  sent ([A-12](../evidence/03-claim-index.md#a-12)).
- **Schema tests:** bullet attribution and the role constraint.
- **Story attribution:** since 2026-10-24 each bullet carries its story number, held by the schema.
  Before that, attribution was positional and could be wrong ([M-56](../evidence/04-metric-ledger.md#m-56)).
- **Live telemetry**, 32 résumés, 2026-10-21 → 10-24:
  - mean 17.6 bullets ([M-07](../evidence/04-metric-ledger.md#m-07));
  - about $0.11 in language-model calls per résumé ([M-03](../evidence/04-metric-ledger.md#m-03));
  - median 207 s ([M-05](../evidence/04-metric-ledger.md#m-05)).

## Results and limitations

**What the design achieves:**
- The writer is not given the posting to copy (posting language can still arrive through saved
  evidence; see limit 5). *Note, 2026-10-31: this holds for the bullet writer. Since 2026-10-28 a
  summary planner reads the posting, and its brief reaches the summary writers by design
  ([A-83](../evidence/03-claim-index.md#a-83)).*
- It can only attribute a bullet to a story it was given.
- It cannot attribute across roles.
- The checks that used to drop lines afterwards became unnecessary, or are kept only for measurement.

**What it does not achieve. This design is not hallucination-proof:**
1. **No code compares final text with the evidence on Live.** Every bullet is stored `UNGROUNDED`.
   "Use only the facts in the text above" is an instruction, not a check
   ([K-23](../evidence/03-claim-index.md#k-23)). *Note, 2026-10-31: still true of bullets. Since 2026-10-28 Jev reads each
   summary sentence against the stories it cites and the result is reported, never enforced
   ([A-84](../evidence/03-claim-index.md#a-84)).*
2. **"Supported" → "led" is not checked at build time.** The agency check runs only inside Fix
   ([D-08](../evidence/05-discrepancies.md#d-08)).
3. **The withholding is partly enforced.** It rests on code-built prompts plus a unit test. The
   runtime guard is a substring check with no test of its own, and the declared "forbidden inputs"
   check isn't executed in this flow ([D-07](../evidence/05-discrepancies.md#d-07)).
4. **Strong evidence can still be written weakly.** About 1 in 6 requirements assessed strong came
   out partial or absent on the reviewed résumé, a figure from a Beta commit
   ([M-57](../evidence/04-metric-ledger.md#m-57)). The fix tried for it shortened résumés and was reverted. The
   question is open.
5. **Posting language can still enter through the evidence**, via gap-chat drafts the person saves.
   *Note, 2026-10-31: since 2026-10-28 it can also reach the summaries through the planner's brief
   ([A-83](../evidence/03-claim-index.md#a-83)), and the chat can read a posting when the person asks what it says
   ([K-31](../evidence/03-claim-index.md#k-31)).*

**The one deliberate repair step is Fix.** It is person-pressed: the person decides a line should
be repaired. The rewrite passes a deterministic gate covering numbers, new words, relation and
agency. It is named as catch-and-repair, not presented as prevention ([A-17](../evidence/03-claim-index.md#a-17)).

## What changed after learning from use

1. **The roadmap changed shape.** Every proposal of the form "add a check that fixes X" became
   "which stage produced X, and what input or shape makes X impossible?". That is why summaries got
   a sentence shape and bullets got a schema.
2. **I stopped optimizing selection precision.** The experiment that made the selector smarter made
   résumés shorter. The measurement rule now is: bullets and stories first, then what reviewers
   find.
3. **I learned to read the review as an instrument, not a judge.** The reviewers are model
   personas. Their verdicts calibrate the system against itself, which is useful for consistency and
   says nothing about real recruiters ([D-19](../evidence/05-discrepancies.md#d-19)).
4. **Next.** Restore an automated support measurement on Live résumés as a report, not a gate, so the
   residual risk is measured instead of assumed ([Roadmap](../ROADMAP.md)).
