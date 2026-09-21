# Canada 2023
---
📍 30 tools demonstrated at **Black Hat Arsenal Canada 2023**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security) (2)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (3)
- [🌐 Web/AppSec](#-webappsec) (2)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (1)
- [🔍 OSINT](#-osint) (1)
- [🔴 Red Teaming](#-red-teaming) (5)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (5)
- [🔵 Blue Team & Detection](#-blue-team--detection) (8)
- [🧠 Reverse Engineering](#-reverse-engineering) (3)
---
## ☁️ Cloud Security
<details><summary><strong>Beam OSS: Easily Make your Infra Private Using AWS SSM</strong> — Avi Zetser</summary>

**Track:** Cloud Security · Network Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/entitleio/beam](https://github.com/entitleio/beam)  
📝 **Description:** Beam is an OSS project that simplifies secure access to private infrastructure within non-public VPC environments. It replaces the traditional bastion host approach with AWS Systems Manager (SSM) for access, ensuring better security and user-friendliness, especially in dynamic environments with changing resources and multi-tenancy requirements. Beam eliminates the complexities of configuring SSM access, making it an accessible solution for various applications and environments while maintaining security best practices. Today Beam is available for AWS (SSM) and will expand to Google's Identity-Aware Proxy (IAP).

</details>

<details><summary><strong>Fortifying GCP Security: Open Source Just-In-Time access and Audit Log Monitoring</strong> — Dustin Decker</summary>

**Track:** Cloud Security · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/kartverket/google-jit-access](https://github.com/kartverket/google-jit-access)  
📝 **Description:** Google does not make cloud security easy. The tool we're open sourcing doesn't make it easy either, but it makes it about 10% less painful than the existential dread the default GCP policies have infected on your organization. In this talk, we'll guide you through setting up an audit log sink and evaluating events against Open Policy Agent (OPA) Rego policies. We'll discuss the included MITRE ATT&CK tactics policies and demonstrate how to create new custom policies using the OPA engine. We'll also cover how to make least privilege access control work for your organization with Just-In-Time access provisioning. Our presentation aims to empower GCP users with the knowledge and tools necessary for effective large-scale monitoring of their environments' security and actions. We'll share some experience and insights on the current state of controls within GCP, and how infrastructure providers can enable more powerful tooling. By the end of this talk, attendees will have gained practical knowledge in leveraging open source software to strengthen their GCP security posture. Don't miss this opportunity to stay ahead in the world of cloud security and enhance the protection of your GCP environment.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Attack & Defence AppSec Wargame</strong> — Pedram Hayati</summary>

**Track:** Arsenal Lab · **Event:** Canada 2023  
🔗 **Link:** [https://play.secdim.com/](https://play.secdim.com/)  
📝 **Description:** Come join our capture the flag game (of all skill levels) designed to improve your AppSec/DevSecOps skills and have fun doing it. Attack others by exploiting their apps and defend your app by securing it. The winner is the player whose app survives the longest. We will also explore a range of other AppSec challenges where the goal is to fix (not exploit) the vulnerability. All skill levels are welcome even if this is your first time seeing code or playing in a security game.

</details>

<details><summary><strong>Hands-on Multiprotocol Multiband IoT Hacking</strong> — Paulino Calderon, Eduardo Contreras</summary>

**Track:** Arsenal Lab · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/PacktPublishing/Hands-On-IoT-Solutions-with-Blockchain](https://github.com/PacktPublishing/Hands-On-IoT-Solutions-with-Blockchain)  
📝 **Description:** CatSniffer is an original multiprotocol, multiband, and open-source board made for sniffing, communicating, and attacking IoT (Internet of Things) devices. Join us to get hands-on with this swiss army knife causing a bit of BlueTooth mahem and also attacking real-world devices such a property trackers. Our interactive demos only scratch the surface of what is possible with this portable tool which also works with third-party sniffers such as SmartRF Packet Sniffer, Sniffle, zigbee2mqtt, Z-Stack-firmware, Ubiqua Protocol Analyzer, and our custom firmware. The extensibility makes it fun for beginners and experts alike.

</details>

<details><summary><strong>Vehicle Control Systems: Red vs Blue</strong> — Chris Sistrunk, Camille Felx Leduc</summary>

**Track:** Arsenal Lab · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/KarlVaello/VehicleControlSystem](https://github.com/KarlVaello/VehicleControlSystem)  
📝 **Description:** Real Time Operating Systems (RTOS) form the backbone for embedded systems and control units used in vehicle control technology (such as automobiles, trucks, buses, locomotives, UAVs, etc). In this session, we will get hands on red teaming a popular RTOS that's at the heart of vehicle control systems worldwide. To counter this activity, we will then provide a demo of memory extraction and data analysis following Mandiant's Digital Forensics and Incident Response Framework for Embedded OT Systems.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>HAWK Eye - PII & Secret Detection tool for your Servers, Database, Filesystems, Cloud Storage Services</strong> — Rohit Kumar</summary>

**Track:** Web AppSec · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/rohitcoder/hawk-eye](https://github.com/rohitcoder/hawk-eye)  
📝 **Description:** HAWK Eye is a command-line tool that scans multiple data sources including S3, MySQL, PostgreSQL, Redis, Firebase, filesystem, and GCS for PII data and secret exposure. It uses advanced text analysis and OCR techniques to detect sensitive information across cloud storage, databases, and file systems.

</details>

<details><summary><strong>Security Attacks as Software Tests: Building dev-oriented AppSec challenges with Play open source SDK</strong> — Pedram Hayati</summary>

**Track:** Web AppSec · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/secdim/play-sdk](https://github.com/secdim/play-sdk)  
📝 **Description:** This talk focuses on the unique process of transforming security attacks into software tests for building secure programming challenges using an open-source SDK, 'Play'. A practical workshop where we explore the mechanics of choosing real-world-inspired security vulnerabilities, and transforming them into cloud-native apps with integrated security tests which can then be played as challenges. These challenge provides a new dimension to the traditional Capture The Flag experiences, emphasizing not just the identification but the remediation of vulnerabilities

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Slim (Toolkit)</strong> — Kyle Quest</summary>

**Track:** Code Assessment · Cloud Security · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/slimtoolkit/slim](https://github.com/slimtoolkit/slim)  
📝 **Description:** Slim's mission is to secure your software supply chain — automatically. DevSecOps teams at BigID, Airbus, and Confluent implement Slim's prescriptive framework to secure their applications and automatically remove vulnerabilities before they get to production. The result? Faster remediation with a more comprehensive security solution. With SlimToolkit, CISOs and CTOs to trust in the software their teams deliver while using their preferred systems, software, or base images. We analyze and secure millions of containers a year and can start your team down the road to "Vuln0" in minutes. Our prescriptive open source framework and CNCF sandbox tool, guides teams in mapping their software ecosystem and proactively prioritizing and eliminating vulnerabilities. We provide continuous monitoring of threats, real-time policy enforcement, and clear lines of ownership and accountability. Whether you are a small team aiming to establish a strong security foundation or a large regulated enterprise seeking to meet rigorous compliance standards, Slim is here to support you every step of the way.

</details>

---
## 🔍 OSINT
<details><summary><strong>!CVE: A New Platform for Unacknowledged Cybersecurity !Vulnerabilities</strong> — Hector Marco, Samuel Arevalo</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Canada 2023  
🔗 **Link:** [https://www.notcve.org/](https://www.notcve.org/)  
📝 **Description:** In the ever-evolving cybersecurity landscape, the identification and acknowledgment of vulnerabilities through the Common Vulnerabilities and Exposures (CVE) system play a crucial role. However, vendor discretion in determining whether a security issue warrants a CVE assignment often results in overlooked vulnerabilities that pose significant risks. This presentation introduces the !CVE initiative, a groundbreaking platform that addresses this critical gap by identifying, tracking, and sharing unacknowledged cybersecurity vulnerabilities. Our presentation begins with an overview of the CVE system and the challenges security researchers face in dealing with unacknowledged vulnerabilities. We discuss real-world examples of security issues ignored by vendors and explore the potential consequences of these hidden threats. We then delve into the !CVE platform, detailing its mission, features, and collaborative approach to empower the security community. Through case studies, we demonstrate the value of the !CVE initiative in strengthening the cybersecurity ecosystem, highlighting the significance of addressing vulnerabilities not recognized by vendors. We also showcase the reporting process, expert panel, and public availability of !CVE reports, fostering a transparent and inclusive environment for vulnerability tracking and sharing. Join us in exploring the world of unacknowledged cybersecurity vulnerabilities and learn how the !CVE initiative is bridging the gap between vendor discretion and community-driven security efforts. By raising awareness and fostering collaboration, we can create a more secure and resilient digital landscape for all.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Abusing Microsoft SQL Server with SQLRecon</strong> — Sanjiv Kawa</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/skahwah/SQLRecon](https://github.com/skahwah/SQLRecon)  
📝 **Description:** In November 2022, Kaspersky Lab publicly released research which outlined that reoccurring attacks against Microsoft SQL Server rose by 56% (https://usa.kaspersky.com/about/press-releases/2022_kaspersky-finds-reoccurring-attacks-using-microsoft-sql-server-rise-by-56-in-2022). I'd like to share a tool I wrote called SQLRecon, which will demonstrate how adversaries are leveraging Microsoft SQL services to facilitate with furthering their presence within enterprise networks through privilege escalation and lateral movement. I will also share defensive considerations which organizations can practically implement to mitigate attacks. I feel that this will add a fresh perspective on the various ancillary services within enterprise Windows networks which are under less scrutiny, however still ripe for abuse. For red team operators, SQLRecon helps address the post-exploitation tooling gap by modernizing the approach operators can take when attacking SQL Servers. The tool is written in C#, rather than long-standing existing tools that use PowerShell or Python. SQLRecon has been designed with operational security and detection avoidance in mind – with a special focus on stealth, reconnaissance, lateral movement, and privilege escalation. The tool was designed to be modular, allowing for ease of extensibility from the hacker community. SQLRecon is compatible stand-alone or within a diverse set of command and control (C2) frameworks (Cobalt Strike, Nighthawk, Mythic, PoshC2, Sliver, Havoc, etc). When using the latter, SQLRecon can be executed either in-process, or through traditional fork and run. Furthermore, I will be releasing a new version, one that is currently only used internally on advanced red team engagements by IBM X-Force Red's Adversary Services team.

</details>

<details><summary><strong>CS2BR – Automatically porting Cobalt Strike BOFs to Brute Ratel</strong> — Mortiz Thomas, Patrick Eisenschmidt</summary>

**Track:** Exploitation and Ethical Hacking · Malware Offense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/NVISOsecurity/cs2br-bof](https://github.com/NVISOsecurity/cs2br-bof)  
📝 **Description:** Sometimes you're constrained in your choice of tools when emulating threats in red team assessments. When we used Brute Ratel for an assessment, we learned that it doesn't support regular BOFs (beacon object files). As a result, we developed CS2BR: it makes regular BOFs compatible with Brute Ratel. In this lab, we'll show you that and how the tool works!

</details>

<details><summary><strong>go-exploit: An Exploit Framework for Go</strong> — Jacob Baines</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/vulncheck-oss/go-exploit](https://github.com/vulncheck-oss/go-exploit)  
📝 **Description:** go-exploit is an exploit development framework for Go. The framework helps exploit developers create small, self-contained, portable, and consistent exploits. Many proof-of-concept exploits rely on interpreted languages with complicated packaging systems. They implement wildly differing user interfaces, and have limited ability to be executed within a target network. Some exploits are integrated into massive frameworks that are burdened by years of features and dependencies which overwhelm developers and hinder the attacker's ability to deploy the exploits from unconventional locations. To overcome these challenges, go-exploit offers a lightweight framework with minimal dependencies, written in Go—a language renowned for its portability and cross-compilation capabilities. The framework strikes a balance between simplicity for rapid proof-of-concept development and the inclusion of sophisticated built-in features for operational use.

</details>

<details><summary><strong>PowerGuest: AAD Guest Exploitation Beyond Enumeration</strong> — Michael Bargury, Lana Salameh</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/Kiosec/AD-Exploitation](https://github.com/Kiosec/AD-Exploitation)  
📝 **Description:** Azure AD guest accounts are widely used to grant external parties limited access to enterprise resources, with the assumption that these accounts pose little security risk. As you're about to see, this assumption is dangerously wrong. PowerGuest is a new tool that allows you to achieve the full potential of a guest in Azure AD by exploiting a series of undocumented internal APIs and common misconfiguration for collecting privileges, and using those for data exfiltration and actions on target, leaving no traces behind. The tool operates by leveraging shared credentials shared over Power Platform, a low-code / no-code platform built into Office365. PowerGuest allows gaining unauthorized access to sensitive business data and capabilities including corporate SQL servers, SharePoint sites, and KeyVault secrets. Furthermore, it allows guests to create and control internal business applications to move laterally within the organization. All capabilities are fully operational with the default Office 365 and Azure AD configuration.

</details>

<details><summary><strong>PurpleOPS - A Simple Tool to Help Track and Share Purple Team Data</strong> — Willem Mouton, Harrison Mitchell</summary>

**Track:** Exploitation and Ethical Hacking · Data Forensics/Incident Response · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/CyberCX-STA/PurpleOps](https://github.com/CyberCX-STA/PurpleOps)  
📝 **Description:** Purple team exercises are probably one of the most useful types of activities that organizations can engage in these days. Key to effective purple teaming is good communication, data collection and knowledge sharing. For us, this has been a bit of a pain point having to try and manually keep track of activities, actions and events. We did find some tools to aid with this, but none of them truly opensource or flexible enough to allow us to do what we wanted to do. So we built PurpleOPS, which is at its core a data collection tool aligned to MITRE ATT&CK and integrated into other fantastic open-source projects such as Atomic Redteam. It is easy to customize with your own internal knowledge base and test cases, plus it's also written in python3 using Flask, so it's super easy to adjust to your needs.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Artificial Intelligence Phishing Email Detector</strong> — Waqur Ahmed</summary>

**Track:** Vulnerability Assessment · Human Factors · **Event:** Canada 2023  
🔗 **Link:** Not Available  
📝 **Description:** An artificial intelligence based phishing email detector that analyses emails and its content, vocabulary, sender, subject etc and detects if its a phishing email even if was not flagged as one by an email gateway based on the analysis of collection of phishing emails.

</details>

<details><summary><strong>Enhancing Vulnerability Research through the Use of Virtual Reality Workspaces</strong> — datalocaltmp .</summary>

**Track:** Vulnerability Assessment · Reverse Engineering · **Event:** Canada 2023  
🔗 **Link:** Not Available  
📝 **Description:** A project exploring the use of virtual reality workspaces to enhance vulnerability research workflows, integrating tools for binary analysis, reverse engineering, and systems-level security research into immersive VR environments.

</details>

<details><summary><strong>Introducing RAVEN: Discovering and Analyzing CI/CD Vulnerabilities in Scale</strong> — Alex Ilgayev, Elad Pticha, Oreen Livni</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/CycodeLabs/raven](https://github.com/CycodeLabs/raven)  
📝 **Description:** RAVEN performs massive scans of GitHub Actions CI workflows and indexes the discovered data into a Neo4j graph database. It enables users to identify CI/CD pipeline vulnerabilities through workflow analysis and generates security reports based on predefined queries.

</details>

<details><summary><strong>LLM Gateway – an OSS to Monitor LLM Interactions</strong> — Jeff Schwartzentruber, Nik Kershaw</summary>

**Track:** Vulnerability Assessment · **Event:** Canada 2023  
🔗 **Link:** Not Available  
📝 **Description:** As the LLM landscape evolves businesses will need tools to help monitor and mitigate vulnerabilities these new technologies introduce. The LLM Gateway Framework acts as a proxy, frontend, and logging services to monitor and manage LLM interactions across any providers. LLM gateway can be found here on Github

</details>

<details><summary><strong>MAD Goat Project</strong> — Luís Ventuzelos</summary>

**Track:** Vulnerability Assessment · Web AppSec · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/MAD-Goat-Project](https://github.com/MAD-Goat-Project)  
📝 **Description:** Modern Application Development (MAD) makes use of a series of building blocks, like microservices, containerized applications, infrastructure as code, open-source software, and API communication. In today's landscape, a single application can have dozens of independent services communicating with one another, and the relation between all these services can be hard to grasp for the security testing tools available in the market. Application security testing (AST) tools like SAST, DAST, SCA, or SCS can help companies to protect the software they produce. However, with the increased complexity of software applications and their interoperability with diverse systems, it becomes harder for individual AST tools to discover vulnerabilities in a complete application. The main objective of the MAD Goat project is to develop a web-based software application that takes into consideration all the MAD building blocks, while offering a vulnerable application by nature. This vulnerable application will serve as a security benchmark project to understand the quality of different security test scanners. The application has also an educational focus in its nature, offering its users an interactive learning experience. Through engaging lessons, users can enhance their understanding of the main vulnerabilities associated with MAD and develop mitigation strategies.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Advanced Threat Mitigation with RL + SDN</strong> — Ezzeldin Tahoun</summary>

**Track:** Network Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/ATMoS-Waterloo/ATMoS](https://github.com/ATMoS-Waterloo/ATMoS)  
📝 **Description:** The more security tools on a network the better for observing advanced attacks, but the worse for the network bandwidth or quality of service. Ideally a hunter decides where we point our security tools at any given time to find threat actors in our networks. Since, threat investigators and hunters are rare and expensive, this is a tool that uses SDN and RL to automatically conduct threat hunting investigations, migrating suspicious users to network with more stringent security controls, such as Deep packet inspection firewall, s network intrusion prevent systems, web gateways, ssl decryption, etc. Detects and Contains threats in milliseconds.

</details>

<details><summary><strong>Grove: An Open-Source Log Collection Framework</strong> — Peter Adkins, Melissa Hardware</summary>

**Track:** Data Forensics/Incident Response · Network Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/hashicorp-forge/grove](https://github.com/hashicorp-forge/grove)  
📝 **Description:** Grove is a log collection framework designed to support a unified way of collecting, storing, and routing logs from Software as a Service (SaaS) providers which do not natively support log streaming. This is performed by periodically collecting logs from configured sources, and writing them to arbitrary destinations. Grove enables teams to collect security related events from their vendors in a reliable and consistent way, while allowing this data to be stored and analyzed with existing tools.

</details>

<details><summary><strong>Malicious Executions: Unmasking Container Drifts and Fileless Malware with Falco</strong> — Lorenzo Susini, Stefano Chierici</summary>

**Track:** Malware Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/falcosecurity/falco](https://github.com/falcosecurity/falco)  
📝 **Description:** Containers are the most popular technology for deploying modern applications. SPOILER ALERT: bypassing well-known security controls is also popular. In this talk, we explain how to use the recent updates in Falco, a CNCF open-source container security tool, to detect drifts and fileless malware in containerized environments. As a best practice, containers should be considered immutable. Early this year, Falco introduced new features to detect container drift via OverlayFS, which can spot if binaries are added or modified after the container's deployment. New binaries are often a sign of an ongoing attack. Of course, attackers can also use more advanced evasion techniques to stay hidden. By using in-memory, fileless execution, attackers can bypass most of the security controls such as drift detection and still reach their goals with no stress. To combat fileless attacks, Falco has also added memfd-based fileless execution thanks to its visibility superpowers on Linux kernel system calls. Combining Falco's existing runtime security capabilities with these two new detection layers forms the foundation of a defense in depth strategy for cloud-native workloads. We will walk you through real-world scenarios based on recent threats and malware, demoing how Falco can help detect and respond to these malicious behaviors and comparing both drift and fileless attack paths.

</details>

<details><summary><strong>Mitre Attack Flow Detector</strong> — Ezzeldin Tahoun</summary>

**Track:** Data Forensics/Incident Response · AI, ML & Data Science · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/ezztahoun/attack_flow_detector](https://github.com/ezztahoun/attack_flow_detector)  
📝 **Description:** Using correlation and clustering models, turn tons of alerts into mitre attack flows. The model finds the attack flows, using its ability to evaluate alerts temporal proximity, kill chain sequentiality, shared entities and similar attributes to other alerts of interest, among others. In real time this model can save your operations endless hours of correlating incidents and finding noteworthy attack flows, that if not detected in time would lead to breaches.

</details>

<details><summary><strong>Mitre Attack Technique Detector</strong> — Ezzeldin Tahoun</summary>

**Track:** Data Forensics/Incident Response · **Event:** Canada 2023  
🔗 **Link:** Not Available  
📝 **Description:** Using Natural Language Processing models, enrich any alert with its relevant attack techniques. The model detects the techniques using contextual, and situational awareness as well as its linguistic cyber expertise. In real time this model can save your operations endless hours of tagging incidents with their mitre techniques.

</details>

<details><summary><strong>Network Monitoring Tools for macOS</strong> — Patrick Wardle</summary>

**Track:** Malware Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/objective-see/Netiquette](https://github.com/objective-see/Netiquette)  
📝 **Description:** As the majority of malware contains networking capabilities, it is well understood that detecting unauthorized network access is a powerful detection heuristic. However, while the concepts of network traffic analysis and monitoring to detect malicious code are well established and widely implemented on platforms such as Windows, there remains a dearth of such capabilities on macOS. Here, we will present various tools capable of enumerating network state, statistics, and traffic, directly on a macOS host. We will showcase open-source tools that leverage low-level APIs, private frameworks, and user-mode extensions that provide insight into all networking activity on macOS: Specifically we'll demonstrate: * A network monitor that allows one to explore all network sockets and connections, either via an interactive UI, or from the commandline. * A DNS monitor that uses Apple's Network Extension Framework to monitors DNS requests and responses directly from the Terminal. * A firewall that monitors and filters all network traffic, giving users with the ability to block unknown/unauthorized outgoing connections.

</details>

<details><summary><strong>SinCity: Build Your Dream Lab Environment</strong> — Matan Hart, Shay Yaish</summary>

**Track:** Network Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/tenable/sincity](https://github.com/tenable/sincity)  
📝 **Description:** Security practitioners are still wasting time today building and maintaining lab environments through "manual" and cumbersome processes. In doing so, they are missing out on the potential DevOps methodologies and Infrastructure-as-Code (IaC) practices offer. This daunting work must end now. This arsenal demonstration will introduce SinCity, a GPT-powered, MITRE ATT&CK-based tool which automates the provisioning and management of an IT environment in a conversational way. SinCity reduces the efforts needed to build a full-blown lab environment from months to minutes by providing an abstraction layer for customizing network topologies, crafting attack scenarios, and tuning security controls. Attendees who frequently sandbox malware, analyze TTPs, or evaluate detection capabilities - this arsenal will save you precious time.

</details>

<details><summary><strong>Windows On ARM Rootkit Detector</strong> — Rotem Salinas</summary>

**Track:** Malware Defense · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/cyberark/woarkd](https://github.com/cyberark/woarkd)  
📝 **Description:** A utility for Windows 11 ARM64 systems that detects SSDT hooking attempts, a technique used by rootkits to intercept system calls by modifying kernel function pointers.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>A Ghidra Visualization is worth a Thousand GDB breakpoints</strong> — datalocaltmp .</summary>

**Track:** Reverse Engineering · **Event:** Canada 2023  
🔗 **Link:** Not Available  
📝 **Description:** Whether reverse engineering malware, debugging an application, or researching device security; being able to quickly gain a deep understanding of the project at hand is a huge advantage. This arsenal showcase aims to provide a practical guide to producing visualizations of native code execution within Ghidra to better direct time and efforts (and prevent setting endless breakpoints). I will be demoing the current opensource tool stack for code execution visualization (Ghidra + Frida + DragonDance + Lighthouse), and how they practically work together to visualize Android Application execution. I will then describe the limitations of the current tooling and the necessity I saw to develop my own tool. This tool specifically extends the code coverage to Non-rooted Android devices and Android non-app processes. I will then demo using my version of the coverage collection tool for Non-Rooted Android devices, specifcally by generating visualizations of native code executing on a Quest 2 VR headset.

</details>

<details><summary><strong>Ghidriff: Ghidra Binary Diffing Engine</strong> — John McIntosh</summary>

**Track:** Reverse Engineering · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/clearbluejar/ghidriff](https://github.com/clearbluejar/ghidriff)  
📝 **Description:** "As seen in most security blog posts today, binary diffing tools are essential for reverse engineering, vulnerability research, and malware analysis. Patch diffing is a technique widely used to identify changes across versions of binaries as related to security patches. By diffing two binaries, a security researcher can dig deeper into the latest CVEs and patched vulnerabilities to understand their root cause. Ghidriff is a new open-source Python package that offers a command line binary diffing capability leveraging the power of the Ghidra Software Reverse Engineering (SRE) Framework with a fresh take on the standard patch diffing workflow. Like other binary diffing solutions, Ghidriff relies on SRE tooling to distill complex binaries into objects and relationships that can be compared. Unlike other tools, Ghidriff offers a command line experience, simplifying the entire patch diffing workflow to only a single step, significantly reducing analysis time. Additionally, the results of the diff are rendered as concise markdown files that can be shared on GitHub, GitLab, blogs, or almost anywhere. Come check out Ghidriff's unique features, and let's learn together how to patch diff modern CVEs."

</details>

<details><summary><strong>ParseAndC 3.0 – Parse Everything Everywhere All At Once</strong> — Parbati Manna</summary>

**Track:** Reverse Engineering · Code Assessment · **Event:** Canada 2023  
🔗 **Link:** [https://github.com/intel/ParseAndC](https://github.com/intel/ParseAndC)  
📝 **Description:** This is the 3.0 version of the ParseAndC tool that was presented in BH and DEFCON last year, with many new features added. The 1.0 version was capable of mapping any C structure(s) to any datastream, and then visually displaying the 1:1 correspondence between the variables and the data in a very colorful, intuitive display so that it was very easy to understand which field had what value. In 2.0 version, we essentially expand the C language so that C structures alone has the same power as full-fledged C programs. We introduce Dynamic structure, which changes depending on what data it has seen till now. It supports variable-sized array, variable-sized bitfield, and addition/deletion of struct members depending on what value the previous struct members have. Suppose we are parsing the network packets, and after we decode the IP header, depending on the protocol field this tool can automatically decode the next header as either the TCP or UDP. We also add speculative execution, where user just provides the key expected values of certain fields (like magic numbers, mentioned by C initializations), and the tool automatically finds out from which offset to map so that all fields indeed have the expected value. This tool is extremely portable – it's a single Python 1MB text file, is cross-platform (Windows/Mac/Unix), and also works in the terminal /batch mode without GUI or Internet connection. The tool is self-contained - it doesn't import anything, to the extent that it implements its own C compiler (front-end) from scratch!! This tool is useful for both security- and non-security testing alike (reverse engineering, network traffic analyzing, packet processing etc.). It is currently being used at Intel widely. The author of this tool led many security hackathons at Intel and there this tool was found to be very useful.

</details>

---
