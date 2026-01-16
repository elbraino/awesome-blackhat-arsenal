import os
import json
import argparse
from collections import defaultdict
from datetime import datetime

# -------------------------------
# 🔧 Configuration & Constants
# -------------------------------
ROOT_DIR = "tools"                # Root directory containing event/year folders
MAIN_README = "README.md"         # Path for the main README

# Category → (Label, Badge Color)
CATEGORY_MAP = {
    "Exploitation and Ethical Hacking": ("🔴 Red Teaming", "red"),
    "Malware Offense": ("🔴 Red Teaming", "red"),
    "Network Attacks": ("🔴 Red Teaming", "red"),
    "Reverse Engineering": ("🧠 Reverse Engineering", "orange"),
    "OSINT - Open Source Intelligence": ("🔍 OSINT", "lightgrey"),
    "Internet of Things": ("🟣 Red Teaming / Embedded", "purple"),
    "Hardware / Embedded": ("🟣 Red Teaming / Embedded", "purple"),
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
}

# -------------------------------
# 🧩 Utility Functions
# -------------------------------

def extract_track_label(track_entry):
    """Cleans up track entry text."""
    if not isinstance(track_entry, str):
        return ""
    return track_entry.replace("Track:", "").strip()

def determine_category(track_list):
    """Maps track to a standard category using CATEGORY_MAP."""
    if not track_list or not isinstance(track_list, list):
        return ("Others", "lightgrey")
    for track in track_list:
        track_clean = extract_track_label(track)
        if track_clean in CATEGORY_MAP:
            return CATEGORY_MAP[track_clean]
    return ("Others", "lightgrey")

def badge(text, color):
    """Generates a Shields.io badge markdown string."""
    return f"![{text}](https://img.shields.io/badge/{text.replace(' ', '%20')}-{color})"

def sanitize_anchor(text):
    """Converts text to a GitHub anchor-safe format."""
    return text.lower().replace(" ", "-").replace("/", "").replace("&", "").replace("--", "-")

def die(msg, code=1):
    print(msg)
    raise SystemExit(code)

# -------------------------------
# 🧰 CLI Args
# -------------------------------
parser = argparse.ArgumentParser(description="Generate Awesome Black Hat Arsenal READMEs.")
parser.add_argument(
    "--event",
    help="Only process the subfolders inside tools/<event> (e.g., tools/USA, tools/Europe).",
)
parser.add_argument(
    "--year",
    help="Only process tools/<event>/<year>. Requires --event.",
)
args = parser.parse_args()

if args.year and not args.event:
    die("Error: --year requires --event (expected tools/<event>/<year>).")

# Validate paths based on options
event_filter = args.event
year_filter = args.year

if event_filter:
    event_path = os.path.join(ROOT_DIR, event_filter)
    if not os.path.isdir(event_path):
        die(f"Error: event folder does not exist: {event_path}")

    if year_filter:
        year_path = os.path.join(event_path, year_filter)
        if not os.path.isdir(year_path):
            die(f"Error: year folder does not exist: {year_path}")

# -------------------------------
# 🏠 Generate Main README Header
# -------------------------------
now = datetime.now()
last_update = now.strftime("%B %Y").replace(" ", "%20")
main_readme = [
    f"# Awesome Black Hat Arsenal [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Update](https://img.shields.io/badge/Updated-{last_update}-blue)](https://github.com/elbraino/awesome-blackhat-arsenal)",
    "[![Project Logo](logo.png)](https://www.blackhat.com/html/arsenal.html)",
    "> 🚀 A curated list of cutting-edge cybersecurity tools showcased at the Black Hat Arsenal events — covering offensive, defensive, and research-focused security utilities.",
    "",
    "Whether you're in red teaming, blue teaming, appsec, or OSINT — this list helps you explore and leverage the best tools demonstrated live by security professionals across the world.",
    "",
    "## Contents",
    "1. [How This List Is Organized](#how-this-list-is-organized)",
    "2. [Locations](#locations)",
    "   - [Asia](#asia)",
    "   - [Canada](#canada)",
    "   - [Europe](#europe)",
    "   - [MEA](#mea)",
    "   - [USA](#usa)",
    "## How This List Is Organized",
    "- The tools are grouped by the **location** of the Black Hat event (e.g., USA, Europe, Asia).",
    "- Under each location, tools are further organized by **year**.",
    "- Inside the section of every year, you will find the tools organized **by track category**, each with descriptions, authors, and GitHub links (where available).",
    "---",
    "## Locations",
]

# -------------------------------
# 📁 Decide what to edit
# -------------------------------
if not os.path.isdir(ROOT_DIR):
    die(f"Error: ROOT_DIR does not exist or is not a directory: {ROOT_DIR}")

locations = sorted(os.listdir(ROOT_DIR))
locations_to_edit = [event_filter] if event_filter else locations

# -------------------------------
# 📁 Traverse All Locations & Years (optionally filtered)
# -------------------------------
for location in locations:
    loc_path = os.path.join(ROOT_DIR, location)
    if not os.path.isdir(loc_path):
        continue

    main_readme.append(f"### {location}")

    years = sorted(os.listdir(loc_path))
    years_to_edit = [year_filter] if year_filter and event_filter else years

    for year in years:
        year_path = os.path.join(loc_path, year)
        if not os.path.isdir(year_path):
            continue

        # Use full-length links
        rel_readme = f"https://github.com/elbraino/awesome-blackhat-arsenal/blob/main/{ROOT_DIR}/{location}/{year}/README.md"
        main_readme.append(f"- [{year}]({rel_readme})")

        # Skip README edit/creation if not in 'locations_to_edit'
        if location not in locations_to_edit or year not in years_to_edit:
            continue

        tools_by_category = defaultdict(list)

        # --------------------------------------------
        # 📄 Process JSON files under each year folder
        # --------------------------------------------
        for file in os.listdir(year_path):
            if not file.endswith(".json"):
                continue

            json_path = os.path.join(year_path, file)
            with open(json_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except Exception:
                    print(f"Error while loading JSON file '{json_path}'")
                    raise SystemExit(1)

            if not isinstance(data, list):
                data = [data]

            # ✍️ Parse each tool entry
            for tool in data:
                badge_color = {
                    "USA": "black",
                    "Europe": "blue",
                    "Asia": "green",
                    "MEA": "orange",
                    "Canada": "purple"
                }.get(location, "gray")

                loc_year_badge = badge(f"{location} {year}", badge_color)

                name = tool.get("Tool Name", "Unnamed Tool")
                url = (tool.get("GitHub URL") or "").strip()
                description = tool.get("Description", "No description provided.")
                tracks = tool.get("Tracks", [])
                speakers_raw = tool.get("Speakers", [])
                speakers = speakers_raw if isinstance(speakers_raw, list) else [str(speakers_raw)]

                # Determine category and style
                category, color = determine_category(tracks)
                speaker_tags = " ".join([badge(s, "informational") for s in speakers])
                category_tag = badge(f"Category: {category}", color)
                link_line = f"🔗 **Link:** [{name}]({url})" if url else "🔗 **Link:** Not Available"

                # Final tool block
                entry = (
                    f"<details><summary><strong>{name}</strong></summary>\n\n"
                    f"{loc_year_badge} {category_tag} {speaker_tags}\n\n"
                    f"{link_line}  \n"
                    f"📝 **Description:** {description}\n\n"
                    f"</details>\n"
                )
                tools_by_category[category].append(entry)

        # -------------------------------
        # 📄 Generate Sub README per Year
        # -------------------------------
        subreadme = [
            f"# {location} {year}",
            "---",
            f"📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal {year}** event held in **{location}**.",
            "Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.",
            "",
            "## 📚 Contents"
        ]

        for cat in sorted(tools_by_category):
            subreadme.append(f"- [{cat}](#{sanitize_anchor(cat)})")
        subreadme.append("---")

        for cat, tools in tools_by_category.items():
            subreadme.append(f"## {cat}")
            for tool_block in tools:
                subreadme.append(tool_block)
            subreadme.append("---")

        # 💾 Write sub-README
        with open(os.path.join(year_path, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(subreadme))

# -------------------------------
# 🧾 Finalize Main README Footer
# -------------------------------
main_readme.append("---")
main_readme.extend([
    "## Contributing",  # Fixed to match ToC
    "We welcome community contributions to make this list better!",
    "",
    "🛠 How to Contribute:",  # Fixed to match ToC
    "- 📁 Tools are grouped by **Black Hat event location** (`USA`, `Europe`, etc.) and **year** inside `tools/`. ",
    "- 🧠 Inside each year's folder, tools are organized by **track categories** such as `Red Teaming`, `OSINT`, `Reverse Engineering`, etc.",
    "- 📝 Each tool is defined by a structured `.json` file including:",
    "  - Tool Name",
    "  - Description",
    "  - GitHub URL (if available)",
    "  - Tracks",
    "  - Speaker(s)",
    "",
    "📄 To Add a Tool:",  # Fixed to match ToC
    "1. Create a JSON file inside the appropriate folder:",
    "   ```",
    "   tools/{LOCATION}/{YEAR}/tool-name.json",
    "   ```",
    "2. Follow the [CONTRIBUTING.md](CONTRIBUTING.md) for format guidelines.",
    "3. Submit a pull request.",
    "",
    "> ⚠️ Keep content concise and correctly categorized. Badges and README entries are auto-generated.",
    "\n",
])

# 💾 Write Main README
with open(MAIN_README, "w", encoding="utf-8") as f:
    f.write("\n".join(main_readme))
