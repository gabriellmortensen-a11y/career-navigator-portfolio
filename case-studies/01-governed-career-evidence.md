# Case study 01 — Building a governed career evidence system

**One line:** I turned "AI that knows my career" from a pile of model-written notes into a record
where only the person makes something true, and the database refuses to let two jobs' evidence
compose into one claim.

**Audience notes.** *Product:* trust as a product requirement. *Technical:* where enforcement lives
(prompt, code, schema). *TPM:* how a principle survived three rebuilds.

---

## Customer problem and context

A tailored résumé or interview answer is only as good as what the system believes about the person.
In the first versions, that belief was assembled from three things:
- résumé imports;
- chat answers;
- model "enrichments" of both.

Two failures made the problem concrete.

1. **The system was quoting itself** (2026-08-13). An investigation of the step that turned raw
   evidence into canonical career statements found it was citing the context the system itself had
   put into the prompt, not the person's evidence.
   - **49.47%** of proposals cited a Career Story summary that the prompt supplied, not the person's
     evidence.
   - Only **19.65%** of proposals were admitted ([M-01](../evidence/04-metric-ledger.md#m-01),
     [M-02](../evidence/04-metric-ledger.md#m-02)).
2. **Requirements were being established by combining unrelated jobs** (2026-09-24). A requirement
   was satisfied by stitching together evidence from two or three unrelated roles. Every piece was
   true. The combined claim was not true of any single piece of work. The system was manufacturing
   evidence ([H-07](../evidence/03-claim-index.md#h-07)).

For a job seeker, either failure is worse than a weak résumé. It is a résumé they can't defend in an
interview.

## My ownership

I set the rules and made the calls. Claude Code agents implemented, measured and reported. I wrote
none of the code. Specifically, I:
- Decided that approval is a person's act and, later, *which* acts count as approval: an explicit
  Save, not a background "make findable" press.
- Diagnosed the cross-role problem from using the product on real postings, and asked for answers
  from one coherent body of work.
- Retired a per-résumé human acceptance gate, because it assigned to me work the system is supposed
  to do ([H-09](../evidence/03-claim-index.md#h-09)).
- Required the chat to confirm the role before saving, even when it thinks it knows.
- Reversed my own earlier rule that flagged stories stay usable, once a résumé proved why
  ([K-17](../evidence/03-claim-index.md#k-17)).

## Constraints

- **Built for me first, then for others.** The record had to be multi-tenant without leaking.
- **Cheap enough to run on every change.** Per-piece model judging was too slow and too costly.
- **The record grows in fragments.** The rules had to compose fragments without inventing
  connections.
- **Agents revive old rules.** Anything that lived only in prose got reintroduced or forgotten
  ([H-12](../evidence/03-claim-index.md#h-12)).

## Alternatives considered

| Option | Why not |
|---|---|
| Let the model extract and store atomic claims automatically | Turning a line into a claim with a subject, scope and figure is a *derivation*, and whether it says what the person meant is theirs to say. Replaced by person-ticked verbatim spans ([K-10](../evidence/03-claim-index.md#k-10)) |
| Human approval of every derived item (capabilities, indexes) | It would defeat the purpose of automatically making approved evidence findable. The boundary is *use as evidence*, not derivation ([H-18](../evidence/03-claim-index.md#h-18)) |
| Keep the role boundary as a retrieval preference | Preferences get relaxed by the next prompt or agent. It moved into the schema |
| Split stories back into fragments for precision | Measured over 63 jobs: 20 strong requirements became light and 3 stronger. Rejected ([K-07](../evidence/03-claim-index.md#k-07)) |

## Decision and reasoning

**Put the rules where they can't be argued with.**

| Rule | Where it lives |
|---|---|
| Only a person makes evidence authoritative | One writer (Change Documents), a deterministic contract frozen at proposal, refusals kept with reasons ([K-10](../evidence/03-claim-index.md#k-10)) |
| A role owns what may compose | PostgreSQL composite foreign keys on evidence and résumé bullets ([K-01](../evidence/03-claim-index.md#k-01), [K-02](../evidence/03-claim-index.md#k-02)) |
| Accounts never see each other | Forced row-level security; a runtime role that owns nothing ([P-12](../evidence/03-claim-index.md#p-12)) |
| A conclusion is not a fact | Code-applied provenance labels and one byte-identical rule in nine coaching prompts ([K-20](../evidence/03-claim-index.md#k-20)) |

When the system was extracted into a clean application (2026-10-03), these became the two "authority
boundaries" of the new codebase. The governing instruction was to "migrate only capabilities and data
whose authority and purpose are understood" ([P-30](../evidence/03-claim-index.md#p-30)).

## Implementation

- **Change Documents.** Every addition, composition or retirement is a document. Admission is
  checked in code: required fields, spans that are verbatim substrings, limits. The contract's
  version and hash are frozen at proposal.
- **Stories.** Fragments of the same work within one role are glued into stories. Embeddings
  shortlist the pairs and Jev answers "same piece of work?". The story is assembled from the
  fragments' own words ([K-06](../evidence/03-claim-index.md#k-06)).
- **Corrections by code.** The chat proposes only *wrong → right*. Code builds the corrected story
  and retires the old one with a link ([K-15](../evidence/03-claim-index.md#k-15)).
- **Duplicates handled conservatively.** Only exact copies are removed. "Already on the record" is
  decided by a phrase test, then Jev ([K-16](../evidence/03-claim-index.md#k-16)).
- **Flags.** A deterministic reading flags belief-statements without an instance. The person
  overrides it either way. Flagged stories never reach a résumé or a shared link.

## Verification

- **Schema-level tests.** PostgreSQL raises on a mixed-role link. A cross-role bullet citation is
  refused. Same-role composition still works.
- **A 20-test tenancy suite.** A stranger cannot read or write. The runtime role is not a superuser.
  Every table is owned or declared shared.
- **QC-1 reproduced independently.** A separate observability tool reproduced the contamination and
  yield rates to the hundredth of a percent (2026-08-13). The counts did not reproduce, which is why
  the rates lead.
- **Re-checked for this portfolio (2026-10-25).** The QC-1 figures were re-summed at both sources;
  the role key was recomputed against a Live row; the importer's parser was run on this portfolio's
  own evidence file.

## Results

| Result | Evidence |
|---|---|
| Prompt-sourced citations fell from **49.47% → 3.62%** of proposals; admission yield rose **19.65% → 45.65%** | [M-01](../evidence/04-metric-ledger.md#m-01), [M-02](../evidence/04-metric-ledger.md#m-02) (one run per arm, 8 projections) |
| A mixed-role claim is now **unwritable**, not just unlikely | [K-01](../evidence/03-claim-index.md#k-01) |
| Before the bullet constraint shipped, 0 of 12,440 candidates, 46 selections and 34 bullets disagreed on role, so the constraint codified current behaviour ([M-54](../evidence/04-metric-ledger.md#m-54)) | [K-02](../evidence/03-claim-index.md#k-02) |
| Every entry path ends in a person's press, with two named exceptions | [Knowledge 02](../knowledge/02-admission-and-acceptance.md#every-way-in) |

## Limitations

These are open:
- **Story composition** writes without a person's confirmation. It adds no claims and is reversible,
  but it is not directly tested.
- **A brought résumé** is recorded on "Accept as is" without the proposal page its importer promises
  ([D-05](../evidence/05-discrepancies.md#d-05)).
- **The single-writer test** is a text scan with an allowlist, not a structural guarantee
  ([K-11](../evidence/03-claim-index.md#k-11)).
- **Restoring retired evidence** is described in the contract and not implemented
  ([K-18](../evidence/03-claim-index.md#k-18)).
- **Model selection still happens in places.** Concept indexing is a model choosing from a shortlist
  ([P-05](../evidence/03-claim-index.md#p-05)).

## What changed after learning from use

1. **From prompts to schema.** Each time a rule lived only in instructions, it was eventually broken
   or revived. The role boundary moved into the database because of that pattern, not in anticipation
   of it.
2. **From "approve everything" to "approve what becomes true".** I stopped approving per résumé and
   per derived index. I kept approval where a fact enters the record. Approval moved to the point
   where it actually changes what is true.
3. **From trusting scripts to trusting the database.** On 2026-10-05, while database-enforced
   tenancy was being built, an agent's cleanup script connected as the schema owner (which bypasses
   row-level security) and deleted 17,183 rows across 50 tables ([M-55](../evidence/04-metric-ledger.md#m-55)). The same change forced row-level
   security with a non-owner runtime role, required an explicit account for imports, and documented
   the lost measurement artifacts as lost rather than re-creating them ([H-17](../evidence/03-claim-index.md#h-17)).
4. **From the model's guess to the person's confirmation.** After the chat filed an addition under
   its own guess of the role, Save started filing additions only under the role shown on the card. The
   guess is preselected and marked, so the person sees it and can change it ([K-13](../evidence/03-claim-index.md#k-13)).
