# Asia 2018
---
📍 23 tools demonstrated at **Black Hat Arsenal Asia 2018**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (2)
- [📱 Mobile Security](#-mobile-security) (1)
- [🔍 OSINT](#-osint) (1)
- [🔴 Red Teaming](#-red-teaming) (6)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (6)
- [🔵 Blue Team & Detection](#-blue-team--detection) (4)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (3)
---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Jackhammer - One Security Vulnerability Assessment/Management Tool</strong> — Rajagopal VR, Krishna Chaitanya Yarramsetty</summary>

**Track:** Code Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/olacabs/jackhammer](https://github.com/olacabs/jackhammer)  
📝 **Description:** Jackhammer is an integrated tool suite that comes with out-of-the-box industry standard integrations. It is a first-of-its-kind tool that combines static analysis, dynamic web app analysis, mobile security, API security, network security, CMS security, AWS/Azure security tools, docker/container security, and vulnerability manager that gives a complete glimpse into security posture of the organization. Using this suite, even senior leadership can have a comprehensive view of their organization's security. Why was it needed? Security, while being imperative for any organization, it is hard to comprehend by most of the developers. Security engineers need to scrutinize every service or app turning security analysis a time intensive and repetitive. What if there exists a tool that can empower everyone to test their code for vulnerabilities, automate security analysis, and show the overall security hygiene of the company? How does it work? Jackhammer initiates various types of scans using existing proven tools and the results are consumed by onboard vulnerability manager. Unique dashboard presents intuitive interface giving the user a holistic view of the code base. The normalized reports are instantly accessible to developers, QAs, TPMs, and security personnel. It can be plugged/integrated with: CI systems and Git via hooks giving complete control over code commits AWS/Azure account and can keep on scanning complete IP space in realtime Additional commercial/open source tools within few minutes and manage those tools from jackhammerTicketing systems (like Jira) slack/pagerduty for real time alerting in addition to SMS and emails It creates a sandbox using dockers for every tool and scales the systems when the scan needs it and descale on completion of the scans. The spin-up and tear down is a completely automated process so no person needs to look at the resources making it inexpensive and cost-effective. https://github.com/olacabs/jackhammer

</details>

<details><summary><strong>puzzCode Make Backdoors Great Again!</strong> — Sheng-Hao Ma</summary>

**Track:** Code Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/aaaddress1/puzzCode](https://github.com/aaaddress1/puzzCode)  
📝 **Description:** puzzCode is a simple compiler based on mingw, written in C# to build windows applications in such a way that they can't be analysed by standard analysis tools (e.g. IDA, Ollydbg, x64dbg, Snowman Decompiler, etc.) puzzCode is based on MinGW to compile C/C++ source code to assembly language while also obfuscating every instruction. puzzCode transforms each original instruction into obfuscated code by breaking each function into countless pieces. The most important thing is that the executable (exe) file, once compiled by puzzCode will be undetectable by antivirus as it effectively will create a completely new application.

</details>

---
## 📱 Mobile Security
<details><summary><strong>Androsia - A Step Ahead in Securing Sensitive In-Memory Android Application Data</strong> — Samit Anwer</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/samitanwer/Androsia-Documentation](https://github.com/samitanwer/Androsia-Documentation)  
📝 **Description:** Each Android app runs in its own VM, with every VM allocated a limited heap size for creating new objects. Neither the app nor the OS differentiates between regular objects and objects that contain security sensitive information. The sensitive objects like any other object are kept around in the heap until the app hits a memory constraint. The OS then invokes the Dalvik garbage collector in order to reclaim memory from unreferenced objects on the heap and provides the reclaimed memory back to the app. However, there is no guarantee the objects containing security sensitive information will be cleared from memory. Even though objects might not be used ahead in the program, they might still be referenced directly or indirectly by a GC root which would prevent them from getting collected - a situation known as memory leak. Android does not provide explicit APIs to reclaim memory from sensitive objects which are not "used" ahead in the program. "java.security.*" library does provide classes for holding sensitive data (like KeyStore.PasswordProtection) and API's (like destroy()) to remove sensitive content from the objects. However, the onus of calling these APIs is on the developer. Developers may invoke these APIs at a stage very late in the code or worst may even forget to invoke them. This leaves a window of time where the security critical objects, which are not used any further in the program, live in the heap memory and wait to be garbage collected. During this window, a compromise of the app can allow an attacker to read the credentials by dumping the heap memory. This is a needless risk every Android application lives with today. We propose a tool called Androsia, which uses a summary based [1] inter-procedural data-flow analysis to determine the points in the program where security sensitive objects are last used (so that their content can be cleared). Androsia then performs bytecode transformation of the app to flush out the secrets resetting the objects to their default values. [1] D. Yan, G. Xu, and A. Rountev. Rethinking soot for summary-based wholeprogram analysis. In Proceedings of the ACM SIGPLAN International Workshop on State of the Art in Java Program Analysis, SOAP '12, pages 9–14, New York, NY, USA, 2012. ACM

</details>

---
## 🔍 OSINT
<details><summary><strong>Trape: The Phishing Evolution</strong> — Jose Pino, Jhonathan Espinosa</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/jofpin/trape](https://github.com/jofpin/trape)  
📝 **Description:** Trape is a recognition tool that allows you to track people and make phishing attacks in real time; the information you can get is very detailed. The objective is to teach the world the possible outcomes through this strategy -- the big Internet companies could be monitoring you, getting information beyond your IP, such as the sessions of your sites or Internet services.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Automated Penetration Toolkit (APT2)</strong> — Adam Compton</summary>

**Track:** Network Attacks · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/tatanus/apt2](https://github.com/tatanus/apt2)  
📝 **Description:** Nearly every penetration test begins the same way - run a NMAP scan, review the results, choose interesting services to enumerate and attack/exploit, and perform post-exploitation activities. What was once a fairly time consuming manual process, is now automated! Automated Penetration Testing Toolkit (APT2) is an extendable modular framework designed to automate common tasks performed during penetration testing. APT2 can chain data gathered from different modules together to build dynamic attack paths. Starting with a NMAP scan of the target environment, discovered ports and services become triggers for the various modules which in turn can fire additional triggers. Have FTP, Telnet, or SSH? APT2 will attempt common authentication. Have SMB? APT2 determines what OS and looks for shares, null sessions, and other information. Modules include everything from enumeration, scanning, brute forcing, and even integration with Metasploit. Come check out how APT2 will save you time on every engagement. Have you seen APT2 before? Great, now come and check out some of the new and enhanced features which include stream lined operations, additional modules, and improvements to the overall ease of module creation and development.

</details>

<details><summary><strong>CQTools: The Ultimate Hacking Toolkit</strong> — Paula Januszkiewicz, Greg Tworek</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/blackdiverx/cqtools](https://github.com/blackdiverx/cqtools)  
📝 **Description:** CQURE Team has written over 200 hacking tools during penetration testing. We decided to choose the top 35 tools and pack them in a toolkit called CQTools. This toolkit allows you to deliver complete attacks within the infrastructure, starting with sniffing and spoofing activities, going through information extraction, password extraction, custom shell generation, custom payload generation, hiding code from antivirus solutions, various keyloggers and leverage this information to deliver attacks. Some of the tools are based on discoveries that were released to the world for the first time by CQURE Team; some of the tools took years to complete, and all of the tools work in a straightforward manner. CQTools is the ultimate toolkit to have when delivering penetration test. The tools simply work, and we use them in practice during our cybersecurity assignments. Come and have a look how our CQTools can boost your penetration testing experience!

</details>

<details><summary><strong>CrackMapExec v4.0</strong> — Marcello Salvati</summary>

**Track:** Network Attacks · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/byt3bl33d3r/CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec)  
📝 **Description:** Ever needed to pentest a network with 10 gazillion hosts with a very limited time frame? Ever wanted to Mimikatz entire subnets? How about shelling entire subnets? How about dumping SAM hashes? Share spidering? Keeping track of all the credentials you pillaged? (The list goes on)! All while doing this in the stealthiest way possible? Look no further than CrackMapExec! CrackMapExec (a.k.a CME) is a modular post-exploitation tool written in Python that helps automate assessing the security of *large* Active Directory networks. Built with stealth in mind, CME follows the concept of "Living off the Land": abusing built-in Active Directory features/protocols to achieve it's functionality and allowing it to evade most endpoint protection, IDS and IPS solutions. Although meant to be used primarily for offensive purposes, CME can be used by blue teams as well to assess account privileges, find misconfigurations and simulate attack scenarios. In this demo, the author will be showing off v4.0, a major update to the tool bringing more feature and capabilities than ever before! If you are interested in the latest and greatest Active Directory attacks/techniques, weaponizing them at scale and general cool AD stuff this is the demo for you!

</details>

<details><summary><strong>NetRipper - Smart Traffic Sniffing for Penetration Testers</strong> — Ionut Popescu</summary>

**Track:** Malware Offense · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/NytroRST/NetRipper](https://github.com/NytroRST/NetRipper)  
📝 **Description:** NetRipper is a post-exploitation tool targeting Windows systems which uses API hooking in order to intercept network traffic. It also uses encryption-related functions from a low privileged user, making it able to capture both plain-text traffic and encrypted traffic before encryption/after decryption.

</details>

<details><summary><strong>PyExfil</strong> — Yuval Nativ</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/ytisf/PyExfil](https://github.com/ytisf/PyExfil)  
📝 **Description:** PyExfil is a data exfiltration package with various data exfiltration techniques for various scenarios.

</details>

<details><summary><strong>RouterSploit</strong> — Marcin Bury, Blane Cordes</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/threat9/routersploit](https://github.com/threat9/routersploit)  
📝 **Description:** RouterSploit is an exploitation framework for embedded devices written in python.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Archery - Open Source Vulnerability Assessment and Management</strong> — Anand Tiwari</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/archerysec/archerysec](https://github.com/archerysec/archerysec)  
📝 **Description:** Archery is an open-source vulnerability assessment and management tool which helps developers and pentesters to perform scans and manage vulnerabilities. Archery uses popular open-source tools to perform comprehensive scanning for web application and network. It also performs web application dynamic authenticated scanning and covers the whole applications by using selenium. The developers can also utilize the tool for implementation of their DevOps CI/CD environment. The main capabilities of our Archery include: Perform Web and Network Vulnerability Scanning using open-source tools. Correlates and Collaborate all raw scans data, show them in a consolidated manner. Perform authenticated web scanning. Perform web application scanning using selenium. Vulnerability Management. Enable REST API's for developers to perform scanning and Vulnerability Management. Useful for DevOps teams for Vulnerability Management. More documentation here: https://archerysec.github.io/archerysec/

</details>

<details><summary><strong>Faraday v3 - Collaborative Penetration Test and Vulnerability Management Platform</strong> — Emilio Couto</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/infobyte/faraday](https://github.com/infobyte/faraday)  
📝 **Description:** The idea behind Faraday is to help you to share all the information that is generated during a pentest, vulnerability assessment or scan without changing the way you work. You run a command, import a report, and Faraday will normalize the results and share them with the rest of the team in real-time. Faraday has more than 60 plugins available (and counting), including the most popular commercial and open-source tools. If you use a tool that Faraday doesn't have a plugin for, you can create your own! During this presentation we're going to release Faraday v3.0 with all the new features that we were working on for the last couple of months that include a huge back-end change. Come check it out!

</details>

<details><summary><strong>GyoiThon</strong> — Isao Takaesu, Masafumi Masuya, Toshitsugu Yoneyama, Takeshi Terada, Tomoyuki Kudo</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/gyoisamurai/GyoiThon](https://github.com/gyoisamurai/GyoiThon)  
📝 **Description:** GyoiThon is a growing penetration test tool using Deep Learning. Deep Learning improves classification accuracy in proportion to the amount of learning data. Therefore, GyoiThon will be taking in new learning data during every scan. Since GyoiThon uses various features of software included in HTTP response as learning data, the more you scan, the more the accuracy of software detection improves. For this reason, GyoiThon is a growing penetration test tool. GyoiThon identifies the software installed on web server (OS, Middleware, Framework, CMS, etc...) based on the learning data. After that, GyoiThon executes valid exploits for the identified software. GyoiThon automatically generates reports of scan results. GyoiThon executes the above processing automatically. GyoiThon consists of three engines: Software analysis engine - It identifies software based on HTTP response obtained by normal access to web server using Deep Learning base and signature base. Vulnerability determination engine - It collects vulnerability information corresponding to identify software by the software analysis engine. And, the engine executes an exploit corresponding to the vulnerability of the software and checks whether the software is affected by the vulnerability. Report generation engine - It generates a report that summarizes the risks of vulnerabilities and the countermeasure. Traditional penetration testing tools are very inefficient because they execute all signatures; however, unlike traditional penetration testing tools, GyoiThon is very efficient because it executes only valid exploits for the identified software. As a result, the user's burden will be greatly reduce, and GyoiThon will greatly contribute to the security improvement of many web servers.

</details>

<details><summary><strong>Horus - Binary Library Security Scanning Engine</strong> — Qin Chen, Jiashui Wang</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2018  
🔗 **Link:** Not Available  
📝 **Description:** Horus is a scanning engine for mobile security mainly used to detect security risks of binary library, including detection of binary vulnerabilities and malicious behavior. Horus is currently used within Alipay Inc. It is designed as a rule-based framework. As many mobile apps use a large number of third-party libraries - such as libopenssl, libffmpeg and so on - Horus supports security detection of various types of binary libraries. New product or new task connects to it by calling the interface. By adding and removing defined rules (CVE,patch,txt), the user will get a distribution or matching statistic for vulnerability, backdoor or malicious activity, etc. Now,It matches rules at different level: binary function level, binary pattern level and binary instruction level. Horus has resolved thousands of application security risks and help us improve the security of applications effectively and reliably. We want to open this security scanning engine through Arsenal. We hope to improve matching algorithms and performance of Horus in the future with more ai power inside. We also hope more and more security developers can work together to improve Horus.

</details>

<details><summary><strong>Prowler - Cluster Network Scanner</strong> — Faith See Wan Yi, Chi Seng Wong, Timothy Liu</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/tlkh/prowler](https://github.com/tlkh/prowler)  
📝 **Description:** Prowler is a Cluster Network Vulnerability Scanner, developed during Singapore Infosec Community Hackathon - HackSmith v1.0. It is implemented on a cluster of Raspberry Pi and it will scan a network for vulnerabilities, such as default/weak credentials, that can be easily exploited.

</details>

<details><summary><strong>Zeus - AWS Auditing & Hardening Tool</strong> — Deniz Parlak</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/DenizParlak/Zeus](https://github.com/DenizParlak/Zeus)  
📝 **Description:** Zeus is a powerful tool for AWS EC2 /S3 / CloudTrail / CloudWatch / KMS best hardening practices. It checks security settings according to the profiles the user creates and changes them to recommended settings based on the CIS AWS Benchmark source at request of the user.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Cloud Security Suite - One Stop Tool for AWS/GCP Security Audit</strong> — Jayesh Chauhan, Shivankar Madaan</summary>

**Track:** Network Defense · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/SecurityFTW/cs-suite](https://github.com/SecurityFTW/cs-suite)  
📝 **Description:** Nowadays, cloud infrastructure is pretty much the de-facto service used by large/small companies. Most of the major organizations have entirely moved to cloud. With more and more companies moving to cloud, the security of cloud becomes a major concern. While AWS & GCP provides you protection with traditional security methodologies and has a neat structure for authorisation/configuration, its security is as robust as the person in charge of creating/assigning these configuration policies. As we all know, human error is inevitable and any such human mistake could lead to catastrophic damage to the environment. A few vulnerable scenarios: Your security groups, password policy or IAM policies are not configured properly S3 buckets are world-readableWeb servers supporting vulnerable ssl ciphersPorts exposed to public with vulnerable services running on themIf root credentials are usedLogging or MFA is disabledAnd many more such scenarios... Knowing all this, audit of AWS/GCP infrastructure becomes a hectic task! There are few open source tools that help AWS/GCP auditing, but none of them have an exhaustive checklist. Also, collecting, setting up all the tools, and looking at different result sets is a painful task. Moreover, while maintaining big infrastructures, system audit of server instances is a major task as well. CS Suite is a one stop tool for auditing the security posture of the AWS/GCP infrastructure and does OS audits as well. CS Suite leverages current open-source tools capabilities and has other missing checks added into one tool to rule them all. CS-Suite also supports JSON output which can be consumed for further usage.

</details>

<details><summary><strong>QR Safety Scanner</strong> — Tan Ashley</summary>

**Track:** Malware Defense · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/xPrinny/QrSafetyScanner](https://github.com/xPrinny/QrSafetyScanner)  
📝 **Description:** A QR scanner that checks if the QR code contains malicious links. Recently QR codes are being use everywhere, for advertisements, payments, name cards, etc. However, if someone would to exploit these QR codes by hiding malicious links, devices will be infected with malware.

</details>

<details><summary><strong>UserLine</strong> — Chema Garcia</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/THIBER-ORG/userline](https://github.com/THIBER-ORG/userline)  
📝 **Description:** This tool automates the process of creating logon relations from MS Windows Security Events by showing a graphical relation among users domains, source and destination logons, session duration as well as get information regarding logged on users at a given datetime (among other options), providing a starting point to begin the forensic analysis/incident triage.

</details>

<details><summary><strong>WiPi-Hunter - Detects Illegal Wireless Network Activities</strong> — Mehmet Kutlay Kocer, Besim Altinok</summary>

**Track:** Network Defense · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/WiPi-Hunter](https://github.com/WiPi-Hunter)  
📝 **Description:** WipiHunter is developed for detecting illegal wireless network activities; howver, it shouldn't be seen only as a piece of code. Instead, actually it is a philosophy. You can infer from this project new wireless network illegal activity detection methods. New methods, new ideas and different point of views can be obtained from this project. Example: WiFi Pineapple attacks, Fruitywifi, mana-toolkit, karma attack. WiPi-Hunter Modules: PiSavar: Detects activities of PineAP module and starts deauthentication attack (for fake access points - WiFi Pineapple Activities Detection)PiFinger: Searches for illegal wireless activities in networks you are connected and calculate wireless network security score (detect wifi pineapple and other fakeAPs)PiDense: Monitor illegal wireless network activities. (Fake Access Points)PiKarma: Detects wireless network attacks performed by KARMA module (fake AP). Starts deauthentication attack (for fake access points)PiNokyo: If threats like wifi pineapple attacks or karma attacks are active around, users will be informed about these threats.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Firmware Analysis and Comparision Tool (FACT)</strong> — Peter Weidenbach</summary>

**Track:** Hardware/Embedded · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/fkie-cad/FACT_core](https://github.com/fkie-cad/FACT_core)  
📝 **Description:** The Firmware Analysis and Comparison Tool (FACT) is intended to automate Firmware Security analysis. Thereby, it shall be easy to use (web GUI), extend (plug-in system) and integrate (REST API). When analyzing Firmware, you face several challenges: unpacking, initial analysis, identifying changes towards other versions, find other firmware images that might share vulnerabilities you just found. FACT is able to automate many aspects of these challenges leading to a massive speedup in the firmware analysis process. This means you can focus on the fun part of finding new vulnerabilities, whereas FACT does all the boring stuff for you. Source code: https://protect-eu.mimecast.com/s/FefbCNL66FZqmPNsmynnm?domain=github.com Additional information: https://protect-eu.mimecast.com/s/siORCOM00sNLmZACv-Iml?domain=fkie-cad.github.io

</details>

<details><summary><strong>OWASP SecureTea Tool Project</strong> — Ade Yoseman Putra, Bambang Rahmadi Kurniawan Payu</summary>

**Track:** Internet Of Things · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/OWASP/SecureTea-Project](https://github.com/OWASP/SecureTea-Project)  
📝 **Description:** The OWASP SecureTea Project that was developed to be used by anyone who is interested in Security IOT (Internet of Things) and still needs further development. It functions by keeping track of the movement of the mouse/touchpad, detecting who accesses the laptop with mouse/touchpad installed, and sending warning messages via Twitter.

</details>

<details><summary><strong>Project Walrus : An Android App for Card Cloning</strong> — Daniel Underhay, Matthew Daley</summary>

**Track:** Hardware/Embedded · **Event:** Asia 2018  
🔗 **Link:** [https://github.com/TeamWalrus/Walrus](https://github.com/TeamWalrus/Walrus)  
📝 **Description:** Project Walrus is an Android app we're developing to let pentesters make better use of their contactless card devices, like the Proxmark and the Chameleon Mini. Come and see how Walrus can help you on your next red team, or just come so I can clone your access cards.

</details>

---
