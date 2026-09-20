"""Make a review-only layout from the exact profile README; never edit its repo."""
import argparse
from pathlib import Path

TITLE = "## Technical Boundary Audit & Repair for AI Systems\n"
HEADING = ('<picture>\n'
           '  <source media="(max-width: 600px)" srcset="heading_mobile.gif">\n'
           '  <img src="heading.gif" alt="Technical Boundary Audit & Repair for AI Systems — softly flowing purple and cyan light">\n'
           '</picture>\n')
CREATURE = "![Crowned black cat visiting contribution cells; decorative glow over a dated activity snapshot](crowned_cat.gif)\n\n"


def build(source):
    if not source.startswith(TITLE) or source.count(TITLE) != 1:
        raise ValueError("Expected the exact, single existing heading")
    intro, separator, body = source[len(TITLE):].partition("\n\n")
    if not separator:
        raise ValueError("Missing introductory paragraph boundary")
    return HEADING + intro + "\n\n" + CREATURE + body


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile_readme", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.write_text(build(args.profile_readme.read_text()))
