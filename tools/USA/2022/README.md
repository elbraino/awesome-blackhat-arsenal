# USA 2022
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2022** event held in **USA**.
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
<details><summary><strong>AADInternals: The Swiss Army Knife for Azure AD & M365</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nestori Syynimaa](https://img.shields.io/badge/Nestori%20Syynimaa-informational)

🔗 **Link:** Not Available  
📝 **Description:** AADInternals is a popular attacking and administration toolkit for Azure Active Directory and Microsoft 365, used by red and blue teamers worldwide. The toolkit is written in PowerShell, making it easy to install and use by anyone familiar with the Microsoft ecosystem.

With AADInternals, one can create backdoors, perform elevation of privilege and denial-of-service attacks, extract information, and even bypass multi-factor authentication (MFA).

Join this session to see in action the research results conducted during the past three years, including a new technique to extract AD FS signing certificates remotely, exporting certificates of AAD joined devices, gathering OSINT, and more!

</details>

<details><summary><strong>AttackForge ReportGen v2: Powerful Pentest Reporting Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Fil Filiposki](https://img.shields.io/badge/Fil%20Filiposki-informational) ![Stas Filshtinskiy](https://img.shields.io/badge/Stas%20Filshtinskiy-informational)

🔗 **Link:** Not Available  
📝 **Description:** AttackForge ReportGen is a freely available and downloadable pentest reporting tool with powerful features such as:
- Rich template library in DOCX format to cover different types of pentest reports
- Support for over 200 tags - covering projects, vulnerabilities, assets, attack chains, test cases, retesting, and more
- Support for DOCX reports
- Support for tables, images, styled text, custom fields
- Easy to apply styles & changes directly in Word – no need or hassle to write code
- Logic engine for complex reporting requirements and templates

</details>

<details><summary><strong>AWSGoat : A Damn Vulnerable AWS Infrastructure</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Sanjeev Mahunta](https://img.shields.io/badge/Sanjeev%20Mahunta-informational)

🔗 **Link:** [AWSGoat : A Damn Vulnerable AWS Infrastructure](https://github.com/ine-labs/AWSGoat)  
📝 **Description:** Compromising an organization's cloud infrastructure is like sitting on a gold mine for attackers. And sometimes, a simple misconfiguration or a vulnerability in web applications, is all an attacker needs to compromise the entire infrastructure. Since the cloud is relatively new, many developers are not fully aware of the threatscape and they end up deploying a vulnerable cloud infrastructure. When it comes to web application pentesting on traditional infrastructure, deliberately vulnerable applications such as DVWA and bWAPP have helped the infosec community in understanding the popular web attack vectors. However, at this point in time, we do not have a similar framework for the cloud environment.

In this talk, we will be introducing AWSGoat, a vulnerable by design infrastructure on AWS featuring the latest released OWASP Top 10 web application security risks (2021) and other misconfiguration based on services such as IAM, S3, API Gateway, Lambda, EC2, and ECS. AWSGoat mimics real-world infrastructure but with added vulnerabilities. The idea behind AWSGoat is to provide security enthusiasts and pen-testers with an easy to deploy/destroy vulnerable infrastructure where they can learn how to enumerate cloud applications, identify vulnerabilities, and chain various attacks to compromise the AWS account. The deployment scripts will be open-source and made available after the talk.

</details>

<details><summary><strong>AzureGoat : A Damn Vulnerable Azure Infrastructure</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Rachna Umaraniya](https://img.shields.io/badge/Rachna%20Umaraniya-informational)

🔗 **Link:** [AzureGoat : A Damn Vulnerable Azure Infrastructure](https://github.com/ine-labs/AzureGoat)  
📝 **Description:** Microsoft Azure cloud has become the second-largest vendor by market share in the cloud infrastructure providers (as per multiple reports), just behind AWS. There are numerous tools and vulnerable applications available for AWS for the security professional to perform attack/defense practices, but it is not the case with Azure. There are far fewer options available to the community. AzureGoat is our attempt to shorten this gap.

In this talk, we will be introducing AzureGoat, a vulnerable by design infrastructure on the Azure cloud environment. AzureGoat will allow a user to do the following:

- Explore a vulnerable infrastructure hosted on an Azure account
- Exploring different ways to get a foothold into the environment, e.g., vulnerable web app, exposed endpoint, attached MSI
- Learn and practice different attacks by leveraging misconfigured Azure components like Virtual Machines, Storage Accounts, App Services, Databases, etc.
- Abusing Azure AD roles and permissions
- Auditing and fixing misconfiguration in IaC
- Redeploying the fixed/patched infrastructure

The user will be able to deploy AzureGoat on their Azure account using a pre-created Docker image and scripts. Once deployed, the AzureGoat can be used for target practice and be conveniently deleted later.

All the code and deployment scripts will be made open-source after the talk.

</details>

<details><summary><strong>Badrats: Initial Access Made Easy</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Anthony Rose](https://img.shields.io/badge/Anthony%20Rose-informational) ![Kevin Clark](https://img.shields.io/badge/Kevin%20Clark-informational)

🔗 **Link:** [Badrats: Initial Access Made Easy](https://gist.github.com/GMMan/4fa8860dc60460828217?permalink_comment_id=1451134)  
📝 **Description:** Remote Access Trojans (RATs) are one of the defining tradecraft for identifying an Advanced Persistent Threat. The reason being is that APTs typically leverage custom toolkits for gaining initial access, so they do not risk burning full-featured implants. Badrats takes characteristics from APT Tactics, Techniques, and Procedures (TTPs) and implements them into a custom Command and Control (C2) tool with a focus on initial access and implant flexibility. The key goal is to emulate that modern threat actors avoid loading fully-featured implants unless required, instead opting to use a smaller staged implant.

Badrats implants are written in various languages, each with a similar yet limited feature set. The implants are designed to be small for antivirus evasion and provides multiple methods of loading additional tools, such as shellcode, .NET assemblies, PowerShell, and shell commands on a compromised host. One of the most advanced TTPs that Badrats supports is peer-to-peer communications over SMB to allow implants to communicate through other compromised hosts.

</details>

<details><summary><strong>bloodyAD</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Baptiste Crepin](https://img.shields.io/badge/Baptiste%20Crepin-informational)

🔗 **Link:** Not Available  
📝 **Description:** BloodyAD is an Active Directory Privilege Escalation Framework. It helps you interact with the Active Directory (AD) to read/modify its objects in order to perform privilege escalation.
Two modes exist, the first one lets you perform atomic operations on the AD, it's the manual mode. The second one automates most of the privilege escalation operations.
The tool can be installed on Linux and Windows and is designed to be used on your offensive machine even if you're not on the local network of the targeted AD, relying on encapsulation protocols like SOCKS.

</details>

<details><summary><strong>Cotopaxi - M2M Protocols Assessment Toolkit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jakub Botwicz](https://img.shields.io/badge/Jakub%20Botwicz-informational)

🔗 **Link:** [Cotopaxi - M2M Protocols Assessment Toolkit](https://github.com/Samsung/cotopaxi)  
📝 **Description:** Cotopaxi is a set of tools for security testing of endpoints using state-of-the-art Machine-To-Machine network protocols (like AMQP, CoAP, gRPC, HTTP/2, HTCPCP, MQTT, DTLS, KNX, mDNS, QUIC, RTSP, SSDP).

</details>

<details><summary><strong>CQPenetrationTesting Toolkit: Powerful Toolset That All Pentesters Want to Have</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Paula Januszkiewicz](https://img.shields.io/badge/Paula%20Januszkiewicz-informational) ![Mike Jankowski-Lorek](https://img.shields.io/badge/Mike%20Jankowski-Lorek-informational)

🔗 **Link:** Not Available  
📝 **Description:** CQ Penetration Testing Toolkit supports you in performing complex penetration tests as well as shows the ways to use them, and the situations in which they apply. It guides you through the process of gathering intel about network, workstations, and servers. Common technics for antimalware avoidance and bypass, lateral movement, and credential harvesting. The toolkit allows also for decrypting RSA keys and EFS protected files as well as blobs and objects protected by DPAPI and DPAPI-NG. This powerful toolkit is useful for those who are interested in penetration testing and professionals engaged in pen-testing working in the areas of database, system, network, or application administration. Among published presented tools are CQARPSpoofer, CQCat, CQDPAPIBlobDecrypter, CQMasterKeyDecrypt, CQReverseShellGen, and many more.

</details>

<details><summary><strong>ElfPack: ELF Binary Section Docking in Stageless Payload Delivery</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dimitry Snezhkov](https://img.shields.io/badge/Dimitry%20Snezhkov-informational)

🔗 **Link:** Not Available  
📝 **Description:** When it comes to generating and delivering malware on Linux, offensive operators have choices. Some objectives call for a dynamic payload bootstrap off the wire, others require stageless implants.

Often, malware deployed with bundled payloads can be successfully detected and analyzed. However, we think there are opportunities to improve on the process of embedding payloads in standalone implants that can elevate their survival levels.

ElfPack is one such development in the static payload embedding and loading tailored for adversary simulation teams. In our demo we will demonstrate the mechanisms of construction of ELF binaries, focusing on how ELFPack can use sections facilitate a successful stealthy payload hosting, retrieval and loading.

We will show the concept of ELF section docking, whereby a section containing payload can be independently attached to the payload-agnostic loader. We will further expand the concept to address in-field (re-)attachment of sections to loaders without the use of compilers which may be very useful for long-haul offensive operations.

Furthermore, we will show how ElfPack can be successfully used as an alternative to executable packing when addressing complex payloads and providing teams with options and flexibility in multiple payload delivery scenarios.

We will demonstrate both detection opportunities and the enhanced evasion features implemented in a ElfPack proof-of-concept loader and injector tooling.

We feel that ElfPack and section docking in general can help solve some of the payload bundling challenges for the offensive operators, and also introduce ideas to hunters to detect and respond to this technique.

</details>

<details><summary><strong>MacAttack - A Client/Server Framework with Macro Payloads for Domain Recon and Initial Access</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Chris Nevin](https://img.shields.io/badge/Chris%20Nevin-informational)

🔗 **Link:** Not Available  
📝 **Description:** While using macros for malicious purposes is nothing new, this tool provides a suite of payloads ideal for initial recon and footholds that will not burn other methods of attack. MacAttack is a framework that generates payloads for use in Excel and includes client/server communication to perform dynamic alterations at runtime and collate received data.
The payloads included in MacAttack cover a number of areas that have not been published before, including a new stealth technique for hiding payloads, methods for retrieving a user's hash, and performing common recon/early stages attacks such as As-Rep roasting, retrieving documents, browser credentials, password spraying the domain, enumerating users, and domain fronting. The client/server communication and GUI will allow for dynamic checks such as only allowing a password spray to run once or once within a certain time period even if multiple targets enable the payload at the same time, and will provide a visual representation of the enumerated information. Part of the benefit of this tool is that this information is retrievable from a "zero foothold" position - a phishing campaign may be detected or blocked - but this does not burn any existing beacons and the potential rewards can be as great as multiple sets of credentials for users and relevant authentication portals. Microsoft are rolling out changes to macros that have still not been fully deployed by the time of the deadline - and research into these changes and impacts will be included in the discussion. It looks like these changes will only affect O365 to begin with and will include a "recommended policy" to implement.

</details>

<details><summary><strong>MUSHIKAGO-femto: Automated Pentest & First Aid Tool for IT/OT Environments</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yuta Ikegami](https://img.shields.io/badge/Yuta%20Ikegami-informational) ![Masato Hamamura](https://img.shields.io/badge/Masato%20Hamamura-informational)

🔗 **Link:** Not Available  
📝 **Description:** At the Black Hat USA 2021 Arsenal, we presented MUSHIKAGO, an automated penetration testing tool for both IT and OT. MUSHIKAGO can automatically perform penetration tests and post-exploitation in various environments without prior learning.

This time, we have newly evolved MUSHIKAGO as MUSHIKAGO-femto, incorporating cutting-edge features. The evolution includes the implementation of a mechanism to perform first aid on the tested system and acquire immune functions so that the same attack can be defended against attacks that could be achieved by penetration tests. A function was implemented to defend against vulnerability attacks by applying patches, injecting FW functions or proprietary IPS into terminals. Specifically, taking advantage of the fact that the penetration test was able to penetrate the system, patches are applied as if injecting a vaccine at the penetrated terminal, or a unique thin IPS is incorporated. This allows the system to be defended before the actual attacker can exploit the vulnerability or misconfiguration. Based on these results, MUSHIKAGO-femto has become the Next-Generation Pentest Tool that strengthens system defenses while performing penetration testing.

Other additional features include the implementation of a scan function to detect ICS protocols in order to detect ICS devices with high accuracy. MUSHIKAGO-femto has both Active Scan and Passive Scan functions, enabling comprehensive detection of PLCs and ICS devices. This enables automatic penetration of OT system. This makes it possible to perform automatic penetration tests on OT system with high accuracy. In the demo, we will show how it can perform automatic penetration testing and automatic protection against Hack THe Box and VulnHub machines. We will also show that it is possible to perform effective penetration testing in our OT/ICS environment.

</details>

<details><summary><strong>PyRDP: Remote Desktop Protocol MITM for Purple Teamers</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Lisandro Ubiedo](https://img.shields.io/badge/Lisandro%20Ubiedo-informational)

🔗 **Link:** [PyRDP: Remote Desktop Protocol MITM for Purple Teamers](https://github.com/GoSecure/pyrdp/releases)  
📝 **Description:** PyRDP is a Remote Desktop Protocol (RDP) monster-in-the-middle (MITM) tool and library useful in intrusion testing, and protocol and malware research. Its out-of-the-box offensive capabilities can be divided in three broad categories: client-side, MITM-side and server-side. On the client-side, PyRDP can actively steal any clipboard activity, crawl mapped drives and collect all keystrokes. On the MITM-side PyRDP records everything on the wire in several formats (logs, JSON events), captures the user's hashes on-the-fly to enable hash cracking, it also allows an attacker to take control of an active session and performs a pixel perfect recording of the RDP screen. On the server-side, on-logon PowerShell or command injection can be performed when a legitimate client connects.

As a research tool, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It can replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation or to generate IOCs. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads.

This year we have implemented NetNTLMv2 hash capturing for NLA sessions which enables pentesters and offensive researchers to crack hashes in order to retrieve passwords used during the user's connection.

</details>

<details><summary><strong>SCMKit: Source Code Management Attack Toolkit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Brett Hawkins](https://img.shields.io/badge/Brett%20Hawkins-informational)

🔗 **Link:** Not Available  
📝 **Description:** Source Code Management (SCM) systems play a vital role within organizations and have been an afterthought in terms of defenses compared to other critical enterprise systems such as Active Directory. SCM systems are used in the majority of organizations to manage source code and integrate with other systems within the enterprise as part of the DevOps pipeline, such as CI/CD systems like Jenkins. These SCM systems provide attackers with opportunities for software supply chain attacks and can facilitate lateral movement and privilege escalation throughout an organization.

This presentation will announce the public release of SCMKit, a toolkit that can be used to attack SCM systems. SCMKit allows the user to specify the SCM system and attack module to use, along with specifying valid credentials (username/password or API key) to the respective SCM system. Currently, the SCM systems that SCMKit supports are GitHub Enterprise, GitLab Enterprise and Bitbucket Server. The attack modules supported include reconnaissance, privilege escalation and persistence. SCMKit was built in a modular approach, so that new modules and SCM systems can be added in the future by the information security community.

</details>

<details><summary><strong>Secureworks® Primary Refresh Token (PRT) viewer</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nestori Syynimaa](https://img.shields.io/badge/Nestori%20Syynimaa-informational)

🔗 **Link:** [Secureworks® Primary Refresh Token (PRT) viewer](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/ReplayOfPrimaryRefreshToken.md)  
📝 **Description:** Azure AD registered and joined devices use a device certificate and transport key to sign and decrypt communication between the device and Azure AD. The most important part of this is Primary Refresh Token (PRT) and an associated session key. The session key can be decrypted with the transport key and subsequent communication with the session key.
Secureworks® Primary Refresh Token (PRT) viewer automates the decryption process. Using the transport key exported from the target computer, it automatically decrypts the session key from the PRT authentication request response. With the decrypted session key, it decrypts subsequent requests/responses decrypted with the session key.
The tool enables monitoring the traffic between the target device and Azure AD in plaintext, allowing extracting keys, access tokens, and other secrets.
The tool is available as Burp Suite Extender and Fiddler Add-On.

</details>

<details><summary><strong>SharpSCCM</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Chris Thompson](https://img.shields.io/badge/Chris%20Thompson-informational) ![Duane Michael](https://img.shields.io/badge/Duane%20Michael-informational)

🔗 **Link:** [SharpSCCM](https://github.com/Mayyhem/SharpSCCM)  
📝 **Description:** SharpSCCM is an open-source C# utility for interacting with SCCM, inspired by the PowerSCCM project by @harmj0y, @jaredcatkinson, @enigma0x3, and @mattifestation. This tool can be used to demonstrate the impact of configuring SCCM without the recommended security settings, which can be found here: https://docs.microsoft.com/en-us/mem/configmgr/core/clients/deploy/plan/security-and-privacy-for-clients

Currently, SharpSCCM supports the NTLMv2 coercion attack techniques noted in this post (https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a), as well as the attack techniques noted in this post (https://enigma0x3.net/2016/02/29/offensive-operations-with-powersccm/), which have been modified to coerce NTLMv2 authentication rather than running PowerShell on the target. SharpSCCM can also be used to dump information about the SCCM environment from a client, including the plaintext credentials for Network Access Accounts.

Research is ongoing to add SharpSCCM features to:
- pull and decrypt Network Access Account credentials from SCCM servers using a low-privileged account on any client machine
- execute actions in SCCM environments that require PKI certificates to secure client/server communications
- escalate privileges from local administrator on site servers to SCCM Full Administrator

</details>

<details><summary><strong>SMBeagle</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Simon Gurney](https://img.shields.io/badge/Simon%20Gurney-informational)

🔗 **Link:** [SMBeagle](https://github.com/punk-security/smbeagle)  
📝 **Description:** SMBeagle is an SMB file share auditing and enumeration tool that rapidly hunts out file shares and inventories their contents. Built from a desire to find poorly protected files, SMBeagle casts the spotlight on files vulnerable to ransomware, watering hole attacks and which may contain sensitive credentials.

SMBeagle hunts out all files it can see in the network and reports if the file can be read and/or written. All these findings are streamed out to either a CSV file or an elasticsearch host?

Businesses of all sizes often have file shares with awful file permissions.

Large businesses have sprawling file shares and its common to find sensitive data with misconfigured permissions and small businesses often have a small NAS in the corner of the office with no restrictions at all!

SMBeagle crawls these shares and lists out all the files it can read and write. If it can read them, so can ransomware.

SMBeagle can provide penetration testers with the less obvious routes to escalate privileges and move laterally.

By outputting directly into elasticsearch, testers can quickly find readable scripts and writeable executables.

Finding watering hole attacks and unprotected passwords never felt so easy!

</details>

<details><summary><strong>SquarePhish: Combining QR Codes and OAuth 2.0 Device Code Flow for Advanced Phishing Attacks</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nevada Romsdahl](https://img.shields.io/badge/Nevada%20Romsdahl-informational) ![Kam Talebzadeh](https://img.shields.io/badge/Kam%20Talebzadeh-informational)

🔗 **Link:** Not Available  
📝 **Description:** SquarePhish is an advanced phishing tool that uses a technique combining the OAuth Device code authentication flow and QR Codes.

</details>

<details><summary><strong>Stratus Red Team, an Open-Source Adversary Emulation Tool for the Cloud</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Christophe Tafani-Dereeper](https://img.shields.io/badge/Christophe%20Tafani-Dereeper-informational)

🔗 **Link:** [Stratus Red Team, an Open-Source Adversary Emulation Tool for the Cloud](https://github.com/datadog/stratus-red-team/releases)  
📝 **Description:** Stratus Red Team is an open-source project for adversary emulation and validation of threat detection in the cloud. It comes with a catalog of cloud-native attack techniques mapped to MITRE ATT&CK that you can easily detonate against a live cloud environment or Kubernetes cluster.

Stratus Red Team supports common AWS and Kubernetes attack techniques. You can point it at a live AWS account or Kubernetes cluster and easily detonate TTPs commonly used by offensive actors, without any prerequisite infrastructure or configuration needed. It helps you validate your threat detection end-to-end and even has a programmatic interface to integrate it with existing automation.
Stratus Red Team transparently leverages Terraform to provision the infrastructure required to detonate TTPs, and Go to perform the actual attacks. The TTPs it packages are opinionated: granular, threat-informed, and actionable for defenders.

</details>

<details><summary><strong>Suborner: A Windows Bribery for Invisible Persistence</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sebastián Castro](https://img.shields.io/badge/Sebastián%20Castro-informational)

🔗 **Link:** [Suborner: A Windows Bribery for Invisible Persistence](https://github.com/tismalhas/sfgfssfgsdgf?search=1)  
📝 **Description:** Whenever an attacker is trying to persist the access on a compromised machine, the first offensive approach usually involves the creation of a new identity. Nevertheless, this may not work easily under hardened environments with diverse detection mechanisms against common attack vectors.

What if we "suborn" Windows to create our own hidden account that will grant us total access to a victim, while stealthily impersonating any account we want?

Now it is possible with the Suborner Attack.

This technique will dynamically create an invisible machine account with custom credentials and custom properties without calling any user management Win32 APIs (e.g. netapi32.dll::netuseradd) and therefore evading detection mechanisms (e.g Event IDs 4720, 4721). By "suborning" Windows, we can also impersonate any desired account to keep our stealthiness even after a successful authentication/authorization.

To show its effectiveness, the attack is going to be demonstrated against the latest Windows version available.

</details>

<details><summary><strong>The Metasploit Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

🔗 **Link:** [The Metasploit Framework](https://github.com/zerosteiner)  
📝 **Description:** Modern attack emulation is a multi-step process involving different tools and techniques as testers execute custom workflows to achieve their objectives. One primary advantage of the Metasploit Framework is a unified approach to solving this problem.

This arsenal demonstration will cover some of the latest improvements to the Metasploit Framework and showcase how these improvements maximize effectiveness while performing common tasks. Viewers will see the latest workflows for capturing credentials, UI optimizations for running modules, and demonstrations of Metasploit's new payload-less session types. Capturing credentials is an integral part of many penetration testing methodologies and, when combined with the Metasploit database, can be a powerful technique for users engaged in breaching simulations. The latest features streamline configuring all the services Metasploit has capture modules for and managing them as a single unit. Users will also learn about some of the latest improvements related to pivoting in Metasploit, which allow capturing services to be started on compromised hosts when combined.

</details>

<details><summary><strong>Vajra - Your Weapon To Cloud</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Raunak Parmar](https://img.shields.io/badge/Raunak%20Parmar-informational)

🔗 **Link:** [Vajra - Your Weapon To Cloud](https://github.com/shantanu561993/Vajra-1)  
📝 **Description:** Abstract:

Vajra (Your Weapon to Cloud) is a framework capable of validating the cloud security posture of the target environment. In Indian mythology, the word Vajra refers to the Weapon of God Indra (God of Thunder and Storms). Because it is cloud-connected, it is an ideal name for the tool.
Vajra supports multi-cloud environments and a variety of attack and enumeration strategies for both AWS and Azure. It features an intuitive web-based user interface built with the Python Flask module for a better user experience. The primary focus of this tool is to have different attacking and enumerating techniques all in one place with web UI interfaces so that it can be accessed anywhere by just hosting it on your server.


The following modules are currently available:

• Azure
- Attacking
1. OAuth Based Phishing (Illicit Consent Grant Attack)
- Exfiltrate Data
- Enumerate Environment
- Deploy Backdoors
- Send mails/Create Rules
2. Password Spray
3. Password Brute Force
- Enumeration
1. Users
2. Subdomain
3. Azure Ad
4. Azure Services
- Specific Service
1. Storage Accounts
• AWS
- Enumeration
1. IAM Enumeration
2. S3 Scanner
- Misconfiguration

</details>

<details><summary><strong>WhiskeySAML and Friends</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Tony Gore](https://img.shields.io/badge/Tony%20Gore-informational) ![Kam Talebzadeh](https://img.shields.io/badge/Kam%20Talebzadeh-informational) ![Nestori Syynimaa](https://img.shields.io/badge/Nestori%20Syynimaa-informational)

🔗 **Link:** Not Available  
📝 **Description:** Solorigate was one of the most significant cybersecurity attacks we have ever faced. One tactic used during the attack was to extract a token signing certificate from the on-prem Active Directory Federation Services (ADFS) server. With the certificate, adversaries were able to impersonate any user of the target organization and exfiltrate information. The technique used to extract the certificate required access to the target server.

Secureworks is constantly conducting primary research to find new vulnerabilities and techniques the adversaries may exploit. Based on this research, we are also conducting applied research to build proofs-of-concept and tools to demonstrate and automate the exploitations.

In this talk, we will introduce a new technique that allows extracting the signing certificate remotely without logging in on the target server. We'll cover the conceptual design of the new technique and walk through how it was developed and we will introduce/demonstrate three tools written in Python, which allows performing the whole attack remotely and automatically with a small input data set and the weaponization of the technique.

</details>

<details><summary><strong>Zuthaka: A Collaborative Free Open-Source Command & Controls (C2s) Integration Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Lucas Bonastre](https://img.shields.io/badge/Lucas%20Bonastre-informational) ![Alberto Herrera](https://img.shields.io/badge/Alberto%20Herrera-informational)

🔗 **Link:** Not Available  
📝 **Description:** A collaborative free open-source Command & Control development framework that allows developers to concentrate on the core function and goal of their C2.
Zuthaka presents a simplified API for fast and clear integration of C2s and provides a centralized management for multiple C2 instances through a unified interface for Red Team operations.
Zuthaka is more than just a collection of C2s, it is also a solid foundation that can be built upon and easily customized to meet the needs of the exercise that needs to be accomplished. This integration framework for C2 allows developers to concentrate on a unique target environment and not have to reinvent the wheel.
After we first presented Zuthakas' MVP at Black Hat USA 2021, we are now presenting the first release with a live demo lab to share the possibilities of integration and flexibility of Red Team infrastructure.

</details>

---
## Others
<details><summary><strong>Adhrit: Android Security Suite</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Abhishek JM](https://img.shields.io/badge/Abhishek%20JM-informational) ![Rahul Sani](https://img.shields.io/badge/Rahul%20Sani-informational) ![Amrudesh Balakrishnan](https://img.shields.io/badge/Amrudesh%20Balakrishnan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Adhrit is an open-source Android application security analysis suite. The tool is an effort to find an efficient solution to all the needs of mobile security testing and automation. Adhrit has been built with a focus on flexibility and modularization. It currently uses the Ghera benchmarks to identify vulnerable code patterns in the bytecode. Apart from bytecode scanning, Adhrit can also identify hardcoded secrets within Android applications. The tool also comes with a built-in integration to popular software like Jira and Slack which can be configured to automate and streamline.

</details>

<details><summary><strong>Hooke: A Sandbox Tool for both Android and iOS Apps</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Miao Liu](https://img.shields.io/badge/Miao%20Liu-informational) ![Xiangxing Qian](https://img.shields.io/badge/Xiangxing%20Qian-informational) ![Bo Zhang](https://img.shields.io/badge/Bo%20Zhang-informational) ![Fan Yao](https://img.shields.io/badge/Fan%20Yao-informational) ![Zhenyu Zhu](https://img.shields.io/badge/Zhenyu%20Zhu-informational) ![Yijie Zhao](https://img.shields.io/badge/Yijie%20Zhao-informational) ![Yi Zeng](https://img.shields.io/badge/Yi%20Zeng-informational)

🔗 **Link:** Not Available  
📝 **Description:** Mainstream mobile phone systems have implemented privacy features that allow users to keep an eye on how apps access their data, such as Privacy Dashboard for Android and App Privacy Report for iOS. However, while we delved into the implementation of these systems, we found that it was not as accurate and credible as expected. We developed our offline App privacy leak detection platform - Hooke, to identify privacy-sensitive behaviors much more clearly and directly.

For data access, we identified over 300 privacy-related APIs across 8 categories for both Android and iOS, and we constructed sandbox environments and added instrumentation to collect runtime information like parameters, stack traces and app status. For network behavior, we found a general solution to bypass ssl pinning, and tried to decrypt network traffic to prevent sensitive data escape. To facilitate locating privacy issues, our sandbox also recorded App runtime screens and timestamps during the test phase, which are associated directly with dynamic behaviors.

Our tool, Hooke, shows App behaviors in the aspect of privacy data access, network traffic and screen recordings, and we also implemented an intelligent rule engine to analyze this data. Finally, these three categories data are associated and presented in the form of a timeline, aiming to directly and easily locate an App's behavior throughout the app's lifecycle by dragging the timeline. With the help of Hooke, we found dozens of privacy leak issues hidden in malicious Apps and third-party SDKs.﻿

</details>

<details><summary><strong>The Dependency Combobulator</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Moshe Zioni](https://img.shields.io/badge/Moshe%20Zioni-informational)

🔗 **Link:** [The Dependency Combobulator](https://github.com/moshe-apiiro)  
📝 **Description:** The Dependency Combobulator is a modular and extensible framework to detect and prevent dependency confusion leakage and potential attacks. This facilitates a holistic approach for ensuring secure application releases that can be evaluated against different sources (e.g., GitHub, Artifactory) and many package management schemes (e.g., ndm, pip, maven).


The framework can be used by security auditors, and pentesters and even baked into an enterprise's application security program and release cycle in an automated fashion.

This major new release will include support for a new line of package schemes/artifact ingestion.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>Amini Project</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Salvador Mendoza](https://img.shields.io/badge/Salvador%20Mendoza-informational)

🔗 **Link:** [Amini Project](https://github.com/ryanbgriffiths/ICRA2024PaperList)  
📝 **Description:** The AirTag IoT device is a tracking tool developed by Apple and designed to help people find misplaced objects. However, even when Apple states that AirTag technology is solely used for tracking items, a growing number of malicious individuals are taking advantage for the simplicity to install it and set up to track unaware targets, in other words, people.

Amini is a specialized open-source hardware project to scan, detect, spoof, and play a sound for AirTag devices. This project is part of "Spy-wear: Misuse of Apple AirTags" research where we analyzed a privacy concern about AirTag misuse for tracking capabilities. It was designed to be implemented with Arduino environment, for flexible designs, and to be used in any Arduino-supported devices with BLE capabilities.

</details>

<details><summary><strong>Faceless - Deepfake detection</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Manh Pham](https://img.shields.io/badge/Manh%20Pham-informational)

🔗 **Link:** Not Available  
📝 **Description:** Faceless is a deepfake detection system.

The proposed deepfake detection model is based on the EfficientNet structure with some customizations. It is hoped that an approachable solution could remind Internet users to stay secure against fake contents and counter the emergence of deepfakes.
The deepfake dataset were used in the final model is Celeb-DF

</details>

<details><summary><strong>Ghostwriter</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Christopher Maddalena](https://img.shields.io/badge/Christopher%20Maddalena-informational)

🔗 **Link:** [Ghostwriter](https://github.com/chrismaddalena)  
📝 **Description:** Ghostwriter is a part of your team. It enables collaborative management of penetration test and red team assessments. It helps you manage the critical pieces of every project, including client information, project plans, infrastructure, findings, and reports in one application.

Since its debut at BHUSA Arsenal in 2019, Ghostwriter has grown and matured. Last year was a building year for the project. Now, the development team is excited to re-introduce Ghostwriter with new features to be rolled out in Q1 and Q2 2022 – such as a new GraphQL API! This new version gives teams the power to manage their projects via the API layer and custom scripts or integration with third-party projects.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>ArcherySec - Manage and Automate your Vulnerability Assessment</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational)

🔗 **Link:** [ArcherySec - Manage and Automate your Vulnerability Assessment](https://github.com/archerysec/archerysec)  
📝 **Description:** ArcherySec is an open-source vulnerability assessment and automation tool which helps developers and pentesters to perform scans and manage vulnerabilities. ArcherySec uses popular open-source tools to perform comprehensive scanning for web applications and networks. It also performs web application dynamic authenticated scanning and covers the whole application by using selenium. The developers can also utilize the tool for the implementation of their DevOps CI/CD environment.

Overview of the tool
- Perform web and network vulnerability scanning using open-source tools.
- Correlates and collaborates all raw scans data, shows them in a consolidated manner.
- Multi-user role-based accounts admin, analyst & viewer
- Policy-based CI/CD integration
- Perform authenticated web scanning.
- Perform web application scanning using selenium.
- Vulnerability management.
- Enable REST APIs for developers to perform scanning and vulnerability management.
- JIRA Ticketing System.
- Periodic scans.
- Useful for DevOps teams for vulnerability management.

</details>

<details><summary><strong>Automating Fuzzable Target Discovery with Static Analysis</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Alan Cao](https://img.shields.io/badge/Alan%20Cao-informational)

🔗 **Link:** Not Available  
📝 **Description:** Vulnerability researchers conducting security assessments on software will often harness the capabilities of coverage-guided fuzzing through powerful tools like AFL++ and libFuzzer. This is important as it automates the bughunting process and reveals exploitable conditions in targets quickly. However, when encountering large and complex codebases or closed-source binaries, researchers have to painstakingly dedicate time to manually audit and reverse engineer them to identify functions where fuzzing-based exploration can be useful.

Fuzzable is a framework that integrates both with C/C++ source code and binaries to assist vulnerability researchers in identifying function targets that are viable for fuzzing. This is done by applying several static analysis-based heuristics to pinpoint risky behaviors in the software and the functions that executes them. Researchers can then utilize the framework to generate basic harness templates, which can then be used to hunt for vulnerabilities, or to be integrated as part of a continuous fuzzing pipeline, such as Google's oss-fuzz.

In addition to running as a standalone tool, Fuzzable is also integrated as a plugin for Binary Ninja, with support for other disassembly backends being developed.

</details>

<details><summary><strong>CWE_Checker: Architecture-Independent Binary Vulnerability Analysis</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Nils-Edvin Enkelmann](https://img.shields.io/badge/Nils-Edvin%20Enkelmann-informational)

🔗 **Link:** Not Available  
📝 **Description:** Assessing the security of programs running on embedded devices is a difficult task. Source code is generally unavailable and both static and dynamic binary analysis tools often do not offer support for the many different hardware configurations found in embedded devices.

The cwe_checker is an open-source tool for finding bugs and vulnerabilities in binary executables without requiring source code access or any knowledge about the hardware. By using static analysis techniques built atop Ghidra P-Code it supports a wide range of CPU architectures including x86, ARM, MIPS and PowerPC. While its focus is the analysis of ELF binaries commonly found in Linux-based firmware, there exists experimental support for PE files and even bare-metal binaries.

The cwe_checker offers detection of over 16 different bug classes including Buffer Overflows (CWE-119), Use-After-Frees (CWE-416) and Null Dereferences (CWE-476). The tool is built in a modular fashion where each analysis can use its own bug detection technique ranging from simple heuristics to complex data flow analysis. Furthermore, each analysis has a set of configuration parameters that can be modified to adjust the analysis to specific usage scenarios. For example, you can add your own functions to the "Use of potentially dangerous function" check (CWE-676).

It is easy to integrate the cwe_checker into other tools and workflows using the alternative JSON output. For example, as a plugin into the Firmware Analysis and Comparison Tool (FACT) you can use it to hunt for vulnerabilities in large firmware data sets.

</details>

<details><summary><strong>GoGoGadget - Post Exploitation Utilities for Embedded Systems</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Sean Heath](https://img.shields.io/badge/Sean%20Heath-informational) ![Marc Bohler](https://img.shields.io/badge/Marc%20Bohler-informational) ![Dylan Harbaugh](https://img.shields.io/badge/Dylan%20Harbaugh-informational)

🔗 **Link:** Not Available  
📝 **Description:** GoGoGadget is a toolkit that provides useful command line utilities for embedded systems using a broad variety of processor architectures and operating systems. GoGoGadget is written in Go and cross-compiles to a static binary that runs on any of thirteen operating systems and supports thirteen processor architectures with all required libraries included.

</details>

<details><summary><strong>HazProne : Cloud Hacking</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Staford Titus S](https://img.shields.io/badge/Staford%20Titus%20S-informational) ![Devansh Patel](https://img.shields.io/badge/Devansh%20Patel-informational)

🔗 **Link:** Not Available  
📝 **Description:** HazProne is a Cloud Pentesting Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand aws resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!

</details>

<details><summary><strong>MI-X (Am I Exploitable?).</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Ofri Ouzan](https://img.shields.io/badge/Ofri%20Ouzan-informational) ![Yotam Perkal](https://img.shields.io/badge/Yotam%20Perkal-informational)

🔗 **Link:** Not Available  
📝 **Description:** ‘Am I Exploitable?’, is an open source tool aimed at effectively determining whether a local host or a running container image is truly vulnerable to a specific vulnerability by accounting for all factors which affect *actual* exploitability. The tool prints the logical steps it takes in order to reach a decision and can generate a flow chart depicting the complete logical flow.

The first critical step to address any security vulnerability is to verify whether or not your environment is affected. Even if a vulnerable package is installed on your system, this condition alone does not determine exploitability as several conditions must be in place in order for the vulnerability to be applicable (exploitable). For example, can the vulnerability only be exploited under a specific configuration or in a specific OS?.

Most conventional vulnerability scanners rely on package manager metadata in order to determine the installed components (and in which versions) and then cross reference this data with vulnerability advisories in order to determine what vulnerabilities affect the system. The problem with that is that often software may be deployed without a package manager. For example, software might be built from source and then added to an image or unzipped from a tarball to a specific location on the file system. In these cases, no package manager data is associated with the application, which can result in false negatives (a scanner will “miss” these vulnerabilities) and offer a false sense of security.

We aim to build a community of researchers that can improve the validation process of historically dangerous vulnerabilities, as well as newly discovered ones, so users and organizations will understand whether they are vulnerable or not, as well as which validation flow is used to reach that verdict, and what steps are necessary for remediation or mitigation.

</details>

<details><summary><strong>Patronus: Swiss Army Knife SAST Toolkit</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Akhil Mahendra](https://img.shields.io/badge/Akhil%20Mahendra-informational) ![Ashwin Shenoi](https://img.shields.io/badge/Ashwin%20Shenoi-informational) ![Akshansh Jaiswal](https://img.shields.io/badge/Akshansh%20Jaiswal-informational)

🔗 **Link:** Not Available  
📝 **Description:** Patronus is a fully dockerised and comprehensive config driven Security Framework which helps to detect security vulnerabilities in the Software Development Life Cycle of any application. The framework inculcates a highly automated approach for vulnerability identification and management. With Patronus's fully whitebox approach, the framework currently covers four major verticals; Secrets Scanning, Software Composition Analysis, Static Application Security Testing and Asset Inventory. Finding all these four verticals together is a very strenuous task in the industry as no other framework currently solves this like Patronus which provides a fully comprehensive dashboard containing all the four verticals in a single central platform, and this is something very unique to Patronus. Patronus automatically identifies the latest code commits and focuses on the major aspects of the application source code to identify and detect key and high severity vulnerabilities within the application and aims for minimal false positives in the reports.

The framework focuses on the needs of the security engineers and the developers alike with a dedicated web dashboard to abstract all the nitty gritty technicalities of the security vulnerabilities detected and also empowers the user with higher level of vulnerability tracking for better patch management. The dashboard is built completely with analytics, functionality and maintaining ease in mind to demonstrate and display various metrics for the scans and vulnerabilities. It also helps to search, analyze and resolve vulnerabilities on-the-go and provides a completely consolidated vulnerability report.

Patronus is very powerful and hugely reduces the time and efforts of the security team in thoroughly reviewing any application from a security lens. The framework comes with an on-demand scanning feature apart from the scheduled daily automated scans, using which developers and security engineers can scan particular branches and repositories at any point of time in the SDLC, directly from the dashboard or integrations like Slack. The framework is completely adaptable and various software like Slack and Jira can be easily integrated directly with Patronus for better accessibility and tracking since most organizations today use these extensively.

</details>

<details><summary><strong>SimpleRisk</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

🔗 **Link:** [SimpleRisk](https://github.com/aparsons/simplerisk)  
📝 **Description:** As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform organizational Governance, Risk Management, and Compliance activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to manage control frameworks, policies, and exceptions, facilitate audits, and perform risk prioritization and mitigation activities. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

</details>

<details><summary><strong>Unleash Purple Knight: Fend Off Invaders Lurking in Your Active Directory</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Ran Harel](https://img.shields.io/badge/Ran%20Harel-informational)

🔗 **Link:** Not Available  
📝 **Description:** Purple Knight is a free Active Directory (AD) and Azure AD security assessment tool developed by Semperis identity security experts that has been downloaded by 5,000+ users since its first release in spring 2021. Purple Knight runs as a standalone utility that queries the AD environment and performs a set of tests against many aspects of AD's security posture, including AD Delegation, account security, AD Infrastructure security, Group Policy security, and Kerberos security. The tool scans for indicators of exposure (IOEs) and indicators of compromise (IOCs). Each security indicator is mapped to security frameworks such as MITRE ATT&CK and the French National Agency for the Security of Information Systems (ANSII).

Purple Knight produces a report that includes an overall score, scores in individual categories, and prioritized guidance from identity security experts that serves as a roadmap for improving overall security posture. The report includes an explanation of what aspects of the indicator were evaluated and the likelihood that the exposure will compromise AD.

Purple Knight is continuously updated to address new security indicators based on original research and in response to emerging threats. As an example, the Purple Knight team released indicators for the Windows Print Spooler service and PetitPotam flaws within days after their discovery. New updates to be demonstrated at Arsenal include:
• Newest in the 100+ indicators of exposure (IOEs) and indicators of compromise (IOCs)
• New Azure Active Directory security indicators
• Post-breach forensics capabilities that enable incident response teams to specify an attack window to accelerate remediation

Purple Knight continuously evolves through feedback from an engaged community of users on the Purple Knight Slack channel and through individual outreach to users who communicate directly with the product teams.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>CANalyse (2.0): A vehicle network analysis and attack tool.</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Kartheek Lade](https://img.shields.io/badge/Kartheek%20Lade-informational) ![Rahul J](https://img.shields.io/badge/Rahul%20J-informational)

🔗 **Link:** [CANalyse (2.0): A vehicle network analysis and attack tool.](https://github.com/canalyse/CANalyse-2.0)  
📝 **Description:** A prerequisite to using telegram option of this tool is that the Hardware implant is already installed in the car and capable of communicating with the Network inside the vehicle. Also, the library requiremnt are satisfied.

Let's assume we have a car in which we have connected with USBtin(or user choice) which is connected to Raspberry pi (or any linux machine of userchoice) and the pi can communicate on the internet.
LInk to USBtin - https://www.fischl.de/usbtin/

What is CANalyse?

Canalyse uses python-can library to sniff vehicle network packets and analyze the gathered information and uses the analyzed information to command & control certain functions of the car.

CANalyse is a software tool built to analyze the log files in a creative powerful way to find out unique data sets automatically and able to connect to simple interfaces such as Telegram. Basically, while using this tool you can provide your bot-ID and be able to use the tool over the internet through telegram.

canalyse can be installed inside a raspberry-PI, it is made to analyse log files in a creative way and also made to exploit the vehicle through a telegram bot by recording and analyzing the data logs.

</details>

<details><summary><strong>EMBA – Open-Source Firmware Security Testing</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michael Messner](https://img.shields.io/badge/Michael%20Messner-informational) ![Pascal Eckmann](https://img.shields.io/badge/Pascal%20Eckmann-informational)

🔗 **Link:** [EMBA – Open-Source Firmware Security Testing](https://github.com/e-m-b-a/emba/blob/master/emba)  
📝 **Description:** IoT (Internet of Things) and OT (Operational Technology) are the current buzzwords for networked devices on which our modern society is based on. In this area, the used operating systems are summarized with the term firmware. The devices themselves, also called embedded devices, are essential in the private and industrial environments as well as in the so-called critical infrastructure.
Penetration testing of these systems is quite complex as we have to deal with different architectures, optimized operating systems and special protocols. EMBA is an open-source firmware analyzer with the goal to simplify and optimize the complex task of firmware security analysis. EMBA supports the penetration tester with the automated detection of 1-day vulnerabilities on binary level. This goes far beyond the plain CVE detection: With EMBA you always know which public exploits are available for the target firmware. Besides the detection of already known vulnerabilities, EMBA also supports the tester on the next 0-day. For this, EMBA identifies critical binary functions, protection mechanisms and services with network behavior on a binary level. There are many other features built into EMBA, such as fully automated firmware extraction, finding file system vulnerabilities, hard-coded credentials, and more.

EMBA is the open-source firmware scanner, created by penetration testers for penetration testers.

</details>

<details><summary><strong>FACT 4.0</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Johannes vom Dorp](https://img.shields.io/badge/Johannes%20vom%20Dorp-informational)

🔗 **Link:** [FACT 4.0](https://github.com/Jianqiuer/Awesome6DPoseEstimation)  
📝 **Description:** Analyzing Firmware specifically to identify potential vulnerabilities is a common activity for security analysts, pentesters, researchers or engineers concerned with embedded devices such as in IoT. FACT offers an automated and usable platform to gain an immediate overview of potential vulnerabilities based on the firmware of a device and supercharges the process of finding deep vulnerabilities.

For this FACT automatically breaks down a firmware into its components, analyzes all components and summarizes the results. The analysis can then be perused in the desired amount of detail using either the responsive web application or a REST API.

The offered analyses include a list of included software and libraries, a matching of said software to CVE databases, identification of hard-coded credentials, private key material and weak configuration among others. FACT also applies source and binary code analysis to identify (possibly exploitable) bugs in the components and offers a large amount of meta data for further manual analysis.

A focus of recent development has been to offer more information regarding interdependencies between firmware components to ease the identification of data flow inside a firmware. This allows quickly grading the risk involved with uncovered vulnerabilities or configuration flaws by finding possible attack vectors concerning given component.

Finally, FACT offers multiple ways to collect and fuse analysis results, such as firmware comparison, advanced search options including regular expression on binary components and an integrated statistics module.

</details>

<details><summary><strong>IR(Inreared) BadUSB attack</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michihiro Imaoka](https://img.shields.io/badge/Michihiro%20Imaoka-informational)

🔗 **Link:** Not Available  
📝 **Description:** Conventional BadUSB executes a pre-programmed key sequence upon insertion.
This lecture reports a new vulnerability that arises from the addition of an IR receiver element to the traditional BadUSB, such as the IR Infrared Receiver TL1838 VS1838B 1838 38Khz.
The addition of this element allows an external operator to execute key sequences at arbitrary times. Multiple pre-programmed key sequences can be selected at will by external operation.

</details>

<details><summary><strong>RF( Radio Frequency ) Offensive and Defense Exercise Server</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michihiro Imaoka](https://img.shields.io/badge/Michihiro%20Imaoka-informational)

🔗 **Link:** Not Available  
📝 **Description:** We believe that cyber security should not only cover the Internet space but also the RF (radio frequency) space.
In the radio space, interception, decryption, tampering, jamming, and spoofing are actively practiced against hostile countries.　For example, the Russian Красуха-4 is a well-known electronic warfare weapon.
In fact, it has a longer history than the Internet, and there is much to learn from it.
However, there are not so many RF training environments that can be easily used.

</details>

<details><summary><strong>Wiretapping Tool to Sniff Packets Directly from LAN Cables</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michihiro Imaoka](https://img.shields.io/badge/Michihiro%20Imaoka-informational)

🔗 **Link:** Not Available  
📝 **Description:** Wiretapping tool to sniff packets directly from LAN cables

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>CASPR - Code Trust Audit Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ajit Hatti](https://img.shields.io/badge/Ajit%20Hatti-informational)

🔗 **Link:** Not Available  
📝 **Description:** With CASPR, we are addressing the Supply Chain Attacks by Left Shifting the code signing process.
CASPR aims to provide simple scripts and services architecture to ensure all code changes in an organization are signed by trusted keys; trustability of these keys should be instantly verifiable every time the code changes are consumed. It also makes the auditing and accountability of code-changes easier and cryptographically verifiable, leaving no scope for malicious actors to sneak in untrusted code at any point in the Software Development Life Cycle.

</details>

<details><summary><strong>CrowdSec - The Network Effect of Cybersecurity</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Philippe Humeau](https://img.shields.io/badge/Philippe%20Humeau-informational) ![Jean Devaux](https://img.shields.io/badge/Jean%20Devaux-informational)

🔗 **Link:** Not Available  
📝 **Description:** Discover CrowdSec, an open-source and collaborative intrusion prevention and detection system relying on IP behavior analysis and IP reputation. CrowdSec analyzes visitor behavior & provides an adapted response to all kinds of attacks. The solution also enables users to protect each other. Each time an IP is blocked, all community members are informed, so they can also block it. Already used in 160+ countries, the solution builds a crowd-sourced CTI database to secure individuals, companies, institutions etc.﻿

</details>

<details><summary><strong>Detecting Linux Kernel Rootkits with Tracee</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yaniv Agman](https://img.shields.io/badge/Yaniv%20Agman-informational) ![Ziv Karliner](https://img.shields.io/badge/Ziv%20Karliner-informational) ![Asaf Eitani](https://img.shields.io/badge/Asaf%20Eitani-informational) ![Alon Zivony](https://img.shields.io/badge/Alon%20Zivony-informational)

🔗 **Link:** Not Available  
📝 **Description:** Linux Kernel Rootkits is an advanced and fascinating topic in cyber security. These tools are stealthy and evasive by design and often target the lower levels of the OS, unfortunately there aren't many solid security tools that can provide an extensive visibility to detect these kinds of tools.
Tracee is a Runtime Security and forensics tool for Linux, utilizing eBPF technology to trace systems and applications at runtime, analyze collected events to detect suspicious behavioral patterns, and capture forensics artifacts.

Tracee was presented in BH EU 2020 and BH USA 2021. Thus far we have presented Tracee-ebpf and spoke about its passive capabilities to collect OS events based on given filters, and Tracee-rules, which is the runtime security detection engine. But Tracee has another capability to safely interact with the Linux kernel, which grants Tracee even more superpowers.

Tracee was designed to provide observability on events in running containers. It was released in 2019 as an OSS project, allowing practitioners and researchers to benefit from its capabilities. Now, Tracee has greatly evolved, adding more robust and advanced capabilities. Tracee is a runtime security and forensics tool for Linux, built to address common Linux security issues.

For references see:
https://blog.aquasec.com/ebpf-container-tracing-malware-detection
https://blog.aquasec.com/advanced-persistent-threat-techniques-container-attacks

</details>

<details><summary><strong>Detecting Typo-Squatting, Backdoored, Abandoned, and Other "Risky" Open-Source Packages Using Packj</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ashish Bijlani](https://img.shields.io/badge/Ashish%20Bijlani-informational)

🔗 **Link:** [Detecting Typo-Squatting, Backdoored, Abandoned, and Other "Risky" Open-Source Packages Using Packj](https://github.com/ossillate-inc/packj)  
📝 **Description:** Software supply chain attacks on open-source software ecosystems, particularly on popular package managers such as NPM, PyPI have increased tremendously in the last few years. Today, developers must thoroughly analyze packages, and avoid risky packages that may expose them to high levels of supply chain risks.

But, there exists no tool to measure supply chain risks lurking in open-source packages. Current practices include sourcing only mature, stable, popular, and reputable packages, where such attributes are inferred from publicly available metrics, such as GitHub stars, package downloads, and software development activity. However, such vanity metrics do not reveal true information about the security posture of packages. More importantly, an attacker-controlled bot can easily manipulate such metrics. Manually vetting hundreds of dependencies is infeasible.

In this talk, we will present our open-source command line vetting tool, called Packj that allows developers to easily analyze dependencies for "risky" code/attributes and provide actionable insights into their security posture. In this presentation, we will cover the technical details of our tool and discuss its usage. Packj tool powers also our large-scale security vetting infrastructure that continuously analyzes millions of published packages, and provides detailed risk assessment reports. We have already detected a number of abandoned, typo-squatting, and malicious packages. We will present our findings, highlight different types of attack techniques adopted by bad actors, and discuss measures that developers can take to thwart such attacks. With our work, we hope to enhance productivity of the developer community by exposing undesired behavior in untrusted third-party code, maintaining developer trust and reputation, and enforcing security of package managers.

</details>

<details><summary><strong>DotDumper: Automatically Unpacking DotNet Based Malware</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Max Kersten](https://img.shields.io/badge/Max%20Kersten-informational)

🔗 **Link:** Not Available  
📝 **Description:** Analysts at corporations of any size face an ever-increasing amount of DotNet based malware. The malware comes in all shapes and forms, ranging from skiddish stealers all the way to nation state backed targeted malware. The underground market, along with public open-source tools, provide a plethora of ways to obfuscate and pack the malware. Unpacking malware is time consuming, difficult, and tedious, which poses a problem.

To counter this, DotDumper automatically dumps interesting artifacts during the malware's execution, ranging from base64 decoded values to decrypted PE files. As such, the malware decrypts and executes the next stage, while DotDumper conveniently provides a copy of said decrypted stage. All this is done via a simple, compact, intuitive, and easy-to-use command-line interface.

Aside from the dumped artifacts, DotDumper provides an extensive log of the traced execution, based on managed hooks. For each hook, the log contains the original function name, arguments and their values, and the return value. Since DotDumper ensures that the original function is called, the malware's execution continues as if it was executed normally, allowing the analyst to get as many stages from the sample as possible.

DotDumper can execute DotNet Framework executables, as well as dynamic link libraries, due to the fully-fledged reflective loader which is embedded. Any given function can be selected within a library, along with any required variables and their values, all easily accessible from DotDumper's command-line interface.

DotDumper has proven to be effective in dealing with the renowned AgentTesla stealer or the WhisperGate Wiper loader, allowing an analyst to easily fetch the decrypted and unpacked in-memory only stages, thus decreasing up the time spent on unpacking, allowing for faster response to the given threat.

</details>

<details><summary><strong>In0ri: Open Source Defacement Detection With Deep Learning</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Trung Nguyen Hoang](https://img.shields.io/badge/Trung%20Nguyen%20Hoang-informational) ![Tieu Dong Duong](https://img.shields.io/badge/Tieu%20Dong%20Duong-informational)

🔗 **Link:** Not Available  
📝 **Description:** In0ri is the first open source system for detecting defacement attacks by utilizing image-classification convolutional neural network. In this presentation, we will be demonstrating the process of setting up In0ri and have it detect defacement attacks. And optionally the process of training the machine learning model. We will also be explaining the reason behind In0ri's high accuracy when classifying defacement attacks.

</details>

<details><summary><strong>LATMA - lateral movement analyzer</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Gal Sadeh](https://img.shields.io/badge/Gal%20Sadeh-informational) ![Dor Segal](https://img.shields.io/badge/Dor%20Segal-informational)

🔗 **Link:** Not Available  
📝 **Description:** LATMA is a tool for offline detection and investigation of lateral movement attack based on AD event logs. The tool assists security teams to overcome the main challenges:

Data collection and preparation: in theory, event logs are an available data source to look for authentication anomalies. In practice, however, the source and destination machines are not represented in the same manner (hostname vs. IP), which prevents the ability to directly detect movement of a user account across different machines. LATMA conforms the representation of the source and destination machines, making the even log ready for analysis which is the tool's primary objectives.

Data analysis: LATMA scans the even data, looking for authentication patterns we have learned to be associated with lateral movement. For example, a chain of authentications where a single account logs from machine A to machine B and consecutively from machine B to C. Another example is what we call White-Cane in which an account logs from a single source to multiple destinations one after the other. The patterns LATMA searches for are based on our analysis of attacks in the wild, as well as on novel detection algorithm we have developed.

LATMA can be used in any environment where Kerberos and NTLM auditing is enabled, making it an easy and useful tool to any security professionals that handle an Active Directory environment. Offline analysis of authentications, while not real-time, is an efficient method to hunt for active lateral movement that goes under the radar and can provide the means to contain it before it reaches its objectives.

</details>

<details><summary><strong>N3XT G3N WAF: ML based WAF with Retraining and Detainment through Honeypots</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Pengfei Yu](https://img.shields.io/badge/Pengfei%20Yu-informational) ![Bosen Zhang](https://img.shields.io/badge/Bosen%20Zhang-informational) ![Matthew Ng](https://img.shields.io/badge/Matthew%20Ng-informational) ![Elizabeth Lim](https://img.shields.io/badge/Elizabeth%20Lim-informational)

🔗 **Link:** Not Available  
📝 **Description:** With the explosive growth of web applications since the early 2000s, web-based attacks have progressively become more rampant. One common solution is the Web Application Firewall (WAF). However, tweaking rules of current WAFs to improve the detection mechanisms can be complex and difficult.

NGWAF seeks to address the drawback method mentioned earlier with a novel machine learning and honeypot based architecture.

Firstly, we replace the traditional rulesets with deep learning models to reduce the complexity of managing and updating those rules. Instead of manually identifying rules, we use machine learning to automate the process of learning patterns from previous malicious data. In addition, we include a system model maintenance where we monitor the performance of the model and regularly retrain the model with new malicious data collected. A detection mechanism based on a fully automated machine learning pipeline will greatly reduce the manpower required and potential for error involved in WAF maintenance.

Malicious data detected will then be redirected into our novel system: an interactive, honeypotted, quarantine environment built to isolate potential hostile attackers and act as a sinkhole to gather current attack methods. Unlike conventional WAFs that just drop or block malicious attempts, NGWAF traps and diverts the threat actors to emulated systems to soften the impact of their malicious actions. By detaining the attacker to a series of scalable honeypotted environments, we are able to observe and collect their out-in-the-wild malicious data for future improvements to the detection mechanism. These data are automatically scrubbed and can be batched to be retrained into our detection model.

NGWAF is scalable and can be easily deployed either natively or in a cloud environment.

</details>

<details><summary><strong>Objective-See's Mac Security Tools</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [Objective-See's Mac Security Tools](https://github.com/objective-see/FileMonitor)  
📝 **Description:** Objective-See's security tools are free, open-source, and provide a myriad of ways to protect macOS systems from hackers, malware, or even commercial applications that behave poorly!

In this demo, will cover our most popular tools including, LuLu, OverSight, BlockBlock and more.

We'll also highlight various command-line tools (that leverage Apple's new Endpoint Security Framework) designed to facilitate both malware analysis and macOS spelunking.

</details>

<details><summary><strong>Ox4Shell - Deobfuscate Log4Shell payloads with ease</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Daniel Abeles](https://img.shields.io/badge/Daniel%20Abeles-informational) ![Ron Vider](https://img.shields.io/badge/Ron%20Vider-informational)

🔗 **Link:** [Ox4Shell - Deobfuscate Log4Shell payloads with ease](https://github.com/ox-eye/Ox4Shell)  
📝 **Description:** Since the release of the Log4Shell vulnerability (CVE-2021-44228), many tools were created to obfuscate Log4Shell payloads, making the lives of security engineers a nightmare.

Threat actors tend to apply obfuscation techniques to their payloads for several reasons. Most security protection tools, such as web application firewalls (WAFs), rely on rules to match malicious patterns. By using obfuscated payloads, threat actors are able to circumvent the rules logic and bypass security measures. Moreover, obfuscated payloads increase analysis complexity and, depending upon the degree of obfuscation, can also prevent them from being reverse-engineered.

Decoding and analyzing obfuscated payloads is time-consuming and often results in inaccurate data. However, doing so is crucial for understanding attackers' intentions.

We believe that security teams around the world can benefit from using Ox4Shell to dramatically reduce their analysis time. To help the security community, we have decided to release Ox4Shell - a payload deobfuscation tool that would make your life much easier.

</details>

<details><summary><strong>Protecting your Crypto Asset against Malicious JS Phishing</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jordan Garzon](https://img.shields.io/badge/Jordan%20Garzon-informational) ![Asaf Nadler](https://img.shields.io/badge/Asaf%20Nadler-informational)

🔗 **Link:** Not Available  
📝 **Description:** Cryptocurrencies and NFT are taking over with predictions of 90% of the population holding at least one of them by the end of the decade. Users that want to facilitate these new assets, trade them and sell them typically do that using wallets, and in particular hot wallets that are easy-to-use. The most popular hot wallets today (e.g., MetaMask) are browser based and are thus vulnerable to phishing and scams made possible through malicious JavaScript, such as a recent campaign carried out by the Lazarus group which resulted in more than 400M$ worth of stolen cryptocurrencies.

We release our internal tool used by the Security Operation and the research at Akamai to scan the JS from any website.
It includes a Python recursive crawler that extracts every JS from any domain (written within the HTML or imported), analyzes it with a model and heuristics - that we provide -, and brings metadata ( from VT, publicwww…) It finally gives a score to every piece of code running on any URL of a specified domain.
The code works also as a Web App and exposes a REST API as well.

We will finish by presenting some real detection we caught with this tool and explaining them.

</details>

<details><summary><strong>Sandbox Scryer</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Greg Dalcher](https://img.shields.io/badge/Greg%20Dalcher-informational) ![Joel Spurlock](https://img.shields.io/badge/Joel%20Spurlock-informational)

🔗 **Link:** Not Available  
📝 **Description:** "Sandbox Scryer: An open source tool leveraging free sandbox technologies to enable threat hunting and intelligence"

When defending against APTs or Advanced Persistent Threats, persistent is the most important aspect of that definition. Often a security solution will stop a threat actor on initial access, when they inject command and control beacons into processes, or when they move laterally. Which leads to important questions. What's next? Will the actor try again? What are they after? How do I improve my defenses when the threat actor inevitably tries again?

A defender must be able to answer these questions. SoC analyst time is among the most valuable in any organization, and automated research tools such as sandboxes can be a valuable solution to accelerate this process. Unfortunately, making sense of all the data takes time. Indicators of Compromise (IOCs) are invaluable for communicating actionable intelligence about attacks, as is identifying relevant secondary payloads and top ATT&CK tactics and techniques among all the data a sandbox can generate. This critical information can be used to drive threat hunting, assessment of attack success and penetration, and pre-emptive identification of risk of future attack.

In this demonstration, we will showcase an open source tool, the Sandbox Scryer, which performs sample submission to the free Hybrid Analysis Sandbox, retrieval of results of the Sandbox's automated analysis, and extraction from these sets of important IOCs and techniques matched against MITRE Att&ck. This open source tool will be made available, which enables an organization to adapt it to their favorite free or paid sandbox (of which there are many), along with expanding it to produce of types of IOCs.

</details>

<details><summary><strong>Sandboxing in Linux with zero lines of code</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ignat Korchagin](https://img.shields.io/badge/Ignat%20Korchagin-informational)

🔗 **Link:** [Sandboxing in Linux with zero lines of code](https://github.com/xairy/usb-hacking)  
📝 **Description:** Linux seccomp is a simple, yet powerful tool to sandbox running processes and significantly decrease potential damage in case the application code gets exploited. It provides fine-grained controls for the process to declare what it can and can't do in advance and in most cases has zero performance overhead.

The only disadvantage: to utilize this framework, application developers have to explicitly add sandboxing code to their projects and developers usually either delay this or omit completely as their main focus is mostly on the functionality of the code rather than security. Moreover, the seccomp security model is based around system calls, but many developers, writing their code in high-level programming languages and frameworks, either have little knowledge to no experience with syscalls or just don't have easy-to-use seccomp abstractions or libraries for their frameworks.

All this makes seccomp not widely adopted—but what if there was a way to easily sandbox any application in any programming language without writing a single line of code? This presentation discusses potential approaches with their pros and cons.

</details>

<details><summary><strong>Siembol: An Open-Source Real-Time SIEM Tool Based on Big Data Technologies</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Marian Novotny](https://img.shields.io/badge/Marian%20Novotny-informational) ![Yassin Raman](https://img.shields.io/badge/Yassin%20Raman-informational)

🔗 **Link:** [Siembol: An Open-Source Real-Time SIEM Tool Based on Big Data Technologies](https://github.com/G-Research/siembol/discussions/749)  
📝 **Description:** Siembol is an in-house developed security data processing application, forming the core of an internal Security Data Platform.

Following the experience of using Splunk, and as early adopters of Apache Metron, the team needed a highly efficient, real-time event processing engine with fewer limitations and more enhanced features. With Metron now retired, Siembol hopes to give the community an evolved alternative.

Siembol improvements over Metron:
- Components for real-time alert escalation: CSIRT teams can easily create a rule-based alert from a single data source, or they can create advanced correlation rules that combine various data sources. Moreover, Siembol UI supports importing a Sigma rule into Siembol alerting.
- Ability to integrate with other systems using dedicated components and plugin architecture for easy integration with incident response tools
- Advanced parsing framework for building fault-tolerant parsers
- Enhanced enrichment component allowing for defining rules and joining enrichment tables
- Configurations and rules are defined by a modern Angular web application, with a git-based approval process
- Supports OAuth2/OIDC for authentication and authorization in Siembol UI
- Easy installation for use with prepared docker images, helm charts and quick start guide

Siembol Use Cases:
- SIEM log collection using open-source technologies
- Detection tool for discovery of leaks and attacks on infrastructure
- Real-time stream Sigma rule evaluation without the need to index logs

</details>

<details><summary><strong>Slips: Free Software Machine Learning Tool for Network Intrusion Prevention System</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Alya Gomaa](https://img.shields.io/badge/Alya%20Gomaa-informational) ![Sebastian Garcia](https://img.shields.io/badge/Sebastian%20Garcia-informational) ![Kamila Babayeva](https://img.shields.io/badge/Kamila%20Babayeva-informational)

🔗 **Link:** [Slips: Free Software Machine Learning Tool for Network Intrusion Prevention System](https://github.com/stratosphereips/StratosphereLinuxIPS)  
📝 **Description:** Slips is a behavioral-based intrusion prevention system, and the first free software to use machine learning to detect attacks in the network. It is a modular system that profiles the behavior of IP addresses and performs detections in time windows.
Slips' modules detect a range of attacks both to and from the protected devices.
Slips connects to other Slips using P2P, and exports alerts to other systems.

Slips works in several directionality modes. The user can choose to detect attacks coming *to* or going *from* these profiles. This makes it easy to protect your network but also to focus on infected computers inside your network.

Slips includes the download/management of external Threat Intelligence feeds (now working with 44 external feeds, including our own), whois/asn/geocountry/mac vendor enrichment, a LSTM neural net for malicious behavior detection, port scans, ICMP scans, long connection detection, data upload, malicious JA3/SSL certificate matching, leak detection and many more.
Ensembling algorithms are used for blocking decisions.
The P2P module connects to other Slips to share alerts.

Slips can read packets from an interface, PCAPs, Suricata, Zeek, Argus and Nfdump, and can output alerts files. Having Zeek as a base tool, Slips can correctly build a sorted timeline of flows combining all Zeek logs. Slips can send alerts using the STIX/TAXII protocol, to CESNET servers using IDEA0 format or to Slack.

The Kalipso Node.js interface allows the analysts to see the profiles' behaviors and detections performed by Slips modules directly in the console. Kalipso displays the flows of each profile and time window and compares those connections in charts/bars. It also summarizes the whois/asn/geocountry information for each IP in your traffic. Kalipso is being migrated to a web console.

</details>

<details><summary><strong>stegoWiper: A powerful and flexible active attack for disrupting stegomalware</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Alfonso Munoz](https://img.shields.io/badge/Alfonso%20Munoz-informational) ![Manuel Urueña](https://img.shields.io/badge/Manuel%20Urueña-informational)

🔗 **Link:** [stegoWiper: A powerful and flexible active attack for disrupting stegomalware](https://github.com/mindcrypt/stegowiper)  
📝 **Description:** Over the last 10 years, many threat groups have employed stegomalware or other steganography-based techniques to attack organizations from all sectors and in all regions of the world. Some examples are: APT15/Vixen Panda, APT23/Tropic Trooper, APT29/Cozy Bear, APT32/OceanLotus, APT34/OilRig, APT37/ScarCruft, APT38/Lazarus Group, Duqu Group, Turla, Vawtrack, Powload, Lokibot, Ursnif, IceID, etc.
Our research shows that most groups are employing very simple techniques (at least from an academic perspective) and known tools to circumvent perimeter defenses, although more advanced groups are also using steganography to hide C&C communication and data exfiltration. We argue that this lack of sophistication is not due to the lack of knowledge in steganography (some APTs have already experimented with advanced algorithms) but simply because organizations are not able to defend themselves, even against the simplest steganography techniques.
During the demonstration we will show the practical limitations of applying existing automated steganalysis techniques for companies that want to prevent infections or information theft by these threat actors.
For this reason, we have created stegoWiper, a tool to blindly disrupt any image-based stegomalware, attacking the weakest point of all steganography algorithms: their robustness. We'll show that it is capable of disrupting all steganography techniques and tools (Invoke-PSImage, F5, Steghide, openstego, ...) employed nowadays, as well as the most advanced algorithms available in the academic literature, based on matrix encryption, wet-papers, etc. (e.g. Hill, J-Uniward, Hugo). In fact, the more sophisticated a steganography technique is, the more disruption stegoWiper produces.
Moreover, our active attack allows us to disrupt any steganography payload from all the images exchanged by an organization by means of a web proxy ICAP (Internet Content Adaptation Protocol) service, in real time and without having to identify which images contain hidden data first.

</details>

<details><summary><strong>Stop Wasting Time: Use Falco Plugins to Extend Detection with any Event Stream</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Stefano Chierici](https://img.shields.io/badge/Stefano%20Chierici-informational) ![Alberto Pellitteri](https://img.shields.io/badge/Alberto%20Pellitteri-informational)

🔗 **Link:** Not Available  
📝 **Description:** Data leaks can cost companies a fortune, storing millions of logs which "might" come in handy in the future. The majority of the time, only a small portion of those logs are actually useful in the event of a security investigation. Using newly developed Falco plugins, you can generate live events for the point in time you are interested in and forward those for further analysis, speeding and simplifying incident response.

Falco is a CNCF open source container security tool designed to detect anomalous activity in your local machine, containers, and Kubernetes clusters. It taps into Linux kernel system calls and Kubernetes Audit logs to generate an event stream of all system activity. Thanks to its powerful and flexible rules language, Falco will generate security events when it finds malicious behaviors as defined by a customizable set of Falco rules.

The recent major Falco update introduced support of Falco Plugins, opening Falco to a new world of data that Falco can handle and process. This new approach allows users to create and integrate different types of Falco plugins and extend the Falco detection engine with new event sources and generate security events using Falco rules. The event sources that can be integrated in Falco are infinited. AWS CloudTrail, Docker, and Video Stream are already available, and the Falco community is already working on new plugins to integrate new event sources.

During this talk, we show the new Falco plugins approach and how you can use it in real breaches. The recent OKTA breach is a perfect example. By developing the related plugin and Falco rules for OKTA events, it was possible to detect and get an immediate alert if something anomalous happened in your environment.

</details>

<details><summary><strong>Streamlining and Automating Threat Hunting With Kestrel</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Xiaokui Shu](https://img.shields.io/badge/Xiaokui%20Shu-informational) ![Paul Coccoli](https://img.shields.io/badge/Paul%20Coccoli-informational) ![Ian Molloy](https://img.shields.io/badge/Ian%20Molloy-informational) ![Jiyong Jang](https://img.shields.io/badge/Jiyong%20Jang-informational)

🔗 **Link:** Not Available  
📝 **Description:** Kestrel is a rapidly evolving threat hunting language designed to accelerate cyber threat hunting by providing a layer of abstraction to build reusable, composable, and shareable hunt-flow. It brings two key innovations to the security community: (i) a composable way expressing threat hypothesis development over entity-relational data abstractions, and (ii) an open-source language runtime generating and executing repetitive hunt instructions on local hunting sites, remote data sources, and in the cloud. Kestrel significantly simplifies hunting and sharing by creating a standard way to encode a single hunt step, chain multiple hunt steps, and fork/merge hunt-flows to develop threat hypothesis. It focuses threat hunters on the reusable business logic of hunt, other than writing multiple endpoint query languages, understanding incompatible query results, and converting analytics and visualization for each specific hunt.

This arsenal session will showcase the latest language development and community opportunities for Kestrel. We will start with powerful federated data retrieval using the Structured Threat Information eXpression (STIX) standard and STIX-shifter and lift the results into an entity-relational data model. Then we will showcase analytic hunt steps besides data retrieval steps, compare the new Python analytics interface with the container-based interface, and execute analytics for context enrichment, de-obfuscation, and visualization. After creating, executing, saving, and re-executing huntbooks, we will connect Kestrel with the Open Command and Control (OpenC2) standard to respond to "investigate" commands and automate huntbook execution, data gathering, false positive elimination, and comprehensive analysis.

Making it ready to try by the audience, we will demonstrate live hunts in Jupyter Notebooks launched and executed in a Binder cloud sandbox as part of a purple team exercise. At the end of the session, we will introduce the kestrel-huntbook repo for people to reuse existing huntbooks and share their hunting knowledge with their colleagues and other hunters in the community.

</details>

<details><summary><strong>SubParse - Malware Artifact and Correlation Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Josh Stroschein](https://img.shields.io/badge/Josh%20Stroschein-informational)

🔗 **Link:** [SubParse - Malware Artifact and Correlation Framework](https://github.com/jstrosch/subparse)  
📝 **Description:** SubParse is a modular framework designed for the automation of malware analysis using static and dynamic analysis, external threat intelligence sources and historical data/event correlation. The novelty of this approach comes in the correlation of extracted data to not only assist in identification of current samples, but also in correlating any facet of information with other samples stored within the framework. Data will be accessible through an intuitive web-based user interface which offers a comprehensive filter syntax sub-system.

Static file identification and parsing is the entry point into the framework. Currently, the scope of the framework is to support Windows-based portable executable (PE) files and Linux executables (ELF). However, the modularity of the framework allows for the easy integration of additional file parsers through plugins. Static file characteristics can be extracted using file format parsing, such as: file hashes, compile time, version information, code entry address, and section information. Across a larger sample set these attributes can offer unique views into threat actor operations and allow for the correlation of previously uncorrelated samples.

Analysis can be further enriched using enricher plugins. After completion of the static file parsing, the framework looks for any enabled enrichers. Enrichers provide an open-ended opportunity to gather additional data about the sample and add it to the framework. For example, an enricher that utilizes services provided by Abuse.ch can provide additional insight into malware behavior.

Another key enricher provides dynamic analysis. The framework will orchestrate dynamic analysis using a CAPEv2 sandbox. Dynamic analysis will provide behavioral insights into the malware, such as process activity, memory allocations and network activity. These results will be exported from CAPE and correlated with the sample within SubParse. For these artifacts, they will be submitted to the framework for full analysis and correlated to the original sample.

</details>

<details><summary><strong>The Mathematical Mesh</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Phillip Hallam-Baker](https://img.shields.io/badge/Phillip%20Hallam-Baker-informational)

🔗 **Link:** [The Mathematical Mesh](https://github.com/hallambaker)  
📝 **Description:** The Mathematical Mesh is a Threshold Key Infrastructure that allows cryptographic applications to provide effortless security. Threshold key generation and threshold key agreement are used to provide end-to-end security of data in transmission and data at rest without requiring any additional user interactions.

Once a device is connected to a user's personal Mesh through a simple, one-time configuration step, all private key and credential management functions are automated. Devices may be provisioned with private keys required to support applications such as OpenPGP, S/MIME and SSH according to intended use of that device.

</details>

---
## 🔍 OSINT
<details><summary><strong>Defaultinator: An Open Source Search Tool for Default Credentials</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Curt Barnard](https://img.shields.io/badge/Curt%20Barnard-informational)

🔗 **Link:** Not Available  
📝 **Description:** Have you ever had to Google around trying to find a default password for a router? Are you sick of combing through user manuals just to find admin:admin buried on page 37. Then it's time you tried Defaultinator. This newly released tool is a repository for default credentials made searchable via API or the intuitive web interface. Why would someone make such a tool? Why, I'm so glad you asked!

Static device passwords are not only Really Bad, they are sometimes illegal. Yet legacy or poorly secured IoT devices still often contain default or hardcoded passwords. It's hard to know if you have default passwords in your environment, but this tool is here to help you find them. Or maybe you are on a Red Team engagement and want to audit for CWE-798 (Use of Hard-coded Credentials). Defaultinator has your back.

In this talk, I'll cover how default passwords contribute to the spread of malware, how common it is to see them used in brute force attacks 'in the wild', and how a tool like Defaultinator can help you identify them and remove them from your own environment.

</details>

<details><summary><strong>Octopii - AI-powered Personal Identifiable Information (PII) scanner</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Owais Shaikh](https://img.shields.io/badge/Owais%20Shaikh-informational)

🔗 **Link:** [Octopii - AI-powered Personal Identifiable Information (PII) scanner](https://github.com/redhuntlabs/Octopii)  
📝 **Description:** Octopii is an open-source AI-powered Personal Identifiable Information (PII) scanner that can look for image assets such as Government IDs, passports, photos and signatures in a directory.

</details>

<details><summary><strong>Recon.Cloud - Cloud Attack Surface Management and Cloud Reconaissance</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Michael Silva](https://img.shields.io/badge/Michael%20Silva-informational)

🔗 **Link:** [Recon.Cloud - Cloud Attack Surface Management and Cloud Reconaissance](https://gist.github.com/emanb29/17ad89bd6cea2124f45e8b3dbec8fc9a)  
📝 **Description:** Recon.Cloud is a public and free AWS cloud security reconnaissance tool that will enable users to reveal publicly exposed cloud assets on any domain. There are many tools in the market that are open to users for reconnaissance efforts, but there are few that specifically scope recon efforts to look at the cloud alone. Typical recon tools provide an exhaustive list of all assets they detect – there is no scope to define the cloud assets themselves. This leaves users overwhelmed with too much information that can be difficult and time-consuming to comb through.

</details>

<details><summary><strong>ReconPal: Leveraging NLP for Infosec</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Shantanu Kale](https://img.shields.io/badge/Shantanu%20Kale-informational) ![Sherin Stephen](https://img.shields.io/badge/Sherin%20Stephen-informational)

🔗 **Link:** [ReconPal: Leveraging NLP for Infosec](https://github.com/pentesteracademy/reconpal)  
📝 **Description:** Recon is one of the most important phases that seem easy but takes a lot of effort and skill to do right. One needs to know about the right tools, correct queries/syntax, run those queries, correlate the information, and sanitize the output. All of this might be easy for a seasoned infosec/recon professional to do but for rest, it is still near to magic. How cool it will be to ask a simple question like "Find me an open Memcached server in Singapore with UDP support?" or "How many IP cameras in Singapore are using default credentials?" in WhatsApp chat or a web portal and get the answer?

The integration of GPT-3, deep learning-based language models to produce human-like text, with well-known recon tools like Shodan is the foundation of ReconPal. In this talk, we will be introducing ReconPal with report generation capabilities and interactive terminal sessions. We are also introducing a miniature attack module, allowing users to execute popular exploits against the server with just the voice commands. The code will be open-source and made available after the talk.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Exploiting & Securing Trains</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Amine Amri](https://img.shields.io/badge/Amine%20Amri-informational) ![Daniel dos Santos](https://img.shields.io/badge/Daniel%20dos%20Santos-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Hands-on RF Hacking 101: From Waveforms to System Takeover</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Paul Clark](https://img.shields.io/badge/Paul%20Clark-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Vehicle Control System</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Shishir Gupta](https://img.shields.io/badge/Shishir%20Gupta-informational) ![Chris Sistrunk](https://img.shields.io/badge/Chris%20Sistrunk-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>FireTail - inline API security checking</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Jeremy Snyder](https://img.shields.io/badge/Jeremy%20Snyder-informational)

🔗 **Link:** Not Available  
📝 **Description:** FireTail sits on top of popular open source frameworks for building web services and APIs, like OpenAPI/Swagger, Express and Rails, and then provides in-line security processing of the API calls. FireTail checks for (in sequential order):
1. API call is hitting valid route using a valid method. This allows for a zero-trust, declarative API structure, with proper error handling at the HTTP layer.
2. Inspection of authentication token. Does the API expect a JWT, application-issued API key or other? FireTail will check whether a valid token of the correct type is present.
3. Payload inspection. FireTail will look for and fail invalid queries.

</details>

<details><summary><strong>GoTestWAF - well-known open-source WAF tester now supports API security hacking</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ivan Novikov](https://img.shields.io/badge/Ivan%20Novikov-informational)

🔗 **Link:** Not Available  
📝 **Description:** GoTestWAF is a well-known open-source WAF testing tool which supports a wide range of attacks, bypassing techniques, data encoding formats, and protocols, including legacy web, REST, WebSocket, gRPC, and more.

With this major update, the tool now supports Swagger/OpenAPI-based scanning and becomes the first open-source testing tool available for API security solutions.

</details>

<details><summary><strong>Makes: A tool for avoiding supply chain attacks</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Daniel Salazar](https://img.shields.io/badge/Daniel%20Salazar-informational)

🔗 **Link:** [Makes: A tool for avoiding supply chain attacks](https://github.com/jatrost/awesome-kubernetes-threat-detection/blob/main/README.md)  
📝 **Description:** As the open-source ecosystem keeps growing, and applications increase their reliance on public libraries, we also see a spike in supply chain attacks. Recent scandals like SolarWinds or Log4j remind us how exposed software is when it comes to malicious, vulnerable or broken packages. Modern applications have thousands of dependencies, which means that managing dependency trees only becomes harder over time, while exposure keeps rising.

Think about how often you need things like

- keeping execution environments frozen for a strict dependency control (I'm looking at you, supply chain attacks);
- running applications locally so you can try whatever you are coding;
- executing CI/CD pipelines locally so you can make sure jobs (Linters, tests, deployments, etc.) are passing;
- running applications anywhere, no matter what OS you are using;
- knowing the exact dependency tree your application has for properly managing risk (Software Bill of Materials);
- making sure applications will work as expected in production environments.

At Fluid Attacks, we have experienced such concerns firsthand. That is why we created Makes, an open-source framework for building CI/CD pipelines and application environments in a way that is

- secure: Direct and indirect dependencies for both applications and CI/CD pipelines are cryptographically signed, granting an immutable software supply chain;
- easy: Can be installed with just one command and has dozens of generic CI/CD builtins;
- fast: Supports a distributed and completely granular cache;
- portable: Runs on Docker, VM's, and any Linux-based OS;
- extensible: Can be extended to work with any technology.

Makes is production ready and used currently in 11 different products that range from static and dynamic websites to vulnerability scanners. It was released on GitHub in July 2021 and has already been starred 170 times. It currently has 9 contributors from the community and gets a minor update each month.

</details>

<details><summary><strong>Node Security Shield - A Lightweight RASP for NodeJS Applications</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Sukesh Pappu](https://img.shields.io/badge/Sukesh%20Pappu-informational) ![Lavakumar Kuppan](https://img.shields.io/badge/Lavakumar%20Kuppan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Node Security Shield (NSS) is an Open source Runtime Application Self-Protection (RASP) tool which aims at bridging the gap for comprehensive NodeJS security.
NSS is designed to be Developer and Security Engineer friendly and enables them to declare what resources an application can access.
Inspired by the Log4Shell vulnerability which can be exploited because an application can make arbitrary network calls, we felt there is a need for an application to have a mechanism so that it can declare what privileges it allows in order to make the exploitation of such vulnerabilities harder by implementing additional controls.
In order to achieve this, NSS (Node Security Shield) has a Resource Access Policy and the concept is similar to CSP (Content Security Policy). Resource Access Policy lets developer/security engineers declare what resources an application should access and Node Security Shield will enforce it.
If the Application is compromised and requests 'attacker.com' Node Security Shield will block it automatically and thus protect the application from malicious attacks.
Node Security Shield was first announced in Black Hat Asia 2022 Arsenal. This is the first major update after its release. This release adds support for the 'module-level' Resource Access Policy.
Allowing Developers or Security Engineers to declare what resources a module can access.

</details>

<details><summary><strong>Open-Source API Firewall: New Features & Functionalities</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ivan Novikov](https://img.shields.io/badge/Ivan%20Novikov-informational)

🔗 **Link:** [Open-Source API Firewall: New Features & Functionalities](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Web.md)  
📝 **Description:** The open-source API Firewall by Wallarm is a great option for API development. It offers a rich feature set, and its underlying technology is mature. The firewall's new feature of blocklisting for compromised tokens and cookies is a great way to gain visibility into threats and prevent issues. The feature is easy to set up and offers a high degree of visibility into the security posture of your APIs and services.

</details>

<details><summary><strong>VulnLab Web Application Vulnerabilities Lab</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ahmet Emin Horasanlı](https://img.shields.io/badge/Ahmet%20Emin%20Horasanlı-informational) ![Okan Avci](https://img.shields.io/badge/Okan%20Avci-informational)

🔗 **Link:** Not Available  
📝 **Description:** VulnLab is a lab environment to learn various Web vulnerabilities and test different exploitation techniques developed with PHP and runs on Docker container. The main reason we created Vulnlab is that there are already well-known applications with similar content but these applications are getting out of date day by day. In order to solve this problem,
VulnLab will be updated by our community when a new vulnerability has been found such as spring4shell or log4j. Currently, Vulnlab only includes the OWASP TOP 10 vulnerabilities.

</details>

<details><summary><strong>What's new in reNgine?</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Yogesh Ojha](https://img.shields.io/badge/Yogesh%20Ojha-informational)

🔗 **Link:** [What's new in reNgine?](https://github.com/yogeshojha/rengine)  
📝 **Description:** reNgine, an automated reconnaissance framework, helps quickly discover the attack surface and identifies vulnerabilities using extremely customizable and powerful scan engines. The most recent update introduces some of the most innovative features such as powerful sub scans feature, highly configurable reconnaissance & vulnerability pdf report, Tools Arsenal which allows updating preinstalled tools, their configurations, WHOIS identification, identifies related domains and related TLDs, and tons of actionable insights such as most common vulnerability, most common CVE IDs, etc. In a nutshell, the newer upgrade of reNgine makes it more than just a recon tool! The latest update aims to fix the gap in the traditional recon tools and probably a much better alternative for some of the commercial recon and vulnerability assessment tools.

This talk will be a walkthrough on some of the newest features to be introduced in reNgine and how corporates and individuals can make the best use of it.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Kubescape: Open-Source Kubernetes Security Single-Pane-of-Glass</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Jonathan Kaftzan](https://img.shields.io/badge/Jonathan%20Kaftzan-informational) ![Rotem Refael](https://img.shields.io/badge/Rotem%20Refael-informational)

🔗 **Link:** Not Available  
📝 **Description:** Kubescape (https://github.com/armosec/kubescape) is a K8s open-source tool that provides a multi-cloud K8s single pane of glass, including risk analysis, security compliance, RBAC visualizer, and image vulnerabilities scanning.
Kubescape scans K8s clusters, YAML files, and HELM charts, detecting misconfigurations according to multiple frameworks (such as the NSA-CISA, MITRE ATT&CK, and more), software vulnerabilities, and RBAC (role-based-access-control) violations at early stages of the CI/CD pipeline, calculates risk score instantly and shows risk trends over time.
It became one of the fastest-growing Kubernetes tools among developers due to its easy-to-use CLI interface, flexible output formats, and automated scanning capabilities, saving Kubernetes users and admins precious time, effort, and resources.
Kubescape integrates natively with other DevOps tools, including Jenkins, CircleCI, Github workflows, Prometheus, and Slack, and supports multi-cloud K8s deployments like EKS, GKE, and AKS.

in this session, we will reveal new capabilities and features for the first time

</details>

<details><summary><strong>RIDE: Efficient Highly-Precise Systematic Automatic Bug Hunting in Android Systems</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Qidan He](https://img.shields.io/badge/Qidan%20He-informational)

🔗 **Link:** [RIDE: Efficient Highly-Precise Systematic Automatic Bug Hunting in Android Systems](https://github.com/djeebus/defcon24ical/blob/master/defcon24.ics)  
📝 **Description:** Vulnerabilities in various android systems such as the AOSP and vendor-specific components directly impact user security & privacy and should be eliminated. Do we have a way to efficiently identify bugs in ready-to-ship phones conveniently and precisely? From a researcher perspective, vendor codes are mainly closed-source which means they cannot use open-source auditing tools and usually the only obtainable resource is phone firmware. From vendor QA and security team's perspective, the ability to perform a systematic vulnerability assessment directly on ready-to-ship phone images would also be much more useful and easier than maintaining complex dependency and version information on each model.

We come up with a framework named RIDE (Rom Intelligent Defect assEsment) that directly operates on factory images of major android systems such as AOSP, Samsung, Huawei, Xiaomi, Oppo etc, which discovered 40+ CVEs including critical and high severity level bugs in the vendors in less than one year. RIDE combines highly precise whole-program static taint analysis and dynamic blackbox binary fuzzing to pinpoint vulnerabilities in user-space code such as system apps, system services and bundled closed-source libraries. In this talk, we will share in detail about the system's design and architecture, including the whole-program static analysis algorithm and implementation with high precision and acceptable performance, and the blackbox fuzzing component which is fed by the information collected from previous static analysis. Also, we will share the detail and exploitation of several bugs found, which range from system-level arbitrary file read/write/code execution to RCE ones in AOSP and other major vendors etc.

</details>

<details><summary><strong>Route Sixty-Sink: Connecting Application Inputs to Sinks Using Static Analysis</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Dillon Franke](https://img.shields.io/badge/Dillon%20Franke-informational) ![Michael Maturi](https://img.shields.io/badge/Michael%20Maturi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Route Sixty-Sink is an open source static analysis tool that traces the flow of user input through any .NET binary and determines whether it is passed as an argument to a dangerous function call (a "sink"). Route Sixty-Sink does this using two main modules:

1. RouteFinder, which enumerates API routes in MVC-based and classic ASP page web applications.
2. SinkFinder, which takes an entry point and creates a call graph of all classes and method calls. Then, it queries strings, method calls, and class names for "sinks".

By tying these two pieces of functionality together, Route Sixty-Sink is able to quickly identify high fidelity vulnerabilities that would be difficult to discover using black box or manual static analysis approaches.

We have used Route Sixty-Sink to reveal and successfully exploit vulnerabilities including unsafe object deserialization, SQL injection, command injection, arbitrary file uploads and access, authorization bypasses, and more in both open-source and proprietary .NET applications.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>ParseAndC 2.0 – We Don't Need No C Programs (for Parsing)</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Parbati Kumar Manna](https://img.shields.io/badge/Parbati%20Kumar%20Manna-informational)

🔗 **Link:** Not Available  
📝 **Description:** This is the 2.0 version of the ParseAndC tool that was presented in BH and DEFCON last year, with many new features added. The 1.0 version was capable of mapping any C structure(s) to any datastream, and then visually displaying the 1:1 correspondence between the variables and the data in a very colorful, intuitive display so that it was very easy to understand which field had what value.

In 2.0 version, we essentially expand the C language so that C structures alone has the same power as full-fledged C programs. We introduce Dynamic structure, which changes depending on what data it has seen till now. It supports variable-sized array, variable-sized bitfield, and addition/deletion of struct members depending on what value the previous struct members have. Suppose we are parsing the network packets, and after we decode the IP header, depending on the protocol field this tool can automatically decode the next header as either the TCP or UDP. We also add speculative execution, where user just provides the key expected values of certain fields (like magic numbers, mentioned by C initializations), and the tool automatically finds out from which offset to map so that all fields indeed have the expected value.

This tool is extremely portable – it's a single Python 1MB text file, is cross-platform (Windows/Mac/Unix), and also works in the terminal /batch mode without GUI or Internet connection. The tool is self-contained - it doesn't import anything, to the extent that it implements its own C compiler (front-end) from scratch!!

This tool is useful for both security- and non-security testing alike (reverse engineering, network traffic analyzing, packet processing etc.). It is currently being used at Intel widely. The author of this tool led many security hackathons at Intel and there this tool was found to be very useful.

</details>

<details><summary><strong>unblob</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Quentin Kaiser](https://img.shields.io/badge/Quentin%20Kaiser-informational)

🔗 **Link:** [unblob](https://github.com/IamAlch3mist/Awesome-Embedded-Systems-Vulnerability-Research)  
📝 **Description:** One of the major challenges of embedded security analysis is the sound and safe extraction of arbitrary firmware.

Specialized tools that can extract information from those firmwares already exists, but we wanted something smarter that could identify both start offset of a specific chunk (e.g. filesystem, compression stream, archive) and end offset.

We stick to the format standard as much as possible when deriving these offsets, and we clearly define what we want out of identified chunks (e.g., not extracting meta-data to disk, padding removal).

This strategy helps us feed known valid data to extractors and precisely identify unidentified chunks, turning unknown unknowns into known unknowns.

Given the modular design of unblob and the ever expanding repository of supported formats, unblob could be used in areas outside of embedded security such as data recovery, memory forensics, or malware analysis.

unblob has been developed with the following objectives in mind:

* Accuracy - chunk start offsets are identified using battle tested rules, while end offsets are computed according to the format's standard without deviating from it. We minimize false positives as much as possible by validating header structures and discarding overflowing chunks.
* Security - unblob does not require elevated privileges to run. It's heavily tested and has been fuzz tested against a large corpus of files and firmware images. We rely on up-to-date third party dependencies that are locked to limit potential supply chain issues. We use safe extractors that we audited and fixed where required (e.g., path traversal in ubi_reader, path traversal in jefferson, integer overflow in Yara).
* Extensibility - unblob exposes an API that can be used to write custom format handlers and extractors in no time.
* Speed - we want unblob to be blazing fast, that's why we use multi-processing by default, make sure to write efficient code, use memory-mapped files, and use Hyperscan as high-performance matching library. Computation intensive functions are written in Rust and called from Python using specific bindings.

</details>

---