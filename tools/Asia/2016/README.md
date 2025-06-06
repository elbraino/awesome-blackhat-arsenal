# Asia 2016
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2016** event held in **Asia**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [📱 Mobile Security](#📱-mobile-security)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
---
## 🔵 Blue Team & Detection
<details><summary><strong>BTA: An Open-Source Active Directory Security Audit Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joffrey Czarny](https://img.shields.io/badge/Joffrey%20Czarny-informational)

🔗 **Link:** [BTA: An Open-Source Active Directory Security Audit Framework](https://github.com/adulau/hack-lu-website/blob/master/agenda/index.md)  
📝 **Description:** When it comes to the security of the information system, Active Directory domain controllers are, or should be, at the center of concerns, which are (normally) to ensure compliance with best practices, and during a compromise proved to explore the possibility of cleaning the information system without having to rebuild Active Directory. Indeed, backdoors can be implemented in Active Directory to help an intruder to gain back his privileges. However, few tools implement this cleaning/survey process despite several ways existing for backdooring Active Directory.We propose to present some possible backdoors which could be set by an intruder in Active Directory to keep administration rights. For example, how to modify the AdminSDHolder container in order to reapply rights after administrator actions. Then, we will present BTA, an audit tool for Active Directory databases, and our methodology for verifying the application of good practices and the absence of malicious changes in these databases. One of example, that we will show, is how to spot accounts which have DCSync rights and pulls account credentials through the standard Domain Controller replication API.The presentation will be organized as follows:We begin by describing the stakes around the Active Directory, centerpiece of any information system based on Microsoft technologies.We will continue by demonstrating some backdoors in order to keep admins rights or to help an intruder to quickly recover admins rights.We will present BTA and the methodology developed to analysis Active Directory.We conclude with a feedback on real world usage of BTA.More information can be found on the Bitbucket repository: https: //bitbucket.org/iwseclabs/bta

</details>

<details><summary><strong>Limon - Sandbox for Analyzing Linux Malwares</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Monnappa K A](https://img.shields.io/badge/Monnappa%20K%20A-informational)

🔗 **Link:** [Limon - Sandbox for Analyzing Linux Malwares](https://github.com/monnappa22/Limon/blob/master/limon.py)  
📝 **Description:** Limon is a sandbox for automating Linux malware analysis. It collects, analyzes, and reports on the run time indicators of Linux malware. It allows one to inspect the Linux malware before execution, during execution, and after execution (post-mortem analysis) by performing static, dynamic and memory analysis using open source tools. Limon analyzes the malware in a controlled environment, monitors its activities and its child processes to determine the nature and purpose of the malware. It determines the malware's process activity, interaction with the file system, network, it also performs memory analysis and stores the analyzed artifacts for later analysis.For more information, please visit this blog post on Limon: http://malware-unplugged.blogspot.in/2015/11/limon-sandbox-for-analyzing-linux.html; the download link is also available on GitHub: https://github.com/monnappa22/Limon.

</details>

<details><summary><strong>VirusTotal</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Karl Hiramoto](https://img.shields.io/badge/Karl%20Hiramoto-informational)

🔗 **Link:** [VirusTotal](https://github.com/orgs/VirusTotal/people)  
📝 **Description:** VirusTotal is the free online file and URL scanner that everyone knows. However there are many free features that many users don't know about such as:A free public API for anyone to automate file or URL analysis.IP address and domain reputation. See malware files known to be associated with a particular IP address or domain, and history Passive DNS infoSearching on file hash, and related filesSysinternals, Carbon black, etc. integrationsStatic analysis of files, structural analysis of many file types (PE, ELF, APK, ZIP, RAR, MACHO, .NET, office, etc)Sandbox dynamic analysis of PE, APK, Apple Mach-O, and applications.ROMS, BIOS, and firmware filesSSDEEP, authentihash, imphash, and other similarity indexesCertificate checks on signed filesWhitelisting of trusted filesFree desktop scanning applications for Windows, MAC, and open source for compilation on linux.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>HackSys Extreme Vulnerable Driver</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ashfaq Ansari](https://img.shields.io/badge/Ashfaq%20Ansari-informational)

🔗 **Link:** [HackSys Extreme Vulnerable Driver](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver)  
📝 **Description:** HackSys Extreme Vulnerable Driver is an intentionally vulnerable Windows Kernel driver developed for security enthusiasts to learn and polish their exploitation skills. HackSys Extreme Vulnerable Driver caters to a wide range of vulnerabilities ranging from simple Buffer Overflow to complex Use After Free, Pool Overflow, Type Confusion and Arbitrary Memory Overwrite. This allows researchers to explore different exploitation techniques for every implemented vulnerabilities. HackSys Extreme Vulnerable Driver also comes with the mitigation for each implemented vulnerability which helps kernel driver developers understand how these mitigations are applied.Source Code: https://github.com/hacksysteam/HackSysExtremeVulnerableDriver Blog: http://www.payatu.com/hacksys-extreme-vulnerable-driver/

</details>

<details><summary><strong>Rudra: The Destroyer of Evil</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ankur Tyagi](https://img.shields.io/badge/Ankur%20Tyagi-informational)

🔗 **Link:** [Rudra: The Destroyer of Evil](https://github.com/7h3rAm/rudra)  
📝 **Description:** Rudra aims to provide a developer-friendly framework for exhaustive analysis of (PCAP and PE) files. It provides features to scan and generate reports that include file's structural properties, entropy visualization, compression ratio, theoretical minsize, etc. These details, alongwith file-format specific analysis information, help an analyst to understand the type of data embedded in a file and quickly decide if it deserves further investigation.Rudra is the only tool to provide an effective bot based query mechanism for scanning files. Users can use Twitter and mention a Pastebin link that stores the base64 encoded version of the file to be scanned. It will pull the file from Pastebin, perform base64 decoding, initiate scanning on decoded file, submit base64 encoded json report to Pastebin and post a reply tweet with its link. This provides a quick and effective option to try Rudra without installing it.Rudra supports scanning PE files and can perform API scans, anti{debug, vm, sandbox} detection, packer detection, authenticode verification, alongwith Yara, shellcode, and regex detection upon them. Additionally, following new features are being added for the first beta release:Interactive console providing access to all internal data structures and objects, exposing a rich API for usersPlugin architecture to operate upon decoded file content (usecases might be to write a decoder for a new RAT found in the wild or to write a custom unpacker for a binary stub, etc.)Extracting subfiles and optionally scanning them if neededHeuristics to identify suspicious network flows and exe filesThe report for each analyzed file can be dumped to disk as a JSON/HTML/PDF. If needed, analysis can be customized via CLI arguments, config file, or interactive console.Rudra also supports protocol identification, decoding, and normalization. It can analyze embedded URLs and IP addresses within files and gather whois/geolocation information for them. Users can view live mapping of identified hosts and correlate the results from different analysis modules to perform deeper investigation.

</details>

<details><summary><strong>StackPivotChecker</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Xiaoning Li](https://img.shields.io/badge/Xiaoning%20Li-informational) ![Haifei Li](https://img.shields.io/badge/Haifei%20Li-informational)

🔗 **Link:** Not Available  
📝 **Description:** StackPivotChecker is a tool to provide instruction level inspection on stack pivoting behavior from 0-day. It provides rapid 0-day analysis capability. This lightweight tool to help research to address first stack pivoting point from complex 0-day execution path; it addressed real 0-day such as CVE-2013-0640.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Halcyon IDE - Unofficial IDE for Nmap Script Development</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Sanoop Thomas](https://img.shields.io/badge/Sanoop%20Thomas-informational)

🔗 **Link:** Not Available  
📝 **Description:** Halcyon is the first unofficial IDE for Nmap script development. The existing challenge in developing Nmap Scripts (NSE) is the lack of an IDE that gives easiness in building custom scripts for real world scanning. Halcyon is free to use, java based application that has code intelligence, code builder, auto-completion, debugging and error correction and a bunch of other features similar like other development IDE(s) for traditional programming languages. This research was started to give better development interface/environment to researchers and thus enhance the number of NSE writers in the community. Halcyon IDE can understand Nmap library and traditional LUA syntax as well. At the same time it also comes with an offline Nmap wiki that helps Nmap script writers an easy way to access development library references. Possible repetitive codes such as web crawling, bruteforcing etc., is pre-built in the IDE and this makes easy for script writers to save their time while development majority of test scenarios. The IDE gives options to debug the code, make code error free, export the code to the library and several other pre/post development tasks from within the same interface itself.

</details>

---
## 📱 Mobile Security
<details><summary><strong>Janus</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Chen Yexuan](https://img.shields.io/badge/Chen%20Yexuan-informational) ![Tang Zhushou](https://img.shields.io/badge/Tang%20Zhushou-informational)

🔗 **Link:** Not Available  
📝 **Description:** Janus is feedback-driven, interactive Android security analysis platform that facilitates a collection of advanced security analysis tools with the capabilities from vulnerability discovery to malicious application detection. Its main purpose is to enable large scale Android application security analysis by integrating automated, customizable analysis results and human interventions.Specifically, Janus works as follows. First, Janus leverages lightweight malware scanners, similarity detection tools, and vulnerability detection tools to help researchers diagnose whether a given Android application is malicious or vulnerable.Next, Janus provides a set of tools to perform more fine-grained and heavier analyses, including dynamic taint analysis, program slicing, and machine learning, etc. In particular, security researchers are involved in this phase. By integrating these automated analyses and human interventions, Janus will confirm the detection results, filter false positives, and also extract the features of the application. These features will be used to guide subsequent analyses to quickly find similar vulnerabilities or malicious applications.We will demonstrate Janus with a number of real world malicious and vulnerable applications.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Pocsuite</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Zhang Zuyou](https://img.shields.io/badge/Zhang%20Zuyou-informational)

🔗 **Link:** Not Available  
📝 **Description:** Pocsuite is an open-source remote vulnerability testing framework developed by the Knownsec Security Team.Written in Python and supported both validation and exploitation two plugin-invoked modes, Pocsuite could import batch targets from files and test them against multiple exploit-plugins in advance.There are two ways to work with Pocsuite: configuring exploit-required arguments and running in console-based modes; and handling the output from steps in interactive modes. Besides, it could display output in a human-friendly graph providing more useful information for pentesters.Like Metasploit, it is a development kit for pentesters to develop their own exploits. Users could utilize some auxiliary modules packaged in Pocsuite to extend their exploit functions or integrate Pocsuite to develop other vulnerability assessment tools.At last, Pocsuite is also an extremely useful tool to integrate Seebug and ZoomEye APIs in a collaborative way. Vulnerability assessment can be done automatically and effectively by searching targets through ZoomEye and acquiring PoC scripts from Seebug or locally.

</details>

<details><summary><strong>Seebug</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Zhong Chenming](https://img.shields.io/badge/Zhong%20Chenming-informational)

🔗 **Link:** [Seebug](https://github.com/echarts-maps/echarts-cities-js)  
📝 **Description:** Seebug is an open vulnerability platform based on vulnerability and PoC/Exp sharing communities. So far, it already has 50,000+ vulnerabilities and 40,000+ PoC/Exps.On this platform, users can submit new vulnerabilities or update information of existing ones that are lacking of details such as summaries, PoC/Exps, solutions, CVE-ID and other basic fields. In exchange, we will reward you with KBs, which can be used to buy other submissions (such as PoCs) or converted into RMB directly (1 KB is equivalent to RMB 5 Yuan currently).Seebug provides an opportunity for vulnerability learning. We plan to open BBS and CFP columns in the near future so that users can submit their technical articles, ideas, and communicate with each other on vulnerability mining issues.Besides, each vulnerability is accompanied by a lifeline, recording all the relevant events during this process and offering a complete picture about the vulnerability development course.With the help of ZoomEye, the latest vulnerabilities across the world can be detected timely and displayed on the vulnerability detail page. Based on the result, we can effectively conduct emergency response activities and provide online detection tools, affected vendor lists and early warning upon necessary.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>SAIVS (Spider Artificial Intelligence Vulnerability Scanner)</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational) ![Takeshi Terada](https://img.shields.io/badge/Takeshi%20Terada-informational)

🔗 **Link:** Not Available  
📝 **Description:** SAIVS is an artificial intelligence to find vulnerabilities in Web applications. The goal of SAIVS is to find vulnerabilities like a human security engineer. In January 2016, We developed the beta SAIVS. Beta SAIVS has the following capabilities:It can crawl simple Web applications. SAIVS can crawl Web applications that include dynamic pages such as "login," "create account" and "information search".It can find for vulnerabilities. SAIVS can find vulnerabilities such as "Cross Site Scripting" and "SQL Injection".It can output a scanning report. SAIVS can output a scanning report. The report includes target URLs and location of the found vulnerabilities.SAIVS can also perform the following human-like actions: "SAIVS recognizes the type of the page. If it crawls the login page without having a login credential, it creates login credential in the create account page. After it log in with the created login credentials, it crawls the rest of the pages and scans for vulnerabilities. When it finishes all pages, it outputs a scanning report." SAIVS uses machine learning algorithms such as Naive Bayes, Q-Learning, Multi-layer Perceptron in order to achieve one of the aforementioned capabilities: It can crawl simple Web applications. Our session will explain how this ability was made possible by the machine learning algorithms.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>SecBee</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Tobias Zillner](https://img.shields.io/badge/Tobias%20Zillner-informational)

🔗 **Link:** [SecBee](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Wireless.md)  
📝 **Description:** SecBee is a ZigBee security testing tool. It is basically a kind of ZigBee vulnerability scanner, which allows the mapping of ZigBee networks and enables security testers and developers to check the actual product implementation for ZigBee specific vulnerabilities.Currently it supports direct and indirect ZigBee communication and provides features for command injection, scan for enabled devices, sniff network keys in plaintext and encrypted with the ZigBee default key and an insecure rejoin request.The tool is still under development and additional features are added. The final goal is to test for the correct application and implementation of every ZigBee security service.

</details>

---
## 🔍 OSINT
<details><summary><strong>SensePost Toolset</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Daniel Cuthbert](https://img.shields.io/badge/Daniel%20Cuthbert-informational)

🔗 **Link:** [SensePost Toolset](https://github.com/planglois925/twitter_networker_simple/blob/master/data.json)  
📝 **Description:** The SensePost Toolset consists of numerous transforms and mini-sets of transforms. This includes OSINT, language translation, twitter monitoring, Spotify, Skype stalking and detailed in-depth foot-printing capabilities.Sense Post Toolkit:https://www.sensepost.com/discover/tools/maltego/osint/SPToolset/

</details>

<details><summary><strong>ZoomEye - CyberSpace Search Engine</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Zhou Yang](https://img.shields.io/badge/Zhou%20Yang-informational)

🔗 **Link:** Not Available  
📝 **Description:** ZoomEye is a cyberspace search engine released in 2013. Unlike Shodan which only crawls the port fingerprints of Internet-connected devices and does less work on fingerprint parsing, ZoomEye crawls on not only Internet-connected devices, but also websites to get the fingerprints. All of these fingerprints are powered by our two major engines Xmap and Wmap. Xmap is specialized to port scanning, and Wmap focuses on Web Application fingerprint crawling and parsing.We distribute the crawlers running 7/24 across the world, providing both host device and web application searches to the public by crawling and indexing. Users can also achieve integration and automation with our platform API.This talk covers a basic introduction on our crawling and analyzing architecture, some thoughts on scanning crawling strategies, and the major process on parsing and analyzing devices and website fingerprints.To better understand the complexity of the cyberspace, we work hard on fingerprint parsing and analysis to get more detailed and complete metadata. We think that more accurate and formatted data will do great help to our research. Besides, some cases will be demonstrated in comparison with Shodan and Censys.io to prove our strengths.The ZoomEye 101 section introduces how ZoomEye helps to enhance our research or do some hacking stuff. The audience will learn not only the revolution history of ZoomEye, but also some helpful Internet research methodologies.

</details>

---