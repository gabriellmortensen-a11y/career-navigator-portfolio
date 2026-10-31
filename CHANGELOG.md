# Changelog

This file records portfolio releases. Portfolio versions use calendar versioning and are
independent of the section versions and of the application's commits
([COMPATIBILITY](COMPATIBILITY.md#versions)).

## 2026.10.1 — 2026-10-31

Describes Live a week later. The application gained an interview coach, an application chat, a chat
on every page that can read the account, Growth action plans, a rebuilt way of writing résumé
summaries, and a living résumé that can show a GitHub portfolio. This release describes those,
re-verifies every earlier claim against the new commit, and corrects what had become false.

**Pins:** Knowledge 3.1 · Product 4.1 · Applications 5.0 · describes Live `00eac95` (2026-10-31)
· baseline unchanged (the 2026-09-30 case-study source package, earlier build `38f4bbf`).

### Added
- **[Applications 07](applications/07-navi-and-career-chat.md): Navi, the chat on every page.** The
  tab that opens the page's own chat, the rail, and Career Chat's governed, read-only access to the
  account.
- **The interview coach** ([Applications 05](applications/05-research-and-interview-prep.md)) and a new
  diagram, [Architecture 08](architecture/08-interview-coach.md).
- **The application chat**, the Upcoming card and the opportunities pane's labels
  ([Applications 04](applications/04-discovery-to-application.md)).
- **Growth action plans** ([Applications 02](applications/02-gap-conversations.md)).
- **The living résumé** (formerly "Share my career conversation") and **the GitHub portfolio behind
  it** ([Applications 06](applications/06-sharing-and-integrations.md)). This repository is the one
  connected to my own living résumé.
- **Résumé summaries from a supported positioning**, bullets written as their finished line, and
  citations that follow a line's words ([Applications 03](applications/03-resume-planning-writing-review.md),
  [Architecture 04](architecture/04-resume-flow.md)).
- **Asking the living résumé about a portfolio document.** A visitor can ask it to show or summarize
  a document ("case study 1", then "summarize it"), and the answer is written from that document
  ([A-123](evidence/03-claim-index.md#a-123)).
- **Evidence:** claims K-31–K-34, P-33–P-37 and A-61–A-123; metrics M-60–M-82 (Live telemetry,
  re-queried on 2026-10-31, for M-60 and M-67–M-71); discrepancies D-25–D-39; decisions DEC-37–DEC-75.
- **Decision IDs.** Every row of the [decision log](product/07-decision-log.md) has a stable ID with
  its own anchor (for example [`#dec-01`](product/07-decision-log.md#dec-01)). Added to the published
  repository on 2026-10-31, before this release.
- [INSPECT.md](INSPECT.md): where to inspect each kind of artifact, linked to the exact file, section
  or anchor. Added on 2026-10-31, before this release, and extended in it.

### Changed
- **Applications 4.0 → 5.0**: capabilities added (above) and removed. *Tune my evidence* was retired
  ([A-107](evidence/03-claim-index.md#a-107)). Interview Prep's *Prepare* button, *Quick answers* link
  and walkthrough link went with the card that held them ([A-52](evidence/03-claim-index.md#a-52),
  [D-39](evidence/05-discrepancies.md#d-39)).
- **Product 4.0 → 4.1**: Beta and Live no longer run the same code. Since 2026-10-28 Live is its own
  line, with three Beta-only evidence features left off ([P-37](evidence/03-claim-index.md#p-37)).
  Assessment has one stated model exception ([DEC-47](product/07-decision-log.md#dec-47)).
- **Knowledge 3.0 → 3.1**: new paths that *offer* changes to the record (all still through the
  person's Save), new things that are never evidence, and authority labels on what the chat reads.
- Commit hashes that are no longer in Live's history, because Live was rebuilt by cherry-pick, are
  replaced by their identical copies.

### Corrected
- [A-19](evidence/03-claim-index.md#a-19) said saving person edits re-ran the review. It never did,
  and a test says so.
- [A-21](evidence/03-claim-index.md#a-21) said the reverted experiment was not in Live's history. Its
  two commits are, and they cancel out.
- [D-01](evidence/05-discrepancies.md#d-01) cited a file path that does not exist.
- The Upcoming card, which 2026.10.0 noted as not covered, is now described
  ([A-72](evidence/03-claim-index.md#a-72)).

### Verified for this release
- Every existing claim and discrepancy was re-checked against `00eac95` (the investigations read
  `79658ad`; the three commits after it, "Make all public" `821b151` and the document summaries
  `d6e7c36` and `00eac95`, touch only the portfolio module and the living résumé, read in full). See
  [evidence/06](evidence/06-verification-log.md).
- Live telemetry re-queried read-only on 2026-10-31, my account only
  ([M-60](evidence/04-metric-ledger.md#m-60), [M-67](evidence/04-metric-ledger.md#m-67)–[M-71](evidence/04-metric-ledger.md#m-71)).
- The full test suite passed on `00eac95` before its deploy ([M-79](evidence/04-metric-ledger.md#m-79)).
- An independent review spot-checked 109 claims; 88 held as written. Its 42 findings (17 factual, 10
  overclaims, 11 consistency, 4 quotes, no public-safety finding) were all corrected, four claims moved
  from Verified to Limited ([evidence/06](evidence/06-verification-log.md#2026101--independent-review)).
- The two withheld findings ([D-02](evidence/05-discrepancies.md#d-02), [D-17](evidence/05-discrepancies.md#d-17))
  stay withheld; their status was not re-examined in this release.

## 2026.10.0 — 2026-10-25

First release of this portfolio repository.

**Pins:** Knowledge 3.0 · Product 4.0 · Applications 4.0 · describes Live `7322289` (2026-10-24)
· baseline: the 2026-09-30 case-study source package (earlier build `38f4bbf`).

### Added
- Front door ([README](README.md)) with reading paths for hiring managers and technical reviewers,
  and a [GLOSSARY](GLOSSARY.md).
- [LICENSE](LICENSE): all rights reserved; published for reading and evaluation.
- **Knowledge 3.0** (supersedes Knowledge layer 2.2 of 2026-07-08): evidence model, admission and
  acceptance, provenance and support, incomplete information.
- **Product 4.0** (supersedes Product layer 3.0): problem, users and role; principles with their
  origins and exceptions; architecture; model routing, cost and latency; quality and measurement;
  operations and privacy; decision log.
- **Applications 4.0** (supersedes Application layer 3.0): job analysis and assessment; gap
  conversations; résumé planning, writing and review; discovery to application; research and
  interview preparation; sharing and integrations.
- Six case studies: governed evidence; unsupported claims; evaluation quality, latency and cost;
  discovery to application; gap conversations; operating the human/agent loop.
- Nine Mermaid diagrams with one legend (code, Jev, model, human, storage, external), rendered to SVG.
- Evidence: baseline, source inventory, claim index (116 claims), metric ledger (59 metrics),
  discrepancies (24), verification log.
- [EVOLUTION](EVOLUTION.md) from the layer documents to the current application, and a separated
  [ROADMAP](ROADMAP.md).
- Sanitized examples: verbatim governed prompts, a model-routing excerpt, aggregate run telemetry,
  and a synthetic end-to-end walkthrough.
- [career-evidence/](career-evidence/README.md): the learnings as an importable career-evidence file
  for Career Navigator, checked against the application's own parser.
- Publication checks in `tools/`: links and anchors, Mermaid rendering, sensitive content and
  unfinished markers, and the import shape.

### Verified for this release
- Metric leads checked against sources:
  - contamination 49% → 4% and admission yield 20% → 46%: **verified** (historical, QC-1);
  - résumé cost: **≈ $0.11** in writing and review model calls, plus **≈ $0.02** per assessment run.
    The "$0.15 per résumé" lead is not a single measured figure;
  - "21 applications in ~40 minutes": **not corroborated**;
  - model trial and discovery pilot: **recorded with their limits**.
  See the [metric ledger](evidence/04-metric-ledger.md).
- Discrepancies found in the application are recorded, not fixed ([evidence/05](evidence/05-discrepancies.md)).
- Two open security and privacy findings in the application are listed but their details are
  withheld until fixed ([D-02](evidence/05-discrepancies.md#d-02), [D-17](evidence/05-discrepancies.md#d-17)).
- An independent review found 17 factual errors, 13 overclaims and 13 unsourced numbers before release.
  All were corrected ([evidence/06 §5](evidence/06-verification-log.md#5-independent-review-before-release)).
- Describes Live as of 2026-10-24 (`7322289`). Live received one more commit on 2026-10-25 (a My
  Journey "Upcoming" card), which this release does not cover. (Covered in 2026.10.1.)
