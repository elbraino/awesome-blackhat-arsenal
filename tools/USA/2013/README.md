# USA 2013
---
📍 48 tools demonstrated at **Black Hat Arsenal USA 2013**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [Others](#others) (6)
- [🌐 Web/AppSec](#-webappsec) (9)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (2)
- [📱 Mobile Security](#-mobile-security) (4)
- [🔍 OSINT](#-osint) (3)
- [🔴 Red Teaming](#-red-teaming) (11)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (1)
- [🔵 Blue Team & Detection](#-blue-team--detection) (7)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (2)
- [🧠 Reverse Engineering](#-reverse-engineering) (1)
- [🧠 Social Engineering / General](#-social-engineering--general) (2)
---
## Others
<details><summary><strong>Dependency-Check</strong> — Jeremy Long</summary>

**Track:** — · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** Does your application have dependencies on 3rd party libraries? Do you know if those same libraries have published CVEs? Dependency-Check, an OWASP project, can help by providing identification and monitoring of application dependencies. The core engine can scan the libraries and will create an inventory of all the dependent libraries and whether or not there are any published CVEs. Dependency-Check's new build plugins will be demonstrated as well as how the tool can be used to perform continuous monitoring of your applications and their dependencies.

</details>

<details><summary><strong>ice-hole</strong> — Darren Manners</summary>

**Track:** — · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** Ice-Hole 1.4 is a new update for the tool which brings BYOD targeting via user agents, scheduling of phishing emails from a bank of templates, executable injection via javascript, and can clone websites based upon a URL to include keystroke logging. Ice-Hole is a phishing awareness email program. It is designed to help security analysts/System Administrators keep track and test end users. The tool can be used in conjunction with various third party software like SET for further leverage.

</details>

<details><summary><strong>iMAS - iOS Mobile Application Security libraries</strong> — Gregg Ganley</summary>

**Track:** — · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** iOS application security can be *much* stronger and easy for developers to find, understand and use. iMAS (iOS Mobile Application Security) - is a secure, open source iOS application framework research project focused on reducing iOS application vulnerabilities and information loss. Today, iOS meets the enterprise security needs of customers, however many security experts cite critical vulnerabilities and have demonstrated exploits, which in turn pushes enterprises to augment iOS deployments with commercial or custom solutions. The iMAS intent is to protect iOS applications and data beyond the Apple provided security model and reduce the adversary’s ability and efficiency to perform recon, exploitation, control and execution on iOS mobile applications. iMAS has released five security controls (researching many more) for developers to download and use within iOS applications. This talk will walk through various iOS application vulnerabilities, iMAS security controls, OWASP Mobile top10 and CWE vulnerabilities addressed.

</details>

<details><summary><strong>ModSecurity</strong> — Ryan Barnett</summary>

**Track:** — · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** ModSecurity is a cross-platform (Apache, IIS and Nginx), open source web application firewall module maintained by Trustwave SpiderLabs Research Team. It's popularity is mainly due to its powerful rules language which provides security personnel a means to quickly develop defenses for emerging attack scenarios or virtual patching for identified web application vulnerabilities. Along with its Lua API and data modification capabilities, it provides unparalleled flexibility for custom integrations and security logic. This Arsenal Demo includes many live setups where Black Hat attendees will be able to play with the ModSecurity defenses and try and evade its detections.

</details>

<details><summary><strong>SimpleRisk</strong> — Josh Sokol</summary>

**Track:** — · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact of that event. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/yr company, I ran into these same barriers and where budget wouldn't let me go down the GRC route, I finally decided to do something about it. At BlackHat 2013, I would like to formally debut SimpleRisk, a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time and can be downloaded at http://www.simplerisk.org. SimpleRisk is truly Enterprise Risk Management simplified.

</details>

<details><summary><strong>ThreadFix</strong> — Dan Cornell</summary>

**Track:** — · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** ThreadFix is a software vulnerability aggregation and management system that reduces the time it takes to fix software vulnerabilities. It imports the results from dynamic, static, and manual testing to provide a centralized view of software security defects across development teams and applications. The system allows companies to correlate testing results and streamline software remediation efforts by simplifying feeds to software issue trackers. By auto-generating application firewall rules, this tool allows organizations to continue remediation work uninterrupted. ThreadFix empowers managers with vulnerability trending reports that show progress over time, giving them justification for their efforts.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>HTExploit</strong> — Matias Katz</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/Seabreg/htexploit](https://github.com/Seabreg/htexploit)  
📝 **Description:** HTExploit is an open-source tool written in Python that exploits a weakness in the way that htaccess files can be configured to protect a web directory with an authentication process. By using this tool anyone would be able to list the contents of a directory protected this way, bypassing the authentication process.

</details>

<details><summary><strong>Lair</strong> — Tom Steele</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/lair-framework/lair](https://github.com/lair-framework/lair)  
📝 **Description:** Lair is an open-source project developed for and by pentesters. Built on Meteor and Node.js with a dash of Python, Lair is a web application that normalizes, centralizes, and manages diverse test data from a number of common tools including Nmap, Nessus, Nexpose, and Burp. Unlike existing alternatives, Lair encourages team-based collaboration by automatically pushing updates to team members in real time. Paired with itâs workflow and documentation management, Lair offers a single solution for performing a detailed, thorough penetration test individually or as a team in a manner that has not been done before.

</details>

<details><summary><strong>OWASP Broken Web Applications VM</strong> — Chuck Willis</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/chuckfw/owaspbwa](https://github.com/chuckfw/owaspbwa)  
📝 **Description:** The Open Web Application Security Project (OWASP) Broken Web Applications project (www.owaspbwa.org) provides a free and open source virtual machine loaded with web applications containing security vulnerabilities. This session will showcase the project VM and exhibit how it can be used for training, testing, and experimentation by people in a variety of roles. Demonstrations will cover how the project can be used by penetration testers who discover and exploit web application vulnerabilities, by developers and others who prevent and defend against web application attacks, and by individuals who respond to web application incidents. New features and applications in the recently released version 1.1 of the VM will also be highlighted.

</details>

<details><summary><strong>OWASP Xenotix XSS Exploit Framework</strong> — Ajin Abraham</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/ajinabraham/OWASP-Xenotix-XSS-Exploit-Framework](https://github.com/ajinabraham/OWASP-Xenotix-XSS-Exploit-Framework)  
📝 **Description:** Xenotix XSS Exploit Framework is a penetration testing tool to detect and exploit XSS vulnerabilities in Web Applications. It is basically a payload list based XSS Scanner and XSS Exploitation kit and has has the world's second largest XSS Payload list. It provides a penetration tester the ability to test all the XSS payloads available in the payload list against a web application to test for XSS vulnerabilities. The tool supports both manual mode and automated time sharing based test modes. The exploitation framework in the tool includes a XSS encoder, a victim side XSS keystroke logger, an Executable Drive-by downloader and a XSS Reverse Shell. These exploitation tools will help the penetration tester to create proof of concept attacks on vulnerable web applications during the creation of a penetration test report.

</details>

<details><summary><strong>RAFT 3</strong> — Gregory Fleischer, Nathan Hamiel</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/Averroes/raft](https://github.com/Averroes/raft)  
📝 **Description:** RAFT (Response Analysis and Further Testing) is an open source Python tool designed to assist with web application assessments. RAFT is based on the embedded WebKit browser features available in PyQT. In today’s modern web applications, page generation is highly dynamic with heavy reliance on JavaScript and asynchronous requests. RAFT uses the built-in web browser support to provide analysis capabilities for stored response information. RAFT can interact directly with the rendered content using the browser DOM and injected JavaScript callbacks. This provides interesting capabilities such as fuzzing for DOM based XSS injections in previously captured responses or simulating Clickjacking attacks. RAFT is not an inspection proxy, but is rather a tool to complement your testing toolkit. In addition to defining a custom capture XML format, RAFT also supports directly importing from Burp capture and vulnerability files as well as Paros and WebScarab proxy logs. The integrated web browser can be used to perform additional data capture, content examination, spidering, and vulnerability identification and testing. This Beta release updates the tool to Python 3.3 and latest widely available version of QT. Also featured is an improved command line interface, updated import functionality, and enhanced scan and testing functionality. RAFT is released under a GPLv3 license.

</details>

<details><summary><strong>SPARTY</strong> — Aditya K Sood</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/0xdevalias/sparty](https://github.com/0xdevalias/sparty)  
📝 **Description:** Sparty is an open source tool written in python to audit web applications using sharepoint and frontpage architecture. The motivation behind this tool is to provide an easy and robust way to scrutinize the security configurations of sharepoint and frontpage based web applications. Due to the complex nature of these web administration software, it is required to have a simple and efficient tool that gathers information, check access permissions, dump critical information from default files and perform automated exploitation if security risks are identified. A number of automated scanners fall short of this and Sparty is a solution to that . In the first release, Sparty is capable of performing following tasks: Sparty is tool that provides complete information regarding sharepoint and frontpage environments to design threat models which greatly assist penetration testers in manual verification of flaws. Sparty is really helpful in time critical security assessments.

</details>

<details><summary><strong>Vega</strong> — David Mirza Ahmad</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/vega/vega](https://github.com/vega/vega)  
📝 **Description:** We will be exhibiting Vega 1.0. Vega is a GUI-based, multi-platform, free and open source web security scanner that can be used to find instances of SQL injection, cross-site scripting (XSS), and other vulnerabilities in your web applications. Vega also includes an intercepting/scanning proxy for interactive web application debugging and fuzzing. One of the most interesting features about Vega is that the modules (fuzzing, signature detection) are written in Javascript, users can easily modify them or write their own. The Vega web vulnerability scanner runs on Linux, Windows, and OS X. Vega is released under the EPL 1.0 and can be downloaded from the Subgraph website, http://www.subgraph.com.

</details>

<details><summary><strong>WATOBO</strong> — Andreas Schmidt</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** [https://github.com/siberas/watobo](https://github.com/siberas/watobo)  
📝 **Description:** WATOBO is a security tool for web applications. It is intended to enable security professionals to perform efficient (semi-automated) web application security audits. Most important features:

</details>

<details><summary><strong>WebVerify</strong> — Luis Antonio Rosales Marco</summary>

**Track:** Web AppSec · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** WebVerify is a tool that aims to help in the recognition, vulnerability scanning and search patterns based on its own database. Unlike other tools, WebVerify first recognizes whether the target is a CMS to run other exploits... among its other advantages, WebVerify also provides command scripts to perform common WAF bypass techniques.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>JMSDigger</strong> — Gursev Singh Kalra</summary>

**Track:** Code Assessment · **Event:** USA 2013  
🔗 **Link:** [https://github.com/OpenSecurityResearch/jmsdigger](https://github.com/OpenSecurityResearch/jmsdigger)  
📝 **Description:** JMSDigger is a new tool that can be leveraged to engage and assess enterprise messaging applications with the current release focuses on ActiveMQ. JMSDigger has following features:

</details>

<details><summary><strong>PyPTP</strong> — Matthew Bergin</summary>

**Track:** Code Assessment · **Event:** USA 2013  
🔗 **Link:** [https://github.com/capaulson/pyptp](https://github.com/capaulson/pyptp)  
📝 **Description:** PyPTP is a Python based Pointer-to-Pointer fuzzer which allows for dynamic mapping of Python modules making calls through ctypes into C/C++ DLLs PyPTP boasts a 90-96% code mapping feature that allows for you to easily crawl through python code and extrapolate function calls and the datatypes required to execute those functions.

</details>

---
## 📱 Mobile Security
<details><summary><strong>Automated Electromechanical PIN Cracking: R2B2 and C3BO</strong> — Justin Engler</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/iSECPartners/R2B2](https://github.com/iSECPartners/R2B2)  
📝 **Description:** Password and PIN systems are often encountered on mobile devices. A software approach to cracking these systems is often the simplest, but in some cases a pen tester or forensic investigator may have no better option than to start pushing buttons. Robotic Reconfigurable Button Basher (R2B2) is a robot designed to manually brute force PINs or other passwords via manual entry. R2B2 can operate on touch screens or physical buttons. R2B2 can also handle more esoteric lockscreen types such as pattern tracing. R2B2 can crack a stock Android 4 digit PIN exhaustively in 20 hours. Times for other devices vary depending on lockout policies and related defenses. Capacitive Cartesian Coordinate Bruteforceing Overlay (C3BO) is a combination of electronics designed to electrically simulate touches on a capacitive touch screen device. C3BO has no moving parts and can work faster than R2B2 in some circumstances. Both tools are built with open source software. Parts lists, detailed build instructions, and STL files for 3d printed parts will be available for download. R2B2 and C3BO will be running against live devices at the kiosk!

</details>

<details><summary><strong>Drozer (formerly known as Mercury)</strong> — Tyrone Erasmus, Daniel Bradberry</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/ReversecLabs/drozer](https://github.com/ReversecLabs/drozer)  
📝 **Description:** Drozer, previously known as Mercury, is the de facto tool for vulnerability-hunting on Android phones and in marketplace apps. In these demonstrations we are launching the new version of Drozer: one that has been extended to be a full-on, open-source exploitation framework for Android. Sporting remote exploits for compromising Android devices and shipped with payloads that transcend your average reverse shell, this framework is first of its breed for Android. Drozer also provides standard shellcode that can be used by exploit developers to integrate their Android exploits into the Drozer framework. Various devices will be pwned in these demonstrations, showing how Drozer can be used for initial targeted entry of a device to deploy a Drozer agent. Then, the post exploitation fun can begin: dumping of personal information, taking screenshots, stealing pictures, recording from the microphone and root are all possible. The best part about all of this work is that it is an open-source project that cherishes submissions from the community.

</details>

<details><summary><strong>Smartphone Pentest Framework</strong> — Georgia Weidman</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/georgiaw/Smartphone-Pentest-Framework](https://github.com/georgiaw/Smartphone-Pentest-Framework)  
📝 **Description:** As smartphones enter the workplace, sharing the network and accessing sensitive data, it is crucial to be able to assess the security posture of these devices in much the same way we perform penetration tests on workstations and servers. However, smartphones have unique attack vectors that are not currently covered by available industry tools. The smartphone penetration testing framework, the result of a DARPA Cyber Fast Track project, aims to provide an open source toolkit that addresses the many facets of assessing the security posture of these devices. We will look at the functionality of the framework including information gathering, exploitation, social engineering, and post exploitation through both a traditional IP network and through the mobile modem, showing how this framework can be leveraged by security teams and penetration testers to gain an understanding of the security posture of the smartphones in an organization. SPF can be used as a pivot to gain access to an internal network, gaining access to additional vulnerabilities. SPF can be used to bypass filtering, using SMS to control an exploited internal system. Demonstrations of SPF functionality will be shown.

</details>

<details><summary><strong>ThunderCell</strong> — Georgia Weidman</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** ThunderCell is a new all encompassing mobile security distribution providing the most comprehensive toolset for mobile vulnerability research, exploitation, forensics, and application auditing. The included tools span multiple mobile platforms including Android, iPhone, Windows Phone, BlackBerry, and Software Defined Radio, among others. Created and maintained by mobile researchers, ThunderCell is developed with mobile security practitioners in mind, with everything you need for your next engagement, class, or research project.

</details>

---
## 🔍 OSINT
<details><summary><strong>Information Disclosure in Facebook Graph Api with A.T.H.O.S</strong> — Michael Hudson</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** The Graph API is the primary way that data is retrieved or posted to Facebook. The Getting Started Guide contains an overview of the basics of the API, walks you through using the Graph API Explorer, shows you how names work, how permissions work, what connections are and puts it all together so the rest of this reference make sense. Disclosure Anyone can access the data from ANY user due to the release of information that produces the "Graph API" because of the functionality they have given to this API for developers. The "excess" functionality provided in this API make data users are exposed without any need for it any malicious attacker and make a compilation of information from the target It is possible to identify people according to their id as will be seen in the proof of concept and insecure http protocol also makes it vulnerable to a brute force attack

</details>

<details><summary><strong>iocwriter_11</strong> — William Gibb</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** USA 2013  
🔗 **Link:** [https://github.com/mandiant/ioc_writer](https://github.com/mandiant/ioc_writer)  
📝 **Description:** With the impending release of the OpenIOC 1.1 format for sharing threat intelligence, Mandiant will be releasing a set of open source tools for creating and manipulating OpenIOC objects and moving data in and out of the OpenIOC format. Demonstrations will cover how the tools can be used to create and modify OpenIOC documents, show how it is possible to store Snort and Yara signatures in OpenIOC format and convert those OpenIOC documents back into their native formats. In addition, the integration of these tools into other open source applications will be demonstrated with tools that can automatically extract IOCs from unstructured content.

</details>

<details><summary><strong>Sphere of Influence 3.2</strong> — Darren Manners</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** The purpose of sphere of influence was to address the shortcomings of visualizations with regards to a tactical awareness. The IP address-to-geographical location and organization was designed to aid in the removal of false positives. It also provides details about location, latitude/longitude and organizational information. It addressed the fact that the majority of attacks were coming from the United States and China or from countries with high levels of broadband access. The geographical data was also used to visually show traffic from countries that would not normally be connecting to a particular address space. Although not popular with the internet philosophy that everyone should be able to connect to everyone, it makes sense to limit your exposure to your own sphere of influence. When looking at organizations we can start to examine false positives in a different way. Hackers, viruses and Trojans tend to attack weaker systems. Historically Universities, colleges and home users tend to be the playground of such endeavors. We can use this knowledge against them by examining traffic from these entities for any useful information.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Armitage - A Scriptable Red Team Collaboration Tool</strong> — Raphael Mudge</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/xxgrunge/armitage](https://github.com/xxgrunge/armitage)  
📝 **Description:** Armitage is a scriptable red team collaboration tool built on top of the Metasploit Framework. Through its programming language, Cortana, it's possible to integrate outside tools into Armitage's workflow and make them available in a team friendly way. This demonstration will introduce Armitage's collaboration features and highlight Cortana's improved abilities to integrate tools into Armitage's collaboration architecture.

</details>

<details><summary><strong>g0tbeEF</strong> — Taylor Pennington</summary>

**Track:** Network Attacks · **Event:** USA 2013  
🔗 **Link:** [https://github.com/d4rkcat/g0tbeef](https://github.com/d4rkcat/g0tbeef)  
📝 **Description:** Multi-threaded Python based ARP Poisoning with an Asynchronous Queue using IPTables and QUEUE deigned to capture HTTP traffic and inject a BeEF hook.

</details>

<details><summary><strong>HookME</strong> — Manuel Fernandez</summary>

**Track:** Network Attacks · **Event:** USA 2013  
🔗 **Link:** [https://github.com/NytroRST/HookMe](https://github.com/NytroRST/HookMe)  
📝 **Description:** HookME is a software designed for intercepting communications by hooking the desired process and hooking the API calls for sending and receiving network data. HookMe provides a nice graphic user interface allowing you to change the packet content in real time, dropping or forwarding the packet. It also has a python system plugin to extend the HookMe functionality. It can be used for a lot of purposes such as:

</details>

<details><summary><strong>Invoke-ReflectivePEInjection</strong> — Joe Bialek</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/clymb3r/PowerShell](https://github.com/clymb3r/PowerShell)  
📝 **Description:** PowerShell is a powerful scripting language which has the capability to run scripts on remote systems without writing to disk. Invoke-ReflectivePEInjection is a PowerShell script which can reflectively load and execute a windows PE file such as an EXE or DLL inside the PowerShell process on a remote computer without writing to disk. This is accomplished by (partially) rewriting the Win32 functionality which loads EXEs/DLLs in PowerShell. The script allows a penetration tester to: A beta version of the script is currently available for download on Github at: https://github.com/clymb3r/PowerShell. The final version will be a part of PowerSploit (and hopefully synced in to Kali linux).

</details>

<details><summary><strong>Kfuzz</strong> — Matthew Bergin</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** Kfuzz was my take on kernel level device driver fuzzing with Python. I used Python's ctypes module to interact with the OS kernel and from there manage memory and make subsequent calls to the driver loaded into the kernel.

</details>

<details><summary><strong>ShellNoob</strong> — Yanick Fratantonio</summary>

**Track:** Malware Offense · **Event:** USA 2013  
🔗 **Link:** [https://github.com/reyammer/shellnoob](https://github.com/reyammer/shellnoob)  
📝 **Description:** Writing shellcode is usually really fun, but some parts are boring, error-prone, and insanely difficult to debug without the proper arsenal. ShellNoob is a tool that eases the writing and debugging of shellcode by taking care of all the parts that even a noob could do, and leaving only the fun part for the artist. ShellNoob can convert shellcode from and to many different formats: asm (both Intel and ATT syntax), bin, hex, object, executable, C, Python, bash, Ruby and pretty. It can also automatically resolve the numeric value of all the constants (e.g., O_RDWR) and, similarly, of all the syscalls: as this is performed by generating and executing code on-the-fly, it's easy to extend this feature to a variety of different architectures. A debug switch is implemented as well, that conveniently put a breakpoint at the beginning of the shellcode: with that, it's immediate to assemble the shellcode and have gdb ready to single-step into it. Finally, ShellNoob comes with an interactive opcode-to-binary (and binary-to-opcode) conversion mode, where one can quickly check to which bytes a given instruction is assembled to: this is really valuable when specific bytes cannot be used to successfully exploit a vulnerable program. As it would be pointless to have a handy tool that requires hours to be properly setup, ShellNoob has been designed to be the most portable and flexible tool ever: it only relies on as/gcc/objdump and python! It has already been successfully tested on x86/x86_64/ARM, Linux/FreeBSD, and even on a Raspberry Pi! The tool is also uber-easy to be deployed: ShellNoob is just one self-contained python script. You push the file on the target machine, and you are done. A nice set of "starting" points is included as well. Other than having a set of simple shellcode, ShellNoob comes with some handy scripts that automatically extract the register set and a comprehensive list of valid assembly instructions for a given architecture: in this way, the writer will not lose time to guess what's the correct syntax for a specific assembly instruction. Moreover, even if ShellNoob comes with some already generated list, the heuristics used are general and they can be easily ported to work with other less-known platforms.

</details>

<details><summary><strong>ShinoBOT/ShinoC2</strong> — Shota Shinogi</summary>

**Track:** Malware Offense · **Event:** USA 2013  
🔗 **Link:** [https://github.com/Sh1n0g1/ShinoBOT](https://github.com/Sh1n0g1/ShinoBOT)  
📝 **Description:** A RAT (remote administration tool) and C2 (command/control) server for measuring a target company may or may not provide enough insight, especially when simulating a highly focused attack. After launching the RAT, control will be established by C2 server. The attacker can then do everything from the C2 server.

</details>

<details><summary><strong>Social-Engineer Toolkit</strong> — David Kennedy</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/trustedsec/social-engineer-toolkit](https://github.com/trustedsec/social-engineer-toolkit)  
📝 **Description:** Let's take a deep dive into the newest and brand spanking new of the Social-Engineer Toolkit (SET). This talk will demonstrate the effectiveness of targeted attacks and how easy it is to circumvent today's technology effortlessly. Learn from the creator of SET and the most effective way to perform targeted attacks.

</details>

<details><summary><strong>The cat's meow</strong> — Taylor Pennington</summary>

**Track:** Malware Offense · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** The Cat's Meow is a tool used during our penetration testing which analyzes the most common password scheme seen during our decoding and decryption stage of post exploitation. The tool reads in a password list of already obtained cleartext passwords and produces the most commonly seen Hashcat Masks which can then in turn be used to more quickly reverse other passwords.

</details>

<details><summary><strong>Viproy VOIP Penetration and Exploitation Testing Kit</strong> — Fatih Ozavci</summary>

**Track:** Network Attacks · **Event:** USA 2013  
🔗 **Link:** [https://github.com/fozavci/viproy-voipkit](https://github.com/fozavci/viproy-voipkit)  
📝 **Description:** Viproy VOIP Pen-Test Kit is developed to improve quality of SIP Penetration Tests. It provides authentication feature that helps to create simple tests. It includes 7 different modules with authentication support: options tester, brute forcer, enumerator, invite tester, trust analyzer, proxy and registration tester. All attacks could perform before and after authentication to fuzz SIP services and value added services.

</details>

<details><summary><strong>Xenotix xBOT</strong> — Ajin Abraham</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2013  
🔗 **Link:** [https://github.com/ajinabraham/Xenotix-xBOT](https://github.com/ajinabraham/Xenotix-xBOT)  
📝 **Description:** Xenotix xBOT is a powerful cross platform (Linux,Windows,Mac) bot written in Python that uses certain Google Services as Command & Control Center for the botnet. The bot works flawlessly with a single requirement of a decent internet connection. The xBOT's communication is encrypted as it uses Google's own SSL connection and is nowhere affected by any firewalls or your ISP's tricky network configurations.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>VScan</strong> — Federico Massa</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** Usually, after we performed a Vulnerability Assessment in our organisation, we continue our work with the development of an plan of security improvements with the ultimate goal of reducing the risk and threats and be in conformity with security politics and requirements. This security improvements plan can be difficult to carry out in time, if we cannot in a simple way measure our progress and simplify the process of resolution of vulnerabilities. To address these issues we developed VScan, an open source Vulnerability Management System.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Dalvik Inspector</strong> — Joe Sylve</summary>

**Track:** Data Forensics/Incident Response · **Event:** USA 2013  
🔗 **Link:** [https://github.com/pxb1988/dalvik](https://github.com/pxb1988/dalvik)  
📝 **Description:** Dalvik is the process Virtual Machine used by Android that powers all non-native applications used on Android devices. Through Dalvik memory analysis, a wealth of insight can be gained into the workings of a running application, including all instantiated objects (classes) and the variables, methods, and other per-instance class information. Analysis of structures at this level will allow investigators to see internal application-level state in its “native” form. This is an important evolution in state of cutting edge memory forensics, which allows the investigator to move above the kernel level and see higher-level structures in readable form and with broad context. Our new tool, Dalvik Inspector, provides an easy-to-use graphical interface which allows parsing Dalvik-level constructs from memory captures of Android devices, and facilitates deep, standalone analysis of Android application-internal structures. Dalvik Inspector will be immediately useful for malware analysis, incident response, and traditional forensics investigations.

</details>

<details><summary><strong>De-Cloak</strong> — Darren Manners</summary>

**Track:** Network Defense · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** De-Cloak is designed to extract HTTP user agents from PCAP files and store known user agents in a database. Hackers often hide wget or http requests by using known user agents. However, if we change our own user agents (perhaps via a GPO) we can start to investigate what starts to stand out. Simple but effective.

</details>

<details><summary><strong>Mandiant Redline</strong> — Theodore Wilson</summary>

**Track:** Data Forensics/Incident Response · **Event:** USA 2013  
🔗 **Link:** [https://github.com/mandiant](https://github.com/mandiant)  
📝 **Description:** Redline, Mandiantâs premier free tool, provides host investigative capabilities to users to find signs of malicious activity through memory and file analysis, and the development of a threat assessment profile. With Redline, users can:

</details>

<details><summary><strong>OSfooler: Remote OS Fingerprinting is over</strong> — Jaime Sanchez</summary>

**Track:** Network Defense · **Event:** USA 2013  
🔗 **Link:** [https://github.com/segofensiva/OSfooler-ng](https://github.com/segofensiva/OSfooler-ng)  
📝 **Description:** Using commercial tools to secure your network is recommended, but it is necessary to be one step further to keep the system secure. With this technique you can give that step in order defend your servers against the first phase of all attacks Fingerprinting. This is done by intercepting all traffic that your box is sending in order to camouflage and modify in real time the flags in TCP/IP packets that discover your system. This tool is a practical approach for detecting and defeating: Some features are: Sorry guys, remote OS fingerprinting is over...

</details>

<details><summary><strong>Registry Inspector Forensics (RIF)</strong> — Lodovico Marziale</summary>

**Track:** Data Forensics/Incident Response · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** Registry Inspector Forensics (RIF), based on the widely used Registry Decoder, is a powerful registry forensics platform. It features the ability to acquire and analyze numerous registry hives simultaneously, intelligent search, a plugin-based architecture, both GUI and full command line support and the ability to parse and analyze memory-resident hive files including the volatile hives. This functionality is perfectly suited for forensic investigations, malware analysis, and incident response scenarios. The project is free and open source and under active development.

</details>

<details><summary><strong>TinyLane</strong> — Rob Bathurst</summary>

**Track:** Cryptography · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** The TinyLANEâ¢ is a small mobile encryption device developed by Peak Security, Inc. to allow individuals and businesses to create instant AES256 point-to-point tunnels between two or more TinyLANEs utilizing individual keys for each connection. The TinyLANEâ¢ is capable of functioning on most hardware platforms including ARM, x86, and 64-bit based processors in addition to throughput at near line speed on most connects up to 10 Gigabit.

</details>

<details><summary><strong>Triana</strong> — Juan Garrido</summary>

**Track:** Malware Defense · **Event:** USA 2013  
🔗 **Link:** [https://github.com/CSCSI/Triana](https://github.com/CSCSI/Triana)  
📝 **Description:** I am going to be presenting a new tool for analysing malware or possible threats in certain scenarios where the malware is not accessible or, because legal requirements, it's not possible to provide access to the files to the researchers. This is also a good starting point for newcomers and well-established forensic and malware researchers who want to quickly analise possible threats. In my talk we'll start with current status of malware analysis. Companies that cannot afford having a security team dealing with incoming threats and still want to be responsive against targeted attacks. How they can do it? How we can provide them with a solution to prevent infections? Altought this is a good start, people will find sometimes themselves without access to all the information... even without access to the file! How we can do the previously presented analysis if we cannot access the faulting file? We'll present different solutions to obtain enough information about the malware using only public available information. Finally we'll present Triana, a tool for collecting and analysing all this information and integrate it into a report (DOCX and JSON) that will consolidate the results and provide a score about the malware thread. An example of report can be found here: https://docs.google.com/file/d/0B4ONZdxLeGFKa2o4eng2WFlsYXM/edit?pli=1

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Dude, WTF in my car?</strong> — Alberto Garcia Illera, Javier Vazquez Vidal</summary>

**Track:** Hardware/Embedded · **Event:** USA 2013  
🔗 **Link:** [https://github.com/fjvva/ecu-tool](https://github.com/fjvva/ecu-tool)  
📝 **Description:** The car ECU tuning market is weird. There is little help from people already in it, and most of the equipment is expensive. Well, not anymore! We will show a tool that was built under $25, and that is able to bypass all the security in the car ECU, based of a BOSCH EDC15 and EDC16, which has RSA 256 and seed/key algorithm protection. We will show live demonstrations of how the tool works, with logic analyzer and explanation of all the processes that take place. Black Hat Arsenal gives a unique opportunity to have a close look at tools, so we will explain the most practical side of our tool instead of going deep into the low level explanation, to exploit the most of BH-Arsenal concept. All of this will help the end user to realize that even cars, have secrets that can be "unlocked."

</details>

<details><summary><strong>HackRF</strong> — Michael Ossmann, Jared Boone</summary>

**Track:** Hardware/Embedded · **Event:** USA 2013  
🔗 **Link:** [https://github.com/greatscottgadgets/hackrf](https://github.com/greatscottgadgets/hackrf)  
📝 **Description:** The HackRF project is developing an open source hardware design for a low cost Software Defined Radio (SDR) transceiver platform. SDR technology allows a single piece of equipment to implement virtually any wireless technology (Bluetooth, GSM, ZigBee, etc.), and we hope the availability of a low cost SDR platform will revolutionize wireless communication security research and development throughout the information security community. Having distributed hundreds of beta units (HackRF Jawbreaker) and soliciting feedback, Black Hat Arsenal Tools USA 2013 is the first chance to see the next generation hardware design in person.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Binfuzz.js</strong> — Artem Dinaburg</summary>

**Track:** Reverse Engineering · **Event:** USA 2013  
🔗 **Link:** [https://github.com/artemdinaburg/binfuzz](https://github.com/artemdinaburg/binfuzz)  
📝 **Description:** Binfuzz.js is a library for fuzzing structured binary data in JavaScript. Structured binary data is data that can be easily represented by one or more C structures: it is composed of fixed size fields and any variable length fields are counted by another structure member. Numerous network and file formats are structured binary data, including SSL, DNS, and most image formats. Things that aren't structured binary data include languages (such as HTML or JavaScript) or text-based protocols (such as HTTP) or text-based file formats (such as PDF). A live example will be shown using Binfuzz.js to generate Windows ICO files to stress a browser's icon parsing and display code. ICO is a complex format that contains images of different sizes for optimal display based on context. Binfuzz.js will try generating edge cases such as an icon with 0xFFFF images of size 0xFFFFFFFF by 0xFFFFFFF, and cases such as saying that there are 128 images but only supplying data for one, among many other permutations. It is the author's hope that others will extend binfuzz.js for other use cases.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>FSFlow</strong> — Pat McCoy</summary>

**Track:** Human Factors · **Event:** USA 2013  
🔗 **Link:** [https://github.com/opensecurityresearch/fsflow](https://github.com/opensecurityresearch/fsflow)  
📝 **Description:** FSFlow is a social engineering telemarketer-style call flow application. A call flow guides the social engineer during the call to their target, providing step by step talking points, quick logging of target responses, and an easy way to track pieces of information gained during the call. XML-Based call flows allow anyone to create the a flow and share it with others so they can reproduce the attack.

</details>

<details><summary><strong>SocialKlepto</strong> — Jason Ding</summary>

**Track:** Human Factors · **Event:** USA 2013  
🔗 **Link:** Not Available  
📝 **Description:** We will demonstrate two tools, which one can launch effective social attacks to conduct corporate espionage, and the other one can defend users from such attacks. The first toolkit SocialKlepto can collect valuable competitive intelligence and steal your competitors’ customers without infiltrating their computer networks. SocialKelpto can monitor every social activity of your competitors or any company using a controlled network of fake social accounts, REST APIs, database search, and data analysis. Specifically, the SocialKlepto system can build effective fake LinkedIn accounts, establish trust within business circles, send bulk of persuasive invitations, and monitor every activity of your competitors. Finally, using big data analysis, it can extract valuable information that can turn into sales opportunities and revenue. The second tool is an open and free Chrome plugin for LinkedIn privacy settings. We will release this defensive tool that easily help LinkedIn users check and set their privacy settings, in order to protect them from such social attacks.

</details>

---
