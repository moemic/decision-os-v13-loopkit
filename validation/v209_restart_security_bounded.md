# V209 — Bounded restart and security validation

## Scope, authority and source

Agent-selected work cap: 45 minutes from 00:39 UTC, with new repair starts
stopped by 01:09 UTC and the final 15 minutes reserved for verification,
saving, Git delivery/read-back and handoff. This is a self-imposed bound, not
a new owner authority grant or a usage-limit time estimate.

- Decision Owner: Shin.
- Authorized by the 2026-09-08 V209 task: isolated worktree/branch, bounded
  compression, read-only security inspection, at most two safe repairs, tests,
  commit, work-branch push and remote read-back.
- Not authorized: main direct writes, merge, release, external posting/sending,
  permission changes, secret movement. PR/main admission is one final Shin
  decision after implementation and verification.
- Fetched and live-advertised canonical base:
  `646012d470b53609951d48938fcc78f9c6e35686`.
- Repository: `shin4141/decision-os-v13-loopkit`.
- Work branch: `codex/v209-restart-security-bounded`.
- Main-Write Pause honored: the shared entrance checkout was on old branch
  `codex/13-108-stage-c-repository-identity-continuity` at
  `b73c90ae4dda8f46e2e383a0d00477ca0c0d7d78`, with unrelated untracked state.
  Its tracked and untracked contents were not changed.
- Existing worktrees were inventoried; no pruning, switching or cleanup of
  other worktrees occurred. The app's observed task list had no other active
  V13 task; this is a bounded snapshot, not a global concurrency guarantee.
- Separate detached verification worktree at the same fixed base prevents
  candidate edits from contaminating the full baseline run.

The current canonical Gate remains **HOLD**. This task's execution authority
comes from Shin's fresh request, not HOLD, old handoffs or passing tests.
The V209 first blocks are **CANDIDATE / NOT CURRENT** until separately admitted.
Source content identities are in [the manifest](v209_source_manifest.json).

## Selected repairs — two only

| ID | Selection and value | Boundary / rollback |
| --- | --- | --- |
| A | Explicit AGENTS-first bounded route, forward index in the existing 13-42 trajectory, paired admission candidate, exact source manifest and reviewer evidence. Resolves implicit ordering, dispersed causal decisions and stale candidate/main wording without deleting history. | Existing compression/handoff lifecycle; no parallel authority source. Remove only the V209 prefix/route through a separately authorized revert; preserve old bytes. |
| B | Minimize `decision-os check` CLI diagnostics using the existing `scan` origin sanitizer. Remote output uses credential-free identity, raw Git worktree stderr and unexpected exception bodies are withheld. | CLI output only; original inspection evidence, Gate, exit code and protected v0.1 source hashes stay intact. Reversible work-branch commit. |

No feature, dependency update, generic control layer, permission change or
unselected repair was introduced. Existing test assertions and protected
hashes were not changed. Four new safety tests cover observable behavior;
new restart checks bind real source identities, preserved history and links.

## Bounded security inspection

This is a current-tree and selected-path inspection, not a security
certification or an attack simulation. No live model, external send, exploit,
publication or secret transfer was used. Local unit fixtures use synthetic
sentinels only; their values are not operational credentials.

| Priority surface | Inspected evidence / bounded result |
| --- | --- |
| Secrets / personal data | 585 tracked paths: 584 UTF-8 texts scanned by private-key, provider/GitHub/AWS/Slack token, credential-URL and email patterns; one PNG visually inspected. No live-secret candidate found. Two credential-URL matches and email matches were synthetic test fixtures only. No tracked symlinks. Pattern coverage is not an exhaustive privacy proof. |
| GitHub Actions | No tracked `.github/workflows` files; four issue templates only. No workflow trigger/permission/action pinning finding in this tree. Remote Actions settings and branch protection were not audited. |
| Shell / subprocess | Production Python subprocess call sites enumerated by AST and reviewed by command role; no `shell=True`. Both tracked shell scripts inspected. Commands are explicit argument arrays or trusted manual command inputs; the compact wrapper intentionally executes the caller's command. No changed shell path. |
| Eval / deserialization / archives | No production `eval`, `exec`, pickle/YAML unsafe load, tar/zip extraction call found in the bounded source scan. JSON remains data; no new evaluator or extraction path. |
| Paths / symlinks | Scan exact-file reads, acceleration scope normalization, selective reconnect dir-fd reads, and Guided Intake/manual bridge stores inspected. Existing tests cover escape/glob/symlink rejection. The older AccelerationStore does not establish the same complete symlink-resistant storage boundary as newer stores; adversarial filesystem-race qualification remains unverified, with no exploit performed and no repair selected. |
| External input / authority | Claude supports one distinct mutation with exact replay recognition and rejects unsupported tools/scope escape; Codex launches an explicit executable with shell/hooks/plugins disabled; protected compound paths are mechanically bound in the controller. Static controls and fake-transport tests do not prove live model compliance. |
| Log / receipt exposure | A moderate confidentiality risk in the legacy check CLI was source-confirmed and reproduced using synthetic local fixtures: raw remote components and diagnostic bodies could reach output. Repair B closes those CLI routes. Server request logging is suppressed, session/CSRF tokens are generated and loopback-bound, and acceleration receipts store protocol fields rather than prompt bodies. |
| Send / publish / delete / merge | No default-open external-action route established in inspected surfaces. Claude's unsupported actions and scope escapes fail closed; Companion POST requires Host, Origin, session and CSRF before route handling. External service behavior and other applications were not exercised. |
| Lock / duplicate / stop | Acceleration append holds a process lock around verify-and-append; prior corruption/duplicate/race regressions remain. Guided Intake disallows read-to-write transaction upgrades. Controller STOP/terminal state and protected-path checks inspected. No new authority from a prior default or stop state was claimed. |
| Test/hash integrity | All original tests and protected hashes retained. New tests expose failures before repair; failed baseline is recorded without rebaseline. Full logs remain in ignored `.test-logs/`; only summaries and hashes are committed. |

### Residual security boundary

No critical or high-severity new vulnerability was established in this bounded
inspection. The CLI confidentiality repair is assessed as **moderate**: output
can become a disclosure surface when copied or logged; no actual leaked secret
was found. This classification is scoped and is not a repository-wide verdict.

The frozen legacy `decision_os.checks.inspect_repository` library API still
returns original raw evidence; callers bypassing the CLI must treat it as
private. Its legacy ambient Git-context behavior and complete storage-race
hardening were not repaired. Broad public sharing of arbitrary state-file
bodies is not made safe by the new diagnostic minimization. Any further repair
requires a separate bounded selection that preserves the protected evidence.

## Fresh-context reconstruction review

Exactly one reviewer, `fresh_reconstruction_review`, received no parent history
and no editing authority. It started at AGENTS, followed direct current-state,
proof/compression/handoff and causal evidence, inspected bounded Git ancestry
and live main advertisement, and returned findings only. It ran no tests and
performed no edits or Git mutations.

Initial reconstruction recovered canonical identity, HOLD/Shin, RED as latest
admitted work, 13-43/Value boundaries and no inferred next execution. Gaps:

1. Entry order and stopping point were implicit.
2. The current block retained “Admission Candidate” and authorization-time main
   wording that required Git reasoning to interpret.
3. Exact RED implementation/admission commits and its 8-path manifest were not
   directly named at the restart surface.
4. Failed admission assumptions and MISTAKEN pointers were dispersed.
5. The pair's 382,743 historical characters made unbounded reads expensive.
6. Intervening 13-204/206/207 records were not connected to the old trajectory.

The forward index addresses those gaps and preserves the review's UNKNOWNs:
no independent historical runtime replay, no complete capability inventory,
no live model measurement, no authority from the candidate branch.

Re-read outcome: no operating-state reconstruction blocker found. The reviewer
verified 23 manifest entries, 14 link occurrences and 8 RED paths from the
candidate surfaces. It found one accounting ambiguity: the original nine-item
denominator was not persisted. The R1–R9 register below was added, and the same
reviewer confirmed **9/9 retained** in one final bounded read. This confirms
retention and mapping only, not runtime safety, Git delivery or canonical
admission. The reviewer performed no edits, tests or fetch in either re-read.

## Verification record

- Secret scan: metadata-only pattern results; no credential value was emitted.
- Initial sandbox full run: interrupted before completion so the fixed baseline
  could be rerun with the local server/browser permissions required by the
  existing suite. Its partial output is not counted as the baseline.
- Repair B before implementation: 4 tests, 7 failing assertions/subtests exposed
  raw diagnostic/remote output. No external interaction.
- First post-fix draft: a newly written test incorrectly expected HOLD from the
  existing `complete` fixture, whose Gate is GO. The new assertion was corrected
  to preserve the fixture's actual Gate; no original test was modified.
- Repair B focused verification: 21 tests PASS, 29.267s, exit 0 (4 new safety
  tests plus existing check CLI and scan CLI suites).
- Full fixed main at `646012d470b53609951d48938fcc78f9c6e35686`: 1,552 tests,
  1 failure, 44 errors, 15 skips; 1014.468s, exit 1.
- Full candidate at `2909180092fa4876edcc47752bb0276de3b7641f`: 1,559 tests,
  1 failure, 44 errors, 15 skips; 1027.037s, exit 1.
- Failure identity sets: exactly equal, 45/45, with no added or removed failure.
  Error causes match: 41 `COMPRESSION_BEFORE_IDENTITY_INVALID` and 3
  `FIXED_ARTIFACT_IDENTITY_DRIFT`. All seven new tests pass. The one
  `test_compound_evidence_meter.CompoundEvidenceMeterCanonicalSurfaceTests.test_current_canonical_and_handoff_surfaces_are_consistent`
  failure retains the historical `None. Stop.` expectation. The bounded
  candidate action text differs as declared; that stale expectation is not repaired.
- Exact results, all failure identities and full-log SHA-256/byte counts:
  [verification receipt](v209_verification_receipt.json). Full logs remain in
  ignored `.test-logs/` in the named baseline/candidate worktrees.
- Candidate secret scan: 589 tracked paths; all five credential-URL matches
  are synthetic fixtures in three test files. No live-secret candidate or
  tracked symlink was detected.
- Admission, historical, RED and handoff regressions: 85 tests PASS,
  140.686s, exit 0. This includes generic admission 8, preserved historical 6,
  RED wording 5, handoff acceptance 56 and handoff CLI 10.
- Source manifest / link / history retention checks: 3 tests PASS, 2.376s.
  All 23 source identities and all 8 RED paths resolve; full old state and
  trajectory bytes remain unchanged. All 14 protected v0.1 blobs are unchanged.
- Implementation `2909180092fa4876edcc47752bb0276de3b7641f` was pushed to
  `origin/codex/v209-restart-security-bounded`. Exact remote-tip and all nine
  changed-file byte comparisons passed. The receipt binds that fixed witness.
- No tracked file changed during the candidate full suite. Subsequent changes
  are this validation record and its receipt only; the final metadata commit
  is resolved from the same work-branch ref and read back before task closure.
- Generated `.pyc` files from these two task-owned test worktrees were removed;
  source/history and full logs remain. Other worktrees were not cleaned.
- `git diff --check`: PASS. No PR, merge, main write or external send occurred.

The known baseline is 44 fixed creator-live identity errors and one current-state
consistency failure. Its previous observation is not repair authority. The
fresh fixed-main run, not that expectation, determines this report's result.

## Required restart-item register

The denominator is exactly Shin's nine V209 reconstruction questions. The ten
rows of the compact operating-state table also carry owner/completion/recheck
fields; they are not the retention denominator.

| ID | Original required question | Location in compact surface |
| --- | --- | --- |
| R1 | 現在のCanonical Sourceは何か | Current source / accepted state |
| R2 | 現在のGateは何か | Gate / owner |
| R3 | 直近で何が完了したか | Latest completion; causal spine 7–8 |
| R4 | なぜその判断へ変わったか | Causal spine and changed judgments |
| R5 | 何が未確認・未解決か | Unresolved; failed assumptions / uncertainty |
| R6 | 何をしてはいけないか | Not authorized; lifecycle boundaries |
| R7 | 次に許された一手は何か | Next authorized action; branch/main distinction |
| R8 | 根拠となるcommit、blob、receipt、ファイルはどこか | Exact evidence; source manifest; V209 validation record |
| R9 | 古い記録と現在状態の差は何か | Intervening main table; failed assumptions / lifecycle |

## Compression accounting

Source Surface: the two full baseline current-state/handoff files at
`646012d470b53609951d48938fcc78f9c6e35686`. Compact Surface: one candidate first fenced
block (the pair is duplicated for the admission joint) plus the new forward
trajectory index, before its historical delimiter.

- Full character count: 382,743.
- Compact character count: 13,295.
- Character reduction: 96.53%.
- Required restart denominator: the nine questions in Shin's V209 request;
  all nine are explicitly answered in the compact table/causal spine.
- Measurement status: MEASURED for characters only; retention is additionally
  checked through the one reviewer and source/link tests. No time/token or
  runtime equivalence measurement.
- Full old bytes remain preserved below the new boundaries. The normal AGENTS
  operating contract is common context and excluded from both counts.

## Preserved non-route discrepancy

`docs/ai_reading_order.md` names `docs/trajectory/V13_TRAJECTORY.md` in a
third-party-fork exclusion list, but that path is absent at the inspected
baseline. It is outside the active restart route. V209 binds the actual
existing validation trajectory and records the discrepancy without another repair.

## Canonical base report

```text
V12 State:
PASS — two bounded repairs verified; implementation branch delivery read back; final verification metadata is delivered on the same branch

V13 Next Loop Gate:
HOLD

Reason:
No new test failure; original history and hashes preserved. V209 remains a branch admission candidate.

Next Authorized Action:
Shin decides the one PR/main admission question; a receiver verifies the recorded branch delivery before relying on it; no new execution loop.

Not Authorized:
main direct write or unapproved merge; external action or authority expansion; fixture/hash weakening or unselected repair

Decision Packet Required:
yes — only for PR/main admission, using the fixed branch and this verification evidence

Decision Owner:
Shin

Completion Line:
Both implementation and validation metadata are committed, pushed and read back; canonical admission remains separately gated.
```

## Completion and re-entry

Branch completion requires: both selected repairs verified, full baseline
classified, exact sources/links/history checked, reviewer gaps recorded, clean
commit, authorized branch push and remote read-back. V209 does not claim main
admission; Shin's single remaining decision is whether this concrete branch may
proceed to PR/main admission through the normal review path.

After any approval, the executing AI owns normal checks and canonical read-back:
fetch origin/main, compare the exact paired first blocks and candidate content,
and verify both the reconstruction base and admitted change are ancestors.
Reopen on main drift, a changed approval boundary, an unresolved identity, or a
claim that needs unavailable runtime evidence. Otherwise preserve HOLD.
