# Europe 2020
---
📍 23 tools demonstrated at **Black Hat Arsenal Europe 2020**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (2)
- [🌐 Web/AppSec](#-webappsec) (2)
- [📱 Mobile Security](#-mobile-security) (1)
- [🔍 OSINT](#-osint) (1)
- [🔴 Red Teaming](#-red-teaming) (6)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (1)
- [🔵 Blue Team & Detection](#-blue-team--detection) (6)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (2)
- [🧠 Reverse Engineering](#-reverse-engineering) (2)
---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Dialing Home: ATM Protocol Reversing</strong> — wasabi jrwr</summary>

**Track:** Arsenal Lab · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/arvindbhamidipati/ATM-Network-System](https://github.com/arvindbhamidipati/ATM-Network-System)  
📝 **Description:** A Java-based project that simulates an ATM network infrastructure where multiple banks operate connected ATM machines, modeling interactions between banks, ATMs, customer accounts, and debit cards within a shared network.

</details>

<details><summary><strong>JTAGulator: Assisted Discovery of On-Chip Debug Interfaces</strong> — Joe Grand</summary>

**Track:** Arsenal Lab · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/grandideastudio/jtagulator](https://github.com/grandideastudio/jtagulator)  
📝 **Description:** An open-source hardware tool that assists in identifying on-chip debug (OCD) interfaces such as JTAG and UART from test points on electronic devices.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>SnitchDNS</strong> — Pavel Tsakalidis</summary>

**Track:** Web AppSec · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/ctxis/SnitchDNS](https://github.com/ctxis/SnitchDNS)  
📝 **Description:** "It's always DNS". SnitchDNS is database driven (basic) DNS server built using Twisted, with a fancy web interface to go with it. Ideal for Red Team infrastructure, bug bounties, ad-blocking, DNS tunnels, and more. As it's database driven, any changes are reflected immediately, match wildcard subdomains, source IP restrictions, conditional responses (great for SSRF), Slack/Teams/Email/Push notifications, logging, Swagger 2.0 API, full CLI interface, and more! Ideal use cases are as a DNS Tunnel, DNS forwarding server, red teams, canary tokens, LetsEncrypt DNS challenge, and even ad-blocking.

</details>

<details><summary><strong>Threagile: Agile Threat Modeling Toolkit</strong> — Christian Schneider</summary>

**Track:** Web AppSec · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/Threagile/threagile](https://github.com/Threagile/threagile)  
📝 **Description:** If we can build software in a reliable, reproducible and quick way at any time using Pipeline-as-Code and have also automated security scans as part of it, how can we quickly capture the risk landscape of agile projects to ensure we didn't miss an important thing? Traditionally, this happens in workshops with lots of discussion and model work on the whiteboard. It's just a pity that it often stops then: Instead of a living model, a slowly but surely eroding artifact is created, while the agile project evolves at a faster pace. In order to counteract this process of decay, something has to be done continuously, something like "Threat-Model-as-Code" in the DevSecOps sense. The open-source tool Threagile implements the ideas behind this approach: Agile developer-friendly threat modeling right from within the IDE. Models editable in developer IDEs and diffable in Git, which automatically derive risks including graphical diagram and report generation with recommended mitigation actions. The open-source Threagile toolkit runs either as a command line tool or a full-fledged server with a REST-API: Given information about your data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules (and optionally your custom risk rules) against the processed model. The resulting artifacts are diagrams, JSON, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state. Agile development teams can easily integrate threat modeling into their process by maintaining a simple YAML input file about their architecture and the open-source Threagile toolkits handles the risk evaluation.

</details>

---
## 📱 Mobile Security
<details><summary><strong>AndroGoat: Learn Android Application Security Testing</strong> — Satish Patnayak</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/satishpatnayak/AndroGoat](https://github.com/satishpatnayak/AndroGoat)  
📝 **Description:** AndroGoat is purposely developed open source vulnerable/insecure app using Kotlin. This app has a wide range of vulnerabilities related to certificate pinning, custom URL schemes, Android Network Security Configuration, WebViews, root detection and over 20 other vulnerabilities. Security Testers/Professionals/Enthusiasts, Developers...etc. can use this application to understand and defend the vulnerabilities in Android platform

</details>

---
## 🔍 OSINT
<details><summary><strong>kubeletctl: A Kubelet Client to Attack Kubernetes</strong> — Eviatar Gerzi</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/cyberark/kubeletctl](https://github.com/cyberark/kubeletctl)  
📝 **Description:** kubeletctl is a CLI client for kubelet - the remote agent of Kubernetes on the nodes. It implements all the documented and undocumented API of kubelet but it also includes offensive capabilities: - Scan for vulnerable nodes - Scan for containers with RCE - Run command on multiple containers

</details>

---
## 🔴 Red Teaming
<details><summary><strong>AttackForge: Pentest Management & Collaboration Platform</strong> — Fil Filiposki, Stas Filshtinskiy</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/attackforge/reportgen](https://github.com/attackforge/reportgen)  
📝 **Description:** AttackForge.com is a free-to-use platform to manage your pentesting projects & programs, and to collaborate with everyone who needs to be involved - reducing overheads and pain for Customers, 3rd parties and Pentest Teams. This is what makes AttackForge unique and different to other pentest management & collaboration solutions. It goes beyond automated reporting and issue library. It brings everyone together in one place and gives them tools and workflows to initiate & deliver a pentest from start to end, and also manage remediation testing - with integrations into other industry tools & platforms. Pentesters love to break things. They don't like manual, repetitive, boring tasks such copy/paste vulnerability write-up templates from old reports. AttackForge provides a rich issue library with over 1300 issues already built in that you can keyword search and select on your pentest. You can import vulnerabilities from your favourite tools such as Nessus & BURP, or even directly via the API. Reports can be generated on-demand and in PDF, DOCX, HTML, CSV, JSON. You can even use your own DOCX templates with the ReportGen tool to create fully customized and localised reports in minutes! AttackForge.com also helps people to start a career in penetration testing. AttackForge provides a secure online environment to create a portfolio of pentests to reflect skills, knowledge, and communication ability in an industry-standard way – to demonstrate to recruiters and future employers that they are ready for the workforce. This may also help to reduce the shortage of supply and skills-gap our industry is currently facing.

</details>

<details><summary><strong>Batea: Digging for gold in network data</strong> — Serge-Olivier Paquette</summary>

**Track:** Network Attacks · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/delvelabs/batea](https://github.com/delvelabs/batea)  
📝 **Description:** Batea is a simple tool that showcases how basic machine learning can help security analysts in their day-to-day operations. It is a context-driven network device ranking framework based on the anomaly detection family of machine learning algorithms. The goal of Batea is to allow security teams to automatically filter interesting network devices in large networks using nmap scan reports. We call those Gold Nuggets. Batea outputs the gold nuggets in order of interest for an attacker given the context of the network. The human challenge is, on the one hand, that a typical enterprise network will host thousands of endpoints, far too many for a few security team members to constantly track and evaluate for their "attractiveness" to a potential intruder. On the other hand, the notion of interest is highly context-sensitive. Batea works by constructing a numerical representation of all devices from your nmap reports (XML) and then applying the Isolation Forest algorithm to uncover the gold nuggets. It is easily extendable by adding specific "features", or interesting characteristics, to the numerical representation of the network elements. The features act as elements of intuition, and the unsupervised anomaly detection methods allow the context of the device, along with the total description of the network, to be used as the central building block of the ranking algorithm. Given that we have taken meaningful elements of intuition all at once, the fact that the Isolation Forest algorithm always takes the whole dataset into consideration ensures that the network context is embedded in the ranking used to predict Gold Nuggets. Pen testers can train the Batea machine learning model from scratch on new network data, or use a model that has been pre-trained on various networks.

</details>

<details><summary><strong>C2 Matrix</strong> — Jorge Orchilles, Bryson Bort</summary>

**Track:** Malware Offense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/JoasASantos/C2Matrix-Automation](https://github.com/JoasASantos/C2Matrix-Automation)  
📝 **Description:** Command and Control is one of the most important tactics in the MITRE ATT&CK matrix as it allows the attacker to interact with the target system and realize their objectives. Organizations leverage Cyber Threat Intelligence to understand their threat model and adversaries that have the intent, opportunity, and capability to attack. Red Team, Blue Team, and virtual Purple Teams work together to understand the adversary Tactics, ﻿Techniques, and Procedures to perform adversary emulations and improve detective and preventive controls. The C2 Matrix was created to aggregate all the Command and Control frameworks publicly available (open-source and commercial) in a single resource to assist teams in testing their own controls through adversary emulations (Red Team or Purple Team Exercises). Phase 1 lists all the Command and Control features such as the coding language used, channels (HTTP, TCP, ﻿DNS, SMB, etc.), agents, key exchange, and other operational security features and capabilities.﻿﻿ This allows more efficient decisions making when called upon to emulate and adversary TTPs. It is the golden age of Command and Control (C2) frameworks. Learn how these C2 frameworks work and start testing against your organization to improve detective and preventive controls.

</details>

<details><summary><strong>git-wild-hunt: Pwn API and leaked secrets</strong> — Rod Soto, Jose Hernandez</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/josehelps/git-wild-hunt](https://github.com/josehelps/git-wild-hunt)  
📝 **Description:** Git Wild Hunt is a tool that allows researchers and security operators to find leaked credentials and secrets in Github covering over 30 types of credentials. This tool is great for cloud security/DevOps security awareness or for cloud security pentesters and red teamers. We will show how deep into an organization or even personal sensitive information can be found by simply starting from leaked credentials in a GitHub project.

</details>

<details><summary><strong>Powerglot: Encoding offensive scripts using polyglots for stego-malware, privilege escalation & lateral movement</strong> — Dr. Alfonso Muñoz</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/mindcrypt/powerglot](https://github.com/mindcrypt/powerglot)  
📝 **Description:** In red-team exercises or offensive tasks, masking of payloads is usually done by using steganography, especially to avoid network level protections, being one of the most common payloads scripts developed in powershell. Recent malware and APTs make use of some of these capabilities: APT32, APT37, Ursnif, Powload, LightNeuron/Turla, Platinum APT, Waterbug/Turla, Lokibot, The dukes (operation Ghost), Titanium, etc. But offensive tools based on steganography need a loader to run the payload. Powerglot tries to reduce this exposition using polyglots in several scenarios. Powerglot is a multifunctional and multi-platform attack and defense tool based on polyglots. Powerglot allows to mask a script (powershell, shellscripting, php, ...) mainly in a digital image, although other file formats are in progress. Unlike the usual offensive tools or malware, Powerglot does not need any loader to execute the "information hidden", minimizing the noise on the target system. PowerGlot has a clear utility in offensive tasks but it is also defined as a discovery and blue team tool. To our knowledge, it is the first general and complete open-source tool that allows to search for the presence of masked information with polyglots, information that could be useful to achieve persistence in a system or to hide malware (stego-malware, privilege escalation, lateral movement, reverse shell, etc.)

</details>

<details><summary><strong>pstf^2: Link Scanners Evasion Made Easy</strong> — Gal BItensky</summary>

**Track:** Malware Offense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/G4LB1T/pstf2](https://github.com/G4LB1T/pstf2)  
📝 **Description:** Link scanners are a critical component in many essential security products, checking whether a URL is malicious or not. It is embedded within email security products, sandbox solutions and as a standalone direct link scanner. This tool will present how to circumvent them all using passive browser fingerprinting - a set of techniques allowing a server to profile a client based only on the request being sent. While often used to detect and repel internet bots, we will show how this fingerprinting can be applied against blue teamers, specifically - how a resourceful attacker may use it to determine if it is being scanned and serve benign content to scanners while delivering harmful content to users. pstf^2 leverages passive fingerprints in HTTP, TCP, IP layers and even link-layer protocols.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>ArcherySec 2.0 - Open Source Vulnerability Assessment and Management</strong> — Anand Tiwari</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/archerysec/archerysec](https://github.com/archerysec/archerysec)  
📝 **Description:** ArcherySec is an opensource vulnerability assessment and management tool which helps developers and pentesters to perform scans and manage vulnerabilities. ArcherySec uses popular opensource tools to perform comprehensive scanning for web applications and networks. It also supports multiple continuous integrations and continuous delivery software. The developers could utilize this tool for the implementation of vulnerability management in the DevOps CI/CD environment. - Perform Web and Network Vulnerability Scanning using opensource tools. - Correlates and Collaborate all raw scans data, shows them in a consolidated manner. - Perform authenticated web scanning. - Vulnerability Management. - Enable REST API's for developers to perform scanning and Vulnerability Management. - JIRA Ticketing System. - Sub domain discovery and scanning. - Periodic scans. - Concurrent scans. - Integrate with CI/CD software.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>0365Squatting</strong> — J Francisco Bolivar, Jose Miguel Gomez</summary>

**Track:** Network Defense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/O365Squad/O365-Squatting](https://github.com/O365Squad/O365-Squatting)  
📝 **Description:** One of the main benefits of cloud technology is to deploy quickly services, with minimum interaction from the administrator side, this is an advantage exploited by cyber criminals too. Nowadays the main threats all size companies are facing is phishing, every day cybercriminals are creating more sophisticated techniques to cheat users and make more difficult the job of blue teams. The most common technique used is typo squatting. Part of the Blue team mission is to detect phishing, typo squatters, and attack domains before the phishing campaign begins, there is outside plenty of tools trying to detect that domains based on DNS, however none of them are focus into the cloud. 0365Squatting is a python tool created to identify that domains before the attack start. The tool can create a list of typo squatted domains based on the domain provided by the user and check all the domains against O365 infrastructure, (these domains will not appear on a DNS request). At the same time, this tool can also be used by red teams and bug bunters, one of the classic attacks is the domain takeover so, the second option of this too is to check if the domain is registered in O365 in order to launch a domain takeover attack.

</details>

<details><summary><strong>CornerShot: Gaining Foresight in Restrictive Networks</strong> — Sagie Dulce</summary>

**Track:** Network Defense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/zeronetworks/cornershot](https://github.com/zeronetworks/cornershot)  
📝 **Description:** Legacy internal networks are usually flat, simple for a red team to cut through, and difficult for blue teams to defend. To fix this problem, modern networks apply zero trust access and network segmentation. This new paradigm presents new challenges not only to attackers but to defenders as well. In such environments, visibility becomes crucial. Which computers can access others and be viable candidates for lateral movement? This question is certainly troubling attackers and red teams, but also defenders and blue teams looking to identify and defend such key network paths. CornerShot utilized a novel technique to discover network access between two remote hosts, without requiring privileged access to those hosts. In modern warfare CornerShot is a weapon that allows a soldier to look past a corner (and possibly take a shot), without actually risking exposure. Similarly, the CornerShot capability allows one to look at another hosts' network access non-intrusively, without risking exposure. CornerShot relies on several, well documented, standard Remote Procedure Call (RPC) methods that are used by various Microsoft services. By using methods that only require a non-privileged authenticated account in the domain, CornerShot is able to trigger network traffic from a destination host to a target. Once traffic is generated, CornerShot is able to determine the remote's port state by measuring the time an RPC call took, and the response it received from the destination host. We will demonstrate real world applications, for example: how to scan an entire network access from a single deployment of CornerShot, and how to validate which BloodHound paths are practical given the underlying network access.

</details>

<details><summary><strong>HosTaGe: mobile honeypots for rapid deployment</strong> — Emmanouil Vasilomanolakis, Shreyas Srinivasa, Eirini Lygerou</summary>

**Track:** Network Defense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/aau-network-security/HosTaGe](https://github.com/aau-network-security/HosTaGe)  
📝 **Description:** HosTaGe is a lightweight, low-interaction, and portable honeypot for mobile devices that aims on the detection of malicious network environments. As most malware propagate over the network via specific protocols, a low-interaction honeypot located at a mobile device can check wireless networks for actively propagating malware. HosTaGe supports many commonly used protocols (e.g. HTTP, TELNET, SSH) along with many IoT/ICS specific ones (e.g. MQTT, S7COMM, MODBUS). We envision such honeypots running on all kinds of mobile devices to provide a quick assessment on the potential security state of a network.

</details>

<details><summary><strong>NEW TSURUGI LINUX ACQUIRE & DIGITAL FORENSIC ACQUISITIONS</strong> — Giovanni Rattaro, Marco Giorgi</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/mesquidar/ForensicsTools](https://github.com/mesquidar/ForensicsTools)  
📝 **Description:** Tsurugi ACQUIRE is a dedicated Linux OS to perform DIGITAL FORENSIC acquisition before to start post mortem DFIR investigations.

</details>

<details><summary><strong>Strafer: A Tool to Detect Infections in Elasticsearch Instances</strong> — Aditya K Sood, Rohit Bansal</summary>

**Track:** Malware Defense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/adityaks/strafer](https://github.com/adityaks/strafer)  
📝 **Description:** Elasticsearch infections are rising exponentially. The adversaries are exploiting open and exposed Elasticsearch interfaces to trigger infections in the cloud and non-cloud deployments. During this talk, we will release a tool named "STRAFER" to detect potential infections in the Elasticsearch instances. The tool allows security researchers, penetration testers, and threat intelligence experts to detect compromised and infected Elasticsearch instances running malicious code. The tool also enables you to conduct efficient research in the field of malware targeting cloud databases. In this version of the tool, the following modules are supported: Elasticsearch instance information gathering and reconnaissance Elasticsearch instance exposure on the Internet Detecting potential ransomware infections in the Elasticsearch instances Detecting potential botnet infections such as meow botnet. Detecting infected indices in the Elasticsearch instances Note: This is the first release of the tool and we expect to add more modules in the nearby future.

</details>

<details><summary><strong>Telfhash: Hunting IoT elves</strong> — Fernando Mercês</summary>

**Track:** Malware Defense · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/trendmicro/telfhash](https://github.com/trendmicro/telfhash)  
📝 **Description:** Telfhash is an architecture-agnostic hash based on symbols of ELF files. It can also cluster ELF files with no symbols based on a creative algorithm to cluster them. Designed as a Python library, Telfhash is also shipped with a command-line tool that allows malware researchers to correctly group similar ELF files together. In this demo I'll show you how Telfhash works and how to extract the most of it while conducting malware investigations that involves ELF files, which is a common situation in this IoT/non-PC malware era.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>BLE hardware-less hackme</strong> — Slawomir Jasek</summary>

**Track:** Internet Of Things · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/smartlockpicking/BLE_HackMe](https://github.com/smartlockpicking/BLE_HackMe)  
📝 **Description:** The new, free tool aims to help getting familiar with the very basics of ubiquitous Bluetooth Low Energy technology and its (in)security - without the need of any dedicated hardware. It is based on a specially designed software (running on a typical Windows 10 laptop) - which simulates a BLE device, on the radio layer working exactly the same as a real one. The simulated device contains several "hackme" challenges of increasing level: starting with simple communication protocol introduction up to unlocking smart locks. Most of these challenges can be solved using nothing more than just a free mobile application, which connects via Bluetooth to the laptop running simulated device. This unique approach makes the fun available for everyone who would like to start the journey into fascinating vulnerabilities of BLE devices, but is afraid of gearing up with special hardware or steep learning curve for advanced tools. The basics possible to grasp using the introduced hackme can however be easily applicable to take control of surprisingly lot of real devices surrounding us.

</details>

<details><summary><strong>efi_fuzz: Groundwork to the Metaphysics of coverage-guided UEFI fuzzing</strong> — Assaf Carlsbad, Itai Liba</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/Sentinel-One/efi_fuzz](https://github.com/Sentinel-One/efi_fuzz)  
📝 **Description:** In recent years, firmware-level attacks against UEFI have grown in popularity and became more and more complex. Prominent examples for such attacks from this year alone include CVE-2020-12890 (SMM callout vulnerability in AMD's Mini PCs), CVE-2020-10713 (BootHole, an effective bypass for Secure Boot) as well as the discovery of a new UEFI implant, dubbed MosaicRegressor. As a growing area of concern, these UEFI vulnerabilities shouldn't be taken lightly. Given any of these vulnerabilities, an attacker can get extremely stealthy persistence on the machine, while bypassing many traditional kernel-based or even hypervisor-based mitigations. Unfortunately, the set of tools available to the UEFI research community is still in its infancy phase. As a result, most of the research so far was driven by static analysis of UEFI modules or by leveraging some ad-hoc "dumb" fuzzers. Obviously, these approaches have some serious limitations and downsides: static analysis, while not complemented by dynamic analysis, is limited at best and "dumb" fuzzers don't get any feedback from the fuzzed target and as a result are likely to miss key vulnerabilities. In this talk we'll present efi_fuzz: a modern, coverage-guided fuzzer for UEFI modules based on the Qiling emulation framework and the AFL++ fuzzing engine. The fuzzer is currently capable of fuzzing the contents NVRAM variables and further work is being made to support fuzzing of other attack vectors such as SWSMIs.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Qiling Framework: Deep Dive Into Obfuscated Binary Analysis</strong> — Kai Jern Lau, ChenXu Wu, ZiQiao kong</summary>

**Track:** Reverse Engineering · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/qilingframework/qiling](https://github.com/qilingframework/qiling)  
📝 **Description:** Modern obfuscation techniques are getting more and more challenged. Existing static techniques are no longer sufficient to analyze binary in heavy obfuscated form. To address this issue, we have to provide security analysts with the ability to perform high-fidelity emulation and sophisticated binary instrumentation framework. Qiling Framework (https://qiling.io) is an advanced sandboxed emulator framework. It encloses a rich set of Python APIs that allow security analysts to develop highly customizable analysis tools with minimal implementation efforts. With the facilitation of the emulation technology in Qiling, our engine can run arbitrary executables in a cross-platform-architecture fashion. As such, security analysts could use it to analyze various executable file-formats, including Windows PE, MachO, ELF, UEFI, MBR, etc. Since we released Qiling Framework in Nov 2019, our project has received significant attention from the community. Currently, we have about 60+ contributors and almost 1,700 followers on GitHub. This session shares the latest update on Qiling Framework, focusing on deobfuscating binaries. We will demonstrate how we can provide instant support for presenting code execution flow in the form of intermediate representations (e.g., IDA Pro or R2). Thanks to some advanced features of Qiling Framework, security analysts can use a series of newly added APIs to ease their efforts in reverse engineering. To conclude, we have few live demos to show how to deal with some real sophisticated binaries. I. Syscall, Operating System API and Library Hijack We will demonstrate how we can use different APIs in Qiling Framework to intercept a binary function and hijack its execution. By intercepting a binary function, we meant intercepting a library function or syscall at the stage of pre-execution, execution, and post-execution, without the restrictions imposed by the OS or underlying computing architecture. II. Save and Restore Current Binary Emulation States Sophisticated binaries impose significant challenges for reverse engineering. With the facilitation of a save-and-restore feature in Qiling Framework, security analysts are able to save and resume an emulation state at any stage. This provides the reverse engineering professionals with the ability to avoid repeatedly running a binary from the beginning state. Given the program state entering into a branch (e.g., taking a jump with jz, jnz, and other branch-taken instructions), Qiling can always save the necessary program state and enable program resume later on. III. ollvm de-flattern techniques ollvm is a well-known obfuscation tool. One of its obfuscation techniques is Control Flow Flattening. With Qiling emulation, we can search real control flow and restore it easily. Thanks to the newly added feature to present control flow in an intermediate representation (like IDA microcode API, R2 ESIL, VEX, and etc), the new version of Qiling will make such de-flattern techniques cross-architecture.

</details>

<details><summary><strong>Tracee: Linux malware tracing and forensics using eBPF</strong> — Yaniv Agman, Idan Revivo</summary>

**Track:** Reverse Engineering · **Event:** Europe 2020  
🔗 **Link:** [https://github.com/aquasecurity/tracee](https://github.com/aquasecurity/tracee)  
📝 **Description:** Tracee is a system tracing tool, focused on malware related behaviours. Using eBPF technology of the Linux kernel, Tracee can trace selected system calls and internal kernel functions. Other than tracing, Tracee is also capable of capturing files written to disk or memory (e.g. "fileless" malwares), and extracting binaries that are dynamically loaded to an application's memory (e.g. when a malware uses a packer). With these features, it is possible to quickly gain insights about the running processes that previously required the use of dynamic analysis tools and special knowledge.

</details>

---
