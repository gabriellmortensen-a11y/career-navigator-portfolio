# Architecture 02 — Evidence admission and acceptance

*Live `7322289` (2026-10-24) · narrative: [Knowledge 02](../knowledge/02-admission-and-acceptance.md)*

```mermaid
flowchart TD
  subgraph Paths["Ways in"]
    ADD[/Person writes on Add Evidence/]:::human
    IMP[Résumé file: deterministic parser, no model]:::det
    CHAT([Evidence chat proposes add, correct, enrich or retire]):::model
    GAPD([Guided gap discovery asks one question per turn]):::model
  end

  IMP --> SUG([Editor suggests wording only; never a claim change]):::model
  SUG --> PROP[/Person reviews every job; edits employer and title; accepts or rejects suggestions/]:::human
  CHAT --> REF{{Jev: which record pieces is this about; already covered?}}:::jev
  GAPD --> STOP[Code decides each requirement part and when to stop]:::det
  STOP --> ONE[One consolidated proposal; facts accounted for by code]:::det
  REF --> FIG[Figures the person never said are reported, not removed]:::det
  ONE --> FIG
  FIG --> PICK[/Person confirms or changes the role, guess preselected, and presses Save/]:::human
  ADD --> TICK[/Person ticks verbatim spans/]:::human

  PROP --> CD
  PICK --> CD
  TICK --> CD
  CD[Change Document: contract checked in code, spans verbatim, version and hash frozen]:::det
  CD -->|refused| REFU[(Kept with its reason)]:::store
  CD -->|admitted| APPLY[/Applied by the same person's press: Apply, Save or Approve/]:::human
  APPLY --> WRITE[(Source, claims, story: one role per row, composite foreign keys)]:::store
  WRITE --> DOCU[Canonical evidence document, hashed]:::det
  WRITE --> EMB[[Embeddings]]:::ext
  WRITE --> CON([Concept indexing: model picks from a vector shortlist]):::model

  subgraph Auto["No person in the loop: named exception"]
    NEAR[Cosine-near fragment pairs within one role]:::det
    SAME{{Jev: same piece of work? at least 0.6}}:::jev
    COMP[COMPOSE: a new story from the fragments' own words; fragments retired with reason]:::det
  end
  WRITE --> NEAR --> SAME --> COMP --> WRITE

  RET[/Person says it is wrong: RETIRE; correction names its replacement/]:::human --> WRITE
  FLAG[/Person flags or unflags a story/]:::human --> FL[(Flag overrides the deterministic reading)]:::store
  FL -.->|excluded from| OUT[Résumés and shared links]:::det

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

**Not shown, because it is a known exception rather than the design:** "Accept as is" on a résumé
the person brought records it through the parser and approve step **without** the proposal page
([D-05](../evidence/05-discrepancies.md#d-05)).
