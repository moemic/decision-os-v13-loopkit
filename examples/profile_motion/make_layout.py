"""Make a review-only layout from the exact profile README; never edit its repo."""
import argparse
from pathlib import Path

TITLE = "## Technical Boundary Audit & Repair for AI Systems\n"
HEADING = ('<picture>\n'
           '  <source media="(max-width: 600px)" srcset="heading_mobile.gif">\n'
           '  <img src="heading.gif" alt="Technical Boundary Audit & Repair for AI Systems — softly flowing purple and cyan light">\n'
           '</picture>\n')
CREATURE = "![Round crowned black cat walking through two shockwave-and-nap scenes, exiting right and re-entering left between them](crowned_cat.gif)\n\n"
PORTFOLIO_RELATIVE = "(MERGE_PORTFOLIO.md)"
PORTFOLIO_ABSOLUTE = "(https://github.com/shin4141/shin4141/blob/cc3e38fb2cb4fc3ba339050d30fe1deef9acc425/MERGE_PORTFOLIO.md)"


def build(source):
    if not source.startswith(TITLE) or source.count(TITLE) != 1:
        raise ValueError("Expected the exact, single existing heading")
    intro, separator, body = source[len(TITLE):].partition("\n\n")
    if not separator:
        raise ValueError("Missing introductory paragraph boundary")
    if body.count(PORTFOLIO_RELATIVE) != 1:
        raise ValueError("Expected one relative portfolio link to preserve across repositories")
    # The profile source keeps its relative link; only this cross-repo preview
    # resolves it to the exact source commit so the evidence link still works.
    return (HEADING + intro + "\n\n" + CREATURE + body
            .replace(PORTFOLIO_RELATIVE, PORTFOLIO_ABSOLUTE, 1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile_readme", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.write_text(build(args.profile_readme.read_text()))
