from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
LOOP_SKILL = ROOT / "loop_skills" / "ai_agent_workspace_health_check.md"
PUBLIC_DOCS = (
    ROOT / "docs" / "loop_library_ai_agent_workspace_health_check.md",
    ROOT / "docs" / "loop_library_ai_agent_workspace_health_check_submission.md",
)
RED_EXAMPLE = ROOT / "docs" / "examples" / "workspace_health_check_red_example.md"


class WorkspaceHealthRedRoutingContractTests(unittest.TestCase):
    def test_red_keeps_authorized_read_only_recovery_ai_owned(self) -> None:
        skill = LOOP_SKILL.read_text(encoding="utf-8")

        self.assertIn("An authorized read-only diagnosis", skill)
        self.assertIn("remains\n  AI-owned", skill)
        self.assertNotIn("Return seat to the human.", skill)

    def test_red_does_not_repeat_an_exact_current_repair_approval(self) -> None:
        skill = LOOP_SKILL.read_text(encoding="utf-8")

        self.assertIn("do not ask for the\n  same approval again", skill)
        self.assertIn("this\n  diagnostic loop still stops without executing it", skill)
        self.assertIn("does not by itself invalidate a matching approval", skill)

    def test_new_authority_and_unknown_state_remain_fail_closed(self) -> None:
        skill = LOOP_SKILL.read_text(encoding="utf-8")

        self.assertIn("requires new or expanded authority", skill)
        self.assertIn("returns the exact remaining decision to the Human\n  Seat", skill)
        self.assertIn("unknown, use `HOLD`", skill)
        self.assertIn("RED itself supplies none of that authority", skill)

    def test_direct_public_surfaces_preserve_the_same_routing(self) -> None:
        required = (
            "Keep authorized read-only diagnosis and evidence recovery AI-owned",
            "RED creates no repair authority",
            "unknown authority remains HOLD",
        )
        for path in PUBLIC_DOCS:
            text = path.read_text(encoding="utf-8")
            for fragment in required:
                self.assertIn(fragment, text, path)

        example = RED_EXAMPLE.read_text(encoding="utf-8")
        self.assertIn("Keep authorized read-only reconstruction with the AI", example)
        self.assertIn("the diagnostic loop does not execute it", example)
        self.assertIn("Unknown identity,\nownership, or approval remains HOLD", example)

    def test_root_authority_boundary_is_unchanged(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("Do not return routine cleanup to the Decision Owner", agents)
        self.assertIn("Ask the Decision Owner only when direction", agents)
        self.assertIn("Irreversible, public, monetary, credential-related", agents)


if __name__ == "__main__":
    unittest.main()
