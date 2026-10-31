# Architecture 08 — Interview coach

*Live `00eac95` (2026-10-31) · narrative: [Applications 05](../applications/05-research-and-interview-prep.md#interview-coach)*

One coaching turn runs from the posting down to the person. The side loops are what their next
message can start: a question about the role, told work, a dispute, or a debrief after an
interview.

```mermaid
flowchart TD
  POST[("Posting kept with the opportunity, the interview stage and what the person said about it")]:::store
  POST --> PKG["Package check in code: the record, roles, résumé, gaps, earlier coaching and company research refused before sending"]:::det
  PKG --> ROLE(["Role reading from the posting alone: purpose, problems, outcomes, 4 to 7 hiring signals, unknowns, what this interview listens for"]):::model
  ROLE --> RADMIT["Code admits it: stated only when its quote is in the posting; other quotes and unshown requirement numbers dropped; findings recorded"]:::det
  RADMIT --> RU[("Role reading kept per posting and stage; résumé and record writers never read it")]:::store
  RU --> ORDER{{"Jev orders the signals for this stage"}}:::jev
  ORDER --> CONTRACT["Answer contract per item, by code: what it must establish, length, at most 4 needs; a reason need draws on the employer's problem"]:::det
  CONTRACT --> PIECES{{"Jev per need: cosine top 8 pieces, keep at p 0.15 or above, at most 4"}}:::jev
  REC[("Career record")]:::store --> PIECES
  PIECES --> CLAIMS{{"Jev per sentence: direct and owned at 0.5 or above; related at 0.25, only after they say nothing is more direct"}}:::jev
  CLAIMS --> FEW["Code gives the fewest claims, the record first; told words only where no direct claim"]:::det
  FEW --> TURN(["Coaching turn, Claude Haiku: claims and told words only, never the record (requirement lines only if the role could not be read); shape held by the API"]):::model
  RU -.->|"the role reading, as focus"| TURN
  TURN --> LINE{{"Jev per draft line: do the cited words establish it, or for a reason line, is it a fair inference; 0.5"}}:::jev
  LINE --> COVER["Code writes the footnotes and what each need has: covered, missing, inferred, left out"]:::det
  COVER --> PERSON[/"Person reads the reply and the page, then answers, accepts, disputes or moves on"/]:::human
  PERSON --> HEARD{{"Jev: what the message means, read beside the coach's last message"}}:::jev
  HEARD -->|"answers or accepts"| CONTRACT

  HEARD -->|"about the role"| RQ["Code routes it to the role reading: no claims given, nothing of the record shown"]:::det
  RQ -->|"the role reading only"| TURN

  HEARD -->|"tells their work"| TOLD["Code keeps it for the need Jev reads it answering; offers their words as an addition when the call offered none"]:::det
  TOLD --> DUP{{"Jev: does a piece already say it all"}}:::jev
  DUP --> SAVE1[/"Person presses Save: evidence chat Save, Change Document"/]:::human
  SAVE1 --> REC

  HEARD -->|"a dispute"| DISP["Code finds the target: footnote number, quote, or a run of 4 or more of their words; out of every answer at once"]:::det
  DISP --> SAVE2[/"Person saves the change to that exact text, or the retirement"/]:::human
  SAVE2 --> REC

  HEARD -->|"how the interview went"| DEB{{"Jev: the outcome and the next interview's kind"}}:::jev
  DEB --> CARD["Code reads the dates and adds a card in their own words, one question last"]:::det
  CARD --> SAVE3[/"Person saves the interview card"/]:::human
  SAVE3 --> JC[("Recorded conversation: never career evidence")]:::store
  SAVE3 --> UP[("Upcoming card: the next interview's day")]:::store
  SAVE3 --> HIST["Code folds the preparation into the interview history; the next stage starts fresh"]:::det
  HIST --> CARRY{{"Jev: earlier told words against each open need; what shows a need is not asked again"}}:::jev
  CARRY --> CONTRACT

  TURN -.->|"their reason, practice answers, told work"| JS[("Their words for the opportunity: read again by its later preparations; never evidence")]:::store
  JS -.-> FEW
  PERSON -.->|"known gap D-31: approving a draft with an unsupported line starts a redraft"| TURN

  classDef det fill:#eef2f7,stroke:#475569,color:#111827
  classDef jev fill:#ede9fe,stroke:#6d28d9,color:#111827
  classDef model fill:#dbeafe,stroke:#1d4ed8,color:#111827
  classDef human fill:#dcfce7,stroke:#15803d,color:#111827
  classDef store fill:#fef9c3,stroke:#a16207,color:#111827
  classDef ext fill:#ffedd5,stroke:#c2410c,color:#111827
```

**What to notice:**
- **The posting itself reaches one call, and the record never reaches that call.** The role
  reading sees the posting alone, checked in code before sending ([A-62](../evidence/03-claim-index.md#a-62)). The
  coaching turn sees only the claims Jev chose and what the person told: never the record, and
  the posting's requirement lines only when the role could not be read ([A-63](../evidence/03-claim-index.md#a-63)).
- **Jev decides; the models read and write.** Signal order, claims, line checks and what a message
  means are Jev's ([A-66](../evidence/03-claim-index.md#a-66);
  [DEC-43](../product/07-decision-log.md#dec-43)). Footnotes and coverage are code's
  ([A-64](../evidence/03-claim-index.md#a-64)). A reason is checked as an inference, not as a fact
  ([A-68](../evidence/03-claim-index.md#a-68)).
- **Every change to the record is a person's Save.** Told work is offered by code
  ([A-65](../evidence/03-claim-index.md#a-65)); a dispute is resolved by code and offered as an
  exact-text change ([A-69](../evidence/03-claim-index.md#a-69)). No model call writes to the
  record, and the coaching call can propose only an addition, never a removal.
- **Two stores that are not evidence.** The interview card becomes a recorded conversation and an
  Upcoming date ([A-67](../evidence/03-claim-index.md#a-67),
  [A-72](../evidence/03-claim-index.md#a-72)). The person's words for the opportunity are kept with
  it and are never evidence; the application chat also reads stated reasons from every opportunity
  ([A-70](../evidence/03-claim-index.md#a-70), [D-34](../evidence/05-discrepancies.md#d-34)).
- **One contract for every stage.** The debrief loop returns to the same contract for the next
  interview, with the history as context ([A-67](../evidence/03-claim-index.md#a-67)).
- **One dotted edge is a known gap.** Approving a draft that has an unsupported line marks it stale
  and the coach writes it again: a check starting a rewrite
  ([D-31](../evidence/05-discrepancies.md#d-31)).

**Not shown, because no page links to them since `2c05495`:** the round preparation, Quick answers
and the walkthrough, which still answer at their addresses
([A-52](../evidence/03-claim-index.md#a-52)–[A-54](../evidence/03-claim-index.md#a-54),
[D-39](../evidence/05-discrepancies.md#d-39)).
