# USA 2024
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2024** event held in **USA**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [⚙️ Miscellaneous / Lab Tools](#⚙️-miscellaneous-lab-tools)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
---
## 🔵 Blue Team & Detection
<details><summary><strong>Active Directory Cyber Deception using Huginn</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rohan Durve](https://img.shields.io/badge/Rohan%20Durve-informational) ![Paul Laine](https://img.shields.io/badge/Paul%20Laine-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Attack Path Based Detection Engineering with FalconHound</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Olaf Hartong](https://img.shields.io/badge/Olaf%20Hartong-informational)

🔗 **Link:** [Attack Path Based Detection Engineering with FalconHound](https://github.com/olafhartong/Presentations)  
📝 **Description:** Dive deep into the world of BloodHound, a tool that has revolutionized the way we identify and analyze attack paths. Despite its benefits, we encounter many teams that struggle to maximize its potential due to time constraints or knowledge gaps. This talk aims to bridge these gaps, unveiling tips and tricks to keep your BloodHound database up-to-date and use it for automatic detection and enrichment.

We're excited to introduce you to FalconHound, a toolkit designed to augment BloodHound's capabilities. Discover how FalconHound integrates with a host of security tools, offering features like tracking sessions, environment changes, alerts, and incidents - all in near-real time!
Embrace the power of bi-directional contextual information to prioritize critical alerts better and stop attackers in their tracks before they reach their goal. Learn how tools like BloodHound and FalconHound can serve as extensions of your live monitoring capabilities, helping you catch attackers in real-time and limit the impact of breaches. One of the coolest features is the ability to track active lateral movement, which allows the possibility to stop an attacker in their tracks.

</details>

<details><summary><strong>cloudgrep</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Christopher Doman](https://img.shields.io/badge/Christopher%20Doman-informational)

🔗 **Link:** Not Available  
📝 **Description:** cloudgrep searches cloud storage.

It currently supports searching log files, optionally compressed with gzip (.gz) or zip (.zip), in AWS S3, Azure Storage or Google Cloud Storage.

Why build this?
Directly searching cloud storage, without indexing logs into a SIEM or Log Analysis tool, can be faster and cheaper.
There is no need to wait for logs to be ingested, indexed, and made available for searching.
It searches files in parallel for speed.
This may be of use when debugging applications, or investigating a security incident.

</details>

<details><summary><strong>DOLOS-T (Deceptive Operations: Lure, Observe, and Secure Tool)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Federico Pacheco](https://img.shields.io/badge/Federico%20Pacheco-informational) ![Joaquin Lanfranconi](https://img.shields.io/badge/Joaquin%20Lanfranconi-informational) ![Diego Staino](https://img.shields.io/badge/Diego%20Staino-informational)

🔗 **Link:** Not Available  
📝 **Description:** DOLOS-T (named after Dolos, the Greek god of deception) is an orchestration platform for cyber deception operations that allows deploying realistic high and medium interaction decoys and services to detect threats in the operational infrastructure. It can be deployed in a remote or local environment, and through network traffic redirections, it allows the services to appear to be deployed locally. This enables implementation of deception strategies even in critical production environments with an acceptable level of risk and exposure. The goal is to create realistic environments to detect the target as a decoy. The main strategy is not to hide the service as a decoy, but to detect anomalous behavior early within the environment.

Features:
-Creation of objects that model the goals, storytelling, and context for cyber deception operations and define decoy services with realistic information.
-Automated deployment of decoys with fake user-provided data to create confusion, increase ambiguity, and detect attackers early.
-Breadcrumb and honeytoken tracking panel to support a realistic story.
-Dynamic environments generation that can be easily deployed, discarded, or redefined.
-Centralized log collection to monitor decoy usage activity.
-IoCs from collected logs for attacker engagement.
-Mutation mechanisms to make changes to the environment, such as new services based on detection, self-destruction, and modification of decoy container resources.
-Guidance panel to track design, definitions, and decisions, which helps manage the operations lifecycle.
-First open-source tool of its kind.

The tool is based on our research paper that will be presented at the IEEE ARGENCON 2024 academic conference, titled "Proposal for the implementation of minimalistic cyber deception strategies" (preprint available at IEEE TechRxiv and ResearchGate, DOI: http://dx.doi.org/10.13140/RG.2.2.34289.29289).

Use cases:
-Application server and backend
-Workstations and internal services
-VPN type access.

</details>

<details><summary><strong>Enhance Your Linux DFIR with MasterParser</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Eilay Yosfan](https://img.shields.io/badge/Eilay%20Yosfan-informational)

🔗 **Link:** [Enhance Your Linux DFIR with MasterParser](https://github.com/YosfanEilay)  
📝 **Description:** MasterParser stands as a robust Digital Forensics and Incident Response tool meticulously crafted for the analysis of Linux logs within the var/log directory. Specifically designed to expedite the investigative process for security incidents on Linux systems, MasterParser adeptly scans supported logs, such as auth.log for example, extract critical details including SSH logins, user creations, event names, IP addresses and much more. The tool's generated summary presents this information in a clear and concise format, enhancing efficiency and accessibility for Incident Responders. Beyond its immediate utility for DFIR teams, MasterParser proves invaluable to the broader InfoSec and IT community, contributing significantly to the swift and comprehensive assessment of security events on Linux platforms.

</details>

<details><summary><strong>GenAi VS Phishing</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jordan Garzon](https://img.shields.io/badge/Jordan%20Garzon-informational) ![Omer Yanovich](https://img.shields.io/badge/Omer%20Yanovich-informational)

🔗 **Link:** Not Available  
📝 **Description:** Why does phishing still exist? Despite being one of the oldest types of cyberattacks, it continues to be effective. Cybersecurity remains a constant game of cat and mouse between the white and black hats with both sides continuously developing new strategies to outmaneuver each other. However, the past year marked a significant shift with the implementation of new generative AI models.
How does our brain identify a phishing website? By appearance! If a random domain closely resembles Facebook's login page or a login page of a bank website, it's probably phishing - That's the simple criterion.

We've developed a tool to detect phishing using these generative AI technologies and can "visually" analyze websites. Excitingly, the tool can run in real-time, catching most advanced phishing websites and enabling responses within milliseconds.

Introducing LooksPhishy, currently deployed in production. This tool offers complete customization, enabling the choice of target brands for detection, the option to focus on either logos or the full webpage, and the selection of the most suitable embedding model and LLM. It also gives a description of phishing type (E.g Fake finance website, Mimic login page of Microsoft, Fake shopping website..). It comes equipped with numerous examples for educational purposes and integrates seamlessly into any stack!

</details>

<details><summary><strong>Information-based Heavy Hitters for Real-time DNS Exfiltration Detection</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yarin Ozery](https://img.shields.io/badge/Yarin%20Ozery-informational)

🔗 **Link:** [Information-based Heavy Hitters for Real-time DNS Exfiltration Detection](https://github.com/akamai/Information-based-Heavy-Hitters-for-Real-Time-DNS-Exfiltration-Detection)  
📝 **Description:** DNS exfiltration is a method used by attackers to covertly steal sensitive data from a target network, such as credit card details from point-of-sale machines or passwords and credentials from compromised hosts, by abusing the DNS protocol. In a typical DNS exfiltration attack, a host within the target network is first compromised by a threat actor's malware. Once inside, the malware manipulates the system to send DNS queries containing the stolen data to a DNS authoritative nameserver controlled by the attacker. This is done by encoding the data within the DNS queries. Moreover, bidirectional communication channels can be established by utilizing the DNS response to send instructions to the infected host, which can be used for command-and-control (C&C) purposes.

The Information-based Heavy Hitter (ibHH) method is a novel approach developed to facilitate real-time detection of DNS exfiltration attacks, enabling swift mitigation before substantial data exfiltration occurs. ibHH has been designed to run directly on recursive DNS resolvers, performing inline detection of DNS exfiltration domains without impacting the resolver's DNS resolution performance. To achieve this, ibHH leverages sketching algorithms such as HyperLogLog and weighted sampling techniques commonly utilized in the realm of big data analysis. ibHH estimates the amount of information potentially transmitted to registered domains and raise alerts for domains suspected of being used for data exfiltration, allowing for prompt blocking of malicious domains. A comprehensive evaluation of the method on large-scale real-world data, consisting of over 250 billion DNS queries from real enterprise networks, shows that it can successfully detect DNS exfiltration domains while experiencing a small number of false positive alerts.

This tool demonstrates the ibHH algorithm's capabilities to detect realistic DNS exfiltration attacks in real-time

</details>

<details><summary><strong>LDAP Firewall</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dekel Paz](https://img.shields.io/badge/Dekel%20Paz-informational) ![Sagie Dulce](https://img.shields.io/badge/Sagie%20Dulce-informational)

🔗 **Link:** Not Available  
📝 **Description:** The Lightweight Directory Access Protocol (LDAP) is used in Windows domain environments to interact with the Active Directory schema, allowing users to query information and modify objects (such as users, computers, and groups). For a Windows environment to properly function, LDAP must be left open on the Domain Controllers and be accessible to all users of the domain. As only limited logs are available for LDAP, and it is impossible to natively harden the LDAP configuration, the environment is at a constant risk.

LDAP Firewall is an open-source tool for Windows servers that lets you audit and restrict incoming LDAP requests. Its primary use cases are to protect Domain Controllers, block LDAP-based attacks (such as BloodHound and sAMAccountName spoofing), and tightly control access to the Active Directory schema.

We will present the LDAP Firewall, demonstrating how it defends against previously un-detectable attacks by hardening and monitoring the DC servers. We will also discuss the reverse-engineering process of the Windows LDAP library, how the protocol works, and the technical details of the LDAP Firewall.

</details>

<details><summary><strong>Lightgrep</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jon Stewart](https://img.shields.io/badge/Jon%20Stewart-informational) ![Julia Paluch](https://img.shields.io/badge/Julia%20Paluch-informational)

🔗 **Link:** Not Available  
📝 **Description:** Lightgrep is a multipattern regular expression tool for searching binary data streams, designed for digital forensics. It can search for Unicode-aware patterns in UTF-8, UTF-16, and over 100+ older encodings, including CP-1256, ISO 88599-5, and GB 18030, simultaneously, in binary and mixed-encoding data. As an automata-based engine, it provides reliable operation and copes with large pattern sets, all while adhering to well-known PCRE matching semantics.

Lightgrep has been an open source library and embedded in bulk_extractor for over a decade. It's once again under active development, with new bug fixes and performance improvements. Lightgrep is also now a useful command-line tool in its own right, with features for generating histograms, extracting hit context, and processing logs. Lightgrep is perfectly happy to search binaries, multi-GB logs, foreign language text, memory images, disk images, or unallocated clusters, for thousands of patterns.

Come to this lab to see lightgrep in action and learn to find what you're looking for, quickly and easily.

</details>

<details><summary><strong>Malicious Executions: Unmasking Container Drifts and Fileless Malware with Falco</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Stefano Chierici](https://img.shields.io/badge/Stefano%20Chierici-informational) ![Lorenzo Susini](https://img.shields.io/badge/Lorenzo%20Susini-informational)

🔗 **Link:** Not Available  
📝 **Description:** Containers are the most popular technology for deploying modern applications. SPOILER ALERT: bypassing well-known security controls is also popular. In this talk, we explain how to use the recent updates in Falco, a CNCF open-source container security tool, to detect drifts and fileless malware in containerized environments.

As a best practice, containers should be considered immutable. Early this year, Falco introduced new features to detect container drift via OverlayFS, which can spot if binaries are added or modified after the container's deployment. New binaries are often a sign of an ongoing attack.

Of course, attackers can also use more advanced evasion techniques to stay hidden. By using in-memory, fileless execution, attackers can bypass most of the security controls such as drift detection and still reach their goals with no stress.

To combat fileless attacks, Falco has also added memfd-based fileless execution thanks to its visibility superpowers on Linux kernel system calls. Combining Falco's existing runtime security capabilities with these two new detection layers forms the foundation of an in-depth defense strategy for cloud-native workloads.

We will walk you through real-world scenarios based on recent threats and malware, demoing how Falco can help detect and respond to these malicious behaviors and comparing both drift and fileless attack paths.

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

<details><summary><strong>Network Threat Hunting with SELKS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![None](https://img.shields.io/badge/None-informational)

🔗 **Link:** [Network Threat Hunting with SELKS](https://github.com/StamusNetworks/SELKS/wiki/Docker)  
📝 **Description:** SELKS is a free, open-source, and turn-key Suricata network intrusion detection/protection system (IDS/IPS), network security monitoring (NSM) and threat hunting implementation created and maintained by Stamus Networks.

On the 10th anniversary of its introduction (April 30, 2024) Stamus Networks announced SELKS 10 - which introduced powerful new threat hunting capabilities which will be demonstrated during this session.

</details>

<details><summary><strong>Some Call Me TIM: A Novel, Lightweight Triage and Investigation Platform</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Austin Baker](https://img.shields.io/badge/Austin%20Baker-informational) ![Nick Deneweth](https://img.shields.io/badge/Nick%20Deneweth-informational)

🔗 **Link:** Not Available  
📝 **Description:** SOC anaylsts, threat hunters, and detection engineers have the same core challenge: how can I triage and/or investigate suspicious activity, at scale, while ensuring that all of the work I do goes back into the system to improve future outcomes? TIM is a novel, lightweight triage and investigation platform that enables analysts of all types - SOC, TI, etc. - to quickly pivot and curate relevant events across any kind of data source in comfortable, unintrusive interface. Powered by AGGrid, TIM gives analysts the ability to own their workflows and open up avenues to collaboration that don't exist in the market today.

</details>

<details><summary><strong>Splunk Attack Range</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational) ![Patrick Bareiss](https://img.shields.io/badge/Patrick%20Bareiss-informational)

🔗 **Link:** [Splunk Attack Range](https://github.com/splunk/attack_range/blob/develop/README.md)  
📝 **Description:** The Splunk Attack range is a open-source framework that provides different tools to allow security analysts to test networks, hosts, and applications against several known adversarial TTPs based on Mitre ATT&CK framework. The Splunk Attack Range framework allows the security analyst to quickly and repeatedly replicate and generate data as close to "ground truth" as possible, in a format that allows the creation of detections, investigations, knowledge objects, and SOAR playbooks. The Splunk Attack Ranges contain adversarial simulation engines (Operator, Atomic Red Team), target machines, and a Splunk server receiving attack data which can be downloaded and used for free and provides operators with tools to simulate attacks and create detections and defense artifacts.

</details>

<details><summary><strong>Traceeshark - Interactive System Tracing & Runtime Security using eBPF</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ofek Shaked](https://img.shields.io/badge/Ofek%20Shaked-informational) ![Asaf Eitani](https://img.shields.io/badge/Asaf%20Eitani-informational)

🔗 **Link:** Not Available  
📝 **Description:** Traceeshark brings the world of Linux runtime security monitoring and advanced system tracing to the familiar and ubiquitous network analysis tool Wireshark.

It is now possible, using Wireshark, to record an immense variety of system events using Aqua Security's eBPF based runtime security tool Tracee, and analyze them interactively.

Tracee is a runtime security and forensics tool for Linux, utilizing eBPF technology to trace systems and applications at runtime, analyze collected events to detect suspicious behavioral patterns, and capture forensics artifacts. Up until now, a typical workflow using Tracee involved running Tracee from the CLI, perform some activity, stop Tracee, dump its logs to a file, and analyze the file using command line tools or scripting languages. Analyzing packets captured by Tracee was done separately, and in general the entire process was very manual.

Now, events generated by Tracee can be analyzed interactively using Wireshark's advanced capabilities, which include interactive filtering, displaying statistics and performing advanced data aggregations. Traceeshark also provides the ability to capture events using Tracee directly from Wireshark and have them stream in like a network capture. Another game-changing feature is the ability to analyze system events side by side with network packets generated by Tracee that contain rich context about the system process and container they belong to.

The combination of Tracee's wide use in the security industry and its advanced system tracing and forensic capabilities, together with Wireshark's universal popularity in the entire IT industry, its maturity and ease of use, opens up a whole new world of capabilities for dynamic malware analysis, forensics, kernel hacking and more.

</details>

<details><summary><strong>TrafficWardenX: OpenWRT Security & Monitoring</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sampad Adhikary](https://img.shields.io/badge/Sampad%20Adhikary-informational) ![Tripti Sharma](https://img.shields.io/badge/Tripti%20Sharma-informational)

🔗 **Link:** Not Available  
📝 **Description:** TrafficWardenX is a comprehensive open-source tool tailored for enhancing the security and monitoring capabilities of OpenWRT-enabled networks. With a focus on intuitive analytics and user engagement, TrafficWardenX delivers essential insights and control for maintaining robust network health.

</details>

<details><summary><strong>vArmor: A Sandbox System for Hardening Cloud-Native Containers</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Wei Wei](https://img.shields.io/badge/Wei%20Wei-informational) ![ChangHao Li](https://img.shields.io/badge/ChangHao%20Li-informational)

🔗 **Link:** Not Available  
📝 **Description:** With the rise of cloud-native technologies, organizations are increasingly migrating critical business services to Kubernetes environments. Some are leveraging Kubernetes and Linux containers to create multi-tenant environments. Consequently, enhancing Linux container isolation, mitigating high-risk vulnerabilities, and defending against container environment infiltration have become focal points in cloud-native security.

In response to this growing need for security, our team has developed vArmor, a robust container sandbox solution tailored specifically for cloud-native environments. By leveraging technologies such as AppArmor LSM, BPF LSM, Seccomp, and Kubernetes Operator, vArmor abstracts the underlying complexities of AppArmor/BPF/Seccomp enforcers. This enables users to deploy and use vArmor seamlessly within their application ecosystem, enforcing access controls on container file access, process execution, network communication, system calls, and more.

vArmor supports the combination of multiple enforcers for Linux container protection. It offers various policy modes with dynamic updates, built-in rules, and customizable interfaces for access control in an "Allow by Default" manner. Additionally, it supports behavior modeling to collect container actions and generate models. Furthermore, it can enforce access control on containers in a "Deny by Default" manner based on behavior models.

With vArmor, securing your cloud-native applications is as straightforward as it gets. Say goodbye to complex security setups and hello to enhanced protection without compromising performance.

</details>

<details><summary><strong>Ōkami: Advanced Binary Fingerprinting for Malware Attribution and Code Sharing Detection</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Vishal Thakur](https://img.shields.io/badge/Vishal%20Thakur-informational) ![Benjamyn Whiteman](https://img.shields.io/badge/Benjamyn%20Whiteman-informational)

🔗 **Link:** Not Available  
📝 **Description:** Okami is a cutting-edge tool designed to enhance malware research and cybersecurity analysis. The core functionality of Okami lies in its ability to export and individually hash all subroutines within a binary. These hashes serve as a unique fingerprint, enabling a comprehensive comparison against a database of known binaries. It empowers researchers to meticulously use disassembled code to build a database of malicious files and then use the tool to compare new samples against that database for attribution. Okami works with renowned frameworks like Capstone and Ghidra. The tool will be released at BlackHat 2024, USA and will be fully open-sourced with the entire codebase available on GitHub.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>ADOKit: Azure DevOps Services Attack Toolkit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Brett Hawkins](https://img.shields.io/badge/Brett%20Hawkins-informational)

🔗 **Link:** [ADOKit: Azure DevOps Services Attack Toolkit](https://github.com/xforcered/ADOKit)  
📝 **Description:** Development Operations (DevOps) platforms continue to be high-value systems that attackers target through software supply chain attacks and source code theft attacks. Azure DevOps Services has become one of the popular DevOps platforms due to organizations adopting cloud solutions more heavily. Logging and detecting attacker activity in cloud-based services has become more important than ever, as shown in the attacks conducted by the Storm-0558 threat actor group against Microsoft cloud-based services.

This presentation will show ADOKit, a toolkit that can be used to attack Azure DevOps Services. ADOKit allows the user to specify an attack module, along with specifying valid credentials (API key or stolen authentication cookie) for the respective Azure DevOps Services instance. The attack modules supported include reconnaissance, privilege escalation and persistence. ADOKit was built in a modular approach, so that new modules can be added in the future by the information security community. As part of this presentation, new modules will be publicly released.

</details>

<details><summary><strong>Adversary emulation for the cloud with Stratus Red Team</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Christophe Tafani-Dereeper](https://img.shields.io/badge/Christophe%20Tafani-Dereeper-informational) ![Andrew Krug](https://img.shields.io/badge/Andrew%20Krug-informational)

🔗 **Link:** Not Available  
📝 **Description:** What attacks are used by threat actors in cloud environments? How to reproduce them easily to ensure that our threat detection mechanisms are working as expected?

Stratus Red Team provides a solution to these two questions. With support for AWS, Azure, Google Cloud and Kubernetes, it allows threat detection and cloud security engineering team to reproduce common cloud attacks in a self-contained manner, along with actionable detection insights.

</details>

<details><summary><strong>BadZure: Simulating and Exploring Entra ID Attack Paths</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

🔗 **Link:** [BadZure: Simulating and Exploring Entra ID Attack Paths](https://github.com/mvelazc0/BadZure)  
📝 **Description:** BadZure is an open-source PowerShell tool designed for Entra ID (previously known as Azure AD) security analysis. It automates the creation of vulnerable Entra ID tenant environments by utilizing the Microsoft Graph SDK. The tool configures users, groups, and application registrations, then introduces security misconfigurations to simulate attack paths. Aimed at security researchers and practitioners, BadZure facilitates conducting attack simulations, testing defenses, and enhancing the cybersecurity community's understanding of Entra ID attack vectors

</details>

<details><summary><strong>BOAZ, Yet Another Layered Evasion Tool: Evasion Tool Evaluations and AV Testing</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Thomas Xuan Meng](https://img.shields.io/badge/Thomas%20Xuan%20Meng-informational) ![Richard Macfarlane](https://img.shields.io/badge/Richard%20Macfarlane-informational)

🔗 **Link:** [BOAZ, Yet Another Layered Evasion Tool: Evasion Tool Evaluations and AV Testing](https://github.com/lihebi/biber-dist/blob/master/cs.LG/cs.LG-2019-04.bib)  
📝 **Description:** In the rapidly evolving landscape of cybersecurity, there has been an increasing deployment of evasion techniques in organizational vulnerability assessments and found post-discovery of security incidents, owing to the more sophisticated defense mechanisms. However, there is no consensus on how antivirus (AV) performance against evasion methods and techniques can be methodically evaluated.

Antivirus (AV) solutions, serving as the last line of defense on users' endpoint devices, have evolved into highly complex entities, often operated as 'black boxes' from the user's perspective due to proprietary and security reasons. This dynamic places researchers and attackers in similar positions. While malware authors can fingerprint AV detection mechanisms through various evasion techniques, researchers can employ similar methods to identify improvement opportunities in security products.

Our study aims to bridge the gap in empirical research on the performance of up-to-date antivirus solutions against evasion frameworks and methods in the latest Windows environment with all defense features enabled. As a by-product of this study, I developed a custom evasion framework named BOAZ, which served as an additional and flexible AV evaluation tool. This framework is complemented by a comprehensive suite of 17 evasion tools, evaluated against 71 online AV engines and 14 carefully selected desktop AV solutions. The experiment results revealed significant insights: the successful compromise of contemporary AVs can be achieved by understanding the building blocks of evasion detections and strategically combining existing evasion methods, without requiring advanced programming skills or zero-day exploits. Moreover, the study revealed the iterative relationship between signature and behavioral detections across detection phases.

</details>

<details><summary><strong>BucketLoot - An Automated S3 Bucket Inspector</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Syed UmairUddin Nehri](https://img.shields.io/badge/Syed%20UmairUddin%20Nehri-informational) ![Kunal Agrawal](https://img.shields.io/badge/Kunal%20Agrawal-informational)

🔗 **Link:** Not Available  
📝 **Description:** Thousands of S3 buckets are left exposed over the internet, making it a prime target for malicious actors who may extract sensitive information from the files in these buckets that can be associated with an individual or an organisation. There is a limited research or tooling available that leverages such S3 buckets for looking up secret exposures and searching specific keywords or regular expression patterns within textual files.
BucketLoot is an automated S3 Bucket Inspector that can simultaneously scan all the textual files present within an exposed S3 bucket from platforms such as AWS, DigitalOcean etc. It scans the exposed textual files for:
- Secret Exposures
- Assets (URLs, Domains, Subdomains)
- Specific keywords | Regex Patterns (provided by the user)
The end user can even search for string based keywords or provide custom regular expression patterns that can be matched with the contents of these exposed textual files. All of this makes BucketLoot a great recon tool for bug hunters as well as professional pentesters.
The tool allows users to save the output in a JSON format which makes it easier to pass the results as an input to some third-party product or platform.

</details>

<details><summary><strong>Cloud Offensive Breach and Risk Assessment (COBRA)</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational) ![Harsha Koushik](https://img.shields.io/badge/Harsha%20Koushik-informational)

🔗 **Link:** [Cloud Offensive Breach and Risk Assessment (COBRA)](https://github.com/PaloAltoNetworks/cobra-tool)  
📝 **Description:** Cloud Offensive Breach and Risk Assessment (COBRA) is an open-source tool designed to empower users to simulate attacks within multi-cloud environments, offering a comprehensive evaluation of security controls. By automating the testing of various threat vectors including external and insider threats, lateral movement, and data exfiltration, COBRA enables organizations to gain insights into their security posture vulnerabilities. COBRA is designed to conduct simulated attacks to assess an organization's ability to detect and respond to security threats effectively.

# COBRA Features

1. Seamless Integration for POC and Tool Evaluation: COBRA provides seamless integration for Proof of Concept (POC) and tool evaluation purposes. Whether you're exploring new cloud-native applications or evaluating existing solutions, COBRA offers a user-friendly interface and flexible deployment options to facilitate effortless testing and assessment.

2. Comprehensive Assessment of Cloud-Native Security Posture: Gain unparalleled insights into your organization's existing cloud-native security posture with COBRA. Our advanced assessment capabilities enable you to identify vulnerabilities, assess security controls, and pinpoint areas for improvement. By understanding your current security posture, you can proactively address gaps and strengthen your defenses against emerging threats.

3. Benchmarking Against Industry Standards and Best Practices: COBRA enables you to benchmark your cloud security controls against industry standards and best practices. With our comprehensive benchmarking framework, you can compare your security posture against established benchmarks, identify areas of strength and weakness, and prioritize remediation efforts accordingly.

4. Actionable Insights and Recommendations: COBRA goes beyond providing insights by providing a report delivering actionable recommendations tailored to your organization's specific needs.

5. Continuous Threat Simulation: COBRA offers a modular and templatized approach for users to easily integrate additional modules, allowing for continuous threat simulation and adaptability, by providing a flexible framework for adding modules, COBRA ensures that users can tailor their threat simulation capabilities according to evolving security needs.

</details>

<details><summary><strong>Damn Vulnerable UEFI (DVUEFI): An Exploitation Toolkit and Learning Platform for Unveiling and Fixing UEFI Firmware Vulnerabilities</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Stanislav Lyakhov](https://img.shields.io/badge/Stanislav%20Lyakhov-informational) ![Mickey Shkatov](https://img.shields.io/badge/Mickey%20Shkatov-informational)

🔗 **Link:** Not Available  
📝 **Description:** Inspired by projects such as Damn Vulnerable Web Application and OWASP's Damn Vulnerable Web Sockets, Damn Vulnerable UEFI (DVUEFI) is designed to help guide ethical hackers, security researchers, and firmware enthusiasts in getting started with UEFI firmware security, by facilitating the exploration of vulnerabilities by example. The DVUEFI project is engineered to simulate real-world firmware attacks, offering an environment for practicing and refining exploitation techniques. DVUEFI is accompanied by a robust, continuously evolving catalog of documented UEFI vulnerabilities. Each entry is detailed with exploitation methods, potential impacts, and strategic mitigation recommendations, serving as both a learning tool and a reference for security practitioners.

</details>

<details><summary><strong>DarkWidow: Customizable Dropper Tool Targeting Windows</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Soumyanil Biswas](https://img.shields.io/badge/Soumyanil%20Biswas-informational) ![Chirag Savla](https://img.shields.io/badge/Chirag%20Savla-informational)

🔗 **Link:** Not Available  
📝 **Description:** This is a Dropper/Post-Exploitation Tool targeting Windows machine.

</details>

<details><summary><strong>Echidna: Penetration Test Assist & Collaboration Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![YU Terada](https://img.shields.io/badge/YU%20Terada-informational) ![Soya Aoyama](https://img.shields.io/badge/Soya%20Aoyama-informational)

🔗 **Link:** [Echidna: Penetration Test Assist & Collaboration Tool](https://github.com/epavlick/turker-demographics/blob/master/dictionaries/all/dictionary.ja)  
📝 **Description:** Echidna is a tool designed to support teams or beginners in conducting penetration testing.
While there are many tools available to assist or automate penetration testing, mastering them requires knowledge of numerous commands and techniques, making it challenging for beginners to learn and carry out penetration testing. Furthermore, when conducting penetration tests in a team, each member tends to work independently, which can lead to duplication of work and lack of visibility of progress for managers and beginners.
Therefore, we developed Echidna, which visualizes and shares the terminal console of penetration testers, and recommends the next command based on each situation. Echidna allows us to attack machines with just clicks, making it possible even for students and beginners to learn attack methods.

</details>

<details><summary><strong>Gato</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mason Davis](https://img.shields.io/badge/Mason%20Davis-informational) ![Matthew Jackoski](https://img.shields.io/badge/Matthew%20Jackoski-informational)

🔗 **Link:** [Gato](https://github.com/praetorian-inc/gato/wiki)  
📝 **Description:** Gato, or the GitHub Attack Toolkit, is an enumeration and attack toolkit that allows both blue teamers and offensive security practitioners to identify and exploit GitHub Actions vulnerabilities within an organization's public and private repositories. Gato can automatically enumerate repositories and organizations for exploitable self-hosted runners, readable secrets, and insecure workflows that attackers could leverage for further compromise. Gato also automates the exploitation of these misconfigurations, including dumping secrets or executing commands on a runner.

The tool leverages GitHub personal access tokens, both compromised or provisioned, to perform enumeration and exploitation and aims to identify GitHub repositories where an attacker could execute code in a trusted context. Outcomes often include dumping sensitive GitHub repository variables, such as deploy keys, cloud credentials, or additional GitHub tokens, and code execution on self-hosted runners, commonly an initial access vector.

GitHub recommends that repositories restrict GitHub Actions execution and that self-hosted runners only be employed for private repositories. However, thousands of organizations utilize self-hosted runners or allow GitHub Actions execution in a trusted context with minimal effort. Default configurations are often vulnerable, and Gato uses a mix of workflow file analysis and run-log analysis to identify potentially vulnerable repositories at scale.

Key Features:
* Automated Enumeration: Gato rapidly scans GitHub repositories and organizations, pinpointing those with exploitable self-hosted runners or readable secrets.
* Exploitation Capabilities: Gato fully automates the execution of attacks against discovered misconfigurations, from secret dumping to command execution on Actions runners.
* Practical Value: Empowers red and blue teams to identify and fix critical vulnerabilities before attackers can exploit them.
* Attack Vector Focus: Zeroes in on GitHub Actions as a key infiltration point, often serving as an initial access point for wider breaches.

</details>

<details><summary><strong>GraphRunner: A Post-Exploitation Toolset for M365</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Beau Bullock](https://img.shields.io/badge/Beau%20Bullock-informational)

🔗 **Link:** [GraphRunner: A Post-Exploitation Toolset for M365](https://github.com/dafthack/GraphRunner/blob/main/GraphRunner.ps1)  
📝 **Description:** In the rapidly evolving realm of cloud productivity suites, Microsoft 365 (M365) has solidified its position as a fundamental resource for numerous organizations. While M365 presents a host of opportunities, it equally introduces challenges. By default, M365 offers a range of security measures within its tenant structure. However, it also contains a number of default configurations that hold the potential for exploitation by malicious actors. GraphRunner is a new post-exploitation toolset that can be used to exploit certain default M365 configurations.

During this presentation, I will provide an in-depth exploration of GraphRunner's features, showcasing its role in elevating post-exploitation strategies. Designed to empower both red team professionals and defenders, this toolset equips users with a means to navigate the intricate Graph API at the heart of M365 and manipulate it for offensive purposes. GraphRunner offers functionalities that aid in lateral movement, data exfiltration, privilege escalation, and persistence within M365 accounts. By offering practical demonstrations of the toolset's capabilities, this presentation aims to bridge the gap between theoretical attack concepts and their tangible real-world application.

</details>

<details><summary><strong>HardeningMeter</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ofri Ouzan](https://img.shields.io/badge/Ofri%20Ouzan-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>inspectorGadget</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Heitor Albuquerque Vieira](https://img.shields.io/badge/Heitor%20Albuquerque%20Vieira-informational) ![Henry wayne](https://img.shields.io/badge/Henry%20wayne-informational) ![Scott Graham](https://img.shields.io/badge/Scott%20Graham-informational)

🔗 **Link:** Not Available  
📝 **Description:** The RISC-V Instruction-Set Architecture is a novel ISA open to academia and industry. It is also extensible, meaning anyone can customize the final processor to their specific needs. One of the standard extensions, called C extension, or Compressed Extension, allows for variable-length instructions, much like x86, but with far fewer degrees of freedom: only 2-byte and 4-byte instruction lengths; in contrast to x86, whose instruction encoding goes from 1 to 16 bytes. Although the ISA is ready for multiple 2-byte instructions to be created. This flexibility raises concerns regarding Code Reuse Attacks (CRA) such as Return Oriented Programming (ROP) and Jump-Oriented Programming (JOP) that have been widely exploited in x86 architecture.
This tool, inspectorGadget, assesses the attack surface of binaries compiled to RISC-V architecture. Searching through pre-compiled binaries, particularly of standard operating systems services, it can find useful ROP/JOP functional gadgets for those needing to craft a manual payload or deeply analyze the available gadgets. It delivers a gadget's availability analysis based on some classification groups, depending on the gadget's type of computation (arithmetic operations, register-to-register data movement, load/store operation, control flow, etc.). We also try to find the initializer and dispatcher special gadgets for JOP attacks that follow the dispatcher gadget paradigm. We also strive to link the gadgets utilizing a novel technique.
In any stage of a development pipeline, inspectorGadget can be used to assess the likelihood that a hacker could use the available gadgets to craft a CRA attack. This tool doesn't cover the first step of the exploit, which is related to some memory corruption vulnerabilities like buffer-overflows, format strings, use-after-free, etc. It can also be valuable to test the defense mechanism, assuming that the attacker is able to perform the first step and subsequently needs to rely on CRA, possibly due to using some code injection countermeasures like NX/XD/DEP.

</details>

<details><summary><strong>KubeHound: Identifying attack paths in Kubernetes clusters at scale with no hustle</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Julien Terriac](https://img.shields.io/badge/Julien%20Terriac-informational)

🔗 **Link:** Not Available  
📝 **Description:** There's no two ways about it: Kubernetes is a confusing and complex collection of intertwined systems. Finding attack paths in Kubernetes by hand is a frustrating, slow, and tedious process. Defending Kubernetes against those same attack paths is almost impossible without any third party tooling.

In this workshop we will present KubeHound - an opinionated, scalable, offensive-minded Kubernetes attack graph tool used by security teams across Datadog. We will cover the custom KubeHound DSL and demonstrate its power to identify some of the more interesting and common attack primitives. For the more advanced users, we will cover how to tweak our DSL to have it tailored to your own needs and find relevant attack paths that matter to you.

At last, is this workshop we will also demonstrate two way of using KubeHound:
* As a standalone tool that can be run from a laptop
* Or deployed as a service in your own Kubernetes clusters (KubeHound as a Service)

The main goal of this workshop is to show how defenders can find and eliminate the most dangerous attack paths and how attackers can have a treasure map to fully compromise a Kubernetes cluster by using the free and open source version of KubeHound.

</details>

<details><summary><strong>Living off the O365 land with powerpwn</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Bargury](https://img.shields.io/badge/Michael%20Bargury-informational)

🔗 **Link:** [Living off the O365 land with powerpwn](https://github.com/mbrg/power-pwn)  
📝 **Description:** powerpwn, first introduced at blackhat last year, showcases various capabilities, from enumeration, to data exfiltration, command execution and phishing. These are all enabled by utilizing built-in capabilities within Power Platform, a low-code / no-code platform built into Office365.

With the new upcoming release, powerpwn V2 allows easy unauthorized access to a broader-than-ever array of business data and services inside the Microsoft 365 ecosystem, as well as direct visibility into a variety of secrets and credentials. This is possible by scraping secrets hanging in logs or embedded in applications and without any external tools or exploits - only by capitalizing on your tenant's settings.

powerpwn allows you to exploit Azure AD guest accounts, which were previously wrongly perceived as allowing restrictive access to external parties. It does so by using a series of undocumented internal APIs and common misconfigurations in Microsoft 365 which can allow data exfiltration, backdoor creation, acting upon targets for various attacks (e.g., running ransomware), and unauthorized access to sensitive business data and applications, including corporate SQL servers, Blob storages, Azure tables, and more.

Red teamers can use powerpwn to conveniently maintain persistence within a Microsoft tenant using the inherent platform features, thereby ensuring continuous access to a tenant, even if their account has been disabled. It can also allow you to create, execute, and delete arbitrary commands, as well as credential harvesting & leakage to the outside world.

Equally important, powerpwn V2 leverages the growing adoption of AI in business applications to demonstrate how to further attack users and extract sensitive business data through an understanding of AI mechanics, dynamic analysis and GenAI manipulation.

All features are fully operational with the default Office 365 and Azure AD configuration.

</details>

<details><summary><strong>Moriarty</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Anthony Rose](https://img.shields.io/badge/Anthony%20Rose-informational) ![Jake Krasnov](https://img.shields.io/badge/Jake%20Krasnov-informational)

🔗 **Link:** [Moriarty](https://github.com/NCIP/nci-ocr/blob/master/software/ear/src/test/jmeter/nes_person_data_2.tab)  
📝 **Description:** Moriarty is a.NET tool designed to identify vulnerabilities for privilege escalation in Windows environments. Building upon Watson and Sherlock, Moriarty extends their capabilities by incorporating advanced scanning techniques for newer vulnerabilities and integrating additional checks. This tool supports a wide range of Windows versions, from Windows 10 to Windows 11, and Server versions 2016, 2019, and 2022. Moriarty differentiates itself by its ability to enumerate missing KBs and detect various vulnerabilities linked to privilege escalation, offering suggestions for potential exploits. The tool's extensive database includes well-known vulnerabilities such as PrintNightmare (CVE-2021-1675), Log4Shell (CVE-2021-44228), and SMBGhost (CVE-2020-0796), among others.

</details>

<details><summary><strong>Nebula - 3 years of kicking butts and taking usernames</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Bleon Proko](https://img.shields.io/badge/Bleon%20Proko-informational)

🔗 **Link:** [Nebula - 3 years of kicking butts and taking usernames](https://gist.github.com/kunalj101/ad1d9c58d338e20d09ff26bcc06c4235?permalink_comment_id=3484437)  
📝 **Description:** Nebula is a Cloud Penetration Testing framework. It is build with modules for each provider and each functionality. It covers AWS, Azure (both Graph and Management API, which includes Entra, Azure Subscription based resources and Office365) and DigitalOcean.
Currently covers:
- Public Reconnaissance
- Phishing
- Brute-force and Password Spray
- Enumeration of internal resources after initial access
- Lateral Movement and Privilege Escalation
- Persistence

Ever since I pushed the last update, the tool has changed drastically. Now you will get a teamserver based tool, with a client and server split, authentication to access the tool, user management and a MongoDB database to save the results into.

</details>

<details><summary><strong>Nemesis</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational) ![Lee Chagolla-Christensen](https://img.shields.io/badge/Lee%20Chagolla-Christensen-informational) ![Maxwell Harley](https://img.shields.io/badge/Maxwell%20Harley-informational)

🔗 **Link:** [Nemesis](https://gist.github.com/BenjaminAdams/4f6175e7ede6af50e9ee)  
📝 **Description:** Nemesis is an offensive data enrichment pipeline and operator support system. It ingests data from a variety of different offensive C2 frameworks and performs a number of automations and analytics on both downloaded files and different types of collected data. It aims to automate a number of repetitive tasks operators encounter on engagements, empower operators' analytic capabilities and collective knowledge, and create structured and unstructured data stores of as much operational data as possible to help guide future research and facilitate offensive data analysis.

</details>

<details><summary><strong>NimPlant</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Cas van Cooten](https://img.shields.io/badge/Cas%20van%20Cooten-informational)

🔗 **Link:** [NimPlant](https://github.com/chvancooten/NimPlant)  
📝 **Description:** NimPlant is a light-weight first-stage command and control (C2) implant written in the Nim programming language. Since its release in 2023, it has been favored for its usability, slim implant profile, and evasive capabilities. The functionality is primarily aimed at early-access operations, but it packs powerhouse features such as Beacon Object File (BOF) support and inline execution of .NET assemblies. This allows operators to execute advanced tradecraft with a focus on operational security.

New for Black Hat 2024 is the addition of a Rust implant. This new implant matches the feature set of the original Nim-based implant, but has an increased focus on operational security and memory management. Furthermore, Rust has the performance advantage and has been adopted much more than Nim, which makes it easier to "blend in" with legitimate applications. And no, the tool will not be renamed for this new addition ;)

At Black Hat Arsenal 2024, the design and architecture of NimPlant and the new Rust implant will be discussed. Offensive specialists will be provided with guidance and "pro tips" from the author on how to use the tool in offensive operations, while defensive specialists will be provided with guidance on how to identify and block this tool (and similar) in their network.

</details>

<details><summary><strong>Open Source LLM Security</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ankita Gupta](https://img.shields.io/badge/Ankita%20Gupta-informational) ![Ankush Jain](https://img.shields.io/badge/Ankush%20Jain-informational)

🔗 **Link:** [Open Source LLM Security](https://github.com/ryanbgriffiths/ICRA2024PaperList)  
📝 **Description:** Akto's Open Source LM Security tool will solve the following problems

- Prompt Injection Vulnerabilities
- Overreliance on LLM Outputs
- Insecure Output handling in LLMs
- Sensitive data exposure via LLMs

On average, an organization uses 3+ LLM models. Often most LLMs in production will receive data indirectly via APIs. That means tons and tons of sensitive data is being processed by the LLM APIs. Ensuring the security of these APIs will be very crucial to protect user privacy and prevent data leaks.

Akto's Open Source LLM Security Testing solution addresses these challenges head-on.

By leveraging advanced testing methodologies and state-of-the-art algorithms, Akto provides comprehensive security assessments for GenAI models, including LLMs. The solution incorporates a wide range of innovative features, including over 60 meticulously designed test cases that cover various aspects of GenAI vulnerabilities such as prompt injection, overreliance on specific data sources, and more.

Our tool Akto focuses on solving the above problems by providing:

1. Provide automated LLM Security tests:
1. **OWASP LLM Top 10 coverage** - Akto can automatically test LLM (exposed via APIs) for critical vulnerabilities like Prompt Injection, Sensitive Information Disclosure, etc.
2. **Fully customizable test suite** - This feature enables users to modify existing tests or create their own.
3. **Combine with business logic** - The tests can be invoked as part of the application workflow (e.g., post-login, after support ticket creation, etc.)
2. Automate in your DevSecOps pipeline:
1. **Run tests through CLI** - Developers and security engineers can execute these tests through a single-line CLI.
2. **Integrate with CI/CD** - You can also add Akto to your CI/CD pipeline to automate the entire testing process.
3. **Use LLMs to test LLMs** - You can also use suggestions and prompts from other LLMs to test your LLM

This tool will be very interesting for:

- **Application Security teams** - it's a one stop shop of LLM Security testing. Tests like prompt injection, overreliance will be especially interesting for them.
- **Blue teamers/infra security** - Getting an automated LLM API inventory and getting alerts for any new sensitive APIs. They can also get a view of all sensitive PII data being shared across all their services and across all their LLM APIs.

</details>

<details><summary><strong>Opening the Door: API Key Permission Enumeration</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Joe Leon](https://img.shields.io/badge/Joe%20Leon-informational)

🔗 **Link:** [Opening the Door: API Key Permission Enumeration](https://github.com/JamesLavin/my_tech_resources)  
📝 **Description:** You're a bug bounty hunter and find a live API key - how do you demonstrate the impact of that key leaking? You're an IT administrator and find a hardcoded secret in a PowerShell script - how do you identify the permissions that key holds? Most SaaS providers make it difficult to enumerate the access granted to a particular credential.

In this talk, we're open-sourcing a new tool to enumerate the permissions and access associated with a leaked credential, without requiring access to the provider's UI. We'll walk through the meticulous steps we took to accurately assess each SaaS providers' scopes, as well as share the logic behind how we enumerate permissions, including string analysis, brute forcing and more.

</details>

<details><summary><strong>RedCloud OS : Cloud Adversary Simulation Operating System</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yash Bharadwaj](https://img.shields.io/badge/Yash%20Bharadwaj-informational) ![Manish Kumar Gupta](https://img.shields.io/badge/Manish%20Kumar%20Gupta-informational)

🔗 **Link:** Not Available  
📝 **Description:** RedCloud OS is a Debian based Cloud Adversary Simulation Operating System for Red Teams to assess the security of leading Cloud Service Providers (CSPs). It includes tools optimised for adversary simulation tasks within Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

Enterprises are moving / have moved to Cloud Model or Hybrid Model and since security testing is a continuous procedure, operators / engineers evaluating these environments must be well versed with updated arsenal. RedCloud OS is an platform that contains:

- Custom Attack Scripts
- Installed Native Cloud Provider CLI
- 25+ Multi-Cloud Open-Source Tools
- Tools Categorization as per MITRE ATT&CK Tactics
- Support Multiple Authentication Mechanisms
- In-Built PowerShell for Attacking Azure Environment
- Ease to configure credentials of AWS, Azure & GCP & much more...

Inside each CSP, there are three sub-categories i.e, Enumeration, Exploitation, and Post Exploitation. OS categorises tools & our custom scripts as per the above mentioned sub-categories.

</details>

<details><summary><strong>ROP ROCKET: Advanced Framework for Return-Oriented Programming</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational) ![Shiva Shashank Kusuma](https://img.shields.io/badge/Shiva%20Shashank%20Kusuma-informational)

🔗 **Link:** [ROP ROCKET: Advanced Framework for Return-Oriented Programming](https://github.com/Bw3ll/ROP_ROCKET)  
📝 **Description:** ROP ROCKET is a groundbreaking, next-generation tool for return-oriented programming, boasting unparalleled capabilities. This tool introduces several innovative techniques, including generating Heaven's Gate ROP gadgets, facilitating the transition from x86 to x64 architecture, and a unique approach to invoking Windows syscalls to evade Data Execution Prevention (DEP), eliminating the need for less stealthy Windows API functions.

The focal point of this tool is in automatic ROP chain generation – building complete ROP exploits. Additionally, with this tool, we pioneer several new ROP techniques techniques, including both x86 and x64 Heaven's Gate and using Windows syscalls to bypass DEP. To overcome DEP, we automate chain generation for Windows syscalls NtAllocateVirtualMemory and NtProtectVirtualMemory. Additionally, ROP ROCKET can avoid the need to bypass DEP and have multiple API's chained together, to achieve shellcode-like functionality.

One of the features of ROP ROCKET is the sheer diversity of possibilities in creating these chains, allowing unique and unusual combinations that traditionally might not be achievable by emulation. The tool uses extensive emulation to evaluate the fitness of individual ROP gadgets, allowing unusual or longer ROP gadgets to be used. Additionally, ROP ROCKET builds, emulates, and debugs parts of some ROP chains internally to solve certain problems, allowing for ROP chains to be build with the "mov dereference" or "sniper" approach, rather than relying simply on the "pushad" approach. Distances to certain function parameters can also be dynamically calculated and readjusted with emulation.

Sometimes a ROP chain could be possible if only some ROP gadget did not have bad bytes contained in its address. With ROCKET, we provide a way to "obfuscate" gadgets, allowing the gadget address to be decoded and executed at runtime.

ROP ROCKET is built for performance, as it utilizes multiprocessing, allowing a dozen or more cores to be used. Additionally, the tool provides persistence for binaries already examined, so it will store the gadgets already found. With all possible ROP gadgets, our raw ingredients having been found, ROP chains can be formed in seconds.

For Black Hat Arsenal, we will be releasing new patterns for automatic ROP chain generation. While ROP can be a complex topic, ROP ROCKET provides powerful capabilities to users.

</details>

<details><summary><strong>SCCMHunter</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Garrett Foster](https://img.shields.io/badge/Garrett%20Foster-informational)

🔗 **Link:** [SCCMHunter](https://github.com/garrettfoster13/sccmhunter/wiki)  
📝 **Description:** SCCMHunter is a post exploitation framework written in Python designed to streamline identifying, profiling, and attacking SCCM infrastructure and assets in an Active Directory environment. The tool supports attack path identification and abuse for all currently known tradecraft published in Misconfiguration Manager.

</details>

<details><summary><strong>Silver SAML Forger: Tooling to craft forged SAML responses from Entra ID</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Eric Woodruff](https://img.shields.io/badge/Eric%20Woodruff-informational) ![Tomer Nahum](https://img.shields.io/badge/Tomer%20Nahum-informational)

🔗 **Link:** Not Available  
📝 **Description:** Silver SAML Forger is a tool developed to PoC SAML response forging, also known as Silver SAML and Golden SAML attacks, against applications federated to Entra ID for authentication using the SAML standard. The tool goes along with research into the vulnerabilities that can present in cloud identity providers, such as Entra ID, where if an attacker has access to the private key material Entra ID uses for SAML response signing, that the target applications may be susceptible to these forging attacks.

While Entra ID protects the private key if generated internally, as it cannot be exported, in the real-world organizations follow bad habits that may leave sensitive private key material available to an attacker. These sorts of habits have been observed by the research team that developed the Silver SAML Forger. Using this tool in combination with tools such as Burp Suite, you can demonstrate forging access to a target application. If the application supports certain types of SAML integrations, the identity provider will have no visibility into the authentication – you could think of these attacks as Kerberos Golden-ticket type attacks.

The tool requires the signing certificate to use, the username that is target for impersonation, and some basic federation information about the target application that can be derived from a few different methods.

</details>

<details><summary><strong>StealthGuardian - Automatic TTP Analysis</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Christian Becker](https://img.shields.io/badge/Christian%20Becker-informational) ![Sven Schlüter](https://img.shields.io/badge/Sven%20Schlüter-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Stowaway: Multi-hop Proxy Tool for pentesters</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Haoliang Qi](https://img.shields.io/badge/Haoliang%20Qi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Stowaway is a multi-level proxy tool written in the go language and designed for penetration testers and security researchers. Attackers can use Stowaway to construct their own tree network in a highly restricted intranet environment so that the attacker's external traffic can reach the core network through the layers of proxies of multiple Stowaway nodes. While breaking through network access restrictions, Stowaway can also help attackers hide their own traffic and better lurk in the intranet. In addition, attackers can also use the terminal interface and various auxiliary functions provided by Stowaway to more easily manage the entire tree network and improve the efficiency of penetration testing.

</details>

<details><summary><strong>The Metasploit Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

🔗 **Link:** [The Metasploit Framework](https://github.com/zerosteiner)  
📝 **Description:** The Metasploit Framework released version 6.4 earlier this year, including multiple improvements to Kerberos-related attack workflows. The latest changes added support forging diamond and sapphire tickets, as well as dumping tickets from compromised hosts. Metasploit users can now exploit unconstrained delegation in Active Directory environments for privilege escalation as well as use pass-the-ticket authentication for the Windows secrets dump module. These new Kerberos improvements increase the ways in which tickets can be forged, gathered as well as used.

Additionally, Metasploit has added support for new protocol based sessions, allowing users to interact with targets without uploading payloads, thus increasing their evasive capabilities. These new sessions can be established to database, SMB and LDAP servers. Once opened, they enable users to interact and run post modules with them, all without running a payload on the remote host.

Finally, version 6.4 includes a complete overhaul of how Metasploit handles its own DNS queries. These improvements ensure that users pivoting their traffic over compromised hosts are not leaking their queries and offer a high degree of control over how queries should be resolved.

This Arsenal demonstration will cover these latest improvements and show how the changes can be combined for new, streamlined attack workflows using the latest Metasploit release.

</details>

<details><summary><strong>VishLine</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Matthew Jackoski](https://img.shields.io/badge/Matthew%20Jackoski-informational) ![Mitchel Jordan](https://img.shields.io/badge/Mitchel%20Jordan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Our telephonic phishing simulation tool is a cutting-edge, web-based platform designed to empower cybersecurity teams to create, manage, and execute complex telephonic phishing campaigns without requiring coding skills. This tool uniquely combines customizable Interactive Voice Response (IVR) systems with a collaborative, real-time operational environment, enabling the rapid deployment of simulated phishing attacks to test and enhance organizational defenses. By providing a realistic simulation of various telephonic phishing techniques, our tool assists in identifying vulnerabilities, refining response strategies, and ultimately strengthening the cybersecurity posture against one of the most challenging vectors for security breaches.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Advancing Drone Radiofrequency Warfare: Innovations and Countermeasures</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![David Melendez](https://img.shields.io/badge/David%20Melendez-informational) ![Gabriela García](https://img.shields.io/badge/Gabriela%20García-informational)

🔗 **Link:** Not Available  
📝 **Description:** The proliferation of consumer drones presents a new frontier in security threats, with radiofrequency (RF) warfare emerging as a potent vector. This paper explores the risks posed by RF manipulation in consumer drones and unveils innovative countermeasures. Leveraging the MT7628 chipset, a cost-effective solution is devised to manipulate RF signals for drone control. This presentation demonstrates the feasibility of generating carriers through I2S pins, enabling Amplitude Shift Keying (ASK) modulation. By integrating frequency hopping techniques, the system achieves enhanced evasion against anti-drone measures. Receiver capabilities are bolstered using USB SDR dongles, ensuring robust communication in dynamic environments. Amplification and PCB enhancements optimize transmission efficiency while complying with regulatory standards. Limitations regarding processing speed and regulatory compliance are acknowledged, emphasizing the need for responsible deployment. Live demonstrations underscore the efficacy of the proposed system, showcasing its adaptability and resilience. Furthermore, avenues for future enhancements, including phase modulation for spread spectrum, are discussed, promising further evolution in drone RF warfare defense.

</details>

<details><summary><strong>ICSGoat: A Damn Vulnerable ICS Infrastructure</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Shantanu Kale](https://img.shields.io/badge/Shantanu%20Kale-informational) ![Divya Nain](https://img.shields.io/badge/Divya%20Nain-informational)

🔗 **Link:** [ICSGoat: A Damn Vulnerable ICS Infrastructure](https://github.com/ine-labs/ICSGoat)  
📝 **Description:** ICSGoat: A Damn Vulnerable ICS Infrastructure is a training tool built to emulate SCADA outstations and PLC setups, offering insights into the security threats prevalent in Industrial Control Systems (ICS). Industrial Control Systems are integral to the operation of critical infrastructures, but the increasing interconnectivity of these systems with the internet exposes them to various cybersecurity threats, necessitating effective testing tools to assess the security posture of SCADA and PLC systems. Tailored for ICS engineers, this simulated environment replicates real-world scenarios, spotlighting vulnerabilities inherent in weak architecture.

Featuring multiple insecure protocols, SCADA applications, and PLC attacks, ICSGoat serves as a dynamic platform for comprehending and mitigating potential disruptions to mission-critical systems. Through hands-on exploration within a safe, controlled environment, engineers can fortify their understanding of ICS security, enabling proactive defense measures against evolving threats.

</details>

<details><summary><strong>Introducing Serberus, a multi headed embedded hardware interface tool.</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Patrick Kiley](https://img.shields.io/badge/Patrick%20Kiley-informational)

🔗 **Link:** [Introducing Serberus, a multi headed embedded hardware interface tool.](https://github.com/ee92/mem-key/blob/master/public/assets/words.json)  
📝 **Description:** The Serberus is a multi-headed hardware hacking tool designed to easily connect to your target. It has 4 channels and has headers to interface with UART, JTAG, SPI, I2C and SWD. Serberus is an evolution of the TIMEP, created by a fellow Google employee a few years ago. It has a similar level shifter design to allow you to connect to any logic voltage between 1.65V and 5.5V, there is even a setting to allow you to match the voltage of your target if it is using a non-standard voltage. The project is free and open source with all board layouts, design files and schematics published.

During this arsenal talk I will introduce and demonstrate the Serberus on devices from a simple wifi router as well as multi-serial avionics and electric vehicle systems. I will demonstrate my methodology for rapidly locating, timing and connecting to UARTs beyond just probing likely connection points on a target board.

</details>

<details><summary><strong>Praeda-II</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Deral Heiland](https://img.shields.io/badge/Deral%20Heiland-informational) ![Sam Moses](https://img.shields.io/badge/Sam%20Moses-informational)

🔗 **Link:** Not Available  
📝 **Description:** Praeda - Latin for "plunder, spoils of war, booty". Praeda-II is a complete rewrite and update of the automated data/information harvesting tool Praeda that was originally released in 2014. Praeda-II is designed to conduct security audits on Multifunction Printer (MFP) environments.
Praeda-II leverages various implementation weaknesses and vulnerabilities found on multifunction printers (MFP) and extracts passwords such as Active directory credentials from MFP configurations including SMTP, LDAP, POP3 and SMB settings. The tool is designed to evaluate the MFP device configurations looking for certain setting that adversely impact the devices security posture. Also, the tools output logs are structured to be able to import into other tools such as Metasploit and to be easily parsable for quick identification of critical findings and reporting purposes.
During the demonstration, we will introduce everyone to the tool's framework structure, and show how new test modules and device fingerprinting can be easily added. We will walk all attendees through the various features and functions of this tool and explain how to effectively leverage it during internal penetrations testing, red team operations and blue team internal environment audits. This walkthrough of the tool will include examples, such as testing to gather credentials that can be used to gain access to critical internal systems, address book recovery containing account names and email address, and MFP device misconfigurations that impact an organization security posture.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>AegiScan: A Static Dataflow Analysis Framework for iOS Applications</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Yizhuo Wang](https://img.shields.io/badge/Yizhuo%20Wang-informational) ![Xiaolong Bai](https://img.shields.io/badge/Xiaolong%20Bai-informational) ![Wenchao Li](https://img.shields.io/badge/Wenchao%20Li-informational)

🔗 **Link:** Not Available  
📝 **Description:** iOS is one of the most popular mobile operating systems worldwide, making the security of its applications a public concern. However, there's still a lack of powerful and efficient static dataflow analysis tools for iOS applications, which is essential for vulnerability scanning.
Conducting static dataflow analysis on iOS app binaries presents the following challenges:
1. Objective-C's runtime features, e.g., dynamically dispatched functions (objc_msgsend), pose an obstacle in static method resolution.
2. Classes, structs, and inter-module operations are complicated in context-sensitive and inter-procedural dataflow analysis.
3. Optimization techniques, e.g., app thinning and symbol stripping, increase the complexity of analysis.
To this end, we propose AegiScan, a static dataflow analysis framework for iOS application binaries. It utilizes top-down type propagation to resolve Objective-C MsgSend calls, thereby reconstructing the call graph. It then generates the Code Property Graph for each function to establish context-sensitive dataflow and combines them based on the call graph to facilitate inter-procedural analysis. Moreover, AegiScan parses runtime data segments to recover information lost during optimization, incorporating it into the analysis.
AegiScan is featured with a combination of static analysis and graph database, which makes tasks like vulnerability scanning efficient since the binary analysis only needs to be conducted once, with the results stored in the database for multiple queries. In our experiment, the analysis on a 130MB iOS App binary can be completed in less than 20 minutes. In addition, we develop query APIs based on graph database query language to facilitate vulnerability scanning.
To demonstrate the capability of AegiScan, we applied it to popular iOS Apps and critical macOS system services. It discovered various vulnerabilities, including 0-days in Apple native system services leading to local privilege escalation. This talk will also shed light on some interesting and thought-provoking vulnerabilities.

</details>

<details><summary><strong>AntiDebugSeeker: Automatically Detect Anti-Debug to Simplify Debugging (IDA/Ghidra)</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Takahiro Takeda](https://img.shields.io/badge/Takahiro%20Takeda-informational)

🔗 **Link:** Not Available  
📝 **Description:** Malware authors frequently use anti-debugging techniques to hinder analysis, making the malware either halt its actions or behave unusually upon detection by a debugger.
The complexity of these techniques varies, with malware spread through mass-mailing campaigns or ransomware often employing methods like VM detection, breakpoint detection, and time difference detection
to evade analysis, affecting a wide range of organizations.

"AntiDebugSeeker" is an open-source plugin for the binary analysis tools IDA and Ghidra, which are frequently utilized by analysts.
It streamlines the malware analysis process by automatically identifying the anti-debugging techniques embedded within Windows malware.
Code with anti-debug capabilities often overlaps with techniques used for anti-analysis, as well as with the preparatory steps forprocess injection, which are frequently employed by malware.
Therefore, by flexibly customizing the detection rules, it is possible not only to identify anti-debugging features but also to understand the functionalities of the malware.
Furthermore, the tool also provides functionalities to explain these anti-debugging measures and approaches to the corresponding functions.
This enhances the analyst's ability to understand and counteract the malware's evasion techniques effectively, offering a more comprehensive understanding and response strategy against such threats.

We will demonstrate malware analysis and explain how to use the tool's features, providing a practical understanding of how these features can be applied in actual threat scenarios.

</details>

<details><summary><strong>Breaking Barriers: PyFrida's Simplified Pythonic Approach to Frida Scripting</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Rui Cheng](https://img.shields.io/badge/Rui%20Cheng-informational) ![Guoshuai Zhao](https://img.shields.io/badge/Guoshuai%20Zhao-informational) ![Jiacheng Hu](https://img.shields.io/badge/Jiacheng%20Hu-informational) ![Chengao Zhang](https://img.shields.io/badge/Chengao%20Zhang-informational)

🔗 **Link:** Not Available  
📝 **Description:** Frida is a widely-used binary instrumentation framework. When using Frida, the typical workflow involves writing Frida scripts in JS and injecting them into the target process using frida-tools or Frida's python bindings. This workflow presents several inconveniences, such as:
* Inability to debug Frida scripts in real-time.
* Integration of Frida scripts into projects requires mechanisms like RPC or Socket.
* In the binary security field, Python is more popular than JS, which many users must familiarize themselves with before starting to write Frida scripts.

To address these issues, we developed the PyFrida framework, enabling Frida scripts to be written in Python. It works by implementing a virtual machine in JS and dynamically converting Python code into a sequence of instructions to execute on the virtual machine. With PyFrida, users can write and debug Frida scripts in Python and easily integrate them into Python projects.

</details>

<details><summary><strong>CodeHawk Binary Patcher: High Assurance Binary Patching Without a Reverse Engineer</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Michael Gordon](https://img.shields.io/badge/Michael%20Gordon-informational) ![Henny Sipma](https://img.shields.io/badge/Henny%20Sipma-informational) ![Ben Karel](https://img.shields.io/badge/Ben%20Karel-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>LIBIHT: A Cross-Platform Library for Accessing Intel Hardware Trace Features</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Changyu Zhao](https://img.shields.io/badge/Changyu%20Zhao-informational) ![Di Wu](https://img.shields.io/badge/Di%20Wu-informational) ![Guancheng Li](https://img.shields.io/badge/Guancheng%20Li-informational)

🔗 **Link:** Not Available  
📝 **Description:** Tracing stands as a vital instrument in the realm of complex software reverse engineering, but traditional tracing tools can be hindered by significant performance penalties. Instrumentation-based tracing, for instance, may incur a slowdown of up to 100x, severely limiting its practicality for in-depth analysis.

Intel CPUs have introduced a suite of hardware features, such as Last Branch Record (LBR), Branch Trace Store (BTS), and Intel Processor Trace (Intel PT), which promise to deliver detailed program tracing with minimal overhead. However, harnessing these hardware-assisted tracing capabilities is a complex task that has prevented their widespread adoption.

LIBIHT bridge this gap by offering an open-source library interface that hides all the complexity of hardware-assisted tracing and offering a user-friendly approach to interacting with advanced CPU hardware features. It collects traces by interacting with CPU hardware through its kernel components, while its user-space APIs provide a user friendly api to users.

The library assists reverse engineers by allowing them to:

- Selectively trace execution at a fine-grained level to reconstruct control flow
- Filter traces to focus on regions of interest
- Visualize traces to aid analysis
- Perform initial analysis without dealing with low-level trace formats

By bridging the kernel-user space and simplifying access to hardware traces, LIBIHT opens new capabilities for software analysis problems that are challenging with traditional debugging alone. It also lowers the bar for academic and industrial researchers to leverage the powerful tracing features in modern Intel processors.

In our talk, we will demonstrate LIBIHT's abilities through live demos. Attendees will see how to selectively trace specific regions of interest to efficiently reconstruct control flow graphs. Traces can be filtered to focus only on desired functions or call sequences. Visualization of trace data aids static analysis.

We believe LIBIHT can significantly aid reversing through its ability to efficiently recover precise control flow and execution context at scale. Its capabilities inspire further research extending hardware-assisted program analysis and instrumentation.

</details>

<details><summary><strong>SHAREM: Advanced Shellcode Analysis Framework</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational)

🔗 **Link:** [SHAREM: Advanced Shellcode Analysis Framework](https://github.com/Bw3ll/sharem)  
📝 **Description:** Shellcode is omnipresent, a constant part of the exploitation and malware ecosystem. Injected into process memory, there are limitless possibilities. Yet until recently, analysis techniques were severely lacking. We present SHAREM, an NSA-funded shellcode analysis framework with stunning capabilities that will revolutionize how we approach the analysis of shellcode.

SHAREM can emulate shellcode, identifying more than 25,000 WinAPI functions as well as 99% of Windows syscalls. This emulation data can also be ingested by its own custom disassembler, allowing for functions and parameters to be identified in the disassembly for the first time ever. The quality of disassembly produced by SHAREM is virtually flawless, markedly superior to what is produced by leading disassemblers. In comparison, IDA Pro or Ghidra might produce a vague "call edx," as opposed to identifying what specific function and parameters is being called, a highly non-trivial task when dealing with shellcode.

One obstacle with analyzing shellcode can be obfuscation, as an encoded shellcode may be a series of indecipherable bytes—a complete mystery. SHAREM can easily overcome this, presenting the fully decoded form in the disassembler, unlocking all its secrets. Without executing the shellocode, emulation can be used to help fully deobfuscate the shellcode. In short, a binary shellcode – or even the ASCII text representing a shellcode – could be taken and quickly analyzed, to discover its true, hidden functionality.
One game-changing innovation is complete code coverage. With SHAREM, we ensure that all code is executed, capturing function calls and arguments that might otherwise be impossible to get. This is done by taking a series of snapshots of memory and CPU register context; these are restored if a shellcode ends with unreached code. In practical terms, this means if a shellcode ordinarily would prematurely terminate, we might miss out several malicious functions. Complete code coverage allows us to rewind and restart at specific points we should not be able to reach, discovering all functionality.
New to be unveiled at Arsenal, SHAREM will now integrate AI to help resolve what exactly is going on. The enumerated APIs and parameters can be analyzed to identify malicious techniques, which could be found in MITRE ATT&CK framework and elsewhere.

The ease and simplicity of SHAREM is breathtaking, especially comparison to how much time and effort similar analysis would require otherwise. SHAREM represents a major shift in our capability to analyze shellcode in a highly efficient manner, documenting every possible clue – whether it be functions, parameters, secrets, or artifacts.

For reverse engineers of all kinds, SHAREM is a must-see presentation.

</details>

<details><summary><strong>VivisectION</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![atlas 0fd00m](https://img.shields.io/badge/atlas%200fd00m-informational)

🔗 **Link:** Not Available  
📝 **Description:** Reverse Engineering and Binary Vulnerability Research can be difficult, daunting, exhausting task, making your eyes bleed.

VivisectION leverages the power of the Vivisect Binary Analysis framework to provide Easy-Buttons for numerous Reversing difficulties, empowering reverse-engineers to achieve greater results, and reducing brain-drain in the process.

VivisectION's core value is based on interactive partial-emulation. Imagine reversing a particularly annoying set of functions deep in the belly of an annoying compiled binary. You may find yourself thinking "Man, I wish I had this thing in a debugger." VivisectION's Partial-Emulation capabilities make your wish come true.

Want to strap in an analysis modules and emulate through code? Easy.

Reconstitute Structures and C++ Classes? let's not get crazy!

Come and see....

</details>

<details><summary><strong>Winbindiff: Automated Windows Patch Diffing</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![John McIntosh](https://img.shields.io/badge/John%20McIntosh-informational)

🔗 **Link:** Not Available  
📝 **Description:** Winbindiff: Automated Windows Patch Diffing

Windows is one of the most widely used operating systems in the world, and also one of the most frequently updated. Every month on Patch Tuesday, Microsoft releases feature and security updates that fix bugs and vulnerabilities in Windows binaries. However, these updates often lack detailed information about the nature and severity of the vulnerabilities, leaving security researchers and system administrators in the dark about the risks and implications of the patches.

Enter Winbindiff, a unique command-line tool designed to shine light on the obscured changes in Windows binaries post-update via automated patch diffing. Patch diffing is a technique that compares the patched and unpatched versions of binaries to reveal what was really fixed for a security update. Winbindiff harnesses the power of Winbindex, a web service that provides an index of Windows binaries, and Ghidriff, a Ghidra fueled Python Diffing Engine to automate the patch diffing process.

Winbindiff can automatically find, download, and compare the binaries for a Windows release build. By automating this process, Winbindiff empowers security professionals to swiftly identify, download, and dissect any Windows update. The result? A comprehensive markdown report detailing the diffing outcomes that we like to call a binary biography or "binography". These "binographies" tell the story of a binary over time and reveal critical security changes for an update.

Our presentation will introduce Winbindiff and its pivotal role in demystifying Windows updates. Attendees will witness firsthand how this tool can streamline their security analysis, providing a deeper understanding of each update's impact. Join us to explore how Winbindiff is revolutionizing patch diffing and transforming the way we perceive and react to Windows security updates.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Wargame</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational)

🔗 **Link:** [AI Wargame](https://github.com/pedram-mohajer)  
📝 **Description:** Come join a fun and educational attack and defence AI wargame. You will be given an AI chatbot. Your chatbot has a secret that should always remain a secret! Your objective is to secure your chatbot to protect its secret while attacking other players' chatbots and discovering theirs. The winner is the player whose chatbot survives the longest (king of the hill). All skill levels are welcomed, even if this is your first time seeing code, securing a chatbot, or playing in a wargame.

</details>

<details><summary><strong>CyberChef-like Automation within BurpSuite - Let's get cooking with CSTC</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Florian Haag](https://img.shields.io/badge/Florian%20Haag-informational) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational)

🔗 **Link:** Not Available  
📝 **Description:** Imagine GCHQ's CyberChef integrated in BurpSuite with live modification of requests at your fingertips. That's exactly what we had in mind when we built the Cyber Security Transformation Chef (CSTC) a few years ago. The CSTC is an extension to the popular BurpSuite Proxy built for experts working with web applications. It enables users to define recipes that are applied to outgoing or incoming HTTP requests/ responses automatically. Whatever quirks and specialties an application might challenge you with during an assessment, the CSTC has you covered. Furthermore, it allows to quickly apply custom formatting to a chosen message, if a more detailed analysis is needed.

As an example, imagine an API that requires an HMAC appended to all messages derived from datapoints inside the message body. With the CSTC you can extract the necessary datapoints with ease and calculate the HMAC on the fly. Together with the CSTCs integration into all major BurpSuite components you can now perform automatic intrusion tests with the Scanner, or manual fuzzing using Intruder and Repeater, without worrying about the HMAC any longer. Another use case is to extract JWTs from incoming HTTP responses and use them in outgoing requests of the Scanner. This eliminates the need to worry about expiring JWTs while scanning.

After a few years of silence since the initial release at BlackHat 2020, the CSTC is finally back! It contains new features and improvements such as many new operations to be used in recipes, inclusion of community requested features and a refactoring of the codebase. Alongside the CTSC we will launch a new public repository with recipes we found useful in our experience as penetration testers and of course open for contribution by the community. This helps the community to solve common challenges and getting started working with the CSTC.

</details>

<details><summary><strong>Kestrel 2: Hunt For Threats Across Security Data Lakes</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Xiaokui Shu](https://img.shields.io/badge/Xiaokui%20Shu-informational) ![Paul Coccoli](https://img.shields.io/badge/Paul%20Coccoli-informational) ![Edward Landis](https://img.shields.io/badge/Edward%20Landis-informational)

🔗 **Link:** Not Available  
📝 **Description:** Many organizations today leverage data lakes for organizing security data, from alerts to raw logs and telemetry. While a lot of open-source data lake technology is available like Delta Lake, OpenSearch, and Apache Iceberg, little has been explored in the open source community on how to ease threat discovery using the data. With the establishment of open schema standards like OCSF and OpenTelemetry, we are one step closer to the answer. And this summer, the Kestrel team will release Kestrel 2, which enables security professionals to hunt and investigate on top of one or multiple data lakes with native OCSF, OpenTelemetry, and STIX descriptions in huntflows.

In this session, we will debut Kestrel 2 with an example huntbook and its compiled queries side by side to give the audience an impression of what Kestrel is and what its compiler does. Next we will kick off the fun part---a blue team hunting lab. We will walk through and execute a few simple-to-advanced Kestrel hunts against multi-stage attack campaigns, which the audience can try in their copy of the lab. We will start from hunting simple MITRE techniques using logs from one source, e.g., EDR, move to hunting advanced MITRE techniques by connecting logs from multiple sources. Then, we will dive into a multi-tactic hunt using on-premise logs of an enterprise stored at one data lake and cloud application logs stored at another. We will follow attacker's lateral movement from one data lake to the other in a Kestrel hunt to reveal the entire threat and give insights on response development.

The lab is available in a cloud sandbox (free service by MyBinder) or running on your laptop: https://github.com/opencybersecurityalliance/black-hat-us-2024

</details>

<details><summary><strong>Remediate Cloud Security Threats Automatically in Real-Time with Falco and Event Driven Ansible</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Marat Salakhutdinov](https://img.shields.io/badge/Marat%20Salakhutdinov-informational) ![Aleksandr Varlamov](https://img.shields.io/badge/Aleksandr%20Varlamov-informational)

🔗 **Link:** Not Available  
📝 **Description:** Cloud attacks are fast. After finding an exploitable asset, malicious actors need less than 10 minutes on average to execute an attack. Although identity and access management, vulnerability management, and other preventive controls are common in cloud environments, no organization can stay safe without a threat detection and response program for addressing zero-day exploits, insider threats, and other malicious behavior.

That's why Runtime Security is critical for organizations to fortify their cloud security against evolving cyber threats. Luckily we have Falco, which is an open-source runtime security tool designed to monitor, detect, and respond to abnormal behaviors in applications and containers within cloud-native environments. It provides real-time insights into system activities, allowing organizations to identify and mitigate security threats effectively.

In this workshop, we will harness Falco's capabilities for runtime detection within Kubernetes and Cloud environments and combine it with the power and flexibility of Event-Driven Ansible to leverage it as a response engine to promptly address and mitigate security incidents in real time.

We invite you to join us on this journey, where we will generate security events, detect them with Falco and automatically remediate them in real time with Event-Driven Ansible.

</details>

<details><summary><strong>Reversing Wipers: digital damage for battlefield advantage</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Max Kersten](https://img.shields.io/badge/Max%20Kersten-informational)

🔗 **Link:** Not Available  
📝 **Description:** Starting in 2022, the world saw an uptick in the popularity of wipers, especially related to the Russo-Ukranian conflict, as well as some new wipers with the rising tension in the Middle East. In this lab, you get to try your hand at picking them apart in detail. If you are curious as to what the headline-making malware looks like internally, if you're interested in reverse engineering or malware analysis, or if you simply want to have a look into the life of a malware analyst's work, then this is a lab for you! With the help of Ghidra (NSA's software reverse engineering suite of tools), you will dive head first into real samples, to find and unravel the secrets the wipers contain. Novice and aspiring analysts, as well as experienced analysts, are welcome to join this lab.

</details>

<details><summary><strong>RF Hacking on the Road: Logging Tire Sensors</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Paul Clark](https://img.shields.io/badge/Paul%20Clark-informational)

🔗 **Link:** [RF Hacking on the Road: Logging Tire Sensors](https://github.com/djeebus/defcon24ical/blob/master/defcon24.ics)  
📝 **Description:** Build an SDR-based scanner to log transmissions from tire sensors!

Nearly every tire on every vehicle produced the last few decades contains a digital radio with a unique signature. By scanning, receiving, and logging these Tire Pressure Monitor (TPM) sensor transmissions, you can essentially fingerprint individual tires. Such a TPM logger allows you to determine information about when and how often unique vehicles pass through a given location. You can also extract some information on the make of each vehicle and a rough estimate of its year of manufacture.

In this lab, you'll learn how and when TPM sensors transmit their data and how you can capture and log their communications. You'll then put together some Python code blocks to build a simple, SDR-based logger and test it on real TPM sensors.

</details>

---
## 🔍 OSINT
<details><summary><strong>AI.PassYou - Password dictionary generator using social network information and chatGPT to generate personal keywords.</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Manuel Ginés](https://img.shields.io/badge/Manuel%20Ginés-informational) ![Maria Jesús Prior](https://img.shields.io/badge/Maria%20Jesús%20Prior-informational) ![Marc Ulldemolins](https://img.shields.io/badge/Marc%20Ulldemolins-informational) ![Angel Lopez Domenech](https://img.shields.io/badge/Angel%20Lopez%20Domenech-informational)

🔗 **Link:** Not Available  
📝 **Description:** The tool allows you to generate a dictionary of passwords based on data extracted from your social networks, including personalized information about hobbies, geographic location or language.

The process is divided into three points:

* Extraction of information from social networks
* Use of AI to find keywords inferred from this public information.
* Rule-based dictionary generation process

This process allows the generation of customized dictionaries that greatly increase the effectiveness over traditional password dictionaries.

</details>

<details><summary><strong>Emploleaks v2: Finding [more] Information of your Employees</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Gabriel Franco](https://img.shields.io/badge/Gabriel%20Franco-informational)

🔗 **Link:** Not Available  
📝 **Description:** During red team assessments, our team found that personal information leaked in breaches can be a significant risk to our clients. It is often the case that personal passwords are reused in enterprise environments. But even when they don't, these passwords in conjunction with other personal information can be used to derive working credentials for employer resources.
Collecting this information manually is a tedious process, so we developed a tool that helped us quickly identify any leaked employee information associated with our clients.
The tool proved to be incredibly useful for our team while it was used internally. Still, we recognized the potential benefits it could offer to other organizations facing similar security challenges. Therefore, we made the decision to open-source the tool.

Our security tool enables the collection of personal information through Open Source Intelligence techniques. It begins by taking a company domain and retrieving a list of employees from LinkedIn. It then gathers data on individuals across various social media platforms, such as Twitter, LinkedIn, GitHub, GitLab, and more, with the goal of obtaining personal email addresses. Once these email addresses are found, the tool searches through the COMB database and other internet sources to check if the user's password has been exposed in any leaks.

We believe that by making this tool openly available, we can help organizations proactively identify and mitigate the risk associated with leaked employee credentials, ultimately contributing to a more secure digital ecosystem for everyone.

</details>

<details><summary><strong>Hacking generative AI with PyRIT</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Raja Sekhar Rao Dheekonda](https://img.shields.io/badge/Raja%20Sekhar%20Rao%20Dheekonda-informational)

🔗 **Link:** [Hacking generative AI with PyRIT](https://github.com/Azure/PyRIT)  
📝 **Description:** In today's digital landscape, generative AI (GenAI) systems are ubiquitous, powering everything from simple chatbots to sophisticated decision-making systems. These technologies have revolutionized our daily interactions with digital platforms, enhancing user experiences and productivity. Despite their widespread utility, these advanced AI models are susceptible to a range of security and safety risks, such as data exfiltration, remote code execution, and the generation of harmful content. Addressing these challenges, PyRIT (Python Risk Identification Toolkit for generative AI), developed by the Microsoft AI Red Team, stands out as a pioneering tool designed to identify these risks associated with generative AI systems.
PyRIT empowers security professionals and machine learning engineers to proactively identify risks within their generative AI systems, enabling the assessment of potential risks before they materialize into real-world threats. Traditional methods of manual probing for uncovering vulnerabilities are not only time-consuming but also lack the precision and comprehensiveness required in the fast-evolving landscape of AI security. PyRIT addresses this gap by providing an efficient, effective, and extensible framework for identifying security and safety risks, thereby ensuring the responsible deployment of generative AI systems. It is important to note that PyRIT is not a replacement for manual red teaming of generative AI systems. Instead, it enhances the process by allowing red team operators to concentrate on tasks that require greater creativity. PyRIT helps to assess the robustness of these generative AI models against different responsible AI harm categories such as fabrication/ungrounded content (e.g., hallucination), misuse (e.g., bias), and prohibited content (e.g., harassment).
By the end of this talk, you will understand the presence of security and safety risks within generative AI systems. Through demonstrations, I'll show how PyRIT can effectively identify these risks in AI systems, including those based on text and multi-modal models. This session is designed for security experts involved in red teaming generative AI models and for software/machine learning professionals developing foundational models, equipping them with the necessary tools to detect security and safety vulnerabilities.
Key Features of PyRIT include:
1. Scanning of GenAI models utilizing prompt injection techniques.
2. Support for various attack strategies, including single-turn and multi-turn engagements.
3. Compatibility with Azure OpenAI LLM endpoints, enabling targeted assessments. Easy to extend to custom targets.
4. Prompt Converters: Probe the GenAI endpoint with a variety of converted prompts (Ex., Base64, ASCII).
5. Memory: Utilizes DuckDB for efficient and scalable storage of conversational data, facilitating the storage and retrieval of chat histories, as well as supporting analytics and reporting.

</details>

<details><summary><strong>Octopii v2</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Owais Shaikh](https://img.shields.io/badge/Owais%20Shaikh-informational)

🔗 **Link:** [Octopii v2](https://github.com/redhuntlabs/Octopii)  
📝 **Description:** Octopii is a Personally Identifiable Information (PII) scanner that uses Optical Character Recognition (OCR), regular expression lists and Natural Language Processing (NLP) to search public-facing locations for Government ID, addresses, emails etc in images, PDFs and documents.

</details>

<details><summary><strong>OSINT-Collector</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Nniver d'Ambrosio](https://img.shields.io/badge/Nniver%20d'Ambrosio-informational)

🔗 **Link:** Not Available  
📝 **Description:** This project proposes an advanced framework for integrating and unifying the management of OSINT data. Our primary objective is to develop an intuitive user interface that streamlines the collection, organization, and analysis of these data. Moreover, our tool will leverage cutting-edge algorithms and methodologies to enhance the filtering, analysis, and correlation of collected data. Specifically, our focus lies in the development of sophisticated techniques for extracting valuable insights, making informed inferences, and uncovering hidden relationships. Central to our approach is the integration of Knowledge Graphs (KGs), Ontologies, and Natural Language Processing (NLP) techniques. Knowledge Graphs offer a structured representation of information, encapsulating entities, relationships, and their interconnectedness in a semantic graph format. Complementing this, NLP techniques empower the extraction of meaningful insights from unstructured textual data, including social media posts, news articles, and forum discussions. Additionally, ontologies play a pivotal role in imbuing unstructured data with semantic meaning, thereby contextualizing them within the pertinent domain. Through the seamless integration of these cutting-edge methodologies, our framework aims to empower users of all technical proficiencies to extract invaluable information from the vast expanse of OSINT data. Specifically, our tool facilitates OSINT investigations and aids in the identification of individuals potentially linked to criminal or terrorist activities. Through its robust capabilities, our framework stands as a powerful ally in the quest for actionable intelligence and informed decision-making.

</details>

<details><summary><strong>ThePhish: an automated phishing email analysis tool</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Emanuele Galdi](https://img.shields.io/badge/Emanuele%20Galdi-informational) ![Angelo Delicato](https://img.shields.io/badge/Angelo%20Delicato-informational)

🔗 **Link:** Not Available  
📝 **Description:** ThePhish is an automated phishing email analysis tool based on TheHive, Cortex and MISP. It is a web application written in Python 3 and based on Flask that automates the entire analysis process starting from the extraction of the observables from the header and the body of an email to the elaboration of a verdict which is final in most cases. In addition, it allows the analyst to intervene in the analysis process and obtain further details on the email being analyzed if necessary. In order to interact with TheHive and Cortex, it uses TheHive4py and Cortex4py, which are the Python API clients that allow using the REST APIs made available by TheHive and Cortex respectively.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Apeman: The AWS Policy Evaluation Manager</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Daniel Heinsen](https://img.shields.io/badge/Daniel%20Heinsen-informational)

🔗 **Link:** Not Available  
📝 **Description:** Apeman is a tool designed to simplify the understanding of permissions and potential attack paths within an AWS (Amazon Web Services) environment for both attackers and defenders. AWS's permission model is inherently complex, featuring a detailed policy evaluation system, fine-grained policies, potentially conflicting statements, and various conditions. This complexity can make it challenging to manually determine which principals (users, roles, etc.) have permissions to perform certain actions, leading to a process that is not only tedious but also prone to errors. Apeman addresses this issue by modeling the AWS permission structure within a graph database. This approach enables it to provide an intuitive interface for users to navigate and obtain clear, precise answers about which principals can execute specific actions within the AWS environment. Essentially, it translates the intricate web of AWS permissions into a more understandable and visually navigable format. Furthermore, Apeman offers the capability to dynamically categorize principals into different tiers based on their permissions. Specifically, it can identify which principals or groups of principals are considered "Tier 0." This categorization is crucial because it highlights the principals with the most significant level of access or potential impact, thereby giving users a clearer understanding of the security posture of their AWS environment. By identifying these high-risk entities, Apeman can help identify which access points are the most crucial for securing or attacking an AWS environment.

</details>

<details><summary><strong>Artemis: modular vulnerability scanner with automatic report generation</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Krzysztof Zając](https://img.shields.io/badge/Krzysztof%20Zając-informational)

🔗 **Link:** [Artemis: modular vulnerability scanner with automatic report generation](https://github.com/kazet)  
📝 **Description:** Artemis is a modular vulnerability scanner powering CERT PL (Polish national CERT) large-scale scanning activities. It checks various aspects of website security and builds easy-to-read reports informing organizations about the scanning results.

Since the beginning of 2023, we scanned almost 500 thousand domains and subdomains in our constituency and found more than 200 thousand vulnerabilities and misconfigurations. Identified issues ranged from minor - lack of proper SSL or DMARC configuration, to critical, such as SQL Injection and RCEs.

During the presentation, I'll describe the way Artemis works, what we are looking for, and most significantly - lessons we've learned during our large-scale scanning project. Since the tool is open-source, I'll touch upon how to set up your own scanning pipeline and implement new modules.

</details>

<details><summary><strong>Blackdagger</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Mahmut Erdem Ozgen](https://img.shields.io/badge/Mahmut%20Erdem%20Ozgen-informational) ![Ata Seren](https://img.shields.io/badge/Ata%20Seren-informational) ![Regaip Kurt](https://img.shields.io/badge/Regaip%20Kurt-informational)

🔗 **Link:** [Blackdagger](https://github.com/ErdemOzgen)  
📝 **Description:** Blackdagger represents a significant advancement, offering a comprehensive solution for orchestrating complex workflows in DevOps, DevSecOps, MLOps, MLSecOps, and Continuous Automated Red Teaming (CART) environments.

At its core, Blackdagger simplifies the management and execution of intricate workflows through its user-friendly approach and powerful functionality. Leveraging a declarative YAML format, Blackdagger enables users to define automation pipelines using a Directed Acyclic Graph (DAG), facilitating clear and concise expression of task dependencies and execution logic.

What sets Blackdagger apart is its simplicity and versatility. Unlike traditional cron-based schedulers or workflow orchestration platforms, Blackdagger eliminates the need for extensive scripting or coding. With a built-in Web UI, users can easily manage, rerun, and monitor automation pipelines in real-time, streamlining the workflow management process. Additionally, Blackdagger offers native Docker support, enabling seamless integration with containerized environments, and a versatile toolset for task execution, including making HTTP requests and executing commands over SSH.
Blackdagger stands out due to its comprehensive features aimed at simplifying and enhancing automation workflow management.

Highlights of Blackdagger

* Single binary file installation
* Declarative YAML format for defining DAGs
* Web UI for visually managing, rerunning, and monitoring pipelines
* Use existing programs without any modification
* Self-contained, with no need for a DBMS
* Suitable for Continuous Red Teaming (CART)
* Suitable for DevOps and DevSecOps
* Suitable for MLOps and MLSecOps

</details>

<details><summary><strong>BugHog</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Gertjan Franken](https://img.shields.io/badge/Gertjan%20Franken-informational) ![Tom Van Goethem](https://img.shields.io/badge/Tom%20Van%20Goethem-informational)

🔗 **Link:** [BugHog](https://github.com/DistriNet/BugHog)  
📝 **Description:** BugHog is a comprehensive framework designed to identify the complete lifecycle of browser bugs, from the code change that introduced the bug to the code change that resolved the bug. For each bug's proof of concept (PoC) integrated in BugHog, the framework can perform automated and dynamic experiments using Chromium and Firefox revision binaries.

Each experiment is performed within a dedicated Docker container, ensuring the installation of all necessary dependencies, in which BugHog downloads the appropriate browser revision binary, and instructs the browser binary to navigate to the locally hosted PoC web page. Through observation of HTTP traffic, the framework determines whether the bug is successfully reproduced. Based on experiment results, BugHog can automatically bisect the browser's revision history to identify the exact revision or narrowed revision range in which the bug was introduced or fixed.

BugHog has already been proven to be a valuable asset in pinpointing the lifecycle of security bugs, such as Content Security Policy bugs.

</details>

<details><summary><strong>CVE Half-Day Watcher: Hunting Down Vulnerabilities Before the Patch Drops</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Yakir Kadkoda](https://img.shields.io/badge/Yakir%20Kadkoda-informational) ![Mor Weinberger](https://img.shields.io/badge/Mor%20Weinberger-informational)

🔗 **Link:** Not Available  
📝 **Description:** Defenders and attackers often simplify vulnerabilities into '0-day' or '1-day' categories, neglecting the nuanced gray areas where attackers thrive. In this session, we'll explore critical flaws we've uncovered in the open-source vulnerability disclosure process and introduce our tool to detect open-source projects that are at risk from these flaws. We'll reveal how vulnerabilities can be exploited prior to receiving patches and official announcements, posing significant risks for users. Our comprehensive analysis of GitHub (including issues, pull requests, and commit messages) and NVD metadata will illuminate vulnerabilities that don't neatly fit into the conventional '0-day' or '1-day' classifications but instead fall into 'Half-Day' or '0.75-Day' periods – moments when vulnerabilities are known but not yet fully disclosed or patched. Furthermore, we'll spotlight the techniques employed to identify these vulnerabilities, showcasing various scenarios and vulnerabilities discovered through this method. During this session, we'll introduce an open-source tool designed to detect such vulnerabilities and emphasize the window of opportunity for attackers to exploit this information and develop exploits. Our objective is to aid practitioners in identifying and mitigating issues throughout their vulnerability disclosure lifecycle.

</details>

<details><summary><strong>Graph for Understanding Artifact Composition (GUAC)</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Parth Patel](https://img.shields.io/badge/Parth%20Patel-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Managed Kubernetes Auditing Toolkit (MKAT): Bridge the gap between your cluster and your cloud</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Christophe Tafani-Dereeper](https://img.shields.io/badge/Christophe%20Tafani-Dereeper-informational) ![Andrew Krug](https://img.shields.io/badge/Andrew%20Krug-informational)

🔗 **Link:** Not Available  
📝 **Description:** Most organizations nowadays run Kubernetes on a managed cloud service such as Amazon EKS, Google Cloud GKE or Azure AKS. A number of cloud-specific attack vectors exist in this context, allowing pods to pivot to the cloud environment in often unexpected ways.

The Managed Kubernetes Auditing Toolkit (MKAT) brings several features that help you bridge the gap:
- Identify cloud secrets in Kubernetes resources
- Produce a visual map of which pods have access to the cloud environment
- Test if pod access to the instance metadata service is properly blocked

</details>

<details><summary><strong>SimpleRisk: Governance, Risk Management and Compliance</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

🔗 **Link:** [SimpleRisk: Governance, Risk Management and Compliance](https://github.com/OWASP/www-chapter-austin/blob/master/pasteventsarchive.md)  
📝 **Description:** As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform organizational Governance, Risk Management, and Compliance activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to manage control frameworks, policies, and exceptions, facilitate audits, and perform risk prioritization and mitigation activities. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

</details>

<details><summary><strong>Snapback: Wicked Fast HTTP(S) Screenshots with Automated Password Guessing</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational)

🔗 **Link:** Not Available  
📝 **Description:** Web applications with weak or default passwords are a common easy win for penetration testers. Frequently, network appliances expose a web application for device management that IT staff are not aware of, and therefore never lock down. The only problem for penetration testers is the time it takes to sift through hundreds or even thousands of web interfaces to find ones with weak credentials. This process is usually performed by first taking screenshots of each web service, and then manually searching for the default credentials for each one and manually attempting each credential pair. To greatly speed up the process, Snapback was designed to automatically fingerprint and brute force passwords while taking each screenshot. All of the fingerprinting and brute forcing code is modular, allowing easy extension for newly identified services.

</details>

<details><summary><strong>TheAllCommander 2.0</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Matthew Handy](https://img.shields.io/badge/Matthew%20Handy-informational)

🔗 **Link:** [TheAllCommander 2.0](https://github.com/matt-handy/TheAllCommander)  
📝 **Description:** TheAllCommander was developed originally to provide rapid modelling and testing for novel Command and Control (C2) communications techniques for both Red team development and Blue team defensive modelling. Since inception and since the tool's original launch at Defcon 2022, the tool has evolved to include a flexible framework for modelling client and network Indicators of Compromise (IOC) based on user requests and feedback. By default, the tool is bundled with several emulations of common techniques used by real world threat actors. For every IOC simulation it provides, there is a corresponding set of recommendations for detection and mitigation as part of the tool's Blue Team Guide, which may be implemented by defenders and then directly tested for efficacy with the tool.

TheAllCommander has also been expanded with additional interoperability with modern tradecraft. For example, the tool has been augmented to provide threat emulation of Powershell reverse shells.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>APIDetector: Advanced Swagger Endpoint Detection and Vulnerability Analysis</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Rafael Brinhosa](https://img.shields.io/badge/Rafael%20Brinhosa-informational)

🔗 **Link:** [APIDetector: Advanced Swagger Endpoint Detection and Vulnerability Analysis](https://github.com/brinhosa/apidetector)  
📝 **Description:** APIDetector is a specialized tool crafted to identify and analyze exposed Swagger documentation endpoints across a multitude of web domains and subdomains efficiently. It stands out for its capability to scan over both HTTP and HTTPS protocols while leveraging multi-threading to enhance the speed of security assessments. Designed with a user-friendly interface, it supports various input and output configurations, making it versatile for different security testing scenarios. APIDetector is particularly adept at minimizing false positives, a common challenge in automated scanning tools, thanks to its intelligent detection algorithms. This tool is indispensable for security professionals and developers focused on API security and vulnerability management. It simplifies the process of identifying potentially risky Swagger endpoints that could expose sensitive API details to unauthorized users, thereby bolstering an organization's cybersecurity posture. The tool's effectiveness in real-world scenarios has been validated by its growing user base and positive feedback within the cybersecurity community.

</details>

<details><summary><strong>Faraday: an Open Source Vulnerability Management Platform</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Federico Kirschbaum](https://img.shields.io/badge/Federico%20Kirschbaum-informational)

🔗 **Link:** [Faraday: an Open Source Vulnerability Management Platform](https://github.com/PortSwigger/faraday_old)  
📝 **Description:** Security has two difficult tasks: designing smart ways of getting new information, and keeping track of findings to improve remediation efforts. With Faraday, you may focus on discovering vulnerabilities while we help you with the rest. Just use it in your terminal and get your work organized on the run. Faraday was made to let you take advantage of the available tools in the community in a truly multiuser way.

Faraday aggregates and normalizes the data you load, allowing exploring it into different visualizations that are useful to managers and analysts alike.

</details>

<details><summary><strong>Open-Source API Firewall by Wallarm - Advanced Protection for REST and GraphQL APIs</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tim Erlin](https://img.shields.io/badge/Tim%20Erlin-informational)

🔗 **Link:** Not Available  
📝 **Description:** Introduced at Blackhat 2024 Arsenal, the open-source API Firewall has been significantly upgraded, now extending its protection capabilities to include GraphQL endpoints, in addition to its existing support for REST APIs.

Operating as a high-efficiency intermediary, this API Firewall ensures strict API request and response validation, adhering to both OpenAPI and GraphQL schemas. By employing a positive security model, it enhances API security by allowing only the traffic that meets a predetermined API specification for requests and responses, effectively blocking all other traffic. It's designed to work in cloud-native environments with a huge amount of traffic and is optimized for near-zero latency.

The key features of Wallarm's API Firewall are:
- Endpoint Security: Secure REST and GraphQL API endpoints by blocking non-compliant requests/responses
- Data Breach Prevention: Stop API data breaches by blocking malformed API responses
- Shadow API Discovery: Discover Shadow API endpoints
- Specification Adherence: Block attempts to use request/response parameters not specified in an OpenAPI specification
- Token Validation: Validate JWT access tokens and other OAuth 2.0 tokens using introspection endpoints
- Security Enhancements: Denylist compromised API tokens, keys, and cookies
- Wide Range Attacks Protection: The API Firewall supports ModSecurity Rules and OWASP Core RuleSet v3/v4

This product is open-source and can be found on DockerHub, where it has impressively reached 1 billion downloads.

</details>

<details><summary><strong>Open-Source GoTestWAF by Wallarm: New Features</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tim Erlin](https://img.shields.io/badge/Tim%20Erlin-informational)

🔗 **Link:** Not Available  
📝 **Description:** GoTestWAF is a well-known open-source tool for evaluating Web Application Firewalls (WAFs), Runtime Application Self-Protection (RASPs), Web Application and API Protection (WAAP), and other security solutions by simulating attacks on the protected applications and APIs. The tool supports an extensive array of attack vectors, evasion techniques, data encoding formats, and runs tests across various protocols, including traditional web interfaces, RESTful APIs, WebSocket communications, gRPC, and GraphQL. Upon completion of the tests, it generates an in-depth report grading efficiency of solution and mapping it against OWASP guidelines.

The recently added features to the GoTestWAF are:
- Vendor Identification/Fingerprinting: With session handling improvements, GoTestWAF can automatically identify security tools/vendors and highlights findings in the report.
- OWASP Core Rule Set Testing: A script is added to generate test sets from the OWASP Core Rule Set regression testing suite. These vectors are not available by default and require additional steps as outlined in the readme.
- Regular Expressions for WAF Response Analysis: Regular expressions can be used to analyze WAF responses.
- Cookie Handling: GoTestWAF can consider cookies during scanning and update the session before each request. This allows scanning hosts that require specific WAF-specific cookies, as otherwise, requests are blocked.
- Email Report Sending: GoTestWAF interactively prompts for an email address to send the report.
- New Placeholders: Numerous new placeholders have been added, listed in the readme's "How It Works" section.

</details>

<details><summary><strong>Revealing 2MS: New Secrets Detection Open Source, the Connection to Supply Chain Attacks, and The Developer's Responsibility</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tzachi Zorenshtain](https://img.shields.io/badge/Tzachi%20Zorenshtain-informational) ![Tal Folkman](https://img.shields.io/badge/Tal%20Folkman-informational) ![Ori Ron](https://img.shields.io/badge/Ori%20Ron-informational)

🔗 **Link:** Not Available  
📝 **Description:** Too many secrets (2ms) is a command line tool written in Go language and built over gitleaks. 2ms is capable of finding secrets such as login credentials, API keys, SSH keys and more hidden in code, content systems, chat applications and more.

https://github.com/checkmarx/2ms

</details>

<details><summary><strong>ROADtools - A collection of Azure AD/Entra tools for offensive and defensive security purposes</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Dirk-jan Mollema](https://img.shields.io/badge/Dirk-jan%20Mollema-informational)

🔗 **Link:** [ROADtools - A collection of Azure AD/Entra tools for offensive and defensive security purposes](https://github.com/dirkjanm/ROADtools)  
📝 **Description:** ROADtools is a collection of tools for assessing and defending the security of Microsoft Entra (formerly Azure AD) security. The most notable tools in the framework are ROADrecon and roadtx (ROADtools Token eXchange). ROADrecon is a versatile reconnaissance tool that gives both attackers and defenders deep insights into Azure AD internals. Utilizing undocumented internal API's, it provides insights that are hard to find using official tooling, can bypass security restrictions set by admins, and provides offline access to tenant information through its offline database. Defenders can use ROADrecon to create easy overviews of risky permissions in the tenant, identify hidden permissions on applications and other objects. Roadtx is a new tool in the ROADtools family. Its goal is to support all official and non-official authentication flows and methods of the Microsoft Identity platform, ranging from standard OAuth flows to undocumented and legacy token flows for user and device authentication. The strength of roadtx is its versatility in customizing and modifying the authentication flow, to obtain a variety of authentication tokens that can bypass weakly protected security measures, or to create identity based persistence in the form of devices, Primary Refresh Tokens and Windows Hello keys. Roadtx also supports many different ways of authenticating for automation purposes, making it a tool that cannot be missed for identity security researchers. In the demonstration, we will also demonstrate its lesser-known extension, ROADtools hybrid, which provides protocol implementations for hybrid AD and Entra environments. With ROADtools hybrid, we can perform lateral movement from on-premises AD to Entra, using Sync accounts and Kerberos with Seamless SSO.

</details>

---
## Others
<details><summary><strong>Hooke 2.0: Addressing Privacy and Security Concerns in Mobile Applications</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Yijie Zhao](https://img.shields.io/badge/Yijie%20Zhao-informational) ![Huaisi Liao](https://img.shields.io/badge/Huaisi%20Liao-informational) ![Yu Lan](https://img.shields.io/badge/Yu%20Lan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Hooke 2.0 is an upgraded mobile application privacy and security tool that was initially unveiled at BlackHat USA Arsenal in 2022. It has since undergone significant updates, introducing several key enhancements.

One major enhancement is the advanced dynamic monitoring module. This module builds upon the existing Frida-based monitoring capabilities and introduces two additional monitoring abilities: repackaging monitoring and custom app monitoring. Repackaging monitoring allows for monitoring app behavior on non-rooted devices. AOSP monitoring enables the monitoring of highly protected apps.

Another significant improvement is the groundbreaking network packet capture feature that enables the extraction and analysis of QUIC/HTTP3 protocol packets. This is a notable advancement as there have been no publicly available solutions for capturing QUIC/HTTP3 packets on mobile devices to date. Leveraging memory scanning techniques and network library characteristics, Hooke 2.0 captures packets for various HTTP protocols on both Android and iOS devices. This expanded functionality provides valuable insights into protocol behavior and security.

Furthermore, Hooke 2.0 presents a real-time analysis system with a unified interface that combines dynamic run-time behaviour monitoring and network packet analysis with contextual app information. This integration empowers users to gain a comprehensive understanding of an app's runtime behavior and operations.

</details>

<details><summary><strong>PIZZAbite & BRUSCHETTA-board: THE Hardware Hacking Toolkit!</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

🔗 **Link:** [PIZZAbite & BRUSCHETTA-board: THE Hardware Hacking Toolkit!](https://github.com/whid-injector/BRUSCHETTA-board)  
📝 **Description:** In the last decade we have witnessed the emerging of a new era of connected devices. With this new trend, we also faced a security knowledge gap that in the recent years emerged respect to the (I)IoT landscape. The lack of a properly-defined workflow to approach a security audit of (I)IoT devices and the lack of technical expertise among security personnel in relation to embedded hardware security worsen this gap even further. To bring some clarity and order to this complicated and variegated matter It has been developed PIZZAbite & BRUSCHETTA-board: an all-in-one hardware hacking toolkit that can be considered the swiss-army-knife of any hardware hacker.
BRUSCHETTA-board is the latest device of the so-called WHID's CyberBakery family. It all started in 2019 from a personal need. The idea was to have a board that could gather in one single solution mutliple tools used by hardware hackers to interact with IoT and Embedded targets. It is the natural evolution of the other boards already presented in the past at BlackHat Arsenal: Focaccia-Board, Burtleina-Board and NANDo-Board. It has been designed for any hardware hacker out there that is looking for a fairly-priced all-in-one debugger & programmer that supports: UART, JTAG, I2C & SPI protocols and allows to interact with different targets' voltages (i.e., 1.8, 2.5, 3.3 and 5 Volts!).
PIZZAbite is a cheaper and open-hardware version of a commercial PCB holder, perfect for probing & holding your PCB while soldering or inspection. The PIZZAbite PCB probes are mounted on flexible metal arm and a powerful magnet in the base for easy positioning. The one of the kind "lift and drop" function takes away the need for annoying and complicated set screws. Thanks to the extreme flexibility of the arms connected to the PIZZAbite PCBs, the compressible needle (a.k.a. PogoPin) maintain constant pressure at the probing point so even if the board is bumped into the probe tip will always stay in position.
In this presentation, we will review with practical examples how PIZZAbite & BRUSCHETTA-board work against real IoT devices.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Horusec: Elevating Vulnerability Detection in your code.</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Filipi Pires](https://img.shields.io/badge/Filipi%20Pires-informational) ![Gilmar Esteves](https://img.shields.io/badge/Gilmar%20Esteves-informational)

🔗 **Link:** Not Available  
📝 **Description:** Horusec is an open source tool that performs static code analysis to identify security flaws during the development process. Currently, the languages for analysis are: C#, Java, Kotlin, Python, Ruby, Golang, Terraform, Javascript, Typescript, Kubernetes, PHP, C, HTML, JSON, Dart, Elixir, Shell, Nginx, Swift. The tool has options to search for key leaks and security flaws in all files of your project, as well as in Git history. Horusec can be used by the developer through the CLI and by the DevSecOps team on CI /CD mats.

</details>

<details><summary><strong>JDoop: A black-box static analysis tool for Java web applications</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![HaoHao Chen](https://img.shields.io/badge/HaoHao%20Chen-informational)

🔗 **Link:** Not Available  
📝 **Description:** JDoop is a black-box static analysis tool for Java Web applications improved based on Doop. Using taint analysis, it currently supports scanning for command injection, SQLI injection, JDBC deserialization and other data flow types of vulnerabilities.

We have improved the context Sensitive strategies and PT Analysis algorithms are adapted to the Servlet and spring frameworks, which effectively improves the accuracy of analysis compared to other tools.

</details>

<details><summary><strong>PinguCrew</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Alejo Moles Ramos](https://img.shields.io/badge/Alejo%20Moles%20Ramos-informational)

🔗 **Link:** Not Available  
📝 **Description:** PinguCrew is a web-based fuzzer platform that allows security researchers to test their software for vulnerabilities in a scalable and efficient manner.

PinguCrew runs the tests on the user's own machines, giving them full control over the fuzzing process. This allows for more customization and flexibility, as users can set up their own testing environments with their desired configurations and testing parameters.

</details>

<details><summary><strong>Surfactant - Modular Framework for File Information Extraction and SBOM Generation</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational)

🔗 **Link:** Not Available  
📝 **Description:** Surfactant is a modular framework for extracting information from filesystems, primarily for generating an SBOM (Software Bill of Materials). The information extracted can then be used to identify the various vendors or libraries associated with a file, and establish relationships between files. The resulting SBOM can be used for system level impact analysis (such as for IoT, Smart Grid, or ICS devices) of vulnerabilities, and the information gathered can be used to help inform what files to focus on for manual analysis.

Several recently added features will be demonstrated, including functionality for helping visualize the contents of a file system and the relationships between files. The initial results from integrating new methods to identify the package that files (compiled binaries or scripts) belong to will also be discussed.

</details>

---