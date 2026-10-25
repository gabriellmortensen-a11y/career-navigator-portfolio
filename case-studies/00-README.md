# Case studies

Six case studies, each built from the strongest available evidence. Every one covers:
- the customer problem and context;
- my ownership;
- constraints;
- alternatives;
- the decision and its reasoning;
- implementation;
- verification;
- results and limitations;
- what changed after learning from use.

Numbers link to the [metric ledger](../evidence/04-metric-ledger.md), and capability statuses to the
[claim index](../evidence/03-claim-index.md).

| # | Case study | Best for | Key evidence |
|---|---|---|---|
| 01 | [Building a governed career evidence system](01-governed-career-evidence.md) | Product judgment on trust; data architecture | Prompt contamination 49% → 4%; role boundary in the schema; database-enforced tenancy; a data-loss incident disclosed |
| 02 | [Preventing unsupported claims in tailored résumés](02-preventing-unsupported-claims.md) | AI product design; technical depth | The writer is never given the requirements; bullets bound to stories by schema; residual risks named |
| 03 | [Making evaluation trustworthy, fast and cheap](03-evaluation-quality-latency-cost.md) | Quality, cost and latency trade-offs | 1,164 → 68 judgements, $0.45 → $0.04 per posting; noise floors; model routing evidence |
| 04 | [Connecting job discovery to application execution](04-connecting-discovery-to-application.md) | End-to-end workflow; automation boundaries | Funnel 297 → 92 → 54 for $1.86; never auto-submit; throughput measured, not outcomes |
| 05 | [Designing gap conversations that produce useful evidence](05-gap-conversations-that-produce-evidence.md) | Conversational UX with integrity constraints | Model for words, code for state; themes; one proposal; role confirmed by the person |
| 06 | [Operating a product with an implementation agent](06-operating-the-human-agent-loop.md) | TPM / delivery; working with AI coding agents | Beta-before-Live, incidents and their source fixes, disclosure over cosmetics |

**A note on voice.** Case studies are written in my voice because they describe my product
decisions and judgement. The code, and many of the proposals I accepted, came from Claude Code agents ([Product 01](../product/01-problem-users-and-role.md#my-role)).
