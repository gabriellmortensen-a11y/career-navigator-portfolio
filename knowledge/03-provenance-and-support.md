# Knowledge 03 — Provenance and support

*Knowledge 3.1 · describes Live `00eac95` (2026-10-31)*

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
- Later prompts label earlier text their own way and are outside the tested set: application
  answers in the apply kit, the living résumé, and the application chat, which labels what the
  person told and said in its own codes ([D-20](../evidence/05-discrepancies.md#d-20)). The
  policies added since 2026-10-25 (application chat, role reading, Growth) are not among the nine.

## Every record the chat reads says whose it is

Since 2026-10-28 Career Chat can read the person's account
([A-102](../evidence/03-claim-index.md#a-102)). Every record it reads carries one of ten authority
labels, set by code; a record with an unknown label is refused. The chat is told to keep them apart
([K-32](../evidence/03-claim-index.md#k-32)).

| Label | Given to the model as |
|---|---|
| `record` | "your record: your own words, saved by you" |
| `set_by_you` | "set by you" |
| `your_note` | "your own note" |
| `employer` | "the employer's words (the posting): what they ask for, not evidence of yours" |
| `reading` | "Career Navigator's reading of your record against the posting (an estimate)" |
| `reviewer` | "a Career Navigator reviewer's assessment of the résumé (a simulated recruiter or hiring manager): not the employer's view, and not a reason an employer gave" |
| `resume` | "résumé wording Career Navigator wrote: not evidence" |
| `generated` | "written by Career Navigator from your record" |
| `research` | "company research gathered from the web: unverified" |
| `connection` | "a connection you added" |

Two rules follow from the labels:
- **A reviewer's finding is never the employer's reason.** An answer about gaps across rejected
  opportunities carries a fixed sentence, put in by code: "These are gaps identified by Career
  Navigator's reviewers. They are not confirmed reasons the employers rejected the applications."
  ([A-103](../evidence/03-claim-index.md#a-103)). That the model says it is a policy rule.
- **The employer's words are material, not instructions.** Posting and research text in what was
  read is labeled untrusted ([K-31](../evidence/03-claim-index.md#k-31)).

## Stated, inferred, drafted

Three newer paths keep what a source says apart from what is inferred from it:
- **A role reading** marks a finding "stated" only when its basis is explicit **and** code finds the
  quoted phrase in the posting. Everything else is "inferred" or listed as unknown. What code can't
  verify is recorded as a finding, never repaired ([A-62](../evidence/03-claim-index.md#a-62)).
- **A reason for wanting a role** that the person hasn't given is drafted from their record by the
  interview coach. Jev checks it as a fair inference from the work it cites, adding no work, scope,
  result, title or number. Its footnote says it is "inferred from your record — keep it if it's true
  for you, or tell me your own reason". A request to write the reason is never stored as the reason
  ([A-68](../evidence/03-claim-index.md#a-68)).
- **A living-résumé interpretation** of what the owner would do in a situation is labeled
  "Likely approach inferred from N recorded decisions" by code and never written to the record; the
  policy, not code, keeps it out of the owner's voice ([A-114](../evidence/03-claim-index.md#a-114)).

## How support is handled in interview and application answers

The interview coach (since 2026-10-25) and the application chat (since 2026-10-27) control support
the same way the résumé writer does: on the input side.

- **The writer sees only verified claims.** Code sets what each answer must establish. Jev reads the
  record's sentences per need, and the coaching call is shown only the chosen claims and what the
  person told it. It never sees the record, and sees the posting's requirement lines only when the role could not be read. A need that nothing verified
  shows is asked about, never filled with weaker material ([A-63](../evidence/03-claim-index.md#a-63)).
- **Every draft line has a footnote**: the exact words it rests on, their role, and Jev's reading of
  whether they establish the whole line. An unsupported line is marked and keeps the answer from
  being ready. There is nothing to press ([A-64](../evidence/03-claim-index.md#a-64)).
- **The application chat reports, never repairs.** Each line cites its sources and Jev checks it.
  Unsupported lines, over-length and unsourced quotes are reported ([A-73](../evidence/03-claim-index.md#a-73)).
- **One exception, named.** In the coach, approving a draft whose line Jev reads as unsupported
  makes the coach write it again. That is a check triggering a rewrite, which conflicts with the
  project rule that checks only detect and report ([D-31](../evidence/05-discrepancies.md#d-31)).

## How support is handled in résumé writing

The current résumé flow (since 2026-10-13/14) puts its controls on the **input side**, at the
stages that write ([Applications 03](../applications/03-resume-planning-writing-review.md)):

- **The bullet writer never sees the job's requirements.** It sees only the stories a selector picked,
  copied in by code. Code builds every writer prompt, and a runtime guard refuses a writer prompt
  that carries the requirements block ([A-12](../evidence/03-claim-index.md#a-12)).
- **Every bullet names its source story** through a schema enum the API enforces, so attribution
  is structural, not positional ([A-13](../evidence/03-claim-index.md#a-13)).
- **A bullet cannot cite another role's evidence**: the database refuses it
  ([K-02](../evidence/03-claim-index.md#k-02)).
- **Sentences two stories share reach the writer once**, so one fact is not written twice
  ([A-14](../evidence/03-claim-index.md#a-14)).
- **A changed line's citations follow its words.** Since 2026-10-29, when the person rewords a line
  on the review page, it is cited only for what Jev reads its new words as showing; a removed line
  is cited for nothing ([A-93](../evidence/03-claim-index.md#a-93)).

**The summaries are a separate path** (since 2026-10-28). They are not written by the bullet writer
([A-101](../evidence/03-claim-index.md#a-101)):
- A planner reads the posting and writes a positioning brief. An assertion in the brief can cite
  only the matched stories, through a schema enum; a citation is not required ([A-82](../evidence/03-claim-index.md#a-82)).
- The summary writers never get the posting, the requirements, or the brief's field for the
  employer's problem. A guard refuses a writer message holding the opening of any long requirement or posting line.
  But the brief is written in the employer's vocabulary where it fits, so posting wording reaches
  the writers by design ([A-83](../evidence/03-claim-index.md#a-83)).
- The planner and writers read the stories restated in plain words. Jev reads the originals
  ([A-87](../evidence/03-claim-index.md#a-87)).
- Jev reads each summary sentence against the stories it cites. What Jev and code find is shown on
  the review page as labels. The summary is placed as written and never replaced
  ([A-84](../evidence/03-claim-index.md#a-84)).

Clause-by-clause verification of written text exists, but **it does not run on Live résumés**.
Every Live bullet and summary is stored as `UNGROUNDED`, and the phase records itself as skipped
([K-23](../evidence/03-claim-index.md#k-23)). The Jev reading of summary sentences above is a report and changes nothing.
That was a deliberate trade:
- Grounding took **493.5 s of a 14-minute** generation in the previous flow.
- It was moved off the build path when the input-side design replaced it.
- It remains for measurement ([K-24](../evidence/03-claim-index.md#k-24)).

The consequence is a real residual risk. **No code compares final bullets with the evidence on
Live**, and the summaries' reading is reported, not enforced. The writer's instruction ("use only the facts, figures and names in the text above") is a
prompt rule. The reviewers and the editor are deliberately not shown the career record
([Applications 03 → residual risks](../applications/03-resume-planning-writing-review.md#residual-risks)).

## Checks: what they look for and what they do

| Check | How | Runs on Live résumés? | Effect |
|---|---|---|---|
| Writer-prompt requirement guard | Code (substring) | Yes, before the call | Refuses the call |
| Summary-writer guard: no requirement or posting line | Code (substring) | Yes, before the call | Refuses the call ([A-83](../evidence/03-claim-index.md#a-83)) |
| Story-number schema on bullets | API-enforced enum | Yes | Bullets without a valid story are dropped |
| Summary sentence support | Jev, against the stories each sentence cites | Yes | **Report only**; placed as written ([A-84](../evidence/03-claim-index.md#a-84)) |
| Summary findings: opener, more than one figure, tool lists, logistics, the page's character cap, word count | Code | Yes | **Label only** ([A-84](../evidence/03-claim-index.md#a-84)) |
| Copy-editor correction gate | Code: no new figure or name, no negation change, ≤6 words | Yes | Refuses an unsafe correction |
| Coverage review (recruiter and hiring-manager seats) | Two model calls | Yes | **Reports only** |
| Repeat and twin labels | Jev | Yes | **Label only**; nothing removed |
| Readability measures | Code | Yes | **Report only** |
| Assertion-level grounding + numeric monotonicity | Model + code | **No** (measurement only) | Detects |
| Relation and agency ("supported" → "led") | Code | **No** (Fix gate only) | Refused in the older flow |
| Copied posting phrases | Code | Bullets: **no**, made unnecessary because the bullet writer never sees the posting. Summaries: yes, any six-word run copied from the posting | Summaries: **label only** ([A-84](../evidence/03-claim-index.md#a-84)) |

**The calibration that justified assertion-level grounding (2026-10-03).** On five artifacts, the
old sentence-level validator called **48/48** statements established. Assertion-level grounding
found **19/48** fully established. An optimizer run had accepted a policy that manufactured causal
claims (10, of which 8 failed). The acceptance was reversed, and the validator was replaced for
measurement ([M-25](../evidence/04-metric-ledger.md#m-25)).

**The one deliberate repair step is Fix.** Fix is person-pressed. It rewrites a sentence with an
open finding (and, on a résumé written before 2026-10-28, a refused summary), puts the rewrite
through a deterministic gate (numbers lost or added, new words not in the evidence, relation or
agency changes) and re-reviews it. It is a catch-and-repair step and is named as one
([A-17](../evidence/03-claim-index.md#a-17)). On résumés whose summaries came from a positioning brief, Fix writes no summary.
A *missing* summary is written on its own from a red button where it is missing, and nothing is
reviewed again ([A-90](../evidence/03-claim-index.md#a-90)). The
automatic repair phase that briefly preceded it was removed the same day it shipped (2026-10-12).
The product owner's position: the checks give assurance; they are not there to fix an issue.

## Evidence-side checks

- **Evidence chat.** A figure in a proposal that the person never said is reported beside the
  proposal, not removed. A correction that changes nothing is reported too
  ([K-25](../evidence/03-claim-index.md#k-25)). The interview coach's offers go through the same check; the application
  chat's do not ([D-36](../evidence/05-discrepancies.md#d-36)).
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
| Clause-level grounding of Live résumé text | Not run on Live: Verified (K-23); the grounding path Superseded, retained for measurement (K-24) | [K-23](../evidence/03-claim-index.md#k-23), [K-24](../evidence/03-claim-index.md#k-24) |
| Fix (person-pressed repair with gate) | Verified; a catch-and-repair step by design | [A-17](../evidence/03-claim-index.md#a-17) |
| Chat figure check, report-only | Verified (not run on application-chat offers, D-36) | [K-25](../evidence/03-claim-index.md#k-25) |
| Every record the chat reads carries its authority | Verified | [K-32](../evidence/03-claim-index.md#k-32) |
| A posting reaches the chat only inside what was read, as the employer's words | Limited | [K-31](../evidence/03-claim-index.md#k-31) |
| Career Chat read layer | Verified | [A-102](../evidence/03-claim-index.md#a-102) |
| Reviewer gaps never said as the employer's reasons | Verified | [A-103](../evidence/03-claim-index.md#a-103) |
| Role reading: stated only with a quote found in the posting | Verified | [A-62](../evidence/03-claim-index.md#a-62) |
| A drafted reason checked as an inference and labeled | Verified | [A-68](../evidence/03-claim-index.md#a-68) |
| Situational questions as labeled interpretations | Verified | [A-114](../evidence/03-claim-index.md#a-114) |
| Interview answers only from verified claims | Verified | [A-63](../evidence/03-claim-index.md#a-63) |
| Draft-line footnotes | Limited (approving an unsupported line triggers a redraft, D-31) | [A-64](../evidence/03-claim-index.md#a-64) |
| Application chat: lines checked by Jev, reported | Verified | [A-73](../evidence/03-claim-index.md#a-73) |
| Citations follow a line's words | Verified | [A-93](../evidence/03-claim-index.md#a-93) |
| Professional summary from a supported positioning | Verified | [A-82](../evidence/03-claim-index.md#a-82) |
| Summary writers never given the posting (the brief carries its vocabulary) | Limited | [A-83](../evidence/03-claim-index.md#a-83) |
| Summaries placed as written; findings as labels | Limited | [A-84](../evidence/03-claim-index.md#a-84) |
| Plain words; Jev reads the originals | Verified | [A-87](../evidence/03-claim-index.md#a-87) |
| Red button writes just a missing summary | Limited | [A-90](../evidence/03-claim-index.md#a-90) |
| Earlier summary paths | Superseded (replaced 2026-10-28 by `ba6f332`, `2ac4c41`) | [A-101](../evidence/03-claim-index.md#a-101) |
