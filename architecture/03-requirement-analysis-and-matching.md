# Architecture 03 — Requirement analysis and evidence matching

*Live `7322289` (2026-10-24) · narrative: [Applications 01](../applications/01-job-analysis-and-assessment.md) · no language-model call anywhere on this path ([A-05](../evidence/03-claim-index.md#a-05))*

```mermaid
flowchart TD
  POST[/Person saves a posting: Quick add, Discover Save, or paste/]:::human
  POST --> READ[Rules read every line: ask, about, logistics, unclear; never drop silently]:::det
  READ --> SIFT{{Jev: is this line a requirement? below 0.5 set aside, retired not deleted}}:::jev
  SIFT --> WORD[Rules reword employer-only names so any candidate could show the work]:::det
  WORD --> KIND[Rules split facts to confirm: degree, eligibility, location, bare years]:::det
  KIND --> FREEZE[(Requirements frozen with a fingerprint; later stages refuse drift)]:::store

  subgraph Match["Matching, per requirement"]
    NOM[Three nominators, top 8 each: best sentence, whole story, shared named terms]:::det
    EMB[[Embeddings]]:::ext
    READJ{{Jev reads: story related at least 0.3, then sentences; passage of up to 3 sentences gets credit}}:::jev
    VERD[Direct at 0.5 or above, else supporting; named-tool cap; a story wins at most 3 requirements]:::det
  end
  FREEZE --> NOM
  EMB --> NOM
  NOM --> READJ --> VERD
  VERD --> SEL[(Selection recorded: chosen story and alternates per requirement)]:::store

  SEL --> CORE{{Jev: is it core? would a recruiter or a hiring manager pass without it?}}:::jev
  CORE --> ASSESS[Strong, light, missing; gap only if a reader would pass: missing at 0.6 or above; light never a deal-breaker]:::det
  REV[(Newest résumé review: model reviewer verdicts)]:::store -.->|a reader's no overrides the estimate| ASSESS
  ASSESS --> SHOW[/Person sees gaps by return on time, optional items, facts to confirm/]:::human
  SHOW -->|chat about the gaps| CHAT[Gap conversation: see Applications 02]:::det
  SHOW -->|press Write the résumé| WRITE[Résumé flow: see Architecture 04]:::det

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

**Calibration note.** The 0.6 threshold and the "light is never a deal-breaker" rule were measured
against the app's *model* reviewer verdicts on one account's résumés (19, then 55). They are not
measured against human hiring outcomes ([M-13](../evidence/04-metric-ledger.md#m-13)–[M-15](../evidence/04-metric-ledger.md#m-15)).
