# Evidence 02 — Source inventory

Every source this portfolio draws on: what it is, how it was accessed, and which claims rest on it.
None of the private sources is copied into this repository.

| # | Source | Access | Supports | Visibility |
|---|---|---|---|---|
| S1 | **Application repository at Live `7322289`** (2026-10-24): code, tests, governed seed documents, `docs/`, migrations | Read-only export of the commit; nothing run | All current-system claims (`K-`, `P-`, `A-`); discrepancies `D-01`–`D-23` | Private |
| S2 | **Application git history** (root `0a83529`, 2026-10-03 → `7322289`; Beta `2a5f749`) | `git log` / `git show`; reflog of the Live branch for push times | Dates, triggers, decisions, commit-message measurements; `M-11`, `M-16`–`M-18`, `M-22`–`M-24`, `M-29`, `M-31`, `M-35`–`M-38`, `M-43`–`M-45` | Private |
| S3 | **Earlier build ("beta4")**, `38f4bbf` → `6a9ab0c` | `git log` / `git show` | Bridge from the baseline; `H-04`–`H-15` hashes | Private |
| S4 | **Baseline case-study source package** (2026-09-30) | Read; a digest was produced | All `H-` claims; `M-01`, `M-02`, `M-32`–`M-34`, `M-42` | Private (contains career records) |
| S5 | **Predecessor repository** (layer documents v2.2 / v3.0 / v3.0) | Headers and structure read | `H-01`, `H-02`, `D-24` | Private (libraries are career records) |
| S6 | **Observability side project** (QC-1 fixture) | Fixture re-summed | `M-01`, `M-02` | Private |
| S7 | **Live database, read-only aggregates** (2026-10-25) | `default_transaction_read_only=on`; aggregate SQL over the call ledger, résumé runs, reviews, status events, discovery runs and openings, model checks and kits; one role row read to align the career-evidence import | `M-03`–`M-08`, `M-10`, `M-11`, `M-21`; `K-23`, `P-07`, `P-17`, `D-21` | Private; only aggregates published |
| S8 | **Live host configuration** | Feature-switch names and values only; no secrets read or printed | Which capabilities are on for Live | Private |
| S9 | **Live endpoint probe** | Two unauthenticated GETs on the host's loopback | `A-56`, `D-01` | — |
| S10 | **Session records** (my project notes from working sessions) | Read | Only where labelled "session record": `K-07`, `M-12`, `M-21` (Beta probe), `M-30` (run result), `M-46`, `M-47` | Private |
| S11 | **Owner accounts** (GAB-001…005 in S4) | Read | Role framing, the origin of the product, Bounded Fit's adoption, `H-07`, `H-16`, `H-18` | Private; quoted with attribution |
| S12 | **Model-assignment evidence** (`app/documents/seeds/model_assignments_v1.md` in S1) | Read | `M-19`, `M-20`; routing rationale | Private (excerpted in [assets](../assets/examples/model-assignment-excerpt.md)) |
| S13 | **Public landing page** (`mynavigator.me`) | Read | Brand framing only | Public |

## What was deliberately not used

- **Personal career text** of any kind: résumés, evidence pieces, chat transcripts, interview
  material.
- **Employers and job targets** from my applications, and any posting text.
- **The LinkedIn connections export**, which was not opened.
- **Data from any account other than mine.** No aggregate of other users is published.
- **Exact spend limits and rate limits.** The baseline's risk audit says to omit them.
- **The earlier build's Live-user numbers**, pending a consent decision (NG-08).
- **Session URLs, host addresses, file-system paths and environment files.**
