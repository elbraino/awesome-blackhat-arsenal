#!/usr/bin/env python3
"""Bring every tool file under tools/<Region>/<Year>/ into canonical form.

Content: keys in a fixed order (Tool Name, Description, Github URL, Tracks,
Speakers, Year, Location), the redundant "Event" key dropped, 2-space indent,
UTF-8 (no \\uXXXX escapes), trailing newline.

Filename: slug of the tool name, e.g. "EntraGoat - A Deliberately Vulnerable
Entra ID Environment" -> entragoat-a-deliberately-vulnerable-entra-id-environment.json
Renames go through `git mv` so history follows the file.

Idempotent — a second run changes nothing.  scripts/validate.py enforces both
the content form and the filename rule, so run this after editing a tool.

    python3 scripts/normalize.py            # whole tree
    python3 scripts/normalize.py tools/USA  # one subtree or file
"""
import json
import os
import re
import subprocess
import sys
import unicodedata

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(REPO_ROOT, "tools")

KEY_ORDER = ["Tool Name", "Description", "Github URL", "Tracks", "Speakers", "Year", "Location"]
DROP_KEYS = {"Event"}
MAX_SLUG = 80


def slug(name):
    """Filesystem- and URL-safe file stem derived from a tool name."""
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(text) > MAX_SLUG:
        text = text[:MAX_SLUG].rsplit("-", 1)[0] if "-" in text[:MAX_SLUG] else text[:MAX_SLUG]
    return text or "tool"


def canonical(data):
    """The tool dict with canonical key order and dropped keys."""
    out = {k: data[k] for k in KEY_ORDER if k in data}
    for k in data:
        if k not in out and k not in DROP_KEYS:
            out[k] = data[k]
    return out


def canonical_dump(data):
    return json.dumps(canonical(data), indent=2, ensure_ascii=False) + "\n"


def target_name(path, data, taken):
    """Canonical filename for this tool inside its directory, avoiding collisions."""
    base = slug(data.get("Tool Name", ""))
    current = os.path.basename(path)
    candidate, n = f"{base}.json", 1
    while candidate in taken and candidate != current:
        n += 1
        candidate = f"{base}-{n}.json"
    return candidate


def iter_json_files(targets):
    for target in targets:
        if os.path.isfile(target):
            yield target
            continue
        for root, _dirs, files in os.walk(target):
            for f in sorted(files):
                if f.endswith(".json"):
                    yield os.path.join(root, f)


def main(argv):
    targets = [os.path.abspath(t) for t in argv[1:]] or [TOOLS_DIR]
    rewritten = renamed = 0
    taken_by_dir = {}
    for path in sorted(iter_json_files(targets)):
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        data = json.loads(raw)
        text = canonical_dump(data)
        if text != raw:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            rewritten += 1

        d = os.path.dirname(path)
        taken = taken_by_dir.setdefault(d, set(os.listdir(d)))
        new_name = target_name(path, data, taken)
        if new_name != os.path.basename(path):
            new_path = os.path.join(d, new_name)
            subprocess.run(["git", "mv", "-f", path, new_path], check=True, cwd=REPO_ROOT)
            taken.discard(os.path.basename(path))
            taken.add(new_name)
            renamed += 1
    print(f"{rewritten} files rewritten, {renamed} files renamed")


if __name__ == "__main__":
    main(sys.argv)
