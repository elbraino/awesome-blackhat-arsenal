# Asia 2015
---
📍 12 tools demonstrated at **Black Hat Arsenal Asia 2015**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [Others](#others) (1)
- [🌐 Web/AppSec](#-webappsec) (1)
- [📱 Mobile Security](#-mobile-security) (1)
- [🔴 Red Teaming](#-red-teaming) (5)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (2)
- [🔵 Blue Team & Detection](#-blue-team--detection) (1)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (1)
---
## Others
<details><summary><strong>ShinoBOT Suite</strong> — Shota Shinogi</summary>

**Track:** — · **Event:** Asia 2015  
🔗 **Link:** Not Available  
📝 **Description:** Usually, the malware used in the targeted attack does not come alone. There are exploit documents, dropper/downloader, decoy files, backdoor, and C2 server. Additional techniques used include packer, steganography, DGA, and crypto. ShinoBOT Suite is a tool kit to create and deploy such whole stuff with just a few clicks, to simulate a highly sophisticated attack campaign. The new second version of ShinoBOT Suite contains several way for the exploit (icon spoofing, extension spoofing).

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>OWASP Xenotix XSS Exploit Framework</strong> — Ajin Abraham</summary>

**Track:** Web AppSec · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/ajinabraham/owasp-xenotix-xss-exploit-framework](https://github.com/ajinabraham/owasp-xenotix-xss-exploit-framework)  
📝 **Description:** OWASP Xenotix XSS Exploit Framework is an advanced Cross-Site Scripting (XSS) vulnerability detection and exploitation framework. Xenotix provides zero false positive XSS detection by performing the scan within the browser engines where in real world, payloads get reflected. Xenotix scanner module is incorporated with three intelligent fuzzers to reduce the scan time and produce better results. If you really don't like the tool logic, then leverage the power of Xenotix API to make the tool work like you wanted it to work. It is claimed to have the world's 2nd largest XSS payloads of about 4800+ distinctive XSS payloads. It is incorporated with a feature-rich information gathering module for target reconnaissance. The exploit framework includes real-world offensive XSS exploitation modules for penetration testing and proof-of-concept creation. Say no to alert pop-ups in PoC. Pen-testers can now create appealing proof-of-concepts within a few clicks.

</details>

---
## 📱 Mobile Security
<details><summary><strong>YSO Mobile Security Framework</strong> — Ajin Abraham</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/torque59/YSO-Mobile-Security-Framework](https://github.com/torque59/YSO-Mobile-Security-Framework)  
📝 **Description:** YSO Mobile Security Framework is an intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static and dynamic analysis. We've been depending on multiple tools to carry out reversing, decoding, debugging, code review, and pen-test and this process requires a lot of effort and time. YSO Mobile Security Framework can be used for effective and fast security analysis of Android APK/Android app source code/iOS app source code. The static analyzer is able to perform automated code review, detect insecure permissions and configurations, and detect insecure code like ssl overriding, ssl bypass, weak crypto, obfuscated codes, permission bypasses, hardcoded secrets, improper usage of dangerous APIs, leakage of sensitive/PII information, and insecure file storage. The dynamic analyzer runs the application in a VM and detects the issues at run time. Further analysis is done on the captured network packets, decrypted HTTPS traffic, application dumps, logs, error or crash reports, debug information, stack trace, and the application assets like files, preferences, and databases. This framework is highly scalable that you can add your custom rules with ease. We will be extending this framework to support other mobile platforms like Tizen, Windows phone etc. in future. A quick and clean report can be generated at the end of the tests.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>CapTipper</strong> — Omri Herscovici</summary>

**Track:** Malware Offense · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/omriher/captipper](https://github.com/omriher/captipper)  
📝 **Description:** CapTipper is a python tool to analyze, explore, and revive HTTP malicious traffic. CapTipper sets up a web server that acts exactly as the server in the PCAP file and contains internal tools, with a powerful interactive console, for analysis and inspection of the hosts, objects, and conversations found. The tool provides the security researcher with easy access to the files and the understanding of the network flow, and is useful when trying to research exploits, pre-conditions, versions, obfuscations, plugins, and shellcodes. Feeding CapTipper with a drive-by traffic capture (e.g. of an exploit kit) displays the user with the REQUEST_URI's that were sent and metadata responses. The user can at this point browse to http://127.0.0.1/[URI] and receive the response back to the browser. In addition, an interactive shell is launched for deeper investigation using various commands such as hosts, hexdump, info, ungzip, body, client, dump, and more.

</details>

<details><summary><strong>MetasploitHelper</strong> — Keith Lee, Michael Gianarakis</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/milo2012/metasploitHelper](https://github.com/milo2012/metasploitHelper)  
📝 **Description:** Metasploit is widely used by penetration-testers during pen-test. They contain a lot of useful exploits that can be used during penetration tests. However, it is a painful task to search for related exploits after running a Nmap scan. It is possible that we could forget to use a potential exploit that could get us a shell on the remote system. There are two main types of exploits in Metasploit that we need to consider: Metasploit modules that target URI and modules that target specific ports. I developed MetasploitHelper so that we can bridge Nmap and Metasploit modules. This tool is meant to save a lot of time looking up exploits during penetration tests.

</details>

<details><summary><strong>MITMf - Framework for Man in the Middle Attacks</strong> — Marcello Salvati</summary>

**Track:** Network Attacks · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/byt3bl33d3r/MITMf](https://github.com/byt3bl33d3r/MITMf)  
📝 **Description:** MITMf combines old and new man-in-the-middle techniques into a framework! Have a cool attack that works in a MITM scenario? Just write a plugin!Currently, the available plugins are:Responder - LLMNR, NBT-NS, and MDNS poisonerSSLstrip+ - Partially bypass HSTSSpoof - Redirect traffic using ARP Spoofing, ICMP Redirects DHCP Spoofing, and modify DNS queriesBeEFAutorun - Autoruns BeEF modules based on clients OS or browser typeAppCachePoison - Perform app cache poison attacksSessionHijacking - Performs session hijacking attacks, and stores cookies in a Firefox profileBrowserProfiler - Attempts to enumerate all browser plugins of connected clientsCacheKill - Kills page caching by modifying headersFilePwn - Backdoor executables being sent over http using bdfactoryInject - Inject arbitrary content into HTML contentJavaPwn - Performs drive-by attacks on clients with out-of-date Java browser pluginsjskeylogger - Injects a JavaScript keylogger into clients webpagesReplace - Replace arbitary content in HTML contentSMBAuth - Evoke SMB challenge-response auth attemptsUpsidedownternet - Flips images 180 degrees

</details>

<details><summary><strong>Pentoo</strong> — Anton Bolshakov</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/pentoo/pentoo-overlay](https://github.com/pentoo/pentoo-overlay)  
📝 **Description:** Pentoo is Linux distribution designed for penetration testing. It includes huge up-to-date and tested collection of tools for web, network, wireless, radio, voice, rce security assessments, and forensics investigations. It can run as a LiveUSB or installed on your permanent media. Based on Gentoo Linux, it is available as an overlay for an existing Gentoo installation and can be customized for your needs. In addition, binary profile with precompiled packages are also available. Pentoo comes hardened by default so both userspace applications and the kernel are protected against all types of memory corruption exploits including zero days.

</details>

<details><summary><strong>UYR</strong> — Ali Hadi</summary>

**Track:** Malware Offense · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/mariam118/uyr](https://github.com/mariam118/uyr)  
📝 **Description:** Under Your Radar (UYR) is a new application layer covert channel. It applies multimedia steganographic techniques to hide a secret message. UYR could also be used for data exfiltration and go totally under the radar and bypass monitoring and detection systems due to its novelty way of communication.UYR in its current version could be used for:Secret CommunicationsExfiltrating Text Files (ASCII)Exfiltrating Other Small Binary FilesThe novelty behind UYR is that in reality you're not transferring any messages or text; you're only transferring a KEY!

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Nmap2Nessus</strong> — Keith Lee, Michael Gianarakis</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/milo2012/nmap2nessus](https://github.com/milo2012/nmap2nessus)  
📝 **Description:** Nessus is an awesome tool for vulnerability assessment. For vulnerabilities assessments, sometimes it is useful to run Nmap along side with Nessus. Nmap output can be easily manipulated and the data can be used as input for other tools. Most of the time, we are often faced with tight deadlines. Running the same scan using Nmap and then with Nessus could take up a lot of time and generate a large amount of network traffic. What this tool does is parse a NMAP .xml file, extract ports and IP addresses from the file, and automatically launch a Nessus scan using this information (instead of having to scan the whole network and all the ports again). This results in a faster scan. The tool then queries Nessus for job status and automatically saves the report locally when done. The tool also parses the Nessus reports and extracts important findings from the report so that you don't have to read through the whole report (you can but you don't have to). If you are using VMware Fusion/Workstation, you can use the VMrun command to automatically spin up a VM containing Nessus in a headless mode, runs Nessus scan and shuts down the VM when done.

</details>

<details><summary><strong>SecPod Saner</strong> — Preeti Subramanian</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2015  
🔗 **Link:** [https://www.secpod.com/](https://www.secpod.com/)  
📝 **Description:** A free vulnerability scanner and compliance scanner with remediation. Most malware makes use of loopholes in the system and targets desktops and end-user applications. The anti-malware products that are available in the market focus on cleaning an already infected system based on known malware signatures. It is reported that 67% of malware is unnoticed by anti-virus or anti-malware products because of their polymorphic nature. Hardening the security posture of the system, knowing the loopholes, and applying fixes is a very effective and proven defense system. Although prevalent in the enterprise segment, home and mobile users do not get the benefit of effective vulnerability and configuration management. SecPod Saner is a lightweight, easy to use, enterprise-grade security solution for proactively assessing and securing your personal computer. It identifies security loopholes, misconfiguration, and remediates to ensure systems remain secure.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>CuckooDroid</strong> — Idan Revivo, Ofer Caspi</summary>

**Track:** Malware Defense · **Event:** Asia 2015  
🔗 **Link:** [https://github.com/idanr1986/cuckoo-droid](https://github.com/idanr1986/cuckoo-droid)  
📝 **Description:** To combat the growing problem of Android malware, we present a new solution based on the popular open source framework Cuckoo Sandbox to automate the malware investigation process. Our extension enables the use of Cuckoo's features to analyze Android malware and provides new functionality for dynamic and static analysis. Our framework is extensible and modular, allowing the use of new, as well as existing, tools for custom analysis. The main capabilities of our Cuckoo Android Extension include:Dynamic Analysis - based on Dalvik API hookingStatic Analysis - Integration with AndroguardEmulator Detection PreventionInfrastructure options:Nested VMs for ARM Emulation and VMISupports Android Emulator or Physical DevicesExamples of well-known malware will be used to demonstrate the framework capabilities and its usefulness in malware analysis.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>CLAW</strong> — Joe Cummins</summary>

**Track:** Smart Grid/Industrial Security · **Event:** Asia 2015  
🔗 **Link:** Not Available  
📝 **Description:** Red Tiger Labs Control Layer Assessment Workstation is looking to redefine the way that ICS SCADA and other critical infrastructure utilities examine their cybersecurity posture. Developed in partnership with the Canadian Federal Government, under the direction of ICS experts, the toolset takes a passive approach to cybersecurity by learning to "look, listen, and feel" each network. Building into its suite of cutting-edge technologies developed with the brightest minds in Canadian InfoSec, CLAW combines visualization, mitigation, and remediation activities into one cohesive view of the entire network. The audience will learn not only how this toolset is effectively raising the bar from both an enterprise and control systems perspective, but also real world instances of incident response, vulnerability assessment, and early detection of gaps and overlaps within existing deployments.

</details>

---
