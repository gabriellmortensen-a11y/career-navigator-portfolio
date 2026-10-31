# Changelog

This file records portfolio releases. Portfolio versions use calendar versioning and are
independent of the section versions and of the application's commits
([COMPATIBILITY](COMPATIBILITY.md#versions)).

## Unreleased

Changes since 2026.10.0 that no release pins yet. They add ways to find and cite what is already
here; no claim, status or number changes.

### Added
- **Decision IDs.** Every row of the [decision log](product/07-decision-log.md) has a stable ID,
  `DEC-01` to `DEC-36`, in a new first column, with its own anchor (for example
  [`#dec-01`](product/07-decision-log.md#dec-01)). Order and wording are unchanged.
- [INSPECT.md](INSPECT.md): where to inspect each kind of artifact (product overview, architecture,
  decisions, security and authorization, testing and verification, observability, integrations,
  case studies, claims, metrics and discrepancies, releases, examples), each linked to the exact
  file, section or anchor, with a short authorship note. Linked from the README's reading paths.

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
  Journey "Upcoming" card), which this release does not cover.
