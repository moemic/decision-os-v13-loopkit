from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
BASE = "646012d470b53609951d48938fcc78f9c6e35686"


def git(*args: str) -> bytes:
    return subprocess.check_output(("git", "-C", str(ROOT), *args))


class V209RestartSurfaceTests(unittest.TestCase):
    def test_fixed_source_manifest_resolves_to_exact_baseline_objects(self) -> None:
        manifest = json.loads((ROOT / "validation/v209_source_manifest.json").read_text())
        self.assertEqual(BASE, manifest["canonical_base"])
        self.assertEqual("shin4141/decision-os-v13-loopkit", manifest["repository"])
        self.assertEqual(23, len(manifest["sources"]))
        for entry in manifest["sources"]:
            with self.subTest(path=entry["path"]):
                self.assertEqual(BASE, entry["source_commit"])
                spec = f"{BASE}:{entry['path']}"
                data = git("show", spec)
                self.assertEqual(entry["git_blob"], git("rev-parse", spec).decode().strip())
                self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())
                self.assertEqual(entry["bytes"], len(data))
        for key in ("red_implementation_commit", "red_admission_commit"):
            git("merge-base", "--is-ancestor", manifest[key], BASE)
        changed = git(
            "diff", "94144c4a034267863963d5a81bd67bd203c8277e",
            manifest["red_admission_commit"], "--name-only",
        ).decode().splitlines()
        self.assertEqual(changed, manifest["red_repair_paths"])
        for path in changed:
            self.assertEqual(
                git("rev-parse", f"{BASE}:{path}"),
                git("rev-parse", f"{manifest['red_admission_commit']}:{path}"),
            )

    def test_original_state_and_trajectory_bytes_are_preserved(self) -> None:
        for path, boundary in (
            ("docs/current_signal.md", "current-state-history-boundary:v209-restart-security"),
            ("handoff/current_codex_handoff.md", "current-state-history-boundary:v209-restart-security"),
            ("validation/v13_13_42_closure_trajectory.md", "trajectory-history-boundary:v209-restart-security"),
        ):
            with self.subTest(path=path):
                data = (ROOT / path).read_bytes()
                original = git("show", f"{BASE}:{path}")
                self.assertEqual(1, data.count(boundary.encode()))
                self.assertTrue(data.endswith(original), "historical source bytes changed")

    def test_later_o69_record_stays_forward_of_the_history_boundary(self) -> None:
        path = ROOT / "validation/v13_13_42_closure_trajectory.md"
        data = path.read_text()
        boundary = "<!-- trajectory-history-boundary:v209-restart-security -->"
        o69 = "## O-8 / O-69 テスト境界レビュー比較の保存 — 2026-09-10"

        self.assertEqual(1, data.count(boundary))
        self.assertEqual(1, data.count(o69))
        self.assertLess(data.index(o69), data.index(boundary))

    def test_compact_restart_links_and_exact_commits_resolve(self) -> None:
        path = ROOT / "validation/v13_13_42_closure_trajectory.md"
        text = path.read_text().split("<!-- trajectory-history-boundary:v209-restart-security -->")[0]
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in target:
                continue
            relative, _, anchor = target.partition("#")
            destination = (path.parent / unquote(relative)).resolve()
            with self.subTest(target=target):
                destination.relative_to(ROOT)
                self.assertTrue(destination.is_file(), "restart source is missing")
                if anchor:
                    content = destination.read_text()
                    anchors = {
                        re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
                        for heading in re.findall(r"^#+ (.+)$", content, re.M)
                    }
                    anchors.update(re.findall(r'<a id="([^"]+)"', content))
                    self.assertIn(anchor, anchors)
        for commit in set(re.findall(r"\b[0-9a-f]{40}\b", text)):
            git("cat-file", "-e", f"{commit}^{{commit}}")
            git("merge-base", "--is-ancestor", commit, BASE)


if __name__ == "__main__":
    unittest.main()
