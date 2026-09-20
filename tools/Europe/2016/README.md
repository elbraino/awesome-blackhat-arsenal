# Europe 2016
---
📍 33 tools demonstrated at **Black Hat Arsenal Europe 2016**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [Others](#others) (16)
- [🌐 Web/AppSec](#-webappsec) (5)
- [📱 Mobile Security](#-mobile-security) (2)
- [🔴 Red Teaming](#-red-teaming) (5)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (2)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (3)
---
## Others
<details><summary><strong>.NET Security Guard</strong> — Philippe Arteau</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/dotnet-security-guard/roslyn-security-guard](https://github.com/dotnet-security-guard/roslyn-security-guard)  
📝 **Description:** .NET Security Guard is a code analyzer using the brand new Roslyn API, a framework built to develop analyzers, refactoring tools and build tools. It allows developers to scan their C# and VB.net code for potential vulnerabilities directly from Visual Studio. The analyzers are able to find a wide range of vulnerabilities from injection flaws to cryptographic weaknesses. Example of vulnerable applications will be analyzed in a live demonstration.

</details>

<details><summary><strong>Aktaion</strong> — Joseph Zadeh, Rod Soto</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/jzadeh/aktaion](https://github.com/jzadeh/aktaion)  
📝 **Description:** Crypto Ransomware has become a popular attack vector used by malicious actors to quickly turn infections into profits. From a defensive perspective, the detection of new ransomware variants relies heavily on signatures, point solution posture and binary level indicators of compromise (IOC). This approach is inefficient at protecting targets against the rapid changes in tactics and delivery mechanisms typical of modern ransomware campaigns. We propose a novel approach for blending multiple signals (called micro behaviors) to detect ransomware with more flexibility than using IOC matching alone. The goal of the approach is to provide expressive mechanisms for detection via contextual indicators and micro behaviors that correlate to attacker tactics, even if they evolve with time. The presenters will provide open source code that will allow users and fellow researchers to replicate the use of these techniques. We will conclude with a focus on how to tie this approach to active defense measures and existing infrastructure. This tool will be applied to PCAPS and will then mine and display relationships of Micro Behaviors particular to ransomware traffic. Built with Spark notebook https://github.com/andypetrella/spark-notebook we are leveraging Apache Spark (http://spark.apache.org/) for scalable data processing and MlLib for an analytics API (http://spark.apache.org/mllib/). Thenotebook will provide an interface for the ingestion of heterogenous data and the ability to build a combination of behavior based risk indictors combined with classic signatures. Prototype examples of different risk profiles will be demonstrated with the API via spark notebook but the libraries themselves should be usable in any Java backed code base.

</details>

<details><summary><strong>AMIRA: Automated Malware Incident Response and Analysis for MacOS</strong> — Jakub (Kuba) Sendor</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/Yelp/amira](https://github.com/Yelp/amira)  
📝 **Description:** Even for a big incident response team handling all of the repetitive tasks related to malware infections is a tedious task. Early on, we automated some of the collection and analysis using our own open source OSXCollector. This helped us quickly identify suspicious domains, URLs and file hashes. But our approach to the analysis still required manual steps that was consuming lots of attention from malware responders. Enter automation: Further reducing the repetitive tasks will help you deal faster with the incident discovery, forensic collection and analysis, with fewer possibilities to make a mistake. We have turned our OSXCollector toolkit into AMIRA: Automated Malware Incident Response and Analysis service. AMIRA turns the forensic information gathered by OSXCollector into an actionable response plan, suggesting the infection source as well as suspicious files and domains requiring a closer look. Furthermore, we integrated AMIRA with our incident response platform, making sure that as little interaction as necessary is required from the analyst to trigger the collection of the forensic artifacts. Thanks to that, the incident response team members can focus on what they excel at: finding the unusual patterns and discovering the novel ways that malware was trying to sneak into the corporate infrastructure.

</details>

<details><summary><strong>BloodHound</strong> — Andy Robbins</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/SpecterOps/BloodHound-Legacy](https://github.com/SpecterOps/BloodHound-Legacy)  
📝 **Description:** Active Directory domain privilege escalation is a critical component of most penetration tests and red team assessments, but standard methodology dictates a manual and often tedious process - gather credentials, analyze new systems we now have admin rights on, pivot, and repeat until we reach our objective. Then - and only then - we can look back and see the path we took in its entirety. But that may not be the only, nor shortest path we could have taken. By combining the concept of derivative admin (the chaining or linking of administrative rights), existing tools, and graph theory, we have developed a capability called BloodHound, which can reveal the hidden and unintended relationships in Active Directory domains. BloodHound is operationally-focused, providing an easy-to-use web interface and PowerShell ingestor for memory-resident data collection and offline analysis. BloodHound offers several advantages to both attackers and defenders. Otherwise invisible, high-level organizational relationships are exposed. Most possible escalation paths can be efficiently and swiftly identified. Simplified data aggregation accelerates blue and red team analysis. BloodHound has the power and the potential to dramatically change the way you think about and approach Active Directory domain security. At Black Hat Europe 2016, we will unveil the newest addition to BloodHound: object ACL control relationships. We will also unveil new defensive analytics and automated analysis possible only with BloodHound.

</details>

<details><summary><strong>CodexGigas Malware DNA Profiling Search Engine</strong> — Luciano Martins, Javier Bassi, Rodrigo Cetera</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/codexgigassys/codex-backend](https://github.com/codexgigassys/codex-backend)  
📝 **Description:** Next generation threats are becoming more sophisticated and stealthy, and incident response teams require more advanced tools to respond to such attacks. CodexGigas is a malware profiling search engine that allows malware hunters and analysts to really interrogate the internals of malware and perform searches over a large number of file characteristics. For instance, instead of relying on file-level hashes, we can compute other features such as imported functions, strings, constants, file segments, code regions, or anything that is defined in the file type specification, and that provides us with more than 150 possible searchable patterns, that can be combined. Similar to human fingerprints, every malware has its own unique digital fingerprint that differentiates it from others. As a result, malware will always attempt to hide its true self by deleting or changing this information to avoid detection by antivirus companies and malware researchers. Since malware developers go to great lengths to obfuscate their characteristics, it is often difficult for by researchers and malware analysts to identify multiple characteristics and correlation points. By analyzing malware internals, the algorithm is able to build characteristic families to which a new sample can be categorized and therefore identified for specific behavior, enabling early detection of new malware by comparing against existing malware. Come to see how CodexGigas could be used to enhance your malware hunting capabilities. Link: https://twitter.com/codexgigassys; link: https://github.com/codexgigassys/

</details>

<details><summary><strong>DiffDroid</strong> — Anto Joseph</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** Not Available  
📝 **Description:** DiffDroid is a Framework which makes dynamic security assessments in android much easier with its modules for profiling, logging and modifying application logic. It's extremely user-friendly, uses javascript, makes no changes to the Operating system and is ready to go. You could use it for Malware Analysis, Security Assessments or a few points in your favorite game. :) What's New with DIFFDroid? DIFFDroid uses Frida, you write your code in javascript, a V8 Engined injected into your application runs the code and you can even make changes to your instrumentation code "REALTIME!" It requires you to make zero changes to your device and you could instrument the application even if you don't have root access.

</details>

<details><summary><strong>Exploit Pack</strong> — Juan Sacco</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** Not Available  
📝 **Description:** Exploit Packs contains a full set of 35000+ exploits - you can be sure that your next pentest will become unstoppable. All operating systems are supported, including: Windows, Linux, Unix, Minix, SCO, Solaris, OSX, etc. and even mobile and web platforms. Exploit Pack is an integrated environment for performing and conducting professional penetration tests. As any tool of this type, it requires some basic knowledge and expertise in the matter. Exploit Pack has been designed to be used by hands-on security professionals to support their testing process. With a little bit of effort, anyone can start using the core features of Exploit Pack to test in-deep the security of their applications. Some Exploit Pack's more advanced features will take further learning and experience to master. All of this time-investment is hugely worth it.

</details>

<details><summary><strong>FakeNet-NG</strong> — Peter Kacherginsky</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/mandiant/flare-fakenet-ng](https://github.com/mandiant/flare-fakenet-ng)  
📝 **Description:** FakeNet-NG is a next generation dynamic network analysis tool for malware analysts and penetration testers. FakeNet-NG was inspired by the original FakeNet tool developed by Andrew Honig and Michael Sikorski. FakeNet-NG implements all the old features and many new ones; plus, it is open source and designed to run on modern versions of Windows. FakeNet-NG allows you to intercept and redirect all or specific network traffic while simulating legitimate network services. Using FakeNet-NG, malware analysts can quickly identify malware's functionality and capture network signatures. Penetration testers and bug hunters will find FakeNet-NG's configurable interception engine and modular framework highly useful when testing application's specific functionality and prototyping PoCs. During the tool session attendees will learn the following practical skills:

</details>

<details><summary><strong>Faraday</strong> — Juan Pablo Daniel Borgna</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/infobyte/faraday](https://github.com/infobyte/faraday)  
📝 **Description:** Since collaborative pentesting is more common each day and teams become larger, sharing the information between pentesters can become a difficult task. Different tools, different formats, long outputs (in the case of having to audit a large network) can make it almost impossible. You may end up with wasted efforts, duplicated tasks, a lot of text files scrambled in your working directory. And then, you need to collect that same information from your teammates and write a report for your client, trying to be as clear as possible. The idea behind Faraday is to help you to share all the information that is generated during the pentest, without changing the way you work. You run a command, or import a report, and Faraday will normalize the results and share that with the rest of the team in real time. Faraday has more than 50 plugins available (and counting), including a lot of common tools. And if you use a tool for which Faraday doesn't have a plugin, you can create your own. During this presentation we're going release Faraday v2.0 with all the new features that we were working on for the last couple of months.

</details>

<details><summary><strong>FLOSS</strong> — Moritz Raabe</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/mandiant/flare-floss](https://github.com/mandiant/flare-floss)  
📝 **Description:** The FireEye Labs Obfuscated String Solver (FLOSS) is an open source tool that automatically detects, extracts, and decodes obfuscated strings in Windows Portable Executable (PE) files. Malware analysts, forensic investigators, and incident responders can use FLOSS to quickly extract sensitive strings to identify indicators of compromise (IOCs). Malware authors encode strings in their programs to hide malicious capabilities and impede reverse engineering. Even simple encoding schemes defeat the 'strings' tool and complicate static and dynamic analysis. FLOSS uses advanced static analysis techniques, such as emulation, to deobfuscate encoded strings. FLOSS is extremely easy to use and works against a large corpus of malware. It follows a similar invocation as the 'strings' tool. Users that understand how to interpret the strings found in a binary will understand FLOSS's output. FLOSS extracts higher value strings, as strings that are obfuscated typically contain the most sensitive configuration resources â€" including C2 server addresses, names of dynamically resolved imports, suspicious file paths, and other IOCs. I will describe the computer science that powers the tool, and why it works. I will also show how to use FLOSS and demonstrate the decoding of strings from a wide variety of malware families.

</details>

<details><summary><strong>JTAGulator</strong> — Joe Grand</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/grandideastudio/jtagulator](https://github.com/grandideastudio/jtagulator)  
📝 **Description:** JTAGulator is an open source hardware hacking tool that assists in identifying on-chip debug interfaces from test points, vias, or component pads on a circuit board. It currently supports the detection of JTAG and asynchronous serial/UART interfaces. The tool can save a tremendous amount of time during reverse engineering, particularly for those who don't have the skill and/or equipment required for traditional processes. Black Hat Arsenal Europe 2016 will mark the release of a new firmware version and Joe will provide demonstrations of the tool's expanded functionality.

</details>

<details><summary><strong>Koodous</strong> — Daniel Vaca</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** Not Available  
📝 **Description:** Koodous is a collaborative web platform for Android malware research that combines the power of online analysis tools with social interactions between the analysts over a vast APK repository (at this time, more than 10 million). It also features an Android antivirus app and a public API. Some of the features included in the tool:

</details>

<details><summary><strong>Lynis</strong> — Michael Boelen</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/CISOfy/lynis](https://github.com/CISOfy/lynis)  
📝 **Description:** Lynis is a nifty tool to perform in-depth security tests. It checks your systems for configuration errors, software vulnerabilities, or other weaknesses. Running on the system itself, it can uncover flaws not seen by other tools (e.g. vulnerability scanners). After finishing the scan, it will present the user with a report of the findings. Suggestions are made to enhance your security posture or help you remain compliant with security standards like PCI DSS.Lynis is written in shell script and runs on systems like Linux, macOS, and UNIX-based derivatives. The tool is ideal for those who seek to perform vulnerability assessments and penetration tests, or having to apply system hardening measures.

</details>

<details><summary><strong>Needle</strong> — Marco Lancini</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/ReversecLabs/needle](https://github.com/ReversecLabs/needle)  
📝 **Description:** Assessing the security of an iOS application typically requires a plethora of tools, each developed for a specific need and all with different modes of operation and syntax. The Android ecosystem has tools like "drozer" that have solved this problem and aim to be a "one stop shop" for the majority of use cases, however iOS does not have an equivalent. "Needle" is an open source modular framework which aims to streamline the entire process of conducting security assessments of iOS applications, and acts as a central point from which to do so. Given its modular approach, Needle is easily extensible and new modules can be added in the form of python scripts. Needle is intended to be useful not only for security professionals, but also for developers looking to secure their code. A few examples of testing areas covered by Needle include: data storage, inter-process communication, network communications, static code analysis, hooking and binary protections.â€' The only requirement in order to run Needle effectively is a jailbroken device. The tool's architecture, capabilities and roadmap will be described. A demonstration will also be performed of how Needle can be used to find vulnerabilities in iOS applications from both a black-box and white-box perspective (if source code is provided).

</details>

<details><summary><strong>OWASP ZAP</strong> — Simon Bennetts</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)  
📝 **Description:** The Zed Attack Proxy (ZAP) is currently the most active open source web application security tool and was voted the top security tool in the last Toolswatch annual survey. While it is an ideal tool for people new to appsec, it also has many features specifically intended for advanced penetration testing.

</details>

<details><summary><strong>Yasuo</strong> — Saurabh Harit</summary>

**Track:** — · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/0xsauby/yasuo](https://github.com/0xsauby/yasuo)  
📝 **Description:** Yasuo is a ruby framework that scans for vulnerable 3rd-party web applications. While working on a network security assessment (internal, external, redteam gigs etc.), we often come across vulnerable 3rd-party web applications or web front-ends that allow us to compromise the remote server by exploiting publicly known vulnerabilities. Some of the common & favorite applications are Apache Tomcat administrative interface, JBoss jmx-console, Hudson Jenkins and so on. Searching Exploit-db will reveal over 10,000 remotely exploitable vulnerabilities that exist in tons of web applications/front-ends and could allow an attacker to completely compromise the back-end server. These vulnerabilities range from RCE to malicious file uploads to SQL injection to RFI/LFI etc. Yasuo is built to quickly scan the network for such vulnerable applications. Currently, it supports around 150 vulnerable applications. In addition to discovering the vulnerable applications through their unique signature, it also detects if the app requires authentication. If it does, Yasuo performs a brute-force attack against them. In the end, it outputs the IP, vulnerable app url, login status and credentials, if found. Currently, many new features are being added to Yasuo, like smart brute-forcing, internal network pentest mode, new signatures etc.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>DeepViolet TLS/SSL Scanner</strong> — Milton Smith</summary>

**Track:** Web AppSec · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/spoofzu/DeepViolet](https://github.com/spoofzu/DeepViolet)  
📝 **Description:** DeepViolet TLS/SSL scanner is an information gathering tool for secure web servers. Written in Java, DeepViolet is be run from the command line, as a desktop application, or included as an API in other programs. Use DeepViolet to enumerate web server cipher suites, display X.509 certificate metadata, examine X.509 certificate trust chains, and more. DeepViolet is an open source project written to help educate the technical community around TLS/SSL and strengthen our knowledge of security protocols while we improve security of our web applications. DeepViolet project is always looking for volunteers.

</details>

<details><summary><strong>From XSS to RCE 2.5</strong> — Hans-Michael Varbaek</summary>

**Track:** Web AppSec · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/Varbaek/xsser](https://github.com/Varbaek/xsser)  
📝 **Description:** This presentation demonstrates how an attacker can utilise XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes cool notifications and new attack vectors!

</details>

<details><summary><strong>OWASP CSRFGuard</strong> — Azzeddine RAMRAMI</summary>

**Track:** Web AppSec · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/aramrami/OWASP-CSRFGuard](https://github.com/aramrami/OWASP-CSRFGuard)  
📝 **Description:** OWASP CSRFGuard implements a variant of the synchronizer token pattern to mitigate the risk of CSRF attacks. In order to implement this pattern, CSRFGuard must offer the capability to place the CSRF prevention token within the HTML produced by the protected web application. CSRFGuard 3 provides developers more fine grain control over the injection of the token. Developers can inject the token in their HTML using either dynamic JavaScript DOM manipulation or a JSP tag library. CSRFGuard no longer intercepts and modifies the HttpServletResponse object as was done in previous releases. The currently available token injection strategies are designed to make the integration of CSRFGuard more feasible and scalable within current enterprise web applications. Developers are encouraged to make use of both the JavaScript DOM Manipulation and the JSP tag library strategies for a complete token injection strategy.CSRFGuard WikiPage: https://www.owasp.org/index.php/Category:OWASP_CSRFGuard_Project

</details>

<details><summary><strong>WSSAT - Web Service Security Assessment Tool</strong> — Mehmet Yalcin YOLALAN, Salih TALAY</summary>

**Track:** Web AppSec · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/YalcinYolalan/WSSAT](https://github.com/YalcinYolalan/WSSAT)  
📝 **Description:** WSSAT is an open source web service security scanning tool which provides a dynamic environment to add, update or delete vulnerabilities by just editing its configuration files. This tool accepts WSDL address list as input file and performs both static and dynamic tests against the security vulnerabilities. It also makes information disclosure controls. Objectives of WSSAT are to allow organizations:Perform their web services security analysis at onceSee overall security assessment with reportsHarden their web servicesWSSAT's main capabilities include:Dynamic Testing:Insecure Communication; SSL Not Used Unauthenticated Service Method; Error Based SQL Injection; Cross Site Scripting; XML Bomb; External Entity Attack - XXE XPATH Injection; Verbose SOAP Fault MessageStatic Analysis:Weak XML Schema: Unbounded Occurrences; Weak XML Schema: Undefined Namespace; Weak WS-SecurityPolicy: Insecure Transport; Weak WS-SecurityPolicy: Insufficient Supporting Token Protection; Weak WS-SecurityPolicy: Tokens Not ProtectedInformation Leakage: Server or development platform oriented information disclosureWSSAT's main modules are:ParserVulnerabilities LoaderAnalyzer/AttackerLoggerReport GeneratorThe main difference of WSSAT is to create a dynamic vulnerability management environment instead of embedding the vulnerabilities into the code. More information can be found here: https://github.com/YalcinYolalan/WSSAT

</details>

<details><summary><strong>Yaps</strong> — Fabio Nigi</summary>

**Track:** Web AppSec · **Event:** Europe 2016  
🔗 **Link:** Not Available  
📝 **Description:** The number one security hole is a weak password. Companies are growing without a complete control over exposed services; most of the servers are deployed with default password. Most of the tools today are single host-based, without competing on a cloud/global environment. Configuration and deployment are getting faster -all the services are going in pipeline with automation and scalability focus. Infosec tools need to evolve. The project goal of Yaps *yet another password scanner:*Create a new scanner to work in pipeline with nmap and other source (json, xml, csv) port mapper and enable a scalable full feature weak password scanner, analyse in a flow the port, create a history status based on the history of scan and result, evade incidents and avoid stressful and lockdown test on production servers and giving the users full flexibility to decrease false positive reports. Highly scalable container based (docker, mesos, chronos, python)Modular concept with multi protocol support and fully automated.

</details>

---
## 📱 Mobile Security
<details><summary><strong>AppMon: Runtime Security Testing & Profiling Framework for Native Apps</strong> — Nishant Das Patnaik</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/dpnishant/appmon](https://github.com/dpnishant/appmon)  
📝 **Description:** AppMon is a runtime security testing & profiling framework for macOS, iOS and android apps. It is useful for mobile app penetration testers to validate the security issues report by a source code scanner by validating them by inspecting the API calls at runtime. You may use it for monitoring the app's overall activity during its runtime and focus on things that seem suspicious e.g. information leaks, insecure storage of credentials/secret tokens etc. or insecure implementation of crypto operations or just sniff app's network activity from HTTP to Bluetooth. You may either use one or many of the pre-written user-scripts or quickly learn to write your own scripts modify the app's functionality/logic in the runtime e.g. spoofing the DeviceID, spoofing the GPS co-ordinates, bypassing Apple's TouchID, bypassing root detection etc. We shall demo the features of existing 4 core components: Sniffer, Intruder, Android Tracer & IPA Installer. If there any any additional development to the project we shall include its demo as well.

</details>

<details><summary><strong>Nmap on Android</strong> — Vlatko Kosturjak</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/kost/nmap-android](https://github.com/kost/nmap-android)  
📝 **Description:** Network Mapper is Android frontend for well known Nmap scanner. Frontend will help you to download, install and run Nmap on Android-based phone. It is also a collection of tools to build all known Android architectures: arm, mips and x86 in 32/64 bit architectures. Shiny new 2.0 release will be presented with easy interface and mobile specific scans.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>APT2 - Automated Penetration Testing Toolkit</strong> — Adam Compton, Austin Lane</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/tatanus/apt2](https://github.com/tatanus/apt2)  
📝 **Description:** Nearly every penetration test begins the same way; run a NMAP scan, review the results, choose interesting services to enumerate and attack, and perform post-exploitation activities. What was once a fairly time consuming manual process, is now automated! Automated Penetration Testing Toolkit (APT2) is an extendable modular framework designed to automate common tasks performed during penetration testing. APT2 can chain data gathered from different modules together to build dynamic attack paths. Starting with a NMAP scan of the target environment, discovered ports and services become triggers for the various modules which in turn can fire additional triggers. Have FTP, Telnet, or SSH? APT2 will attempt common authentication. Have SMB? APT2 determines what OS and looks for shares and other information. Modules include everything from enumeration, scanning, brute forcing, and even integration with Metasploit. Come check out how APT2 will save you time on every engagement.

</details>

<details><summary><strong>CROZONO Framework: Leveraging Autonomous Devices as an Attack Vector on Industrial Networks</strong> — Sheila Ayelen Berta, Nicolas Villanueva</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/johnjohnsp1/CROZONO](https://github.com/johnjohnsp1/CROZONO)  
📝 **Description:** CROZONO is a framework that allows performing automated penetration tests from autonomous devices (drones, robots, etc.) that could ease the access to the logical infrastructure of an industrial facility, evading physical barriers. The CROZONO framework is presented in two versions: "CROZONO Explorer" and "CROZONO Attacker."At first, it is advisable to use CROZONO Explorer, as it allows the user to perform information gathering about possible attack vectors on the whole industrial facility's perimeter or any other sector. The information gathered by CROZONO Explorer allows the user to see the location of WiFi Access Points and IP Cameras, together with their security levels. The purpose of this step is to find the easiest way to compromise the industrial facility's security. For example, attacking those WiFi access points which have the lowest security level, if any security measures at all. CROZONO Attacker is a smart framework, it has the capability of performing automated attacks targeted to a network, and to take decisions -without the need of the attacker's intervention- on which attacks to perform based on pre-established parameters and the information gathered about its target. The goal of CROZONO Attacker is to breach the network attacking a WiFi access point and then opening a reverse connection to the attacker via the victim's internet connection. Once performed, CROZONO Attacker allows - through its "LAN discovery" and "LAN Attacks" modules - to discover other devices in the target network and launch several attacks on it. One of the best exclusive features of CROZONO is the report generation about all information gathered. In few minutes, it is possible to explore a zone or an industrial facility's perimeter and know its weak points from the summarization of data captured visually, allowing to see its security exposure levels.

</details>

<details><summary><strong>OWASP ZSC</strong> — Ali Razmjoo Qalaei, Brian Beaudry</summary>

**Track:** Malware Offense · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/OWASP/ZSC](https://github.com/OWASP/ZSC)  
📝 **Description:** OWASP ZSC is an open source software in python language which lets you generate customized shellcodes and convert scripts to an obfuscated script. This software can be run on Windows/Linux/OSX under python. According to other shellcode generators same as metasploit tools and etc, OWASP ZSC using new encodes and methods which antiviruses won't detect. OWASP ZSC encoderes are able to generate shell codes with random encodes and that allows you to generate thousands of new dynamic shellcodes with same job in just a second,that means, you will not get a same code if you use random encodes with same commands, And that make OWASP ZSC one of the best! During the Google Summer of Code we are working on to generate Windows Shellcode and new obfuscation methods. We are working on the next version that will allow you to generate OSX.

</details>

<details><summary><strong>PowerMemory</strong> — Pierre-Alexandre Braeken</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/giMini/PowerMemory](https://github.com/giMini/PowerMemory)  
📝 **Description:** PowerMemory is a PowerShell post-exploitation tool. It uses Microsoft binaries and therefore is able to execute on a machine, even after the Device Guard Policies have been set. In the same way, it will bypass antivirus detection. PowerMemory can retrieve credentials information and manipulate memory. It can execute shellcode and modify process in memory (in userland and kernel land as a rootkit). PowerMemory will access everywhere in user-land and kernel-land by using the trusted Microsoft debugger aka cdb.exe which is digitally signed. We will cover the following subjects:User-land proof-of-concept: attacking the digest Security Support Provider byte per byte with PowerShell and Microsoft debugger to retrieve passwords from memoryKernel-land proof-of-concept: Direct Kernel Object Manipulation with PowerShell and Microsoft debugger o Hiding/Un-hiding a process o Protecting a process o Injecting all privileges in a process with SYSTEM identity o Pass-The-Token attackUser-land proof-of-concept: Injecting and executing a shellcode in a remote process with PowerShell and a Microsoft debuggerIf we have time, we will hack the minesweeper too :-)

</details>

<details><summary><strong>WarBerryPi</strong> — Yiannis Ioannides</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/secgroundzero/warberry](https://github.com/secgroundzero/warberry)  
📝 **Description:** What if the only requirements for taking down a corporate network are 60 minutes and $35? Traditional hacking techniques and corporate espionage have evolved. Advanced attacks nowadays include a combination of social engineering, physical security penetration and logical security hacking. It is our job as security professionals to think outside the box and think about the different ways that hackers might use to infiltrate corporate networks. The WarBerry is a customized RaspBerryPi hacking dropbox which is used in Red Teaming engagements with the sole purpose of performing reconnaissance and mapping of an internal network and providing access to the remote hacking team while remaining covert and bypassing security mechanisms. The outcome of these red teaming exercises is the demonstration that if a low cost microcomputer loaded with python code can bypass security access controls and enumerate and gather such a significant amount of information about the infrastructure network which is located at, then what dedicated hackers with a large capital can do is beyond conception. The talk will be comprised of slides and a demonstration of the WarBerry's capabilities in a virtual network.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Automated Vulnerability Assessment & Penetration Testing Tool</strong> — Shaan Mulchandani, Ravi Keerthi</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2016  
🔗 **Link:** Not Available  
📝 **Description:** As application, network, and product complexity grow, so do the attack surface and likelihood of vulnerabilities. Highly-skilled pen testers do not scale exponentially, and findings don't make it into secure coding practices or DevOps overnight. How can we enable pen testers to focus on what matters: adversary-oriented penetration testing to detect the most difficult vulnerabilities and exploits? What correlations exist between successful exploits and underlying application or network characteristics? And how can we ensure findings actually make it back into the development lifecycle in a meaningful way?Our research, and Python-based VAPT framework seeks to address these questions, and automates certain tasks to assist pen testers:For each application or network update, network reconnaissance and application/network vulnerability assessments are performed using NMap, Nessus, OpenVAS, and W3AFIdentified vulnerabilities, and their CVEs, are used for retrieving relevant exploits from ExploitDBPenetration tests are performed using W3AF and MetasploitResults obtained at each stage are stored and correlated as part of a (Neo4j-based) knowledge graph, which can be maintained across several (application) releases and tool runs. This allows for:Pen Testers to easily visualize vulnerabilities discovered, and successful/failed exploits - in order to rapidly gain context of additional potential exploits that may be run or vulnerabilities that may be discoverable through sophisticated, manual techniquesDevelopers to visualize vulnerabilities that are persistent across multiple parts of their product/application, and/or across multiple successive releasesWe will demo this initial version at Arsenal, however the extensible nature of our framework allows for integration of additional vulnerability assessment & penetration testing tools or (pre-deployment) code security review tools and their findings as well.

</details>

<details><summary><strong>Dradis: Collaboration and Reporting for InfoSec Teams</strong> — Daniel Martin</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/dradis/dradis-ce](https://github.com/dradis/dradis-ce)  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, and Burp. Started in 2007, the Dradis Framework project has been growing ever since (15,000 commits in the last 12 months). Dradis is the best tool to consolidate the output of different scanners, add your manual findings and evidence and have all the engagement information in one place. Come to see the latest Dradis release in action. It's loaded with updates including new tool, connectors (Metasploit, Brakeman, ...), full REST API coverage, testing methodologies and lots of interface improvements (issue tagging, UX improvements and much more). Come and find out why Dradis is being downloaded over 300 times every week. Come and check it out before we run out of stickers!

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Firmware Analysis Toolkit (FAT)</strong> — Aditya Gupta</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/attify/firmware-analysis-toolkit](https://github.com/attify/firmware-analysis-toolkit)  
📝 **Description:** There exists a number of tools in today's security industry which offers static and dynamic analysis of software binaries and mobile applications. However, there is no such toolkit, which helps an embedded or IoT security researcher to analyse firmwares in an in-depth level. FAT or Firmware Analysis Toolkit is a scriptable toolkit suite is a part of Attify's internal pentesting suite which has helped us reduce a significant number of man hours put into firmware analysis in our IoT and smart devices pentest engagements. It comes with an easy to use API which can then be used in additional analysis, as well as for research purposes. It is a toolkit suite which performs static and dynamic analysis of firmwares, also enabling the user to emulate the firmware and having a live firmware device as if a real physical device was sitting on the network. This has been done by taking advantage of Qemu emulation and static vulnerability identification techniques. Below are some of the capabilities of the toolkit : Full emulation of the firmware along with networking Dynamic traffic analysis Static vulnerability identification Integration with tools such as nmap and metasploit for additional assessment and exploitationBy Black Hat EU, there might be more features added to the list which I will later on send once they are in a more concrete stage. FAT has been made possible because of the following open source tools listed below, which FAT leverages at various stages:Binwalk Firmware Modification KitFirmadyneMITMProxyNmapMetasploitSnmpwalkRadare2

</details>

<details><summary><strong>HEATHEN Internet of Things Pentesting Framework</strong> — Chiheb Chebbi</summary>

**Track:** Internet Of Things · **Event:** Europe 2016  
🔗 **Link:** [https://github.com/chihebchebbi/Internet-Of-Things-Pentesting-Framework](https://github.com/chihebchebbi/Internet-Of-Things-Pentesting-Framework)  
📝 **Description:** Oxford defines the Internet of Things as: "A proposed development of the Internet in which everyday objects have network connectivity, allowing them to send and receive data."Heathen IoT of Things Penetration Testing Framework developed as a research project, which automatically help developers and manufacturers build more secure products in the Internet of Things space based on the Open Web Application Security Project (OWASP) by providing a set of features in every fundamental era:Insecure Web InterfaceInsufficient Authentication/AuthorizationInsecure Network ServicesLack of Transport EncryptionPrivacy ConcernsInsecure Cloud InterfaceInsecure Mobile InterfaceInsufficient Security ConfigurabilityInsecure Software/FirmwarePoor Physical Security

</details>

<details><summary><strong>Offense and Defense Toolkits in High/Low Frequency</strong> — Haoqi Shan, Yunding Jian, YANG Qing</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2016  
🔗 **Link:** Not Available  
📝 **Description:** RFID and contact-less smart cards have become pervasive technologies nowadays. IC/RFID cards are generally used in security systems such as airport and military bases that require access control. This presentation introduces the details of contact-less card security risk firstly, then the principles of low frequency(125KHz) attack tool, HackID Pro, will be explained. This tool contains an Android App and a hardware which can be controlled by your phone. HackID Pro can emulate/clone any low frequency IC card to help you break into security system, just type few numbers on your phone. After 125KHz, this presentation will show you how to steal personal information from EMV bank card, whose carrier frequency is high frequency, 13.56MHz, just sitting around you. In the end, our defense tool, Card Defender, will be dissected to explain how this product can protect your card and information in both high/low frequencies. And a little bit tricks that this defense tool can make. This presentation includes three demonstrations. The first demonstration will show how we can use the self-made hardware, HackID Pro, to clone and emulate common seen low frequency ID card, different from the hardware we used - HackID Pro contains an Android App and a module which inject into your phone by audio interface. Second, we will show people how to steal people's privacy information from their EMV card, just walked by them. Finally, we introduce how can we protect that information by our defense tool, Card Defender, and we will explain the principle detailed. This toolkit is developed by Qihoo 360 UnicornTeam, which has many genius hardware/wireless security researcher. UnicornTeam focuses on embedded device vulnerability mining, 2/3/4G communication security, GPS signal faking, smart car security, etc. Members of UnicornTeam also had presentations on DEFCON, Black Hat, Cansecwest, Ruxcon, HITB, Syscan360 and some other international security conference.

</details>

---
