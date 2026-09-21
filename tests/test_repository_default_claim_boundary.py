from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class RepositoryDefaultClaimBoundaryTest(unittest.TestCase):
    def test_operator_explanation_answers_the_four_boundary_questions(
        self,
    ) -> None:
        readme = read("README.md")
        guide = read("docs/verified_save_claude_mvp_v0_1.md")
        section = guide.split("## Repository Default Authority Boundary", 1)[1].split(
            "## Human Choice", 1
        )[0]
        explanation = " ".join(section.split())

        self.assertIn(
            "permission for the repository identity, mechanically derived decision type/action, and normalized exact path",
            explanation,
        )
        self.assertIn("proposed content may differ", explanation)
        self.assertIn("without showing the same diff again", explanation)
        self.assertIn(
            "does not persist or bind the exact diff, proposed content",
            explanation,
        )
        self.assertIn("docs/verified_save_claude_mvp_v0_1.md", readme)

    def test_guide_names_what_the_default_does_not_persist(self) -> None:
        guide = read("docs/verified_save_claude_mvp_v0_1.md")
        boundary = guide.split(
            "## Repository Default Authority Boundary",
            1,
        )[1].split("## Human Choice", 1)[0]

        for excluded_identity in (
            "exact diff",
            "proposed content",
            "future preimage",
            "prompt",
            "task identity",
            "purpose",
            "tool-use identity",
        ):
            self.assertIn(excluded_identity, boundary)


if __name__ == "__main__":
    unittest.main()
