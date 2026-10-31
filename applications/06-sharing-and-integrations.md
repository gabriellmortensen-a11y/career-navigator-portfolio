# Applications 06 — Sharing, integrations and other journeys

*Applications 5.0 · describes Live `00eac95` (2026-10-31)*

**The question this answers:** where else does the career record go, and what keeps it inside the
scope the person chose?

<a id="share-my-career-conversation"></a>

## The living résumé

A public link where anyone can ask about the owner's career, or paste a job posting, and get
answers only from what the owner chose to share ([A-55](../evidence/03-claim-index.md#a-55)). Until
2026-10-31 it was called **Share my career conversation**. The owner makes links with *Share my
living résumé*, on Evidence and on **Settings › Sharing** ([A-105](../evidence/03-claim-index.md#a-105)).

**Owner:** "I want the share a link to be called living resume instead" (`4555460`,
[DEC-70](../product/07-decision-log.md#dec-70)).

**Scope and lifecycle:**
- **Draft until activated.** A link answers nobody until the owner activates it. It can be revoked.
- **The owner chooses the scope:** which roles, which stated limits (ticked one by one), facts for
  visitors, an optional role focus, live or snapshot mode, and an expiry of 7, 30 or 90 days or
  never.
- **Every link also shares the profile's education and certifications:** what, where from and when,
  never a credential's number or note. There is no per-link choice
  ([A-118](../evidence/03-claim-index.md#a-118)).
- **Portfolio sections the owner made public** may be shown beside an answer, cited apart from the
  record ([below](#the-work-behind-an-answer-a-github-portfolio)).
- **The token is stored as a digest.**
- **Scope is computed on the server before retrieval.** Retired and flagged pieces are excluded. In
  snapshot mode, pieces changed since capture are left out. The scope's digest covers the pieces,
  the limits, the education lines and what of the portfolio may be served, so an answer given under
  another scope is never replayed.

**What a visitor sees.** A page titled "\<name>'s living résumé". Code writes the opening message
from what the link shares. It ends: "You can also paste a job posting on its own, and I'll tell you
where my experience fits the role." A posting can be sent without a message; the thread shows "Sent
a job posting" ([A-112](../evidence/03-claim-index.md#a-112)).

**A visitor's turn:**

| Step | Who | What |
|---|---|---|
| 1. Caps | Code | A per-link spend cap, messages per minute per address, and turns per visitor, all before the call |
| 2. Scope | Code | As above, read as the owner |
| 3. Retrieval | Embeddings, within the scope | With a posting: the message and the posting, 12 nearest pieces. Otherwise the message (and the one before), 6. A follow-up to an interpretation carries the decisions it rested on |
| 4. Portfolio | Code | Up to three artifacts ([below](#the-work-behind-an-answer-a-github-portfolio)) |
| 5. Answer | **One model call** (`career_conversation`, Claude Haiku) | The shape is held by the API and fixed in order: the question's kind, the pattern, the basis, the citations, the artifacts and how to refer to the owner come **before** the reply. Visitor text, the posting and repository text are labeled untrusted |
| 6. Lay out | Code | A posting's answer is laid out as a résumé ([below](#a-postings-answer)) |
| 7. Narrow | Code | A claim without a surviving citation becomes "not established"; so does an interpretation. Artifact numbers the call wasn't sent are dropped |
| 8. Label | Code | "Based on my record (n)", or the interpretation's label. Citations are resolved against the scope as it is when the page is shown |

### Question kinds

| Kind | How it is answered | Enforced by |
|---|---|---|
| **Recorded** | In the owner's voice, cited; an outcome is told with the work that produced it | Citation check by code; outcomes by policy |
| **Posting** (alone, or "how would I fit this role?") | A résumé laid out by code, strengths only | Layout by code ([A-112](../evidence/03-claim-index.md#a-112)); strengths only by policy and the shape ([A-113](../evidence/03-claim-index.md#a-113)) |
| **Situational** ("what would they do if …") | A labeled interpretation of comparable recorded decisions, never in the owner's voice | Label and storage by code ([A-114](../evidence/03-claim-index.md#a-114)); the voice by policy |
| **Personal** | Only from what the owner explicitly said | Policy ([A-115](../evidence/03-claim-index.md#a-115)) |
| **Prediction** (offers, relocation, pay, firing, one exact design) | Declined as the owner's own decision | Policy ([A-115](../evidence/03-claim-index.md#a-115)) |

**Something not on the shared record** is said only when asked: "That isn't on my shared record,
which doesn't mean I have no experience with it. That's something to ask me directly." Only a
stated limit may say the owner hasn't done something ([A-113](../evidence/03-claim-index.md#a-113)).

### A posting's answer

Code lays out the answer like a résumé written for the posting
([A-112](../evidence/03-claim-index.md#a-112), [DEC-70](../product/07-decision-log.md#dec-70)):
1. An executive summary in the owner's voice.
2. Each matching role, most recent first, with **the record's** title, employer and dates, never
   the model's. Under each: one line and the cited bullets (the policy asks for two to five).
3. Relevant education and certifications, by number from the profile.

Evidence numbers appear only in the citations. A bullet that a public portfolio artifact shows ends,
by code, "(shown in the portfolio: \<artifact title>)" ([A-121](../evidence/03-claim-index.md#a-121)).

**Strengths only.** No gap, weakness, missing requirement or stated limit appears anywhere, the
summary included. This rests on the policy and on the shape's field descriptions, not on code
([A-113](../evidence/03-claim-index.md#a-113), Limited). On Live on 2026-10-31 a summary closed on
an unasked gap. The summary's own field now says strengths only (`00d91f1`). Nothing measures the
rate since.

**Owner:** "Dont call out weaknesses only that the evidence doesnt cover an area if the user asks"
(`4555460`), and "… dont state gaps voluntarily. Only if asked and state its not on tge record but
doesnt mean that means no experience and to ask the data owner directly." (`7f23b63`)

### Situational questions: labeled interpretations

([A-114](../evidence/03-claim-index.md#a-114), [DEC-71](../product/07-decision-log.md#dec-71))
- **Not in the owner's voice (policy).** "Based on \<first name>'s recorded decisions, they would likely …",
  with the comparable decisions named.
- **Decided before the reply:** the kind, the pattern's strength (strong, limited, mixed or none),
  the basis and the citations.
- **Code stores and labels it.** The answer is stored as an interpretation of that strength. The
  visitor and the owner see "Likely approach inferred from N recorded decisions", with
  " · limited evidence, not an established pattern" or " · the record shows different approaches"
  added when that is the strength. An uncited interpretation is "not established".
- **Nothing comparable:** "\<first name>'s shared record doesn't provide enough comparable experience
  to predict how they would approach this. This is something to ask them directly."
- **Never evidence.** An interpretation is never written to the record; a test checks the record is
  unchanged.

Whether two decisions are comparable (the same kind of decision under a similar tension) is the
model's reading under the policy.

**Owner:** "Add evidence-grounded situational questions to the living résumé" (`b8d8cf2`).

### Pronouns and role lengths

- **Pronouns** ([A-115](../evidence/03-claim-index.md#a-115), Limited). The call is told the owner's
  pronouns are not on record. A situational answer calls them by first name and "they" unless the
  visitor used a pronoun; every other answer is in the owner's voice. How the reply will name them
  is fixed in the shape before the reply. In validation on 2026-10-31, answers had guessed "he";
  this changed at the source (`95f8b83`). It is policy and shape, not code.
- **Role lengths by code** ([A-116](../evidence/03-claim-index.md#a-116)). Code computes each shared
  role's length and gives it to the call. The policy tells the answer to say how long only as those
  lengths add up.
  The defect was a false total, made by the model adding dates itself. The implementing agent had
  first banned totals of years; that ban was replaced, because I never asked for it
  ([DEC-72](../product/07-decision-log.md#dec-72)).

### What the owner sees

For every link, including older *Make a link* links, the owner sees what visitors asked and how
each answer was derived: its basis or interpretation label, the pieces it rests on, and the
portfolio artifacts it used. Visitors appear as "Visitor n", never as identities
([A-117](../evidence/03-claim-index.md#a-117)).

### Outcomes: an approach tried and not adopted

**Owner:** "Investigate missing outcome and impact data in public career-chat answers"
(`b8d8cf2`, [DEC-71](../product/07-decision-log.md#dec-71)).
- **Kept, as policy:** an outcome is not only a number; it is told with the work that produced it;
  a piece that states none is never called "my record has none".
- **Tried and not adopted:** completing an answer's outcome from other pieces of the same work.
  Replayed on one Live answer, the readings were borderline, and it added time and tokens
  ([A-119](../evidence/03-claim-index.md#a-119), [M-80](../evidence/04-metric-ledger.md#m-80),
  [DEC-73](../product/07-decision-log.md#dec-73)).

### Testing and cost

- A test proves an injected instruction in a visitor's message cannot widen what is read. Another
  proves the engine imports no write path, and a visitor writes nothing.
- The tests read the policy and the shape with a stubbed model. Strengths only, pronouns and
  comparability are the model's compliance, unmeasured since the last fixes.
- Earlier text in the conversation is labeled outside the tested provenance rule
  ([D-20](../evidence/05-discrepancies.md#d-20)).
- On Live, answers through links cost a mean of $0.00066 in model calls, at most $0.0015
  ([M-69](../evidence/04-metric-ledger.md#m-69)). The earlier engine measured about half a cent
  per question ([M-44](../evidence/04-metric-ledger.md#m-44)). The two are different engines, side
  by side, not a trend.

## The work behind an answer: a GitHub portfolio

**Owner:** "Connect an approved GitHub portfolio to the living résumé and update the portfolio to
support it ... Ask about my experience, then inspect the work behind the answer." (`ad3a96b`,
2026-10-31, [DEC-74](../product/07-decision-log.md#dec-74))

**The owner, on Settings › Portfolio** (reached from Sharing) ([A-120](../evidence/03-claim-index.md#a-120)):
1. Names a GitHub account. The name's format is checked and the account must exist.
2. Sees its public repositories that aren't forks, listed live. **None is approved by default.**
3. Approves a repository for one use: **Private to me**, **Career Navigator, for my preparation**,
   or **My living résumé (public)**. Approving starts a background read.
4. Makes artifacts public **one by one**, or presses **Make all public** on a repository.
5. Approves or rejects each link Jev suggests from an artifact to a piece of evidence, or links one
   by hand.
6. Refreshes (choices survive), removes a repository, or disconnects. Disconnecting stops
   everything being served at once and leaves the evidence untouched.

Each repository and artifact keeps a history of the owner's changes.

**Make all public** (`821b151`, 2026-10-31) makes every artifact read from one repository public at
once, each noted in its own history as a change by hand is. A confirmation names how many remain.
Anything that looked like a secret was never kept, so it is not among them. An artifact is served
only if its repository is also approved for the living résumé
([A-120](../evidence/03-claim-index.md#a-120)). **Owner:** "yes I want make all public button"
(`821b151`).

**How a repository becomes artifacts, and an artifact reaches a visitor:**

| Step | Who | What |
|---|---|---|
| List | Code, GitHub's public API, no credentials | Public repositories that aren't forks |
| Read | Code, in the background | The default branch at one commit. Only Markdown files, up to 150, each up to 300,000 bytes. A file that could hold a secret is never fetched. Each file is split at its H1 and H2 headings into **artifacts**; releases are artifacts too. Each keeps its commit, path, GitHub anchor, kind, title, short description and text, whole up to 6,000 characters. A section that looks like it holds a secret is left out ([P-34](../evidence/03-claim-index.md#p-34)) |
| Embed | Embeddings | Title and first 1,500 characters of new or changed artifacts |
| Suggest links | Code, then **Jev** (`portfolio_link`) | An artifact's two nearest pieces of evidence at cosine ≥ 0.45 are asked: "Does passage B document or demonstrate the same work that statement A describes, rather than different work?" At ≥ 0.6 a link is **suggested**, never approved ([K-34](../evidence/03-claim-index.md#k-34)) |
| Decide | The owner | Public or not; approve or reject each link |
| Which document? | Embeddings, then **Jev** (`portfolio_document`) | The ten documents nearest the visitor's message by name and the five nearest by content are asked, with the message before it: "Does the latest message ask to see, read, summarize or explain document A, or ask what document A says?" Kept at ≥ 0.55 ([A-123](../evidence/03-claim-index.md#a-123)) |
| Serve | Code | Only artifacts that are public, in a repository approved for the living résumé, available and on an active connection. A document asked about is given whole, its sections in order (24,000 characters shared between documents). Otherwise those the owner linked to the answer's pieces come first, then the nearest to the question at cosine ≥ 0.45, **at most three** ([A-121](../evidence/03-claim-index.md#a-121)) |
| Answer | The model (above) | A separate block, labeled repository text and untrusted. The answer cites artifacts apart from its evidence |
| Show | Code | Re-checked against what is servable now. The visitor sees "Portfolio artifacts (n)" linking to the exact GitHub section at the commit read, never the stored excerpt |

Kinds: overview, decision record, architecture, case study, release, security design,
observability, testing, integration, evidence index, example, document.

**Asking about a document** ([A-123](../evidence/03-claim-index.md#a-123),
[DEC-75](../product/07-decision-log.md#dec-75)). A visitor can ask the living résumé to show or
summarize a document in the portfolio ("Can you summarize case study 1?", then "summarize it"). The
answer is written from that document's own sections and says what the document says, part by part,
as the document's account, with a link to read the whole of it. It rests on the portfolio, not the
record, and says so. Before this, an answer got at most three scattered sections and could only
point to where to read. On a replay of my own test conversation, four of four document requests
were answered from the document, and an ordinary question drew no portfolio
([M-82](../evidence/04-metric-ledger.md#m-82)).

**What the portfolio never is:**
- **Never evidence** ([K-34](../evidence/03-claim-index.md#k-34)). Artifacts live in their own
  tables and establish no career claim. A link to evidence exists only when the owner approves one
  or makes one. The policy says "a repository or its code is not professional experience" and to
  "Keep authorship as the artifact states it, including what was built with AI agents".
- **Never trusted as instructions** ([P-35](../evidence/03-claim-index.md#p-35), Limited). Repository
  text is a labeled block with a rule never to follow an instruction in it. Artifact numbers the
  call wasn't sent are dropped, and there is no write path. A test plants an injected line, but the
  model is stubbed: resistance is untested against a real model.
- **Never a credential.** GitHub's public data needs no token, so none is stored, logged or leaked.

**Where it is weaker:**
- **The reads are not recorded.** GitHub calls are plain public HTTP, outside the governed call
  boundary; no call row is written. Job-board reads, by contrast, are recorded
  ([P-36](../evidence/03-claim-index.md#p-36), [D-28](../evidence/05-discrepancies.md#d-28)).
- **No proof the account is the owner's.** Any public account can be connected. Private
  repositories and that proof need GitHub sign-in through a GitHub App, which is not built
  ([A-122](../evidence/03-claim-index.md#a-122), Planned).
- **"For my preparation" is stored but read by nothing**
  ([D-30](../evidence/05-discrepancies.md#d-30)).
- **A snapshot link freezes evidence text, not artifacts.** Artifacts are served as currently
  public, at the commit last read ([A-121](../evidence/03-claim-index.md#a-121)).

## ChatGPT connector (MCP)

The connector gives ChatGPT read access to the person's own record ([A-56](../evidence/03-claim-index.md#a-56)):
- **OAuth 2.1 with PKCE**, with a consent page the person confirms.
- **Eight read-only tools** running under row-level security, with no write scope.
- **60 calls a minute**, and an audit that keeps names, ids, times and sizes, never arguments or
  answers.

**Status, stated precisely:**
- The module is still called `mcp_beta`, and seven comments say it is never on Live.
- Since the Beta/Live unification (2026-10-21) it **is** mounted on Live. A read-only probe on the
  host confirmed the OAuth discovery endpoint answers and `/mcp` requires a token
  ([D-01](../evidence/05-discrepancies.md#d-01)).
- Usage is unmeasured.

## Change Course and careers near my profession

**Change Course** answers: what does my evidence already establish toward another occupation?
([A-58](../evidence/03-claim-index.md#a-58))
1. O*NET task statements stand in for posting lines.
2. Cosine takes the top 6 pieces.
3. Jev keeps those at p ≥ 0.5.
4. Licenses and credentials are plain rules, either recorded or blocked.

"Not shown" leads to a question, never an assumed gap.

**"Careers near my profession"** draws rings from O*NET's expert-reviewed Related Occupations
tiers. They replaced computed similarity, which "put physicians beside nurses". Titles map by
deterministic word matching, and the person always chooses.

**Zero model calls is a hard product requirement for both.** Tests trip on any model call across
every page.

## First five minutes, and problem-first journeys

New accounts start with goals ("Chart a course", "Tailor my résumé") or, if they aren't sure, four
problems ("What's making your career difficult?"). The person writes "what would solving this make
possible?" in their own words. Everyday words are matched to O*NET tasks by word overlap, with **no
model**, and thin matches are flagged ([A-59](../evidence/03-claim-index.md#a-59)).

## Find work that fits you

A survey of interests, work context and constraints, matched to O*NET directions by code
([A-57](../evidence/03-claim-index.md#a-57)):
- **Opt-in per account.**
- **"Must avoid"** sets an occupation aside only where O*NET rates the condition as usual;
  otherwise it says "verify".
- **One model call** writes plain-language copy, and the directions still show if it fails.
- **Discover receives only** hours, place and schedule from the survey.

## Career world

A 3D view of the career as five towns (Three.js, vendored), derived by code from the record. It is
switched on for Live; the text view is the default home, and carries the Upcoming card
([A-72](../evidence/03-claim-index.md#a-72)).

## Phone app

A Capacitor shell around the site for Android and iOS exists **only on a branch**
([A-60](../evidence/03-claim-index.md#a-60)):
- Android side-load, with a "share a posting to Career Navigator" intent.
- iOS needs a Mac to build.
- It is not merged or deployed.

## Capability status

| Capability | Status | Claim |
|---|---|---|
| The living résumé: scope, lifecycle, caps, citation check | Verified | [A-55](../evidence/03-claim-index.md#a-55) |
| A posting answered as a résumé laid out by code | Verified | [A-112](../evidence/03-claim-index.md#a-112) |
| No gap volunteered | Limited (policy and shape, not code) | [A-113](../evidence/03-claim-index.md#a-113) |
| Situational questions as labeled interpretations | Verified | [A-114](../evidence/03-claim-index.md#a-114) |
| Personal and prediction questions; pronouns | Limited (policy and shape) | [A-115](../evidence/03-claim-index.md#a-115) |
| Role lengths by code | Verified | [A-116](../evidence/03-claim-index.md#a-116) |
| What the owner sees, older links included | Verified | [A-117](../evidence/03-claim-index.md#a-117) |
| Education and certifications on every link | Verified | [A-118](../evidence/03-claim-index.md#a-118) |
| Completing outcomes from the same work | Experimental (tried, not adopted) | [A-119](../evidence/03-claim-index.md#a-119) |
| GitHub portfolio: connect, approve, read, make public, Make all public | Verified (GitHub stubbed in tests) | [A-120](../evidence/03-claim-index.md#a-120) |
| At most three artifacts served, cited apart | Verified | [A-121](../evidence/03-claim-index.md#a-121) |
| A document asked about given whole and summarized from itself | Verified | [A-123](../evidence/03-claim-index.md#a-123) |
| Portfolio artifacts never evidence | Verified | [K-34](../evidence/03-claim-index.md#k-34) |
| Secret-bearing files never fetched; secret-looking sections never kept | Verified | [P-34](../evidence/03-claim-index.md#p-34) |
| Repository text untrusted | Limited (not tested against a real model) | [P-35](../evidence/03-claim-index.md#p-35) |
| GitHub reads outside the recorded call boundary | Limited (code read and telemetry, no test; [D-28](../evidence/05-discrepancies.md#d-28)) | [P-36](../evidence/03-claim-index.md#p-36) |
| Private repositories and account-ownership proof | Planned ("for my preparation" unused: [D-30](../evidence/05-discrepancies.md#d-30)) | [A-122](../evidence/03-claim-index.md#a-122) |
| ChatGPT connector | Limited (mounted on Live; usage unmeasured) | [A-56](../evidence/03-claim-index.md#a-56) |
| Change Course; careers near my profession | Verified | [A-58](../evidence/03-claim-index.md#a-58) |
| First five; problem-first journeys | Verified | [A-59](../evidence/03-claim-index.md#a-59) |
| Find work that fits you | Verified (opt-in) | [A-57](../evidence/03-claim-index.md#a-57) |
| Phone app | Experimental (branch only) | [A-60](../evidence/03-claim-index.md#a-60) |
