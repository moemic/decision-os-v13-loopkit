# Task-two New Repo Capsule Fit Audit (synthetic)

Destination / Purpose: one private, local reservation-to-pickup status
checklist from supplied facts. Text drafting and handoff only; no public
surface, code, API, contact, notification, audit, or automation. Owner: Mira.

## Active guards and why

- Mira's Seat, local-only authority, completion/UNKNOWN/handoff core:
  prevents importing another owner's permissions or declaring pickup readiness
  from incomplete facts. Sources: hub `4ca74a6:AGENTS.md` and
  `26c9eea:docs/new_repo_scaffold_standard.md` §Universal Core.
- Separate recorded reservation, physical confirmation, and actionable pickup
  status. Source: `source/reservation_facts.md`.

## Selected candidate guidance and exact trigger

- `docs/selected_mira_note_001.md` carries one scoped structure from Mira's
  own task-one observation. Trigger: the new source has a recorded request
  while physical readiness is not yet established. The source facts satisfy
  the trigger, so the executing AI should read the selected guide; it remains
  advisory rather than a promoted rule. Source: hub
  `4ca74a6:field_notes/mira_001_recorded_not_ready.md`, with SHA-256 in the
  selected guide.

## Other conditional guards and exact reconnect triggers

- If Mira asks to notify borrowers or publish wording, stop for separate
  authorization and reassess contact/public-surface guards. Sources: hub
  `4ca74a6:AGENTS.md` and
  `26c9eea:templates/v13_build_capsule_minimum_contract.md` §Public Surface.
- If the destination purpose changes beyond this private checklist, re-run
  this audit before acting. Source:
  `26c9eea:docs/new_repo_scaffold_standard.md` §Fit Audit Re-evaluation.
- If Mira requests handoff, read `docs/handoff_command.md`. Source:
  `26c9eea:docs/new_repo_scaffold_standard.md` §Handoff Command.

## Excluded guards and why

- The whole upstream Field Note corpus, previous task-one checklist, and
  upstream author's goals/current state: the selected Mira note supplies the
  relevant structure; the new source supplies current facts. Sources: hub
  `4ca74a6:AGENTS.md`, `4ca74a6:field_notes/mira_001_recorded_not_ready.md`,
  and `26c9eea:docs/fork_codex_quickstart.md`.
- Runtime/API, scraping, evaluation, automation, money, and release guards:
  outside this private text-only task. Source:
  `26c9eea:templates/v13_build_capsule_minimum_contract.md`
  §Repo-specific Capsule Fit Audit and this workspace's `README.md`.

## UNKNOWN and recheck

- Actual pickup hours, promised date, physical stock state of any real item,
  and permission to notify borrowers: absent from
  `source/reservation_facts.md`. Do not infer them. Mira must supply and
  authorize them before operational use.

This is this destination's sole Fit Audit. The note was selected because its
trigger matches, not because every saved item must be transported.
