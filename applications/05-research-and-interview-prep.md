# Applications 05 — Company research and interview preparation

*Applications 4.0 · describes Live `7322289` (2026-10-24)*

**The question this answers:** once an application is in motion, how does the system help the
person prepare, using what they have actually done and what is publicly known about the company?

## Company research

A research run happens only when the person presses for it; opening a page never searches
([A-50](../evidence/03-claim-index.md#a-50)).

1. **Search.** At most four Tavily searches, built only from public posting fields, five results
   each.
2. **Filter (code).** Keep sources on the company's own domain, or that name the company, up to 12.
   If none survive, the run ends "empty" with no model call.
3. **Write.** One model call writes the brief. Claude Haiku is the default: on replays it produced
   comparable briefs at about 40% of the cost.
4. **Admit (code).** Citations to sources the writer wasn't shown are dropped. A brief needs the
   company's identity confirmed and at least one web-sourced fact.

The brief appears on *Prepare my application* and on the interview pages.

**A comparison that kept the simpler path.** Claude's own web search was tried for sourcing on Beta
([A-51](../evidence/03-claim-index.md#a-51)):
- Its sources were staler, it missed the company's official site, and it cost several times more.
- The newer search tool returned no citable text at all.

Tavily stayed. Claude search remains Beta-only behind a guard that refuses Live.

## Interview preparation

Every interview stage starts from **evidence Jev chose**, not evidence the writer picks
([A-52](../evidence/03-claim-index.md#a-52)):
1. Cosine reads the top 12 pieces.
2. Jev's "establishes" question keeps those at p ≥ 0.5, at most 4.
3. With no Jev credential the stage fails visibly. A neighbourhood is never passed off as support.

| Stage | What it does | Controls |
|---|---|---|
| **Preparation** | Likely questions, STAR stories with proof depth (interview-ready / résumé-capable / thin), pressure points with their basis | Input hash reuse; strict output schema; citations not shown are dropped |
| **Practice** | The person answers; feedback | Strict schema; dropped figures and promises flagged, never fixed |
| **Your own questions** | Questions the person adds are practised like the suggested ones | The practice call is told the person added it |
| **Offer a suggestion** | A reframed answer beside the person's, once per answer | Adds no facts; gaps marked as prompts |
| **Find answers in my evidence** | The evidence that answers a question | Support at p ≥ 0.5; up to 2 "related at most" pieces at ≥ 0.15 |
| **Quick answers** | A glanceable say-first / points / close per question, for freezing moments ([A-53](../evidence/03-claim-index.md#a-53)) | Kind decided by code: *answer*, *bridge* (nearest related evidence, labelled) or *none*, which opens the chat on that question |
| **Guided walkthrough** | 8 steps on top of the above | **Known defect:** writes from the preparation's cosine candidate pool, not Jev's chosen set ([A-54](../evidence/03-claim-index.md#a-54), [D-12](../evidence/05-discrepancies.md#d-12)) |

**Earlier conclusions keep their basis.** Pressure points carry their basis: feedback, requirement,
expectation or possible. Something the interviewer said is labelled differently from an inference
nobody said ([K-20](../evidence/03-claim-index.md#k-20)).

**Output shapes are enforced by the API, not repaired in a parser.** Practice feedback lists used to
come back as prose or objects. Since 2026-10-20 four stages send a strict JSON schema to the
provider ([A-52](../evidence/03-claim-index.md#a-52)).

## What I decided not to build

A live answer tool for video interviews was discussed and **not built**. Covert transcription of an
interviewer raises consent problems: all-party consent laws and employer rules. Preparation beats
mid-interview answers, and *Quick answers* is the glanceable compromise.

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Company research (Tavily + brief + admit) | Verified | [A-50](../evidence/03-claim-index.md#a-50) |
| Claude web search for research | Experimental (Beta-only, not adopted) | [A-51](../evidence/03-claim-index.md#a-51) |
| Preparation, practice, own questions, suggestions, evidence answers | Verified | [A-52](../evidence/03-claim-index.md#a-52) |
| Quick answers with bridge | Verified | [A-53](../evidence/03-claim-index.md#a-53) |
| Guided walkthrough | Limited (evidence-source defect) | [A-54](../evidence/03-claim-index.md#a-54) |
