# Asia 2020
---
📍 26 tools demonstrated at **Black Hat Arsenal Asia 2020**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [🌐 Web/AppSec](#-webappsec) (1)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (1)
- [📱 Mobile Security](#-mobile-security) (3)
- [🔍 OSINT](#-osint) (1)
- [🔴 Red Teaming](#-red-teaming) (7)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (3)
- [🔵 Blue Team & Detection](#-blue-team--detection) (5)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (2)
- [🧠 Reverse Engineering](#-reverse-engineering) (1)
- [🧠 Social Engineering / General](#-social-engineering--general) (2)
---
## 🌐 Web/AppSec
<details><summary><strong>ModSecurity 3.0</strong> — Kevin Jones</summary>

**Track:** Web AppSec · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/owasp-modsecurity/ModSecurity](https://github.com/owasp-modsecurity/ModSecurity)  
📝 **Description:** ModSecurity is a toolkit for real-time web application monitoring, logging, and access control. I like to think about it as an enabler: there are no hard rules telling you what to do; instead, it is up to you to choose your own path through the available features.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>The OWASP RAF: Static Application Security Testing Tool</strong> — Ade Yoseman</summary>

**Track:** Code Assessment · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/OWASP/RiskAssessmentFramework](https://github.com/OWASP/RiskAssessmentFramework)  
📝 **Description:** The OWASP Risk Assessment Framework consist of Static Application Security Testing and Risk Assessment tools. Even though there are many SAST tools available for testers, the compatibility and the environment setup process is complex. By using OWASP Risk Assessment Framework's Static Application Security Testing tool, testers will be able to analyze and review their code quality and vulnerabilities without any additional setup. OWASP Risk Assessment Framework can be integrated in the DevSecOps toolchain to help developers to write and produce secure code. User Guide https://github.com/OWASP/RiskAssessmentFramework/blob/master/user-guide.md

</details>

---
## 📱 Mobile Security
<details><summary><strong>Android Application Vulnerability Hunting System</strong> — Lance Jiang, Todd Han, Lilang Wu</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/saeidshirazi/awesome-android-security](https://github.com/saeidshirazi/awesome-android-security)  
📝 **Description:** So far, there are many tools for vulnerability scanning, such as Mobsf, Yaazhini, 360 microscope, Tencent King Kong system. These tools have been able to cover a large part of the app vulnerability and many have supported dynamic and static vulnerability scanning, but there are a lot of false alert. The purpose of dynamic and static combination is also to improve the accuracy of vulnerability scanning, thereby reducing the rate of false alert, and also can make up for the shortcomings each other, so as to find out the vulnerabilities as much as possible, but the system is too large, the maintenance cost is high, and the scanning result is not ideally, it would be better that there is a simple and efficient tool. SAST is a static android application vulnerability scanning tool. The architecture is simple and easy to use, and the maintenance cost is very low. Although it is a static scanning tool, the accuracy is very high. It is consists of androguard and vulnerability patterns. Because androguard is a powerful open source tool, it is highly customizable and provides excellent support in apk analysis. The vulnerability pattern mainly integrates the known and the latest app vulnerability features. Each pattern is independent of each other, no influence on each other, and strong scalability, so it is fast to update a new pattern and have a good performance. At the same time, it is used to scan various types of top500 applications in Google Play, and found out a lot of potential security issues for many applications, and we submitted some vulnerabilities to the vendors, which are currently being processed.

</details>

<details><summary><strong>Mobexler: An All-in-One Mobile Pentest VM</strong> — Abhinav Mishra</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/tanprathan/MobileApp-Pentest-Cheatsheet](https://github.com/tanprathan/MobileApp-Pentest-Cheatsheet)  
📝 **Description:** Mobexler is a mobile pentest VM that include a wide variety of tools to help in Android and iOS pentesting. It includes tools for both static and dynamic analysis of applications. It allows pentesters to use a single VM to pentest both Android and iOS applications. With the host OS as elementary it also provides an awesome UI experience and allow for intuitive usage of tools just like you would on a host install. External devices can be connected via USB and can be used to install and test application. Why we made Mobexler ? We made Mobexler because there was no such platforms out there which was up to date with the latest pentest tools for both static and dynamic testing which included tools like frida and objection and can be used for both android and ios pentesting. Mobexler was built keeping in mind that any user can just download the VM and begins testing for both platforms without going through the trouble of installation and configuration of all the different tools required. Future work includes: 1. Reduce the VM size. 2. Include reading material in the VM itself. 3. Add a custom repository which can be used to directly install the tools and not download the VM. 4. Build the VM for different Linux flavours.

</details>

<details><summary><strong>Runtime Memory Analysis Tool for Mobile Applications (MemoEB - MEMOry Extraction Binding)</strong> — Igor Lyrchikov, Egor Saltykov</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/Gracker/Android-App-Memory-Analysis](https://github.com/Gracker/Android-App-Memory-Analysis)  
📝 **Description:** We are going to release a tool for automated runtime memory analysis for mobile apps (IOS & Android). All the existing tools are not working with runtime memory analysis processes preferring to dump and analyze memory after app finish it's execution. Our our idea is to gather information during runtime to be able to track changes of the state and application behavior with the final goal being to simplify reverse engineering of obfuscated code and to build call graphs based on catched traces during execution. We also made a single interface to manage this process and automated some most common checks that should be done during penetration test.

</details>

---
## 🔍 OSINT
<details><summary><strong>Maltego - Host.io</strong> — Christian Heinrich</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/cmlh/Maltego-Host.io](https://github.com/cmlh/Maltego-Host.io)  
📝 **Description:** Maltego is a link analysis application of technical infrastructure and social media and enriches disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project. Host.io provides a list of outbound links, backlinks, etc for a given domain name. The integration of Host.io with Maltego displays technical infrastructure in an easy to understand graph format.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>DFEX</strong> — Emilio Couto</summary>

**Track:** Network Attacks · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/ekiojp/dfex](https://github.com/ekiojp/dfex)  
📝 **Description:** DFEX - [DNS File EXfiltration] Data exfiltration is a common technique used for post-exploitation, DNS is one of the most common protocols through firewalls. We take the opportunity to build a unique protocol for transferring files across the network. Existing tools have some limitations and NG Firewalls are getting a bit "smarter", we have been obliged to explore new combinations of tactics to bypass these. Using the good old fashion "HIPS" (Hidden In Plain Sigh) tricks to push files out.

</details>

<details><summary><strong>Invoke-AntiVM: A Powershell Module for VM Evasion</strong> — Paolo Di Prodi, Fred Gutierrez</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/robomotic/invoke-antivm](https://github.com/robomotic/invoke-antivm)  
📝 **Description:** Recently, attackers have been using living off the land tools such as Powershell and the community has developed a large arsenal based on it such as - just to mention a few - PowerSploit, Invoke-Mimikatz, Powerup, Nishang,Powershell Empire, Invoke-Obfuscation and recently Covenant. With so many options available to attackers Windows has introduced advanced Powershell logging capabilities and the AMSI interface. This is not enough however because the attackers have started to use VM detections within their payload to thwart analysis, one needs to remember that powershell script logging only de-obfuscate the functions that have been executed. Therefore we wrote a powershell module with a set of functions that an attacker or a pentester can import in their powershell implant to decide whether the target is a sandbox VM or possibly a real target. In addition to the techniques used in Nishang (Check-VM) which are mostly based on signatures of specific registry keys and process names, we have used a more general – and behavioral – approach which includes all the information from the OS including for example how many programs are installed, what screenshot is used, what network cards are installed, what is the history usage of certain applications such as explorer or word etc. etc. We have also added a fingerprinting module which can be included into a word document for example that once is run collects key metrics from the running OS and reports them into a pastebin account or gmail account, after being compressed and encrypted. Once on pastsebin the attacker can download the exfiltrated profile via a python script and decode for further analysis. We are also building a simple machine learning module that given enough data points is able to infer the decision boundary to determine if a host is a VM or not in addition or in replacement of setting manual thresholds. This is a pretty powerful recon technique for red-team pentesting because in most cases the sandbox will execute the incoming attached documents (if they contain macros for example) thus allowing the exfiltration of the VM data. This can then be used to tweak the payload to avoid the specific sandbox solution and to make sure the malicious payload is run into a real target. We developed this tool to increase awareness of recent techniques for the reverser community. It includes a full readme that explains how can be just in conjunction with Invoke-Obfuscation, Invoke-Cradle and the MaliciousMacroGenerator. We are also periodically running the fingerprinting service to provide profiles for popular online services such as HybridAnalysis, AnyRun, CuckooSandbox as well desktop solutions such as Qemu, VirtualBox, and VMWare.

</details>

<details><summary><strong>P.A.K.U.R.I Penetration Test Achieve Knowledge Unite Rapid Interface</strong> — Makoto Sugita</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/01rabbit/PAKURI](https://github.com/01rabbit/PAKURI)  
📝 **Description:** PAKURI is a semi-automated, user-friendly framework for penetration testing tools. Using only the keypad, you can use the penetration test tool like a game. It's also a great introductory tool for beginners. Learn the flow of penetration testing with PAKURI without having to wrestle with confusing command lines and tools.https://github.com/01rabbit/PAKURI

</details>

<details><summary><strong>PEASS: Privilege Escalation Awesome Scripts SUITE</strong> — Carlos Polop</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng)  
📝 **Description:** PEASS - Privilege Escalation Awesome Scripts SUITE is as the name suggests a collection of privilege escalation scripts. We have a script for Linux, Windows and a Windows .net4 executable. We are launching macOSx version at Black Hat Asia 2020. These tools search for possible local privilege escalation paths that you could exploit and print them with nice colours so you can recognise misconfigurations easily.

</details>

<details><summary><strong>PEsidious: Creating Chaos with Evasive Mutative Malware</strong> — Bedang Sen, Chandni  Vaya</summary>

**Track:** Malware Offense · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/cyberforce/pesidious](https://github.com/cyberforce/pesidious)  
📝 **Description:** Over the past two decades, research has been conducted on using AI to detect malware by extracting features and then classifying them using machine learning algorithms. What's more interesting is how adversaries have begun using AI to attack these AI models. One current use case of such an approach is the use of AI (GAN) to generate Deepfakes. Pesidious draws inspiration from this approach to use AI to mutate the malware samples in order to evade AI-based classifiers. The tool uses the Generative Adversarial Network to first generate benign-looking imports and sections that can make malware look benign and fool machine learning models. We further use deep reinforcement learning to teach a model in which other mutations can reduce the detection rate for malware. The various mutations include changes to imports, exports, headers, signature, sections, and size. Pesidious bagged the first place prize and a whopping $40000 in the HITB CyberWeek AI challenge 2019, and we are back again with some additional features to improve its efficiency and the chaos it brings with it! The tool presented and views expressed are solely our own and do not express the views or opinions of our employer.

</details>

<details><summary><strong>The Grinder Framework - Bringing Light to the Shodan</strong> — Anton Nikolaev, Denis Kolegov</summary>

**Track:** Network Attacks · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/sdnewhop/grinder](https://github.com/sdnewhop/grinder)  
📝 **Description:** The security-related search engines like Shodan, Censys or ZoomEye are daily cybersecurity research tools. They can be used to gather information within threat Intelligence, discover vulnerable hosts, craft fingerprints for vulnerability scanners. At the same time, such search engines have some fundamental limitations and constraints leading to blind spots, false negatives and wrong results. It is very disappointing, especially when new research has been started and the cost of a mistake could be days or even weeks spent in the wrong direction. The Grinder Framework is an open-source security research toolkit adopted to Internet-wide surveys and allows you to use the full power of tools like Nmap, Shodan, Censys, Vulners, TLS-attacker and bringing the light through tailored scanning and threat intelligence approach. The Grinder was born in the SD-WAN New Hope project when we explored SD-WAN security on the Internet. In this talk, we will describe the essence of the Grinder framework and show how you can employ it in your security researches. We will consider the blind spots of the modern search engines, describe non-trivial use cases we worked out during our Internet-scale surveys and illustrate new features by examples from the SD-WAN New Hope, AIsec and DICOMSec projects.

</details>

<details><summary><strong>WMIHacker: A New Way to Use 135 Port Lateral Movement Bypass AV and Transfer File</strong> — Li Jiafeng</summary>

**Track:** Network Attacks · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/rootclay/wmihacker](https://github.com/rootclay/wmihacker)  
📝 **Description:** After the eternal blue virus flood, most intranets no longer open port 445, so the 135-port DCOM service becomes another exploitable point. We need a tool or method that can use 135 ports to execute commands and the Ability to transfer files. WMIHacker is such a tool and can bypass av. Remote command execution tools such as psexec (sysinternals) and wmiexec (impacket) are frequently used during lateral movement. However, these tools will be killed by anti-virus software and the command executed will fail. Psexec will create services and leaves a lot of logs, including a lot of operations such as service creation. The way win32_process.create used by wmiexec.py will no doubt be blocked by AV. I found a new way to execute commands on a machine with an AV and can overwrite window2003 to the latest version of windows. Because I use VBScript to run it. There is no doubt that someone is studying the same content as I did. I found that there are many ways to execute on the internet, including deriving win32_process, registering COM and making it as a malicious provider, msi abuse, etc., but these known ways of using Being intercepted by av.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>USB Controlled Stress Test Tool</strong> — William Yang, Qian Wenhao</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2020  
🔗 **Link:** Not Available  
📝 **Description:** Windows anti-forensics USB monitoring tool for stress test.

</details>

<details><summary><strong>Vulmap: Online Local Vulnerability Scanners Project</strong> — Yavuz Atlas, Hakan Bayir</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/vulmon/Vulmap](https://github.com/vulmon/Vulmap)  
📝 **Description:** Vulmap is an open source online local vulnerability scanner project. It consists of online local vulnerability scanning scripts for Windows and Linux. These scripts can be used for defensive and offensive purposes. It is possible to conduct vulnerability assessments by using these scripts. Also they can be used for privilege escalation by pentesters/red teamers. Vulmap scans vulnerabilities on localhost, shows related exploits and downloads them. It basically, scan localhost to gather installed software information and ask Vulmon API if there are any vulnerabilities and exploits related with installed software. If any vulnerability exists, Vulmap shows CVE ID, risk score, vulnerability's detail link, exploit ids and exploit titles. Exploits can be downloaded with Vulmap also. Main idea of Vulmap is getting real-time vulnerability data from Vulmon instead of relying of a local vulnerability database. Even the most recent vulnerabilities can be detected with this approach. Also its exploit download feature helps privilege escalation process. Since most Linux installations have Python, Vulmap Linux is developed with Python while Vulmap Windows is developed with PowerShell to make it easy to run it on most Windows versions without any installation.

</details>

<details><summary><strong>Vuls: Agent-less Vulnerability Scanner for Linux, FreeBSD, Container Image, Running Container, WordPress, Application Libraries, and Network Devices</strong> — Kota Kanbe</summary>

**Track:** Vulnerability Assessment · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/future-architect/vuls](https://github.com/future-architect/vuls)  
📝 **Description:** Over 10,000 new vulnerabilities are registered on the NVD each year. Constantly monitoring new vulnerabilities and keeping a manual inventory of installed software to determine which devices are affected is necessary. Without automation, vulnerability lifecycle managed imposes huge burdens and challenges. Having personally experienced these challenges, Kota Kanbe created Vuls, an open source vulnerability scanner for Linux and FreeBSD [https://github.com/future-architect/vuls]. With users worldwide, Vuls has over 7,000 GitHub stars and is the highest-ranked security-tool https://github.com/topics/security-tools Vuls lets you know which servers and software are affected by newly disclosed vulnerabilities. Using multiple detection methods and data sources including changelog, Package Manager, NVD and OVAL, Vuls is more accurate than other open source scanners. Additionally, using CPE offers a wide detection range. Vuls not only detects vulnerabilities in OS packages but also in non-OS packages such as libraries for programming languages and network devices. https://vuls.io/docs/en/usage-scan-non-os-packages.html Wordpress vulnerability scanning(core, plugins, themes) is also supported. Scan WordPress ... https://vuls.io/docs/en/usage-scan-wordpress.html Another important feature is the speed; by using parallel processing, numerous servers can be scanned at high speeds with most scans completed within 10 seconds. Vuls supports major distributions of Linux and FreeBSD as well as containers such as Docker, LXC and LXD. Vuls is extremely easy to set up since it connects to other servers via SSH for the scans. Of course, it can also be used to scan servers locally without SSH. Vuls is a Dynamic Scanner which logs in running servers. This means that it's possible to acquire the useful state of the server for system administrators. For instance, Vuls will let you know if there are processes affected by an update and when daemons forgot to perform a restart after the update. With non-intrusive scans, Vuls works well with Continuous Integration and can help find vulnerabilities very quickly by conducting scans every day. How can a system administrator automate vulnerability lifecycle management?

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>MalViz.ai</strong> — Vasu Sethia, Shivam Kataria</summary>

**Track:** Malware Defense · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/Alex-Nguyen/MalViz](https://github.com/Alex-Nguyen/MalViz)  
📝 **Description:** The growth of internet and users increases exponentially and drastically in this decade that provides services inheriting various benefits to users such as online banking,marketing, buying /selling and various facility management services etc. It attracts some people to develop programs that perform various malicious activities intentionally or unintentionally such as stealing sensitive informationfrom computer, displaying advertisement, causing harmful, unwanted activities. The malicious software are referred as malwares. Therefore, this tool helps in detecting, classifying and visualizing the features of malware. Our tool uses the application of Malware Analysis, Machine learning and deep learning algorithms and some general framework applications to automatically classify whether the uploaded file is "Malicious or Legitimate". If it is legitimate the user is free to use but if it is malicious then that uploaded file(malware) is taken for review .It is analyzed and important features of the malware are represented in graph based network.

</details>

<details><summary><strong>Nethive Project</strong> — Chrisando Ryan Pardomuan Siahaan, Vandevlin Alfonso Wibawa, Yohan Muliono, Aditya Kurniawan</summary>

**Track:** Network Defense · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/chrisandoryan/Nethive-Project](https://github.com/chrisandoryan/Nethive-Project)  
📝 **Description:** The Nethive Project provides a Security Information and Event Management (SIEM) infrastructure empowered by CVSS measurements. Nethive Architecture consists of four main components: - Nethive Engine monitors every request coming through HTTP protocol to detect and identify any attempt of SQL Injection attacks. It also anonymously monitors every SQL query response to provide a wide range of XSS protection for your server, with both Stored and Reflected XSS attacks fully covered. - Nethive Auditing watch everything that happens inside your valuable system, with your permission of course. This would detects any strange and suspicious activity inside the system, whether it is a post-exploitation attempt of an attacks, or simply someone you trust is making mistake inside your system. - Nethive Dashboard provides you with resourceful, sleek user inferface that gives you the advantage of knowing everything. From resource consumption to the recent read-write action, it gives you full detail of what's happening, in near real-time. - Nethive CVSS analyze the unfortunately already happening attacks and measure its vulnerability metrics, making sure you are ready to put your reports done in no time.

</details>

<details><summary><strong>OWASP Nettacker</strong> — Sri Harsha Gajavalli, Ali Razmjoo, Sam Stepanyan</summary>

**Track:** Network Defense · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/hofhaeckerei/owasp-nettacker](https://github.com/hofhaeckerei/owasp-nettacker)  
📝 **Description:** Nettacker project was created to automated for information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and information. This software is able to use SYN, ACK, TCP, ICMP and many other protocols to detect and bypass the Firewalls/IDS/IPS and devices. By using a unique solution in Nettacker to find protected services such as SCADA, we could make a point to be one of the bests of scanners.

</details>

<details><summary><strong>OWASP Python Honeypot</strong> — Sri Harsha Gajavalli, Ali Razmjoo</summary>

**Track:** Network Defense · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/OWASP/Python-Honeypot](https://github.com/OWASP/Python-Honeypot)  
📝 **Description:** OWASP Honeypot is an open-source software in Python language which is designed for creating honeypot and honeynet in an easy and secure way! This project is compatible with Python 2.x and 3.x and tested on Windows, Mac OS X, and Linux.

</details>

<details><summary><strong>Sample Analysing Forensics Examiner (SAFE)</strong> — George Chen, Suranga Premakumara</summary>

**Track:** Data Forensics/Incident Response · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/geo-chen/safe](https://github.com/geo-chen/safe)  
📝 **Description:** Security incidents are usually created by alerts or events, which are based on a small set of forwarded logs. When a server is suspected to be compromised, we go back to the host machine to perform forensics on the rest of the logs to investigate the network traffic and endpoint. Sample Analysing Forensics Examiner (SAFE) enables security administrators/engineers to run automated forensics investigations effortlessly on a selected set of machines, either specified or via sampling, to get individual baseline threat scores on the likelihood of a server compromise. A number of logs, including web server, syslog, system, network logs are surveyed for this analysis. With SAFE, security engineers can easily survey a selected pool of servers to hunt for any potential infection or compromise.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Attack Demonstration Tool Kits for Industry 4.0 Using AI and Cloud</strong> — Wataru Matsuda, Mariko Fujimoto, Takuho MItsunaga</summary>

**Track:** Smart Grid/Industrial Security · **Event:** Asia 2020  
🔗 **Link:** Not Available  
📝 **Description:** Industry 4.0 is a new concept of automation data exchange in manufacturing, and technologies and structures are significantly different from the current general ICS. Autonomous judgment and execution are required, and it is based on information exchange using AI and cloud technologies. Devices are supposed to connect interactively that can create new attack surfaces and risks of cyber-attacks. For instance, if AI on the cloud is used for controlling the ICS, attackers could change parameters for controlling ICS by contaminating the judgment of AI. In such a situation, attackers could compromise ICS without accessing the ICS network. Detecting such attacks is quite challenging if operators rely on AI to judge the desirable parameters of ICS. Therefore, it is important to instruct cyber risks of ICS in Industry 4.0. We introduce attack demonstration took kits for Industry 4.0 using actual machines (water supply pump system). This tool kit is portable, and easy to prepare, so is useful for instructing the cyber-risks of ICS whenever and whenever we want. In aspects of Industry 4.0, we especially focus on the security risks of ICS in the following aspects: - When computers and devices are connected interactively - When AI on the cloud is used for controlling the ICS We will show you a demonstration of attacks: the attacker can change the physical status of ICS without accessing the ICS network through an attack against AI.

</details>

<details><summary><strong>Wi-Fi Access Point Rootkits</strong> — Nishant Sharma, Jeswin Mathai</summary>

**Track:** Internet Of Things · **Event:** Asia 2020  
🔗 **Link:** Not Available  
📝 **Description:** Wi-Fi access point (AP) security is one of the most important aspects when it comes to securing networks. The compromise of a Wi-FI AP (which mostly also double-up as a router in SOHO environments) can lead to several secondary attacks. There are multiple vectors that are used to compromise the WiFi AP ranging from default passwords to sophisticated 0-days. But, after compromising the device, avoiding detection and maintaining access are the most important areas which eventually dictate the impact of the compromise. We are going to release a set of code snippets along with the documentation making it easy for people who want to understand the working of Kernel rootkits for IoT devices like Wi-Fi APs. The code will cover hiding a process, renaming a process, blocking kill command on certain processes, network stack based RAT and much more. The code will be released under GPL v2.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>QiLing: Lightweight Advanced Binary Analyzer</strong> — KaiJern Lau, Wu Chen Xu, Kong Zi Qiao</summary>

**Track:** Reverse Engineering · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/qilingframework/qiling](https://github.com/qilingframework/qiling)  
📝 **Description:** Analyzing binaries mostly rely on high level user tools. At the same time, you need to run the binary on the same target architecture & platform. These restrictions limit advanced automatic analysis, require special hardware resources (such as for IoT analysis), and also expose against malicious binaries. QIling is a sandbox framework that focuses on providing high level Python API to enable users to build highly customizable analysis tool on top. Using emulator technology inside, our engine can run any machine code on any target platforms. This allows analyzing Windows malware on Linux Arm64, or running IoT firmware based on Mips on MacOS, and so on. This research introduces a comprehensive overview on the Qiling. We will present all the technical issues we had to deal with, including emualating operating system layers such as syscalls, loader and linker, how qiling supports all executable file formats (PE, MachO, ELF, UEFI and MBR), and finally how we provide a framework for users to easily build their analysis tools on top of this foundation. To conclude the presentation, we will show some cool live demos, such as:Run IDA on top of Qiling of with Qiling's IDA scriptable pluginEmulate, debug and instrument MBR from Qiling Framework

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>Phishing Simulation Assessment</strong> — Jyoti Raval</summary>

**Track:** Human Factors · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/jenyraval/Phishing-Simulation](https://github.com/jenyraval/Phishing-Simulation)  
📝 **Description:** People in IT eco-system are becoming 'favorite' targets because, 1. they remain weakest link and 2. organisation are becoming mature in securing technology. For a security tester, it is a daunting task to set up a phishing campaign, which includes, decide a look-alike domain, buy it, setup a phishing website with infrastructure, design an email and choose target audience, track the open/click/download and build the analytics. All of these activities are time-consuming and demands a certain skill-set. Phishing Simulation provides one-stop-solution for organisation to understand security awareness posture without actually performing 'live' phishing attack. Phishing Simulation prepares phishing assessment with tailor-made questions specific to organisation, facilitates target users to complete the assessment, provides an intuitive tutorial and builds the analytics on basis of responses and the meta-data collected about user. Phishing Simulation has 2 modules: Admin Module: This module will be used by tester to setup and monitor phishing assessments - On the basis of inputs provided by tester like organisation name, email ID, domain name, tool automatically generates questions with tailor-made data such as look-alike domains using typo-squatting technique, spoofed sender address, look-alike web-site content - Assessment will comprise of questions having phishing web-site, spear-phishing email, SMiShing, scenario-based question to make it close to real-world phishing attacks - Tool also provides analytics in form of graphs to represent security awareness posture of organisation by different categories such as department, employee, target-user action Client Module: This module will be used by target user to complete the assessment and view tutorial - Every user within a campaign itself will have 10 unique questions to answer, with the mix of positive and negative scenarios - Passing criteria is to answer every question correct because all it takes is just one click!

</details>

<details><summary><strong>Sharkcop: A Phishing Detector Using Machine Learning</strong> — Anh Ngoc, Tung Cao, Aiden Pearce</summary>

**Track:** Human Factors · **Event:** Asia 2020  
🔗 **Link:** [https://github.com/caohoangtung/sharkcop](https://github.com/caohoangtung/sharkcop)  
📝 **Description:** Sharkcop use criterias such as ssl certifucate, domain length, domain age,... with SVM classification algorithm to determine if a url is phishing or not. Sharkcop includes a restful web server and a chrome extension to highlight malicious links on Facebook and Messenger.

</details>

---
