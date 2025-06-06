# USA 2019
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2019** event held in **USA**.
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
<details><summary><strong>AADInternals: PowerShell Module for Administering Azure AD and Office 365</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nestori Syynimaa](https://img.shields.io/badge/Nestori%20Syynimaa-informational)

🔗 **Link:** [AADInternals: PowerShell Module for Administering Azure AD and Office 365](https://github.com/Gerenios/AADInternals)  
📝 **Description:** AADInternals is a PowerShell module for administering Azure AD and Office 365. It is a result of hours of reverse-engineering and debugging of Microsoft tools related to Azure AD, such as PowerShell modules, directory synchronisation, and admin portals.

AADInternals contains tools for retrieving detailed information about Azure AD/Office 365 tenant not available otherwise, tools for manipulating Azure AD objects (e.g., users and passwords), and tools for creating backdoors to Azure AD/Office 365. The backdoor tools are based on the discovery and research of a vulnerability in Azure AD identity federation.

</details>

<details><summary><strong>ACsploit: Exploiting Algorithmic Complexity Vulnerabilities</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Adam Jacobson](https://img.shields.io/badge/Adam%20Jacobson-informational) ![William Vega](https://img.shields.io/badge/William%20Vega-informational)

🔗 **Link:** Not Available  
📝 **Description:** Algorithmic Complexity (AC) vulnerabilities arise when a program uses an algorithm with a particularly inefficient worst-case computational complexity, and allows a user to provide input that will trigger it. Determining whether a program is vulnerable requires more than an understanding of what algorithms the program implements. It also requires understanding
how user input is filtered and formatted before it's given to the potentially exploitable algorithm. One way to do this is with time consuming manual analysis, such as reverse engineering, static code review, or debugging. Alternatively, feeding the algorithm input formatted to trigger its worst case, and then measuring the effects in time (i.e. CPU utilization) and space (e.g. RAM or disk usage) is quicker and requires less skill.

ACsploit is a command-line utility that generates worst-case inputs to commonly used algorithms, such as sorting, hashing, string manipulation, etc. It is modular and highly configurable, supporting a wide variety of user-specified constraints on the generated output, allowing it to appropriately fit the requirements of the application under test. ACsploit also supports an equally wide array of output formats to assist the user in delivering the resulting exploit from ACsploit to the target system. ACsploit supports both script-driven and interactive use through a familiar Metasploit-like interface. Originally developed under the DARPA STAC program to help rapidly triage potential AC vulnerabilities, we have released ACsploit as an open source tool to the broader vulnerability researcher community.

ACsploit comes with algorithmic complexity exploits for 30+ algorithms and is easily extensible. It's designed to allow members of the community to contribute new exploit modules, input constraints, and output formatters to expand upon all aspects of its functionality. Future plans for the development of ACsploit include debugger integration and a testing framework for measuring resource usage by the targeted application.

</details>

<details><summary><strong>Apfell: Multi-Platform Command and Control</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Cody Thomas](https://img.shields.io/badge/Cody%20Thomas-informational)

🔗 **Link:** [Apfell: Multi-Platform Command and Control](https://github.com/its-a-feature/Mythic)  
📝 **Description:** Apfell is a collaborative, command and control platform designed to facilitate a plug-n-play architecture. It uses a web-based front-end so that it can be accessed from any OS and a Python/Docker based back-end. Apfell focuses on quality of life improvements for operators, especially while operating across macOS and *nix operating systems, such as searchable tasks, per-task comments, artifact tracking, MITRE ATT&CK mappings/exports, multiple concurrent c2 profiles, command versioning, and much more. It features a JavaScript for Automation (JXA) agent that runs in memory on macOS devices, but offers agents across a variety of platforms and services.

</details>

<details><summary><strong>AttackForge: Pentest Collaboration Platform for Everyone</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Fil Filiposki](https://img.shields.io/badge/Fil%20Filiposki-informational) ![Stas Filshtinskiy](https://img.shields.io/badge/Stas%20Filshtinskiy-informational)

🔗 **Link:** Not Available  
📝 **Description:** AttackForge.com is a free-to-use collaboration platform to manage pentesting projects. AttackForge allows a project team to easily collaborate in one place, reducing overheads and pain for Business, Technology and Pentest Team. This is what makes AttackForge unique and different to other pentest collaboration solutions. It goes beyond automated reporting and issue library. It's like JIRA for pentesting.

Pentesters love to break things. However they hate responding to unnecessary emails and phone calls; having to chase people for details to start testing; having to figure out who to talk to when things aren't working; and most of all having to write and review reports. AttackForge.com is purpose built to help pentesters focus their time and efforts on breaking things, and reduce distractions and unnecessary tasks. This helps to get the best out of the pentest team and provide better results for business.

AttackForge.com also helps people to start a career in penetration testing. AttackForge provides a secure online environment to create a portfolio of pentests to reflect skills, knowledge and communication ability in an industry-standard way – to demonstrate to recruiters and prospective employers that they are ready for the workforce. This may in turn help to reduce the shortage of supply and skills-gap our industry is currently facing.

</details>

<details><summary><strong>AVET: AntiVirus Evasion Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Daniel Sauder](https://img.shields.io/badge/Daniel%20Sauder-informational)

🔗 **Link:** [AVET: AntiVirus Evasion Tool](https://github.com/govolution/avetosx)  
📝 **Description:** AVET is an antivirus evasion tool that is based on different antivirus evasion techniques as described in my research, found here:

https://govolutionde.files.wordpress.com/2014/05/avevasion_pentestmag.pdf
https://deepsec.net/docs/Slides/2014/Why_Antivirus_Fails_-_Daniel_Sauder.pdf

What & Why:

When running an exe file made with msfpayload & co, the exe file will often be recognized by the antivirus software
AVET is an antivirus evasion tool targeting windows machines with executable files
Different kinds of payloads can be used now: shellcode, exe and dlls
More techniques can be used now, such as shellcode injection, process hollowing and more
Most payloads can be delivered from a file, the network or command line
The payload can be encrypted with a key, the key can be delivered like payloads
Tested for Kali 2018.x (64bit) and tdm-gcc (should work on other Kali/Linux/32bit versions also)

AVET Version 2 was released in the beginning of 2019:

Internal mechanisms for building the executable have been rewritten, new features can be added much easier now
https://github.com/govolution/bfg has been integrated

With the new architecture and features of AVET 2 you can, for example, now build an executable that is loading an encrypted .exe file via network or file, receiving the key also via network or file, decrypt in memory and then inject via process hollowing. The same applies also for other payloads like shellcode or dlls and other techniques.

Presentation: https://govolution.files.wordpress.com/2019/08/bhusa19_arsenal_avet.pdf

</details>

<details><summary><strong>barq: The AWS Post-Exploitation Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mohammed Aldoub](https://img.shields.io/badge/Mohammed%20Aldoub-informational)

🔗 **Link:** [barq: The AWS Post-Exploitation Tool](https://github.com/Voulnet/barq)  
📝 **Description:** barq is a post-exploitation framework that allows you to easily perform attacks on a running AWS infrastructure. It allows you to attack running EC2 instances without having the original instance SSH keypairs. It also allows you to perform enumeration and extraction of stored Secrets and Parameters in AWS.

</details>

<details><summary><strong>Break out the Box (BOtB): Container Analysis, Exploitation and CICD Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Chris Le Roy](https://img.shields.io/badge/Chris%20Le%20Roy-informational)

🔗 **Link:** [Break out the Box (BOtB): Container Analysis, Exploitation and CICD Tool](https://github.com/brompwnie/botb)  
📝 **Description:** BOtB is the first tool aimed at hackers and developers to automate Container exploitation. BOtB is a tool that can be used to analyze and identify vulnerabilities for Containers such as LXC and Docker. Not only does BOtB provide the user with a detailed analysis of identified vulnerabilities of the container, BOtB provides an autopwn feature which allows for the user to automagically exploit the vulnerabilities identified and break out onto the host. BOtB is able to identify multiple container vulnerabilities and contains a vast collection of exploits to break out of the container. BOtB is also developer friendly and has a Continuous Integration Continuous Development (CICD) mode which when enabled, BOtB will attempt to autopwn identified vulnerabilities but instead of dropping to host shells, it will return exit codes greater than 0 which is used by CICD technologies to indicate failed tests. When used in an Agile SDLC process implementing DevSecOps principles, this can assist developers with identifying Container issues prior to production deployments. BOtB is written in Golang and is distributed as a binary for multiple platforms.

</details>

<details><summary><strong>CALDERA: Automating Adversary Emulation</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![David Hunt](https://img.shields.io/badge/David%20Hunt-informational)

🔗 **Link:** [CALDERA: Automating Adversary Emulation](https://github.com/0x4D31/awesome-threat-detection)  
📝 **Description:** Adversary emulation is great, but it can be time consuming – so why not automate it? CALDERA automates the adversary emulation process, allowing users to run fully automated adversary emulation exercises, aligning its operations with MITRE ATT&CK. Blue and red teamers alike can use CALDERA for training, to test analytics and defensive tools, and just generally to stress test their networks and systems.


CALDERA was first released in late 2017 featuring its end-to-end “adversary mode” capability, where operators could use CALDERA to run fully end-to-end tests emulating the full adversary lifecycle. This mode allowed CALDERA to run intelligently and autonomously, leveraging a planning system to dynamically compose operations.


Since this first release, the MITRE team has continued to expand CALDERA’s capabilities, releasing a new “chain mode” in 2019. This new mode allows users much more control over CALDERA, letting them orchestrate and automate atomic unit tests as opposed to end-to-end operations. With more fine-grained control over CALDERA, users can better control their operations to accommodate more use cases, such as testing and refining analytics.


This demo will highlight both of CALDERA’s modes, providing demos and guides on how to use CALDERA including how to extend it with new plugins and adding additional tests. CALDERA is open source and can be downloaded off of the MITRE GitHub repository.

</details>

<details><summary><strong>Commando VM 2.0: Security Distribution for Penetration Testers and Red Teamers</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jacob Barteaux](https://img.shields.io/badge/Jacob%20Barteaux-informational) ![Blaine Stancill](https://img.shields.io/badge/Blaine%20Stancill-informational) ![Nhan Huynh](https://img.shields.io/badge/Nhan%20Huynh-informational)

🔗 **Link:** [Commando VM 2.0: Security Distribution for Penetration Testers and Red Teamers](https://github.com/mandiant/commando-vm)  
📝 **Description:** Commando VM is an open-source Windows-based security distribution designed for Penetration Testers and Red Teamers. It is an add-on from FireEye's very successful Reverse Engineering distribution: FLARE VM. Much like Kali Linux, Commando VM is designed with an arsenal of open-source offensive tools that will help operators achieve assessment objectives.

Being built on Windows, Commando VM comes with all the native support for accessing Active Directory environments. Additionally, Commando VM includes Web Application assessment tools, scripting languages (such as Python and Go), Information Gathering tools (such as Nmap, WireShark, and PowerView), Exploitation Tools (such as PowerSploit, GhostPack and Mimikatz), Persistence tools, Lateral Movement tools, Evasion tools, Post-Exploitation tools (such as FireEye's SessionGopher), Remote Access tools, Command-Line tools, and all the might of FLARE VM's reversing tools.

Commando VM 1.0 was greeted with tremendous enthusiasm and praise when it debuted at Black Hat Asia in Singapore this year; afterwards, it generated lots of media buzz. Less than two weeks after release our GitHub repository had over 2000 followers and over 400 forks. For Black Hat USA, we are debuting Commando VM 2.0, with full support for Kali on the Windows Subsystem for Linux, as well as giving users the ability to customize what tools get installed on their system.

</details>

<details><summary><strong>Dolos Cloak: Your NAC Can't See This</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational)

🔗 **Link:** [Dolos Cloak: Your NAC Can't See This](https://github.com/fkasler/dolos_cloak)  
📝 **Description:** Dolos Cloak is a new tool designed to give penetration testers and red team members the ability to easily bypass 802.1x network access controls. The tool performs an advanced man-in-the-middle attack against nearly any authorized network device, automatically configures a NAT to blend in, and pass legitimate traffic unaltered. Simply plug a Dolos Cloak device in between a network jack and an available workstation, IP phone, printer, or other device and walk away. Dolos Cloak can be configured to call home using TPC/UDP reverse shells, SSH, VPN, Empire, or other custom methods to maintain a stealthy foothold on the network. The creation of Dolos Cloak was inspired by sysadmins that thought they could rely solely on 802.1x to keep attackers off their networks.

</details>

<details><summary><strong>Fudge: A Collaborative C2 Framework for Purple Teaming</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Kris Anderson](https://img.shields.io/badge/Kris%20Anderson-informational)

🔗 **Link:** [Fudge: A Collaborative C2 Framework for Purple Teaming](https://github.com/IvanLazarevsky/AIML_1sem/blob/master/nltk_feature_names4_wm.json)  
📝 **Description:** Fudge is a Python3/Flask web-based C2 framework and Powershell implant designed to facilitate purple teaming activities, post-campaign review and timelining.

Fudges' inception is based on 3 main areas:

Creating a suitable way for blue teamers to review the chronological activities a red team engagement, allowing them to assess if key alerts were missed.
Finding ways to incrementally increase detection rates, allowing defenders to identify the intrusion. This provides a gauge of skill & target areas for upskilling if the intrusion is not identified.
Providing a way for junior testers to experience red teaming without increasing risk to the campaign OpSec/client network.
Purple teaming was born out of the need for tighter integration between offensive and defensive teams. If the red team is successful in compromise, their ability to export the campaign timeline and logging can prove invaluable insight to the blue team. Allowing defenders to review network and host logs as they follow a campaign timeline, allows for blind spots to be identified and tooling adjusted and tuned.

Fudges' implant also supports varying levels and types of obfuscation to allow for varying levels of noise to be made during the engagement to help a SoC benchmark their detection skills.

Lastly, Fudge is designed around team usage, which allows for a senior red teamer to allow another user to have read or read/write access to the campaign. These access controls allow a junior member to view the campaign and see the kind of commands, and techniques used in a post-exploitation environment.

Fudge can be found on Github at: https://github.com/Ziconius/Fudge

</details>

<details><summary><strong>FumbleChain: A Purposefully Vulnerable Blockchain</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nils Amiet](https://img.shields.io/badge/Nils%20Amiet-informational)

🔗 **Link:** Not Available  
📝 **Description:** FumbleChain is a deliberately insecure blockchain designed to raise awareness about blockchain security. Cryptocurrencies and blockchains are still relatively new, and there have been plenty of news stories about people losing money through compromises in various components making up a blockchain ecosystem. FumbleChain hopes to bridge the awareness gap in a fun way, one in which nobody loses money.

FumbleChain allows people to test their skills attacking the chain and store running on top. The FumbleStore is a CTF in the form of a fake e-commerce web application that offers products you can buy using FumbleCoins, which is the ecosystem's cryptocurrency. Purchasing new products requires players to exploit flaws and steal coins from crypto-wallets. Of course, you could mine coins and use the system legitimately, but where's the fun in that?

The project is written in Python making it easy for anyone to read and modify its source code. It's also modular, making it easy to hack and add new challenges. The entire project is fully dockerized, letting anyone play with FumbleChain in a quick and hassle-free way.

</details>

<details><summary><strong>Koadic: Two Years of Mischief</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sean Dillon](https://img.shields.io/badge/Sean%20Dillon-informational) ![Nate Caroe](https://img.shields.io/badge/Nate%20Caroe-informational)

🔗 **Link:** Not Available  
📝 **Description:** Koadic is a post-exploitation toolkit that leverages the Windows Script Host, delivering all the features expected from a modern RAT via VBScript/JScript. Koadic was first released at DEF CON in 2017, and has since seen two years of development. Koadic is robust enough to have been chosen in nation-state cyberespionage campaigns by APT favorites such as Fancy Bear, Stone Panda, and MuddyWater. It has been the tool of choice on the road to domain admin for many pentests, especially in environments where PowerShell and filesystems are heavily audited by antivirus.

New payloads have been added since release, such as Squiblytwo WMIC.exe XSL files (discovered by SubTee and Mattifestation) and Bitsadmin.exe transfer jobs. Existing payloads have been upgraded to include obfuscation and antivirus evasion.

Several new implants have been added, including UAC bypasses via slui, fodhelper, compmgmtlauncher, and compdefaults. A loot finder module automates the process of finding files which may contain sensitive data. Persistence is now available via registry autoruns, WMI, and scheduled tasks. "One shot" stagers now allow an implant to be run immediately on a zombies first call home.

A new credential storage feature has been added, transforming Mimikatz outputs acquired into a readily searchable format. A full fledged API is also available, allowing all available functionality of the toolkit to be automated through HTTP interactions. There are innumerable bug fixes, improvements to reliability, and additional stealth since the initial release, with new features being added regularly.

</details>

<details><summary><strong>Kube-Hunter: Pentest Platform for Kubernetes Environments</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Cherny](https://img.shields.io/badge/Michael%20Cherny-informational)

🔗 **Link:** [Kube-Hunter: Pentest Platform for Kubernetes Environments](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Containers.md)  
📝 **Description:** Kubernetes is today's most popular container orchestrator. But it's also a complex distributed system, with defaults tuned for usability rather than for security. More so, configuring Kubernetes correctly is not trivial. Failing to configure Kubernetes in a secure way exposes the applications running on it to imminent risk, regardless of how securely those application are built.

We recognized the need to assess the level of security of a Kubernetes cluster deployment, and built kube-hunter to be an extensible pentesting and risk assessment platform for Kubernetes environments. We contributed quite a few discovery and hunt techniques from the get-go, and will add more over time. Kube-hunter is also designed to be easily extended by the community. This is the current list of tests:
Passive Tests (tests not making any change to the cluster):

Generates ip addresses to scan, based on cluster/scan type
Scans known Kubernetes ports to determine open endpoints for discovery
Checks for an open API Server
Checks for open Kubelet ports
Checks for an open Proxy service
Checks for email addresses in kubernetes ssl certificates
Hunts for a dashboard behind the proxy
Hunts open Dashboards, gets the type of nodes in the cluster
Reads specific endpoints on open ports in the readonly Kubelet server
Hunting Azure cluster deployments using specific known configurations
Hunting etcd, checks for remote availability of etcd, its version, and read access to the DB
Hunting API server using the service account token obtained from a compromised pod
Vulnerabilities hunter:
○ CVE-2018-1002105
○ CVE-2019-1002100

Active Tests (may perform state-changing actions on the cluster):

Retrieves logs from a random container
Hunts Proxy when exposed, extracts the version
Hunts when proxy is exposed, extracts the build date of kubernetes
Executes uname inside of a random container
Gets the Azure subscription file on the host by executing inside a container
Hunting etcd, checks for remote write access to etcd- will attempt to add a new key to the etcd DB
Accessing the api server might grant an attacker full control over the cluster

</details>

<details><summary><strong>Lauschgerät: Gets in the Way of your Victim's Traffic and Out of Yours</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Adrian Vollmer](https://img.shields.io/badge/Adrian%20Vollmer-informational)

🔗 **Link:** [Lauschgerät: Gets in the Way of your Victim's Traffic and Out of Yours](https://github.com/SySS-Research/Lauschgeraet)  
📝 **Description:** Lauschgerät gets in the way of your victim and out of yours. This python tool acts as a convenient man-in-the-middle tool to sniff traffic, terminate TLS encryption, host malicious services and bypass 802.1X - provided you have physical access to the victim machine, or at least its network cable.

There are three ways to run it: Either on its own dedicated device like a Raspberry Pi or Banana Pi, in a virtual machine with two physical USB-NICs attached, or on your regular pentest system in its own network namespace. It will look like a completely transparent piece of wire to both victim systems you are getting in the middle of, even if they are using 802.1X because it is implementing the ideas presented in a talk by Alva Lease 'Skip' Duckwall IV.

The Lauschgerät operates with three interfaces: Two interfaces going to the victim client and the victim switch respectively, and one management interface which you can connect to and initiate the redirection of traffic, inject your own traffic, start and stop malicious services, and so forth. It comes with a few services included, such as a service that terminates TLS encryption (which will of course cause a certificate warning on the victim's end) or a service that performs the classic "SSL strip" attack. And more to come!

An optional wireless interfaces can either be used as another management interface or for intercepting traffic of wireless devices. The management can be done via SSH or via a web application, making sure you can hit the ground running.

</details>

<details><summary><strong>Mr.SIP: SIP-Based Audit & Attack Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ismail Melih Tas](https://img.shields.io/badge/Ismail%20Melih%20Tas-informational)

🔗 **Link:** [Mr.SIP: SIP-Based Audit & Attack Tool](https://github.com/meliht)  
📝 **Description:** Mr.SIP is a simple console based SIP-based Audit and Attack Tool. Originally it was developed to be used in academic work to help developing novel SIP-based DDoS attacks and then the idea has been converted into a fully functional SIP-based penetration testing tool. So far, it has been used more than 5 journal papers. Mr.SIP can also be used as SIP client simulator and SIP traffic generator.

The initial academic journal paper which Mr.SIP is used is titled "Novel SIP-based DDoS Attacks and Effective Defense Strategies" published in Computers & Security 63 (2016) 29-44 by Elsevier, Science Direct http://sciencedirect.com/science/article/pii/S0167404816300980.

In the current state, Mr.SIP comprises 7 sub-modules named as SIP-NES (network scanner), SIP-ENUM (enumerator), SIP-DAS (DoS attack simulator), SIP-ASP (attack scenario player), SIP-EVA (eavesdropper), SIP-SIM (signaling manipulator) and SIP-CRACK (cracker). Since it provides a modular structure to developers, more modules will continue to be added by the authors and it is open to be contributed by the open-source developer community.

SIP-NES is a network scanner. It needs the IP range or IP subnet information as input. It sends SIP OPTIONS message to each IP addresses in the subnet/range and according to the responses, it provides the output of the potential SIP clients and servers on that subnet.

SIP-ENUM is a enumerator. It needs the output of SIP-NES and also pre-defined SIP usernames. It generates SIP REGISTER messages and sends them to all SIP components and try to find the valid SIP users on the target network. You can write the output in a file.

SIP-DAS is a DoS/DDoS attack simulator. It comprises four components: powerful spoofed IP address generator, SIP message generator, message sender and response parser. It needs the outputs of SIP-NES and SIP-ENUM along with some pre-defined files.

IP spoofing generator has 3 different options for spoofed IP address generation, i.e., manual, random and by selecting spoofed IP address from subnet. IP addresses could be specified manually or generated randomly. Furthermore, in order to bypass URPF filtering, which is used to block IP addresses that do not belong to the subnet from passing onto the Internet, we designed a spoofed IP address generation module. Spoofed IP generation module calculated the subnet used and randomly generated spoofed IP addresses that appeared to come from within the subnet.
SIP-DAS basically generates legitimate SIP INVITE message and sends it to the target SIP component via TCP or UDP. In the current state, it doesn't support instrumentation which helps you to understand the impact of the attack by using Mr.SIP, but we will support it very soon. In the current state, we can see the impact of the attack by checking the CPU and memory usage of the victim SIP server.

SIP is a text-based protocol such as HTTP but more complex than HTTP. For example, when we talk about SIP INVITE message, there are some specific headers and parameters need to be vendor specific and unique for each call. SIP Message Generator allows you to bypass security perimeters bu generating all these headers and parameters as it should be, so basic it is harder to be detected by anomaly detection engines that these messages are generated automatically. You can generate SIP methods such as INVITE message, REGISTER message, etc. You can specify the message count, the destination port, you can use predefined toUser list, fromUser list, userAgent list etc.

In order to bypass automatic message generation detection (anomaly detection) systems, random "INVITE" messages are generated that contained no patterns within the messages. Each generated "INVITE" message is grammatically compatible with SIP RFCs and acceptable to all of the SIP components.

"INVITE" message production mechanism specifies the target user(s) in the "To" header of the message. This attack can be executed against a single user or against legitimate SIP users on the target SIP server as an intermediary step before the DoS attack. The legitimate SIP users are enumerated and written to a file. Next, they are placed randomly in the "To" header of the generated "INVITE" messages. "Via, "User-Agent, "From," and "Contact" headers within an "INVITE" message were syntactically generated using randomly selected information from the valid user agent and IP address lists. The tag parameter in the "From" header, the branch and source-port parameters in the "Via" header, and the values in the "Call-ID" header are syntactically and randomly generated using the valid user agent list. In addition, the source IP addresses in the "Contact" and "Via" headers are also generated using IP spoofing.

UDP is used widely in SIP systems as a transport protocol, so attacks on the target server are implemented by sending the generated attack messages in the network using UDP. Also, TCP can be used optionally. The message sender of SIP-DAS allows the optional selection of how many SIP messages could be sent during one second. The number of SIP messages sent in one second depended on the resources (CPU and RAM) of the attacker machine.

SIP-ASP is Attack Scenario Player. It is working like a sub-function of SIP-DAS. It has a powerful parser and allows you to create stateful SIP attack call flows. In our academic studies, we have developed new attack vectors by using our SIP-DAS and SIP-ASP such as re-transmission based DDoS attacks and reflection based DRDoS attacks.

SIP-EVA is an eavesdropper. It sniffs the target network and can grasp the SIP messages. It allows you to extract call specific information such as who is calling, who is called, the duration of the call, the unique call-ID value and you can even download the media content of the call.

SIP-SIM is a signaling manipulator. It is working like an Intercepting SIP Proxy. It uses the same sniffer mechanism with SIP-EVA but it allows you to catch the messages between clients and server and you can replicate the messages and manipulate some headers and/or parameters as you want and send it to the victim server. By using SIP-SIM you can do Caller-ID spoofing attacks. SIP-SIM support both LAN-based and WAN-based Caller-ID spoofing attacks. But in order to make WAN-based Caller-ID spoofing attack, you need to have proper service provider account.

SIP-CRACK is a password cracker. Again, it uses the same sniffing mechanism and it allows you to catch the SIP REGISTER messages, extract the authentication data such as hash values. You can do brute-force based cracking, or you can choose a dictionary or rainbow table cracking. So SIP is a time-critical protocol and cracking should be an offline attack.

</details>

<details><summary><strong>PivotSuite: Hack The Hidden Network - A Network Pivoting Toolkit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Manish Gupta](https://img.shields.io/badge/Manish%20Gupta-informational)

🔗 **Link:** [PivotSuite: Hack The Hidden Network - A Network Pivoting Toolkit](https://github.com/RedTeamOperations/PivotSuite)  
📝 **Description:** PivotSuite is a portable, platform independent and powerful network pivoting toolkit, which helps Red Teamers/Penetration Testers to use a compromised system to move around inside a network. It is a Standalone Utility, which can be uses as a Server or as a Client.

PivotSuite as a Server: If the Compromised host is directly accessible (Forward Connection) from our pentest machine, then we can run pivotsuite as a server on a compromised machine and access the different subnet hosts from our pentest machine, which was only accessible from a compromised machine.

PivotSuite as a Client: If the Compromised host is behind a Firewall/NAT and isn't directly accessible from our pentest machine, then we can run pivotsuite as a server on pentest machine and pivotsuite as a client on compromised machine for creating a reverse tunnel. Using this, we can reach different subnet hosts from our pentest machine, which was only accessible from a compromised machine.

Key Features:

Supported Forward & Reverse TCP Tunneling
Supported Forward & Reverse Socks5 Proxy Server
UDP over TCP and TCP over TCP Protocol Supported
Corporate Proxy Authentication (NTLM) Supported
Inbuilt Network Enumeration Functionality, Eg. Host Discovery, Port Scanning, OS Command Execution
PivotSuite allows to get access to different Compromised host and their network, simultaneously (Act as C&C Server)
Single Pivoting, Double Pivoting and Multi-level pivoting can perform with help of PivotSuite
PivotSuite also works as SSH Dynamic Port Forwarding but in the Reverse Direction

Advantage Over Other tools:

Doesn't required admin/root access on Compromised host
PivotSuite also works when Compromised host is behind a Firewall / NAT, When Only Reverse Connection is allowed
No dependency other than python standard libraries
No Installation Required
UDP Port is accessible over TCP

</details>

<details><summary><strong>PowerShell-RAT</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Viral Maniar](https://img.shields.io/badge/Viral%20Maniar-informational)

🔗 **Link:** [PowerShell-RAT](https://github.com/Viralmaniar/Powershell-RAT/actions)  
📝 **Description:** PowerShell-RAT is a stealthy tool which exfiltrates sensitive information from the Windows environment through screenshots and keystrokes. The exfiltrated information is sent to a malicious user over a HTTPS protocol in the form of email attachments. The RAT can be invoked with a single key press using 'Hail Mary' option. Gmail is used to receive files from the backdoored machine. As Gmail is considered one of the highly trusted domains, this would allow an attacker to avoid network detection by NextGen Firewalls.

During a Red Team engagement, this tool can be executed on any Windows machine which backdoors the user machine using a number of task schedulers which will run the PowerShell scripts. Once backdoored, malicious user receives screenshots of the user activities via email every 5 minutes. After the email is received, screenshots are deleted from the machine to clean up the disk space, hence, avoiding the detection.

On successful authentication on a Windows machine, backdoor triggers the keystroke module on the user machine. It saves every key press via keyboard in the "log.txt" file on the user machine and sends it to the malicious user every hour as an email attachment. Setup requires a dedicated throw away Gmail account with modification to PowerShell script credential variables and a malicious user needs to enable "Allow less secure apps" under the security settings of the Gmail account to receive screenshots and key logs from the backdoored machine.

Target system can be identified using attachments naming convention which is Computer name followed by the timestamp. The backdoor Python file can be converted into an executable using Pyinstaller. During demo, I would also walk through a number of defence mechanisms to detect stealthy backdoors using publicly available tools such as Sysinternals from Microsoft.

</details>

<details><summary><strong>PyRDP: Python 3 Remote Desktop Protocol Man-in-the-Middle (MITM) and Library</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Francis Labelle](https://img.shields.io/badge/Francis%20Labelle-informational) ![Émilio Gonzalez](https://img.shields.io/badge/Émilio%20Gonzalez-informational)

🔗 **Link:** Not Available  
📝 **Description:** PyRDP is an RDP man-in-the-middle tool that has applications in pentesting and malware research. On the pentesting side, PyRDP has a number of features that allow attackers to compromise RDP sessions when combined with TCP man-in-the-middle solutions. If network-level authentication (NLA) is not enforced on an organization's RDP servers, attackers can use PyRDP to take complete control of RDP sessions. The graphical interface shows the client's credentials, keystrokes and clipboard contents as well as the current screen. It also has a "take control" button that allows attackers to hijack sessions. While the attacker is in control, all output going to the client is blocked to hide malicious activity. PyRDP also lists the contents of the drives mapped by the clients and allows attackers to download files from them. Finally, attackers can configure the man-in-the-middle to automatically run payloads on new connections. These payloads can be console commands or PowerShell scripts, and are hidden from the clients. Attackers can make use of PyRDP even when NLA is enforced by redirecting traffic to their own virtual machine. This setup allows them to collect credentials and use the functionalities for stealing clipboard contents and files.

On the malware research side, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It has the ability to replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads. This accelerates malware analysis since there is no need to search for the payloads on the infected machines or in the network activity.

</details>

<details><summary><strong>Router Exploit Shovel: Automated Application Generation for Stack Overflow Types on Wireless Routers</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Qinghao Tang](https://img.shields.io/badge/Qinghao%20Tang-informational) ![Yuan Zhuang](https://img.shields.io/badge/Yuan%20Zhuang-informational)

🔗 **Link:** [Router Exploit Shovel: Automated Application Generation for Stack Overflow Types on Wireless Routers](https://gist.github.com/Lysak/a0ca30a3e6732d39199b27c170a8cd28)  
📝 **Description:** Router exploits shovel is an automated application generation tool for stack overflow types on wireless routers. The tool implements the key functions of exploits, it can adapt to the length of the data padding on the stack, generate the ROP chain, generate the encoded shellcode, and finally assemble them into a complete attack code. The user only needs to attach the attack code to the overflow location of the POC to complete the Exploit of the remote code execution. The tool also incorporates live recovery, leaving no trace of attack after the Exploit attack is completed.

</details>

<details><summary><strong>Scapy: Python-Based Interactive Packet Manipulation Program + Library</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Guillaume Valadon](https://img.shields.io/badge/Guillaume%20Valadon-informational)

🔗 **Link:** [Scapy: Python-Based Interactive Packet Manipulation Program + Library](https://github.com/secdev/scapy)  
📝 **Description:** Scapy (https://github.com/secdev/scapy) is a renowned packet manipulation tool written in Python that supports a wide number of protocols on many different platforms (Linux, macOS, *BSD, and Windows). Initially developed by Philippe Biondi since 2003, it is now maintained by Guillaume Valadon, Pierre Lalet and Gabriel Potter. While the existence of this tool is well-known, its grip is much less, to the community's detriment. This presentation aims at filling this gap using practical and detailed examples.

</details>

<details><summary><strong>SIEMs Framework: Open Source MultiSIEM Python Attack Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yamila Levalle](https://img.shields.io/badge/Yamila%20Levalle-informational) ![Claudio Caracciolo](https://img.shields.io/badge/Claudio%20Caracciolo-informational)

🔗 **Link:** Not Available  
📝 **Description:** SIEMs are defensive tools increasingly used in information security, especially in large companies and regulated companies to monitor critical networks and devices. However, from the standpoint of the attacker, the permissions that the SIEMs have on the devices and accounts of a corporate network are very broad. Administrative access to a SIEM can be used to obtain code execution in the server where the SIEM is installed, and, in some cases, also in the "client" equipment from which the SIEM collects events, such as Active Directory servers, Databases, and network devices like Firewalls and Routers.

During our investigation, we detected many attack vectors that could be used in different SIEMs to compromise them, such as:

Obtaining the user accounts and passwords of critical equipment stored in the SIEM (LDAP/AD servers, databases, network devices, generally accounts with administrative permissions)
Developing and installing malicious applications such as a bind shell or a reverse shell to compromise the server where the SIEM is installed, or send malicious applications to compromise the devices from which the SIEM collects the events
Performing a brute force attack on the SIEM web interface
Reading arbitrary files from the server where the SIEM is installed
Using log events as intelligence source

Based on the results of this research, we developed an open source tool in Python: SIEMs Framework that allows to automate the mentioned attacks, both in commercial and open source SIEMs.

</details>

<details><summary><strong>SILENTTRINITY (v0.2.0): Async Post-Exploitation Agent Powered by Python, C# & .NET's DLR</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Marcello Salvati](https://img.shields.io/badge/Marcello%20Salvati-informational)

🔗 **Link:** [SILENTTRINITY (v0.2.0): Async Post-Exploitation Agent Powered by Python, C# & .NET's DLR](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)  
📝 **Description:** SILENTTRINITY is an asynchronous post-exploitation agent powered by Python, IronPython, C# and .NET's DLR (Dynamic Language Runtime), it attempts to weaponize and demonstrate the flexibility that BYOI (Bring Your Own Interpreter) payloads have over traditional C# implants. What are BYOI payloads? Turns out, by harnessing the sheer craziness of the .NET framework, you can embed entire interpreters inside of .NET languages allowing you to natively execute scripts written in third-party languages (like Python) on windows! Not only does this allow you to dynamically access all of the .NET API from a scripting language of your choosing, but it also allows you to still remain completely in memory and has a number of advantages over traditional C# payloads! Essentially, BYOI payloads allow you to have all the "power" of PowerShell, without going through PowerShell in anyway! Additionally, you can nest multiple interpreters within each other to perform what I've coined "engine inception"! If you're interested in bleeding-edge and out of the ordinary C#/.NET offensive trade-craft, this is the demo for you!

</details>

<details><summary><strong>SSHoRTy: Linux/MacOS Armored SSH Implant Delivery With a Smile</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dimitry Snezhkov](https://img.shields.io/badge/Dimitry%20Snezhkov-informational)

🔗 **Link:** Not Available  
📝 **Description:** SSHoRTY is a Linux/MacOS implant attempting to alleviate the challenges Red Teams face at establishing initial foothold on non-Windows machines and initiating clean egress communications to the team C2 servers across a stack of defensive monitoring. Native SSH tunnels with automated port forwards, convenient SOCKS proxy capabilities built right into a reverse shell. All that wrapped in a HTTP/S proxy-aware fully encrypted websocket connection to evade even the most tight policies. Built on demand for every deployment, with a choice of binary-embedded shared keys or out-of-band channels PKI authentication, SSHoRTy is also very progressive. It can even be injected as a shared library into a running process to hide its presence. It assumes nothing, and just gives the Red a consistent, reliable and flexible tunnel into the network.

</details>

<details><summary><strong>The Air-Gap Malware of X-Sploit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jie Fu](https://img.shields.io/badge/Jie%20Fu-informational) ![Yongtao Wang](https://img.shields.io/badge/Yongtao%20Wang-informational) ![Jinglun Li](https://img.shields.io/badge/Jinglun%20Li-informational)

🔗 **Link:** [The Air-Gap Malware of X-Sploit](https://github.com/Trustworthy-AI-Group/Adversarial_Examples_Papers)  
📝 **Description:** X-Sploit is a Linux-based Red-Teaming-Toolkit for IT security experts and geeks. In this presentation, we will introduce a physical penetration tip, the Air-gap malware in X-Sploit Toolkit. The victim device's hardware adapter could be controlled and used for backdoor data transmission without interfering with the target's existing connection status and communication.


Advantage:
Cross-platform support (Windows, Mac OS, Linux)
Bypass Firewall/IDS/IPS
No signature, more difficult to detect
Used in isolate network environment attack
Does not affect the victim's existing connection status and communication

</details>

<details><summary><strong>WIG: Wi-Fi Information Gathering</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Andres Blanco](https://img.shields.io/badge/Andres%20Blanco-informational)

🔗 **Link:** [WIG: Wi-Fi Information Gathering](https://github.com/6e726d)  
📝 **Description:** WIG (Wi-Fi Information Gathering) is a free and open source (GPLv3) utility for IEEE 802.11 device fingerprinting. WIG uses Wi-Fi network interfaces that supports monitor mode to obtain information on nearby devices with Wi-Fi support. The tool supports vendors proprietary protocols such as Apple AirDrop/AirPlay, Cisco Client eXtensions, Wi-Fi Protected Setup (WPS) and Wi-Fi Direct. Using these protocols the tool is able to find and fingerprint potential Wi-Fi targets that other tools are not able to find. The tool output it's useful on the threat modeling phase during wi-fi penetration testing or to find potential targets during a network assessment.

</details>

<details><summary><strong>WMImplant: An Offensive Use Case of WMI</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Chris Truncer](https://img.shields.io/badge/Chris%20Truncer-informational)

🔗 **Link:** [WMImplant: An Offensive Use Case of WMI](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)  
📝 **Description:** When looking forward to the latest defenses that are being seen in environments all over the world today, we're consistently seeing EDR, "Next-Gen AV", and application whitelisting. Of the available defenses, application whitelisting seemed like the most interesting challenge to undertake. We wanted to build something that would work against one of the best application whitelisting solutions from a detection/prevention perspective, Windows Defender Application Control (WDAC), previously known as Device Guard.

WDAC aims to lock down Windows workstations via multiple methods, one example is digital signature based rule enforcement when determining if an application is allowed to execute. Another, is that WDAC automatically enforces PowerShell into Constrained Language Mode (CLM), a severely restricted version of PowerShell. So how can you operate in a restricted WDAC environment?

WMImplant is one possible answer. Why not leverage a service that is built in to Windows and enabled by default since the days of Windows Server 2000? Windows Management Instrumentation (WMI) enables us to execute commands on systems, remotely and locally. WIth the enforcement of PowerShell Constrained Langauge Mode (CLM), our PowerShell based code had to adhere to the restrictions of the language mode. WMImplant is fully PowerShell CLM compliant and is designed to provide a Meterpreter-esque menu for users to easily perform post-exploitation tasks against the targeted system.

Come learn how a CLM compliant code-base designed to operate exclusively over WMI can allow you to survive and thrive in a heavily restricted application whitelisting environment.

</details>

<details><summary><strong>WTS: Scenario-Based WiFi Network Threat Simulation</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Besim Altinok](https://img.shields.io/badge/Besim%20Altinok-informational) ![Legendary Nacar](https://img.shields.io/badge/Legendary%20Nacar-informational) ![Can Kurnaz](https://img.shields.io/badge/Can%20Kurnaz-informational)

🔗 **Link:** Not Available  
📝 **Description:** The WiFi Network Threat Simulation project is designed to perform scenario-based wifi network security tests. Thanks to the modules inside, you can test both the user and AP devices as well as the wireless IDS and IPS devices.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>ACT: Semi-Automated Cyber Threat Intelligence</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Martin Eian](https://img.shields.io/badge/Martin%20Eian-informational)

🔗 **Link:** [ACT: Semi-Automated Cyber Threat Intelligence](https://gist.github.com/georgepar/3d5cda48c50c6ee57f56aaea9b99603d)  
📝 **Description:** ACT is an open-source threat intelligence platform that has been built from the ground up to address the real-world needs of security analysts, incident responders and threat researchers across all industries. The platform is the product of a 3-year collaborative research project between the private sector, security agencies, CERTs and universities.


ACT enables advanced threat enrichment, threat analysis, visualisation, process automation, lossless information sharing and powerful graph analysis. Its modular design and APIs facilitate implementing new workers for enrichment, analysis, information sharing, and countermeasures.


Included in the platform is Scio, a component that ingests human-readable reports, like threat advisories and blog posts, and uses natural language processing and pattern matching to extract structured threat information to import to the platform. Our Github repositories also include support for information import and data enrichment from MISP, MITRE ATT&CK, VirusTotal, PassiveDNS, ShadowServer and Splunk, with more on the way.


So why build yet another threat intelligence platform?
In 2014 we set out to find a platform on the market to meet the needs of our SOC and threat intelligence team. Our requirements were not particularly unique: we needed a platform that would help us to collect and organise our knowledge of threats, facilitate analysis and sharing, and make it easy to retrieve that knowledge when needed. We spent too much time on manual processes, copy-pasting information between different systems. Much of our knowledge was in an unstructured form, like threat reports, that made it difficult and time consuming to figure out if we had relevant knowledge that could help us decide how to handle security alerts and security incidents.


Sound familiar? After evaluating the existing platforms, we concluded they could not easily be adapted to meet our requirements. In speaking with our partners, customers and the security community, we saw we were not alone and decided to research and develop a new platform: ACT.


This session will focus on threat analysis using the GUI to demonstrate how ACT can help SOC analysts, incident responders and threat analysts/hunters/researchers.

Source code: https://github.com/mnemonic-no/act

</details>

<details><summary><strong>An Easy ATT&CK-Based Sysmon Hunter Tool</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Bowen Pan](https://img.shields.io/badge/Bowen%20Pan-informational)

🔗 **Link:** Not Available  
📝 **Description:** This tool delivers a more effective way to APT hunt and IR, and make it even easier to discover un-attributed attacks. Our goal is below:

Find evidence of any phase in cyber attack lifecycle based on the large amount of event logs.
Help to recover the probable ways of intrusion.
We'd like to view APT threat in its whole lifecycle, not just malware, tools and infrastructures.

The next step was to do some research on APT threat hunting, based on incident data analyzing. Our basic concept uses some widely known and classic theory, like ATT&CK and Threat Intelligence. We then tried more practical ways of processing and analyzing incident data and built our own model. The core of this topic will teach you how we standardized data and filtered abnormal behavior, and three major analysis model in our practice, Time-line analysis, Graphic analysis, Statistic analysis. Finally, we will show the practiced cases on some APT group and post-exploitation tools.

Source Code: https://github.com/baronpan/SysmonHunter

</details>

<details><summary><strong>AutoMacTC: Finding Worms in Apple Orchards - Using AutoMacTC for macOS Incident Response</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Kshitij Kumar](https://img.shields.io/badge/Kshitij%20Kumar-informational) ![Jai Musunuri](https://img.shields.io/badge/Jai%20Musunuri-informational)

🔗 **Link:** Not Available  
📝 **Description:** The recent rise of macOS in enterprise environments has not gone unnoticed by adversaries, who often take advantage of unmanaged and unsupervised Mac assets for their misdeeds.

A traditional forensic approach can no longer support enterprise investigations – they require rapid triage and response, often due to resource constraints and a pressing need for answers and remediation. Performing forensic imaging and deep-dive analysis can be incredibly time-consuming and induce data fatigue in analysts, who may only need a select number of artifacts to identify leads and start finding answers. The resources-to-payoff ratio is impractical.

In this presentation, we will discuss AutoMacTC: an open-source Python framework that can be quickly deployed to gather forensic data on macOS devices, from the artifacts that matter most to you and your investigation. Incident response in the macOS world requires that analysts know where to look for evil, gather the relevant data quickly, and know how to discern the malicious from the innocuous. AutoMacTC captures sufficient data into a singular location, equipping responders with all of the above.

</details>

<details><summary><strong>Beagle: Accelerating Incident Response With Graphs</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Omer Yampel](https://img.shields.io/badge/Omer%20Yampel-informational)

🔗 **Link:** Not Available  
📝 **Description:** Beagle is a tool which aims to accelerate an analyst's ability to respond to incidents by allowing them to quickly and reliably generate incident response oriented graphs from a variety of data sources.

Beagle takes, as input, a wide variety of types of data:

Host based logs such as FireEye HX, Sysmon or security event logs.
Full memory images (using volatility).
Sandbox reports such as Cuckoo.
Streamed data from your SIEM.

Beagle also supports inserting alert nodes into your graphs. For example, FireEye HX triages will contain an alert, and the process which it has alerted on. Beagle will automatically insert an alert node, and create the edge between the alert node and what it alerted on.

In Beagle's web interface, analysts can select the data they uploaded and quickly work through the incident. If an alert node is present, the graph will automatically focus on the context around that node based on what the alert node has an edge to, allowing analysts to extremely quickly pivot through an incident. Analysts can pivot between nodes using simple clicks, as well as remove and search for nodes. Additionally, the graphs can be transformed into rooted trees, or seen as timelines (based on what is currently visible in the graph).

Beagle is also easily extended. Do you have a unique data source not yet supported? Implement 7 functions and Beagle will support it. Graph algorithms can also be implemented using networkx, and can be automatically run when a graph is viewed in the browser, allowing you to even further speed up your incident response time.

Beagle: https://github.com/yampelo/beagle

</details>

<details><summary><strong>BLACKPHENIX: Malware Analysis + Automation Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Chris Navarrete](https://img.shields.io/badge/Chris%20Navarrete-informational)

🔗 **Link:** [BLACKPHENIX: Malware Analysis + Automation Framework](https://github.com/fortinet/ips-bph-framework)  
📝 **Description:** Various approaches have been developed through the years for malware analysis and vary from static, dynamic, behavioral, network, memory, and automated. Each analyst has developed his/her own strategy when analyzing malware. However, the accuracy of the results relies densely on their knowledge of system internals, analytical skills, and even reverse engineering. Therefore, novice analysts generate a strict dependency on experienced people to ensure the proper delivery of threat reports.

Even experienced analysts and reverse engineers could miss critical details, such as unexplored code paths, a specific or new self-defense mechanism, a challenging obfuscation algorithm difficult to decipher quickly, or hidden data that was not revealed in early stages. All of this is due to time constraints or a potential lack of information tracking throughout the analysis process.

BLACKPHENIX performs an Intelligent Automation and Analysis by combining all the known malware analysis approaches, automating the time-consuming stages and counter-attacking malware behavioral patterns. The objective: generate precise IOCs by revealing the real malware purpose and exposing its hidden data and related functionalities that are used to exfiltrate or compromise the user's information.

This framework focuses on consolidating, correlating, and cross-referencing the data collected between analysis stages by the execution of Python scripts and helper modules, providing full synchronization between the debugger, disassembler, and supporting components. The automation modules allow interaction with external tools and libraries that can be used to scale the framework functionality by developing plug-ins on top of it, allowing people of any skill level adapt it to their needs and producing actionable threat information in the shape of technical threat reports, IPS/AV signatures or the discovery of new malware attacks, variants or families.

The presentation will include a live demo of the system processing real different categories of malware taken from the wild.

</details>

<details><summary><strong>Cloud Security Suite: One-Stop Tool for AWS/GCP/Azure Security Audit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jayesh Chauhan](https://img.shields.io/badge/Jayesh%20Chauhan-informational)

🔗 **Link:** [Cloud Security Suite: One-Stop Tool for AWS/GCP/Azure Security Audit](https://github.com/jayeshchauhan)  
📝 **Description:** Nowadays, cloud infrastructure is pretty much the de-facto service used by large/small companies. Most of the major organizations have entirely moved to cloud. With more and more companies moving to cloud, the security of cloud becomes a major concern.

While AWS, GCP & Azure provide you protection with traditional security methodologies and have a neat structure for authorization/configuration, their security is as robust as the person in-charge of creating/assigning these configuration/policies. Also, the massive scale at which cloud services are adopted in enterprises, merged with inevitability of human error, often leads to catastrophic damages to the business.

Few vulnerable scenarios:

Security groups/policies, password policy or IAM policies are not configured adequately
S3 buckets and Azure blobs are world-readable
Web servers are supporting vulnerable SSL ciphers
Ports exposed to public with vulnerable services running
If root credentials are used
Logging or MFA is disabled
And many more such scenarios...

Knowing all this, audit of cloud infrastructure becomes a hectic task! There are a few open source tools which help in cloud auditing however none of them provides an exhaustive checklist. Also, setting up all the tools and looking at different result sets is a redundant task. While managing massive infrastructures, system audit of server instances is a challenging task as well.

CS Suite is a one stop tool for auditing the security posture of the AWS/GCP/Azure infrastructures along with server audit feature. CS Suite leverages capabilities of current open source tools and has plethora of custom checks into one tool to rule them all.

</details>

<details><summary><strong>CyBot: Open-Source Threat Intelligence Chat Bot (Platform Enhanced)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tony Lee](https://img.shields.io/badge/Tony%20Lee-informational)

🔗 **Link:** [CyBot: Open-Source Threat Intelligence Chat Bot (Platform Enhanced)](https://github.com/ali-ce/datasets/blob/master/Artificial-Intelligence/ChatterbotsDB.csv)  
📝 **Description:** Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to debut the end result of our research (a chat bot that we affectionately call CyBot) at Black Hat Arsenal Vegas 2017. To build on that momentum we also brought CyBot to Black Hat Europe and Asia to gather more great feedback and ideas from an enthusiastic international crowd. This year's Black Hat Vegas will allow us to share new features that stemmed from Black Hat feedback as well as enhancements provided by a platform upgrade.

Best of all, if you know even a little bit of Python, you can help our global collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!

</details>

<details><summary><strong>EventList</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Miriam Wiesner](https://img.shields.io/badge/Miriam%20Wiesner-informational)

🔗 **Link:** [EventList](https://github.com/miriamxyra)  
📝 **Description:** EventList: What the log?! So many events, so little time...
Detecting adversaries is not always easy - especially when it comes to correlating Windows Event Logs to real-world attack patterns and techniques. EventList helps to match Windows Event Log IDs with the MITRE ATT&CK framework (and vice-versa) and offers methods to simplify the detection in corporate environments worldwide.

Use this tool to:

Import either MSFT Baselines or custom GPOs
Find out immediately which Events are being generated and what MITRE ATT&CK techniques are being covered by the selected Baseline/GPO
Choose MITRE ATT&CK techniques and generate GPOs to generate the events needed for detection
Generate Agent Forwarder Configs to only cover the events needed for the detection (avoid being "Log spammed")
Generate Queries to detect the chosen MITRE ATT&CK techniques, regardless of the SIEM solution used

</details>

<details><summary><strong>IOC Explorer: Correlate IOC in Automatic Way</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Lion Gu](https://img.shields.io/badge/Lion%20Gu-informational)

🔗 **Link:** [IOC Explorer: Correlate IOC in Automatic Way](https://github.com/lion-gu/ioc-explorer)  
📝 **Description:** IOC correlation is usually a manual or semi-automatic work. It takes a lot of time to search multiple data sources and process different IOC types. IOC Explorer aims to introduce an automatic way to search data across major OSINT sources, like VirusTotal. Moreover, recursive searching feature will explore more possible IOCs based on previous IOCs, then build IOC relations automatically.

Source Code: https://github.com/lion-gu/ioc-explorer

</details>

<details><summary><strong>KSBox: A Fine-Grained macOS Malware Sandbox</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yu Wang](https://img.shields.io/badge/Yu%20Wang-informational)

🔗 **Link:** Not Available  
📝 **Description:** Last year I published the Kemon open source project, which included a Pre and Post callback-based kernel inline hook engine. By using this engine, we can easily implement IPC and XPC monitoring, which helps build a fine-grained macOS malware sandbox. Therefore, there will be a new useful tool in our arsenal in August: KSBox.

Currently, KSBox malware sandbox has the following features: process and file operation monitoring; macOS IPC, XPC and network traffic monitoring; dynamic library and kernel extension monitoring; Mandatory Access Control (MAC) policy monitoring and filtering, etc. In short, security analysts can use this project to better analyze and gain insight into macOS malware.

</details>

<details><summary><strong>LMYN: Let's Map Your Network</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Pramod Rana](https://img.shields.io/badge/Pramod%20Rana-informational)

🔗 **Link:** [LMYN: Let's Map Your Network](https://github.com/varchashva/LetsMapYourNetwork)  
📝 **Description:** It is of utmost importance for any security engineer and network administrator to understand their network before securing and managing it, and it becomes a daunting task to have a 'true' understanding of a widespread network. In a mid to large-size organisation's network, having a network architecture diagram doesn't provide a complete understanding, and manual verification is a nightmare. Hence, in order to secure and manage entire network, it is important to have a complete picture of all the systems connected to your network.

BOTTOM LINE - YOU CAN'T SECURE WHAT YOU ARE NOT AWARE OF.

LetsMapYourNetwork (LMYN) aims to provide an easy-to-use interface to visualise any network in graphical-form with zero manual error at any point-of-time, where a node represents a system and relationship between nodes represents the connection.

Key Features

Project management
Bulk load of existing CMDB
Ability to perform on-demand network activities
Cloud (AWS) support
Enumeration
Ability to analyse 'interesting' network only
Continuous monitoring
Segregation of backend activities and UI
Docker support

</details>

<details><summary><strong>Malboxes</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Olivier Bilodeau](https://img.shields.io/badge/Olivier%20Bilodeau-informational) ![Maxime Carbonneau](https://img.shields.io/badge/Maxime%20Carbonneau-informational)

🔗 **Link:** [Malboxes](https://github.com/GoSecure/malboxes/releases)  
📝 **Description:** Malboxes is a tool to streamline and simplify the creation and management of virtual machines used for malware analysis.

Building analysis machines is a tedious task. One must have all the proper tools installed on a VM such as a specific version of vulnerable software (ie: Flash), Sysinternal tools, debuggers (Windbg), network traffic analyzers (Wireshark), man-in-the-middle tools (Fiddler). One must also avoid leaking his precious proprietary software licenses (IDA). At the moment, this menial job is not automated and is repeated by every analyst.

Malboxes leverages the DevOps principle of infrastructure as code to enable researchers to automatically create fully operational and reusable analysis machines. The tool uses Vagrant and Packer to do an initial out-of-band bootstrapping. Afterward, chocolatey is used to install further tools benefiting from the chocolatey package repository.

Attendees will learn a simple tool for safe malware analysis practice that is easy to grasp, enabling them to start doing analysis faster. Seasoned malware researchers will also gain from this demo by seeing how the DevOps approach can be applied to simplify and accelerate their labs' malware reverse-engineering capacity or reduce its management overhead.

</details>

<details><summary><strong>MalConfScan with Cuckoo: Automatic Malware Configuration Data Extraction and Memory Forensic</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tomoaki Tani](https://img.shields.io/badge/Tomoaki%20Tani-informational) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational)

🔗 **Link:** Not Available  
📝 **Description:** "MalConfScan with Cuckoo" is a tool for automatically extracting known malware configuration data. With the growing number of malware variants emerging day by day, the automation of malware analysis using sandbox systems is becoming popular. Such systems have a function to list malware behavior on Windows OS, such as communication, file and registry creation. On the other hand, malware analysts spend more time extracting malware configuration data rather than analyzing malware behavior. There are two reasons for it:

1. Many malware variants mostly share the same code except for configuration data. In other words, a type of malware and configuration data are the only elements that need to be checked.

2. Malware configuration data contains an attack campaign ID and communication encryption keys. This information would be the critical data for investigating logs in incident response, and also for knowing the actor's target.

We present a malware analysis tool to extract configuration data for incident responders and malware analysts. This tool automates analysis for many types of malware based on our long-time research and, reduce the time spent on malware analysis. In addition, this tool can be used not only for malware analysis but also for memory forensics. It can help a victim organization with malware infection to identify C2 server information and encryption key which are necessary for their incident response.

</details>

<details><summary><strong>MoP: Master of Puppets - Open Source Super Scalable Advanced Malware Tracking Framework for Reverse Engineers</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Omri Ben-Bassat](https://img.shields.io/badge/Omri%20Ben-Bassat-informational)

🔗 **Link:** Not Available  
📝 **Description:** MoP ("Master of Puppets") is an open source framework for reverse engineers who wish to create and operate trackers for new malware found in the wild for research purpose. To make it simple - MoP framework takes care of all the generic malware tracker stuff so the reverse engineer is left with pure reverse engineering work, You only need to implement a simple plugin on top of MoP which describes the malware's network protocol. MoP ships with a variety of workstation simulation capabilities, such as fake filesystem manager and fake process manager, multi-worker orchestration, TOR integration and more, all aiming to deceive adversaries into interacting with our simulated environment and possibly drop new unique samples. Since everything is done in pure python, no virtual machines or Docker containers are needed and no actual malicious code is executed, all of which enables us to scale up in a click of a button, connecting to potentially thousands of different malicious servers at once from a single instance running on a single laptop. MoP framework comes with a number of pre-built plugins for known RATs, such as NjRAT and Gh0stRAT which will be showcased live with real command and control servers!

</details>

<details><summary><strong>Real-Time Detection Tool of High-Risk Attacks Leveraging Kerberos and SMB</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mariko Fujimoto](https://img.shields.io/badge/Mariko%20Fujimoto-informational) ![Wataru Matsuda](https://img.shields.io/badge/Wataru%20Matsuda-informational) ![Takuho Mitsunaga](https://img.shields.io/badge/Takuho%20Mitsunaga-informational)

🔗 **Link:** Not Available  
📝 **Description:** In Advanced Persistent Threat (APT) attacks, attackers tend to attack against the Active Directory. Especially vulnerabilities fixed in MS14-068 and MS17-010 have been leveraged to get administrator privileges. Attackers who can get administrator privileges likely create "Golden Ticket" and "Silver Ticket" to disguise themselves as arbitrary administrative accounts for a long period. However, detecting these attacks is quite difficult since legitimate accounts and processes are leveraged. Since sometimes attackers successfully accomplish lateral movement in a short period, immediate detection is needed.

We will introduce a real-time detection tool for the following attack activities against Active Directory using Event logs and Kerberos packets.
-Attacks leveraging the vulnerability fixed in MS14-068 and MS17-010
-Attacks using Golden Ticket
-Attacks using Silver Ticket

We introduced the detection tool for Golden Ticket from Event Logs in Black Hat Europe 2018, but sometimes false positive occurs because of the Kerberos specification. In this time, we introduce the improved tool. The detection rate is improved, and introduce a new feature to detect Silver Ticket attacks.

Our tool can detect attacks against Windows 2008 R2, 2012, 2016. Additionally, our tool utilizes only Domain Controller's built-in Event Logs and minimum Kerberos packets. Thus, it can be implemented in easy way and helps immediate incident response.

Finally, ATT&CK, a knowledge base of adversary tactics and techniques, is becoming common recently. The tool can identify the possible tactics for each detected attack activity automatically.

Source code: https://github.com/sisoc-tokyo/Real-timeDetectionAD_ver2

</details>

<details><summary><strong>RedHunt-OS v2: Virtual Machine for Adversary Emulation and Threat Hunting</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sudhanshu Chauhan](https://img.shields.io/badge/Sudhanshu%20Chauhan-informational) ![Kunal Aggarwal](https://img.shields.io/badge/Kunal%20Aggarwal-informational)

🔗 **Link:** Not Available  
📝 **Description:** The ultimate aim of any security exercise (offensive or defensive) is to make the organization more resilient and adaptive towards modern adversaries. RedHunt OS (Virtual Machine) from RedHunt Labs aims to provide defenders a platform containing the toolset to emulate adversaries as well as advanced logging and monitoring setup to actively hunt such adversaries.

The project aims to provide a one-stop shop which defenders can quickly spin up and practice blue team exercises in the presence as well as the absence of an active attacker. On the other hand, the red team can utilize the platform to identify and understand the footprints they leave behind during a red team exercise. Apart from Adversary Emulation and Threat Hunting tools, the OS also provides Open Source Intelligence (OSINT) and Threat Intelligence tools. Both red and blue teams can utilize the setup to become better at what they do, ultimately leading to better security.

</details>

<details><summary><strong>SilkETW: Collecting Actionable ETW Data</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ruben Boonen](https://img.shields.io/badge/Ruben%20Boonen-informational)

🔗 **Link:** [SilkETW: Collecting Actionable ETW Data](https://github.com/FuzzySecurity/BH-Arsenal-2019)  
📝 **Description:** Event Tracing for Windows (ETW) provides researchers with a rich data set which can be leveraged both for defensive as well as offensive purposes. ETW collectors can alert the user to malicious behavior such as user-land APC injection from the Kernel, or equally, allow an attacker to spy on keyboard and mouse activity. The scope for ETW research is large but the information security community has been slow to adopt it. The two primary problems with ETW are: the complexities involved in event collection, and the volume of data that is generated.

SilkETW is a flexible C# ETW wrapper which attempts to mitigate the aforementioned issues by providing a straightforward interface for data collection, various filtering mechanics, and an output format that can be easily processed. ETW output can be written locally to disk, to the Windows event log or shipped off (using POST requests) to 3rd party infrastructure such as Elasticsearch.

This project was originally implemented by the FireEye Advanced Practices (AP) team to aid in the rapid analysis of novel attacker trade-craft, and to feed that analysis back into the detection engineering process.

</details>

<details><summary><strong>Splunk Threat Hunting Application</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Olaf Hartong](https://img.shields.io/badge/Olaf%20Hartong-informational)

🔗 **Link:** [Splunk Threat Hunting Application](https://github.com/olafhartong/ThreatHunting)  
📝 **Description:** This is a Splunk application containing several dashboards and over 120 reports that will facilitate initial hunting indicators to investigate. One of the reasons this app was created is because the endpoint is an often used entry way into a network. There are quite some Endpoint Detection & Remediation (EDR) solutions out there and most of them are quite good; however, they can be costly and not everyone is able to afford that (yet).

The goal was to create an alternative approach to the detection aspect, using the MITRE ATT&CK framework and work with the existing environment. It allows you to leverage your existing data platform, in this case Splunk.

</details>

<details><summary><strong>SysmonX: An Augmented and Community-Driven Drop-In Replacement of Sysmon</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Marcos Oviedo](https://img.shields.io/badge/Marcos%20Oviedo-informational) ![Joel Spurlock](https://img.shields.io/badge/Joel%20Spurlock-informational)

🔗 **Link:** [SysmonX: An Augmented and Community-Driven Drop-In Replacement of Sysmon](https://github.com/marcosd4h/sysmonx)  
📝 **Description:** Sysmon is a free and powerful host-level tracing tool, developed by an epic team at Microsoft, which has been widely adopted and deployed by defenders over the last few years. The tool provides a free alternative for those who want to augment the Microsoft Windows Auditing Capabilities, effectively enabling them to detect anomalous endpoint behaviors and to perform threat-hunting activities over the collected data.

Despite providing a lot of features, Sysmon main disadvantage is around its closed-source nature. Not having the ability to extend the tool data collection or to extend the way that the tool filters, aggregate and logically correlate events are impacting on the tool's ability to keep up with the current threat landscape. What is more, the infosec community is not empowered to fix the well-known subversion and evasion techniques created to bypass tool auditing (i.e Matt Graeber talk at BH USA 18).

Introducing SysmonX: SysmonX is an open-source, community-driven, and drop-in replacement version of Sysmon that provides a modularized architecture with the purpose of enabling the infosec community to:

Extend the Sysmon data collection sources and create new security events
Extend the Sysmon ability to correlate events. Effectively enabling new logical operations between events and the creation of advanced detection capabilities
Enrich the current set of events with more data!
Enable the false positive reduction by narrowing down suspicious events through dedicated scanners
Extend the security configuration schema
React to known subversion and evasion techniques that impact Sysmon, and by doing so, increasing the resilience of security auditing and data collection mechanism such as this one.

SysmonX is composed of a standalone binary that gets itself deployed as a windows service, supports legacy Sysmon configurations and event reporting mechanism, while also providing users the ability to configure all the SysmonX aspects through command-line interface. The SysmonX binary is a drop-in replacement of Sysmon. This effectively means that SysmonX is a feature-compatible version of Sysmon (same input, same output). This is possible thanks to the SysmonX ability to package, deploy, manage Sysmon binaries behind the scene. SysmonX uses this to intercept data collected by Sysmon drivers, enrich them, along with the ability to create, combine, and add scanning logic on top of new security events. The result is a combined output, with the old good features from Sysmon + the new features from SysmonX.

Example of new security events and features added to SysmonX are:

Cmdline and Parent Process Spoofing detection
WMI calls over all the namespaces, not just root:subscription
Ability to collect authentication information
Ability to collect powershell events
Ability to collect DNS lookups
Ability to detect userspace injection techniques (eventing + memory inspection through built in scanner modules)
Ability to perform regex over security event fields
Many more!

Source Code: https://github.com/marcosd4h/sysmonx

</details>

<details><summary><strong>Trash Taxi: Taking Out the Garbage in Your Infrastructure</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Cable](https://img.shields.io/badge/Patrick%20Cable-informational)

🔗 **Link:** [Trash Taxi: Taking Out the Garbage in Your Infrastructure](https://github.com/jiayiwangjw/pythonstudy/blob/master/001_Essential%20notes002.py)  
📝 **Description:** Auditors dream of a world in which they can guarantee that few possess unrestricted administrator access. Yet, developers and operations staff often need to debug complex events - that only occur with load - in production. How can we balance the need to grant occasional superuser access with the incentive to ensure changes make their way back into configuration management, while reducing the risk of configuration drift? We built Trash Taxi to help us understand why people use "sudo -i," and also clean up hosts that have had arbitrary commands run on them by "taking out the trash" as in: terminating them.

</details>

<details><summary><strong>TSURUGI Linux Open Source Project: DFIR Investigations, Malware Analysis and OSINT Activities Made Easy</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Giovanni Rattaro](https://img.shields.io/badge/Giovanni%20Rattaro-informational) ![Marco Giorgi](https://img.shields.io/badge/Marco%20Giorgi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
A Tsurugi Linux special BLACKHAT EDITION will be released and shared with the participants.

</details>

<details><summary><strong>VECTR: Purple Teams Simulation Platform</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Chris Salerno](https://img.shields.io/badge/Chris%20Salerno-informational) ![Phil Wainwright](https://img.shields.io/badge/Phil%20Wainwright-informational)

🔗 **Link:** [VECTR: Purple Teams Simulation Platform](https://github.com/Brian-MacMonigle/typing-speed-website/blob/master/WordFilter.py)  
📝 **Description:** VECTR is a free tool and platform designed to facilitate your red and blue security teams through comprehensive purple team threat simulations. Document your attacks, develop metrics, gauge the effectiveness of your defensive tools, and improve your detection capabilities through historical performance tracking. We'll demo how to operationalize your purple teams and show measurable progress of your program with live test cases and simulations.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Alexa HackerMode 2.0: Voice Auto Pwn Using Kali Linux and Alexa Skill Combo</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![David Cross](https://img.shields.io/badge/David%20Cross-informational) ![Cate Jennison](https://img.shields.io/badge/Cate%20Jennison-informational) ![James Blackburn](https://img.shields.io/badge/James%20Blackburn-informational)

🔗 **Link:** [Alexa HackerMode 2.0: Voice Auto Pwn Using Kali Linux and Alexa Skill Combo](https://github.com/xssninja/HackerMode2.0)  
📝 **Description:** HackerMode 2.0 code-named: "Death Star" is an Alexa driven auto-sploit tool designed for the cloud. Not only will it help with syntax and encodings, but it will go full hacker mode and exploit systems automatically for you.

"Alexa, ask HackerMode to hack IP address 192.168.1.135" will instruct Alexa to begin and manage the process of port scanning, fingerprinting, exploit selection, and smart brute forcing exploits through Metasploit 4 or 5.

Alexa will entertain you with mood music or various other activities while it roots and dumps users and passwords from your target. If the exploit is taking a while you can check in on the progress by asking "How's the hack going?"

</details>

<details><summary><strong>EXPLIoT: IoT Security Testing and Exploitation Framework</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Aseem Jakhar](https://img.shields.io/badge/Aseem%20Jakhar-informational) ![Murtuja Bharmal](https://img.shields.io/badge/Murtuja%20Bharmal-informational)

🔗 **Link:** Not Available  
📝 **Description:** EXPLIoT

noun
/ɛkˈsplʌɪəti:/

A Framework for security testing and exploiting IoT products and IoT infrastructure. It provides a set of plugins (test cases) which are used to perform the assessment and can be extended easily with new ones. The name EXPLIoT (pronounced expl-aa-yo-tee) is a pun on the word exploit and explains the purpose of the framework i.e. IoT exploitation. It is developed in python3.

It can be used as a standalone tool for IoT security testing and more interestingly, it provides building blocks for writing new plugins/exploits and other IoT security assessment test cases with ease. EXPLIoT supports most IoT communication protocols, hardware interfacing functionality and test cases that can be used from within the framework to quickly map and exploit an IoT product or IoT Infrastructure.
It will help the security community in writing quick IoT test cases and exploits. The objectives of the framework are:
1. Easy of use
2. Extendable
3. Support for hardware, radio and IoT protocol analysis

Currently, the framework has support for analyzing and exploiting various IoT, radio and hardware protocols. The current suite includes:
- BLE
- CAN
- DICOM (Will be fully implemented before the conference)
- MQTT
- Modbus
- I2C
- SPI
- UART

We are also very happy to announce that we have released a comprehensive documentation including User and Developer guide to help the security community kick start quickly and easily with the framework. Source code and documentation is available here - https://gitlab.com/expliot_framework/expliot

We are currently working on plugins for medical, radio and hardware analysis and will release it at Blackhat.

</details>

<details><summary><strong>LoRaWAN Auditing Framework</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Esteban Martinez Fayo](https://img.shields.io/badge/Esteban%20Martinez%20Fayo-informational) ![Matias Sequeira](https://img.shields.io/badge/Matias%20Sequeira-informational)

🔗 **Link:** Not Available  
📝 **Description:** IoT deployments continue to grow, and one part of that significant growth is composed of millions of LPWAN (low-power wide-area network) sensors deployed in hundreds of cities (Smart Cities) around the world, also in industries and homes. One of the most used LPWAN technologies is LoRa for which LoRaWAN is the network standard (MAC layer). LoRaWAN is a secure protocol with built in encryption, but implementation issues and weaknesses affect the security of most current deployments.

This project intends to provide a series of tools to craft, parse, send, analyze and crack a set of LoRaWAN packets in order to audit or pentest the security of a LoraWAN infrastructure.

</details>

<details><summary><strong>Medaudit: Auditing Medical Devices and Healthcare Infrastructure</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Anirudh Duggal](https://img.shields.io/badge/Anirudh%20Duggal-informational)

🔗 **Link:** [Medaudit: Auditing Medical Devices and Healthcare Infrastructure](https://github.com/anirudhduggal/medaudit)  
📝 **Description:** Medaudit is a healthcare/ medical device auditing tool that would help anyone auditing a healthcare networks and medical devices. At the time of writing, there are no tools - commercial or free - that can help security pentest healthcare infrastructure. This tool aims to close that gap and help security analysts use their web app skill set to analyze medical devices. The tool support HL7 protocol right now and will have support for FHIR and DICOM in near future.

The tool does the following things:

Create a visual map of HL7 traffic flow on a network (Passive analysis), extract HL7 traffic on the network.
Scan and verify for open HL7 ports on a host
Perform DOS attacks against HL7 streams on HL7 reciever
Send HL7 messages (malformed attacks)
Fuzzer
Malicious HL7 Server

The tool also acts a proxy using web API so you can reuse web application tests on medical devices.

</details>

<details><summary><strong>ShodanSeeker: Command-Line Tool Using Shodan API</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Laura Garcia](https://img.shields.io/badge/Laura%20Garcia-informational)

🔗 **Link:** [ShodanSeeker: Command-Line Tool Using Shodan API](https://github.com/laincode)  
📝 **Description:** The large number of assets published on the Internet - some of which organizations are not even aware of their existence - increase the probability of services being exposed that could put them at risk. As a first step towards resolving this problem, we introduce ShodanSeeker.

Taking advantage of Shodan's crawlers, ShodanSeeker analyzes historical records on-the-fly to discover differences between previously performed scans in order to identify new published services.

Enhancing the capabilities of Shodan's real-time stream of data, our fully customizable solution monitors and generates notification messages once a new risk service is discovered.

Presentation slides: https://drive.google.com/open?id=1Fi5XJ5-1QyXSawHKXVm_emF3NUR2Nx7X

</details>

---
## Others
<details><summary><strong>Arsenal Intro to Open Source Meet-Up: Day 1</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Nabil Ouchn](https://img.shields.io/badge/Nabil%20Ouchn-informational) ![Rachid Harrando](https://img.shields.io/badge/Rachid%20Harrando-informational) ![Maximiliano Soler](https://img.shields.io/badge/Maximiliano%20Soler-informational)

🔗 **Link:** Not Available  
📝 **Description:** Visit the Arsenal Lounge for a meet-up with the Arsenal Review Board and other tool authors. This casual gathering will allow you to discuss your current projects, receive feedback from the ToolsWatch team, connect with other open source contributors, and learn about the Arsenal program and how to become a presenter!

</details>

<details><summary><strong>Arsenal Intro to Open Source Meet-Up: Day 2</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Maximiliano Soler](https://img.shields.io/badge/Maximiliano%20Soler-informational) ![Nabil Ouchn](https://img.shields.io/badge/Nabil%20Ouchn-informational) ![Rachid Harrando](https://img.shields.io/badge/Rachid%20Harrando-informational)

🔗 **Link:** Not Available  
📝 **Description:** Visit the Arsenal Lounge for a meet-up with the Arsenal Review Board and other tool authors. This casual gathering will allow you to discuss your current projects, receive feedback from the ToolsWatch team, connect with other open source contributors, and learn about the Arsenal program and how to become a presenter!

</details>

<details><summary><strong>Cylon-6: An EDID Fuzzer Based on Raspberry Pi Hardware</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Wei Wang](https://img.shields.io/badge/Wei%20Wang-informational)

🔗 **Link:** Not Available  
📝 **Description:** EDID stands for "Extended Display Identification Data", is a data format for monitors to describe thier capabilities, such as screen size or resolutions. EDID is transmitted to graphics card through DDC, a data channel based on I2C bus, which directly bridges the graphics card and EEPROM inside display devices.

The EDID data (128 or 256 Bytes) is stored in EEPROM. So, there is an attack scenario by messing with EDID data. Andy Davis already made a speech at BlackHat EU 2012 to show his research on fuzzing EDID and CEC, and he did find some vulnerabilities or problems. However, Raspberry Pi (RPi) was not widely used at the time when Andy chose Arduino to do the job. So, we build an EDID fuzzer based on RPi, making it rather easy to perform EDID fuzzing.

We make RPi to work as an I2C slave device with the help of GPIO, and simulate EEPROM operations to act like a real EEPROM device. Thus we can return any data back to operating system when VGA or HDMI cable is plugged in. Besides, this tool is also able to attach and detach the "display" automatically, by setting high or low voltage on the "hotplug" pin inside VGA and HDMI interfaces.

In general, this tool is will assist security researchers to perform EDID fuzzing against any kinds of graphics drivers, without knowing about I2C protocol or EEPROM. All we need is a RPi (2 or later) , and use some dupont lines to connect the RPi to VGA/HDMI interfaces. The code and documents will be available on Github as soon as been fully tested. And we will appreciate it if anyone interested in this project helps to improve it and make it a powerful tool for IoT security filed.

Source code: https://github.com/kings-way/cylon-6

</details>

<details><summary><strong>FACT 3.0: Firmware Analysis and Comparison Tool</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Johannes vom Dorp](https://img.shields.io/badge/Johannes%20vom%20Dorp-informational)

🔗 **Link:** [FACT 3.0: Firmware Analysis and Comparison Tool](https://github.com/osmc/kernel-package-tool-osmc/blob/master/debian/changelog)  
📝 **Description:** The Firmware Analysis and Comparison Tool (FACT) is intended to automate firmware security analysis. Thereby, it shall be easy to use (web GUI), extend (plug-in system) and integrate (REST API). When analyzing Firmware, you face several challenges: unpacking, initial analysis, identifying changes towards other versions, find other firmware images that might share vulnerabilities you just found. FACT is able to automate many aspects of these challenges leading to a massive speed-up in the firmware analysis process. This means you can focus on the fun part of finding new vulnerabilities, whereas FACT does all the boring stuff for you.

</details>

<details><summary><strong>Objection: Runtime Mobile Exploration</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Leon Jacobs](https://img.shields.io/badge/Leon%20Jacobs-informational)

🔗 **Link:** [Objection: Runtime Mobile Exploration](https://github.com/leonjza)  
📝 **Description:** Objection is a runtime mobile exploration toolkit, powered by Frida. It was built with the aim of helping assess mobile applications and their security posture without the need for a jailbroken or rooted mobile device. Objection allows for many common pentesting tasks to be performed such as disabling SSL inspection, interacting with the applicable platforms keystore/keychain as well as the ability to upload/download files from a device. Additionally, more advanced usage such as code path tracing and live Java object inspection, to name a few, is possible.

</details>

<details><summary><strong>Smalien</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Hiroki Inayoshi](https://img.shields.io/badge/Hiroki%20Inayoshi-informational) ![Kazuya Aoki](https://img.shields.io/badge/Kazuya%20Aoki-informational)

🔗 **Link:** Not Available  
📝 **Description:** Investigating how an application handles sensitive information is essential for mobile security researchers to understand behavior of the application and determine whether it is harmless or malicious. Our information flow analysis and information leakage detection tool, called Smalien, should be a good buddy when you start a journey of Android application analysis. Once you give an application to Smalien, it understands the application thoroughly by executing static information flow analysis of Dalvik bytecode files extracted from the application. Smalien performs not only static analysis but also dynamic analysis, implicit information flow detection, and privacy policy enforcement at runtime by parasitizing the application. Smalien instruments additional bytecode to the application, and the bytecode executes dynamic analysis when the application has launched on an Android device.
Smalien has following functions, and we will give a demonstration of it with real-world applications during the tool session.


Smalien analyzes an Android application statically and gathers information of classes, methods, variables, etc.
Smalien presents the results of the analysis graphically such as a method call graph and an information flow diagram
Smalien performs dynamic taint analysis on an Android device
Smalien enforces privacy policy specified by an analyst
Smalien detects information leakage due to implicit information flows
Smalien logs actual information operated by any bytecode or API call, such as http request, at runtime to encourage an analyst in his/her inspection

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>ARSENAL LAB - Applied Hardware Attacks: Prototyping Malicious Hardware on the Cheap</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Joe FitzPatrick](https://img.shields.io/badge/Joe%20FitzPatrick-informational) ![Mike Grover](https://img.shields.io/badge/Mike%20Grover-informational) ![Chris Gammell](https://img.shields.io/badge/Chris%20Gammell-informational) ![Piotr Esden-Tempski](https://img.shields.io/badge/Piotr%20Esden-Tempski-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>ARSENAL LAB - ICU-ICS: An ICS Assessment Framework Tool</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Jeff Gellner](https://img.shields.io/badge/Jeff%20Gellner-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>ARSENAL LAB - JTAGulator: Assisted Discovery of On-Chip Debug Interfaces</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational)

🔗 **Link:** [ARSENAL LAB - JTAGulator: Assisted Discovery of On-Chip Debug Interfaces](https://github.com/RakhithJK/Cyber-Security_Collection/blob/master/Readme_en.md)  
📝 **Description:** For over five years, the JTAGulator has been the de facto open source tool for identifying interfaces commonly used for hardware hacking, such as JTAG and UART, from a target product's test points, vias, component pads, or connectors. The tool bridges the gap between gaining physical access to circuitry and exploiting it, and can save a significant amount of effort compared to traditional reverse engineering processes. For the first time at Black Hat Arsenal, attendees will have the opportunity to play with the JTAGulator and a variety of real-world embedded devices in an informal, hands-on environment.

</details>

<details><summary><strong>ARSENAL LAB - ZigBee Hacking: Smarter Home Invasion with ZigDiggity</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Francis Brown](https://img.shields.io/badge/Francis%20Brown-informational) ![Matthew Gleason](https://img.shields.io/badge/Matthew%20Gleason-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🔍 OSINT
<details><summary><strong>Attack Surface Mapper: Automate and Simplify the OSINT Process</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Andreas Georgiou](https://img.shields.io/badge/Andreas%20Georgiou-informational) ![Jacob Wilkin](https://img.shields.io/badge/Jacob%20Wilkin-informational)

🔗 **Link:** Not Available  
📝 **Description:** Reconnaissance is an integral part of the testing process. Successfully scanning and footprinting the attack surface can assist Red Teamers in crafting precise attacks, but can also help defenders identify weak spots.

Attack Surface Mapper aims to automates and simplify the OSINT process. It does this by taking a target domain as input, then analysing it using passive OSINT techniques and (optional) active reconnaissance methods. It expands the attack surface automatically with the aim to provide actual useful intelligence for an engagement.

This means that you can plug in a target domain, make a cup of tea and come back later to collect:

Email
Usernames
Breached Passwords
Phone Numbers
Linked IPs
Target subdomains
Website Maps
Social Media Presences
Open Ports

This is a list of techniques that Attack Surface Mapper uses:

[+] Reconnaissance:

Find IPs from ASN
Find Subdomains
BruteForce Subdomains
Port Scanning
Hostname Discovery
Passive & Active DNS Record capturing
WHOIS records
Take screenshots of web portals and remote services

[+] Intel Extraction:

Content Discovery (Phone Number, Addresses and Vacancy Postings)
Scrap LinkedIn Employee Names & Email addresses
Check Public Breaches
Find AWS buckets
Interesting Files (e.g PDF and XML)
Interesting Strings (sensitive data such us API keys, AWS secret keys and CreditCard numbers).

[+] Plugins:

Support for Shodan API
Support for dnsdumpster [Generate a DNS map]

</details>

<details><summary><strong>CertPivot: Infra-Chaining + Cert-Check</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Ajit Hatti](https://img.shields.io/badge/Ajit%20Hatti-informational)

🔗 **Link:** Not Available  
📝 **Description:** CertPivot is a newest module of LAMMA specifically focuses on 2 features. One is Infra-Chaining using TLS certificates and second Cert-Check which looks for non-trusted TLS certificates in the trust store of a given machine.

Infra-Chaining feature of CertPivot module is useful specially for threat hunters and incident respondents, where as Certi-Check feature can be additionally used by admins and crypto-auditors

</details>

<details><summary><strong>Dradis Framework: Combine the Output of 20 Scanners and Automate Your Reporting</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [Dradis Framework: Combine the Output of 20 Scanners and Automate Your Reporting](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Docs_and_Reports.md?plain=1)  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration and reporting tool. It can import from 20+ popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007, Dradis Framework is still downloaded 400+ **per week**. Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.

If you're still reviewing your scan results manually, or putting together your reports by hand, or sending emails to your colleagues to coordinate your projects, or copying and pasting findings from old reports instead of having a findings database, you need to check Dradis out. Some of the features that set Dradis apart are:

Built in testing methodologies (OWASP, OSTMM, PTES,...)
Flexible reporting
Team collaboration: commenting, notifications, Slack integration
Burp extension
Full REST API coverage to build your own integrations
Dozens of open-source plugins to inspire your own
Solid community of users
Best tool to prepare your OSCP certification

If you're looking for a collaboration tool that has a track record, is open source, and keeps improving every day (there have been over 850 improvements and 4 major releases, since last year), come and visit our Arsenal station.

</details>

<details><summary><strong>PasteHunter: Scanning Pastebin with Yara Rules</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Kevin Breen](https://img.shields.io/badge/Kevin%20Breen-informational)

🔗 **Link:** [PasteHunter: Scanning Pastebin with Yara Rules](https://github.com/InQuest/awesome-yara)  
📝 **Description:** From a security analytics and Threat Intelligence perspective, Pastebin is a treasure trove of information. All content that is uploaded to Pastebin and not explicitly set to private (which requires an account) is listed and can be viewed by anyone.

Hackers and script kiddies are quick to push their warez on to the site for the world to see and developers/network engineers are prone to accidentally leaking internal configurations and credentials. Anyway, how can we the lowly security analyst sift through all this data and use it to our advantage? We can scrape Pastebin and check all the data uploaded to see if any of it is of interest to us. There are some tools that can monitors paste sites with a set of regular expressions but I wanted more control and flexibility.

Having used Yara extensively in Malware analysis and Threathunting I saw it as a powerful method for quickly scanning large amounts of data and identifying the contents.

Over the last two years of development Pastehunter has grown to include modular inputs that can read from any data source and process the data in to a searchable indexed data set that also has the ability to send notifications with minutes of data matching your rules going public.

Inputs include Pastebin, Github Gists and all StackExchange posted questions. Ouptuts include Elastic Search and SMS / WhatsApp / Slack amongst others.

</details>

<details><summary><strong>Spartacus as a Service (SaaS): Privacy via Obfuscation</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Mike Kiser](https://img.shields.io/badge/Mike%20Kiser-informational)

🔗 **Link:** Not Available  
📝 **Description:** The Third Servile War was over. The slave army has been defeated, and the survivors are offered a pardon by their Roman captors. The only requirement was that they identify Spartacus, their leader (Kirk Douglas). Rather than give away his identity, however, they all begin to yell out "I'm Spartacus!"—thus preserving his anonymity by overwhelming the Romans with possibilities. (Spoiler alert: they all die as a result.)

Since users cannot rely on governments to ensure privacy, a different method of privacy assurance is proposed: privacy through obfuscation.

"Spartacus as a Service (SaaS)" is an open-source proof-of-concept is introduced that facilitates these obfuscation techniques. This will allow for automatic obfuscation of a chosen identity on a small scale, and lessons learned from its usage will be discussed.

Additional information:

Current version at: https://github.com/derrumbe/Spartacus-as-a-Service
Open-source tool written largely in Node.js under an MIT license
Development is ongoing, and this is expected to be a long-term project (first official release would coincide with BlackHat/DefCon)
Authorization for obfuscation is done via OAuth for a signed in user (explicit consent is therefore given)
Additional resources have been incorporated to accommodate this content. A Markov chain is used to generate new content based on a textual repository (ranging from political platforms to the oft-used Jane Austen canon to Aaron Franklin's book on BBQ (he's a big deal here in Austin.)) Amazon Mechanical Turk may be used to circumvent bothersome pieces such as captchas.
Note that this is not a tool that *prevents* targeted advertising and the like, instead it seeks to dilute the value of information that companies know about a user, masking the true information from the fake, so that it is impossible to tell what the real content (or in some cases, who the person) actually is.

</details>

<details><summary><strong>TALR: Automating the Sharing and Ingestion of SIEM Rules</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Nick Ascoli](https://img.shields.io/badge/Nick%20Ascoli-informational) ![Kevin Foster](https://img.shields.io/badge/Kevin%20Foster-informational)

🔗 **Link:** [TALR: Automating the Sharing and Ingestion of SIEM Rules](https://github.com/SecurityRiskAdvisors/TALR)  
📝 **Description:** Keeping up with the evolving landscape of attacker techniques can feel like an uphill battle. Many organizations use a SIEM to perform log correlation and analysis and can attest that keeping rules current is a challenge. To combat the burden of keeping pace with the offensive community, this presentation will detail a new initiative to develop, share, and assess the latest and greatest in alerting logic—the Threat Alert Logic Repository (TALR). TALR is a repository of curated SIEM rules, designed for quick and easy ingestion in to the SIEM tool of your choice. The TALR repository is a publicly available TAXII server intended to keep SIEM engineers and analysts up-to-date on the latest and greatest detection logic. The TALR agent will provide a means to submit new rules to the repository, and to download updates for the latest detection rules (using our repository, or any TAXII server hosting TALR formatted SIEM content).

Attendees will gain a comprehensive overview of TALR and understand how to incorporate it into their environments as a way to remain on the cutting edge of alerting logic, and as a means of enacting more contextualized and informed response.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Azucar: Multi-Threaded Plugin-Based Tool to Help Assess the Security of Azure Cloud Environment Subscription</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Juan Garrido](https://img.shields.io/badge/Juan%20Garrido-informational)

🔗 **Link:** [Azucar: Multi-Threaded Plugin-Based Tool to Help Assess the Security of Azure Cloud Environment Subscription](https://github.com/nccgroup/azucar/blob/master/Azucar.ps1)  
📝 **Description:** Azucar is a multi-threaded plugin-based tool to help assess the security of Azure Cloud environment subscription. By leveraging the Azure API, Azucar automatically gathers a variety of configuration data and analyses all data relating to a particular subscription in order to determine security risks.

</details>

<details><summary><strong>CSF: Container Security Framework</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Vaibhav Gupta](https://img.shields.io/badge/Vaibhav%20Gupta-informational)

🔗 **Link:** Not Available  
📝 **Description:** There are billions of containers started by organizations on a daily basis. Thus, there has been a considerable need to invest in container security along with the security for conventional compute instance (like a physical machine, AWS EC2, etc.). Currently, there is no open-source automated solution that enables the organization to constantly monitor security hygiene of their container ecosystem.

ArmourBird CSF - Container Security Framework is an extensible, modular, API-first framework build for regular security monitoring of docker installations and containers against CIS and other custom security checks.

ArmourBird CSF has a client-server architecture and is thus divided into two components:

a) CSF Client

This component is responsible for monitoring the docker installations, containers, and images on target machines
In the initial release, it will be checking against Docker CIS benchmark
The checks in the CSF client will be configurable and thus will be expanded in future releases and updates
It has been build on top of Docker bench for security

b) CSF Server

This will be the receiver agent for the security logs generated by the various distributed CSF clients (installed on multiple physical/virtual machines)
This will also have a UI sub-component for unified management and dashboard-ing of the various vulnerabilities/issues logged by the CSF Clients
This server will also expose APIs that can be used for integrating with other systems

Watch out this GitHub space for update: https://github.com/armourbird
Follow the tool updates on twitter: https://twitter.com/ArmourBird

</details>

<details><summary><strong>cwe_checker: Hunting Binary Code Vulnerabilities Across CPU Architectures</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Nils-Edvin Enkelmann](https://img.shields.io/badge/Nils-Edvin%20Enkelmann-informational) ![Thomas Barabosch](https://img.shields.io/badge/Thomas%20Barabosch-informational)

🔗 **Link:** [cwe_checker: Hunting Binary Code Vulnerabilities Across CPU Architectures](https://gist.github.com/DaffyDuke/06c022992b3e9e3de76e819c95c55e0b)  
📝 **Description:** cwe_checker is an open source suite of tools to detect common bug classes like Use After Free (CWE-416) or Null Pointer Dereference (CWE-476). These bug classes are formally known as Common Weakness Enumerations (CWEs). Its main goal is to quickly point analysts to vulnerable code paths in binaries (e.g. firmware) without access to the source code.

cwe_checker is built on top of the Binary Analysis Platform (BAP). By using an intermediate representation for the binary code it can analyze ELF binaries of different CPU architectures, including x86/64, ARM, MIPS, and PPC. It has a modular and extensible architecture implementing static and dynamic analysis techniques. So far cwe_checker implements checks for more than 15 CWE classes including CWE-190 (Integer Overflow), CWE-415 (Double Free), and CWE- 676 (Use of Potentially Dangerous Function).

In addition, cwe_checker has been adopted as a core plugin for the Firmware Analysis & Comparison Tool (FACT). This enables analysts to hunt for vulnerabilities in large firmware data sets. Furthermore, the results of cwe_checker are exportable and there is an IDA Pro plugin that highlights any findings in the binary.

</details>

<details><summary><strong>Scout Suite: A Multi-Cloud Security Auditing Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Xavier Garceau-Aranda](https://img.shields.io/badge/Xavier%20Garceau-Aranda-informational)

🔗 **Link:** [Scout Suite: A Multi-Cloud Security Auditing Tool](https://github.com/nccgroup/ScoutSuite/wiki)  
📝 **Description:** Scout Suite (https://github.com/nccgroup/ScoutSuite) is an open source multi-cloud security-auditing tool, which enables security posture assessment of cloud environments. Using the APIs exposed by cloud providers, Scout Suite gathers configuration data for manual inspection and highlights risk areas. Rather than going through dozens of pages on the web consoles, Scout Suite presents a clear view of the attack surface automatically.

The following cloud providers are currently supported:

Amazon Web Services
Microsoft Azure
Google Cloud Platform

During the presentation, we will run Scout Suite against a number of cloud environments preconfigured with typical flaws. We will display how Scout Suite can be used to identify and help with remediation of security misconfigurations.

We will also release support for a number of new cloud providers (Oracle Cloud Infrastructure, Alibaba Cloud & IBM Cloud), and demonstrate how Scout Suite's cloud-agnostic architecture allows for great extensibility.

Presentation Slides: https://github.com/nccgroup/ScoutSuite/files/3502099/BH.Arsenal.2019.Scout.Suite.pdf

</details>

<details><summary><strong>SimpleRisk GRC</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

🔗 **Link:** [SimpleRisk GRC](https://github.com/aparsons/simplerisk)  
📝 **Description:** As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk, via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

</details>

<details><summary><strong>TaintedLove: Dynamic Security Analysis Tool for Ruby</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Benoit Côté-Jodoin](https://img.shields.io/badge/Benoit%20Côté-Jodoin-informational)

🔗 **Link:** [TaintedLove: Dynamic Security Analysis Tool for Ruby](https://github.com/Shopify/tainted_love/blob/master/tainted_love.gemspec)  
📝 **Description:** TaintedLove is a dynamic security analysis tool for Ruby. It leverages Ruby's object tainting and monkey patching features to identify potentially vulnerable code paths at runtime. TaintedLove is library agnostic and provides a simple framework to extend the detection of unsafe method usage and user input tracking.

</details>

<details><summary><strong>TROMMEL: Sift Through Embedded Device Files to Identify Potential Vulnerable Indicators</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Kyle O'Meara](https://img.shields.io/badge/Kyle%20O'Meara-informational)

🔗 **Link:** Not Available  
📝 **Description:** TROMMEL sifts through embedded device files to identify potential vulnerable indicators. TROMMEL significantly lessens the manual analysis time of the researcher by automating much of the vulnerability discovery and analysis process.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>chocoProxy: Aiding in the Reverse Engineering of Windows Applications' Network Traffic</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Eva Tanaskoska](https://img.shields.io/badge/Eva%20Tanaskoska-informational) ![Rick Veldhoven](https://img.shields.io/badge/Rick%20Veldhoven-informational)

🔗 **Link:** Not Available  
📝 **Description:** chocoProxy is a Windows tool intended to aid in reverse engineering Windows applications' network traffic. The proxy works by hooking the sending and receiving Windows APIs after being injected into a target process. The traffic can be modified to arbitrary values to observe the behaviour of an application when provided with unexpected input. The tool is meant to expedite the discovery and development of memory corruption exploits that occur in the implementation of complex and custom network protocols. chocoProxy takes away the necessity for exploit developers to reverse engineer a network protocol by utilizing the existing client/server functionality in the target.

</details>

<details><summary><strong>The Go Reverse Engineering Tool Kit</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Joakim Kennedy](https://img.shields.io/badge/Joakim%20Kennedy-informational)

🔗 **Link:** [The Go Reverse Engineering Tool Kit](https://gist.github.com/0xdevalias/4e430914124c3fd2c51cb7ac2801acba)  
📝 **Description:** The Go Reverse Engineering Tool Kit (go-re.tk) is a new open source toolset for analyzing Go binaries. The tool is designed to extract as much metadata as possible from stripped binaries to aid both reverse engineering and malware analysis. Gore can, for example, detect the compiler version used, extract type information and recover function information, including source code line numbers for functions and source tree structure.

The core library is written in Go, but the tool kit includes C-bindings and a library implementation in Python. When using the C-bindings or the Python library, it is possible to write plugins for other analysis tools such as IDA Pro and Ghidra. The toolset also includes "redress", a command line tool to "re-dress" stripped Go binaries. It can both be used standalone to print out extracted information from the binary or as a radare2 plugin to reconstruct stripped symbols and type information.

The goal with the tool kit is to lower the bar to enter for anyone that wants to analyze programs written in Go.

Source Code: https://github.com/goretk

</details>

<details><summary><strong>YARASAFE: Automatic Binary Function Similarity Checks with Yara</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Luca Massarelli](https://img.shields.io/badge/Luca%20Massarelli-informational)

🔗 **Link:** [YARASAFE: Automatic Binary Function Similarity Checks with Yara](https://github.com/lucamassarelli/yarasafe)  
📝 **Description:** YARASAFE is a new Yara module that automates the generation of rules containing binary similarity checks. Given a binary function, YARASAFE computes automatically its signature and includes it into a rule that will match any similar function.

This module rely on SAFE, a tool developed to create embedding vectors to represent binary functions. SAFE generates similarity-preserving embeddings: given two similar functions, their SAFE embeddings will be similar.

To create the embedding of a desired function YARASAFE includes an IDA Pro plugin: it sufficient to select the function in IDA and run the plugin to obtain its embedding.

YARASAFE can be used to create automatically yara rules for different purposes:

- Malware hunting
- Library function recognition
- Vulnerable function detection

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Electronegativity: Identify Misconfigurations and Security Anti-Patterns in Electron Applications</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Lorenzo Stella](https://img.shields.io/badge/Lorenzo%20Stella-informational)

🔗 **Link:** [Electronegativity: Identify Misconfigurations and Security Anti-Patterns in Electron Applications](https://github.com/phosphore)  
📝 **Description:** Electronegativity is a tool to identify misconfigurations and security anti-patterns in Electron-based applications (electronjs.org).

This is the first and only tool capable of detecting potential weaknesses and implementation bugs when developing applications using Electron, as recommended in the official security guidelines of the Electron project. Software developers and security auditors can use this tool to create secure desktop applications using web technologies.

After being first introduced at Black Hat US 2017 (Electronegativity - A Study of Electron Security) and featured in Black Hat Asia 2019 (Preloading Insecurity In Your Electron), the tool will be showcased for the first time ever at the Black Hat USA 2019 Arsenal where we will demonstrate its potential by scanning well-known applications.

Come see live demonstrations of Electronegativity hunting Electron applications for vulnerabilities and walk away with an open-source (Apache 2.0) static analysis engine to help secure your Electron applications!

</details>

<details><summary><strong>SASTRI: Plug and Play VM for SAST/*Static Application Security Testing Realtime Integration*/</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Rushikesh D. Nandedkar](https://img.shields.io/badge/Rushikesh%20D.%20Nandedkar-informational) ![Lalit Bhandari](https://img.shields.io/badge/Lalit%20Bhandari-informational)

🔗 **Link:** Not Available  
📝 **Description:** Abiding by the new hot concept of "Secure By Design," SASTRI is project carved out of the experiences/struggles/conflicts of product security engineers. It is an in-house SAST capability (plug and play VM) we are proposing, to make security engineers' inputs more receivable and reachable to the product developers and the decision-makers - while making our products more and more secure. This will save a lot of security engineers' and DevOps experts' time when it coms to setting up and fine tuning the SAST tools.

Highlights of SASTRI are:

Open source (hence free to edit and reconfigure)
Presently capable of scanning Python, C, C++ programs
Almost zero understanding of security principles is required to "run" SASTRI. (For bug resolution, yes definitely a deep understanding is required)
Automated bug reporting
Email alert for the issues reported
Same email contains attachment of report where buggy code snippet is mentioned along with the exact position of bug
Easy to integrate approach

SASTRI is an effort towards making SAST tools available right at the time of unit testing of code, in an automated way. The reason being, in most of Agile flavors of development, security testing is done in the end of the sprint, leaving very little to no time for bug fixes. Also, the smaller time window for security testing results in "not so in depth security testing" and "superficial fixes."
However, on the other hand, introducing security testing right at the programming phase in SDLC, can help in:

Finding vulnerabilities which are easy to exploit but difficult to mitigate
Finding vulnerabilities which are present due to complicated execution paths
Finding vulnerabilities specific to insecure configuration
Setting up basic secure code development principles amongst developers (Trust me this is the trickiest task, as most of the Devs are super possessive about their code and coding styles.

Also, this effort can help reduce apprehensions of security engineers when uploading source code on some vendors server which they do not trust. The list of advantages is huge; we have tried generalize them to the least count possible.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Eyeballer: A Picture is Worth a Thousand Vulns - Weaponized Machine Learning to Target Website Screenshots</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Dan Petro](https://img.shields.io/badge/Dan%20Petro-informational) ![Gavin Stroy](https://img.shields.io/badge/Gavin%20Stroy-informational)

🔗 **Link:** Not Available  
📝 **Description:** AI-based hacking tools are here and taking aim at your network perimeter. With recent advances in machine learning, hackers can now solve tasks that previously required human experience and decision making. Our open source tool Eyeballer uses a convolutional neural network to sift through mountains of screenshots and tells the hacker what is likely to have vulnerabilities and what isn't, just by looking at it.

You know a busted website when you see one: broken HTML, blocky frames—something obviously written in raw PHP before MVC frameworks even existed, made custom by your target over a decade ago. Signature-based scanners won't help you find this diamond-in-the-rough vulnerability. And who has time to look through 100,000 EyeWitness screenshots to find your most likely entry point? This is where AI comes in to give those websites a quick eyeballing so you don't have to.

The future of hacking will augment human expertise with AI analysis. To help spur this on, we'll be releasing both the source code behind Eyeballer and our training dataset of tens of thousands of carefully curated website screenshots. We'll also be showing off live demos of the whole thing so you can witness for yourself the results of melding machine and man.

</details>

<details><summary><strong>Ghost in the Browser: Backdooring with Shadow Workers</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Emmanuel Law](https://img.shields.io/badge/Emmanuel%20Law-informational) ![Claudio Contin](https://img.shields.io/badge/Claudio%20Contin-informational)

🔗 **Link:** [Ghost in the Browser: Backdooring with Shadow Workers](https://gist.github.com/pmarreck/28b3049a1a70b8b4f2eaff4466d0c76a)  
📝 **Description:** Service Workers are all the rage for progressive web apps nowadays. This talk will take a look at Service Workers from a different perspective. We will be focusing on our tool called "Shadow Workers" that serves as an exploitation toolkit to weaponize Service Workers

We'll explore some of the tools features including the ability to implant a pseudo backdoor in the browser and ghost through a victim's browser session to sniff, manipulate, and even proxy data silently.

We'll demo the various persistence mechanisms our tool provides to keep service workers alive and demo how MITM can be done at the browser layer. We'll also release a compendium tool to provide various mitigation mechanisms against such attacks.

</details>

<details><summary><strong>JSShell: An Interactive XSS Management & Browser Debugging Tool</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Daniel Abeles](https://img.shields.io/badge/Daniel%20Abeles-informational)

🔗 **Link:** [JSShell: An Interactive XSS Management & Browser Debugging Tool](https://github.com/Den1al/JSShell)  
📝 **Description:** JSShell is an interactive multi-user web based javascript shell that enables the user to debug esoteric browsers and manage XSS (cross site scripting) campaigns. It was originally created during research to have the ability to debug remote esoteric browsers that did not have a simple debugging console. This tool can be also used to easily attach to a XSS (Cross Site Scripting) payload to achieve browser remote code execution (similar to the BeeF framework) and manage the vulnerability.

Version 2.0 is created entirely from scratch, introducing new exciting features, stability and maintainability.

</details>

<details><summary><strong>ReDTunnel: Explore Internal Networks via DNS Rebinding Tunnel</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tomer Zait](https://img.shields.io/badge/Tomer%20Zait-informational) ![Nimrod Levy](https://img.shields.io/badge/Nimrod%20Levy-informational)

🔗 **Link:** [ReDTunnel: Explore Internal Networks via DNS Rebinding Tunnel](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Network_Attacks.md)  
📝 **Description:** Did you wonder how you could browse target's internal network without deploying anything on the victim machine? Sounds like magic, right? Imagine that you could have a one-click setup that will provide you a magic tunnel from the outside world. That's when we came up with the "ReD Tunnel" idea. The design goal was to use tools that exist on the victim's device, like the browser, rather than rely on 0days to stay below the radar of the most advanced AV. To create this new capability, we decided to combine two concepts: JavaScript reconnaissance techniques and the DNS rebinding attack. Open your browser, wait until the victim visits your website and start browsing the internal websites in their network. Now, when red-teaming you could really "be a guest, but feel at home".

</details>

<details><summary><strong>RWDD: Remote Web Deface Detection Tool</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ade Yoseman Putra](https://img.shields.io/badge/Ade%20Yoseman%20Putra-informational) ![Prashant KV](https://img.shields.io/badge/Prashant%20KV-informational)

🔗 **Link:** Not Available  
📝 **Description:** RWDD (Remote Web Deface Detection) tool is an application designed to help secure a web with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever source code of website changed (by programmer or attacker).

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>King Phisher: A Phishing Campaign Toolkit</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

🔗 **Link:** [King Phisher: A Phishing Campaign Toolkit](https://github.com/rsmusllp/king-phisher)  
📝 **Description:** King Phisher is a phishing toolkit created to meet the highly customized and flexible needs that offensively-focused security testers require. It boasts a wide range of features to facilitate it's use both on offensive, breaching-centric engagements as well as for user awareness training.

This arsenal demonstration will show the newer features that have been added to King Phisher in recent years. Viewers will see the latest campaign improvements including from the template selection process to gathering MFA tokens, validating submitted credentials and the Let's Encrypt integration. By integrating with Let's Encrypt through certbot, users are able to quickly and easily issue certificates for, and enable HTTPS for their phishing sites. Finally, viewers will see a demonstration of the newest plugins for campaign data management, the usage of various alerting services and finally SPAM evasion.

Source code: https://github.com/securestate/king-phisher

</details>

<details><summary><strong>Social Attacker: Automated Phishing on Social Media Platforms</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Jacob Wilkin](https://img.shields.io/badge/Jacob%20Wilkin-informational)

🔗 **Link:** [Social Attacker: Automated Phishing on Social Media Platforms](https://github.com/Greenwolf/social_attacker)  
📝 **Description:** Social Attacker is the first Open Source, Multi-Site, automated Social Media Phishing Framework. It allows you to automate the phishing of Social Media users on a mass scale by handling the connecting to, and messaging of targets.

You provide Social Attacker with a phishing message and a list of target profiles (collected either by hand or with Social Mapper). Then over a timeframe you set, it attempts to connect to the targets and, if they accept, sends them phishing message. It can even scrape a targets public profile history and use rudimentary message generation to craft a personal message specific to that person, as an alternative to sending the same phish to all targets.

Social Attacker provides Red Teamers, Penetration Testers & Social Engineers an efficient way to exploit and pivot through an alternative attack route.

Social Attacker supports the following Social Media platforms:

LinkedIn
Facebook
Twitter
VKontakte

Additional Features Include:

Report Generation
Tracking Connections & Clicks
Customized Phishing Message Generation

</details>

<details><summary><strong>SPF: SpeedPhishing Framework</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational)

🔗 **Link:** [SPF: SpeedPhishing Framework](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/phishing/spf.md)  
📝 **Description:** SpeedPhishing Framework (SPF) is a small collection of tools which can assist penetration testers in quickly/automatically deploying phishing exercises in minimal time.

Among the various capabilities included with SPF is the ability to automate the phishing process of OSINT and target selection, deployment of one or more phishing websites, the crafting and sending of phishing emails to the targets, recording the results, and generating a basic report.

SPF also includes more advanced capabilities such as dynamically building new web phishing templates, automatically validating captured credentials against target mail servers and the pillaging of sensitive information, and SPF can assist in the phishing of multifactor authentication portals.

</details>

---