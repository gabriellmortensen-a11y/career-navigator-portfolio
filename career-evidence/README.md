# Career evidence — the portfolio's learnings, importable

[`career-navigator-learnings.txt`](career-navigator-learnings.txt) carries the whole portfolio's
learnings as **career evidence** for Career Navigator itself: 39 accomplishment statements under one
role. Each statement is derived from verified claims and metrics in this repository. It adds no claim
of its own (see the [map](#where-each-statement-comes-from) below).

## Why it is shaped this way

- **Plain text, résumé layout.** The application's importer reads PDF, DOCX and plain text, not
  Markdown. It anchors on a date-range line and reads the employer and title above it. Each bullet
  becomes one piece of evidence, with the whole bullet as its span.
- **The role header matches the existing role exactly:** `Career Navigator (Independent)` /
  `Founder / Product Leader` / `Apr 2026 – Present`. The importer matches an employer by name and a
  role by title, so the statements land on that role instead of creating a new one. April 2026 is
  the start date already on that role in the record. The portfolio's earliest dated artifacts are
  from July 2026, so the last statement's "three and a half months" counts from July.
- **Written as a product owner, not an engineer.** Decisions I originated say *set*, *defined*,
  *required*, *ruled*, *chose* or *designed*. Work the agents proposed or measured, and I accepted,
  says *approved* or *accepted*. Features I put in front of users say *launched*. No statement claims
  I wrote code ([Product 01](../product/01-problem-users-and-role.md#my-role); the
  [decision log](../product/07-decision-log.md) marks which decisions were mine).
- **Qualifiers stay attached to numbers** ("one before/after run on 8 real projections", "32
  production résumés"). The résumé writer uses figures as written, so the record carries their limits.

`tools/check_import.py` runs the application's own reader on this file. The result: one role, 39
bullets, nothing unplaced, start `2026-04`.

## How to import it

1. Open **`/evidence/import`** in Career Navigator and upload `career-navigator-learnings.txt`.
   Reading the file writes nothing: it records a proposal.
2. On the proposal page, confirm the job reads as *Career Navigator (Independent)* — *Founder /
   Product Leader*. If you have renamed that role since, edit the employer or title there to match.
3. The **Résumé Writing Check** starts on upload and offers wording suggestions. Accept or decline
   each one. A suggestion that would change what a line claims is never offered.
4. Press **Approve**. Each statement becomes an ADD Change Document under that role and is indexed.

**Expected cost:** roughly ten cents, paid by your own account. That is an *estimate* from
2026-10-21 → 10-24 per-call averages: one concept-indexing model call per statement at about
$0.0018, plus the writing check's editor call or calls. It is not a measured figure.

## Things to know before you import

- **Overlap with what's already there.** Your role already holds evidence about this work.
  - Exact or contained copies are joined automatically when stories are composed.
  - Differently worded statements about the same work stay separate until composition glues them by
    Jev's "same work" question (≥ 0.6), which happens at the next job preparation.
  - Review the role on the Evidence page afterwards, and retire anything you'd rather not keep.
- **Import this file once.** Imported bullets get position-based locators
  (`career-navigator-independent-founder-product-leader-01` … `-39`), and a locator may not be
  reused. A second import of the same role would be refused for every position already used. None
  are used on Live today.

  This is a real limitation of the importer, recorded here rather than worked around. For later
  updates, add new statements through the evidence chat or Add Evidence.
- **These are statements, not stories.** Story composition and the résumé selector decide how they
  are used. Nothing here forces a bullet onto a résumé.

## Where each statement comes from

| # | Statement (short) | Evidence |
|---|---|---|
| 1 | Founded and own Career Navigator | [Product 01](../product/01-problem-users-and-role.md), [Product 03](../product/03-system-architecture.md) |
| 2 | Product owner without writing code; 652 of 683 commits co-authored by agents | [H-16](../evidence/03-claim-index.md#h-16), [M-31](../evidence/04-metric-ledger.md#m-31) |
| 3 | Discovery before representation | [Product 01](../product/01-problem-users-and-role.md#the-problem) |
| 4 | Model proposes, person approves; single governed writer | [K-10](../evidence/03-claim-index.md#k-10), [H-03](../evidence/03-claim-index.md#h-03) |
| 5 | One coherent body of work → composite foreign keys | [H-07](../evidence/03-claim-index.md#h-07), [K-01](../evidence/03-claim-index.md#k-01), [K-02](../evidence/03-claim-index.md#k-02) |
| 6 | Prompt contamination 49.5% → 3.6%; yield 19.7% → 45.7% | [M-01](../evidence/04-metric-ledger.md#m-01), [M-02](../evidence/04-metric-ledger.md#m-02) |
| 7 | Retired the per-résumé acceptance gate | [H-09](../evidence/03-claim-index.md#h-09) |
| 8 | Extraction: 5 / 6 / 5 / 7; clean-room test | [P-30](../evidence/03-claim-index.md#p-30) |
| 9 | Data-loss incident → forced row-level security | [H-17](../evidence/03-claim-index.md#h-17), [P-12](../evidence/03-claim-index.md#p-12) |
| 10 | Fix defects at the source | [Product 02 §3](../product/02-principles.md#3-defects-are-fixed-at-their-source-never-papered-over) |
| 11 | Probability model selects; models reason and write | [Product 02 §4](../product/02-principles.md#4-jev-selects-models-reason-and-write) |
| 12 | Accepted redesign: 1,164 → 68 judgments; 267 → 46 s; $0.45 → $0.04 | [M-22](../evidence/04-metric-ledger.md#m-22) |
| 13 | 461 vs 413 of 531; 93% agreement | [M-23](../evidence/04-metric-ledger.md#m-23) |
| 14 | Readings ranged by up to 3 major findings; acceptance reversed | [M-26](../evidence/04-metric-ledger.md#m-26) |
| 15 | 48/48 vs 19/48 (measurement only today) | [M-25](../evidence/04-metric-ledger.md#m-25) |
| 16 | Recruiter-selects flow; writer never sees requirements | [A-11](../evidence/03-claim-index.md#a-11), [A-12](../evidence/03-claim-index.md#a-12) |
| 17 | Bullets name their story; cross-role refusal | [A-13](../evidence/03-claim-index.md#a-13), [K-02](../evidence/03-claim-index.md#k-02), [M-56](../evidence/04-metric-ledger.md#m-56) |
| 18 | Summary shape: 73% / 96% → 0 of 20 | [M-17](../evidence/04-metric-ledger.md#m-17) |
| 19 | The most bullets: 18–20 → 10–13 bullets, reverted | [M-18](../evidence/04-metric-ledger.md#m-18) |
| 20 | Eligibility never screened; degree as risk | [A-04](../evidence/03-claim-index.md#a-04) |
| 21 | Gap = a reader would pass; 84% vs 74% on 19 résumés | [A-06](../evidence/03-claim-index.md#a-06), [M-13](../evidence/04-metric-ledger.md#m-13) |
| 22 | The model reviewers' actual verdicts override the estimate | [A-07](../evidence/03-claim-index.md#a-07) |
| 23 | Themes (13 → 1); code holds the state | [A-08](../evidence/03-claim-index.md#a-08), [A-09](../evidence/03-claim-index.md#a-09), [M-45](../evidence/04-metric-ledger.md#m-45) |
| 24 | One proposal; role confirmed by the person; Growth areas | [K-13](../evidence/03-claim-index.md#k-13), [K-28](../evidence/03-claim-index.md#k-28) |
| 25 | Discover Jobs; 297 / 92 / 54 for $1.86 | [A-30](../evidence/03-claim-index.md#a-30), [A-32](../evidence/03-claim-index.md#a-32), [M-10](../evidence/04-metric-ledger.md#m-10) |
| 26 | Assess before writing; never submit | [A-37](../evidence/03-claim-index.md#a-37), [A-39](../evidence/03-claim-index.md#a-39) |
| 27 | Apply kits: question sources decided in code | [A-38](../evidence/03-claim-index.md#a-38) |
| 28 | Bounded, cited company research | [A-50](../evidence/03-claim-index.md#a-50), [A-51](../evidence/03-claim-index.md#a-51) |
| 29 | Interview prep from chosen evidence; quick answers | [A-52](../evidence/03-claim-index.md#a-52), [A-53](../evidence/03-claim-index.md#a-53) |
| 30 | Per-task model routing with evidence | [P-02](../evidence/03-claim-index.md#p-02), [M-19](../evidence/04-metric-ledger.md#m-19), [M-20](../evidence/04-metric-ledger.md#m-20) |
| 31 | ≈ $0.11, 207 s, 17.6 bullets; one assessment run ≈ $0.02 (upper bound) | [M-03](../evidence/04-metric-ledger.md#m-03), [M-05](../evidence/04-metric-ledger.md#m-05), [M-07](../evidence/04-metric-ledger.md#m-07), [M-51](../evidence/04-metric-ledger.md#m-51) |
| 32 | One governed boundary; measured cost only | [P-01](../evidence/03-claim-index.md#p-01), [P-03](../evidence/03-claim-index.md#p-03) |
| 33 | Beta first; approved commits; full suite | [P-11](../evidence/03-claim-index.md#p-11) |
| 34 | Durable work, separate worker, backup and rollback | [P-09](../evidence/03-claim-index.md#p-09), [P-10](../evidence/03-claim-index.md#p-10), [M-29](../evidence/04-metric-ledger.md#m-29) |
| 35 | Privacy in the design | [P-14](../evidence/03-claim-index.md#p-14), [A-38](../evidence/03-claim-index.md#a-38), [A-55](../evidence/03-claim-index.md#a-55), [A-56](../evidence/03-claim-index.md#a-56) |
| 36 | Capability registry: 45 capabilities, 6 flows | [P-06](../evidence/03-claim-index.md#p-06) |
| 37 | This portfolio: claims, metrics, discrepancies | [evidence/](../evidence/00-README.md) |
| 38 | Rules in prose get undone; moved into enforcement | [H-12](../evidence/03-claim-index.md#h-12), [Case study 06](../case-studies/06-operating-the-human-agent-loop.md) |
| 39 | From design documents to the current application | [H-01](../evidence/03-claim-index.md#h-01), [EVOLUTION](../EVOLUTION.md) |
