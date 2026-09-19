# 🔧 arsenal-builder — importing a new Black Hat Arsenal event

Scripts that turn a Black Hat Arsenal schedule page into one JSON file per tool
under `tools/<Region>/<Year>/`. The final steps are always the same and run from
the **repo root**:

```bash
python3 scripts/normalize.py    # canonical key order, formatting and file names
python3 scripts/validate.py     # must report 0 errors
python3 AutoReadme.py           # regenerates every README, the indexes and tools.json/csv
```

## Setup

```bash
pip install -r arsenal-builder/requirements.txt
cp arsenal-builder/.env.example arsenal-builder/.env   # then fill in the keys you need
```

| Key | Used by |
|-----|---------|
| `OPENAI_API_KEY`, `GEMINI_API_KEY` | `CategoryPredicter.py` (LLM track prediction) |
| `SERPER_API_KEY` | `add_github_urls.py` (Google search for repo URLs) |

`.env` is git-ignored. Never commit real keys.

## Current approach (2026 events)

The 2026 schedule pages are rendered behind Cloudflare and populated by JS, so
the legacy scraper doesn't work on them. The USA 2026 import is the reference
example — copy and adapt these for the next event:

| Step | Script (run from `arsenal-builder/`) | Output |
|------|--------------------------------------|--------|
| 1. Scrape the schedule with Selenium | `scrape_usa_2026.py` / `scrape_asia_2026.py` | `Data/<Region>/<code>-26_arsenal_schedule_index.html.json` |
| 2. Dedupe sessions, normalize tracks, write one JSON per tool | `build_usa_2026.py` | `../tools/USA/2026/*.json` |
| 3. Find candidate GitHub repos via the GitHub search API | `gh_candidates.py` | `Data/USA/us-26_gh_candidates.json` |
| 4. Write the manually verified URLs and descriptions | `apply_usa_2026_urls.py`, `apply_usa_2026_descriptions.py` | updates `../tools/USA/2026/*.json` |
| 5. Normalize, validate, regenerate | `scripts/normalize.py`, `scripts/validate.py`, `AutoReadme.py` (repo root) | canonical files, READMEs, indexes, data |

Track names must be one of the 20 listed in [CONTRIBUTING.md](../CONTRIBUTING.md);
`build_usa_2026.py` shows how to map the drifting names on the BH site to them.

## Legacy pipeline (2013–2025 imports)

`run.py` (repo root) chains these steps. **Each script has its input/output
folder hard-coded near the top or bottom of the file — set it before running.**

| Step | Script | Notes |
|------|--------|-------|
| 1 | `scrape_blackhat_schedule.py` (modern pages) or `scrape_old_html_schedule.py` (pre-2019 static HTML) | reads URLs from `NewLinks/<Region>.txt` or `Links/<Region>.txt` |
| 2 | `update_metadata_fields.py` | adds `Year`/`Country` to each scraped session in `Data/<Region>/` |
| 3 | `split_tools_to_individual_files.py` | one file per tool, e.g. `Asia/2023/0001_ToolName.json` |
| 4 | `CategoryPredicter.py` | optional LLM track prediction |
| 5 | `add_github_urls.py` | Serper search for a GitHub URL per tool; does a HEAD check |
| 6 | `flatten_tool_files.py <Region>` (repo root) | strips the `0001_` prefixes and moves files into `tools/<Region>/<Year>/` |
| 7–8 | `scripts/normalize.py`, `scripts/validate.py`, `AutoReadme.py` (repo root) | |

## Data/

`Data/` holds raw scrape output. The committed files are the inputs used for the
Asia 2023/2026 and USA 2026 imports and are kept so those imports can be re-run.
