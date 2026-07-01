#!/usr/bin/env python3
"""Fix math rendering across all chapters — idempotent.

mdbook's CommonMark parser (pulldown-cmark) breaks LaTeX inside
$$...$$ / $...$ math spans in three ways:
  1. Paired underscores  ->  parsed as <em>...</em> emphasis
  2. \\  (LaTeX row break) ->  collapsed to single backslash
  3. \\!  (thin space)    ->  collapsed to literal !

Fix (safe to run multiple times):
  - Escape unescaped underscores as \\_ (lookbehind prevents double-escaping)
  - Double unescaped backslash-punctuation pairs (lookbehind prevents re-doubling)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIRS = [ROOT / "src" / "chapters", ROOT / "chapters"]


def fix_math_span(m: "re.Match[str]") -> str:
    s = m.group(0)
    # Double any single backslash before ! or \ that is not already doubled.
    # Negative lookbehind ensures we don't turn \\\\ -> \\\\\\\\
    s = re.sub(r"(?<!\\)\\([!\\])", r"\\\\\1", s)
    # Escape underscores not already preceded by a backslash.
    s = re.sub(r"(?<!\\)_", r"\\_", s)
    return s


def fix_text(text: str) -> str:
    text = re.sub(r"\$\$.*?\$\$", fix_math_span, text, flags=re.DOTALL)
    text = re.sub(r"(?<!\$)\$(?!\$)[^$\n]+?\$(?!\$)", fix_math_span, text)
    return text


def main() -> int:
    changed = 0
    errors = 0
    for src_dir in SRC_DIRS:
        if not src_dir.exists():
            print(f"skip (not found): {src_dir}")
            continue
        for path in sorted(src_dir.glob("*.md")):
            try:
                original = path.read_text(encoding="utf-8")
                fixed = fix_text(original)
                if fixed != original:
                    path.write_text(fixed, encoding="utf-8")
                    print(f"  fixed  {path.relative_to(ROOT)}")
                    changed += 1
                else:
                    print(f"  ok     {path.relative_to(ROOT)}")
            except Exception as e:
                print(f"  ERROR  {path}: {e}", file=sys.stderr)
                errors += 1
    print(f"\n{changed} file(s) updated, {errors} error(s).")
    return errors


if __name__ == "__main__":
    raise SystemExit(main())
