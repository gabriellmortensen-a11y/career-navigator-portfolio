# Applications 02 — Gap conversations

*Applications 5.0 · describes Live `00eac95` (2026-10-31) · case study: [05](../case-studies/05-gap-conversations-that-produce-evidence.md)*

**The question this answers:** when a job exposes a gap, how does the system help the person supply
real evidence for it, without putting words in their mouth?

## The shape of a conversation

A gap conversation is the evidence chat, focused on one opportunity, with its own thread. Since
2026-10-30 it opens as **Navi** in the rail, from the CN tab on the opportunity's pages at the
Explore and Résumé stages ([Applications 07](07-navi-and-career-chat.md),
[A-105](../evidence/03-claim-index.md#a-105)).

1. **The queue comes from the assessment.** Before a résumé exists, that means gaps by impact, then
   optional items. After a review, it is what a reader who said *no* named as blocking. A line about
   the role, and a fact to confirm such as a degree, never enter it
   ([A-06](../evidence/03-claim-index.md#a-06)).
2. **Related gaps become one theme.**
   - Gap texts are embedded; pairs at cosine ≥ 0.35 go to Jev's "same area?" question.
   - Average-link grouping at ≥ 0.5, with no chaining.
   - On one posting, 13 related compliance requirements became 1 theme ([A-09](../evidence/03-claim-index.md#a-09)).
   - A theme is counted as one gap on every page, as in the chat ([below](#rules-the-conversation-follows)).
3. **Each requirement in a theme is still tracked on its own.** A long listing line may already have
   been divided into its asks at Chart My Course ([A-05](../evidence/03-claim-index.md#a-05)).
   Rules split each requirement into parts:
   - years (the lower end of a range);
   - named tools ("or similar" noted);
   - how they were used.

   *Code* decides each part from the person's words and the record
   ([A-10](../evidence/03-claim-index.md#a-10), [K-26](../evidence/03-claim-index.md#k-26)).
4. **The model asks one question per turn.** One governed model call (Claude Haiku) writes the reply.
   It sees the focus requirement and the evidence Jev says the message refers to
   ([A-08](../evidence/03-claim-index.md#a-08)). When Jev reads the message as a question about the
   account, what the read layer read goes to the call too
   ([A-102](../evidence/03-claim-index.md#a-102)).
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
   be changed ([K-13](../evidence/03-claim-index.md#k-13)). **The Save goes straight to the job.**
   Jev reads the saved story once for that requirement, as Chart My Course reads a contender. Code
   makes it the chosen story if it reads stronger, otherwise an alternate, and keeps the assessment
   current when that is the only change. There is no new Chart My Course and no language-model call
   ([A-81](../evidence/03-claim-index.md#a-81)).
8. **A limit becomes a Growth area.** When the person says they haven't done something, the chat
   offers *Add to Growth* **on that turn, once**. It never offers again on a later turn, nor for
   something already listed for the same requirement ([A-108](../evidence/03-claim-index.md#a-108)).
   Adding stays the person's own press. A Growth area is never evidence
   ([K-28](../evidence/03-claim-index.md#k-28)). What happens next is [below](#from-a-limit-to-a-plan-growth-action-plans).

**Owner:** "I want the evidence I updated from the gap to go straight to the job without having to
do a new charted course ... a deterministic thing" (`3e1992d`, 2026-10-27,
[DEC-45](../product/07-decision-log.md#dec-45)).

**The ledger.** One record, rebuilt from the turns each time, drives the counter ("Gap 3 of 7 · 2
reviewed · 4 after this"), the breakdown and what the model is told. It was built because the
model's own count contradicted the page. It counts themes. After a Save the chat says how many gaps
are still open and, when it differs, how many are still to talk through ("3 gaps still open; 2
still to talk through").

## Rules the conversation follows

These are written into the governed chat policy and backed by code where it matters:
- **"Direct, then stop."** Answer the question; don't pad.
- **A theme is one gap, on every page.** The opportunity page, the review page, the opportunities
  pane, the chat's top line and what the chat is told all count related requirements as one gap. A
  gap whose saved story still reads light stays open, and the chat never says "the last gap" while
  one is open ([A-78](../evidence/03-claim-index.md#a-78), [DEC-66](../product/07-decision-log.md#dec-66)).
  "That's all" is about the requirement being asked. It moves on and never records the others as
  declined.
- **Believe it the first time.** If the person says their work was in another field, don't keep
  asking about the posting's field. The trigger: a job chat for a games product role kept asking
  about players and level caps after being told twice the product wasn't a game.
- **Never invent the missing part.** What they didn't do or can't say is a limit, not a fact.
- **Earlier conclusions keep their basis.** A previous reading is labeled as a reading
  ([K-20](../evidence/03-claim-index.md#k-20)).
- **Nothing is ever cut.** Proposals and messages up to 20,000 characters are kept whole. Pieces
  the message names exactly are shown to the model in full.

**Where counting by theme is weaker** ([D-35](../evidence/05-discrepancies.md#d-35)): the opportunity
and review pages group gaps when they render, which can make paid embedding and Jev calls. If grouping
fails, each requirement is counted as its own gap and the failure is only logged.

## From a limit to a plan: Growth action plans

A Growth item records something the person said they haven't done. Since 2026-10-30 each item can
carry an **action plan**: an outcome that would get them evidence of it, and the small milestones
to it ([A-109](../evidence/03-claim-index.md#a-109)).

**What the person sees on Growth:**
- A card counting items **With an action plan**, **Deferred** and **Completed** (every item ever
  marked *I've done this now*).
- **Suggest action plans** asks Navi, in the background, to suggest a plan for every item without
  one. Each is shown as *Navi's suggestion*.
- For each suggestion: **Accept**, **Write my own** (replaces the outcome and clears its
  milestones) or **Defer**. Milestones can be added or deleted. A finish date and each milestone's
  date can be set or cleared; every date is optional.

**How it works:**

| Step | Who | What |
|---|---|---|
| Suggest | **Model** (`growth_plan`, Claude Haiku by the seed assignment, its own governed policy), run in the background | For up to 40 items without a plan: the area, the requirement it came from, the posting's title and company, and what the person said; plus their roles (title, employer, dates) and Career Direction goals. Its declared package forbids the record's text. The API holds the answer's shape: an outcome and milestones per item number |
| Admit | Code | A plan is kept only with an outcome and at least one milestone, for an item it was given, once. It is stored as written, beside the call that wrote it. An item without a kept plan is offered again. A failure changes nothing |
| Decide | The person (code, no call) | Accept, write their own, defer; add or delete milestones; set or clear dates |
| Navi on Growth | **Model** (`growth_chat`, Claude Haiku by the seed, its own policy) | The CN tab on Growth opens Navi on its own thread. It sees today's date, the list numbered with its states, outcomes, dates and milestones ("Milestone 3.2"), recent turns and the message, never the record's text. It returns a reply and actions by the numbers shown ([A-110](../evidence/03-claim-index.md#a-110)) |
| Resolve | Code | Each action is checked against the list as it stands. Each doable one is said in the list's own words, and each refused one with why ("“\<item>” has no plan yet: accept one or write your own first.") |
| Save | The person, then code | The actions run in order through the page's own functions. Nothing changes before Save |

**What the policy asks of a plan:**
- **An outcome gets evidence:** a certification earned, a feature shipped to a named bar, work
  published. A document on its own is no outcome, unless it is published under their name or what
  it describes ships, launches or is used.
- **Milestones are small steps** to that outcome, and no first step only lists or compares.

**Owner** (`1ea9a97`, 2026-10-30, [DEC-69](../product/07-decision-log.md#dec-69)):
- "For the growth page I want a card at the top that says how many items have an action plan,
  deferred and completed with a button that creates action plan suggestions for each growth item
  and the user accepts the item or writes their own, sets a completion date and a next step
  milestone with a date for that."
- "It has to be actionable item that gets them evidence. Like getting a certification or shipping a
  feature with a regulation bar"
- "These are going to require a model to make the suggested action items. Use haiku for it. Make it
  a policy as well"
- "The growth page chat pane needs to be able to do all of these actions too."

**A plan is never evidence** ([K-33](../evidence/03-claim-index.md#k-33)). The plan call is never
shown the record's text, and nothing that writes a résumé, an application or outreach reads a plan.
The boundary test, though, names only the Growth list's own table (which holds the plans), not the
milestones' table or the plan modules. A plan
reaches the record only the ordinary way: *I've done this now* takes the item off the list and
opens the chat with "I've now done this: \<area>. Help me add it to my record." The person tells
it, and Save writes it.

**Where it is weaker** ([A-111](../evidence/03-claim-index.md#a-111)):
- Save is all or none only because the web handler rolls back on an error. No test drives an
  action failing mid-save.
- "Their own outcome in their words, nothing added" is a policy sentence. Code stores whatever text
  the call returns. On Beta, Navi once expanded a person's own outcome into its own words; the
  policy now says their words, nothing added (`33e9233`).
- Growth calls had not yet run on Live when measured, so the model they use there is unverified
  ([M-68](../evidence/04-metric-ledger.md#m-68), [D-27](../evidence/05-discrepancies.md#d-27)).

## Cost and speed

| Measure | Value |
|---|---|
| A chat call (Haiku, prompt-cached) | Mean $0.0033 over 108 Live calls ([M-21](../evidence/04-metric-ledger.md#m-21)) |
| Plain questions | Answered at low reasoning effort: about 45% less time on 13 replayed turns ([M-36](../evidence/04-metric-ledger.md#m-36)) |
| Changes and gap discovery | Medium effort |
| Suggest action plans | One call for 15 Growth items cost $0.0027 on Beta ([M-81](../evidence/04-metric-ledger.md#m-81)) |

## What went wrong and changed

| Observed | Stage changed |
|---|---|
| The model returned discovery fields loose, so nothing was proposed | The policy's output example now nests them; the stopping turn must carry discovery |
| The draft held only the last turn's facts | The draft accumulates; facts are accounted for by code, not by the model's list |
| A question was appended twice; facts were restated on reopen | Word-overlap check on questions; reopening doesn't refill the opening line |
| "That's all" closed every requirement in a theme | Applies only to the requirement asked |
| The chat filed an addition under its own guess of the role | The role is shown on the card to confirm or change before Save |
| A double press recorded a story twice | Save claims the turn atomically ([K-16](../evidence/03-claim-index.md#k-16)) |
| A stated limit was recorded while nothing was offered for Growth, and an item added on one turn was offered again on the next | Growth is offered on the turn it is said, once ([A-108](../evidence/03-claim-index.md#a-108)) |
| On Live, an opportunity page said 4 gaps while the chat said 2 ([M-78](../evidence/04-metric-ledger.md#m-78)): the page counted requirements, and a just-saved story still read light | Every page counts themes, and a light save stays open ([A-78](../evidence/03-claim-index.md#a-78)) |
| On Beta, Growth suggested a document reviewed by someone as an outcome | The plan policy: a document alone is no outcome (`95f8b83`) |

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Guided gap discovery; code-decided stop; one proposal | Verified | [A-08](../evidence/03-claim-index.md#a-08) |
| Themes | Limited (tests stub Jev; measured on 8 jobs) | [A-09](../evidence/03-claim-index.md#a-09) |
| A theme is one gap on every page; a light save stays open | Verified | [A-78](../evidence/03-claim-index.md#a-78) |
| Requirement parts decided by code | Limited (one Beta replay) | [A-10](../evidence/03-claim-index.md#a-10) |
| Role confirmed by the person on Save (guess preselected) | Verified | [K-13](../evidence/03-claim-index.md#k-13) |
| A gap's saved story goes straight to the job | Verified | [A-81](../evidence/03-claim-index.md#a-81) |
| Growth offered on the turn, once | Verified | [A-108](../evidence/03-claim-index.md#a-108) |
| Growth areas kept apart | Limited (the boundary test is a text scan) | [K-28](../evidence/03-claim-index.md#k-28) |
| Growth action plans | Verified (models stubbed in tests) | [A-109](../evidence/03-claim-index.md#a-109) |
| Navi on Growth | Verified | [A-110](../evidence/03-claim-index.md#a-110) |
| All-or-none Save; their own words | Limited (handler rollback; policy only) | [A-111](../evidence/03-claim-index.md#a-111) |
| Growth plans and milestones never evidence | Limited (boundary test names the list's table, which holds the plans, not the milestones' table or plan modules) | [K-33](../evidence/03-claim-index.md#k-33) |
