# Asia 2026
---
📍 49 tools demonstrated at **Black Hat Arsenal Asia 2026**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security) (4)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (8)
- [🌐 Web/AppSec](#-webappsec) (2)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (2)
- [🔍 OSINT](#-osint) (1)
- [🔴 Red Teaming](#-red-teaming) (4)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (7)
- [🔵 Blue Team & Detection](#-blue-team--detection) (8)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (2)
- [🤖 AI, ML & Data Science](#-ai-ml--data-science) (8)
- [🧠 Reverse Engineering](#-reverse-engineering) (3)
---
## ☁️ Cloud Security
<details><summary><strong>KubeShadow (Advanced Offensive Kubernetes Red-Team Framework)</strong> — Aashita Pandey, Binayak Choudhury</summary>

**Track:** Cloud Security · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/ashifly/KubeShadow](https://github.com/ashifly/KubeShadow)  
📝 **Description:** KubeShadow is a Go-based modular red-team framework for end-to-end adversary emulation against Kubernetes environments including EKS, GKE, AKS, and self-hosted clusters. It combines a recon engine, graph-based chaining, and a plugin architecture covering control-plane and workload exploitation (etcd injection, kubelet hijack, sidecar/init-container injection, RBAC escalation, ephemeral container attacks), multi-cloud identity pivoting, and exfiltration adapters. Built-in lab manifests, an interactive dashboard, and prioritized remediation guidance support reproducible PoCs and purple-team exercises.

</details>

<details><summary><strong>Oblivion Token : M365 Conditional Access Policy Bypass OST (Offensive Tooling)</strong> — Nuttakorn Tungpoonsup, Waris Damkham</summary>

**Track:** Cloud Security · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Waariss/OblivionToken](https://github.com/Waariss/OblivionToken)  
📝 **Description:** Oblivion Token is an offensive-research utility for testing Microsoft 365 Conditional Access Policy (CAP) bypass scenarios in a repeatable, scriptable way. It emits valid OIDC ID tokens and OAuth2 access tokens for Microsoft Graph API post-exploitation automation, exercising token-centric workflows against Microsoft first-party applications without browser prompts. Red-teamers and security researchers use it to expose where device, network, and app-context assumptions in CAP enforcement break down.

</details>

<details><summary><strong>Prowler Open Cloud Security - release of v6.0</strong> — Toni de la Fuente</summary>

**Track:** Cloud Security · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/prowler-cloud/prowler](https://github.com/prowler-cloud/prowler)  
📝 **Description:** Prowler is an open-source cloud security platform that performs continuous monitoring, security assessments, audits, incident response support, hardening, and forensics readiness across AWS, Azure, GCP, Kubernetes, and M365. It runs hundreds of checks mapped to compliance frameworks including CIS, NIST 800, NIST CSF, CISA, FedRAMP, PCI-DSS, GDPR, HIPAA, FFIEC, SOC2, and ENS. The v6.0 release expands coverage and integrations for multi-cloud security teams managing posture at scale.

</details>

<details><summary><strong>SkyEye: When Your Vision Reaches Beyond IAM Boundary Scope in the Cloud</strong> — Minh Hoang Nguyen, Anh Minh Ho, Bao Son To</summary>

**Track:** Cloud Security · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/0x7a6b4c/SkyEye](https://github.com/0x7a6b4c/SkyEye)  
📝 **Description:** SkyEye is a cooperative multi-principal IAM enumeration framework for AWS that overcomes the blind spots of principal-centric reconnaissance tools. It introduces the Cross-Principal IAM Enumeration Model (CPIEM) and Transitive Cross-Role Enumeration Model (TCREM) to synchronize sessions across multiple user and role credentials, dynamically chaining permissions to surface privilege escalation paths invisible to siloed enumeration. SkyEye maps AWS actions to MITRE ATT&CK Cloud TTPs with severity ratings to support red team adversary simulation and cloud detection engineering.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Security Playground (Hands-On-Activity)</strong> — Abhishek S, Keshav Malik, Surya Kanagasabapathi</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** Not Available  
📝 **Description:** AI Security Playground is an open-source, gamified training platform that teaches security risks unique to AI and GenAI environments, including LLMs, AI agents, and MCP servers. It guides participants through real-world attacks ranging from beginner to advanced, covering exploits against AI agents, MCP server misconfigurations, and prompt injection techniques. An AI-powered judge provides immediate feedback as users solve each challenge, helping developers and security practitioners build offensive and defensive AI security skills.

</details>

<details><summary><strong>AI Wargame</strong> — Pedram Hayati</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** [https://play.secdim.com/](https://play.secdim.com/)  
📝 **Description:** AI Wargame is an interactive attack-and-defense platform where players secure their own AI chatbot's secrets while attempting to extract secrets from opponents' chatbots. It provides a king-of-the-hill style competition for learning prompt injection, AI security hardening, and chatbot defense techniques at all skill levels. Each player has access to their chatbot's source code repository to run, test, debug, and push changes during the game.

</details>

<details><summary><strong>Casino Heist v2</strong> — Richard Tan, Anthony Sai Richardo</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Kiinzu/Casino-Heist](https://github.com/Kiinzu/Casino-Heist)  
📝 **Description:** Casino Heist v2 is a smart contract security playground centered on Solidity contracts deployed on the Ethereum blockchain. It pairs each challenge with theoretical foundations, exploitation walkthroughs, and mitigation guidance, spanning fundamentals such as reentrancy and integer overflow through advanced attack vectors inspired by real-world incidents. The platform serves CTF players, security researchers, educators, and developers exploring blockchain security.

</details>

<details><summary><strong>Circuit Breaker CTF</strong> — Manzel Seet, Kenneth Tong</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** Not Available  
📝 **Description:** Circuit Breaker CTF is a testbench for power industry security research that simulates devices and protocols across the generation, transmission, distribution, and consumer chain. Building on prior iterations focused on individual device exploitation, it introduces system-level interactions and highlights the role and adaptability of circuit breakers across diverse operational environments. Participants engage with realistic ICS scenarios to practice exploitation and defense techniques specific to electrical power infrastructure.

</details>

<details><summary><strong>Damn Vulnerable Model Context Protocol (DVMCP) Platform</strong> — Ankit Garg, Harish Santhanalakshmi Ganesan</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/harishsg993010/damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)  
📝 **Description:** Damn Vulnerable MCP (DVMCP) is a deliberately insecure implementation of the Model Context Protocol built as an educational and research platform for security in LLM-integrated systems. It simulates real-world MCP risks such as prompt injection, tool poisoning, excessive permissions, rug-pull attacks, token theft, and multi-vector exploits across ten progressive Docker-deployable challenges. Recent additions include identity-based attacks, MCP-specific supply chain scenarios, and a web dashboard for interactive challenge navigation, real-time monitoring, and analytics.

</details>

<details><summary><strong>PwnSat: A Vulnerable-by-Design Satellite Hardware and Platform for AeroSpace Hacking and Research</strong> — Romel Marin cordoba, Kevin Jahaziel Leon Morales</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Pwnsat/FlatSat](https://github.com/Pwnsat/FlatSat)  
📝 **Description:** PWNSAT is an open-source vulnerable-by-design aerospace cybersecurity platform that combines a physical CubeSat, a ground station, a Mission Operations Center, and RF communication links. It replicates a real space mission using aerospace protocols such as CCSDS and AX.25 over LoRa and FSK, with intentional vulnerabilities introduced at the radio frequency, firmware, and MOC service layers under the SPARTA framework. The platform supports CTF-style exercises, technical audits, and penetration testing of satellite systems for researchers and educators.

</details>

<details><summary><strong>Sysrupt: Portable OT/ICS and Hardware Security Training Platform (CompatriOT v2)</strong> — Season Cherian, Vivek NJ</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/traboda/CompatrIoT](https://github.com/traboda/CompatrIoT)  
📝 **Description:** Sysrupt is a portable, self-contained OT/ICS and hardware security training platform that evolves the CompatrIoT project from Black Hat Asia 2025 into the operational technology domain. Built around a Radxa A5E SBC, dual ESP32-C6 microcontrollers, a PLC simulator, and an onboard managed Ethernet switch, it lets participants observe and manipulate live OT protocol traffic while watching attacks affect physical outputs. The platform includes hardware-based signing of proof-of-exploit tokens for verifiable scoring in CTFs and research labs.

</details>

<details><summary><strong>ThreatShield – The Intelligent Way of Threat Modelling</strong> — Satyam Nagpal, Sayooj Nagpal, Ashwin Shenoi, Nandu S. Pillai</summary>

**Track:** Arsenal Lab · **Event:** Asia 2026  
🔗 **Link:** Not Available  
📝 **Description:** ThreatShield is an AI-powered threat modeling and security analysis tool that automates STRIDE-based threat model generation using OpenAI's enterprise API. It ingests heterogeneous inputs such as PRDs, architecture diagrams, Confluence pages, Slack threads, and meeting transcripts, then produces structured threat models, attack trees, DREAD scoring, and prioritized mitigations. The tool helps security engineering teams scale threat modeling across product development without relying on manual whiteboard sessions.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>BugHound MCP</strong> — Krishna Naidu, eric tee, Lwin Min Oo, Kai-Wei Hoon, Valen Sai</summary>

**Track:** Web AppSec · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/binderlabs/BugHound-MCP](https://github.com/binderlabs/BugHound-MCP)  
📝 **Description:** BugHound MCP is a Model Context Protocol-based security automation framework that streamlines bug bounty hunting through natural language commands. It orchestrates specialized security tools across reconnaissance, scanning, and analysis domains, translating simple prompts into coordinated security workflows so researchers can run comprehensive assessments through conversational interactions instead of complex command chains.

</details>

<details><summary><strong>Canary WAF</strong> — Amelia Chua</summary>

**Track:** Web AppSec · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/umiyuikaiteitan/Canary-WAF](https://github.com/umiyuikaiteitan/Canary-WAF)  
📝 **Description:** Canary WAF is a deceptive defense system that combines a Web Application Firewall with honeypot capabilities for web application security. It redirects detected web attack attempts to a fake database populated with synthetic data, drawing attackers away from production systems while collecting telemetry on their techniques. The platform provides defenders with real-time attack visibility and intelligence to inform incident response and threat modeling.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Aegis: LLM SAST Framework for Blacklight Code Hunts</strong> — Can Oztas</summary>

**Track:** Code Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/canoztas/aegis](https://github.com/canoztas/aegis)  
📝 **Description:** Aegis is an open-source SAST framework that leverages LLMs to analyze source code for security vulnerabilities and produce detailed reports. Its flexible architecture supports a range of LLM providers as well as traditional machine learning models, allowing teams to plug in different backends for vulnerability detection across diverse codebases.

</details>

<details><summary><strong>SBoM Play</strong> — Anant Shrivastava</summary>

**Track:** Code Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/cyfinoid/sbomplay](https://github.com/cyfinoid/sbomplay)  
📝 **Description:** SBoM Play is a browser-based SBOM exploration and intelligence extraction platform that runs entirely client-side without backend infrastructure. It imports SBOMs or extracts them directly from GitHub repositories, then enriches dependency data using OSV, deps.dev, and ecosyste.ms to provide a unified view across repositories and organizations. The tool surfaces tech debt patterns, version drift, license posture, SBOM quality gaps, end-of-life packages, dependency confusion indicators, and maintainer risk signals beyond traditional vulnerability tracking.

</details>

---
## 🔍 OSINT
<details><summary><strong>Dradis Framework: Intelligent Automation for collaboration and reporting</strong> — Daniel Martin</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/dradis/dradis-ce](https://github.com/dradis/dradis-ce)  
📝 **Description:** Dradis Framework is an open-source pentest management and reporting tool that centralizes findings, notes, and evidence across cybersecurity teams. It combines results from scanners such as Nessus, Burp Suite, and Nikto with manual findings and attack narratives to streamline collaboration and automate reporting. The latest iteration extends Dradis Echo for LLM-assisted reporting with context awareness and prompt library building, alongside redesigned navigation, API scanner uploads, and a new MITRE ATT&CK calculator.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>EntraGoat - A Deliberately Vulnerable Entra ID Environment</strong> — Jonathan Elkabas, Eric Woodruff</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Semperis/EntraGoat](https://github.com/Semperis/EntraGoat)  
📝 **Description:** EntraGoat is a deliberately vulnerable Microsoft Entra ID (formerly Azure Active Directory) environment that simulates real-world misconfigurations and attack paths in a hands-on, CTF-style lab. It deploys multiple privilege escalation scenarios directly into an existing tenant, focusing on black-box methodologies across IAM, application, and service principal abuses. The platform is intended for security researchers, red teamers, and identity defenders building practical experience with Entra ID attack chains.

</details>

<details><summary><strong>Golden dMSA: One Key to Rule Them All</strong> — Adi Malyanker</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Semperis/GoldenDMSA](https://github.com/Semperis/GoldenDMSA)  
📝 **Description:** Golden dMSA is a post-exploitation tool that exploits a design flaw in delegated Managed Service Accounts (dMSAs) introduced in Windows Server 2025, enabling forest-wide compromise of managed service account credentials. After temporary control of a single domain and access to KDS root key material, it enumerates protected dMSA and gMSA accounts from non-privileged contexts and algorithmically reconstructs their passwords offline, bypassing the strengthened controls these accounts were designed to enforce.

</details>

<details><summary><strong>SAMLSmith</strong> — Eric Woodruff</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Semperis/SAMLSmith](https://github.com/Semperis/SAMLSmith)  
📝 **Description:** SAMLSmith is a C# offensive tool for forging SAML responses against enterprise identity providers, evolving earlier proof-of-concept tooling for Entra ID response forging into a full red-team utility. It supports multiple identity provider response forging, an AD FS-specific mode, SAML request processing with InResponseTo, WS-Federation responses, and PFX certificate extraction from AD FS encrypted material and DKM keys. Operators use it to execute Golden SAML and Silver SAML attacks against SaaS applications when signing key material can be obtained.

</details>

<details><summary><strong>SquarePhish 2.0 - QR Code OAuth 2.0 Device Code Flow Phishing for Primary Refresh Token</strong> — Nevada Romsdahl, Kam Talebzadeh</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/nromsdahl/squarephish2](https://github.com/nromsdahl/squarephish2)  
📝 **Description:** SquarePhish 2.0 is an advanced phishing toolkit that combines QR codes with the OAuth 2.0 device code authentication flow to capture Microsoft Entra ID Primary Refresh Tokens. The tool leverages the Microsoft Authentication Broker client ID to convert refresh tokens into PRTs, granting broad single sign-on access to Microsoft cloud resources via Family of Client IDs (FOCI) tokens. It enables red teams and defenders to test detection and prevention capabilities against modern device code phishing attacks.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>actsense: GitHub Actions Workflow Auditor</strong> — Kumar Ashwin</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/0xCardinal/actsense](https://github.com/0xCardinal/actsense)  
📝 **Description:** actsense is a local, vendor-agnostic framework for auditing GitHub Actions workflows and their dependencies. It statically maps all actions, including nested composite, JavaScript, and Docker actions, and runs over 30 security checks covering pinning, permissions, events, and secrets, while also assessing Docker images and external dependencies for unpinned or unpinnable references. Findings are presented through an interactive dependency graph that exposes the full transitive action graph and helps teams trace relationships, triage supply chain risks, and secure CI/CD pipelines without leaking data to third parties.

</details>

<details><summary><strong>BoardSentinel: An Automated Static Analysis Framework for BMC Firmware Vulnerability Detection</strong> — Zhong Wang, Lewei Qu, Sheng Ma</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** Not Available  
📝 **Description:** BoardSentinel is an automated static analysis framework that extracts, analyzes, and detects vulnerabilities in Baseboard Management Controller (BMC) firmware from major vendors including AMI MegaRAC, OpenBMC, Dell iDRAC, and H3C HDM. It combines a universal firmware extraction engine that handles embedded filesystems such as SquashFS, CramFS, JFFS2, and FIT images with hybrid vulnerability detection that pairs IDA Pro and Radare2 analysis with Semgrep pattern matching and custom Python detectors. An extensible YAML-based rule system allows rapid integration of newly disclosed CVEs, enabling researchers and security teams to assess BMC firmware security at scale without deep reverse engineering expertise.

</details>

<details><summary><strong>Dep-Hallucinator: Detecting Dependency Confusion from AI/LLM-Hallucinated Packages</strong> — Serhan Bahar</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/serhanwbahar/dep-hallucinator](https://github.com/serhanwbahar/dep-hallucinator)  
📝 **Description:** Dep-Hallucinator is an open-source security scanner that identifies AI/LLM-hallucinated package dependencies before they enable slopsquatting attacks. It queries official package registries through native APIs and applies machine learning to distinguish AI-generated naming patterns from legitimate packages, addressing the finding that 19.7% of AI-suggested dependencies are non-existent and that 58% of these hallucinated names are repeated consistently. The tool helps developers and security teams detect dependency confusion risks introduced by AI coding assistants.

</details>

<details><summary><strong>DursGo: Web App Security Scanner with AI Analysis Vulnerability</strong> — Mohammad Ali Syarief, Nur Fadhillah</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/roomkangali/dursgo](https://github.com/roomkangali/dursgo)  
📝 **Description:** DursGo is a Go-powered web application security scanner that combines high-performance automated scanning with LLM-driven analysis for penetration testing and security audits. It performs technology fingerprinting, intelligent crawling and endpoint discovery (with optional headless browser support for SPAs), and concurrent execution of vulnerability modules such as XSS and SQL injection, including OAST verification for blind issues. Findings are deduplicated and enriched with AI-generated context to deliver actionable insights.

</details>

<details><summary><strong>Flutterscan: Mobile App Security SAST Framework for Flutter</strong> — Rohit Narayanan M, Akhil Mahendra</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/RohitNarayananM/flutterscan](https://github.com/RohitNarayananM/flutterscan)  
📝 **Description:** Flutterscan is a static application security testing framework purpose-built for the Flutter and Dart ecosystem, addressing gaps left by general-purpose mobile SAST tools. It maps detections to the OWASP Mobile Top 10 and MSTG guidelines to identify insecure coding patterns across Dart files, AndroidManifest.xml, and YAML configurations, and integrates into CI/CD pipelines such as GitHub Actions with output in JSON, SARIF, HTML, and YAML formats for pull-request review.

</details>

<details><summary><strong>SupplyShield: Protecting Your Software Supply Chain</strong> — Rahul Sunder, Yadhu Krishna, Hritik Vijay, Sourav Kumar, Akash Methani</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/supplyshield/supplyshield](https://github.com/supplyshield/supplyshield)  
📝 **Description:** SupplyShield is an open-source application security orchestration framework that integrates SBOM generation and Software Composition Analysis (SCA) into the SDLC at scale, supporting environments with thousands of daily microservice builds. It identifies minimal top-level package upgrades to resolve transitive vulnerabilities, prioritizes findings using EPSS scoring, raises actionable items as GitHub issues, and supports build comparison to track newly introduced packages and vulnerabilities. The framework reduces mean time to detect zero-day issues like Log4j to minutes through a centralized dashboard with key security metrics.

</details>

<details><summary><strong>Zorya: Go Binary Vulnerability Detection with Concolic Execution</strong> — Karolina GORNA, Keith Makan</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Ledger-Donjon/zorya](https://github.com/Ledger-Donjon/zorya)  
📝 **Description:** Zorya is a concolic execution framework written in Rust and engineered to detect runtime vulnerabilities in compiled Go binaries without source code access. It combines Ghidra's P-Code binary lifting with Z3 constraint solving and uses panic-gated exploration to focus symbolic reasoning on vulnerability-leading paths, applying multi-layer reachability filtering to reduce solver queries by two orders of magnitude. The tool surfaces state-dependent bugs and runtime panics in Go-based distributed systems, network services, and container orchestration platforms before they reach production.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Azazel-Pi: Offline Edge-AI SOC/NOC Gateway with Mock-LLM Scoring and Ollama Fallback</strong> — Makoto SUGITA</summary>

**Track:** Network Defense · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/01rabbit/Azazel-Pi](https://github.com/01rabbit/Azazel-Pi)  
📝 **Description:** Azazel-Pi is a portable Raspberry Pi-based SOC/NOC gateway for small networks operating on untrusted links, combining Suricata signals with an on-device Mock-LLM Scorer (a deterministic, rule-assisted micro-model) for real-time threat scoring and a Dockerized Ollama runtime hosting Qwen2.5-1.5B-Instruct as a fallback for low-confidence cases. The scorer outputs a 0-100 risk score that drives a policy planner mapping score bands to tc-based traffic shaping, nftables/iptables micro-policies, and selective NAT redirection to OpenCanary decoys. The pipeline runs fully offline and automatically, with an e-paper panel exposing posture and mode without shell access, while the same scoring logic powers internal QoS to prioritize essential sessions.

</details>

<details><summary><strong>Broń Vault: Open-Source Web-App for Stealer Log Parsing and Exploration</strong> — YoKo Kho, Tomi Ashari, Lalu Raynaldi Pratama Putra</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/itsec-research/bron-vault](https://github.com/itsec-research/bron-vault)  
📝 **Description:** Broń Vault is an open-source web application that automates parsing and exploration of stealer log data, transforming raw archives into structured, queryable intelligence. It replaces manual scripting and inconsistent parsing logic with a unified pipeline that supports 20+ host-info parser variants, installed software parsing, and per-device detail views via a drag-and-drop interface. The tool helps security teams triage credential theft datasets at scale and surface actionable intelligence from information stealer campaigns.

</details>

<details><summary><strong>FLARE-VM: Continuously Sharpening the Analyst's Edge</strong> — Joshua Stroschein, Jae Young Kim</summary>

**Track:** Malware Defense · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/mandiant/flare-vm](https://github.com/mandiant/flare-vm)  
📝 **Description:** FLARE-VM is an open-source collection of installation scripts from Mandiant's FLARE team that automates the build of a Windows-based reverse engineering and malware analysis virtual machine. It provides a revamped GUI, shared package repositories for tool selection, and end-to-end automation including a VirtualBox build script that produces ready-to-export analysis VMs. The framework reduces setup time for malware analysts, reverse engineers, and offensive security practitioners maintaining customized analysis environments.

</details>

<details><summary><strong>Hashtopolis</strong> — Marvin Schwarz, Jesse van Zutphen</summary>

**Track:** Cryptography · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/hashtopolis/server](https://github.com/hashtopolis/server)  
📝 **Description:** Hashtopolis is an open-source client-server platform for managing and monitoring distributed password-recovery tasks using Hashcat and compatible engines. It provides a centralized web interface and REST API to coordinate large-scale cracking operations across heterogeneous GPU and CPU agents, with keyspace partitioning, job scheduling, and real-time telemetry on task progress, performance, and hardware. The platform is licensed under GPL 3.0 and used for legitimate security testing, auditing, and forensic research.

</details>

<details><summary><strong>HoneyOps (A fast, lightweight honeypot cloud-based builder written in Go)</strong> — Melvin Lee, Nicholas Lim</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/PastelOps/HoneyOps](https://github.com/PastelOps/HoneyOps)  
📝 **Description:** HoneyOps is a cloud-based honeypot deployment tool written in Go that provisions and manages decoy environments through an intuitive interface accessible to a range of skill levels. It complements a companion YARA rule collection to support proactive threat detection, monitoring, and analysis of attacker activity in cloud infrastructure for security researchers and threat analysts.

</details>

<details><summary><strong>PacketDuck: AI-Assisted Incident Response</strong> — Daksh Thapar, Rian Tan, Ravin Nagpal</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2026  
🔗 **Link:** Not Available  
📝 **Description:** PacketDuck is an AI-assisted triage acceleration tool that helps L1 SOC analysts rapidly analyze PCAP data during incident response. It surfaces high-risk network behaviors, prioritizes threats, and generates forensic insights to reduce mean time to triage. The tool fits into incident response workflows where analysts must quickly verdict suspicious captures and escalate genuine intrusions.

</details>

<details><summary><strong>StyX A Dual Mode IoT Forensic Tool</strong> — Dr Sapna V M, Sherwin Allen, Meeran Ahmed, Sathvik S, Shambo Sarkar, Prasad Honnavalli</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/SherwinAllen/styx](https://github.com/SherwinAllen/styx)  
📝 **Description:** StyX is a dual-mode IoT forensic framework that unifies evidence acquisition for Android-based smartwatches and smart assistant cloud ecosystems into a single workflow. For smartwatches, it uses ADB to extract Wi-Fi, Bluetooth, IP, and filesystem artifacts with SHA-256 integrity hashing and a web-based viewer. For smart assistants, it automates authenticated login (including OTP and push 2FA) to acquire and report on the last seven days of voice transcripts and audio commands, enabling scalable forensic analysis of smart home devices.

</details>

<details><summary><strong>vet: Open Source Software Supply Chain Security Guardrail in the age of AI SDLC</strong> — Abhisek Datta</summary>

**Track:** Malware Defense · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/safedep/vet](https://github.com/safedep/vet)  
📝 **Description:** vet is an open-source software supply chain security tool tailored for AI-assisted SDLC workflows. Unlike traditional SCA tools, it proactively detects malicious packages before they appear in OSV, integrates as an MCP server with AI IDEs and coding agents like Cursor and Claude Code, and supports conversational analysis over scan results. This positions vet between package-level malicious code detection and developer-first defense in the era of AI coding assistants.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Drone Remote ID Spoofer and Low Cost Receiver Application</strong> — Llorenç Romá Alvarez</summary>

**Track:** Internet Of Things · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/cyber-defence-campus/droneRemoteIDSpoofer](https://github.com/cyber-defence-campus/droneRemoteIDSpoofer)  
📝 **Description:** This project pairs a Python-based drone Remote ID spoofer with an extended Remote ID monitoring web platform that enables offline-capable, real-time, and replayable monitoring of civilian drone broadcasts over WiFi as required by the ASD-STAN prEN 4709-002 standard. The spoofer broadcasts fake Remote IDs in the ASD-STAN and proprietary DJI formats using scapy and an injection-capable WiFi adapter. The receiver application has been extended with full ASD-STAN support, multithreaded performance, and a user-friendly offline mapping frontend.

</details>

<details><summary><strong>NVWA: A Novel Method for Automated Vulnerability Discovery in Embedded Firmware</strong> — Jiaxu Zhao, Yanyan Zou, Yuekang Li, Wei Huo</summary>

**Track:** Hardware/Embedded · **Event:** Asia 2026  
🔗 **Link:** [https://doi.org/10.5281/zenodo.15605329](https://doi.org/10.5281/zenodo.15605329)  
📝 **Description:** NÜWA is a static analysis tool for embedded firmware that detects vulnerabilities by identifying constraint semantic inconsistencies in input-validation code. It performs inter-procedural analysis using function summaries to overcome path explosion and extracts the semantics of input constraints to reduce false positives. Evaluated against five state-of-the-art tools on 31 disclosed vulnerabilities, NÜWA has uncovered 152 previously unknown vulnerabilities across IoT vendors, with 88 assigned CVE IDs.

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>Agent Miner: A General AI Agent Security Auditing Agent Based on Multi-Agent Collaboration</strong> — Lewei Qu, Zeyu Luo, Zezhi Lin, Yue Yang, Sushuang Ma</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** Not Available  
📝 **Description:** Agent Miner is a security auditing tool for general AI agents such as computer-use, browser-use, and mobile-use agents, built on a multi-agent collaborative architecture that decomposes complex audits into subtasks orchestrated through a directed acyclic graph workflow. It performs attack-surface-driven static analysis to identify vulnerability points and generate proof-of-concept exploits, then automatically deploys the target agent in a simulated environment to validate findings. The framework has uncovered more than 15 vulnerabilities across over 10 mainstream open-source AI agents, resulting in 7 assigned CVEs.

</details>

<details><summary><strong>Bastet - AI Smart Contract Vulnerability Detector</strong> — Alice Hsu, Daky Wang, Chengyu Liou</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/OneSavieLabs/Bastet](https://github.com/OneSavieLabs/Bastet)  
📝 **Description:** Bastet is a security infrastructure that pairs a curated dataset of common DeFi smart contract vulnerabilities with an AI-driven automated detection process, focusing on issues frequently rated medium-to-high risk in audit competitions that are difficult to surface with traditional static analysis. The dataset draws from real-world on-chain incidents and audit competition findings, while tailored detection workflows improve AI accuracy in identifying complex vulnerability patterns. Bastet currently ships over 10 detection workflows and 55+ rules, and has flagged more than 25 on-chain contracts containing medium- to high-risk vulnerabilities within its rule coverage.

</details>

<details><summary><strong>CodeRetrX: One-Click to Start Your Journey of Agentic Bug Hunting</strong> — Guancheng Li, Yuxuan Sun, Tianrui Chen</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/XuanwuAI/CodeRetrX](https://github.com/XuanwuAI/CodeRetrX)  
📝 **Description:** CodeRetrX is a code analysis and semantic retrieval library designed to lower the barrier for agent-driven vulnerability discovery. It provides a suite of agentic analysis tools, including cross-referencing, semantic search, code structure inspection, and an embedded CodeQL engine, all exposed via the MCP protocol, alongside a retrieval engine that achieves around 90% recall on complex semantic patterns at roughly 25% of the token cost of full LLM traversal. Researchers can launch or extend agentic bug-hunting setups by connecting to the MCP server or calling the CodeRetrX API.

</details>

<details><summary><strong>Continuous CyberBattleSim: A More Realistic Simulation for AI-driven Attack Path Discovery</strong> — Franco Terranova, Abdelkader Lahmadi</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/terranovafr/C-CyberBattleSim](https://github.com/terranovafr/C-CyberBattleSim)  
📝 **Description:** Continuous CyberBattleSim (C-CyberBattleSim) is an extension of Microsoft's CyberBattleSim that trains and evaluates reinforcement learning agents on cyber attack path prediction modeled as a vulnerability chaining problem. It enriches scenario generation with Cyber Threat Intelligence drawn from empirical Shodan distributions, automates vulnerability outcome inference from metadata, and integrates a graph neural network and language model embedding to represent nodes and vulnerabilities in continuous vector spaces. The framework supports more scalable and generalizable RL training for synthetic environments resembling real-world infrastructures.

</details>

<details><summary><strong>DataTrap - Adaptive LLM-Powered Honeypot Framework</strong> — Ori Nakar</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/ThalesGroup/dd-honeypot](https://github.com/ThalesGroup/dd-honeypot)  
📝 **Description:** DataTrap is an open-source, extensible honeypot framework that simulates realistic application behavior across HTTP, HTTPS, SSH, and database protocols, covering web applications, IoT devices, and databases. It combines recorded application payloads with contextual metadata and LLM reasoning to generate dynamic, context-aware responses, and includes a honeypot dispatcher that routes traffic to the most appropriate honeypot type along with an LLM-based reporting module that converts captured data into actionable threat intelligence. DataTrap is distributed as a Docker image for rapid deployment.

</details>

<details><summary><strong>LLMInspector - Advanced LLM Fingerprinting & Security Testing Tool</strong> — Alfonso Munoz, Jacobo Blancas</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/michelin/LLMInspector](https://github.com/michelin/LLMInspector)  
📝 **Description:** LLMInspector is a penetration testing suite for auditing Large Language Models deployed in production environments. It fingerprints models through behavioral patterns, response characteristics, and semantic signatures, and runs prompt injection testing against both commercial APIs and open-source deployments. It integrates with Ollama to analyze over 200 local models for adversarial behavior and alignment issues.

</details>

<details><summary><strong>NOVA Ecosystem: Your AI Security Arsenal</strong> — Thomas Roccia</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/Nova-Hunting/nova-framework](https://github.com/Nova-Hunting/nova-framework)  
📝 **Description:** NOVA is an open-source prompt pattern matching engine that detects and classifies adversarial prompts targeting LLM applications, introducing the concept of Indicators of Prompt Compromise (IoPC). It combines keyword rules, semantic similarity, and LLM-based evaluation in a YARA-inspired syntax, integrating into LLM pipelines, MCP servers, and red-team frameworks. The ecosystem extends to PromptIntel and Proximity modules for hunting jailbreaks, data exfiltration, and prompt injection attempts before execution.

</details>

<details><summary><strong>Prompt Hardener: Automated Evaluation and Hardening of LLM System Prompts</strong> — Yoshiki Kitamura, Junki Yuasa</summary>

**Track:** AI, ML & Data Science · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/cybozu/prompt-hardener](https://github.com/cybozu/prompt-hardener)  
📝 **Description:** Prompt Hardener is an open-source toolkit that evaluates and strengthens system prompts used in LLM applications against prompt injection. It uses an LLM to review prompts against defensive techniques such as spotlighting, instruction defense, role consistency, random sequence enclosure, and secrets exclusion, then generates structured feedback and rewrite suggestions. An adversarial testing module executes payloads inspired by the OWASP Top 10 for LLM Applications to verify mitigation effectiveness across an evaluate-improve-verify workflow.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>From PoC to Breakthrough: arkdecompiler - The Decompiler for HarmonyOS NEXT</strong> — Xiaoyu He, Qidan He</summary>

**Track:** Reverse Engineering · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/jd-opensource/arkdecompiler](https://github.com/jd-opensource/arkdecompiler)  
📝 **Description:** arkdecompiler is a decompiler purpose-built for HarmonyOS NEXT, Huawei's Android-incompatible operating system based on the HongMeng kernel and ArkCompiler toolchain. It parses Panda Binary Files and Panda Bytecode into Panda IR, then reconstructs the native ArkTS AST and translates it back to source code. The release expands beyond the Black Hat USA 2025 proof-of-concept to support arrays, objects, functions, branches, loops, exceptions, closures, modules, and incremental compilation for security analysis of native HarmonyOS applications.

</details>

<details><summary><strong>Mothra: Timeless Debugging of EVM Transactions with Ghidra</strong> — Yuejie Shi, Aohui Wang</summary>

**Track:** Reverse Engineering · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/ambergroup-labs/Mothra](https://github.com/ambergroup-labs/Mothra)  
📝 **Description:** Mothra is a Ghidra extension for reverse engineering EVM bytecode that adds timeless debugging of Ethereum Virtual Machine transactions. It integrates with Ghidra's Debugger tool to let researchers replay an EVM transaction and step forward and backward at the opcode level, inspecting state at any point in execution. The tool supports smart contract auditing, exploit analysis, and post-incident investigation of on-chain activity.

</details>

<details><summary><strong>QuantumStrand (qs): A Structural Approach to String Analysis for Rapid Indicator Filtering</strong> — Joshua Stroschein, Jae Young Kim</summary>

**Track:** Reverse Engineering · **Event:** Asia 2026  
🔗 **Link:** [https://github.com/mandiant/flare-floss](https://github.com/mandiant/flare-floss)  
📝 **Description:** QuantumStrand (qs) is an experimental static string analysis tool from Mandiant's FLARE team that transforms flat strings output into a structural map of a binary. It parses PE files into a tree of sections, headers, resources, overlays, and embedded files, then enriches each extracted string with contextual tags driven by expert heuristics and global prevalence databases. Malware analysts use it to filter noise during triage and rapidly focus on indicators that matter, with full layout and tag data exported as JSON.

</details>

---
