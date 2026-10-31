# Roadmap

**Nothing on this page is built** unless it says "experimental", which means built but not on Live.
The current system is described in [Knowledge](knowledge/00-README.md), [Product](product/00-README.md)
and [Applications](applications/00-README.md). Every item links to the finding that motivates it.

*Updated for release 2026.10.1 (Live `00eac95`, 2026-10-31).*

## Now: defects found in review (fix at the source)

| Item | Why | Finding |
|---|---|---|
| Fix two open security and privacy findings (details withheld from this public version until fixed) | Found in this review | [D-02](evidence/05-discrepancies.md#d-02), [D-17](evidence/05-discrepancies.md#d-17) |
| Narrow the eligibility pattern, and make one classifier decide fact vs requirement | Technical requirements (high availability, on-call, export-control programs) are never reviewed | [D-11](evidence/05-discrepancies.md#d-11) |
| Have the interview walkthrough read the evidence Jev chose | It reads the cosine candidate pool | [D-12](evidence/05-discrepancies.md#d-12) |
| Make Discover's "Already applied" write a status event | The activity card undercounts | [D-13](evidence/05-discrepancies.md#d-13) |
| Make *Ask your record* narrow when the model omits fields | The fallback widens to "sufficient" | [D-15](evidence/05-discrepancies.md#d-15) |
| Stop the interview coach rewriting a draft because a check found an unsupported line | A check may report; it may not trigger a rewrite | [D-31](evidence/05-discrepancies.md#d-31) |
| Make a model assignment reach a database that already has the document | New stages ran on the default model on Live until set by hand | [D-27](evidence/05-discrepancies.md#d-27) |
| Run the evidence chat's figure check on application-chat offers | Offers skip it | [D-36](evidence/05-discrepancies.md#d-36) |
| Leave out flagged stories the way the résumé does when writing the career journey | It leaves out only the ones the person flagged | [D-37](evidence/05-discrepancies.md#d-37) |
| Count gaps by theme without a paid call at page render, and say when grouping failed | A failed grouping counts by requirement silently | [D-35](evidence/05-discrepancies.md#d-35) |
| Record which turn a statement for an opportunity came from | `turn_id` is never written | [D-34](evidence/05-discrepancies.md#d-34) |
| Update stale documents and comments (README pipeline, "Beta only" headers, test inventory, the résumé flow's and the coach's own descriptions, the chat-read coverage document) | Agents and readers act on them | [D-03](evidence/05-discrepancies.md#d-03), [D-04](evidence/05-discrepancies.md#d-04), [D-18](evidence/05-discrepancies.md#d-18), [D-25](evidence/05-discrepancies.md#d-25), [D-29](evidence/05-discrepancies.md#d-29), [D-32](evidence/05-discrepancies.md#d-32) |

## Next: measurement I need before changing the design again

| Item | Why |
|---|---|
| **Support report on Live résumé bullets** (assertion-level grounding as a report, not a gate) | **Partly shipped:** since 2026-10-28 each summary sentence is read by Jev against its stories and reported ([A-84](evidence/03-claim-index.md#a-84)). Bullets: nothing yet; their risk is assumed, not measured ([K-23](evidence/03-claim-index.md#k-23)) |
| **Writer first-pass quality vs editor fixes**, plus per-call seconds for writer, selector, reviewers and summary calls, and the time of an interview-coach turn | Required by the project rules; today only cost is separable ([P-17](evidence/03-claim-index.md#p-17), [D-21](evidence/05-discrepancies.md#d-21)) |
| **Join real outcomes to the assessment calibration** | Thresholds are calibrated against model personas, not hiring decisions ([D-19](evidence/05-discrepancies.md#d-19)) |
| **Rejection-stage tracking** | Requested; `from_status` already holds what's needed. Career Chat can now list each status change when asked, which is not stage tracking ([A-42](evidence/03-claim-index.md#a-42)) |
| **Run the model check on Live** | Routing still rests on one trial; none of the stages governed since 2026-10-25 can be replayed ([P-07](evidence/03-claim-index.md#p-07)) |
| **A human-labeled evaluation set for the current pipeline** | The earlier build's sealed holdout has no result, and the current pipeline has none. The application chat's evaluation is scored by a code rubric, not by people ([M-42](evidence/04-metric-ledger.md#m-42), [A-74](evidence/03-claim-index.md#a-74)) |
| **Measure Career Chat's read routing on Live** | Calibrated once on Beta; Jev is stubbed in every test ([A-104](evidence/03-claim-index.md#a-104)) |

## Later: product capabilities requested or designed, not built

| Item | Status | Note |
|---|---|---|
| Move story selection and the gap-panel judgment to Jev | Planned | Brings remaining model selections under the "Jev selects" rule. **Partly:** the professional summary's stories are classed by Jev first (2026-10-28); bullets and the gap panel are unchanged ([D-10](evidence/05-discrepancies.md#d-10)) |
| Pass the "which requirement this story shows" link to the writer without shrinking résumés | Open question | The first attempt cut bullets from 18–20 to 10–13 and was reverted ([M-18](evidence/04-metric-ledger.md#m-18)) |
| Restore retired evidence from the product | Planned | The contract describes it; no code path ([K-18](evidence/03-claim-index.md#k-18)) |
| Lineage edges written in production | Planned | Table and writer exist and are tested; unused ([K-08](evidence/03-claim-index.md#k-08)) |
| Read Lever and Ashby forms from the page the person has open | Planned | Their public APIs expose no form. Since 2026-10-27 the person can add a form's questions by hand or in the application chat, which is not form reading ([A-40](evidence/03-claim-index.md#a-40)) |
| Referral asks and outcomes | Planned | Not tracked today ([A-45](evidence/03-claim-index.md#a-45)) |
| Career breaks shorter than ten years | Planned | Not surfaced today ([K-29](evidence/03-claim-index.md#k-29)) |
| Evidence-tuning and dashboard requests beyond what shipped | Planned | The observability pages shipped. *Tune my evidence* shipped and was retired on 2026-10-30; its role readings live on Career Direction ([A-107](evidence/03-claim-index.md#a-107)). Further requests stay here until built |
| Private repositories in the GitHub portfolio, and proof that a connected GitHub account is the owner's (sign-in through a GitHub App) | Planned | Today only public repositories are read, by account name ([A-122](evidence/03-claim-index.md#a-122)) |
| Use the "Career Navigator, for my preparation" portfolio level | Planned | The level can be chosen and is stored, but nothing reads it ([A-122](evidence/03-claim-index.md#a-122), [D-30](evidence/05-discrepancies.md#d-30)) |
| Give Interview Prep's earlier preparation, quick answers and walkthrough a way back onto the page, or retire them | Candidate | Their links went with the card the coach replaced on 2026-10-25; the routes still answer ([D-39](evidence/05-discrepancies.md#d-39)) |
| Phone app release | **Experimental** | Capacitor shell on a branch; side-load first; iOS needs a Mac ([A-60](evidence/03-claim-index.md#a-60)). The website's own phone layout changed on Live on 2026-10-30 ([A-80](evidence/03-claim-index.md#a-80)) |
| Subheadings over long roles on a résumé | **Experimental** | Beta only; an opt-in box ([A-99](evidence/03-claim-index.md#a-99)) |
| Career themes, major outcomes and the evidence timeline | **Experimental** | Beta only; kept off Live by my decision ([A-100](evidence/03-claim-index.md#a-100), [DEC-50](product/07-decision-log.md#dec-50)) |
| Hosted career-site index for every account | Planned (today: admin-only, Limited) | Pending terms review and cost per relevant job at scale ([A-31](evidence/03-claim-index.md#a-31)) |
| A "résumé signal model" | Parked | Documented and deliberately not implemented |

## Considered and declined

| Idea | Why not |
|---|---|
| A live answer tool for video interviews | Consent: covert transcription of an interviewer; preparation is the better product |
| Auto-submitting applications | The person submits. The system never does |
| Forcing ATS menus with trusted input | Bypasses site protections |
| Per-item human approval of derived indexes | It defeats the purpose; the boundary is use as evidence ([H-18](evidence/03-claim-index.md#h-18)) |
| A more selective story picker | Fewer bullets, no reviewer gain ([M-18](evidence/04-metric-ledger.md#m-18)) |
| A "polish" step after tightening each bullet | Changed the meaning of 6 to 8 of 23 bullets and flagged none; closed the same day ([M-64](evidence/04-metric-ledger.md#m-64), [DEC-58](product/07-decision-log.md#dec-58)) |
| Completing a living-résumé answer's outcome from other pieces of the same work | Borderline readings for more time and tokens; outcomes are governed by policy instead ([M-80](evidence/04-metric-ledger.md#m-80), [DEC-73](product/07-decision-log.md#dec-73)) |
| Résumé writing-quality measurements on Live | They are for testing writing changes on Beta only ([A-98](evidence/03-claim-index.md#a-98), [DEC-62](product/07-decision-log.md#dec-62)) |
