# Compatibility — how the sections relate

This portfolio has three independently versioned sections, plus supporting material. This document
says what each section is responsible for, which versions go together, and the vocabulary they all
share.

## The three sections

The split continues the July 2026 layer model, but the content was rewritten from the implemented
system ([H-01](evidence/03-claim-index.md#h-01)).

| Section | Answers | Owns | Depends on |
|---|---|---|---|
| **[Knowledge](knowledge/00-README.md)** | *What is true about the person, and how does the system know?* | The evidence model, admission and acceptance, provenance and support, incomplete information | Nothing |
| **[Product](product/00-README.md)** | *Why does it exist, how should it decide, and how is it run?* | Problem and role, principles, architecture, model routing and cost, measurement, operations, decisions | Knowledge (it governs how evidence may be used) |
| **[Applications](applications/00-README.md)** | *How does the record turn into help with a real job search?* | Job analysis, gap conversations and Growth plans, résumés, discovery to application, the interview coach, the living résumé and sharing, Navi (the chat on every page) | Knowledge (it reads only accepted evidence); Product (it obeys the principles) |

**Supporting material** is not versioned separately. It is pinned by the portfolio release:

| Folder | Role | Authority |
|---|---|---|
| [case-studies/](case-studies/00-README.md) | Narratives of decisions and learning | Link to the sections for mechanism and to `evidence/` for numbers; never the authoritative description of behavior |
| [architecture/](architecture/00-README.md) | Diagrams | Authoritative for diagrams; the prose lives in Product 03 and the section documents |
| [evidence/](evidence/00-README.md) | Baseline, sources, claim index, metric ledger, discrepancies, verification log | **Authoritative for every status and every number** |
| [assets/](assets/examples/README.md) | Sanitized examples and rendered diagrams | Illustrative; Mermaid source in `architecture/` wins |
| [career-evidence/](career-evidence/README.md) | The portfolio's learnings as importable career evidence | Derived from the claim index; carries no new claims |
| [GLOSSARY.md](GLOSSARY.md) | Definitions of terms | Definitions only; no claims |

## One home per topic

To avoid two authoritative versions of anything, each topic has exactly one home. Other documents
link to it.

| Topic | Home |
|---|---|
| What a capability does and its status | The section document, with the claim in [evidence/03](evidence/03-claim-index.md) |
| Any number | [evidence/04 metric ledger](evidence/04-metric-ledger.md) |
| Where docs and code disagree | [evidence/05 discrepancies](evidence/05-discrepancies.md) |
| Why something was decided | [Product 07 decision log](product/07-decision-log.md) |
| History before and since the baseline | [EVOLUTION](EVOLUTION.md) |
| Future work | [ROADMAP](ROADMAP.md) |

## Versions

**This release: Portfolio 2026.10.1** (2026-10-31). The portfolio uses calendar versioning
(`YYYY.MM.patch`), so its versions can never be confused with section versions, the historical layer
versions, or the application's commit identifiers.

| Portfolio release | Knowledge | Product | Applications | Describes application | Baseline |
|---|---|---|---|---|---|
| **2026.10.1** (2026-10-31) | **3.1** | **4.1** | **5.0** | Live `00eac95` (2026-10-31). Since 2026-10-28 Beta is a separate line ([P-37](evidence/03-claim-index.md#p-37)) | Unchanged |
| 2026.10.0 (2026-10-25) | 3.0 | 4.0 | 4.0 | Live `7322289` (2026-10-24); Beta `2a5f749`, identical tree | Case-study source package of 2026-09-30, earlier build `38f4bbf` |
| *(historical, not a portfolio release)* | 2.2 (2026-07-08) | 3.0 (2026-07-08) | 3.0 (2026-07-08) | None: written before the software | — |

**Section version rules:**
- **Major** when the section's model changes: a new unit of evidence, a new authority boundary, a new
  principle, a capability added or removed.
- **Minor** when content is added or a status changes without a model change.
- **Patch** for corrections.

A portfolio release pins one version of each section and one application commit. Section numbering
continues the historical layers (Knowledge 2.2 → 3.0; Product and Application 3.0 → 4.0) so the
lineage is visible. The historical layers are not carried forward as current content.

**Compatibility rules:**
1. A section may cite only claims and metrics that exist in the `evidence/` of the same release.
2. Applications may describe a capability only if Knowledge permits the evidence use it relies on.
   For example, Growth areas and their action plans are never evidence, so nothing that writes for an
   employer reads them; a living-résumé link may say a limit only where the owner ticked it.
3. If the application commit changes, every "describes Live …" line and every status must be
   re-verified before the release is cut ([evidence/06](evidence/06-verification-log.md)).

## Status vocabulary

Used in every section, the claim index and the case studies.

| Status | Meaning | Minimum evidence |
|---|---|---|
| **Verified** (implemented and verified) | In the code at the described commit, switched on for Live, and exercised by tests that target the behavior | Code + targeted tests (+ telemetry where available) |
| **Limited** (implemented, limited verification) | In the code and on Live, but the tests are weak (source inspection, stubs, static checks), the measurement is small or single-account, or a known defect affects it | Code + something weaker than a targeted test |
| **Experimental** | Built, but only on Beta, behind the experiments switch, on a branch, or tried and reverted | Code or commits on a non-Live path |
| **Planned** | Designed or requested, with no implementation; includes "requested, not started" | A stated intent; no code |
| **Superseded** | Built and replaced. The replacement and its commit are named | Code or history + the replacing commit |
| *Verified (historical)* | True of an earlier system and checked against its records; says nothing about the current system | Baseline ledger fact + commit check |

**Other terms:**
- **"Jev"** is an external probability model (TypeSafe's Jev). It is asked fixed, typed yes/no
  questions and returns probabilities. The product uses it to rank, select and decide states.
- **"Model"** without qualification means a language model: gpt-5-mini, Claude Haiku, or gpt-5 for
  measurement.
- **"The reviewers"** are the app's two model personas (recruiter and hiring manager), never people.
