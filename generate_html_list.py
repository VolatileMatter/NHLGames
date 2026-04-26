#!/usr/bin/env python3
"""
generate_html_list.py
─────────────────────
Scans the /html/ directory and writes html_list.json containing a sorted
list of all .html and .htm filenames found there.

Run this from the repo root any time you add new forum HTML files:
    python generate_html_list.py

The output file (html_list.json) is read by index.html at page load.
"""

import json
import os
import sys

HTML_DIR  = "html"
OUT_FILE  = "html_list.json"


def main():
    # Verify the html/ directory exists
    if not os.path.isdir(HTML_DIR):
        print(f"[!] Directory '{HTML_DIR}/' not found. Creating it for you.")
        os.makedirs(HTML_DIR)
        print(f"[+] Created '{HTML_DIR}/'. Add your 720pier HTML files there and re-run.")
        # Write empty list so index.html doesn't break
        write_list([])
        return

    # Collect all .html / .htm files, sorted alphabetically
    files = sorted(
        f for f in os.listdir(HTML_DIR)
        if f.lower().endswith((".html", ".htm"))
    )

    if not files:
        print(f"[!] No HTML files found in '{HTML_DIR}/'. Add some and re-run.")
        write_list([])
        return

    write_list(files)
    print(f"[+] Found {len(files)} file(s) in '{HTML_DIR}/':")
    for f in files:
        print(f"      {f}")
    print(f"[+] Written to '{OUT_FILE}'.")


def write_list(files):
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(files, fh, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()