# Architecture 01 — Components and boundaries

*Live `7322289` (2026-10-24) · narrative: [Product 03](../product/03-system-architecture.md)*

```mermaid
flowchart LR
  subgraph Clients
    B[/Person in a browser/]:::human
    EXT[Chrome extension: fills, never submits]:::det
    GPT[[ChatGPT via MCP, read-only]]:::ext
    VIS[/Visitor on a shared conversation link/]:::human
  end

  subgraph Host["One small Linux host: Beta and Live, same code"]
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
      GAP[Gap conversations]:::det
      RES[Résumé flow]:::det
      DIS[Discovery and apply kits]:::det
      JRN[Research, interview prep, statuses]:::det
      SHR[Sharing and MCP tools]:::det
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
  end

  B --> PAGES
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
  DIS --> ATS
  Domain --> DB
  EXE -->|one row per call| DB

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

## Boundaries the diagram encodes

| Boundary | Enforced by | Claim |
|---|---|---|
| Accounts never see each other | Forced row-level security; the runtime role owns nothing | [P-12](../evidence/03-claim-index.md#p-12) |
| Every outside call goes through one boundary | Stage must be governed or declared; no fallback; priced models only; tests forbid provider calls elsewhere | [P-01](../evidence/03-claim-index.md#p-01) |
| The web process never runs slow work | Work is a committed row; the runner claims it | [P-09](../evidence/03-claim-index.md#p-09) |
| Only one module writes career evidence | Change Documents; text-scan test | [K-10](../evidence/03-claim-index.md#k-10), [K-11](../evidence/03-claim-index.md#k-11) |
| ChatGPT and shared links can only read | No write tools or scope; the share engine imports no write path | [A-55](../evidence/03-claim-index.md#a-55), [A-56](../evidence/03-claim-index.md#a-56) |
| The extension cannot submit | No submit code path; test `the extension never submits` | [A-39](../evidence/03-claim-index.md#a-39) |
