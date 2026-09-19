#!/usr/bin/env python3
"""Flag tool URLs that look like wrong matches from the automated URL fill.

Heuristic only — nothing is modified. Prints a Markdown report grouped by
reason, for manual review:

  python3 scripts/audit_urls.py > url-audit.md
  python3 scripts/audit_urls.py --check-age > url-audit.md   # also query GitHub (needs `gh auth`)

--check-age looks each repo up via the GitHub API and additionally flags repos
that return 404, were renamed/transferred, or were created more than a year
after the event (a strong sign the automated URL fill matched the wrong project).
Responses are cached in .cache/gh-repos.json so re-runs are cheap.
"""
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(REPO_ROOT, "tools")

STOPWORDS = {
    "the", "and", "for", "with", "from", "your", "into", "tool", "tools", "toolkit", "framework",
    "security", "open", "source", "platform", "based", "using", "new", "automated", "analysis",
    "attack", "attacks", "defense", "detection", "scanner", "project", "version", "beyond", "next",
    "generation", "lab", "labs", "system", "systems", "hacking", "testing", "test", "suite",
}
BAD_PATH_RE = re.compile(r"/(orgs|people|files|issues|pulls|wiki|releases|search|topics|sponsors|marketplace)(/|$)|\.pdf$", re.I)


def tokens(text):
    return {t for t in re.findall(r"[a-z0-9]{3,}", text.lower()) if t not in STOPWORDS}


def squash(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def classify(name, url):
    """Return a reason string if the URL looks suspicious, else None."""
    p = urlparse(url)
    if p.netloc != "github.com":
        return None  # non-GitHub hosts are usually deliberate (product sites); skip
    parts = [x for x in p.path.split("/") if x]
    if BAD_PATH_RE.search(p.path):
        return "path is not a repo (orgs/people/files/issues/wiki/pdf)"
    if len(parts) == 1:
        owner = parts[0]
        if tokens(owner) & tokens(name) or squash(owner) in squash(name) or squash(name) in squash(owner):
            return None
        return "user/org page whose name doesn't match the tool"
    if len(parts) < 2:
        return "malformed"
    owner, repo = parts[0], parts[1]
    name_t = tokens(name)
    repo_t = tokens(repo.replace("-", " ").replace("_", " ").replace(".", " "))
    owner_t = tokens(owner.replace("-", " ").replace("_", " "))
    sq_name, sq_repo = squash(name), squash(repo)
    if (repo_t & name_t) or (owner_t & name_t):
        return None
    if sq_repo and (sq_repo in sq_name or (len(sq_name) >= 4 and sq_name in sq_repo)):
        return None
    # CamelCase repo names: split on case boundaries and retry
    if tokens(re.sub(r"([a-z])([A-Z])", r"\1 \2", repo)) & name_t:
        return None
    return "repo name shares no word with the tool name"


CACHE_PATH = os.path.join(REPO_ROOT, ".cache", "gh-repos.json")


def gh_repo(owner_repo):
    """Return {'created': 'YYYY', 'full_name': ...} or {'status': 404} for a GitHub repo."""
    r = subprocess.run(["gh", "api", f"repos/{owner_repo}", "--jq", "{created_at: .created_at, full_name: .full_name}"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return {"status": 404 if "Not Found" in r.stderr or "404" in r.stderr else "error"}
    d = json.loads(r.stdout)
    return {"created": d["created_at"][:4], "full_name": d["full_name"]}


def lookup_repos(owner_repos):
    cache = {}
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, encoding="utf-8") as f:
            cache = json.load(f)
    todo = [x for x in owner_repos if x not in cache]
    print(f"looking up {len(todo)} repos ({len(cache)} cached)", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=4) as pool:
        for key, info in zip(todo, pool.map(gh_repo, todo)):
            cache[key] = info
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=1)
    return cache


def age_reason(url, year, cache):
    p = urlparse(url)
    parts = [x for x in p.path.split("/") if x]
    if p.netloc != "github.com" or len(parts) < 2:
        return None
    info = cache.get(f"{parts[0]}/{parts[1]}")
    if not info:
        return None
    if info.get("status") == 404:
        return "repo not found (404)"
    if info.get("status") == "error":
        return None
    if info["full_name"].lower() != f"{parts[0]}/{parts[1]}".lower():
        return f"repo was renamed/transferred (now {info['full_name']})"
    if int(info["created"]) > int(year) + 1:
        return f"repo created {info['created']}, more than a year after the {year} event"
    return None


def main():
    check_age = "--check-age" in sys.argv
    flagged = defaultdict(list)
    total = 0
    records = []
    for root, _dirs, files in sorted(os.walk(TOOLS_DIR)):
        for f in sorted(files):
            if not f.endswith(".json"):
                continue
            path = os.path.join(root, f)
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
            url = (d.get("Github URL") or "").strip()
            if not url:
                continue
            total += 1
            records.append((os.path.relpath(path, REPO_ROOT), d.get("Tool Name", ""), url, d.get("Year", "0")))

    cache = {}
    if check_age:
        keys = sorted({"/".join(urlparse(u).path.split("/")[1:3]) for _r, _n, u, _y in records
                       if urlparse(u).netloc == "github.com" and len([x for x in urlparse(u).path.split("/") if x]) >= 2})
        cache = lookup_repos(keys)

    for rel, name, url, year in records:
        reason = (age_reason(url, year, cache) if check_age else None) or classify(name, url)
        if reason:
            flagged[reason].append((rel, name, url))

    n = sum(len(v) for v in flagged.values())
    print(f"# URL accuracy audit\n\n{n} of {total} URLs flagged for manual review. "
          "Heuristics only — a flagged URL may be correct (e.g. a repo named after a codename).\n")
    for reason, rows in sorted(flagged.items(), key=lambda kv: -len(kv[1])):
        print(f"\n## {reason} ({len(rows)})\n")
        print("| File | Tool | URL |\n|---|---|---|")
        for rel, name, url in rows:
            print(f"| `{rel}` | {name} | {url} |")


if __name__ == "__main__":
    main()
