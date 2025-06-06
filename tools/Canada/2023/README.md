# Canada 2023
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2023** event held in **Canada**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [⚙️ Miscellaneous / Lab Tools](#⚙️-miscellaneous-lab-tools)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
---
## 🔍 OSINT
<details><summary><strong>!CVE: A New Platform for Unacknowledged Cybersecurity !Vulnerabilities</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Hector Marco](https://img.shields.io/badge/Hector%20Marco-informational) ![Samuel Arevalo](https://img.shields.io/badge/Samuel%20Arevalo-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## Others
<details><summary><strong>A Ghidra Visualization is worth a Thousand GDB breakpoints</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![datalocaltmp .](https://img.shields.io/badge/datalocaltmp%20.-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Abusing Microsoft SQL Server with SQLRecon</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Sanjiv Kawa](https://img.shields.io/badge/Sanjiv%20Kawa-informational)

🔗 **Link:** [Abusing Microsoft SQL Server with SQLRecon](https://github.com/Tw1sm/PySQLRecon)  
📝 **Description:** In November 2022, Kaspersky Lab publicly released research which outlined that reoccurring attacks against Microsoft SQL Server rose by 56% (https://usa.kaspersky.com/about/press-releases/2022_kaspersky-finds-reoccurring-attacks-using-microsoft-sql-server-rise-by-56-in-2022).


I'd like to share a tool I wrote called SQLRecon, which will demonstrate how adversaries are leveraging Microsoft SQL services to facilitate with furthering their presence within enterprise networks through privilege escalation and lateral movement. I will also share defensive considerations which organizations can practically implement to mitigate attacks. I feel that this will add a fresh perspective on the various ancillary services within enterprise Windows networks which are under less scrutiny, however still ripe for abuse.


For red team operators, SQLRecon helps address the post-exploitation tooling gap by modernizing the approach operators can take when attacking SQL Servers. The tool is written in C#, rather than long-standing existing tools that use PowerShell or Python. SQLRecon has been designed with operational security and detection avoidance in mind – with a special focus on stealth, reconnaissance, lateral movement, and privilege escalation. The tool was designed to be modular, allowing for ease of extensibility from the hacker community. SQLRecon is compatible stand-alone or within a diverse set of command and control (C2) frameworks (Cobalt Strike, Nighthawk, Mythic, PoshC2, Sliver, Havoc, etc). When using the latter, SQLRecon can be executed either in-process, or through traditional fork and run.


Furthermore, I will be releasing a new version, one that is currently only used internally on advanced red team engagements by IBM X-Force Red's Adversary Services team.

</details>

<details><summary><strong>Beam OSS: Easily Make your Infra Private Using AWS SSM</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Avi Zetser](https://img.shields.io/badge/Avi%20Zetser-informational)

🔗 **Link:** [Beam OSS: Easily Make your Infra Private Using AWS SSM](https://gist.github.com/GrahamcOfBorg/cc1bbf961b65e106514cb3f2032d718c)  
📝 **Description:** Beam is an OSS project that simplifies secure access to private infrastructure within non-public VPC environments. It replaces the traditional bastion host approach with AWS Systems Manager (SSM) for access, ensuring better security and user-friendliness, especially in dynamic environments with changing resources and multi-tenancy requirements. Beam eliminates the complexities of configuring SSM access, making it an accessible solution for various applications and environments while maintaining security best practices. Today Beam is available for AWS (SSM) and will expand to Google's Identity-Aware Proxy (IAP).

</details>

<details><summary><strong>CS2BR – Automatically porting Cobalt Strike BOFs to Brute Ratel</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Mortiz Thomas](https://img.shields.io/badge/Mortiz%20Thomas-informational) ![Patrick Eisenschmidt](https://img.shields.io/badge/Patrick%20Eisenschmidt-informational)

🔗 **Link:** Not Available  
📝 **Description:** Sometimes you're constrained in your choice of tools when emulating threats in red team assessments. When we used Brute Ratel for an assessment, we learned that it doesn't support regular BOFs (beacon object files). As a result, we developed CS2BR: it makes regular BOFs compatible with Brute Ratel. In this lab, we'll show you that and how the tool works!

</details>

<details><summary><strong>Enhancing Vulnerability Research through the Use of Virtual Reality Workspaces</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![datalocaltmp .](https://img.shields.io/badge/datalocaltmp%20.-informational)

🔗 **Link:** Not Available  
📝 **Description:** 

</details>

<details><summary><strong>Fortifying GCP Security: Open Source Just-In-Time access and Audit Log Monitoring</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Dustin Decker](https://img.shields.io/badge/Dustin%20Decker-informational)

🔗 **Link:** Not Available  
📝 **Description:** Google does not make cloud security easy. The tool we're open sourcing doesn't make it easy either, but it makes it about 10% less painful than the existential dread the default GCP policies have infected on your organization.


In this talk, we'll guide you through setting up an audit log sink and evaluating events against Open Policy Agent (OPA) Rego policies. We'll discuss the included MITRE ATT&CK tactics policies and demonstrate how to create new custom policies using the OPA engine. We'll also cover how to make least privilege access control work for your organization with Just-In-Time access provisioning.


Our presentation aims to empower GCP users with the knowledge and tools necessary for effective large-scale monitoring of their environments' security and actions. We'll share some experience and insights on the current state of controls within GCP, and how infrastructure providers can enable more powerful tooling.


By the end of this talk, attendees will have gained practical knowledge in leveraging open source software to strengthen their GCP security posture. Don't miss this opportunity to stay ahead in the world of cloud security and enhance the protection of your GCP environment.

</details>

<details><summary><strong>Ghidriff: Ghidra Binary Diffing Engine</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![John McIntosh](https://img.shields.io/badge/John%20McIntosh-informational)

🔗 **Link:** Not Available  
📝 **Description:** "As seen in most security blog posts today, binary diffing tools are essential for reverse engineering, vulnerability research, and malware analysis. Patch diffing is a technique widely used to identify changes across versions of binaries as related to security patches. By diffing two binaries, a security researcher can dig deeper into the latest CVEs and patched vulnerabilities to understand their root cause.


Ghidriff is a new open-source Python package that offers a command line binary diffing capability leveraging the power of the Ghidra Software Reverse Engineering (SRE) Framework with a fresh take on the standard patch diffing workflow.
Like other binary diffing solutions, Ghidriff relies on SRE tooling to distill complex binaries into objects and relationships that can be compared. Unlike other tools, Ghidriff offers a command line experience, simplifying the entire patch diffing workflow to only a single step, significantly reducing analysis time. Additionally, the results of the diff are rendered as concise markdown files that can be shared on GitHub, GitLab, blogs, or almost anywhere.


Come check out Ghidriff's unique features, and let's learn together how to patch diff modern CVEs."

</details>

<details><summary><strong>Grove: An Open-Source Log Collection Framework</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Peter Adkins](https://img.shields.io/badge/Peter%20Adkins-informational) ![Melissa Hardware](https://img.shields.io/badge/Melissa%20Hardware-informational)

🔗 **Link:** [Grove: An Open-Source Log Collection Framework](https://gist.github.com/LisaDawn/7003846)  
📝 **Description:** Grove is a log collection framework designed to support a unified way of collecting, storing, and routing logs from Software as a Service (SaaS) providers which do not natively support log streaming.


This is performed by periodically collecting logs from configured sources, and writing them to arbitrary destinations.


Grove enables teams to collect security related events from their vendors in a reliable and consistent way, while allowing this data to be stored and analyzed with existing tools.

</details>

<details><summary><strong>Mitre Attack Flow Detector</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ezzeldin Tahoun](https://img.shields.io/badge/Ezzeldin%20Tahoun-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Mitre Attack Technique Detector</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ezzeldin Tahoun](https://img.shields.io/badge/Ezzeldin%20Tahoun-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>ParseAndC 3.0 – Parse Everything Everywhere All At Once</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Parbati Manna](https://img.shields.io/badge/Parbati%20Manna-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>PurpleOPS - A Simple Tool to Help Track and Share Purple Team Data</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Willem Mouton](https://img.shields.io/badge/Willem%20Mouton-informational) ![Harrison Mitchell](https://img.shields.io/badge/Harrison%20Mitchell-informational)

🔗 **Link:** Not Available  
📝 **Description:** Purple team exercises are probably one of the most useful types of activities that organizations can engage in these days. Key to effective purple teaming is good communication, data collection and knowledge sharing. For us, this has been a bit of a pain point having to try and manually keep track of activities, actions and events. We did find some tools to aid with this, but none of them truly opensource or flexible enough to allow us to do what we wanted to do. So we built PurpleOPS, which is at its core a data collection tool aligned to MITRE ATT&CK and integrated into other fantastic open-source projects such as Atomic Redteam. It is easy to customize with your own internal knowledge base and test cases, plus it's also written in python3 using Flask, so it's super easy to adjust to your needs.

</details>

<details><summary><strong>Slim (Toolkit)</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Kyle Quest](https://img.shields.io/badge/Kyle%20Quest-informational)

🔗 **Link:** [Slim (Toolkit)](https://github.com/orgs/slimtoolkit/people)  
📝 **Description:** Slim's mission is to secure your software supply chain — automatically.
DevSecOps teams at BigID, Airbus, and Confluent implement Slim's prescriptive framework to secure their applications and automatically remove vulnerabilities before they get to production. The result? Faster remediation with a more comprehensive security solution.

With SlimToolkit, CISOs and CTOs to trust in the software their teams deliver while using their preferred systems, software, or base images. We analyze and secure millions of containers a year and can start your team down the road to "Vuln0" in minutes.

Our prescriptive open source framework and CNCF sandbox tool, guides teams in mapping their software ecosystem and proactively prioritizing and eliminating vulnerabilities. We provide continuous monitoring of threats, real-time policy enforcement, and clear lines of ownership and accountability.

Whether you are a small team aiming to establish a strong security foundation or a large regulated enterprise seeking to meet rigorous compliance standards, Slim is here to support you every step of the way.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Advanced Threat Mitigation with RL + SDN</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ezzeldin Tahoun](https://img.shields.io/badge/Ezzeldin%20Tahoun-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Malicious Executions: Unmasking Container Drifts and Fileless Malware with Falco</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Lorenzo Susini](https://img.shields.io/badge/Lorenzo%20Susini-informational) ![Stefano Chierici](https://img.shields.io/badge/Stefano%20Chierici-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Network Monitoring Tools for macOS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [Network Monitoring Tools for macOS](https://github.com/drduh/macOS-Security-and-Privacy-Guide)  
📝 **Description:** As the majority of malware contains networking capabilities, it is well understood that detecting unauthorized network access is a powerful detection heuristic. However, while the concepts of network traffic analysis and monitoring to detect malicious code are well established and widely implemented on platforms such as Windows, there remains a dearth of such capabilities on macOS.


Here, we will present various tools capable of enumerating network state, statistics, and traffic, directly on a macOS host. We will showcase open-source tools that leverage low-level APIs, private frameworks, and user-mode extensions that provide insight into all networking activity on macOS:


Specifically we'll demonstrate:


* A network monitor that allows one to explore all network sockets and connections, either via an interactive UI, or from the commandline.


* A DNS monitor that uses Apple's Network Extension Framework to monitors DNS requests and responses directly from the Terminal.


* A firewall that monitors and filters all network traffic, giving users with the ability to block unknown/unauthorized outgoing connections.

</details>

<details><summary><strong>SinCity: Build Your Dream Lab Environment</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Matan Hart](https://img.shields.io/badge/Matan%20Hart-informational) ![Shay Yaish](https://img.shields.io/badge/Shay%20Yaish-informational)

🔗 **Link:** Not Available  
📝 **Description:** Security practitioners are still wasting time today building and maintaining lab environments through "manual" and cumbersome processes. In doing so, they are missing out on the potential DevOps methodologies and Infrastructure-as-Code (IaC) practices offer. This daunting work must end now.


This arsenal demonstration will introduce SinCity, a GPT-powered, MITRE ATT&CK-based tool which automates the provisioning and management of an IT environment in a conversational way. SinCity reduces the efforts needed to build a full-blown lab environment from months to minutes by providing an abstraction layer for customizing network topologies, crafting attack scenarios, and tuning security controls.


Attendees who frequently sandbox malware, analyze TTPs, or evaluate detection capabilities - this arsenal will save you precious time.

</details>

<details><summary><strong>Windows On ARM Rootkit Detector</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rotem Salinas](https://img.shields.io/badge/Rotem%20Salinas-informational)

🔗 **Link:** Not Available  
📝 **Description:** 

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Artificial Intelligence Phishing Email Detector</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Waqur Ahmed](https://img.shields.io/badge/Waqur%20Ahmed-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Introducing RAVEN: Discovering and Analyzing CI/CD Vulnerabilities in Scale</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Alex Ilgayev](https://img.shields.io/badge/Alex%20Ilgayev-informational) ![Elad Pticha](https://img.shields.io/badge/Elad%20Pticha-informational) ![Oreen Livni](https://img.shields.io/badge/Oreen%20Livni-informational)

🔗 **Link:** Not Available  
📝 **Description:** 

</details>

<details><summary><strong>LLM Gateway – an OSS to Monitor LLM Interactions</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Jeff Schwartzentruber](https://img.shields.io/badge/Jeff%20Schwartzentruber-informational) ![Nik Kershaw](https://img.shields.io/badge/Nik%20Kershaw-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>MAD Goat Project</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Luís Ventuzelos](https://img.shields.io/badge/Luís%20Ventuzelos-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Attack & Defence AppSec Wargame</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Hands-on Multiprotocol Multiband IoT Hacking</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Paulino Calderon](https://img.shields.io/badge/Paulino%20Calderon-informational) ![Eduardo Contreras](https://img.shields.io/badge/Eduardo%20Contreras-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Vehicle Control Systems: Red vs Blue</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Chris Sistrunk](https://img.shields.io/badge/Chris%20Sistrunk-informational) ![Camille Felx Leduc](https://img.shields.io/badge/Camille%20Felx%20Leduc-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🔴 Red Teaming
<details><summary><strong>go-exploit: An Exploit Framework for Go</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jacob Baines](https://img.shields.io/badge/Jacob%20Baines-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>PowerGuest: AAD Guest Exploitation Beyond Enumeration</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Bargury](https://img.shields.io/badge/Michael%20Bargury-informational) ![Lana Salameh](https://img.shields.io/badge/Lana%20Salameh-informational)

🔗 **Link:** Not Available  
📝 **Description:** Azure AD guest accounts are widely used to grant external parties limited access to enterprise resources, with the assumption that these accounts pose little security risk. As you're about to see, this assumption is dangerously wrong.


PowerGuest is a new tool that allows you to achieve the full potential of a guest in Azure AD by exploiting a series of undocumented internal APIs and common misconfiguration for collecting privileges, and using those for data exfiltration and actions on target, leaving no traces behind. The tool operates by leveraging shared credentials shared over Power Platform, a low-code / no-code platform built into Office365.


PowerGuest allows gaining unauthorized access to sensitive business data and capabilities including corporate SQL servers, SharePoint sites, and KeyVault secrets. Furthermore, it allows guests to create and control internal business applications to move laterally within the organization. All capabilities are fully operational with the default Office 365 and Azure AD configuration.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>HAWK Eye - PII & Secret Detection tool for your Servers, Database, Filesystems, Cloud Storage Services</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Rohit Kumar](https://img.shields.io/badge/Rohit%20Kumar-informational)

🔗 **Link:** Not Available  
📝 **Description:** 

</details>

<details><summary><strong>Security Attacks as Software Tests: Building dev-oriented AppSec challenges with Play open source SDK</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---