from __future__ import annotations

from copy import deepcopy
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from decision_os.cli import main
from tests.test_decision_os_checks import create_repository, tree_digest


class CheckOutputSafetyTests(unittest.TestCase):
    def invoke(self, payload: dict, exit_code: int = 0) -> tuple[int, dict, str]:
        output = io.StringIO()
        with patch("decision_os.cli.inspect_repository", return_value=(payload, exit_code)):
            result = main(["check", "."], stdout=output)
        text = output.getvalue()
        return result, json.loads(text), text

    def test_remote_userinfo_query_fragment_and_local_path_are_not_emitted(self) -> None:
        cases = (
            ("https://fixture-user:fixture-password@example.invalid/team/repo.git?fixture-query#fixture-fragment", "example.invalid/team/repo.git"),
            ("fixture-user@example.invalid:team/repo.git", "example.invalid/team/repo.git"),
            ("/private/fixture-local/repo", "LOCAL_PATH"),
            ("https://fixture-user:fixture-password@[invalid", "UNKNOWN"),
            ("UNKNOWN", "UNKNOWN"),
        )
        for origin, expected in cases:
            with self.subTest(expected=expected):
                payload = {"v12_state": "PASS", "v13_gate": "HOLD", "evidence": [
                    {"check": "git.repository", "status": "PASS", "source": "Git",
                     "detail": {"head": "a" * 40, "origin": origin, "root_name": "repo"}}
                ]}
                before = deepcopy(payload)
                result, observed, text = self.invoke(payload)
                self.assertEqual(0, result)
                self.assertFalse(any(value in text for value in (
                    "fixture-user", "fixture-password", "fixture-query", "fixture-fragment", "fixture-local"
                )), "private remote components reached CLI output")
                self.assertEqual(expected, observed["evidence"][0]["detail"]["origin"])
                self.assertEqual("HOLD", observed["v13_gate"])
                self.assertEqual(before, payload, "output rendering must not mutate inspection evidence")

    def test_git_failure_keeps_failure_and_exit_without_raw_stderr(self) -> None:
        payload = {"v12_state": "UNKNOWN", "v13_gate": "UNKNOWN", "evidence": [
            {"check": "git.worktree", "status": "FAIL", "source": "Git worktree",
             "detail": {"command": ["status"], "returncode": 128, "stderr": "fixture-private-diagnostic"}}
        ]}
        result, observed, text = self.invoke(payload, 3)
        self.assertEqual(3, result)
        self.assertFalse("fixture-private-diagnostic" in text, "raw diagnostic reached CLI output")
        item = observed["evidence"][0]
        self.assertEqual("FAIL", item["status"])
        self.assertEqual(128, item["detail"]["returncode"])
        self.assertEqual(["status"], item["detail"]["command"])

    def test_unexpected_exception_keeps_type_and_exit_without_body(self) -> None:
        output = io.StringIO()
        with patch("decision_os.cli.inspect_repository", side_effect=RuntimeError("fixture-private-exception")):
            result = main(["check", "."], stdout=output)
        self.assertEqual(6, result)
        self.assertFalse("fixture-private-exception" in output.getvalue(), "exception body reached CLI output")
        self.assertEqual("RuntimeError", json.loads(output.getvalue())["evidence"][0]["detail"]["type"])

    def test_real_local_check_redacts_remote_without_changing_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = create_repository(Path(directory), "complete")
            subprocess.run(("git", "-C", str(repository), "config", "remote.origin.url",
                            "https://fixture-user:fixture-password@example.invalid/team/repo.git?fixture-query#fixture-fragment"),
                           check=True, capture_output=True)
            before = tree_digest(repository)
            output = io.StringIO()
            result = main(["check", str(repository)], stdout=output)
            self.assertEqual(0, result)
            self.assertFalse(any(value in output.getvalue() for value in (
                "fixture-user", "fixture-password", "fixture-query", "fixture-fragment"
            )), "private remote components reached real CLI output")
            self.assertEqual(before, tree_digest(repository))
            payload = json.loads(output.getvalue())
            self.assertEqual("PASS", payload["v12_state"])
            self.assertEqual("GO", payload["v13_gate"])


if __name__ == "__main__":
    unittest.main()
