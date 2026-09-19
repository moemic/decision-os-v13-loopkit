# FN125 validation scope: correction to PR #166 m03

Baseline: `c152410809add234f8e9f4bd670ee9c3c21242d7` (PR #166).
This bounded correction starts from
[`memory_five_patterns/report.md`](memory_five_patterns/report.md), follows m03
only, and does not repeat the five-perspective evaluation.

## Where the qualification was lost

| Stage | Existing evidence | Finding |
| --- | --- | --- |
| Input | `memory_five_patterns/cases.json`, m03 `situation` / neutral prompt | Asked to compare persisted registration, receiving-context judgment and a missing Bundle from existing examples. No synthetic reminder was given to the reader. Evaluator expectations, not reader input, explicitly required the synthetic-only limit. `real-record-review` describes reviewing an existing record; it does not classify the underlying data as production work. |
| Acquired source | `validation/field_note_125_operational_validation.md`, baseline Case 1 lines 46–67 | `Synthetic Boundary: 8 / 8 PASS` and the adjacent synthetic-only sentence already qualify the `240 / 240` result. The m03 receipt confirms the entire 192-line record was displayed. This was not a retrieval miss. |
| Reader final | m03's delivered answer, preserved separately with this correction | Compared Case 1/2/3A and noted unavailable original records, but did not carry the synthetic-only qualification into the comparison. This is the observed omission. It did not explicitly claim measured business benefit, but its unqualified examples could be read too broadly. |
| Saved evaluation | `reads.json` m03 `limits`, `results.json` m03 `claim_limits: PARTIAL`, report and matrix | Already expose the omission and source-access/synthetic limits. Preserve these original judgments. The saved `decision` summary alone omits the data class; its linked correction must travel with any reuse. PR #166 saved a summary and read receipts, not a verbatim repository copy of the entire final answer. |
| Next source route | AGENTS → current FN125 card → Canon / practice references → operational-validation record | The original Case 1 already labels the data, but the case conclusions and closure summary can be compressed without that label. The repair is a scope preface on this specific validation record, not a new requirement for all rules. |

The source does not justify relabeling every historical action as an invented
event. Case 1's evaluation dataset is synthetic-only. Cases 2/3A are persisted
observations of receiving-context and transport handling; their original
external executions are not re-audited here. These distinctions allow evidence
from prepared validation cases to remain useful without treating it as measured
effectiveness in real business work.

## Connected correction

Read m03's old comparison together with this qualification:

> Case 1's registered evaluation data were synthetic-only; its aggregate and
> boundary PASS do not establish business-work effectiveness. The recorded
> artifact, receiving-context and missing/recovered-Bundle decisions support a
> bounded comparison of proof selection in the validation history. m03 is an
> actual observation of an AI reading those records, not a new production use
> of FN125. The original external histories and general real-work effects remain
> unverified.

The original m03 judgment, input, acquisition receipts, PARTIAL assessment and
all other PR #166 cases remain intact. The newly saved original-answer text is
a transcription of the earlier delivered public reader final, separate from
this correction; it is not a rewritten historical answer. Original snapshot
links inside that text are retained as originally delivered.

## Minimal route repair

Only the entrance of `validation/field_note_125_operational_validation.md`
gains a scoped reading/reporting preface. It binds the data class and permitted
interpretation to these case conclusions and explicitly preserves the value of
observed validation behavior. Every original byte remains below a new boundary.
The already-correct Case 1 synthetic label, old results and closure table are
not rewritten.

FN125 Canon, version, current card, real-use ledger and AGENTS are unchanged.
No synthetic observation is added to the production denominator. The earlier
report receives only a forward correction link; general guides need no new
reporting obligation.

## One fresh-reader check: predeclared contract

One new `fork_turns: none` reader receives the same m03 question and normal
AGENTS entrance, with read-only scope and honest candidate provenance. Its
prompt does not mention synthetic data, the missing qualifier, expected paths,
or the desired answer. No mid-trial hint is allowed. No second reader/retry is
authorized by this check.

The independent snapshot is based on PR #166 with only the source preface
changed. The prior evaluator bundle `validation/memory_five_patterns/` is
withheld from the working files by sparse checkout; new correction/evaluation
artifacts are absent. Normal published instructions/current-state blocks remain,
including their pre-existing summary of the reporting limitation. This is a
route verification, not an experiment isolating the preface's causal effect.

Success requires acquiring the relevant source and reporting both the correct
conditional decisions and their evidence class: synthetic-only evaluation data
are not business-work effect measurements; an observed AI response or recorded
validation decision remains valid scoped evidence. Unavailable external sources
and unmeasured effects must remain unknown. A correct phrase without confirmed
source acquisition is insufficient. If omission persists, record it and stop;
reopen only for a concrete unresolved extraction/reporting boundary with new
authority, not until a desired answer is obtained.

The single check, actual answer/read receipts, preservation tests and delivery
will be appended after the observation, without replacing this initial diagnosis.

<!-- fn125-scope-correction-follow-up -->

The [original response and separate correction](fn125_scope_correction.json)
and [single-reader setup / receipts](fn125_scope_reader_001.json) accompany it.

## Single-check outcome

The one fresh reader followed AGENTS → FN125 card → Canon → the full validation
record, including the new preface. Its final answer explicitly states:

> Case 1の240/240・8/8は**synthetic-only評価**であり、業務効果ではありません。

It also keeps Case 2/3A as observations in the validation history, says the
original external histories are not reproduced/reverified, and claims no real
registration, Capsule acceptance or demonstrated effect. It still uses those
observations to compare proof strength and resumption timing. Thus the data
qualification survived acquisition and reporting in this one session, without
invalidating the observed conditional judgments.

The exact answer and reader-reported ranges are in the receipt. Six source
paths were displayed across four stages; source-text characters total 49,586.
Whole-blob Python reads are separately recorded, not counted as full historical
model input. The source ranges/counts match the fixed candidate, and HEAD/tree,
origin/main, clean state and withheld evaluator working files were unchanged
after the check. No hints, intervention, follow-up or retry occurred.
The reader candidate contains only the source preface; later correction links,
guide notes and admission summaries were not reader inputs. The source bytes
used by the reader are checked against the delivered source, while existing
regressions cover the current-state delivery surfaces.

This is not proof of business effectiveness, general reporting reliability or
a causal effect of the preface alone. It does not repeat the other five-pattern
cases or add a real-use ledger execution. If a future authorized use drops the
scope again, preserve that exact output and source range, then revisit only the
point where the qualifier was lost. No automatic recheck is selected.

## Validation and delivery

Original Case 1 wording/results and every older validation byte are preserved.
FN125 Canon/version/card/ledger and AGENTS remain unchanged. Original PR #166
input, reads, assessments and setup are unchanged; its report only gains the
forward correction link. The original m03 final and corrected qualification
remain separate; the initial omission is not rewritten as if the qualifier had
been present.

Relevant existing regressions passed: **88 tests**, 132.568 seconds. This is
the current-state, historical preservation, handoff, delayed-outcome and
rule-practice regression group, not a rerun of the five-pattern AI trials.

```console
python3 -B scripts/compact_test_output.py --log .test-logs/fn125-scope-regression.log -- python3 -B -m unittest tests.test_delayed_outcome tests.test_rule_practice tests.test_current_state_admission tests.test_13_42_13_43_historical_regression tests.test_v209_restart_surface tests.test_decision_os_handoff_acceptance
python3 -B scripts/rule_practice.py --check --base origin/main
git diff --check
```

The rule/card/history and diff checks passed. One-off checks verified the
original validation and current-state byte suffixes, original report prefix,
unchanged rule/ledger/PR166 input-read-assessment records, frozen initial
diagnosis/contract prefix, reader source hash and range counts, clean candidate
identity, original/new answer hashes, JSON and local links. The disposable
reader clone was removed after its receipts were saved and integrity checked.
The broad legacy suite, original external executions and real-work effect were
not re-run or inferred.

Canonical delivery remains pending the PR and exact fetched-main read-back.
The delivery PR's final body receipt will record reviewed head, merge identity,
changed paths, paired blocks and ancestry. No global display duty, new feature,
monitor, release, tag or outreach is introduced.
