# Example — model routing as a governed document (excerpt)

**What this is:** an excerpt from the governed `model_assignments` document as seeded at Live
`7322289`. Each task names its model, the recommended model, and **why**, with the evidence and its
sample size. A change made on Admin › Models is a new version of this document. No personal data.

Context: [Product 04](../../product/04-model-routing-cost-latency.md) ·
[Case study 03](../../case-studies/03-evaluation-quality-latency-cost.md) ·
metrics [M-19](../../evidence/04-metric-ledger.md#m-19), [M-20](../../evidence/04-metric-ledger.md#m-20).

> Evidence behind the first recommendations (2026-10-19): a résumé trial on a copy of Live (Haiku
> 5.5, Sonnet 5.5 and gpt-5-mini, the same reviewer for all), and a replay of 50 recent real calls of
> the short tasks through Haiku 5.5 beside what gpt-5-mini answered.

```json
{
  "tasks": {
    "evidence_chat": {
      "model": "claude-haiku-5-5",
      "recommended": "claude-haiku-5-5",
      "why": "Replayed 6 real chats: sound, focused answers in 8 s against 13 s, at about half the cost."
    },
    "claim_extraction": {
      "model": "claude-haiku-5-5",
      "recommended": "claude-haiku-5-5",
      "why": "Replayed 6 real passages: every claim gpt-5-mini read was read by Haiku too, at about a tenth of the cost."
    },
    "concept_indexing": {
      "recommended": "gpt-5-mini-2025-08-07",
      "why": "Replayed 10 real calls: Haiku tagged 2 of the 21 concepts gpt-5-mini tagged. Far too strict for this task."
    },
    "relationship_review": {
      "recommended": "gpt-5-mini-2025-08-07",
      "why": "Haiku is stricter: the same verdict on 55% of 105 pieces, nearly every difference a 'supporting' it calls not relevant. Arguably more honest, but switching changes match counts everywhere, which is a product decision."
    },
    "resume_flow_writer": {
      "recommended": "gpt-5-mini-2025-08-07",
      "why": "Résumé trial: Haiku at high effort costs half as much, but reviewers counted fewer relevant accomplishments on 4 of 6 postings. Sonnet costs three times as much."
    },
    "resume_recruiter_select": {
      "recommended": "gpt-5-mini-2025-08-07",
      "why": "Résumé trial: with Haiku picking the stories, even gpt-5-mini's writing scored fewer accomplishments. The picks are where the gap comes from."
    },
    "resume_coverage_review": {
      "recommended": "gpt-5-mini-2025-08-07",
      "why": "The reviewer stays the same so every résumé's verdict can be compared with every other's. Change it deliberately, not for cost."
    }
  }
}
```

Tasks with only a `recommended` entry fall through to the application default (gpt-5-mini). The
lookup order is: the caller's explicit model → this document → the policy's own model → the default
([P-02](../../evidence/03-claim-index.md#p-02)).
