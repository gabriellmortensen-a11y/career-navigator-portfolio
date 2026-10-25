# Knowledge — what is true about the person

**Section version: Knowledge 3.0** (2026-10-25) · supersedes the Knowledge layer v2.2 ("CareerOS",
2026-07-08) · describes Live `7322289` (2026-10-24) · see [COMPATIBILITY](../COMPATIBILITY.md)

The Knowledge section answers: **what is true about a person's career, how does information become
part of the record, and how does the system avoid claiming more than the record shows?** It depends
on no other section. Product and Applications depend on it.

| # | Document | Answers |
|---|---|---|
| 01 | [The career evidence model](01-evidence-model.md) | Roles, sources, claims, stories; the role boundary; identity and canonical text |
| 02 | [Admission and acceptance](02-admission-and-acceptance.md) | Proposal vs record; the single writer; every way in; corrections, duplicates, flags |
| 03 | [Provenance and support](03-provenance-and-support.md) | Earlier conclusions vs facts; how support is controlled in writing; what checks do and don't do |
| 04 | [Incomplete information](04-incomplete-information.md) | Not-established states; years; gaps; career breaks; unreadable postings |

## The three rules this section stands on

1. **A model may propose; only a person may approve** ([Knowledge 02](02-admission-and-acceptance.md)).
2. **Evidence from two roles never composes into one claim**, and the database enforces it
   ([Knowledge 01](01-evidence-model.md)).
3. **Unknown is never "no", and nothing is invented to fill a gap**
   ([Knowledge 04](04-incomplete-information.md)).

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
