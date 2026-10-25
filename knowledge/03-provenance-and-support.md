# Knowledge 03 — Provenance and support

*Knowledge 3.0 · describes Live `7322289` (2026-10-24)*

**The question this answers:** when the system says something about a person, can it show where
that came from, and what stops it from saying more than the evidence does?

## Two kinds of drift this guards against

1. **Conclusions turning into facts.** A coaching step reads an earlier model's interpretation, such
   as "their roadmap work shows platform leadership", and repeats it as if the person had said it.
2. **Writing outrunning evidence.** A writer turns "supported the migration" into "led the
   migration", or adds a figure nobody stated.

The system treats these differently. Provenance labels handle the first. For the second it relies
on controlled inputs at the source plus checks that *report*. It has no single "hallucination
filter", and it does not claim to be hallucination-proof.

## Earlier conclusions keep their basis

Every coaching prompt receives earlier material with a label, applied by code rather than by the
model ([K-20](../evidence/03-claim-index.md#k-20)):

| Label | Meaning given to the model |
|---|---|
| **SAID** | Whether something was said by the interviewer, remembered as said by the candidate, or is "an inference … nobody said it". A missing code is treated as an inference. |
| **EARLIER** | Anything a previous model call wrote: "a reading of the evidence, not evidence; repeating it adds nothing". |
| **READING** | A reviewer's note. |

Nine coaching policies carry an identical `## Earlier conclusions` section: chat, interview
preparation, practice, framing, evidence answers, walkthrough, next actions, conversation
interpretation and research answers. A test fails if any copy differs by a byte. The rule says:
- keep each claim's basis;
- "not established" is never a weakness unless the person said so;
- never strengthen ownership;
- ask one targeted question instead of assuming.

A separate detector flags drafted answers that *promise* things ("I'll send the metrics deck") and
never removes them ([K-21](../evidence/03-claim-index.md#k-21)).

**Limits:**
- The test checks the seed files, not the versions published in each database.
- Two later prompts (application answers in the apply kit, and the public career conversation)
  label earlier text their own way and are outside the tested set
  ([D-20](../evidence/05-discrepancies.md#d-20)).

## How support is handled in résumé writing

The current résumé flow (since 2026-10-13/14) puts its controls on the **input side**, at the
stages that write ([Applications 03](../applications/03-resume-planning-writing-review.md)):

- **The writer never sees the job's requirements.** It sees only the stories a selector picked,
  copied in by code. Code builds every writer prompt, and a runtime guard refuses a writer prompt
  that carries the requirements block ([A-12](../evidence/03-claim-index.md#a-12)).
- **Every bullet names its source story** through a schema enum the API enforces, so attribution
  is structural, not positional ([A-13](../evidence/03-claim-index.md#a-13)).
- **A bullet cannot cite another role's evidence**: the database refuses it
  ([K-02](../evidence/03-claim-index.md#k-02)).
- **Sentences two stories share reach the writer once**, so one fact is not written twice
  ([A-14](../evidence/03-claim-index.md#a-14)).

Clause-by-clause verification of written text exists, but **it does not run on Live résumés**.
Every Live bullet is stored as `UNGROUNDED`, and the phase records itself as skipped
([K-23](../evidence/03-claim-index.md#k-23)). That was a deliberate trade:
- Grounding took **493.5 s of a 14-minute** generation in the previous flow.
- It was moved off the build path when the input-side design replaced it.
- It remains for measurement ([K-24](../evidence/03-claim-index.md#k-24)).

The consequence is a real residual risk. **No code compares final bullets with the evidence on
Live.** The writer's instruction ("use only the facts, figures and names in the text above") is a
prompt rule. The reviewers and the editor are deliberately not shown the career record
([Applications 03 → residual risks](../applications/03-resume-planning-writing-review.md#residual-risks)).

## Checks: what they look for and what they do

| Check | How | Runs on Live résumés? | Effect |
|---|---|---|---|
| Writer-prompt requirement guard | Code (substring) | Yes, before the call | Refuses the call |
| Story-number schema on bullets | API-enforced enum | Yes | Bullets without a valid story are dropped |
| Copy-editor correction gate | Code: no new figure or name, no negation change, ≤6 words | Yes | Refuses an unsafe correction |
| Coverage review (recruiter and hiring-manager seats) | Two model calls | Yes | **Reports only** |
| Repeat and twin labels | Jev | Yes | **Label only**; nothing removed |
| Readability measures | Code | Yes | **Report only** |
| Assertion-level grounding + numeric monotonicity | Model + code | **No** (measurement only) | Detects |
| Relation and agency ("supported" → "led") | Code | **No** (Fix gate only) | Refused in the older flow |
| Copied posting phrases | Code | **No**, made unnecessary because the writer never sees the posting | — |

**The calibration that justified assertion-level grounding (2026-10-03).** On five artifacts, the
old sentence-level validator called **48/48** statements established. Assertion-level grounding
found **19/48** fully established. An optimiser run had accepted a policy that manufactured causal
claims (10, of which 8 failed). The acceptance was reversed, and the validator was replaced for
measurement ([M-25](../evidence/04-metric-ledger.md#m-25)).

**The one deliberate repair step is Fix.** Fix is person-pressed. It rewrites a refused summary or a
sentence with an open finding, puts the rewrite through a deterministic gate (numbers lost or added,
new words not in the evidence, relation or agency changes) and re-reviews it. It is a
catch-and-repair step and is named as one ([A-17](../evidence/03-claim-index.md#a-17)). The
automatic repair phase that briefly preceded it was removed the same day it shipped (2026-10-12).
The product owner's words: the checks are "an assurance… not to actually fix an issue."

## Evidence-side checks

- **Evidence chat.** A figure in a proposal that the person never said is reported beside the
  proposal, not removed. A correction that changes nothing is reported too
  ([K-25](../evidence/03-claim-index.md#k-25)).
- **Résumé import.** The editor runs in *suggestion* mode. A suggestion that would change what a line
  claims ("Supported" to "Led") is never offered. Accepted corrections travel with the change as the
  original text plus the correction ([K-12](../evidence/03-claim-index.md#k-12)).
- **Guided discovery.** Code decides whether each fact the person gave is in the draft: 40% stem
  overlap, and every figure present. A fact that is neither in the draft nor deliberately left out
  is shown to the person.

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Earlier-conclusion labels and rule in 9 coaching policies | Verified (seed-level) | [K-20](../evidence/03-claim-index.md#k-20) |
| Promise detector, report-only | Verified | [K-21](../evidence/03-claim-index.md#k-21) |
| Writer withheld from requirements | Limited (unit test + substring guard; declared package check not executed) | [A-12](../evidence/03-claim-index.md#a-12) |
| Bullet → story attribution by schema | Verified | [A-13](../evidence/03-claim-index.md#a-13) |
| Clause-level grounding of Live résumé text | Superseded on the Live path (retained for measurement) | [K-23](../evidence/03-claim-index.md#k-23), [K-24](../evidence/03-claim-index.md#k-24) |
| Fix (person-pressed repair with gate) | Verified; a catch-and-repair step by design | [A-17](../evidence/03-claim-index.md#a-17) |
| Chat figure check, report-only | Verified | [K-25](../evidence/03-claim-index.md#k-25) |
