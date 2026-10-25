# Applications 04 — From discovery to application

*Applications 4.0 · describes Live `7322289` (2026-10-24) · diagram: [Architecture 05](../architecture/05-discovery-to-tracking.md) · case study: [04](../case-studies/04-connecting-discovery-to-application.md)*

**The question this answers:** how does an opening get from "somewhere on the internet" to a
submitted application the person stands behind?

```text
Discover ─► screen ─► queue ─► Save ─► Chart My Course (assess) ─► gap chat ─► Write the résumé
   ─► apply kit ─► browser extension fills ─► person submits ─► Mark applied ─► status history
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
2. The person chats about the gaps ([Applications 02](02-gap-conversations.md)).
3. They press **Write the résumé** ([Applications 03](03-resume-planning-writing-review.md)).

I asked for this gate on 2026-10-22: "It should never write a resume when discovery and charting a
course goes. There should be a gate for review before doing it." ([A-37](../evidence/03-claim-index.md#a-37)).

## 3. Apply kit and browser extension

**Apply kit (Greenhouse forms)** ([A-38](../evidence/03-claim-index.md#a-38)). The kit reads the
form's questions from the public endpoint, and **code** decides each question's source:

| Source | Questions | Handling |
|---|---|---|
| Details | Name, contact, links | From the profile |
| File | Résumé | The written résumé's PDF |
| Draft | Experience questions, cover letter | Jev picks up to 4 pieces per question (a cover letter's against the posting's top critical requirements); one model call with an enforced shape. Unsupported figures, promises and commitments only the person can make are **flagged** |
| Yours | Work authorization, sponsorship, pay, relocation, start date, consent | Never drafted |
| Voluntary | Gender, race, veteran, disability | **Never filled, remembered or sent** |

**Lever and Ashby** get a résumé-only kit and are told so. Their public APIs expose no form, and one
job host disallows its form endpoint in robots.txt, so it is not used
([A-40](../evidence/03-claim-index.md#a-40)).

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
  ([A-41](../evidence/03-claim-index.md#a-41)).
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

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Discover: sources, profiles, screening, de-duplication, queues, schedules | Verified | [A-30](../evidence/03-claim-index.md#a-30)–[A-35](../evidence/03-claim-index.md#a-35) |
| Hosted career-site index | Limited (admin only; one Live run) | [A-31](../evidence/03-claim-index.md#a-31) |
| Unreadable postings held | Verified | [A-36](../evidence/03-claim-index.md#a-36) |
| Assess first; Write gate | Verified | [A-37](../evidence/03-claim-index.md#a-37) |
| Apply kit (Greenhouse) | Verified | [A-38](../evidence/03-claim-index.md#a-38) |
| Browser extension | Limited | [A-39](../evidence/03-claim-index.md#a-39) |
| Status history, activity card | Verified | [A-41](../evidence/03-claim-index.md#a-41) |
| Rejection-stage tracking | Planned (not started) | [A-42](../evidence/03-claim-index.md#a-42) |
| Connections import, "who you know there" | Verified | [A-43](../evidence/03-claim-index.md#a-43) |
| Connection message draft | Limited | [A-44](../evidence/03-claim-index.md#a-44) |
| Referral tracking | Planned (not started) | [A-45](../evidence/03-claim-index.md#a-45) |
