#!/usr/bin/env python3
"""Print every distinct non-empty 'Github URL' from tools/**, one per line.
Used by the weekly link-check workflow; handy for ad-hoc checks too."""
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(REPO_ROOT, "tools")


def main():
    urls = set()
    for root, _dirs, files in os.walk(TOOLS_DIR):
        for f in files:
            if f.endswith(".json"):
                with open(os.path.join(root, f), encoding="utf-8") as fh:
                    url = (json.load(fh).get("Github URL") or "").strip()
                if url:
                    urls.add(url)
    print("\n".join(sorted(urls)))


if __name__ == "__main__":
    main()
