# Applications 03 — Résumé planning, writing and review

*Applications 4.0 · describes Live `7322289` (2026-10-24) · diagram: [Architecture 04](../architecture/04-resume-flow.md) · case study: [02](../case-studies/02-preventing-unsupported-claims.md)*

**The question this answers:** how does the system turn selected evidence into a résumé, and what
keeps the writing from claiming more than the evidence shows?

## The design in one paragraph

Selection decides *which evidence* goes on the page. A selector (a model playing a recruiter) sees
the job's requirements and the candidate stories, and answers with story **numbers** only. Code
copies the chosen stories, verbatim, into the writer's prompt. **The writer never sees the
requirements, the posting or anything the selector wrote.** Each bullet comes back tagged with the
story it was written from, through a schema the API enforces. Reviewers and one editor pass read the
finished page and **report**; they don't rewrite it. This is the "recruiter-selects" flow, live since
2026-10-14 ([A-11](../evidence/03-claim-index.md#a-11)).

## Who decides what

| Role | Kind | Decides |
|---|---|---|
| **Selection** | Code + Jev | Each requirement's chosen story and alternates; the story pool sized to the page |
| **Selector** ("recruiter") | Language model | Which stories go in each section, and which draft pieces to keep, by number |
| **Writer** | Language model | The wording of each section from the stories it was handed |
| **Editor** | Language model + code gate | Spelling, grammar and mechanical corrections only, as an overlay |
| **Reviewers** (recruiter, hiring manager) | Language model ×2 | Report coverage, importance and impact per requirement; advance yes/no |
| **Person** | Human | Press Write; reword, remove, reorder lines; press Fix; accept |

## Stage by stage: what each stage receives

| # | Stage | Kind | Receives | Sees requirement or posting text? | Produces |
|---|---|---|---|---|---|
| 1 | Write press | Human | — | — | A queued run; refused without an assessment ([A-37](../evidence/03-claim-index.md#a-37)) |
| 2 | Evidence documents | Code | Stories | No | Canonical, hashed text per story |
| 3 | Selection | Code (+ Jev on ties) | The frozen assessment reading | Jev only, on ties | Chosen story per requirement, alternates |
| 4 | Flag filter | Code + person's flags | Stories | No | Flagged stories removed ([K-17](../evidence/03-claim-index.md#k-17)) |
| 5 | Shared facts | Embeddings + Jev | One role's story sentences | No | Sentences two stories share, given to one of them ([A-14](../evidence/03-claim-index.md#a-14)) |
| 6 | Selector: pick stories | **Model** | Job title, every requirement (R1…Rn), numbered whole stories | **Yes** | Numbers only |
| 7 | Writer: draft | **Model** | The picked stories, copied by code, in the selector's order; the writing rule | **No.** A runtime guard refuses the call if the requirements block appears | Bullets `{story n, text}`, the number held to an enum; or summary text |
| 8 | Selector: keep pieces | **Model** | Requirements + numbered draft pieces | **Yes** | Numbers only |
| 9 | Writer: tighten | **Model** | Kept pieces only + limits (bullet ≤ 25 words; summary at most 3 sentences of at most 15 words; role summary at most 2; requested in the prompt) | **No** | Final bullets (schema) and sentences |
| 10 | Store | Code | — | — | Bullets with their story's event id, stored `UNGROUNDED`; the database refuses a cross-role citation ([K-02](../evidence/03-claim-index.md#k-02)) |
| 11 | Competencies | **Model** | Bullets only (the posting is a forbidden input, checked) | **No** | Competencies with citations; uncited ones dropped |
| 12 | Page fit | Code (+ Jev first-minute bullets) | Bullets, the exported PDF | Jev only | Cuts from the end of the selector's order; never empties a role ([A-18](../evidence/03-claim-index.md#a-18)) |
| 13 | Coverage review | **Model ×2** | Requirements (no eligibility lines; education labelled a risk), the finished lines, readability measures | **Yes** (never the career record) | One row per requirement per seat; **report only** ([A-15](../evidence/03-claim-index.md#a-15)) |
| 14 | Editor | **Model** → code gate → **model** verify | Résumé lines only | **No** | Corrections as an overlay: no new figure or name, no negation change, ≤ 6 words ([A-16](../evidence/03-claim-index.md#a-16)) |
| 15 | Repeat labels | Jev | Bullets, summary pieces | Jev only | "Repeats line N" labels; **nothing removed** |
| 16 | Readability | Code | The rendered page | No | Findings, report only |
| 17 | What's next | **Model** | The review and the nearest evidence | Yes | Actions, e.g. "this story states no result: add one" |
| 18 | Person edits | Human | — | — | Reword, remove, reorder; the review re-runs ([A-19](../evidence/03-claim-index.md#a-19)) |
| 19 | Fix (optional) | Human → **model** → code gate → re-review | One line, its findings and its own evidence | **No** | A repaired line or summary, at most two attempts ([A-17](../evidence/03-claim-index.md#a-17)) |

### Exactly how requirement text is withheld

Three things keep requirement text out of the writer ([A-12](../evidence/03-claim-index.md#a-12)):
1. Code builds every writer prompt from story text, the writer's own draft and policy text.
2. The selector's reply is parsed into integers, so nothing it writes reaches the writer.
3. A unit test asserts that no writer prompt contains the requirements.

**The limits of that enforcement:**
- The runtime guard is a **substring check**. It catches the requirements heading or the whole
  block, not one requirement's wording, and no test exercises the guard itself.
- The writer's declared "forbidden inputs" (requirements, posting) are documentation in this flow.
  The check that would enforce them is not called ([D-07](../evidence/05-discrepancies.md#d-07)).
- Requirement wording can still enter **through the evidence**. The gap chat drafts stories with the
  requirement in view, and the person saves them. The chat policy tells the model not to borrow the
  posting's words; that is a prompt rule, not a code check.

## Why this design

| Alternative | What happened |
|---|---|
| Writer sees requirements, checks catch overreach (older flow) | Copied posting phrases had to be detected and dropped: 52 of 265 bullets on Beta, nearly all one test account, and 2 of 220 on Live ([M-43](../evidence/04-metric-ledger.md#m-43)). Relation and agency checks refused lines after the fact. Grounding took two thirds of a 14-minute run ([A-20](../evidence/03-claim-index.md#a-20), [M-35](../evidence/04-metric-ledger.md#m-35)) |
| Automatic repair after review | Shipped and removed the same day: it was catch-and-repair ([Product 02 §3](../product/02-principles.md#3-defects-are-fixed-at-their-source-never-papered-over)) |
| Content-plan branch: labelled story parts, evidence-isolated writing | Built on a branch (12 commits), superseded before deployment |
| **Recruiter-selects (chosen)** | I did by hand what I wanted the system to do, and it beat every engineered variant. My instruction: do exactly that, and "never pass on to the writer text of what to write from the recruiter" |

## Measured behaviour (Live, 32 résumés, 2026-10-21 → 10-24)

| Measure | Value |
|---|---|
| Bullets per résumé | mean 17.6, range 9–30 ([M-07](../evidence/04-metric-ledger.md#m-07)) |
| Language-model cost | ≈ $0.11 per résumé ([M-03](../evidence/04-metric-ledger.md#m-03)) |
| Wall clock | median 207 s ([M-05](../evidence/04-metric-ledger.md#m-05)) |

**Summary length was fixed by the shape of the request.** Asked for one text "of at most N words",
73% of executive summaries and 96% of role summaries were over the readability limit. Asked for at
most three sentences of at most 15 words (two for a role summary), 0 of 20 were. The shape is still
a prompt request, not an enforced schema ([M-17](../evidence/04-metric-ledger.md#m-17)).

## Residual risks

The design is **not hallucination-proof**:

1. **No code compares final text with the evidence on Live.** Every bullet is stored `UNGROUNDED`.
   The writer's "use only the facts in the text above" is a prompt rule. Reviewers and the editor
   are deliberately not shown the career record ([K-23](../evidence/03-claim-index.md#k-23)).
2. **Ownership inflation is not checked at build time.** For example, "supported" becoming "led".
   The relation and agency checks exist but run only inside Fix ([D-08](../evidence/05-discrepancies.md#d-08)).
3. **Strong evidence can still be written weakly.** A measurement recorded in a Beta commit found about
   1 in 6 requirements assessed *strong* came out partial or absent on the reviewed résumé
   ([M-57](../evidence/04-metric-ledger.md#m-57)). Telling the
   selector which story shows which requirement shortened résumés from 18–20 bullets to 10–13 with
   no reviewer gain, so it was reverted ([A-21](../evidence/03-claim-index.md#a-21),
   [M-18](../evidence/04-metric-ledger.md#m-18)).
4. **Conflicting figures in the record go undetected** in this flow (the check exists only in the
   older path).
5. **Some limits are requested, not enforced.** "One bullet per story" and the summary sentence
   counts are prompt instructions. Since 2026-10-24 a split story is attributed correctly, but it is
   not prevented.
6. **A story containing the literal word "REQUIREMENTS" would trip the guard** and fail the run.

The controls that do exist are structural: the writer's inputs, story attribution by schema, the
database's role boundary, and the editor's gate. The coverage review reports anything it finds a
reader would notice.

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Recruiter-selects flow | Verified | [A-11](../evidence/03-claim-index.md#a-11) |
| Writer withheld from requirements | Limited (unit test + substring guard; declared check not executed) | [A-12](../evidence/03-claim-index.md#a-12) |
| Bullet → story attribution by schema | Verified | [A-13](../evidence/03-claim-index.md#a-13) |
| Shared-sentence de-duplication | Limited (thresholds set on one record) | [A-14](../evidence/03-claim-index.md#a-14) |
| Coverage review, report only | Verified | [A-15](../evidence/03-claim-index.md#a-15) |
| One editor pass with code gate | Verified | [A-16](../evidence/03-claim-index.md#a-16) |
| Fix (person-pressed repair) | Verified; catch-and-repair by design | [A-17](../evidence/03-claim-index.md#a-17) |
| Printed-page fit | Verified | [A-18](../evidence/03-claim-index.md#a-18) |
| Person edits | Verified | [A-19](../evidence/03-claim-index.md#a-19) |
| Older writer with post-hoc checks | Superseded | [A-20](../evidence/03-claim-index.md#a-20) |
| Selector told story strengths | Experimental, reverted | [A-21](../evidence/03-claim-index.md#a-21) |
| Clause-level grounding on Live | Superseded on the Live path | [K-23](../evidence/03-claim-index.md#k-23), [K-24](../evidence/03-claim-index.md#k-24) |
