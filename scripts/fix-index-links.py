#!/usr/bin/env python3
"""Fix relative links in book/index.html.

mdbook copies the first chapter's rendered HTML (chapters/00-cover.md)
to book/index.html. The copy keeps links relative to the chapters/
folder (e.g. href="./12-ceteris-paribus.html"), which is wrong once
that content lives at the book root instead of book/chapters/. This
rewrites such links to point at book/chapters/ correctly.
"""
import re
import sys
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "book"
INDEX_HTML = BOOK_DIR / "index.html"
CHAPTERS_DIR = BOOK_DIR / "chapters"


def fix_links(html: str) -> str:
    chapter_files = {p.name for p in CHAPTERS_DIR.glob("*.html")}

    def replace(match: "re.Match[str]") -> str:
        prefix, target = match.group(1), match.group(2)
        if target in chapter_files:
            return f'href="{prefix}chapters/{target}"'
        return match.group(0)

    return re.sub(r'href="(\./|)([\w.\-]+\.html)"', replace, html)


def main() -> int:
    if not INDEX_HTML.exists():
        print(f"error: {INDEX_HTML} not found", file=sys.stderr)
        return 1

    html = INDEX_HTML.read_text(encoding="utf-8")
    fixed = fix_links(html)
    INDEX_HTML.write_text(fixed, encoding="utf-8")
    print(f"fixed links in {INDEX_HTML}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
