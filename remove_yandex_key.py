#!/usr/bin/env python3
"""
remove_yandex_key.py
─────────────────────
Strips the Yandex.Translate API key from all HTML files in /html/.

GitHub push protection blocks commits containing this key. This script
removes the entire line containing the key so the files are safe to commit.

The line it targets looks like:
    var S_YK = 'trnsl.1.1.XXXXXXX...';

Run from the repo root:
    python remove_yandex_key.py

Then re-add and amend your commit:
    git add html/
    git commit --amend --no-edit
    git push origin main
"""

import os
import re

HTML_DIR = "html"
# Matches the Yandex key assignment line in any whitespace/quote variation
YANDEX_PATTERN = re.compile(r".*S_YK\s*=\s*['\"]trnsl\.[^'\"]+['\"].*\n?")


def scrub_file(filepath: str) -> bool:
    """Remove Yandex key line(s) from a single file. Returns True if modified."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        original = f.read()

    cleaned = YANDEX_PATTERN.sub("", original)

    if cleaned == original:
        return False  # Nothing to do

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(cleaned)
    return True


def main():
    if not os.path.isdir(HTML_DIR):
        print(f"[!] Directory '{HTML_DIR}/' not found. Nothing to do.")
        return

    html_files = [
        f for f in os.listdir(HTML_DIR)
        if f.lower().endswith((".html", ".htm"))
    ]

    if not html_files:
        print(f"[!] No HTML files found in '{HTML_DIR}/'. Nothing to do.")
        return

    modified = []
    skipped  = []

    for filename in sorted(html_files):
        filepath = os.path.join(HTML_DIR, filename)
        if scrub_file(filepath):
            modified.append(filename)
            print(f"  [cleaned] {filename}")
        else:
            skipped.append(filename)
            print(f"  [clean]   {filename}  (no key found)")

    print()
    print(f"Done. {len(modified)} file(s) modified, {len(skipped)} already clean.")

    if modified:
        print()
        print("Next steps to fix your blocked push:")
        print("  git add html/")
        print("  git commit --amend --no-edit")
        print("  git push origin main")


if __name__ == "__main__":
    main()