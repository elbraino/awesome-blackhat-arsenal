# Europe 2015
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2015** event held in **Europe**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [🌐 Web/AppSec](#🌐-webappsec)
- [📱 Mobile Security](#📱-mobile-security)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
---
## 📱 Mobile Security
<details><summary><strong>Android Device Testing Framework v.13</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Jake Valletta](https://img.shields.io/badge/Jake%20Valletta-informational)

🔗 **Link:** [Android Device Testing Framework v.13](https://github.com/erlang-punch/awesome-erlang?search=1)  
📝 **Description:** The Android Device Testing Framework ("dtf") project started back in 2014 as a collection of scripts and utilities that aimed to help individuals answer the question: "Where are the vulnerabilities on this mobile device?"  Since then, dtf has grown into a robust and extensive data collection and analysis framework with over 30 modules that allow testers to obtain information from their Android device, process this information into databases, and then start searching for vulnerabilities (all without requiring root privileges).  These modules help you focus on changes made to AOSP components such as applications, frameworks, system services, as well as lower-level components such as binaries, libraries, and device drivers.  In addition, you'll be able to analyze new functionality implemented by the OEMs and other parties to find vulnerabilities.

</details>

<details><summary><strong>Android InsecureBank</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Dinesh Shetty](https://img.shields.io/badge/Dinesh%20Shetty-informational)

🔗 **Link:** [Android InsecureBank](https://github.com/dineshshetty/Android-InsecureBankv2)  
📝 **Description:** Ever wondered how different attacking and exploiting a Mobile application would be, from a traditional web application? Gone are the days when knowledge of just SQL Injection or XSS could help you land a lucrative high-paying infoSec job.Watch as Dinesh walks you through his new and shiny updated custom application - "Android-InsecureBank" and some other source code review tools, to help you understand some known and some not so known Android Security bugs and ways to exploit them.This presentation will cover Mobile Application Security attacks that will get n00bs as well as 31337 attendees started on the path of Mobile Application Penetration testing.Some of the vulnerabilities in the Android InsecureBank application that will be discussed (but not limited to) are:- Flawed Broadcast Receivers- Root Detection and Bypass- Local Encryption issues- Vulnerable Activity Components- Insecure Content Provider access- Insecure Webview implementation- Weak Cryptography implementation- Application Patching- Sensitive Information in MemoryExpect to see a lot of demos, tools, hacking and have lots of fun.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Commix: Detecting And Exploiting Command Injection Flaws</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Anastasios Stasinopoulos](https://img.shields.io/badge/Anastasios%20Stasinopoulos-informational)

🔗 **Link:** [Commix: Detecting And Exploiting Command Injection Flaws](https://github.com/commixproject/commix)  
📝 **Description:** Command injections are prevalent to any application independently of its operating system that hosts the application or the programming language that the application itself is developed.The impact of command injection attacks ranges from loss of data confidentiality and integrity to unauthorized remote access to the system that hosts the vulnerable application. A prime example of a real, infamous command injection vulnerability that clearly depicts the threats of this type of code injection was the recently discovered Shellshock bug.Despite the prevalence and the high impact of the command injection attacks, little attention has been given by the research community to this type of code injection. In particular, we have observed that although there are many software tools to detect and exploit other types of code injections such as SQL injections or Cross Site Scripting, to the best of our knowledge there is no dedicated and specialized software application that detects and exploits automatically command injection attacks. This paper attempts to fill this gap by proposing an open source tool that automates the process of detecting and exploiting command injection flaws on web applications, named as commix, (COMMand Injection  eXploitation).This tool supports a plethora of functionalities, in order to cover several exploitation scenarios. Moreover, Commix is capable ofdetecting, with high success rate, whether a web application is vulnerable to command injection attacks. Finally, during the evaluation of the tool we have detected several 0-day vulnerabilities in applications.Overall, the contributions of this work are: a) We provide a comprehensive analysis and categorization of command injection attacks; b) We present and analyze our open source tool that automates the process of detecting and exploiting command injection vulnerabilities; c) We will reveal(during presentation) several 0-day command injection vulnerabilities that Commix detected on various web based applications from home services (embedded devices) to web servers.

</details>

<details><summary><strong>Credmap: The Credential Mapper</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Roberto Salgado](https://img.shields.io/badge/Roberto%20Salgado-informational)

🔗 **Link:** [Credmap: The Credential Mapper](https://github.com/lightos)  
📝 **Description:** It is not uncommon for people who are not experts in security to reuse credentials on different websites; even security savvy people reuse credentials all the time. For this reason "credmap: the Credential Mapper" was created, to bring awareness to the dangers of credential reuse. Credmap takes a user and password as input and it attempts to login on a variety of known websites to test if the user has reused credentials on any of these. New websites can be easily added with simple knowledge of Python.Credmap is also capable of searching in public credential dumps of compromised websites (e.g. r0ckyou, AM, Adobe, etc.) and collecting the user's password from there to then test with on other websites. Credmap was written purely in Python and is open-source and available on GitHub.

</details>

<details><summary><strong>Dvcs-Ripper</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Vlatko Kosturjak](https://img.shields.io/badge/Vlatko%20Kosturjak-informational)

🔗 **Link:** [Dvcs-Ripper](https://github.com/justinsteven/advisories/blob/main/2022_git_buried_bare_repos_and_fsmonitor_various_abuses.md)  
📝 **Description:** DVCS-Ripper will rip web accessible (distributed) version control systems ranging from Subversion and git to Mercurial and Bazaar. It can rip repositories even when directory browsing is turned off. The new release adds support for ripping packed refs in git and it speeds up git ripping drastically. Currently it is the fastest and most feature packed source code ripper tool.

</details>

<details><summary><strong>From XSS to RCE 20</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Hans-Michael Varbaek](https://img.shields.io/badge/Hans-Michael%20Varbaek-informational)

🔗 **Link:** [From XSS to RCE 20](https://github.com/Varbaek/xsser/blob/master/xsser.py)  
📝 **Description:** This presentation demonstrates how an attacker can utilise XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload.Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications.

</details>

<details><summary><strong>Jack</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Chris Le Roy](https://img.shields.io/badge/Chris%20Le%20Roy-informational)

🔗 **Link:** [Jack](https://github.com/brompwnie)  
📝 **Description:** Jack is a novel web based tool to assist in the identification and illustration of abusing web resources in terms of ClickJacking. Jack allows implementers to identify if certain online resources are vulnerable to ClickJacking and also allows implementers to generate a PoC to harvest submitted user credentials to illustrate the affect of the vulnerability. Jack also allows implementers to generate a local instance of the PoC site and deploy it a HTTP container such as Apache.

</details>

<details><summary><strong>OWASP Security Knowledge Framework</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Riccardo ten Cate](https://img.shields.io/badge/Riccardo%20ten%20Cate-informational) ![Glenn ten Cate](https://img.shields.io/badge/Glenn%20ten%20Cate-informational)

🔗 **Link:** [OWASP Security Knowledge Framework](https://github.com/blabla1337/skf-flask)  
📝 **Description:** Over 10 years of experience in web application security bundled into a single application. The Security Knowledge Framework is a vital asset to the coding toolkit of you and your development team. Use SKF to learn and integrate security by design in your web application.In a nutshell:- Training developers in writing secure code- Security support pre-development (Security by design, early feedback of possible security issues- Security support post-development(Double check your code by means of the OWASP ASVS checklists)- Code examples for secure coding

</details>

---
## 🔴 Red Teaming
<details><summary><strong>D1c0m-X2</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Hudson](https://img.shields.io/badge/Michael%20Hudson-informational)

🔗 **Link:** Not Available  
📝 **Description:** In this second version of the tool, a plugin for the exploitation of ORACLE database will be added, which will become an even more attractive exploit.DICOM (Digital Imaging and Communications in Medicine) is recognized worldwide for the exchange of medical tests, designed for handling, display, storage, printing, and transmission standard. It includes defining a file format and a network communication protocol.Target:D1c0m-X.2 is a tool that is responsible for searching the TCP / IP ports of Robot surgery or x-rays, CT scans, MRI or other medical devices that use this protocol, and once found, check if the firmware is vulnerable. If they are not vulnerable, it will try to exploit using scripts, which are intended to block the connection between the server and the Robot, making a DDOS or accessing the System.Before launching the attack, D1c0m-X.2 also explores the possibility of an intrusion through the Corporative Web of the Hospital or Clinic, if the intrusion is achieved, we proceed to interact with shell console, applying different vulnerabilities, such as SQLI, Default password, etc.Finally, the DUMP of critical information of Patients, Doctors and Staff is automated.

</details>

<details><summary><strong>Nishang - Tracking A Windows User</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nikhil Mittal](https://img.shields.io/badge/Nikhil%20Mittal-informational)

🔗 **Link:** [Nishang - Tracking A Windows User](https://github.com/samratashok/nishang)  
📝 **Description:** In this demonstration, we will see how scripts based on built-in Windows tools Windows PowerShell PowerShell, VB Script, .Net Framework, native commands, Registry etc. could be used to keep track of a Windows user.  In addition to having backdoor access, these tools and scripts provide capabilities like taking pics from user webcam, recording MIC, screen-shot/live-streaming of user screen, logging keys, internet history, location tracking and much more.All the scripts in the demo would be a part of Nishang framework.

</details>

<details><summary><strong>Panoptic</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Roberto Salgado](https://img.shields.io/badge/Roberto%20Salgado-informational)

🔗 **Link:** [Panoptic](https://github.com/lightos)  
📝 **Description:** Since it's debut 2 years ago, Panoptic has become the go-to open source penetration testing tool for automating the process of search and retrieval of common log and config files through path traversal vulnerabilities. For the brand new release, Panoptic will have new and enhanced capabilities, such as being able to automate the escalation of a Local File Inclusion (LFI) vulnerability to Remote Code Execution (RCE) and even spawn a meterpretrer session.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Dockscan</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Vlatko Kosturjak](https://img.shields.io/badge/Vlatko%20Kosturjak-informational)

🔗 **Link:** Not Available  
📝 **Description:** Dockscan is a vulnerability assessment and audit tool for Docker and container installations. It will report on docker installation security issues as well as docker container configurations. The tool helps both system administrator administering Docker to help them secure Docker, as well as security auditors and penetration testers who need to audit Docker installation.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Haka - An Open Source Security Oriented Language</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mehdi Talbi](https://img.shields.io/badge/Mehdi%20Talbi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Haka is an open source security oriented language that allows to specify and apply security policies on live captured traffic. Haka is based on Lua. It is a simple, lightweight (~200 kB) and fast (a JiT compiler is available) scripting language.The scope of Haka is twofold. First of all, Haka enables the specification of security rules to filter unwanted streams and report malicious activities. Haka provides a simple API for advanced packet and stream manipulation. One can drop, create and inject packets. Haka supports also on-the-fly packet modification. This is one of the main features of Haka since all complex tasks such as resizing packets, setting correctly sequence numbers are done transparently to the user. This enables to specify and deploy complex mitigation scenarios.Secondly, Haka is endowed with a grammar allowing to specify protocols and their underlying state machine. Haka supports both type of protocols : binary-based protocols (e.g. dns) and text-based protocols (e.g. http). The specification covers packet-based protocols such as ip as well as stream-based protocols like http. Thanks to that grammar, we were able to specify several protocols including ip, icmp, tcp, udp, http, dns, smtp and ssl.Haka is embedded into a modular framework including multiple packet capture modules (pcap, nfqueue), logging and alerting modules (syslog, elasticsearch), and auxiliary modules such as a pattern matching engine and an instruction disassembler module. The latter allow to write fine-grained security rules to detect obfuscated malware for instance. Haka was designed in a modular fashion enabling users to extend it with additional modules.Haka is intended to be used by all security communities: network security officer wishing to deploy quickly new security controls, academics wishing to evaluate the detection efficiency of a new algorithm, or security experts trying to investigate an incident on a specific protocol such as a scada protocol.

</details>

<details><summary><strong>IntelMQ</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tomas Lima](https://img.shields.io/badge/Tomas%20Lima-informational) ![L. Aaron Kaplan](https://img.shields.io/badge/L.%20Aaron%20Kaplan-informational)

🔗 **Link:** [IntelMQ](https://github.com/certtools/intelmq/blob/develop/AUTHORS)  
📝 **Description:** IntelMQ is a solution for collecting and processing security feeds, pastebins, and tweets using a message queue protocol. It's a community driven initiative called IHAP (Incident Handling Automation Project) which was conceptually designed by European CERTs during several InfoSec events. Its main goal is to give to incident responders an easy way to collect & process threat intelligence thus improving the incident handling processes of CERTs.

</details>

<details><summary><strong>VolatilityBot</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Martin Korman](https://img.shields.io/badge/Martin%20Korman-informational)

🔗 **Link:** [VolatilityBot](https://github.com/mkorman90)  
📝 **Description:** The Volatility Bot-Excavator: effective automation for executable file extraction. Made by and for security researchers.Part of the work security researchers have to go through when they have to study new malware or wish to analyse suspicious executables, is to extract the binary file and all the different satellite injections and strings decrypted during the malware's execution. This initial process is mostly manual, which can make it long and incomprehensive.Enter the Volatility Bot-Excavator. This is a tool developed by and for malware researchers, leveraging the Volatility Framework. This new automation tool cuts out all the guesswork and manual extraction from the binary extraction phase. Not only does it automatically extract the executable (exe), but it also fetches all new processes created in memory, code injections, strings, IP addresses and so on.Beyond the obvious value of having a complete extraction automated and produced in under one minute, the Bot-Excavator is highly effective against a large variety of malware codes and their respective load techniques. It can take on complex malware including banking trojans such as ZeuS, Cridex, and Dyre, just as easily as it extracts from simpler downloaders of the like of Upatre, Pony or even from targeted malware like Havex.After the Bot-Excavator finishes the extraction, it can further automate repair or prepare the extracted elements for the next step in analysis. For example, it can the Portable Executable (PE) header, prepare for static analysis via tools like IDA, go to a YARA scan, etc.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Hardsploit: Like Metasploit But For Hardware Hacking</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Yann Allain](https://img.shields.io/badge/Yann%20Allain-informational)

🔗 **Link:** Not Available  
📝 **Description:** Why we chose to create HardSploit: It is clear that something is needed to help the security community to evaluate, audit and/or control the level of security in embedded systems.HardSploit is a complete tool box (hardware & software), a framework which aims to:- Facilitate the auditing of electronic systems for industry 'security' workers (consultants, auditors, pentesters, product designers, etc.)- Increase the level of security (and trust!) of new products designed by the industryHardSploit Modules & Framework:Hardsploit is an all-in-one tool hardware pentest tool with software and electronic aspects. This is a technical and modular platform (using FPGA) to perform security tests on electronic communications interfaces of embedded devices.The main hardware security audit functions are:- Sniffer- Scanner- Interact- Dump memoryHardsploit's Modules will let hardware pentesters intercept, replay and/or send data via each type of electronic bus used by the hardware target. The level of interaction that pentesters will have depends on the features of the electronic bus.Hardsploit's Modules further enable you to analyze electronic bus (serial and parallel types), JTAG, SPI, I2C's, parallel addresses & data bus on chip.Assisted Visual Wiring Function:No more stress with that tremendous part of Hardware pen testing: You will know what needs to be connected and where!We integrated into the tool an assisted visual wiring function to help you connect your wires to the hardware target:- GUI will display the pin organization (Pin OUT) of the targeted chip.- GUI will guide you throughout the wiring process between Hardsploit Connector and the target- GUI will control a set of LEDs that will turn ON and OFF to easily let you find the right Hardsploit Pin Connector to connect to your targetThe software part of the project will help to conduct an end-to-end security audit and will be compatible (integrated) with existing tools such as Metasploit. We will offer integration with other APIs in the future.Our ambition is to provide a tool equivalent to those of the company Qualys or Nessus (Vulnerability Scanner) or the Metasploit framework but in the domain of embedded systems/electronics.

</details>

<details><summary><strong>Kautilya - Fastest Shells Youll Ever Get</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Nikhil Mittal](https://img.shields.io/badge/Nikhil%20Mittal-informational)

🔗 **Link:** [Kautilya - Fastest Shells Youll Ever Get](https://gist.github.com/tejashinde?direction=asc&sort=updated)  
📝 **Description:** Kautilya is a framework which enables using Human Interface Devices (HIDs) in Penetration Testing. Kautilya is capable of generating ready-to-use payloads for a HID.In this demonstration, you will see how Kautilya could be used to get access to a computer, dumping system secrets in plain, data, executing shellcode in memory, installing backdoors, dropping malicious files and much more. New payloads to backdoor a Windows machine will be released in this presentation.

</details>

---
## 🔍 OSINT
<details><summary><strong>VirusTotal.com</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Karl Hiramoto](https://img.shields.io/badge/Karl%20Hiramoto-informational)

🔗 **Link:** [VirusTotal.com](https://github.com/orgs/VirusTotal/people)  
📝 **Description:** VirusTotal.com is the free online file and URL scanner that everyone knows. However there are many free features that many users don't know about such as:- IP address and domain reputation. See malware files known to be associated with a particular IP address or domain- Passive DNS info- Searching on file hash, and related files- Carbon black integration- Ctatic analysis of files, structural analysis of many file types (PE, ELF, APK, ZIP, RAR, MACHO, .NET, office, etc)- Sandbox dynamic analysis of PE, and APK files- ROMS, BIOS, and firmware files- SSDEEP, authentihash, imphash, and other similarity indexes- Certificate checks on signed files- Whitelisting of trusted files- Free desktop scanning applications for Windows, MAC, and open source for compilation on linux.

</details>

---