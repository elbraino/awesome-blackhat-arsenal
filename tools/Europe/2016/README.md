# Europe 2016
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2016** event held in **Europe**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [🌐 Web/AppSec](#🌐-webappsec)
- [📱 Mobile Security](#📱-mobile-security)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
---
## 📱 Mobile Security
<details><summary><strong>AppMon: Runtime Security Testing & Profiling Framework for Native Apps</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Nishant Das Patnaik](https://img.shields.io/badge/Nishant%20Das%20Patnaik-informational)

🔗 **Link:** Not Available  
📝 **Description:** AppMon is a runtime security testing & profiling framework for macOS, iOS and android apps. It is useful for mobile app penetration testers to validate the security issues report by a source code scanner by validating them by inspecting the API calls at runtime. You may use it for monitoring the app's overall activity during its runtime and focus on things that seem suspicious e.g. information leaks, insecure storage of credentials/secret tokens etc. or insecure implementation of crypto operations or just sniff app's network activity from HTTP to Bluetooth. You may either use one or many of the pre-written user-scripts or quickly learn to write your own scripts modify the app's functionality/logic in the runtime e.g. spoofing the DeviceID, spoofing the GPS co-ordinates, bypassing Apple's TouchID, bypassing root detection etc.We shall demo the features of existing 4 core components: Sniffer, Intruder, Android Tracer & IPA Installer. If there any any additional development to the project we shall include its demo as well.

</details>

<details><summary><strong>Nmap on Android</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Vlatko Kosturjak](https://img.shields.io/badge/Vlatko%20Kosturjak-informational)

🔗 **Link:** [Nmap on Android](https://github.com/kost/NetworkMapper)  
📝 **Description:** Network Mapper is Android frontend for well known Nmap scanner. Frontend will help you to download, install and run Nmap on Android-based phone. It is also a collection of tools to build all known Android architectures: arm, mips and x86 in 32/64 bit architectures.Shiny new 2.0 release will be presented with easy interface and mobile specific scans.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>APT2 - Automated Penetration Testing Toolkit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational) ![Austin Lane](https://img.shields.io/badge/Austin%20Lane-informational)

🔗 **Link:** [APT2 - Automated Penetration Testing Toolkit](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/vulnerability_assessment/apt2.md)  
📝 **Description:** Nearly every penetration test begins the same way; run a NMAP scan, review the results, choose interesting services to enumerate and attack, and perform post-exploitation activities. What was once a fairly time consuming manual process, is now automated! Automated Penetration Testing Toolkit (APT2) is an extendable modular framework designed to automate common tasks performed during penetration testing. APT2 can chain data gathered from different modules together to build dynamic attack paths. Starting with a NMAP scan of the target environment, discovered ports and services become triggers for the various modules which in turn can fire additional triggers. Have FTP, Telnet, or SSH? APT2 will attempt common authentication. Have SMB? APT2 determines what OS and looks for shares and other information. Modules include everything from enumeration, scanning, brute forcing, and even integration with Metasploit. Come check out how APT2 will save you time on every engagement.

</details>

<details><summary><strong>CROZONO Framework: Leveraging Autonomous Devices as an Attack Vector on Industrial Networks</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sheila Ayelen Berta](https://img.shields.io/badge/Sheila%20Ayelen%20Berta-informational) ![Nicolas Villanueva](https://img.shields.io/badge/Nicolas%20Villanueva-informational)

🔗 **Link:** Not Available  
📝 **Description:** CROZONO is a framework that allows performing automated penetration tests from autonomous devices (drones, robots, etc.) that could ease the access to the logical infrastructure of an industrial facility, evading physical barriers. The CROZONO framework is presented in two versions: "CROZONO Explorer" and "CROZONO Attacker."At first, it is advisable to use CROZONO Explorer, as it allows the user to perform information gathering about possible attack vectors on the whole industrial facility's perimeter or any other sector. The information gathered by CROZONO Explorer allows the user to see the location of WiFi Access Points and IP Cameras, together with their security levels. The purpose of this step is to find the easiest way to compromise the industrial facility's security. For example, attacking those WiFi access points which have the lowest security level, if any security measures at all.CROZONO Attacker is a smart framework, it has the capability of performing automated attacks targeted to a network, and to take decisions -without the need of the attacker's intervention- on which attacks to perform based on pre-established parameters and the information gathered about its target. The goal of CROZONO Attacker is to breach the network attacking a WiFi access point and then opening a reverse connection to the attacker via the victim's internet connection. Once performed, CROZONO Attacker allows - through its "LAN discovery" and "LAN Attacks" modules - to discover other devices in the target network and launch several attacks on it.One of the best exclusive features of CROZONO is the report generation about all information gathered. In few minutes, it is possible to explore a zone or an industrial facility's perimeter and know its weak points from the summarization of data captured visually, allowing to see its security exposure levels.

</details>

<details><summary><strong>OWASP ZSC</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ali Razmjoo Qalaei](https://img.shields.io/badge/Ali%20Razmjoo%20Qalaei-informational) ![Brian Beaudry](https://img.shields.io/badge/Brian%20Beaudry-informational)

🔗 **Link:** Not Available  
📝 **Description:** OWASP ZSC is an open source software in python language which lets you generate customized shellcodes and convert scripts to an obfuscated script. This software can be run on Windows/Linux/OSX under python. According to other shellcode generators same as metasploit tools and etc, OWASP ZSC using new encodes and methods which antiviruses won't detect. OWASP ZSC encoderes are able to generate shell codes with random encodes and that allows you to generate thousands of new dynamic shellcodes with same job in just a second,that means, you will not get a same code if you use random encodes with same commands, And that make OWASP ZSC one of the best! During the Google Summer of Code we are working on to generate Windows Shellcode and new obfuscation methods. We are working on the next version that will allow you to generate OSX.

</details>

<details><summary><strong>PowerMemory</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pierre-Alexandre Braeken](https://img.shields.io/badge/Pierre-Alexandre%20Braeken-informational)

🔗 **Link:** [PowerMemory](https://github.com/giMini/PowerMemory/blob/master/PowerMemory.ps1)  
📝 **Description:** PowerMemory is a PowerShell post-exploitation tool. It uses Microsoft binaries and therefore is able to execute on a machine, even after the Device Guard Policies have been set. In the same way, it will bypass antivirus detection. PowerMemory can retrieve credentials information and manipulate memory. It can execute shellcode and modify process in memory (in userland and kernel land as a rootkit). PowerMemory will access everywhere in user-land and kernel-land by using the trusted Microsoft debugger aka cdb.exe which is digitally signed.We will cover the following subjects:User-land proof-of-concept: attacking the digest Security Support Provider byte per byte with PowerShell and Microsoft debugger to retrieve passwords from memoryKernel-land proof-of-concept: Direct Kernel Object Manipulation with PowerShell and Microsoft debugger o Hiding/Un-hiding a process o Protecting a process o Injecting all privileges in a process with SYSTEM identity o Pass-The-Token attackUser-land proof-of-concept: Injecting and executing a shellcode in a remote process with PowerShell and a Microsoft debuggerIf we have time, we will hack the minesweeper too :-)

</details>

<details><summary><strong>WarBerryPi</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yiannis Ioannides](https://img.shields.io/badge/Yiannis%20Ioannides-informational)

🔗 **Link:** [WarBerryPi](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/red_team/warberrypi.md)  
📝 **Description:** What if the only requirements for taking down a corporate network are 60 minutes and $35? Traditional hacking techniques and corporate espionage have evolved. Advanced attacks nowadays include a combination of social engineering, physical security penetration and logical security hacking. It is our job as security professionals to think outside the box and think about the different ways that hackers might use to infiltrate corporate networks.The WarBerry is a customized RaspBerryPi hacking dropbox which is used in Red Teaming engagements with the sole purpose of performing reconnaissance and mapping of an internal network and providing access to the remote hacking team while remaining covert and bypassing security mechanisms. The outcome of these red teaming exercises is the demonstration that if a low cost microcomputer loaded with python code can bypass security access controls and enumerate and gather such a significant amount of information about the infrastructure network which is located at, then what dedicated hackers with a large capital can do is beyond conception. The talk will be comprised of slides and a demonstration of the WarBerry's capabilities in a virtual network.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Automated Vulnerability Assessment & Penetration Testing Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Shaan Mulchandani](https://img.shields.io/badge/Shaan%20Mulchandani-informational) ![Ravi Keerthi](https://img.shields.io/badge/Ravi%20Keerthi-informational)

🔗 **Link:** Not Available  
📝 **Description:** As application, network, and product complexity grow, so do the attack surface and likelihood of vulnerabilities. Highly-skilled pen testers do not scale exponentially, and findings don't make it into secure coding practices or DevOps overnight.How can we enable pen testers to focus on what matters: adversary-oriented penetration testing to detect the most difficult vulnerabilities and exploits? What correlations exist between successful exploits and underlying application or network characteristics? And how can we ensure findings actually make it back into the development lifecycle in a meaningful way?Our research, and Python-based VAPT framework seeks to address these questions, and automates certain tasks to assist pen testers:For each application or network update, network reconnaissance and application/network vulnerability assessments are performed using NMap, Nessus, OpenVAS, and W3AFIdentified vulnerabilities, and their CVEs, are used for retrieving relevant exploits from ExploitDBPenetration tests are performed using W3AF and MetasploitResults obtained at each stage are stored and correlated as part of a (Neo4j-based) knowledge graph, which can be maintained across several (application) releases and tool runs. This allows for:Pen Testers to easily visualize vulnerabilities discovered, and successful/failed exploits - in order to rapidly gain context of additional potential exploits that may be run or vulnerabilities that may be discoverable through sophisticated, manual techniquesDevelopers to visualize vulnerabilities that are persistent across multiple parts of their product/application, and/or across multiple successive releasesWe will demo this initial version at Arsenal, however the extensible nature of our framework allows for integration of additional vulnerability assessment & penetration testing tools or (pre-deployment) code security review tools and their findings as well.

</details>

<details><summary><strong>Dradis: Collaboration and Reporting for InfoSec Teams</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [Dradis: Collaboration and Reporting for InfoSec Teams](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Docs_and_Reports.md?plain=1)  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, and Burp. Started in 2007, the Dradis Framework project has been growing ever since (15,000 commits in the last 12 months). Dradis is the best tool to consolidate the output of different scanners, add your manual findings and evidence and have all the engagement information in one place.Come to see the latest Dradis release in action. It's loaded with updates including new tool, connectors (Metasploit, Brakeman, ...), full REST API coverage, testing methodologies and lots of interface improvements (issue tagging, UX improvements and much more). Come and find out why Dradis is being downloaded over 300 times every week. Come and check it out before we run out of stickers!

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>DeepViolet TLS/SSL Scanner</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Milton Smith](https://img.shields.io/badge/Milton%20Smith-informational)

🔗 **Link:** [DeepViolet TLS/SSL Scanner](https://github.com/spoofzu/DeepViolet/blob/master/src/main/java/com/mps/deepviolet/api/CipherSuiteUtil.java)  
📝 **Description:** DeepViolet TLS/SSL scanner is an information gathering tool for secure web servers. Written in Java, DeepViolet is be run from the command line, as a desktop application, or included as an API in other programs. Use DeepViolet to enumerate web server cipher suites, display X.509 certificate metadata, examine X.509 certificate trust chains, and more. DeepViolet is an open source project written to help educate the technical community around TLS/SSL and strengthen our knowledge of security protocols while we improve security of our web applications. DeepViolet project is always looking for volunteers.

</details>

<details><summary><strong>From XSS to RCE 2.5</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Hans-Michael Varbaek](https://img.shields.io/badge/Hans-Michael%20Varbaek-informational)

🔗 **Link:** [From XSS to RCE 2.5](https://github.com/Varbaek/xsser)  
📝 **Description:** This presentation demonstrates how an attacker can utilise XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes cool notifications and new attack vectors!

</details>

<details><summary><strong>OWASP CSRFGuard</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Azzeddine RAMRAMI](https://img.shields.io/badge/Azzeddine%20RAMRAMI-informational)

🔗 **Link:** [OWASP CSRFGuard](https://github.com/aramrami/OWASP-CSRFGuard)  
📝 **Description:** OWASP CSRFGuard implements a variant of the synchronizer token pattern to mitigate the risk of CSRF attacks. In order to implement this pattern, CSRFGuard must offer the capability to place the CSRF prevention token within the HTML produced by the protected web application. CSRFGuard 3 provides developers more fine grain control over the injection of the token. Developers can inject the token in their HTML using either dynamic JavaScript DOM manipulation or a JSP tag library. CSRFGuard no longer intercepts and modifies the HttpServletResponse object as was done in previous releases. The currently available token injection strategies are designed to make the integration of CSRFGuard more feasible and scalable within current enterprise web applications. Developers are encouraged to make use of both the JavaScript DOM Manipulation and the JSP tag library strategies for a complete token injection strategy.CSRFGuard WikiPage: https://www.owasp.org/index.php/Category:OWASP_CSRFGuard_Project

</details>

<details><summary><strong>WSSAT - Web Service Security Assessment Tool</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Mehmet Yalcin YOLALAN](https://img.shields.io/badge/Mehmet%20Yalcin%20YOLALAN-informational) ![Salih TALAY](https://img.shields.io/badge/Salih%20TALAY-informational)

🔗 **Link:** [WSSAT - Web Service Security Assessment Tool](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/webapp_security/wssat.md)  
📝 **Description:** WSSAT is an open source web service security scanning tool which provides a dynamic environment to add, update or delete vulnerabilities by just editing its configuration files. This tool accepts WSDL address list as input file and performs both static and dynamic tests against the security vulnerabilities. It also makes information disclosure controls.Objectives of WSSAT are to allow organizations:Perform their web services security analysis at onceSee overall security assessment with reportsHarden their web servicesWSSAT's main capabilities include:Dynamic Testing:Insecure Communication; SSL Not Used Unauthenticated Service Method; Error Based SQL Injection; Cross Site Scripting; XML Bomb; External Entity Attack - XXE XPATH Injection; Verbose SOAP Fault MessageStatic Analysis:Weak XML Schema: Unbounded Occurrences; Weak XML Schema: Undefined Namespace; Weak WS-SecurityPolicy: Insecure Transport; Weak WS-SecurityPolicy: Insufficient Supporting Token Protection; Weak WS-SecurityPolicy: Tokens Not ProtectedInformation Leakage: Server or development platform oriented information disclosureWSSAT's main modules are:ParserVulnerabilities LoaderAnalyzer/AttackerLoggerReport GeneratorThe main difference of WSSAT is to create a dynamic vulnerability management environment instead of embedding the vulnerabilities into the code. More information can be found here: https://github.com/YalcinYolalan/WSSAT

</details>

<details><summary><strong>Yaps</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Fabio Nigi](https://img.shields.io/badge/Fabio%20Nigi-informational)

🔗 **Link:** Not Available  
📝 **Description:** The number one security hole is a weak password. Companies are growing without a complete control over exposed services; most of the servers are deployed with default password. Most of the tools today are single host-based, without competing on a cloud/global environment. Configuration and deployment are getting faster -all the services are going in pipeline with automation and scalability focus.Infosec tools need to evolve. The project goal of Yaps *yet another password scanner:*Create a new scanner to work in pipeline with nmap and other source (json, xml, csv) port mapper and enable a scalable full feature weak password scanner, analyse in a flow the port, create a history status based on the history of scan and result, evade incidents and avoid stressful and lockdown test on production servers and giving the users full flexibility to decrease false positive reports.Highly scalable container based (docker, mesos, chronos, python)Modular concept with multi protocol support and fully automated.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Firmware Analysis Toolkit (FAT)</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Aditya Gupta](https://img.shields.io/badge/Aditya%20Gupta-informational)

🔗 **Link:** [Firmware Analysis Toolkit (FAT)](https://github.com/adi0x90/attifyos)  
📝 **Description:** There exists a number of tools in today's security industry which offers static and dynamic analysis of software binaries and mobile applications. However, there is no such toolkit, which helps an embedded or IoT security researcher to analyse firmwares in an in-depth level. FAT or Firmware Analysis Toolkit is a scriptable toolkit suite is a part of Attify's internal pentesting suite which has helped us reduce a significant number of man hours put into firmware analysis in our IoT and smart devices pentest engagements. It comes with an easy to use API which can then be used in additional analysis, as well as for research purposes. It is a toolkit suite which performs static and dynamic analysis of firmwares, also enabling the user to emulate the firmware and having a live firmware device as if a real physical device was sitting on the network. This has been done by taking advantage of Qemu emulation and static vulnerability identification techniques. Below are some of the capabilities of the toolkit : Full emulation of the firmware along with networking Dynamic traffic analysis Static vulnerability identification Integration with tools such as nmap and metasploit for additional assessment and exploitationBy Black Hat EU, there might be more features added to the list which I will later on send once they are in a more concrete stage. FAT has been made possible because of the following open source tools listed below, which FAT leverages at various stages:Binwalk Firmware Modification KitFirmadyneMITMProxyNmapMetasploitSnmpwalkRadare2

</details>

<details><summary><strong>HEATHEN Internet of Things Pentesting Framework</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Chiheb Chebbi](https://img.shields.io/badge/Chiheb%20Chebbi-informational)

🔗 **Link:** [HEATHEN Internet of Things Pentesting Framework](https://github.com/chihebchebbi/Internet-Of-Things-Pentesting-Framework)  
📝 **Description:** Oxford defines the Internet of Things as: "A proposed development of the Internet in which everyday objects have network connectivity, allowing them to send and receive data."Heathen IoT of Things Penetration Testing Framework developed as a research project, which automatically help developers and manufacturers build more secure products in the Internet of Things space based on the Open Web Application Security Project (OWASP) by providing a set of features in every fundamental era:Insecure Web InterfaceInsufficient Authentication/AuthorizationInsecure Network ServicesLack of Transport EncryptionPrivacy ConcernsInsecure Cloud InterfaceInsecure Mobile InterfaceInsufficient Security ConfigurabilityInsecure Software/FirmwarePoor Physical Security

</details>

<details><summary><strong>Offense and Defense Toolkits in High/Low Frequency</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Haoqi Shan](https://img.shields.io/badge/Haoqi%20Shan-informational) ![Yunding Jian](https://img.shields.io/badge/Yunding%20Jian-informational) ![YANG Qing](https://img.shields.io/badge/YANG%20Qing-informational)

🔗 **Link:** Not Available  
📝 **Description:** RFID and contact-less smart cards have become pervasive technologies nowadays. IC/RFID cards are generally used in security systems such as airport and military bases that require access control. This presentation introduces the details of contact-less card security risk firstly, then the principles of low frequency(125KHz) attack tool, HackID Pro, will be explained. This tool contains an Android App and a hardware which can be controlled by your phone. HackID Pro can emulate/clone any low frequency IC card to help you break into security system, just type few numbers on your phone. After 125KHz, this presentation will show you how to steal personal information from EMV bank card, whose carrier frequency is high frequency, 13.56MHz, just sitting around you. In the end, our defense tool, Card Defender, will be dissected to explain how this product can protect your card and information in both high/low frequencies. And a little bit tricks that this defense tool can make.This presentation includes three demonstrations. The first demonstration will show how we can use the self-made hardware, HackID Pro, to clone and emulate common seen low frequency ID card, different from the hardware we used - HackID Pro contains an Android App and a module which inject into your phone by audio interface. Second, we will show people how to steal people's privacy information from their EMV card, just walked by them. Finally, we introduce how can we protect that information by our defense tool, Card Defender, and we will explain the principle detailed.This toolkit is developed by Qihoo 360 UnicornTeam, which has many genius hardware/wireless security researcher. UnicornTeam focuses on embedded device vulnerability mining, 2/3/4G communication security, GPS signal faking, smart car security, etc. Members of UnicornTeam also had presentations on DEFCON, Black Hat, Cansecwest, Ruxcon, HITB, Syscan360 and some other international security conference.

</details>

---