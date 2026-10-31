# Applications 01 — Job analysis and assessment

*Applications 5.0 · describes Live `00eac95` (2026-10-31) · diagram: [Architecture 03](../architecture/03-requirement-analysis-and-matching.md)*

**The question this answers:** given a job posting, what does it actually ask for, how well does
the person's evidence show it, and which shortfalls matter?

Rules read the posting, Jev answers fixed questions, embeddings retrieve, and code decides. The path
from posting to assessment makes **one kind of language-model call, a stated exception I chose**: a
requirement line that lists several asks is read once for the asks it holds
([A-05](../evidence/03-claim-index.md#a-05), [DEC-47](../product/07-decision-log.md#dec-47)). Nothing else on this path calls a model.

## 1. Reading the posting (rules)

- **Every content line is a candidate.** It is labeled *ask*, *about*, *logistics* or *unclear*.
  Section headings corroborate a label but don't decide it. Nothing is dropped silently
  ([A-01](../evidence/03-claim-index.md#a-01)).
- **Lines are split only at whole sentences.** Lines that a fixed-width paste broke are rejoined. A
  sentence opening with "Or" stays with the requirement it offers another way to meet; it never
  becomes a requirement of its own ([A-95](../evidence/03-claim-index.md#a-95)).
- **Junk is retired, not deleted.** Jev sets aside lines that aren't requirements, below 0.5. On 500
  real lines from 16 postings, 143 (29%) were set aside, and all were junk on inspection. If Jev
  fails, every line is kept ([A-02](../evidence/03-claim-index.md#a-02),
  [M-16](../evidence/04-metric-ledger.md#m-16)).
- **Employer-only language is reworded by rules.** "Experience with \<the employer's internal
  product\>" becomes the product's description. The employer becomes "the company". The original is
  retired and kept. A candidate can't show experience with a product that only exists inside the
  employer, but they can show the underlying work ([A-03](../evidence/03-claim-index.md#a-03)).
- **The result is frozen with a fingerprint.** Later stages refuse to run against requirements that
  drifted. An old posting is re-read when the reader improves.

**A line that lists several asks** (since 2026-10-27). One posting line asked for several things in one
sentence. Read whole against single sentences, no story could show it, so the job kept it light while
the gap chat established two of its parts. I chose "one small call" over rules for this (my words,
`a41a455`; [DEC-47](../product/07-decision-log.md#dec-47)):
1. At Chart My Course, *code* picks the lines that look like several asks: long (90 characters or
   more) and listing (at least two separators).
2. *One call* per posting (Haiku by assignment) reads all such lines, each once, for the asks it
   holds, in the line's own words.
3. *Code* admits a division only if every ask is made of the line's own words (plus joining words
   such as "and", "experience", "ability"), inventing nothing. It then retires the line (never
   deleted), appends its asks and re-freezes the set.
4. A line read as one ask is marked and never read again. A list of tools ("SQL, Tableau, Power BI")
   is one ask, whose parts the gap chat reads by rules.

On Live, 145 lines have been divided into 416 asks and 190 read as one ask
([M-67](../evidence/04-metric-ledger.md#m-67)). The test that enforces "no model in Chart My Course" now checks that this is the
only model step in the flow's registry; it checks the registry, not the call graph
([A-05](../evidence/03-claim-index.md#a-05)).

**Facts vs requirements.**
- A requirement about the person's situation is a *fact to confirm*, not something to match
  against evidence: a degree, a certification, work eligibility, travel, location, a bare "N years
  of experience".
- "5 years of SQL" is a requirement. The years are taken off before the line is read against
  evidence, and counted separately ([Knowledge 04](../knowledge/04-incomplete-information.md#years-are-counted-only-from-what-the-person-said)).

## 2. Matching evidence (embeddings + Jev)

1. **Stories, not fragments.** Fragments of the same work within a role are glued into stories
   ([K-06](../evidence/03-claim-index.md#k-06)).
2. **Three nominators per requirement**, top 8 each: the best single sentence by cosine, the whole
   story by cosine, and shared named terms. The union was chosen because one ranker alone missed
   evidence at measured depths ([M-27](../evidence/04-metric-ledger.md#m-27)).
3. **Jev reads each contender:**
   - the whole story first ("related?" below 0.3 is not relevant);
   - then the top five contenders sentence by sentence;
   - if the story establishes the requirement but no single sentence does, a passage of up to three
     sentences gets credit.

   The winner is **direct** (≥ 0.5) or **supporting**. A requirement that names a tool the story
   doesn't name is capped at supporting.
4. **Spread.** A story may win at most three requirements; past that, a close contender takes it.
   Alternates #2–#3 are kept.
5. **A story saved from a gap goes straight to the job** (since 2026-10-27). At Save, Jev reads it
   once for that requirement, as above. *Code* makes it the chosen story if it reads stronger (the
   old one becomes an alternate), else keeps it as an alternate. There is no new Chart My Course and
   no model call, and the assessment stays current when that is the only change. My words: "I want
   the evidence I updated from the gap to go straight to the job without having to do a new charted
   course ... a deterministic thing" (`3e1992d`; [A-81](../evidence/03-claim-index.md#a-81), [DEC-45](../product/07-decision-log.md#dec-45)).

## 3. The assessment: strong, light, missing, and "would a reader pass?"

| Verdict | Meaning |
|---|---|
| **Strong** | The chosen story is direct |
| **Light** | Chosen but supporting |
| **Missing** | Nothing chosen |
| **Fact to confirm** | Degree, years, location, eligibility: listed apart |

Jev answers per requirement:
- Is it *core*?
- Per reader seat: would a recruiter, or a hiring manager, pass on a candidate who doesn't show it?
- Is it *about the role* rather than something a candidate could show? Two fixed questions, asked
  once at Chart My Course and cached, so a page never pays for them.

These questions are asked about the requirement and the role only, never the evidence.

From those answers ([A-06](../evidence/03-claim-index.md#a-06)):
- **A gap** is a missing or light requirement a reader (a recruiter or hiring-manager persona) would
  likely pass on. Missing at ≥ 0.6 is a
  deal-breaker. A light requirement never is, because half of them (320 of 602) were written strong
  on the résumé ([M-15](../evidence/04-metric-ledger.md#m-15)).
- **"Could be stronger"** is everything else: optional, with a measured chance of being noticed
  ([M-14](../evidence/04-metric-ledger.md#m-14)).
- **Two kinds of line are never gaps.** A line both "about the role" readings call about the role
  leaves the gap queue. A fact to confirm, such as a degree, is never a gap, and since 2026-10-27 not
  on the résumé review either ([A-06](../evidence/03-claim-index.md#a-06)).
- **Related gaps count as one, on every page.** Since 2026-10-30 the opportunity page, the review
  page, the opportunities pane and the chat all count a theme as one gap, as the chat always did. A
  gap whose saved story still reads light stays open. The trigger was a page that said 4 gaps while
  the chat said 2, because two of the four were one theme ([A-78](../evidence/03-claim-index.md#a-78), [M-78](../evidence/04-metric-ledger.md#m-78)).
- **The odds are shown in words, not percentages.** "If you do the next k…", "If you stop now…".

**The model reviewers' actual reading overrides the estimate.** Once a résumé has been reviewed, what
a model reviewer who said
*no* found short and called material becomes a gap for that reader. The trigger was a job where the
estimate said a reader would approve and the review said the opposite. My response: "a real reading
should over ride, thats common sense right?" ([A-07](../evidence/03-claim-index.md#a-07)).

**Calibration and its limit.** The 0.6 threshold called the recruiter seat's decision right 84% of
the time (always-forward baseline 74%) and the hiring-manager seat's 79% (58%), on 19 reviewed
résumés ([M-13](../evidence/04-metric-ledger.md#m-13)). The "readers" are the app's model personas,
so this is consistency, not a hiring-outcome prediction ([D-19](../evidence/05-discrepancies.md#d-19)).

## 4. What the person sees and controls

- **Chart My Course** assesses and shows strong, light and missing, the gaps ranked by return on
  time and counted by theme, the optional items, and the facts to confirm.
- **Each opportunity card says where it stands** before applying: "Ready to apply" or "N gaps",
  counted by the page's own rule and kept ([A-79](../evidence/03-claim-index.md#a-79)).
- **Nothing writes a résumé until the person presses *Write the résumé*.** A written résumé can
  always be rewritten; the preparation re-reads changed evidence first
  ([A-37](../evidence/03-claim-index.md#a-37)).
- **Gaps lead into a conversation** ([Applications 02](02-gap-conversations.md)).

## Known defects

- **Two classifiers decide "fact or requirement" and disagree** on some phrasings. The eligibility
  pattern used for the reviewers also matches technical requirements: high availability, on-call
  response, export-control compliance programs. Those are then never reviewed
  ([D-11](../evidence/05-discrepancies.md#d-11)).
- **Jev outages degrade silently** to "unranked" or "no theme" in some places. Selection then relies
  on order alone. A failed division leaves lines whole, and a failed "about the role" reading leaves
  every line eligible as a gap; both are logged.
- **Counting gaps by theme can make paid embedding and Jev calls while a page renders**, and if the
  grouping fails the page counts by requirement without saying so ([D-35](../evidence/05-discrepancies.md#d-35)).
- **The second classifier now reaches the review page too.** Since 2026-10-27 it also decides which
  lines the résumé review counts as gaps ([D-11](../evidence/05-discrepancies.md#d-11)).

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Posting reading by rules; freeze and fingerprint | Verified | [A-01](../evidence/03-claim-index.md#a-01) |
| A sentence opening with "Or" stays with its requirement | Verified | [A-95](../evidence/03-claim-index.md#a-95) |
| Requirement sift (Jev) | Limited (one measurement) | [A-02](../evidence/03-claim-index.md#a-02) |
| Employer-language rewording | Limited | [A-03](../evidence/03-claim-index.md#a-03) |
| Assessment with one stated model exception (a line that lists several asks) | Verified (test checks the capability registry, not the call graph) | [A-05](../evidence/03-claim-index.md#a-05) |
| A gap's saved story goes straight to the job | Verified | [A-81](../evidence/03-claim-index.md#a-81) |
| Gap = a reader would pass; lines about the role never gaps | Limited (one account; model reviewers as reference) | [A-06](../evidence/03-claim-index.md#a-06) |
| A theme is one gap everywhere; a light save stays open | Verified | [A-78](../evidence/03-claim-index.md#a-78) |
| Opportunity labels: Ready to apply / N gaps | Verified | [A-79](../evidence/03-claim-index.md#a-79) |
| Real reading overrides the estimate | Verified | [A-07](../evidence/03-claim-index.md#a-07) |
| Nothing writes a résumé without the Write press | Verified | [A-37](../evidence/03-claim-index.md#a-37) |
| Eligibility never screened; degree as risk | Verified (pattern over-matches, D-11) | [A-04](../evidence/03-claim-index.md#a-04) |
