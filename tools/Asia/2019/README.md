# Asia 2019
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2019** event held in **Asia**.
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
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
---
## 🔴 Red Teaming
<details><summary><strong>ACSploit: Exploit Algorithmic Complexity Vulnerabilities</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Scott Tenaglia](https://img.shields.io/badge/Scott%20Tenaglia-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>CommandoVM: Security Distribution for Penetration Testers and Red Teamers</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jacob Barteaux](https://img.shields.io/badge/Jacob%20Barteaux-informational) ![Blaine Stancill](https://img.shields.io/badge/Blaine%20Stancill-informational) ![Nhan Huynh](https://img.shields.io/badge/Nhan%20Huynh-informational)

🔗 **Link:** [CommandoVM: Security Distribution for Penetration Testers and Red Teamers](https://github.com/mandiant/commando-vm)  
📝 **Description:** CommandoVM is an open-source Windows-based security distribution designed for Penetration Testers and Red Teamers. It is an add-on from FireEye's very successful Reverse Engineering distribution: FLARE VM. Much like Kali Linux, CommandoVM is designed with an arsenal of open-source offensive tools that will help operators achieve assessment objectives.

Being built on Windows, CommandoVM comes with all the native support for accessing Active Directory environments. CommandoVM includes Web Application assessment tools, scripting languages (such as Python and Go), Information Gathering tools (such as Nmap, WireShark, and PowerView), Exploitation Tools (such as PowerSploit, GhostPack and Mimikatz), Persistence tools, Lateral Movement tools, Evasion tools, Post-Exploitation tools (such as FireEye's SessionGopher), Android Hacking tools, Remote Access tools, Command-Line tools, and all the might of FLARE VM's reversing tools.

Quality-of-Life changes to the OS include: disabling UAC, Windows Defender and Windows Firewall, disabling LLMNR and NetBIOS , having some pinned applications (CMD, PowerShell, Sublime Text, VS Code) run as administrator automatically, as well as added context menu options like "Open With Sublime Text" and "Open Command Prompt Here" to ease the frustration of working with a Windows pen-testing environment. CommandoVM strives to be your go-to Windows environment for penetration tests, red team engagements, and Capture-the-Flag events.

</details>

---
## Others
<details><summary><strong>CIRCO: Cisco Implant Raspberry Controlled Operations</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Emilio Couto](https://img.shields.io/badge/Emilio%20Couto-informational)

🔗 **Link:** [CIRCO: Cisco Implant Raspberry Controlled Operations](https://gist.github.com/standardgalactic/7f03809c56f4b098b95a50ada32cd02c)  
📝 **Description:** Designed under Raspberry Pi Zero and aimed for cover red-team Ops, we take advantage of SecNetDevOps tools to capture network credentials in a stealth mode.

The tool uses a low profile hardware/electronics and different methods for credentials exfiltration. It also uses a combination of honeypots and information gather to lure Automation Systems into reveling network credentials (ssh/telnet/snmp) to our implant.

</details>

<details><summary><strong>CQTools: The New Ultimate Hacking Toolkit</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Paula Januszkiewicz](https://img.shields.io/badge/Paula%20Januszkiewicz-informational) ![Adrian Denkiewicz](https://img.shields.io/badge/Adrian%20Denkiewicz-informational) ![Mike Jankowski-Lorek](https://img.shields.io/badge/Mike%20Jankowski-Lorek-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>RF-Xfil: Prototype Toolkit for Data Exfiltration Over Radio Frequencies</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Jie Feng Ho](https://img.shields.io/badge/Jie%20Feng%20Ho-informational) ![Ragul Balaji Velusamy Sathiakumar](https://img.shields.io/badge/Ragul%20Balaji%20Velusamy%20Sathiakumar-informational) ![Andre Ng](https://img.shields.io/badge/Andre%20Ng-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>DaaS: Decompilation as a Service</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Lucas Esposito](https://img.shields.io/badge/Lucas%20Esposito-informational) ![Rodrigo Cetera](https://img.shields.io/badge/Rodrigo%20Cetera-informational)

🔗 **Link:** Not Available  
📝 **Description:** "Decompilation-as-a-Service" or "DaaS" is a tool designed to change the way of file decompiling. An analyst usually decompiles malware samples one by one using a program with a GUI. That's pretty good when dealing with a few samples, but it becomes really tedious to do with larger amounts. Not to mention if you have to decompile different types of files, with different tools and even different operating systems. Besides, lots of decompilers cannot be integrated with other programs because they do not have proper command line support.

DaaS aims to solve all those problems at the same time. The most external layer of DaaS is docker-compose, so it can run on any OS with Docker support. All the other components run inside Docker so now we can integrate the decompiler with any program on the same computer. In addition, we developed an API to use DaaS from the outside, so you can also connect the decompiler with programs from other computers and use the decompiler remotely. In our particular case at Deloitte Threat Intelligence team, we needed to decompile thousands of samples received from different systems and to be able to distribute processing and dynamically scale our capabilities.

Although the tool's modular architecture allows you to easily create workers for decompiling many different file types, we started with the most challenging problem: decompile .NET executables. To accomplish that, we used Wine on a Docker container to run Windows decompilers flawlessly on a Linux environment. In addition, on Windows some programs create useless or invisible windows in order to work, so we needed to add xvfb (x11 virtual frame buffer; a false x11 environment) to wrap those decompilers and avoid crashes on our pure command line environment. This allows you to install DaaS in any machine without desktop environment and be able to use any decompiler anyway.

You can access the tool's source code at: https://github.com/codexgigassys/daas

</details>

<details><summary><strong>ProcJack + Clove: Non-Invasive Code Instrumentation</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Toshihito Kikuchi](https://img.shields.io/badge/Toshihito%20Kikuchi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Code instrumentation is expensive work, especially when a target application is large and complex, or even impossible if you don't know the build environment or source code.

This technique, non-invasive code instrumentation, leverages two known techniques: Reflective DLL Injection and Microsoft Detours, enabling you to inject arbitrary code at arbitrary places without re-compiling the target application.

The project consists of two parts: DLL injector and Injectee DLL. You can write your own logic(s) to run and interact with the code of the target process in Assembly and/or C++ and embed it into a DLL file, which can be injected into any user-mode process running on Windows x86 or x64. After injected, the Detours' part of the DLL dynamically re-routes the target's code to run your logic.

Linux, ARM, or kernel-mode is not supported. Injection into Google Chrome and Microsoft Edge will be demonstrated.

Presentation Slides: https://github.com/msmania/procjack/blob/master/BHAsia-2019-Arsenal.pdf

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Ghosts in the Browser: Backdooring with Service Workers</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Emmanuel Law](https://img.shields.io/badge/Emmanuel%20Law-informational) ![Claudio Contin](https://img.shields.io/badge/Claudio%20Contin-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>ModSecurity 3.1: Stepping up the Game for Web Attacks</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Victor Hora](https://img.shields.io/badge/Victor%20Hora-informational) ![Felipe Zimmerle](https://img.shields.io/badge/Felipe%20Zimmerle-informational)

🔗 **Link:** Not Available  
📝 **Description:** With this upcoming release of ModSecurity we are delivering improved performance, stability and new exciting features!

We are bringing the possibility of virtual patch on demand through the ability of reloading the rules without restart among other improvements in that area. Additionally, we will be showing a testing feature that is exclusive to ModSecurity that allows rules writers and WAF administrators to effortlessly search and match for known malware payloads and signatures. This intends to step-up the game on the detection and blocking of countless types of malware and exploits.

In this presentation we will also be demonstrating the flexibility of ModSecurity by showing the feasibility of running a WAF inside an IoT device.

This release includes around 300 commits since the first 3.0 release with fixes, improvements and features added to the bleeding edge version of the open source libModSecurity. It contains a number of improvements in different areas: These include, clean ups, better practices for improved code readability, resilience, overall performance, support to a few missing features, LuaJIT and a number of fixes to actions and transformations.

Last but not least, there's an improved user experience while reading the logs with a new API component that allows the unique id informed on transactions, making possible to match an id that it is already in use by the consuming application (the connector).

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>GyoiThon: Penetration Testing Using Machine Learning</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Masafumi Masuya](https://img.shields.io/badge/Masafumi%20Masuya-informational) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational) ![Toshitsugu Yoneyama](https://img.shields.io/badge/Toshitsugu%20Yoneyama-informational) ![Takeshi Terada](https://img.shields.io/badge/Takeshi%20Terada-informational)

🔗 **Link:** Not Available  
📝 **Description:** In GyioThon released at Black Hat Asia 2018 Arsenal, we used Deep Learning to enable us to identify products that traditional penetration test tools could not identify. In the original GyoiThon, as well as in other tools, it has always been necessary for someone to investigate product-specific features and signature generation with continuous updates, which we've been working to update to make easier. GyoiThon is the growing penetration test tool using Deep Learning. Deep Learning improves classification accuracy in proportion to the amount of learning data. Therefore GyoiThon will be taking in new learning data every scanning. Since GyoiThon uses various features of software included in HTTP response as learning data, you scan more, the accuracy of software detection improves. For this reason, GyoiThon is the growing penetration test tool.

GyoiThon identifies the software installed on web server (OS, Middleware, Framework, CMS, etc...) based on the learning data. After that, GyoiThon executes valid exploits for the identified software. GyoiThon automatically generates reports of scan results. GyoiThon executes the above processing fully automatically.

GyoiThon's major updates:
- Automatically generates the signature to identify various products.
- Can generate signatures necessary for product identification by even users without Deep Learning knowledge using Deep Learning. You no longer have to investigate product-specific features. You no longer need to create a signature, because GyoiThon itself can generate signatures fully automatically.

GyoiThon is the first penetration test tool that made it possible to generate signatures automatically. GyoiThon is evolving as the growing penetration test tool. For further details: https://github.com/gyoisamurai/GyoiThon/blob/master/handout/BHA2018_handout.pdf

GitHub: https://github.com/gyoisamurai/GyoiThon﻿
Presentation Slides: https://github.com/gyoisamurai/GyoiThon/blob/master/handout/BHASIA2019_slide.pdf

</details>

<details><summary><strong>Halcyon IDE: Nmap Script Development IDE</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Sanoop Thomas](https://img.shields.io/badge/Sanoop%20Thomas-informational)

🔗 **Link:** [Halcyon IDE: Nmap Script Development IDE](https://github.com/s4n7h0/Halcyon-IDE)  
📝 **Description:** Halcyon IDE lets you quickly and easily develop Nmap scripts for performing advanced scans on applications and infrastructures with a wide range capabilities from recon to exploitation. It is the first IDE released exclusively for Nmap script development. Halcyon IDE is a free and open-sourced project (always will be) released under MIT license to provide an easier development interface for rapidly growing information security community around the world. The project was initially started as an evening free-time "coffee shop" project and has taken a serious step for its developer/contributors to spend dedicated time for its improvements very actively.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>IoT Hunter: A Framework Tool for Building IoT Threat Intelligence System</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Xiaolong Guo](https://img.shields.io/badge/Xiaolong%20Guo-informational) ![Meng Su](https://img.shields.io/badge/Meng%20Su-informational) ![Lei Bi](https://img.shields.io/badge/Lei%20Bi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Tencent IoT Hunter is a framework tool created to quickly build the IoT threat intelligence platform, which is more specifically designed to analyze IOT threats. The tool contains all important modules for IOT threat analysis, including information collection, data extraction, threat data analysis, and intelligence visualization. Intelligence data includes, but is not limited to, static information extraction, dynamic operation information extraction, and third-party network platform information. The goal of this tool is to help security researchers quickly and easily build their own IOT intelligence platform for IOT malware research and threat tracking.

Using this framework tool, you can get the malicious information (CNC, Domain, function, etc.) in the IoT sample file very precisely and fine-grained. Compared with the traditional simple string extraction, this extraction method is more accurate and supports the extraction of encrypted information. This malicious information can be directly used to integrate into the IoT malicious information base and threat cloud search services, without the need for analysts to re-confirm, greatly improving the efficiency of malicious information processing.

Traditional intelligence information extraction tools are often used to extract predefined information. The framework provides a good extension interface, where users can write personalized plugins to expand the scope of information extraction. For the emerging threats, security analysts can quickly integrate analysis experience such as decryption algorithm into the framework, accurately extract malicious intelligence, and reduce invalid redundant information.

In the tool demonstration phase, we will demonstrate how to use the entire tool. Including the static information of IOT samples. Take popular IOT threats as examples to show how to precisely extract CNC, weak passwords, and configuration files. We will also show how to develop and integrate the platform plug-ins to extract any specific intelligence information of concern. All of the above data information is imported to the platform, security personnel can be free to carry out data analysis, malware track, threat visualization.

</details>

<details><summary><strong>VxHunter: A Tool Set for VxWorks Based Embedded Device Analyses</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Wenzhe Zhu](https://img.shields.io/badge/Wenzhe%20Zhu-informational) ![Ruikai Liu](https://img.shields.io/badge/Ruikai%20Liu-informational) ![Jiashui Wang](https://img.shields.io/badge/Jiashui%20Wang-informational) ![Yu Zhou](https://img.shields.io/badge/Yu%20Zhou-informational)

🔗 **Link:** Not Available  
📝 **Description:** VxWorks is the industry's leading real-time operating system. It has been widely used in various industry scenarios, which require real-time, deterministic performance and, in many cases, safety and security certifications such as the NASA's Insight Spacecraft. There was lot's of research on Linux based Router and camera, rarely seen research of VxWorks based device.

Most of VxWorks based IoT devices on the market didn't contain any built-in debugger like WDB(VxWorks WDB Debug Agent) or command line debugger. Without debugger it's almost impossible to analyze the root cause of vulnerability or exploit vulnerabilities.

VxHunter contains an firmware analyze tool and an serial debugger tool. The firmware analysis tool is an IDA plugin which can automatically analyze and rebase firmware to correct loading address, fix function name from symbol table, etc. The serial debugger tool is designed for the target which didn't have built-in debugger like WDB. With VxHunter's help, we successfully analyzed and exploited the CVE-2018-19528 vulnerability.

</details>

---
## 🔍 OSINT
<details><summary><strong>Maltego: FullContact</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Christian Heinrich](https://img.shields.io/badge/Christian%20Heinrich-informational)

🔗 **Link:** [Maltego: FullContact](https://github.com/cmlh/Maltego-FullContact/blob/master/Transform_Hub.xml)  
📝 **Description:** FullContact allows you to search on an e-mail address, Twitter username, location, name, company, and alias or verify an e-mail address.

Maltego is a link analysis application of technical infrastructure and/or social media networks from disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project.

The integration of FullContact with Maltego links the input to it's e-mail address, Twitter username, location, name, company and alias in an easy to understand graph format that can be enriched with other sources of data.

</details>

<details><summary><strong>RTS: Real Time Scrapper</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Naveen Rudrappa](https://img.shields.io/badge/Naveen%20Rudrappa-informational)

🔗 **Link:** [RTS: Real Time Scrapper](https://github.com/NaveenRudra/RTTM)  
📝 **Description:** RTS (Realtime scrapper) is a tool developed to scrap all pasties, github, reddit, etc. in real time to identify occurrence of search terms configured. Upon match, an email will be triggered. Thus, allowing a company to react in case of leakage of code, any hacks tweeted, etc. and harden themselves against an attack before it goes viral.

</details>

<details><summary><strong>Squatm3gator: 360° Cybersquatting</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Davide Cioccia](https://img.shields.io/badge/Davide%20Cioccia-informational) ![Stefan Petrushevski](https://img.shields.io/badge/Stefan%20Petrushevski-informational)

🔗 **Link:** Not Available  
📝 **Description:** Squatm3gator (presented at BHEU 2018) is a python tool designed to enumerate available and not available domains generated by modifying the original domain name through different techniques:

- Substitution attack
- Flipping attack
- Duplicate attack
- Homoglyph attack

Squatm3gator is based on Squatm3 and will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks.

The new release will contains the following improvements:

- for each domain to retrieve whois information
- highlights soon-to-expire domains
- first release of automatic phishing website detection

Presentation Slides: http://i.blackhat.com/asia-19/Arsenal/BH-Asia-2019_Arsenal.pptx

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>MLsploit: A Cloud-Based Framework for Adversarial Machine Learning Research</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Evan Yang](https://img.shields.io/badge/Evan%20Yang-informational) ![Li Chen](https://img.shields.io/badge/Li%20Chen-informational) ![Nilaksh Das](https://img.shields.io/badge/Nilaksh%20Das-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>NFC Scrambler</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Davis Zheng](https://img.shields.io/badge/Davis%20Zheng-informational) ![Ashley Tan](https://img.shields.io/badge/Ashley%20Tan-informational)

🔗 **Link:** [NFC Scrambler](https://gist.github.com/duhaime/b2226d787214d7780f446b3e081cbf10)  
📝 **Description:** NFC Scrambler is an android app that emulates a rfid card to prevent nfc skimming. Rfid cards are used nearly everywhere, either in the forms of identification cards or credit cards. RFID Skimming statistics reveal that every two seconds a new case of identity theft is reported in the United States; however, not everyone can afford a rfid blocker card or wallet. Thus this app will help them block rfid skimming for free.

</details>

<details><summary><strong>Unprotect Project: Unprotect Malware for the Mass</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Thomas Roccia](https://img.shields.io/badge/Thomas%20Roccia-informational)

🔗 **Link:** [Unprotect Project: Unprotect Malware for the Mass](https://github.com/Spacial/awesome-csirt/blob/master/README.md?plain=1&eCsjs5f=Vat78MGQ)  
📝 **Description:** To perform malicious actions, attackers create malware; however, they cannot achieve their goals unless their attempts remain undetected. There is a cat and-mouse game between defenders and attackers, which includes attackers monitoring the operations of security technologies and practices.

The Unprotect Project is an open-source project that aims to propose a complete classification about Evasion Techniques to help to understand and analyze a malware. This project is dedicated to Windows PE malware but will be extended to other platforms in the future.

Presentation Slides: https://drive.google.com/file/d/1koZ5emW2vu9o3gvWdaWZx_mz90bD3rSH/view

</details>

<details><summary><strong>VoIP Wireshark Attack-Defense Toolkit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational) ![Ashish Bhangale](https://img.shields.io/badge/Ashish%20Bhangale-informational) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational)

🔗 **Link:** [VoIP Wireshark Attack-Defense Toolkit](https://github.com/pentesteracademy/voipshark)  
📝 **Description:** VoIP Wireshark Attack-Defense Toolkit is a collection of Wireshark plugins which enables a pentester to analyze VoIP traffic. The toolkit can provide summary of VoIP traffic, automatically decrypt VoIP calls wherever possible, export the call audio to popular formats, detect attacks/misconfigurations, and highlight the DTMF/SMS interactions. This eliminates the need for a separate software/framework to analyze VoIP traffic. The plugins are written in Lua and are easy to add to Wireshark. And, the toolkit, just like Wireshark, is platform independent.

</details>

<details><summary><strong>Weapons of Office Destruction: Prevention with Machine Learning</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jason Zhang](https://img.shields.io/badge/Jason%20Zhang-informational) ![Felipe Ducau](https://img.shields.io/badge/Felipe%20Ducau-informational)

🔗 **Link:** Not Available  
📝 **Description:** The broad-brush popularity of Microsoft (MS) Office documents led them to become one of the main cyber-attacking vectors to spread malware via email attachments or web downloads. The first major outbreak of its kind is the notorious macro-based malware "Melissa" during the turn of last century and this century. Since 2014 we started to see rising weaponized Office documents, particularly visual basic application (VBA) macro-based attacks (banking Trojan like "Dridex" or ransomware such as "Locky"). According to a Sophos report in 2017, over 80% of document-based malware were delivered via MS Word or Excel files. Even though these attacks are not new in nature, the increasing volume and complexity of the attacks impose huge challenges to traditional signature-based anti-virus (AV) products.

As a countermeasure, AV companies have spent an enormous amount of effort creating heuristic rules over decades for signature-based detection. To better leverage the rules already used in traditional AV solutions, we propose to combine them statistically using a simple random forest-based machine learning (ML) classifier. In this demonstration, a comprehensive list of over 3000 existing heuristic rules is used to train the ML model. The training data feed comprises around 92600 real-world benign and malicious MS Office documents including Word, Excel and PowerPoint file formats. The testing datasets include 17929 malicious files and 12511 benign files collected recently. Evaluation results indicate that the proposed approach exhibits enhanced performance and significantly outperforms eleven well known commercial anti-virus scanners with a much higher true positive rate (TPR) of 98.46% achieved while maintaining a low false positive rate (FPR) of 0.33%. Of the evaluated commercial AV scanners, the best one achieves only a TPR of 87.5%, which is more than 10% lower than the proposed ML model.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>npm-scan: An Extensible, Heuristic-Based Vulnerability Scanning Tool for Installed NPM Packages</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Eugene Lim](https://img.shields.io/badge/Eugene%20Lim-informational) ![Bernard Lim](https://img.shields.io/badge/Bernard%20Lim-informational) ![Matthew Wong](https://img.shields.io/badge/Matthew%20Wong-informational)

🔗 **Link:** [npm-scan: An Extensible, Heuristic-Based Vulnerability Scanning Tool for Installed NPM Packages](https://github.com/davidar/dblp.yaml/blob/master/journals/aes.bib)  
📝 **Description:** An extensible, heuristic-based vulnerability scanning tool for installed npm packages.

Active heuristics-based scanning: quick and easy for anyone to use

Improves/enforces quality of open source coding

</details>

<details><summary><strong>pytm: A Pythonic Framework for Threat Modeling</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Rohit Shambhuni](https://img.shields.io/badge/Rohit%20Shambhuni-informational) ![Izar Tarandach](https://img.shields.io/badge/Izar%20Tarandach-informational)

🔗 **Link:** Not Available  
📝 **Description:** pytm is a Pythonic framework for threat modeling. Developers can define their system in Python code as a collection of objects and annotate them with properties. Security practitioners can add threats to the "Threats" object (see https://github.com/izar/pytm/blob/master/pytm/threats.py). The logic lives in the "condition" of the "Threats" object, where members of target can be logically evaluated. If the "condition" returns a "True", that means the rule found a potential threat. More details at https://github.com/izar/pytm

Usage:
tm.py [-h] [--debug] [--resolve] [--dfd] [--report] [--all]
[--exclude EXCLUDE] [--seq]

optional arguments:
-h, --help show this help message and exit
--debug print debug messages
--resolve identify threats
--dfd output DFD (default)
--report output report
--all output everything
--exclude EXCLUDE specify threat IDs to be ignored
--seq output sequential diagram

</details>

---