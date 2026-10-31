# Knowledge 01 — The career evidence model

*Knowledge 3.1 · describes Live `00eac95` (2026-10-31) · statuses as defined in [COMPATIBILITY](../COMPATIBILITY.md#status-vocabulary)*

**The question this answers:** what is true about a person's career, and in what unit is it held?

## The unit is a role, and a role owns its evidence

A career record is a chronology of **roles**: an employer plus a title, with dates. Every piece of
evidence belongs to exactly one role.

| Object | What it holds | Why it exists |
|---|---|---|
| **Role** | Employer + title, normalized into one key per account | The chronology is the one thing a generated document may never author |
| **Source** | The person's own text, with a locator that is never rewritten | The provenance anchor every claim points back to |
| **Claim** | One assertion, stored as a *verbatim span* of its source | A claim can always be shown in the person's words |
| **Event (story)** | Claims composed into one occurrence, with the reason they belong together | The unit that résumés, interviews and assessments read |
| **Piece** | A whole sentence of a story, derived by rule for retrieval | What search and Jev read; not stored as its own record |

The rule that matters most: **evidence from two roles may relate, share concepts and answer the
same requirement, but it may never land in one row.** PostgreSQL enforces this. Composite foreign
keys tie an event, its claims and the link between them to a single role, so the database refuses a
mixed-role event ([K-01](../evidence/03-claim-index.md#k-01)). Since 2026-10-07 the same rule covers
résumé output. A bullet printed under one job cannot cite another job's evidence
([K-02](../evidence/03-claim-index.md#k-02)).

### Why the boundary is in the schema, not in a prompt

In September 2026 the previous build ("Job Fit") could establish a requirement by combining
evidence from two or three unrelated roles. Each combined claim was true in parts, but none was true
of any single piece of work. The product owner's diagnosis was that the system was *manufacturing*
evidence. The fix was to force answers to come from one coherent body of work: "Bounded Fit", which
"became the product through use" ([H-07](../evidence/03-claim-index.md#h-07)).

When the system was extracted into a clean application on 2026-10-03, that lesson stopped being a
retrieval preference. It became a schema constraint, so no future stage, prompt or agent change
could reintroduce it ([K-01](../evidence/03-claim-index.md#k-01)).

## Identity and canonical text

- **One key per role.** The key is `role:employer|title`, with case and whitespace normalized and
  nothing else. "A title differing by a word is a different role until the authoritative record says
  otherwise." The key is unique per account ([K-03](../evidence/03-claim-index.md#k-03)).
- **One locator per source.** Two pieces of evidence may not share a locator. Claim and event keys
  derive from it, so every claim walks back to the text it came from
  ([K-03](../evidence/03-claim-index.md#k-03)).
- **A canonical evidence document per story.** It is rendered deterministically: each claim span is
  located in its source, overlapping intervals are merged, and each is rendered once. No
  summarizing, paraphrasing or semantic deduplication happens. The text is hashed, and a corpus
  fingerprint lets later stages detect that the record changed underneath them
  ([K-04](../evidence/03-claim-index.md#k-04)).
- **Retirement, not deletion.** Retired evidence is a tombstone with a reason and, for a correction,
  the replacing story. One function defines "eligible": not retired
  ([K-05](../evidence/03-claim-index.md#k-05)).

## Stories: fragments glued within one role

People add their career in fragments: a résumé line here, a chat answer there. Since 2026-10-13,
fragments within one role that describe the same piece of work are composed into one **story**.

The composition rule:
1. Embeddings shortlist the candidate pairs.
2. Jev, a probability model that answers typed questions, decides "same work?".
3. Exact or contained copies are joined without asking.

The story is assembled from the fragments' own words; the replaced fragments are retired with the
reason ([K-06](../evidence/03-claim-index.md#k-06)).

Story composition explains a visible number change. When fragments were first glued (2026-10-13),
one account's count went from 176 "evidence pieces" to 86. Nothing was lost; merged stories count once.
The product now says "examples from your experience" ([M-52](../evidence/04-metric-ledger.md#m-52)).

**Limits, stated:**
- Gluing runs automatically. It adds no new claims and is reversible, but no person confirms it.
- There is no direct test of the compose operation itself, only of its helpers.
- An attempt to split already-glued stories was measured and **rejected**. Across 63 jobs ([M-53](../evidence/04-metric-ledger.md#m-53)), splitting
  turned 20 strong requirements light and strengthened 3
  ([K-07](../evidence/03-claim-index.md#k-07)).

## What sits beside the record and is never evidence

The product now keeps several kinds of text about a person that are not career evidence. Each has
its own table, none is written through a Change Document, and none can establish a requirement. The
only way any of it reaches the record is the person telling it to the chat and pressing Save
([Knowledge 02](02-admission-and-acceptance.md#every-way-in)).

| Kept | What it is | Why it is not evidence | Claim |
|---|---|---|---|
| **Growth areas and Growth action plans** | A limit the person stated, and for each one an outcome that would get them evidence, with milestones | A plan is work not yet done. The plan call is never shown the record's text, and nothing that writes a résumé, an application or outreach reads a plan | [K-28](../evidence/03-claim-index.md#k-28), [K-33](../evidence/03-claim-index.md#k-33) |
| **Their words for one opportunity** | Their reason for wanting it, practice answers, and work told to the interview coach, kept with that opportunity | Said for one opportunity and read again only by its preparations and as their stated reasons in application answers. The row does not record the turn it came from ([D-34](../evidence/05-discrepancies.md#d-34)) | [A-70](../evidence/03-claim-index.md#a-70) |
| **An interview's account** | What happened in an interview, saved from a card as the opportunity's conversation | A record of a conversation, not of work | [A-67](../evidence/03-claim-index.md#a-67) |
| **A role reading** | A posting read on its own: the role's purpose, problems and hiring signals | It is about the employer | [A-62](../evidence/03-claim-index.md#a-62) |
| **The career journey and plain words** | A model's summary of the whole career and of each role, and stories restated in plain words, both read by the résumé summaries | Derived text. Jev reads the original stories, never the restatements | [A-86](../evidence/03-claim-index.md#a-86), [A-87](../evidence/03-claim-index.md#a-87) |
| **A situational interpretation** | A living-résumé answer to "what would they do if…", built from comparable recorded decisions | An inference, labeled as one, never in the owner's voice and never written to the record | [A-114](../evidence/03-claim-index.md#a-114) |
| **A GitHub portfolio artifact** | A section or release of a public repository the owner approved | A separate authority: it shows or supports work. The policy says "a repository or its code is not professional experience". It is tied to a piece of evidence only by a link the owner approves | [K-34](../evidence/03-claim-index.md#k-34) |
| **What Career Chat reads** | Records read from the account to answer one message | Reading creates nothing. A posting reaches the chat only inside that read, labeled as the employer's words | [K-31](../evidence/03-claim-index.md#k-31), [A-102](../evidence/03-claim-index.md#a-102) |

## What is legacy

The generation-one corpus imported on 2026-10-03 carries `Body` and `Atom` rows. New evidence writes
neither. The README's chain "source → body → exactly one authoritative role" describes that legacy
data, not the current write path ([D-03](../evidence/05-discrepancies.md#d-03)).

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Role boundary enforced by composite foreign keys | Verified | [K-01](../evidence/03-claim-index.md#k-01) |
| Résumé bullets cannot cite another role's evidence | Verified | [K-02](../evidence/03-claim-index.md#k-02) |
| Per-account canonical identity (role key, locator) | Verified | [K-03](../evidence/03-claim-index.md#k-03) |
| Deterministic canonical evidence document, hashed | Verified | [K-04](../evidence/03-claim-index.md#k-04) |
| Retire, never delete | Verified | [K-05](../evidence/03-claim-index.md#k-05) |
| Story composition by Jev within one role | Limited (no direct test of compose) | [K-06](../evidence/03-claim-index.md#k-06) |
| Generic artifact-lineage table | Planned (built and tested, but no production writer) | [K-08](../evidence/03-claim-index.md#k-08) |
| Growth areas kept apart from evidence | Limited (the boundary test is a text scan) | [K-28](../evidence/03-claim-index.md#k-28) |
| Growth plans and milestones never evidence | Limited (the boundary test names the Growth list's table, which holds the plans, not the milestones' table or the plan modules) | [K-33](../evidence/03-claim-index.md#k-33) |
| Their words for one opportunity, never career evidence | Verified (the turn it came from is not recorded, D-34) | [A-70](../evidence/03-claim-index.md#a-70) |
| An interview's account kept as the opportunity's conversation | Verified | [A-67](../evidence/03-claim-index.md#a-67) |
| Role read from the posting alone | Verified | [A-62](../evidence/03-claim-index.md#a-62) |
| Career journey written when none is saved | Limited | [A-86](../evidence/03-claim-index.md#a-86) |
| Plain words, kept for reuse; Jev reads the originals | Verified | [A-87](../evidence/03-claim-index.md#a-87) |
| Situational questions as labeled interpretations | Verified | [A-114](../evidence/03-claim-index.md#a-114) |
| Portfolio artifacts never evidence | Verified | [K-34](../evidence/03-claim-index.md#k-34) |
| A posting reaches the chat only inside what was read | Limited (no test of a proposal on a turn that read a posting) | [K-31](../evidence/03-claim-index.md#k-31) |
| Career Chat read layer | Verified | [A-102](../evidence/03-claim-index.md#a-102) |

## What changed since Knowledge 2.2

Knowledge 2.2 (2026-07-08) was **CareerOS**: a set of hand-maintained Markdown libraries for one
person, in git, at versions 2.0 to 2.3. They covered profile, timeline, project write-ups, metrics,
leadership, interview stories, résumé bullets, application history and narrative. Approval meant
editing a file and committing it.

Knowledge 3.0 describes a multi-tenant database record:
- the role boundary is enforced in the schema;
- provenance is carried on every row;
- every change goes through one governed writer ([Knowledge 02](02-admission-and-acceptance.md));
- row-level security separates accounts ([Product 06](../product/06-operations-and-privacy.md)).

The libraries' **principle** survives intact: "Every generated artifact must remain
interview-defensible and traceable to verified evidence." Their **contents** are private and are
not reproduced in this portfolio.
