# USA 2023
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2023** event held in **USA**.
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
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🔴 Red Teaming
<details><summary><strong>Abusing Microsoft SQL Server with SQLRecon</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sanjiv Kawa](https://img.shields.io/badge/Sanjiv%20Kawa-informational)

🔗 **Link:** [Abusing Microsoft SQL Server with SQLRecon](https://github.com/Tw1sm/PySQLRecon)  
📝 **Description:** In November 2022, Kaspersky Lab publicly released research which outlined that reoccurring attacks against Microsoft SQL Server rose by 56% (https://usa.kaspersky.com/about/press-releases/2022_kaspersky-finds-reoccurring-attacks-using-microsoft-sql-server-rise-by-56-in-2022).

I'd like to share a tool I wrote called SQLRecon, which will demonstrate how adversaries are leveraging Microsoft SQL services to facilitate with furthering their presence within enterprise networks through privilege escalation and lateral movement. I will also share defensive considerations which organizations can practically implement to mitigate attacks. I feel that this will add a fresh perspective on the various ancillary services within enterprise Windows networks which are under less scrutiny, however still ripe for abuse.

For red team operators, SQLRecon helps address the post-exploitation tooling gap by modernizing the approach operators can take when attacking SQL Servers. The tool is written in C#, rather than long-standing existing tools that use PowerShell or Python. SQLRecon has been designed with operational security and detection avoidance in mind – with a special focus on stealth, reconnaissance, lateral movement, and privilege escalation. The tool was designed to be modular, allowing for ease of extensibility from the hacker community. SQLRecon is compatible stand-alone or within a diverse set of command and control (C2) frameworks (Cobalt Strike, Nighthawk, Mythic, PoshC2, Sliver, Havoc, etc). When using the latter, SQLRecon can be executed either in-process, or through traditional fork and run.

Furthermore, I will be releasing a new version, one that is currently only used internally on advanced red team engagements by IBM X-Force Red's Adversary Services team.

</details>

<details><summary><strong>Afterimage: Evading Traditional IOC Blocking</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Davis Zheng](https://img.shields.io/badge/Davis%20Zheng-informational) ![Ken Tong](https://img.shields.io/badge/Ken%20Tong-informational) ![Mario Lim](https://img.shields.io/badge/Mario%20Lim-informational) ![Wei Jie Chan](https://img.shields.io/badge/Wei%20Jie%20Chan-informational) ![Weihan Goh](https://img.shields.io/badge/Weihan%20Goh-informational)

🔗 **Link:** Not Available  
📝 **Description:** Malicious IP addresses are critical indicators of cyber threats, and blocking these addresses is a standard practice during network forensics and incident response. Current solutions for maintaining anonymity, such as Tor nodes and botnets, have proven to be either compromised or illegal, thus posing challenges for legitimate red team exercises. In response to this growing demand for an effective solution, we have developed Afterimage, a novel application that enables attackers to enumerate and attack from multiple IP addresses without requiring the infrastructure of a botnet and with minimal time and effort.

Afterimage operates as an intermediary, accepting malicious traffic from an attacker through an open port, forwarding it to a proxy, and ultimately to the victim. If the proxy's IP is blocked, the application automatically cycles to another proxy to continue sending traffic. This process is more efficient and secure than existing methods such as VPNs, which are often monitored and costly, or compromised solutions like Tor nodes and botnets.

Our proposed solution, written in Python, is designed for deployment on remote servers, enabling multiple attackers to connect simultaneously. This unique approach to IP address cycling addresses key challenges faced during red team exercises, providing a more secure and effective solution for cyber security testing. By leveraging Afterimage, blue teams and SOCs can enhance their incident response capabilities and improve their overall cyber defense strategies.

</details>

<details><summary><strong>BloodHound 5.0</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Andy Robbins](https://img.shields.io/badge/Andy%20Robbins-informational) ![Rohan Vazarkar](https://img.shields.io/badge/Rohan%20Vazarkar-informational)

🔗 **Link:** [BloodHound 5.0](https://github.com/ly4k/BloodHound)  
📝 **Description:** BloodHound 5.0 is faster, more powerful, and easier to deploy and use than any previous version. With this major update, we are completely overhauling BloodHound's code and bringing many features from the commercial versions of BloodHound to the free and open source version. That convergence means we can release features much faster, and that the application is much faster than it ever has been. It also means the deployment model is fundamentally changing.


Come see our Arsenal presentation to see how to set up and use BloodHound 5.0, including attack path analysis and execution demonstrations covering on-prem Active Directory and Azure.

</details>

<details><summary><strong>Building Our Nemesis: Fighting Data with Data</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Lee Christensen](https://img.shields.io/badge/Lee%20Christensen-informational) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational) ![Max Harley](https://img.shields.io/badge/Max%20Harley-informational)

🔗 **Link:** Not Available  
📝 **Description:** The offensive industry is about exploring what's possible. Part of this is observing and taking lessons from other disciplines that have already solved a myriad of related challenges, from proper software engineering practices to using graph theory for offensive problems. But despite various leaps forward over the last several years, the offensive post-exploitation community has yet to fully embrace data analysis and enrichment pipelines beyond basic log aggregation and searching. If offensive tools were structured for automated processing instead of solely human consumption, we could unify post-ex data to exploit the known (and unknown) relationships within the data our offensive tools emit.

Imagine a system that could ingest data from any C2 framework or post-ex tool, and could not just automate common operator tasks like binary analysis for known vulnerabilities and hash extraction and cracking of encrypted documents, but could perform complex offline analysis like host privilege escalation. If we could unify all post-exploitation data from offensive engagements we could improve operator workflows, provide tradecraft assistance, facilitate automation of onerous tasks, and uncover new data-driven research opportunities. A year ago, our team embarked on the development of just such a system, and we are excited to introduce the result of our effort: Nemesis.

</details>

<details><summary><strong>Commando VM and FLARE VM: Enhanced Toolsets for Penetration Testing and Windows-Based Malware Analysis</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![George Litvinov](https://img.shields.io/badge/George%20Litvinov-informational) ![Alex Tselevich](https://img.shields.io/badge/Alex%20Tselevich-informational) ![Jake Barteaux](https://img.shields.io/badge/Jake%20Barteaux-informational) ![Dennis Tran](https://img.shields.io/badge/Dennis%20Tran-informational) ![Joseph Clay](https://img.shields.io/badge/Joseph%20Clay-informational)

🔗 **Link:** [Commando VM and FLARE VM: Enhanced Toolsets for Penetration Testing and Windows-Based Malware Analysis](https://github.com/mandiant/commando-vm)  
📝 **Description:** We are excited to release the latest version of Commando VM and showcase recent advancements of FLARE VM at the Black Hat Arsenal. Commando VM is a virtual machine distribution focused on penetration testing and red teaming. FLARE VM is tailored for malware analysis and reverse engineering. Both Windows-based tools have undergone significant enhancements to improve their usability, functionality, and efficiency. The projects now open source all packages, allowing the community to add and improve tools. Additionally, we have implemented a new GUI installation process to streamline the setup and configuration experience for both new and experienced users.

The latest iteration boasts new profiles for Commando VM, enabling users to tailor their environment to specific penetration testing and red teaming scenarios. Whether the user focuses on Cloud, Web App, or Internal testing, Commando VM has a ready-to-use profile for them with all relevant configurations and toolkit. In addition to that, the user can also create and save their own custom profile, allowing them to easily automate future VM deployments.

Furthermore, we have made substantial quality of life improvements, including debloating and performance optimization, resulting in faster, leaner, and more efficient virtual machines. Users will benefit from these enhancements as they navigate through the intricacies of malware analysis, reverse engineering, and penetration testing with the updated Commando VM and FLARE VM toolsets.

Join us at the Black Hat Arsenal to discover the power and flexibility of the next generation of Commando VM and FLARE VM. We will share how the updated tools can support your workflows in malware analysis, reverse engineering, and penetration testing. Additionally, you will learn how to contribute new tool and code updates benefiting thousands of analysts around the world.

</details>

<details><summary><strong>CuddlePhish: Bypassing MFA on Nearly Impenetrable Web Portals</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational)

🔗 **Link:** Not Available  
📝 **Description:** With the increased adoption of multi-factor authentication, traditional credential harvesting attacks are quickly losing effectiveness. Instead, redteamers have shifted focus away from credential harvesting and are now focussing on session hijacking attacks. Popular redteaming tools like Evilginx2 use transparent proxies to collect both credential AND session cookies from phishing targets. But what if the target service uses more advanced authentication flows like Oauth or SAML? What about apps that use JavaScript to directly thwart MitM attacks? Or even worse, services that don't grant authorization through session cookies at all? Our team has seen many instances of MitM protections like these, and in response, we are raising the bar for session hijacking tradecraft. Instead of using a transparent proxy, our solution leverages browser automation to force target users to log us into services for them. We don't just get to view the traffic. We get full control of an authenticated browser tab. Our solution, CuddlePhish, allows operators to bypass MFA even when MitM protections are in place, target multiple users simultaneously, key log users' credentials, trigger arbitrary javascript on victims' browsers to either redirect them or deliver payloads, and hijack not just session cookies, but authenticated browser tabs themselves. We have successfully used this attack against extremely difficult portals like Gmail and Lastpass.

</details>

<details><summary><strong>EmploLeaks: Finding Leaked Employees Info for the Win</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Gabriel Franco](https://img.shields.io/badge/Gabriel%20Franco-informational) ![Javier Aguinaga](https://img.shields.io/badge/Javier%20Aguinaga-informational)

🔗 **Link:** Not Available  
📝 **Description:** 

</details>

<details><summary><strong>EvilnoVNC: Next-Gen Spear Phishing Attacks</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Joel Gámez Molina](https://img.shields.io/badge/Joel%20Gámez%20Molina-informational)

🔗 **Link:** [EvilnoVNC: Next-Gen Spear Phishing Attacks](https://github.com/JoelGMSec/EvilnoVNC)  
📝 **Description:** One of the main attack vectors in Red Team exercises, and possible entry points for an attacker, are phishing campaigns.

Currently, there are all kinds of tools and countermeasures to perform or defend against them, with a very high level of maturity and fully consolidated by the industry for many years.

On the other hand, there are hardly any tools oriented to Spear Phishing or any other type of more sophisticated attack, regardless of whether you are part of the Red Team or the Blue Team.

In this presentation, and from a totally offensive approach, we will explain how it has been possible to develop a new tool aimed at Spear Phishing, which will use techniques never seen before for this purpose, allowing us to see what the victim is doing in real time, intercept keystrokes with a keylogger, obtain and decrypt cookies, among many other things.

</details>

<details><summary><strong>Exegol: Professional Hacking Setup</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Charlie Bromberg](https://img.shields.io/badge/Charlie%20Bromberg-informational) ![Mathieu Calemard du Gardin](https://img.shields.io/badge/Mathieu%20Calemard%20du%20Gardin-informational)

🔗 **Link:** Not Available  
📝 **Description:** Exegol is a free and open-source pentesting environment made for professionals. It allows pentesters to conduct their engagements in a fast, effective, secure and flexible way. Exegol is a set of pre-configured and finely tuned docker images that can be used with a user-friendly Python wrapper to deploy dedicated and disposable environments in seconds.

</details>

<details><summary><strong>Faraday: Open Source Vulnerability Manager</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Federico Kirschbaum](https://img.shields.io/badge/Federico%20Kirschbaum-informational)

🔗 **Link:** [Faraday: Open Source Vulnerability Manager](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/vulnerability_assessment/faraday.md)  
📝 **Description:** Faraday is a powerful and versatile security tool designed to help cybersecurity professionals perform effective and efficient penetration testing. It is an open-source framework that enables security testers to manage and track their penetration testing activities, from initial reconnaissance to final reporting.

With Faraday, users can integrate multiple tools and methodologies, including vulnerability scanning, exploitation, and post-exploitation techniques. It supports a wide range of tools, such as Metasploit, Nmap, and Burp Suite, and provides a central console to manage all the testing activities.

</details>

<details><summary><strong>GCP Scanner</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Maksim Shudrak](https://img.shields.io/badge/Maksim%20Shudrak-informational) ![Jacob Butler](https://img.shields.io/badge/Jacob%20Butler-informational)

🔗 **Link:** Not Available  
📝 **Description:** Google Cloud Platform (GCP) is a rapidly growing cloud infrastructure with millions of customers worldwide and more than a hundred of various products offered to them. While Cloud offers undeniable benefits in scalability, performance and security, it also opens new and unique challenges for security engineers working with Cloud. One such challenge is credential management.

Cloud credentials such as GCP service account (SA) key can open access to the most critical parts of cloud infrastructure. An incorrectly stored or leaked SA key with such permissions represents high interest for an attacker. Security engineers need to understand the impact of such key leak/compromise to draft a proper security response.

The main objective of GCP Scanner is to offer the community a tool that can be used to evaluate the security impact of a given cloud identity compromise. Security engineers can use this tool to assess the impact of a certain credentials leak, OAuth2 token, potential compromise of a GCP VM or Kubernetes pod.

By now, the only option available was to rely on heavy-weight solutions or time-consuming manual analysis that require privileged access to the affected GCP organization. In contrast, the GCP Scanner works with individual credentials and offers an easy-to-use solution that can be executed from various types of environments with just a single command.

In the demo, we will talk about the scanner architecture and show the audience on how to use the tool in various types of situations (leaked GCP service account key, compromised end-user credentials, VMs and Docker containers, standalone binary from any machine). We will also cover how the scanner can be used to evaluate whether a GCP SA key can be used to impersonate other service accounts and understand potential impact.

</details>

<details><summary><strong>Konstellation: RBACpacking in Kubernetes</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Zach Grace](https://img.shields.io/badge/Zach%20Grace-informational)

🔗 **Link:** Not Available  
📝 **Description:** Konstellation is a new open-source tool that simplifies Kubernetes role-based access control (RBAC) data collection and security analysis. Kubernetes RBAC is a powerful tool to manage access to resources, but its complexity increases exponentially as principals and resources grow, making it challenging to analyze the resulting data at scale. Konstellation uses graph theory to map and analyze all Kubernetes resources and RBAC permissions, which simplifies analysis of RBAC implementations for security vulnerabilities.

Konstellation allows engineers to understand what actions principals are allowed to perform on resources, analyze complex relationships not visible in native Kubernetes or other tools, and find overprovisioning and privilege escalation paths. Additionally, Konstellation is configuration-driven, allowing for quick adaptation to different environments, configurations, and analysis needs.

The tool features three primary modes: enumeration, data ingestion, and querying. The enumeration mode connects directly to a Kubernetes cluster, enumerates each resource type returned by the API server, and writes the results to files in JSON format. Alternatively, Konstellation can ingest kubectl JSON output.

Konstellation is schema-less and uses structured output from enumeration to determine data structures. Every resource instance and its attributes map into a Neo4j node with node properties. Users can query all enumerated resource data from the schema without data loss. After ingesting the resource instances, Konstellation maps relationships using Neo4j cypher queries defined in its configuration.

Query mode allows for rapid data analysis. Konstellation ships with 40+ queries that look for privilege escalation paths and known vulnerable configurations. Users also can perform ad-hoc queries through command line or directly in Neo4j.

Analyzing Kubernetes RBAC weaknesses at scale can be daunting, but Konstellation offers a clear overview of RBAC implementations and simplifies the process of identifying security vulnerabilities.

</details>

<details><summary><strong>Modern Active Directory Attacks with the Metasploit Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

🔗 **Link:** [Modern Active Directory Attacks with the Metasploit Framework](https://github.com/SP2-MC2/Readability-Resources/blob/master/cyberDictionary.txt)  
📝 **Description:** Active Directory is the foundation of the infrastructure for many organizations. As of 2023, Metasploit has added a wide range of new capabilities and attack workflows to support Active Directory exploitation. This Arsenal demonstration will cover new ways to enumerate information from LDAP, attacking Active Directory Certificate Services (AD CS), leveraging Role Based Constrained Delegation, and using Kerberos authentication.

The Kerberos features added in Metasploit 6.3 will be a focal point. The audience will learn how to execute multiple attack techniques, including Pass-The-Ticket (PTT), forging Golden/Silver Tickets, and authenticating with AD CS certificates. Finally, users will see how these attack primitives can be combined within Metasploit to streamline attack workflows with integrated ticket management. The demonstration will also highlight inspection capabilities that are useful for decrypting traffic and tickets for debugging and research purposes.

</details>

<details><summary><strong>PowerGuest: AAD Guest Exploitation Beyond Enumeration</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Bargury](https://img.shields.io/badge/Michael%20Bargury-informational) ![Lana Salameh](https://img.shields.io/badge/Lana%20Salameh-informational)

🔗 **Link:** Not Available  
📝 **Description:** Azure AD guest accounts are widely used to grant external parties limited access to enterprise resources, with the assumption that these accounts pose little security risk. As you're about to see, this assumption is dangerously wrong.

PowerGuest is a new tool that allows you to achieve the full potential of a guest in Azure AD by exploiting a series of undocumented internal APIs and common misconfiguration for collecting privileges, and using those for data exfiltration and actions on target, leaving no traces behind. The tool operates by leveraging shared credentials shared over Power Platform, a low-code / no-code platform built into Office365.

PowerGuest allows gaining unauthorized access to sensitive business data and capabilities including corporate SQL servers, SharePoint sites, and KeyVault secrets. Furthermore, it allows guests to create and control internal business applications to move laterally within the organization. All capabilities are fully operational with the default Office 365 and Azure AD configuration.

</details>

<details><summary><strong>Scanhanced: An Automation Tool for Pentesting and Vulnerability Assessments</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![David Niederweis](https://img.shields.io/badge/David%20Niederweis-informational)

🔗 **Link:** Not Available  
📝 **Description:** A lot of the initial steps in black box penetration testing involve information gathering using techniques such as port scanning. This information is then usually used for OSINT such as searching for known vulnerabilities for the found services and versions. Next steps often include searching for exploits for the found vulnerabilities. This process is inconvenient as it is often both labor and time intensive, both of which can often be a limiting factor for an engagement.
Scanhanced solves this by providing an easy command line interface that can then perform the previously mentioned steps automatically, reducing both labor and time needed to minutes. It will perform a port scan, and then using that information attempt to find vulnerabilities and search community resources for exploits. Additionally, Scanhanced provides additional features such as identifying whether a given exploit is available in existing exploit frameworks, being able to download exploits, or download the vulnerable apps in question. Moreover, Scanhanced can produce output in JSON, XML, or CSV for use in further automation or ingestion into another tool if so desired.
This entire process in addition to more complex functionality can be performed with an easy to use command and flags, saving pentesters time and from having to do tedious work.

</details>

<details><summary><strong>SecScanC2 -- Manage Assesment to Create P2P Network for Security Scanning & C2</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Weichao Zhou](https://img.shields.io/badge/Weichao%20Zhou-informational) ![Yue Zhuo](https://img.shields.io/badge/Yue%20Zhuo-informational) ![Hongwei Pan](https://img.shields.io/badge/Hongwei%20Pan-informational)

🔗 **Link:** Not Available  
📝 **Description:** In the realm of security attack and defense, as well as penetration testing, two key challenges often arise. Firstly, attack scanning is frequently detected by defensive security systems, resulting in the scanning IP being blocked. Secondly, when defensive assets are controlled and connected back to the command and control (C2) server, security devices may detect the connection, leading to countermeasures against penetration testers. To address these challenges and enable safe, efficient asset detection and secure connections to controlled assets, we have enhanced the Kademlia protocol and developed a Distributed Hash Table (DHT) technology.

Our hacking tool is highly effective during attack scanning, consisting of a large number of Internet nodes that dynamically update IDs and node tree structures at regular intervals. This approach allows each session to initiate requests from different nodes during the scanning process, thus avoiding IP blocking due to high-frequency scanning. Moreover, when connecting controlled assets back to the C2 server, nodes are randomly selected based on a user-defined hop count, effectively preventing penetration testers from being traced and significantly enhancing the stealthiness of the entire penetration testing process.

</details>

<details><summary><strong>SharpSCCM 2.0 - Abusing Microsoft's C2 Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Chris Thompson](https://img.shields.io/badge/Chris%20Thompson-informational) ![Diego Lomellini](https://img.shields.io/badge/Diego%20Lomellini-informational)

🔗 **Link:** [SharpSCCM 2.0 - Abusing Microsoft's C2 Framework](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/RESOURCES.md)  
📝 **Description:** SharpSCCM 2.0 - Abusing Microsoft's C2 Framework

SharpSCCM is a post-exploitation tool designed to leverage Microsoft Endpoint Configuration Manager (a.k.a. ConfigMgr, formerly SCCM) for credential gathering and lateral movement without requiring access to the SCCM administration console GUI (e.g., from a C2 agent).

The release of SharpSCCM 2.0 includes new functionality to execute arbitrary commands on groups of devices, coerce NTLM authentication from remote SCCM clients that belong to specific users, dump and decrypt additional credentials from an SCCM client or by requesting them from a management point, and triage of local client files for software distribution point locations.

This session will include demonstrations of multiple techniques that can be used to take over an SCCM site, dump credentials from an SCCM client, execute arbitrary commands on remote SCCM clients, and coerce NTLM authentication from remote SCCM clients and servers.

Each demo will be followed by practical recommendations for mitigating these attacks and Q&A.

</details>

<details><summary><strong>Tool Aids in Monitoring Dynamic Scanning</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![pan hongwei](https://img.shields.io/badge/pan%20hongwei-informational) ![Weichao Zhou](https://img.shields.io/badge/Weichao%20Zhou-informational) ![Yue Zhuo](https://img.shields.io/badge/Yue%20Zhuo-informational)

🔗 **Link:** Not Available  
📝 **Description:** Antivirus software, as one of the important tools to protect computer security, its detection technology is also constantly developing. At the same time, penetration testing and malicious attacks have become more difficult. The core principle of our newly developed network security tool is to load the security software to be used into memory and relocate all import function tables (IAT) to a middle code area, so that it can continue to run without being killed. When each external function is referenced, it will jump to the middle stub function and retain the call information. If our security tool is killed by antivirus software, we can easily find the detection point of antivirus software based on the call information. Our security tool can detect its scanning rules in real time while antivirus software is running, so as to help you understand the behavior and rules of antivirus software. Our tool can detect antivirus software without disrupting its normal work, so as to help you better understand the behavior and rules of antivirus software.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Risky Business: Hands-on AI Payload Analysis</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Hyrum Anderson](https://img.shields.io/badge/Hyrum%20Anderson-informational) ![Sagar Samtani](https://img.shields.io/badge/Sagar%20Samtani-informational) ![Christina Liaghati](https://img.shields.io/badge/Christina%20Liaghati-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Hands-on RF Hacking: Your Table is (always) Ready</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Paul Clark](https://img.shields.io/badge/Paul%20Clark-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Practical IoT Hacking: Introduction to Multi-Band Hacking with the CatSniffer</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Paulino Calderon](https://img.shields.io/badge/Paulino%20Calderon-informational) ![Eduardo Contreras](https://img.shields.io/badge/Eduardo%20Contreras-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Akto - Open Source API Security Tool</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ankush Jain](https://img.shields.io/badge/Ankush%20Jain-informational) ![Ankita Gupta](https://img.shields.io/badge/Ankita%20Gupta-informational)

🔗 **Link:** Not Available  
📝 **Description:** We released Open source Akto in Feb '23 & we have 310 stars on Github. This tool is mainly focuses on solving the problems below:
1. Tough api inventory for both testers, compliance and developers
2. Testing with complex chained apis - Multi step authentication, refresh/access token etc.
3. Automated testing of APIs - Both OWASP Top 10 and some business logic tests

Our tool Akto focuses on solving the above problems by providing:
1. Provide automated API inventory -
a)Automated - Akto can populate inventory automatically from traffic sources like Burp Proxy, Postman or even Chrome HAR files.
b) All formats - Akto also covers different formats of APIs such as JSON, GraphQL, gRPC, JSONP, forms.
2. Inspects traffic & provides alerts on suspicious apis -
a) Sensitive data - Akto comes with an in-built library for sensitive data patterns. Akto can tell which APIs are sharing sensitive data such as SSN, email, Phone number etc. Users can add their own patterns too.
b) Alerts - Users can set up daily alerts using Slack and Webhooks to get alerts about new sensitive data/APIs found
3. Automated API testing which covers OWASP Top 10 & some business logic testing
a) OWASP Coverage - Akto has 130+ tests to cover for OWASP Top 10
b) Business logic tests - Akto also supports business logic tests such as BOLA, Broken Function Level Authorization, Broken Authentication etc.
c) Add your own - Users can also add their own tests.

This tool will be very interesting for:
a) Bugbounty Hunters - has a blackbox feature where complex apis can be uploaded from Burp history & can be useful for chained requests.
b) Pentesters & testing teams in appsec - getting accurate api collection is complex & time consuming. Provides a one stop solution for getting the inventory. Tests like BOLA and BFLA will be especially interesting for them.
c) Blue teamers/infra security - Getting an automated API inventory and getting alerts for any new sensitive APIs. They can also get a view of all sensitive PII data being shared across all their services and across all their APIs. They can check unauthenticated APIs, download the swagger file and use it in other security apps too.

</details>

<details><summary><strong>AppSecLens: AI-Driven Adaptive Application Risk Ranking</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Melih Tas](https://img.shields.io/badge/Melih%20Tas-informational) ![Neslisah Topcu](https://img.shields.io/badge/Neslisah%20Topcu-informational)

🔗 **Link:** Not Available  
📝 **Description:** AppSecLens is an innovative web application security tool, specifically designed to assist organizations in proactively managing their attack surface, identifying vulnerabilities, and prioritizing remediation efforts with a focus on Application Risk Ranking.

Inspired by VulnHero, AppSecLens identifies related web applications using domain knowledge, conducts context-based discoveries, and employs AI-powered algorithms to assign application risk rankings. The tool evaluates web applications based on criteria such as potential business risks, presence of PII/NPI/HPI data, authentication structure, underlying technology stack, patch cadence, and security posture. AppSecLens's AI-driven algorithm assigns automatic tags and labels accordingly, enabling efficient risk prioritization.

By integrating with third-party APIs and threat intelligence databases, AppSecLens remains up-to-date with the latest vulnerabilities and exploits. The tool also supports seamless collaboration with other security tools and systems, facilitating coordinated remediation efforts. Its customizable dashboards and reporting options empower users to monitor and manage risks effectively, ensuring a more robust and secure web application environment.

</details>

<details><summary><strong>BlueMap - An Interactive Tool for Azure Exploitation</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Maor Tal](https://img.shields.io/badge/Maor%20Tal-informational)

🔗 **Link:** [BlueMap - An Interactive Tool for Azure Exploitation](https://github.com/SikretaLabs/BlueMap)  
📝 **Description:** As demonstrated in BlackHat UK & Asia - BlueMap helps cloud red teamers and security researchers identify IAM misconfigurations, information gathering, and abuse of managed identities in interactive mode without ANY third-party dependencies. No more painful installations on the customer's environment, and No more need to custom the script to avoid SIEM detection!

The tool leaves minimum traffic in the network logs to help during red team engagements from on-prem to the cloud. Developed in Python and implemented all Azure integrations from scratch with zero dependencies on Powershell stuff. The idea behind the tool is to let security researchers and red team members have the ability to focus on more Opsec rather than DevOps stuff.

</details>

<details><summary><strong>Cloud AuthZ Trainer (CAZT)</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Rodney Beede](https://img.shields.io/badge/Rodney%20Beede-informational)

🔗 **Link:** [Cloud AuthZ Trainer (CAZT)](https://github.com/Coalfire-Research/cazt)  
📝 **Description:** CAZT is a simulator of cloud-provider responsible REST APIs. It includes a lab manual for getting hands-on practice with how to attack authorization vulnerabilities in a cloud API.

It is different from other vulnerable cloud practice environments because it focuses on the cloud-provider shared responsibility instead of the customer. This enables pen testers to gain experience with testing the cloud vendor itself as well as an understanding of what a vulnerable cloud service will look like.

</details>

<details><summary><strong>Emulating Any HTTP Software as a Honeypot with HASH: A Deceptive Defense Against Cyberattacks</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Eslam Salem](https://img.shields.io/badge/Eslam%20Salem-informational)

🔗 **Link:** [Emulating Any HTTP Software as a Honeypot with HASH: A Deceptive Defense Against Cyberattacks](https://github.com/mmjang/AnkiIRExtension/blob/master/hwd.json)  
📝 **Description:** HASH (HTTP Agnostic Software Honeypot), an open-source framework for creating and launching low interaction honeypots. With simple YAML configuration files HASH can simulate any HTTP based software with built in randomization capabilities to avoid being identified.

</details>

<details><summary><strong>Nekuda: IDN-Squatting Detector</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Gal Bitensky](https://img.shields.io/badge/Gal%20Bitensky-informational) ![Adi Pick](https://img.shields.io/badge/Adi%20Pick-informational)

🔗 **Link:** [Nekuda: IDN-Squatting Detector](https://github.com/G4LB1T/Nekuda)  
📝 **Description:** Put yourself in the shoes of a fraudster, you are trying to create a phishing website. Why inserting detectable unicode characters into a mostly-ASCII domain when you can register an entire domain in unicode? This is available when one uses a lesser-known feature called Internationalized Domain Name Top Level Domains (IDN TLD). Consider registering domains like google.com's lookalike in Hebrew - גוגל.קום, アマゾン.コム in Japanese instead of amazon.com or 微软.公司 which is the Chinese equivalent of microsoft.com.

Nekuda (dot in Hebrew) assists blue teamers to detect such domains. Its input is a string (e.g. the blue teamer's employer Brand name) and it emits over 150 potential IDN TLD domains and its registration status. It covers a potential gap in proactive phishing detection and prevention strategies and can be easily integrated into existing open-source tools like dnstwist.

</details>

<details><summary><strong>route-detect: Find Authentication and Authorization Security Bugs in Web Application Routes</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Matt Schwager](https://img.shields.io/badge/Matt%20Schwager-informational)

🔗 **Link:** [route-detect: Find Authentication and Authorization Security Bugs in Web Application Routes](https://github.com/mschwager)  
📝 **Description:** This demo introduces route-detect. route-detect is a command-line tool that seeks to aid security researchers and engineers in finding authentication (authn) and authorization (authz) security bugs in web application routes. These bugs are some of the most common security issues found today. The following industry standard resources highlight the severity of the issue:

- 2021 OWASP Top 10 #1 - Broken Access Control
- 2021 OWASP Top 10 #7 - Identification and Authentication Failures
- 2019 OWASP API Top 10 #2 - Broken User Authentication
- 2019 OWASP API Top 10 #5 - Broken Function Level Authorization

Of course, not all authn or authz bugs occur in web application routes, but route-detect seeks to confront this pervasive class of bugs.

</details>

<details><summary><strong>SucoshScanny</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Mustafa Bilgici](https://img.shields.io/badge/Mustafa%20Bilgici-informational) ![Recep Tibet Öğünç](https://img.shields.io/badge/Recep%20Tibet%20Öğünç-informational)

🔗 **Link:** Not Available  
📝 **Description:** SucoshScan is a automated open source SAST(Static Application Security Testing) framework. It's can detect a lot of vulnerability(RCE,SSTI,Insecure Deserilisation,SSRF,SQLI,CSRF etc.) in given source code.For now, only the detection modules of python(flask,django) and nodejs(express js.) languages are finished. In the future, specific detection functions will be written for php (Laravel, Codeigniter), .NET, Go languages.

</details>

<details><summary><strong>Swimming with the (Data)Flow – Analyzing & Visualizing Web Application Data Flows for Enhanced Penetration Testing</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Florian Haag](https://img.shields.io/badge/Florian%20Haag-informational) ![Henry Wischerath](https://img.shields.io/badge/Henry%20Wischerath-informational) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational)

🔗 **Link:** Not Available  
📝 **Description:** Imagine pentesting a large web application with hundreds of pages and forms, as well as user roles and tenants. You discover that your chosen username is reflected in many locations inside the application, but you don't have a detailed overview. You want to test whether the chosen username is handled properly or allows for injection attacks, such as Cross-Site Scripting or Server-Site Template Injection. Now you face the challenge of finding all locations where your payloads appear when injecting into the username. In large applications, you'll likely miss some, potentially leaving vulnerabilities undetected.

This is where FlowMate comes into play, our novel tool to detect data flows in applications for enhanced vulnerability assessments. FlowMate consists of two components: A BurpSuite plugin and a data flow graph based on Neo4j. It records inputs to the application as you go through the pages. In contrast to existing tools that require server-side access, FlowMate works from a black-box perspective by observing HTTP request and response pairs. Thereby FlowMate records all input parameters and locations as well as user-supplied values. In parallel, all HTTP responses from the server are matched against the central store of already identified parameter values to find occurrences of known input parameters. This results in a data graph, mapping inputs to outputs simply while using the application.

Understanding the data flow results in a significant improvement of test coverage in web app pentests, as all input and output occurrences of parameters can be systematically tested for vulnerabilities. More precisely, analysts can use FlowMate in the following ways: First, for a given input parameter, FlowMate shows all output locations, thus enabling verification of output filtering and encoding, even across role, tenant, and session boundaries. Second, for a given form, FlowMate visualizes all parameters and their respective output locations across the application.

</details>

<details><summary><strong>vAPI: Vulnerable Adversely Programmed Interface</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tushar Kulkarni](https://img.shields.io/badge/Tushar%20Kulkarni-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Analyzing SAP Communication Security: Introducing sncscan</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Nicolas Schickert](https://img.shields.io/badge/Nicolas%20Schickert-informational) ![Jonas Wamsler](https://img.shields.io/badge/Jonas%20Wamsler-informational) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational)

🔗 **Link:** Not Available  
📝 **Description:** SAP systems are used around the world to handle crucial business processes and highly confidential data such as financial details or information regarding a company's staff. To ensure confidentiality and integrity, sensitive data, and especially access credentials, must only be transmitted over encrypted communication channels. Transport layer encryption for SAP systems is provided by the Secure Network Communications (SNC) protocol. Currently, the configuration of the SAP SNC protocol (such as the Quality of Protection parameter or the installed CryptoLib) can only be audited with authenticated access to the SAP system or by manually connecting to the system through the SAP GUI. These approaches have additional requirements and are impractical for assessing the security of a larger number of systems.

To address the beforementioned issues, we developed 'sncscan', an SNC scanner, that works without authentication and similar to the various tools that are available to analyze the security of services that use SSL/TLS. To achieve this, 'sncscan' starts SNC handshakes with varying encryption parameters to the tested service and analyzes the returned error messages and responses. This is especially useful in context of professional penetration tests and enables us to identify configuration weaknesses and provide actionable recommendations on improving the transport security in SAP environments.

'sncscan' benefits from the tools and research of the `pysap` project and will be released as Open-Source tool in the OWASP CBAS-SAP project. It aims to enable security researchers, professional penetration testers and SAP basis administrators to verify the correct use of the SNC protocol.

Currently 'sncscan' can analyze the SNC configuration of the SAP Router protocol. The next steps are to implement similar functionality for the protocols DIAG and RFC to increase the coverage of SAP services.

</details>

<details><summary><strong>Bugsy - Automated Vulnerability Remediation CLI</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Eitan Worcel](https://img.shields.io/badge/Eitan%20Worcel-informational) ![Jonathan Afek](https://img.shields.io/badge/Jonathan%20Afek-informational) ![Kirill Efimov](https://img.shields.io/badge/Kirill%20Efimov-informational)

🔗 **Link:** Not Available  
📝 **Description:** Bugsy is a command-line interface (CLI) tool that provides automatic security vulnerability remediation for your code. It is a community edition version of Mobb, the first vendor-agnostic automatic security vulnerability remediation tool. Bugsy is designed to help developers easily identify and fix security vulnerabilities in their code.

When pointed at an open-source repo, Bugsy will automatically scan the repo using Snyk Code and produce fixes the developer can easily review and commit.

</details>

<details><summary><strong>Build Inspector Open Source</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Jeremy Banker](https://img.shields.io/badge/Jeremy%20Banker-informational)

🔗 **Link:** [Build Inspector Open Source](https://github.com/vmware-archive/build-inspector)  
📝 **Description:** Build Inspector provides processing of plain-text CI/CD build and deployment logs with an eye towards identifying consumed and produced dependencies, along with identifying actions that introduce additional risk into the process. Quickly identify changes from one pipeline run to the next, and home in on spots where developers have added unnecessary risk or are performing actions that could be opportunities for a supply chain compromise.

</details>

<details><summary><strong>CodeTotal: Shift Left Just Became Easier</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Eyal Paz](https://img.shields.io/badge/Eyal%20Paz-informational) ![Nicolas Vuillamy](https://img.shields.io/badge/Nicolas%20Vuillamy-informational)

🔗 **Link:** Not Available  
📝 **Description:** Looking for a powerful and easy-to-use open-source scanning tool? CodeTotal is your solution! CodeTotal is an online scanning tool aggregates multiple open-source scanning tools, providing free and lightning-fast code scanning.

But CodeTotal offers much more than just speed and convenience. Our unique tool also aggregates the data from these scans, enabling users to identify any security issues that their current scanning software may have missed. With CodeTotal, you can even verify alerts suspected to be possible false positives, getting a valuable second opinion that can help you stay ahead of any potential threats.

Tired of maintaining multiple tool environments for each repository? CodeTotal offers a simple and streamlined solution. No more wasting time setting up and maintaining 10 to 20 tool environments - CodeTotal takes care of everything for you. Our revolutionary tool allows developers to independently scan their code for security issues in minutes, freeing up valuable resources and avoiding the need for involvement or approval from R&D and DevOps.

But that's not all. CodeTotal also produces an SBOM, giving developers a detailed view of their code dependencies and ensuring that any licensing issues are immediately flagged. With CodeTotal, you can use open-source libraries confidently and with peace of mind.

</details>

<details><summary><strong>Daksh SCRA (Source Code Review Assist Tool)</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Debasis Mohanty](https://img.shields.io/badge/Debasis%20Mohanty-informational)

🔗 **Link:** [Daksh SCRA (Source Code Review Assist Tool)](https://github.com/coffeeandsecurity/DakshSCRA)  
📝 **Description:** Daksh SCRA is an open source tool that assists with manual source code review by providing helpful information to the code reviewer. This tool differs from traditional code review tools because it aims to help reviewers collect various details about the code base and identify areas of interest to review and confirm potential vulnerabilities. Even if code reviewers use automated code review tools, there are still many manual tasks they must perform to confirm findings and ensure precision in the code review process.

Although there are numerous automated code review tools available, none of them can perform a reconnaissance of the code base and provide code reviewers with useful insights. Typically, code reviewers must search for relevant information to confirm findings or ensure precision. Daksh SCRA offers valuable information such as technology and platform usage, functionalities, use cases, vulnerable patterns, and libraries used, among other data.

While most code review tools search for vulnerable patterns, they often report a high percentage of false positives. Daksh SCRA, on the other hand, is designed to be a reconnaissance tool that provides code reviewers with maximum insights about the target code base to assist with precise code review. Although Daksh SCRA is in its infancy stage, it is still a usable tool that supports a wide range of languages and platforms, and new features will be added in future releases.

</details>

<details><summary><strong>SCodeScanner - An Open-Source Source-Code Scanner</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Utkarsh Agrawal](https://img.shields.io/badge/Utkarsh%20Agrawal-informational)

🔗 **Link:** [SCodeScanner - An Open-Source Source-Code Scanner](https://github.com/agrawalsmart7/scodescanner)  
📝 **Description:** SCodeScanner is a powerful tool for identifying vulnerabilities in source-code. It is designed to be easy to use and provides a range of features to help users quickly and accurately identify vulnerabilities with fewer false positives.

Some key features of SCodeScanner include:

- Support multiple languages: SCodeScanner is capable of scanning source code written in multiple languages such as JAVA, PHP and YAML. The most commonly used languages in web development.

- Relatively Less false positives: SCodeScanner includes flags that help to eliminate false positives and only report on vulnerabilities that are mostly confirmed to exist.

- Custom rules: SCodeScanner works with semgrep and allows users to create their own rules to scan for advanced patterns.

- Ability to track user input variables: SCodeScanner can identify instances where user input variables are defined in one file but used insecurely in another file for better coverage.

- Fast scanning: SCodeScanner's rules are designed to check for multiple vulnerabilities at once, which results in a faster scanning process.

- Integration: SCodeScanner can integrate with CI/CD pipelines and also pass results to bug-tracking services such as Jira and Slack, allowing users to easily share the results of their scans with their team.

- Scan mutltiple ways: It automatically download all git repo mentioned inside a txt file and start scan. Not only this but also support git, folder, file scans aswell.

Proof of results, SCodeScanner has already found 5 vulnerabilities in multiple Wordpress plugins and has been awarded following CVEs:

CVE-2022-1604
CVE-2022-1465
CVE-2022-1474
CVE-2022-1527
CVE-2022-1532

Overall, SCodeScanner is a valuable tool for any developer or security professional looking to identify vulnerabilities in their source-code before it is published in production. Its fast scanning, less false positives, and CI/CD pipeline integrations as well as bug-tracking services, make it a powerful tool for ensuring the security of your code.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>AntiSquat - An AI-Powered Phishing Domain Finder</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Umair Nehri](https://img.shields.io/badge/Umair%20Nehri-informational) ![Owais Shaikh](https://img.shields.io/badge/Owais%20Shaikh-informational)

🔗 **Link:** Not Available  
📝 **Description:** If you host a domain on the internet representing an individual or organization, chances are that there exists a phishing domain designed specially to attack the users of your product or website.
AntiSquat is an AI-Powered typo-squatting domain finder that checks for phishing domains based on misspellings. It has a flagging system that leverages a combination of Machine Learning Models as well as various other checks such as web page similarity matching. These are performed in real-time on the target domain, thus making sure that the results are impactful.

</details>

<details><summary><strong>ARCTIC - Automated Remediation for Correlation Threat Intelligence Collections</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ankit Anurag](https://img.shields.io/badge/Ankit%20Anurag-informational) ![Ashwath K](https://img.shields.io/badge/Ashwath%20K-informational) ![Manikandan Rajappan](https://img.shields.io/badge/Manikandan%20Rajappan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Arctic builds on the open-source MISP platform to enable threat intelligence based correlation of indicators of compromise using multiple sources like internally collected intelligence, intelligence filtered through free and paid feeds, cloud feeds from Guardduty and Route53,etc. and gives a relevance score to each IOC (Indicator of Compromise) which is specific to the organisation.

It uses MISP to further enrich the IOC and maps it with the MITRE TTPs which can be used to identify the suspected APTs involved in the attack

</details>

<details><summary><strong>CASPR - Code Trust Auditing Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ajit Hatti](https://img.shields.io/badge/Ajit%20Hatti-informational)

🔗 **Link:** Not Available  
📝 **Description:** CASPR is known for addressing the Supply Chain Attacks by Left Shifting the code signing process.
CASPR provides simple scripts and services architecture to ensure all code changes in an organisation are signed by trusted keys. What matters is where these keys are residing. Storing signing keys on a user's device has a certain degree of risk when the device is compromised.

In the latest release of CASPR, we are enabling developers to sign code commits from the keys stored on the phone.

CASPR makes the auditing and accountability of code-changes easier and cryptographically verifiable, leaving no scope for malicious actors to sneak in untrusted code at any point in the Software Development Life Cycle.

</details>

<details><summary><strong>CQData: Data Extraction & Forensic Toolkit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Paula Januszkiewicz](https://img.shields.io/badge/Paula%20Januszkiewicz-informational) ![Mike Jankowski-Lorek](https://img.shields.io/badge/Mike%20Jankowski-Lorek-informational)

🔗 **Link:** Not Available  
📝 **Description:** CQData Toolkit enables you to perform extraction of data that can be extremely useful during the investigation and incident. One of the most important things to learn during the incident is to learn the identity connected with the attack and also become familiar with hacker's actions through the detailed process tracking. CQData can extract information from the Automatic Destinations, generate a timeline, convert Automatic Destination into useful lists of processes, recover files, extract information from the configuration, calculate the vector of the attack based on the process related information and search across other affected computers, decode encrypted users' data, find encrypted data on the computer and display its characteristic, search for confirmation that logs were not manipulated with etc. It is a toolkit that authors use during the incident investigation. Toolkit was created with one purpose, to address the gaps in the evidence analysis and data collection tools. CQData also leverages the reverse engineering research done in the DPAPI area and our recent 1-year research in the Automatic Destinations area.

</details>

<details><summary><strong>Defending software development ecosystems with Safe Package</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mike Doyle](https://img.shields.io/badge/Mike%20Doyle-informational)

🔗 **Link:** [Defending software development ecosystems with Safe Package](https://github.com/lorin/resilience-engineering)  
📝 **Description:** With typosquatting, with account takeover, and with dependency hijacking attackers are using malicious packages to target our deployment pipelines. They mimic popular packages like Material Tailwind, hijack popular dependencies like event-stream, and compromise privileged accounts. This talk explains these classes of attack with examples and introduces safe-package, an open-source security wrapper for all kinds of package managers that neutralizes these attacks.

</details>

<details><summary><strong>Dissect: The Open-Source Framework for Large-Scale Host Investigations</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Stefan de Reuver](https://img.shields.io/badge/Stefan%20de%20Reuver-informational) ![Erik Schamper](https://img.shields.io/badge/Erik%20Schamper-informational)

🔗 **Link:** Not Available  
📝 **Description:** Dissect is an incident response framework build from various parsers and implementations of file formats. Tying this all together, Dissect allows you to work with tools named target-query and target-shell to quickly gain access to forensic artefacts, such as Runkeys, Prefetch files, and Windows Event Logs, just to name a few!

And the best thing: all in a singular way, regardless of underlying container (E01, VMDK, QCoW), filesystem (NTFS, ExtFS, FFS), or Operating System (Windows, Linux, ESXi) structure / combination. You no longer have to bother extracting files from your forensic container, mount them (in case of VMDKs and such), retrieve the MFT, and parse it using a separate tool, to finally create a timeline to analyse. This is all handled under the hood by Dissect in a user-friendly manner.

This way you spend less time with the boring processing steps and have more time doing actual analysis or research!

</details>

<details><summary><strong>eBPFShield: Unleashing the Power of eBPF for OS Kernel Exploitation and Security.</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sagar Bhure](https://img.shields.io/badge/Sagar%20Bhure-informational)

🔗 **Link:** Not Available  
📝 **Description:** Are you looking for an advanced tool that can help you detect and prevent sophisticated exploits on your systems? Look no further than eBPFShield. Let's take a technical look at some of the capabilities of this powerful technology:

DNS monitoring feature is particularly useful for detecting DNS tunneling, a technique used by attackers to bypass network security measures. By monitoring DNS queries, eBPFShield can help detect and block these attempts before any damage is done.

IP-Intelligence feature allows you to monitor outbound connections and check them against threat intelligence lists. This helps prevent command-and-control (C2) communications, a common tactic used by attackers to control compromised systems. By blocking outbound connections to known C2 destinations, eBPFShield can prevent attackers from exfiltrating sensitive data or delivering additional payloads to your system.

eBPFShield Machine Learning feature, you can develop and run advanced machine learning algorithms entirely in eBPF. We demonstrate a flow-based network intrusion detection system(IDS) based on machine learning entirely in eBPF. Our solution uses a decision tree and decides for each packet whether it is malicious or not, considering the entire previous context of the network flow.

eBPFShield Forensics helps address Linux security issues by analyzing system calls and kernel events to detect possible code injection into another process. It can also help identify malicious files and processes that may have been introduced to your system, allowing you to remediate any security issues quickly and effectively.

During the workshop, we'll delve deeper into these features and demonstrate how eBPFShield can help you protect your systems against even the most advanced threats.

</details>

<details><summary><strong>Effective Alert Triage and Email Analysis with Security Onion and Sublime Platform</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Josh Kamdjou](https://img.shields.io/badge/Josh%20Kamdjou-informational) ![Wes Lambert](https://img.shields.io/badge/Wes%20Lambert-informational)

🔗 **Link:** Not Available  
📝 **Description:** In this workshop, we will explore the integration of two cutting-edge free and open platforms: Security Onion, a versatile solution for threat hunting, enterprise security monitoring, and log management; and Sublime Platform, an innovative open email security platform designed to prevent email attacks such as BEC, malware, and credential phishing. Sublime Platform's unique domain-specific language (DSL) enables detection-as-code, allowing for highly customizable email security detection.

Attendees will learn how to:

1. Set up and configure the integration between Security Onion and Sublime Platform, leveraging the combined strength of these tools to detect, prevent, triage, and enrich email threats.
2. Utilize Sublime Platform's DSL for detection-as-code, crafting tailored rules and policies to identify and prevent a wide range of email threats.
3. Effectively triage Sublime email alerts within Security Onion, streamlining incident response and reducing the time needed to identify and remediate threats.
4. Pivot to Sublime for in-depth investigation and analysis of suspicious emails, extracting valuable context and indicators to inform security decisions.
5. Enrich and correlate Sublime alerts with other data sources in Security Onion, such as Zeek HTTP/DNS/TLS records, Suricata alerts, and full PCAP to answer questions with network metadata such as: Did the user click on the link? Has anyone ever visited this domain or link before? And more.

By combining Security Onion's robust capabilities with Sublime Platform's innovative approach to email security, participants will gain hands-on experience in creating a comprehensive defense against email-based attacks.

Equip yourself with the knowledge and tools needed to combat the evolving landscape of email threats by attending this workshop, and take advantage of these powerful, free solutions to bolster your organization's defenses.

</details>

<details><summary><strong>Find Blind Spots in Your Security with Paladin Cloud</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![John Richards](https://img.shields.io/badge/John%20Richards-informational)

🔗 **Link:** [Find Blind Spots in Your Security with Paladin Cloud](https://github.com/kagisearch/smallweb/blob/main/smallweb.txt)  
📝 **Description:** Paladin Cloud is an extensible, Security-as-Code (SaC) platform designed to help developers and security teams reduce risks in their cloud environments. It functions as a policy management plane across multi-cloud and enterprise systems, protecting applications and data. The platform contains best practice security policies and performs continuous monitoring of cloud assets, prioritizing security violations based on severity levels to help you focus on the events that matter..

Its resource discovery capability creates an asset inventory, then evaluates security policies against each asset. Powerful visualization enables developers to quickly identify and remediate violations on a risk-adjusted basis. An auto-fix framework provides the ability to automatically respond to policy violations by taking predefined actions.

Paladin Cloud is more than a tool to manage cloud misconfiguration. It's a holistic cloud security platform that can be used for continuous monitoring and reporting across any domain.

</details>

<details><summary><strong>Fortifying GCP Security: Open Source Just-In-Time access and Audit Log Monitoring</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dustin Decker](https://img.shields.io/badge/Dustin%20Decker-informational)

🔗 **Link:** Not Available  
📝 **Description:** Google does not make cloud security easy. The tool we're open sourcing doesn't make it easy either, but it makes it about 10% less painful than the existential dread the default GCP policies have infected on your organization.

In this talk, we'll guide you through setting up an audit log sink and evaluating events against Open Policy Agent (OPA) Rego policies. We'll discuss the included MITRE ATT&CK tactics policies and demonstrate how to create new custom policies using the OPA engine. We'll also cover how to make least privilege access control work for your organization with Just-In-Time access provisioning.

Our presentation aims to empower GCP users with the knowledge and tools necessary for effective large-scale monitoring of their environments' security and actions. We'll share some experience and insights on the current state of controls within GCP, and how infrastructure providers can enable more powerful tooling.

By the end of this talk, attendees will have gained practical knowledge in leveraging open source software to strengthen their GCP security posture. Don't miss this opportunity to stay ahead in the world of cloud security and enhance the protection of your GCP environment.

</details>

<details><summary><strong>Grove: An Open-Source Log Collection Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Peter Adkins](https://img.shields.io/badge/Peter%20Adkins-informational) ![Melissa Hardware](https://img.shields.io/badge/Melissa%20Hardware-informational)

🔗 **Link:** [Grove: An Open-Source Log Collection Framework](https://gist.github.com/LisaDawn/7003846)  
📝 **Description:** Grove is a log collection framework designed to support a unified way of collecting, storing, and routing logs from Software as a Service (SaaS) providers which do not natively support log streaming.

This is performed by periodically collecting logs from configured sources, and writing them to arbitrary destinations.

Grove enables teams to collect security related events from their vendors in a reliable and consistent way, while allowing this data to be stored and analyzed with existing tools.

</details>

<details><summary><strong>Identity Threat Hunting with Kestrel</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Paul Coccoli](https://img.shields.io/badge/Paul%20Coccoli-informational) ![Sulakshan Vajipayajula](https://img.shields.io/badge/Sulakshan%20Vajipayajula-informational) ![Ritesh Kumar](https://img.shields.io/badge/Ritesh%20Kumar-informational)

🔗 **Link:** Not Available  
📝 **Description:** Attacks on Identity and access systems are starting points for major data breaches achieved through privilege escalation and lateral movement. Identity-threat hunting reduces time needed to detect traces of an attacker so that the consequences of a breach can be controlled. Identity-threat hunting involves data collection from identity providers, normalization and application of analytics while navigating the rabbit holes of authentication flows across the systems. Kestrel is a threat hunting language that accelerates cyber threat hunting by providing a layer of abstraction to build reusable, composable, and shareable "hunt-flows", providing a great platform for identity-threat hunting.


This arsenal session will showcase identity-threat hunting built on top of Kestrel. Starting with federated data retrieval from IAM systems using the OASIS Structured Threat Information eXpression (STIX) standard via OCA's STIX-shifter and lifting the results into an entity-relational data model. Then we will showcase analytic hunt steps besides data retrieval steps, walking you through the use case to hunt malicious activity in login data.


To showcase the capability of kestrel and identity threat hunting, we use event data gathered from IBM Security Verify Identity and access management (IAM). The queries and analysis follow OASIS STIX standards. Our hunt book will work with any Identity provider that has a stix-shifter connector.


The showcase uses a search for the IP address with multiple failed logins and later drills down and correlates with threat intel of known malicious activity for those IP addresses. The demo will also showcase the geographical distribution of those suspicious IP addresses, a list of applications which are accessed by these compromised IP addresses and accounts details of the logged-in user by IP address.


Making it ready to try by the audience, we will demonstrate live hunts in Jupyter Notebooks. At the end of the session, we will introduce the kestrel-huntbook repo for people to reuse existing huntbooks and share their hunting knowledge with their colleagues and other hunters in the community

</details>

<details><summary><strong>MELEE: A Tool to Identify Ransomware Infections in MySQL Deployments</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Aditya K Sood](https://img.shields.io/badge/Aditya%20K%20Sood-informational)

🔗 **Link:** [MELEE: A Tool to Identify Ransomware Infections in MySQL Deployments](https://github.com/adityaks/melee)  
📝 **Description:** Attackers are abusing MySQL instances for conducting nefarious operations on the Internet. The cybercriminals are targeting exposed MySQL instances and triggering infections at scale to exfiltrate data, destruct data, and extort money via ransom. For example one of the significant threats MySQL deployments face is ransomware. We have authored a tool named "MELEE" to detect potential infections in MySQL instances. The tool allows security researchers, penetration testers, and threat intelligence experts to detect compromised and infected MySQL instances running malicious code. The tool also enables you to conduct efficient research in the field of malware targeting cloud databases.

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

<details><summary><strong>Noriben: Quick and Easy Automated Malware Analysis Sandbox</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Brian Baskin](https://img.shields.io/badge/Brian%20Baskin-informational)

🔗 **Link:** [Noriben: Quick and Easy Automated Malware Analysis Sandbox](https://github.com/Rurik/Noriben)  
📝 **Description:** Noriben is a Python-based tool that works Sysinternals Procmon to automatically collect, analyze, and report on runtime indicators of malware. It allows for the collection and analysis of unusual behavior on a system while attacks are being performed. The use of Noriben allows for manual analysis of malware while collecting its behavior, such as the use of command line arguments or manual debugging. With a host-based component, it can even run and collect info from thousands of malware samples automatically.

</details>

<details><summary><strong>RuleCraftLab - A Detection Rule Development Platform</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Numan Mete Ozaltin](https://img.shields.io/badge/Numan%20Mete%20Ozaltin-informational) ![Eren Karabacak](https://img.shields.io/badge/Eren%20Karabacak-informational)

🔗 **Link:** Not Available  
📝 **Description:** "RuleCraftLab" is an open-source platform that provides SOC engineers, security researchers, and detection engineers with a robust environment for developing and testing detection content using real threat logs from actual systems. As the landscape of threats continues to evolve and diversify, there is a growing need for accurate and effective rules to detect and mitigate these threats. However, traditional rule development methods often lack real-world context, relying on blog posts or public rules without thorough testing. "RuleCraftLab" addresses these challenges by offering a dedicated playground where users can develop and test their rules in a realistic environment to streamline the rule development process.

</details>

<details><summary><strong>SinCity: Build Your Dream Lab Environment</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Matan Hart](https://img.shields.io/badge/Matan%20Hart-informational) ![Shay Yaish](https://img.shields.io/badge/Shay%20Yaish-informational)

🔗 **Link:** Not Available  
📝 **Description:** Security practitioners are still wasting time today building and maintaining lab environments through "manual" and cumbersome processes. In doing so, they are missing out on the potential DevOps methodologies and Infrastructure-as-Code (IaC) practices offer. This daunting work must end now.

This arsenal demonstration will introduce SinCity, a GPT-powered, MITRE ATT&CK-based tool which automates the provisioning and management of an IT environment in a conversational way. SinCity reduces the efforts needed to build a full-blown lab environment from months to minutes by providing an abstraction layer for customizing network topologies, crafting attack scenarios, and tuning security controls.

Attendees who frequently sandbox malware, analyze TTPs, or evaluate detection capabilities - this arsenal will save you precious time.

</details>

<details><summary><strong>SSHook: A Lightweight Syscall Hooking Tool for Uncovering Hidden Malicious Instructions</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Zixi Liao](https://img.shields.io/badge/Zixi%20Liao-informational) ![Bin Ma](https://img.shields.io/badge/Bin%20Ma-informational)

🔗 **Link:** Not Available  
📝 **Description:** Most Android hook ways aim at watching APIs for Java or Native code. However, some malicious apps try to escape hooking and access sensitive data using syscall directly, so it is crucial in order to uncover hidden code that some malicious apps use to bypass standard hooking techniques and access sensitive data directly through system calls. We have implemented a syscall hooking tool based on Seccomp-BPF named SSHook, which gives better balance between performance and compatibility.

Seccomp-BPF was introduced into Linux kenel to filter syscalls and their arguments, we transform this security feature into a syscall hook framework which support devices range from Android 8.1 to Android 13. Our tool SSHook combined Seccomp-BPF with throwing an exception to catch syscall, and resuming instructions for normal execution by preparing additional threads earlier, which avoids frequent interruptions and possible risks like deadlocks, suspensions, or crashes. For performance improvement, we have implemented a flag that determines whether to resume execution using either the inactive parameter or the higher 4 bytes of an integer type, but the program can still run normally without any impact. Besides, SSHook is a lightweight framework but performs efficiently and robustly compared with other invasive or complicated solutions, which keep stable and reliable by standing on the shoulders of kernel features.

SSHook can help to identify suspicious behavior in malicious Apps which abuse syscall to steal privacy files or collect sensitive data like MAC, applist, which can be integrated into sandbox environment to conduct more complete dynamic analysis. Furthermore, SSHook allows us to replace syscall arguments and bypass hooking tools to evade detection, which is particularly useful in preventing the collection of device fingerprints and protecting user privacy against tracking.

</details>

<details><summary><strong>T3SF (Technical TableTop Exercises Simulation Framework)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Federico Pacheco](https://img.shields.io/badge/Federico%20Pacheco-informational) ![Joaquin Lanfranconi](https://img.shields.io/badge/Joaquin%20Lanfranconi-informational)

🔗 **Link:** Not Available  
📝 **Description:** T3SF is a framework that offers a modular structure for the orchestration of events from a master scenario events list (MSEL) together with a set of rules defined for each exercise and a configuration that allows defining the parameters of the correspondent platform. The main module performs the communication with the specific module (Discord, Slack, Telegram, WhatsApp, Teams, etc.) which allows the events to be presented in the input channels as injects for each platform. Also, the framework supports different use cases: single organization-multiple areas, multiple organization-single area, and multiple organization-multiple areas. It has been successfully tested in exercises with international companies, which allowed us to validate its commercial level.

Tabletop exercises have 2 approaches: traditional (scenarios with discussion) and modern (automatic events on a platform). The 1st platform was funded by the DHS (USA) with USD20 MM over 10 years. In 2021 we proposed a novel approach using free collaborative platforms, which allowed the development of a free and open source framework.

The original research paper presented and published at the IEEE ARGENCON 2022 academic congress, under the title "Cybersecurity Incident Response Simulation for Organizational and Classroom Learning." (preprint available at IEEE TechRxiv).

The tool itself was first presented and released in the most important cybersecurity conference in Spain (RootedCon 2022) and then updated and presented in the most important cybersecurity conference in Latin America (Ekoparty 2022, video available on YouTube). Then it was presented at FIRST Technical Colloquium Amsterdam 2023 (April) and BlackHat Asia Arsenal 2023.

This version is a major update that includes new features like a better GUI frontend for configuration and scenario setup, an automatic inject creation engine based on a given set of parameters (design decisions) and real time interactions based on ChatGPT predefined prompts.

</details>

<details><summary><strong>ThreatPatrol</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Viral Maniar](https://img.shields.io/badge/Viral%20Maniar-informational)

🔗 **Link:** [ThreatPatrol](https://github.com/Viralmaniar)  
📝 **Description:** ThreatPatrol is a powerful open-source SaaS tool that offers Blue Teams a wealth of information on potential threats, allowing them to gain situational awareness and perform threat hunting. The tool's flexibility is a significant advantage, as it can be hosted on the cloud or on an internal standalone machine, providing users with the convenience and customisation options they need.

ThreatPatrol offers a comprehensive database of over 160 threat actor groups, indicators of compromise (IOCs), tactics, techniques, and procedures (TTPs), and their modus operandi out of the box. This information is regularly updated to ensure that users have access to the latest information on potential threats, providing insights into emerging threats and enabling proactive measures to prevent cyber-attacks.

Cyber Defenders can add, update, or degrade TTPs and IOCs for their network and map them to the MITRE Framework, which can be visualised on the dashboard in graph form, and generate reports for sharing with executive members. By proactively collecting and analysing data on potential threats, cyber teams can improve their situational awareness, enabling them to take appropriate action to prevent or mitigate attacks.

ThreatPatrol also provides feeds from over 100+ different sources, allowing organisations to stay up-to-date with the latest attack methods and trends, adjust their security posture, and protect themselves better against cyber threats. With improved situational awareness, organisations can respond more quickly and effectively when incidents occur, making ThreatPatrol an essential tool for protecting valuable data and avoiding the devastating consequences of a cyber-attack.

</details>

<details><summary><strong>ThreatScraper: Automated Threat Intelligence Gathering and Analysis from VirusTotal</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Aaron Morath](https://img.shields.io/badge/Aaron%20Morath-informational) ![Scott Graham](https://img.shields.io/badge/Scott%20Graham-informational)

🔗 **Link:** Not Available  
📝 **Description:** The continuous growth of malware threats necessitates efficient and comprehensive tools for tracking malware detection and propagation. VirusTotal serves as a popular platform for aggregating malware information submitted by Anti-Virus (AV) software providers, which can be searched using parameters such as hashes (SHA-1, SHA-256, MD5), file names, and malicious web links. In order to enhance and automate the process of malware intelligence gathering, we introduce ThreatScraper, a Python-based tool that automates free API queries and rescanning tasks on VirusTotal.
ThreatScraper is designed to periodically request reports on specified files and save the results in a local database. It allows users to pull and aggregate malicious file reports from multiple AV vendors over time, providing insights into the adoption of malware detection across providers. Easily implemented from any Windows command line, ThreatScraper can rescan a file, pull a report, and then sleep until the next designated time identified by the user.
By leveraging ThreatScraper, developers can efficiently identify potentially malicious files, track when an AV provider has flagged a file as malicious and monitor the categorization of the file. The tool ultimately aids in enhancing threat intelligence gathering and response capabilities for users, developers, and enterprise entities.

</details>

<details><summary><strong>Vovk - Advanced Dynamic Yara Rule Generator</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Vishal Thakur](https://img.shields.io/badge/Vishal%20Thakur-informational)

🔗 **Link:** [Vovk - Advanced Dynamic Yara Rule Generator](https://github.com/ChanChiChoi/tiny-crawler/blob/master/paperMeta4arxiv_byArchive/arxiv-cs-2009.txt)  
📝 **Description:** Vovk - Debugging module for Advanced Dynamic Yara Rule Generation.
Vovk is a dynamic analysis tool that can be used as a module with the debugger (WinDBG). The tool itself is a DLL, built using both WdbgExts and DbgEng frameworks.
The way the tool works is pretty straightforward. You load Vovk into the debugger and then execute it. It runs through the malware and collects code snippets from memory and writes them to Yara file as a complete ruleset on the disk. You can then use the generated Yara ruleset to contain and neutralize malware campaigns or simply respond to security incidents that you are working on.

</details>

<details><summary><strong>YAMA: Yet Another Memory Analyzer for Malware Detection</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tomoaki Tani](https://img.shields.io/badge/Tomoaki%20Tani-informational) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational)

🔗 **Link:** [YAMA: Yet Another Memory Analyzer for Malware Detection](https://github.com/t-tani)  
📝 **Description:** YAMA is a system for generating tools that can inspect whether specific malware is present in memory during incident response. While numerous security countermeasure products exist for malware detection, targeted attacks utilizing malware that operates only in memory remain challenging to detect using existing products and continue to pose a threat.
Looking at existing open-source software (OSS) projects, some, such as PeSieve and Moneta, perform memory scans on live memory. However, few offer detection methods specifically tailored to particular malware for live systems. As file-less malware threats increase, having the means to verify the presence of malware in memory across multiple endpoints becomes crucial in incident response.
Using our proposed YAMA system, the scanner generated can create memory scanners tailored explicitly to any malware. The scanner generated by YAMA is a standalone executable capable of running on most 64-bit Windows OS. When infection investigation of malware present only in memory is required during incident response, executing the scanner created by YAMA on the suspected device will easily detect whether it is infected. Furthermore, in cases where a large-scale infection is suspected, the scanner can be distributed via Active Directory (AD) to clarify the infection status within the network.
YAMA is expected to be a powerful support tool for enhancing the investigative capabilities of Blue Teams, who conduct incident response daily.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>APKiD: Fast Identification of Mobile RASP SDKs</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Eduardo Novella](https://img.shields.io/badge/Eduardo%20Novella-informational)

🔗 **Link:** Not Available  
📝 **Description:** APKiD is like "PEiD" for Android applications. It gives information on how an APK was built by fingerprinting compilers, packers, obfuscators, and protectors. The main idea behind the tool is to help provide context on how the APK was potentially built or changed after it was built. This is all context useful for attributing authorship and finding patterns.

Extracting information about how the APK was made, it can provide a lot of information to assess the healthiness of an Android application (e.g. malware or pirated). The framework is the combination of a bunch of Yara rules and Python wrappers that scan files within APKs. Mainly, APKiD unpacks files and explores AndroidManifest.xml, DEX and ELF files to match rules and offers results based on them.

</details>

<details><summary><strong>Glyph - An Architecture Independent Binary Analysis Tool for Fingerprinting Functions Through NLP</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Corey Hartman](https://img.shields.io/badge/Corey%20Hartman-informational)

🔗 **Link:** [Glyph - An Architecture Independent Binary Analysis Tool for Fingerprinting Functions Through NLP](https://github.com/Xenios91)  
📝 **Description:** Reverse engineering is an important task performed by security researchers to identify vulnerable functions and malicious functions in IoT (Internet of Things) devices that are often shared across multiple devices of many system architectures. Common techniques to currently identify the reuse of these functions do not perform cross-architecture identification unless specific data such as unique strings are identified that may be of use in identifying a piece of code. Utilizing natural language processing techniques, Glyph allows you to upload an ELF binary (32 & 64 bit) for cross-architecture function fingerprinting, upon analysis, a web-based function symbol table will be created and presented to the user to aid in their analysis of binary executables/shared objects.

</details>

<details><summary><strong>SHAREM: Advanced Windows Shellcode Analysis Framework with Ghidra Plugin</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational) ![Jake Hince](https://img.shields.io/badge/Jake%20Hince-informational) ![Max Kersten](https://img.shields.io/badge/Max%20Kersten-informational)

🔗 **Link:** [SHAREM: Advanced Windows Shellcode Analysis Framework with Ghidra Plugin](https://github.com/Bw3ll/sharem)  
📝 **Description:** Shellcode can be cryptic, especially when encoded. Understanding its functionality is not straightforward. SHAREM is a cutting-edge Shellcode Analysis Framework, with both emulation and its own disassembler. SHAREM's unprecedented capabilities can allow us to unravel the mysteries of shellcode in new ways not seen.

Windows syscalls have become trendy in offensive security, yet SHAREM is the only tool that can emulate and log all user-mode Windows syscalls. Additionally, SHAREM also emulates and logs thousands of WinAPI functions. SHAREM is the only shellcode tool to parse and discover not only parameters, but also entire structures passed as parameters. SHAREM doesn't present parameters as hexadecimal values, but converts each to human readable format, in vivid colors.

Disassemblers like IDA Pro and Ghidra can be poor at disassembling shellcode accurately. SHAREM's disassembler is significantly more accurate with its original analysis capabilities. SHAREM additionally can uniquely integrate emulation results to provide flawless disassembly. Novel signature identifications are used to identify each function in the shellcode, and parameter values. SHAREM uses unique capabilities to accurately identify data, presenting data the correct way, not as misinterpreted instructions. SHAREM also uniquely provides complete-code coverage via emulation, capturing all functionality.

New at Arsenal, we will release a new script that allows SHAREM's output to be ingested by Ghidra. While Ghidra can handle shellcode in some cases, it simply cannot beat a framework specifically designed to handle and emulate shellcode. As such, this new release leverages SHAREM's advanced capabilities. Additionally, major updates include revamped complete-code coverage, timeless debugging of stack, nearly doubling the number of supported WinAPIs.

SHAREM provides unprecedented capabilities with encoded shellcode. Not only does it fully deobfuscate shellcode through emulation, discovering WinAPIs and syscalls, but it automatically recovers the shellcode's deobfuscated form. SHAREM presents error-free disassembly of its decoded form, with function calls and parameters labelled.

</details>

<details><summary><strong>Z9 - Malicious PowerShell Script Analyzer</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Shota Shinogi](https://img.shields.io/badge/Shota%20Shinogi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Reversing a malicious PowerShell script can be a very tedious and time-consuming process, especially when the script is obfuscated. Z9 provides an efficient solution to this problem. It is a PowerShell script analyzer that can quickly deobfuscate the script and determine whether it is malicious or not. Z9 leverages several detection engines to make an informed decision.

* Obfuscation Detection
* Randomized String Detection
* URL Extractor
* Blacklist
* AI (Logistic Regression)
* Sandbox

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>AutoSuite: An Open-Source Multi-Protocol Low-Cost Vehicle Bus Testing Framework</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Mingming Wan](https://img.shields.io/badge/Mingming%20Wan-informational) ![Zhongyu Wang](https://img.shields.io/badge/Zhongyu%20Wang-informational) ![Xingcan Chen](https://img.shields.io/badge/Xingcan%20Chen-informational)

🔗 **Link:** Not Available  
📝 **Description:** Vehicle buses such as FlexRay, LIN, CAN (FD) and Ethernet are the cornerstones of ECUs communication. At present, the security research of vehicle buses mainly focuses on CAN Bus. Due to the characteristics of the protocol itself, CAN data is usually transmitted within the domain. while Flexray is often used as a backbone network connecting powertrain control, autonomous driving, and body control domains for cross-domain communication and transmission of critical data.
It is commonly used in high-end brands such as Audi, Lotus, and BMW. However, security research on Flexray is still in its infancy.

We will present AutoSuite, an open-source, multi-protocol, low-cost vehicle bus testing framework, consisting of the AutoBox(hardware) and AutoFunc (software). AutoSuite can be used to access the FlexRay bus and simulate malicious ECUs to send forged data to realize cross-domain ECU attacks and discover potential security vulnerabilities.

AutoBox is probably the first open-source, multi-protocol, low-cost vehicle bus testing hardware that support FlexRay. It can automatically analyze FlexRay bus configuration parameters, join the cluster, and send malicious data on the FlexRay bus. The hardware cost is about $200, which is much lower than the commercial FlexRay bus testing tool Vector VN8910 ($50k). AutoBox also supports remote control, multiple device collaboration, and Ethernet, LIN, and CAN (FD) protocols. AutoBox will provide a friendly, open-source, and low-cost testing tool for vehicle bus researchers, much like HACKRF has become a low-cost alternative to USRP.

AutoFunc may be the first open-source software for functional-level communication testing and functional-level fuzzing that supports condition monitoring. Current open-source vehicle bus testing methods mainly rely on random fuzzing of the CAN protocol by using random data frame IDs, payloads, and DLC. However, a vehicle function typically involves multiple data frames, and a single data frame may not have any impact on the bus. With opendbc and other open-source projects, the .dbc file is no longer a commercial secret. AutoFunc can organize the frames defined in the .dbc file into specific functions, and monitor the function where the crash occurs to achieve a multi-protocol fuzzing test.

In addition, we will show 2 demos,
(1) Demonstrate all functions supported by AutoBox, such as FlexRay, CAN, LIN, Ethernet, WiFi, etc.
(2) Functional-level fuzzing using AutoBox and AutoFunc.

</details>

<details><summary><strong>CLExtract: An End-to-End Tool Decoding Highly Corrupted Satellite Stream from Eavesdropping</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Minghao Lin](https://img.shields.io/badge/Minghao%20Lin-informational) ![Minghao Cheng](https://img.shields.io/badge/Minghao%20Cheng-informational) ![Yueqi Chen](https://img.shields.io/badge/Yueqi%20Chen-informational) ![Xu Zheng](https://img.shields.io/badge/Xu%20Zheng-informational) ![Dongsheng Luo](https://img.shields.io/badge/Dongsheng%20Luo-informational) ![Huajiang Chen](https://img.shields.io/badge/Huajiang%20Chen-informational)

🔗 **Link:** Not Available  
📝 **Description:** While satellite communication with ground stations can be eavesdropped on using consumer-grade products, the received signals are oftentimes highly corrupted and cannot be effectively decoded using the traditional finite-state machine (FSM) based approach.

To this end, we develop a tool named CLExtract which utilizes contrastive learning techniques to decode and recover corrupted satellite streams. Unlike the traditional FSM-based approach which relies on critical fields that become unreliable after corruption, CLExtract directly learns the features of packet headers at different layers and identifies them in a stream sequence. By filtering out these headers, CLExtract extracts the innermost payload which contains sensitive and private data. Further, CLExtract incorporates data augmentation techniques to entitle the trained contrastive learning models with robustness against unseen forms of corruption.

To evaluate CLExtract, we performed eavesdropping on the spectrum range from 11 GHZ to 12.75 GHZ in a suburban area of a metropolis with more than 10 million of population in Asia, covering radio signals from seven commercial satellites. CLExtract can successfully decode and recover 71-99% of the total 23.6GB eavesdropped data, a significant improvement over the traditional FSM-based approach implemented by GSExtract which only recovers 2%.

During the arsenal presentation, we will make CLExtract open source and demonstrate its usage to the security community using real-world satellite streams. This way, we hope to foster future research on satellite offense and defense techniques.

</details>

<details><summary><strong>EMBA – From Firmware to Exploit</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michael Messner](https://img.shields.io/badge/Michael%20Messner-informational)

🔗 **Link:** Not Available  
📝 **Description:** 

</details>

<details><summary><strong>HIDE & SEEK: An Open Source Implant for Red Teams</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jonathan Fischer](https://img.shields.io/badge/Jonathan%20Fischer-informational)

🔗 **Link:** [HIDE & SEEK: An Open Source Implant for Red Teams](https://github.com/mgeeky/ProtectMyTooling)  
📝 **Description:** Many Enterprises are shifting away from dedicated workstations and cubes, and moving to a more flexible workspace with thin client and desk hoteling. This creates the ideal landscape for hardware implant attacks. The current implant market, as it exists today, has not kept up with this shift. While closed source for-profit solutions exist, by their nature they lack the flexibility and customization to adapt to large scale targeted deployments. Open source projects similarly exist but focus more on individual workstations (dumb keyboards and remote terminals) relying on corporate networks for remote control and are easily detectable. Neither solution today is able to meet the needs of a modern Red Team.
This presentation introduces an open source, freely available hardware implant which adopts modern IoT technologies, leveraging non-standard communication channels to create a remotely managed mesh network of hardware implants. Attendees will learn about the new techniques and tactics that we used to create a new breed of open-source hardware implant. Topics covered in this presentation will include the scaling of implants for a stealthy enterprise takeover, creating and utilizing a flexible command and control mesh network, creating a new class of remote access shells that survive idle screen lock, and more. Attendees will leave the talk with new tactics and a new platform from which to innovate their own custom implants from. Live demos will be used to demonstrate these new tactics against real world infrastructure.
Previous hardware implant talks have covered: basic implants, their benefits, injecting keystrokes, Wi-Fi connectivity, and attack scripts. This presentation builds off of those but shows attendees how to leverage new techniques and technologies to push the innovation of hardware implants forward evolutionarily for use in today's modern Red Team operations.

</details>

<details><summary><strong>ICS Forensics Tools</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Ori Perez](https://img.shields.io/badge/Ori%20Perez-informational) ![Maayan Shaul](https://img.shields.io/badge/Maayan%20Shaul-informational)

🔗 **Link:** [ICS Forensics Tools](https://github.com/nikhil130yadav/k-means-cluster-on-text-data/blob/master/output_30000words_3000Topics.txt)  
📝 **Description:** open source forensic toolkit for analyzing Industrial PLC metadata and project files. ICS Forensics Tools enables investigators to identify suspicious artifacts on ICS environment for detection of compromised devices during incident response or manual check. ICS Forensics Tools is open source, which allows investigators to verify the actions of the tool or customize it to specific needs. We will be announcing two new forensics tools.These presentation will include live demonstrations, as well as a quick and easy-to-use forensics guide utilizing the tool. The tools will be available for immediate use, right before the session begins.

</details>

<details><summary><strong>Out-Of-Band Anti Virus Dock (OOBAVD) - A Hardware & Artificial Intelligence Based Anti Virus Solution</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Pengfei Yu](https://img.shields.io/badge/Pengfei%20Yu-informational) ![Bosen Zhang](https://img.shields.io/badge/Bosen%20Zhang-informational) ![Jing Zhi Tan](https://img.shields.io/badge/Jing%20Zhi%20Tan-informational) ![Winston Ho](https://img.shields.io/badge/Winston%20Ho-informational) ![Howard Yang](https://img.shields.io/badge/Howard%20Yang-informational)

🔗 **Link:** Not Available  
📝 **Description:** USB-based attacks account for more than 52% of all cybersecurity attacks on operational technology (OT) systems in the industrial control systems (ICS) industry. The discovery of Stuxnet in 2015 served as a stark reminder that even air-gapped computers, previously thought to be impervious to cyberattacks, are vulnerable. These systems are found in secure military organizations or Supervisory Control and Data Acquisition (SCADA) systems. The societal impact of such attacks can be enormous. Stuxnet, for example, caused significant damage to Iran's nuclear programs and facilities.

While air-gapped systems are considered "secure," they are inconvenient for computer operators, particularly when performing updates and transferring data, which require the use of mobile storage devices, such as USB sticks. Unfortunately, this introduces a flaw into the air-gapped systems, exposing them to computer viruses and malware. Furthermore, adding new peripherals to these systems, such as keyboards and mice, allows BadUSB attacks to be carried out.

OOBAVD is a solution to close this gap. OOBAVD acts as a intermediary between the air-gapped system and USB devices, scanning and blocking detected malicious files from the air-gapped system. Furthermore, malware can attack commercial software-based antivirus software on the host machine by blocking, corrupting, and replacing core antivirus engine files, rendering them inoperable and defenseless. OOBAVD being out of band in the transfer process, is mitigated from this risk.

OOBAVD is designed to have minimum software pre-installed, which reduces the attack surface area to be infected by malware. OOBAVD can also be wiped clean and flashed before connecting to new air-gapped computers, removing persistent malware that manages to infect OOBAVD.

</details>

<details><summary><strong>Puppet Fuzz: Discovering Critical Kernel Vulnerabilities with Innovative Approach</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Siqi Chen](https://img.shields.io/badge/Siqi%20Chen-informational) ![Minghang Shen](https://img.shields.io/badge/Minghang%20Shen-informational) ![Chunyang Han](https://img.shields.io/badge/Chunyang%20Han-informational) ![Xin Wang](https://img.shields.io/badge/Xin%20Wang-informational)

🔗 **Link:** Not Available  
📝 **Description:** Internet of Things (IoT) devices have become an integral part of our lives, but their security vulnerabilities pose a significant risk to our privacy and security. While previous research has focused on user space components of embedded firmware, we have discovered that kernel vulnerabilities in these complex devices are particularly high-risk, potentially leading to full system compromise.
Kernel modules are typically tightly bound to the kernel, but because different IoT devices use different kernel versions and compile options, it is difficult to load them correctly in other simulated environments. However, true device-based fuzz testing is very time-consuming and resource-intensive. Additionally, unlike user-level programs, kernel-level programs require a device reboot after every crash, which further limits the development of IoT kernel fuzz testing.
To address these challenges, we propose a novel approach that abstracts closed-source kernel modules code to execute on a stable Linux kernel environment that we have constructed by using our aspect oriented system. This platform allows us to transfer library function calls and stack management, enabling us to detect kernel-level vulnerabilities that were previously difficult to identify. In addition, due to our front-end and back-end separation design, the platform can easily support IoT drivers of multiple architectures. Our approach has enabled us to discover a multitude of issues across devices from top manufacturers such as Netgear, Cisco, Asus, HP,TPLink,DLink and Western Digital etc.
In this talk, we will show our method and present one such universal kernel hardware module vulnerability, demonstrating how we were able to exploit a kernel driver vulnerability to achieve remote command execution on the device. Our platform provides a replicable and stable environment that forms the basis for efficient and effective kernel fuzz testing, ultimately improving the security of IoT devices and protecting the privacy of their users.

</details>

<details><summary><strong>Safe Scan&C2 Tool</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Weichao Zhou](https://img.shields.io/badge/Weichao%20Zhou-informational)

🔗 **Link:** Not Available  
📝 **Description:** In the process of security attack and defense, as well as penetration testing, there are two prominent issues. First, the attack scanning is often detected by the security systems of the defense side, resulting in the scanning IP being blocked. Second, when the defense side is controlled and assets are connected back to the command and control (C2) server, it may be detected by security devices, leading to countermeasures against the penetration testers. In order to safely and conveniently conduct asset detection during the attack and defense process, as well as secure connection back to the controlled assets on the defense side, we have improved the Kademlia protocol and developed a distributed hash table (DHT) technology. We have also developed a networking tool that consists of a large number of Internet nodes, which dynamically updates IDs and node tree structures at regular intervals. This allows each session to initiate requests from a different node during the scanning process, preventing IP blocking due to high-frequency scanning. Additionally, during the controlled asset's connection back to the C2 server, nodes are randomly selected based on user-selected hop count, effectively preventing penetration testers from being traced, thus improving the penetration testing process.

</details>

<details><summary><strong>Thunderstorm: Turning Off the Lights in Your Data Center</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Joel Gámez Molina](https://img.shields.io/badge/Joel%20Gámez%20Molina-informational)

🔗 **Link:** [Thunderstorm: Turning Off the Lights in Your Data Center](https://github.com/JoelGMSec/MyTalks)  
📝 **Description:** One of the main premises of any IT installation, is to protect the entire infrastructure against possible failures. In addition to firewalls and other network elements, one of the vital points is the electrical system.

Thanks to uninterruptible power supplies (UPS), it is possible to cover and manage these issues economically. The main problem, is that many of these systems inherit the same bugs as other IoT devices, which makes them vulnerable to all kinds of attacks.

In this presentation, we will explain how it has been possible to develop different zero-day vulnerabilities thanks to social engineering, some investment, and a bit of common sense. Among other things, these flaws would make it possible to compromise the electrical system of an office or even that of a Data Center.

Since these devices share common components, it would be possible to obtain remote code execution (with the highest possible privileges) and/or denial of service on more than 100 different manufacturers. Moreover, all of this has been automated in a single framework, making it possible to detect and exploit these vulnerabilities easily, simply and fully automatically.

</details>

---
## Others
<details><summary><strong>BLE CTF - A Bluetooth Low Energy Security Research Platform</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ryan Holeman](https://img.shields.io/badge/Ryan%20Holeman-informational)

🔗 **Link:** [BLE CTF - A Bluetooth Low Energy Security Research Platform](https://github.com/Charmve/BLE-Security-Attack-Defence)  
📝 **Description:** BLE CTF is a series of Bluetooth Low Energy challenges in a capture the flag format. It was created to teach the fundamentals of interacting with and hacking Bluetooth Low Energy services. Each exercise, or flag, aims to interactively introduce a new concept to the user.

Over the past few years, BLE CTF has expanded to support multiple platforms and skill levels. Various books, workshops, trainings, and conferences have utilized it as an educational platform and CTF. As an open source, low cost of entry, and expandable education solution, BLE CTF has helped progress Bluetooth security research.

This demo will showcase the BLE CTF platform and its new variants. This will be the first public release of the CTF's newly supported hardware and companion firmware. Along with firmware for newly supported devices, a new expansion for the modular BLE CTF Infinity will be exhibited.

</details>

<details><summary><strong>BucketLoot - An Automated S3 Bucket Inspector</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Umair Nehri](https://img.shields.io/badge/Umair%20Nehri-informational) ![Owais Shaikh](https://img.shields.io/badge/Owais%20Shaikh-informational)

🔗 **Link:** Not Available  
📝 **Description:** Thousands of S3 buckets are left exposed over the internet, making it a prime target for malicious actors who may extract sensitive information from the files in these buckets that can be associated with an individual or an organisation. There is a limited research or tooling available that leverages such S3 buckets for looking up secret exposures and searching specific keywords or regular expression patterns within textual files.
BucketLoot is an automated S3 Bucket Inspector that can simultaneously scan all the textual files present within an exposed S3 bucket from platforms such as AWS, DigitalOcean etc. It scans the exposed textual files for:
- Secret Exposures
- Assets (URLs, Domains, Subdomains)
- Specific keywords | Regex Patterns (provided by the user)
The end user can even search for string based keywords or provide custom regular expression patterns that can be matched with the contents of these exposed textual files. All of this makes BucketLoot a great recon tool for bug hunters as well as professional pentesters.
The tool allows users to save the output in a JSON format which makes it easier to pass the results as an input to some third-party product or platform.

</details>

<details><summary><strong>Damn Vulnerable Bank</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Rewanth Tammana](https://img.shields.io/badge/Rewanth%20Tammana-informational) ![Hrushikesh Kakade](https://img.shields.io/badge/Hrushikesh%20Kakade-informational) ![Akshansh Jaiswal](https://img.shields.io/badge/Akshansh%20Jaiswal-informational)

🔗 **Link:** [Damn Vulnerable Bank](https://github.com/rewanthtammana/Damn-Vulnerable-Bank)  
📝 **Description:** With over 2.5 billion devices and millions of apps, Android is ruling the market. Developers had additional responsibility to protect the information and integrity of their users. Considering these high numbers, preventive measures should be taken to secure Android applications used by people across the globe.

We built an open-source vulnerable Banking application, a clone close to real-world banking applications. The existing vulnerable applications cover only basic OWASP vulnerabilities. Our vulnerable application covers multiple things like Binary analysis, Debugger detection bypasses, Frida analysis, writing custom code to decrypt data, and a lot more along with basic OWASP vulnerabilities. This product will be a one-stop place for android application security enthusiasts.

</details>

<details><summary><strong>DIAL - Did I Alert Lambda? Centralised Security Misconfiguration Detection Framework</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Saransh Rana](https://img.shields.io/badge/Saransh%20Rana-informational) ![Rashid Feroze](https://img.shields.io/badge/Rashid%20Feroze-informational) ![Harsh Varagiya](https://img.shields.io/badge/Harsh%20Varagiya-informational)

🔗 **Link:** Not Available  
📝 **Description:** Workloads on the cloud provide equal opportunities for hackers as much as they do for internal teams. Cloud-native companies are open to attacks from both outside forces and from within. With the ever-growing risk of a security breach and cloud misconfiguration being one of the most common factors of the same, the mean time to detect is supposed to be reduced to seconds instead of minutes/hours.

DIAL, or "Did I just alert Lambda?", is a cutting-edge security monitoring and alerting system that provides centralized visibility and analysis of potential internal threats and security misconfigurations across multiple AWS accounts. By leveraging the stateless nature of AWS Lambda, DIAL enables easy modular deployment and makes it highly scalable and cost-efficient, making it an efficient and effective tool for detecting and mitigating security risks.

It's an event-driven framework, because of which detection time for identifying any security misconfiguration is less than 4 secs whereas traditional SIEM detection time for misconfigurations is more than 5-7 minutes and It can easily be deployed in any organization using its cloud formation stack.

With DIAL, you can deploy a central security monitoring solution on your AWS accounts for pennies compared to deploying a traditional SIEM solution and can gain end-to-end visibility of their AWS infrastructure and receive timely alerts on issues like public database exposure and over-permissive IAM policies, helping them to proactively safeguard their systems and data.

</details>

<details><summary><strong>Dracon, Security Engineering Automation, No Code, At Your Fingertips</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Spyros Gasteratos](https://img.shields.io/badge/Spyros%20Gasteratos-informational) ![Vijendra Patel](https://img.shields.io/badge/Vijendra%20Patel-informational)

🔗 **Link:** Not Available  
📝 **Description:** Dracon is an open source, Application and Cloud Security Orchestration and Correlation (ASOC) platform, empowering organisations to establish and manage comprehensive application security programs. By creating customizable pipelines, Dracon enables the execution of a wide range of security tools against any target. During a pipeline execution Dracon runs user-configured tools in parallel. Concurrently, results from each tool are deduplicated, enriched with information based on organisational or regulatory policies, compliance requirements, and more, before being forwarded to any visualisation or data processing sink.
The primary objective of Dracon is to offer a scalable and flexible framework that enables execution of arbitrary security tools on code and infrastructure while processing the results in a versatile manner. Under the hood, Dracon runs parallel user-configured security tools(Producer Stage), aggregates, and transforms the results into an internal format.
Once results are normalised, Dracon can apply user defined information enrichment. An enricher is custom code that allows users to enhance the information presented based on internal policies and compliance requirements. Out of the box, Dracon supports Deduplication, Policy and SBOM information enrichers, while writing a new enricher is made easy for the user with the help of provided libraries.
Finally, Dracon directs enriched results to a layer of user-configurable Consumers. A consumer can be any data visualisation, alerting or vulnerability management solution. This powerful, extensible platform simplifies security engineering and enables organisations to strengthen their cybersecurity posture.

</details>

<details><summary><strong>Easy EASM - The Zero Dollar Attack Surface Management Tool</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Jason Haddix](https://img.shields.io/badge/Jason%20Haddix-informational) ![Olivia Gallucci](https://img.shields.io/badge/Olivia%20Gallucci-informational) ![Gunnar Andrews](https://img.shields.io/badge/Gunnar%20Andrews-informational)

🔗 **Link:** [Easy EASM - The Zero Dollar Attack Surface Management Tool](https://github.com/g0ldencybersec/EasyEASM)  
📝 **Description:** Easy EASM is just that... the easiest to set-up tool to give your organization visibility into its external facing assets.

The industry is dominated by $30k vendors selling "Attack Surface Management," but OG bug bounty hunters and red teamers know the truth. External ASM was born out of the bug bounty scene. Most of these $30k vendors use this open-source tooling on the backend.

With ten lines of setup or less, using open source tools, and one button deployment, Easy EASM will give your organization a complete view of your online assets. Easy EASM scans you daily and alerts you via Slack or Discord on newly found assets! Easy EASM also spits out an Excel skeleton for a Risk Register or Asset Database! This isn't rocket science.. but it's USEFUL. Don't get scammed. Grab Easy EASM and feel confident you know what's facing attackers on the internet.

</details>

<details><summary><strong>Introducing varc: Volatile Artifact Collector</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Chris Doman](https://img.shields.io/badge/Chris%20Doman-informational) ![Matt Muir](https://img.shields.io/badge/Matt%20Muir-informational)

🔗 **Link:** Not Available  
📝 **Description:** Varc (https://github.com/cado-security/varc) is a recently-released
open source volatile artifact collection tool.

Driven by a philosophy of simplicity and reliability, the tool was
developed to aid investigation of security incidents, and is available
to the community under a friendly licence. Varc achieves this by
collecting a snapshot of volatile data from a system and outputting it
as JSON - so that it can easily be ingested by another parser or read
by a human investigator.


Varc’s design philosophy has an emphasis on portability, meaning that
it can run across operating systems, in cloud and on-premise
environments – and also supports serverless artifact collection.


And if there is a demo talk requirement:

In this talk, Matt Muir, Threat Intelligence Researcher, Cado Security
and Chris Doman, CTO Cado Security will discuss the motivation for
developing varc. They’ll also cover the technical challenges inherent
to volatile artifact collection in serverless environments and across
operating systems. Finally, they’ll give a live demonstration of varc
and show the audience how it can be used to aid incident response.


Description
The talk will be divided into the following 4 sections:
1) Background and Motivation
2) Technical Challenges
3) varc Demonstration
4) Conclusion


Background and Motivation
Matt and Chris will begin the talk with some discussion of what
exactly varc is and an overview of its features. They’ll then move
on to discuss the reason for Cado Security’s development of this tool
and what problems varc addresses, when compared with other volatile
collection tools. Some background to varc’s design philosophy will
also be provided.


Technical Challenges
In this section, Matt and Chris will discuss the various technical
challenges that working with volatile data presents. This will include
an overview of which artifacts were deemed important to an incident
responder and how these can be accessed via Python code on the various
operating systems varc supports. There will also be some discussion on
how varc operates in serverless environments and what this means for
investigators working in this area.

varc Demonstration
This section will include a demonstration of varc on a system where
some malicious activity has occurred. Matt and Chris will highlight
artifacts of interest and demonstrate varc’s extraction and
presentation of these to the audience.


Conclusion
The talk will conclude with discussion about how varc is integrated
into Cado and how this benefits users of the platform. Matt and Chris
will also discuss the potential for further work in this area and
provide the audience with details of how they can get involved.
Finally, a Q&A session will give the audience an opportunity to have
any questions about varc answered.

</details>

<details><summary><strong>MORF - Mobile Reconnaissance Framework</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Amrudesh Balakrishnan](https://img.shields.io/badge/Amrudesh%20Balakrishnan-informational) ![Abhishek JM](https://img.shields.io/badge/Abhishek%20JM-informational) ![Himanshu Das](https://img.shields.io/badge/Himanshu%20Das-informational)

🔗 **Link:** Not Available  
📝 **Description:** MORF - Mobile Reconnaissance Framework is a powerful, lightweight, and platform-independent offensive mobile security tool designed to help hackers and developers identify and address sensitive information within mobile applications. It is like a Swiss army knife for mobile application security, as it uses heuristics-based techniques to search through the codebase, creating a comprehensive repository of sensitive information it finds. This makes it easy to identify and address any potentially sensitive data leak.

One of the prominent features of MORF is its ability to automatically detect and extract sensitive information from various sources, including source code, resource files, and native libraries. It also collects a large amount of metadata from the application, which can be used to create data science models that can predict and detect potential security threats. MORF also looks into all previous versions of the application, bringing transparency to the security posture of the application.

The tool boasts a user-friendly interface and an easy-to-use reporting system that makes it simple for hackers and security professionals to review and address any identified issues. With MORF, you can know that your mobile application's security is in good hands.

Overall, MORF is a Swiss army knife for offensive mobile application security, as it saves a lot of time, increases efficiency, enables a data-driven approach, allows for transparency in the security posture of the application by looking into all previous versions, and minimizes the risk of data breaches related to sensitive information, all this by using heuristics-based techniques.

</details>

<details><summary><strong>Pcapinator: Rise of the PCAP Machines</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Mike Spicer](https://img.shields.io/badge/Mike%20Spicer-informational)

🔗 **Link:** Not Available  
📝 **Description:** Pcapinator is a powerful and versatile network analysis tool that combines the strengths of TShark and Python to provide comprehensive and efficient packet deconstruction into a format usable for further analysis. Inspired by the Terminator, Pcapinator is designed to relentlessly analyze, decode, and filter network packets using all of the resources a system makes available to it, making it a formidable asset for diving deep into PCAPs.

Leveraging the robust capabilities of Wireshark's TShark tool, Pcapinator parses and extracts vital information from pcap files, while Python's extensive libraries and scripts offer advanced processing and automation options. Pcapinator is built to handle extremely large PCAP files, search for anomalies in those files, and uncover the hard-to-find information in network traffic, making it an essential tool for PCAP analysis.

</details>

<details><summary><strong>PurpleOPS - A Simple Tool to Help Track and Share Purple Team Data</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Willem Mouton](https://img.shields.io/badge/Willem%20Mouton-informational) ![Harrison Mitchell](https://img.shields.io/badge/Harrison%20Mitchell-informational)

🔗 **Link:** Not Available  
📝 **Description:** Purple team exercises are probably one of the most useful types of activities that organizations can engage in these days. Key to effective purple teaming is good communication, data collection and knowledge sharing. For us, this has been a bit of a pain point having to try and manually keep track of activities, actions and events. We did find some tools to aid with this, but none of them truly opensource or flexible enough to allow us to do what we wanted to do. So we built PurpleOPS, which is at its core a data collection tool aligned to MITRE ATT&CK and integrated into other fantastic open-source projects such as Atomic Redteam. It is easy to customize with your own internal knowledge base and test cases, plus it's also written in python3 using Flask, so it's super easy to adjust to your needs.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>From Boar to More: Upgrading Your Security with Trufflehog's Terminal UI</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Hon Kwok](https://img.shields.io/badge/Hon%20Kwok-informational) ![Miccah Castorina](https://img.shields.io/badge/Miccah%20Castorina-informational)

🔗 **Link:** Not Available  
📝 **Description:** Trufflehog is an open-source tool that helps organizations detect sensitive data leaks across their software development life cycle. It identifies text with potentially sensitive information and verifies if they are actually secret keys or passwords, reducing false-positive noise that often leads to alert fatigue.

Previously Trufflehog required command-line interface expertise and familiarity, which could be challenging to non-technical users. A new feature was recently added to provide a terminal user interface (TUI), enhancing accessibility for individuals with varying levels of technical expertise. Easy-to-use tooling contributes to a collaborative security culture that ultimately empowers individuals to engage in and improve their organization's security posture. Trufflehog's TUI enables anyone, regardless of technical skills, to scan for secrets across their organization and be a hero.

</details>

---
## 🔍 OSINT
<details><summary><strong>GodEye: Advanced Geo-Localization Through AI-Powered Visual Analysis</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Tung Cao Hoang](https://img.shields.io/badge/Tung%20Cao%20Hoang-informational) ![Son Le Duy](https://img.shields.io/badge/Son%20Le%20Duy-informational) ![Hieu Nam Tran Ngoc](https://img.shields.io/badge/Hieu%20Nam%20Tran%20Ngoc-informational) ![Anh Nguyen Ngoc](https://img.shields.io/badge/Anh%20Nguyen%20Ngoc-informational)

🔗 **Link:** Not Available  
📝 **Description:** God Eye is an innovative AI-powered geo-localization tool that can estimate a photograph's location without the need for EXIF data extraction. God Eye aims to improve the accuracy of current geolocation estimation techniques by combining cutting-edge models and techniques. The tool has a straightforward web-based interface that allows users to upload images and receive location estimates automatically. God Eye constantly improves its accuracy and expands its capabilities by comparing and training with open street view data and other crawled data sources. God Eye's primary applications are in open-source intelligence (OSINT) and cybersecurity, where it aids forensic investigations by identifying image source and location. God Eye, with its robust technology and user-friendly design, is poised to become an indispensable tool for professionals in a variety of fields who require precise and dependable image-based geolocation.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>HazProne: Cloud Vulnerability Simulator</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Staford Titus S](https://img.shields.io/badge/Staford%20Titus%20S-informational)

🔗 **Link:** Not Available  
📝 **Description:** HazProne is a Cloud Vulnerability Simulator Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand AWS resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!

</details>

<details><summary><strong>Prowler, Open Source for Multi-Cloud Security Assessments and Pentesting</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Toni de la Fuente](https://img.shields.io/badge/Toni%20de%20la%20Fuente-informational) ![Pepe Fagoaga](https://img.shields.io/badge/Pepe%20Fagoaga-informational)

🔗 **Link:** Not Available  
📝 **Description:** Whether you use AWS, Azure or Google Cloud, Prowler helps to assess, audit, pentest and harden your cloud infrastructure configuration and resources.

</details>

<details><summary><strong>Responding to Microsoft 365 Security Reviews Faster with Monkey365</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Juan Garrido](https://img.shields.io/badge/Juan%20Garrido-informational)

🔗 **Link:** Not Available  
📝 **Description:** Monkey 365 is a multi-threaded plugin-based tool to help assess the security posture of not only Microsoft 365, but also Azure subscriptions and Azure Active Directory. It contains multiple controls and currently supports CIS 1.4/1.5, HIPAA, GDPR, as well as custom security rules.

</details>

<details><summary><strong>SimpleRisk: Governance, Risk Management & Compliance</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

🔗 **Link:** [SimpleRisk: Governance, Risk Management & Compliance](https://github.com/OWASP/www-chapter-austin/blob/master/pastevents.md)  
📝 **Description:** As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform organizational Governance, Risk Management, and Compliance activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to manage control frameworks, policies, and exceptions, facilitate audits, and perform risk prioritization and mitigation activities. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

</details>

<details><summary><strong>Wabhawk/Catch - Unsupervised Machine Learning Detection</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Walid Daboubi](https://img.shields.io/badge/Walid%20Daboubi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Webhawk/Catch helps automatically finding web attack traces in HTTP logs without using any preset rules. Based on the usage of Unsupervised Machine Learning, Catch groups log lines into clusters, and detects the outliers that it considers as potentially attack traces. The tool takes as input a raw HTTP log file (Apache, Nginx..) and returns a report with a list of findings.

Catch uses PCA (Principal Component Analysis) technique to select the most relevant features (Example: user-agent, IP address, number of transmitted parameters, etc.. ). Then, it runs DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm to get all the possible log line clusters and anomalous points (potential attack traces).

Advanced users can fine tune Catch based on a set of options that help optimising the clustering algorithm (Example: minimum number of points by cluster, or the maximum distance between two points within the same cluster).

The current version of Webhawk/Catch generates an easy-to-read HTML report which includes all the findings, and the severity of each one.

</details>

---