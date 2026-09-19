# Europe 2025
---
📍 59 tools demonstrated at **Black Hat Arsenal Europe 2025**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security) (6)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (6)
- [🌐 Web/AppSec](#-webappsec) (3)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (1)
- [🔍 OSINT](#-osint) (1)
- [🔴 Red Teaming](#-red-teaming) (12)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (12)
- [🔵 Blue Team & Detection](#-blue-team--detection) (6)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (2)
- [🤖 AI, ML & Data Science](#-ai-ml--data-science) (7)
- [🧠 Reverse Engineering](#-reverse-engineering) (2)
- [🧠 Social Engineering / General](#-social-engineering--general) (1)
---
## ☁️ Cloud Security
<details><summary><strong>Beyond the Static rules: Cloud-Native Anomaly Detection with Kubescape</strong> — Ben Hirschberg, Amit Schendel</summary>

**Track:** Cloud Security · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/kubescape/kubescape](https://github.com/kubescape/kubescape)  
📝 **Description:** Kubescape is a CNCF Incubating Kubernetes security platform (10k+ GitHub stars) that provides configuration scanning, vulnerability monitoring, and eBPF-based runtime anomaly detection. Its new runtime detection capability goes beyond static rules by learning normal application behavior and detecting anomalies without constant manual tuning.

</details>

<details><summary><strong>Cloud Sec AI BOT</strong> — Nandan Gupta, Prashant Venkatesh, Swarup Natukula</summary>

**Track:** Cloud Security · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/nandangupta-security/CloudSecAIBot](https://github.com/nandangupta-security/CloudSecAIBot)  
📝 **Description:** One interface. All your clouds: Ask any question to the BOT regarding any security misconfiguration and receive consolidated results from AWS, Azure, and Google Cloud without mastering different CLI syntaxes. Cloud Sec AI Bot helps security engineers of multiple flavors validating any cloud misconfiguration such as exposed public storage, missing MFA configurations, excessive role permissions, and least-privilege policy violations across your entire cloud infrastructure.

</details>

<details><summary><strong>KubeShadow - Advanced Offensive Kubernetes Red-Team Framework</strong> — Aashita Pandey, Binayak Choudhury</summary>

**Track:** Cloud Security · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ashifly/KubeShadow](https://github.com/ashifly/KubeShadow)  
📝 **Description:** KubeShadow is an advanced red team and adversary simulation framework purpose-built to exploit, persist, and operate within Kubernetes clusters in stealth. Far beyond traditional misconfiguration scanners, KubeShadow delivers real-world offensive capabilities designed to emulate high-caliber threat actors operating across AWS EKS, GCP GKE, and Azure AKS managed clusters.

</details>

<details><summary><strong>Securing Secrets from Dev Machine to Deployments Using SLV</strong> — Shibly Meeran, Sriram Krishnan, Keshav Kandasamy</summary>

**Track:** Cloud Security · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/amagioss/slv](https://github.com/amagioss/slv)  
📝 **Description:** SLV (Secure Local Vault) bridges the gap between local developer environments and secure CI/CD pipelines by offering a lightweight, CLI-first tool for managing secrets without relying on centralized, cloud-hosted secrets managers. This talk will demonstrate how sensitive credentials can leak across development to production workflows and how SLV prevents this through isolated, encrypted vaults, ephemeral secrets injection, and audit-friendly flows. With real-world attack paths as context, we will show how SLV hardens secrets handling from the first line of code to final deployment.

</details>

<details><summary><strong>SkyEye: When Your Vision Reaches Beyond IAM Boundary Scope in the Cloud</strong> — Minh Hoang Nguyen, Anh Minh Ho, Bao Son To</summary>

**Track:** Cloud Security · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/0x7a6b4c/SkyEye](https://github.com/0x7a6b4c/SkyEye)  
📝 **Description:** SkyEye is a cloud IAM enumeration and analysis tool that aggregates permissions across multiple principals (users, roles, groups) to build a complete picture of effective IAM permissions. It identifies hidden privilege escalation vectors, misconfigurations, and compliance gaps that principal-specific tools miss by correlating inline and managed policies across the entire IAM landscape.

</details>

<details><summary><strong>Spotter – Universal Kubernetes Security Engine</strong> — Madhu Akula</summary>

**Track:** Cloud Security · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/madhuakula/spotter](https://github.com/madhuakula/spotter)  
📝 **Description:** Spotter is an open-source Kubernetes security engine that uses CEL (Common Expression Language) for unified policy definitions across the entire cluster lifecycle—development, CI/CD, admission control, runtime, and continuous monitoring. It supports both enforcement and monitoring modes with policies mapped to CIS benchmarks and MITRE ATT&CK.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Wargame</strong> — Pedram Hayati, Davide Cioccia, Stefan Petrushevski</summary>

**Track:** Arsenal Lab · **Event:** Europe 2025  
🔗 **Link:** [https://play.secdim.com/](https://play.secdim.com/)  
📝 **Description:** AI Wargame is an interactive attack-and-defense platform where players secure their own AI chatbot's secrets while attempting to extract secrets from opponents' chatbots. It provides a king-of-the-hill style competition for learning prompt injection, AI security hardening, and chatbot defense techniques at all skill levels.

</details>

<details><summary><strong>Capture the Train: Purple Team Edition!</strong> — Arnaud Soullie, Florian Pouchet</summary>

**Track:** Arsenal Lab · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/wavestone-cdt/caldera-s7](https://github.com/wavestone-cdt/caldera-s7)  
📝 **Description:** Caldera-S7 and Caldera-OPCUA are MITRE CALDERA plugins that add ICS attack capabilities for Siemens S7 and OPC-UA protocols. Used in the Capture the Train purple team exercise, they enable launching real ICS attacks against PLCs and SCADA systems to assess detection effectiveness of industrial monitoring solutions.

</details>

<details><summary><strong>Minino: Multiband Hacking Now with GPS</strong> — Paulino Calderon, Eduardo Contreras</summary>

**Track:** Arsenal Lab · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ElectronicCats/Minino](https://github.com/ElectronicCats/Minino)  
📝 **Description:** Minino is a Swiss Army knife for IoT hacking, designed to empower security professionals with a versatile, all-in-one toolkit for assessing and attacking IoT devices. Minino integrates WiFi, Bluetooth Low Energy (BLE), Zigbee, Thread, Matter, and a GPS module into a compact, open-source hardware solution

</details>

<details><summary><strong>Models as Malware: Attacking and Defending the AI Supply Chain</strong> — Nathan Chang, Roee Landesman</summary>

**Track:** Arsenal Lab · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ShenaoW/awesome-llm-supply-chain-security](https://github.com/ShenaoW/awesome-llm-supply-chain-security)  
📝 **Description:** A curated resource collection and hands-on lab for understanding AI supply chain security risks. Covers attacks that embed malicious payloads in AI model serialization formats (Pickle, SafeTensors, ONNX) distributed through platforms like HuggingFace, and demonstrates detection and defense techniques against backdoored model files.

</details>

<details><summary><strong>ThreatShield – The Intelligent Way of Threat Modelling</strong> — Satyam Nagpal, Sayooj Nagpal, Ashwin Shenoi</summary>

**Track:** Arsenal Lab · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/threatshield/threatshield](https://github.com/threatshield/threatshield)  
📝 **Description:** ThreatShield is an AI-powered threat modeling and security analysis tool designed to automate and elevate threat modeling using OpenAI's enterprise API. It processes raw documents like PRDs, architecture diagrams, confluence docs, slack threads and meeting transcripts to generate structured STRIDE-based threat models, attack trees, DREAD scoring, and mitigstions.

</details>

<details><summary><strong>WHIDBOARD: Plug It In, Set It Up & Get Ready to Hack!</strong> — Luca Bongiorni</summary>

**Track:** Arsenal Lab · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/whid-injector/WHIDBOARD](https://github.com/whid-injector/WHIDBOARD)  
📝 **Description:** WHIDBOARD is the ultimate tool-suite for Hardware Hackers. It is designed to act as the perfect Swiss-Army-Knife for hacking any (I)IoT & Embedded devices. Thanks to its core controller (a.k.a. BRUSCHETTAPRO) it can support the interaction with multiple protocols (i.e. UART, SPI, I2C, JTAG & SWD) as well as different Logic Levels (i.e. 1.8V, 2.5V, 3.3V and the VREF of the target itself). Nonetheless, it also allows the hacker to enumerate (UART, JTAG & SWD) thanks to its 24 channels' Pin Enumerator feature, as well as the ability to act as a 8 channels Logic Analyzer at 24MHz.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Blackdagger: Cyber Workflow Automation Framework</strong> — Mahmut Erdem Özgen, Ata Seren, Elif Başar Özgen, Ömer Kutay Atilla</summary>

**Track:** Web AppSec · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ErdemOzgen/blackdagger](https://github.com/ErdemOzgen/blackdagger)  
📝 **Description:** Blackdagger is an innovative workflow automation framework specifically designed to simplify and accelerate cybersecurity operations across DevOps, DevSecOps, MLOps, MLSecOps, and Continuous Automated Red Teaming (CART). At its core, Blackdagger reduces complexity and manual overhead by leveraging a novel declarative YAML-based Directed Acyclic Graph (DAG) approach, enabling users to intuitively define automation pipelines, clearly visualize task dependencies, and minimize extensive scripting or coding typically required by traditional cronbased schedulers and orchestration platforms. A user-friendly built-in Web UI further empowers users by providing easy, real-time management, monitoring, and execution of workflows.

</details>

<details><summary><strong>DepConfuse: Shielding Your Packages from Dependency Confusion Attacks</strong> — Akhil Mahendra, Harsh Varagiya, Sourav Kumar, Akshansh Jaiswal</summary>

**Track:** Web AppSec · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/th3-j0k3r/DepConfuse](https://github.com/th3-j0k3r/DepConfuse)  
📝 **Description:** DepConfuse is a command-line tool that proactively detects dependency confusion vulnerabilities, a growing threat in modern software supply chains. By scanning SBOMs or PURLs, it identifies internal package names that are vulnerable to takeover in the public registry, allowing teams to remediate issues early in the development lifecycle.

</details>

<details><summary><strong>Project Foxhound</strong> — Thomas Barber, David Klein</summary>

**Track:** Web AppSec · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/SAP/project-foxhound](https://github.com/SAP/project-foxhound)  
📝 **Description:** Project Foxhound is a modified Firefox browser with built-in dynamic taint tracking that automatically detects client-side (DOM-based) cross-site scripting (XSS) vulnerabilities. Developed by SAP, it traces data flows from attacker-controlled sources to security-sensitive sinks in real-time, identifying DOM XSS that traditional server-side scanning tools miss.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Catch the Flow: Securing CI/CD Workflows with Flowlyt</strong> — Chanchal Kalnarayan, Hare Krishna Rai, Gaurav Joshi</summary>

**Track:** Code Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/harekrishnarai/flowlyt](https://github.com/harekrishnarai/flowlyt)  
📝 **Description:** Flowlyt is a CI/CD workflow security scanner that detects vulnerabilities in GitHub Actions workflows. It identifies risks such as malicious third-party actions, secret exfiltration paths, insecure permissions, and supply chain attack vectors like the tj-actions/changed-files compromise (CVE-2025-30066), helping teams secure their CI/CD pipelines.

</details>

---
## 🔍 OSINT
<details><summary><strong>Exposor - A Contactless Reconnaissance Tool Using Internet Search Engines with a Unified Syntax</strong> — Abdulla Abdullayev</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/abuyv/exposor](https://github.com/abuyv/exposor)  
📝 **Description:** Exposor is a contactless reconnaissance tool that queries multiple internet search engines (Shodan, Censys, FOFA, ZoomEye, etc.) using a unified syntax. It eliminates the need to learn different query languages for each platform, enabling efficient discovery of exposed technologies and vulnerabilities across an organization's attack surface.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>DroidGround: A Flexible Playground for Android CTF Challenges</strong> — Angelo Delicato</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/SECFORCE/droidground](https://github.com/SECFORCE/droidground)  
📝 **Description:** DroidGround is an application that enables hosting new kinds of Android CTF challenges. It allows to setup a remotely accessible Android jailed to the target application and provides a series of features to allow the player to solve the challenge and get the flag directly from the web application. In this way it is possible to create challenges in which the player has to get RCE on the device to read the flag form a text file on the device.

</details>

<details><summary><strong>EntraGoat - A Deliberately Vulnerable Entra ID Environment</strong> — Tomer Nahum, Jonathan Elkabas</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Semperis/EntraGoat](https://github.com/Semperis/EntraGoat)  
📝 **Description:** EntraGoat is a deliberately vulnerable environment designed to simulate real-world security misconfigurations and attack scenarios in Microsoft Entra ID (formerly Azure Active Directory). Security professionals, researchers, and red teamers can leverage EntraGoat to gain hands-on experience identifying and exploiting identity and access management (IAM) vulnerabilities, privilege escalation paths, and other security flaws specific to cloud-based Entra ID environments.

</details>

<details><summary><strong>GHARF: GitHub Actions RedTeam Framework</strong> — Yusuke Kubo, Yuuki Matsumoto</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/nttcom/gharf](https://github.com/nttcom/gharf)  
📝 **Description:** GHARF (GitHub Actions RedTeam Framework) applies CI/CD principles to red team operations, enabling automated attack scenario development, tool preparation, and execution environment provisioning through GitHub Actions workflows. It reduces the time and effort required to conduct frequent, high-quality red team exercises.

</details>

<details><summary><strong>Ghosts in the DOM: Hunting and Exploiting Hidden postMessage Listeners Using FrogPost Extension</strong> — Lidor Ben Shitrit, Assaf Levkovich</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/thisis0xczar/FrogPost](https://github.com/thisis0xczar/FrogPost)  
📝 **Description:** FrogPost is a browser extension for advanced postMessage security analysis. It dynamically discovers event handlers and performs AST-based static analysis to track data taint, identify common sinks (like eval or innerHTML), and crucially, extract the conditional logic (e.g., if (event.data.type === 'chat')) that guards these sinks.

</details>

<details><summary><strong>Golden dMSA: One Key to Rule Them All</strong> — Adi Malyanker</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Semperis/GoldenDMSA](https://github.com/Semperis/GoldenDMSA)  
📝 **Description:** Golden dMSA is a post-exploitation tool that exploits vulnerabilities in Active Directory Managed Service Accounts to escalate privileges across an entire forest. By compromising a single domain, it obtains Kerberos tickets and derives passwords for all dMSAs and gMSAs, bypassing security restrictions that normally prevent non-privileged users from enumerating these protected accounts.

</details>

<details><summary><strong>IOCTL-hammer - Parameter centric IOCTL Fuzzer for Windows Drivers</strong> — Mohit Kulamkolly, Mohanraj Ravichandran</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/netskopeoss/ioctlhammer](https://github.com/netskopeoss/ioctlhammer)  
📝 **Description:** IOCTL-hammer is a lightweight, Python-based fuzzing harness designed for efficient and targeted security auditing of Windows driver IOCTL interfaces. This tool addresses the high barrier to entry for kernel driver testing by providing a simple, accessible framework that focuses on the most common vulnerability patterns: buffer mismanagement. Rather than relying on complex, coverage-guided instrumentation, ioctl-hammer adopts a parameter-centric methodology, systematically manipulating the four core user-mode buffer descriptors sent via DeviceIoControl.

</details>

<details><summary><strong>Keep COM and Hijack On: Redefining Windows Session Hijacking</strong> — Andrew Oliveau</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/3lp4tr0n/SessionHop](https://github.com/3lp4tr0n/SessionHop)  
📝 **Description:** SessionHop is a red team tool that exploits Windows COM (Component Object Model) objects for credential theft and session hijacking. It leverages underexplored COM abuse techniques to perform cross-session attacks, enabling lateral movement and privilege escalation through Windows COM infrastructure.

</details>

<details><summary><strong>PowerPwn Uncovered: Advanced Agentic Recon & Exploitation</strong> — Avishai Efrat</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/mbrg/power-pwn](https://github.com/mbrg/power-pwn)  
📝 **Description:** PowerPwn is an offensive and defensive security toolset for Microsoft 365 Power Platform and Copilot AI services. It supports reconnaissance, privilege escalation, data exfiltration, and backdoor persistence across Power Apps, Power Automate, and Copilot Studio, enabling red teams to assess M365 low-code/no-code attack surfaces.

</details>

<details><summary><strong>ReForge: Where Crashes Become Weapons</strong> — Sohan Simha Prabhakar, Samarth Bhaskar Bhat, Abinav Harsha, Danindu Gammanpilage</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/danindu/ReForge](https://github.com/danindu/ReForge)  
📝 **Description:** ReForge is an AI-powered pipeline that takes binary crash artefacts from AFL++ and automatically forges them into working proof-of-concept exploits; complete with human-readable analysis reports. Under the hood, it integrates a multi-agent system: a cloud-based LLM generates the exploit, a local custom-AI model explains it, and a lightweight coordinator (MCP) manages validation and retry logic. Each exploit is auto-tested against an un-instrumented target binary before being stored with metadata and analysis, making the results immediately actionable.

</details>

<details><summary><strong>ROP ROCKET: Advanced ROP Automation for Exploitation</strong> — Bramwell Brizendine</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Bw3ll/ROP_ROCKET](https://github.com/Bw3ll/ROP_ROCKET)  
📝 **Description:** ROP ROCKET is an advanced Return-Oriented Programming (ROP) automation tool that generates complete ROP exploit chains. It features novel techniques including x86/x64 Heaven's Gate invocation via ROP, direct Windows syscall chains (NtAllocateVirtualMemory, NtProtectVirtualMemory) to bypass DEP without Windows API calls, and multi-API chaining as an alternative to traditional shellcode.

</details>

<details><summary><strong>SAMLSmith</strong> — Eric Woodruff, Tomer Nahum</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Semperis/SAMLSmith](https://github.com/Semperis/SAMLSmith)  
📝 **Description:** SAMLSmith is the go-to tool for penetrating SAML applications with response forging. An evolution of the original tooling developed for proof-of-concept of SAML response forging in Entra ID, SAMLSmith takes further research around SAML response forging and combines it into a tool crafted for offensive scenarios.

</details>

<details><summary><strong>Virga: Local LLM Embedded C2 Framework</strong> — Jun Miura, SHUNRI Kudo</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/r74tech/virga](https://github.com/r74tech/virga)  
📝 **Description:** Virga is a new cross-platform command & control (C2) framework powered by a local large language model (LLM). This framework can generate a beacon implant with an embedded LLM, and perform autonomous post-exploitation actions on a target system. In other words, the embedded LLM model autonomously generates and executes the appropriate command based on the situation. Additionally, each beacon has an in-memory database (MemDB) in which the command results are saved in order to improve subsequent actions.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Breaking the Tunnel: Real-Time API Interception in MDM-Locked Mobile Apps with KnoxSpy</strong> — Subho Halder</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/appknox/knoxspy](https://github.com/appknox/knoxspy)  
📝 **Description:** KnoxSpy is a real-time API interception tool for MDM-locked mobile applications. It bypasses the VPN tunnel enforcement that renders conventional proxies ineffective, enabling security professionals to intercept, inspect, and test API traffic from MDM-managed apps that would otherwise be inaccessible to standard interception techniques.

</details>

<details><summary><strong>CVE2CAPEC - Convert CVEs to MITRE ATT&CK</strong> — Maxime ALAY-EDDINE, Romain Loisel</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Galeax/CVE2CAPEC](https://github.com/Galeax/CVE2CAPEC)  
📝 **Description:** CVE2CAPEC is a free and open source MITRE ATT&CK Navigator generator. Give it a list of CVEs, and it computes automatically all CWEs, CAPECs and MITRE ATT&CK Techniques to draw the appropriate MITRE ATT&CK matrix.

</details>

<details><summary><strong>DICE: Device Identification and Classification Engine</strong> — Ricardo Yaben, Emmanouil Vasilomanolakis</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/RicYaben/dice](https://github.com/RicYaben/dice)  
📝 **Description:** DICE (Device Identification and Classification Engine) is a network scanning and fingerprinting tool that identifies and classifies Internet-connected devices. It analyzes network traffic patterns and device characteristics to map IoT and embedded devices across networks, helping security teams assess and manage their device attack surface.

</details>

<details><summary><strong>EKSi Lite: Simple lightweight EKS Cluster Listing & Security Tool</strong> — Anjali Shukla, Divyanshu Shukla</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/peachycloudsecurity/EKSi-lite](https://github.com/peachycloudsecurity/EKSi-lite)  
📝 **Description:** EKSi is a lightweight command line python tool designed for quick enumeration and listing of Kubernetes resources within Amazon EKS context, showing the relationships between AWS services and Kubernetes components during internal security audits. During internal security reviews and operational assessments, security professionals often need to quickly gather information about EKS cluster components without navigating through the AWS console or multiple kubectl commands. EKSi solves this problem by providing a cli for extracting and listing components within EKS and Kubernetes context.

</details>

<details><summary><strong>Kubernetes Goat - A Hands-on Interactive Kubernetes Security Playground</strong> — Madhu Akula</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/madhuakula/kubernetes-goat](https://github.com/madhuakula/kubernetes-goat)  
📝 **Description:** Kubernetes Goat is an intentionally vulnerable Kubernetes cluster environment designed for hands-on security learning. It contains real-world misconfiguration scenarios, vulnerable workloads, and attack simulations that teach practitioners how to exploit and secure Kubernetes clusters and container deployments.

</details>

<details><summary><strong>LLMMobile v2 - Smart Vulnerability Scanner for Mobile Apps</strong> — Pinar Sadioglu, Musa Şana</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection](https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection)  
📝 **Description:** This tool provides a unified solution for mobile app security analysis, supporting both static inspection for Android and iOS apps and dynamic runtime analysis for Android applications. It enhances testing depth through autonomous exploration agents that simulate real user interactions, uncovering hidden risks that traditional methods might miss. An AI-based reasoning layer further improves accuracy by reducing false positives and contextualizing vulnerabilities. Designed for scalability and usability, the tool features a centralized dashboard and integrates smoothly into existing development pipelines.

</details>

<details><summary><strong>MBPTL - Most Basic Penetration Testing Lab</strong> — Bayu Fedra Abdullah</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/bayufedra/MBPTL](https://github.com/bayufedra/MBPTL)  
📝 **Description:** MBPTL (Most Basic Penetration Testing Lab) is an open-source training platform providing a comprehensive hands-on environment for learning the five essential phases of penetration testing: Reconnaissance, Vulnerability Analysis, Exploitation, Password Cracking, and Post-Exploitation. It goes beyond application-only labs like DVWA by covering the full pentest lifecycle.

</details>

<details><summary><strong>Nightingale: Docker for Pentesters</strong> — Raja Nagori</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/RAJANAGORI/Nightingale](https://github.com/RAJANAGORI/Nightingale)  
📝 **Description:** Nightingale is a Docker-based penetration testing environment that provides a pre-configured, consistent, and repeatable setup with all essential pentesting tools. It eliminates complex manual installations by packaging security assessment tools into resource-efficient Docker containers ready for immediate use.

</details>

<details><summary><strong>OWASP EKS Goat: Hands-On AWS EKS Security</strong> — Anjali Shukla, Divyanshu Shukla</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/OWASP/www-project-eks-goat](https://github.com/OWASP/www-project-eks-goat)  
📝 **Description:** OWASP EKS Goat is an open source, intentionally vulnerable AWS EKS cluster designed for hands on security testing and learning. It provides a realistic vulnerable environment to explore supply chain vulnerabilities that can lead to the compromise of AWS Cloud resources, including EKS and ECR, through cloud & RBAC misconfigurations.

</details>

<details><summary><strong>Raising BloodHound Attack Paths to Life</strong> — Beyviel David</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/SpecterOps/BloodHound](https://github.com/SpecterOps/BloodHound)  
📝 **Description:** BloodHound is an Active Directory and Azure attack path analysis tool that uses graph theory to reveal hidden relationships and privilege escalation paths in AD environments. It maps users, groups, computers, ACLs, and delegated permissions to identify exploitable chains that attackers can traverse to reach high-value targets.

</details>

<details><summary><strong>SBoM Play</strong> — Anant Shrivastava</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/cyfinoid/sbomplay](https://github.com/cyfinoid/sbomplay)  
📝 **Description:** SBOMPlay is a browser-first, privacy-aware SBOM visualization and enrichment tool designed to showcase the real potential of SBOMs beyond just vulnerability tracking.

</details>

<details><summary><strong>SupplyShield: Protecting Your Software Supply Chain</strong> — Rahul Sunder, Yadhu Krishna, Hritik Vijay, Sourav Kumar</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/supplyshield/supplyshield](https://github.com/supplyshield/supplyshield)  
📝 **Description:** SupplyShield is a robust security framework designed to protect against complex software supply chain attacks. It helps organizations seamlessly integrate supply chain security into their Software Development Lifecycle (SDLC), addressing the challenges of managing hundreds of microservices and thousands of daily builds. SupplyShield focuses on generating a Software Bill of Materials (SBOM) and performing Software Composition Analysis (SCA) for microservices.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Atomic Honeypot - A Tool That Can Hack Back the Attackers Who Are Trying to Connect to Your Database</strong> — Dan Gardner, Martin Rakhmanov, Alexander Rubin</summary>

**Track:** Malware Defense · **Event:** Europe 2025  
🔗 **Link:** Not Available  
📝 **Description:** Atomic Honeypot is an active defense tool that exploits vulnerabilities in MySQL and PostgreSQL client libraries to counter-attack adversaries attempting to compromise your databases. It leverages CVEs in database backup tools (mysqldump, pg_dump, pg_restore) to turn the tables on attackers, supporting both MySQL and PostgreSQL deception scenarios.

</details>

<details><summary><strong>CQURE Automatic Destinations Toolkit: Forensics, AppID Analysis & Jump List Reverse Engineering</strong> — Paula Januszkiewicz</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/CQURE](https://github.com/CQURE)  
📝 **Description:** The CQURE Automatic Destinations Toolkit is a forensic and research-grade collection of tools designed to analyze and interpret Windows Automatic Destinations (*. automaticDestinations-ms) files — a rich but underutilized source of timeline and user activity data. These binary files, associated with Jump Lists, contain detailed historical evidence of user interaction with applications and files. The tools are used internally by the CQURE Team in advanced forensics and have been developed based on real-world investigations requiring deep binary parsing and timeline construction from partially overwritten storage devices.

</details>

<details><summary><strong>DNSBomb Toolkit: Evaluating New Powerful-Ever Pulsing DoS Attacks</strong> — Xiang Li, Yuqi Qiu</summary>

**Track:** Network Defense · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/idealeer/dnsbomb.github.io](https://github.com/idealeer/dnsbomb.github.io)  
📝 **Description:** DNSBomb Toolkit is the first public toolset for evaluating, reproducing, and defending against a new class of pulsing DoS attacks that exploit widely deployed DNS mechanisms. Based on our IEEE S&P 2024 paper, the toolkit enables controlled experiments of DNS query accumulation, amplification, and pulsing via timeout abuse, query aggregation, and fast-returning mechanisms. We provide both attack simulation and detection modules to empower researchers, vendors, and defenders to test and patch vulnerable DNS software or configurations. DNSBomb Toolkit has already contributed to over 10 CVE disclosures and security patches across major DNS vendors, including BIND, Unbound, PowerDNS, and Knot.

</details>

<details><summary><strong>Pygraphistry</strong> — Sindre Breda, Leo Meyerovich</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/graphistry/pygraphistry](https://github.com/graphistry/pygraphistry)  
📝 **Description:** PyGraphistry is a GPU-accelerated Python library that makes it easy to analyze and visualize large-scale graphs—ideal for uncovering complex patterns in cybersecurity, threat hunting, and fraud detection. It combines rich interactive visualizations with dataframe-native graph querying, ML workflows, and seamless integration into existing Python, web, and notebook environments. With support for tools like Pandas, cuDF, and NetworkX, PyGraphistry helps security professionals go from raw data to insight faster—without needing deep expertise in graph theory or infrastructure.

</details>

<details><summary><strong>The Only 'Kanvas' You Need When Responding to Security Incidents</strong> — Jinto Antony</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/WithSecureOpenSource/Kanvas](https://github.com/WithSecureOpenSource/Kanvas)  
📝 **Description:** KANVAS is an open-source IR (Incident Response) case management tool with an intuitive desktop interface, built using Python. It provides a unified workspace for investigators working with SOD (Spreadsheet of Doom) or similar spreadsheets, enabling key workflows to be completed without switching between multiple applications. Kanvas supports many external lookups, making it easier to add context during investigations.

</details>

<details><summary><strong>TSURUGI LINUX: The Sharpest Weapon in Your DFIR Arsenal</strong> — Giovanni Rattaro, Marco GIorgi</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/project-tsurugi/tsurugidb](https://github.com/project-tsurugi/tsurugidb)  
📝 **Description:** Tsurugi Linux is a purpose-built DFIR (Digital Forensics and Incident Response) Linux distribution pre-loaded with hundreds of forensic analysis, incident response, and malware analysis tools. It provides a ready-to-use investigation platform for evidence acquisition, timeline analysis, memory forensics, and network forensics.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>EMFIF2 - Electro Magnetic Fault Injection Fuzzing Framework</strong> — Luca Bongiorni, Andrea Bissoli</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2025  
🔗 **Link:** Not Available  
📝 **Description:** EMFIF2 (Electro Magnetic Fault Injection Fuzzing Framework) automates hardware fault injection attacks using CNC-positioned electromagnetic pulse (EMP) generators. It provides a modular, scriptable approach to fuzzing embedded systems through targeted EM glitching, enabling researchers to discover hardware vulnerabilities with minimal manual intervention and observe device fault responses in real-time.

</details>

<details><summary><strong>PwnPad: A Hardware Hacking Learning Platform</strong> — Georgios Roumeliotis</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/twelvesec/PwnPad](https://github.com/twelvesec/PwnPad)  
📝 **Description:** PwnPad is an open-source hardware training platform designed to teach embedded security through hands-on experimentation. Built to be affordable and fully reproducible, PwnPad enables users to learn real-world exploitation techniques using common protocols like UART, I2C, and SPI, along with fault injection and side-channel attacks.

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>A.I.G（AI-Infra-Guard）</strong> — Wu Huiyu, Cheng Huangsheng, Zheng Xing</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)  
📝 **Description:** A.I.G（AI-Infra-Guard） is an open-source security assessment tool designed to identify and mitigate vulnerabilities in AI infrastructure. It provides comprehensive scanning capabilities for AI models, data pipelines, and deployment environments, ensuring robust security measures are in place to protect against potential threats.

</details>

<details><summary><strong>From Triage to Threat Modeling: Open-Source Security LLM in Action</strong> — Dhruv Kedia, Sajana Weerawardhena</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/yacwagh/arrows](https://github.com/yacwagh/arrows)  
📝 **Description:** Arrows is an open-source, instruction-tuned Large Language Model (LLM) purpose-built for security workflows. It assists with SOC alert triage, threat modeling, and offensive security tasks, providing an AI assistant specifically trained on cybersecurity knowledge to reduce manual analysis overhead.

</details>

<details><summary><strong>MIPSEval: Multi-turn LLM Evaluation of LLM Safety</strong> — Muris Sladić, Sebastian Garcia</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/stratosphereips/MIPSEval](https://github.com/stratosphereips/MIPSEval)  
📝 **Description:** MIPSEval is an automated multi-turn LLM safety evaluation framework that tests language models against jailbreaking, prompt injection, and guardrail bypass techniques. It enables continuous, repeatable safety assessments of both base models and LLM-powered applications, providing quick and precise evaluation after any model or system prompt changes.

</details>

<details><summary><strong>Patch Wednesday - Multi-Agent System for Patch Diffing</strong> — Maor Dahan</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/T-RN-R/PatchDiffWednesday](https://github.com/T-RN-R/PatchDiffWednesday)  
📝 **Description:** PatchDiffWednesday is an AI-driven multi-agent framework that automates Microsoft Patch Tuesday analysis. It ingests KB metadata, performs binary patch diffing for each CVE, and generates end-to-end root-cause analysis reports, automating the most time-consuming steps of monthly patch triage.

</details>

<details><summary><strong>Red AI Range (RAR)</strong> — Mahmut Erdem Özgen, Ata Seren, Elif Başar Özgen, Ömer Kutay Atilla</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ErdemOzgen/RedAiRange](https://github.com/ErdemOzgen/RedAiRange)  
📝 **Description:** Red AI Range (RAR) is a comprehensive security platform designed specifically for AI red teaming and vulnerability assessment. It creates realistic environments where security professionals can systematically discover, analyze, and mitigate AI vulnerabilities through controlled testing scenarios.

</details>

<details><summary><strong>Spikee: Simple Prompt Injection Kit for Evaluation and Exploitation</strong> — Donato Capitella</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ReversecLabs/spikee](https://github.com/ReversecLabs/spikee)  
📝 **Description:** Spikee is an open-source prompt injection testing toolkit for evaluating and exploiting LLM application security risks. Built from two years of real-world GenAI security assessments, it focuses on practical attack outcomes—data exfiltration, XSS, resource exhaustion—arising from the interaction between LLMs and their host applications, rather than typical content-generation harms.

</details>

<details><summary><strong>SQL Data Guard: Enforcing Safe LLM-to-Database Interactions via Inline or MCP Deployment</strong> — Ori Nakar, Sofia Naer, Muly Levy</summary>

**Track:** AI, ML & Data Science · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/ThalesGroup/sql-data-guard](https://github.com/ThalesGroup/sql-data-guard)  
📝 **Description:** SQL Data Guard, introduced at Black Hat Asia 2025, protects against insecure SQL by validating and rewriting queries to enforce access restrictions and block injection payloads. As LLMs increasingly generate SQL dynamically, we extend sql-data-guard with a containerized application that secures MCP-based systems. It intercepts queries, applies schema-aware policies, and ensures only safe, compliant SQL reaches internal database services—adding a crucial protection layer for AI-driven environments.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>NeitherScan: Mass Scanner for a Potential Vulnerability in Windows Kernel Drivers</strong> — Kotaro Osugi, Jun Miura</summary>

**Track:** Reverse Engineering · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/DisAsterGroup/NeitherScan](https://github.com/DisAsterGroup/NeitherScan)  
📝 **Description:** NeitherScan is a mass scanner for identifying Windows kernel drivers that use the METHOD_NEITHER I/O control flag, which allows user-space applications to pass arbitrary buffers directly to kernel space. This flag is a known indicator for CWE-781 (Improper Address Validation in IOCTL with METHOD_NEITHER), enabling rapid discovery of potentially vulnerable drivers at scale.

</details>

<details><summary><strong>Tanto 2.0</strong> — Kyle Martin</summary>

**Track:** Reverse Engineering · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Vector35/tanto](https://github.com/Vector35/tanto)  
📝 **Description:** Tanto 2.0: an open-source, binary analysis, slicing framework and plugin for Binary Ninja designed to help discover and verify bugs and vulnerabilities faster than ever before. As government-funded programs and private-sector research continue to encounter increasingly complex problems that require more data and context to solve, slicing aims to cut those problems back down to size.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>AnonyMask: Automated Masking and Unmasking of Explicit and Implicit Privacy Data</strong> — Yohan Muliono, Cecilia Audrey Herli, Vincent Kartamulya Santoso, Nadya Clarine Purba</summary>

**Track:** Human Factors · **Event:** Europe 2025  
🔗 **Link:** [https://github.com/Caudrey/AnonyMask](https://github.com/Caudrey/AnonyMask)  
📝 **Description:** AnonyMask is a privacy-preserving tool designed to automatically detect, mask, and unmask privacy data across various file formats. It allows enterprises to leverage the power of Large Language Model (LLM) or Retrieval-Augmented Generation (RAG) while ensuring that private or confidential information remains secure and compliant. With a single click, users can anonymize both explicit and implicit privacy data before sending it to LLM or RAG for analysis—and restore the original content afterward using smart unmasking. AnonyMask offers a secure, customizable, and offline-capable privacy-preserving document compatible with common file types such as .pdf, .docx, .xlsx, .csv, and .txt.

</details>

---
