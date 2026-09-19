# run.py — One-click script to go from scraped data to auto-generated README

import os
import sys
import subprocess

# -----------------------------
# ✅ CONFIGURATION
# -----------------------------
REGION = sys.argv[1] if len(sys.argv) > 1 else "USA"  # e.g. python run.py Europe
SCRAPE_MODE = "modern"  # Options: "modern" or "legacy"

# Folder paths (can be customized if needed)
BASE = os.getcwd()
INPUT_FILE = f"NewLinks/{REGION}.txt" if SCRAPE_MODE == "modern" else f"Links/{REGION}.txt"
SCRAPE_SCRIPT = f"arsenal-builder/scrape_blackhat_schedule.py" if SCRAPE_MODE == "modern" else f"arsenal-builder/scrape_old_html_schedule.py"
RAW_JSON_DIR = f"Data/{REGION}"
INDIV_TOOL_DIR = f"{REGION}Indiv"
CLEANED_TOOL_DIR = f"{REGION}Cleaned"

# -----------------------------
# 🧪 Step-by-step Pipeline
# -----------------------------
steps = [
    ("🔎 Step 1: Scraping Event Schedule Pages", f"python {SCRAPE_SCRIPT}"),
    ("🗂️ Step 2: Adding Year & Country", "python arsenal-builder/update_metadata_fields.py"),
    ("🔄 Step 3: Splitting Tools into Individual Files", "python arsenal-builder/split_tools_to_individual_files.py"),
    ("📊 Step 4: Predicting Categories with LLM", "python arsenal-builder/CategoryPredicter.py"),
    ("🔗 Step 5: Finding GitHub URLs", "python arsenal-builder/add_github_urls.py"),
    ("📁 Step 6: Flattening Folder Structure (Optional)", "python arsenal-builder/flatten_tool_files.py"),
    ("📝 Step 7: Generating Final README Files", "python AutoReadme.py")
]

print("""
############################################################
🚀 Awesome Black Hat Arsenal Toolchain - Auto Runner
############################################################
""")
print("Starting Arsenal Builder Pipeline for:", REGION)

for label, command in steps:
    print(f"\n{label}\n{'-' * len(label)}")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running: {command}\n{e}\nExiting pipeline.")
        break

print("\n✅ All steps completed! Check your README.md and tools folder.")