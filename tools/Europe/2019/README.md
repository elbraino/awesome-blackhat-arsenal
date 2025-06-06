# Europe 2019
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2019** event held in **Europe**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🔴 Red Teaming / AppSec
<details><summary><strong>ART: Adversarial Robustness 360 Toolbox for Machine Learning Models</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Irina Nicolae](https://img.shields.io/badge/Irina%20Nicolae-informational) ![Beat Buesser](https://img.shields.io/badge/Beat%20Buesser-informational)

🔗 **Link:** [ART: Adversarial Robustness 360 Toolbox for Machine Learning Models](https://github.com/lfai/proposing-projects/blob/master/proposals/trusted-ai.adoc)  
📝 **Description:** Adversarial attacks against machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). These attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness 360 Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defense methods for machine learning models. ART provides an implementation for many state-of-the-art methods for attacking and defending machine learning. At Black Hat, we will introduce the major version 1.0, which contains new powerful black-box attacks, support for additional machine learning libraries, as well as new defenses and detectors. Through ART, the attendees will (re)discover how to attack and defend diverse machine learning systems.

</details>

<details><summary><strong>Automatic API Attack Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Boris Serebro](https://img.shields.io/badge/Boris%20Serebro-informational)

🔗 **Link:** [Automatic API Attack Tool](https://github.com/imperva/automatic-api-attack-tool)  
📝 **Description:** Imperva's customizable API attack tool takes an API specification as an input, creates and runs attacks which are based on it as an output.

After researching the web, we didn't find an automatic tool which takes an API specification and checks the server offering the service against it. But we saw a high demand for such a tool from the community. So we decided to build it.

The tool is able to parse the API specification and create fuzzing attack scenarios based on what it defines, and outside of its definition. Each endpoint is injected with cleverly generated values within the boundaries defined by the specification, and outside of it, the appropriate requests are sent and their success or failure are reported in a detailed manner. It is also able to run various security attack vectors targeted at the existing endpoints, or even non-existing ones (such as illegal resource access, XSS, SQLi and RFI).
No human intervention needed, simply run the tool and get the results.

The tool can be easily extended to adapt to the various needs; whether it is a developer who wants to test the API she wrote or an organization which wants to run regular vulnerability or positive security scans on its public API, you name it. It is built with CI/CD in mind.

We are using this tool, among other tools, to check our security products internally.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>AttackForge.com: A Pentest Management & Collaboration Platform for Everyone</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Fil Filiposki](https://img.shields.io/badge/Fil%20Filiposki-informational) ![Stas Filshtinskiy](https://img.shields.io/badge/Stas%20Filshtinskiy-informational)

🔗 **Link:** Not Available  
📝 **Description:** AttackForge.com is a free-to-use collaboration platform to manage pentesting projects. AttackForge allows a project team to easily collaborate in one place, reducing overheads and pain for all people involved - Customer, 3rd parties and Pentest Team. This is what makes AttackForge unique and different to other pentest collaboration solutions. It goes beyond automated reporting and issue library. It brings everyone together in one place and gives them tools and workflows to initiate & deliver a pentest, and also manage remediation testing.

Pentesters love to break things. However, they hate responding to unnecessary emails and phone calls; having to chase people for details to start testing; having to figure out who to talk to when things aren't working; and most of all having to write and review reports. AttackForge.com is purpose built to help pentesters focus their time and efforts on breaking things, and reduce distractions and unnecessary tasks. This helps to get the best out of the pentest team and provide better results for customers.

AttackForge.com also helps people to start a career in penetration testing. AttackForge provides a secure online environment to create a portfolio of pentests to reflect skills, knowledge, and communication ability in an industry-standard way – to demonstrate to recruiters and future employers that they are ready for the workforce. This may also help to reduce the shortage of supply and skills-gap our industry is currently facing.

</details>

<details><summary><strong>Backoori: Tool Aided Persistence via Windows URI Schemes Abuse</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Giulio Comi](https://img.shields.io/badge/Giulio%20Comi-informational)

🔗 **Link:** [Backoori: Tool Aided Persistence via Windows URI Schemes Abuse](https://github.com/giuliocomi/backoori)  
📝 **Description:** The widespread adoption of custom URI protocols to launch specific Universal App can be diverted to nefarious purposes. The URI schemes in Windows 10 can be abused in such a way to maintain persistence via fileless technique. Backdooring a compromised user (Administrator privileges not required) is a matter of seconds. The attack is transparent to the unaware victim that won't be able to identify the attack and to the antivirus solutions that are currently not monitoring the specific Registry keys involved. These subtle fileless payloads can be triggered in many contexts, from the Narrator in the Windows logon screen (a novel Accessibility Feature abuse discovered by Giulio right before deciding to implement Backoori) to the classical web attack surface. The payloads can also be dropped in gadgets that can interact between each other by abusing, once again, the Windows URI protocols.

</details>

<details><summary><strong>CyberRange: An Open-Source Offensive/Defensive Security Lab in AWS</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Thomas Cappetta](https://img.shields.io/badge/Thomas%20Cappetta-informational)

🔗 **Link:** Not Available  
📝 **Description:** This CyberRange project represents the first open-source Cyber Range blueprint in the world.

This project provides a bootstrap framework for a complete offensive, defensive, reverse engineering, and security intelligence tooling in a private research lab using the AWS Cloud. This project contains vulnerable systems, open-source tools.

It simply provides a researcher with a disposable offensive/defensive AWS-based environment in less than 10 minutes.

</details>

<details><summary><strong>Docker Security Playground</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Gaetano Perrone](https://img.shields.io/badge/Gaetano%20Perrone-informational) ![Francesco Caturano](https://img.shields.io/badge/Francesco%20Caturano-informational) ![Simon Pietro Romano](https://img.shields.io/badge/Simon%20Pietro%20Romano-informational)

🔗 **Link:** Not Available  
📝 **Description:** Docker Security Playground is an architecture leveraging a microservices-based approach in order to build complex network infrastructures specifically tailored to the study of network security. The idea is to leverage latest fashion virtualization techniques in order to: (i) reproduce real-world networking scenarios; (ii) build ad-hoc network playgrounds involving vulnerable nodes/services and malicious users/tools; (iii) provide lab participants with low-cost, COTS-based, easily reproducible networking tools.

</details>

<details><summary><strong>DSInternals PowerShell Module</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Grafnetter](https://img.shields.io/badge/Michael%20Grafnetter-informational)

🔗 **Link:** [DSInternals PowerShell Module](https://github.com/MichaelGrafnetter/DSInternals)  
📝 **Description:** The DSInternals PowerShell Module exposes many internal and undocumented security-related features of Active Directory. It is included in FireEye's Commando VM and its cmdlets can be used in the following scenarios:

- Active Directory password auditing that discovers accounts sharing the same passwords or having passwords in a public database like HaveIBeenPwned.
- Offline ntds.dit file manipulation, password resets, group membership changes, SID History injection and enabling/disabling accounts.
- Bare-metal recovery of domain controllers from just IFM backups (ntds.dit + SYSVOL).
- Online password hash dumping through the Directory Replication Service Remote Protocol (MS-DRSR).
- Domain or local account password hash injection, either through the Security Account Manager Remote Protocol (MS-SAMR) or by directly modifying the database.
- LSA Policy modification through the Local Security Authority Remote Protocol (MS-LSAD / LSARPC).
- Extracting credential roaming data and DPAPI domain backup keys, either online through directory replication and LSARPC, or offline from ntds.dit files.

</details>

<details><summary><strong>Exploitivator: A Tool to Automate Exploitation as Part of the Scanning Process</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nick Dunn](https://img.shields.io/badge/Nick%20Dunn-informational)

🔗 **Link:** Not Available  
📝 **Description:** Exploitivator is a tool which takes a range of IP addresses and scans for user-specified vulnerabilities, automatically exploiting any verified instances of vulnerable machines with a Metasploit payload. The tool also includes an additional feature to run multiple MSF scans against a range of IP addresses, without a need to repeatedly set up and then run each scan.

</details>

<details><summary><strong>FruityDC</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![xtr4nge .](https://img.shields.io/badge/xtr4nge%20.-informational)

🔗 **Link:** [FruityDC](https://github.com/xtr4nge/FruityDC)  
📝 **Description:** FruityDC is focused on dynamic callbacks for re-establishing communication with C2 infrastructure and for achieving persistence, how payloads can heal themselves after being blocked including how communication can be re-established via dynamic parametric data. The methods described are code agnostic.

</details>

<details><summary><strong>Haaukins: A Highly Accessible and Automated Virtualization Platform for Security Education</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jens Myrup Pedersen](https://img.shields.io/badge/Jens%20Myrup%20Pedersen-informational)

🔗 **Link:** Not Available  
📝 **Description:** Haaukins is a highly accessible platform for security education, which allows users to try out ethical hacking and penetration testing using Kali Linux through a browser. It makes it possible to conduct trainings for even large groups without the need for installing virtual environments or other tools – the participants can work on their own laptops just through their web browser of choice, and have access within a couple of minutes.

Haaukins allows the teacher/instructor to set up an event using a command line interface specifying e.g. which challenges to include and how many labs are needed. Labs can include different kind of challenges, such as a number of vulnerable machines. The challenges can also include e.g. sniffing network traffic between different machines. Once an event is setup, users/teams can easily register and see the challenges as in any CTF.

What makes Haaukins stand out is that each user is assigned a virtual lab, which is accessed through a Kali Linux accessible through a web browser. After registration, the user just clicks the "connect" button, and he can access the Kali Linux desktop.

Haaukins is designed with training in mind rather than for competition. For this reason a number of features are implemented such as Dynamic Flags, so the teams cannot exchange flags between each other, and a randomization of IP addresses throughout the challenges, so teams really have to work their own way through.

It is easy to contribute with new challenges, since challenges can consist of any set of docker images and VirtualBox OVA's.

During the last year, the platform has been tested out with different target audiences, including OWASP groups, networks of IT professionals, companies, high schools and higher education.

</details>

<details><summary><strong>HomePwn</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pablo Gonzalez](https://img.shields.io/badge/Pablo%20Gonzalez-informational) ![Francisco Jose Ramirez Vicente](https://img.shields.io/badge/Francisco%20Jose%20Ramirez%20Vicente-informational)

🔗 **Link:** Not Available  
📝 **Description:** The hyperconnected world is a reality nowadays. Today, we should consider that companies have a considerable number of these devices within their workplaces or offices. With the famous BYOD (Bring Your Own Device) companies are opening an attack vector that can be exposed or increased by the different devices that employees can carry to the office, either on their body, on a keyring, in their backpack or even on their clothes. The many different technologies that can be used are a vector attack for assailants and Red Team members.

The emergence of millions of devices, from different nature, have caused changes in the security applied for each of them. Using several technologies between these devices makes security heterogeneous. Bluetooth Low-Energy, WiFi, NFC are just some examples of the technologies being used by millions of devices around our society. Most of them can be found at home or in our offices. Companies are suffering many attacks that can come through a wrong configuration and can be used by an attacker to gain access to other resources within the company itself. HomePwn is a framework that provides several features for auditing and pentesting on devices connected to the Internet using different technologies such: WiFi, Bluetooth Low-Energy, or NFC, among others.

HomePwn is a framework that provides features to audit and pentesting devices that company employees can use in their day-to-day work and inside the same working environment.

</details>

<details><summary><strong>LinkTap: New Threats are Already Around You - The IPV6 Attack Must be Understood</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Kunzhe Chai](https://img.shields.io/badge/Kunzhe%20Chai-informational) ![YongTao Wang](https://img.shields.io/badge/YongTao%20Wang-informational) ![Jinglun Li](https://img.shields.io/badge/Jinglun%20Li-informational)

🔗 **Link:** Not Available  
📝 **Description:** Due to the exhaustion of IPv4 free address space, the use of IPv6 on the Internet is gradually increasing. All Windows operating systems since Windows Vista have IPv6 enabled by default. IPv6 brings a series of improvements compared to IPV4, but these improvements are also put a double-edged sword.

Recently, we have been focusing on "IPv6" attack research and found that in the IPV6 environment, there are many attack points, such as Iptables will fail, use IPV6 to bypass the Web defense strategy and abuse IPV6-specific protocols for man-in-the-middle attacks, and Other attack ideas!

In this presentation, I will disclose the attack methods and ideas I have found for IPV6, and will also release tools for IPV6 attacks.

</details>

<details><summary><strong>Octopus: Pre-operation C2 Server</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mohammad Askar](https://img.shields.io/badge/Mohammad%20Askar-informational)

🔗 **Link:** [Octopus: Pre-operation C2 Server](https://github.com/mhaskar/Octopus)  
📝 **Description:** Octopus is an open source, pre-operation C2 server based on python which can control an Octopus powershell agent through HTTP/S.

The main purpose of creating Octopus is for use before any red team operation, where rather than starting the engagement with your full operational arsenal and infrastructure, you can use Octopus first to attack the target and gather information before you start your actual red team operation.

Octopus works in a very simple way to execute commands and exchange information with the C2 over a well encrypted channel, which makes it inconspicuous and undetectable from almost every AV, endpoint protection, and network monitoring solution.

One cool feature in Octopus is called ESA, which stands for "Endpoint Situational Awareness", which will gather some important information about the target that will help you to gain better understanding of the target network endpoints that you will face during your operation, thus giving you a shot to customize your real operation arsenal based on this information.

Octopus is designed to be stealthy and covert while communicating with the C2, as it uses AES-256 by default for its encrypted channel between the powershell agent and the C2 server. You can also opt for using SSL/TLS by providing a valid certficate for your domain and configuring the Octopus C2 server to use it.

</details>

<details><summary><strong>OWASP Nettacker (Updated - More in-depth Demo)</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Paul Harragan](https://img.shields.io/badge/Paul%20Harragan-informational) ![Sam Stepanyan](https://img.shields.io/badge/Sam%20Stepanyan-informational)

🔗 **Link:** [OWASP Nettacker (Updated - More in-depth Demo)](https://github.com/OWASP/Nettacker/wiki/Events)  
📝 **Description:** Nettacker project was created to automate for information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and information. This software is able to use SYN, ACK, TCP, ICMP and many other protocols to detect and bypass the Firewalls/IDS/IPS and devices. By using a unique solution in Nettacker to find protected services such as SCADA, we could make a point to be one of the bests of scanners.

</details>

<details><summary><strong>PyExfil: A Python Data Exfiltration Package</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yuval Nativ](https://img.shields.io/badge/Yuval%20Nativ-informational)

🔗 **Link:** [PyExfil: A Python Data Exfiltration Package](https://github.com/cjcase/beaconleak)  
📝 **Description:** PyExfil is a python data exfiltration package for python containing servers and clients for enabling covert channels communication. The package started as a self exploratory code project and developed into a library that helps analyze various detection mechanisms.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>AVCLASS++: Yet Another Massive Malware Labeling Tool</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yuma Kurogome](https://img.shields.io/badge/Yuma%20Kurogome-informational)

🔗 **Link:** Not Available  
📝 **Description:** Addressing malware threats requires constant efforts to create and maintain a dataset. Especially, labeling malware samples is a vital part of shepherding a dataset. AVCLASS, a tool which takes as input VirusTotal reports and returns labels that aggregates scan results of multiple anti-viruses, is one of the most well-used oracles in both academia and industry.

However, AVCLASS often suffers from the following drawbacks. First, AVCLASS is prone to fail labeling samples that have just been posted to VirusTotal because only a few anti-viruses give labels to such samples. An inconvenient truth: when we provided AVCLASS with 20,000 VirusTotal reports, half of them could not be labeled. Second, AVCLASS cannot determine if the label is randomly generated (as with domain generation algorithms of malware) or not. Some anti-viruses that VirusTotal has worked with after AVCLASS released were labeled with the DGA, resulting in a biased label. Because of them, we are forced to make a lot of manual, tedious intervention in malware labeling (otherwise, we need to drop samples with inconsistent labels from the dataset).

In this session, we present AVCLASS++, an open-source successor of AVCLASS. AVCLASS++ is carefully designed to address these drawbacks by arming with label propagation and DGA detection. We shall describe these techniques and demonstrate that AVCLASS++ can perform labeling more accurately than the vanilla one. Users of the vanilla AVCLASS can use AVCLASS ++ with the almost same command-line options as before. Even if you have never used AVCLASS, the use of AVCLASS++ is quite easy -- just prepare a malware sample and VirusTotal report, and give them as arguments. We envision that AVCLASS++ supports both practitioners (such as SOC operators, CSIRT members, and malware analysts) and academic researchers, and thus contributes to the further development of prompt security operation and reproducible security research.

</details>

<details><summary><strong>CrackQ: Intelligent Password Cracking</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dan Turner](https://img.shields.io/badge/Dan%20Turner-informational)

🔗 **Link:** [CrackQ: Intelligent Password Cracking](https://github.com/f0cker/crackq)  
📝 **Description:** CrackQ is, first and foremost, a Python based queuing system for managing hash cracking using Hashcat. There are several tools available for this purpose, CrackQ was born from the frustration of using these tools on a daily basis. It adds some new and interesting additional features as solutions to these frustrations. CrackQ is essentially a REST API with clients in the form of a Python CLI tool and a web GUI. The API design is very stable and works very reliably as a platform to use for day-to-day password cracking within an offensive-security team. The tool is designed to be easy to install and comprises of currently 4 docker images, built on production ready containers segregating each component, all controlled seamlessly using docker-compose. The tool will also include detailed analysis/reporting with graphs representing a multitude of metrics and automated "intelligent" cracking using various pre-existing techniques and machine learning solutions. The tool will be released open-source in the coming months.

</details>

<details><summary><strong>Malware Initial Assessment with pestudio</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Marc Ochsenmeier](https://img.shields.io/badge/Marc%20Ochsenmeier-informational)

🔗 **Link:** Not Available  
📝 **Description:** pestudio is used by Computer Emergency Response Teams and Labs worldwide in order to perform Malware Initial Assessment.

</details>

<details><summary><strong>Omniscient: Lets Map Your Network</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Pramod Rana](https://img.shields.io/badge/Pramod%20Rana-informational)

🔗 **Link:** [Omniscient: Lets Map Your Network](https://github.com/varchashva/LetsMapYourNetwork)  
📝 **Description:** Omniscient: Lets Map Your Network aims to provide an easy-to-use and point-in-time interface to security engineers and network administrators to represent their network in graphical form with zero manual error, where a node represents a system and relationship between nodes represents a direct connection. It also monitors the 'identified' network with user-defined periodicity and provides the analytics on rogue systems/devices present in network.

It is utmost important for any security engineer to understand their network first before securing it and it becomes a daunting task to have a 'true' understanding of a widespread network. In a mid to large level organisation's network having a network architecture diagram doesn't provide the complete understanding of network and manual verification is a nightmare. Hence in order to secure entire network it is important to have a complete picture of all the systems which are connected to your network, irrespective of their type, function, technology etc.

BOTTOM LINE - YOU CAN'T SECURE WHAT YOU ARE NOT AWARE OF.

Omniscient does it in two phases:
1. Learning: In this phase, Omniscient 'learns' the network by utilising passive network enumeration, active scans and upload of existing CMDB for on-premises network; and by querying the APIs for cloud networks. Then it builds graph database leveraging the responses of all learning activities. User can perform any of the learning activities at any point of time and Omniscient will incorporate the results in existing database.

2. Monitoring: This is a continuous and automatic process, where Omniscient monitors the 'identified' network (with user-defined periodicity) for any changes, compare it with existing information and update the graph database accordingly.

</details>

<details><summary><strong>Sigma Hunting App for Splunk</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Bareiß](https://img.shields.io/badge/Patrick%20Bareiß-informational)

🔗 **Link:** [Sigma Hunting App for Splunk](https://github.com/P4T12ICK/Sigma-Hunting-App)  
📝 **Description:** The Sigma Hunting App for Splunk addresses two main challenges: missing collaboration in detection rule development and automated deployment of detection rules. By using Sigma as an generic signature description language, security analysts and security researcher from all over the world can work together independent from their SIEM tool. The joint detection rule development improves the general detection capabilities of the Security Operations Centers. The manual deployment of a detection rule in Splunk was a time-consuming task in order to complete all the needed fields for a scheduled search. The Sigma Hunting App solves that problem by providing a dedicated Splunk App, which can be used to dynamically update Sigma detection rules from a Git repository.

Furthermore, the Sigma Hunting App supports the analyst in their investigations of triggered detection rules. The triggered detection rules are stored as events in a separate threat-hunting index enriched with data of the Mitre ATT&CK Matrix.

The audience should learn the following aspects:

A modern approach of detection rule development
Continuous Delivery in detection rule development through the Sigma Hunting App
Installing and configuring the Sigma Hunting App
Automated deployment of detection rules into Splunk
Features of the Sigma Hunting App
Using Sigma Hunting App to find suspicious behavior

</details>

<details><summary><strong>The Big zBang Theory: Active Directory Risk Assessment</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Asaf Hecht](https://img.shields.io/badge/Asaf%20Hecht-informational) ![Nimrod Stoler](https://img.shields.io/badge/Nimrod%20Stoler-informational)

🔗 **Link:** [The Big zBang Theory: Active Directory Risk Assessment](https://github.com/cyberark/zBang)  
📝 **Description:** zBang is an Active Directory Risk Assessment tool that alerts against five different Active Directory attack vectors: ACLight, Skeleton Key, SID History, Risky SPN, and Mystique.

Organizations and red-teamers should utilize zBang to identify potential attack vectors and improve the security posture of the network. The results can be analyzed with a graphic interface specifically designed for the tool.

The new zBang tool discovers critical findings like:

The most privileged accounts that must be protected, including suspicious Shadow Admins.
Possible infected DCs with the "Skeleton Key" malware.
Suspicious SID history with hidden privileges.
Risky configurations of SPNs that might lead to credential theft of domain admins.
Risky Kerberos delegation configurations in the network.

The scans do not require any extra privileges; the tool performs read-only LDAP queries to the DC and can be run using any domain user.

</details>

<details><summary><strong>Zhouhe: Threat Analysis and Detection of Network Traffic</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rui Xiao](https://img.shields.io/badge/Rui%20Xiao-informational) ![Rui Zhang](https://img.shields.io/badge/Rui%20Zhang-informational)

🔗 **Link:** Not Available  
📝 **Description:** Today, the malicious behavior of hackers is aimed at all kinds of terminals, servers, and websites. Sadly, when the hacker came, did something, and took away what we didn't know, in many cases. However, no matter what the hacker did, his behavior in the network could not be erased. Zhouhe is a free tool/platform, it has detection rules and machine learning algorithms maintained by a team of experts to detect threats, it provides network threat analysis and detection capabilities. You only need to upload traffic files to let you quickly understand the threats and malicious behaviors in the network.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Drone Hacking with DroneSploit</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Alexandre D'Hondt](https://img.shields.io/badge/Alexandre%20D'Hondt-informational) ![Yannick Pasquazzo](https://img.shields.io/badge/Yannick%20Pasquazzo-informational)

🔗 **Link:** Not Available  
📝 **Description:** This project is aimed to provide a Metasploit-like CLI framework tailored to drone hacking.

It currently supports modules for the C-me and Flitt drones (Hobbico) but should be extended in a near future with new modules for other brands and models (i.e. Parrot and DJI).

</details>

<details><summary><strong>IotSecFuzz: Security Framework</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Ilya Shaposhnikov](https://img.shields.io/badge/Ilya%20Shaposhnikov-informational) ![Sofia Marakhovich](https://img.shields.io/badge/Sofia%20Marakhovich-informational) ![Sergey Bliznyuk](https://img.shields.io/badge/Sergey%20Bliznyuk-informational)

🔗 **Link:** [IotSecFuzz: Security Framework](https://github.com/securestep9/iotsecfuzz)  
📝 **Description:** IoTSecFuzz is Open Source framework which was created with the aim of combining the maximum number of utilities for comprehensive testing of IoT device security at all levels of implementation. It has a convenient console in order to use it as a stand-alone application, as well as the ability to import it as a library.

</details>

<details><summary><strong>WHID Elite: The Hacking Device for Pwning Computers, Moving Cranes, Exploding Things and Electrocuting Nuts</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

🔗 **Link:** Not Available  
📝 **Description:** During the last few years, Red Teaming engagements have become more and more popular. This trend pushed some hackers to R&D and release new opensource devices with the intent to make PhySec operations even more interesting. Smoothing the path to new TTPs and improving some old ones. During this talk, I will present two new hacking devices developed from Offensive Ninjas, for Offensive Ninjas:
- WHID Elite (a 2G-enabled offensive device that allows a threat actor to remotely inject keystrokes, bypass air-gapped systems, conduct mousejacking attacks, do acoustic surveillance, RF replay attacks and much more).
- USBsamurai (a Remotely Controlled Malicious USB HID Injecting Cable DIY for less than 10$ that can be used to compromise targets remotely in the most stealthiest way ever seen).

</details>

---
## Others
<details><summary><strong>DSIEM: Security Event Correlation Engine for ELK Stack</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Toto A Atmojo](https://img.shields.io/badge/Toto%20A%20Atmojo-informational) ![Memet Anwar](https://img.shields.io/badge/Memet%20Anwar-informational)

🔗 **Link:** Not Available  
📝 **Description:** DSIEM is a security event correlation engine for ELK stack, allowing the platform to be used as a dedicated and full-featured SIEM system.

DSIEM provides OSSIM-style correlation for normalized logs/events, perform lookup/query to threat intelligence and vulnerability information sources, and produces risk-adjusted alarms.

</details>

<details><summary><strong>EventList: What the log?! So Many Events, so Little Time...</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Miriam Wiesner](https://img.shields.io/badge/Miriam%20Wiesner-informational)

🔗 **Link:** [EventList: What the log?! So Many Events, so Little Time...](https://github.com/OWASP/www-chapter-london/blob/master/tab_pastevents.md)  
📝 **Description:** Detecting adversaries is not always easy - especially when it comes to correlating Windows Event Logs to real-world attack patterns and techniques. EventList helps to match Windows Event Log IDs with the MITRE ATT&CK framework (and vice-versa) and offers methods to simplify the detection in corporate environments worldwide.

</details>

<details><summary><strong>Mobile-ADSheild: Attack Automatic Analysis and Interception Engine in Mobile App</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Shijie Cao](https://img.shields.io/badge/Shijie%20Cao-informational) ![Hao Zhao](https://img.shields.io/badge/Hao%20Zhao-informational)

🔗 **Link:** Not Available  
📝 **Description:** Mobile-ADSheild is a mobile app active defense engine that defends against most vulnerability exploits.
We will introduces the Mobile-ADSheild engine, which can be freely integrated into any app and can be used to launch the app's self-protection capabilities through a simple API interface. The engine does not require the mobile developer to make too many changes, just need to start the engine, it will run itself after the app is launched.

</details>

<details><summary><strong>MPFuzzer: Fuzzing for Mini Program Vulnerabilities</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Wenjie LI](https://img.shields.io/badge/Wenjie%20LI-informational) ![Guoyong YI](https://img.shields.io/badge/Guoyong%20YI-informational)

🔗 **Link:** Not Available  
📝 **Description:** Mini programs are lightweight apps that run inside another app. They don't need to be downloaded or upgraded through app stores. They make it possible for one app to perform the service of many apps add up and have over one billion users in China, which brings new mobile security challenges. Hackers can bypass the security defenses of Mini programs in various ways(like string truncation, whitelist bypass, malformed label). A successful exploit of bypassing may lead to arbitrary code execution or leak of sensitive data.

Security workers are struggling to discover and fix vulnerabilities in the workflow of the mini program. It results in a greater need for automated mini-program fuzz testing tools.

We will introduce the MPFuzzer, the first fuzz testing tool which finds vulnerabilities in mini program technology stacks automatically by trying different strategies.

MPFuzzer can fuzz any mini program platform in the field by configuring a simple config file without writing any code. The key inside our work is to quickly generate large numbers of mini program code and mutate them to test as many mini program technology stacks as possible.

As a practical impact, our tool has detected more than ten mini program critical vulnerabilities.

</details>

<details><summary><strong>RansomCoin</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Éireann Leverett](https://img.shields.io/badge/Éireann%20Leverett-informational) ![Erin Burns](https://img.shields.io/badge/Erin%20Burns-informational)

🔗 **Link:** Not Available  
📝 **Description:** Most ransomware analysis is focused on the malware, but what if you are *just* chasing the money? You want those cryptocurrency addresses and thos other IoCs fast, and you don't particularly care about what exploit is being used this time around.

This is the tool for you! RansomCoin is a suite of tools designed to scrape IoCs and multiple crytpocurrencies from a large corpus of malware. It can also do ransomnotes, or entire VMs after your dynamic analysis. It can process one file in seconds or 100K files in a few hours. After that, you can use the other tools in the suite, to examine transactions, or pump the dat into MISP instances.

</details>

<details><summary><strong>SEC Xtractor: Assisted Hardware Analysis Tool</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Thomas Weber](https://img.shields.io/badge/Thomas%20Weber-informational)

🔗 **Link:** [SEC Xtractor: Assisted Hardware Analysis Tool](https://github.com/Trustworthy-AI-Group/Adversarial_Examples_Papers)  
📝 **Description:** The SEC Xtractor Assisted Hardware Analysis Tool was originally designed as internal hardware analysis tool. It was used as all-in-one solution to dump NAND / NOR / SPI and I²C flash memory chips. Because of different voltage levels of some chips, the SEC Xtractor provides the option to adjust the voltage from from 1.8V to 5.5V. Its program code is completely written in standard C which enables any programmer to modify the code without a lot of knowledge about hardware. Custom memory chips can also be added to the firmware in this way.

Beside reading flash memory chips, the SEC Xtractor has integrated JTAG-bruteforce functionality with configurable pin count. UART transmit pins can be found with a passive UART identifier module.

Another capability of the SEC Xtractor is the directly available FT2232H module that enables the device to use OpenOCD and two serial ports out of the box, also with configurable voltage levels.

</details>

<details><summary><strong>spispy: Open source SPI flash emulation</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Trammell Hudson](https://img.shields.io/badge/Trammell%20Hudson-informational)

🔗 **Link:** [spispy: Open source SPI flash emulation](https://github.com/osresearch)  
📝 **Description:** spispy is an open source hardware tool for emulating SPI flash chips that makes firmware development and boot security research easier by avoiding the slow flash chip erase and programming cycles. It also logs flash accesses, providing insight into the early boot process and enables TOCTOU attacks against the running firmware.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>DumpTheGit</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Malkit Singh](https://img.shields.io/badge/Malkit%20Singh-informational)

🔗 **Link:** [DumpTheGit](https://github.com/shubhamshubhankar/DumpTheGit)  
📝 **Description:** DumpTheGit searches through public repositories to find sensitive information uploaded to the Github repositories.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>huskyCI: Performing Security Tests Inside Your CI</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Rafael dos Santos](https://img.shields.io/badge/Rafael%20dos%20Santos-informational)

🔗 **Link:** [huskyCI: Performing Security Tests Inside Your CI](https://github.com/rafaveira3)  
📝 **Description:** huskyCI is an open-source tool that performs security tests inside CI pipelines of multiple projects and centralizes all results into a database for further analysis and metrics.

</details>

<details><summary><strong>Mal2Vec: Word2Vec Variant for Analytics of Web Attacks</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ori Or-Meir](https://img.shields.io/badge/Ori%20Or-Meir-informational) ![Itsik Mantin](https://img.shields.io/badge/Itsik%20Mantin-informational)

🔗 **Link:** Not Available  
📝 **Description:** Word2Vec is one of the most successful and popular technologies for Natural Language Processing. It facilitates the understanding of the semantics of words using their context. Many other domains adopted the Word2Vec approach and used embedding of domain objects in Euclidean spaces for distance calculation, clustering, visualization and more.

Mal2Vec is a Word2Vec-based framework for analytics of security incidents that helps the analyst understand the contextual relations between attack vectors, and thus to understand better attack flows. The tool looks at malicious web request as words and at sequences of malicious web requests as sentences, and applies a variant of Word2Vec to embed the attack vectors in Euclidean space and to analyze their contextual relations. Using this approach, the analyst can get better understanding of the attack flows, e.g., he can see which attack vectors tend to come together.

While we developed Mal2Vec to improve our understanding of web attack based on analysis of security events of Web Application Firewall (WAF), we also provide an easy customization flow that will make it useful for analytics of other cyber-attack data.

</details>

---
## 🔍 OSINT
<details><summary><strong>RTTM: Real Time Threat Monitoring Tool</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Naveen Rudrappa](https://img.shields.io/badge/Naveen%20Rudrappa-informational) ![Murali Krishna Segu](https://img.shields.io/badge/Murali%20Krishna%20Segu-informational)

🔗 **Link:** Not Available  
📝 **Description:** Monitoring possible threats of your company on the Internet is an impossible task to be achieved manually. Hence, many threats of the company go unnoticed until it becomes viral in public - thus causing monetary/reputation damage. This is where RTTM comes into action. RTTM (Real-Time Threat Monitoring Tool) is a tool developed to scrap all pasties, GitHub,reddit..etc in real-time to identify an occurrence of search terms configured. Upon a match, an email will be triggered. Thus allowing the company to react in case of leakage of code, any hacks tweeted..etc.. and harden themselves against an attack before it goes viral.

Over the past 2 years, the tool has evolved from a simple search. Artificial intelligence has been implemented to perform a better search. If regex is needed even that is supported. Thus, behavior is close to human and reduces false positives.

The best part of the tool is that alert will be sent to email in less than 60 seconds from the time threat has made it to the internet. Thus allowing response in real-time to happen.

The same tool in malicious user hands can be used offensively to get an update on any latest hacks, code leakage, etc..

</details>

<details><summary><strong>TheTHE: The Thread Hunting Experience</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![David Garcia](https://img.shields.io/badge/David%20Garcia-informational) ![Pablo San Emeterio](https://img.shields.io/badge/Pablo%20San%20Emeterio-informational) ![Sergio de los Santos](https://img.shields.io/badge/Sergio%20de%20los%20Santos-informational)

🔗 **Link:** [TheTHE: The Thread Hunting Experience](https://github.com/epavlick/turker-demographics/blob/master/dictionaries/qual-cutoff/0.50/dictionary.ilo)  
📝 **Description:** TheTHE is an environment intended to help analysts and hunters over the early stages of their work in an easier, unified and quicker way. One of the major drawbacks when dealing with a hunting is the collection of information available on a high number of sources, both public and private.

All this information is usually scattered and sometimes even volatile.

Perhaps at a certain point there is no information on a particular IOC (Indicator of Compromise), but that situation may change within a few hours and become crucial for the investigation.

Based on our experience on Threat Hunting, we have created a free and open source framework to make the early stages of the investigation simpler from:

- Automation of tasks and searches.

- Rapid API processing of multiple tools.

- Unification of information in a single interface, so that screenshots, spreadsheets, text files, etc. are not scattered.

- Enrichment of collected data.

- Periodic monitoring of a given IOC in case new information or related movements appear.

TheTHE has a web interface where the analyst starts its work by entering IOCs that will be sent to a backend, where the system will automatically look up for such resource on the various configured platforms in order to obtain unified information from different sources and access related reports or data existing on them. Furthermore, any change in the resources to be analyzed will be monitored.

Everything is executed on a local system, without needing to share information with third parties until such information is not organized, linked, complete and synthesized. This allows that in case the information must be analyzed on any other platform later (such as a Threat Intelligence Platform), it can be done in the most enriching possible manner.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>TapIt: SMS Phishing Framework</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Samuel Pua](https://img.shields.io/badge/Samuel%20Pua-informational)

🔗 **Link:** Not Available  
📝 **Description:** Email phishing is the weapon of choice for most attackers and red teamers alike for getting initial compromise on a network. Email phishing awareness is also heightened in today's cyber security atmosphere. What if I told you there's another social engineering method to achieve initial compromise that is largely unnoticed by defenders?

Mobile phones and SMS are technologies that are largely unmonitored by defenders. TapIt aims to exploit scenarios and situations where SMS Phishing (SMiShing) may be used by attackers to achieve their goals, such as initial compromise, credentials harvesting & 2FA phishing.

TapIt allows easy execution of large-scale SMS phishing campaigns, allowing SMS to be sent to large number of recipients, and to follow-up with tracking of these SMS. Its in-built functionality will also allow ease of setup for purpose of credentials harvesting, delivery of payloads and social engineering.

</details>

---