# Asia 2019
---
📍 23 tools demonstrated at **Black Hat Arsenal Asia 2019**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [🌐 Web/AppSec](#-webappsec) (2)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (2)
- [🔍 OSINT](#-osint) (3)
- [🔴 Red Teaming](#-red-teaming) (2)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (2)
- [🔵 Blue Team & Detection](#-blue-team--detection) (6)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (4)
- [🧠 Reverse Engineering](#-reverse-engineering) (2)
---
## 🌐 Web/AppSec
<details><summary><strong>Ghosts in the Browser: Backdooring with Service Workers</strong> — Emmanuel Law, Claudio Contin</summary>

**Track:** Web AppSec · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/clod81/block_service_workers](https://github.com/clod81/block_service_workers)  
📝 **Description:** Service Workers are all the rage for progressive web apps nowadays. This talk will take a look at Service Workers from a different perspective. We'll take a look at how they can be abused and weaponized by attackers. We'll be exploring some techniques on how an attacker can create a pseudo backdoor in the browser and ghost through a victim's browser session to sniff, manipulate, and even proxy data silently. Come find out how MITM can be done at the browser layer and what are some of its limitations. The presentation will include attack demos and we'll also introduce various mitigation mechanisms against them.

</details>

<details><summary><strong>ModSecurity 3.1: Stepping up the Game for Web Attacks</strong> — Victor Hora, Felipe Zimmerle</summary>

**Track:** Web AppSec · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/owasp-modsecurity/ModSecurity](https://github.com/owasp-modsecurity/ModSecurity)  
📝 **Description:** With this upcoming release of ModSecurity we are delivering improved performance, stability and new exciting features! We are bringing the possibility of virtual patch on demand through the ability of reloading the rules without restart among other improvements in that area. Additionally, we will be showing a testing feature that is exclusive to ModSecurity that allows rules writers and WAF administrators to effortlessly search and match for known malware payloads and signatures. This intends to step-up the game on the detection and blocking of countless types of malware and exploits. In this presentation we will also be demonstrating the flexibility of ModSecurity by showing the feasibility of running a WAF inside an IoT device. This release includes around 300 commits since the first 3.0 release with fixes, improvements and features added to the bleeding edge version of the open source libModSecurity. It contains a number of improvements in different areas: These include, clean ups, better practices for improved code readability, resilience, overall performance, support to a few missing features, LuaJIT and a number of fixes to actions and transformations. Last but not least, there's an improved user experience while reading the logs with a new API component that allows the unique id informed on transactions, making possible to match an id that it is already in use by the consuming application (the connector).

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>npm-scan: An Extensible, Heuristic-Based Vulnerability Scanning Tool for Installed NPM Packages</strong> — Eugene Lim, Bernard Lim, Matthew Wong</summary>

**Track:** Code Assessment · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/spaceraccoon/npm-scan](https://github.com/spaceraccoon/npm-scan)  
📝 **Description:** An extensible, heuristic-based vulnerability scanning tool for installed npm packages. Active heuristics-based scanning: quick and easy for anyone to useImproves/enforces quality of open source coding

</details>

<details><summary><strong>pytm: A Pythonic Framework for Threat Modeling</strong> — Rohit Shambhuni, Izar Tarandach</summary>

**Track:** Code Assessment · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/owasp/pytm](https://github.com/owasp/pytm)  
📝 **Description:** pytm is a Pythonic framework for threat modeling. Developers can define their system in Python code as a collection of objects and annotate them with properties. Security practitioners can add threats to the "Threats" object (see https://github.com/izar/pytm/blob/master/pytm/threats.py). The logic lives in the "condition" of the "Threats" object, where members of target can be logically evaluated. If the "condition" returns a "True", that means the rule found a potential threat. More details at https://github.com/izar/pytm Usage: tm.py [-h] [--debug] [--resolve] [--dfd] [--report] [--all] [--exclude EXCLUDE] [--seq] optional arguments: -h, --help show this help message and exit --debug print debug messages --resolve identify threats --dfd output DFD (default) --report output report --all output everything --exclude EXCLUDE specify threat IDs to be ignored --seq output sequential diagram

</details>

---
## 🔍 OSINT
<details><summary><strong>Maltego: FullContact</strong> — Christian Heinrich</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/cmlh/Maltego-FullContact](https://github.com/cmlh/Maltego-FullContact)  
📝 **Description:** FullContact allows you to search on an e-mail address, Twitter username, location, name, company, and alias or verify an e-mail address. Maltego is a link analysis application of technical infrastructure and/or social media networks from disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project. The integration of FullContact with Maltego links the input to it's e-mail address, Twitter username, location, name, company and alias in an easy to understand graph format that can be enriched with other sources of data.

</details>

<details><summary><strong>RTS: Real Time Scrapper</strong> — Naveen Rudrappa</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/NaveenRudra/RTTM](https://github.com/NaveenRudra/RTTM)  
📝 **Description:** RTS (Realtime scrapper) is a tool developed to scrap all pasties, github, reddit, etc. in real time to identify occurrence of search terms configured. Upon match, an email will be triggered. Thus, allowing a company to react in case of leakage of code, any hacks tweeted, etc. and harden themselves against an attack before it goes viral.

</details>

<details><summary><strong>Squatm3gator: 360° Cybersquatting</strong> — Davide Cioccia, Stefan Petrushevski</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/david3107/squatm3gator](https://github.com/david3107/squatm3gator)  
📝 **Description:** Squatm3gator (presented at BHEU 2018) is a python tool designed to enumerate available and not available domains generated by modifying the original domain name through different techniques: - Substitution attack - Flipping attack - Duplicate attack - Homoglyph attack Squatm3gator is based on Squatm3 and will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks. The new release will contains the following improvements: - for each domain to retrieve whois information - highlights soon-to-expire domains - first release of automatic phishing website detection Presentation Slides: https://i.blackhat.com/asia-19/Arsenal/BH-Asia-2019_Arsenal.pptx

</details>

---
## 🔴 Red Teaming
<details><summary><strong>ACSploit: Exploit Algorithmic Complexity Vulnerabilities</strong> — Scott Tenaglia</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/twosixlabs/acsploit](https://github.com/twosixlabs/acsploit)  
📝 **Description:** Algorithmic Complexity (AC) vulnerabilities arise when a program uses an algorithm with a particularly inefficient worst-case computational complexity, and allows a user to provide input that will trigger it. Determining whether a program is vulnerable requires more than an understanding of what algorithms the program implements. It also requires understanding how user input is filtered and formatted before it's given to the potentially exploitable algorithm. One way to do this is with time consuming manual analysis, such as reverse engineering, static code review, or debugging. Alternatively, feeding the algorithm input formatted to trigger its worst case, and then measuring the effects in time (i.e. CPU utilization) and space (e.g. RAM or disk usage) is quicker and requires less skill. ACsploit is a command-line utility that generates worst-case inputs to commonly used algorithms, such as sorting, hashing, string manipulation, etc. It is modular and highly configurable, supporting a wide variety of user-specified constraints on the generated output, allowing it to appropriately fit the requirements of the application under test. ACsploit also supports an equally wide array of output formats to assist the user in delivering the resulting exploit from ACsploit to the target system. ACsploit supports both script-driven and interactive uses through a familiar Metasploit-like interface. Originally developed under the DARPA STAC program to help rapidly triage potential AC vulnerabilities, we are now releasing ACsploit as an open-source tool to the broader vulnerability researcher community. ACsploit comes with algorithmic complexity exploits for 30+ algorithms and is easily extensible. It's designed to allow members of the community to contribute new exploit modules, input constraints, and output formatters to expand upon all aspects of its functionality. Future plans for the development of ACsploit include debugger integration and a testing framework for measuring resource usage by the targeted application.

</details>

<details><summary><strong>CommandoVM: Security Distribution for Penetration Testers and Red Teamers</strong> — Jacob Barteaux, Blaine Stancill, Nhan Huynh</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/mandiant/commando-vm](https://github.com/mandiant/commando-vm)  
📝 **Description:** CommandoVM is an open-source Windows-based security distribution designed for Penetration Testers and Red Teamers. It is an add-on from FireEye's very successful Reverse Engineering distribution: FLARE VM. Much like Kali Linux, CommandoVM is designed with an arsenal of open-source offensive tools that will help operators achieve assessment objectives. Being built on Windows, CommandoVM comes with all the native support for accessing Active Directory environments. CommandoVM includes Web Application assessment tools, scripting languages (such as Python and Go), Information Gathering tools (such as Nmap, WireShark, and PowerView), Exploitation Tools (such as PowerSploit, GhostPack and Mimikatz), Persistence tools, Lateral Movement tools, Evasion tools, Post-Exploitation tools (such as FireEye's SessionGopher), Android Hacking tools, Remote Access tools, Command-Line tools, and all the might of FLARE VM's reversing tools. Quality-of-Life changes to the OS include: disabling UAC, Windows Defender and Windows Firewall, disabling LLMNR and NetBIOS , having some pinned applications (CMD, PowerShell, Sublime Text, VS Code) run as administrator automatically, as well as added context menu options like "Open With Sublime Text" and "Open Command Prompt Here" to ease the frustration of working with a Windows pen-testing environment. CommandoVM strives to be your go-to Windows environment for penetration tests, red team engagements, and Capture-the-Flag events.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>GyoiThon: Penetration Testing Using Machine Learning</strong> — Masafumi Masuya, Isao Takaesu, Toshitsugu Yoneyama, Takeshi Terada</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/gyoisamurai/GyoiThon](https://github.com/gyoisamurai/GyoiThon)  
📝 **Description:** In GyioThon released at Black Hat Asia 2018 Arsenal, we used Deep Learning to enable us to identify products that traditional penetration test tools could not identify. In the original GyoiThon, as well as in other tools, it has always been necessary for someone to investigate product-specific features and signature generation with continuous updates, which we've been working to update to make easier. GyoiThon is the growing penetration test tool using Deep Learning. Deep Learning improves classification accuracy in proportion to the amount of learning data. Therefore GyoiThon will be taking in new learning data every scanning. Since GyoiThon uses various features of software included in HTTP response as learning data, you scan more, the accuracy of software detection improves. For this reason, GyoiThon is the growing penetration test tool. GyoiThon identifies the software installed on web server (OS, Middleware, Framework, CMS, etc...) based on the learning data. After that, GyoiThon executes valid exploits for the identified software. GyoiThon automatically generates reports of scan results. GyoiThon executes the above processing fully automatically. GyoiThon's major updates: - Automatically generates the signature to identify various products. - Can generate signatures necessary for product identification by even users without Deep Learning knowledge using Deep Learning. You no longer have to investigate product-specific features. You no longer need to create a signature, because GyoiThon itself can generate signatures fully automatically. GyoiThon is the first penetration test tool that made it possible to generate signatures automatically. GyoiThon is evolving as the growing penetration test tool. For further details: https://github.com/gyoisamurai/GyoiThon/blob/master/handout/BHA2018_handout.pdf GitHub: https://github.com/gyoisamurai/GyoiThon Presentation Slides: https://github.com/gyoisamurai/GyoiThon/blob/master/handout/BHASIA2019_slide.pdf

</details>

<details><summary><strong>Halcyon IDE: Nmap Script Development IDE</strong> — Sanoop Thomas</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/s4n7h0/Halcyon-IDE](https://github.com/s4n7h0/Halcyon-IDE)  
📝 **Description:** Halcyon IDE lets you quickly and easily develop Nmap scripts for performing advanced scans on applications and infrastructures with a wide range capabilities from recon to exploitation. It is the first IDE released exclusively for Nmap script development. Halcyon IDE is a free and open-sourced project (always will be) released under MIT license to provide an easier development interface for rapidly growing information security community around the world. The project was initially started as an evening free-time "coffee shop" project and has taken a serious step for its developer/contributors to spend dedicated time for its improvements very actively.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>CQTools: The New Ultimate Hacking Toolkit</strong> — Paula Januszkiewicz, Adrian Denkiewicz, Mike Jankowski-Lorek</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/blackdiverx/cqtools](https://github.com/blackdiverx/cqtools)  
📝 **Description:** CQURE Team has written over 200 hacking tools during penetration testing. We decided to choose the top 39 tools and pack them in a toolkit called CQTools. We are going to announce 5 new tools at Black Hat Asia, allowing the ultimate privilege elevation and network attacks! This toolkit allows you to deliver complete attacks within the infrastructure, starting with sniffing and spoofing activities, going through information extraction, password extraction, custom shell generation, custom payload generation, hiding code from antivirus solutions, various keyloggers and leverage this information to deliver attacks. Some of the tools are based on discoveries that were released to the world for the first time by CQURE Team; some of the tools took years to complete, and all of the tools work in a straightforward manner. CQTools is the ultimate toolkit to have when delivering a penetration test. The tools work simply, and we use them in practice during our cybersecurity assignments. Come and have a look at how our CQTools can boost your penetration testing experience!

</details>

<details><summary><strong>MLsploit: A Cloud-Based Framework for Adversarial Machine Learning Research</strong> — Evan Yang, Li Chen, Nilaksh Das</summary>

**Track:** Malware Defense · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/mlsploit](https://github.com/mlsploit)  
📝 **Description:** MLsploit is a machine learning (ML) evaluation and fortification framework designed for education and research. It focuses on ML security related techniques in adversarial settings, such as adversarial creation, detection, and countermeasure. It consists of plug-able components or services which could demonstrate various security research topics. The MLsploit has a service-oriented architecture (SOA), a web portal to interact with users, and a RESTful API to automate the requests. The web portal is the main module to integrate various components through RESTful API with a defined JSON message. Each component can be implemented by any language on any platform with RESTful API supports. The components can be built as a serverless function or a micro-service wrapped into a portable container image. This flexible component design is agnostic to underlining ML module implementation and not lock-in to a specific cloud provider. MLsploit provides essential services to support cloud environments such as unique id, message queue, big data storage, and basic authentication. Several security projects will be demoed in this presentation. The "Resilient ML" is a micro-service for malware classifier creation, inference, and feature evaluation. The "AVPass" and "PETransformer" are Docker wrapped services which can transform malicious binaries to adversarial and bypass the ML detector. The components "Shield" and "Adagio" are defenses against image and audio adversarial. The project "Barnum" is for anomaly detection on Windows platform. MLsploit could integrate various of security projects and evaluate the ML adversarial and defenses. We believe that MLsploit can be a useful general framework for ML security researches. Contributors from ISTC-ARSA: Nilaksh Das, Siwei Li, Chanil Jeon, Jinho Jung*, Shang-Tse Chen*, Carter Yagemann*, Evan Downing*, Haekyu Park, Evan Yang, Li Chen, Michael Kounavis, Ravi Sahita, David Durham, Scott Buck, Polo Chau, Taesoo Kim, Wenke Lee (*equal contribution).

</details>

<details><summary><strong>NFC Scrambler</strong> — Davis Zheng, Ashley Tan</summary>

**Track:** Network Defense · **Event:** Asia 2019  
🔗 **Link:** Not Available  
📝 **Description:** NFC Scrambler is an android app that emulates a rfid card to prevent nfc skimming. Rfid cards are used nearly everywhere, either in the forms of identification cards or credit cards. RFID Skimming statistics reveal that every two seconds a new case of identity theft is reported in the United States; however, not everyone can afford a rfid blocker card or wallet. Thus this app will help them block rfid skimming for free.

</details>

<details><summary><strong>Unprotect Project: Unprotect Malware for the Mass</strong> — Thomas Roccia</summary>

**Track:** Malware Defense · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/fr0gger/unprotect](https://github.com/fr0gger/unprotect)  
📝 **Description:** To perform malicious actions, attackers create malware; however, they cannot achieve their goals unless their attempts remain undetected. There is a cat and-mouse game between defenders and attackers, which includes attackers monitoring the operations of security technologies and practices. The Unprotect Project is an open-source project that aims to propose a complete classification about Evasion Techniques to help to understand and analyze a malware. This project is dedicated to Windows PE malware but will be extended to other platforms in the future. Presentation Slides: https://drive.google.com/file/d/1koZ5emW2vu9o3gvWdaWZx_mz90bD3rSH/view

</details>

<details><summary><strong>VoIP Wireshark Attack-Defense Toolkit</strong> — Nishant Sharma, Ashish Bhangale, Jeswin Mathai</summary>

**Track:** Network Defense · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/pentesteracademy/voipshark](https://github.com/pentesteracademy/voipshark)  
📝 **Description:** VoIP Wireshark Attack-Defense Toolkit is a collection of Wireshark plugins which enables a pentester to analyze VoIP traffic. The toolkit can provide summary of VoIP traffic, automatically decrypt VoIP calls wherever possible, export the call audio to popular formats, detect attacks/misconfigurations, and highlight the DTMF/SMS interactions. This eliminates the need for a separate software/framework to analyze VoIP traffic. The plugins are written in Lua and are easy to add to Wireshark. And, the toolkit, just like Wireshark, is platform independent.

</details>

<details><summary><strong>Weapons of Office Destruction: Prevention with Machine Learning</strong> — Jason Zhang, Felipe Ducau</summary>

**Track:** Malware Defense · **Event:** Asia 2019  
🔗 **Link:** Not Available  
📝 **Description:** The broad-brush popularity of Microsoft (MS) Office documents led them to become one of the main cyber-attacking vectors to spread malware via email attachments or web downloads. The first major outbreak of its kind is the notorious macro-based malware "Melissa" during the turn of last century and this century. Since 2014 we started to see rising weaponized Office documents, particularly visual basic application (VBA) macro-based attacks (banking Trojan like "Dridex" or ransomware such as "Locky"). According to a Sophos report in 2017, over 80% of document-based malware were delivered via MS Word or Excel files. Even though these attacks are not new in nature, the increasing volume and complexity of the attacks impose huge challenges to traditional signature-based anti-virus (AV) products. As a countermeasure, AV companies have spent an enormous amount of effort creating heuristic rules over decades for signature-based detection. To better leverage the rules already used in traditional AV solutions, we propose to combine them statistically using a simple random forest-based machine learning (ML) classifier. In this demonstration, a comprehensive list of over 3000 existing heuristic rules is used to train the ML model. The training data feed comprises around 92600 real-world benign and malicious MS Office documents including Word, Excel and PowerPoint file formats. The testing datasets include 17929 malicious files and 12511 benign files collected recently. Evaluation results indicate that the proposed approach exhibits enhanced performance and significantly outperforms eleven well known commercial anti-virus scanners with a much higher true positive rate (TPR) of 98.46% achieved while maintaining a low false positive rate (FPR) of 0.33%. Of the evaluated commercial AV scanners, the best one achieves only a TPR of 87.5%, which is more than 10% lower than the proposed ML model.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>CIRCO: Cisco Implant Raspberry Controlled Operations</strong> — Emilio Couto</summary>

**Track:** Hardware/Embedded · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/ekiojp/circo](https://github.com/ekiojp/circo)  
📝 **Description:** Designed under Raspberry Pi Zero and aimed for cover red-team Ops, we take advantage of SecNetDevOps tools to capture network credentials in a stealth mode. The tool uses a low profile hardware/electronics and different methods for credentials exfiltration. It also uses a combination of honeypots and information gather to lure Automation Systems into reveling network credentials (ssh/telnet/snmp) to our implant.

</details>

<details><summary><strong>IoT Hunter: A Framework Tool for Building IoT Threat Intelligence System</strong> — Xiaolong Guo, Meng Su, Lei Bi</summary>

**Track:** Internet Of Things · **Event:** Asia 2019  
🔗 **Link:** Not Available  
📝 **Description:** Tencent IoT Hunter is a framework tool created to quickly build the IoT threat intelligence platform, which is more specifically designed to analyze IOT threats. The tool contains all important modules for IOT threat analysis, including information collection, data extraction, threat data analysis, and intelligence visualization. Intelligence data includes, but is not limited to, static information extraction, dynamic operation information extraction, and third-party network platform information. The goal of this tool is to help security researchers quickly and easily build their own IOT intelligence platform for IOT malware research and threat tracking. Using this framework tool, you can get the malicious information (CNC, Domain, function, etc.) in the IoT sample file very precisely and fine-grained. Compared with the traditional simple string extraction, this extraction method is more accurate and supports the extraction of encrypted information. This malicious information can be directly used to integrate into the IoT malicious information base and threat cloud search services, without the need for analysts to re-confirm, greatly improving the efficiency of malicious information processing. Traditional intelligence information extraction tools are often used to extract predefined information. The framework provides a good extension interface, where users can write personalized plugins to expand the scope of information extraction. For the emerging threats, security analysts can quickly integrate analysis experience such as decryption algorithm into the framework, accurately extract malicious intelligence, and reduce invalid redundant information. In the tool demonstration phase, we will demonstrate how to use the entire tool. Including the static information of IOT samples. Take popular IOT threats as examples to show how to precisely extract CNC, weak passwords, and configuration files. We will also show how to develop and integrate the platform plug-ins to extract any specific intelligence information of concern. All of the above data information is imported to the platform, security personnel can be free to carry out data analysis, malware track, threat visualization.

</details>

<details><summary><strong>RF-Xfil: Prototype Toolkit for Data Exfiltration Over Radio Frequencies</strong> — Jie Feng Ho, Ragul Balaji Velusamy Sathiakumar, Andre Ng</summary>

**Track:** Hardware/Embedded · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/ragulbalaji/RF-Xfil](https://github.com/ragulbalaji/RF-Xfil)  
📝 **Description:** We present a proof of concept (PoC) tool for exfiltrating data over FM radio frequency generated using an off-the-shelf USB-to-VGA dongle. Developed during Hacksmith v2.0, the RF-Xfil runs on a Linux target, feeding audio, screenshot, text, and keystroke data over a FM radio channel. Specifically, we leveraged osmo-fl2k to generate FM radio signals on the Fresco Logic FL2000 chipset. Using the tool, we were able to exfiltrate data successfully about 50 meters away in a nearby concrete building. This tool may be adapted for Red Teaming engagements to covertly exfiltrate data from within air-gapped environments or for environments with heavily locked-down network controls. With an easy to use command line interface and a cheaper alternative to traditional SDR hardware in the market, RF-Xfil lowers the barrier of entry for prospective enthusiasts looking to learn more about software defined radio (SDR). Future work includes improving the code base for more effective and reliable radio transmission signal amplification, and signal to noise ratio to enhance the viability of persistent data exfiltration.

</details>

<details><summary><strong>VxHunter: A Tool Set for VxWorks Based Embedded Device Analyses</strong> — Wenzhe Zhu, Ruikai Liu, Jiashui Wang, Yu Zhou</summary>

**Track:** Smart Grid/Industrial Security · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/pagalaxylab/vxhunter](https://github.com/pagalaxylab/vxhunter)  
📝 **Description:** VxWorks is the industry's leading real-time operating system. It has been widely used in various industry scenarios, which require real-time, deterministic performance and, in many cases, safety and security certifications such as the NASA's Insight Spacecraft. There was lot's of research on Linux based Router and camera, rarely seen research of VxWorks based device. Most of VxWorks based IoT devices on the market didn't contain any built-in debugger like WDB(VxWorks WDB Debug Agent) or command line debugger. Without debugger it's almost impossible to analyze the root cause of vulnerability or exploit vulnerabilities. VxHunter contains an firmware analyze tool and an serial debugger tool. The firmware analysis tool is an IDA plugin which can automatically analyze and rebase firmware to correct loading address, fix function name from symbol table, etc. The serial debugger tool is designed for the target which didn't have built-in debugger like WDB. With VxHunter's help, we successfully analyzed and exploited the CVE-2018-19528 vulnerability.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>DaaS: Decompilation as a Service</strong> — Lucas Esposito, Rodrigo Cetera</summary>

**Track:** Reverse Engineering · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/sunsmarterjie/daas](https://github.com/sunsmarterjie/daas)  
📝 **Description:** "Decompilation-as-a-Service" or "DaaS" is a tool designed to change the way of file decompiling. An analyst usually decompiles malware samples one by one using a program with a GUI. That's pretty good when dealing with a few samples, but it becomes really tedious to do with larger amounts. Not to mention if you have to decompile different types of files, with different tools and even different operating systems. Besides, lots of decompilers cannot be integrated with other programs because they do not have proper command line support. DaaS aims to solve all those problems at the same time. The most external layer of DaaS is docker-compose, so it can run on any OS with Docker support. All the other components run inside Docker so now we can integrate the decompiler with any program on the same computer. In addition, we developed an API to use DaaS from the outside, so you can also connect the decompiler with programs from other computers and use the decompiler remotely. In our particular case at Deloitte Threat Intelligence team, we needed to decompile thousands of samples received from different systems and to be able to distribute processing and dynamically scale our capabilities. Although the tool's modular architecture allows you to easily create workers for decompiling many different file types, we started with the most challenging problem: decompile .NET executables. To accomplish that, we used Wine on a Docker container to run Windows decompilers flawlessly on a Linux environment. In addition, on Windows some programs create useless or invisible windows in order to work, so we needed to add xvfb (x11 virtual frame buffer; a false x11 environment) to wrap those decompilers and avoid crashes on our pure command line environment. This allows you to install DaaS in any machine without desktop environment and be able to use any decompiler anyway. You can access the tool's source code at: https://github.com/codexgigassys/daas

</details>

<details><summary><strong>ProcJack + Clove: Non-Invasive Code Instrumentation</strong> — Toshihito Kikuchi</summary>

**Track:** Reverse Engineering · **Event:** Asia 2019  
🔗 **Link:** [https://github.com/msmania/procjack](https://github.com/msmania/procjack)  
📝 **Description:** Code instrumentation is expensive work, especially when a target application is large and complex, or even impossible if you don't know the build environment or source code. This technique, non-invasive code instrumentation, leverages two known techniques: Reflective DLL Injection and Microsoft Detours, enabling you to inject arbitrary code at arbitrary places without re-compiling the target application. The project consists of two parts: DLL injector and Injectee DLL. You can write your own logic(s) to run and interact with the code of the target process in Assembly and/or C++ and embed it into a DLL file, which can be injected into any user-mode process running on Windows x86 or x64. After injected, the Detours' part of the DLL dynamically re-routes the target's code to run your logic. Linux, ARM, or kernel-mode is not supported. Injection into Google Chrome and Microsoft Edge will be demonstrated. Presentation Slides: https://github.com/msmania/procjack/blob/master/BHAsia-2019-Arsenal.pdf

</details>

---
