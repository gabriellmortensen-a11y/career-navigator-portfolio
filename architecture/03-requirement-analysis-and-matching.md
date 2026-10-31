# Architecture 03 — Requirement analysis and evidence matching

*Live `00eac95` (2026-10-31) · narrative: [Applications 01](../applications/01-job-analysis-and-assessment.md) · one language-model call on this path, a stated exception: reading a line that lists several asks ([A-05](../evidence/03-claim-index.md#a-05))*

```mermaid
flowchart TD
  POST[/Person saves a posting: Quick add, Discover Save, or paste/]:::human
  POST --> READ["Rules read every line: ask, about, logistics, unclear; never drop silently; a sentence opening with Or stays with its requirement"]:::det
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
  FREEZE --> DIV(["At Chart My Course: the posting's long lines listing several asks are read once, in one call (Claude Haiku by assignment)"]):::model
  DIV --> ADMIT["Code keeps an ask only if made of the line's own words plus joining words; the line is retired, its asks appended, the set re-frozen"]:::det
  ADMIT --> NOM
  EMB --> NOM
  NOM --> READJ --> VERD
  VERD --> SEL[(Selection recorded: chosen story and alternates per requirement)]:::store

  SEL --> CORE{{"Jev: is it core? would a recruiter or a hiring manager pass without it? is it about the role, not something a candidate could show? (asked once, cached)"}}:::jev
  CORE --> ASSESS["Strong, light, missing; gap only if a reader would pass: missing at 0.6 or above; light never a deal-breaker; a line about the role or a fact to confirm is never a gap"]:::det
  REV[(Newest résumé review: model reviewer verdicts)]:::store -.->|a reader's no overrides the estimate| ASSESS
  ASSESS --> SHOW[/Person sees gaps by return on time and counted by theme, optional items, facts to confirm/]:::human
  SHOW -->|chat about the gaps| CHAT[Gap conversation: see Applications 02]:::det
  CHAT -.->|a saved story is read once by Jev and applied to the job at Save| SEL
  SHOW -->|press Write the résumé| WRITE[Résumé flow: see Architecture 04]:::det

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

**The model exception.** Since 2026-10-27 one model call per posting (Claude Haiku by assignment,
[D-27](../evidence/05-discrepancies.md#d-27)) reads that posting's long listing lines at Chart My
Course, chosen by the product owner over rules; code admits only asks made of the line's own words
(plus joining words such as "and", "experience", "ability") ([A-05](../evidence/03-claim-index.md#a-05)). A sentence opening with "Or" stays with its requirement
([A-95](../evidence/03-claim-index.md#a-95)). A story saved from a gap updates the job's selection at Save with no new charting
([A-81](../evidence/03-claim-index.md#a-81)). Gaps are counted by theme on every page ([A-78](../evidence/03-claim-index.md#a-78)).

**Calibration note.** The 0.6 threshold and the "light is never a deal-breaker" rule were measured
against the app's *model* reviewer verdicts on one account's résumés (19, then 55). They are not
measured against human hiring outcomes ([M-13](../evidence/04-metric-ledger.md#m-13)–[M-15](../evidence/04-metric-ledger.md#m-15)).
