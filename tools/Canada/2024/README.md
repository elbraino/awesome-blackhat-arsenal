# Canada 2024
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2024** event held in **Canada**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming)
- [🔴 Red Teaming](#-red-teaming)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec)
- [🔵 Blue Team & Detection](#-blue-team--detection)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded)
- [🤖 AI, ML & Data Science](#-ai-ml--data-science)
- [🧠 Reverse Engineering](#-reverse-engineering)
---
## ☁️ Cloud Security
<details><summary><strong>DetentionDodger: Finding Rusted Links on the Chains of Fate</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Bleon Proko](https://img.shields.io/badge/Bleon%20Proko-informational)

🔗 **Link:** [DetentionDodger: Finding Rusted Links on the Chains of Fate](https://github.com/permiso-io-tools/detentiondodger)  
📝 **Description:** A security assessment tool that identifies AWS IAM users whose credentials have been compromised by searching for users with quarantine policies and analyzing their permissions against known attack scenarios.

</details>

<details><summary><strong>Zentaris Attack Path Risk Categorization Using Hypergraphs</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Sai Sitharaman](https://img.shields.io/badge/Sai%20Sitharaman-informational)

🔗 **Link:** [Zentaris Attack Path Risk Categorization Using Hypergraphs](https://github.com/zetafence)  
📝 **Description:** A cloud security tool from Zetafence that analyzes and categorizes attack paths in cloud environments using hypergraph-based risk assessment to identify and prioritize security vulnerabilities.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Wargame</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational)

🔗 **Link:** [AI Wargame](https://play.secdim.com/)  
📝 **Description:** An AI wargame framework built around the OpenAI Gym API that enables reinforcement learning research by allowing developers to create and train intelligent agents that compete in a strategic battle environment.

</details>

<details><summary><strong>Hands-on RF Hacking: Your Table is (always) Ready</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Paul Clark](https://img.shields.io/badge/Paul%20Clark-informational)

🔗 **Link:** [Hands-on RF Hacking: Your Table is (always) Ready](https://github.com/busydadsec/cyber-labs)  
📝 **Description:** A collection of hands-on cybersecurity labs focused on RF hacking, Wi-Fi exploitation, SDR (HackRF), mobile forensics, and Android app testing conducted in isolated lab environments for educational purposes.

</details>

<details><summary><strong>Remediate Cloud Security Threats Automatically in Real-Time with Falco and Event Driven Ansible</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Marat Salakhutdinov](https://img.shields.io/badge/Marat%20Salakhutdinov-informational) ![Aleksandr Varlamov](https://img.shields.io/badge/Aleksandr%20Varlamov-informational)

🔗 **Link:** [Remediate Cloud Security Threats Automatically in Real-Time with Falco and Event Driven Ansible](https://github.com/falcosecurity/falco)  
📝 **Description:** A cloud-native runtime security tool for Linux that monitors kernel events like syscalls and alerts on abnormal behavior in real-time, with support for container and Kubernetes metadata enrichment.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Surfactant - Modular Framework for File Information Extraction and SBOM Generation</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational)

🔗 **Link:** [Surfactant - Modular Framework for File Information Extraction and SBOM Generation](https://github.com/llnl/Surfactant)  
📝 **Description:** Surfactant is a modular framework for extracting information from filesystems, primarily for generating an SBOM (Software Bill of Materials). The information extracted can then be used to identify the various vendors or libraries associated with a file, and establish relationships between files. The resulting SBOM can be used for system level impact analysis (such as for IoT, Smart Grid, or ICS devices) of vulnerabilities, and the information gathered can be used to help inform what files to focus on for manual analysis. Several recently added features will be demonstrated, including functionality for helping visualize the contents of a file system and the relationships between files. The initial results from integrating new methods to identify the package that files (compiled binaries or scripts) belong to will also be discussed.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>CODASM: Hiding Payloads in Plain .text</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Moritz Thomas](https://img.shields.io/badge/Moritz%20Thomas-informational)

🔗 **Link:** [CODASM: Hiding Payloads in Plain .text](https://github.com/NVISOsecurity/codasm)  
📝 **Description:** Sometimes we just can't afford the luxury of staging our C2 payloads but need to bring them along as part of the initial payload we deliver. This can become quite the challenge as modern AVs and EDRs feature some pretty sophisticated static and dynamic analysis strategies. One strategy, detection of high file entropy, proved to be an unexpected but annoying challenge we needed to overcome during an assessment. The specific EDR we faced just wouldn't let our binaries pass - so we went to find a solution. This tool implements an approach to decrease a payload's entropy while increasing its size.

</details>

<details><summary><strong>Cyber Arsenal47</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Simardeep Singh](https://img.shields.io/badge/Simardeep%20Singh-informational)

🔗 **Link:** [Cyber Arsenal47](https://github.com/tombstoneghost/cyber-arsenal47)  
📝 **Description:** Our project presents an innovative security suite engineered to revolutionize the landscape of security assessments. Developed primarily in GoLang, our toolkit boasts a comprehensive suite of modules crafted for various security assessment scenarios. Python serves as the orchestrator, seamlessly interfacing with the GoLang modules, thereby establishing a robust bridge between the user interface and the underlying functionality. This tool empowers users with automated scanning capabilities, streamlining the process of identifying vulnerabilities across systems and networks. Through the combination of Python's versatility and GoLang's performance, our solution provides an efficient and effective means of conducting security assessments, catering to the evolving demands of cybersecurity professionals. In summary, our Synergetic Security Suite represents a paradigm shift in security assessment methodologies, offering unparalleled efficiency and effectiveness through its fusion of Python and GoLang technologies.

</details>

<details><summary><strong>DarkWidow: Customizable Dropper Tool Targeting Windows</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Soumyanil Biswas](https://img.shields.io/badge/Soumyanil%20Biswas-informational)

🔗 **Link:** [DarkWidow: Customizable Dropper Tool Targeting Windows](https://github.com/reveng007/DarkWidow)  
📝 **Description:** This is a Customizable Dropper Tool targeting Windows machine.

</details>

<details><summary><strong>KnowsMore</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Helvio Junior](https://img.shields.io/badge/Helvio%20Junior-informational)

🔗 **Link:** [KnowsMore](https://github.com/helviojunior/knowsmore)  
📝 **Description:** KnowsMore is a swiss army knife tool for pentesting Microsoft Active Directory (NTLM Hashes, BloodHound, NTDS and DCSync)

</details>

<details><summary><strong>Living off the O365 land with powerpwn</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Bargury](https://img.shields.io/badge/Michael%20Bargury-informational) ![Avishai Efrat](https://img.shields.io/badge/Avishai%20Efrat-informational)

🔗 **Link:** [Living off the O365 land with powerpwn](https://github.com/mbrg/power-pwn)  
📝 **Description:** An offensive and defensive security toolset for Microsoft 365 Power Platform that provides modules for tenant scanning, Copilot security testing, discovering misconfigured bots, and identifying data exposure risks.

</details>

<details><summary><strong>Mythic</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Cody Thomas](https://img.shields.io/badge/Cody%20Thomas-informational)

🔗 **Link:** [Mythic](https://github.com/its-a-feature/Mythic)  
📝 **Description:** A cross-platform, post-exploit red teaming framework built with GoLang and Docker that provides a collaborative web UI for operators and managers to conduct authorized security assessments.

</details>

<details><summary><strong>Nebula - 3 years of kicking *aaS and taking usernames</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Bleon Proko](https://img.shields.io/badge/Bleon%20Proko-informational)

🔗 **Link:** [Nebula - 3 years of kicking *aaS and taking usernames](https://github.com/CyberDataLab/nebula)  
📝 **Description:** A platform for training federated learning models within both centralized and decentralized architectures, enabling privacy-preserving collaborative machine learning across distributed devices without requiring a central server.

</details>

<details><summary><strong>PyRDP: Remote Desktop Protocol Interception</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Olivier Bilodeau](https://img.shields.io/badge/Olivier%20Bilodeau-informational) ![Andréanne Bergeron](https://img.shields.io/badge/Andréanne%20Bergeron-informational)

🔗 **Link:** [PyRDP: Remote Desktop Protocol Interception](https://github.com/gosecure/pyrdp)  
📝 **Description:** A Python-based RDP man-in-the-middle tool that intercepts Remote Desktop Protocol connections to capture credentials, monitor user activity, record sessions, and extract files transferred over RDP.

</details>

<details><summary><strong>ShellSilo</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Tarek Ahmed](https://img.shields.io/badge/Tarek%20Ahmed-informational)

🔗 **Link:** [ShellSilo](https://github.com/nixpal/shellsilo)  
📝 **Description:** A Python-based utility that converts C syntax code into syscall assembly language and corresponding shellcode, streamlining the process of constructing structures, assigning variables, and making system calls for x64 Windows.

</details>

<details><summary><strong>Silver SAML Forger: Tooling to craft forged SAML responses from Entra ID</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Eric Woodruff](https://img.shields.io/badge/Eric%20Woodruff-informational) ![Tomer Nahum](https://img.shields.io/badge/Tomer%20Nahum-informational)

🔗 **Link:** [Silver SAML Forger: Tooling to craft forged SAML responses from Entra ID](https://github.com/semperis/silversamlforger)  
📝 **Description:** Silver SAML Forger is a tool developed to PoC SAML response forging, also known as Silver SAML and Golden SAML attacks, against applications federated to Entra ID for authentication using the SAML standard. The tool goes along with research into the vulnerabilities that can present in cloud identity providers, such as Entra ID, where if an attacker has access to the private key material Entra ID uses for SAML response signing, that the target applications may be susceptible to these forging attacks. While Entra ID protects the private key if generated internally, as it cannot be exported, in the real-world organizations follow bad habits that may leave sensitive private key material available to an attacker. These sorts of habits have been observed by the research team that developed the Silver SAML Forger. Using this tool in combination with tools such as Burp Suite, you can demonstrate forging access to a target application. If the application supports certain types of SAML integrations, the identity provider will have no visibility into the authentication – you could think of these attacks as Kerberos Golden-ticket type attacks. The tool requires the signing certificate to use, the username that is target for impersonation, and some basic federation information about the target application that can be derived from a few different methods.

</details>

<details><summary><strong>Volatile Vault: Data Exfiltration in 2024</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Patrick Eisenschmidt](https://img.shields.io/badge/Patrick%20Eisenschmidt-informational) ![Moritz Thomas](https://img.shields.io/badge/Moritz%20Thomas-informational)

🔗 **Link:** [Volatile Vault: Data Exfiltration in 2024](https://github.com/molatho/volatilevault)  
📝 **Description:** A secure data exfiltration platform for red team operators that encrypts all data in the browser using AES-GCM, stores files temporarily with automatic deletion, and features a plugin system supporting various storage and transport mechanisms.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Blackdagger</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Mahmut Erdem Ozgen](https://img.shields.io/badge/Mahmut%20Erdem%20Ozgen-informational) ![Ata Seren](https://img.shields.io/badge/Ata%20Seren-informational) ![Regaip Kurt](https://img.shields.io/badge/Regaip%20Kurt-informational)

🔗 **Link:** [Blackdagger](https://github.com/ErdemOzgen/blackdagger)  
📝 **Description:** Blackdagger is a cutting-edge automation tool designed for orchestrating complex workflows across DevOps, DevSecOps, MLOps, MLSecOps, and Continuous Automated Red Teaming (CART) environments. Utilizing a declarative YAML format, it allows for the definition of automation pipelines using a Directed Acyclic Graph (DAG), simplifying the management and execution of intricate workflows. With a focus on ease of use and versatility, Blackdagger features a built-in Web UI for managing, rerunning, and monitoring automation pipelines, alongside native Docker support for seamless integration within containerized environments. https://github.com/ErdemOzgen/blackdagger https://blackdagger.readthedocs.io/en/latest/

</details>

<details><summary><strong>CloudPrivs</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Connor MacLeod](https://img.shields.io/badge/Connor%20MacLeod-informational)

🔗 **Link:** [CloudPrivs](https://github.com/AbstractClass/CloudPrivs)  
📝 **Description:** CloudPrivs is a tool to help you determine exactly what privileges are associated with a given set of cloud credentials. What makes CloudPrivs different that other similar tools is that it directly interrogates the cloud provider SDK to generate test cases, ensuring maximal coverage even when new cloud services are added. CloudPrivs also supports a robust plugin system making it simple to dynamically modify the generated test cases or insert custom tests.

</details>

<details><summary><strong>CVE Half-Day Watcher: Hunting Down Vulnerabilities Before the Patch Drops</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Yakir Kadkoda](https://img.shields.io/badge/Yakir%20Kadkoda-informational) ![Mor Weinberger](https://img.shields.io/badge/Mor%20Weinberger-informational)

🔗 **Link:** [CVE Half-Day Watcher: Hunting Down Vulnerabilities Before the Patch Drops](https://github.com/Research-Nautilus/CVE-Half-Day-Watcher)  
📝 **Description:** Defenders and attackers often simplify vulnerabilities into '0-day' or '1-day' categories, neglecting the nuanced gray areas where attackers thrive. In this session, we'll explore critical flaws we've uncovered in the open-source vulnerability disclosure process and introduce our tool to detect open-source projects that are at risk from these flaws. We'll reveal how vulnerabilities can be exploited prior to receiving patches and official announcements, posing significant risks for users. Our comprehensive analysis of GitHub (including issues, pull requests, and commit messages) and NVD metadata will illuminate vulnerabilities that don't neatly fit into the conventional '0-day' or '1-day' classifications but instead fall into 'Half-Day' or '0.75-Day' periods – moments when vulnerabilities are known but not yet fully disclosed or patched. Furthermore, we'll spotlight the techniques employed to identify these vulnerabilities, showcasing various scenarios and vulnerabilities discovered through this method. During this session, we'll introduce an open-source tool designed to detect such vulnerabilities and emphasize the window of opportunity for attackers to exploit this information and develop exploits. Our objective is to aid practitioners in identifying and mitigating issues throughout their vulnerability disclosure lifecycle.

</details>

<details><summary><strong>Graph for Understanding Artifact Composition (GUAC)</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Parth Patel](https://img.shields.io/badge/Parth%20Patel-informational)

🔗 **Link:** [Graph for Understanding Artifact Composition (GUAC)](https://github.com/guacsec/guac)  
📝 **Description:** Graph for Understanding Artifact Composition (GUAC) is an open-source dependency management and security tool that looks across all first-party, third-party, and open-source software, aggregating the software security metadata into a high-fidelity graph database to locate, store, analyze, and correlate software artifact data. The frequency of software attacks and increased use of open-source tooling have created a significant lack of confidence in the integrity and security of the software supply chain. Securing it can be a real headache when dealing with hundreds of pieces of software each with its own hundreds of dependencies and new vulnerabilities being discovered each day. GUAC responds by being the source of truth. GUAC can provide developers and security teams with a shared understanding of software knowledge gaps, compliance, and threat detection. It also is an effective tool for managing third-party risk and incident response. With GUAC, users can establish connections and compliance in their software catalog, unveil gaps in software supply chain data, and enable threat detection and response. The tool ingests and analyzes software supply chain metadata from a myriad of internal and external sources and multiple common metadata document types, including: - Software Bill of Materials (SBOMs) in both SPDX and CycloneDX formats and transforming them into data nodes and relationships, providing insights into software and dependencies - Ingesting and transforming SLSA and in-toto attestations into their constituent facts, offering crucial information about the provenance and integrity of software components - Being flexible and extensible to ingest data from local file systems, AWS S3, Google Cloud, OCI registries, and external package repositories - Embracing additional metadata and threat information from sources like the deps.dev and OSV APIs GUAC provides seamless visibility across an organization's software ecosystem, easily integrating with existing tools.

</details>

<details><summary><strong>R0fuzz: A Collaborative Fuzzer</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Season Cherian](https://img.shields.io/badge/Season%20Cherian-informational) ![Vishnu Dev T J Dev T J](https://img.shields.io/badge/Vishnu%20Dev%20T%20J%20Dev%20T%20J-informational) ![Vivek N J N J](https://img.shields.io/badge/Vivek%20N%20J%20N%20J-informational)

🔗 **Link:** [R0fuzz: A Collaborative Fuzzer](https://github.com/ashwathi8/r0fuzz)  
📝 **Description:** Industrial control systems (ICS) are critical to national infrastructure, demanding robust security measures. "R0fuzz" is a collaborative fuzzing tool tailored for ICS environments, integrating diverse strategies to uncover vulnerabilities within key industrial protocols such as Modbus, Profinet, DNP3, OPC, BACnet, etc. This innovative approach enhances ICS resilience against emerging threats, providing a comprehensive testing framework beyond traditional fuzzing methods.

</details>

<details><summary><strong>Veip_Gen</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Austin Norby](https://img.shields.io/badge/Austin%20Norby-informational)

🔗 **Link:** [Veip_Gen](https://github.com/Quantumite/veip_gen)  
📝 **Description:** Veip_Gen is a scriptable, command-line based tool for generating vulnerable programs to support teaching and learning buffer overflow vulnerabilities. The capability uses well-known vulnerable functions with a configurable amount of stack space and buffer sizes to create unique, vulnerable programs as examples for exploitation. The capability allows you to specify vulnerable functions such as strcpy, sprintf, gets, and more. In addition, the configurable stack size and buffer size introduces different amounts of stack space that needs to be overflowed to teach, or learn, about the conditions that make buffer overflows exploitable. In addition, there are currently two major types of exploitable programs that can be produced: vanilla and conditional. The vanilla buffer overflows are what you see when first learning to overwrite the EIP register and gain execution from the stack. This type is still configurable with stack and buffer sizes as well. Second, the conditional type lets you configure a condition that must be satisfied before being able to exploit the example, vulnerable program. Either, there must be a certain number of arguments present or there must be a series of bytes that must be matched in order to trigger the vulnerable code path. Reducing the barrier to entry and education for complex, cyber security topics will increase the readiness and capability of the cyber security workforce writ large and this tool will help those both teaching and learning to better understand the buffer overflow exploits with an unlimited number of examples that can be created simply from the command-line.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Automatically Map & Enrich ALL Alerts, Events & Logs with MITRE Attack Techniques</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ezzeldin Tahoun](https://img.shields.io/badge/Ezzeldin%20Tahoun-informational) ![Lynn Hamida](https://img.shields.io/badge/Lynn%20Hamida-informational) ![Nidheesh Panchal](https://img.shields.io/badge/Nidheesh%20Panchal-informational) ![Kevin Shi](https://img.shields.io/badge/Kevin%20Shi-informational)

🔗 **Link:** [Automatically Map & Enrich ALL Alerts, Events & Logs with MITRE Attack Techniques](https://github.com/Dan-Duran/mitre-attack-mapper)  
📝 **Description:** Using Natural Language Processing models, enrich any alert with its relevant attack techniques. The model detects the techniques using contextual, and situational awareness as well as its linguistic cyber expertise. In real time this model can save your operations endless hours of tagging incidents with their mitre techniques.

</details>

<details><summary><strong>AVSniper</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Helvio Junior](https://img.shields.io/badge/Helvio%20Junior-informational)

🔗 **Link:** [AVSniper](https://github.com/helviojunior/avsniper)  
📝 **Description:** A security analysis tool that identifies which specific strings in Windows executable files trigger antivirus detection by systematically extracting strings from PE files, creating modified versions, and testing them against antivirus software.

</details>

<details><summary><strong>Azure Unified Audit Log Mail Item Extractor'</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Richard Smith](https://img.shields.io/badge/Richard%20Smith-informational)

🔗 **Link:** [Azure Unified Audit Log Mail Item Extractor'](https://github.com/invictus-ir/Microsoft-Extractor-Suite)  
📝 **Description:** A PowerShell module for acquiring data from Microsoft 365 and Azure for incident response and cyber security purposes. It automates the extraction of logs, audit trails, and configuration data across Exchange Online, Entra ID, and Azure environments.

</details>

<details><summary><strong>Continuously Correlate & Contextualize ALL Alerts, Events & Logs</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ezzeldin Tahoun](https://img.shields.io/badge/Ezzeldin%20Tahoun-informational) ![Lynn Hamida](https://img.shields.io/badge/Lynn%20Hamida-informational) ![Nidheesh Panchal](https://img.shields.io/badge/Nidheesh%20Panchal-informational) ![Kevin Shi](https://img.shields.io/badge/Kevin%20Shi-informational)

🔗 **Link:** [Continuously Correlate & Contextualize ALL Alerts, Events & Logs](https://github.com/Dan-Duran/mitre-attack-mapper)  
📝 **Description:** Using correlation and clustering models, turn tons of alerts into mitre attack flows. The model finds the attack flows, using its ability to evaluate alerts temporal proximity, kill chain sequentiality, shared entities and similar attributes to other alerts of interest, among others. In real time this model can save your operations endless hours of correlating incidents and finding noteworthy attack flows, that if not detected in time would lead to breaches.

</details>

<details><summary><strong>eBPFShield: Unleashing the Power of eBPF for OS Kernel Exploitation and Security</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sagar Bhure](https://img.shields.io/badge/Sagar%20Bhure-informational)

🔗 **Link:** [eBPFShield: Unleashing the Power of eBPF for OS Kernel Exploitation and Security](https://github.com/sagarbhure/ebpfshield)  
📝 **Description:** Are you looking for an advanced tool that can help you detect and prevent sophisticated exploits on your systems? Look no further than eBPFShield. Let's take a technical look at some of the capabilities of this powerful technology: DNS monitoring feature is particularly useful for detecting DNS tunneling, a technique used by attackers to bypass network security measures. By monitoring DNS queries, eBPFShield can help detect and block these attempts before any damage is done. IP-Intelligence feature allows you to monitor outbound connections and check them against threat intelligence lists. This helps prevent command-and-control (C2) communications, a common tactic used by attackers to control compromised systems. By blocking outbound connections to known C2 destinations, eBPFShield can prevent attackers from exfiltrating sensitive data or delivering additional payloads to your system. eBPFShield Machine Learning feature, you can develop and run advanced machine learning algorithms entirely in eBPF. We demonstrate a flow-based network intrusion detection system(IDS) based on machine learning entirely in eBPF. Our solution uses a decision tree and decides for each packet whether it is malicious or not, considering the entire previous context of the network flow. eBPFShield Forensics helps address Linux security issues by analyzing system calls and kernel events to detect possible code injection into another process. It can also help identify malicious files and processes that may have been introduced to your system, allowing you to remediate any security issues quickly and effectively. During the session, we'll delve deeper into these features and demonstrate how eBPFShield can help you protect your systems against even the most advanced threats.

</details>

<details><summary><strong>Enhancing Windows Event Log Analysis with Open-Source Tools: Hayabusa and Takajo</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Fukusuke Takahashi](https://img.shields.io/badge/Fukusuke%20Takahashi-informational) ![Akira Nishikawa](https://img.shields.io/badge/Akira%20Nishikawa-informational)

🔗 **Link:** [Enhancing Windows Event Log Analysis with Open-Source Tools: Hayabusa and Takajo](https://github.com/Yamato-Security/hayabusa)  
📝 **Description:** Windows Event Log analysis is crucial for detecting security incidents and understanding system activities in forensic investigations. This session introduces two open-source tools from Yamato Security, a Japan-based security community founded by Zach Mathis. Yamato Security developed Hayabusa and Takajo to enhance the speed and accuracy of Windows Event Log analysis. Hayabusa leverages open-source Sigma rules to detect malicious activity in event logs, providing actionable insights. Takajo complements this by parsing Hayabusa's JSONL output, enabling rapid triage and analysis of key forensic artifacts, further streamlining incident response workflows. Together, these tools offer an integrated solution for Windows forensics, allowing for faster and more precise investigations. Join us to explore their features, real-world use cases, and how they enhance forensic analysis of Windows environments using Sigma rules. - https://github.com/Yamato-Security/hayabusa - https://github.com/Yamato-Security/takajo

</details>

<details><summary><strong>TCP/IP Communication without Network Attack Surfaces. (No Open Ports on External Interfaces)</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Colin Constable](https://img.shields.io/badge/Colin%20Constable-informational) ![Xavier Chathavong](https://img.shields.io/badge/Xavier%20Chathavong-informational)

🔗 **Link:** [TCP/IP Communication without Network Attack Surfaces. (No Open Ports on External Interfaces)](https://github.com/Marcokorcak/TCP-IP-Attack)  
📝 **Description:** A cybersecurity lab demonstrating TCP/IP protocol vulnerabilities including SYN flood attacks, TCP reset attacks, session hijacking, and reverse shell creation using Docker containers to simulate network environments.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>The Perfect BLEnd: Reversing a Bluetooth-Controlled Smart Blender for Better Smoothies</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational)

🔗 **Link:** [The Perfect BLEnd: Reversing a Bluetooth-Controlled Smart Blender for Better Smoothies](https://github.com/nightlark/web-bluetooth-controller)  
📝 **Description:** A template repository for generating web pages that control Bluetooth Low Energy (BLE) devices through a browser interface using the Web Bluetooth API, enabling interaction with BLE devices via Chrome, Edge, or Opera.

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>3P Data Risk Metric (3PDRM)</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Thomas Lee](https://img.shields.io/badge/Thomas%20Lee-informational)

🔗 **Link:** [3P Data Risk Metric (3PDRM)](https://github.com/mit-drl/pyrmm)  
📝 **Description:** A Python library for developing neural network models that predict risk metrics such as probability of failure for kinodynamic systems, enabling risk prediction for autonomous systems operating in complex environments.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>NopEmulator</strong></summary>

![Canada 2024](https://img.shields.io/badge/Canada%202024-purple) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Austin Norby](https://img.shields.io/badge/Austin%20Norby-informational)

🔗 **Link:** [NopEmulator](https://github.com/Quantumite/NopEmulator)  
📝 **Description:** A Ghidra script that emulates Intel x64 instructions to determine if a NOP sled is present in a binary by executing code sequences and comparing execution context before and after, useful for malware analysis and exploit detection.

</details>

---