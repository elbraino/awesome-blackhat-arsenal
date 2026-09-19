#!/usr/bin/env python3
"""Generate every derived file from tools/<Region>/<Year>/*.json:

  README.md                       root index
  tools/<Region>/<Year>/README.md one page per event, grouped by category
  tools/BY_CATEGORY.md            every tool, grouped by track, across all events
  tools/BY_NAME.md                every tool A–Z, with all events it was presented at
  tools.json, tools.csv           machine-readable aggregate

Output is deterministic (sorted, no timestamps) so CI can diff it.

  python3 AutoReadme.py                          # regenerate everything
  python3 AutoReadme.py --event USA --year 2026  # only rewrite that event page
                                                 # (indexes and root are always full)
"""
import argparse
import csv
import json
import os
import re
from collections import defaultdict

# -------------------------------
# 🔧 Configuration & Constants
# -------------------------------
ROOT_DIR = "tools"                # Root directory containing event/year folders
MAIN_README = "README.md"         # Path for the main README
BY_CATEGORY = os.path.join(ROOT_DIR, "BY_CATEGORY.md")
BY_NAME = os.path.join(ROOT_DIR, "BY_NAME.md")
TOOLS_JSON = "tools.json"
TOOLS_CSV = "tools.csv"

# Track → (Category label, badge colour).  Keys are the 20 canonical track names;
# scripts/validate.py reads this dict by name to check they stay in sync.
CATEGORY_MAP = {
    "Exploitation and Ethical Hacking": ("🔴 Red Teaming", "red"),
    "Malware Offense": ("🔴 Red Teaming", "red"),
    "Network Attacks": ("🔴 Red Teaming", "red"),
    "Reverse Engineering": ("🧠 Reverse Engineering", "orange"),
    "OSINT - Open Source Intelligence": ("🔍 OSINT", "lightgrey"),
    "Internet Of Things": ("🟣 Red Teaming / Embedded", "purple"),
    "Code Assessment": ("🌐 Web/AppSec or Red Teaming", "blue"),
    "Web AppSec": ("🌐 Web/AppSec", "blue"),
    "Vulnerability Assessment": ("🔴 Red Teaming / AppSec", "red"),
    "Smart Grid/Industrial Security": ("🟣 Red Teaming / Embedded", "purple"),
    "Android, iOS and Mobile Hacking": ("📱 Mobile Security", "yellow"),
    "Cryptography": ("🔵 Blue Team & Detection", "cyan"),
    "Network Defense": ("🔵 Blue Team & Detection", "cyan"),
    "Malware Defense": ("🔵 Blue Team & Detection", "cyan"),
    "Data Forensics/Incident Response": ("🔵 Blue Team & Detection", "cyan"),
    "Arsenal Lab": ("⚙️ Miscellaneous / Lab Tools", "gray"),
    "Human Factors": ("🧠 Social Engineering / General", "pink"),
    "AI, ML & Data Science": ("🤖 AI, ML & Data Science", "brightgreen"),
    "Hardware/Embedded": ("🟣 Red Teaming / Embedded", "purple"),
    "Cloud Security": ("☁️ Cloud Security", "blue"),
}
OTHERS = "Others"

# -------------------------------
# 🧩 Utility Functions
# -------------------------------

def category_for(tracks):
    """First canonical track decides the category; no tracks → Others."""
    for track in tracks:
        if track in CATEGORY_MAP:
            return CATEGORY_MAP[track][0]
    return OTHERS


def sanitize_anchor(text):
    """Converts heading text to the anchor slug GitHub generates for it.

    GitHub lowercases, drops everything except letters, digits, spaces,
    hyphens and underscores (so emoji and punctuation vanish), then turns
    spaces into hyphens. Consecutive hyphens are kept.
    """
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.replace(" ", "-")


def md_escape(text):
    """Escape characters that would break a Markdown list line."""
    return text.replace("|", "\\|").replace("\n", " ")


def link_line(url):
    return f"🔗 **Link:** [{url}]({url})" if url else "🔗 **Link:** Not Available"


def write(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip("\n") + "\n")


def die(msg, code=1):
    print(msg)
    raise SystemExit(code)


# -------------------------------
# 📥 Load
# -------------------------------

def load_tools():
    """Every tool as a flat record, sorted by (location, year, name)."""
    records = []
    for location in sorted(os.listdir(ROOT_DIR)):
        loc_path = os.path.join(ROOT_DIR, location)
        if not os.path.isdir(loc_path):
            continue
        for year in sorted(os.listdir(loc_path)):
            year_path = os.path.join(loc_path, year)
            if not os.path.isdir(year_path):
                continue
            for file in os.listdir(year_path):
                if not file.endswith(".json"):
                    continue
                path = os.path.join(year_path, file)
                with open(path, encoding="utf-8") as f:
                    try:
                        tool = json.load(f)
                    except json.JSONDecodeError as e:
                        die(f"Error while loading JSON file '{path}': {e}")
                speakers = tool.get("Speakers") or []
                tracks = tool.get("Tracks") or []
                records.append({
                    "location": location,
                    "year": year,
                    "path": path.replace(os.sep, "/"),
                    "name": (tool.get("Tool Name") or "Unnamed Tool").strip(),
                    "url": (tool.get("Github URL") or "").strip(),
                    "description": (tool.get("Description") or "No description provided.").strip(),
                    "tracks": [t for t in tracks if isinstance(t, str)],
                    "speakers": [s for s in speakers if isinstance(s, str)],
                })
    records.sort(key=lambda r: (r["location"], r["year"], r["name"].lower(), r["path"]))
    return records


# -------------------------------
# 📄 Event page
# -------------------------------

def render_event_readme(location, year, records):
    by_category = defaultdict(list)
    for r in records:
        by_category[category_for(r["tracks"])].append(r)

    lines = [
        f"# {location} {year}",
        "---",
        f"📍 {len(records)} tools demonstrated at **Black Hat Arsenal {location} {year}**, "
        "grouped by track category. Expand a tool for its description.",
        "",
        "See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · "
        "[main index](../../../README.md)",
        "",
        "## 📚 Contents",
    ]
    for cat in sorted(by_category):
        lines.append(f"- [{cat}](#{sanitize_anchor(cat)}) ({len(by_category[cat])})")
    lines.append("---")

    for cat in sorted(by_category):
        lines.append(f"## {cat}")
        for r in by_category[cat]:
            speakers = ", ".join(r["speakers"])
            summary = f"<strong>{r['name']}</strong>" + (f" — {speakers}" if speakers else "")
            tracks = " · ".join(r["tracks"]) if r["tracks"] else "—"
            lines.append(
                f"<details><summary>{summary}</summary>\n\n"
                f"**Track:** {tracks} · **Event:** {location} {year}  \n"
                f"{link_line(r['url'])}  \n"
                f"📝 **Description:** {r['description']}\n\n"
                f"</details>\n"
            )
        lines.append("---")

    write(os.path.join(ROOT_DIR, location, year, "README.md"), lines)


# -------------------------------
# 📚 Cross-event indexes
# -------------------------------

def event_link(r):
    return f"[{r['location']} {r['year']}]({r['location']}/{r['year']}/README.md)"


def render_by_category(records):
    by_track = defaultdict(list)
    for r in records:
        for t in (r["tracks"] or [OTHERS]):
            by_track[t if t in CATEGORY_MAP else OTHERS].append(r)
    sections = [t for t in list(CATEGORY_MAP) + [OTHERS] if by_track.get(t)]

    lines = [
        "# All tools by track",
        "",
        f"Every tool from every Black Hat Arsenal event ({len(records)} presentations), grouped by track. "
        "Tools with several tracks appear under each. See also [all tools A–Z](BY_NAME.md).",
        "",
        "## Contents",
    ]
    lines += [f"- [{t}](#{sanitize_anchor(t)}) ({len(by_track[t])})" for t in sections]
    for t in sections:
        lines += ["", f"## {t}", ""]
        for r in sorted(by_track[t], key=lambda r: (r["name"].lower(), r["year"], r["location"])):
            link = f" · [repo]({r['url']})" if r["url"] else ""
            lines.append(f"- **{md_escape(r['name'])}** — {event_link(r)}{link}")
    write(BY_CATEGORY, lines)


def render_by_name(records):
    groups = defaultdict(list)
    for r in records:
        groups[r["name"].lower()].append(r)

    def initial(name):
        c = name[:1].upper()
        return c if c.isascii() and c.isalpha() else "0-9"

    by_letter = defaultdict(list)
    for rs in groups.values():
        by_letter[initial(rs[0]["name"])].append(rs)
    letters = sorted(by_letter)  # "0-9" sorts before "A"

    recurring = sum(1 for rs in groups.values() if len(rs) > 1)
    lines = [
        "# All tools A–Z",
        "",
        f"{len(groups)} distinct tools across {len(records)} presentations; {recurring} were presented at more "
        "than one event. Tools are grouped by name, so a tool shown at several events is one line with every event listed. "
        "See also [all tools by track](BY_CATEGORY.md).",
        "",
        "## Contents",
        " · ".join(f"[{c}](#{sanitize_anchor(c)})" for c in letters),
    ]
    for c in letters:
        lines += ["", f"## {c}", ""]
        for rs in sorted(by_letter[c], key=lambda rs: rs[0]["name"].lower()):
            rs = sorted(rs, key=lambda r: (r["year"], r["location"]))
            latest = rs[-1]
            events = ", ".join(event_link(r) for r in rs)
            link = f" · [repo]({latest['url']})" if latest["url"] else ""
            lines.append(f"- **{md_escape(latest['name'])}** — {events}{link}")
    write(BY_NAME, lines)


# -------------------------------
# 🗃️ Aggregates
# -------------------------------

def write_aggregates(records):
    rows = [{
        "Tool Name": r["name"],
        "Description": r["description"],
        "Github URL": r["url"],
        "Tracks": r["tracks"],
        "Speakers": r["speakers"],
        "Year": r["year"],
        "Location": r["location"],
        "Path": r["path"],
    } for r in records]
    with open(TOOLS_JSON, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(TOOLS_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["Tool Name", "Location", "Year", "Tracks", "Speakers", "Github URL", "Description", "Path"])
        for r in rows:
            w.writerow([r["Tool Name"], r["Location"], r["Year"], "; ".join(r["Tracks"]),
                        "; ".join(r["Speakers"]), r["Github URL"], r["Description"], r["Path"]])


# -------------------------------
# 🏠 Root README
# -------------------------------

def render_root_readme(records):
    per_location = defaultdict(lambda: defaultdict(int))
    for r in records:
        per_location[r["location"]][r["year"]] += 1
    total = len(records)

    def loc_heading(loc):
        return f"{loc} ({sum(per_location[loc].values())} tools)"

    lines = [
        f"# Awesome Black Hat Arsenal [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
        f"[![Tools](https://img.shields.io/badge/Tools-{total}-blue)](#locations)",
        "[![Project Logo](logo.png)](https://www.blackhat.com/html/arsenal.html)",
        "> 🚀 A curated list of cutting-edge cybersecurity tools showcased at the Black Hat Arsenal events — "
        "covering offensive, defensive, and research-focused security utilities.",
        "",
        "Whether you're in red teaming, blue teaming, appsec, or OSINT — this list helps you explore and leverage "
        "the best tools demonstrated live by security professionals across the world.",
        "",
        "## Contents",
        "- [How This List Is Organized](#how-this-list-is-organized)",
        "- [Browse](#browse)",
        "- [Locations](#locations)",
    ]
    lines += [f"  - [{loc}](#{sanitize_anchor(loc_heading(loc))})" for loc in sorted(per_location)]
    lines += [
        "- [Data](#data)",
        "- [Contributing](#contributing)",
        "",
        "## How This List Is Organized",
        "- Tools are grouped by the **location** of the Black Hat event (USA, Europe, Asia, Canada, MEA), then by **year**.",
        "- Each year has its own page where tools are grouped **by track category**, with description, speakers and "
        "repository link.",
        "- Two cross-event indexes let you browse the whole collection by track or by name.",
        "",
        "## Browse",
        f"- 🗂️ [All tools by track](tools/BY_CATEGORY.md) — the {len(CATEGORY_MAP)} Arsenal tracks, every event",
        "- 🔤 [All tools A–Z](tools/BY_NAME.md) — one line per tool, with every event it was presented at",
        "",
        "## Locations",
    ]
    for loc in sorted(per_location):
        lines.append(f"### {loc_heading(loc)}")
        lines += [f"- [{y}]({ROOT_DIR}/{loc}/{y}/README.md) — {n} tools" for y, n in sorted(per_location[loc].items())]
        lines.append("")
    lines += [
        "## Data",
        f"The whole list is available as [`tools.json`](tools.json) and [`tools.csv`](tools.csv) "
        f"({total} rows: name, description, URL, tracks, speakers, year, location). Both are regenerated from "
        "the per-tool JSON files under `tools/` — treat them as read-only.",
        "",
        "## Contributing",
        "We welcome community contributions to make this list better!",
        "",
        "- 📁 Each tool is one JSON file at `tools/{LOCATION}/{YEAR}/<tool-name-slug>.json` with: Tool Name, Description, "
        "GitHub URL (if available), Tracks, Speakers.",
        "- 📝 Follow [CONTRIBUTING.md](CONTRIBUTING.md) for the format and the list of valid track names.",
        "- ✅ Run `python3 scripts/normalize.py`, `python3 scripts/validate.py` (must report 0 errors) and `python3 AutoReadme.py` "
        "(regenerates every README, index and data file), then open a pull request.",
        "",
        "> ⚠️ All README files, the indexes and `tools.json`/`tools.csv` are generated — edit the JSON files, not these.",
    ]
    write(MAIN_README, lines)


# -------------------------------
# 🚀 Main
# -------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate Awesome Black Hat Arsenal READMEs, indexes and data files.")
    parser.add_argument("--event", help="Only rewrite event pages under tools/<event> (e.g. USA).")
    parser.add_argument("--year", help="Only rewrite tools/<event>/<year>. Requires --event.")
    args = parser.parse_args()

    if args.year and not args.event:
        die("Error: --year requires --event (expected tools/<event>/<year>).")
    if not os.path.isdir(ROOT_DIR):
        die(f"Error: ROOT_DIR does not exist or is not a directory: {ROOT_DIR}")
    if args.event and not os.path.isdir(os.path.join(ROOT_DIR, args.event)):
        die(f"Error: event folder does not exist: {os.path.join(ROOT_DIR, args.event)}")
    if args.year and not os.path.isdir(os.path.join(ROOT_DIR, args.event, args.year)):
        die(f"Error: year folder does not exist: {os.path.join(ROOT_DIR, args.event, args.year)}")

    records = load_tools()

    by_event = defaultdict(list)
    for r in records:
        by_event[(r["location"], r["year"])].append(r)
    for (location, year), rs in sorted(by_event.items()):
        if args.event and location != args.event:
            continue
        if args.year and year != args.year:
            continue
        render_event_readme(location, year, rs)

    render_by_category(records)
    render_by_name(records)
    write_aggregates(records)
    render_root_readme(records)
    print(f"Generated {len(by_event)} event pages, 2 indexes, {TOOLS_JSON}, {TOOLS_CSV} and {MAIN_README} "
          f"from {len(records)} tools.")


if __name__ == "__main__":
    main()
