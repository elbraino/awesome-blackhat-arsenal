# Canada 2024
---
📍 33 tools demonstrated at **Black Hat Arsenal Canada 2024**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security) (2)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (3)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (1)
- [🔴 Red Teaming](#-red-teaming) (11)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (6)
- [🔵 Blue Team & Detection](#-blue-team--detection) (7)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (1)
- [🤖 AI, ML & Data Science](#-ai-ml--data-science) (1)
- [🧠 Reverse Engineering](#-reverse-engineering) (1)
---
## ☁️ Cloud Security
<details><summary><strong>DetentionDodger: Finding Rusted Links on the Chains of Fate</strong> — Bleon Proko</summary>

**Track:** Cloud Security · Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/permiso-io-tools/detentiondodger](https://github.com/permiso-io-tools/detentiondodger)  
📝 **Description:** AWSCompromisedKeyQuarantineV2 (v3 was released during the creation of this article) is an AWS policy that attaches to identities whose credentials are leaked. It denies access to certain actions, applied by the AWS team in the event that an IAM user's credentials have been compromised or exposed publicly. AWS recently modified their public documentation to include the following: While it is not the intended use of the policy, many see it as the first line of defense for an exposed access key. In fact, we have observed several organizations preemptively assign this policy to sensitive identities to limit actions that can occur. DetentionDodger was built as a tool to automate the process of enumerating the account for users with leaked credentials and finding out their privileges and the impact they will have on the account.

</details>

<details><summary><strong>Zentaris Attack Path Risk Categorization Using Hypergraphs</strong> — Sai Sitharaman</summary>

**Track:** Cloud Security · Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/zetafence/zentaris](https://github.com/zetafence/zentaris)  
📝 **Description:** Zentaris is a Cloud-Agnostic Attack Path Risk Categorization tool that maps cloud attack paths playbooks to a comprehensive risk categorization system. The framework heavily utilizes graph semantics to effectively model and evaluate risk profiles. Such a tool can be utilized to discover and categorize risks across AWS, GCP, Azure infrastructures, as well as with Kubernetes clusters. The risk evaluation system enables enterprises to categorize those playbooks and evaluate by risk levels, providing enterprises with a contextual understanding, and threat priorities.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Wargame</strong> — Pedram Hayati</summary>

**Track:** Arsenal Lab · Web AppSec · **Event:** Canada 2024  
🔗 **Link:** [https://play.secdim.com/](https://play.secdim.com/)  
📝 **Description:** Come join a fun and educational attack and defence AI wargame. You will be given an AI chatbot. Your chatbot has a secret that should always remain a secret! Your objective is to secure your chatbot to protect its secret while attacking other players' chatbots and discovering theirs. The winner is the player whose chatbot survives the longest (king of the hill). All skill levels are welcomed, even if this is your first time seeing code, securing a chatbot, or playing in a wargame. Right at the start, there will be a briefing to show how to play in the wargame. Knowledge of the OpenAI Python SDK helps but is not a requirement. Each player has access to their chatbot source code repository where they can run, test, debug and push their changes.

</details>

<details><summary><strong>Hands-on RF Hacking: Your Table is (always) Ready</strong> — Paul Clark</summary>

**Track:** Arsenal Lab · Reverse Engineering · **Event:** Canada 2024  
🔗 **Link:** Not Available  
📝 **Description:** Hack your restaurant pager with software defined radio! You'll sniff for control signals from "the restaurant's" transmitter used to trigger other pagers. Then you'll capture a transmission and examine how it's put together. With your understanding of the payload structure, you'll then generate a modified transmission to trigger your own pager. This project will combine low-level waveform analysis with higher level scripting to get the job done.

</details>

<details><summary><strong>Remediate Cloud Security Threats Automatically in Real-Time with Falco and Event Driven Ansible</strong> — Marat Salakhutdinov, Aleksandr Varlamov</summary>

**Track:** Arsenal Lab · Data Forensics/Incident Response · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/falcosecurity/falco](https://github.com/falcosecurity/falco)  
📝 **Description:** Cloud attacks are fast. After finding an exploitable asset, malicious actors need less than 10 minutes on average to execute an attack. Although identity and access management, vulnerability management, and other preventive controls are common in cloud environments, no organization can stay safe without a threat detection and response program for addressing zero-day exploits, insider threats, and other malicious behavior. That's why Runtime Security is critical for organizations to fortify their cloud security against evolving cyber threats. Luckily we have Falco, which is an open-source runtime security tool designed to monitor, detect, and respond to abnormal behaviors in applications and containers within cloud-native environments. It provides real-time insights into system activities, allowing organizations to identify and mitigate security threats effectively. In this workshop, we will harness Falco's capabilities for runtime detection within Kubernetes and Cloud environments and combine it with the power and flexibility of Event-Driven Ansible to leverage it as a response engine to promptly address and mitigate security incidents in real time. We invite you to join us on this journey, where we will generate security events, detect them with Falco and automatically remediate them in real time with Event-Driven Ansible.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Surfactant - Modular Framework for File Information Extraction and SBOM Generation</strong> — Ryan Mast</summary>

**Track:** Code Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/llnl/Surfactant](https://github.com/llnl/Surfactant)  
📝 **Description:** Surfactant is a modular framework for extracting information from filesystems, primarily for generating an SBOM (Software Bill of Materials). The information extracted can then be used to identify the various vendors or libraries associated with a file, and establish relationships between files. The resulting SBOM can be used for system level impact analysis (such as for IoT, Smart Grid, or ICS devices) of vulnerabilities, and the information gathered can be used to help inform what files to focus on for manual analysis. Several recently added features will be demonstrated, including functionality for helping visualize the contents of a file system and the relationships between files. The initial results from integrating new methods to identify the package that files (compiled binaries or scripts) belong to will also be discussed.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>CODASM: Hiding Payloads in Plain .text</strong> — Moritz Thomas</summary>

**Track:** Malware Offense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/NVISOsecurity/codasm](https://github.com/NVISOsecurity/codasm)  
📝 **Description:** Sometimes we just can't afford the luxury of staging our C2 payloads but need to bring them along as part of the initial payload we deliver. This can become quite the challenge as modern AVs and EDRs feature some pretty sophisticated static and dynamic analysis strategies. One strategy, detection of high file entropy, proved to be an unexpected but annoying challenge we needed to overcome during an assessment. The specific EDR we faced just wouldn't let our binaries pass - so we went to find a solution. This tool implements an approach to decrease a payload's entropy while increasing its size.

</details>

<details><summary><strong>Cyber Arsenal47</strong> — Simardeep Singh</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/tombstoneghost/cyber-arsenal47](https://github.com/tombstoneghost/cyber-arsenal47)  
📝 **Description:** Our project presents an innovative security suite engineered to revolutionize the landscape of security assessments. Developed primarily in GoLang, our toolkit boasts a comprehensive suite of modules crafted for various security assessment scenarios. Python serves as the orchestrator, seamlessly interfacing with the GoLang modules, thereby establishing a robust bridge between the user interface and the underlying functionality. This tool empowers users with automated scanning capabilities, streamlining the process of identifying vulnerabilities across systems and networks. Through the combination of Python's versatility and GoLang's performance, our solution provides an efficient and effective means of conducting security assessments, catering to the evolving demands of cybersecurity professionals. In summary, our Synergetic Security Suite represents a paradigm shift in security assessment methodologies, offering unparalleled efficiency and effectiveness through its fusion of Python and GoLang technologies.

</details>

<details><summary><strong>DarkWidow: Customizable Dropper Tool Targeting Windows</strong> — Soumyanil Biswas</summary>

**Track:** Malware Offense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/reveng007/DarkWidow](https://github.com/reveng007/DarkWidow)  
📝 **Description:** This is a Customizable Dropper Tool targeting Windows machine.

</details>

<details><summary><strong>KnowsMore</strong> — Helvio Junior</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/helviojunior/knowsmore](https://github.com/helviojunior/knowsmore)  
📝 **Description:** KnowsMore is a swiss army knife tool for pentesting Microsoft Active Directory (NTLM Hashes, BloodHound, NTDS and DCSync)

</details>

<details><summary><strong>Living off the O365 land with powerpwn</strong> — Michael Bargury, Avishai Efrat</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/mbrg/power-pwn](https://github.com/mbrg/power-pwn)  
📝 **Description:** powerpwn, first introduced at blackhat last year, showcases various capabilities, from enumeration, to data exfiltration, command execution and phishing. These are all enabled by utilizing built-in capabilities within Power Platform, a low-code / no-code platform built into Office365. With the new upcoming release, powerpwn V2 allows easy unauthorized access to a broader-than-ever array of business data and services inside the Microsoft 365 ecosystem, as well as direct visibility into a variety of secrets and credentials. This is possible by scraping secrets hanging in logs or embedded in applications and without any external tools or exploits - only by capitalizing on your tenant's settings. powerpwn allows you to exploit Azure AD guest accounts, which were previously wrongly perceived as allowing restrictive access to external parties. It does so by using a series of undocumented internal APIs and common misconfigurations in Microsoft 365 which can allow data exfiltration, backdoor creation, acting upon targets for various attacks (e.g., running ransomware), and unauthorized access to sensitive business data and applications, including corporate SQL servers, Blob storages, Azure tables, and more. Red teamers can use powerpwn to conveniently maintain persistence within a Microsoft tenant using the inherent platform features, thereby ensuring continuous access to a tenant, even if their account has been disabled. It can also allow you to create, execute, and delete arbitrary commands, as well as credential harvesting & leakage to the outside world. Equally important, powerpwn V2 leverages the growing adoption of AI in business applications to demonstrate how to further attack users and extract sensitive business data through an understanding of AI mechanics, dynamic analysis and GenAI manipulation. All features are fully operational with the default Office 365 and Azure AD configuration.

</details>

<details><summary><strong>Mythic</strong> — Cody Thomas</summary>

**Track:** Exploitation and Ethical Hacking · Malware Offense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/its-a-feature/Mythic](https://github.com/its-a-feature/Mythic)  
📝 **Description:** Mythic is an open-source command and control (C2) framework for offensive and defensive assessments. It leverages Docker and a microservice architecture so that new types of agents, communications profiles, and more can be easily integrated at run time. Mythic 3.3 introduced a few new features including custom authentication schemes, command augmentation containers, and an eventing engine. This allows operators to write GitHub Action-like files and register actions to be performed on cron schedules, on new callbacks, in response to tasks finishing, and even blocking tasks that aren't opsec safe. Mythic has many open-source contributors that create their own agents and communications profiles that can be found here: https://mythicmeta.github.io/overhttps://mythicmeta.github.io/overview/view/.

</details>

<details><summary><strong>Nebula - 3 years of kicking *aaS and taking usernames</strong> — Bleon Proko</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/CyberDataLab/nebula](https://github.com/CyberDataLab/nebula)  
📝 **Description:** Nebula is a Cloud Penetration Testing framework. It is build with modules for each provider and each functionality. It covers AWS, Azure (both Graph and Management API, which includes Entra, Azure Subscription based resources and Office365) and DigitalOcean. Currently covers: - Public Reconnaissance - Phishing - Brute-force and Password Spray - Enumeration of internal resources after initial access - Lateral Movement and Privilege Escalation - Persistence Ever since I pushed the last update, the tool has changed drastically. Now you will get a teamserver based tool, with a client and server split, authentication to access the tool, user management and a MongoDB database to save the results into.

</details>

<details><summary><strong>PyRDP: Remote Desktop Protocol Interception</strong> — Olivier Bilodeau, Andréanne Bergeron</summary>

**Track:** Malware Offense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/gosecure/pyrdp](https://github.com/gosecure/pyrdp)  
📝 **Description:** PyRDP is a Remote Desktop Protocol (RDP) monster-in-the-middle (MITM) tool and library useful in intrusion testing, and protocol and malware research. Its out-of-the-box offensive capabilities can be divided into three broad categories: client-side, MITM-side and server-side. On the client-side, PyRDP can actively steal any clipboard activity, crawl mapped drives and collect all keystrokes. On the MITM-side PyRDP records everything on the wire in several formats (logs, JSON events), captures the user's hashes on-the-fly to enable hash cracking, it also allows an attacker to take control of an active session and performs a recording of the RDP session. On the server-side, on-logon PowerShell or command injection can be performed when a legitimate client connects. As a research tool, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It can replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation or to generate IOCs. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads. This tool is continuously maintained and used to gather information about adversaries. We think you should deploy it to learn more about who is after you. You'll be surprised what RDP can reveal.

</details>

<details><summary><strong>ShellSilo</strong> — Tarek Ahmed</summary>

**Track:** Exploitation and Ethical Hacking · Reverse Engineering · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/nixpal/shellsilo](https://github.com/nixpal/shellsilo)  
📝 **Description:** SHELLSILO is a cutting-edge tool that translates custom C syntax into syscall assembly and its corresponding shellcode. It streamlines the process of constructing and utilizing structures, assigning variables, and making system calls. With this tool, integrating strings into your shellcode and initializing Unicode strings has never been easier.

</details>

<details><summary><strong>Silver SAML Forger: Tooling to craft forged SAML responses from Entra ID</strong> — Eric Woodruff, Tomer Nahum</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/semperis/silversamlforger](https://github.com/semperis/silversamlforger)  
📝 **Description:** Silver SAML Forger is a tool developed to PoC SAML response forging, also known as Silver SAML and Golden SAML attacks, against applications federated to Entra ID for authentication using the SAML standard. The tool goes along with research into the vulnerabilities that can present in cloud identity providers, such as Entra ID, where if an attacker has access to the private key material Entra ID uses for SAML response signing, that the target applications may be susceptible to these forging attacks. While Entra ID protects the private key if generated internally, as it cannot be exported, in the real-world organizations follow bad habits that may leave sensitive private key material available to an attacker. These sorts of habits have been observed by the research team that developed the Silver SAML Forger. Using this tool in combination with tools such as Burp Suite, you can demonstrate forging access to a target application. If the application supports certain types of SAML integrations, the identity provider will have no visibility into the authentication – you could think of these attacks as Kerberos Golden-ticket type attacks. The tool requires the signing certificate to use, the username that is target for impersonation, and some basic federation information about the target application that can be derived from a few different methods.

</details>

<details><summary><strong>Volatile Vault: Data Exfiltration in 2024</strong> — Patrick Eisenschmidt, Moritz Thomas</summary>

**Track:** Network Attacks · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/molatho/volatilevault](https://github.com/molatho/volatilevault)  
📝 **Description:** In the dynamic realm of red team operations, selecting the right tools for data exfiltration is critical, yet comes with obstacles such as triggering Data Exfiltration Prevention (DEP) systems. We present "Volatile Vault" as a solution, a custom-built platform tailored to evade DEP detection. Our tool encrypts the data on the client-side and then provides a modular approach for uploading said data. Some of the currently implemented upload strategies are chunked HTTP uploads to multiple domain fronted endpoints (AWS) or QUIC as an alternative protocol.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Blackdagger</strong> — Mahmut Erdem Ozgen, Ata Seren, Regaip Kurt</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/ErdemOzgen/blackdagger](https://github.com/ErdemOzgen/blackdagger)  
📝 **Description:** Blackdagger is a cutting-edge automation tool designed for orchestrating complex workflows across DevOps, DevSecOps, MLOps, MLSecOps, and Continuous Automated Red Teaming (CART) environments. Utilizing a declarative YAML format, it allows for the definition of automation pipelines using a Directed Acyclic Graph (DAG), simplifying the management and execution of intricate workflows. With a focus on ease of use and versatility, Blackdagger features a built-in Web UI for managing, rerunning, and monitoring automation pipelines, alongside native Docker support for seamless integration within containerized environments. https://github.com/ErdemOzgen/blackdagger https://blackdagger.readthedocs.io/en/latest/

</details>

<details><summary><strong>CloudPrivs</strong> — Connor MacLeod</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/AbstractClass/CloudPrivs](https://github.com/AbstractClass/CloudPrivs)  
📝 **Description:** CloudPrivs is a tool to help you determine exactly what privileges are associated with a given set of cloud credentials. What makes CloudPrivs different that other similar tools is that it directly interrogates the cloud provider SDK to generate test cases, ensuring maximal coverage even when new cloud services are added. CloudPrivs also supports a robust plugin system making it simple to dynamically modify the generated test cases or insert custom tests.

</details>

<details><summary><strong>CVE Half-Day Watcher: Hunting Down Vulnerabilities Before the Patch Drops</strong> — Yakir Kadkoda, Mor Weinberger</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/Research-Nautilus/CVE-Half-Day-Watcher](https://github.com/Research-Nautilus/CVE-Half-Day-Watcher)  
📝 **Description:** Defenders and attackers often simplify vulnerabilities into '0-day' or '1-day' categories, neglecting the nuanced gray areas where attackers thrive. In this session, we'll explore critical flaws we've uncovered in the open-source vulnerability disclosure process and introduce our tool to detect open-source projects that are at risk from these flaws. We'll reveal how vulnerabilities can be exploited prior to receiving patches and official announcements, posing significant risks for users. Our comprehensive analysis of GitHub (including issues, pull requests, and commit messages) and NVD metadata will illuminate vulnerabilities that don't neatly fit into the conventional '0-day' or '1-day' classifications but instead fall into 'Half-Day' or '0.75-Day' periods – moments when vulnerabilities are known but not yet fully disclosed or patched. Furthermore, we'll spotlight the techniques employed to identify these vulnerabilities, showcasing various scenarios and vulnerabilities discovered through this method. During this session, we'll introduce an open-source tool designed to detect such vulnerabilities and emphasize the window of opportunity for attackers to exploit this information and develop exploits. Our objective is to aid practitioners in identifying and mitigating issues throughout their vulnerability disclosure lifecycle.

</details>

<details><summary><strong>Graph for Understanding Artifact Composition (GUAC)</strong> — Parth Patel</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/guacsec/guac](https://github.com/guacsec/guac)  
📝 **Description:** Graph for Understanding Artifact Composition (GUAC) is an open-source dependency management and security tool that looks across all first-party, third-party, and open-source software, aggregating the software security metadata into a high-fidelity graph database to locate, store, analyze, and correlate software artifact data. The frequency of software attacks and increased use of open-source tooling have created a significant lack of confidence in the integrity and security of the software supply chain. Securing it can be a real headache when dealing with hundreds of pieces of software each with its own hundreds of dependencies and new vulnerabilities being discovered each day. GUAC responds by being the source of truth. GUAC can provide developers and security teams with a shared understanding of software knowledge gaps, compliance, and threat detection. It also is an effective tool for managing third-party risk and incident response. With GUAC, users can establish connections and compliance in their software catalog, unveil gaps in software supply chain data, and enable threat detection and response. The tool ingests and analyzes software supply chain metadata from a myriad of internal and external sources and multiple common metadata document types, including: - Software Bill of Materials (SBOMs) in both SPDX and CycloneDX formats and transforming them into data nodes and relationships, providing insights into software and dependencies - Ingesting and transforming SLSA and in-toto attestations into their constituent facts, offering crucial information about the provenance and integrity of software components - Being flexible and extensible to ingest data from local file systems, AWS S3, Google Cloud, OCI registries, and external package repositories - Embracing additional metadata and threat information from sources like the deps.dev and OSV APIs GUAC provides seamless visibility across an organization's software ecosystem, easily integrating with existing tools.

</details>

<details><summary><strong>R0fuzz: A Collaborative Fuzzer</strong> — Season Cherian, Vishnu Dev T J Dev T J, Vivek N J N J</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/ashwathi8/r0fuzz](https://github.com/ashwathi8/r0fuzz)  
📝 **Description:** Industrial control systems (ICS) are critical to national infrastructure, demanding robust security measures. "R0fuzz" is a collaborative fuzzing tool tailored for ICS environments, integrating diverse strategies to uncover vulnerabilities within key industrial protocols such as Modbus, Profinet, DNP3, OPC, BACnet, etc. This innovative approach enhances ICS resilience against emerging threats, providing a comprehensive testing framework beyond traditional fuzzing methods.

</details>

<details><summary><strong>Veip_Gen</strong> — Austin Norby</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/Quantumite/veip_gen](https://github.com/Quantumite/veip_gen)  
📝 **Description:** Veip_Gen is a scriptable, command-line based tool for generating vulnerable programs to support teaching and learning buffer overflow vulnerabilities. The capability uses well-known vulnerable functions with a configurable amount of stack space and buffer sizes to create unique, vulnerable programs as examples for exploitation. The capability allows you to specify vulnerable functions such as strcpy, sprintf, gets, and more. In addition, the configurable stack size and buffer size introduces different amounts of stack space that needs to be overflowed to teach, or learn, about the conditions that make buffer overflows exploitable. In addition, there are currently two major types of exploitable programs that can be produced: vanilla and conditional. The vanilla buffer overflows are what you see when first learning to overwrite the EIP register and gain execution from the stack. This type is still configurable with stack and buffer sizes as well. Second, the conditional type lets you configure a condition that must be satisfied before being able to exploit the example, vulnerable program. Either, there must be a certain number of arguments present or there must be a series of bytes that must be matched in order to trigger the vulnerable code path. Reducing the barrier to entry and education for complex, cyber security topics will increase the readiness and capability of the cyber security workforce writ large and this tool will help those both teaching and learning to better understand the buffer overflow exploits with an unlimited number of examples that can be created simply from the command-line.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Automatically Map & Enrich ALL Alerts, Events & Logs with MITRE Attack Techniques</strong> — Ezzeldin Tahoun, Lynn Hamida, Nidheesh Panchal, Kevin Shi</summary>

**Track:** Data Forensics/Incident Response · AI, ML & Data Science · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/Dan-Duran/mitre-attack-mapper](https://github.com/Dan-Duran/mitre-attack-mapper)  
📝 **Description:** Using Natural Language Processing models, enrich any alert with its relevant attack techniques. The model detects the techniques using contextual, and situational awareness as well as its linguistic cyber expertise. In real time this model can save your operations endless hours of tagging incidents with their mitre techniques.

</details>

<details><summary><strong>AVSniper</strong> — Helvio Junior</summary>

**Track:** Malware Defense · Malware Offense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/helviojunior/avsniper](https://github.com/helviojunior/avsniper)  
📝 **Description:** A security analysis tool that identifies which specific strings in Windows executable files trigger antivirus detection by systematically extracting strings from PE files, creating modified versions, and testing them against antivirus software.

</details>

<details><summary><strong>Azure Unified Audit Log Mail Item Extractor'</strong> — Richard Smith</summary>

**Track:** Data Forensics/Incident Response · Cloud Security · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/invictus-ir/Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite)  
📝 **Description:** A PowerShell module for acquiring data from Microsoft 365 and Azure for incident response and cyber security purposes. It automates the extraction of logs, audit trails, and configuration data across Exchange Online, Entra ID, and Azure environments.

</details>

<details><summary><strong>Continuously Correlate & Contextualize ALL Alerts, Events & Logs</strong> — Ezzeldin Tahoun, Lynn Hamida, Nidheesh Panchal, Kevin Shi</summary>

**Track:** Data Forensics/Incident Response · AI, ML & Data Science · **Event:** Canada 2024  
🔗 **Link:** Not Available  
📝 **Description:** Using correlation and clustering models, turn tons of alerts into mitre attack flows. The model finds the attack flows, using its ability to evaluate alerts temporal proximity, kill chain sequentiality, shared entities and similar attributes to other alerts of interest, among others. In real time this model can save your operations endless hours of correlating incidents and finding noteworthy attack flows, that if not detected in time would lead to breaches.

</details>

<details><summary><strong>eBPFShield: Unleashing the Power of eBPF for OS Kernel Exploitation and Security</strong> — Sagar Bhure</summary>

**Track:** Network Defense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/sagarbhure/ebpfshield](https://github.com/sagarbhure/ebpfshield)  
📝 **Description:** Are you looking for an advanced tool that can help you detect and prevent sophisticated exploits on your systems? Look no further than eBPFShield. Let's take a technical look at some of the capabilities of this powerful technology: DNS monitoring feature is particularly useful for detecting DNS tunneling, a technique used by attackers to bypass network security measures. By monitoring DNS queries, eBPFShield can help detect and block these attempts before any damage is done. IP-Intelligence feature allows you to monitor outbound connections and check them against threat intelligence lists. This helps prevent command-and-control (C2) communications, a common tactic used by attackers to control compromised systems. By blocking outbound connections to known C2 destinations, eBPFShield can prevent attackers from exfiltrating sensitive data or delivering additional payloads to your system. eBPFShield Machine Learning feature, you can develop and run advanced machine learning algorithms entirely in eBPF. We demonstrate a flow-based network intrusion detection system(IDS) based on machine learning entirely in eBPF. Our solution uses a decision tree and decides for each packet whether it is malicious or not, considering the entire previous context of the network flow. eBPFShield Forensics helps address Linux security issues by analyzing system calls and kernel events to detect possible code injection into another process. It can also help identify malicious files and processes that may have been introduced to your system, allowing you to remediate any security issues quickly and effectively. During the session, we'll delve deeper into these features and demonstrate how eBPFShield can help you protect your systems against even the most advanced threats.

</details>

<details><summary><strong>Enhancing Windows Event Log Analysis with Open-Source Tools: Hayabusa and Takajo</strong> — Fukusuke Takahashi, Akira Nishikawa</summary>

**Track:** Data Forensics/Incident Response · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/Yamato-Security/hayabusa](https://github.com/Yamato-Security/hayabusa)  
📝 **Description:** Windows Event Log analysis is crucial for detecting security incidents and understanding system activities in forensic investigations. This session introduces two open-source tools from Yamato Security, a Japan-based security community founded by Zach Mathis. Yamato Security developed Hayabusa and Takajo to enhance the speed and accuracy of Windows Event Log analysis. Hayabusa leverages open-source Sigma rules to detect malicious activity in event logs, providing actionable insights. Takajo complements this by parsing Hayabusa's JSONL output, enabling rapid triage and analysis of key forensic artifacts, further streamlining incident response workflows. Together, these tools offer an integrated solution for Windows forensics, allowing for faster and more precise investigations. Join us to explore their features, real-world use cases, and how they enhance forensic analysis of Windows environments using Sigma rules. - https://github.com/Yamato-Security/hayabusa - https://github.com/Yamato-Security/takajo

</details>

<details><summary><strong>TCP/IP Communication without Network Attack Surfaces. (No Open Ports on External Interfaces)</strong> — Colin Constable, Xavier Chathavong</summary>

**Track:** Network Defense · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/Marcokorcak/TCP-IP-Attack](https://github.com/Marcokorcak/TCP-IP-Attack)  
📝 **Description:** - instead of "managing" attack surfaces, you can have ZERO network attack surfaces? In other words, nothing to attack with no network ports open! - instead of giving full visibility into your ecosystem, you could make everything invisible by default, granting access only to a select few who require it? - when a hacker scans the networks, there is nothing to attack? How is this all possible? Atsign's new open-source protocol brings this vision to life..Built on the principles of Networking 2.0, it ensures edge-to-edge data encryption, keeps all keys at the edge, and cryptographically signs everything, preventing any form of snooping, even by us.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>The Perfect BLEnd: Reversing a Bluetooth-Controlled Smart Blender for Better Smoothies</strong> — Ryan Mast</summary>

**Track:** Internet Of Things · Hardware/Embedded · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/nightlark/web-bluetooth-controller](https://github.com/nightlark/web-bluetooth-controller)  
📝 **Description:** A template repository for generating web pages that control Bluetooth Low Energy (BLE) devices through a browser interface using the Web Bluetooth API, enabling interaction with BLE devices via Chrome, Edge, or Opera.

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>3P Data Risk Metric (3PDRM)</strong> — Thomas Lee</summary>

**Track:** AI, ML & Data Science · Vulnerability Assessment · **Event:** Canada 2024  
🔗 **Link:** Not Available  
📝 **Description:** As organizations increasingly rely on third-party vendors and service providers, the risk of data breaches originating from external partners has become a critical concern. Traditional approaches to data security often overlook the cumulative-risk from the complex network of third-party relationships that can expose sensitive information to potential cyber threats. The derived calculation leverages a range of factors, including vendor cybersecurity posture, historical breach data, and the nature of data shared, to provide a predictive probability for each third-party entity. Through the application of regression analysis and risk modeling techniques, this framework enables organizations to better assess and prioritize their third-party risks, offering a more data-driven approach to mitigating potential exposures. The derived calculation provides a structured approach to calculate the probability of third-party cyber risks.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>NopEmulator</strong> — Austin Norby</summary>

**Track:** Reverse Engineering · **Event:** Canada 2024  
🔗 **Link:** [https://github.com/Quantumite/NopEmulator](https://github.com/Quantumite/NopEmulator)  
📝 **Description:** The NopEmulator is a Ghidra Script developed for the purpose of emulation Intel x64 instructions to determine if a Nop Sled is present in the binary. This tool originated from prior research that only used the ability to execute or parse the code as the only heuristic for valid Nop Sleds being present. This tool takes it one step further to emulate the instructions and validate if the resulting execution context is truly a Nop Sled. The tool can be applied to reverse engineering, malware analysis, and even to detecting exploits in network traffic that use Nop Sleds to transfer execution. While using the tool, the analyst has the option to configure how the script operates based on analysis need. This includes modifying the registers being analyzed by ignoring unimportant ones or specific ones based on their analysis needs. The script can also run from start-to-end, address-to-addresd, address for a length of bytes, or full analysis. The full analysis does a full bruteforce pass of every possible start and end value looking for Nop Sleds hidden within the bytes. In addition, when found, a comment is added to the starting and ending addresses to make analysis easier.

</details>

---
