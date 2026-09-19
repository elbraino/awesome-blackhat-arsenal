"""One-off data cleanup for Tier 2 of the improvement roadmap (safe subset).

- Description: strip, collapse embedded newlines / runs of whitespace to one
  space, and put a space after a full stop where two sentences were glued
  together by scraping ("...Directory.We propose" -> "...Directory. We propose").
  Tokens that look like URLs, dotted identifiers (java.lang.String) or
  CamelCase.Names (or ACRONYMS.Followed by a word) are left alone.
- Repair mojibake (UTF-8 read as Latin-1) in names, speakers and descriptions.
- Github URL: reduce links into a repo (/blob/, /tree/, /raw/) to the repo root.

Only files whose content changes are rewritten, preserving each file's style.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fix_tier0_data import dump_like  # noqa: E402

TOOLS_GLOB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools", "*", "*")

GLUED_RE = re.compile(r"^(\S*?[a-z0-9)])\.([A-Z][a-z]+.*)$")
INSIDE_REPO_RE = re.compile(r"^(https://github\.com/[^/]+/[^/]+)/(blob|tree|raw)/.*$")


def _unglue_token(tok):
    """'Directory.We' -> 'Directory. We'; leaves URLs, dotted.identifiers and CamelCase.Names alone."""
    if "://" in tok or tok.count(".") != 1:
        return tok
    m = GLUED_RE.match(tok)
    if not m or re.search(r"[A-Z]", m.group(1)[1:]):
        return tok
    return f"{m.group(1)}. {m.group(2)}"


def normalize_description(text):
    text = re.sub(r"\s*\n\s*", " ", text.strip())
    text = re.sub(r"[ \t]{2,}", " ", text)
    return " ".join(_unglue_token(tok) for tok in text.split(" "))


def fix_mojibake(text):
    """Repair UTF-8 text that was decoded as Latin-1 once ('LÃ³pez' -> 'López')."""
    if not isinstance(text, str) or not re.search(r"[ÃÂ][\x80-\xbf]", text):
        return text
    try:
        return text.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def fix(tool):
    changed = False
    for key in ("Tool Name", "Description"):
        if fix_mojibake(tool.get(key)) != tool.get(key):
            tool[key] = fix_mojibake(tool[key])
            changed = True
    if isinstance(tool.get("Speakers"), list):
        fixed = [fix_mojibake(x) for x in tool["Speakers"]]
        if fixed != tool["Speakers"]:
            tool["Speakers"] = fixed
            changed = True
    desc = tool.get("Description")
    if isinstance(desc, str):
        new = normalize_description(desc)
        if new != desc:
            tool["Description"] = new
            changed = True
    url = tool.get("Github URL")
    if isinstance(url, str):
        m = INSIDE_REPO_RE.match(url)
        if m:
            tool["Github URL"] = m.group(1)
            changed = True
    return changed


def main():
    touched = 0
    paths = sorted(glob.glob(TOOLS_GLOB + "/*.json") + glob.glob(TOOLS_GLOB + "/.*.json"))
    for path in paths:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        data = json.loads(raw)
        if fix(data):
            with open(path, "w", encoding="utf-8") as f:
                f.write(dump_like(data, raw))
            touched += 1
    print(f"{touched} of {len(paths)} files updated")


if __name__ == "__main__":
    main()
