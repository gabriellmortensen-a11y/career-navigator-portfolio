# Case study 04 — Connecting job discovery to application execution

**One line:** I turned "find jobs, then do everything by hand" into one path:
1. search only from my own professions;
2. screen with evidence, not titles;
3. hold unreadable postings instead of guessing;
4. assess before writing;
5. pre-fill the application;
6. leave the submit button to the person.

**Audience notes.** *Product:* where automation stops and why. *Technical:* sources, screening,
de-duplication, the extension's limits. *TPM:* a funnel measured end to end, with its caveats.

---

## Customer problem and context

Applying well to many jobs takes a lot of small steps. You find openings across a dozen applicant
tracking systems (ATSs), work out which are real fits, tailor the résumé, answer the form's
questions, and keep track of where you are. Each step is either tedious or easy to get wrong:
- re-typing the same contact details;
- claiming a skill you can't back up;
- applying to a closed posting;
- losing track of which résumé went where.

Most tools automate the volume, with auto-apply and bulk submission. I wanted the opposite: **make
each good application cheap, and make no decision for me.**

## My ownership

- **I asked for the end-to-end path one stage at a time**, and used each on my own search before
  asking for the next.
- **I set the boundaries:**
  - search from my own record only ("stick to my evidence and professions");
  - never auto-submit;
  - never bypass a site's protections;
  - nothing writes a résumé until I press Write ("There should be a gate for review before doing
    it").
- **I found the defects that shaped the design by using it:**
  - title-only saves that blocked assessment;
  - search reach that missed whole employers;
  - kits that called Ashby jobs "closed";
  - rejections filed under the wrong status.

## Constraints

- **No credentials, no scraping around refusals, and robots.txt honored** wherever a page isn't an
  ATS public API.
- **Sensitive data stays out of searches.** Health and disability terms never leave the system in a
  query.
- **Cheap enough to run daily**: a few cents per run, with hard monthly caps on paid sources.
- **Nothing reads like a fit without evidence.** An opening whose posting couldn't be read is never
  recommended.

## Alternatives considered

| Option | Why not, or why |
|---|---|
| A job-board aggregator API | Costs, terms and staleness. The ATSs' own public APIs are free, current and verify the posting exists |
| Suggest roles from saved jobs | Drifted toward whatever I'd clicked. Replaced by roles from my own record in the last five years ([A-30](../evidence/03-claim-index.md#a-30)) |
| Use a language model to screen or explain fits | Screening is selection, so it belongs to Jev and code. No model writes explanations ([A-32](../evidence/03-claim-index.md#a-32)) |
| Save an unreadable posting by its title | Blocked assessment four times on Live. Replaced by **Save anyway** + Needs details + paste box ([A-36](../evidence/03-claim-index.md#a-36)) |
| Auto-apply | Rejected. The extension fills; the person submits ([A-39](../evidence/03-claim-index.md#a-39)) |
| Force Greenhouse's custom menus with trusted input | Rejected as bypassing site protections. The answer is shown beside the menu instead |
| A hosted career-site index for everyone | Pilot first, admin account only, own monthly cap ([A-31](../evidence/03-claim-index.md#a-31)) |

## Decision and reasoning

**Automate everything up to a decision, then stop.**

| Stage | Automated | Left to the person |
|---|---|---|
| Discover | Searching, verifying, de-duplicating, screening | Reviewing the profile; Save / Not interested |
| Assess | Reading the posting; strong / light / missing; gaps | Which gaps to work on |
| Write | Selecting stories, writing, fitting, reviewing | Pressing Write; editing |
| Apply | Reading the form; sorting questions by source; drafting experience answers; filling fields | Eligibility, pay, logistics, EEO answers; menus; **submitting** |
| Track | Counting activity from status history | Setting every status |

## Implementation

**Discover Jobs** ([Applications 04](../applications/04-discovery-to-application.md)):
- **Sources:** five ATS public APIs; robots-respecting employer `JobPosting` pages; a public
  large-employer feed; HN "Who is hiring?"; a domain-limited Tavily finder.
- **Screening:**
  1. embedding closeness ≥ 0.5, set from measured spreads (matching roles 0.57–0.70, software roles
     0.43–0.45);
  2. practical rules where only a *must* excludes;
  3. Jev on up to six requirement lines per readable posting.
- **De-duplication** by ids, requisitions and URLs, never merging two ATS ids. A posting is closed
  only when its ATS stops listing it.
- **Scheduled runs** auto-*assess* up to three lower-ranked fits for review, and never write.

**Apply kit and extension.** For Greenhouse forms, code decides each question's source. Experience
answers are drafted from Jev-chosen evidence in one call with an enforced shape. Unsupported
figures, promises and commitments only the person can make are flagged. Voluntary EEO questions are
never filled, remembered or sent ([A-38](../evidence/03-claim-index.md#a-38)). The extension pairs
by a confirmed code, fills what it can, outlines what it filled, and never submits.

**Tracking.** Every status change is an event, and undo is another event. "Rejected" is separate
from "Declined offer". An activity card counts from dated history only
([A-41](../evidence/03-claim-index.md#a-41)).

## Verification

- **106 discovery tests**, including:
  - `an unread search result is never recommended or assessed`;
  - `an opening far from the profile is screened out with why`;
  - `an Ashby job is said to be Ashby, never closed`.
- **Apply kit:** 21 tests, including `the extension never submits`.
- **Assess-first:** 21 tests, including `nothing writes a résumé without the Write press`.
- **Live telemetry**, read-only aggregates, 2026-10-25.

## Results

**Funnel** (my account, 18 runs, 2026-10-20 → 10-25) ([M-10](../evidence/04-metric-ledger.md#m-10)):

| Stage | Count |
|---|---:|
| Found (including repeats across runs) | 4,290 |
| Distinct openings stored | 297 |
| Assessed against my evidence | 92 |
| Recommended | 54 |
| Saved as opportunities (includes openings saved without being recommended) | 59 |
| **Total cost** | **$1.86** |

**Widening sources.** One run before the change found 578, kept 34 as close and read 8 against the
evidence. A later run found 338, kept 60 and read 30, recommending 21 for $0.048. **This is not
evidence that the new sources worked:** the same change raised the read cap from 8 to 30, "close" is
capped at 60, and "found" actually fell. Different days and queries, too ([M-11](../evidence/04-metric-ledger.md#m-11)).

**Career-site index pilot** (Beta, session record) ([M-12](../evidence/04-metric-ledger.md#m-12)):
- Two title-led searches returned 40 jobs, with **0 overlap** with the other sources, and 10 were
  recommended.
- **25 of the 40** were on systems the other sources can't read.
- Responsibility-led searches returned 1 and then 0 jobs, which is why the index runs title-led only.

**Throughput** ([M-08](../evidence/04-metric-ledger.md#m-08), [M-09](../evidence/04-metric-ledger.md#m-09)):
- The densest recorded 40-minute window holds **13** applications, and the busiest evening **16**.
- I had remembered "21 in about 40 minutes". The status history does not show it, so it stays as
  my own recollection, not a measurement.

## Limitations

- **Outcomes are not claimed.** Throughput is not success. Interviews and offers are not joined to
  anything the product did, and there is one user ([Product 05](../product/05-quality-and-measurement.md#what-is-not-measured)).
- **Kits read only Greenhouse forms.** Lever and Ashby get a résumé only. *Note, 2026-10-31: since
  2026-10-27 the person can add any form's questions by hand or in the application chat, which
  drafts answers with them; the kit still reads only Greenhouse forms ([A-40](../evidence/03-claim-index.md#a-40),
  [A-73](../evidence/03-claim-index.md#a-73)).*
- **The extension can't operate Greenhouse's searchable menus**, has only static tests, and its fill
  rate is unmeasured.
- **Discover's "Already applied" writes no status event**, so activity undercounts
  ([D-13](../evidence/05-discrepancies.md#d-13)).
- **The rejection stage isn't tracked**, and referrals aren't tracked
  ([A-42](../evidence/03-claim-index.md#a-42), [A-45](../evidence/03-claim-index.md#a-45)).
- **The "recommended" tier** uses thresholds set on one person's profiles.

## What changed after learning from use

1. **"Never guess" moved upstream.** Title-only saves broke assessment, so the save step began
   asking for the posting. Today an unreadable opening can be kept, but it is never treated as read.
2. **Reach was measured before it was widened.** The 578 → 34 → 8 run showed whole employers missing,
   because their jobs sit on systems the first three ATS APIs don't cover. The fix added sources that
   respect robots.txt, not a scraper.
3. **Assessment and writing were separated** after discovery and charting started writing résumés I
   hadn't asked for. Scheduled runs now assess only.
4. **Labels follow how the person thinks.** I filed employer rejections under "Declined", so the
   activity card counted none. The vocabulary changed; the counting rule didn't.
