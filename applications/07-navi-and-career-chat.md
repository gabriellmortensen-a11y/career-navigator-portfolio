# Applications 07 — Navi: the chat on every page

*Applications 5.0 · describes Live `00eac95` (2026-10-31) · diagram: [Architecture 01](../architecture/01-components.md)*

**The question this answers:** where does the person talk to Career Navigator, and what may the
chat read about their account when they ask about it?

**Navi** is the chat. Since 2026-10-30 every reply is labeled Navi and every message of the
person's is labeled You ([A-106](../evidence/03-claim-index.md#a-106)). It is one chat with a
thread per focus. In code and in earlier documents it is "the evidence chat"; the work that gave
the general chat read access calls it "Career Chat". Whatever it proposes for the record still
waits for the person's Save ([K-13](../evidence/03-claim-index.md#k-13)).

## One chat, opened from the page

A small tab with the app's icon ("CN") sits on the right edge of every signed-in page. Pressing it
opens the chat **for that page** ([A-105](../evidence/03-claim-index.md#a-105)):

| Page | The tab opens | Described in |
|---|---|---|
| An opportunity's pages (the job, its résumé reviews and runs) at Explore or Résumé | The chat about its gaps | [Applications 02](02-gap-conversations.md) |
| The same pages at Prepare | The application chat (when apply kits are switched on, as on Live) | [Applications 04](04-discovery-to-application.md) |
| The same pages at Interview | The interview coach | [Applications 05](05-research-and-interview-prep.md) |
| Growth | Navi on Growth | [Applications 02](02-gap-conversations.md#from-a-limit-to-a-plan-growth-action-plans) |
| Every other page | The general chat, which can read the account | [Below](#career-chat-reads-the-account) |
| The chat's own page | No tab | — |

- **Code picks the chat** from the page's address and the opportunity's stage. A stage named in
  the address wins. On any error, the general chat opens.
- **Opening sends nothing.** The chat opens without a first message.
- **No model call** is added by the tab or the rail.

**Owner:** "If you are on an opportunity page like explore the opportunity, resume writer etc I
want it to be relative to that page otherwise it should be the general chat." (`a98124c`,
2026-10-30, [DEC-68](../product/07-decision-log.md#dec-68))

**Owner:** "I also want the chat agent to be called navi and that is the name used as the label
when it responds and you for the users responses" (`bf7bb02`, 2026-10-30,
[DEC-67](../product/07-decision-log.md#dec-67)). The box the person types into has no visible
label, only a name for screen readers.

## The rail

The chat has opened in a rail since 2026-10-23. The rail is a frame holding the chat page itself:
beside the page from 1,100 px wide, over it below that, and the whole screen on a phone (760 px and
under) ([A-106](../evidence/03-claim-index.md#a-106)).

| Behavior | How |
|---|---|
| **The chat stays with its page** | Closed and reopened on the same page, it brings back the chat last open there. Another page never inherits it. Open state and the chat's address are kept per page for the browser session |
| **The page keeps up** | When the chat has done something (a save, a gap worked), the page behind reads itself again and puts its own content in place, scrolled where it was. While something is typed on the page, it waits and reloads when the chat closes |
| **Links out of the chat** | Open in the page behind. Messages pass only between frames of the site's own origin. External links open in a new tab |
| **Width** | Draggable, remembered in the browser |
| **Phone** | The rail covers the screen. Since 2026-10-30 the opportunities list does too, over the header and the tab, with the page held still |

The page catching up came from a report quoted in `e756924` (2026-10-29): "the gap work I did is
not updating the opportunity page unless I refresh it".

**Why the rail is Limited:** its tests read the source of its script and templates. No browser
test drives the rail, the catch-up or the phone layout. "Navi" is the page's label: only the Growth
chat's policy tells the model its name.

## The menu around it

On 2026-10-30 the menu changed with the tab ([A-105](../evidence/03-claim-index.md#a-105),
[DEC-68](../product/07-decision-log.md#dec-68)):

| Before | Now |
|---|---|
| Your Career listed Opportunities, Evidence, Flagship résumés, Chat, Tune my evidence, Connections and Growth | **Four pages:** Opportunities, Evidence, Connections, Growth |
| Chat was a menu item | Reached from the tab and from each page's chat links |
| Flagship résumés was a menu item | A card on Evidence ("See flagship résumés") |
| **Tune my evidence** (shipped 2026-10-21) | **Retired.** Its addresses lead to Career Direction, where the target roles it read against are kept and each is read on its own page ([A-107](../evidence/03-claim-index.md#a-107)). Its years reading lives on there ([D-14](../evidence/05-discrepancies.md#d-14)) |
| Sharing was reached only from a button on Evidence | **Settings › Sharing** since 2026-10-31 (`79658ad`). Settings › Portfolio is reached from it ([Applications 06](06-sharing-and-integrations.md)) |

**Owner:** "I want to deprecate the tune my evidence page and the chat option from the navbar under
your career. … The only thing that should be left under the Your Career page is Opportunities,
Evidence, Connections and Growth" (`a98124c`).

## Career Chat reads the account

The person can ask the general chat, or a gap chat, about their own account: "what gaps did
reviewers find where I was rejected?", "which résumé did I send to O3?", "who do I know at companies
where I have open applications?", "which of my stories have never been used?". The chat answers
from records read for that message, with the app's counts, says whose each record is, and lists
links to the pages that show them ([A-102](../evidence/03-claim-index.md#a-102)). Reading changes
nothing.

**Owner:** "Give Career Chat governed read access to the user's complete Career Navigator record."
(`eb73d50`, 2026-10-28, [DEC-49](../product/07-decision-log.md#dec-49))

### How a message is read

| Step | Who | What |
|---|---|---|
| 1. Route | **Jev** (stage `chat_reads_route`) | One fixed question per read operation, each asked about the chat's previous reply and the message. Each answer is kept at its own line, between 0.6 and 0.8 |
| 2. Prune | Code | An operation whose question another answers is not read twice |
| 3. Resolve | Code | What the message names: an opportunity by its number in the chat's own list, by the chat's focus, or by a company's normalized name (title words choose among several); a role; a story by its number in the last reply. **Never guessed:** several matches are asked back ("It names several opportunities: … Ask which one.") |
| 4. Read | Code | 14 plain read operations (below). No model, no Jev, no writes |
| 5. Across rejected opportunities | Code, then Jev and embeddings | Gap kinds and recurring groups ([below](#gaps-across-rejected-opportunities)) |
| 6. Render | Code | A `RECORDS` part: what was read, code's counts, what is missing and why, and whose each record is |
| 7. Answer | **Model** (`evidence_chat`, Claude Haiku) | Everything the chat already gets, plus `RECORDS`. The page lists what was read, with links |

The read operations: the opportunities list; one opportunity; its posting; its stage history; its
reviews; gaps across rejected opportunities; résumés sent and what came after; a role's evidence and
where it was used; history never used; a story's corrections; companies applied to more than once;
what waits on the person; connections at open opportunities; an application's questions.

**Where it runs.** The general chat and the gap chats. The interview coach, the application chat
and Navi on Growth have their own paths and do not read. A failure to read is said in the
answer, never hidden.

### Whose each record is

Every record read carries its authority, and the chat is told to keep them apart
([K-32](../evidence/03-claim-index.md#k-32)):

| Authority | Said to the chat as |
|---|---|
| The person's record | "your own words, saved by you" |
| Something the person set | "set by you" |
| The person's note | "your own note" |
| The posting | "the employer's words … not evidence of yours" |
| Career Navigator's reading | "an estimate" |
| A reviewer's assessment | "a simulated recruiter or hiring manager: not the employer's view, and not a reason an employer gave" |
| Résumé wording | "not evidence" |
| Generated text | "written by Career Navigator from your record" |
| Company research | "unverified" |
| A connection | "a connection you added" |

**A posting reaches the chat only inside `RECORDS`**, when the person asks what it says, labeled
the employer's words and untrusted ([K-31](../evidence/03-claim-index.md#k-31)). This narrows the
chat's "no posting" rule rather than removing it. Anything to add still goes through a proposal and
Save, but no test covers a proposal made on a turn that also read a posting.

### Gaps across rejected opportunities

([A-103](../evidence/03-claim-index.md#a-103))
- **One gap is one requirement at one opportunity**, with the reviewers' points kept apart. A
  repeated posting is one opportunity, matched by exact keys only.
- **Kinds come from stored fields first** (a qualification, reviewer uncertainty), then from four
  Jev questions on the reviewer's note.
- **Recurring groups:** pairs at cosine ≥ 0.5 go to Jev's same-area question. Groups are for the
  answer only and are never stored.
- **Every such answer carries a fixed sentence:** "These are gaps identified by Career Navigator's
  reviewers. They are not confirmed reasons the employers rejected the applications."

On Live the read layer works without the evidence timeline, career themes and major outcomes. A
story's title is its own first sentence, and gaps are grouped by the gap chat's method
([P-37](../evidence/03-claim-index.md#p-37)). **Owner:** "Leave the evidence timeline, career
themes, and major outcomes off of live." (`88123b4`, [DEC-50](../product/07-decision-log.md#dec-50))

### What it never reads

Written down with a reason for each, and enforced by there being no operation that reads it
([P-33](../evidence/03-claim-index.md#p-33)):
- secrets: password hashes, sessions, invitation, reset, share, extension and connector tokens;
- security records: sign-in, rate limits, connector audit;
- raw provider payloads, policies and prompts, admin pages, and Jev's and a model's working;
- other accounts, and tables not owned per account, so living-résumé visitor conversations are never
  read;
- saved answers about work authorization, sponsorship, age, pay, logistics and self-identification;
- connections' email, phone, LinkedIn link and appearance.

Tests cover three of these: other accounts, the person's own eligibility answers, and connections'
email.

### Guarantees and where they are weaker

| Guarantee | By |
|---|---|
| Read-only | A test listens to every statement the reads send: only reads |
| The chat's evidence and retrieval are unchanged by reading | Test, byte for byte |
| Tenancy | Row-level security, as on every page; test |
| Counts are code's | The part states them in words; the policy says never to count lines itself |
| The chat and the review page read the same rows | Test |

Weaker ([A-104](../evidence/03-claim-index.md#a-104)):
- **Calibrated once, on Beta.** The routing lines and the note readings were set on one account
  ([M-75](../evidence/04-metric-ledger.md#m-75)). Jev is stubbed in every test, so routing
  accuracy has no test.
- **Up to 14 Jev questions per message**, asked one after another, cached by words.
- **The coverage document is Beta's.** On Live it lists pages and a test that exist only on Beta
  ([D-29](../evidence/05-discrepancies.md#d-29)).

### Use on Live

Since the read layer reached Live on 2026-10-28, one of 40 chat turns on my account read the account.
Routing asked Jev 336 questions, $0.0071 in all, a median 0.2 s each; answers served from the
cache write no row ([M-70](../evidence/04-metric-ledger.md#m-70)). Every evidence-chat call on Live
since 2026-10-25 ran on Claude Haiku ([M-68](../evidence/04-metric-ledger.md#m-68)).

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Tab opens the page's chat; four-page menu; Sharing in Settings | Verified | [A-105](../evidence/03-claim-index.md#a-105) |
| The rail: stays with its page, page keeps up, Navi and You labels, phone layout | Limited (source-inspection tests only) | [A-106](../evidence/03-claim-index.md#a-106) |
| Tune my evidence | Superseded by Career Direction's role pages (`a98124c`) | [A-107](../evidence/03-claim-index.md#a-107) |
| Career Chat read layer | Verified | [A-102](../evidence/03-claim-index.md#a-102) |
| Reviewer gaps across rejected opportunities | Verified | [A-103](../evidence/03-claim-index.md#a-103) |
| Read-layer calibration | Limited (one Beta account; Jev stubbed in tests) | [A-104](../evidence/03-claim-index.md#a-104) |
| Every record read carries its authority | Verified | [K-32](../evidence/03-claim-index.md#k-32) |
| A posting reaches the chat only inside `RECORDS` | Limited (no test of a proposal on a posting-reading turn) | [K-31](../evidence/03-claim-index.md#k-31) |
| What Career Chat never reads | Limited (enforced by construction; three exclusions tested) | [P-33](../evidence/03-claim-index.md#p-33) |
