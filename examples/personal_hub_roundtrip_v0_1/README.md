# Personal Hub Roundtrip v0.1 — Synthetic Worked Example

This is a local synthetic trial. Mira is invented; no participant was
recruited. The same Codex task performed both workspace runs, so this is not
an independent-user, independent-model, or fresh-context evaluation.

## The example in one view

```text
Mira's first message
  ↓
owner-controlled hub instructions + handoff
  ↓
task one: tool return checklist
  ↓
Mira Note 001 saved to the hub
  ↓
task two: reservation-to-pickup checklist in a separate folder
  ↓
Mira Note 001 selected for a matching state gap and applied
```

## What Mira said first

[`first_message.md`](first_message.md) supplies Mira's own Aspire, current
state, protected conditions, and local-only permission. It explicitly keeps
upstream goals, current tasks, Gate, and permissions out of her state.

## What the hub kept

[`hub/AGENTS.md`](hub/AGENTS.md) is the active owner-controlled instruction
surface. [`hub/final_handoff.md`](hub/final_handoff.md) is the final restart
state. The public LoopKit library remained available in the local copy, while
upstream operating state stayed reference material.

## Task one: what entered its capsule

The destination was one private tool-return checklist.

- [`task_one/AGENTS.md`](task_one/AGENTS.md): Mira's Seat, local-only
  authority, source-evidence boundary, three-state distinction, completion,
  and handoff.
- [`task_one/capsule_fit_audit.md`](task_one/capsule_fit_audit.md): why those
  guards were active; triggers for public/contact/purpose changes; excluded
  runtime, automation, and upstream state; unknown inspection criteria.
- [`task_one/source.md`](task_one/source.md): the new task facts.
- [`task_one/output.md`](task_one/output.md): the executed checklist.
- [`task_one/final_handoff.md`](task_one/final_handoff.md): result, unknowns,
  stop boundary, and ownership.

The output separated `received / logged`, `inspection pending`, and
`available to lend`. The reusable candidate returned to Mira's hub is
[`hub/mira_note_001.md`](hub/mira_note_001.md): a recorded event does not by
itself establish a later actionable state when a verification step intervenes.
Its task-one evidence and limits are in
[`task_one/RESULT.md`](task_one/RESULT.md).

## Task two: what was carried and why

The new source concerned reservations rather than returns. It again contained
a ledger entry, an interval where the tool may still be on loan, and a physical
shelf confirmation before `ready for pickup`. That matched Mira Note 001's
trigger.

- [`task_two/capsule_fit_audit.md`](task_two/capsule_fit_audit.md) records the
  match and excludes the whole upstream corpus and old checklist.
- [`task_two/selected_mira_note_001.md`](task_two/selected_mira_note_001.md)
  carries the note's source commit, SHA-256, candidate status, selection
  reason, reusable structure, and limits.
- [`task_two/task_agents.md`](task_two/task_agents.md) makes the new
  workspace's facts and permission controlling.
- [`task_two/reservation_facts.md`](task_two/reservation_facts.md) supplies the
  second job's facts.
- [`task_two/reservation_checklist.md`](task_two/reservation_checklist.md)
  visibly applies the three-state structure and adds evidence for every
  transition.
- [`task_two/final_handoff.md`](task_two/final_handoff.md) records activation,
  remaining unknowns, and the stop.

[`task_two/RESULT.md`](task_two/RESULT.md) distinguishes **saved**,
**selected**, and **applied**. It also records the unobserved effects.

## What Mira did not need to explain again

For task two, Mira supplied the new job and its new facts. She did not restate:

- the distinction between a recorded event and an actionable state;
- the need for an evidence-bearing intermediate check;
- the rule for leaving a missing transition `UNKNOWN`; or
- the no-promise and no-publication limits attached to that lesson.

Those items came from the selected owner note. She still had to supply the
new purpose, current facts, and current permission; a prior lesson cannot
decide those.

## Evidence boundary

This example confirms one local synthetic document roundtrip and local source
checks. It does not confirm token savings, Astra usage reduction, third-party
ease of use, real operational correctness, error reduction, general
selection reliability, or GitHub star growth.
