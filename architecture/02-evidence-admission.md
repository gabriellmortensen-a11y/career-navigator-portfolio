# Architecture 02 — Evidence admission and acceptance

*Live `00eac95` (2026-10-31) · narrative: [Knowledge 02](../knowledge/02-admission-and-acceptance.md)*

```mermaid
flowchart TD
  subgraph Paths["Ways in"]
    ADD[/Person writes on Add Evidence/]:::human
    IMP[Résumé file: deterministic parser, no model]:::det
    CHAT([Evidence chat, Navi: proposes add, correct, enrich or retire]):::model
    GAPD([Guided gap discovery asks one question per turn]):::model
    TALK[/Person tells the interview coach or the application chat about their work, or says a line is wrong/]:::human
  end

  IMP --> SUG([Editor suggests wording only; never a claim change]):::model
  SUG --> PROP[/Person reviews every job; edits employer and title; accepts or rejects suggestions/]:::human
  CHAT --> REF{{Jev: which record pieces is this about; already covered?}}:::jev
  GAPD --> STOP[Code decides each requirement part and when to stop]:::det
  STOP --> ONE[One consolidated proposal; facts accounted for by code]:::det
  TALK --> HEARD{{"Jev: does the message tell their work, and for which need? Does it say a line is wrong?"}}:::jev
  HEARD -->|tells work| OFFER["Code offers their own words: an addition, or added to the piece the answer rests on; a word like 'it' is named only if every word of theirs is kept"]:::det
  HEARD -->|says a line is wrong| DISP["Code resolves the line from a footnote number, a quote or a phrase; the change offered is to that exact record text, only the words named"]:::det
  OFFER --> REF
  REF --> FIG[Figures the person never said are reported, not removed]:::det
  ONE --> FIG
  FIG --> PICK[/Person confirms or changes the role, guess preselected, and presses Save/]:::human
  DISP --> PICK
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
  FL -.->|excluded from| OUT[Résumés and living-résumé links]:::det

  subgraph Never["Never a way in"]
    GRW[Growth areas, action plans and milestones]:::det
    INT[Living-résumé answers, situational interpretations included]:::det
    ART[GitHub portfolio artifacts and their owner-approved links]:::det
    JS[Interview cards, and the person's words kept for one opportunity]:::det
    RD[What Career Chat read for a message]:::det
  end
  Never -.->|never| CD
  GRW -.->|"I've done this now: the person tells the chat"| CHAT

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

**New since 2026.10.0:**
- **Work told to the interview coach or the application chat is offered by code**, in the person's
  own words, and written only on Save ([A-65](../evidence/03-claim-index.md#a-65),
  [A-75](../evidence/03-claim-index.md#a-75)).
- **A line the person says is wrong is resolved by code**, and the change offered is to that exact
  record text; the coaching model cannot offer a removal ([A-69](../evidence/03-claim-index.md#a-69)).
- **Never a way in:** Growth plans ([K-33](../evidence/03-claim-index.md#k-33)); living-résumé
  interpretations ([A-114](../evidence/03-claim-index.md#a-114)); portfolio artifacts
  ([K-34](../evidence/03-claim-index.md#k-34)); interview cards and the person's words for one
  opportunity ([A-67](../evidence/03-claim-index.md#a-67), [A-70](../evidence/03-claim-index.md#a-70));
  what Career Chat reads ([K-31](../evidence/03-claim-index.md#k-31)). A Growth item reaches the
  record only when the person tells the chat what they did and saves it.

**Not shown, because they are known exceptions rather than the design:**
- "Accept as is" on a résumé the person brought records it through the parser and approve step
  **without** the proposal page ([D-05](../evidence/05-discrepancies.md#d-05)).
- Offers from the application chat skip the figure check that the evidence chat and the coach run
  ([D-36](../evidence/05-discrepancies.md#d-36)).
