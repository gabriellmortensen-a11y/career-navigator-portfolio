# Glossary

Terms used across the portfolio, in plain language.

## The product

| Term | Meaning |
|---|---|
| **Career record** | Everything the person has approved about their career, organized by role |
| **Role** | One job: an employer plus a title, with dates. Every piece of evidence belongs to exactly one role |
| **Fragment / story / piece** | A *fragment* is one thing the person added. A *story* is fragments about the same piece of work, glued together within one role. A *piece* is one sentence of a story, used for search |
| **Claim / span** | A claim is one assertion stored as a *span*: an exact substring of the person's own text |
| **Proposal** | Anything not yet true: a chat suggestion, a parsed résumé, a draft. Only a person's press turns a proposal into evidence |
| **Change Document** | The single, contract-checked record through which evidence is added, composed or retired |
| **Flag** | A marker on a story that generalizes without an instance ("viewed problems as systems"). Flagged stories are not used on résumés; the person can flag or unflag |
| **Growth area** | Something the person says they haven't done. Kept on its own list; never evidence |
| **Growth action plan** | For one Growth item: an outcome that would get the person evidence of it, plus milestones. Suggested by Navi, decided by the person; never evidence |
| **Milestone** | One small step of a Growth plan, in order, with an optional date |
| **Requirement** (also *demand*) | One line of a job posting that asks for something |
| **Fact to confirm** | A requirement about the person's situation (degree, location, eligibility, bare years), not read against evidence |
| **Chart My Course** | The assessment of one job: each requirement marked *strong*, *light* or *missing*. No language model, with one stated exception: a line that lists several asks is read once for its asks |
| **Requirement division** | That exception: one small model call reads a long requirement line that lists several asks into separate asks, kept only if made of the line's own words |
| **Gap / optional** | A *gap* is a light or missing requirement a reader persona would likely pass on. Everything else short is *optional* ("could be stronger") |
| **Deal-breaker** | A missing requirement where Jev's "would pass" probability is at least 0.6 |
| **Theme** | Related gaps asked about as one conversation, and counted as one gap on every page; each requirement is still tracked on its own |
| **Pane label** | What an opportunity card says before applying: "Ready to apply" or "N gaps", counted by the page's own rule and kept |
| **Write the résumé** | The press that starts a résumé. Nothing writes one without it |
| **Selector / writer / editor** | The three language-model roles in writing résumé bullets. The selector picks stories by number against the requirements; the writer writes each bullet as its finished line from the picked stories only; the editor corrects wording through a code gate |
| **Positioning brief** | What the résumé summaries are written from: a planner reads the posting and the person's matched stories and writes the assertions a summary should make, each citing stories. The summary writers read the brief, never the posting |
| **Plain words** | Stories restated in plain language, ten at a time, for the summary planner and writers to read. Kept for reuse. Jev always reads the original stories |
| **Career journey** | One paragraph about the whole career and one per role, written by a model from the person's stories when none is saved; read by the résumé summaries. Derived text, never evidence |
| **Reviewer seats / personas** | Two model calls that read a finished résumé as a "recruiter" and a "hiring manager". They are model personas, **not people** |
| **Fix** | A person-pressed repair of one résumé line (or, on older résumés, a summary), checked by code and re-reviewed |
| **Red button** | The button shown where a résumé summary is missing; pressing it writes only that summary, and nothing is reviewed again |
| **`UNGROUNDED`** | The state every Live résumé bullet and summary is stored in: no code has checked its wording clause by clause against the evidence |
| **Quick add** | Saving a job posting by pasting it |
| **Apply kit** | For a Greenhouse application form: each question sorted by source (profile, résumé, drafted from evidence, the person's own answer, voluntary). For other forms the person adds the questions |
| **Application chat** | The chat for one opportunity's application. It answers the application's questions with the person, from claims Jev picks per part of a question, and offers what they tell for their record. *Use this answer* fills the kit field; nothing is submitted |
| **Interview coach** | The chat for one opportunity's interviews, leading Interview Prep. It reads the role first, plans what to prepare, drafts answers only from verified claims, and practices with the person |
| **Role reading** | A model's reading of a posting on its own, with nothing of the person's record: why the role exists, its problems and outcomes, hiring signals, what is unknown, and what an interview stage is likely to establish. A finding is "stated" only if code finds its quote in the posting |
| **Claim** (interview coach, application chat) | One sentence of the person's record that Jev read as showing what an answer must establish. The only facts a draft may state. Not the same as a *claim* in the career record |
| **Footnote** | The mark on every line of a coach draft that shows the exact words it rests on, their role, and whether Jev reads them as establishing the line |
| **Told work** | What the person tells the coach or the application chat about their own work. Used as their words in the answer, and offered for their record by code; saved only by their press |
| **Upcoming card** | A card on My Journey listing every date still ahead, soonest first: what the person adds, an opportunity's interview day, a recorded conversation's next step |
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
| **Navi** | The chat's name in the app since 2026-10-30: replies are labeled Navi, the person's messages You. Called the "evidence chat" in code and "Career Chat" in the read-layer work |
| **CN tab / chat rail** | The tab on the right of every page that opens Navi in a side rail (the whole screen on a phone), for the page you are on |
| **Page chat** | The chat the tab opens: an opportunity's own chat by stage (gaps, application, interview coach), Navi on Growth, or the general chat |
| **Read layer / read operation** | The read-only operations Career Chat uses to answer questions about the account. Jev chooses which ones a message needs; code runs them |
| **`RECORDS`** | The part of a chat call that holds what was read for this message, with code's counts and whose each record is |
| **Authority label** | Whose a record is (your record, the employer's words, a simulated reviewer's assessment, unverified research, …), said with every record the chat reads |
| **Living résumé** | A public link (formerly "Share my career conversation") where anyone can ask about the owner's career or paste a posting, answered only from what the owner chose to share |
| **Situational interpretation** | A living-résumé answer to "what would they do if…", built from comparable recorded decisions, labeled as an inference and never stored as evidence |
| **Pattern strength** | How well recorded decisions support an interpretation: strong, limited, mixed or none |
| **Portfolio artifact** | One section or release of a GitHub repository the owner approved, pinned to the commit read, served only if made public. It shows work; it is never evidence |
| **Portfolio link** | An owner-approved tie between an artifact and one piece of evidence; Jev may suggest it |
| **Sharing level** | What an approved repository is for: private to me, Career Navigator preparation (not yet used), or the living résumé (public) |

## Process and history

| Term | Meaning |
|---|---|
| **Beta / Live** | Two environments on the same host. Every change goes to Beta first. They ran the same code from 2026-10-21 to 10-27; since 2026-10-28 Live is its own line without three Beta-only features |
| **`live-approved`** | The branch Live deployed from until 2026-10-25: commits the product owner approved after using them on Beta |
| **Live branch** (`live-chat-reads`, `live-summaries`, `live-kept`) | Since 2026-10-28, the branch for one Live release, rebuilt from Beta's approved commits by cherry-pick |
| **Release gate** | The step between Beta and Live: the product owner uses the change, then approves it |
| **Earlier build ("beta4")** | The previous codebase (2026-08-06 → 10-02), described by the 2026-09-30 retrospective |
| **Extraction** | The 2026-10-03 rebuild into a clean application that migrated only what was understood |
| **QC-1** | An August 2026 quality investigation of the earlier build's canonicalization step |
| **Canonicalization / admission yield** (historical) | In the earlier build, turning raw evidence into standard career statements (*projections*). *Admission yield* is the share of proposed statements accepted |
| **Observatory** | A short-lived separate measurement tool (2026-08-13) that reproduced QC-1 |
| **Session record** | A measurement recorded in project notes during a working session, not in a commit or document. Always labeled |
