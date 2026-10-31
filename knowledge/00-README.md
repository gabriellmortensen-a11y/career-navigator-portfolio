# Knowledge — what is true about the person

**Section version: Knowledge 3.1** (2026-10-31) · supersedes Knowledge 3.0 (2026-10-25) and the
Knowledge layer v2.2 ("CareerOS", 2026-07-08) · describes Live `00eac95` (2026-10-31) · see
[COMPATIBILITY](../COMPATIBILITY.md)

The Knowledge section answers: **what is true about a person's career, how does information become
part of the record, and how does the system avoid claiming more than the record shows?** It depends
on no other section. Product and Applications depend on it.

| # | Document | Answers |
|---|---|---|
| 01 | [The career evidence model](01-evidence-model.md) | Roles, sources, claims, stories; the role boundary; identity and canonical text; what sits beside the record and is never evidence |
| 02 | [Admission and acceptance](02-admission-and-acceptance.md) | Proposal vs record; the single writer; every way in, including what code offers from a conversation; corrections, duplicates, flags |
| 03 | [Provenance and support](03-provenance-and-support.md) | Earlier conclusions vs facts; whose each record is; stated vs inferred; how support is controlled in writing; what checks do and don't do |
| 04 | [Incomplete information](04-incomplete-information.md) | Not-established states; years; gaps; career breaks; unreadable postings; silence on a shared record |

## The three rules this section stands on

1. **A model may propose; only a person may approve** ([Knowledge 02](02-admission-and-acceptance.md)).
2. **Evidence from two roles never composes into one claim**, and the database enforces it
   ([Knowledge 01](01-evidence-model.md)).
3. **Unknown is never "no", and nothing is invented to fill a gap**
   ([Knowledge 04](04-incomplete-information.md)).

## What changed since Knowledge 3.0

Knowledge 3.1 adds content and changes no rule. The unit of evidence, the single writer, the role
boundary and the three rules above are as they were in 3.0. What is new is more ways a conversation
can *offer* a change, more things kept beside the record that are never evidence, and labels on
what the chat reads.

| 3.0 (2026-10-25) | 3.1 (2026-10-31) |
|---|---|
| The evidence chat proposed additions, corrections and retirements | The interview coach and the application chat also offer the person's own words, by code, as an addition to their record or to the piece an answer rests on. A line the person says is wrong becomes a correction to that exact text. Every one still goes through their Save and the Change Document ([Knowledge 02](02-admission-and-acceptance.md#every-way-in)) |
| Growth areas were the one list kept apart from evidence | Also kept apart: Growth action plans, the person's words for one opportunity, living-résumé interpretations, GitHub portfolio artifacts, and what Career Chat reads ([Knowledge 01](01-evidence-model.md#what-sits-beside-the-record-and-is-never-evidence)) |
| Earlier conclusions carried a label in nine coaching policies | Every record the chat reads also says whose it is: the person's record, the employer's words, an estimate, a simulated reviewer, unverified research ([Knowledge 03](03-provenance-and-support.md#every-record-the-chat-reads-says-whose-it-is)) |
| No Live résumé text was read against the evidence | Bullets still are not. Since 2026-10-28 each summary sentence is read by Jev against the stories it cites, and the result is reported ([Knowledge 03](03-provenance-and-support.md#how-support-is-handled-in-résumé-writing)) |
| Flagged stories were left out of résumé bullets and shared links | Also left out of the stories résumé summaries are written from ([K-17](../evidence/03-claim-index.md#k-17)) |
| *Tune my evidence* counted years its own way | That page was retired on 2026-10-30. Career Direction's role pages keep its reading, and its years rule ([Knowledge 04](04-incomplete-information.md#years-are-counted-only-from-what-the-person-said)) |

## What changed since Knowledge 2.2

| 2.2 (2026-07-08) | 3.0 (2026-10-25) |
|---|---|
| Hand-maintained Markdown libraries for one person, in git | A multi-tenant PostgreSQL record with row-level security |
| "Verified evidence" meant a person edited and committed a file | A Change Document with a deterministic contract, applied by a person's press |
| Libraries by topic (projects, metrics, stories, bullets) | Roles → sources → verbatim claims → stories; topic views are derived, not stored |
| Principle: "Every generated artifact must remain interview-defensible and traceable to verified evidence" | **Same principle.** Each bullet now names its story by schema, and the database refuses a cross-role citation |
| Major / minor / patch versioning of libraries | Per-row provenance, versioned contracts and governed policy documents |

The 2.2 libraries' contents are private career records and are **not** reproduced in this portfolio.
Only their structure and purpose are described.
