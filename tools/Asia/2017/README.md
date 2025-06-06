# Asia 2017
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2017** event held in **Asia**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [📱 Mobile Security](#📱-mobile-security)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
---
## 🔴 Red Teaming
<details><summary><strong>CellAnalysis</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pedro Cabrera](https://img.shields.io/badge/Pedro%20Cabrera-informational)

🔗 **Link:** [CellAnalysis](https://github.com/pcabreracamara)  
📝 **Description:** CellAnalysis is a tool every pentester should add to his/her arsenal. Nowadays there are other tools intended to find fake cells (fake stations, IMSI Catchers, etc.), most of them use active monitoring; that is, they monitor traffic coming to the SIM card on a smartphone, so that only cell attacks are scanned on the same network as the SIM card. CellAnalysis offers a different approach, it performs a passive traffic monitoring, so it doesn't require a SIM card or a mobile device, just an OsmocomBB phone or compatible device SDR (rtlsdr, usrp, hackrf or bladerf) to start monitoring all the frequencies of the GSM spectrum.Far from being an out-of-the-box tool, it has been developed using shell-scripting to make easier the code modification or the customization by the pentester, as well as the integration with other tools. SDR device or OsmocomBB phone connected to the computer running Linux will analyze the spectrum or a part of it, in search of cells and for each cell found, a quantitative and qualitative analysis of the information transmitted will be carried out. Alarms generation is not based on a scoring system, but each parameter chosen as a potential threat will generate an alarm if it is evaluated as such in the cell under study.

</details>

<details><summary><strong>Damn Vulnerable SS7 Network</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Akib Sayyed](https://img.shields.io/badge/Akib%20Sayyed-informational)

🔗 **Link:** [Damn Vulnerable SS7 Network](https://github.com/akibsayyed/safeseven)  
📝 **Description:** Telecom network was closed for years but recent advancement in open source telecom opens new doors for telecom hacking. SS7 is core network protocol in 2G and 3G. Many people have proved that these network is insecure, but to date no proper tool or vulnerable network is available in the information security community.This talk will present security loopholes in SS7 network and will cover the SS7 Protocol security and the real telecom security penetration testing on the lab. The demonstration is prepared from real SS7 Penetration testing experience. During this demo I'm going to publish my SS7 Penetration testing tool that I've built for SS7 Assessment. The Damn vulnerable SS7 Network will also be available for information security community. The talk will first present the basics of this vulnerability including: information leaks, denial of service, toll and billing fraud, privacy leaks and SMS fraud.Attendees will able to understand the basics of the SS7 network and tool usage and in additional; attendees will also understand the different type of attacks in the SS7 network.Here are some attacks supported by this tool:Subscriber privacy leaksBilling fraudsDenial of service attacksRevenue FraudsIdentity impersonation attacksIntercepting incoming servicesIllegal redirects

</details>

<details><summary><strong>MetasploitHelper Reloaded</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Keith Lee](https://img.shields.io/badge/Keith%20Lee-informational) ![Maxwell Koh](https://img.shields.io/badge/Maxwell%20Koh-informational)

🔗 **Link:** Not Available  
📝 **Description:** MetasploitHelper was developed to assist penetration testers in internal engagements. There are a large number of exploits and modules that are available to penetration testers to use. However, it is often difficult and challenging for penetration testers to keep up to date with the latest exploits.MetasploitHelper tends to make things easier for testers by testing and matching Metasploit modules against open ports and URI paths on the target hosts.What's New!Better detection and matching for web application exploits in MetasploitExploit-DB is a very popular source of working exploits. Currently, there are more than 21,298 web application exploits available.The number of exploits for web applications are increasing at a very fast rate due to more applications being developed and used.We have added a parser for the web application exploits in Exploit-DB and added them to metasploitHelper and now you can scan and detect more exploitable vulnerabilities much easier.

</details>

<details><summary><strong>Shadow-Box: Lightweight Hypervisor-Based Kernel Protector</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Seunghun Han](https://img.shields.io/badge/Seunghun%20Han-informational) ![Junghwan Kang](https://img.shields.io/badge/Junghwan%20Kang-informational)

🔗 **Link:** [Shadow-Box: Lightweight Hypervisor-Based Kernel Protector](https://github.com/YukZhao/SEConfPaperList)  
📝 **Description:** Protection mechanisms running in the kernel-level (Ring 0) cannot completely prevent security threats such as rootkits and kernel exploits because the threats can subvert the protections with the same privileges. This means protections need to be provided with higher privileges. Creating Ring -1 is plausible using VT such as ARM TrustZone, Intel VT-x, and AMD AMD-v. The existing VT (Virtualization Technologies) supports to separate the worlds into a host (normal world, ring -1, host) and a guest (normal world, ring 0 ~ ring 3). Previous research such as NumChecker, Secvisor, NICKLE, Lares, and OSck used VT to protect kernel.In this demo, we show a security monitoring framework for operating systems, Shadow-box, using state-of-the-art virtualization technologies. Shadow-box is introduced at Black Hat Asia 2017 briefing and has a novel architecture inspired by a shadow play. We made Shadow-box from scratch, and it is primarily composed of a lightweight hypervisor and a security monitor. The lightweight hypervisor, Light-box, efficiently isolates an OS inside a guest machine, and projects static and dynamic kernel objects of the guest into the host machine so that our security monitor in the host can investigate the projected images. The security monitor, Shadow-Watcher, places event monitors on static kernel elements and tests security of dynamic kernel elements. We manipulate address translations from the guest physical address to the host physical address in order to exclude unauthorized accesses to the host and the hypervisor spaces. In that way, Shadow-box can properly introspect the guest operating system and mediate all accesses, even when the operating system is compromised.Shadow-box is an open source project (MIT license), and we have been successfully operating Shadow-box in real world since last year. Real world environment is different from laboratory environment. So, we have gone through many trials and errors for a year, and have learned lessons from them. We share our know-hows about using virtualization technology and deploying research into the wild.

</details>

<details><summary><strong>ShinoBOT.ps1</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Shota Shinogi](https://img.shields.io/badge/Shota%20Shinogi-informational)

🔗 **Link:** [ShinoBOT.ps1](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/red_team/shinobot.md)  
📝 **Description:** ShinoBOT is a RAT simulator for the pentesters, researchers.The powershell based version is released and it allows you to test the detection performance of your security environment against the powershell based attacks, which increase recently.As the previous version you can use ShinoBOT Suite to perform the whole APT scenario, from exploit to data exfiltration.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>HaboMalHunter: An Automated Malware Analysis Tool for Linux ELF Files</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jingyu Yang](https://img.shields.io/badge/Jingyu%20Yang-informational) ![Zhao Liu](https://img.shields.io/badge/Zhao%20Liu-informational)

🔗 **Link:** [HaboMalHunter: An Automated Malware Analysis Tool for Linux ELF Files](https://github.com/Tencent/HaboMalHunter/blob/master/WhitePaper.md)  
📝 **Description:** HaboMalHunter is an automated malware analysis tool for Linux ELF files, which is a sub-project of Habo Analysis System independently developed by Tencent Antivirus Laboratory. It can comprehensively analyze samples from both static information and dynamic behaviors, trigger and capture behaviors of the samples in the sandbox and output the results in various formats. The generated report reveals significant information about process, file I/O , network and system calls.Recently, HaboMalHunter has opened its source code under the MIT license, aimed to share and discuss the automatic analysis technology with researchers alike. The project applies digital forensics techniques, such as kernel space system call tracing and memory analysis, and it emphasizes the importance of collaboration with mainstream security tools by making it easy to add third-party YARA rules and supporting the output of .mdb files that are hash-based signature of the ClamAV. The tool, by generating a .syscall file containing a system call number sequence, is also friendly to artificial intelligence research on malware classification and detection.HaboMalHunter has also been deployed and validated with a large-scale cluster at Tencent Antivirus Laboratory. With the processing ability of thousands of ELF malware samples per day, most of which are from the VirusTotal, HaboMalHunter helps security analysts extract static and dynamic features effectively and efficiently. We hope to present the technical architecture and the detailed implementation about HaboMalHunter and to demonstrate it with several typical real-world Linux malware samples.DOWNLOAD: https://github.com/Tencent/HaboMalHunter

</details>

<details><summary><strong>LAMMA 1.0</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ajit Hatti](https://img.shields.io/badge/Ajit%20Hatti-informational)

🔗 **Link:** Not Available  
📝 **Description:** LAMMA 1.0 is an attempt to create a Swiss-Army-Knife for security and quality Assessment of Cryptographic implementations. This major update of LAMMA has all new modules for testing trust stores, source code analysis and logical flaws in crypto-coding.LAMMA 1.0 with new features & fixes makes crypto-testing more effective and smoother even for large scale implementations. You can use and enhance LAMMA 1.0, as it's a FREE and OPEN SOURCE.

</details>

<details><summary><strong>Smart Whitelisting Using Locality Sensitive Hashing</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jonathan Oliver](https://img.shields.io/badge/Jonathan%20Oliver-informational) ![Jayson Pryde](https://img.shields.io/badge/Jayson%20Pryde-informational)

🔗 **Link:** [Smart Whitelisting Using Locality Sensitive Hashing](https://github.com/hrbrmstr/tlsh/blob/master/R/tlsh-package.R)  
📝 **Description:** Using cryptographic hashes (such as SHA1 or MD5) for whitelisting results in some limitations. Machine Learning extensions of whitelisting may be used for execution control, verification, minimizing false positives from other detection methods or other purpose.Locality Sensitive Hashing is a state of the art method in machine learning for the scalable approximate-nearest-neighbor search.The identification of executable files which are very similar to known legitimate executable files fits very well within this paradigm.ToolsWe provide open source tools for the evaluation of TLSH (a locality sensitive hash) of executable programs.We also provide a backend query service which we will make available to researchers on an ongoing basis.In this talk, we show the effectiveness of applying locality sensitive hashing techniques to identify files similar to legitimate executable files. In the demo we will:Give a brief explanation of locality sensitive hashingDescribe typical modifications made to legitimate executable files (such as security updates, patches, functionality enhancements, and corrupted files)Given a program P, demonstrate how the tool can be used to query for similar executable filesDemonstrate how meta data (such as certificates) can be employed to confirm the legitimacy of program P

</details>

<details><summary><strong>Zenected Threat Defense VPN</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tomasz Jakubowski](https://img.shields.io/badge/Tomasz%20Jakubowski-informational)

🔗 **Link:** Not Available  
📝 **Description:** Zenected is a cloud-based security threat protection service. It's delivered through a set of pre-configured services. Once a user connects to Zenected, that user's network traffic is filtered to keep the bad things out (e.g. phishing sites, malware). The only thing this a user has to configure on the endpoint device (be it a mobile device, a desktop or laptop or IoT device) is your VPN connection. Oh, btw - because you are using VPN, your network traffic is kept secret even if you connect using your favorite coffee store WFi.All mentioned services are updated every hour with a new set of threat indicators. The feeds are delivered by Perun Works.Zenected is easy to manage. It uses a web front-end for administrators to manage your instance. An administrator user can:Manage Zenected users including adding more admin usersBlacklist URLs or domain names that you don't want your users to accessWhitelist URLs or domain names, that were identified as malicious but you still want your users to be able to get to themReview exception requests from usersIf you are a Zenected end-user what you will like about it, is:No need to install additional software on your mobile phone, tablet or laptop â Zenected uses standard OS features build-in into all modern systemsIf you encounter a certain resource blocked by the system, you can request an exception. Each exception is then reviewed by an administrator.More details available on the webpage: https://zenected.com

</details>

---
## 🔍 OSINT
<details><summary><strong>Maltego Have I Been Pwned?</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Christian Heinrich](https://img.shields.io/badge/Christian%20Heinrich-informational)

🔗 **Link:** [Maltego Have I Been Pwned?](https://github.com/cmlh/Maltego-haveibeenpwned/blob/master/Transform_Hub/Transform_Hub.xml)  
📝 **Description:** "Have I been pwned?" allows you to search across multiple data breaches to see if your email addresses or aliases has been compromised by Duowan, Taobao, Tianya, etcMaltego is a link analysis application of technical infrastructure and/or social media networks from disparate sources of Open Source INTelligence (OSINT).  Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World  and Top 125 Network Security Tools by the Nmap Project.The integration of "Have I been pwned?" with Maltego presents these breaches in an easy to understand graph format that can be enriched with other sources of data.

</details>

<details><summary><strong>MineMeld</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Luigi Mori](https://img.shields.io/badge/Luigi%20Mori-informational)

🔗 **Link:** [MineMeld](https://github.com/jtschichold)  
📝 **Description:** Using threat intelligence to enforce security policy poses several challenges. Sources of threat indicators often place indicators in multiple formats or format them inconsistently. Using indicators from multiple sources and packaging them into different formats requires a large investment of time and effort, especially as you discover new sources of indicators. It is also difficult to keep track of updates to threat indicator sources, since they are updated at different times and not always on a regular basis. To automate many of these manual processes, we have released MineMeld.MineMeld is an open source Threat Intelligence framework you can use, among other things, to process indicators and automatically enforce policy on your firewall or augment logs in your SIEM. At the core of MineMeld is a flexible and extensible engine where the data flow is described via a graph of nodes exchanging indicators with a protocol inspired by BGP. By changing the nodes and how they are connected, you can easily define any kind of Threat Intelligence processing logic. And if you need support for a new format, a new protocol or a new logic, you can develop & add your own custom node to the graph.

</details>

---
## 📱 Mobile Security
<details><summary><strong>NAD - A Tool for Performing Dynamic Runtime Analysis of Android Functions</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Han Lee](https://img.shields.io/badge/Han%20Lee-informational)

🔗 **Link:** [NAD - A Tool for Performing Dynamic Runtime Analysis of Android Functions](https://github.com/MattPD/cpplinks/blob/master/analysis.dynamic.md)  
📝 **Description:** Android application penetration testing goes further than testing the client to server communication. In order to get a holistic view on the risk exposure, a thorough analysis of the application has to be done to understand how the application works. This is also imperative to be able to bypass jailbreak detection, SSL pinning, or figure out how the application is handling encryption (e.g. being able to decrypt certain values).There are several approaches available:The application can be decompiled, modified and recompiled. This approach however may not always work due to errors while decompiling.Patch the application by utilizing method hooks and overriding the original method. In order to identify the correct code and method to patch, the penetration tester has to go through the very time consuming process of figuring out the correct methods.Adding to the frustration, most applications in release mode produce minified and obfuscated code. The above-mentioned problems makes analyzing an Android application a very tedious process, even before the actual analysis of the application has started. Currently there are no tools available for Android that allow for easy method hooking. This is why I started developing NAD, a tool which allows testers to perform on the fly method hooks.This talk aims to demonstrate an Android tool built upon the Xposed framework. This tool is an attempt to be the "Burp suite" for Android application methods. It provides the user with several abilities to ease such frustration and make life easier:Perform trace method callsIntercept all methods of the Android applicationPause the applicationModify the input parameters of the hooked methodModify the return value of the hooked methodMy goal for developing this tool is to save time and provide more insight into compiled Android applications.DOWNLOAD: https://github.com/HanLee/Not-a-debugger

</details>

<details><summary><strong>OWASP Seraphimdroid</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Ade Yoseman Putra](https://img.shields.io/badge/Ade%20Yoseman%20Putra-informational)

🔗 **Link:** [OWASP Seraphimdroid](https://github.com/OWASP/PageCreator/blob/master/all_leaders.csv)  
📝 **Description:** Indonesia is undoubtedly one of the most attractive markets in Southeast Asia. With a population of over 250 million - the largest in the region and the fourth largest in the world, after China, India, and the US - who wouldn't keep an eye on this market?According to We Are Social's compendium of world digital stats, Indonesia now has 88.1 million active internet users, up 15 percent over the past 12 months. Its mobile market has exploded over the past couple of years. SIM subscriptions in Indonesia stand at 326.3 million, way more than its population. This means each mobile phone user owns an average of two SIM cards. 85 percent of the population own mobile phones, while 43 percent carry smartphones.Mobile apps offer a level of convenience that the world has never known before. From home, the office, on the road and even from the hotel room in another country on vacation - can login to any voicemail at work, check the credit card balance, view the bank balance, buy new clothes, book travel and more. This extreme level of convenience has brought with it an extreme number of security risks as user's credit card details, bank logins, passwords and more are flying between devices and backend databases and systems across the net. Understanding these risks can help many people prepare their app and protect, their data and their users.OWASP Seraphimdroid is a privacy and security protection app for Android devices. It enables users to protect their devices against malicious software (viruses, trojans, worms, etc.), phishing SMS, MMS messages, execution of dangerous USSD codes, theft and loosing. Also, it enables user to protect their privacy and to control the usage of applications and services via various kinds of locks.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>OpenSCAP</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Martin Preisler](https://img.shields.io/badge/Martin%20Preisler-informational)

🔗 **Link:** [OpenSCAP](https://github.com/mpreisler)  
📝 **Description:** OpenSCAP is the only free and open source implementation of the NIST SCAP standard. It has two major use cases:Vulnerability assessment - enables users to automatically scan their machines for vulnerabilities using OVAL CVE feeds coming from the operating system vendors - Red Hat, Canonical, SUSE, ... OpenSCAP can load the CVE feed and examine the machine, virtual machine storage image or container. Any missing patches are reported.Security compliance - allows fully automated evaluation and remediation of machines using SCAP security policies. Instead of looking at vulnerabilities in this use-case we are looking for weaknesses in the configuration. A good source for SCAP security policies is the open source SCAP Security Guide project which we will demo with OpenSCAP. Check out the list of available products and profiles by visiting https://static.open-scap.org/One of the main improvements in the latest 1.2 branch is the ability to scan various resources using similar command-line interface. We will cover scanning bare-metal machines, remote machines over ssh, VMs, VM storage images, containers and container images.SCAP Workbench is a GUI front-end for OpenSCAP. It allows users to customize security policies for their organization by selecting/deselecting rules and choosing different values (e.g.: password min length) for evaluation. The result can be saved in a so-called tailoring file. To demonstrate we will make such a customized policy.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Unicorn's RFID Armoury</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Haoqi Shan](https://img.shields.io/badge/Haoqi%20Shan-informational) ![Yang Qing](https://img.shields.io/badge/Yang%20Qing-informational) ![Yunding Jian](https://img.shields.io/badge/Yunding%20Jian-informational)

🔗 **Link:** Not Available  
📝 **Description:** RFID and contact-less smart cards have become pervasive technologies nowadays. IC/RFID cards are generally used in security systems such as airport and military bases that require access control. This presentation introduces the details of contact-less card security risk firstly, then the principles of low frequency(125KHz) attack tool, HackID Pro, will be explained. This tool contains an Android App and a hardware which can be controlled by your phone. HackID Pro can emulate/clone any low frequency IC card to help you break into security system, just type few numbers on your phone. After 125KHz, this presentation will show you how to steal personal information from EMV bank card, whose carrier frequency is high frequency, 13.56MHz, just sitting around you. In the end, our defense tool, Card Defender, will be dissected to explain how this product can protect your card and informations in both high/low frequency way and some tricks that this defense tool can do.

</details>

<details><summary><strong>WiDy: WiFi 0wnage in Under $5</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Vivek Ramachandran](https://img.shields.io/badge/Vivek%20Ramachandran-informational) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational) ![Ashish Bhangale](https://img.shields.io/badge/Ashish%20Bhangale-informational)

🔗 **Link:** Not Available  
📝 **Description:** WiDy is an open source Wi-Fi Attack and Defense platform created to run on the extremely cheap ESP8266 (<$5) IoT platform. We've written a simple framework which you can hack and create your own tools or automate attack/defense tasks. Among the attacks WiDy is able to perform out of the box, include:Honeypot AttacksCaptive Portal AttacksServing Exploits to browsers using DNS redirectionWi-Fi ScannerWi-Fi Be Gone (similar to TV-be-gone)Sniffing and InjectionBeacon Floods like MDKDeauthentication & DisasscoationClient monitoringWiFi IDS/IPS functionalityâ¦ other interesting applicationsThe key advantage of using the ESP8266 to recreate Wi-Fi attack/defense functionality is that anyone can now build these tools and physically deploy them in under $5 in the field! One can only imagine the kind of projects the community can create once the core code is available to modify and hack. We have also used the Arduino based platform to make it easier to work with our code. Of course, experienced developers can recreate/port this code to work with the manufacturer SDKs or with the Open ESP SDK. The code is written entirely in C.All code and scripts will be open sourced under MIT license and launched at Black Hat Asia Arsenal!

</details>

---