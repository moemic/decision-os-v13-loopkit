from copy import deepcopy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts.rule_practice import CARD, LEDGER, ROOT, main, preserve_history, render, validate, write_card


BASE = "d0182a1e917e800aefe50f95cd4d400b1fa272fd"


class RulePracticeTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / LEDGER).read_text())
        # Synthetic cases exist only in memory, never in the production ledger.
        self.entry = deepcopy(self.data["entries"][0])
        self.entry.update(id="test-01", execution_id="test:only-in-memory")
        self.entry["version"] = self.data["current_version"]
        self.data["entries"] = [self.entry]

    def test_maintain_unknown_and_reference_are_distinct(self):
        validate(self.data, ROOT)
        self.assertIn("**maintain**", render(self.data))
        for kind, result in (("applied", "unknown"), ("reference", "observed"),
                             ("connection", "observed")):
            with self.subTest(kind=kind, result=result):
                self.entry.update(kind=kind, result=result, decision="maintain")
                with self.assertRaises(ValueError):
                    validate(self.data, ROOT)
                self.entry["decision"] = "unassessed"
                validate(self.data, ROOT)
                expected = "observed results: 0; unknown results: 1" if kind == "applied" else "Distinct applied executions: 0"
                self.assertIn(expected, render(self.data))

    def test_counterexample_stays_visible_until_evidenced_resolution(self):
        for issue in ("counterexample", "condition_mismatch"):
            with self.subTest(issue=issue):
                data = deepcopy(self.data)
                bad = data["entries"][0]
                bad.update(issue=issue, decision="revise", change_scope="operational",
                           reason="Observed proof choice missed a material condition.")
                later = deepcopy(self.entry)
                later.update(id="test-02", execution_id="test:later")
                data["entries"].append(later)
                validate(data, ROOT)
                self.assertIn("**test-01 / revise", render(data))
                # Twenty positive records do not revise the rule or erase a counterexample.
                for i in range(3, 23):
                    item = deepcopy(later)
                    item.update(id=f"test-{i:02}", execution_id=f"test:later-{i}")
                    data["entries"].append(item)
                validate(data, ROOT)
                self.assertEqual(self.data["current_version"], data["current_version"])
                self.assertIn("**test-01 / revise", render(data))
                data["entries"][-1].update(resolves=["test-01"], resolution_reason="Named evidence resolves this condition.")
                validate(data, ROOT)
                self.assertNotIn("**test-01 / revise", render(data))
                data["entries"][-1].update(result="unknown", decision="unassessed")
                with self.assertRaisesRegex(ValueError, "cannot close"):
                    validate(data, ROOT)

    def test_duplicate_execution_amends_without_counting_again(self):
        later = deepcopy(self.entry)
        later["id"] = "test-02"
        self.data["entries"].append(later)
        with self.assertRaisesRegex(ValueError, "explicit amendment"):
            validate(self.data, ROOT)
        later["supersedes"] = "test-01"
        with self.assertRaisesRegex(ValueError, "no new observation"):
            validate(self.data, ROOT)
        later["observation"] = "A later result changed what could be established for the same execution."
        validate(self.data, ROOT)
        self.assertIn("Distinct applied executions: 1", render(self.data))
        later["id"] = "test-01"
        with self.assertRaisesRegex(ValueError, "duplicate entry"):
            validate(self.data, ROOT)

    def test_unknown_amendment_remains_unknown_until_a_result_is_observed(self):
        self.entry.update(result="unknown", decision="unassessed",
                          observation="Result is not yet available.")
        later = deepcopy(self.entry)
        later.update(id="test-02", supersedes="test-01",
                     unknowns="Result still pending; receiver and retry condition established.")
        self.data["entries"].append(later)
        validate(self.data, ROOT)
        self.assertIn("observed results: 0; unknown results: 1", render(self.data))
        later.update(result="observed", decision="maintain",
                     observation="The named later result is now observed.")
        validate(self.data, ROOT)
        self.assertIn("Distinct applied executions: 1; observed results: 1", render(self.data))

    def test_card_replace_failure_preserves_existing_bytes_and_reports_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.md"
            path.write_bytes(b"existing card\n")
            path.chmod(0o640)
            with patch("scripts.rule_practice.os.replace", side_effect=OSError("simulated replace failure")):
                with self.assertRaisesRegex(OSError, "replace failure"):
                    write_card(path, "new card\n")
            self.assertEqual(b"existing card\n", path.read_bytes())
            self.assertEqual([path], list(Path(directory).iterdir()))
            write_card(path, "new card\n")
            self.assertEqual("new card\n", path.read_text())
            self.assertEqual(0o640, path.stat().st_mode & 0o777)

    def test_cli_does_not_claim_a_save_when_card_write_fails(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        before = (ROOT / CARD).read_bytes()
        with patch("sys.argv", ["rule_practice.py", "--write"]), \
                patch("scripts.rule_practice.write_card", side_effect=OSError("write unavailable")), \
                redirect_stdout(stdout), redirect_stderr(stderr):
            self.assertEqual(1, main())
        self.assertNotIn("Updated", stdout.getvalue())
        self.assertIn("UNVERIFIED practice surface", stderr.getvalue())
        self.assertEqual(before, (ROOT / CARD).read_bytes())

    def test_old_versions_and_decisions_survive_forward_revision(self):
        old = deepcopy(self.data)
        revised = deepcopy(self.data["versions"][0])
        revised["id"] = "test-v2"
        self.data["versions"].append(revised)
        self.data["current_version"] = "test-v2"
        preserve_history(old, self.data)
        validate(self.data, ROOT)
        self.assertIn("No practice assessment yet", render(self.data))
        for key in ("versions", "entries"):
            damaged = deepcopy(self.data)
            damaged[key][0]["id"] = "changed-history"
            with self.assertRaisesRegex(ValueError, "historical"):
                preserve_history(old, damaged)
        reverted = deepcopy(self.data)
        reverted["current_version"] = old["current_version"]
        with self.assertRaisesRegex(ValueError, "new version"):
            preserve_history(self.data, reverted)

    def test_version_switch_does_not_hide_attention_or_grant_human_authority(self):
        self.entry.update(issue="condition_mismatch", decision="pause", change_scope="human_judgment")
        next_version = deepcopy(self.data["versions"][0])
        next_version["id"] = "test-v2"
        self.data["versions"].append(next_version)
        self.data["current_version"] = "test-v2"
        validate(self.data, ROOT)
        card = render(self.data)
        self.assertIn("**test-01 / pause", card)
        self.assertIn("human_judgment", card)
        self.assertIn("never instructions or permission", card)

    def test_missing_evidence_and_source_drift_fail_closed(self):
        for change in ("source", "evidence"):
            data = deepcopy(self.data)
            if change == "source":
                data["versions"][0]["source"]["sha256"] = "0" * 64
            else:
                data["entries"][0]["evidence"] = ["validation/nonexistent-v214-evidence.md"]
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate(data, ROOT)

    def test_current_projection_and_next_read_route(self):
        actual = json.loads((ROOT / LEDGER).read_text())
        validate(actual, ROOT)
        self.assertEqual(render(actual), (ROOT / CARD).read_text())
        result = subprocess.run([sys.executable, "-B", "scripts/rule_practice.py", "--check", "--base", BASE],
                                cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn(CARD, (ROOT / "AGENTS.md").read_text())
        self.assertIn("../../" + LEDGER, (ROOT / CARD).read_text())
        # Named real evidence remains separate from all the in-memory synthetic cases.
        self.assertFalse(any(e["execution_id"].startswith("test:") for e in actual["entries"]))

    def test_prior_current_state_and_original_version_preserved(self):
        for path in ("docs/current_signal.md", "handoff/current_codex_handoff.md"):
            before = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
            self.assertTrue((ROOT / path).read_bytes().endswith(before), path)
        original = self.data["versions"][0]
        self.assertEqual("fn125-v1", original["id"])
        self.assertEqual(BASE, original["source"]["commit"])
        self.assertEqual("32132630bb9eaf2fe7d75cb8fe17dd9803bd1dc8504057268658ad3d9813cd53",
                         original["source"]["sha256"])

    def test_cli_rejects_stale_attention_card_and_unversioned_source_change(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(root)],
                           check=True, capture_output=True)
            data = json.loads((ROOT / LEDGER).read_text())
            source = next(v for v in data["versions"] if v["id"] == data["current_version"])["source"]["path"]
            paths = {"scripts/rule_practice.py", LEDGER, CARD, source}
            for item in data["versions"] + data["entries"]:
                paths.update(ref.split("#", 1)[0] for ref in item["evidence"])
            for path in paths:
                (root / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, root / path)

            def cli(option):
                return subprocess.run([sys.executable, "-B", "scripts/rule_practice.py", option],
                                      cwd=root, text=True, capture_output=True)

            self.assertEqual(0, cli("--check").returncode)
            issue = deepcopy(self.entry)
            issue.update(id="test-new-warning", execution_id="test:new-warning",
                         issue="counterexample", decision="revise", change_scope="operational")
            data["entries"].append(issue)
            (root / LEDGER).write_text(json.dumps(data))
            stale = cli("--check")
            self.assertEqual(1, stale.returncode)
            self.assertIn("stale card", stale.stderr)
            self.assertEqual(0, cli("--write").returncode)
            self.assertIn("**test-new-warning / revise", (root / CARD).read_text())
            self.assertEqual(0, cli("--check").returncode)
            (root / source).write_text((root / source).read_text() + "\nUnversioned change.\n")
            changed = cli("--check")
            self.assertEqual(1, changed.returncode)
            self.assertIn("bind a new version", changed.stderr)


if __name__ == "__main__":
    unittest.main()
