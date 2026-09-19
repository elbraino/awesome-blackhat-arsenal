# USA 2026
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2026** event held in **USA**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools)
- [🌐 Web/AppSec](#-webappsec)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming)
- [🔍 OSINT](#-osint)
- [🔴 Red Teaming](#-red-teaming)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec)
- [🔵 Blue Team & Detection](#-blue-team--detection)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded)
- [🤖 AI, ML & Data Science](#-ai-ml--data-science)
- [🧠 Reverse Engineering](#-reverse-engineering)
---
## ☁️ Cloud Security
<details><summary><strong>BadZure: Building Cloud Attack Labs with AI</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

🔗 **Link:** [BadZure: Building Cloud Attack Labs with AI](https://github.com/mvelazc0/BadZure)  
📝 **Description:** BadZure provisions deliberately misconfigured Entra ID and Azure environments from a natural-language description of the desired scenario. It generates identities, groups, applications, cloud resources, and permission assignments that mirror organic enterprise tenants, then layers traversable privilege escalation chains built on service principal abuse, credential theft from Key Vaults and Storage Accounts, and managed identity token theft. Terraform deployment makes each lab repeatable and disposable for purple teaming, detection engineering, and training.

</details>

<details><summary><strong>Bedrock Keys Security (BKS): Hunting Phantom IAM Users Created by AWS Bedrock API Keys</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Sergio Garcia](https://img.shields.io/badge/Sergio%20Garcia-informational)

🔗 **Link:** [Bedrock Keys Security (BKS): Hunting Phantom IAM Users Created by AWS Bedrock API Keys](https://github.com/BeyondTrust/bedrock-keys-security)  
📝 **Description:** AWS Bedrock API keys are bearer tokens that embed the account ID and IAM username in plain base64, and each long-term key silently provisions a full IAM user that survives key deletion. BKS is an open-source toolkit covering the whole lifecycle of these keys across Amazon Bedrock and Claude Platform on AWS: it scans Organizations for phantom users, ranks them by risk, removes orphans, decodes leaked keys offline, reconstructs CloudTrail activity, and ships Service Control Policies plus Sigma and CloudTrail Lake detections.

</details>

<details><summary><strong>CLOAK : Cloud Testing Agent Harness</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Arpan Abani Sarkar](https://img.shields.io/badge/Arpan%20Abani%20Sarkar-informational)

🔗 **Link:** [CLOAK : Cloud Testing Agent Harness](https://github.com/openrec0n/cloak)  
📝 **Description:** CLOAK is an open-source AI red team agent for cloud security assessments, built as a harness for Claude Code so operators work from the terminal. Its Dual Output Rendering architecture keeps sensitive identifiers such as ARNs, account IDs, and resource names out of the model's context window while complete assessment data stays local. Defense-in-depth hooks enforce dry-run previews and gate sensitive access behind human approval, and a companion web interface browses execution history.

</details>

<details><summary><strong>Emulate cloud-native attacks with Stratus Red Team</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Andrew Krug](https://img.shields.io/badge/Andrew%20Krug-informational)

🔗 **Link:** [Emulate cloud-native attacks with Stratus Red Team](https://github.com/DataDog/stratus-red-team)  
📝 **Description:** Stratus Red Team lets threat detection and cloud security engineering teams reproduce common cloud attacks in a self-contained way to confirm that detection mechanisms work as expected. It supports AWS, Azure, Google Cloud, Entra ID, and Kubernetes, and each emulated technique ships with actionable detection insight describing the telemetry defenders should expect to see.

</details>

<details><summary><strong>findmytakeover - find dangling domains in a multi cloud environment</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Aniruddha Biyani](https://img.shields.io/badge/Aniruddha%20Biyani-informational)

🔗 **Link:** [findmytakeover - find dangling domains in a multi cloud environment](https://github.com/anirudhbiyani/findmytakeover)  
📝 **Description:** findmytakeover detects dangling DNS records across multi-cloud environments. Rather than relying on wordlists or brute-forcing DNS servers, it enumerates all DNS zones and the infrastructure present within the configured cloud service providers, across one or many accounts, and reports records whose backing infrastructure no longer exists and which are therefore exposed to subdomain takeover.

</details>

<details><summary><strong>notyet: Automated IAM Persistence Analysis Through AWS Eventual Consistency Abuse</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Eduard Agavriloae](https://img.shields.io/badge/Eduard%20Agavriloae-informational)

🔗 **Link:** [notyet: Automated IAM Persistence Analysis Through AWS Eventual Consistency Abuse](https://github.com/OFFENSAI/notyet)  
📝 **Description:** AWS IAM is eventually consistent: key deletion, policy detachment, and role removal take seconds to propagate through the authorization system. notyet exploits that window to maintain access indefinitely, automatically rotating credentials and restoring permissions faster than responders can revoke them. A web interface lets defenders and researchers test their containment procedures against these persistence techniques and confirm whether revoking compromised credentials actually neutralises the threat.

</details>

<details><summary><strong>OWASP EKS Goat: Hands-On AWS EKS Security</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![peachycloudsecurity](https://img.shields.io/badge/peachycloudsecurity-informational) ![Divyanshu Shukla](https://img.shields.io/badge/Divyanshu%20Shukla-informational)

🔗 **Link:** [OWASP EKS Goat: Hands-On AWS EKS Security](https://github.com/OWASP/www-project-eks-goat)  
📝 **Description:** OWASP EKS Goat is an open-source, intentionally vulnerable AWS EKS cluster for hands-on security testing and training. It presents realistic supply chain weaknesses that lead to compromise of EKS and ECR through cloud and RBAC misconfiguration, with scenarios covering a CVE-vulnerable application as an entry point, misconfigured IAM roles and Kubernetes RBAC, backdoored ECR images, and privilege escalation from pods to EC2 nodes. Documentation covers hardening with Kyverno, GuardDuty, and eBPF runtime security.

</details>

<details><summary><strong>Pathrunner: An AWS Privilege Escalation Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Seth Art (sethsec)](https://img.shields.io/badge/Seth%20Art%20(sethsec)-informational)

🔗 **Link:** [Pathrunner: An AWS Privilege Escalation Framework](https://github.com/DataDog/pathrunner)  
📝 **Description:** Pathrunner is a modular AWS privilege escalation framework, comparable to Metasploit or NetExec but aimed at cloud identities and focused on IAM. Building on the paths catalogued at pathfinding.cloud, it automates exploitation of more than 65 escalation paths with configurable payloads and options — exfiltrating a Lambda function's IAM credentials, or having that function create a backdoored role to assume. It can import PMapper graphs to see which paths are exploitable, auto-discover destination resources, and chain multiple escalation steps.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Attack & Defence Wargame: The Insurance Company Edition</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational) ![Davide Cioccia](https://img.shields.io/badge/Davide%20Cioccia-informational) ![Harley Wilson](https://img.shields.io/badge/Harley%20Wilson-informational)

🔗 **Link:** [AI Attack & Defence Wargame: The Insurance Company Edition](https://play.secdim.com/)  
📝 **Description:** A live adversarial wargame in which each participant operates an LLM-backed insurance chatbot holding domain knowledge and sensitive customer records, then attempts to breach everyone else's. Players harden their own bot against prompt injection, indirect instruction override, and data exfiltration while probing rivals for protected data. Unlike a static-flag CTF, the attack surface shifts as defenders patch and attackers adapt; each player has full access to their chatbot's source repository.

</details>

<details><summary><strong>Anthropic-Cybersecurity-Skills</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Mahipal](https://img.shields.io/badge/Mahipal-informational)

🔗 **Link:** [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)  
📝 **Description:** This project supplies the cybersecurity domain knowledge that agentskills.io-compatible coding agents ship without: 734 open-source skills across 37 security subdomains, mapping more than 127 MITRE ATT&CK techniques with tool-specific commands, NIST CSF alignment, and procedural workflows backed by over 1,000 runnable Python scripts. Each skill follows progressive disclosure with YAML frontmatter for discovery. The Apache-2.0 collection installs into Claude Code, GitHub Copilot, or Codex CLI through a single npx command.

</details>

<details><summary><strong>APTL: Advanced Purple Team Labs</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![atomik](https://img.shields.io/badge/atomik-informational)

🔗 **Link:** [APTL: Advanced Purple Team Labs](https://github.com/Brad-Edwards/aptl)  
📝 **Description:** APTL is an MIT-licensed, Docker-based purple team laboratory bundling an open-source SOC stack, Model Context Protocol servers, and a scenario system. It lets researchers pit red and blue team AI agents against one another, study their behaviour, and test enhancement strategies. The lab runs on commodity hardware with consumer-grade AI services and captures all telemetry so that experiments can be reviewed and reproduced.

</details>

<details><summary><strong>Chef Special: Updates to CSTC - CyberChef-inspired Message Transformator in BurpSuite</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational) ![Kai Glauber](https://img.shields.io/badge/Kai%20Glauber-informational) ![Florian Haag](https://img.shields.io/badge/Florian%20Haag-informational)

🔗 **Link:** [Chef Special: Updates to CSTC - CyberChef-inspired Message Transformator in BurpSuite](https://github.com/usdAG/cstc)  
📝 **Description:** The Cyber Security Transformation Chef is a Burp Suite extension that brings CyberChef-style recipes to live HTTP request and response modification. Recipes apply automatically across Scanner, Intruder, and Repeater, handling application quirks such as body-derived HMACs or expiring JWTs so testers can scan and fuzz without manual re-signing. The latest release adds many new operations, improved request sending and conditional handling, and support for multiple active recipes in parallel.

</details>

<details><summary><strong>EMBA – The product security analysis framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Michael Messner](https://img.shields.io/badge/Michael%20Messner-informational) ![Benedikt Kühne](https://img.shields.io/badge/Benedikt%20Kühne-informational)

🔗 **Link:** [EMBA – The product security analysis framework](https://github.com/e-m-b-a/emba)  
📝 **Description:** EMBA is an open-source firmware security analyser for the IoT, ICS, and OT devices that underpin modern infrastructure, where varied architectures, trimmed operating systems, and special protocols make testing hard. It automates firmware extraction and binary-level detection of known vulnerabilities, going past plain CVE matching to report which public exploits apply, and also aids discovery of unknown issues, insecure scripting, and hard-coded credentials. AI integration assists with more complex findings.

</details>

<details><summary><strong>Hecate: a trivial UART tool</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![. maxi](https://img.shields.io/badge/.%20maxi-informational) ![Joe FitzPatrick](https://img.shields.io/badge/Joe%20FitzPatrick-informational) ![Nyx](https://img.shields.io/badge/Nyx-informational)

🔗 **Link:** [Hecate: a trivial UART tool](https://github.com/tigard-tools/hecate)  
📝 **Description:** Hecate is an open-source embedded UART implant development framework that turns any CircuitPython-compatible microcontroller into a customisable serial implant with minimal code. It supports passive sniffing of serial communications between two systems, datalogging of captured UART traffic, payload injection to spoof communications, and full implant-in-the-middle operation that modifies data in transit. The framework lowers the barrier to embedded implant development while remaining flexible enough for research and rapid prototyping.

</details>

<details><summary><strong>LLM Hacking 101</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Maor Tal](https://img.shields.io/badge/Maor%20Tal-informational)

🔗 **Link:** [LLM Hacking 101](https://github.com/RootInj3c/LLM-Playground)  
📝 **Description:** LLM Hacking 101 is a two-hour hands-on Arsenal lab introducing practical offensive techniques against LLM-powered and agentic systems. Participants progress from foundational jailbreak development to guardrail bypass, exploring both direct and indirect prompt injection, then move on to agent tool enumeration and exploitation to see how reasoning layers and tool integrations extend attacker influence. Exercises run in a dedicated environment on the PwnBox.AI platform using realistic AI-enabled scenarios.

</details>

<details><summary><strong>Tengu Marauder Vanguard Version 2.0</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Lexie Thach](https://img.shields.io/badge/Lexie%20Thach-informational) ![Justice Passe](https://img.shields.io/badge/Justice%20Passe-informational)

🔗 **Link:** [Tengu Marauder Vanguard Version 2.0](https://github.com/Lexicon121/Tengu-Marauder-Vanguard)  
📝 **Description:** Tengu Marauder Vanguard 2.0 is an open-source robotic platform for physical red team operations and wireless network assessment, built on the Raspberry Pi 5 with a Flask interface that offers real-time target visualisation, integrated network scanning, and fleet management from one console. Version 2 adds Bluetooth scanning and SDR-based RF tooling, dual-band 2.4/5 GHz WiFi testing via an ESP32-C5 module, on-board AI inference through the Hailo AI HAT 2, and network coordination across units using a Banana Pi BPI-R4 running OpenWrt.

</details>

<details><summary><strong>ThreatShield - The Intelligent Way of Threat Modelling</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Satyam Nagpal](https://img.shields.io/badge/Satyam%20Nagpal-informational) ![Ashwin Shenoi](https://img.shields.io/badge/Ashwin%20Shenoi-informational) ![Sayooj B Kumar](https://img.shields.io/badge/Sayooj%20B%20Kumar-informational) ![Aman Sapra](https://img.shields.io/badge/Aman%20Sapra-informational)

🔗 **Link:** [ThreatShield - The Intelligent Way of Threat Modelling](https://github.com/threatshield/threatshield)  
📝 **Description:** ThreatShield is an AI-powered threat modeling and security analysis tool that automates the work using an enterprise LLM API. It ingests raw material — product requirement documents, architecture diagrams, Confluence pages, Slack threads, and meeting transcripts — and produces structured STRIDE and PASTA threat models, attack trees, DREAD scoring, mitigation plans, and ASVS test cases, turning scattered design artifacts into an actionable security assessment.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Pentesting made easy - Keeping sessions alive with session-chains</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Kai Glauber](https://img.shields.io/badge/Kai%20Glauber-informational) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational) ![Arvid Mukherjee](https://img.shields.io/badge/Arvid%20Mukherjee-informational)

🔗 **Link:** Not Available  
📝 **Description:** session-chains automatically establishes and refreshes authenticated sessions for any number of accounts, addressing the short-lived sessions, multistep logins, and dynamic MFA tokens that break authenticated automation during web application tests. Testers define reusable chains modelling the application's authentication flow; the tool then maintains valid sessions in the background and exposes them to downstream tooling. It integrates with Burp Suite and its extensions as well as CLI tools such as sqlmap and nuclei.

</details>

<details><summary><strong>Precogly: Open Source Threat Modeling for AI-Assisted Security</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Vikram Narayan](https://img.shields.io/badge/Vikram%20Narayan-informational)

🔗 **Link:** [Precogly: Open Source Threat Modeling for AI-Assisted Security](https://github.com/precogly/precogly)  
📝 **Description:** Precogly is an open-source alternative to commercial enterprise threat modeling platforms. It provides community-driven threat libraries, a full data flow diagram editor with reusable templates, and a unified threat analysis workspace, with integrations for taxonomies such as LINDDUN, CAPEC, and ATT&CK and compliance standards including PCI-DSS and NIST. Hooks allow AI-assisted threat modeling at enterprise scale, and reporting views serve security teams, risk managers, and compliance managers.

</details>

<details><summary><strong>QuicDraw & QuicDraw-UI: Racing and Fuzzing HTTP/3</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Maor Abutbul](https://img.shields.io/badge/Maor%20Abutbul-informational)

🔗 **Link:** [QuicDraw & QuicDraw-UI: Racing and Fuzzing HTTP/3](https://github.com/cyberark/QuicDrawH3)  
📝 **Description:** QuicDraw(H3) is an Apache-2.0 licensed security research tool for fuzzing and race-condition testing of HTTP/3 servers over QUIC. It implements a mechanism called Quic-Fin-Sync that enables high-speed, single-packet race-condition testing against HTTP/3 endpoints, and ships with a companion user interface for driving and reviewing test runs.

</details>

<details><summary><strong>WaffleX: Adaptive Semantic Analysis for WAF Resilience Testing</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Samet Can Tasci](https://img.shields.io/badge/Samet%20Can%20Tasci-informational) ![Mehmet Önder Key](https://img.shields.io/badge/Mehmet%20Önder%20Key-informational)

🔗 **Link:** Not Available  
📝 **Description:** WaffleX is a web defence validation framework for finding normalization gaps and parser inconsistencies across modern application delivery stacks. Instead of static payload lists it generates context-aware, semantically equivalent request variants to measure how CDNs, reverse proxies, WAFs, and origin applications interpret the same input differently. Correlating response behaviour, enforcement signals, and transformation patterns helps defenders reproduce blind spots and harden inspection logic, with an emphasis on explainability and reproducibility at scale.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Continuous Threat Modeling in Agentic AI era - tmdd</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![mik0w](https://img.shields.io/badge/mik0w-informational)

🔗 **Link:** [Continuous Threat Modeling in Agentic AI era - tmdd](https://github.com/attasec/tmdd)  
📝 **Description:** TMDD brings threat modeling into the repository so it stays current as code evolves. Using an AI agent of the user's choice, it analyses source to infer components and data flows and generates a version-controlled YAML threat model that is reviewed through pull requests. Threats and mitigations are linked to specific files for continuous validation, and the tool renders Markdown and HTML reports, surfacing undocumented attack surface and logic-level flaws.

</details>

<details><summary><strong>pymsi - Interactive MSI Installer Analysis in Python and the Browser</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational)

🔗 **Link:** [pymsi - Interactive MSI Installer Analysis in Python and the Browser](https://github.com/nightlark/pymsi)  
📝 **Description:** pymsi is a pure Python library for parsing, analysing, and extracting files from Windows Installer (MSI) packages, giving direct access to database tables, embedded streams, and installer metadata. A fully client-side web version wraps the library in a familiar lessmsi-style interface usable from any operating system. Unlike Windows-only tools such as lessmsi and orca, pymsi runs anywhere a suitable Python interpreter does, suiting sandboxed inspection of potentially malicious installers and automated analysis pipelines.

</details>

<details><summary><strong>SBoMPlay : SBoM Exploration and Intelligence extraction platform</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Anant Shrivastava](https://img.shields.io/badge/Anant%20Shrivastava-informational)

🔗 **Link:** [SBoMPlay : SBoM Exploration and Intelligence extraction platform](https://github.com/cyfinoid/sbomplay)  
📝 **Description:** SBoM Play is a browser-first, privacy-aware platform for exploring SBOMs without server setup or uploading dependency data anywhere. It imports SBOMs or extracts them from GitHub repositories and enriches them using osv.dev, deps.dev, and ecosyste.ms, presenting a unified view across repositories and organisations. Beyond vulnerability tracking it surfaces version drift and sprawl, license posture, SBOM quality scoring against CISA, BSI TR-03183, and CERT-In benchmarks, end-of-life packages, dependency confusion indicators, and maintainer concentration risk. Licensed GPL 3.0.

</details>

<details><summary><strong>Surfactant - Modular Framework for File Information Extraction and SBOM Generation</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational) ![Matthew Kelley](https://img.shields.io/badge/Matthew%20Kelley-informational)

🔗 **Link:** [Surfactant - Modular Framework for File Information Extraction and SBOM Generation](https://github.com/LLNL/Surfactant)  
📝 **Description:** Surfactant extracts software metadata from filesystems to help analysts understand system composition and generate a Software Bill of Materials. It identifies components, vendors, and third-party libraries from binaries and file artifacts and builds the relationships between them, supporting system-level vulnerability impact analysis for IoT, smart grid, and ICS devices. New capabilities include name and version recovery through Qiling userspace emulation, inter-binary reachability analysis with angr, Motorola S-record and Intel HEX firmware conversion, and capa integration.

</details>

<details><summary><strong>Vulnhalla 2.0: LLM-Guided Triage of CodeQL Findings</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Simcha Kosman](https://img.shields.io/badge/Simcha%20Kosman-informational)

🔗 **Link:** [Vulnhalla 2.0: LLM-Guided Triage of CodeQL Findings](https://github.com/cyberark/Vulnhalla)  
📝 **Description:** Vulnhalla is an open-source pipeline that runs CodeQL at scale and uses an LLM agent to triage findings as true or false positives. It extracts exactly the context the model needs from the CodeQL database via structured CSV artifacts for fast retrieval, then drives the model through reviewer-style checks — reachability, controllability, sanitization, boundary conditions — instead of one-shot prompts. Version 1.0 contributed to CVE-2025-60021 in Apache bRPC; version 2.0 adds Python and JavaScript support and local, closed-source analysis.

</details>

---
## 🔍 OSINT
<details><summary><strong>Dradis Framework: Intelligent Automation for collaboration and reporting</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [Dradis Framework: Intelligent Automation for collaboration and reporting](https://github.com/dradis/dradis-ce)  
📝 **Description:** Dradis is a self-hosted, GPLv2 collaboration and reporting platform that centralises findings, evidence, and attack narratives, combining output from Nessus, Burp Suite, Nikto, and more than 47 other scanners with manual research. Recent releases add context-aware LLM assistance with bring-your-own-model support so data stays on the user's infrastructure, agents and a prompt library for repeatable AI workflows, REST API scanner uploads, inline commenting for QA, and a MITRE ATT&CK coverage calculator.

</details>

<details><summary><strong>MORF - Mobile Reconnaissance Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Amrudesh](https://img.shields.io/badge/Amrudesh-informational) ![Abhishek JM](https://img.shields.io/badge/Abhishek%20JM-informational) ![Himanshu Kumar Das](https://img.shields.io/badge/Himanshu%20Kumar%20Das-informational)

🔗 **Link:** [MORF - Mobile Reconnaissance Framework](https://github.com/amrudesh1/morf)  
📝 **Description:** MORF is a lightweight, platform-independent mobile security analysis tool that automatically discovers sensitive information embedded in Android and iOS applications. Built for penetration testers, security professionals, and developers, it surfaces hardcoded secrets and other exposure across an application package and reports on the overall mobile security posture.

</details>

<details><summary><strong>ShadowHunt 2.0: Uncovering Shadow IT and Hidden Secrets</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Yakir Kadkoda](https://img.shields.io/badge/Yakir%20Kadkoda-informational) ![Assaf Morag](https://img.shields.io/badge/Assaf%20Morag-informational)

🔗 **Link:** [ShadowHunt 2.0: Uncovering Shadow IT and Hidden Secrets](https://github.com/cooltoolz/ShadowHunt2.0)  
📝 **Description:** ShadowHunt exposes shadow IT on public repositories, where employees push company code or fork internal projects from personal accounts. It maps personal repositories back to organisational staff by analysing public activity on GitHub, Docker Hub, Quay, Gist, and GHCR along with commit metadata, manifests, templates, and contributor patterns, then scans those repositories for leaked tokens, keys, and configuration files. It also generates base64 permutations to catch secrets that evade conventional scanners.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Brutus: Modern Multi-Protocol Credential Testing in Go</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![UNC1739](https://img.shields.io/badge/UNC1739-informational)

🔗 **Link:** [Brutus: Modern Multi-Protocol Credential Testing in Go](https://github.com/praetorian-inc/brutus)  
📝 **Description:** Brutus is a credential testing tool written in Go and shipped as a single dependency-free binary, addressing the build and integration friction of legacy tools such as THC Hydra. It covers more than 20 protocols including SSH, MySQL, PostgreSQL, MSSQL, Redis, SMB, RDP, and MongoDB, and streams JSON for pipeline use with fingerprintx and naabu. Notable additions include embedded SSH badkeys, RDP sticky-keys backdoor detection, and optional LLM-suggested vendor default credentials.

</details>

<details><summary><strong>ConfigManBearPig - Identify, Visualize, and Navigate SCCM Attack Paths in BloodHound</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mayyhem](https://img.shields.io/badge/Mayyhem-informational)

🔗 **Link:** [ConfigManBearPig - Identify, Visualize, and Navigate SCCM Attack Paths in BloodHound](https://github.com/SpecterOps/ConfigManBearPig)  
📝 **Description:** ConfigManBearPig collects data from a Microsoft Configuration Manager (formerly SCCM) environment using only a low-privileged Active Directory context. It identifies every hierarchy takeover path documented in the Misconfiguration Manager knowledgebase, along with several privilege escalation and credential gathering techniques, then maps and connects those relationships into the BloodHound graph so operators and defenders can explore and query SCCM attack paths interactively.

</details>

<details><summary><strong>CyberArkHound</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Javier Azofra Ovejero](https://img.shields.io/badge/Javier%20Azofra%20Ovejero-informational)

🔗 **Link:** [CyberArkHound](https://github.com/jazofra/CyberArkHound)  
📝 **Description:** CyberArkHound is an open-source assessment tool written in Go that exports CyberArk PVWA data — users, groups, safes, accounts, platforms, and permissions — into a BloodHound-compatible OpenGraph JSON file. Bridging privileged access management data with BloodHound's attack path engine makes opaque CyberArk permission structures queryable in Cypher and visible as attack graphs, exposing direct credential access, privilege escalation routes, dual control weaknesses, and credential chain dependencies that standard PAM auditing leaves hidden.

</details>

<details><summary><strong>FAInd my XPC: Automated Discovery of Privilege Escalation via macOS XPC Trust Boundaries - powered by LLM</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Hillel Pinto](https://img.shields.io/badge/Hillel%20Pinto-informational)

🔗 **Link:** [FAInd my XPC: Automated Discovery of Privilege Escalation via macOS XPC Trust Boundaries - powered by LLM](https://github.com/XMCyber/FAInd-my-xpc)  
📝 **Description:** XPC Hunter automates discovery and validation of privilege escalation through macOS XPC trust boundaries. It combines static binary analysis using otool protocol extraction and string-based service discovery, dynamic runtime enumeration via CDHash cache exploitation with NIB-injected JXA payloads, and LLM-based semantic scoring to rank attack surface. The tool targets applications exposing root-level XPC services protected only by CDHash trust, reducing hours of per-target reverse engineering to minutes across an entire installation.

</details>

<details><summary><strong>Ghost in the IDE</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pardhiv](https://img.shields.io/badge/Pardhiv-informational) ![Jayaram yalla](https://img.shields.io/badge/Jayaram%20yalla-informational)

🔗 **Link:** Not Available  
📝 **Description:** Ghost in the IDE is a command-and-control platform demonstrating supply chain attacks across the JetBrains IntelliJ, Visual Studio Code, and Eclipse plugin ecosystems simultaneously. It shows how a single plugin published to a marketplace — where review relies largely on automated static analysis — can pivot through a development organisation, exfiltrating source code, harvesting cloud credentials from the clipboard, logging keystrokes, and establishing persistent backdoors with the full privileges of developer workstations.

</details>

<details><summary><strong>Ghostwriter</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Christopher Maddalena](https://img.shields.io/badge/Christopher%20Maddalena-informational)

🔗 **Link:** [Ghostwriter](https://github.com/GhostManager/Ghostwriter)  
📝 **Description:** Ghostwriter is a free and open-source platform for offensive security operations that simplifies report writing, asset tracking, and assessment management. It manages clients, maintains a reusable findings library, and organises the infrastructure and domains used during engagements, while its reporting engine provides collaborative writing and customisable templates. Recent releases add Google Docs-style collaborative report editing, collaborative project notes, and integration with BloodHound Community Edition.

</details>

<details><summary><strong>JS-Tap v3: JavaScript Post-Exploitation Moves to the Endpoint</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Hoodoer](https://img.shields.io/badge/Hoodoer-informational)

🔗 **Link:** [JS-Tap v3: JavaScript Post-Exploitation Moves to the Endpoint](https://github.com/hoodoer/JS-Tap)  
📝 **Description:** JS-Tap began as a JavaScript XSS and post-exploitation payload with a C2 server; version 3 extends it to the endpoint with implants for browser extensions, Electron desktop applications, and Node.js CLI tools, all driven from one C2. The browser extension steals sessions across every domain visited and can inject the original DOM beacon on command, Electron patching covers apps such as Slack, Signal Desktop, and VS Code, and stolen sessions export as portable tickets for live session riding through the target's network.

</details>

<details><summary><strong>MLOKit: MLOps Attack Toolkit</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Brett Hawkins](https://img.shields.io/badge/Brett%20Hawkins-informational)

🔗 **Link:** [MLOKit: MLOps Attack Toolkit](https://github.com/h4wkst3r/MLOKit)  
📝 **Description:** MLOKit is an open-source C# toolkit for attacking MLOps platforms through their REST APIs, taking an attack module and valid credentials for the target. It supports Azure ML, Amazon SageMaker, Google Cloud Vertex AI, MLFlow, BigML, and Palantir AIP, with modules for reconnaissance, training data theft, model theft, model poisoning, and notebook attacks. This release adds nine modules covering compute instance enumeration, SSH key implantation, malicious training jobs for code execution, credential harvesting from job variables and logs, and JupyterLab execution over WebSocket.

</details>

<details><summary><strong>MSCodePhish - Dynamic Device Code Phishing Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Raunak Parmar](https://img.shields.io/badge/Raunak%20Parmar-informational) ![3xpl01tc0d3r](https://img.shields.io/badge/3xpl01tc0d3r-informational)

🔗 **Link:** [MSCodePhish - Dynamic Device Code Phishing Framework](https://github.com/TROUBLE-1/MSCodePhish)  
📝 **Description:** MSCodePhish turns Microsoft's Device Code OAuth flow into an embeddable phishing primitive. Rather than pre-generating codes and racing the 15-minute timeout, it exposes an API that a phishing page calls from JavaScript the moment a victim loads it, returning a fresh device code rendered as something like a coupon code. The framework polls Microsoft's token endpoint, captures the resulting refresh token and claims, and lets operators track campaigns and mint access tokens for ARM, Key Vault, Graph, Storage, or custom scopes.

</details>

<details><summary><strong>MSSQLHound - Identify, Visualize, and Navigate MSSQL Attack Paths in BloodHound</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mayyhem](https://img.shields.io/badge/Mayyhem-informational) ![Javier Azofra](https://img.shields.io/badge/Javier%20Azofra-informational)

🔗 **Link:** [MSSQLHound - Identify, Visualize, and Navigate MSSQL Attack Paths in BloodHound](https://github.com/SpecterOps/MSSQLHound)  
📝 **Description:** MSSQLHound enumerates Microsoft SQL Server principals and permissions at the domain, server, and database levels, processes the relationships between them, and identifies abusable attack paths. Results are mapped and connected into the BloodHound graph so operators and defenders can explore and query MSSQL privilege relationships interactively alongside Active Directory paths.

</details>

<details><summary><strong>Pentest Copilot V2: The Agentic Pentesting Workspace</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dhruva Goyal](https://img.shields.io/badge/Dhruva%20Goyal-informational) ![Sitaraman Subramanian](https://img.shields.io/badge/Sitaraman%20Subramanian-informational)

🔗 **Link:** [Pentest Copilot V2: The Agentic Pentesting Workspace](https://github.com/bugbasesecurity/pentest-copilot)  
📝 **Description:** Pentest Copilot V2 is an AI-native, browser-based workspace that gives pentesters, red teamers, and CTF players a single interface for reconnaissance, exploitation support, scripting, automation, and web testing, replacing a patchwork of terminals, browser tabs, notes, proxies, and one-off scripts. Version 2 moves the tool from a heavily human-in-the-loop assistant toward autonomy: it executes multi-step tasks with less supervision, uses parallel subagents, integrates with established security tooling, and applies guardrails for authorised environments.

</details>

<details><summary><strong>PwnSat 2.0: The Vulnerable Satellite Hacking Platform for Learning Through Research</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Romel Marin](https://img.shields.io/badge/Romel%20Marin-informational) ![Eduardo Contreras](https://img.shields.io/badge/Eduardo%20Contreras-informational)

🔗 **Link:** [PwnSat 2.0: The Vulnerable Satellite Hacking Platform for Learning Through Research](https://github.com/r0r0x-xx/PwnSat-2.0)  
📝 **Description:** PwnSat 2.0 is an open-source, vulnerable-by-design aerospace cybersecurity platform combining a physical 1U CubeSat, a LoRa/FSK ground station, and native support for an enterprise-grade command, control, and communications environment. Where version 1.0 covered RF attacks, this release adds full-chain mission compromise: lateral movement from a compromised ground station backend to unauthorised satellite control, live exploitation of CCSDS and AX.25, firmware memory corruption on the flight computer, and telemetry stream hijacking, mapped to the SPARTA framework.

</details>

<details><summary><strong>ROP ROCKET: New ASLR Bypass Mini-Tool & Automating Advanced ROP Attacks</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dr. Bramwell Brizendine](https://img.shields.io/badge/Dr.%20Bramwell%20Brizendine-informational) ![Shiva Shashank Kusuma](https://img.shields.io/badge/Shiva%20Shashank%20Kusuma-informational)

🔗 **Link:** [ROP ROCKET: New ASLR Bypass Mini-Tool & Automating Advanced ROP Attacks](https://github.com/Bw3ll/ROP_ROCKET)  
📝 **Description:** ROP ROCKET is an advanced Windows code-reuse attack framework with extensive automatic chain generation, including direct syscall chains, Heaven's Gate transitions between x86 and x64, and shellcodeless techniques that chain roughly 25 security-relevant WinAPIs. Gadget emulation — sometimes recursive across portions of a chain — resolves parameter, pointer, and distance problems that otherwise defeat automation. The new ASLR Bypass Mini-Tool generates nine bypasses for 64-bit high-entropy ASLR, building complete x64 chains that recover key system DLL bases.

</details>

<details><summary><strong>ShellWasp: Creating Shellcode with Windows Syscalls</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dr. Bramwell Brizendine](https://img.shields.io/badge/Dr.%20Bramwell%20Brizendine-informational)

🔗 **Link:** [ShellWasp: Creating Shellcode with Windows Syscalls](https://github.com/Bw3ll/ShellWasp)  
📝 **Description:** ShellWasp generates Windows syscall shellcode for 32-bit WoW64, tackling problems that make pure syscall shellcode impractical: system service numbers change across OS builds, WoW64 mechanics differ between Windows 7 and Windows 10/11, and building the required structures in position-independent assembly is painful. It identifies the target build at runtime, generates a syscall array with correct SSNs, and manages reuse. Build discovery methods include PEB, User_Shared_Data, and PEB-via-r12, alongside novel non-standard WoW64 syscall invocation paths.

</details>

<details><summary><strong>Social Engineering with Reel</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![James Williams](https://img.shields.io/badge/James%20Williams-informational)

🔗 **Link:** Not Available  
📝 **Description:** Reel is a workflow-driven phishing framework supporting credential capture campaigns with optional real-time MFA relay as well as email sending. Every element is configurable through its workflow system, allowing complex multi-stage campaigns to be composed, and a plugin system lets operators extend core functionality without modifying the framework's code.

</details>

<details><summary><strong>The Metasploit Framework 6.5: Malleable C2 Payloads, New Relay Capability and Protocol Session Upgrades</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jack Heysel](https://img.shields.io/badge/Jack%20Heysel-informational) ![zeroSteiner](https://img.shields.io/badge/zeroSteiner-informational)

🔗 **Link:** [The Metasploit Framework 6.5: Malleable C2 Payloads, New Relay Capability and Protocol Session Upgrades](https://github.com/rapid7/metasploit-framework)  
📝 **Description:** Metasploit 6.5 expands evasion and relaying. New Malleable C2 profiles for HTTP Meterpreter let operators define custom traffic patterns and headers so payload communications blend with network baselines and evade deep packet inspection and egress filtering. HTTP-to-SMB and HTTP-to-LDAP relaying open new attack workflows, and protocol-based sessions such as SMB can now be upgraded directly into Meterpreter, bridging a simple relay and full post-exploitation control, including ntlmrelay2self chains to domain admin via Shadow Credentials or RBCD.

</details>

<details><summary><strong>Trajan: Cross-Platform CI/CD Security Scanner</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Rahul Saranjame](https://img.shields.io/badge/Rahul%20Saranjame-informational) ![Ranganatha Rao Sridhar](https://img.shields.io/badge/Ranganatha%20Rao%20Sridhar-informational) ![Tanishq Rupaal](https://img.shields.io/badge/Tanishq%20Rupaal-informational)

🔗 **Link:** [Trajan: Cross-Platform CI/CD Security Scanner](https://github.com/praetorian-inc/trajan)  
📝 **Description:** Trajan is an open-source CI/CD security scanner providing vulnerability detection, attack validation, and infrastructure enumeration across GitHub Actions, GitLab CI, Azure DevOps, and Jenkins. It unifies and extends Praetorian's earlier Gato and Glato tools while adding first-class Azure DevOps support and attack coverage for AI/LLM pipelines. Six detection plugins cover 15 vulnerability types including pipeline injection, secrets exposure, service connection abuse, and self-hosted agent risk, alongside nine attack modules and 14 enumeration subcommands.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>AD Miner – One step further applying graph theory for Active Directory security analysis</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Clément TEYTAUD](https://img.shields.io/badge/Clément%20TEYTAUD-informational)

🔗 **Link:** [AD Miner – One step further applying graph theory for Active Directory security analysis](https://github.com/AD-Security/AD_Miner)  
📝 **Description:** AD Miner audits Active Directory and Entra ID environments by applying graph theory to data extracted from the BloodHound graph database. Rather than reporting the shortest attack paths, it uses weighted path-finding algorithms such as Dijkstra to surface the most easily exploitable compromise paths, prioritising realistic adversary routes for remediation. Sixty-five control points cover misconfigurations, excessive privileges, and identity hygiene, and reports serve both as audit appendices and as continuous posture monitoring.

</details>

<details><summary><strong>EMBArk – Firmware Analysis for the Enterprise</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Benedikt Kuehne](https://img.shields.io/badge/Benedikt%20Kuehne-informational) ![Michael Messner](https://img.shields.io/badge/Michael%20Messner-informational)

🔗 **Link:** [EMBArk – Firmware Analysis for the Enterprise](https://github.com/e-m-b-a/embark)  
📝 **Description:** EMBArk is a web-based enterprise front end for automated firmware security analysis, letting teams upload, analyse, track, and report on firmware vulnerabilities from a central system. It supports both single-host and distributed analysis across worker nodes, and exposes a web UI, CLI, and API so results integrate into larger supply chain workflows. The platform lets organisations verify vendor security claims for anything from a simple IoT gadget to a multi-system factory solution.

</details>

<details><summary><strong>fetter</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Christopher Ariza](https://img.shields.io/badge/Christopher%20Ariza-informational)

🔗 **Link:** [fetter](https://github.com/fetter-io/fetter-rs)  
📝 **Description:** Fetter scans the packages actually installed across every Python virtual environment or an entire system and checks them against the OSV vulnerability database, returning detailed findings and CVSS scores. Repository controls limit what can be downloaded and tools like pip-audit examine requirements and lock files, but neither answers what vulnerable packages are really present — a gap that matters when malware such as spellcheckpy is installed outside declared dependencies. Fetter reports the highest-risk packages across an infrastructure in seconds.

</details>

<details><summary><strong>Keychecker : SSH Key based attack tool for DVCS Systems</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Anant Shrivastava](https://img.shields.io/badge/Anant%20Shrivastava-informational)

🔗 **Link:** [Keychecker : SSH Key based attack tool for DVCS Systems](https://github.com/cyfinoid/keychecker)  
📝 **Description:** KeyChecker is a Python CLI tool that fingerprints SSH private keys and identifies which Git hosting accounts they unlock, turning a recovered key into a scoped blast radius report. It performs local key intelligence across OpenSSH, PEM, and DER formats, detecting key type, size, passphrase protection, and fingerprints, then validates against GitHub, GitLab, Bitbucket, Codeberg, Gitea, and Hugging Face using safe handshakes and read-only git ls-remote probes. Licensed GPL 3.0 and free of write operations.

</details>

<details><summary><strong>OWASP Faction 2.0</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Summitt](https://img.shields.io/badge/Josh%20Summitt-informational) ![Sandra Arber](https://img.shields.io/badge/Sandra%20Arber-informational)

🔗 **Link:** [OWASP Faction 2.0](https://github.com/factionsecurity/faction)  
📝 **Description:** OWASP Faction is an open-source penetration testing assessment and reporting platform, and version 2.0 is a ground-up rebuild giving teams control over every stage of the assessment lifecycle. The release introduces AI-assisted report writing, a CLI integration framework, a full application inventory and tracking system, and a new user interface. It targets the bottlenecks of manual engagements with a collaborative, extensible workflow that scales from a solo consultant to a large enterprise team.

</details>

<details><summary><strong>PrivacyTrollShield: An Open-Source Scanner for Privacy Compliance</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Aaron Tekippe](https://img.shields.io/badge/Aaron%20Tekippe-informational)

🔗 **Link:** [PrivacyTrollShield: An Open-Source Scanner for Privacy Compliance](https://github.com/atekippe/PrivacyTrollShield)  
📝 **Description:** PrivacyTrollShield is an open-source scanner that finds the tracking behaviour behind the wave of wiretapping litigation aimed at public websites. It launches a headless browser and monitors every network request before and after consent interactions, comparing actual site behaviour against what the consent banner promises. The tool detects more than 40 pre-consent trackers, flags session replay tools by data sensitivity, identifies form data leaking to third parties, and verifies that declining consent genuinely stops collection.

</details>

<details><summary><strong>ReARM: Release Governance Platform</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Pavel Shukhman](https://img.shields.io/badge/Pavel%20Shukhman-informational)

🔗 **Link:** [ReARM: Release Governance Platform](https://github.com/relizaio/rearm)  
📝 **Description:** ReARM — Reliza's Artifact and Release Management — is a DevSecOps and supply chain security tool that doubles as an SBOM/xBOM repository and evidence store. It organises product releases together with their metadata, including Bills of Materials in various formats and associated security findings, maintaining security documents and findings on a per-release basis.

</details>

<details><summary><strong>ThreatXtension: AI-Powered Browser Extension Security Analysis Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Itzik Chimino](https://img.shields.io/badge/Itzik%20Chimino-informational) ![Bar Haim](https://img.shields.io/badge/Bar%20Haim-informational)

🔗 **Link:** [ThreatXtension: AI-Powered Browser Extension Security Analysis Framework](https://github.com/barvhaim/ThreatXtension)  
📝 **Description:** ThreatXtension automates Chrome extension security analysis by combining static application security testing with LLM-powered threat intelligence, assessing permission risk, detecting obfuscated malicious patterns, and generating natural-language threat summaries. A LangGraph pipeline orchestrates acquisition from the Chrome Web Store, manifest V2/V3 parsing, parallel analyzer execution, and result synthesis, backed by custom Semgrep rulesets mapped to MITRE ATT&CK. It supports IBM WatsonX, OpenAI, and local Ollama backends across CLI, web UI, and FastMCP interfaces.

</details>

<details><summary><strong>WebAgentAudit: Security Auditing of Web-Based AI Agents Through Browser Automation</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Nethanel Gelernter](https://img.shields.io/badge/Nethanel%20Gelernter-informational)

🔗 **Link:** [WebAgentAudit: Security Auditing of Web-Based AI Agents Through Browser Automation](https://github.com/atom41research/webagentaudit)  
📝 **Description:** WebAgentAudit is an open-source Python framework for security auditing of AI agents that expose no API — the chatbots, assistants, and LLM widgets embedded in websites, often operated by third parties. Given a URL, it locates the chat elements, builds a communication channel through browser automation, and runs probes for prompt injection, system prompt extraction, jailbreaks, and role confusion, entirely algorithmically and without consuming LLM API tokens. Built on Playwright, it handles floating widgets, iframes, and lazy-loaded panels.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>AC Scanner - QubitAC Automated Post-Quantum Cryptography Discovery Tool</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Anurag Swarnim Yadav](https://img.shields.io/badge/Anurag%20Swarnim%20Yadav-informational) ![hachinijuku](https://img.shields.io/badge/hachinijuku-informational)

🔗 **Link:** [AC Scanner - QubitAC Automated Post-Quantum Cryptography Discovery Tool](https://github.com/qubitac/AC-Scanner)  
📝 **Description:** AC Scanner is an open-source pipeline that discovers an organisation's cryptographic surface across TLS endpoints and SSH services and assesses it against NIST post-quantum standards. A single command chains subdomain enumeration, DNS resolution, OpenSSL handshake analysis, ssh-audit inspection, and quantum vulnerability scoring, emitting a Cryptographic Bill of Materials in JSONL, JSON, or Markdown for an interactive dashboard. It gives defenders an evidence-grade path from discovery to Harvest Now Decrypt Later compliance reporting.

</details>

<details><summary><strong>ARAY: Benign Binary Synthesis for Signature Validation Without the Malware</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Emanuel Valente](https://img.shields.io/badge/Emanuel%20Valente-informational)

🔗 **Link:** [ARAY: Benign Binary Synthesis for Signature Validation Without the Malware](https://github.com/c2dc/aray)  
📝 **Description:** Aray generates non-malicious executables that match a given YARA rule, letting security teams validate detection logic without handling malware samples. From a .yar file it produces a benign Linux ELF, Windows PE, or generic artifact satisfying every structural constraint, including byte-offset placement, section alignment, integer constant encoding, UTF-16LE wide strings, and PE header requirements. A nine-node LangGraph pipeline drives an LLM, with local small models supported for fully offline operation.

</details>

<details><summary><strong>Azazel-Edge : Deterministic Edge Decision Support for Constrained SOC/NOC Operations</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Makoto "Mr. Rabbit" SUGITA](https://img.shields.io/badge/Makoto%20"Mr.%20Rabbit"%20SUGITA-informational)

🔗 **Link:** [Azazel-Edge : Deterministic Edge Decision Support for Constrained SOC/NOC Operations](https://github.com/01rabbit/Azazel-Edge)  
📝 **Description:** Azazel-Edge is a deterministic edge decision appliance for small, temporary, or rapidly deployed networks where defenders work with limited infrastructure, staff, and connectivity. It evaluates operational reliability and security threat context separately, resolves them through a deterministic action arbiter, and records selected evidence, rejected alternatives, and structured explanation. Optional AI assistance is confined to operator support and never participates in action selection, targeting disaster response, field operations, and isolated networks.

</details>

<details><summary><strong>capa: Beyond Disassembly: Dynamic Matching for Static Blindspots</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mike Hunhoff](https://img.shields.io/badge/Mike%20Hunhoff-informational) ![Josh Stroschein](https://img.shields.io/badge/Josh%20Stroschein-informational)

🔗 **Link:** [capa: Beyond Disassembly: Dynamic Matching for Static Blindspots](https://github.com/mandiant/capa)  
📝 **Description:** capa identifies capabilities in executable files through rule-based matching, and this release applies that engine directly to dynamic execution data to cover what static analysis cannot reach: packed samples and large, obfuscated Rust and Go binaries. The dynamic matching engine groups and sequences related API calls to recognise complex behaviours such as memory allocation and code injection after unpacking or de-obfuscation, giving analysts consistent capability recovery across static and dynamic domains without manually triaging execution traces.

</details>

<details><summary><strong>Chameleon Forensics (Android): Assume Adversarial Logical Extraction Forensic Tool</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joseph Lim](https://img.shields.io/badge/Joseph%20Lim-informational) ![Vivek Balachandran](https://img.shields.io/badge/Vivek%20Balachandran-informational)

🔗 **Link:** [Chameleon Forensics (Android): Assume Adversarial Logical Extraction Forensic Tool](https://github.com/Ins1ght32/Chameleon-Forensics-Android)  
📝 **Description:** Chameleon Forensics is an Android logical acquisition tool built on the assumption that the target device may have been modified to detect and disrupt forensic extraction. Extending the process in NIST SP 800-101 Revision 1, it adds a pre-acquisition triage step that flags applications likely to interfere with acquisition, then applies adversarial-aware collection workflows. The approach aims to make evidence collection more reliable in environments where conventional ADB or agent-based assumptions do not hold.

</details>

<details><summary><strong>Cleric: ETW Sandbox and Memory Scanner</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Brandon McGrath](https://img.shields.io/badge/Brandon%20McGrath-informational)

🔗 **Link:** Not Available  
📝 **Description:** Cleric is an integrated Windows malware analysis framework for deep runtime inspection of suspicious processes. Paladin, a C++ memory scanner, applies 15 detection techniques across threads, memory regions, modules, and syscall stubs to find RWX regions, callstack anomalies, IAT/EAT hooks, and API tampering. A C# orchestrator coordinates PE-Sieve, Frida hooking, and ETW/Sysmon collection; a Python ETL pipeline normalises the results into JSON, CSV, SQLite, or MongoDB for a React dashboard.

</details>

<details><summary><strong>Command Line Threat Analyzer</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rohit Mukherjee](https://img.shields.io/badge/Rohit%20Mukherjee-informational)

🔗 **Link:** Not Available  
📝 **Description:** The Command Line Threat Analyzer detects and analyses suspicious command line activity on Windows, Linux, and macOS, correlating related commands across time and context so analysts see the whole attack sequence rather than isolated alerts. More than 240 detection rules are organised hierarchically by operating system, category, and technique, with regex pattern matching, behavioural analysis for novel patterns, MITRE ATT&CK mapping, an interactive visualisation dashboard, and a rule creation wizard.

</details>

<details><summary><strong>CrowdSentinel: AI-Orchestrated Threat Hunting Across Unified Security Data Sources</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Thomas Xuan Meng](https://img.shields.io/badge/Thomas%20Xuan%20Meng-informational)

🔗 **Link:** [CrowdSentinel: AI-Orchestrated Threat Hunting Across Unified Security Data Sources](https://github.com/thomasxm/CrowdSentinels-AI-MCP)  
📝 **Description:** CrowdSentinel is an open-source Model Context Protocol server that unifies Elasticsearch, Wireshark, Chainsaw, and thousands of detection rules behind a single natural-language endpoint, exposing 79 MCP tools. A request such as hunting for lateral movement triggers autonomous execution across EQL sequences, Sigma rules, and PCAP analysis with IoC correlation held in persistent investigation state. The Cyber Kill Chain, Pyramid of Pain, and Diamond Model guide analysis, and detections receive automatic MITRE ATT&CK mapping.

</details>

<details><summary><strong>INFLEX: Cross-Format Malware Analysis and Correlation Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Kyle Murbach](https://img.shields.io/badge/Kyle%20Murbach-informational) ![Luke Bower](https://img.shields.io/badge/Luke%20Bower-informational)

🔗 **Link:** Not Available  
📝 **Description:** INFLEX is a heterogeneous malware analysis framework that analyses, enriches, and correlates artifacts across PE, ELF, shellcode, and malicious documents in one workflow, combining static analysis, emulation, optional dynamic sandboxing, and threat intelligence enrichment. Deep feature extraction covers structural metadata, disassembly, behavioural traces, and function-level hashing to identify shared code across variants. Normalised results are stored in a scalable database so analysts can correlate relationships across large collections and accelerate triage.

</details>

<details><summary><strong>Intercept.js: Context-Aware YARA for Runtime Detection In JavaScript Environments</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rishi Kant](https://img.shields.io/badge/Rishi%20Kant-informational)

🔗 **Link:** [Intercept.js: Context-Aware YARA for Runtime Detection In JavaScript Environments](https://github.com/rishi-sekantsec/sekant-intercept-js)  
📝 **Description:** Intercept.js is an open-source detection engine written in vanilla JavaScript that fuses byte-level pattern matching with runtime context in a single rule model, targeting browsers, email clients, and Office add-ins where payloads exist only as in-memory buffers. Compatible with standard YARA syntax and modules, it lets rules combine content inspection with metadata such as domain novelty, sender reputation, MIME discrepancies, and user gesture state. Aho-Corasick matching and enforced match caps keep it viable in constrained environments.

</details>

<details><summary><strong>KEIP: Kernel-Enforced Install-Time Policies</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![otsmane ahmed](https://img.shields.io/badge/otsmane%20ahmed-informational)

🔗 **Link:** [KEIP: Kernel-Enforced Install-Time Policies](https://github.com/Otsmane-Ahmed/KEIP)  
📝 **Description:** KEIP is a real-time behavioural monitor that targets Python supply chain attacks at package installation time. Using eBPF and Linux Security Modules, it hooks the kernel to intercept and evaluate network activity from pip install and python processes, terminating the whole process group when an installation script attempts anomalous operations such as a reverse shell on a non-standard port or C2 scanning. Forensic .pth auditing detects silent persistence dropped in site-packages, and Linux file capabilities allow sudo-less enforcement in CI/CD.

</details>

<details><summary><strong>LogonTracer v2: Faster Malicious Windows Logon Investigations with AI Agent</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational) ![Yuki Yano](https://img.shields.io/badge/Yuki%20Yano-informational)

🔗 **Link:** [LogonTracer v2: Faster Malicious Windows Logon Investigations with AI Agent](https://github.com/JPCERTCC/LogonTracer)  
📝 **Description:** LogonTracer v2 helps defenders find suspicious Windows logons buried in high-volume event data by organising authentication activity into a graph of users and hosts and reducing large event sets to a small number of high-value leads. Version 2 adds AI-assisted workflows: an agent that investigates Windows Event Logs for malicious logon patterns, LLM-based summarisation that turns complex activity into readable investigation summaries, and Sigma rule generation that converts discovered behaviour into reusable detections.

</details>

<details><summary><strong>MachStealer:One Pipeline Behind Every macOS Infostealer</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Atsushi Sada](https://img.shields.io/badge/Atsushi%20Sada-informational)

🔗 **Link:** [MachStealer:One Pipeline Behind Every macOS Infostealer](https://github.com/ultra-supara/MachStealer)  
📝 **Description:** MachStealer is an open-source proof of concept for macOS on Apple Silicon that reproduces the credential harvesting pipeline shared by AMOS, Poseidon, Banshee, Cthulhu, and Cuckoo: Keychain extraction, PBKDF2 key derivation, SQLite database copy, and AES decryption, with parameters matching Chromium's source. It covers cookies, saved logins, credit cards, history, and extensions across all Chrome profiles. Exfiltration, C2, persistence, and anti-analysis are deliberately omitted so defenders can validate EDR detection safely.

</details>

<details><summary><strong>Mecha Hayabusa by Yamato Security</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tanaka Zakku](https://img.shields.io/badge/Tanaka%20Zakku-informational) ![Akira Nishikawa](https://img.shields.io/badge/Akira%20Nishikawa-informational) ![PINK](https://img.shields.io/badge/PINK-informational)

🔗 **Link:** [Mecha Hayabusa by Yamato Security](https://github.com/Yamato-Security/mecha-hayabusa)  
📝 **Description:** Mecha Hayabusa is a Model Context Protocol server that connects the Windows event log analysis tool Hayabusa to large language models for natural-language digital forensics and threat hunting. It converts CSV-based Hayabusa timelines into a local DuckDB database and exposes structured investigation capabilities, letting an LLM run a full DFIR workflow from dataset triage and hypothesis development through attack-phase analysis, lateral movement correlation, and structured incident report generation.

</details>

<details><summary><strong>MEM-SBOM: Runtime SBOM Generation from Python Process Memory</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Hala Ali](https://img.shields.io/badge/Hala%20Ali-informational) ![Andrew Case](https://img.shields.io/badge/Andrew%20Case-informational)

🔗 **Link:** [MEM-SBOM: Runtime SBOM Generation from Python Process Memory](https://github.com/HalaAli198/MEM-SBOM)  
📝 **Description:** MEM-SBOM is a suite of Volatility 3 plugins that reconstructs Software Bills of Materials directly from the runtime state of Python applications. Static tools read build manifests and package files, which diverge from reality in an ecosystem full of conditional imports, lazy loading, custom loaders, and multi-process execution. By analysing process memory, MEM-SBOM recovers every loaded module, resolves package versions, and emits CycloneDX-compliant output describing what actually ran — valuable when a host has crashed, been encrypted by ransomware, or is otherwise inaccessible.

</details>

<details><summary><strong>Nogitsune: eBPF-Based Anti-VM Detection for Linux Malware Analysis</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![t0x1n](https://img.shields.io/badge/t0x1n-informational) ![Harsh Ramjibhai](https://img.shields.io/badge/Harsh%20Ramjibhai-informational)

🔗 **Link:** Not Available  
📝 **Description:** Nogitsune is an eBPF-based anti-VM defeat toolkit for Linux malware analysis, removing the need to patch QEMU, rebuild SeaBIOS, or hold hypervisor access. It intercepts file reads and syscalls in the kernel and rewrites hardware identifiers before malware sees them, turning an exposed VirtualBox guest into a convincing physical workstation. The toolkit covers ten DMI file paths, spoofs MAC addresses across file read, ioctl, and netlink queries, hides processes including itself, and alters disk, CPU, and memory attributes at runtime on stock kernels.

</details>

<details><summary><strong>Obscurize: Malware for Defense and Counter Offense</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Aaron Beardslee](https://img.shields.io/badge/Aaron%20Beardslee-informational)

🔗 **Link:** Not Available  
📝 **Description:** Obscurize inverts the environment checks that malware performs before detonating, adapting the userland DLL injection technique of the r77 rootkit documented in Securonix's OBSCURE#BAT research. A Windows service reflectively injects agent DLLs into every new process and applies 20 Detours API hooks with no kernel driver, spoofing at the API layer via GetSystemFirmwareTable, NtQueryValueKey, and systeminfo.exe output interception. Defensive mode makes real hardware look like a virtual machine so malware self-terminates; Trap mode makes a VM look genuine so samples run their full chain.

</details>

<details><summary><strong>PETriage: Cross-Platform PE Surface Analysis for Malware Triage</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yuki Umemura](https://img.shields.io/badge/Yuki%20Umemura-informational)

🔗 **Link:** [PETriage: Cross-Platform PE Surface Analysis for Malware Triage](https://github.com/uky007/PETriage)  
📝 **Description:** PETriage is a Rust-based static PE surface analysis tool that runs natively and fully offline on Linux, macOS, and Windows, sparing analysts a Windows VM for routine triage. It inspects PE structure, metadata, imports, resources, and overlays, integrating suspicious API indicators and anomaly detection with rule IDs, severity levels, and evidence fields, and surfaces OPSEC artifacts such as leaked PDB paths. A CLI workflow with structured JSON and NDJSON output, batch processing, and severity gating supports automation, with optional GUI and TUI interfaces.

</details>

<details><summary><strong>Practical Ransomware Detection on macOS (via Math, not AI)</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [Practical Ransomware Detection on macOS (via Math, not AI)](https://github.com/objective-see/RansomWhere)  
📝 **Description:** RansomWhere? is a free, open-source tool that generically detects and stops macOS ransomware by observing the behaviour common to nearly every variant: rapidly transforming user files into encrypted data. Built on Apple's Endpoint Security framework, it applies entropy-based analysis to separate benign file activity from encryption and simple mathematical heuristics to distinguish encrypted data from compressed data. The approach uses no signatures and no machine learning, and has been tested against real macOS ransomware samples.

</details>

<details><summary><strong>StegoScan</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Luke Bower](https://img.shields.io/badge/Luke%20Bower-informational)

🔗 **Link:** [StegoScan](https://github.com/LCBOWER33/StegoScan)  
📝 **Description:** StegoScan automates steganography detection across websites, web servers, and local directories, combining multiple steganalysis techniques with AI-driven object and text recognition. A single command can sweep entire domains or IP ranges, scraping and deeply extracting a wide range of file formats before running layered tests — in one case recovering a message hidden in an image embedded in a PDF linked from the original page. AI models improve text recovery from media degraded by noise, distortion, or unconventional fonts.

</details>

<details><summary><strong>Suricata 8: Discover the Difference in Network Detection</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Peter Manev](https://img.shields.io/badge/Peter%20Manev-informational) ![Jeff Lukcovsky](https://img.shields.io/badge/Jeff%20Lukcovsky-informational) ![Lukas Sismis](https://img.shields.io/badge/Lukas%20Sismis-informational)

🔗 **Link:** [Suricata 8: Discover the Difference in Network Detection](https://github.com/OISF/suricata)  
📝 **Description:** Suricata is a high-performance open-source network analysis and threat detection engine used across private and public organisations and embedded by major vendors, operating as an IDS, IPS, firewall, network security monitor, and PCAP logger. Version 8, the product of two years of community and consortium development, adds a firewall mode of operation, a complete Lua overhaul, eight new protocols including mDNS, LDAP, DNS-over-HTTPS, and WebSocket, more than 100 new detection keywords, bidirectional rules, and CPU affinity controls.

</details>

<details><summary><strong>Suricata Turbo: Let Your NIC Drop the Flows Suricata Won't Miss</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Lukas Sismis](https://img.shields.io/badge/Lukas%20Sismis-informational)

🔗 **Link:** [Suricata Turbo: Let Your NIC Drop the Flows Suricata Won't Miss](https://github.com/DynaNIC/suricata-turbo)  
📝 **Description:** Suricata Turbo adds hardware traffic filtering offload to Suricata so that benign traffic never reaches the CPU. Suricata can already bypass uninteresting flows such as encrypted traffic or elephant flows in software, but the CPU still touches every packet; Turbo pushes that decision into the network card while Suricata continues to track offloaded flows through the hardware connection table. It supports both preconfigured filtering rules and dynamic filtering driven by detection policy at runtime, on commodity cards from multiple vendors.

</details>

<details><summary><strong>Suzaku by Yamato Security</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tanaka Zakku](https://img.shields.io/badge/Tanaka%20Zakku-informational) ![Akira Nishikawa](https://img.shields.io/badge/Akira%20Nishikawa-informational) ![PINK](https://img.shields.io/badge/PINK-informational)

🔗 **Link:** [Suzaku by Yamato Security](https://github.com/Yamato-Security/suzaku)  
📝 **Description:** Suzaku is an open-source, Sigma-based threat hunting and DFIR timeline generator for cloud logs from Yamato Security, the team behind Hayabusa. Written in Rust for memory safety and performance, it scans JSON and compressed JSON.gz log files with multithreading to surface attacker activity across large datasets. This release deepens AWS CloudTrail analysis with new API category support, improved GeoIP enrichment, and wider Sigma correlation coverage, and introduces Azure log support. Output is available as CSV, JSON, and JSONL.

</details>

<details><summary><strong>TSURUGI LINUX - the sharpest weapon in your DFIR arsenal</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Giovanni 'sug4r' Rattaro](https://img.shields.io/badge/Giovanni%20'sug4r'%20Rattaro-informational) ![Marco 'Blackmoon' Giorgi](https://img.shields.io/badge/Marco%20'Blackmoon'%20Giorgi-informational)

🔗 **Link:** [TSURUGI LINUX - the sharpest weapon in your DFIR arsenal](https://tsurugi-linux.org/)  
📝 **Description:** Tsurugi Linux is a DFIR-focused Linux distribution assembled by working incident responders for the moments when the right tool is needed at the wrong time. It ships a ready-to-use forensics toolset so analysts are not blocked by missing internal information or unavailable tooling during an incident, and it also serves educational use. A special Black Hat edition is released to attendees alongside an updated version of the BENTO portable toolkit.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>ICSForge™: OT/ICS Security Coverage Validation Platform</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Can Kurnaz](https://img.shields.io/badge/Can%20Kurnaz-informational)

🔗 **Link:** [ICSForge™: OT/ICS Security Coverage Validation Platform](https://github.com/ICSForge/ICSForge)  
📝 **Description:** ICSForge is an open-source OT/ICS security coverage validation platform that helps defenders and OT engineers test detection, visibility, and readiness against real industrial attack techniques. It generates realistic traffic and PCAPs across more than 500 scenarios in ten industrial protocols including Modbus/TCP, DNP3, S7comm, IEC-104, OPC UA, EtherNet/IP, BACnet/IP, MQTT, GOOSE, and PROFINET DCP, covering 68 of 83 MITRE ATT&CK for ICS v18 techniques. A safe-by-design sender-receiver architecture avoids touching other OT devices.

</details>

<details><summary><strong>LoRaCraft – Crafting Attacks for LoRaWAN Networks</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Pinar](https://img.shields.io/badge/Pinar-informational) ![musana](https://img.shields.io/badge/musana-informational)

🔗 **Link:** [LoRaCraft – Crafting Attacks for LoRaWAN Networks](https://github.com/pinarsadioglu/loracraft)  
📝 **Description:** LoRaCraft is a LoRaWAN security assessment framework built for real audits of the smart meters, agricultural sensors, and industrial automation that rely on the protocol. It covers join request replay against LoRaWAN 1.0.x DevNonce weaknesses, AES-CTR bit-flipping, authenticated packet injection with known session keys, energy depletion through confirmed uplink flooding and MAC command abuse, and rogue gateway operation. Traffic arrives from PCAPs, MQTT subscriptions to ChirpStack or TTN, or a built-in fake gateway, with optional SDR-based jamming and PHY sniffing.

</details>

<details><summary><strong>Medaudit, an AI assisted Tool for Auditing Hospital Networks and Pentesting Medical Devices</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Anirudh Duggal](https://img.shields.io/badge/Anirudh%20Duggal-informational) ![Vinod Tiwari](https://img.shields.io/badge/Vinod%20Tiwari-informational)

🔗 **Link:** [Medaudit, an AI assisted Tool for Auditing Hospital Networks and Pentesting Medical Devices](https://github.com/anirudhduggal/medaudit2)  
📝 **Description:** Medaudit is an open-source toolkit for auditing medical device network traffic with a focus on the HL7 protocol. It identifies unencrypted transmissions, detects PHI and PII exposure, and evaluates device resilience through fuzz testing and malformed payloads, with AI-assisted triage prioritising high-risk findings. A web interface manages projects, visualises traffic, and exports results, aimed at network auditors and healthcare security teams working between compliance and proactive testing.

</details>

<details><summary><strong>SafeScribe - Edge Device AI Meeting Notetaker</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Syed Hadi](https://img.shields.io/badge/Syed%20Hadi-informational)

🔗 **Link:** Not Available  
📝 **Description:** SafeScribe is a privacy-first desk device that transcribes and summarises meetings entirely on-device and delivers structured notes to the user's inbox as a PDF. It requires no subscription, no cloud service, and no vendor lock-in, targeting organisations that want meeting transcription without sending audio or transcripts to a third party.

</details>

<details><summary><strong>VulnZoo: A Complete Vulnerable IoT Ecosystem for Security Research and Training</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jorge Wallace Ruiz](https://img.shields.io/badge/Jorge%20Wallace%20Ruiz-informational) ![Máximo García Aroca](https://img.shields.io/badge/Máximo%20García%20Aroca-informational)

🔗 **Link:** [VulnZoo: A Complete Vulnerable IoT Ecosystem for Security Research and Training](https://github.com/DEKRA-Cybersecurity/VulnZoo)  
📝 **Description:** VulnZoo is an open-source ecosystem of deliberately vulnerable devices covering embedded, medical, industrial, and automotive environments. Where most training platforms present isolated components, VulnZoo models a complete IoT product from device firmware through mobile applications to cloud services, so learners and researchers can study realistic attack chains that move between multiple components rather than exercising a single target in isolation.

</details>

<details><summary><strong>xEndity</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Zeus Chan](https://img.shields.io/badge/Zeus%20Chan-informational) ![Kenneth Lee](https://img.shields.io/badge/Kenneth%20Lee-informational) ![Ernest Lim](https://img.shields.io/badge/Ernest%20Lim-informational)

🔗 **Link:** [xEndity](https://github.com/kenleejl/xEndityv2)  
📝 **Description:** xEndity is an open-source, end-to-end IoT firmware emulation platform that turns raw firmware binaries into network-ready virtual device instances without physical hardware. Three components handle the pipeline: xQuire for firmware acquisition and indexing, xScout for binary analysis, extraction, and vulnerability scanning, and xFormation for emulation orchestration, network isolation, and telemetry collection. The result serves both as an unrestricted penetration testing range and as a high-interaction honeypot layer, with Suricata IDS and a telemetry dashboard for behavioural analysis.

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>AgentsLeak: Runtime Protection for AI Coding Agents</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Inga Cherny](https://img.shields.io/badge/Inga%20Cherny-informational)

🔗 **Link:** [AgentsLeak: Runtime Protection for AI Coding Agents](https://github.com/IngaCherny/AgentsLeak)  
📝 **Description:** AgentsLeak is an open-source runtime security platform that hooks into AI coding agent engines such as Claude Code and Cursor and evaluates security policy before every action. It monitors file access, network connections, process creation, and command execution, applying real-time blocking and behavioural sequence detection, and surfaces activity through a security dashboard. The result is endpoint-protection-style enforcement purpose-built for AI agent sessions.

</details>

<details><summary><strong>Bastet: An Infrastructure for Benchmarking LLM Smart Contract Auditing</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Alice Hsu](https://img.shields.io/badge/Alice%20Hsu-informational) ![SunSec](https://img.shields.io/badge/SunSec-informational)

🔗 **Link:** [Bastet: An Infrastructure for Benchmarking LLM Smart Contract Auditing](https://github.com/OneSavieLabs/Bastet)  
📝 **Description:** Bastet pairs a curated dataset of common DeFi smart contract vulnerabilities with an AI-driven automated detection process. It concentrates on flaws that static analysis tools miss but that are routinely rated medium to high severity in audit competitions and frequently cause financial loss. The dataset draws on real-world issues observed on-chain and in competitions, and tailored detection workflows benchmark and improve LLM accuracy across development, auditing, and ongoing monitoring.

</details>

<details><summary><strong>GolemHalt: A Deterministic Reference Monitor for AI Coding Agents</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Matthew Maisel](https://img.shields.io/badge/Matthew%20Maisel-informational) ![John Brock](https://img.shields.io/badge/John%20Brock-informational) ![Adam Mondl](https://img.shields.io/badge/Adam%20Mondl-informational)

🔗 **Link:** [GolemHalt: A Deterministic Reference Monitor for AI Coding Agents](https://github.com/sondera-ai/sondera-coding-agent-hooks)  
📝 **Description:** GolemHalt is a reference monitor that regulates the behaviour of AI coding agents with hard, deterministic boundaries rather than system prompts or probabilistic guardrails. Rust hook binaries, the formally verifiable Cedar Policy Language, and YARA-X intercept every shell command, file operation, and web request made by Claude Code, Cursor, GitHub Copilot, Gemini CLI, and VS Code. Agent workflows are mapped into a standardised Trajectory Event Model to block irreversible actions and control information flow before execution.

</details>

<details><summary><strong>HoneyMCP: A Deception Security Layer for MCP Servers</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Bar Haim](https://img.shields.io/badge/Bar%20Haim-informational) ![Alon Malach](https://img.shields.io/badge/Alon%20Malach-informational)

🔗 **Link:** [HoneyMCP: A Deception Security Layer for MCP Servers](https://github.com/barvhaim/HoneyMCP)  
📝 **Description:** HoneyMCP is an open-source deception layer for Model Context Protocol servers that detects AI-agent attacks through one-line integration. It injects deceptive ghost tools, either statically defined or LLM-generated, to surface data exfiltration attempts and indirect prompt injection. Triggered tools emit high-fidelity AttackFingerprint telemetry covering session, tool sequence, threat category, and context, and two response modes are available: immediate lockout, or sustained deception using synthetic outputs.

</details>

<details><summary><strong>MCParasite: Universal MCP Worm Security Testing Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Utku YILDIRIM](https://img.shields.io/badge/Utku%20YILDIRIM-informational) ![Ozzy](https://img.shields.io/badge/Ozzy-informational)

🔗 **Link:** [MCParasite: Universal MCP Worm Security Testing Framework](https://github.com/Y1LD1R1M-1337/mcparasite)  
📝 **Description:** MCParasite is an open-source research framework that chains known prompt injection and tool poisoning techniques to test whether they compose into a self-propagating worm inside the Model Context Protocol. Tool poisoning occurs at connection time, before any user interaction and without exploitable code on the target: a malicious MCP server need only exist in the agent's context. The framework shows lateral spread through Slack, Jira, GitHub, Notion, and email, and reports that five of six frontier models tested exhibited full or partial propagation.

</details>

<details><summary><strong>Nemesis 2.2</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational) ![Lee Chagolla-Christensen](https://img.shields.io/badge/Lee%20Chagolla-Christensen-informational)

🔗 **Link:** [Nemesis 2.2](https://github.com/SpecterOps/Nemesis)  
📝 **Description:** Nemesis is an open-source centralised data processing platform that ingests, enriches, and supports collaborative human and AI analysis of files collected during offensive security assessments. Version 2.2 adds ingestion of full disk images and large forensic containers with automatic carving, and a complete DPAPI auto-decryption pipeline spanning classic DPAPI through Chromium's v3 app-bound encryption for browser cookies and saved logins. Optional LLM agents handle finding triage, credential extraction, and document summarisation, alongside file linking and per-host reporting.

</details>

<details><summary><strong>Praxis - Semantic Command & Control Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Tyler Holmwood](https://img.shields.io/badge/Tyler%20Holmwood-informational)

🔗 **Link:** [Praxis - Semantic Command & Control Framework](https://github.com/originsec/praxis)  
📝 **Description:** Praxis is an open-source adversarial command and control framework for discovering, controlling, and orchestrating AI computer-use agents such as Claude, Codex, and Cursor across endpoints. Because these agents can read files, execute commands, and interact directly with systems, Praxis serves as a research platform for exploring what an attacker with legitimate or illegitimate endpoint access can do through them, and for showing defenders what that activity looks like in practice.

</details>

<details><summary><strong>RedTeamSimmer: A Web Based Adversary Emulation Platform and Atomic Red Team Test Orchestration</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Abx](https://img.shields.io/badge/Abx-informational)

🔗 **Link:** [RedTeamSimmer: A Web Based Adversary Emulation Platform and Atomic Red Team Test Orchestration](https://github.com/BreachSimRange/RedTeamSimmer)  
📝 **Description:** RedTeamSimmer is an open-source web platform for orchestrating Atomic Red Team tests across enterprise Windows environments, replacing memorised PowerShell syntax and per-endpoint prerequisite management with a Flask server, lightweight Go agents, and a real-time dashboard. Operators browse the full ATT&CK catalogue, run tests with automatic prerequisite handling, and watch live colour-coded output. It ships adversary emulation plans modelled on APT28, APT41, FIN7, Lazarus Group, and Wizard Spider, plus Sigma, Splunk, and Elastic detection mappings.

</details>

<details><summary><strong>Sage: Giving an AI the Keys to Your C2 Framework</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Russel Van Tuyl](https://img.shields.io/badge/Russel%20Van%20Tuyl-informational)

🔗 **Link:** [Sage: Giving an AI the Keys to Your C2 Framework](https://github.com/MythicAgents/sage)  
📝 **Description:** Sage is an open-source AI-powered virtual agent for the Mythic C2 framework that uses a multi-agent system to operate Mythic and the agents running on compromised hosts. Rather than executing on a target, Sage runs in its own container on the Mythic server and acts as an AI operator: enumerating callbacks, tasking agents, interpreting results, building payloads, and chaining multi-step operations from natural language. Built on LangGraph with support for Anthropic, OpenAI, AWS Bedrock, Ollama, and OpenAI-compatible APIs.

</details>

<details><summary><strong>Splunk MCP LLM SIEMulator: Open Source AI Security Monitoring Through Model Context Protocol Integration</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational)

🔗 **Link:** [Splunk MCP LLM SIEMulator: Open Source AI Security Monitoring Through Model Context Protocol Integration](https://github.com/rsfl/splunk-mcp-llm-siemulator)  
📝 **Description:** The Splunk MCP LLM SIEMulator is an open-source framework that brings local LLM deployments into SIEM visibility using the Model Context Protocol. Integrating MCP servers with Splunk lets security teams apply established threat hunting methods to AI workloads, correlate AI events with wider security telemetry, and detect prompt injection, jailbreak attempts, shadow AI usage, and anomalous model behaviour. It ships pre-built Splunk detection rules and dashboards alongside simulations of prompt injection, API reconnaissance, resource exhaustion, and unauthorised model access.

</details>

<details><summary><strong>unrelabel: how to destroy an ML model</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Ozzy](https://img.shields.io/badge/Ozzy-informational)

🔗 **Link:** [unrelabel: how to destroy an ML model](https://github.com/oz9un/unrelabel)  
📝 **Description:** unrelabel is an interactive toolkit that demonstrates label-poisoning attacks against machine learning classifiers, showing how little effort it takes to compromise a pipeline through its training data. Strategies range from brute-force label corruption to stealthy attacks that leave labels clean yet still break the model, each trading damage against effort and detectability. A CLI and a three-step web interface report vulnerability scores, confusion matrices, and accuracy breakdowns for sklearn, CSV, numpy, and HuggingFace datasets.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>From Breakthrough to Completeness: arkdecompiler - The Decompiler for HarmonyOS NEXT</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Xiaoyu He](https://img.shields.io/badge/Xiaoyu%20He-informational) ![Qidan He](https://img.shields.io/badge/Qidan%20He-informational) ![Guangxi Li](https://img.shields.io/badge/Guangxi%20Li-informational)

🔗 **Link:** [From Breakthrough to Completeness: arkdecompiler - The Decompiler for HarmonyOS NEXT](https://github.com/jd-opensource/arkdecompiler)  
📝 **Description:** arkdecompiler reconstructs ArkTS source code from the Panda Bytecode used by Huawei's HarmonyOS NEXT, which runs a native stack independent of AOSP. This release moves the engine from structural proof of concept to semantic completeness, adding exhaustive instruction coverage for generators, async and arrow functions, destructuring, spread-based super calls, and iterators, plus path-sensitive analysis and SSA-to-source transformation. An automated pipeline validated the decompiler across 86,150 TypeScript and JavaScript samples.

</details>

<details><summary><strong>RPCExplorer</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![shmctl](https://img.shields.io/badge/shmctl-informational)

🔗 **Link:** Not Available  
📝 **Description:** RPCExplorer maps and probes the Windows RPC attack surface at scale, turning an interface UUID into something searchable and testable. It enumerates live endpoints through the RPC Endpoint Mapper, captures bindings such as ncalrpc, named pipes, and TCP, and scans on-disk DLLs for unregistered interfaces, loading everything into an interactive web UI with full-text search and filters for SYSTEM-hosted interfaces, missing security callbacks, and risky parameter types. Symbol enrichment, an optional decompiler pipeline, and direct method invocation close the loop from discovery to validation.

</details>

<details><summary><strong>SEmuRAI: Software Emulation and Reversing AI Agent</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Gun Rui Tew](https://img.shields.io/badge/Gun%20Rui%20Tew-informational)

🔗 **Link:** [SEmuRAI: Software Emulation and Reversing AI Agent](https://github.com/DevNerdGR/SEmuRAI-mcp)  
📝 **Description:** SEmuRAI is a dynamic analysis toolkit that gives LLM-driven reverse engineering agents sandboxed binary emulation, including breakpoints and memory and register read/write access. Agentic reverse engineering workflows typically rely on static analysis alone, which struggles with obfuscated or large binaries stripped of contextual information. Benchmarks across three test cases of increasing complexity compared static-only analysis against the combined setup and found that adding SEmuRAI improved agent performance, particularly on the harder tasks.

</details>

<details><summary><strong>SHAREM: Next-Generation Shellcode Analysis Tool</strong></summary>

![USA 2026](https://img.shields.io/badge/USA%202026-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Dr. Bramwell Brizendine](https://img.shields.io/badge/Dr.%20Bramwell%20Brizendine-informational)

🔗 **Link:** [SHAREM: Next-Generation Shellcode Analysis Tool](https://github.com/Bw3ll/sharem)  
📝 **Description:** SHAREM is an NSA-funded shellcode analysis framework that emulates shellcode to recover behaviour static analysis cannot reach. It identifies more than 45,538 unique WinAPI functions and 99% of Windows syscalls, and its custom disassembler labels the actual API being invoked along with its parameters where other disassemblers show only a generic indirect call. Emulation deobfuscates self-decoding shellcode without live execution, typically in 10 to 30 seconds, and can revisit prior execution contexts to expose code beyond the obvious path.

</details>

---