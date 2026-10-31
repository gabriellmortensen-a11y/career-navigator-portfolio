# Evidence — what every claim rests on

This folder is authoritative for **every status and every number** in the portfolio
([COMPATIBILITY](../COMPATIBILITY.md#one-home-per-topic)).

| # | Document | Contents |
|---|---|---|
| 01 | [Baseline](01-baseline.md) | What the earlier retrospective was, which commit it describes, how it is used, its limitations |
| 02 | [Source inventory](02-source-inventory.md) | Every source, how it was accessed, what rests on it, what was deliberately not used |
| 03 | [Claim index](03-claim-index.md) | 116 claims (Knowledge, Product, Applications, History), each with status, evidence and how it was verified |
| 04 | [Metric ledger](04-metric-ledger.md) | Every published number: definition, sample, period, source, kind, system state, limits |
| 05 | [Discrepancies](05-discrepancies.md) | 39 places where documents, comments or rules disagree with the code at Live `00eac95` |
| 06 | [Verification log](06-verification-log.md) | How the evidence was gathered and checked, and the publication checks this release passed |

**How to read a citation:**
- `K-`, `P-`, `A-` and `H-` IDs are claims.
- `M-` IDs are metrics.
- `D-` IDs are discrepancies.
- File paths such as `app/resume/recruiter_flow.py` refer to the private application repository at
  Live commit `00eac95` (release 2026.10.1). Commits that Live's rebuild by cherry-pick left out of its
  history are cited by their identical copies.
- Short hashes such as `5d50ba7` are commits in that repository. Hashes noted as "beta4" belong to the
  earlier build.
