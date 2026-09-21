# README personal-hub first view — publication record

Date: 2026-09-21 JST

## Identity and authority

- Repository: `https://github.com/shin4141/decision-os-v13-loopkit.git`
- Reconstruction base: `382ac253f90de74a3f103d9040f6ddb10748d2de`
- Work branch: `codex/readme-first-view-hub`
- Decision Owner: Shin
- Authorized delivery: README reorganization, related tests and current-state
  records, push, PR, merge, public UI read-back, and safe return to the ordinary
  `v13-main-ready` worktree.
- Excluded: feature or permission changes, repeat V219/V220 trials, SNS or
  external contact, and claims of observed reader effect.

## Observed problem and bounded objective

The baseline README had 1,225 source lines. Its normally visible path placed
conversation recycle, practice memory, External Intelligence explanation and
many product/evidence surfaces before or around the personal-hub entry. Shin
reported the length and mixed information as a burden. Actual abandonment,
completion time and downstream effect were not measured.

The bounded change makes `Start your own hub` the first primary heading, keeps
the minimum decision conditions visible, and makes alternate trials and depth
available through two closed details blocks. It changes information
architecture, not feature behavior, evidence meaning, permission, or Gate.

## Same-method visible-word comparison

The baseline and candidate use the same deterministic method:

1. read the whole Markdown source;
2. exclude lines inside `<details> ... </details>` because those blocks are
   closed in the initial GitHub rendering;
3. keep code-block text because it is initially visible;
4. replace Markdown links with their labels, remove badge images and HTML tags;
5. count English alphanumeric/hyphen/apostrophe tokens and Japanese runs with
   the same regular expression.

| Version | Source lines | Normally visible words |
|---|---:|---:|
| fetched `origin/main` at `382ac253` | 1,225 | 6,684 |
| candidate | 281 | 353 |
| change | -944 | -6,331 (-94.7%) |

This is a display-volume measurement, not evidence of lower abandonment,
faster setup, lower token use, or improved work quality.

## Initial view retained

- short statement of purpose;
- use with the reader's purpose and rules while keeping author knowledge as
  reference rather than inherited authority;
- Japanese start link;
- writable-local environment, branch/worktree, local instruction/handoff
  mutation, diff review, commit, owner setup and job-input requirements;
- public clone command and optional-Fork boundary;
- the published Personal Hub Roundtrip link;
- one short saved → selected → applied example, detailed worked example and
  V219/V220 evidence boundary;
- public/private/unpublished availability boundary; and
- compact prototype status.

## Folded or linked depth

The first closed block contains inspection-first, Try one line first, Ask your
AI first, standalone conversation `♻️`, and practice-memory routes. The second
closed block routes completion and handoff, incident tooling, optional
Companion, Field Notes, Loop Maps, Decision Packets, Paid Pilot, public project
state, safety and historical evidence to their existing pages. No new detail
page was needed.

## Compatibility and focused checks

- Explicit legacy anchors preserve the known external/internal routes for the
  mixed-language conversation entry, Paid Pilot, local read-only scan, Try one
  line first, Ask your AI first and the removed time-claim heading.
- `tests/test_external_intelligence_onboarding.py` checks primary ordering,
  closed details, visible volume, owner/evidence boundaries, destination
  existence, Japanese entry and old anchors.
- `tests/test_repository_default_claim_boundary.py` follows the shortened
  Companion link to the canonical detailed permission boundary.
- Existing personal-hub quickstart, worked example and V219/V220 records are
  read and linked but are not executed again.

## UI, publication and return checks

Branch UI observed on GitHub before PR:

- desktop `1440 × 1000`: `Start your own hub` rendered as the first primary
  README heading; both details were closed initially;
- narrow `390 × 844`: the same primary path rendered without page-level
  horizontal overflow and both details were closed initially;
- both details expanded at both tested widths; `Try one line first`, `Ask your
  AI first`, completion routes, Companion and Paid Pilot links became visible;
- the Personal Hub link opened the branch quickstart at `Personal Hub
  Roundtrip — Minimal Start`;
- the Japanese link opened `docs/getting_started_ja.md` at `日本語の開始案内`;
- GitHub emitted `user-content-...` DOM targets for the known old conversation,
  Paid Pilot, read-only scan and removed time-claim anchors.

Pending before admission:

- merge the approved PR and read back unauthenticated public `main`;
- fetch public main into the ordinary repository, update `v13-main-ready` only
  if it remains clean and safe, then verify the outer `v13` entry reaches the
  same-version instructions, first current-state block and first handoff block.

## Rollback

Revert the publication merge commit. This restores the earlier long README;
the existing quickstarts, examples, validation evidence and historical blocks
remain unchanged.
