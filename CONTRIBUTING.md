
# 🧩 Contributing to Awesome Black Hat Arsenal

We’re excited to have you contribute to this curated archive of cybersecurity tools from Black Hat Arsenal events. This guide explains how to add tools properly so they are auto-integrated into the list.

---

## 📁 Repository Structure

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

- Tools are grouped by **location** (`USA`, `Europe`, `Asia`, etc.)
- Then by **year** of the Black Hat event
- Each tool is a single `.json` file inside its year folder

---

## 🧠 Tool JSON Format

Each `.json` file should be a dictionary with the following fields:

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

* `Tool Name`: Name of the tool
* `Description`: 1–3 sentence description (avoid marketing fluff)
* `Tracks`: List of applicable track names, e.g. `"Track: Reverse Engineering"`
* `Speakers`: Name(s) of the presenters (can be multiple)
* `Github URL`: GitHub or official repo (if public)

---

## ✅ Track Names

Use one or more of the following valid track names:

* Track: Exploitation and Ethical Hacking
* Track: Reverse Engineering
* Track: OSINT - Open Source Intelligence
* Track: Internet of Things
* Track: Hardware / Embedded
* Track: Web AppSec
* Track: Code Assessment
* Track: Malware Offense
* Track: Malware Defense
* Track: Network Attacks
* Track: Network Defense
* Track: Smart Grid/Industrial Security
* Track: Android, iOS and Mobile Hacking
* Track: Cryptography
* Track: Data Forensics/Incident Response
* Track: Human Factors
* Track: Arsenal Lab

If a tool doesn’t fit any, just omit `Tracks`, and it will be placed in the `Uncategorized` section.

---

## 🧪 Validation

Once you add a JSON file:

* Ensure it opens without error in any JSON linter
* Run the README generation script (or submit a PR and we’ll handle it)

---

## 🔁 Pull Requests

* One PR per tool or group of tools
* PR title format: `Add Tool: Cool Exploit Framework (USA 2023)`
* Make sure you're placing tools in the correct folder path

---

## 🧑‍💻 Questions?

If you're unsure about track mapping or folder structure, open an issue or drop your question in the PR. We're happy to help.

---

Thank you for helping build the most complete and categorized arsenal of security tools online! 🛡️


