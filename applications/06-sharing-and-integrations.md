# Applications 06 — Sharing, integrations and other journeys

*Applications 4.0 · describes Live `7322289` (2026-10-24)*

**The question this answers:** where else does the career record go, and what keeps it inside the
scope the person chose?

## Share my career conversation

A public link where anyone can ask about the owner's career and get answers in the owner's voice,
only from what the owner chose to share ([A-55](../evidence/03-claim-index.md#a-55)).

**Scope and lifecycle:**
- **Draft until activated.** A link answers nobody until the owner activates it.
- **The owner chooses the scope:** which roles, optional limits, live or snapshot mode, and an
  expiry of 7, 30 or 90 days or never.
- **The token is stored as a digest.**
- **Scope is computed on the server before retrieval.** Retired and flagged pieces are excluded. In
  snapshot mode, pieces changed since capture are left out.

**A visitor's turn:**
1. **Code caps:** a per-link spend cap, messages per minute per address, and turns per visitor.
2. **Retrieval:** embeddings within the chosen scope.
3. **Answer:** one model call.
4. **Citation check:** an uncited claim becomes "not established".

**Testing and cost:**
- A test proves an injected instruction in a visitor's message cannot widen what is read. Another
  proves the engine imports no write path.
- Measured cost of the earlier share link was about half a cent per question ([M-44](../evidence/04-metric-ledger.md#m-44)).



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
4. Licences and credentials are plain rules, either recorded or blocked.

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
switched on for Live; the text view is the default home.

## Phone app

A Capacitor shell around the site for Android and iOS exists **only on a branch**
([A-60](../evidence/03-claim-index.md#a-60)):
- Android side-load, with a "share a posting to Career Navigator" intent.
- iOS needs a Mac to build.
- It is not merged or deployed.

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Career conversation share | Verified | [A-55](../evidence/03-claim-index.md#a-55) |
| ChatGPT connector | Limited (mounted on Live; usage unmeasured) | [A-56](../evidence/03-claim-index.md#a-56) |
| Change Course; careers near my profession | Verified | [A-58](../evidence/03-claim-index.md#a-58) |
| First five; problem-first journeys | Verified | [A-59](../evidence/03-claim-index.md#a-59) |
| Find work that fits you | Verified (opt-in) | [A-57](../evidence/03-claim-index.md#a-57) |
| Phone app | Experimental (branch only) | [A-60](../evidence/03-claim-index.md#a-60) |
