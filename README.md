# Awesome Black Hat Arsenal [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Tools](https://img.shields.io/badge/Tools-2030-blue)](#locations)
[![Project Logo](logo.png)](https://www.blackhat.com/html/arsenal.html)
> 🚀 A curated list of cutting-edge cybersecurity tools showcased at the Black Hat Arsenal events — covering offensive, defensive, and research-focused security utilities.

Whether you're in red teaming, blue teaming, appsec, or OSINT — this list helps you explore and leverage the best tools demonstrated live by security professionals across the world.

## Contents
1. [How This List Is Organized](#how-this-list-is-organized)
2. [Locations](#locations)
   - [Asia](#asia)
   - [Canada](#canada)
   - [Europe](#europe)
   - [MEA](#mea)
   - [USA](#usa)
## How This List Is Organized
- The tools are grouped by the **location** of the Black Hat event (e.g., USA, Europe, Asia).
- Under each location, tools are further organized by **year**.
- Each year has its own README where tools are grouped **by track category**, each with description, speakers, and GitHub link (where available).
---
## Locations
### Asia
- [2015](tools/Asia/2015/README.md) — 15 tools
- [2016](tools/Asia/2016/README.md) — 14 tools
- [2017](tools/Asia/2017/README.md) — 16 tools
- [2018](tools/Asia/2018/README.md) — 23 tools
- [2019](tools/Asia/2019/README.md) — 23 tools
- [2020](tools/Asia/2020/README.md) — 26 tools
- [2021](tools/Asia/2021/README.md) — 22 tools
- [2022](tools/Asia/2022/README.md) — 22 tools
- [2023](tools/Asia/2023/README.md) — 43 tools
- [2024](tools/Asia/2024/README.md) — 58 tools
- [2025](tools/Asia/2025/README.md) — 51 tools
- [2026](tools/Asia/2026/README.md) — 49 tools
### Canada
- [2023](tools/Canada/2023/README.md) — 30 tools
- [2024](tools/Canada/2024/README.md) — 33 tools
- [2025](tools/Canada/2025/README.md) — 34 tools
### Europe
- [2014](tools/Europe/2014/README.md) — 5 tools
- [2015](tools/Europe/2015/README.md) — 18 tools
- [2016](tools/Europe/2016/README.md) — 17 tools
- [2017](tools/Europe/2017/README.md) — 37 tools
- [2018](tools/Europe/2018/README.md) — 38 tools
- [2019](tools/Europe/2019/README.md) — 38 tools
- [2020](tools/Europe/2020/README.md) — 23 tools
- [2021](tools/Europe/2021/README.md) — 41 tools
- [2022](tools/Europe/2022/README.md) — 37 tools
- [2023](tools/Europe/2023/README.md) — 55 tools
- [2024](tools/Europe/2024/README.md) — 64 tools
- [2025](tools/Europe/2025/README.md) — 59 tools
### MEA
- [2024](tools/MEA/2024/README.md) — 18 tools
- [2025](tools/MEA/2025/README.md) — 19 tools
### USA
- [2013](tools/USA/2013/README.md) — 42 tools
- [2014](tools/USA/2014/README.md) — 49 tools
- [2015](tools/USA/2015/README.md) — 51 tools
- [2016](tools/USA/2016/README.md) — 87 tools
- [2017](tools/USA/2017/README.md) — 87 tools
- [2018](tools/USA/2018/README.md) — 89 tools
- [2019](tools/USA/2019/README.md) — 91 tools
- [2020](tools/USA/2020/README.md) — 51 tools
- [2021](tools/USA/2021/README.md) — 64 tools
- [2022](tools/USA/2022/README.md) — 83 tools
- [2023](tools/USA/2023/README.md) — 90 tools
- [2024](tools/USA/2024/README.md) — 93 tools
- [2025](tools/USA/2025/README.md) — 125 tools
- [2026](tools/USA/2026/README.md) — 100 tools
---
## Contributing
We welcome community contributions to make this list better!

🛠 How to Contribute:
- 📁 Tools are grouped by **Black Hat event location** (`USA`, `Europe`, etc.) and **year** inside `tools/`. 
- 🧠 Each year's README (auto-generated) groups tools by **track category** such as `Red Teaming`, `OSINT`, `Reverse Engineering`, etc.
- 📝 Each tool is defined by a structured `.json` file including:
  - Tool Name
  - Description
  - GitHub URL (if available)
  - Tracks
  - Speaker(s)

📄 To Add a Tool:
1. Create a JSON file inside the appropriate folder:
   ```
   tools/{LOCATION}/{YEAR}/tool-name.json
   ```
2. Follow the [CONTRIBUTING.md](CONTRIBUTING.md) for format guidelines.
3. Run `python3 AutoReadme.py` to regenerate the README files.
4. Submit a pull request.

> ⚠️ Keep content concise and correctly categorized. Badges and README entries are auto-generated.

