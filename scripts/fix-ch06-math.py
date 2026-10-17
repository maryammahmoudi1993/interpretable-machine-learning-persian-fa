#!/usr/bin/env python3
"""One-off fix for chapter 6 math formatting.

mdbook's CommonMark parser (pulldown-cmark) interprets stray
underscores inside $$...$$ / $...$ as markdown emphasis delimiters
(turning e.g. `x^{(i)}_{1} ... x^{(i)}_{2}` into
`x^{(i)}<em>{1} ... x^{(i)}</em>{2}`), and collapses doubled
backslashes (`\\\\`, used for LaTeX row breaks) and `\\!` (thin
space) down to a single character because CommonMark treats a
backslash followed by ASCII punctuation as an escape sequence.

This rewrites every math span in chapters/06-linear-regression.md
(and its src/ copy) so that, after CommonMark's escape processing,
MathJax still receives literal underscores and backslashes.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [
    ROOT / "chapters" / "06-linear-regression.md",
    ROOT / "src" / "chapters" / "06-linear-regression.md",
]


def fix_math(m: "re.Match[str]") -> str:
    s = m.group(0)
    s = s.replace("\\\\", "\\\\\\\\")  # \\  -> \\\\  (survives as \\)
    s = s.replace("\\!", "\\\\!")      # \!  -> \\!   (survives as \!)
    s = s.replace("_", "\\_")          # _   -> \_    (survives as literal _)
    return s


def fix_text(text: str) -> str:
    text = re.sub(r"\$\$.*?\$\$", fix_math, text, flags=re.DOTALL)
    text = re.sub(r"(?<!\$)\$(?!\$)[^$\n]+?\$(?!\$)", fix_math, text)
    return text


def main() -> int:
    for path in TARGETS:
        if not path.exists():
            print(f"error: {path} not found", file=sys.stderr)
            return 1
        original = path.read_text(encoding="utf-8")
        fixed = fix_text(original)
        path.write_text(fixed, encoding="utf-8")
        print(f"fixed {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
