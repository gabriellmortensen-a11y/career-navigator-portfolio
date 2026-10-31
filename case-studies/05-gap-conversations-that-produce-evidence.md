# Case study 05 — Designing gap conversations that produce useful evidence

**One line:** A chat that "helps you fill gaps" easily becomes a chat that fills them *for* you. I
redesigned it so that:
- only gaps a reader would act on are raised;
- related gaps are asked as one theme;
- each requirement is tracked by code;
- the conversation stops when code says so;
- the result is one proposal the person saves to a role they confirm.

**Audience notes.** *Product:* conversational UX with integrity constraints. *Technical:* a model
for the words, code for the state. *TPM:* iterating a conversational feature on real transcripts
with a small paid test budget.

---

## Customer problem and context

The assessment tells a person what a job asks for that their record doesn't show strongly. The next
step is getting them to say what they actually did. That is the evidence a recruiter needs, often
work they forgot or never wrote down. The first versions of the gap chat had five problems.

1. **Too many gaps.** One job showed 15 "gaps" while both model reviewers said they would
   advance the candidate. A gap is only what a reader would pass on you without; in my words, "if
   that's the case, they're really not gaps" (`e718941`).
2. **One question per requirement.** On one posting, thirteen closely related compliance
   requirements were asked as thirteen gaps.
3. **The model kept the count.** The model reported its own progress, which contradicted the page.
4. **Facts went missing.** A draft held only the last turn's facts. A fact the person gave could
   vanish from the proposal.
5. **It didn't believe the person.** A job chat for a games product role kept asking about players
   and level caps after being told twice the product wasn't a game.

## My ownership

I defined what a gap is, how the conversation should feel, and when it should stop. I tested it on
my own live applications, turn by turn, and reported the failures with transcript turn numbers. I
approved each paid test in advance: cents per run, with the budget stated before any spend. The
agents designed the state machine and the ledger.

## Constraints

- **The model writes, it doesn't decide.** Whether a requirement is answered, and when to stop, are
  state decisions. They belong to code and Jev ([Product 02 §4](../product/02-principles.md#4-jev-selects-models-reason-and-write)).
- **Nothing is invented.** A limit the person states is recorded as a limit, never as a fact.
- **Nothing is saved without the person**, and nothing is saved to a role the person hasn't
  seen and confirmed.
- **Cheap and fast.** A conversational turn has to cost a fraction of a cent and come back in
  seconds.

## Alternatives considered

| Option | Why not |
|---|---|
| Ask about every short requirement | The "15 gaps, both readers advance" problem |
| Let the model decide when a gap is answered | It declared victory early and counted wrong |
| One fixed questionnaire per requirement type | Doesn't work across fields; it must "work beyond just" one domain |
| Save each answer as it arrives | Fragments, duplicates, and answers glued to the wrong story |

## Decision and reasoning

**Model for the words; code for the state.**

1. **What counts as a gap** comes from the assessment: a missing or light requirement a recruiter or hiring-manager persona would likely pass on.
   Everything else is optional and labeled that way. After a review, the model reviewers' actual
   "no"s override the estimate ([A-06](../evidence/03-claim-index.md#a-06),
   [A-07](../evidence/03-claim-index.md#a-07)).
2. **Themes.** Related gaps are grouped by embeddings plus a Jev "same area?" question. On one
   posting, 13 compliance requirements became 1 theme, while each requirement is still tracked on
   its own ([A-09](../evidence/03-claim-index.md#a-09)).
3. **Requirement parts** are split by rules into years, named tools ("or similar") and how they were
   used. Code decides each part from the person's own words. Years count only from numbers or dates
   they state ([A-10](../evidence/03-claim-index.md#a-10), [K-26](../evidence/03-claim-index.md#k-26)).
4. **Stopping is code.** The conversation stops when:
   - the person stops;
   - nothing is open;
   - the next question would repeat one already asked;
   - or Jev reads the working draft as establishing every requirement.

   "Stopping is never saving" ([A-08](../evidence/03-claim-index.md#a-08)).
5. **One ledger** is rebuilt from the turns each time. It drives the counter ("Gap 3 of 7 · 2
   reviewed · 4 after this"), the breakdown and what the model is told. The policy tells the model
   to answer counts only from that ledger.
6. **One proposal at the end**, either a new story or a fuller one that replaces an older one. Facts
   are accounted for by code: in the draft, deliberately left out, or flagged.
7. **The person saves to a role they confirm**, with the chat's guess preselected and marked. I asked
   that it confirm the role even when it thinks it knows ([K-13](../evidence/03-claim-index.md#k-13)).
8. **Limits become Growth areas** by their own press, and are never evidence
   ([K-28](../evidence/03-claim-index.md#k-28)).

## Implementation

- **The chat.** One governed model call per turn (Claude Haiku), prompt-cached, streaming. The
  policy carries the rules, and code supplies the queue, the ledger and the facts.
- **Jev picks the evidence.** It decides which record pieces a message refers to, whether an addition
  is already covered, and whether the draft establishes the requirement.
- **Effort by message kind.** Plain questions run at low reasoning effort; changes and discovery at
  medium.
- **Nothing is cut.** Messages and proposals up to 20,000 characters are kept whole, and pieces named
  exactly are shown in full.

## Verification

- **Tests:**
  - discovery state and stop rules (`test_discovery.py`);
  - the ledger (`test_gap_ledger.py`);
  - requirement parts (19 tests);
  - Growth areas, including that no résumé or apply module reads them;
  - role-picked Save and the atomic turn claim.
- **Paid replays on Beta, each approved in advance:**
  - A full gap conversation run cost $0.020 ([M-47](../evidence/04-metric-ledger.md#m-47)). It found four defects, each fixed in the policy or the
    code: discovery fields not nested, the draft holding only the last turn's facts, a question
    appended twice, facts restated on reopen.
  - A replay on one job after the requirement-parts change matched the intended sequence: tools →
    years → use → the technical requirement → stop, naming what was still open.
- **Live telemetry:** mean **$0.0033** per chat call over 108 calls, p50 11.5 s
  ([M-21](../evidence/04-metric-ledger.md#m-21)).

## Results

- **Fewer, real gaps.** Across eight of my jobs, clusters of 13, 11 and 10 related requirements
  became 1, 3 and 4 themes ([M-45](../evidence/04-metric-ledger.md#m-45)). Jobs where readers would advance show their shortfalls as optional, not as gaps.
- **Conversations end themselves.** Code-decided stops replaced the model's own sense of "done".
- **Every saved proposal lands on a role the person confirmed**, with its facts accounted for.
- **On one job**, the record of 16 gaps reconciled to 12 reviewed (7 with new evidence, 5 with no more
  to add), 1 in progress and 3 still to explore ([M-46](../evidence/04-metric-ledger.md#m-46)).

## Limitations

- **Threshold tests stub Jev.** Themes and thresholds were measured on a handful of jobs. The test
  suite stubs Jev with fixed answers: grouping and the no-chaining rule are exercised, Jev's real
  behavior is not ([A-09](../evidence/03-claim-index.md#a-09)). *(Corrected 2026-10-31: this said each gap was its own theme.)*
- **Two rules for years.** *Tune my evidence* uses a different years rule (dated roles read by Jev).
  The two can disagree ([D-14](../evidence/05-discrepancies.md#d-14)). *Note, 2026-10-31: that page was retired on 2026-10-30;
  Career Direction's role pages keep its reading and its rule ([A-107](../evidence/03-claim-index.md#a-107)).*
- **Posting language can still enter.** The chat sees the focus requirement. If the person accepts a
  draft that echoes it, posting language enters the record. The policy asks the model not to borrow
  posting words; no code checks it. *Note, 2026-10-31: since 2026-10-28 the chat can also read a
  posting's text when the person asks what it says, labeled as the employer's words; a proposal
  made on that turn still needs Save ([K-31](../evidence/03-claim-index.md#k-31)).*
- **The "closes the gap" judgment is still a model.** On the older résumé-review gap panel it is a
  model judgment, reused for identical input ([K-14](../evidence/03-claim-index.md#k-14)).

## What changed after learning from use

1. **"Believe it the first time."** After the games-role transcript, the policy now records a
   field-only dimension as not done once the person says the field isn't theirs. It never asks about
   it again, and it asks in their field's words what their work did for the same need.
2. **"That's all" means this requirement.** In a theme, "that's all" used to close every
   requirement. It now closes only the one being asked.
3. **The model stopped keeping score.** The ledger exists because the model's count was wrong in
   front of me.
4. **The gap definition moved from "short" to "would a reader pass".** It is now driven by the model
   reviewers' actual "no"s when a review exists.
