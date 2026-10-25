# Evidence 01 — The baseline

**The baseline this portfolio starts from is the 2026-09-30 case-study source package.** It is a
private retrospective of the earlier build, built against that build's commit `38f4bbf` (2026-09-29).
Behind it sits the July 2026 layered documentation. Everything since is in [EVOLUTION](../EVOLUTION.md).

## What the baseline is

| Item | Identity |
|---|---|
| **Earlier portfolio / retrospective** | The case-study source package (`docs/case-study/` in the earlier build's private working copy). Built 2026-09-30, read-only. A committed copy lives on a local branch (`case-study-source`, last commit `39e5e2f`, 2026-09-30 14:56) |
| **System it describes** | The earlier build, "beta4", at commit **`38f4bbf`** (2026-09-29 16:27 PT). 621 commits since 2026-08-06; the private repository was named for its original product name |
| **Also covers** | The July predecessor repository (last commit `ba28bf1`, 2026-08-06; 112 commits; never deployed) and a short-lived observability side project (8 commits, 2026-08-13, last `dd881b7`) |
| **Earliest product documents** | Knowledge layer **v2.2**, Product layer **v3.0** and Application layer **v3.0**, all stamped 2026-07-08, committed into the predecessor on 2026-07-29/31 ([H-01](03-claim-index.md#h-01)) |
| **Contents** | A fact ledger of 705 facts, each classified (616 proven, 42 strongly implied, 42 needing the owner, 5 owner-supplied) with a publish status. Also a quantitative ledger of 231 numbers, a chronology, generations G0–G11 of the architecture, 45 failed approaches and reversals, a contradiction register (C-1…C-11), a publication-risk audit (49 findings), a case-study skeleton and diagrams A–H |
| **Owner accounts** | GAB-001 (division of labour: I wrote no code), GAB-002 (delegated selection), GAB-003 (a derived index is not evidence), GAB-004 (how Bounded Fit became the product), GAB-005 (why the product exists) |

## How this portfolio uses it

- **Historical claims** (`H-xx` in the [claim index](03-claim-index.md)) cite the package's fact-ledger
  IDs. Only facts marked publishable (SAFE, or SANITIZE in their sanitized form) are used.
- **No PENDING or PRIVATE fact is used.** In particular, numbers derived from the earlier build's Live
  users wait on the owner's consent decision (NG-08) and are omitted: whole-history spend, account
  counts, Live timings and the first real-user defect.
- **The package's publication rules are applied to this repository:**
  - no career-record text;
  - no employer or job-target names;
  - no infrastructure details;
  - no session links;
  - no screenshots of real records;
  - no exact spend limits.
- **The baseline's "current" is historical.** Everything the package calls current describes
  2026-09-29. The application was re-extracted on 2026-10-03, so none of the package's current-state
  diagrams (A, C, H) describe today's system.

## Spot-checks of the baseline (2026-10-25)

| Check | Result |
|---|---|
| Commit hashes cited for key historical claims exist (`git cat-file -e`) | 113 of 113, across the three earlier repositories |
| Quoted numbers and phrases in 25 key commit bodies match | 73 of 73 (four after normalising line wraps) |
| QC-1 contamination and yield re-summed at both sources (commit body; observability fixture) | Match: 141/285 = 49.47% → 5/138 = 3.62%; 56/285 = 19.65% → 63/138 = 45.65% ([M-01](04-metric-ledger.md#m-01)) |
| Census figures (commits, trailers, guard counts) | As stated |

## Limitations of the baseline, stated

1. **The newest package content is uncommitted.** GAB-005 and one current-state fact exist only in
   the untracked working copy (705 facts vs 703 committed).
2. **The working copy has introduced one error.** A recorded misspelling defect was "corrected" in
   two files. The committed copy is right.
3. **Five quantitative-ledger rows are looser than the fact ledger.** The fact ledger is stricter, and
   this portfolio follows it.
4. **The three-layer framing is verified in git but is not a ledger fact.** This portfolio describes
   only the layers' names, versions, dates and purposes, never their contents (which are private
   career records).
5. **The last three days of the earlier build are outside it.** The 23 commits after `38f4bbf`
   (2026-09-30 → 10-02) fall outside the package. The experiments that defined the extraction
   (V2-1033…1061) were never committed and have no hashes. Their only trace is the extraction itself.
6. **Live deploy dates before 2026-10-14 are not in git.** Before that date "Live" rests on commit
   wording or project notes. From then on it rests on the push history of the branch Live deploys
   from.

## The bridge from baseline to current

```text
beta4 38f4bbf (2026-09-29, baseline) ─► 23 commits ─► beta4 6a9ab0c (2026-10-02, last)
        └─ uncommitted experiments V2-1033…1061 ─► extraction 0a83529 (2026-10-03, new repository)
              ─► 683 non-merge commits ─► Live 7322289 (2026-10-24)  ≡ Beta 2a5f749 (identical tree)
```
