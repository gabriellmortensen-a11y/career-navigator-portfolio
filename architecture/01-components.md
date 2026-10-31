# Architecture 01 — Components and boundaries

*Live `00eac95` (2026-10-31) · narrative: [Product 03](../product/03-system-architecture.md)*

```mermaid
flowchart LR
  subgraph Clients
    B[/Person in a browser/]:::human
    RAIL["Navi rail on every page: the chat in a frame, opened from the CN tab"]:::det
    EXT[Chrome extension: fills, never submits]:::det
    GPT[[ChatGPT via MCP, read-only]]:::ext
    VIS[/Visitor on a living résumé link/]:::human
  end

  subgraph Host["One small Linux host: Beta, and Live on its own branch since 2026-10-28"]
    subgraph Web["Web process (accepts work, never runs it)"]
      PAGES[Server-rendered pages and APIs]:::det
      AUTH[Accounts, sessions, extension pairing, OAuth for MCP]:::det
    end
    subgraph Runner["Runner process (lower priority)"]
      OPS[Durable background operations: claim, heartbeat, retry, drain]:::det
    end
    subgraph Domain["Domain modules"]
      REC[Career record: single writer, Change Documents]:::det
      JOB[Job intake and assessment]:::det
      GAP[Gap conversations and Growth plans]:::det
      READS["Career Chat read layer: 14 read-only operations, Jev-routed"]:::det
      RES[Résumé flow]:::det
      DIS[Discovery and apply kits]:::det
      JRN[Research, interview coach, application chat, statuses, Upcoming]:::det
      SHR[Living résumé, GitHub portfolio and MCP tools]:::det
    end
    subgraph Gov["Governed boundary: every model, Jev, embedding, search and scrape call"]
      EXE[Execution: policy version required, no fallback, priced models only]:::det
      ASSIGN[Model assignments document]:::store
      DOCS[Governed policy documents, versioned]:::store
    end
    DB[(PostgreSQL per environment: forced row-level security)]:::store
  end

  subgraph Outside["External services"]
    OAI[[OpenAI: gpt-5-mini, embeddings]]:::ext
    ANT[[Anthropic: Claude Haiku]]:::ext
    JEV[[Jev: typed probability questions]]:::ext
    TAV[[Tavily search]]:::ext
    APF[[Apify career-site index]]:::ext
    ATS[[ATS public APIs and robots-permitted employer pages]]:::ext
    GH[[GitHub public API, no credentials]]:::ext
  end

  B --> PAGES
  B --> RAIL
  RAIL --> PAGES
  EXT --> AUTH
  GPT --> AUTH
  VIS --> PAGES
  PAGES -->|enqueue| OPS
  PAGES --> Domain
  OPS --> Domain
  Domain --> EXE
  EXE --> ASSIGN
  EXE --> DOCS
  EXE --> OAI
  EXE --> ANT
  EXE --> JEV
  EXE --> TAV
  EXE --> APF
  DIS -->|"each read recorded as job_board_fetch"| ATS
  SHR -->|"plain HTTP, not recorded"| GH
  READS -->|read only| DB
  Domain --> DB
  EXE -->|one row per call| DB

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

Since 2026-10-28 Live is deployed from its own branch, rebuilt from Beta's commits, without three
Beta-only evidence features ([P-37](../evidence/03-claim-index.md#p-37),
[DEC-50](../product/07-decision-log.md#dec-50)). The rail runs in the browser around every page and
adds no call ([A-106](../evidence/03-claim-index.md#a-106)).

## Boundaries the diagram encodes

| Boundary | Enforced by | Claim |
|---|---|---|
| Accounts never see each other | Forced row-level security; the runtime role owns nothing | [P-12](../evidence/03-claim-index.md#p-12) |
| Every model, Jev, embedding, search and scrape call goes through one boundary | Stage must be governed or declared; no fallback; priced models only; tests forbid provider calls elsewhere. GitHub's public API is read outside it, unrecorded | [P-01](../evidence/03-claim-index.md#p-01), [P-36](../evidence/03-claim-index.md#p-36), [D-28](../evidence/05-discrepancies.md#d-28) |
| The web process never runs slow work | Work is a committed row; the runner claims it | [P-09](../evidence/03-claim-index.md#p-09) |
| Only one module writes career evidence | Change Documents; text-scan test | [K-10](../evidence/03-claim-index.md#k-10), [K-11](../evidence/03-claim-index.md#k-11) |
| Career Chat only reads, and never reads what is excluded | Read operations only, tested by a statement listener; row-level security; no operation reads the written exclusions | [A-102](../evidence/03-claim-index.md#a-102), [P-33](../evidence/03-claim-index.md#p-33) |
| ChatGPT and living-résumé links can only read | No write tools or scope; the living-résumé engine imports no write path | [A-55](../evidence/03-claim-index.md#a-55), [A-56](../evidence/03-claim-index.md#a-56) |
| Portfolio artifacts are never evidence, and only those the owner made public are served | Their own tables; a link to evidence only by the owner's approval; served only from repositories approved for the living résumé | [K-34](../evidence/03-claim-index.md#k-34), [A-121](../evidence/03-claim-index.md#a-121) |
| GitHub is read without credentials | Public API only; no token exists to store | [A-120](../evidence/03-claim-index.md#a-120) |
| The extension cannot submit | No submit code path; test `the extension never submits` | [A-39](../evidence/03-claim-index.md#a-39) |
