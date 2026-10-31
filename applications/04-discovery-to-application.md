# Applications 04 — From discovery to application

*Applications 5.0 · describes Live `00eac95` (2026-10-31) · diagram: [Architecture 05](../architecture/05-discovery-to-tracking.md) · case study: [04](../case-studies/04-connecting-discovery-to-application.md)*

**The question this answers:** how does an opening get from "somewhere on the internet" to a
submitted application the person stands behind?

```text
Discover ─► screen ─► queue ─► Save ─► Chart My Course (assess) ─► gap chat ─► Write the résumé
   ─► Ready to apply / N gaps ─► apply kit ─► application chat (optional) ─► browser extension fills
   ─► person submits ─► Mark applied ─► status history ─► interview day on Upcoming ─► interview coach
```

Every arrow that commits the person to something is a human press. No step submits an application.

## 1. Discover Jobs

**Search profiles.** Each field is a *must*, a *preference* or *unknown*, and an empty field is
unknown, never "no". Rules for suggestions ([A-30](../evidence/03-claim-index.md#a-30)):
- Roles are suggested **only from the person's own record**: roles held now or in the last five
  years. Never from saved jobs. My instruction was "stick to my evidence and professions".
- Title variants are searched beside the person's own titles, never instead of them.
- Health, disability and accommodation terms are dropped from every query, and the person is told.
- An unreviewed profile never runs.

**Sources.** No credentials anywhere. A refusal (401, 403, 429) is reported, never worked around.

| Source | How | Cost |
|---|---|---|
| Greenhouse, Lever, Ashby, SmartRecruiters, Workable | Public posting APIs; being returned by the API is the verification | Free |
| Employer career pages | Read only where robots.txt allows, and only their schema.org `JobPosting` data | Free |
| A large employer's own job search | Public feed, robots-checked | Free |
| HN "Who is hiring?" | Public API; top-level company posts' job links only | Free |
| Tavily finder | Web search limited to ATS and career-site domains | Per search; monthly cap |
| Hosted career-site index | An Apify actor (the same data source the open-source *jobsweep* project uses; no code shared). **Admin account only**, title-led searches, weekly, own monthly cap ([A-31](../evidence/03-claim-index.md#a-31)) | Per job returned |

**Screening uses no language model** ([A-32](../evidence/03-claim-index.md#a-32)):
1. **Close.** Embedding similarity of title, department and the opening of the description to the
   person's roles must be ≥ 0.5. Measured spreads: matching roles 0.57–0.70, software roles
   0.43–0.45. Anything below is excluded, with its similarity stated.
2. **Practical rules.** Only a *must* against a stated fact excludes. Unknowns are kept and said.
   Posted conditions go on a "to check" list.
   - **Location:** ten metro areas. Remote is never assumed open to where the person lives unless
     the posting says so ([A-33](../evidence/03-claim-index.md#a-33)).
   - **There is no work-eligibility screen.**
3. **Evidence.** Readable postings only: up to 6 requirement lines, each read by Jev against the
   person's evidence (keep p ≥ 0.5, at most 4 pieces). Close but unkept evidence is "related", never
   direct.
4. **Tier.** Excluded, lower or recommended, with a priority score. Unread or unverified postings
   are never recommended.

**De-duplication** ([A-34](../evidence/03-claim-index.md#a-34)):
- **Within a run**, by board id, requisition id, canonical URL, then company|title|place. Two ATS
  ids are never merged, because real boards list the same title and city twice.
- **Across runs**, an opening is new, seen, updated or a repost. It is closed only when its ATS
  stops listing it, never because a search missed it.
- **Across profiles**, decisions (saved, not interested, applied) carry by identity or link.

**Unreadable postings are held, not guessed** ([A-36](../evidence/03-claim-index.md#a-36)). *Save
anyway* keeps the title, company and link under **Needs details**, and a paste box asks for the
text. The trigger: four title-only saves on Live blocked Chart My Course.

**Scheduled runs** run daily or weekly in the person's timezone. They auto-*assess* (never write) up
to 3 lower-ranked fits per run for review ([A-35](../evidence/03-claim-index.md#a-35)).

**Live funnel** (my account, 18 runs, 2026-10-20 → 10-25): 4,290 found (including repeats across
runs) → 297 distinct openings stored → 92 assessed → 54 recommended → 59 saved. Total cost $1.86
([M-10](../evidence/04-metric-ledger.md#m-10)).

## 2. Assess, close gaps, write

Saving an opening goes through the same intake as *Quick add*. From there:
1. **Chart My Course** assesses ([Applications 01](01-job-analysis-and-assessment.md)).
2. The person chats about the gaps ([Applications 02](02-gap-conversations.md)). A story saved
   there goes straight to the job ([A-81](../evidence/03-claim-index.md#a-81)): Jev reads it once
   for that requirement, exactly as Chart My Course reads a contender, and code makes it the chosen
   story if it is stronger, else an alternate. No new charting, no language-model call.
3. They press **Write the résumé** ([Applications 03](03-resume-planning-writing-review.md)).
4. The opportunities pane says where the opportunity stands (below).

I asked for this gate on 2026-10-22: "It should never write a resume when discovery and charting a
course goes. There should be a gate for review before doing it." ([A-37](../evidence/03-claim-index.md#a-37)).

**Owner**, on a gap's saved story: "I want the evidence I updated from the gap to go straight to the
job without having to do a new charted course ... a deterministic thing" (`3e1992d`, 2026-10-27;
[DEC-45](../product/07-decision-log.md#dec-45)).

**Ready to apply, or N gaps.** Before applying, each opportunity with a written résumé shows a label
on its card in the opportunities pane: *Ready to apply* when it has no gaps, else *N gaps*
([A-79](../evidence/03-claim-index.md#a-79)). Filters cover *Ready to apply* and *Has gaps*.
- **One rule.** The count is the opportunity page's own: the gaps of the newest assessment when it
  is newer than the résumé's review, else the review's. Related requirements (a theme) count as one
  gap, on the pane as on every page ([A-78](../evidence/03-claim-index.md#a-78)).
- **Kept, never stale.** Each count is kept with what it was counted from: the newest résumé, its
  review and next steps, and the assessment with its saved stories applied. A label shows only
  while that basis is current. A stale one is never shown; the job is counted again in the
  background, with no language model, and shows no label until then. Counts are kept because
  building every review view for 71 résumés took 86 s on Beta
  ([M-76](../evidence/04-metric-ledger.md#m-76)).

**Owner:** "If a resume is created for a job and there are no gaps I want it to have a ready to
apply label. If it has gaps then I want the label to say X gaps." (`05abced`, 2026-10-27;
[DEC-46](../product/07-decision-log.md#dec-46)).

## 3. Apply kit and browser extension

**Apply kit (Greenhouse forms)** ([A-38](../evidence/03-claim-index.md#a-38)). The kit reads the
form's questions from the public endpoint, and **code** decides each question's source:

| Source | Questions | Handling |
|---|---|---|
| Details | Name, contact, links | From the profile |
| File | Résumé | The written résumé's PDF |
| Draft | Experience questions, cover letter | Jev picks up to 4 pieces per question (a cover letter up to 8, read against the posting's three top requirements, critical first); one model call with an enforced shape. Unsupported figures, promises and commitments only the person can make are **flagged**. An answer taken from the application chat is labeled "From the application chat — check it and make it yours" |
| Yours | Work authorization, sponsorship, pay, relocation, start date, consent | Never drafted |
| Voluntary | Gender, race, veteran, disability | **Never filled, remembered or sent** |

**Forms the kit can't read.** The kit reads only Greenhouse forms. For Lever and Ashby, and any form
it can't read, the kit says so: the person adds the application's questions word for word, on the
kit or in the application chat, and the browser extension can't fill that form. Their public APIs
expose no form, and one job host disallows its form endpoint in robots.txt
([A-40](../evidence/03-claim-index.md#a-40)).

**Application chat** ([A-73](../evidence/03-claim-index.md#a-73)). *Need help preparing my
application* (on *Prepare my application* and on the kit), *Help with this question* under each
question the kit drafts, and the chat tab on the Prepare stage open a chat for one opportunity's application
questions. It is on Live behind the apply-kit switch. It works with the person, one question at a
time:
1. **Find the question.** Jev reads which of the kit's questions the message names. A question
   pasted from the form is taken as a new one when Jev reads it at p ≥ 0.35; then one model call
   reads the question out of the message and code adds it to the kit
   ([A-76](../evidence/03-claim-index.md#a-76)).
2. **Read the role and the question.** The role is read from the posting first, as for the
   interview coach ([A-62](../evidence/03-claim-index.md#a-62)). It and the company research become
   numbered employer facts, stated or likely. One model call reads the question into at most five
   parts, what it tests and its kind. A length in the question's own words wins over the reading's.
   The record query for each part is code's (the part plus the question), not the model's: a
   model-written query wandered from run to run
   ([DEC-48](../product/07-decision-log.md#dec-48)).
3. **Choose (Jev).** Jev picks record sentences per part, as the coach does. A question asking for an
   example is answered from one piece of work, and one piece holding two pieces of work is never
   joined. What the person has said they want (stated reasons on any opportunity, their career goal
   and vision) becomes a reason of theirs only where Jev reads it as one for this job. Success in a
   piece of work is never read as liking it.
4. **Write (model).** One call writes the answer. It is never shown the record: its declared package
   forbids evidence, the career corpus and roles, and code checks that before the call. Every line
   cites the sources it was given. An answer that runs out of room is written once more with more
   room; failing that, none of it is shown.
5. **Check (Jev, then code).** Jev checks every line against its sources. A line they don't
   establish is marked, never rewritten. An unsourced reason is marked theirs to confirm. A quote no
   source holds, a length over the limit, a draft that ends mid-sentence and the app's labels in
   the text are reported, never repaired.
6. **Use (the person).** *Use this answer* puts the draft in the kit's field. Nothing is submitted.
   How much the person edits it afterwards is kept.

A line the person says is wrong comes out of the draft, its sources out of every answer, and an
exact-text correction is offered for their record, as in the coach. The answer card also offers
*Why this answer?*, *Copy*, *Make shorter*, *Make more personal* and *Try another example*.

**What they tell becomes an offer for their record** ([A-75](../evidence/03-claim-index.md#a-75)).
When the person tells the chat more about their work for an answer, Jev reads which part it answers
and code offers their words for their record. When the answer's draft rests on pieces of their
record, the offer is an addition to the cited piece nearest their words (by embedding); otherwise it
is a new piece, its role preselected when the answer's claims share one. The card shows
what is being added on its own, then the whole piece as Save will leave it, with the addition
highlighted. "It" and similar words are replaced by what they refer to, so the stored text reads on
its own. Code accepts the named version only when every word they said is kept and each added word
is already in the conversation, the draft or the piece; otherwise their exact words are kept.
Nothing is written until Save.

**Owner** (2026-10-30; [DEC-64](../product/07-decision-log.md#dec-64)):
- "doing a great job of taking in what I am saying to update the answers to the questions I am
  trying to answer but its not updating the evidence record when something is discovered, like it
  should" (`75cba31`);
- "I want it so the cards shows whats being added on its own and then shows the whole new text with
  the new stuff being highlighted on what is being added before I save anything" (`e13e428`);
- "Even though I typed It I dont want it to be stored as It. I want it to be stored as the actual
  thing It is supposed to be so if retrieved on its own it doesent need the added context"
  (`e0f9456`).

**The work an answer was drafted from stays its work** ([A-77](../evidence/03-claim-index.md#a-77)).
When the chat drafts from one piece of work and asks a follow-up, the person's answer is combined
with that work; the chat does not switch to another piece while that one still shows a part.
**Owner:** "It asked me a question about the statement it gave me then didnt combine the two
together and lost the context" (`56c565f`, 2026-10-30).

**How well it works.** Measured on five questions from two employers' opportunities, on a Beta copy
of one account, scored by code on ten criteria ([M-72](../evidence/04-metric-ledger.md#m-72)):
every case drafted from checked evidence or asked one focused question, and no invented quote,
figure or outcome reached a draft unflagged. The prose did not reach my own baseline answers. A
first turn on a question took 30–70 s ([M-72](../evidence/04-metric-ledger.md#m-72);
[A-74](../evidence/03-claim-index.md#a-74)). On Live since
2026-10-27, the writer's median was 9.3 s per call
([M-71](../evidence/04-metric-ledger.md#m-71)). The first Live call ran on gpt-5-mini, before the
Claude Haiku assignment was set by hand ([M-68](../evidence/04-metric-ledger.md#m-68),
[D-27](../evidence/05-discrepancies.md#d-27)).

The threshold for a pasted question is thin: stored Live readings put pasted questions at
0.41–0.54 and answers or requests at ≤ 0.07 ([M-74](../evidence/04-metric-ledger.md#m-74)), on one
account. It was lowered from 0.45 after a pasted question was missed
([DEC-65](../product/07-decision-log.md#dec-65)).

**Chrome extension (MV3)** ([A-39](../evidence/03-claim-index.md#a-39)):
- **Installation.** It is a developer-mode ("load unpacked") install from Settings, not a Chrome Web
  Store listing.
- **Pairing.** It pairs with the account by a short check code the person confirms on both sides.
  The token is stored only as a digest and can be revoked per browser.
- **Filling.** It fills text fields, native selects and the résumé file, and outlines what it
  filled.
- **Menus it can't operate.** Greenhouse's searchable menus can't be scripted by synthetic events,
  so the extension shows the kit's answer beside them for the person to pick. It does not force
  them: I ruled out bypassing site protections.
- **Submission.** **It never submits.** After the confirmation page it offers *Mark as applied*.

## 4. Tracking

- **Statuses are set only by the person.** Every change is a status event; undo is a new event
  ([A-41](../evidence/03-claim-index.md#a-41)). Changing a status to *Interviewing* asks for the
  interview's day.
- **The Upcoming card** ([A-72](../evidence/03-claim-index.md#a-72)) sits on My Journey, just below
  "Your career, area by area". It lists everything with a date still ahead, soonest first:
  - trainings, deadlines and events the person adds there;
  - each opportunity's interview day, asked in a date box under every place a status can become
    *Interviewing*: the status menu, the opportunity's own status, and a status the chat proposes.
    A new day moves the opportunity's next interview rather than adding one;
  - a recorded conversation's dated next step (*Record a conversation* asks "When is it");
  - the next interview's day from the interview coach's debrief
    ([Applications 05](05-research-and-interview-prep.md#6-one-contract-many-interviews)).

  Closed opportunities and past dates drop off, and the same interview given twice is listed once.
  Code only, no model. The dates never reach a résumé, an application or a shared link. Days only:
  a time of day is not kept.
- **"Rejected" is distinct from "Declined offer".** Before 2026-10-21 rejections were being filed
  as "Declined", so the activity card counted zero rejections. The vocabulary was fixed, and the
  past data repaired after a backup.
- **The activity card** counts applied, entered-interviewing and rejected over 24 h, 7 d and 30 d,
  from dated history only. Periods before dated history began say "comparison unavailable", never
  zero.

**Throughput, measured:** the densest recorded 40-minute window holds **13** applications, and the
busiest evening 16 ([M-08](../evidence/04-metric-ledger.md#m-08)). An earlier recollection of "21
applications in about 40 minutes" is **not corroborated** by the status history
([M-09](../evidence/04-metric-ledger.md#m-09)). Throughput is not an outcome. Interview and offer
outcomes are not claimed ([Product 05](../product/05-quality-and-measurement.md#what-is-not-measured)).

**The opportunities sidebar** ([A-80](../evidence/03-claim-index.md#a-80)). In order: the heading
with its count and *+ Add*, a full-width *Discover jobs*, search, the views *All / To do / In
progress / Closed*, *Filters* and *Sort* on one row, active filters as removable chips with *Clear
filters*, then the list. Every status falls in exactly one view: To do is explore, résumé and
prepare; In progress is interview and offer; Closed is regroup. Every earlier filter and card label
is kept. On a phone, the list covers the whole screen, as the chat does. Only the view rule has a
behavioral test; the rest are template and style checks.

**Owner** (2026-10-30; [DEC-67](../product/07-decision-log.md#dec-67)): "Simplify the Opportunities
sidebar controls while preserving job-card information" (`8d4c569`), and "The opportunities pane on
mobile is not mobile friendly." (`bf7bb02`).

## 5. Connections and referrals

- **LinkedIn connections import** ([A-43](../evidence/03-claim-index.md#a-43)):
  - previewed, then confirmed;
  - matched by profile URL, then email, while a name alone is only a "possible duplicate" for the
    person to decide;
  - personal details dropped after import.
- **"Who you know there"** is computed when the page renders: connections at the job's company,
  same job family first.
- **Connection message draft** ([A-44](../evidence/03-claim-index.md#a-44)): one model call given
  only the chosen relationship, names, company, role and the person's note, never the career record.
  Nothing is sent.
- **Referral asks and outcomes are not tracked** ([A-45](../evidence/03-claim-index.md#a-45)).

## Known gaps

- Discover's *Already applied* writes no status event, so the activity card misses it
  ([D-13](../evidence/05-discrepancies.md#d-13)).
- The stage at which a rejection happened is not tracked ([A-42](../evidence/03-claim-index.md#a-42)).
- Extension fill rate is unmeasured. The extension has only static tests.
- Counting gaps by theme can make paid embedding and Jev calls when an opportunity or review page renders,
  and a failed grouping silently counts each requirement as its own gap
  ([D-35](../evidence/05-discrepancies.md#d-35)).
- Application-chat offers skip the figure check the evidence chat runs on its proposals
  ([D-36](../evidence/05-discrepancies.md#d-36)). When code rejects a named version of their words,
  the rejection is only logged, so its rate can't be measured
  ([D-21](../evidence/05-discrepancies.md#d-21)).
- A new stage's seed model assignment never reaches an existing database by itself
  ([D-27](../evidence/05-discrepancies.md#d-27)).

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Discover: sources, profiles, screening, de-duplication, queues, schedules | Verified | [A-30](../evidence/03-claim-index.md#a-30)–[A-35](../evidence/03-claim-index.md#a-35) |
| Hosted career-site index | Limited (admin only; one Live run) | [A-31](../evidence/03-claim-index.md#a-31) |
| Unreadable postings held | Verified | [A-36](../evidence/03-claim-index.md#a-36) |
| Assess first; Write gate | Verified | [A-37](../evidence/03-claim-index.md#a-37) |
| A gap's saved story goes straight to the job | Verified | [A-81](../evidence/03-claim-index.md#a-81) |
| Pane labels: Ready to apply / N gaps | Verified | [A-79](../evidence/03-claim-index.md#a-79) |
| A theme counts as one gap on the pane and every page | Verified (grouping itself Limited, [A-09](../evidence/03-claim-index.md#a-09)) | [A-78](../evidence/03-claim-index.md#a-78) |
| Apply kit (Greenhouse) | Verified | [A-38](../evidence/03-claim-index.md#a-38) |
| Forms the kit can't read (Lever, Ashby): questions added by the person | Verified | [A-40](../evidence/03-claim-index.md#a-40) |
| Application chat | Verified | [A-73](../evidence/03-claim-index.md#a-73) |
| Application chat evaluation | Limited (one account; prose below my baseline) | [A-74](../evidence/03-claim-index.md#a-74) |
| Told work offered as an addition, "it" named | Verified | [A-75](../evidence/03-claim-index.md#a-75) |
| A pasted form question taken as new | Limited (thin margin; one account) | [A-76](../evidence/03-claim-index.md#a-76) |
| The work an answer was drafted from stays its work | Verified | [A-77](../evidence/03-claim-index.md#a-77) |
| Browser extension | Limited | [A-39](../evidence/03-claim-index.md#a-39) |
| Status history, activity card | Verified | [A-41](../evidence/03-claim-index.md#a-41) |
| Upcoming card and interview-day boxes | Verified | [A-72](../evidence/03-claim-index.md#a-72) |
| Opportunities sidebar: views, filters, phone layout | Limited (mostly template and style checks) | [A-80](../evidence/03-claim-index.md#a-80) |
| Rejection-stage tracking | Planned (not started) | [A-42](../evidence/03-claim-index.md#a-42) |
| Connections import, "who you know there" | Verified | [A-43](../evidence/03-claim-index.md#a-43) |
| Connection message draft | Limited | [A-44](../evidence/03-claim-index.md#a-44) |
| Referral tracking | Planned (not started) | [A-45](../evidence/03-claim-index.md#a-45) |
