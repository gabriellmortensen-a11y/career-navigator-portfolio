# Applications 05 — Company research and interview preparation

*Applications 5.0 · describes Live `00eac95` (2026-10-31) · diagram: [Architecture 08](../architecture/08-interview-coach.md)*

**The question this answers:** once an application is in motion, how does the system help the
person prepare, using what they have actually done and what is publicly known about the company?

Since 2026-10-25 the answer is the **interview coach**: a conversation that leads the person
through one interview's preparation and fills in the Interview Prep page as it goes
([A-71](../evidence/03-claim-index.md#a-71)). The round preparation it replaced still shows what
it produced before, but no page starts a new one
([A-52](../evidence/03-claim-index.md#a-52), [D-39](../evidence/05-discrepancies.md#d-39)).

## Company research

A research run happens only when the person presses for it; opening a page never searches
([A-50](../evidence/03-claim-index.md#a-50)).

1. **Search.** At most four Tavily searches, built only from public posting fields, five results
   each.
2. **Filter (code).** Keep sources on the company's own domain, or that name the company, up to 12.
   If none survive, the run ends "empty" with no model call.
3. **Write.** One model call writes the brief. Claude Haiku is the default: on replays it produced
   comparable briefs at a lower cost.
4. **Admit (code).** Citations to sources the writer wasn't shown are dropped. A brief needs the
   company's identity confirmed and at least one web-sourced fact.

The brief appears on *Prepare my application* and on the interview pages.

**Where the brief goes next.** The interview coach is given it beside the posting, to say as the
research's, never instead of the posting. The application chat gets its facts as numbered employer
facts, stated or likely ([A-73](../evidence/03-claim-index.md#a-73)). The coach's role reading
never sees it: that call reads the posting alone ([A-62](../evidence/03-claim-index.md#a-62)).

**A comparison that kept the simpler path.** Claude's own web search was tried for sourcing on Beta
([A-51](../evidence/03-claim-index.md#a-51)):
- Its sources were staler, it missed the company's official site, and it cost several times more.
- The newer search tool returned no citable text at all.

Tavily stayed. Claude search remains Beta-only behind a guard that refuses Live.

## Interview coach

The coach is the evidence chat focused on one interview, in its own thread, so nothing from another
opportunity's coaching shows ([A-61](../evidence/03-claim-index.md#a-61)). The person opens it from
Interview Prep, or from the chat tab while on that stage. One governed model call writes each turn,
in an output shape the API holds.

**Owner:** "a guided coaching conversation" (`bec595c`, 2026-10-25;
[DEC-37](../product/07-decision-log.md#dec-37)). The first coach, earlier that day, was a menu of
requirement topics and a stage checklist. It was replaced the same day.

**Owner:** "… I don't want that button I want the coach to guide all the way through the plan and
fill out the page. The navigate the interview card needs to go so the buttons are at the top."
(`2c05495`; [DEC-41](../product/07-decision-log.md#dec-41)). That card held the *Prepare* button
and the links to Quick answers and the walkthrough (see
[Round preparation](#round-preparation-quick-answers-and-the-walkthrough)).

### What a session looks like

1. **A plan.** The coach reads the role (step 1 below), then writes a plan of three to five items
   (code keeps at most five) for this interview: for example *Your introduction*, *A product you built*, *Why this role*,
   *Questions for the recruiter*. Code keeps the plan and never takes a rewritten one unless the
   person asks.
2. **One item at a time.** Each reply is headed so it can be scanned: *What the role needs*, the
   turn's work, *What I need from you*. It ends with one question, and the question comes last.
3. **Progress counts only what happened.** A plan is not an explanation, a draft is not practice,
   and understanding comes only from an answer the person gave.
4. **The page fills in.** Interview Prep shows, in the plan's order with jump buttons: what the
   role is for, each item's standing, the verified drafts with their footnotes, what is still
   missing, and work waiting for the person's Save.
5. **Nothing becomes evidence by itself.** Teaching, drafts and practice never become career
   evidence. Anything that would change the record waits for the person's Save.

### Who decides what

| Step | Who | What |
|---|---|---|
| Read the role from the posting | Model (`role_understanding`) | Purpose, problems, outcomes, hiring signals, unknowns, what this interview listens for |
| Order the signals for this stage | Jev | A probability, used for order only |
| What each answer must establish | Code | The answer contract, from the role reading |
| Which sentences of the record show it | Embeddings, then Jev | Pieces near each need, then each sentence: direct? owned? |
| Write the turn | Model (`evidence_chat`) | The reply, the plan (once) and the draft, citing claims |
| Does each draft line hold | Jev | Its cited words against the line |
| What the person's message means | Jev | Fixed yes/no questions |
| Keep the plan; count progress; write coverage; offer told work; resolve disputes; read dates | Code | From kept state and Jev's readings |
| Anything that touches the record | The person | Save |

Both model stages are assigned Claude Haiku. On Live, every role reading and coaching turn since
2026-10-25 ran on it ([M-68](../evidence/04-metric-ledger.md#m-68)).

### 1. The role first, from the posting alone

Before anything about the person is read, one model call reads the posting
([A-62](../evidence/03-claim-index.md#a-62)). It is given the title and company, the posting,
its numbered requirement lines, the interview stage and what the person said about the interview.
Its declared package forbids the record, roles, résumé, reviewer readings, gaps, earlier coaching,
the conversation and company research. Code checks the package before the call is sent.

It returns:
- why the role likely exists and whom it serves;
- its problems, outcomes and ownership, each with its basis, stated or inferred;
- four to seven hiring signals, each with what it means and the lines it draws on;
- what the posting leaves unknown;
- what this interview is likely to listen for, including what the person's opening should
  establish.

**Code admits the reading.** A part is "stated" only when its basis is explicit **and** its quote
is found in the posting. Quotes not found in the posting are not kept, and a part called explicit
with none left is a finding. Requirement numbers the call wasn't shown are dropped and recorded.
Signals that copy a line and lists past the policy's limits are recorded as findings and kept as
they came. A basis other than explicit or inferred is read as inferred. An empty reading keeps
nothing and is said. One reading is kept per posting and interview stage. Résumé and record writers
never read it.

Asked "what is this role really about?" or "what will the recruiter expect?", the coach answers from
this reading, with no claims given and nothing of the record shown. A thin record never changes the
reading.

**Owner** decision, 2026-10-25 ([DEC-38](../product/07-decision-log.md#dec-38)); the commit
(`c2e2081`) carries no quote. The trigger: asked what a recruiter would expect, the coach gave a
generic checklist and drafted an introduction before knowing what the employer was hiring for.

### 2. Answers only from verified, requirement-relevant claims

**Owner:** "Build interview answers only from requirement-relevant, verified evidence" (`291517d`;
[DEC-39](../product/07-decision-log.md#dec-39)). The trigger, on Live: an introduction drafted
from 35 pieces of the record, leftover test text among them
([M-77](../evidence/04-metric-ledger.md#m-77)).

How an answer is built ([A-63](../evidence/03-claim-index.md#a-63)):
1. **Code** sets what the answer must establish, from the role reading. For an introduction:
   what this interview's opening should establish, plus the person's reason for the role. For
   other items: up to three hiring signals they draw on. Also a length per kind of answer, at most
   four needs, and what would distract.
2. **Embeddings, then Jev**, choose claims. Per need, cosine reads the top 8 pieces and Jev keeps
   those at p ≥ 0.15, at most 4. Jev then reads each sentence of those pieces: does it show the
   need directly, and was the work theirs? Direct and owned both need p ≥ 0.5. A sentence stands for
   one need only. A related sentence (p ≥ 0.25) is used only after the person says they have
   nothing more direct.
3. **Code** gives the writer the fewest claims that answer: the record first, the person's told
   words only where no direct claim exists. A sentence they disputed is excluded.
4. **The model** writes the draft, each line citing claim keys. It is shown only those claims and
   what the person told: never the record; the posting's requirement lines only while the role hasn't
   been read.
5. **Jev** checks each line ([step 3](#3-footnotes-nothing-to-press)).
6. **Code** writes what the answer covers into the reply, need by need: "footnote 2", "missing — no
   verified evidence on your record yet", "on your record, but not in this draft". The reply
   cannot call an answer complete; coverage is code's.

What nothing verified shows is asked about, one question at a time. It is never filled with weaker
material. **Owner:** "The intro has to satisfy the job requirements or the coach needs to say
evidence is missing" (`56e932b`), and "The question needs to be at the end of the message instead
of the beginning" (`345d02a`).

### 3. Footnotes, nothing to press

Every line of a draft has a footnote ([A-64](../evidence/03-claim-index.md#a-64)). Hover or tap
shows the exact words it rests on, from which role, why that evidence, and Jev's reading of
whether those words establish the whole line (p ≥ 0.5). A line its words don't establish is
marked, and the answer is not ready while it stands. A line that cites a key it wasn't given is
marked too.

**Owner:** "Not a button a user presses" (`1e85a1a`) and "I dont want any boxes at all. I just
want foot notes." (`7e02ed2`) ([DEC-40](../product/07-decision-log.md#dec-40)). These removed the
*Take this line out* and *Add it* buttons and the box under each draft.

**Known gap: approving triggers a redraft.** When the person approves a draft ("Sounds great")
that has a line Jev reads as unsupported, code marks the draft stale and the coach writes it again
before it can stand. A check is starting a rewrite there, which conflicts with the project rule
that checks only detect and report ([D-31](../evidence/05-discrepancies.md#d-31)). The application
chat, by contrast, only marks such a line.

### 4. Work the person tells: validated by asking, offered by code

When the person tells the coach about their own work ([A-65](../evidence/03-claim-index.md#a-65)):
1. **Jev** reads whether the message tells work, and which need it speaks to. It is used as
   theirs for that need: said as theirs, not saved.
2. **The model** asks for what makes it usable: what system, their personal part, the outcome.
3. **Code** offers their own words, verbatim, as an addition to their record whenever the turn's
   call offered nothing. Never their reason for the role. More told about the same work replaces
   the waiting offer. The role is preselected when the answer's record claims all come from one
   role; otherwise it is chosen beside Save.
4. **Jev** reads whether a piece of that role already says it all (`chat.matched`); if so it is
   shown, not offered.
5. **The person** presses Save. It goes through the evidence chat's Save and a Change Document
   ([K-13](../evidence/03-claim-index.md#k-13)).

"Validated" is conversational, not a gate. Code offers on any turn where the call offered nothing,
so an offer can come before the coach's follow-up questions. The person decides at Save. An item
is not finished while told work is still being explored or waiting to be saved. What the app sends
for the person ("I saved it to my record. Go on.") is never shown as their message.

### 5. What a message means is Jev's reading

**Owner:** "It needs to be able to reason on human language on its own. Hard coded signals are a
failure." (`0018434`, 2026-10-26; [DEC-43](../product/07-decision-log.md#dec-43)). The trigger:
"Let's come back to this" was not understood, and "Ok next" accepted an unfinished answer. The
coach's phrase patterns and word lists were removed. This applies the rule that Jev selects
([DEC-16](../product/07-decision-log.md#dec-16)).

Each meaning a rule acts on is a fixed yes/no question Jev reads about the person's reply beside
the coach's last message ([A-66](../evidence/03-claim-index.md#a-66)): leave this part for now,
accept the draft, yes, none, not sure, lead, draft it, a question about the role, tells their work,
gives their reason, another part, a dispute, how an interview went, a new application question.
- Code acts on a threshold per question.
- A question is read only when a rule asks, once per message, and the reading is cached.
- Leaving an unfinished part is confirmed by code, and only their yes sets it aside.
- Code still reads what isn't meaning: the app's own messages, dates, footnote numbers and the
  question mark.

**Why it is Limited.** The thresholds were set against 106 messages from one account, on Beta
([M-73](../evidence/04-metric-ledger.md#m-73)). Tests read through a stand-in for Jev with fixed
Beta readings. A few word lists still read the person's words when a dispute is ambiguous
([D-33](../evidence/05-discrepancies.md#d-33)).

### 6. One contract, many interviews

**Owner:** "It should all just be a reusable contract where the identity like hiring manager or
recruiter is agnostic but sets the context for the agent. Same with context from coaching history
... the interview could move to a loop as an example as well." (`5244374`;
[DEC-44](../product/07-decision-log.md#dec-44)). The trigger: a hiring-manager preparation asked
again for the person's reason, because code had retired the reason when it read it again.

([A-67](../evidence/03-claim-index.md#a-67))
- **Every stage, one contract.** A recruiter screen, a hiring-manager interview, a panel or loop,
  and an executive interview are prepared by the same code. The stage sets only what the
  interviewer is called, whether one answer at that depth is enough, whether a reasoning check comes
  before practice, and a recruiter's bounds. What the stage listens for comes from the role reading
  for that stage.
- **Debrief.** After an interview the person tells the coach how it went. Jev reads the outcome
  (moving forward, waiting to hear, turned down) and what kind of interview comes next. Code reads
  dates. The model reads who the next interview is with, shown on the card for the person to check.
  The call acknowledges and asks nothing; code adds a card in the person's own words and one
  question, last.
- **Save.** Saved, the card becomes the opportunity's recorded conversation, never career
  evidence. The next interview's day goes on the Upcoming card
  ([A-72](../evidence/03-claim-index.md#a-72);
  [Applications 04](04-discovery-to-application.md#4-tracking)). The finished preparation folds
  into an interview history, shown as it was.
- **The next round.** The next preparation starts fresh, with earlier interviews as context. Jev
  reads what the person told before against each open need of a new answer. What shows a need is
  theirs for it and is not asked again. Waiting to hear starts nothing; turned down plans nothing
  more.

### 7. Their reason, drafted from the record and checked as an inference

When the person hasn't said why they want the role, the coach drafts a reason from their record
([A-68](../evidence/03-claim-index.md#a-68)):
1. **Code** gives the reason need the employer's problem, from the role reading.
2. **Embeddings and Jev** read the record against that problem in the same search. The strongest
   sentence of the person's own work, at the related level or above, is what the reason draws on.
3. **The model** writes the reason line, citing that work. An introduction is one connected story
   with the reason as its thread, not a list followed by a reason.
4. **Jev** checks the line as an inference: a fair inference from all the work it cites beside the
   employer's problem, adding no work, scope, result, title or number (p ≥ 0.5).
5. **Code** labels it: "inferred from your record — keep it if it's true for you, or tell me your
   own reason". Kept as it is, it becomes theirs.

With nothing to infer from, the coach says so, then asks. A request such as "write my reason from
my history" is never stored as their reason.

**Owner** (2026-10-30; [DEC-63](../product/07-decision-log.md#dec-63)): "I keep trying it to write
the first part or at least give me a draft that I could say is good enough or not from my career
history ... if not then the coach says its not and then asks" (`e0b79e0`), then "… Its trying to
find direct evidence as the test versus a test of the things it was infered by instead. The whole
thing needs to be a cohesion of the data and how it ties to the job role" (`a81cf41`). Before, the
reason was theirs alone to say and was left out of every draft; then a drafted reason was checked
as if it were a direct fact, against one sentence, and was marked unsupported. This behavior is
new and rests on one Live session.

### 8. Disputes resolved by code, corrected to the exact text

The person says a footnote, a sentence, or a phrase in a line is wrong
([A-69](../evidence/03-claim-index.md#a-69)):
1. **Jev** reads the message as a dispute.
2. **Code** finds what it points at. "Footnote 3" is line 3 of the draft they are looking at, or of
   the draft they name. A quote matches by most of its words. Otherwise a unique run of four or
   more of their words. If two sources could be meant, code asks which first, and their answer is
   the same dispute.
3. **Code** takes the claim out of the draft and every answer at once, and keeps the disputed words
   from every later call.
4. **Code** offers the change to that exact record text: only the words they named when they name
   part of a sentence, in the record's own wording; the whole piece retired when they name nearly
   all of it.
5. **The person** presses Save. A correction writes the new story and retires the old one with its
   replacement named ([K-15](../evidence/03-claim-index.md#k-15)).

No model call decides any of it, and the coaching model cannot offer a removal. Saying something is
wrong is never taken as work told. **Owner:** "I found that there is an error in one and tried to
fix it and it falls apart at that point. Need this fixed so it actually follows what I am doing"
(`aa49142`, 2026-10-30). Before, a dispute resolved only by a footnote number or a near-whole quote.

### 9. Their words, kept for the opportunity

Their reason for wanting the opportunity, their answers to practice questions and work they told
the coach are kept with the opportunity ([A-70](../evidence/03-claim-index.md#a-70)). They are
listed on Interview Prep and read again by its later preparations, a conversation started over
included. A newer reason replaces an older one; the same reason read into another answer does not
retire itself. The application chat reads every opportunity's stated reasons as candidate reasons
of the person's ([A-73](../evidence/03-claim-index.md#a-73)). They are never career evidence.

**Owner:** "My answers should become retrivable evidence for the job too. Like the motivation part"
(`05b0624`; [DEC-42](../product/07-decision-log.md#dec-42)). "Evidence for the job" was built as
statements kept per opportunity, never as career evidence.

### Known gaps in the coach

- Approving a draft with an unsupported line triggers a redraft
  ([D-31](../evidence/05-discrepancies.md#d-31)).
- The coach's own descriptions lag the code: the capability registry still labels its routing
  "by the words of the message", a Jev stage description still names posting lines, and two
  docstrings are out of date ([D-32](../evidence/05-discrepancies.md#d-32)).
- Word lists still read the person's words in dispute disambiguation
  ([D-33](../evidence/05-discrepancies.md#d-33)).
- A kept statement records no link to the turn it came from, and the application chat's reading
  across opportunities is undocumented in the code ([D-34](../evidence/05-discrepancies.md#d-34)).
- Coach turns store no wall-clock seconds, so coach latency can only be approximated from the call
  ledger ([D-21](../evidence/05-discrepancies.md#d-21)).
- The claim thresholds (0.5, 0.25) are not recorded as calibrated against a labeled set. The
  model check for the role reading has not been run. The quality of drafted answers is unmeasured
  on Live.

## Round preparation, Quick answers and the walkthrough

Before the coach, each interview stage started with a **round preparation** built from **evidence
Jev chose**, not evidence the writer picks ([A-52](../evidence/03-claim-index.md#a-52)):
1. Cosine reads the top 12 pieces.
2. Jev's "establishes" question keeps those at p ≥ 0.5, at most 4.
3. With no Jev credential the stage fails visibly. A neighborhood is never passed off as support.

Since `2c05495` (2026-10-25) no page starts one. Its *Prepare* form, the *Quick answers* link and
the walkthrough link were in the *Navigate the interview* card, which was removed so the coach
leads the page. The routes still answer at their addresses
([D-39](../evidence/05-discrepancies.md#d-39)).

| Stage | What it does | Controls | Since 2026-10-25 |
|---|---|---|---|
| **Preparation** | Likely questions, STAR stories with proof depth (interview-ready / résumé-capable / thin), pressure points with their basis | Input hash reuse; strict output schema; citations not shown are dropped | **Superseded** for starting one, by the coach. An earlier preparation still shows |
| **Practice** | The person answers; feedback | Strict schema; dropped figures and promises flagged, never fixed | Works on an earlier preparation's questions |
| **Your own questions** | Questions the person adds are practiced like the suggested ones | The practice call is told the person added it | Works |
| **Offer a suggestion** | A reframed answer beside the person's, once per answer | Adds no facts; gaps marked as prompts | Works |
| **Find answers in my evidence** | The evidence that answers a question | Support at p ≥ 0.5; up to 2 "related at most" pieces at ≥ 0.15 | Works |
| **Quick answers** | A glanceable say-first / points / close per question, for freezing moments ([A-53](../evidence/03-claim-index.md#a-53)) | Kind decided by code: *answer*, *bridge* (nearest related evidence, labeled) or *none*, which opens the chat on that question | Works at its address; **no page links to it** |
| **Guided walkthrough** | 8 steps on top of the above ([A-54](../evidence/03-claim-index.md#a-54)) | **Known defect:** writes from the preparation's cosine candidate pool, not Jev's chosen set ([D-12](../evidence/05-discrepancies.md#d-12)) | Defect unchanged; **no page links to it** |

**Earlier conclusions keep their basis.** Pressure points carry their basis: feedback, requirement,
expectation or possible. Something the interviewer said is labeled differently from an inference
nobody said ([K-20](../evidence/03-claim-index.md#k-20)). The coach's role reading keeps the same
line: stated only with a quote found in the posting, otherwise inferred
([A-62](../evidence/03-claim-index.md#a-62)).

## Output shapes held by the API

Output shapes are enforced by the API, not repaired in a parser. Practice feedback lists used to come back
as prose or objects. Since 2026-10-20 four stages send a strict JSON schema to the provider: the
preparation, practice, evidence answers and the apply kit's drafted answers
([A-52](../evidence/03-claim-index.md#a-52)). Since 2026-10-25 the role reading
([A-62](../evidence/03-claim-index.md#a-62)) and every coaching turn
([A-61](../evidence/03-claim-index.md#a-61)) do too, and since 2026-10-27 the application chat's
question reading and its writer ([A-73](../evidence/03-claim-index.md#a-73)).

One limit showed up on a Beta replay: with the role reading's opening as objects, the strict grammar
was too large and every reading failed. The opening became plain strings (`99134d5`).

## What I decided not to build

A live answer tool for video interviews was discussed and **not built**. Covert transcription of an
interviewer raises consent problems: all-party consent laws and employer rules. Preparation beats
mid-interview answers. *Quick answers* was the glanceable compromise; since 2026-10-25 no page links
to it ([A-53](../evidence/03-claim-index.md#a-53)).

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Company research (Tavily + brief + admit) | Verified | [A-50](../evidence/03-claim-index.md#a-50) |
| Claude web search for research | Experimental (Beta-only, not adopted) | [A-51](../evidence/03-claim-index.md#a-51) |
| Interview coach: a guided conversation, plan kept by code, progress only from what happened | Verified | [A-61](../evidence/03-claim-index.md#a-61) |
| Role read from the posting alone, first | Verified | [A-62](../evidence/03-claim-index.md#a-62) |
| Answers only from verified, requirement-relevant claims | Verified | [A-63](../evidence/03-claim-index.md#a-63) |
| Draft-line footnotes | Limited (approval triggers a redraft, [D-31](../evidence/05-discrepancies.md#d-31)) | [A-64](../evidence/03-claim-index.md#a-64) |
| Told work validated by asking, offered by code | Verified | [A-65](../evidence/03-claim-index.md#a-65) |
| Jev reads what a message means | Limited (one account's calibration; Jev stood in by tests) | [A-66](../evidence/03-claim-index.md#a-66) |
| One contract for every stage; debrief; interview history | Verified | [A-67](../evidence/03-claim-index.md#a-67) |
| Reason drafted from the record, checked as an inference | Verified | [A-68](../evidence/03-claim-index.md#a-68) |
| Disputes resolved by code; exact-text corrections | Verified | [A-69](../evidence/03-claim-index.md#a-69) |
| Their words kept for the opportunity, never evidence | Verified | [A-70](../evidence/03-claim-index.md#a-70) |
| Interview Prep led by the coach; old entry points removed | Verified | [A-71](../evidence/03-claim-index.md#a-71) |
| Round preparation: starting one | Superseded by the coach (`2c05495`); an earlier preparation, own questions, suggestions and evidence answers still work | [A-52](../evidence/03-claim-index.md#a-52) |
| Quick answers with bridge | Limited (works at its address; no page links to it) | [A-53](../evidence/03-claim-index.md#a-53) |
| Guided walkthrough | Limited (evidence-source defect; no page links to it) | [A-54](../evidence/03-claim-index.md#a-54) |
