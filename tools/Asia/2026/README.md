# Asia 2026
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2026** event held in **Asia**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Contents
- [☁️ Cloud Security](#☁️-cloud-security)
- [⚙️ Miscellaneous / Lab Tools](#⚙️-miscellaneous-lab-tools)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🤖 AI, ML & Data Science](#🤖-ai,-ml-data-science)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Flutterscan: Mobile App Security SAST Framework for Flutter</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Rohit Narayanan M](https://img.shields.io/badge/Rohit%20Narayanan%20M-informational) ![Akhil Mahendra](https://img.shields.io/badge/Akhil%20Mahendra-informational)

🔗 **Link:** [Flutterscan: Mobile App Security SAST Framework for Flutter](https://github.com/RohitNarayananM/flutterscan)  
📝 **Description:** Flutterscan is a static application security testing framework purpose-built for the Flutter and Dart ecosystem, addressing gaps left by general-purpose mobile SAST tools. It maps detections to the OWASP Mobile Top 10 and MSTG guidelines to identify insecure coding patterns across Dart files, AndroidManifest.xml, and YAML configurations, and integrates into CI/CD pipelines such as GitHub Actions with output in JSON, SARIF, HTML, and YAML formats for pull-request review.

</details>

<details><summary><strong>BoardSentinel: An Automated Static Analysis Framework for BMC Firmware Vulnerability Detection</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Zhong Wang](https://img.shields.io/badge/Zhong%20Wang-informational) ![Lewei Qu](https://img.shields.io/badge/Lewei%20Qu-informational) ![Sheng Ma](https://img.shields.io/badge/Sheng%20Ma-informational)

🔗 **Link:** Not Available  
📝 **Description:** BoardSentinel is an automated static analysis framework that extracts, analyzes, and detects vulnerabilities in Baseboard Management Controller (BMC) firmware from major vendors including AMI MegaRAC, OpenBMC, Dell iDRAC, and H3C HDM. It combines a universal firmware extraction engine that handles embedded filesystems such as SquashFS, CramFS, JFFS2, and FIT images with hybrid vulnerability detection that pairs IDA Pro and Radare2 analysis with Semgrep pattern matching and custom Python detectors. An extensible YAML-based rule system allows rapid integration of newly disclosed CVEs, enabling researchers and security teams to assess BMC firmware security at scale without deep reverse engineering expertise.

</details>

<details><summary><strong>Zorya: Go Binary Vulnerability Detection with Concolic Execution</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Karolina GORNA](https://img.shields.io/badge/Karolina%20GORNA-informational) ![Keith Makan](https://img.shields.io/badge/Keith%20Makan-informational)

🔗 **Link:** [Zorya: Go Binary Vulnerability Detection with Concolic Execution](https://github.com/Ledger-Donjon/zorya)  
📝 **Description:** Zorya is a concolic execution framework written in Rust and engineered to detect runtime vulnerabilities in compiled Go binaries without source code access. It combines Ghidra's P-Code binary lifting with Z3 constraint solving and uses panic-gated exploration to focus symbolic reasoning on vulnerability-leading paths, applying multi-layer reachability filtering to reduce solver queries by two orders of magnitude. The tool surfaces state-dependent bugs and runtime panics in Go-based distributed systems, network services, and container orchestration platforms before they reach production.

</details>

<details><summary><strong>actsense: GitHub Actions Workflow Auditor</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Kumar Ashwin](https://img.shields.io/badge/Kumar%20Ashwin-informational)

🔗 **Link:** [actsense: GitHub Actions Workflow Auditor](https://github.com/0xCardinal/actsense)  
📝 **Description:** actsense is a local, vendor-agnostic framework for auditing GitHub Actions workflows and their dependencies. It statically maps all actions, including nested composite, JavaScript, and Docker actions, and runs over 30 security checks covering pinning, permissions, events, and secrets, while also assessing Docker images and external dependencies for unpinned or unpinnable references. Findings are presented through an interactive dependency graph that exposes the full transitive action graph and helps teams trace relationships, triage supply chain risks, and secure CI/CD pipelines without leaking data to third parties.

</details>

<details><summary><strong>DursGo: Web App Security Scanner with AI Analysis Vulnerability</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Mohammad Ali Syarief](https://img.shields.io/badge/Mohammad%20Ali%20Syarief-informational) ![Nur Fadhillah](https://img.shields.io/badge/Nur%20Fadhillah-informational)

🔗 **Link:** [DursGo: Web App Security Scanner with AI Analysis Vulnerability](https://github.com/roomkangali/dursgo)  
📝 **Description:** DursGo is a Go-powered web application security scanner that combines high-performance automated scanning with LLM-driven analysis for penetration testing and security audits. It performs technology fingerprinting, intelligent crawling and endpoint discovery (with optional headless browser support for SPAs), and concurrent execution of vulnerability modules such as XSS and SQL injection, including OAST verification for blind issues. Findings are deduplicated and enriched with AI-generated context to deliver actionable insights.

</details>

<details><summary><strong>SupplyShield: Protecting Your Software Supply Chain</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Rahul Sunder](https://img.shields.io/badge/Rahul%20Sunder-informational) ![Yadhu Krishna](https://img.shields.io/badge/Yadhu%20Krishna-informational) ![Hritik Vijay](https://img.shields.io/badge/Hritik%20Vijay-informational) ![Sourav Kumar](https://img.shields.io/badge/Sourav%20Kumar-informational) ![Akash Methani](https://img.shields.io/badge/Akash%20Methani-informational)

🔗 **Link:** [SupplyShield: Protecting Your Software Supply Chain](https://github.com/supplyshield/supplyshield)  
📝 **Description:** SupplyShield is an open-source application security orchestration framework that integrates SBOM generation and Software Composition Analysis (SCA) into the SDLC at scale, supporting environments with thousands of daily microservice builds. It identifies minimal top-level package upgrades to resolve transitive vulnerabilities, prioritizes findings using EPSS scoring, raises actionable items as GitHub issues, and supports build comparison to track newly introduced packages and vulnerabilities. The framework reduces mean time to detect zero-day issues like Log4j to minutes through a centralized dashboard with key security metrics.

</details>

<details><summary><strong>Dep-Hallucinator: Detecting Dependency Confusion from AI/LLM-Hallucinated Packages</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Serhan Bahar](https://img.shields.io/badge/Serhan%20Bahar-informational)

🔗 **Link:** [Dep-Hallucinator: Detecting Dependency Confusion from AI/LLM-Hallucinated Packages](https://github.com/serhanwbahar/dep-hallucinator)  
📝 **Description:** Dep-Hallucinator is an open-source security scanner that identifies AI/LLM-hallucinated package dependencies before they enable slopsquatting attacks. It queries official package registries through native APIs and applies machine learning to distinguish AI-generated naming patterns from legitimate packages, addressing the finding that 19.7% of AI-suggested dependencies are non-existent and that 58% of these hallucinated names are repeated consistently. The tool helps developers and security teams detect dependency confusion risks introduced by AI coding assistants.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Damn Vulnerable Model Context Protocol (DVMCP) Platform</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Ankit Garg](https://img.shields.io/badge/Ankit%20Garg-informational) ![Harish Santhanalakshmi Ganesan](https://img.shields.io/badge/Harish%20Santhanalakshmi%20Ganesan-informational)

🔗 **Link:** [Damn Vulnerable Model Context Protocol (DVMCP) Platform](https://github.com/harishsg993010/damn-vulnerable-MCP-server)  
📝 **Description:** Damn Vulnerable MCP (DVMCP) is a deliberately insecure implementation of the Model Context Protocol built as an educational and research platform for security in LLM-integrated systems. It simulates real-world MCP risks such as prompt injection, tool poisoning, excessive permissions, rug-pull attacks, token theft, and multi-vector exploits across ten progressive Docker-deployable challenges. Recent additions include identity-based attacks, MCP-specific supply chain scenarios, and a web dashboard for interactive challenge navigation, real-time monitoring, and analytics.

</details>

<details><summary><strong>AI Wargame</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational) ![Harley Wilson](https://img.shields.io/badge/Harley%20Wilson-informational)

🔗 **Link:** [AI Wargame](https://play.secdim.com/)  
📝 **Description:** AI Wargame is an interactive attack-and-defense platform where players secure their own AI chatbot's secrets while attempting to extract secrets from opponents' chatbots. It provides a king-of-the-hill style competition for learning prompt injection, AI security hardening, and chatbot defense techniques at all skill levels. Each player has access to their chatbot's source code repository to run, test, debug, and push changes during the game.

</details>

<details><summary><strong>PwnSat: A Vulnerable-by-Design Satellite Hardware and Platform for AeroSpace Hacking and Research</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Romel Marin cordoba](https://img.shields.io/badge/Romel%20Marin%20cordoba-informational) ![Kevin Jahaziel Leon Morales](https://img.shields.io/badge/Kevin%20Jahaziel%20Leon%20Morales-informational)

🔗 **Link:** [PwnSat: A Vulnerable-by-Design Satellite Hardware and Platform for AeroSpace Hacking and Research](https://github.com/Pwnsat/FlatSat)  
📝 **Description:** PWNSAT is an open-source vulnerable-by-design aerospace cybersecurity platform that combines a physical CubeSat, a ground station, a Mission Operations Center, and RF communication links. It replicates a real space mission using aerospace protocols such as CCSDS and AX.25 over LoRa and FSK, with intentional vulnerabilities introduced at the radio frequency, firmware, and MOC service layers under the SPARTA framework. The platform supports CTF-style exercises, technical audits, and penetration testing of satellite systems for researchers and educators.

</details>

<details><summary><strong>ThreatShield – The Intelligent Way of Threat Modelling</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Satyam Nagpal](https://img.shields.io/badge/Satyam%20Nagpal-informational) ![Sayooj Nagpal](https://img.shields.io/badge/Sayooj%20Nagpal-informational) ![Ashwin Shenoi](https://img.shields.io/badge/Ashwin%20Shenoi-informational) ![Nandu S. Pillai](https://img.shields.io/badge/Nandu%20S.%20Pillai-informational)

🔗 **Link:** Not Available  
📝 **Description:** ThreatShield is an AI-powered threat modeling and security analysis tool that automates STRIDE-based threat model generation using OpenAI's enterprise API. It ingests heterogeneous inputs such as PRDs, architecture diagrams, Confluence pages, Slack threads, and meeting transcripts, then produces structured threat models, attack trees, DREAD scoring, and prioritized mitigations. The tool helps security engineering teams scale threat modeling across product development without relying on manual whiteboard sessions.

</details>

<details><summary><strong>Casino Heist v2</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Richard Tan](https://img.shields.io/badge/Richard%20Tan-informational) ![Anthony Sai Richardo](https://img.shields.io/badge/Anthony%20Sai%20Richardo-informational)

🔗 **Link:** [Casino Heist v2](https://github.com/Kiinzu/Casino-Heist)  
📝 **Description:** Casino Heist v2 is a smart contract security playground centered on Solidity contracts deployed on the Ethereum blockchain. It pairs each challenge with theoretical foundations, exploitation walkthroughs, and mitigation guidance, spanning fundamentals such as reentrancy and integer overflow through advanced attack vectors inspired by real-world incidents. The platform serves CTF players, security researchers, educators, and developers exploring blockchain security.

</details>

<details><summary><strong>Circuit Breaker CTF</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Manzel Seet](https://img.shields.io/badge/Manzel%20Seet-informational) ![Kenneth Tong](https://img.shields.io/badge/Kenneth%20Tong-informational)

🔗 **Link:** Not Available  
📝 **Description:** Circuit Breaker CTF is a testbench for power industry security research that simulates devices and protocols across the generation, transmission, distribution, and consumer chain. Building on prior iterations focused on individual device exploitation, it introduces system-level interactions and highlights the role and adaptability of circuit breakers across diverse operational environments. Participants engage with realistic ICS scenarios to practice exploitation and defense techniques specific to electrical power infrastructure.

</details>

<details><summary><strong>Sysrupt: Portable OT/ICS and Hardware Security Training Platform (CompatriOT v2)</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Season Cherian](https://img.shields.io/badge/Season%20Cherian-informational) ![Vivek NJ](https://img.shields.io/badge/Vivek%20NJ-informational)

🔗 **Link:** [Sysrupt: Portable OT/ICS and Hardware Security Training Platform (CompatriOT v2)](https://github.com/traboda/CompatrIoT)  
📝 **Description:** Sysrupt is a portable, self-contained OT/ICS and hardware security training platform that evolves the CompatrIoT project from Black Hat Asia 2025 into the operational technology domain. Built around a Radxa A5E SBC, dual ESP32-C6 microcontrollers, a PLC simulator, and an onboard managed Ethernet switch, it lets participants observe and manipulate live OT protocol traffic while watching attacks affect physical outputs. The platform includes hardware-based signing of proof-of-exploit tokens for verifiable scoring in CTFs and research labs.

</details>

<details><summary><strong>AI Security Playground (Hands-On-Activity)</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Abhishek S](https://img.shields.io/badge/Abhishek%20S-informational) ![Keshav Malik](https://img.shields.io/badge/Keshav%20Malik-informational) ![Surya Kanagasabapathi](https://img.shields.io/badge/Surya%20Kanagasabapathi-informational)

🔗 **Link:** Not Available  
📝 **Description:** AI Security Playground is an open-source, gamified training platform that teaches security risks unique to AI and GenAI environments, including LLMs, AI agents, and MCP servers. It guides participants through real-world attacks ranging from beginner to advanced, covering exploits against AI agents, MCP server misconfigurations, and prompt injection techniques. An AI-powered judge provides immediate feedback as users solve each challenge, helping developers and security practitioners build offensive and defensive AI security skills.

</details>

---
## ☁️ Cloud Security
<details><summary><strong>Prowler Open Cloud Security - release of v6.0</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Toni de la Fuente](https://img.shields.io/badge/Toni%20de%20la%20Fuente-informational)

🔗 **Link:** [Prowler Open Cloud Security - release of v6.0](https://github.com/prowler-cloud/prowler)  
📝 **Description:** Prowler is an open-source cloud security platform that performs continuous monitoring, security assessments, audits, incident response support, hardening, and forensics readiness across AWS, Azure, GCP, Kubernetes, and M365. It runs hundreds of checks mapped to compliance frameworks including CIS, NIST 800, NIST CSF, CISA, FedRAMP, PCI-DSS, GDPR, HIPAA, FFIEC, SOC2, and ENS. The v6.0 release expands coverage and integrations for multi-cloud security teams managing posture at scale.

</details>

<details><summary><strong>SkyEye: When Your Vision Reaches Beyond IAM Boundary Scope in the Cloud</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Minh Hoang Nguyen](https://img.shields.io/badge/Minh%20Hoang%20Nguyen-informational) ![Anh Minh Ho](https://img.shields.io/badge/Anh%20Minh%20Ho-informational) ![Bao Son To](https://img.shields.io/badge/Bao%20Son%20To-informational)

🔗 **Link:** [SkyEye: When Your Vision Reaches Beyond IAM Boundary Scope in the Cloud](https://github.com/0x7a6b4c/SkyEye)  
📝 **Description:** SkyEye is a cooperative multi-principal IAM enumeration framework for AWS that overcomes the blind spots of principal-centric reconnaissance tools. It introduces the Cross-Principal IAM Enumeration Model (CPIEM) and Transitive Cross-Role Enumeration Model (TCREM) to synchronize sessions across multiple user and role credentials, dynamically chaining permissions to surface privilege escalation paths invisible to siloed enumeration. SkyEye maps AWS actions to MITRE ATT&CK Cloud TTPs with severity ratings to support red team adversary simulation and cloud detection engineering.

</details>

<details><summary><strong>Oblivion Token : M365 Conditional Access Policy Bypass OST (Offensive Tooling)</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Nuttakorn Tungpoonsup](https://img.shields.io/badge/Nuttakorn%20Tungpoonsup-informational) ![Waris Damkham](https://img.shields.io/badge/Waris%20Damkham-informational)

🔗 **Link:** [Oblivion Token : M365 Conditional Access Policy Bypass OST (Offensive Tooling)](https://github.com/Waariss/OblivionToken)  
📝 **Description:** Oblivion Token is an offensive-research utility for testing Microsoft 365 Conditional Access Policy (CAP) bypass scenarios in a repeatable, scriptable way. It emits valid OIDC ID tokens and OAuth2 access tokens for Microsoft Graph API post-exploitation automation, exercising token-centric workflows against Microsoft first-party applications without browser prompts. Red-teamers and security researchers use it to expose where device, network, and app-context assumptions in CAP enforcement break down.

</details>

<details><summary><strong>KubeShadow (Advanced Offensive Kubernetes Red-Team Framework)</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Aashita Pandey](https://img.shields.io/badge/Aashita%20Pandey-informational) ![Binayak Choudhury](https://img.shields.io/badge/Binayak%20Choudhury-informational)

🔗 **Link:** [KubeShadow (Advanced Offensive Kubernetes Red-Team Framework)](https://github.com/ashifly/KubeShadow)  
📝 **Description:** KubeShadow is a Go-based modular red-team framework for end-to-end adversary emulation against Kubernetes environments including EKS, GKE, AKS, and self-hosted clusters. It combines a recon engine, graph-based chaining, and a plugin architecture covering control-plane and workload exploitation (etcd injection, kubelet hijack, sidecar/init-container injection, RBAC escalation, ephemeral container attacks), multi-cloud identity pivoting, and exfiltration adapters. Built-in lab manifests, an interactive dashboard, and prioritized remediation guidance support reproducible PoCs and purple-team exercises.

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>NOVA Ecosystem: Your AI Security Arsenal</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Thomas Roccia](https://img.shields.io/badge/Thomas%20Roccia-informational)

🔗 **Link:** [NOVA Ecosystem: Your AI Security Arsenal](https://github.com/fr0gger/nova-framework)  
📝 **Description:** NOVA is an open-source prompt pattern matching engine that detects and classifies adversarial prompts targeting LLM applications, introducing the concept of Indicators of Prompt Compromise (IoPC). It combines keyword rules, semantic similarity, and LLM-based evaluation in a YARA-inspired syntax, integrating into LLM pipelines, MCP servers, and red-team frameworks. The ecosystem extends to PromptIntel and Proximity modules for hunting jailbreaks, data exfiltration, and prompt injection attempts before execution.

</details>

<details><summary><strong>Agent Miner: A General AI Agent Security Auditing Agent Based on Multi-Agent Collaboration</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Lewei Qu](https://img.shields.io/badge/Lewei%20Qu-informational) ![Zeyu Luo](https://img.shields.io/badge/Zeyu%20Luo-informational) ![Zezhi Lin](https://img.shields.io/badge/Zezhi%20Lin-informational) ![Yue Yang](https://img.shields.io/badge/Yue%20Yang-informational) ![Sushuang Ma](https://img.shields.io/badge/Sushuang%20Ma-informational)

🔗 **Link:** Not Available  
📝 **Description:** Agent Miner is a security auditing tool for general AI agents such as computer-use, browser-use, and mobile-use agents, built on a multi-agent collaborative architecture that decomposes complex audits into subtasks orchestrated through a directed acyclic graph workflow. It performs attack-surface-driven static analysis to identify vulnerability points and generate proof-of-concept exploits, then automatically deploys the target agent in a simulated environment to validate findings. The framework has uncovered more than 15 vulnerabilities across over 10 mainstream open-source AI agents, resulting in 7 assigned CVEs.

</details>

<details><summary><strong>Prompt Hardener: Automated Evaluation and Hardening of LLM System Prompts</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Yoshiki Kitamura](https://img.shields.io/badge/Yoshiki%20Kitamura-informational) ![Junki Yuasa](https://img.shields.io/badge/Junki%20Yuasa-informational)

🔗 **Link:** [Prompt Hardener: Automated Evaluation and Hardening of LLM System Prompts](https://github.com/cybozu/prompt-hardener)  
📝 **Description:** Prompt Hardener is an open-source toolkit that evaluates and strengthens system prompts used in LLM applications against prompt injection. It uses an LLM to review prompts against defensive techniques such as spotlighting, instruction defense, role consistency, random sequence enclosure, and secrets exclusion, then generates structured feedback and rewrite suggestions. An adversarial testing module executes payloads inspired by the OWASP Top 10 for LLM Applications to verify mitigation effectiveness across an evaluate-improve-verify workflow.

</details>

<details><summary><strong>Continuous CyberBattleSim: A More Realistic Simulation for AI-driven Attack Path Discovery</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Franco Terranova](https://img.shields.io/badge/Franco%20Terranova-informational) ![Abdelkader Lahmadi](https://img.shields.io/badge/Abdelkader%20Lahmadi-informational)

🔗 **Link:** [Continuous CyberBattleSim: A More Realistic Simulation for AI-driven Attack Path Discovery](https://github.com/terranovafr/C-CyberBattleSim)  
📝 **Description:** Continuous CyberBattleSim (C-CyberBattleSim) is an extension of Microsoft's CyberBattleSim that trains and evaluates reinforcement learning agents on cyber attack path prediction modeled as a vulnerability chaining problem. It enriches scenario generation with Cyber Threat Intelligence drawn from empirical Shodan distributions, automates vulnerability outcome inference from metadata, and integrates a graph neural network and language model embedding to represent nodes and vulnerabilities in continuous vector spaces. The framework supports more scalable and generalizable RL training for synthetic environments resembling real-world infrastructures.

</details>

<details><summary><strong>CodeRetrX: One-Click to Start Your Journey of Agentic Bug Hunting</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Guancheng Li](https://img.shields.io/badge/Guancheng%20Li-informational) ![Yuxuan Sun](https://img.shields.io/badge/Yuxuan%20Sun-informational) ![Tianrui Chen](https://img.shields.io/badge/Tianrui%20Chen-informational)

🔗 **Link:** [CodeRetrX: One-Click to Start Your Journey of Agentic Bug Hunting](https://github.com/XuanwuAI/CodeRetrX)  
📝 **Description:** CodeRetrX is a code analysis and semantic retrieval library designed to lower the barrier for agent-driven vulnerability discovery. It provides a suite of agentic analysis tools, including cross-referencing, semantic search, code structure inspection, and an embedded CodeQL engine, all exposed via the MCP protocol, alongside a retrieval engine that achieves around 90% recall on complex semantic patterns at roughly 25% of the token cost of full LLM traversal. Researchers can launch or extend agentic bug-hunting setups by connecting to the MCP server or calling the CodeRetrX API.

</details>

<details><summary><strong>DataTrap - Adaptive LLM-Powered Honeypot Framework</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Ori Nakar](https://img.shields.io/badge/Ori%20Nakar-informational)

🔗 **Link:** [DataTrap - Adaptive LLM-Powered Honeypot Framework](https://github.com/ThalesGroup/dd-honeypot)  
📝 **Description:** DataTrap is an open-source, extensible honeypot framework that simulates realistic application behavior across HTTP, HTTPS, SSH, and database protocols, covering web applications, IoT devices, and databases. It combines recorded application payloads with contextual metadata and LLM reasoning to generate dynamic, context-aware responses, and includes a honeypot dispatcher that routes traffic to the most appropriate honeypot type along with an LLM-based reporting module that converts captured data into actionable threat intelligence. DataTrap is distributed as a Docker image for rapid deployment.

</details>

<details><summary><strong>LLMInspector - Advanced LLM Fingerprinting & Security Testing Tool</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Alfonso Munoz](https://img.shields.io/badge/Alfonso%20Munoz-informational) ![Jacobo Blancas](https://img.shields.io/badge/Jacobo%20Blancas-informational)

🔗 **Link:** [LLMInspector - Advanced LLM Fingerprinting & Security Testing Tool](https://github.com/michelin/LLMInspector)  
📝 **Description:** LLMInspector is a penetration testing suite for auditing Large Language Models deployed in production environments. It fingerprints models through behavioral patterns, response characteristics, and semantic signatures, and runs prompt injection testing against both commercial APIs and open-source deployments. It integrates with Ollama to analyze over 200 local models for adversarial behavior and alignment issues.

</details>

<details><summary><strong>Bastet - AI Smart Contract Vulnerability Detector</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Alice Hsu](https://img.shields.io/badge/Alice%20Hsu-informational) ![Daky Wang](https://img.shields.io/badge/Daky%20Wang-informational) ![Chengyu Liou](https://img.shields.io/badge/Chengyu%20Liou-informational)

🔗 **Link:** [Bastet - AI Smart Contract Vulnerability Detector](https://github.com/OneSavieLabs/Bastet)  
📝 **Description:** Bastet is a security infrastructure that pairs a curated dataset of common DeFi smart contract vulnerabilities with an AI-driven automated detection process, focusing on issues frequently rated medium-to-high risk in audit competitions that are difficult to surface with traditional static analysis. The dataset draws from real-world on-chain incidents and audit competition findings, while tailored detection workflows improve AI accuracy in identifying complex vulnerability patterns. Bastet currently ships over 10 detection workflows and 55+ rules, and has flagged more than 25 on-chain contracts containing medium- to high-risk vulnerabilities within its rule coverage.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Hashtopolis</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Marvin Schwarz](https://img.shields.io/badge/Marvin%20Schwarz-informational) ![Jesse van Zutphen](https://img.shields.io/badge/Jesse%20van%20Zutphen-informational)

🔗 **Link:** [Hashtopolis](https://github.com/hashtopolis/server)  
📝 **Description:** Hashtopolis is an open-source client-server platform for managing and monitoring distributed password-recovery tasks using Hashcat and compatible engines. It provides a centralized web interface and REST API to coordinate large-scale cracking operations across heterogeneous GPU and CPU agents, with keyspace partitioning, job scheduling, and real-time telemetry on task progress, performance, and hardware. The platform is licensed under GPL 3.0 and used for legitimate security testing, auditing, and forensic research.

</details>

<details><summary><strong>vet: Open Source Software Supply Chain Security Guardrail in the age of AI SDLC</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Abhisek Datta](https://img.shields.io/badge/Abhisek%20Datta-informational)

🔗 **Link:** [vet: Open Source Software Supply Chain Security Guardrail in the age of AI SDLC](https://github.com/safedep/vet)  
📝 **Description:** vet is an open-source software supply chain security tool tailored for AI-assisted SDLC workflows. Unlike traditional SCA tools, it proactively detects malicious packages before they appear in OSV, integrates as an MCP server with AI IDEs and coding agents like Cursor and Claude Code, and supports conversational analysis over scan results. This positions vet between package-level malicious code detection and developer-first defense in the era of AI coding assistants.

</details>

<details><summary><strong>PacketDuck: AI-Assisted Incident Response</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Daksh Thapar](https://img.shields.io/badge/Daksh%20Thapar-informational) ![Rian Tan](https://img.shields.io/badge/Rian%20Tan-informational) ![Ravin Nagpal](https://img.shields.io/badge/Ravin%20Nagpal-informational)

🔗 **Link:** Not Available  
📝 **Description:** PacketDuck is an AI-assisted triage acceleration tool that helps L1 SOC analysts rapidly analyze PCAP data during incident response. It surfaces high-risk network behaviors, prioritizes threats, and generates forensic insights to reduce mean time to triage. The tool fits into incident response workflows where analysts must quickly verdict suspicious captures and escalate genuine intrusions.

</details>

<details><summary><strong>Broń Vault: Open-Source Web-App for Stealer Log Parsing and Exploration</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![YoKo Kho](https://img.shields.io/badge/YoKo%20Kho-informational) ![Tomi Ashari](https://img.shields.io/badge/Tomi%20Ashari-informational) ![Lalu Raynaldi Pratama Putra](https://img.shields.io/badge/Lalu%20Raynaldi%20Pratama%20Putra-informational)

🔗 **Link:** [Broń Vault: Open-Source Web-App for Stealer Log Parsing and Exploration](https://github.com/itsec-research/bron-vault)  
📝 **Description:** Broń Vault is an open-source web application that automates parsing and exploration of stealer log data, transforming raw archives into structured, queryable intelligence. It replaces manual scripting and inconsistent parsing logic with a unified pipeline that supports 20+ host-info parser variants, installed software parsing, and per-device detail views via a drag-and-drop interface. The tool helps security teams triage credential theft datasets at scale and surface actionable intelligence from information stealer campaigns.

</details>

<details><summary><strong>Azazel-Pi: Offline Edge-AI SOC/NOC Gateway with Mock-LLM Scoring and Ollama Fallback</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Makoto SUGITA](https://img.shields.io/badge/Makoto%20SUGITA-informational)

🔗 **Link:** [Azazel-Pi: Offline Edge-AI SOC/NOC Gateway with Mock-LLM Scoring and Ollama Fallback](https://github.com/01rabbit/Azazel-Pi)  
📝 **Description:** Azazel-Pi is a portable Raspberry Pi-based SOC/NOC gateway for small networks operating on untrusted links, combining Suricata signals with an on-device Mock-LLM Scorer (a deterministic, rule-assisted micro-model) for real-time threat scoring and a Dockerized Ollama runtime hosting Qwen2.5-1.5B-Instruct as a fallback for low-confidence cases. The scorer outputs a 0-100 risk score that drives a policy planner mapping score bands to tc-based traffic shaping, nftables/iptables micro-policies, and selective NAT redirection to OpenCanary decoys. The pipeline runs fully offline and automatically, with an e-paper panel exposing posture and mode without shell access, while the same scoring logic powers internal QoS to prioritize essential sessions.

</details>

<details><summary><strong>FLARE-VM: Continuously Sharpening the Analyst's Edge</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joshua Stroschein](https://img.shields.io/badge/Joshua%20Stroschein-informational) ![Jae Young Kim](https://img.shields.io/badge/Jae%20Young%20Kim-informational)

🔗 **Link:** [FLARE-VM: Continuously Sharpening the Analyst's Edge](https://github.com/mandiant/flare-vm)  
📝 **Description:** FLARE-VM is an open-source collection of installation scripts from Mandiant's FLARE team that automates the build of a Windows-based reverse engineering and malware analysis virtual machine. It provides a revamped GUI, shared package repositories for tool selection, and end-to-end automation including a VirtualBox build script that produces ready-to-export analysis VMs. The framework reduces setup time for malware analysts, reverse engineers, and offensive security practitioners maintaining customized analysis environments.

</details>

<details><summary><strong>StyX A Dual Mode IoT Forensic Tool</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dr Sapna V M](https://img.shields.io/badge/Dr%20Sapna%20V%20M-informational) ![Sherwin Allen](https://img.shields.io/badge/Sherwin%20Allen-informational) ![Meeran Ahmed](https://img.shields.io/badge/Meeran%20Ahmed-informational) ![Sathvik S](https://img.shields.io/badge/Sathvik%20S-informational) ![Shambo Sarkar](https://img.shields.io/badge/Shambo%20Sarkar-informational) ![Prasad Honnavalli](https://img.shields.io/badge/Prasad%20Honnavalli-informational)

🔗 **Link:** [StyX A Dual Mode IoT Forensic Tool](https://github.com/SherwinAllen/styx)  
📝 **Description:** StyX is a dual-mode IoT forensic framework that unifies evidence acquisition for Android-based smartwatches and smart assistant cloud ecosystems into a single workflow. For smartwatches, it uses ADB to extract Wi-Fi, Bluetooth, IP, and filesystem artifacts with SHA-256 integrity hashing and a web-based viewer. For smart assistants, it automates authenticated login (including OTP and push 2FA) to acquire and report on the last seven days of voice transcripts and audio commands, enabling scalable forensic analysis of smart home devices.

</details>

<details><summary><strong>HoneyOps (A fast, lightweight honeypot cloud-based builder written in Go)</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Melvin Lee](https://img.shields.io/badge/Melvin%20Lee-informational) ![Nicholas Lim](https://img.shields.io/badge/Nicholas%20Lim-informational)

🔗 **Link:** [HoneyOps (A fast, lightweight honeypot cloud-based builder written in Go)](https://github.com/PastelOps/HoneyOps)  
📝 **Description:** HoneyOps is a cloud-based honeypot deployment tool written in Go that provisions and manages decoy environments through an intuitive interface accessible to a range of skill levels. It complements a companion YARA rule collection to support proactive threat detection, monitoring, and analysis of attacker activity in cloud infrastructure for security researchers and threat analysts.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Canary WAF</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Amelia Chua](https://img.shields.io/badge/Amelia%20Chua-informational)

🔗 **Link:** [Canary WAF](https://github.com/umiyuikaiteitan/SCC_2025_Group_2)  
📝 **Description:** Canary WAF is a deceptive defense system that combines a Web Application Firewall with honeypot capabilities for web application security. It redirects detected web attack attempts to a fake database populated with synthetic data, drawing attackers away from production systems while collecting telemetry on their techniques. The platform provides defenders with real-time attack visibility and intelligence to inform incident response and threat modeling.

</details>

<details><summary><strong>BugHound MCP</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Krishna Naidu](https://img.shields.io/badge/Krishna%20Naidu-informational) ![eric tee](https://img.shields.io/badge/eric%20tee-informational) ![Lwin Min Oo](https://img.shields.io/badge/Lwin%20Min%20Oo-informational) ![Kai-Wei Hoon](https://img.shields.io/badge/Kai-Wei%20Hoon-informational) ![Valen Sai](https://img.shields.io/badge/Valen%20Sai-informational)

🔗 **Link:** Not Available  
📝 **Description:** BugHound MCP is a Model Context Protocol-based security automation framework that streamlines bug bounty hunting through natural language commands. It orchestrates specialized security tools across reconnaissance, scanning, and analysis domains, translating simple prompts into coordinated security workflows so researchers can run comprehensive assessments through conversational interactions instead of complex command chains.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>SquarePhish 2.0 - QR Code OAuth 2.0 Device Code Flow Phishing for Primary Refresh Token</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nevada Romsdahl](https://img.shields.io/badge/Nevada%20Romsdahl-informational) ![Kam Talebzadeh](https://img.shields.io/badge/Kam%20Talebzadeh-informational)

🔗 **Link:** [SquarePhish 2.0 - QR Code OAuth 2.0 Device Code Flow Phishing for Primary Refresh Token](https://github.com/nromsdahl/squarephish2)  
📝 **Description:** SquarePhish 2.0 is an advanced phishing toolkit that combines QR codes with the OAuth 2.0 device code authentication flow to capture Microsoft Entra ID Primary Refresh Tokens. The tool leverages the Microsoft Authentication Broker client ID to convert refresh tokens into PRTs, granting broad single sign-on access to Microsoft cloud resources via Family of Client IDs (FOCI) tokens. It enables red teams and defenders to test detection and prevention capabilities against modern device code phishing attacks.

</details>

<details><summary><strong>SAMLSmith</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Eric Woodruff](https://img.shields.io/badge/Eric%20Woodruff-informational)

🔗 **Link:** [SAMLSmith](https://github.com/Semperis/SAMLSmith)  
📝 **Description:** SAMLSmith is a C# offensive tool for forging SAML responses against enterprise identity providers, evolving earlier proof-of-concept tooling for Entra ID response forging into a full red-team utility. It supports multiple identity provider response forging, an AD FS-specific mode, SAML request processing with InResponseTo, WS-Federation responses, and PFX certificate extraction from AD FS encrypted material and DKM keys. Operators use it to execute Golden SAML and Silver SAML attacks against SaaS applications when signing key material can be obtained.

</details>

<details><summary><strong>EntraGoat - A Deliberately Vulnerable Entra ID Environment</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jonathan Elkabas](https://img.shields.io/badge/Jonathan%20Elkabas-informational) ![Eric Woodruff](https://img.shields.io/badge/Eric%20Woodruff-informational)

🔗 **Link:** [EntraGoat - A Deliberately Vulnerable Entra ID Environment](https://github.com/Semperis/EntraGoat)  
📝 **Description:** EntraGoat is a deliberately vulnerable Microsoft Entra ID (formerly Azure Active Directory) environment that simulates real-world misconfigurations and attack paths in a hands-on, CTF-style lab. It deploys multiple privilege escalation scenarios directly into an existing tenant, focusing on black-box methodologies across IAM, application, and service principal abuses. The platform is intended for security researchers, red teamers, and identity defenders building practical experience with Entra ID attack chains.

</details>

<details><summary><strong>Golden dMSA: One Key to Rule Them All</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Adi Malyanker](https://img.shields.io/badge/Adi%20Malyanker-informational)

🔗 **Link:** [Golden dMSA: One Key to Rule Them All](https://github.com/Semperis/GoldenDMSA)  
📝 **Description:** Golden dMSA is a post-exploitation tool that exploits a design flaw in delegated Managed Service Accounts (dMSAs) introduced in Windows Server 2025, enabling forest-wide compromise of managed service account credentials. After temporary control of a single domain and access to KDS root key material, it enumerates protected dMSA and gMSA accounts from non-privileged contexts and algorithmically reconstructs their passwords offline, bypassing the strengthened controls these accounts were designed to enforce.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Aegis: LLM SAST Framework for Blacklight Code Hunts</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Can Oztas](https://img.shields.io/badge/Can%20Oztas-informational)

🔗 **Link:** [Aegis: LLM SAST Framework for Blacklight Code Hunts](https://github.com/canoztas/aegis)  
📝 **Description:** Aegis is an open-source SAST framework that leverages LLMs to analyze source code for security vulnerabilities and produce detailed reports. Its flexible architecture supports a range of LLM providers as well as traditional machine learning models, allowing teams to plug in different backends for vulnerability detection across diverse codebases.

</details>

<details><summary><strong>SBoM Play</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Anant Shrivastava](https://img.shields.io/badge/Anant%20Shrivastava-informational)

🔗 **Link:** [SBoM Play](https://github.com/cyfinoid/sbomplay)  
📝 **Description:** SBoM Play is a browser-based SBOM exploration and intelligence extraction platform that runs entirely client-side without backend infrastructure. It imports SBOMs or extracts them directly from GitHub repositories, then enriches dependency data using OSV, deps.dev, and ecosyste.ms to provide a unified view across repositories and organizations. The tool surfaces tech debt patterns, version drift, license posture, SBOM quality gaps, end-of-life packages, dependency confusion indicators, and maintainer risk signals beyond traditional vulnerability tracking.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>From PoC to Breakthrough: arkdecompiler - The Decompiler for HarmonyOS NEXT</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Xiaoyu He](https://img.shields.io/badge/Xiaoyu%20He-informational) ![Qidan He](https://img.shields.io/badge/Qidan%20He-informational)

🔗 **Link:** [From PoC to Breakthrough: arkdecompiler - The Decompiler for HarmonyOS NEXT](https://github.com/jd-opensource/arkdecompiler)  
📝 **Description:** arkdecompiler is a decompiler purpose-built for HarmonyOS NEXT, Huawei's Android-incompatible operating system based on the HongMeng kernel and ArkCompiler toolchain. It parses Panda Binary Files and Panda Bytecode into Panda IR, then reconstructs the native ArkTS AST and translates it back to source code. The release expands beyond the Black Hat USA 2025 proof-of-concept to support arrays, objects, functions, branches, loops, exceptions, closures, modules, and incremental compilation for security analysis of native HarmonyOS applications.

</details>

<details><summary><strong>Mothra: Timeless Debugging of EVM Transactions with Ghidra</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Yuejie Shi](https://img.shields.io/badge/Yuejie%20Shi-informational) ![Aohui Wang](https://img.shields.io/badge/Aohui%20Wang-informational)

🔗 **Link:** [Mothra: Timeless Debugging of EVM Transactions with Ghidra](https://github.com/ambergroup-labs/Mothra)  
📝 **Description:** Mothra is a Ghidra extension for reverse engineering EVM bytecode that adds timeless debugging of Ethereum Virtual Machine transactions. It integrates with Ghidra's Debugger tool to let researchers replay an EVM transaction and step forward and backward at the opcode level, inspecting state at any point in execution. The tool supports smart contract auditing, exploit analysis, and post-incident investigation of on-chain activity.

</details>

<details><summary><strong>QuantumStrand (qs): A Structural Approach to String Analysis for Rapid Indicator Filtering</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Joshua Stroschein](https://img.shields.io/badge/Joshua%20Stroschein-informational) ![Jae Young Kim](https://img.shields.io/badge/Jae%20Young%20Kim-informational)

🔗 **Link:** [QuantumStrand (qs): A Structural Approach to String Analysis for Rapid Indicator Filtering](https://github.com/mandiant/flare-floss)  
📝 **Description:** QuantumStrand (qs) is an experimental static string analysis tool from Mandiant's FLARE team that transforms flat strings output into a structural map of a binary. It parses PE files into a tree of sections, headers, resources, overlays, and embedded files, then enriches each extracted string with contextual tags driven by expert heuristics and global prevalence databases. Malware analysts use it to filter noise during triage and rapidly focus on indicators that matter, with full layout and tag data exported as JSON.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>NVWA: A Novel Method for Automated Vulnerability Discovery in Embedded Firmware</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jiaxu Zhao](https://img.shields.io/badge/Jiaxu%20Zhao-informational) ![Yanyan Zou](https://img.shields.io/badge/Yanyan%20Zou-informational) ![Yuekang Li](https://img.shields.io/badge/Yuekang%20Li-informational) ![Wei Huo](https://img.shields.io/badge/Wei%20Huo-informational)

🔗 **Link:** [NVWA: A Novel Method for Automated Vulnerability Discovery in Embedded Firmware](https://doi.org/10.5281/zenodo.15605329)  
📝 **Description:** NÜWA is a static analysis tool for embedded firmware that detects vulnerabilities by identifying constraint semantic inconsistencies in input-validation code. It performs inter-procedural analysis using function summaries to overcome path explosion and extracts the semantics of input constraints to reduce false positives. Evaluated against five state-of-the-art tools on 31 disclosed vulnerabilities, NÜWA has uncovered 152 previously unknown vulnerabilities across IoT vendors, with 88 assigned CVE IDs.

</details>

<details><summary><strong>Drone Remote ID Spoofer and Low Cost Receiver Application</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Llorenç Romá Alvarez](https://img.shields.io/badge/Llorenç%20Romá%20Alvarez-informational)

🔗 **Link:** [Drone Remote ID Spoofer and Low Cost Receiver Application](https://github.com/cyber-defence-campus/droneRemoteIDSpoofer)  
📝 **Description:** This project pairs a Python-based drone Remote ID spoofer with an extended Remote ID monitoring web platform that enables offline-capable, real-time, and replayable monitoring of civilian drone broadcasts over WiFi as required by the ASD-STAN prEN 4709-002 standard. The spoofer broadcasts fake Remote IDs in the ASD-STAN and proprietary DJI formats using scapy and an injection-capable WiFi adapter. The receiver application has been extended with full ASD-STAN support, multithreaded performance, and a user-friendly offline mapping frontend.

</details>

---
## 🔍 OSINT
<details><summary><strong>Dradis Framework: Intelligent Automation for collaboration and reporting</strong></summary>

![Asia 2026](https://img.shields.io/badge/Asia%202026-green) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [Dradis Framework: Intelligent Automation for collaboration and reporting](https://github.com/dradis/dradis-ce)  
📝 **Description:** Dradis Framework is an open-source pentest management and reporting tool that centralizes findings, notes, and evidence across cybersecurity teams. It combines results from scanners such as Nessus, Burp Suite, and Nikto with manual findings and attack narratives to streamline collaboration and automate reporting. The latest iteration extends Dradis Echo for LLM-assisted reporting with context awareness and prompt library building, alongside redesigned navigation, API scanner uploads, and a new MITRE ATT&CK calculator.

</details>

---