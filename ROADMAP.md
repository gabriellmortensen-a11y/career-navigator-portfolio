# Roadmap

**Nothing on this page is built** unless it says "experimental", which means built but not on Live.
The current system is described in [Knowledge](knowledge/00-README.md), [Product](product/00-README.md)
and [Applications](applications/00-README.md). Every item links to the finding that motivates it.

## Now: defects found in this review (fix at the source)

| Item | Why | Finding |
|---|---|---|
| Fix two open security and privacy findings (details withheld from this public version until fixed) | Found in this review | [D-02](evidence/05-discrepancies.md#d-02), [D-17](evidence/05-discrepancies.md#d-17) |
| Narrow the eligibility pattern, and make one classifier decide fact vs requirement | Technical requirements (high availability, on-call, export-control programs) are never reviewed | [D-11](evidence/05-discrepancies.md#d-11) |
| Have the interview walkthrough read the evidence Jev chose | It reads the cosine candidate pool | [D-12](evidence/05-discrepancies.md#d-12) |
| Make Discover's "Already applied" write a status event | The activity card undercounts | [D-13](evidence/05-discrepancies.md#d-13) |

| Make *Ask your record* narrow when the model omits fields | The fallback widens to "sufficient" | [D-15](evidence/05-discrepancies.md#d-15) |
| Update stale documents and comments (README pipeline, "Beta only" headers, test inventory) | Agents and readers act on them | [D-03](evidence/05-discrepancies.md#d-03), [D-04](evidence/05-discrepancies.md#d-04), [D-18](evidence/05-discrepancies.md#d-18) |

## Next: measurement I need before changing the design again

| Item | Why |
|---|---|
| **Support report on Live résumés** (assertion-level grounding as a report, not a gate) | The residual risk on Live text is currently assumed, not measured ([K-23](evidence/03-claim-index.md#k-23)) |
| **Writer first-pass quality vs editor fixes**, plus per-call seconds for writer, selector and reviewers | Required by the project rules; today only cost is separable ([P-17](evidence/03-claim-index.md#p-17), [D-21](evidence/05-discrepancies.md#d-21)) |
| **Join real outcomes to the assessment calibration** | Thresholds are calibrated against model personas, not hiring decisions ([D-19](evidence/05-discrepancies.md#d-19)) |
| **Rejection-stage tracking** | Requested; `from_status` already holds what's needed ([A-42](evidence/03-claim-index.md#a-42)) |
| **Run the model check on Live** | Routing still rests on one trial ([P-07](evidence/03-claim-index.md#p-07)) |
| **A human-labelled evaluation set for the current pipeline** | The earlier build's sealed holdout has no result, and the current pipeline has none ([M-42](evidence/04-metric-ledger.md#m-42)) |

## Later: product capabilities requested or designed, not built

| Item | Status | Note |
|---|---|---|
| Move story selection and the gap-panel judgement to Jev | Planned | Brings two remaining model selections under the "Jev selects" rule ([D-10](evidence/05-discrepancies.md#d-10)) |
| Pass the "which requirement this story shows" link to the writer without shrinking résumés | Open question | The first attempt cut bullets from 18–20 to 10–13 and was reverted ([M-18](evidence/04-metric-ledger.md#m-18)) |
| Restore retired evidence from the product | Planned | The contract describes it; no code path ([K-18](evidence/03-claim-index.md#k-18)) |
| Lineage edges written in production | Planned | Table and writer exist and are tested; unused ([K-08](evidence/03-claim-index.md#k-08)) |
| Read Lever and Ashby forms from the page the person has open | Planned | Their public APIs expose no form ([A-40](evidence/03-claim-index.md#a-40)) |
| Referral asks and outcomes | Planned | Not tracked today ([A-45](evidence/03-claim-index.md#a-45)) |
| Career breaks shorter than ten years | Planned | Not surfaced today ([K-29](evidence/03-claim-index.md#k-29)) |
| Evidence-tuning and dashboard requests beyond what shipped | Planned | Tune my evidence and the observability pages shipped; further requests stay here until built |
| Phone app release | **Experimental** | Capacitor shell on a branch; side-load first; iOS needs a Mac ([A-60](evidence/03-claim-index.md#a-60)) |
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
