# Workspace Health RED authority-routing repair — 2026-09-06

## Admission evidence

```text
Repository identity: shin4141/decision-os-v13-loopkit
Observed repository root: /Users/sn/Documents/v13/decision-os-v13-loopkit
Fresh remote main: 94144c4a034267863963d5a81bd67bd203c8277e
Fresh observation: git ls-remote origin refs/heads/main
Authorized repair worktree: /Users/sn/Documents/v13/.codex-worktrees/workspace-health-red-routing-repair
Authorized repair branch: codex/workspace-health-red-routing-repair
Repair base: 94144c4a034267863963d5a81bd67bd203c8277e
Decision Owner: Shin
```

The existing entrance checkout was on
`codex/13-108-stage-c-repository-identity-continuity` with unrelated untracked
state. It was not used as the repair target. The isolated worktree was created
from the exact fresh remote-main object after repository identity, scope,
ownership, freshness, and current authorization were established.

## Bounded repair

The Workspace Health Check now separates RED signal severity from authority:

1. authorized read-only diagnosis and evidence recovery remain AI-owned;
2. an exact, current repair approval is not requested again, but the repair is
   presented as a separate phase and is not executed inside the diagnostic loop;
3. new or expanded authority and uncovered irreversible decisions return to the
   Human Seat;
4. unknown identity, ownership, authority, approval coverage, or validity routes
   to HOLD while available authorized read-only recovery continues; and
5. RED creates no write, repair, branch-change, deletion, or GO authority.

Operation names do not replace approval matching. A branch change or deletion
covered by an exact, current approval is not re-asked solely because of its
name; a changed target, scope, use, validity condition, or other uncovered
decision remains fail-closed.

The root `AGENTS.md` authority boundary is unchanged.

## Validation

### Mechanical wording and direct-reference consistency

```text
python -m unittest discover -s tests -p 'test_workspace_health_red_routing.py'
PASS — 5 tests

python -m unittest discover -s tests -p 'test_current_state_admission.py'
PASS — 8 tests

python -m unittest discover -s tests -p 'test_13_42_13_43_historical_regression.py'
PASS — 6 tests

python -m unittest discover -s tests -p 'test_decision_os_handoff_acceptance.py'
PASS — 56 tests

git diff --check
PASS
```

The tests bind the Loop Skill, both directly corresponding public descriptions,
the RED example, and the unchanged root authority boundary.

### Static case judgment

| Case | Expected route | Static result |
| --- | --- | --- |
| RED + authorized read-only diagnosis | AI-owned read-only recovery; Human Seat `none` | PASS |
| RED + exact current repair approval | separate repair phase; no repeated approval; no execution in diagnosis | PASS |
| RED + new authority or uncovered destructive decision | exact remaining Human Seat decision; no execution | PASS |
| RED + identity / owner / authority unknown | HOLD; continue available authorized read-only recovery | PASS |

### Runtime behavior

```text
NOT RUN
```

The Workspace Health Check is a natural-language Loop Skill and no dedicated
executable classifier existed on the inspected fresh main. This Gate authorized
local repair and tests, not a model invocation. Mechanical wording validation
and static judgment are not reported as runtime behavior evidence.

## Current-state and external boundary

This is a local admission candidate only. It does not change the current Gate,
create GO, or establish canonical capability from a branch commit. No push, PR,
merge, or remote read-back is authorized in this task. The existing paired first
blocks in `docs/current_signal.md` and `handoff/current_codex_handoff.md` remain
unchanged. If this repair is later selected for canonical admission, the current
AGENTS admission joint, paired first-block update when applicable, required
regressions, merge, fetched remote read-back, and ancestry check remain open.
