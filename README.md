# Decision-OS V13 LoopKit ♻️

![Release](https://img.shields.io/github/v/release/shin4141/decision-os-v13-loopkit?label=release)
![License](https://img.shields.io/github/license/shin4141/decision-os-v13-loopkit)
![Status](https://img.shields.io/badge/status-operating%20prototype-blue)
![Local read-only scan](https://img.shields.io/badge/scan-local%20read--only-blue)
![Human approval for changes](https://img.shields.io/badge/changes-human%20approval%20required-orange)

[日本語の案内](docs/getting_started_ja.md)

Decision-OS V13 LoopKit helps an AI-assisted workspace remember selected
decisions, failure boundaries, reusable lessons, and a safe restart point
between jobs. It keeps completion and permission visible before another loop
starts.

Use it with your own purpose and rules. The author's public knowledge can stay
available as reference, but the author's goals, current work, permissions, and
publication authority do not become yours.

<a id="beyond-first-contact--optional-and-deeper-surfaces"></a>
<a id="full-experience--start-your-personal-hub-locally"></a>
<a id="-full-experience--start-your-personal-hub-locally"></a>

## Start your own hub

This is the primary route. It creates a writable local hub for your owner
state, rules, restart context, and evidence-bounded lessons.

Before starting, keep these conditions visible:

- use a writable local clone of public `main` on a branch or isolated
  worktree;
- expect setup to rewrite local instruction and handoff files, review the
  diff, and commit the owner state you want to keep;
- declare your Decision Owner, purpose, current state, protected conditions,
  and allowed local operations; and
- provide any tools or source facts required by the job you later authorize.

Clone the public repository:

```console
git clone https://github.com/shin4141/decision-os-v13-loopkit.git my-loopkit-hub
```

A GitHub Fork is optional. Use one only when you want your own GitHub-hosted
remote. Then open the clone in Codex and follow
[Personal Hub Roundtrip — Minimal Start](docs/personal_hub_roundtrip_quickstart.md).
Its owner-setup request separates your state and authority from upstream before
any job runs.

### A short example

1. Job A finishes and saves one evidence-bounded lesson as a candidate.
2. Job B starts from a fresh context and selects only the prior structure that
   fits the new purpose.
3. The AI applies it inside the new job's permission, verifies the result, and
   leaves a restartable handoff.

See the [synthetic saved → selected → applied example](examples/personal_hub_roundtrip_v0_1/)
and its [bounded V219/V220 validation](validation/v220_personal_hub_fresh_chat_reuse.md).
These are synthetic local observations, not proof of third-party ease, token
reduction, time savings, repeated reliability, or general quality improvement.

This route uses public repository surfaces and the new state you create. It
does not unlock a private repository, separate unpublished implementation,
Shin-specific private memory, or upstream state absent from public `main`.

<a id="update-conversation-️--更新案内"></a>
<a id="update-conversation-"></a>
<a id="start-one-governed-next-action-in-codex--codexで最初の一回"></a>
<a id="start-one-governed-next-action-in-codex"></a>
<a id="required-environment"></a>
<a id="prepare-once-in-the-normal-conversation"></a>
<a id="run-the-first-one"></a>
<a id="rule-practice-memory--ルールを使った経験を次へ戻す"></a>
<a id="rule-practice-memory"></a>
<a id="external-intelligence-for-decisions-that-survive-the-chat"></a>
<a id="the-problem"></a>
<a id="what-external-intelligence-changes"></a>
<a id="what-this-repository-supports"></a>
<a id="try-it-in-english--no-fork-required"></a>
<a id="try-one-line-first"></a>
<a id="start-in-5-minutes"></a>
<a id="ask-your-ai-first"></a>
<a id="まず試してみる--fork不要"></a>

<details>
<summary>Common questions and other ways to try V13</summary>

### Can I inspect it before changing local files?

Yes. Use the [English first-contact prompt](copy-paste/external-intelligence-first-contact.md)
to inspect the public repository without cloning or writing. It routes to the
[External Intelligence Quest Board](docs/external_intelligence_onboarding.md)
and keeps public evidence separate from unavailable or private behavior.

External Intelligence means preserving selected past decisions, failure
boundaries, reusable knowledge, and restart context outside one chat so that a
later AI retrieves only the prior structure that matters. It is not model
self-training or an everything-memory claim. Saved observations remain
[lifecycle-bounded](docs/field_note_lifecycle.md).

### Try one line first

Add this to your project instructions:

```text
Before you say "done," leave a restart note: what changed, what remains unresolved, the next safe step, and anything the next AI must not repeat.
```

This is a small handoff trial, not the Personal Hub setup and not evidence that
the wider system improves your work.

### Ask your AI first

If you want a recommendation before adopting anything, ask:

```text
Read this repository's public README and AI Reading Order. Explain which one
small V13 route may fit my current problem, what it would change locally, and
what evidence or permission is still missing. Do not modify files yet.
```

Use the [AI Reading Order](docs/ai_reading_order.md) to keep that inspection
bounded.

### Can I use a standalone ♻️ in Codex?

Yes, after the current owner has established these four fields:

- `Aspire:`
- `Current state:`
- `Protected conditions:`
- `Allowed scope for one ♻️ Run:`

The ordinary conversation route may compare evidence-backed maintenance, cost reduction,
repair, investigation, feature work, recording, and waiting. It runs
at most one already-authorized action and reports **Done:**, **Human judgment
needed:**, or **Waiting:** before it stops. No Companion process, server,
second model, or special button is required.

Read the exact [conversation ♻️ procedure](docs/codex_conversation_next_1_01.md)
and the [Personal Copy + Codex Quickstart](docs/fork_codex_quickstart.md).
Do not inherit Shin's or upstream's goals, Gate, current state, or authority.

### How does practice memory work?

At closure, the AI selects only an evidence-supported difference worth
preserving; no addition is a normal result. The
[Rule practice memory procedure](docs/rule_practice_memory.md#closure-selection)
defines the bounded save, failure, and re-entry path. Reading or running a
synthetic case alone is not another real-use result.

</details>

<a id="next-if-you-need-completion-and-loop-gates"></a>
<a id="turn-one-ai-incident-into-a-paste-ready-rule"></a>
<a id="can-the-next-coding-agent-find-where-to-restart"></a>
<a id="run-the-local-read-only-scan"></a>
<a id="what-a-result-can-look-like"></a>
<a id="how-to-interpret-it"></a>
<a id="choose-what-happens-after-the-result"></a>
<a id="a-result-is-enough"></a>
<a id="b-private-repository-specific-audit"></a>
<a id="check-one-ai-workflow-incident"></a>
<a id="what-ai-coding-incidents-return-to-the-human"></a>
<a id="secondary-adoption-paths"></a>
<a id="for-ai-agent-workspace-users"></a>
<a id="why-fork-this-repo"></a>
<a id="what-a-fork-unlocks"></a>
<a id="after-you-fork-where-to-write"></a>
<a id="fastest-way-to-evaluate-it"></a>
<a id="paid-pilot--ai-agent-handoff-audit"></a>
<a id="let-your-ai-read-v13"></a>
<a id="example-documented-does-not-always-mean-restartable"></a>
<a id="what-this-is"></a>
<a id="setup"></a>
<a id="first-try-the-lite-footer"></a>
<a id="choose-one"></a>
<a id="what-you-get"></a>
<a id="active-signals-vs-parked-horizons"></a>
<a id="observed-codex-output-from-an-agentsmd-verification-task"></a>
<a id="input--decision--output"></a>
<a id="before--after"></a>
<a id="gate-outcomes"></a>
<a id="quick-example"></a>
<a id="input"></a>
<a id="output"></a>
<a id="when-should-i-use-it"></a>
<a id="one-off-review"></a>
<a id="what-does-it-prevent"></a>
<a id="quick-links"></a>
<a id="contributing-and-safety"></a>
<a id="prototype-status"></a>
<a id="current-signal"></a>
<a id="loop-map"></a>
<a id="aspire-oriented-loop-map"></a>
<a id="decision-packet"></a>
<a id="v13-lite-footer"></a>
<a id="field-notes"></a>
<a id="short-example"></a>
<a id="conceptual-flow"></a>
<a id="core-distinction"></a>
<a id="v13-canon"></a>
<a id="core-principle"></a>
<a id="practical-use"></a>
<a id="optional-companion-your-coding-agent-asks-once-the-next-run-remembers"></a>
<a id="current-status"></a>

<details>
<summary>Completion gates, tools, evidence, and project history</summary>

### Completion and restart routes

- [Next-Action Confidence Check](copy-paste/next-action-confidence-check.md):
  separate `PASS / DELAY / BLOCK / UNKNOWN` from `GO / HOLD / CAP / BLOCK`.
- [Restartable Handoff](copy-paste/restartable-handoff.md): leave the next safe
  step and the do-not-repeat boundary.
- [AGENTS.md](AGENTS.md): canonical repository operating and authority rules.
- [Local read-only Workspace Health Check](docs/loop_library_ai_agent_workspace_health_check.md):
  test whether the next coding agent can find the restart point. The
  [distribution guide](docs/v13_runner_distribution_surface_v0_1.md) preserves
  the historical `run-the-local-read-only-scan` route.
- [One-off loop review](prompts/v13_loop_review.md): produce a bounded decision
  after completed work without installing a service.

### Incidents and reusable rules

- [Incident-to-instruction prompt](copy-paste/incident-to-instruction-rule.md):
  turn one sanitized AI-workflow incident into a draft rule.
- [Workflow incident intake](docs/workflow_incident_intake_checker_v0_1.md):
  check one incident without sharing credentials or private repository data.
- [Public incident map](case_studies/external_ai_workflow_incident_map_v0_1.md):
  selected descriptive cases, not population frequency or a product ranking.

### Optional Companion

The Companion is under development and is not used by the normal Codex
conversation `♻️` route. Its confirmed permission reuse is narrower than the
whole product: permission is bound to a repository, action, and exact path;
future proposed content may differ. Read the
[Verified Save boundary and evidence](docs/verified_save_claude_mvp_v0_1.md)
and the [Companion roadmap](docs/companion_product_roadmap_v0_3.md).

### Maps, packets, and memory

- [Loop Map](docs/loop_map.md) and
  [Aspire-Oriented Loop Map](docs/aspire_oriented_loop_map.md)
- [Decision Packet](docs/decision_packet.md) and
  [examples](docs/decision_packet_examples.md)
- [Field Note lifecycle](docs/field_note_lifecycle.md) and
  [Field Note types](docs/field_note_types.md)
- [User roadmap anchors](templates/user_roadmap_anchors.md)
- [V13 reconnection packet](templates/v13_reconnection_packet_template.md)

Field Notes are advisory evidence, not execution authority. Decision Packets,
maps, candidates, and saved observations do not grant permission or start
another loop.

### Service and public project state

- [Paid Pilot — AI Agent Handoff Audit](services/ai_agent_handoff_audit_offer.md):
  offer, fit check, scope, payment boundary, and handling limits.
- [Prototype status](docs/prototype_status.md)
- [Current operating signal](docs/current_signal.md)
- [Use cases](USE_CASES.md) and [mistake/repair log](MISTAKEN.md)
- [Contributing](CONTRIBUTING.md), [Security](SECURITY.md), and
  [Code of Conduct](CODE_OF_CONDUCT.md)

Historical updates and experiments remain in `validation/`, `field_notes/`,
the current-state history below the first block, and Git history. Their
existence does not prove general effectiveness or authorize repetition.

</details>

## Current status

```text
Status: Prototype scaffold / file-based loop governance kit.
Feature growth is paused; bounded real-task evidence and restartability checks continue.
```
