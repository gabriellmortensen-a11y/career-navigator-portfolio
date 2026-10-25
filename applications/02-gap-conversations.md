# Applications 02 — Gap conversations

*Applications 4.0 · describes Live `7322289` (2026-10-24) · case study: [05](../case-studies/05-gap-conversations-that-produce-evidence.md)*

**The question this answers:** when a job exposes a gap, how does the system help the person supply
real evidence for it, without putting words in their mouth?

## The shape of a conversation

A gap conversation is the evidence chat, focused on one opportunity, with its own thread:

1. **The queue comes from the assessment.** Before a résumé exists, that means gaps by impact, then
   optional items. After a review, it is what a reader who said *no* named as blocking
   ([A-06](../evidence/03-claim-index.md#a-06)).
2. **Related gaps become one theme.**
   - Gap texts are embedded; pairs at cosine ≥ 0.35 go to Jev's "same area?" question.
   - Average-link grouping at ≥ 0.5, with no chaining.
   - On one posting, 13 related compliance requirements became 1 theme ([A-09](../evidence/03-claim-index.md#a-09)).
3. **Each requirement in a theme is still tracked on its own.** Rules split it into parts:
   - years (the lower end of a range);
   - named tools ("or similar" noted);
   - how they were used.

   *Code* decides each part from the person's words and the record
   ([A-10](../evidence/03-claim-index.md#a-10), [K-26](../evidence/03-claim-index.md#k-26)).
4. **The model asks one question per turn.** One governed model call (Claude Haiku) writes the reply.
   It sees the focus requirement and the evidence Jev says the message refers to
   ([A-08](../evidence/03-claim-index.md#a-08)).
5. **Code decides when to stop**:
   - the person stops;
   - nothing is open;
   - the next question would repeat an earlier one (embedding ≥ 0.9);
   - or Jev reads the working draft as establishing every requirement.

   "Stopping is never saving."
6. **One consolidated proposal.** It is either an addition or a fuller story that replaces an older
   one. Facts the person gave are accounted for by code: in the draft, deliberately left out, or
   flagged as missing ([K-25](../evidence/03-claim-index.md#k-25)).
7. **The person saves it to a role they confirm.** The chat's guess is preselected and marked, and can
   be changed ([K-13](../evidence/03-claim-index.md#k-13)).
8. **A limit becomes a Growth area.** What the person says they haven't done can go on a separate
   Growth list, by its own press. A Growth area is never evidence
   ([K-28](../evidence/03-claim-index.md#k-28)).

**The ledger.** One record, rebuilt from the turns each time, drives the counter ("Gap 3 of 7 · 2
reviewed · 4 after this"), the breakdown and what the model is told. It was built because the
model's own count contradicted the page.

## Rules the conversation follows

These are written into the governed chat policy and backed by code where it matters:
- **"Direct, then stop."** Answer the question; don't pad.
- **A theme is one gap.** "That's all" is about the requirement being asked. It moves on and never
  records the others as declined.
- **Believe it the first time.** If the person says their work was in another field, don't keep
  asking about the posting's field. The trigger: a job chat for a games product role kept asking
  about players and level caps after being told twice the product wasn't a game.
- **Never invent the missing part.** What they didn't do or can't say is a limit, not a fact.
- **Earlier conclusions keep their basis.** A previous reading is labelled as a reading
  ([K-20](../evidence/03-claim-index.md#k-20)).
- **Nothing is ever cut.** Proposals and messages up to 20,000 characters are kept whole. Pieces
  the message names exactly are shown to the model in full.

## Cost and speed

| Measure | Value |
|---|---|
| A chat call (Haiku, prompt-cached) | Mean $0.0033 over 108 Live calls ([M-21](../evidence/04-metric-ledger.md#m-21)) |
| Plain questions | Answered at low reasoning effort: about 45% less time on 13 replayed turns ([M-36](../evidence/04-metric-ledger.md#m-36)) |
| Changes and gap discovery | Medium effort |

## What went wrong and changed

| Observed | Stage changed |
|---|---|
| The model returned discovery fields loose, so nothing was proposed | The policy's output example now nests them; the stopping turn must carry discovery |
| The draft held only the last turn's facts | The draft accumulates; facts are accounted for by code, not by the model's list |
| A question was appended twice; facts were restated on reopen | Word-overlap check on questions; reopening doesn't refill the opening line |
| "That's all" closed every requirement in a theme | Applies only to the requirement asked |
| The chat filed an addition under its own guess of the role | The role is shown on the card to confirm or change before Save |
| A double press recorded a story twice | Save claims the turn atomically ([K-16](../evidence/03-claim-index.md#k-16)) |

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Guided gap discovery; code-decided stop; one proposal | Verified | [A-08](../evidence/03-claim-index.md#a-08) |
| Themes | Limited (tests stub Jev; measured on 8 jobs) | [A-09](../evidence/03-claim-index.md#a-09) |
| Requirement parts decided by code | Limited (one Beta replay) | [A-10](../evidence/03-claim-index.md#a-10) |
| Role confirmed by the person on Save (guess preselected) | Verified | [K-13](../evidence/03-claim-index.md#k-13) |
| Growth areas kept apart | Verified | [K-28](../evidence/03-claim-index.md#k-28) |
