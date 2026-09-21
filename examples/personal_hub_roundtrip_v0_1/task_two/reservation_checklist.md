# Private reservation-to-pickup checklist — synthetic draft

Source: `source/reservation_facts.md`. Structure consulted:
`docs/selected_mira_note_001.md` (candidate guidance, not authority).
This draft is not a borrower notification or a promise of pickup time.

1. **Request recorded:** Enter the request ID and desired pickup day in the
   reservations ledger. This records a request; it does not show that the
   tool is physically present or ready for pickup.
2. **Physical confirmation pending:** The tool may still be on loan. Keep
   readiness unresolved until the tool has returned and the assigned
   volunteer confirms it is on the pickup shelf.
3. **Ready for pickup:** Use this status in a private draft only after that
   physical shelf confirmation. Do not infer it from the ledger entry or
   desired pickup day alone.

## Evidence for each transition

| Transition | Supplied fact | Result without that fact |
| --- | --- | --- |
| No record → request recorded | A volunteer enters request ID and desired day in the ledger. | Recording is `UNKNOWN`. |
| Recorded → physically confirmed | An assigned volunteer confirms the returned tool on the pickup shelf. | Physical presence is `UNKNOWN`; no ready status. |
| Physically confirmed → ready-for-pickup wording | The source permits this wording only after shelf confirmation. | Do not say ready. |

Pickup hours, a promised date, actual stock state, and permission to notify a
borrower remain `UNKNOWN`. Mira must supply and authorize those facts before
operational use or any external message.
