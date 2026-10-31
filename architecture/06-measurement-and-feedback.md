# Architecture 06 — Measurement and feedback

*Live `00eac95` (2026-10-31) · narrative: [Product 05](../product/05-quality-and-measurement.md), [Product 06](../product/06-operations-and-privacy.md)*

```mermaid
flowchart TD
  subgraph Work["Every call"]
    CALL[Any model, Jev, embedding, search or scrape call]:::det
    GOV[Governed boundary: policy version or declared exemption; priced models only; no fallback]:::det
    LEDGER[(model_execution: stage, policy version, model, tokens incl. cached and reasoning, cost, seconds, outcome, context hash; never the prompt)]:::store
    RUNS[(Run records: phases with calls, cost, seconds)]:::store
  end
  CALL --> GOV --> LEDGER
  CALL --> RUNS

  subgraph Read["Readers"]
    SPEND[Spend and failures by day, stage, model, account]:::det
    FLOWS[How the system flows: 66 capabilities, 9 flows, 30-day cost]:::det
    AVR[Assessment vs review: predicted reader calls against reviewer verdicts]:::det
    ALERT[Alerts every 15 minutes: failed work, failed calls, overdue work, daily spend, host health]:::det
  end
  LEDGER --> SPEND
  LEDGER --> FLOWS
  RUNS --> AVR
  LEDGER --> ALERT
  ALERT --> MAIL[/Owner emailed when the set of problems changes/]:::human

  subgraph Loops["Feedback loops"]
    MC[Model check: replay real prompts through candidates under a cap; deterministic scores; noise floor]:::det
    CAND[[Candidate models]]:::ext
    REC[Recommend the cheapest within 0.10; never switch]:::det
    USE[/Person presses Use this/]:::human
    ASSIGN[(New version of the model assignments document)]:::store
    CAL[/Thresholds updated by hand in code from Assessment vs review/]:::human
    OUT[(Status history: applied, interviewing, rejected)]:::store
  end
  LEDGER --> MC
  MC --> CAND --> REC --> USE --> ASSIGN --> GOV
  AVR --> CAL
  OUT -. not yet connected to calibration .-> CAL

  subgraph Release["Release loop"]
    SUITE[Full suite on the exact code]:::det
    BETA[Deploy to Beta]:::det
    LOOK[/Owner uses it on Beta/]:::human
    LIVE["Approved commits cherry-picked onto Live's own branch; deploy with backup, drain, document snapshot, probe, automatic rollback"]:::det
  end
  SUITE --> BETA --> LOOK --> LIVE
  LOOK -. finds defects in use .-> SUITE

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

**Gaps the diagram makes visible:**
- Status history does not feed calibration.
- Per-call seconds are missing for the writer, selector and reviewers
  ([P-17](../evidence/03-claim-index.md#p-17)).
- Model check has not yet been run on Live ([P-07](../evidence/03-claim-index.md#p-07)).
- Per-call seconds are also missing for the résumé summary calls, and an interview-coach turn stores
  no time on the turn ([D-21](../evidence/05-discrepancies.md#d-21)).
- A model named only in the seed file never reaches an existing database's assignments document,
  so the routing loop starts from what Admin › Models holds ([D-27](../evidence/05-discrepancies.md#d-27)).
- GitHub reads for the portfolio go around the governed boundary and write no ledger row
  ([P-36](../evidence/03-claim-index.md#p-36), [D-28](../evidence/05-discrepancies.md#d-28)). ATS reads also go around it but are recorded.
- Since 2026-10-28 the release loop ends on Live's own branch, rebuilt from Beta's commits by
  cherry-pick, without three Beta-only features ([P-37](../evidence/03-claim-index.md#p-37)).
