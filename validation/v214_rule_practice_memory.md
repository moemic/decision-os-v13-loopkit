# V214 — Rule practice memory and revision path

Status: validated implementation and admission candidate; PR/main delivery is pending.

## Scope and starting point

- Authorization: Shin's V214 request covers design, implementation, validation,
  commit/push, PR/review response, main merge, remote read-back and routine cleanup.
  No release/tag/SNS, Companion work, new model/harness, bulk migration, automatic
  loop, paper rewrite or expansion of ♻️ selection.
- Canonical repository: `shin4141/decision-os-v13-loopkit`.
- Fetched base: `d0182a1e917e800aefe50f95cd4d400b1fa272fd`.
- Work branch: `codex/v214-rule-practice-memory`; isolated clean worktree from that base.
- Number audit: no V214/13-214 path or content in the inspected V13 main tree;
  no prior matching local V13 branch before creation. The parent workspace has
  a `V214-shin4141.github.io` checkout whose remote is a different repository.
  This task uses descriptive V13-local names and touches none of that record.
- Repository protection read: main branch protection returned **404 Branch not
  protected**, rulesets returned `[]`; recent PR #162 had no required checks or
  reviews. These are observations, not permission to bypass later protections.
  Recheck the actual PR before merge; do not use admin/force or edit settings.

## Existing structure and the missing joint

| Existing source inspected | Reused behavior / limit |
| --- | --- |
| AGENTS.md and the first current-signal/handoff blocks | Bounded initial read, conditional deep read, current authority, paired admission, immutable historical suffix and remote read-back |
| docs/field_note_lifecycle.md; FN039 | Existing lifecycle and evidence-based promotion; no use-count promotion |
| FN125 and its operational validation | Already Canon-promoted, repeatedly routed for continuation; exact artifact proof, context-dependent exceptions and forward-only downgrade |
| FN024; docs/roadmap_anchors.md | Preserve Human Seat, Carrier and re-entry; improve later operating conditions toward Human-Seat-Preserving Autonomous Compounding |
| FN124; FN144 | Runtime compliance remains a limit; memory is not authority. FN144 remains verification pending, not newly promoted |
| docs/field_notes_lite_v0_1_design.md and Companion maturity/reconnect code | Exact identity, activation and real-use distinctions exist, but are tied to Companion/lower-model runs. Reuse the distinctions, do not reopen that runtime or change its ledger |
| validation/ and the current-state admission tests | Existing evidence storage and canonical delivery checks |

Missing: one ordinary rule's current version and short applicability card did
not link a real application, a reason to maintain/revise, and unresolved practice
attention back into the next default read. The bounded delta adds that joint.
No new Field Note is needed and the FN125 Canon bytes remain unchanged.

## Selection from the current state and Aspire

FN125 is already required during repository continuation and has previous
operational validation. V214 itself requires a real continuation through a
workspace with old checkouts, making its result observable without inventing
another job. Strengthening this path improves later re-entry while keeping
proof recovery AI-owned and authority at the Human Seat. A broad ♻️ selection
change and a Companion maturity extension would expand the authorized slice.

## Real use

Stable execution identity:
`shin4141/decision-os-v13-loopkit:v214-rule-practice-memory:continuation`.

The parent directory had no committed repository state. The identified V13
checkout was on a historical branch at `b73c90a`, with existing untracked local
work. The closing AI did not modify that work or accept its old handoff as
current. It established the exact origin, fetched main (routine sandbox network
access recovery), read current AGENTS and the first pair, and created the
dedicated worktree at `d0182a1…`.

The existing `admit_from_fetched_origin_main` helper then accepted that exact
pair and confirmed reconstruction base `42e406e858b05b6b8aff5cc6669cf10ad506b424`
as an ancestor. [Machine-readable observation](v214_rule_practice_reentry.json)
records the pair digest, rule digest and clean-worktree result before edits.
It was produced by reading the actual fetched ref and working tree, not by a
synthetic fixture. The prior source identities remain reproducible in Git.

The actual decision was **Artifact Provenance Guard**. No specific prior-chat
judgment was needed because the user supplied current task authority and the
required state was persisted. The observed outcome was an admitted starting
state and bounded implementation from it. No claim is made that a hypothetical
mistake was certainly prevented.

Burden was not zero: the first broad search and an old handoff read produced
unnecessarily large output before switching to the bounded route. That friction
is retained in the practice record. Measured time/cost savings, user burden and
general causal effectiveness are unknown.

Assessment: **maintain fn125-v1 for this artifact-sufficient condition**. The
existing minimum-proof principle resolved the observed ambiguity. Excessive
reading is reason to follow that principle and use a lighter access path, not
evidence to expand authority or rewrite the rule. Reassess if a later use admits
the wrong source, needs unpersisted judgment, hides ambiguity or repeats needless
proof burden. One applied execution is recorded; further read-backs and
amendments in this same continuation are not independent experiences.

## Design and claim boundary

- Top: one generated card reached by AGENTS §2/§6; current rule, conditions,
  exceptions, version, attention, latest bounded judgment and deep references.
- Lower: one append-only JSON ledger referencing existing validation records.
  Fixed Git source + digest bind the old rule; amendments preserve prior entries.
- A small local script validates and renders. It does not infer conclusions,
  activate candidate changes, run evidence text or grant authority.
- `--base` protects previous version/entry objects. Same execution amendments
  require `supersedes` and count once. Significant issues survive later
  maintenance or version switches unless explicitly resolved with observed
  evidence. The card check rejects a stale projection.
- Real-use and unknown-result counts are descriptive, not success/effect meters.
  No threshold or automatic promotion; tests remain outside the saved ledger.
- User procedure distinguishes operational maintenance in existing authority
  from purpose/authority/protection changes requiring the Decision Owner.

## Verification

Results on the V214 candidate:

- `git diff --check`: PASS.
- 99 tests PASS in 106.939s: practice memory (initial 8), generic current-state
  admission, 13-42/13-43 historical regressions, V209 preservation, handoff
  acceptance, public onboarding and Workspace Health RED routing.
- After adding the stale-card/source-drift CLI test and making warning evidence
  clickable, all 9 final practice-memory tests PASS in 1.309s. The unchanged
  regression modules were not repeated without a new reason.
- Synthetic maintenance, counterexample/condition mismatch, unknown outcome,
  reference/connection exclusion, same-execution amendment, historical version
  preservation, unresolved warning carry-forward, explicit resolution and
  stale-card rejection are covered. Synthetic cases remain only in test memory
  and a temporary clone; production has one real execution, not ten or twenty.
- Source digest and the original fetched pair digest reproduce from fixed Git
  objects. Both current-state files retain their entire pre-V214 bytes as suffixes.
  FN125 itself is byte-identical to the starting main.
- All relative links and anchors in the new card, procedure and this record
  resolve. The existing promotion and historical tests were not weakened.

Reproduce:

```console
python3 -B scripts/rule_practice.py --check --base origin/main
python3 -B scripts/compact_test_output.py --log .test-logs/v214-focused.log -- \
  python3 -B -m unittest tests.test_rule_practice tests.test_current_state_admission \
  tests.test_13_42_13_43_historical_regression tests.test_v209_restart_surface \
  tests.test_decision_os_handoff_acceptance tests.test_external_intelligence_onboarding \
  tests.test_workspace_health_red_routing
```

Local complete output is retained in `.test-logs/v214-focused.log` and
`.test-logs/v214-practice-final.log`; the final command now includes 100 distinct
test cases. The known unrelated full legacy creator-live/fixed-identity baseline
was not rerun or repaired, and its claims are not upgraded.

### Next-read connection check

Before delivery, the executing AI read the generated card through the normal
FN125 entry. It recovered `fn125-v1`, the artifact-sufficient condition, the
exceptions, no recorded open issue, **maintain** and the unmeasured limits without
loading old current-state histories. Following the named lower record recovered
the stable execution ID and the exact main/pair/source evidence. A fresh local
process checked the same committed projection and source links.

The card is 26 lines / 2,379 characters; the full existing FN125 is 12,652
characters. This is character-count evidence only, not time/token/cost savings.
Card SHA-256: `7a2080e06e96dd23d894241babe9f58c5e0e4cd06b834c01407f9d2b8af95686`.
Pair SHA-256: `9e335dcf3a23143d69440d1b1f2140570aa8af2cd310370dda3a97e438ec4a75`.
This retrieval is a connection check inside the same task, not a second
independent real use or fresh-model trial.

### Review boundary

The executing AI reviewed changed surfaces for scope, false success claims,
counting, warning loss, history preservation and authority changes. One draft
test would have frozen the current FN125 bytes forever; it was corrected before
commit to preserve the original bound version while permitting a future
authorized new version. This is self-review plus deterministic regression
evidence, not an independent reviewer endorsement.

## Delivery and restart

Pending: commit, push, PR, final checks/review, merge and fresh remote read-back.
No canonical completion is claimed by merely saving these files.

After delivery, start with the admitted paired block and FN125 current card.
Reopen a lower record for a relevant warning, an applicability mismatch, source
identity drift, uncertain authority, or a requested explanation of the decision.
No new loop is authorized by the practice record.

Unconfirmed: other rule families, destination-identity real use in this task,
external reader adoption, independent runtime obedience, general benefits and
all prior unresolved fixed-identity/runtime baselines. This bounded task does
not upgrade those claims.
