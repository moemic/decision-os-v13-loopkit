# README English personal-hub entry — publication record

- Evidence class: bounded documentation and link verification
- Base: `ea0dadb0726394d5c4a37283f163c5ad1b3bc5ef` (`origin/main` at start)
- Work branch: `codex/readme-english-personal-hub`
- Publication PR: pending

## Reason

The public README mixed Japanese into visible headings, the four-field owner
setup prompt, and the Rule practice memory entry. An English reader therefore
could not follow the published path to first personal-hub setup without
understanding Japanese, even though the detailed personal-hub quickstart was
already English.

## Bounded change

- Make visible README headings, explanatory copy, operating instructions, and
  the four-field setup prompt English.
- Explain Rule practice memory in English while labeling linked Japanese
  records and procedures as Japanese.
- Add one top-level `日本語の案内` link to a short Japanese entry page. That page
  carries the moved Japanese first-contact prompt and a concise clone-first
  personal-hub route; it is not a second maintained README.
- Preserve explicit compatibility anchors for the formerly mixed headings and
  the moved Japanese first-contact heading.
- Preserve the published Personal Hub Roundtrip, synthetic worked example,
  V219/V220 evidence limits, optional-Fork boundary, owner and permission
  boundaries, stop conditions, and candidate-note versus adopted-Rule
  distinction.
- Leave historical Japanese records, internal documents, and the V219/V220
  trial artifacts unchanged.

## Impact

After admission, an unauthenticated English reader can follow the README's
copyable setup request into the existing English personal-hub quickstart
without relying on Japanese. Japanese readers have one short entry page from
the top of README and can continue to the existing Japanese Quest Board or the
canonical detailed English personal-hub procedure.

This is a language and routing repair. It does not add a feature, repeat a
synthetic trial, establish third-party usability, or prove token, time, cost,
reliability, or quality improvement.

## Verification contract

- `tests/test_external_intelligence_onboarding.py` checks the English four-field
  prompt, the single Japanese entry link, absence of Japanese in visible README
  copy apart from that link, the moved Japanese first-contact prompt, and the
  personal-hub owner/permission/candidate boundaries.
- The old mixed-heading fragments remain as explicit IDs. The repository's
  historical `README.md#start-one-governed-next-action-in-codex--codexで最初の一回`
  reference therefore still resolves.
- Required local destinations are checked for existence, and Markdown links
  in the changed README and Japanese guide are checked before publication.
- Admission also requires the exact paired first current-state blocks, focused
  historical/handoff regressions, fetched-`origin/main` ancestry and selected
  path equality, plus unauthenticated rendered and raw GitHub read-back.

## Rollback

Revert the publication merge commit. That restores the prior mixed README and
removes the Japanese entry page, reference/test updates, and paired admission
block. It does not delete or rewrite the preserved V219/V220 trials, older
Japanese records, or unrelated work.
