# 🧩 Contributing to Awesome Black Hat Arsenal

We’re excited to have you contribute to this curated archive of cybersecurity tools from Black Hat Arsenal events. This guide explains how to add tools properly so they are auto-integrated into the list.

---

## 📁 Repository Structure

The repository is organized by **location** and **year**. Each tool is placed in a specific folder based on these two criteria.

```

tools/
├── USA/
│   ├── 2023/
│   │   ├── toolname.json
│   │   └── README.md
├── Europe/
│   └── 2024/
│       └── toolname.json

````

- Tools are grouped by **location** (`USA`, `Europe`, `Asia`, etc.).
- Then, tools are categorized by **year** of the Black Hat event.
- Each tool is added as a `.json` file within its respective year folder.

---

## 🧠 Tool JSON Format

Each `.json` file should contain the following fields:

```json
{
  "Tool Name": "Cool Exploit Framework",
  "Description": "A modular post-exploitation tool for cloud environments.",
  "Github URL": "https://github.com/username/tool",
  "Tracks": ["Track: Exploitation and Ethical Hacking"],
  "Speakers": ["Jane Doe"]
}
````

### Required Fields:

* `Tool Name`: The name of the tool.
* `Description`: 1–3 sentence description (avoid marketing fluff).
* `Tracks`: List of applicable track names (e.g., `"Track: Reverse Engineering"`).
* `Speakers`: Name(s) of the presenters (can be multiple).
* `Github URL`: Link to the tool's GitHub repository or official page (if public).

---

## ✅ Track Names

Use one or more of the following **valid track names** (exact spelling, no `Track:` prefix):

* Exploitation and Ethical Hacking
* Vulnerability Assessment
* Web AppSec
* Code Assessment
* Network Attacks
* Network Defense
* Malware Offense
* Malware Defense
* Reverse Engineering
* Data Forensics/Incident Response
* OSINT - Open Source Intelligence
* Android, iOS and Mobile Hacking
* Hardware/Embedded
* Internet Of Things
* Smart Grid/Industrial Security
* Cloud Security
* AI, ML & Data Science
* Cryptography
* Human Factors
* Arsenal Lab

If a tool doesn’t fit into any of these tracks, use an empty list (`"Tracks": []`) and it will be placed in the `Others` section. When a tool has several tracks, **the first one listed decides which section it appears under** in the generated README.

---

## 🧪 Validation

Once you add a JSON file:

* **Validate**: run `python3 scripts/validate.py` from the repo root. It checks every file for required keys, valid track names, well-formed URLs, and that `Year`/`Location` match the folder. It must report **0 errors** (warnings are fine).
* **README generation**: run `python3 AutoReadme.py` from the repo root. It regenerates every event README, the cross-event indexes (`tools/BY_CATEGORY.md`, `tools/BY_NAME.md`), the data files (`tools.json`, `tools.csv`) and the root README. Commit the result — never edit those files by hand.

CI runs both checks on every pull request and fails if the READMEs are out of date.

---

## 🔁 Pull Requests (PRs)

To contribute your tool, follow these steps:

### 1. **Fork the Repository**

Click the "Fork" button at the top right of this repository to create a copy under your GitHub account.

### 2. **Create a Branch**

Once you have forked the repository, create a new branch for your changes. This helps us manage your contributions effectively.

```bash
git checkout -b add-tool-cool-exploit-framework
```

### 3. **Add the Tool JSON**

* Create a new JSON file for your tool under the correct location and year (e.g., `tools/USA/2023/toolname.json`).
* Ensure your file follows the correct format as explained above.

### 4. **Submit a Pull Request**

Once your changes are complete:

* Commit your changes to your forked repository:

  ```bash
  git add .
  git commit -m "Add Tool: Cool Exploit Framework (USA 2023)"
  git push origin add-tool-cool-exploit-framework
  ```

* Open a pull request (PR) from your fork to the main repository. Use the following format for the PR title:

  ```
  Add Tool: Cool Exploit Framework (USA 2023)
  ```

  * **Make sure you're placing the tool in the correct folder** (e.g., `tools/USA/2023/`).
  * **One PR per tool or group of tools** is required.

---

## 🧑‍💻 Questions?

If you're unsure about track mapping, folder structure, or anything else, feel free to open an issue or ask in your PR. We’re here to help!

---

Thank you for contributing to building the most complete and categorized arsenal of cybersecurity tools! 🛡️

---


### Key Points for Submission:
1. **Fork the Repository**: Click "Fork" at the top-right corner of the GitHub page.
2. **Create a Branch**: Name your branch clearly based on the tool you’re adding.
3. **Add the Tool JSON**: Place the JSON file in the correct year and location directory.
4. **Commit & Push**: Commit your changes and push them to your forked repository.
5. **PR Title Format**: Use the format `Add Tool: Cool Exploit Framework (USA 2023)` for your PR title.
6. **Only One Tool per PR**: Keep one PR per tool or group of tools.

