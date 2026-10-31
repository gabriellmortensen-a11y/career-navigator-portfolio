# Product 06 — Operations and privacy

*Product 4.1 · describes Live `00eac95` (2026-10-31)*

## Release process

```text
change on main ─► full local suite ─► Beta deploy ─► product owner uses it on Beta ─► approved commits
                                                                                     cherry-picked onto Live's own
                                                                                     branch for the release
                                                     full suite on that exact code ─► Live deploy (--confirm)
```

| Rule | Since | Why |
|---|---|---|
| Every change goes to Beta first; Live only after I've looked at it on Beta | 2026-10-14 | That day, several direct-to-Live changes broke things I found while using Live |
| Full suite on the exact Live code before any Live deploy | 2026-10-19 | I had asked for "no suite" pushes for speed, then reversed it |
| Beta and Live run the same code and schema; only the labs differ (replaced on 2026-10-28 by the next row) | 2026-10-21 → 10-27 | I wanted parity between the two, so that one test run is enough |
| Live is its own line: rebuilt from Beta's approved commits by cherry-pick, with its own copies of migrations, and without the evidence timeline, career themes and major outcomes | 2026-10-28 | "Leave the evidence timeline, career themes, and major outcomes off of live." (my words, `88123b4`; [P-37](../evidence/03-claim-index.md#p-37), [DEC-50](07-decision-log.md#dec-50)) |
| Live runs from a branch of approved commits: `live-approved` (last pushed 2026-10-25), and from 2026-10-28 a branch per release (`live-chat-reads`, `live-summaries`, `live-kept`) | 2026-10-14 | Main can hold Beta work I haven't approved ([P-11](../evidence/03-claim-index.md#p-11)) |

`ship.sh` encodes the first half: a clean tree, the full suite (it refuses on failure), push, then a
Beta deploy. It stops there: "the step between Beta and Live is a person opening the product"
([P-11](../evidence/03-claim-index.md#p-11)).

## Deploy

`deploy.sh` runs these steps ([P-10](../evidence/03-claim-index.md#p-10)):
1. Checks out a **named commit** on the server. It never syncs a laptop folder, which "is how an
   unrelated half-finished change once reached a production server".
2. Backs up the database before every deploy.
3. Runs migrations before the restart. Migrations are additive.
4. **Drains** running background work for up to 5 minutes. Unfinished work resumes in the next
   runner.
5. Optionally publishes the governed policy documents with the service stopped, after a snapshot
   of the versions in force. All documents publish, or none do.
6. Restarts web and runner, probes the site, and **rolls back automatically** on failure: documents
   first, then code.

Limits: the database is not restored automatically (the restore command is printed). The shell
script itself is untested; only the document publish and restore is.

## Background work

- **Accepting work.** Accepted work is a database row committed before the request answers. It used
  to be an in-memory task: on 2026-10-08 a deploy restarted Live 3 seconds after a posting was
  added, and its indexing vanished while the row kept saying "running".
- **Running work.** Rows are claimed with `SKIP LOCKED`, heartbeat every 20 s, and are recovered
  after interruption ([P-09](../evidence/03-claim-index.md#p-09)).
- **A separate runner process.** Since 2026-10-19 a separate, lower-priority process runs the work.
  Before that, a résumé preparation running in the web process made pages take 4–6 s instead of
  about 1 s on a 2-core host ([M-29](../evidence/04-metric-ledger.md#m-29)).
- **A visible queue.** Each person gets at most two model jobs at a time, and the queue is visible.
- **New kinds of work** since Product 4.0 use the same mechanism: writing a missing résumé summary,
  refreshing a GitHub repository, suggesting Growth plans, and recounting an opportunity's label
  ([P-09](../evidence/03-claim-index.md#p-09)).

## Monitoring

- **Spend and failures:** by day, stage, model and account, plus the latest failures.
- **Alerts every 15 minutes:** failed or abandoned work, repeated failed calls, overdue work, daily
  spend over a threshold, and host health. The owner is emailed when the set of problems changes
  ([P-20](../evidence/03-claim-index.md#p-20)).
- **Request logs:** one line per request carrying a request id and account id, with a warning at
  ≥ 2 s; a 500 page shows its request reference.
- **`/healthz`:** answers 503 when the database can't be read.

## Tenancy and privacy

**Separation is enforced by the database, not by queries** ([P-12](../evidence/03-claim-index.md#p-12)):
- Forced row-level security on every owned table.
- Each row's account defaults from the session setting, so an insert with no account fails.
- The runtime role is neither owner nor superuser. Unset means no rows.
- Background jobs re-declare the account they work for.

| Data | Handling |
|---|---|
| Prompts | Not stored. Only a hash and sizes per call; a past prompt can be rebuilt by re-running the stage's code with sending disabled |
| Model outputs | Stored per call, protected by row-level security |
| Search providers | Rows keep the query and a result count, never pages or keys |
| Job-discovery queries | Built from roles, kinds of work and places; health, disability and accommodation terms are dropped, and the person is told |
| Hosted job index | Never sent résumé or evidence text; results never shared across accounts |
| Living résumé links (renamed from shared conversation links, 2026-10-31) | Token stored as a digest; scope computed on the server before retrieval; per-link spend cap; draft until activated; revocable. The scope also covers the profile's education and certifications, never a credential's number or a note, and the portfolio artifacts the owner made public ([A-55](../evidence/03-claim-index.md#a-55), [A-118](../evidence/03-claim-index.md#a-118)). The owner sees what each visitor asked and how each answer was derived ([A-117](../evidence/03-claim-index.md#a-117)) |
| GitHub portfolio | Public repositories only, read through GitHub's public API with no token stored. Nothing is read until the owner approves a repository; each artifact stays private until they make it public ("Make all public" does it for one repository at once, each noted in its history). Files that could hold secrets are never fetched, and a section that looks like one is never kept ([A-120](../evidence/03-claim-index.md#a-120), [P-34](../evidence/03-claim-index.md#p-34)). Repository text reaches a model only as a labeled, untrusted block ([P-35](../evidence/03-claim-index.md#p-35)). Links to evidence are suggested by Jev and decided by the owner ([K-34](../evidence/03-claim-index.md#k-34)). Disconnecting stops all serving at once |
| Career Chat reads | Read-only operations under the same row-level security as every page; a test checks nothing is written. Never read, by having no operation that reads them: secrets, security records, raw provider payloads, prompts, other accounts, admin data, a model's or Jev's working, saved answers about work authorization, sponsorship, age, pay, logistics and self-identification, and connections' contact details ([A-102](../evidence/03-claim-index.md#a-102), [P-33](../evidence/03-claim-index.md#p-33)). The document listing coverage describes Beta-only pages ([D-29](../evidence/05-discrepancies.md#d-29)) |
| ChatGPT connector | Read-only tools; audit keeps names, ids, times and sizes, never arguments or answers |
| API keys | Read from the environment or key files outside the repository; setter scripts read them with hidden input; never logged |
| Your data | Settings › Your data: export, delete by category, close account |

**Open findings.** This review found two security and privacy findings that are not yet fixed. Their
details are withheld from this public version until they are fixed
([D-02](../evidence/05-discrepancies.md#d-02), [D-17](../evidence/05-discrepancies.md#d-17)).

## Incidents and what changed

| Date | Incident | Change at the source |
|---|---|---|
| 2026-09-28 (earlier build) | A deploy override skipped the release proof and shipped untested code | Removed after 26 hours: "never push to Live without the tests being complete, without my approval" ([H-11](../evidence/03-claim-index.md#h-11)) |
| 2026-10-05 | While tenancy was being built, an agent's cleanup script, connected as the schema owner (which bypasses row-level security), deleted 17,183 rows across 50 tables | Forced RLS, a non-owner runtime role, account-stamped defaults, explicit-account imports. Lost measurement artifacts documented, not re-created ([H-17](../evidence/03-claim-index.md#h-17)) |
| 2026-10-08 | Accepted work vanished on restart | Durable operations |
| 2026-10-14 | Several direct-to-Live changes broke things in use | Beta first; Live from approved commits |
| 2026-10-14 | Jev calls recorded at $0, some calls unrecorded, failures erased by rollbacks | Every transport records itself; Jev priced; failures written on their own transaction ([P-18](../evidence/03-claim-index.md#p-18)) |
| 2026-10-19 | Pages slow while background work ran | Separate runner process |
