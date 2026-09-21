# Mira task two — synthetic reuse result

Owner: Mira (synthetic). The second job ran in a separate local workspace with
new reservation facts. Its capsule selected one candidate lesson saved from
task one and excluded the whole upstream corpus, the old checklist, and
upstream owner state.

## Saved versus selected versus applied

| Item | Observed state |
| --- | --- |
| Mira Note 001 in the hub | SAVED at hub commit `4ca74a6`; saving alone was not reuse |
| `selected_mira_note_001.md` in task two | SELECTED because the new facts contain a ledger entry, an unverified interval, and a physical confirmation before an actionable state |
| Three-state structure and evidence table in `reservation_checklist.md` | APPLIED in a different task output and checked against the new source |
| Effect on real volunteers, explanation burden, tokens, cost, or errors | NOT OBSERVED |

The selected excerpt retains its source path, hub commit, SHA-256, candidate
status, reason for selection, and limits. The output explicitly names it as a
consulted candidate rather than authority.

The second draft separates `request recorded`, `physical confirmation
pending`, and `ready for pickup`, then binds each transition to supplied facts.
It leaves pickup hours, promised date, actual stock, and notification
permission `UNKNOWN`. A local verification checked the source-note digest,
state distinction, physical confirmation, evidence map, unknowns, and no-send
boundary; all checks passed after one test assertion was corrected to account
for Markdown line wrapping. The draft itself did not change for that check.

No Shin-specific Aspire, 100-star goal, upstream Current Gate, active task,
branch authority, publication approval, or social-post plan appears in the
task-two capsule or output. Upstream file paths and fixed commit identifiers
appear only as reference provenance for the capsule mechanism.

V12 State: PASS for this bounded synthetic reuse path.
V13 Next Loop Gate: HOLD — no third task or operational deployment authorized.
