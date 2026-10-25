# Applications 01 — Job analysis and assessment

*Applications 4.0 · describes Live `7322289` (2026-10-24) · diagram: [Architecture 03](../architecture/03-requirement-analysis-and-matching.md)*

**The question this answers:** given a job posting, what does it actually ask for, how well does
the person's evidence show it, and which shortfalls matter?

The whole path from posting to assessment makes **no language-model call**. Rules read the posting,
Jev answers fixed questions, embeddings retrieve, and code decides
([A-05](../evidence/03-claim-index.md#a-05)).

## 1. Reading the posting (rules)

- **Every content line is a candidate.** It is labelled *ask*, *about*, *logistics* or *unclear*.
  Section headings corroborate a label but don't decide it. Nothing is dropped silently
  ([A-01](../evidence/03-claim-index.md#a-01)).
- **Lines are split only at whole sentences.** Lines that a fixed-width paste broke are rejoined.
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

These questions are asked about the requirement and the role only, never the evidence.

From those answers ([A-06](../evidence/03-claim-index.md#a-06)):
- **A gap** is a missing or light requirement a reader (a recruiter or hiring-manager persona) would
  likely pass on. Missing at ≥ 0.6 is a
  deal-breaker. A light requirement never is, because half of them (320 of 602) were written strong
  on the résumé ([M-15](../evidence/04-metric-ledger.md#m-15)).
- **"Could be stronger"** is everything else: optional, with a measured chance of being noticed
  ([M-14](../evidence/04-metric-ledger.md#m-14)).
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
  time, the optional items, and the facts to confirm.
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
  on order alone.

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Posting reading by rules; freeze and fingerprint | Verified | [A-01](../evidence/03-claim-index.md#a-01) |
| Requirement sift (Jev) | Limited (one measurement) | [A-02](../evidence/03-claim-index.md#a-02) |
| Employer-language rewording | Limited | [A-03](../evidence/03-claim-index.md#a-03) |
| Assessment with no language model | Verified (test checks the capability registry, not the call graph) | [A-05](../evidence/03-claim-index.md#a-05) |
| Gap = a reader would pass | Limited (one account; model reviewers as reference) | [A-06](../evidence/03-claim-index.md#a-06) |
| Real reading overrides the estimate | Verified | [A-07](../evidence/03-claim-index.md#a-07) |
| Eligibility never screened; degree as risk | Verified (pattern over-matches, D-11) | [A-04](../evidence/03-claim-index.md#a-04) |
