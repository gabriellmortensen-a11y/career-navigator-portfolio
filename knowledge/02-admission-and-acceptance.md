# Knowledge 02 — Admission and acceptance

*Knowledge 3.0 · describes Live `7322289` (2026-10-24)*

**The question this answers:** how does information become part of someone's career record, and
who decides?

## The rule

> A model may propose. Only a person may approve.

This rule predates the current application. It appears in the first version of the previous build's
agent instructions (August 2026), and it survived every rebuild since
([H-03](../evidence/03-claim-index.md#h-03)). What changed is how it is enforced. It used to be prose
that agents were asked to follow. Today it is a single writer with a versioned contract, and the
database refuses writes that break it.

## One writer, three operations

Every authoritative row (source, claim, event, link) is written by one module through a
**Change Document**. There are three operations:

| Operation | What it does | Who triggers it |
|---|---|---|
| **ADD** | Writes a new story from the person's text, one claim per span they ticked | A person's press |
| **COMPOSE** | Glues fragments of the same work, within one role, into one story | The system (Jev decides), during job preparation |
| **RETIRE** | Retires a story; a correction names its replacement | A person, "by saying it is wrong and pressing Save" |

How a Change Document moves from proposal to record:
1. **Admission is deterministic.** The contract is checked in code: the required fields are present,
   every span is a *verbatim substring* of the text, and length limits hold. No model is involved
   ([K-10](../evidence/03-claim-index.md#k-10)).
2. **The contract is frozen at proposal.** Its version and hash are stored on the change, so applying
   it later re-validates against the rules the person saw, not today's rules.
3. **One press finishes it.** Admit, write and index happen together. If indexing fails, the
   evidence stays authoritative and the index step can be retried.
4. **Refusals are kept.** Database checks require an applied change to say what it wrote and a
   refused change to say why.

**Enforcement and its limits.** A test fails the build if any other module constructs an
authoritative row ([K-11](../evidence/03-claim-index.md#k-11)). It is a text scan with an
allowlist, not a structural guarantee. It does not cover the legacy importers. It has also produced
a false positive: a background runner's `threading.Event()` tripped it, so the import was renamed.

## Every way in

| Path | Who proposes | The human decision | Status |
|---|---|---|---|
| **Add Evidence** page | The person writes; sentences are offered by rule | Tick spans → Propose → Apply | Verified |
| **Résumé import** | A deterministic parser (no model); an optional editor model *suggests* wording | Proposal page shows every job, with editable employer and title; accept or reject each suggestion; Approve | Verified ([K-12](../evidence/03-claim-index.md#k-12)) |
| **Evidence chat** | One governed model call proposes an add, correction, enrichment or retirement | Save, and for an addition, **confirm the role** (the chat's guess is preselected and marked): "it should confirm what role it was with, even if it thinks it knows" | Verified ([K-13](../evidence/03-claim-index.md#k-13)) |
| **Guided gap discovery** (inside the chat) | One question per turn; *code* decides when to stop | One consolidated proposal, then Save. "Stopping is never saving." | Verified ([A-08](../evidence/03-claim-index.md#a-08)) |
| **Gap panel** on a résumé review | The person types; a model checks it against the requirement | "Save all" is the only act that creates evidence | Verified, but the "closes the gap" verdict is a model judgement ([K-14](../evidence/03-claim-index.md#k-14)) |
| **Brought résumé, "Accept as is"** | The same parser | One press on the review page. **There is no proposal page**, which contradicts the importer's own docstring | Limited ([D-05](../evidence/05-discrepancies.md#d-05)) |
| **Story composition** | Jev "same work" | **None**: automatic, no new claims, reversible | Limited ([K-06](../evidence/03-claim-index.md#k-06)) |

Saving a job posting (Quick add, flagship occupations) is not an evidence path. A requirement
"guides; it is never a source of career claims."

## Corrections, duplicates and flags

- **Corrections are built by code.** The chat proposes only *wrong* and *right*. Code builds the
  corrected story by exact replacement, records it, and retires the old one with `replaced_by`. An
  empty *right* means removal (2026-10-24) ([K-15](../evidence/03-claim-index.md#k-15)).
- **Duplicates are removed conservatively.** Only word-for-word copies are taken. A differently
  worded piece that Jev calls "the same work" is never removed for the person
  ([K-16](../evidence/03-claim-index.md#k-16)).
- **Already on the record.** A deterministic phrase-overlap test runs first, then Jev's `COVERS`
  question. An addition the record already says in full is not offered.
- **Flagged evidence is not used.** A deterministic reading flags a story that generalises, measures
  nothing and names no act. The person's Flag or Unflag overrides it either way. Flagged stories are
  excluded from résumés and shared links. The product owner decided this on 2026-10-14, after a
  résumé opened a role with a flagged belief-statement ([K-17](../evidence/03-claim-index.md#k-17)).
  The résumé-side test is a source inspection, not a behavioural test.
- **Restore is planned, not built.** The RETIRE contract says reversal is "clearing `retired_at`",
  but no code path un-retires evidence today ([K-18](../evidence/03-claim-index.md#k-18)).

## Failures that shaped this

Each failure was fixed at the stage that produced it; none was patched downstream.

1. **Work filed under the wrong job** (2026-10-07). A synthetic test résumé put two quantified
   results under a 2011 role.
   - *Cause:* the parser ran one job into the next, and a role chosen in Add Evidence was created
     undated.
   - *Fixed at:* the parser (it now reports unplaced text instead of guessing), role creation (it
     keeps stated dates), and a new schema constraint on bullets ([K-02](../evidence/03-claim-index.md#k-02)).
2. **A cleanup script bypassed tenancy while it was being built** (2026-10-05).
   - *What happened:* a script connected as the schema owner deleted 17,183 rows across 50 tables
     ([M-55](../evidence/04-metric-ledger.md#m-55)) for
     every account. The re-import then nearly resurrected 215 of 221 retired events.
   - *Changed in the same commit:* row-level security forced, a runtime role that owns nothing, an
     account stamped by default, imports that require an explicit account, and retirements carried
     through re-import. What could not be restored is documented,
     not re-pinned ([P-12](../evidence/03-claim-index.md#p-12)).
3. **A double press recorded a story twice**, and "remove the duplicate" offered to retire a
   differently worded piece (2026-10-16).
   - *Fixed at:* Save now claims the turn atomically before writing, and duplicate removal takes only
     exact copies ([K-16](../evidence/03-claim-index.md#k-16)).
4. **The chat filed an addition under its own guess of the role** (2026-10-22).
   - *Fixed at:* Save files an addition only under the role shown on the card, which the person
     confirms or changes (the chat's guess is preselected and marked)
     ([K-13](../evidence/03-claim-index.md#k-13)).

## Where the implementation and the rule still disagree

Some things listed here as limited are deliberate, and they are named rather than hidden:
- Story composition writes without a person's press.
- A brought résumé is recorded without its proposal page.
- Concept indexing at apply time is a model choosing concepts from a vector shortlist. It predates
  the "Jev selects" rule ([P-05](../evidence/03-claim-index.md#p-05)).

See [Discrepancies](../evidence/05-discrepancies.md).
