# Applications 03 — Résumé planning, writing and review

*Applications 5.0 · describes Live `00eac95` (2026-10-31) · diagram: [Architecture 04](../architecture/04-resume-flow.md) · case study: [02](../case-studies/02-preventing-unsupported-claims.md)*

**The question this answers:** how does the system turn selected evidence into a résumé, and what
keeps the writing from claiming more than the evidence shows?

## The design in one paragraph

A résumé holds two kinds of writing, and they are made two ways.

**Bullets.** Selection decides *which evidence* goes on the page. A selector (a model playing a
recruiter) sees the job's requirements and the candidate stories, and answers with story
**numbers** only. Code copies the chosen stories, verbatim, into the writer's prompt. **The bullet
writer never sees the requirements, the posting or anything the selector wrote.** Each bullet is
drafted as the line that will print, tagged with the story it was written from through a schema the
API enforces. Only a bullet longer than two printed lines is shortened. This is the
"recruiter-selects" flow, live since 2026-10-14
([A-11](../evidence/03-claim-index.md#a-11), [A-91](../evidence/03-claim-index.md#a-91)).

**Summaries.** Since 2026-10-28 the professional summary and each role's summary are written from a
supported positioning ([A-82](../evidence/03-claim-index.md#a-82),
[A-85](../evidence/03-claim-index.md#a-85)). A planner model reads the posting into a few needs. Jev
classes the person's stories against those needs. The planner writes a brief whose
assertions can cite only the matched stories (a citation is not required). The summary writers read the brief, never the posting. Jev reads each
sentence against the original stories and code checks the wording. The summary is placed as
written, with what they found shown beside it. Nothing replaces it
([A-84](../evidence/03-claim-index.md#a-84)).

Two reviewer seats and one editor pass then read the finished page and **report**. They don't
rewrite it.

## Who decides what

| Role | Kind | Decides |
|---|---|---|
| **Selection** | Code + Jev | Each requirement's chosen story and alternates; the story pool sized to the page; never a story retired since the job was charted |
| **Selector** ("recruiter") | Language model | Which stories become each role's bullets, and which draft bullets to keep, by number |
| **Bullet writer** | Language model | The wording of each bullet, from the stories it was handed |
| **Summary planner** | Language model | What the posting needs; the positioning brief; which of the Jev-matched stories each assertion cites |
| **Jev** | Probability model | Whether each story is direct or transferable evidence for each need; whether each brief assertion and summary sentence is supported by the stories it cites |
| **Summary writers** (professional, one per role) | Language model | The wording of each summary, from the brief |
| **Editor** | Language model + code gate | Spelling, grammar and mechanical corrections only, as an overlay |
| **Reviewers** (recruiter, hiring manager) | Language model ×2 | Report coverage, importance and impact per requirement; advance yes/no |
| **Person** | Human | Press Write; reword, remove, reorder lines; press Fix on a line; press the red button for a missing summary; download |

## Stage by stage: what each stage receives

The summaries run in a lane of their own, started beside the bullets
([Summaries](#summaries-from-a-supported-positioning) below has their steps). The requirement list
comes from [Applications 01](01-job-analysis-and-assessment.md). Since 2026-10-29 a posting sentence
opening with "Or" stays with the requirement it offers another way to meet
([A-95](../evidence/03-claim-index.md#a-95)).

| # | Stage | Kind | Receives | Sees requirement or posting text? | Produces |
|---|---|---|---|---|---|
| 1 | Write press | Human | — | — | A queued run; refused without an assessment ([A-37](../evidence/03-claim-index.md#a-37)) |
| 2 | Evidence documents | Code | Stories | No | Canonical, hashed text per story |
| 3 | Selection | Code (+ Jev on ties) | The frozen assessment reading | Jev only, on ties | Chosen story per requirement, alternates. A story retired since the job was charted is skipped ([A-94](../evidence/03-claim-index.md#a-94)) |
| 4 | Flag filter | Code + person's flags | Stories | No | Flagged stories removed, for bullets and summaries alike ([K-17](../evidence/03-claim-index.md#k-17)) |
| 5 | Shared facts | Embeddings + Jev | One role's story sentences | No | Sentences two stories share, given to one of them ([A-14](../evidence/03-claim-index.md#a-14)) |
| 6 | Summaries' preparation, **beside stages 7–11** | **Model** (planner) → Jev → **model** | The posting; the stories of every role that may get bullets | **The planner reads the raw posting** | The posting's needs; each story classed against each need; stories in plain words ([A-82](../evidence/03-claim-index.md#a-82), [A-87](../evidence/03-claim-index.md#a-87)); the career journey, when none is saved ([A-86](../evidence/03-claim-index.md#a-86)) |
| 7 | Selector: pick stories (every role at once) | **Model** | Job title, every requirement (R1…Rn), the role's numbered whole stories | **Yes** | Numbers only |
| 8 | Bullet writer: draft | **Model** | The picked stories, copied by code, in the selector's order; the writing rule | **No.** A runtime guard refuses the call if the requirements block appears | Each bullet as its finished line: story number (enum), what was done, at most two results, the line ([A-91](../evidence/03-claim-index.md#a-91), [A-13](../evidence/03-claim-index.md#a-13)) |
| 9 | Selector: keep bullets | **Model** | Requirements + numbered draft bullets | **Yes** | Numbers only |
| 10 | Bullet writer: shorten, **only when needed** | **Model** | Only the kept bullets longer than 220 characters, numbered among themselves | **No** | Shorter text, each back in its own place ([A-91](../evidence/03-claim-index.md#a-91)) |
| 11 | Store | Code | — | — | Bullets with their story's event id, stored `UNGROUNDED`; the database refuses a cross-role citation ([K-02](../evidence/03-claim-index.md#k-02)) |
| 12 | Summaries' finish, **beside stage 13** | **Model** → Jev → **model** → Jev + code | The needs, Jev's classes, the stories in plain words, the journey, the bullets | Writers: **no** (a tested guard). The brief they read was written by a planner that read the posting. Code compares the summary with the posting for copied wording | The positioning brief; the professional summary and each role's summary, with findings ([A-82](../evidence/03-claim-index.md#a-82)–[A-85](../evidence/03-claim-index.md#a-85)) |
| 13 | Competencies | **Model** | Bullets only (the posting is a forbidden input, checked) | **No** | Competencies with citations; uncited ones dropped |
| 14 | Enrichment | Code | The summaries, when they arrive | — | Summaries stored as written, `UNGROUNDED` ([A-84](../evidence/03-claim-index.md#a-84)) |
| 15 | Page fit | Code (+ Jev first-minute bullets) | Bullets, the exported PDF | Jev only | Cuts from the end of the selector's order; never empties a role ([A-18](../evidence/03-claim-index.md#a-18)) |
| 16 | Coverage review, **beside stage 17** | **Model ×2** | Requirements (no eligibility lines; education labeled a risk), the finished lines, readability measures counted by code | **Yes** (never the career record) | One row per requirement per seat; **report only** ([A-15](../evidence/03-claim-index.md#a-15)) |
| 17 | Editor | **Model** → code gate → **model** verify | Résumé lines only | **No** | Corrections as an overlay: no new figure or name, no negation change, ≤ 6 words ([A-16](../evidence/03-claim-index.md#a-16)) |
| 18 | Repeat labels | Jev | Bullets, summary pieces | Jev only | "Repeats line N" labels; **nothing removed** |
| 19 | What's next | **Model** | The review and the nearest evidence | Yes | Actions, e.g. "this story states no result: add one" |
| 20 | Review page | Code + Jev | The stored run and the person's edits | Jev only | Numbered lines ([A-96](../evidence/03-claim-index.md#a-96)); the summaries' findings as labels ([A-84](../evidence/03-claim-index.md#a-84)); citations that follow each line's words ([A-93](../evidence/03-claim-index.md#a-93)); a red button where a summary is missing ([A-90](../evidence/03-claim-index.md#a-90)) |
| 21 | Person edits | Human | — | — | Reword, remove, reorder. **Saving starts no review.** A reworded line is cited only for what Jev reads its new words as showing ([A-19](../evidence/03-claim-index.md#a-19)) |
| 22 | Fix (optional) | Human → **model** → code gate → re-review | One line, its findings and its own evidence | **No** | A repaired line, at most two attempts. On these résumés Fix never writes a summary ([A-17](../evidence/03-claim-index.md#a-17)) |
| 23 | Red button (optional) | Human → **model** → Jev + code | The build's own brief, or, when it kept none, needs and a brief written now from the posting; the stories cited | Writer: **no**; the planner reads the posting only when no brief was kept | Only the missing summary, with its findings; nothing else changes and nothing is reviewed again ([A-90](../evidence/03-claim-index.md#a-90)) |
| 24 | Download | Code | The page with the person's edits and the editor's overlay | — | The same PDF export the page fit measured |

A bullet now has one writing call unless it is too long. How the "one writer pass, one editor pass"
rule is read is recorded in [D-09](../evidence/05-discrepancies.md#d-09).

## Bullets: each written as its finished line

- **The draft's shape** ([A-91](../evidence/03-claim-index.md#a-91)). For each bullet the answer
  must give the story number (an enum of the stories handed over), what the person did in the
  story's own verb, at most two results in the story's own words, and then the line. The line is
  asked for at about 25 words and never more than 27. Only the line is stored.
- **Shortened only past two printed lines.** Only a kept bullet longer than 220 characters is sent
  to be shortened, to at most 25 words. Each answer replaces its own bullet. Most résumés make no
  shortening call. The count, identity and order of bullets stay the selector's.
- **Why 220 characters.** The limit was read off downloaded PDFs. Every bullet up to 228 characters
  printed on two lines. One of 244 printed on three, though the page measure counted it as two
  ([M-62](../evidence/04-metric-ledger.md#m-62)). The printed-page fit is still the backstop: it
  cuts bullets and never rewrites them ([A-18](../evidence/03-claim-index.md#a-18)).
- **One writing rule in both steps** ([A-92](../evidence/03-claim-index.md#a-92)). Keep the kind of
  work and whose it was. Keep each result as stated: achieved, intended, forecast or found in a
  test; never turn an aim into a result. Keep what each detail belongs to and caused, and each
  figure with what it measured. Write a change in words, never with arrows or symbols. This is a
  prompt instruction. No code checks it.
- **On one Beta run's inputs**, the finished-line draft gave the same 20 bullets in the same order
  on the same 40 printed lines, with 3 writer calls where there had been 6
  ([M-63](../evidence/04-metric-ledger.md#m-63)).

**Owner:** *"Improve résumé writing to match the manually edited review …"*; *"figure it out ... can
not exceed the current time ... can not cost any more"* (my words, commit `7411d3f`;
[DEC-59](../product/07-decision-log.md#dec-59)). The standard was my own hand-edited résumé, used as
a writing standard and never as evidence. It replaced a second call that squeezed every bullet to
25 words; the commit records that the squeeze produced the shorthand and most of the meaning errors
I had fixed by hand. A constraint on any writing change: *"Neither accepting fewer bullets nor
changing their order is acceptable"* (my words, commit `ef6ef6c`;
[DEC-57](../product/07-decision-log.md#dec-57)).

## Summaries from a supported positioning

The professional summary says who the person is professionally, their strongest relevant scope, and
how their current work connects to it. It is positioned for the posting and written only from what
their stories support ([A-82](../evidence/03-claim-index.md#a-82),
[DEC-51](../product/07-decision-log.md#dec-51)).

| Step | When | Kind | Sees | Never sees | Output |
|---|---|---|---|---|---|
| 1. Needs | Started before the bullets | **Model** (planner), low reasoning | Job title, the posting text | The career record | Purpose, 3–5 central needs, the leader, the environment, the problems (schema) |
| 2. Classes | Beside the bullets | **Jev** | Each need × each unflagged, unretired story of every role that may get bullets | — | *Direct* (establishes ≥ 0.5), else *transferable* (related ≥ 0.5) |
| 3. Plain words | Beside the bullets; after them for stories behind bullets not yet restated | **Model**, low, ten stories a call | Story text; the saved journey and role summaries | The posting, the needs, the requirements | Restatements, every fact kept, stored for reuse ([A-87](../evidence/03-claim-index.md#a-87)) |
| 4. Brief | After the bullets | **Model** (planner), low | Its own reading of the needs; the matched stories in plain words, with their roles and Jev classes; needs with no evidence; the journey; the bullets already written | The raw posting, the requirement list | Identity, the employer's problem, pillars, operating style, throughline, current-work connection, planned bullet topics, areas to avoid. An assertion can cite only the matched ids (an enum); a citation is not required, and the throughline names roles |
| 5. Brief checks | After 4 | **Jev** | Each assertion against the original stories it cites | — | A probability per assertion, **reported only** |
| 6. Writer | After 5, beside the role writers | **Model**, low | The brief without its employer's-problem field; the word and character budget; the plain text of the cited stories; the journey and role summaries; the planned bullet topics | The posting, the requirements, the employer's problem. A runtime guard refuses the call otherwise | Three required fields: who the person is and the problems they solve; scope or capability; current work. Each clause names the brief field and the stories it rests on |
| 7. Verify | After 6 | **Jev** + code | Each sentence against the original stories its clauses cite; also the journey, for the throughline or a clause that cites nothing | — | Supported or not, per sentence; code flags |
| 8. Place | After 7 | Code | — | — | Placed whenever there is text, whatever was found; stored `UNGROUNDED` |

Jev is asked whether the stories state or directly show what the sentence claims about the person's
work, with no more scope, ownership or result than the stories give. Code flags, and only reports: an
opening "led", "built", "created" or "deployed"; more than one sentence carrying a figure; a list of
three or more tools; job logistics; any six-word run copied from the posting; a paragraph over the
page's character cap; more than 70 words.

### Placed as written, never a backup

**Owner:** *"I dont ever want the default summaries to be a backup"* (my words, commit `62d4327`;
[DEC-53](../product/07-decision-log.md#dec-53)). For thirteen minutes on Beta (`ba6f332` →
`62d4327`, 2026-10-28; both reached Live together) the positioning summary was placed only when
Jev supported every sentence and code flagged nothing; otherwise the older summary stayed. `62d4327` removed that fallback.

The review page now shows labels on the summary: "not supported by your stories" (Jev below 0.5),
"not read by Jev" (Jev gave no answer), and each code flag. They show only while the text reads
exactly as written ([A-84](../evidence/03-claim-index.md#a-84)). Nothing is rewritten. The status is
Limited because placement is tested by source inspection only.

### What the summary writers see

The writers get the brief without its employer's-problem field, since 2026-10-29
([DEC-60](../product/07-decision-log.md#dec-60)). Offered as a field to rest a clause on, the
employer's need had come back as the candidate's own work. A runtime guard refuses a writer's
message that holds the first 60 characters of any requirement or posting line longer than 40
characters, and a test exercises it ([A-83](../evidence/03-claim-index.md#a-83)).

That isolation is **Limited**. The planner writes the identity "in this employer's vocabulary where
it fits", and its avoid list names what the posting asks for that the person can't show. Both reach
the writers **by design**. Short requirements are never compared by the guard. Copied wording is
flagged, not blocked.

### Role summaries

Each role with bullets gets a short summary under its title: what the person owned, what it did for
the people it served, and how far their ownership reached. It does not repeat the bullets' results
([A-85](../evidence/03-claim-index.md#a-85), [DEC-52](../product/07-decision-log.md#dec-52)).

- **Inputs.** The role's title and employer (no dates), its saved summary, the brief's pillars that
  rest on its stories, the stories behind its bullets in plain words, and its bullets (so it does
  not repeat them). Never the posting (same guard), the needs or other roles' stories.
- **Shape.** Code sets the sentence count from the bullet count: one for 1–2 bullets, two for 3–9,
  three for 10 or more. The schema holds that count, and each sentence cites the role's stories by
  enum. Each sentence is asked for at most 15 words.
- **Checks.** Jev reads each sentence against the stories it cites and the role's saved summary.
  Code flags a wrong count, more than 15 words, figures not in its stories, and tool lists.
- **Failure.** Every role writer runs at once, beside the professional writer. One that fails leaves
  the others untouched; that role gets no summary, and the red button appears.

### The career journey

The planner and writers read a career journey: one paragraph for the whole career and one for each
role. Live has no Career Themes page to produce it, so the first résumé build that finds none saved
writes it once, beside the bullets. One model call writes it from the person's stories, never
seeing the job, and it is saved ([A-86](../evidence/03-claim-index.md#a-86)). **Owner:** *"Write it
when missing"* (my words, commit `fd6fd3a`; [DEC-54](../product/07-decision-log.md#dec-54)). It is
derived context, never evidence.

Its limits: nothing on Live rewrites it once it exists. It leaves out only the stories the person
flagged, not those the deterministic reading flags ([D-37](../evidence/05-discrepancies.md#d-37)).
Because Jev reads a throughline clause against it, a summary sentence can be supported by text a
model wrote.

### Plain words

Before the planner and writers read the stories, a model restates them in words a hiring manager
outside the company would understand. Every fact, figure and name is kept, nothing is added, and
internal mechanism names are replaced by what the work does. Ten stories go to a call, and all calls
run at once. Jev always reads the originals. Restatements are stored, keyed by a hash of the words
and a hash of the instruction, so a later résumé reuses them; changed words or a changed instruction
make a new key ([A-87](../evidence/03-claim-index.md#a-87)). They are not shown to the person, and
an error in one reaches the planner and the writers.

### Speed route, reasoning and retries

- **Beside the bullets** ([A-88](../evidence/03-claim-index.md#a-88),
  [DEC-55](../product/07-decision-log.md#dec-55)). The needs call, the career journey when missing,
  Jev's classes and the plain words start in their own threads while every role's bullets are
  written. After the bullets come the remaining plain words, the brief, the brief checks, the
  professional writer and every role writer at once, then verification. Competencies are written
  while the summaries finish, and enrichment waits for them. Each thread is handed its inputs when
  it starts: a name re-bound later had once left a Beta résumé with no summary at all.
- **Low reasoning** for the summary planner and writers. Picks, bullets, competencies, the editor
  and the reviewers keep theirs. On one Beta posting the summaries took 86 s at low reasoning,
  against 148 s and 174 s at medium, with about the same Jev support
  ([M-61](../evidence/04-metric-ledger.md#m-61)).
- **Model.** The summary stages and the career journey have no row in the governed model
  assignments, so they run on the application's default model: gpt-5-mini on Live
  ([M-68](../evidence/04-metric-ledger.md#m-68)).
- **What it did not deliver.** I asked for résumés in half the time and at half the cost. On Live
  the time per résumé did not halve ([Measured behavior](#measured-behavior)).
- **Retries** ([A-89](../evidence/03-claim-index.md#a-89)). A summary call that failed on the
  provider's side (a dropped connection, a time-out, a rate limit, or a 500, 502, 503 or 504 server
  error) is made again, up to three tries in all. An answer that did not fit or did not parse is not
  asked again. A failed Jev read is also made again, up to three tries; a rate limit is left to the
  Jev client, which waits. A sentence Jev could not read is labeled "not read by Jev",
  never "unsupported".
- **The page's character cap.** The professional summary is written to the page's own character
  cap (the writing policy's executive-summary limit), as characters and words, so the page never
  has to cut a sentence from it. Before this, a summary of 538 characters met a 520-character cap
  and the page dropped its third sentence ([M-65](../evidence/04-metric-ledger.md#m-65)). Code flags
  a paragraph over the cap ([A-84](../evidence/03-claim-index.md#a-84)).

### The red button for a missing summary

If a résumé came out without its professional summary, or without a role's, its newest review shows
a **red** button in the résumé, where that summary belongs
([A-90](../evidence/03-claim-index.md#a-90), [DEC-56](../product/07-decision-log.md#dec-56)).
**Owner:** *"rewrite just the missing summary for the resume"*; *"the button to be in the resume
where the missing summary is at. And for the button to be RED"* (my words, commit `caa6460`).

- Pressing it starts background work. It reuses the build's own brief when the build reached one;
  otherwise the needs and a brief are written now. Only the cited stories not yet in plain words
  are restated. One writer call writes the summary, followed by the same Jev and code checks.
- Nothing else changes, and the résumé is not reviewed again. The new summary is never read by the
  reviewers.
- It is a person-pressed retry of a stage that produced nothing, on the same inputs. It is not a
  quality repair, it does not follow a review, and it makes no writer → reviewer loop.
- The status is Limited: the button, its route and the change to Fix are tested by template or
  source inspection, and there is no route test.

## On the review page

- **Line numbers.** Every résumé line shows its number. A finding's "Line N" link scrolls to the
  line and marks the words it quotes ([A-96](../evidence/03-claim-index.md#a-96); template-string
  tests only).
- **Citations follow a line's words** ([A-93](../evidence/03-claim-index.md#a-93),
  [DEC-61](../product/07-decision-log.md#dec-61)). Before 2026-10-29, a bullet reworded in place
  kept every citation, highlight and "repeats" label its old words had. Now:
  - an unchanged line keeps its citations, wherever it moved;
  - a removed line is cited for nothing;
  - a reworded line, or one the review never read, is cited only for the requirements Jev reads its
    new words as showing (establishes or related ≥ 0.5);
  - a "repeats" label goes when either of its two lines changes.

  Jev's readings are cached on a session of their own that commits, so a page that only reads
  still keeps them. Before that, one review with every line reworded asked Jev about 1,100
  (requirement, line) pairs on every view and took 60–130 s per view
  ([M-66](../evidence/04-metric-ledger.md#m-66)). A reworded line is credited on one Jev bar
  (establishes or related); the reviewers never re-read it.
- **Person edits** ([A-19](../evidence/03-claim-index.md#a-19)). The person can reword, remove and
  reorder lines. Their edits are applied first, in the one place every view reads. **Saving starts
  no review:** manual edits are the person's decision. Earlier releases of this portfolio said the
  review re-runs; it never did.
- **Fix, narrower** ([A-17](../evidence/03-claim-index.md#a-17)). On a résumé whose summaries the
  positioning tool wrote, Fix repairs flagged lines only; a missing summary comes from the red
  button. On a résumé built before 2026-10-28, Fix still rewrites a refused summary with the older
  summary writer. Fix is catch-and-repair by design: a model rewrite, a code gate (numbers, new
  words, relation, agency), the editor's re-read, then the review again, at most twice.

## Exactly how requirement text is withheld

**From the bullet writer** ([A-12](../evidence/03-claim-index.md#a-12)):
1. Code builds every bullet-writer prompt from story text, the writer's own draft and policy text.
2. The selector's reply is parsed into integers, so nothing it writes reaches the writer.
3. A unit test asserts that no writer prompt contains the requirements.

**From the summary writers** ([A-83](../evidence/03-claim-index.md#a-83)):
1. Code builds their prompts from the brief without its employer's-problem field, the stories in
   plain words, the journey and the role summaries.
2. A runtime guard refuses a prompt holding the opening of any requirement or long posting line,
   and a test exercises it.
3. Code flags any six-word run copied from the posting.

**The limits of that enforcement:**
- The bullet writer's runtime guard is a **substring check**. It catches the requirements heading or
  the whole block, not one requirement's wording, and no test exercises the guard itself.
- The bullet writer's declared "forbidden inputs" (requirements, posting) are documentation in this
  flow. The check that would enforce them is not called
  ([D-07](../evidence/05-discrepancies.md#d-07)).
- The summary guard compares only the first 60 characters of lines longer than 40 characters.
- **The posting reaches the summaries through the brief, by design.** The planner read the posting
  and writes in its vocabulary where it fits.
- Requirement wording can still enter **through the evidence**. The gap chat drafts stories with the
  requirement in view, and the person saves them. The chat policy tells the model not to borrow the
  posting's words; that is a prompt rule, not a code check.

**Where the posting's words reach:**

| Text | Reaches | Never reaches |
|---|---|---|
| The raw posting | The summary planner (needs); code's check for copied wording | Any writer, the editor, Fix |
| The requirement list | The selector (pick and keep); the reviewers; Jev at selection ties | Any writer, the editor, Fix |
| The planner's needs | Jev's classes; the brief | Any writer directly |
| The brief (without the employer's problem) | The summary writers | The bullet writer, the editor, Fix |

## Why this design

| Alternative | What happened |
|---|---|
| Writer sees requirements, checks catch overreach (older flow) | Copied posting phrases had to be detected and dropped: 52 of 265 bullets on Beta, nearly all one test account, and 2 of 220 on Live ([M-43](../evidence/04-metric-ledger.md#m-43)). Relation and agency checks refused lines after the fact. Grounding took two thirds of a 14-minute run ([A-20](../evidence/03-claim-index.md#a-20), [M-35](../evidence/04-metric-ledger.md#m-35)) |
| Automatic repair after review | Shipped and removed the same day: it was catch-and-repair ([Product 02 §3](../product/02-principles.md#3-defects-are-fixed-at-their-source-never-papered-over)) |
| Content-plan branch: labeled story parts, evidence-isolated writing | Built on a branch (12 commits), superseded before deployment |
| **Recruiter-selects (chosen, for bullets)** | I did by hand what I wanted the system to do, and it beat every engineered variant. My instruction: do exactly that, and never pass the writer the recruiter's text about what to write |
| A second call squeezing every bullet to 25 words (to 2026-10-29) | The squeeze produced shorthand and most of the meaning errors I fixed by hand. Replaced by drafting the finished line ([DEC-59](../product/07-decision-log.md#dec-59)) |
| Polish: each bullet returned tightened and polished (Beta, 2026-10-29) | Changed the meaning of 6 of 23 bullets at low reasoning and 8 at medium, different ones each time, and flagged none. Closed the same day ([A-97](../evidence/03-claim-index.md#a-97), [M-64](../evidence/04-metric-ledger.md#m-64), [DEC-58](../product/07-decision-log.md#dec-58)) |
| Summaries by the selector and writer in the same four steps as bullets (Live to 2026-10-28) | Replaced by the positioning summaries ([A-101](../evidence/03-claim-index.md#a-101)) |
| A summary tool: Jev selects each role's stories, two seats pick by number, one sentence per story (2026-10-28) | Replaced the same day by the positioning summaries ([A-101](../evidence/03-claim-index.md#a-101)) |
| Positioning summary placed only when every check passed, else the older summary (2026-10-28) | **Owner:** never a backup. What Jev and code find is shown instead ([DEC-53](../product/07-decision-log.md#dec-53)) |
| The employer's problem offered to the summary writer as a field to cite | It came back as the candidate's own work. Withheld from the writer since 2026-10-29 ([DEC-60](../product/07-decision-log.md#dec-60)) |

## Measured behavior

### On Live since the speed route (17 résumés, 2026-10-30 → 10-31)

| Measure | Value |
|---|---|
| Wall clock per run | median 210 s, mean 214 s (min 165 s, max 304 s) ([M-60](../evidence/04-metric-ledger.md#m-60)) |
| Recorded cost per run (run ledger: an upper bound, [D-21](../evidence/05-discrepancies.md#d-21)) | mean $0.160, median $0.128 (min $0.103, max $0.278) ([M-60](../evidence/04-metric-ledger.md#m-60)) |
| Model cost per run that can be attributed to the run | selector $0.0130 (5.1 calls), bullet writer $0.0135 (3.8 calls), summaries $0.0222 (6.5 calls) ([M-60](../evidence/04-metric-ledger.md#m-60)) |

Of those three, the summaries cost the most per run. Jev's reads for the summaries are not in these
figures: the classing calls carry no reference to the run. Since 2026-10-25 every summary and
career-journey call on Live ran on gpt-5-mini ([M-68](../evidence/04-metric-ledger.md#m-68)). Not
yet measured on Live: bullets per résumé, the share of runs with no shortening call, how often
summaries are placed with findings, and red-button use.

I asked for half the time and half the cost. M-60 does not show the time halved. The earlier
state's median ([M-05](../evidence/04-metric-ledger.md#m-05)) is a different system state, so the
two sit side by side here and are not a trend.

### Measured on Beta while building it

| Measure | Value |
|---|---|
| Summary time, low vs medium reasoning (one posting, three runs) | 86 s vs 148 s and 174 s, about the same support ([M-61](../evidence/04-metric-ledger.md#m-61)) |
| Characters that fit two printed lines (78 bullets in four downloaded résumés) | every bullet up to 228 characters printed on two lines; one of 244 printed on three ([M-62](../evidence/04-metric-ledger.md#m-62)) |
| Finished-line bullets on one run's inputs | same 20 bullets, same order, same 40 printed lines; 3 writer calls where there were 6 ([M-63](../evidence/04-metric-ledger.md#m-63)) |
| A summary over the page's cap (one run) | 538 characters against 520; the third sentence dropped ([M-65](../evidence/04-metric-ledger.md#m-65)) |
| Polish experiment (one run's 23 bullets) | meaning changed in 6 at low reasoning, 8 at medium ([M-64](../evidence/04-metric-ledger.md#m-64)) |

A Live observation recorded in a commit: before Jev's citation readings were cached on their own
session, one review asked about 1,100 (requirement, line) pairs per view, taking 60–130 s per view
([M-66](../evidence/04-metric-ledger.md#m-66)).

### The earlier state (Live, 32 résumés, 2026-10-21 → 10-24)

These figures describe the flow before the summaries were rebuilt (2026-10-28) and before bullets
were drafted as finished lines (2026-10-29). They are a different system state from the figures
above: side by side, never a trend.

| Measure | Value |
|---|---|
| Bullets per résumé | mean 17.6, range 9–30 ([M-07](../evidence/04-metric-ledger.md#m-07)) |
| Language-model cost of the attributable stages | ≈ $0.11 per résumé ([M-03](../evidence/04-metric-ledger.md#m-03)) |
| Recorded cost per run (run ledger) | mean $0.187, median $0.198 ([M-04](../evidence/04-metric-ledger.md#m-04)) |
| Wall clock | median 207 s ([M-05](../evidence/04-metric-ledger.md#m-05)) |

**Summary length in the earlier flow.** Asked for one text "of at most N words", 73% of executive
summaries and 96% of role summaries were over the readability limit. Asked for at most three
sentences of at most 15 words (two for a role summary), 0 of 20 were
([M-17](../evidence/04-metric-ledger.md#m-17)). That was a prompt request, and it describes the
summaries superseded on 2026-10-28. Now the professional summary is three schema fields sized to the
page's character cap (flagged, not enforced), and a role summary's sentence count is held by the
schema.

## Residual risks

The design is **not hallucination-proof**.

**Checked now, and reported only.** None of these checks changes the page.

| What is read | By | What happens |
|---|---|---|
| Each summary sentence, against the original stories it cites | Jev ([A-84](../evidence/03-claim-index.md#a-84)) | A label on the summary; it stays as written |
| Each brief assertion, against its stories | Jev ([A-82](../evidence/03-claim-index.md#a-82)) | Recorded with the run |
| Summary wording: opener, figures, tool lists, logistics, copied posting wording, length | Code ([A-84](../evidence/03-claim-index.md#a-84)) | A label on the summary |
| A reworded line | Jev ([A-93](../evidence/03-claim-index.md#a-93)) | Its citations follow what it now shows |
| Every requirement, against the finished page | Two reviewer seats ([A-15](../evidence/03-claim-index.md#a-15)) | Rows on the review page |
| Two lines that say the same | Jev | A "repeats" label; nothing removed |

**Still unchecked, or checked only weakly:**

1. **No code compares final bullet text with the evidence on Live.** Every bullet and summary is
   stored `UNGROUNDED`. The writer's "use only the facts in the text above" and the shared writing
   rule are prompt rules ([A-92](../evidence/03-claim-index.md#a-92)). Reviewers and the editor
   are deliberately not shown the career record ([K-23](../evidence/03-claim-index.md#k-23)).
2. **Ownership inflation in bullets is not checked at build time.** For example, "supported"
   becoming "led". The relation and agency checks exist but run only inside Fix
   ([D-08](../evidence/05-discrepancies.md#d-08)). Summaries get Jev's reading, which asks about
   scope, ownership and result, but it only reports.
3. **Strong evidence can still be written weakly.** A measurement recorded in a Beta commit found
   about 1 in 6 requirements assessed *strong* came out partial or absent on the reviewed résumé
   ([M-57](../evidence/04-metric-ledger.md#m-57)). Telling the selector which story shows which
   requirement shortened résumés from 18–20 bullets to 10–13 with no reviewer gain, so it was
   reverted ([A-21](../evidence/03-claim-index.md#a-21),
   [M-18](../evidence/04-metric-ledger.md#m-18)).
4. **Conflicting figures in the record go undetected** in this flow (the check exists only in the
   older path).
5. **Some limits are requested, not enforced.** "One bullet per story" is a prompt instruction;
   since 2026-10-24 a split story is attributed correctly, but it is not prevented. The 27-word
   bullet ceiling is requested; code compares characters only, and a shortened bullet is not
   measured again. Summary word limits are requested and flagged. The summaries' sentence counts are
   now held by the schema.
6. **A story containing the literal word "REQUIREMENTS" would trip the bullet guard** and fail the
   run.
7. **Posting wording reaches the summaries through the brief**, by design, and the guard compares
   only line openings ([A-83](../evidence/03-claim-index.md#a-83)).
8. **Summary support can rest on derived text.** The model-written career journey and the role's
   saved summary are part of what Jev reads a sentence against. On Live the journey is never
   refreshed and leaves out only person-flagged stories
   ([A-86](../evidence/03-claim-index.md#a-86), [D-37](../evidence/05-discrepancies.md#d-37)).
9. **A plain-words error reaches the planner and writers.** Only Jev reads the originals
   ([A-87](../evidence/03-claim-index.md#a-87)).
10. **A model selects.** The planner chooses which Jev-matched stories each assertion cites, which
    extends [D-10](../evidence/05-discrepancies.md#d-10).
11. **No posting text, no summaries.** If the job holds no posting text, the planner never starts
    and the build writes no professional or role summary.
12. **A summary written by the red button is never reviewed.** Its citations come only from Jev on
    page view.
13. **The flow's own descriptions lag the code.** Module docstrings, a trace label and the
    capability registry still describe superseded summary behavior
    ([D-25](../evidence/05-discrepancies.md#d-25)), and some tests exercise summary code that no Live
    path calls ([D-26](../evidence/05-discrepancies.md#d-26)).

The controls that do exist are structural: the writers' inputs, story attribution by schema, the
summaries' cited-story enums and sentence counts, the database's role boundary, and the editor's
gate. Jev's readings of the summaries and the coverage review report anything they find; they never
repair it.

## Beta-only and superseded

| Work | Where it stands | Status | Claim |
|---|---|---|---|
| Polish experiment | Tried on Beta and closed on 2026-10-29. Its commits are in the history Live was rebuilt from but cancel out for bullets. The summary-prompt edits from the same series are on Live, though the closing commit said they stay on Beta ([D-38](../evidence/05-discrepancies.md#d-38)) | Experimental | [A-97](../evidence/03-claim-index.md#a-97) |
| Writing-quality measurements in the Editor verdict card | Beta only. **Owner:** *"Its for testing resume writing changes only"* (my words, commit `cac89cd`; [DEC-62](../product/07-decision-log.md#dec-62)) | Experimental | [A-98](../evidence/03-claim-index.md#a-98) |
| Optional subheadings in long roles (an opt-in box on Write the résumé) | Beta only | Experimental | [A-99](../evidence/03-claim-index.md#a-99) |
| Career themes, major outcomes, evidence timeline | Beta only. **Owner:** *"Leave the evidence timeline, career themes, and major outcomes off of live."* (my words, commit `88123b4`; [DEC-50](../product/07-decision-log.md#dec-50), [P-37](../evidence/03-claim-index.md#p-37)) | Experimental | [A-100](../evidence/03-claim-index.md#a-100) |
| Four-step summaries, then the summary tool | Replaced on 2026-10-28 by the positioning summaries (`ba6f332`, `2ac4c41`) and placed as written (`62d4327`). Both code paths remain with no caller | Superseded | [A-101](../evidence/03-claim-index.md#a-101) |
| Older writer with post-hoc checks | Replaced on Live by the recruiter-selects flow (`5d50ba7`); its summary writer is still used by Fix for résumés built before 2026-10-28 | Superseded | [A-20](../evidence/03-claim-index.md#a-20) |
| Selector told story strengths | Tried on Beta and reverted 23 minutes later. Both commits are in the history Live was rebuilt from, and they cancel out in the résumé flow | Experimental, reverted | [A-21](../evidence/03-claim-index.md#a-21) |

## Capability status

| Capability | Status | Claim |
|---|---|---|
| Recruiter-selects flow, for bullets | Verified | [A-11](../evidence/03-claim-index.md#a-11) |
| Bullet writer withheld from requirements | Limited (unit test + substring guard; declared check not executed) | [A-12](../evidence/03-claim-index.md#a-12) |
| Bullet → story attribution by schema | Verified | [A-13](../evidence/03-claim-index.md#a-13) |
| Shared-sentence de-duplication | Limited (thresholds set on one record) | [A-14](../evidence/03-claim-index.md#a-14) |
| Coverage review, report only | Verified | [A-15](../evidence/03-claim-index.md#a-15) |
| One editor pass with code gate | Verified | [A-16](../evidence/03-claim-index.md#a-16) |
| Fix (person-pressed repair; lines only on positioning-built résumés) | Verified; catch-and-repair by design | [A-17](../evidence/03-claim-index.md#a-17) |
| Printed-page fit | Verified | [A-18](../evidence/03-claim-index.md#a-18) |
| Person edits; saving starts no review | Verified | [A-19](../evidence/03-claim-index.md#a-19) |
| Older writer with post-hoc checks | Superseded | [A-20](../evidence/03-claim-index.md#a-20) |
| Selector told story strengths | Experimental, reverted | [A-21](../evidence/03-claim-index.md#a-21) |
| Professional summary from a supported positioning | Verified | [A-82](../evidence/03-claim-index.md#a-82) |
| Summary writers never given the posting | Limited (the brief carries its vocabulary; the guard compares line openings) | [A-83](../evidence/03-claim-index.md#a-83) |
| Summaries placed as written, findings shown | Limited (placement tested by source inspection) | [A-84](../evidence/03-claim-index.md#a-84) |
| Role summaries | Verified | [A-85](../evidence/03-claim-index.md#a-85) |
| Career journey written when none is saved | Limited (trigger tested by source inspection; never refreshed; [D-37](../evidence/05-discrepancies.md#d-37)) | [A-86](../evidence/03-claim-index.md#a-86) |
| Plain words, kept for reuse | Verified | [A-87](../evidence/03-claim-index.md#a-87) |
| Summaries beside the bullets, at low reasoning | Limited (order tested by source inspection; timing from one Beta posting) | [A-88](../evidence/03-claim-index.md#a-88) |
| Retries on provider failures; unread is not unsupported | Verified | [A-89](../evidence/03-claim-index.md#a-89) |
| Red button for a missing summary | Limited (template and source inspection; no route test) | [A-90](../evidence/03-claim-index.md#a-90) |
| Bullets as finished lines; shortened only past 220 characters | Verified | [A-91](../evidence/03-claim-index.md#a-91) |
| One writing rule in both bullet steps | Limited (prompt only) | [A-92](../evidence/03-claim-index.md#a-92) |
| Citations follow a line's words | Verified | [A-93](../evidence/03-claim-index.md#a-93) |
| Selection skips retired stories | Verified | [A-94](../evidence/03-claim-index.md#a-94) |
| An "Or" sentence stays with its requirement | Verified | [A-95](../evidence/03-claim-index.md#a-95) |
| Review page line numbers | Limited (template strings) | [A-96](../evidence/03-claim-index.md#a-96) |
| Polish experiment | Experimental, closed | [A-97](../evidence/03-claim-index.md#a-97) |
| Writing-quality measurements | Experimental (Beta only) | [A-98](../evidence/03-claim-index.md#a-98) |
| Optional subheadings | Experimental (Beta only) | [A-99](../evidence/03-claim-index.md#a-99) |
| Career themes, major outcomes, evidence timeline | Experimental (Beta only) | [A-100](../evidence/03-claim-index.md#a-100) |
| Four-step summaries and the summary tool | Superseded | [A-101](../evidence/03-claim-index.md#a-101) |
| Clause-level grounding on Live | Not run on Live: Verified (K-23); the grounding path Superseded (K-24) | [K-23](../evidence/03-claim-index.md#k-23), [K-24](../evidence/03-claim-index.md#k-24) |
