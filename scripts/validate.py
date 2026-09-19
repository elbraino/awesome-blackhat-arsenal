#!/usr/bin/env python3
"""Validate every tool JSON under tools/<Region>/<Year>/.

Usage:
    python3 scripts/validate.py            # validate everything
    python3 scripts/validate.py tools/USA  # validate a subtree or single file

Exit code is 1 if any ERROR was found. WARNINGs are informational.
Run this before opening a PR; CI runs it on every push.
"""
import ast
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalize import canonical_dump, slug  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(REPO_ROOT, "tools")

# Keep in sync with CATEGORY_MAP in AutoReadme.py (checked at runtime below).
CANONICAL_TRACKS = {
    "Exploitation and Ethical Hacking",
    "Vulnerability Assessment",
    "Web AppSec",
    "Code Assessment",
    "Network Attacks",
    "Network Defense",
    "Malware Offense",
    "Malware Defense",
    "Reverse Engineering",
    "Data Forensics/Incident Response",
    "OSINT - Open Source Intelligence",
    "Android, iOS and Mobile Hacking",
    "Hardware/Embedded",
    "Internet Of Things",
    "Smart Grid/Industrial Security",
    "Cloud Security",
    "AI, ML & Data Science",
    "Cryptography",
    "Human Factors",
    "Arsenal Lab",
}

REQUIRED_KEYS = {"Tool Name", "Description", "Github URL", "Tracks", "Speakers", "Year", "Location"}
OPTIONAL_KEYS = set()  # "Event" was dropped: Location + Year already say which event

MIN_DESCRIPTION_CHARS = 30       # error below this
SHORT_DESCRIPTION_CHARS = 80     # warning below this
LONG_DESCRIPTION_CHARS = 3000    # warning above this

GITHUB_REPO_RE = re.compile(r"^https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(/.*)?$")
GITHUB_OWNER_RE = re.compile(r"^https://github\.com/[A-Za-z0-9_.-]+$")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, path, msg):
        self.errors.append((path, msg))

    def warn(self, path, msg):
        self.warnings.append((path, msg))


def category_map_keys_from_autoreadme():
    """Read CATEGORY_MAP keys out of AutoReadme.py without importing it
    (importing would run its argparse/side effects)."""
    src_path = os.path.join(REPO_ROOT, "AutoReadme.py")
    with open(src_path, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "CATEGORY_MAP" for t in node.targets
        ):
            return {ast.literal_eval(k) for k in node.value.keys}
    return None


def validate_tool(path, data, report, raw=None):
    """Validate a single decoded tool object. Returns the lowercase tool name (for duplicate checks)."""
    rel = os.path.relpath(path, REPO_ROOT)
    year_dir = os.path.basename(os.path.dirname(path))
    region = os.path.basename(os.path.dirname(os.path.dirname(path)))

    if not isinstance(data, dict):
        report.error(rel, "top-level value must be a JSON object")
        return None

    if raw is not None and raw != canonical_dump(data):
        report.error(rel, "not in canonical form (key order/indent/escapes); run `python3 scripts/normalize.py`")

    keys = set(data)
    for k in sorted(REQUIRED_KEYS - keys):
        report.error(rel, f"missing required key {k!r}")
    for k in sorted(keys - REQUIRED_KEYS - OPTIONAL_KEYS):
        report.error(rel, f"unknown key {k!r} (allowed: {sorted(REQUIRED_KEYS | OPTIONAL_KEYS)})")

    name = data.get("Tool Name")
    if not isinstance(name, str) or not name.strip():
        report.error(rel, "'Tool Name' must be a non-empty string")
        name = None

    desc = data.get("Description")
    if not isinstance(desc, str) or not desc.strip():
        report.error(rel, "'Description' must be a non-empty string")
    else:
        n = len(desc.strip())
        if n < MIN_DESCRIPTION_CHARS:
            report.error(rel, f"'Description' too short ({n} chars, min {MIN_DESCRIPTION_CHARS})")
        elif n < SHORT_DESCRIPTION_CHARS:
            report.warn(rel, f"'Description' is short ({n} chars)")
        elif n > LONG_DESCRIPTION_CHARS:
            report.warn(rel, f"'Description' is long ({n} chars); consider trimming to the first paragraph")

    url = data.get("Github URL")
    if not isinstance(url, str):
        report.error(rel, "'Github URL' must be a string (use \"\" when unknown)")
    else:
        url_s = url.strip()
        if url_s != url:
            report.error(rel, "'Github URL' has surrounding whitespace")
        if url_s:
            if re.search(r"\s", url_s):
                report.error(rel, "'Github URL' contains whitespace")
            elif not url_s.startswith("https://"):
                report.error(rel, f"'Github URL' must start with https:// (got {url_s!r})")
            elif url_s.startswith("https://github.com/"):
                if url_s.endswith("/"):
                    report.error(rel, "'Github URL' has a trailing slash")
                elif GITHUB_OWNER_RE.match(url_s):
                    report.warn(rel, "'Github URL' points to a user/org page, not a repo")
                elif not GITHUB_REPO_RE.match(url_s):
                    report.error(rel, f"'Github URL' is not a valid GitHub repo URL: {url_s!r}")
                elif re.match(r"^https://github\.com/[^/]+/[^/]+/(blob|tree|raw)/", url_s):
                    report.warn(rel, "'Github URL' points inside a repo (blob/tree); prefer the repo root")
            else:
                report.warn(rel, f"'Github URL' is not on github.com: {url_s}")

    tracks = data.get("Tracks")
    if not isinstance(tracks, list):
        report.error(rel, "'Tracks' must be a list (use [] if unknown)")
    else:
        for t in tracks:
            if not isinstance(t, str):
                report.error(rel, f"'Tracks' entry is not a string: {t!r}")
            elif t not in CANONICAL_TRACKS:
                report.error(rel, f"unknown track {t!r}; see CONTRIBUTING.md for the valid names")
        if len(set(tracks)) != len(tracks):
            report.error(rel, "'Tracks' has duplicate entries")
        if not tracks:
            report.warn(rel, "'Tracks' is empty; tool will be listed under 'Others'")

    speakers = data.get("Speakers")
    if not isinstance(speakers, list):
        report.error(rel, "'Speakers' must be a list (use [] if unknown)")
    else:
        for s in speakers:
            if not isinstance(s, str) or not s.strip():
                report.error(rel, f"'Speakers' entry must be a non-empty string: {s!r}")
        if len(set(speakers)) != len(speakers):
            report.error(rel, "'Speakers' has duplicate entries")
        if not speakers:
            report.warn(rel, "'Speakers' is empty")

    year = data.get("Year")
    if not isinstance(year, str) or not re.fullmatch(r"20\d{2}", year):
        report.error(rel, f"'Year' must be a 4-digit year string (got {year!r})")
    elif year != year_dir:
        report.error(rel, f"'Year' {year!r} does not match folder {year_dir!r}")

    location = data.get("Location")
    if not isinstance(location, str) or not location.strip():
        report.error(rel, f"'Location' must be a non-empty string (got {location!r})")
    elif location != region:
        report.error(rel, f"'Location' {location!r} does not match folder {region!r}")

    if name:
        expected = slug(name)
        actual = os.path.basename(path)
        if not re.fullmatch(re.escape(expected) + r"(-\d+)?\.json", actual):
            report.error(rel, f"filename should be {expected}.json (run `python3 scripts/normalize.py`)")

    return name.strip().lower() if name else None


def iter_json_files(targets):
    for target in targets:
        if os.path.isfile(target):
            yield target
            continue
        for root, _dirs, files in os.walk(target):
            for f in sorted(files):
                if f.endswith(".json"):
                    yield os.path.join(root, f)


def run(targets):
    report = Report()

    auto_keys = category_map_keys_from_autoreadme()
    if auto_keys is None:
        report.error("AutoReadme.py", "could not find CATEGORY_MAP")
    elif auto_keys != CANONICAL_TRACKS:
        report.error(
            "AutoReadme.py",
            f"CATEGORY_MAP keys differ from scripts/validate.py CANONICAL_TRACKS: "
            f"only in AutoReadme={sorted(auto_keys - CANONICAL_TRACKS)}, "
            f"only in validate={sorted(CANONICAL_TRACKS - auto_keys)}",
        )

    names_by_dir = defaultdict(list)
    count = 0
    for path in iter_json_files(targets):
        count += 1
        rel = os.path.relpath(path, REPO_ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
            data = json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            report.error(rel, f"invalid JSON: {e}")
            continue
        name = validate_tool(path, data, report, raw=raw)
        if name:
            names_by_dir[os.path.dirname(path)].append((name, rel))

    for d, entries in names_by_dir.items():
        seen = {}
        for name, rel in entries:
            if name in seen:
                report.error(rel, f"duplicate 'Tool Name' in same event (also in {seen[name]})")
            else:
                seen[name] = rel

    return count, report


def main(argv):
    targets = argv[1:] or [TOOLS_DIR]
    targets = [os.path.abspath(t) for t in targets]
    for t in targets:
        if not os.path.exists(t):
            print(f"error: no such path: {t}")
            return 2

    count, report = run(targets)

    for path, msg in report.warnings:
        print(f"WARN  {path}: {msg}")
    for path, msg in report.errors:
        print(f"ERROR {path}: {msg}")

    print(f"\n{count} files checked: {len(report.errors)} errors, {len(report.warnings)} warnings")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
