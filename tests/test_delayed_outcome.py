"""Fixed-source checks for one historical selection's later observed outcome.

These checks establish the evidence connection, not selection effectiveness.
"""

from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unittest

from scripts.rule_practice import preserve_history, render, validate


ROOT = Path(__file__).resolve().parents[1]
CASE_PATH = "validation/delayed_outcome_case_001.json"
BASE = "579f042e738ca117baa27cf7e95d7f0e76019a77"


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def instant(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


class DelayedOutcomeTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads((ROOT / CASE_PATH).read_text())
        self.observation = self.case["observations"][0]

    def source(self, name):
        item = self.case["sources"][name]
        return git("show", f"{item['commit']}:{item['path']}")

    def test_fixed_sources_and_original_records_are_preserved(self):
        self.assertEqual(BASE, self.case["inspection_base"])
        for name, item in self.case["sources"].items():
            with self.subTest(source=name):
                self.assertEqual(item["sha256"], hashlib.sha256(self.source(name)).hexdigest())
                self.assertEqual(instant(item["git_committed_at"]), instant(
                    git("show", "-s", "--format=%cI", item["commit"]).decode().strip()))
                git("merge-base", "--is-ancestor", item["commit"], BASE)
        for name in ("selection", "completion", "later_report"):
            path = self.case["sources"][name]["path"]
            original = git("show", f"{BASE}:{path}")
            self.assertTrue((ROOT / path).read_bytes().startswith(original), path)
        for path in ("docs/current_signal.md", "handoff/current_codex_handoff.md"):
            self.assertTrue((ROOT / path).read_bytes().endswith(git("show", f"{BASE}:{path}")))

    def test_later_repair_resolves_only_the_identified_placement_failure(self):
        before, after, history = [self.source(k) for k in
                                  ("before_repair", "after_repair", "protected_history")]
        self.assertFalse(before.endswith(history))
        self.assertTrue(after.endswith(history))
        heading = "## O-8 / O-69 テスト境界レビュー比較の保存 — 2026-09-10".encode()
        old_section = before[before.index(heading):]
        self.assertEqual(1, after.count(old_section))
        boundary = b"<!-- trajectory-history-boundary:v209-restart-security -->"
        self.assertLess(after.index(old_section), after.index(boundary))
        checks = self.observation["content_checks"]
        for prefix, raw in (("o69", old_section), ("historical_suffix", history)):
            self.assertEqual(checks[prefix + "_bytes"], len(raw))
            self.assertEqual(checks[prefix + "_sha256"], hashlib.sha256(raw).hexdigest())
        path = self.case["sources"]["after_repair"]["path"]
        self.assertEqual(after, git("show", f"{BASE}:{path}"))
        receipt = self.observation["external_receipt"]
        git("merge-base", "--is-ancestor", self.case["sources"]["after_repair"]["commit"], receipt["merge_commit"])
        git("merge-base", "--is-ancestor", receipt["merge_commit"], BASE)
        self.assertIn(b"Run 3 reproduced one failing invariant", self.source("later_report"))

    def test_occurrence_recording_and_confirmation_are_not_conflated(self):
        times = self.observation["event_times"]
        trigger = times["selection_triggered_at"]
        self.assertIn(trigger.encode(), self.source("selection"))
        for time_key, source_name in (("completion_record_committed_at", "completion"),
                                      ("repair_committed_at", "after_repair"),
                                      ("later_report_committed_at", "later_report")):
            self.assertEqual(instant(times[time_key]), instant(self.case["sources"][source_name]["git_committed_at"]))
        ordered = [trigger, times["completion_record_committed_at"], times["repair_committed_at"],
                   times["later_report_committed_at"], times["repair_admitted_at"], self.observation["confirmed_at"]]
        self.assertEqual(sorted(map(instant, ordered)), list(map(instant, ordered)))
        self.assertEqual(times["repair_admitted_at"], self.observation["external_receipt"]["merged_at"])
        for key in ("execution_finished_at", "repair_executed_at"):
            self.assertIsNone(times[key])
            self.assertTrue(times[key + "_unknown_reason"])
        self.assertIsNone(self.case["rule_attribution"]["rule_id"])
        self.assertEqual("UNCONFIRMED", self.observation["assessment"]["effect_improvement"])
        self.assertFalse(self.observation["revisit"]["automatic_schedule"])
        ids = [o["id"] for o in self.case["observations"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_optional_retrieval_preserves_v214_history_and_resolves_links(self):
        ledger_path = "evidence/rule_practice/fn125.json"
        old = json.loads(git("show", f"{BASE}:{ledger_path}"))
        current = json.loads((ROOT / ledger_path).read_text())
        preserve_history(old, current)
        validate(current, ROOT)
        self.assertEqual(render(current), (ROOT / "docs/rule_practice/fn125.md").read_text())
        guide = (ROOT / "docs/rule_practice_memory.md").read_text()
        self.assertIn("../validation/delayed_outcome_case_001.md", guide)
        record = ROOT / "validation/delayed_outcome_case_001.md"
        self.assertIn("delayed_outcome_case_001.json", record.read_text())
        links = re.findall(r"\]\(([^)]+)\)", record.read_text())
        links += self.observation["revisit"]["references"]
        for target in links:
            if "://" in target:
                continue
            path, _, anchor = target.partition("#")
            destination = (ROOT if target.startswith("validation/") else record.parent) / path
            self.assertTrue(destination.is_file(), target)
            if anchor:
                self.assertIn(f'<a id="{anchor}">', destination.read_text())


if __name__ == "__main__":
    unittest.main()
