# Personal Hub Roundtrip — Minimal Start

Use this after you choose to make a personal writable copy of LoopKit. It is
an English, local-only path from your own purpose to one task, one returned
lesson, and one later reuse. It reuses the existing New Repo Capsule, handoff,
Field Note lifecycle, and selective-reading rules. It does not add a capsule
runtime, selector, service, or second repository.

## What “a clean copy for me” means

Your copy keeps the public LoopKit library available for reference. It does
not make the upstream author's current operating state yours.

- You are the Decision Owner of your copy.
- Your purpose, priorities, protected conditions, and permissions control its
  work.
- Upstream goals, current tasks, Gate, branch authority, and publication
  permission remain upstream history.
- You may inspect and selectively adopt useful rules, Field Notes, templates,
  and examples. Their presence alone does not activate them.
- Lessons you accept are saved under your ownership, with their evidence and
  limits.

This requires an active owner setup. A sentence saying “do not follow Shin”
does not by itself replace a root instruction file and handoff that still
describe upstream work.

## 1. Make a personal writable copy

You need Git, a writable local folder, and Codex or Claude Code with access to
that folder. No Companion process, installer, capsule generator, or second
model is required. A GitHub account is needed only if you choose to create a
GitHub Fork or push to GitHub.

Clone public `main` to your computer:

```console
git clone https://github.com/shin4141/decision-os-v13-loopkit.git my-loopkit-hub
```

A GitHub Fork is optional. Use one only when you want a GitHub-hosted remote
under your account. Open the cloned repository root in Codex or Claude Code,
then send:

```text
This is my own writable LoopKit copy. I am the Decision Owner.

Aspire: <what I want this hub to help me accomplish>
Current state: <what exists now and what is missing>
Protect: <facts not to invent; files, money, privacy, or external actions to protect>
Permission for this setup: replace the active root instructions and current
handoff with my minimal owner state; preserve upstream files and history as
references. Create purpose-fitted local capsules, run only the jobs I name,
save evidence-bounded lessons to my hub, and commit locally. Do not publish,
push, contact anyone, deploy, or use credentials unless I separately approve it.

Confirm this setup before acting. Do not treat the upstream author's goals,
current tasks, Gate, branches, or permissions as mine.
```

## 2. Establish the active personal hub

Before the first ordinary job, ask the AI to make these owner-approved local
changes:

1. Replace the root `AGENTS.md` with a short owner-controlled instruction
   surface: your purpose, authority, evidence rule, completion rule, memory
   boundary, and capsule route.
2. If `CLAUDE.md` routes to `AGENTS.md`, make it say that the current personal
   `AGENTS.md` is active.
3. Replace `handoff/current_codex_handoff.md` with your current personal state,
   Gate, next authorized action, missing closure, and stop boundary.
4. Keep upstream rules and state available through Git history or fixed source
   references. Do not delete the Field Notes, templates, examples, or docs you
   may later consult.

Read back the three active files. Search them for inherited owner names,
goals, active tasks, Gates, branches, and permissions. Attribution and fixed
source references may remain; active owner state may not.

## 3. Send the first job

Give the hub one bounded request and its facts. Ask it to create a New Repo
Capsule using the existing
[`new_repo_scaffold_standard.md`](new_repo_scaffold_standard.md):

```text
Create one purpose-fitted capsule in a separate local workspace for this job.
Start from my purpose and source facts. Carry the universal operating core and
only the guards this destination needs. Record active, conditional, excluded,
and UNKNOWN items in docs/capsule_fit_audit.md. Then do the job once, verify
it, leave a handoff, and stop.
```

The capsule should show:

- the destination and owner;
- active instructions in that workspace's `AGENTS.md`;
- selected guards and why they fit;
- reference guidance that is read only when its trigger occurs;
- excluded upstream material and the reason;
- facts still `UNKNOWN`; and
- the final restart point.

## 4. Return one evidence-bounded lesson

After the first job, save only a lesson supported by its source and result.
Keep it a candidate observation unless your own promotion process adopts it as
a rule. Record its trigger, reusable structure, scope, source evidence,
conditions where it must not be applied, and remaining unknowns.

At this point the lesson is **saved**. It is not yet **reused**.

## 5. Start a different job in a different workspace

Give the hub the new job and new source facts. Ask it to inspect candidate
lessons, select only those whose trigger matches, put the selected excerpt and
its provenance in the new capsule, and explain why all other hub or upstream
material was excluded.

The new workspace must still use its own instructions and source facts. A
selected lesson supplies reasoning; it supplies no permission.

Call the lesson:

- **saved** when it exists in the hub;
- **selected** when the new capsule records a trigger match and carries it;
- **applied** only when the new output visibly uses its structure and the
  result is checked against the new source.

## 6. Stop and read the result

The roundtrip is complete when you can inspect:

```text
your first message
→ your active hub state
→ task-one capsule and output
→ returned candidate lesson
→ task-two capsule with selection reason
→ task-two output with visible application
→ final handoff and UNKNOWNs
```

The synthetic worked example is
[`examples/personal_hub_roundtrip_v0_1/`](../examples/personal_hub_roundtrip_v0_1/).
It does not establish third-party usability, token or model-usage reduction,
real workflow benefit, repeated reliability, or star growth.
