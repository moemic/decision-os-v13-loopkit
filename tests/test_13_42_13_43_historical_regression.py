from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest

from decision_os.checks import EXIT_OK, inspect_repository
from decision_os.state import first_fenced_block, parse_fields


REPO_ROOT = Path(__file__).resolve().parents[1]
SURFACES = (
    "docs/current_signal.md",
    "handoff/current_codex_handoff.md",
)
HISTORY_HEADERS = {
    "docs/current_signal.md": (
        b"# Current Signal \xe2\x80\x94 V13 Compact Test Output Reference "
        b"Implementation\n"
    ),
    "handoff/current_codex_handoff.md": (
        b"# Current Codex Handoff \xe2\x80\x94 V13 Compact Test Output Reference "
        b"Implementation\n"
    ),
}
PRE_13_42_CLOSURE_SHA256 = {
    "docs/current_signal.md": (
        "fc24d6ad23c5dc6895b5b8ad214c1765a5cac9434edf320e84df15c828da6089"
    ),
    "handoff/current_codex_handoff.md": (
        "d3dfe6700bdf7d6cf9c083f674626ebe73b2ccb345f8504425e1cd5a5561e511"
    ),
}
V209_RECONSTRUCTION_BASE = "5be89c84d1816a2b185cc2f6e85869a9f1e73d11"
CURRENT_RECONSTRUCTION_BASE = "42e406e858b05b6b8aff5cc6669cf10ad506b424"
V215_ADMITTED_MAIN = "49b27e521f8a29312a6e0767c4c0f19483d999fb"
V216_HISTORY_BOUNDARY = "<!-- current-state-history-boundary:v216-profile-motion-001 -->"
READER_ENTRY_BOUNDARY = (
    "<!-- current-state-history-boundary:conversation-recycle-reader-entry -->"
)


def current_block(relative_path: str) -> str:
    text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
    block = first_fenced_block(text)
    if block is None:
        raise AssertionError(f"{relative_path}: first fenced block is absent")
    return block


def v215_historical_block(relative_path: str) -> str:
    text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
    if text.count(V216_HISTORY_BOUNDARY) != 1:
        raise AssertionError(f"{relative_path}: V216 history boundary is not unique")
    block = first_fenced_block(text.split(V216_HISTORY_BOUNDARY, 1)[1])
    if block is None:
        raise AssertionError(f"{relative_path}: V215 historical block is absent")
    return block


def run_git(cwd: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ("git", "-C", str(cwd), *arguments),
        capture_output=True,
        check=True,
        text=True,
    )


class Historical13_42And13_43RegressionTests(unittest.TestCase):
    def test_fresh_reader_recovers_the_repaired_frontier_from_first_blocks(self) -> None:
        signal_block, handoff_block = [current_block(path) for path in SURFACES]
        self.assertEqual(signal_block, handoff_block)

        fields = parse_fields(signal_block)
        # Only the AGENTS admission fields are universal at a future frontier.
        # V215-specific reader and distribution fields are asserted below as
        # fixed history, not imposed on the new V216 first block.
        required_fields = {
            "canonical_reconstruction_base",
            "current_canonical_main",
            "current_layer",
            "v12_state",
            "completed_work",
            "canonical_current_capability",
            "current_restart_point",
            "active_branch",
            "current_gate",
            "completion_line",
            "missing_closure",
            "next_authorized_action",
            "not_authorized",
            "decision_owner",
            "admission_joint",
            "admission_evidence",
            "remote_read_back",
            "older_material_below",
        }
        self.assertEqual(set(), required_fields.difference(fields))
        relationship = subprocess.run(
            ("git", "-C", str(REPO_ROOT), "merge-base", "--is-ancestor",
             fields["canonical_reconstruction_base"][0], "HEAD"),
            capture_output=True, check=False, text=True,
        )
        self.assertEqual(0, relationship.returncode, relationship.stderr)
        self.assertTrue(fields["current_gate"][0].startswith("HOLD"))
        self.assertEqual("Shin", fields["decision_owner"][0])
        self.assertIn("HISTORICAL ONLY", fields["older_material_below"][0])

    def test_v215_specific_reader_contract_is_exact_preserved_history(self) -> None:
        observed = [v215_historical_block(path) for path in SURFACES]
        self.assertEqual(observed[0], observed[1])
        for relative_path, block in zip(SURFACES, observed):
            fixed = first_fenced_block(run_git(
                REPO_ROOT, "show", f"{V215_ADMITTED_MAIN}:{relative_path}"
            ).stdout)
            self.assertEqual(fixed, block)
        fields = parse_fields(observed[0])
        self.assertEqual(CURRENT_RECONSTRUCTION_BASE,
                         fields["canonical_reconstruction_base"][0])
        self.assertIn("readers may follow the README path",
                      fields["next_authorized_action"][0])
        self.assertIn("not automatically Shin",
                      fields["reader_workspace_decision_owner"][0])
        self.assertTrue(fields["companion_status"][0].startswith("UNDER DEVELOPMENT"))
        self.assertIn("one fresh isolated Codex task",
                      fields["runtime_evidence_boundary"][0])
        self.assertIn("reader_ownership_boundary", fields)

    def test_repository_check_reads_only_the_new_current_authority(self) -> None:
        payload, exit_code = inspect_repository(REPO_ROOT)
        self.assertEqual(EXIT_OK, exit_code)
        fields = parse_fields(current_block(SURFACES[0]))
        self.assertEqual(fields["v12_state"][0].split()[0], payload["v12_state"])
        self.assertEqual(fields["current_gate"][0].split()[0], payload["v13_gate"])
        self.assertEqual(fields["next_authorized_action"][0],
                         payload["next_authorized_action"])

    def test_reconstruction_base_is_real_and_ancestral(self) -> None:
        completed = subprocess.run(
            ("git", "-C", str(REPO_ROOT), "merge-base", "--is-ancestor", CURRENT_RECONSTRUCTION_BASE, "HEAD"),
            capture_output=True,
            check=False,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        title = subprocess.run(
            ("git", "-C", str(REPO_ROOT), "show", "-s", "--format=%s", CURRENT_RECONSTRUCTION_BASE),
            capture_output=True,
            check=True,
            text=True,
        ).stdout.strip()
        self.assertIn("Merge pull request #160", title)

    def test_post_merge_reader_on_origin_main_recovers_steady_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "source"
            remote = parent / "remote.git"
            reader = parent / "reader"

            run_git(parent, "init", "-b", "main", str(source))
            run_git(source, "config", "user.name", "Current State Test")
            run_git(source, "config", "user.email", "current-state@example.invalid")
            for relative_path in SURFACES:
                target = source / relative_path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((REPO_ROOT / relative_path).read_bytes())
            run_git(source, "add", "--", *SURFACES)
            run_git(source, "commit", "-m", "admit current state")

            run_git(parent, "init", "--bare", str(remote))
            run_git(remote, "symbolic-ref", "HEAD", "refs/heads/main")
            run_git(source, "remote", "add", "origin", str(remote))
            run_git(source, "push", "-u", "origin", "main")
            run_git(parent, "clone", str(remote), str(reader))
            run_git(reader, "fetch", "origin", "main")

            observed_head = run_git(reader, "rev-parse", "origin/main").stdout.strip()
            observed_blocks = []
            observed_texts = []
            for relative_path in SURFACES:
                text = run_git(
                    reader,
                    "show",
                    f"origin/main:{relative_path}",
                ).stdout
                block = first_fenced_block(text)
                self.assertIsNotNone(block)
                observed_blocks.append(block)
                observed_texts.append(text)

        self.assertEqual(observed_blocks[0], observed_blocks[1])
        self.assertNotEqual(V215_ADMITTED_MAIN, observed_head)
        self.assertEqual(current_block(SURFACES[0]), observed_blocks[0])
        fields = parse_fields(observed_blocks[0] or "")
        self.assertIn("current_canonical_main", fields)
        self.assertTrue(fields["current_gate"][0].startswith("HOLD"))
        # Synthetic transport/read-back proves the new first pair survives a
        # main clone; it does not promote the real PR. Exact fetched origin/main
        # identity and reconstruction-base ancestry remain separate admission
        # requirements in test_current_state_admission.py and AGENTS.md.
        for relative_path, text in zip(SURFACES, observed_texts):
            self.assertEqual(1, text.count(V216_HISTORY_BOUNDARY))
            history = first_fenced_block(text.split(V216_HISTORY_BOUNDARY, 1)[1])
            self.assertEqual(v215_historical_block(relative_path), history)

    def test_v209_frontier_remains_exact_history_below_reader_entry(self) -> None:
        historical_blocks = []
        for relative_path in SURFACES:
            with self.subTest(relative_path=relative_path):
                text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                self.assertEqual(1, text.count(READER_ENTRY_BOUNDARY))
                history = text.split(READER_ENTRY_BOUNDARY, 1)[1]
                block = first_fenced_block(history)
                self.assertIsNotNone(block)

                fixed_text = run_git(
                    REPO_ROOT,
                    "show",
                    f"{CURRENT_RECONSTRUCTION_BASE}:{relative_path}",
                ).stdout
                fixed_block = first_fenced_block(fixed_text)
                self.assertEqual(fixed_block, block)
                historical_blocks.append(block or "")

        self.assertEqual(historical_blocks[0], historical_blocks[1])
        fields = parse_fields(historical_blocks[0])
        self.assertEqual(
            V209_RECONSTRUCTION_BASE,
            fields["canonical_reconstruction_base"][0],
        )
        self.assertIn("13-43", fields["next_authorized_action"][0])
        self.assertTrue(fields["value_port"][0].startswith("EXTERNAL OWNERSHIP"))
        self.assertIn(
            "Handoff is not complete until the receiving AI knows what it now owns.",
            historical_blocks[0],
        )
        self.assertIn("codex/13-42-closure-13-43-handoff", historical_blocks[0])
        self.assertIn("Value-Locked side", historical_blocks[0])

    def test_pre_13_42_closure_surfaces_remain_byte_preserved_history(self) -> None:
        for relative_path in SURFACES:
            with self.subTest(relative_path=relative_path):
                contents = (REPO_ROOT / relative_path).read_bytes()
                boundary = (
                    b"<!-- current-state-history-boundary:"
                    b"v13-13-42-closure -->\n"
                )
                self.assertEqual(1, contents.count(boundary))
                history_offset = contents.index(HISTORY_HEADERS[relative_path])
                history = contents[history_offset:]
                self.assertEqual(
                    PRE_13_42_CLOSURE_SHA256[relative_path],
                    hashlib.sha256(history).hexdigest(),
                )
                disclaimer = contents[:history_offset]
                self.assertIn(
                    b"cannot be inherited as current authority",
                    disclaimer,
                )
                self.assertIn(b"Next Authorized Action:", history)

    def test_13_43_handoff_transfers_responsibility_without_starting_work(self) -> None:
        handoff = (REPO_ROOT / "handoff/current_codex_handoff.md").read_text(
            encoding="utf-8"
        )
        transfer = handoff.split("## 13-43 Responsibility Transfer", 1)[1].split(
            "<!-- current-state-history-boundary:v13-13-42-closure -->", 1
        )[0]
        for required in (
            "Target Layer:",
            "Repo Root:",
            "Current State:",
            "Current Gate:",
            "Completion Line:",
            "Missing Closure:",
            "Next Owner:",
            "What the Receiving AI Now Owns:",
            "First One Action:",
            "Do Not Continue Boundary:",
            "What must not be inferred:",
            "Value port:",
            "Article:",
            "Operational cleanup that must not be returned to Shin:",
        ):
            self.assertIn(required, transfer)
        self.assertIn(
            "Handoff is not complete until the receiving AI knows what it now owns.",
            transfer,
        )
        self.assertIn("HOLD", transfer)
        self.assertIn("Value-Locked side", transfer)
        self.assertIn("do not begin implementation", transfer)

if __name__ == "__main__":
    unittest.main()
