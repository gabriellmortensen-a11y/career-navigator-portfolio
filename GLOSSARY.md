# Glossary

Terms used across the portfolio, in plain language.

## The product

| Term | Meaning |
|---|---|
| **Career record** | Everything the person has approved about their career, organised by role |
| **Role** | One job: an employer plus a title, with dates. Every piece of evidence belongs to exactly one role |
| **Fragment / story / piece** | A *fragment* is one thing the person added. A *story* is fragments about the same piece of work, glued together within one role. A *piece* is one sentence of a story, used for search |
| **Claim / span** | A claim is one assertion stored as a *span*: an exact substring of the person's own text |
| **Proposal** | Anything not yet true: a chat suggestion, a parsed résumé, a draft. Only a person's press turns a proposal into evidence |
| **Change Document** | The single, contract-checked record through which evidence is added, composed or retired |
| **Flag** | A marker on a story that generalises without an instance ("viewed problems as systems"). Flagged stories are not used on résumés; the person can flag or unflag |
| **Growth area** | Something the person says they haven't done. Kept on its own list; never evidence |
| **Requirement** (also *demand*) | One line of a job posting that asks for something |
| **Fact to confirm** | A requirement about the person's situation (degree, location, eligibility, bare years), not read against evidence |
| **Chart My Course** | The assessment of one job: each requirement marked *strong*, *light* or *missing*. No language model |
| **Gap / optional** | A *gap* is a light or missing requirement a reader persona would likely pass on. Everything else short is *optional* ("could be stronger") |
| **Deal-breaker** | A missing requirement where Jev's "would pass" probability is at least 0.6 |
| **Theme** | Related gaps asked about as one conversation, each requirement still tracked on its own |
| **Write the résumé** | The press that starts a résumé. Nothing writes one without it |
| **Selector / writer / editor** | The three language-model roles in résumé writing. The selector picks stories by number against the requirements; the writer writes from the picked stories only; the editor corrects wording through a code gate |
| **Reviewer seats / personas** | Two model calls that read a finished résumé as a "recruiter" and a "hiring manager". They are model personas, **not people** |
| **Fix** | A person-pressed repair of one résumé line or summary, checked by code and re-reviewed |
| **`UNGROUNDED`** | The state every Live résumé bullet is stored in: no code has checked its wording clause by clause against the evidence |
| **Quick add** | Saving a job posting by pasting it |
| **Apply kit** | For a Greenhouse application form: each question sorted by source (profile, résumé, drafted from evidence, the person's own answer, voluntary) |
| **ATS** | Applicant-tracking system (Greenhouse, Lever, Ashby, Workday…), where employers post jobs and receive applications |

## The machinery

| Term | Meaning |
|---|---|
| **Jev** | A hosted probability model (TypeSafe's Jev). It is asked fixed, typed yes/no questions ("does this sentence establish this requirement?") and returns a probability. Thresholds live in code. Priced per input token |
| **Language model** | gpt-5-mini, Claude Haiku, or gpt-5 for measurement. Used to write and reason |
| **Embedding similarity** (cosine) | A numeric closeness between two texts, used to shortlist candidates before Jev or a person decides |
| **Depth** (retrieval) | How far down a ranked list you must read to keep every piece in a reference set |
| **Governed stage / policy document** | Every model call runs under a named stage with a versioned prompt document; changing it creates a new version |
| **Model assignments** | The governed document that says which model each task calls, and why |
| **Grounding** (clause-level / assertion-level) | Checking written text against the evidence. *Assertion-level* splits a sentence into assertions and checks each. Used for measurement, not on Live résumés |
| **Noise floor / null model** | How much a measurement moves when nothing changed. A difference smaller than that is not an improvement |
| **Constitutional gates** | Pass/fail rules (no invented figures, no cross-role claims) checked before any quality comparison |
| **Row-level security (RLS)** / **tenancy** | The database itself filters every row to the signed-in account, so one person's data can't be read or written by another |
| **Contract tests** | Tests that pin a rule (a boundary, a "no model here") rather than a feature |
| **Clean-room test** | A test that boots the application with the earlier codebase made unimportable |
| **MCP** | Model Context Protocol, which ChatGPT uses to read the person's record through read-only tools |

## Process and history

| Term | Meaning |
|---|---|
| **Beta / Live** | Two environments on the same host and code. Every change goes to Beta first |
| **`live-approved`** | The branch Live deploys from: commits the product owner approved after using them on Beta |
| **Release gate** | The step between Beta and Live: the product owner uses the change, then approves it |
| **Earlier build ("beta4")** | The previous codebase (2026-08-06 → 10-02), described by the 2026-09-30 retrospective |
| **Extraction** | The 2026-10-03 rebuild into a clean application that migrated only what was understood |
| **QC-1** | An August 2026 quality investigation of the earlier build's canonicalization step |
| **Canonicalization / admission yield** (historical) | In the earlier build, turning raw evidence into standard career statements (*projections*). *Admission yield* is the share of proposed statements accepted |
| **Observatory** | A short-lived separate measurement tool (2026-08-13) that reproduced QC-1 |
| **Session record** | A measurement recorded in project notes during a working session, not in a commit or document. Always labelled |
