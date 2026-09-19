# USA 2021
---
📍 64 tools demonstrated at **Black Hat Arsenal USA 2021**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [☁️ Cloud Security](#-cloud-security) (1)
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (3)
- [🌐 Web/AppSec](#-webappsec) (2)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (3)
- [📱 Mobile Security](#-mobile-security) (3)
- [🔍 OSINT](#-osint) (3)
- [🔴 Red Teaming](#-red-teaming) (20)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (9)
- [🔵 Blue Team & Detection](#-blue-team--detection) (11)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (3)
- [🧠 Reverse Engineering](#-reverse-engineering) (6)
---
## ☁️ Cloud Security
<details><summary><strong>Falco + Falcosidekick = A Kubernetes Response Engine</strong> — Stefano Chierici</summary>

**Track:** Cloud Security · Malware Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/falcosecurity/falcosidekick](https://github.com/falcosecurity/falcosidekick)  
📝 **Description:** Falco is the CNCF open-source project for runtime threat detection for containers and Kubernetes. It was created by Sysdig in 2016 and is the first runtime security project to join CNCF as an incubation-level project. Falco is a container security tool designed to detect anomalous activity in your local machine, container, cloud, a managed Kubernetes cluster, or a Kubernetes cluster such as K3s. It taps into system calls and Kubernetes Audit logs to generate an event stream of all system activity. One of the benefits of Falco is in leveraging its powerful and flexible rules language. As a result, Falco will generate security events when it finds abnormal behaviors as defined by a customizable set of rules. Meanwhile, Falco comes with a handful of out-of-the-box detection rules. The Falco community is strong and active, contributing largely to not only the project but methods in which folks can find threats and feed whatever method they choose with examples! Falcosidekick was born providing an easy to use UI to Falco and an enhanced available outputs. Falcosidekick even provides a response engine utilizing serverless (lambda, knative, kubeless, openfaas) which extends capabilities to whatever the security team wants to create remediation functions for with examples such as stopping a container, memdump, etc etc.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Arsenal Reception</strong></summary>

**Track:** Arsenal Lab · **Event:** USA 2021  
🔗 **Link:** [https://github.com/Orange-Cyberdefense/arsenal](https://github.com/Orange-Cyberdefense/arsenal)  
📝 **Description:** Join us on Thursday, November 11, from 2:50 PM – 4:00 PM for drinks and networking as we thank our Arsenal presenters for their contributions to the open-source community.

</details>

<details><summary><strong>Hacking the Digital Drone License Plate</strong> — Bobby Sakaki</summary>

**Track:** Arsenal Lab · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** This game is designed to explore a variety of proposed drone identification protocols, so called UAS Remote ID systems. Your goal will be to find a weakness in a variety Remote ID protocols and exploit it by (generally) forging a message that a receiver will accept as valid. There are eight levels (0-7), where each represents some simulacrum of an existing protocol, a proposed protocol, or an amalgamation of both. Point being: pretty much everything out there is, has been, or can be broken. Requirements: Players will need some sort of device on which they can write and run some basic code and have a connection to the internet. That's basically it. There are no restrictions on the toolset, though you will find languages that support HTTP POST requests, JSON parsing, and cryptographic operations to be very helpful.

</details>

<details><summary><strong>Hands-on Security Analysis of Selected Avionics Systems Using the Triton Testbed</strong> — Dr. Karl Koscher</summary>

**Track:** Arsenal Lab · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** Have you ever wondered how airplanes communicate from the aircraft to the ground facilities and back? In the 737, that magic is performed in the Communications Management Unit (CMU). As the CMU has access to critical avionics buses (all ARINC 429) and accepts potentially untrusted RF traffic, making its role uniquely privileged in bridging the untrusted outside world with the trusted avionics domain, and thus an attractive target for evaluation. In this demonstration, we'll be showing off our Triton Testbed, which virtualizes the other support systems needed for the CMU to function. We can also use the testbed to interact with CMU, either through the typical MCDU display or directly at the ARINC 429 bus level. We can demonstrate real and generated ACARS and VDL2 traffic and show how the CMU responds. Finally, we can demonstrate the application processor of the CMU under emulation in qemu, with i/o redirected to the actual hardware, allowing us to perform several new types of dynamic analyses quickly.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>reNgine: An Automated Reconnaissance Framework</strong> — Yogesh Ojha</summary>

**Track:** Web AppSec · **Event:** USA 2021  
🔗 **Link:** [https://github.com/yogeshojha/rengine](https://github.com/yogeshojha/rengine)  
📝 **Description:** reNgine is an automated reconnaissance engine(framework) that is capable of performing end-to-end reconnaissance with the help of highly configurable scan engines on web application targets. reNgine makes use of various open-source tools and makes a highly configurable pipeline of reconnaissance to gather the recon result. reNgine also makes it possible for users to choose the tools they desire while following the same reconnaissance pipeline, example - with reNgine you aren't limited to using sublist3r for subdomains discovery, rather reNgine allows you to combine multiple tools like sublist3r, subfinder, assetfinder, and easily integrate them into your reconnaissance pipeline. The reconnaissance results are then displayed in a beautiful and structured UI after performing the co-relation in the results produced by these various tools. The developers behind reNgine understand that recon result most often is overwhelming due to the humongous data, so that's why reNgine also comes with advanced query lookup using natural language operators like and, or and not. Imagine, doing recon on facebook.com and filtering the results like http_status!404&page_title=admin|page_title=dashboard&content_length>0&tech=php or severity=critical|severity=high&vulnerability_title=xss|vulerability_title=cve-1234-xxxx reNgine's flexibility to easily incorporate any existing open-source tools and with advanced features like configurable scan engines, parallel scans, advanced query lookup on recon results, instant notification about the scan, scheduled scans, etc, separates reNgine from any other recon frameworks. reNgine can be used for both reconnaissance and actively monitoring the targets. During the Arsenal, the developers behind reNgine will demonstrate the capabilities and new features announcements. What has changed since BHEU 2019? 1. Integration of Vulnerability Scanner 2. More powerful query lookup with recon data 3. OSINT Capabilities (Major update) 4. Scan Comparision - ability to identify the changes in subdomains, newly discovered subdomains or subdomains that disappeared in last scan etc 5. Interesting Lookup: reNgine will automatically identify the interesting subdomains and interesting URLs from recon data using the keywords match. And many more..

</details>

<details><summary><strong>WARCannon: Grep the Entire Internet for WebApp Vulnerabilities</strong> — Brad Woodward</summary>

**Track:** Web AppSec · **Event:** USA 2021  
🔗 **Link:** [https://github.com/c6fc/warcannon](https://github.com/c6fc/warcannon)  
📝 **Description:** Have you ever found a novel vulnerability in a website, framework, javascript library, or third-party integration, and wondered how many other people in the world are vulnerable, too? Have you ever wished that you could non-invasively grep the internet for a vulnerability indicator? WARCannon was built for exactly this purpose, and is fed by Common Crawl via the AWS Open Data program to allow for petabyte-scale analysis of previously-spidered websites. Security researchers and bug bounty hunters can leverage WARCannon to scale their research horizontally across the entire internet in a fast, cost-effective, and entirely non-invasive/invisible way.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Find Security Bugs</strong> — Philippe Arteau</summary>

**Track:** Code Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/find-sec-bugs/find-sec-bugs](https://github.com/find-sec-bugs/find-sec-bugs)  
📝 **Description:** Find Security Bugs is a plugin for the Java static analysis tool SpotBugs. This plugin consists of set rules that focus only on security weaknesses. It can be used by developers or security professionals to find vulnerabilities in their code. The plugin can identify weaknesses in Java web applications from 138 different bug patterns including XSS, SQL injection, XXE, template injection and many more. It can scan any JVM languages such as Kotlin, Scala and Groovy. The assessment can be done in an IDE, such as Eclipse, or IntelliJ. It can also be configured in a continuous integration environment. The most recent additions to the project include features to the IDE integration and Continuous Integration (CI). The IDE IntelliJ integration was greatly improved to have better support for alternative languages such as Kotlin. This makes it easier to scan Android applications. IDE integration is a great perspective for code audit. For developers, continuous integration is a highly sought-after configuration. A new Github Action will be presented. It provides an easy feedback for developers when integrating code to the master branch with a pull request. The Black Hat Arsenal's demonstrations will include a live code review where samples of vulnerability and practical methods will be showcased in the new IDE and CI environment.

</details>

<details><summary><strong>Scanning DNA to Detect Malicious Packages in Your Code</strong> — Carlos Avila, Franco Piergallini, Diego Espitia</summary>

**Track:** Code Assessment · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** PackageDNA is an open-source tool, free and modular tool developed in Python3, that offers developers and researchers the ability to analyze code packages from different programming languages, in search of vulnerabilities in the code, the possible manipulations or spoofing of the package ('typosquatting'), identifying suspicious files, searching for strings in the code, among other data for analysis. PackageDNA, enables threat intelligence analysis or code audits, which allow to detect attacks to the software supply chain, the vast majority of companies integrate third-party code in their developments, thus the need to have a suite such as PackageDNA that performs the analysis of all these external codes and delivers the results of the analysis in a standardized way.

</details>

<details><summary><strong>SGXRay: Automated Vulnerability Finding in SGX Enclave Application</strong> — Zhaofeng Chen, Shaobo He, Qinkun Bao, Mingshen Sun, Kang Li, Shengjian Guo</summary>

**Track:** Code Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/baiduxlab/sgxray](https://github.com/baiduxlab/sgxray)  
📝 **Description:** An automated vulnerability detection tool for Intel SGX enclave applications that identifies security bugs such as unchecked pointer dereferences, invalid memory deallocation, and TOCTOU bugs by analyzing whether developers properly handle data crossing the enclave's trusted boundary.

</details>

---
## 📱 Mobile Security
<details><summary><strong>HOOKA: Deep Dive Into ART(Android Runtime) For Dynamic Binary Analysis</strong> — Seong Hyun Song</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** Google has changed Android runtime drastically each time a new version of Android is released to optimize the performance, storage usage, and system updates of apps. The profiling data has started to be generated in the recent version of Android 10, based on the user's behavior in ART (Android Runtime). Based on the profiling data, the byte code is optimized (Profile-Guided optimization and Cloud Profile optimization) by the compiler (AOT/JIT). ART also interprets and executes different types of code (byte code, oat code, and jit code) generated by the compiler. Such complexity in the structure and the operation method makes ART difficult to understand correctly. However, since all the code of the app is interpreted and executed through ART, if the attacker understands how ART works, it is possible to steal all the information necessary to analyze the app. Therefore, in this paper, we analyze the flow and structure of how the app code is interpreted and executed by objects existing in Android 10 ART. Then, by modifying the ART based on the analysis results, we develop a framework that can steal the information in real-time, such as smali code, interface, parameters, return value, fields, and stack trace of a method that is executed dynamically. In addition, we present an easy technique to effectively analyze the app without accessing the execution code by using tools such as decompiler or disassembler. In existing debugger or hooking frameworks that dynamically analyze the apps in the Android environment, it is forcibly attached to the target analysis process, and the code is injected to read or analyze the code in the memory area while the execution code is loaded in memory. Since these methods are blocked by RASP (Runtime Application Self Protection), it takes a lot of time for attackers or analysts to bypass it and analyze the app. The method proposed in this paper, on the other hand, analyzes the app by modifying the ART (Android Runtime) itself which is responsible for loading and executing the app's execution code in memory in Android. Even if any Anti-Hooking and Anti-Debugging techniques are applied to the app, all the codes are eventually executed through ART. This allows us to dump the dynamically executed code as smali code without being detected by RASP. In addition, all runtime information (such as stack trace, args, return value, etc.) of running functions can be captured and used for the analysis. This technique is basically to redevelop ART in Android. Most similar methods that change the system modules in Android build the Android OS in debug mode. This makes such approach with the system modification more easily detectable by RASP. However, the method proposed in this presentation bypasses AVB (Android Verified Boot) and SafetyNet in the kernel, and then patch only the ART module from Stock Rom released by Google. Therefore, I present an effective method to easily analyze apps without being detected by RASP.

</details>

<details><summary><strong>Ipa-medit: Memory Search and Patch Tool for IPA Without Jailbreaking</strong> — Taichi Kotake</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/sterrasec/ipa-medit](https://github.com/sterrasec/ipa-medit)  
📝 **Description:** Ipa-medit is a memory search and patch tool for resigned ipa without jailbreaking. It was created for mobile game security testing. Memory modification is the easiest way to cheat in games, it is one of the items to be checked in the security test. There are also cheat tools that can be used casually like GameGem and iGameGuardian on iOS. However, there were no tools available for un-jailbroken device. So I made it as a security testing tool. There is an android version of the tool, apk-medit(https://github.com/aktsk/apk-medit), that I created. Many mobile games have jailbreak detection, but ipa-medit does not require jailbreaking, so memory modification can be done without bypassing the jailbreak detection. GitHub: https://github.com/aktsk/ipa-medit

</details>

<details><summary><strong>Solitude: A Privacy Analysis Tool</strong> — Dan Hastings</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/nccgroup/Solitude](https://github.com/nccgroup/Solitude)  
📝 **Description:** Solitude is an open-source privacy analysis tool that aims to help people inspect where their private data goes once it leaves their favorite mobile or web applications. Whether a curious novice or a more advanced researcher, Solitude makes the process of evaluating an app's privacy accessible for everyone. Unfortunately, privacy policies are often difficult to understand when trying to identify how your private data is being shared and whom it's being shared with. As we have seen through research, privacy policies don't always tell the complete truth of what an apps actual data collection practices are. Solitude was built to help give more transparency to users of where their private data goes. Solitude makes the process of proxying HTTP traffic and searching through HTTP traffic more straightforward. Solitude can be configured to look for any type of data that you input in a mobile or web application and reveal where that data is going. The application inspects all outbound HTTP traffic, looks for various hashes of your data and recursively decodes common encoding schemes (base64,URL).

</details>

---
## 🔍 OSINT
<details><summary><strong>New Face, Who Dis? Protecting Privacy in a World of Surveillance</strong> — Mike Kiser</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** While it has its potential benefits, facial recognition is eroding privacy and other human rights. Over the past year, several organizations have acknowledged that they have "scraped" social media and similar sites for photos to build their biometric databases, and photos intended for personal use only have now been potentially weaponized. Industry and government have ethical responsibilities to prevent this, but what if there were a way to enhance privacy for individuals without waiting for the cavalry? Adversarial technology can provide a way to protect this biometric, but it must be as easy to use as picking up their mobile device and taking a photo. Introducing "Ruse," a mobile app that seeks to use adversarial strategies to make personal photos less useful for commercial facial recognition systems while retaining a (relatively) low impact on human usefulness.

</details>

<details><summary><strong>Report Writing Is Half the Battle: Finish Your Report in Less Time and Get Back to Hacking.</strong> — Tabatha DiDomenico</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** USA 2021  
🔗 **Link:** [https://github.com/apress/from-hacking-to-report-writing](https://github.com/apress/from-hacking-to-report-writing)  
📝 **Description:** Source code and resources accompanying the book 'From Hacking to Report Writing' by Robert Svensson, providing examples and templates to help penetration testers efficiently produce professional security assessment reports.

</details>

<details><summary><strong>Scrapesy: Open Source Credential Leak and Validation Tool</strong> — Michael Giordano, Julie Smith</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** USA 2021  
🔗 **Link:** [https://github.com/mikegior/scrapesy](https://github.com/mikegior/scrapesy)  
📝 **Description:** A credential scraping and validation tool that scrapes, downloads, ingests, and parses combolists from known web sources to identify compromised accounts. It can validate discovered credentials against Active Directory or Google Workspace to detect active compromised accounts within an organization.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>All-Purpose Remote Access Trojan</strong> — David Hunt, Alex Manners</summary>

**Track:** Malware Offense · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** Pneuma is a powerful Remote Access Trojan (RAT) which is built to bring open-source command-and-control (C2) servers together. More C2 servers pop up every year, based on the new shiny languages and techniques, however this has littered the security industry and it can be difficult to tell which you should use. Pneuma is designed to give you a central agent which you can use with any C2 server you decide, giving you consistency and flexibility. It is open-source and plug-and-play, allowing you to easily connect it to the C2 of your choice.

</details>

<details><summary><strong>Automated Attack Path Planning and Validation (A2P2V)</strong> — Fukutomo Nakanishi, Jason Youzwak, Michael Hylkema, Satoshi Aoki, Subir Das</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/pentest-a2p2v/pentest-a2p2v-gui](https://github.com/pentest-a2p2v/pentest-a2p2v-gui)  
📝 **Description:** A2P2V (Automated Attack Path Planning and Validation) analyzes network vulnerabilities to automatically identify, plan, and visualize potential attack paths that adversaries could exploit in a network environment.

</details>

<details><summary><strong>Blue Pigeon: Bluetooth-Based Data Exfiltration and Proxy Tool for Red Teamers</strong> — Chia Hui Mah, Jing Loon Goh, Kang Hao Leng</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/bluepigeonproject/blue-pigeon](https://github.com/bluepigeonproject/blue-pigeon)  
📝 **Description:** Blue Pigeon is a Bluetooth-based data exfiltration and proxy tool that enables communication between a remote C2 server and a compromised host, using an Android phone as an intermediary to bypass traditional network monitoring.

</details>

<details><summary><strong>Cloud Katana</strong> — Roberto Rodriguez</summary>

**Track:** Network Attacks · **Event:** USA 2021  
🔗 **Link:** [https://github.com/Azure/Cloud-Katana](https://github.com/Azure/Cloud-Katana)  
📝 **Description:** Cloud Katana is an event-driven, serverless application built on Azure Functions that automates the execution of attack simulation steps to expedite security control research and assessment in cloud and hybrid environments.

</details>

<details><summary><strong>Cloudtopolis: Zero Infrastructure Password Cracking</strong> — Joel Gámez</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/JoelGMSec/Cloudtopolis](https://github.com/JoelGMSec/Cloudtopolis)  
📝 **Description:** Cloudtopolis is a tool that facilitates the installation and provisioning of Hashtopolis on the Google Cloud Shell platform, quickly and completely unattended (and also, free!). Together with Google Collaboratory, it allows us to break hashes without the need for dedicated hardware from any browser (even from your smartphone). Thanks to its implementation through Docker, it can be run almost anywhere in a fast and easy way. In addition, it can be used collaboratively using different accounts, being very useful for use in CTF teams or in Red Team exercises. As a novelty in this talk, automated clients for Windows and Linux (not disclosed yet) will be presented, being able to additionally use the user's local resources together with the graphic cards provided by Colab.

</details>

<details><summary><strong>Cotopaxi: IoT/IIoT/M2M Protocols Security Testing Toolkit</strong> — Jakub Botwicz</summary>

**Track:** Network Attacks · **Event:** USA 2021  
🔗 **Link:** [https://github.com/samsung/cotopaxi](https://github.com/samsung/cotopaxi)  
📝 **Description:** Cotopaxi is a set of tools for security testing of network devices using specific and general network IoT/IIoT/M2M protocols (AMQP, CoAP, DTLS, gRPC, HTTP/2, HTCPCP, KNX, mDNS, MQTT, MQTT-SN, QUIC, RTSP, SSDP).

</details>

<details><summary><strong>CQOffensiveSecurity: The Extreme Windows Offensive Security Toolkit</strong> — Paula Januszkiewicz, Mike Jankowski-Lorek</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** CQOffensiveSecurity Toolkit enables you to perform advanced Windows Infrastructure Penetration Testing. It guides you through the process of gathering intel about network, workstations and servers. Common technics for privilege escalation, antimalware avoidance and bypass, credential harvesting and lateral movement. Toolkit allows also for decrypting RSA keys and EFS protected files as well as blobs and objects protected by DPAPI and DPAPI-NG. This toolkit is commonly used among CQURE Experts and pentesters on daily basis. Among published presented tools: CQRepacker, CQSecretDumper, CQLsasSecretDumper, CQCredentialHarvester, CQSystemEscalator, CQTcbImpersonate, CQSqlTDEdecrypter and many more. During the Black Hat we would like to announce brand new tools for escalation and lateral movement for PKI and ADFS as well as disabling Azure Information Protection to search through encrypted and protected files at rest. CQOffensiveSecurity is a very practical toolkit for pentesters and RedTeamers.

</details>

<details><summary><strong>Cyber Weapon Range</strong> — Brian Sypher, Dan Wolfford, MSc, USAF (R)</summary>

**Track:** Malware Offense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/secdevops-cuse/CyberRange](https://github.com/secdevops-cuse/CyberRange)  
📝 **Description:** CyberRange is an open-source AWS-based cyber range providing a bootstrap framework for offensive, defensive, reverse engineering, and security intelligence tooling in a private research lab environment.

</details>

<details><summary><strong>InQL: Introspection GraphQL Scanner</strong> — Andrea Brancaleoni</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/doyensec/inql](https://github.com/doyensec/inql)  
📝 **Description:** InQL is an open-source toolbox for GraphQL. In addition to introspection and enumeration, our tool allows probing for GraphQL specific vulnerabilities. Over the course of the last few years, InQL became the go-to tool for GraphQL penetration testing thanks to its flexibility. InQL is suited specifically for security audits and manual penetration testing with its tight integration with Burp Suite. In addition to that, InQL also provides an easily accessible API and command-line interface that can be integrated with other “shift-left” security engineering practices. During the session, we will showcase InQL superpowers: black-box queries generation, cycles detection, CSRF helpers, and the newly integrated SQLi exploiter. Resources: - https://github.com/doyensec/inql - https://blog.doyensec.com/2018/05/17/graphql-security-overview.html - https://blog.doyensec.com/2020/03/26/graphql-scanner.html - https://blog.doyensec.com/2021/05/20/graphql-csrf.html - https://blog.doyensec.com/2020/11/19/inql-scanner-v3.html - https://blog.doyensec.com/2020/06/11/inql-scanner-v2.html

</details>

<details><summary><strong>Introducing subCrawl: A Framework for the Analysis and Clustering of Hacking Tools Found Using Open Directories</strong> — Josh Stroschein, Patrick Schläpfer</summary>

**Track:** Malware Offense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/hpthreatresearch/subcrawl](https://github.com/hpthreatresearch/subcrawl)  
📝 **Description:** From phishing kits to command-and-control panels, web shells and multiple samples of malware, open directories can provide a wealth of information into threat actor operations. But how can we discover open directories? And once we discover them, what are the next steps for identifying interesting content? To answer these questions, we created the open-source framework subCrawl. subCrawl is written in Python3 and provides a modular framework for discovering open directories, unique content through signatures and organizing the data with optional output modules, such as MISP. Open directories are simply folders that are viewable on a public web server that provides direct links to all its content. While open directories can be used to legitimately share files, they are often overlooked by threat actors. Therefore, they can provide insight into the structure, tools and malware being used by many threat actors. This oversight can provide direct access to the tools they've placed on a server, such as web shells, C2 panels or proxy scripts. To organize the data, we use our framework subCrawl to aggregate the data with fuzzy hashes, web server information, used scripting languages and more. This approach allows for the creation of signatures that can be used to track tool usage across multiple hosts and cluster threat actor activities. To help manage the hosts explored and the data collected, we create consolidated MISP events, which enables us to cluster the found artifacts and draw interesting conclusions about the use of tools. We will present the open-source framework subCrawl, which reflects our approach for hunting open directories. We will also explore our methodology to detect and cluster malicious content using publicly available threat feeds with the support of the well-known tool MISP, which helps us to store the data in a structured form and cluster it.

</details>

<details><summary><strong>Kubesploit: A Post-Exploitation Framework, Focused on Containerized Environments</strong> — Eviatar Gerzi</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/cyberark/kubesploit](https://github.com/cyberark/kubesploit)  
📝 **Description:** A cross-platform post-exploitation HTTP/2 Command & Control server and agent written in Golang, focused on containerized environments. It enables red teams to simulate real-world attacks against Docker and Kubernetes infrastructure.

</details>

<details><summary><strong>Kubestriker: A Blazing Fast Kubernetes Security Auditing Tool</strong> — Vasant Chinnipilli, Pralhad Chaskar</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/vchinnipilli/kubestriker](https://github.com/vchinnipilli/kubestriker)  
📝 **Description:** Kubestriker performs numerous in depth checks on kubernetes infrastructure to identify any misconfigurations which make organisations an easy target for attackers and safeguards against potential attacks on Kubernetes clusters.

</details>

<details><summary><strong>Lazyrecon v2.0</strong> — Kirill Zhdanov</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/capt-meelo/LazyRecon](https://github.com/capt-meelo/LazyRecon)  
📝 **Description:** Lazyrecon v2.0 is a subdomain discovery tool that discovers and resolves valid subdomains then performs SSRF/LFI/SQLi fuzzing and port scanning. It has a simple modular architecture and is optimized for speed while working with github and wayback machine.

</details>

<details><summary><strong>Merlin</strong> — Russel Van Tuyl</summary>

**Track:** Malware Offense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/Ne0nd0g/merlin](https://github.com/Ne0nd0g/merlin)  
📝 **Description:** A cross-platform post-exploitation command and control (C2) server and agent written in Go that uses HTTP/2 and other protocols to enable operators to maintain persistence and execute commands on compromised systems.

</details>

<details><summary><strong>Mushikago: IT and OT Automation Penetration Tool Using Game AI</strong> — Yuta Ikegami, Masato Hamamura</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/mushikago](https://github.com/mushikago)  
📝 **Description:** Penetration testing is an effective means of discovering vulnerabilities and inadequate settings in the overall system, and of investigating whether there are any operational security risks. However, in manual penetration testing, there are many cases where it is unclear whether the test content is really appropriate, because the diagnosis varies depending on the tester's strong and weak, interests, physical condition, and mental state on that day. Also, excellent testers are already booked by a large amount of work, and it is not always possible to request them without fail. In addition, cyber attacks on ICS (Industrial Control System) have been increasing recently, especially in 2020, when there were many cases of ransomware infections that caused damage to ICS. Furthermore, the number of reports of ICS vulnerabilities is increasing every year. In response to this situation, penetration testing for ICS has been attracting much attention. In this work, we developed Mushikago, an automatic penetration testing tool using game AI, which focuses on the verification of post-exploit among penetration tools. A post-exploit is an attack that an attacker carries out after entering the target environment. By focusing on post-exploit verification, we can understand how far an attacker can actually penetrate and what kind of information is collected. Mushikago uses the GOAP (Goal Oriented Action Planning), which is game AI commonly used in NPC (Non Player Character). To using Mushikago, we can flexibly change the content of the attack according to the environment and mimic the attacks conducted by actual APT attackers and testers. It is also possible to identify terminal information, account information, and network information without manual intervention, and visualize and report them based on MITRE ATT&CK. In addition, Mushikago supports ICS, and can be used for penetration testing across IT and OT (Operation Technology).

</details>

<details><summary><strong>NovAttack</strong> — Mustafa Altınkaynak, Recep Tiryaki</summary>

**Track:** Network Attacks · **Event:** USA 2021  
🔗 **Link:** [https://github.com/novattack/novattack.com](https://github.com/novattack/novattack.com)  
📝 **Description:** The NovAttack platform requires minimal setup time and few resources to implement. We love open source. So NovAttack is open source, it will remain open source. NovAttack simulates real cyber attacks, focusing on the following attack categories. Features / Test Capabilities - IPS / IDS / Firewall - Malware Download - Content Filtering - DLP (Data Loss Protection) - WAF (Web Application Firewall) (New) How does NovAttack work? NovAttack advocates the open source philosophy. Uses the capabilities of PHP and libraries. All communication is prepared with API. NovAttack simulates cyber attacks with its point-to-point connection. Thus, it reduces the amount of false positive. Attack vectors in it can be edited and updated. - NovAttack simulates web-based attacks. - You can provide continuous cyber attack simulation by adding current malware to NovAttack. - You can develop DLP vectors specific to your organization, such as credit card leak). NovAttack provides continuous analysis for you. - You can test your institution's content or URL filter.

</details>

<details><summary><strong>Phishmonger: Welcome to the Phish Market</strong> — Forrest Kasler</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/fkasler/phishmonger](https://github.com/fkasler/phishmonger)  
📝 **Description:** A phishing platform designed for penetration testers that enables crafting phishing emails, creating templates, scheduling campaigns, and tracking results. It provides direct SMTP control, acts as its own mail server, and offers real-time campaign monitoring through websockets.

</details>

<details><summary><strong>PyRDP: Remote Desktop Protocol Monster-in-the-Middle (MITM)</strong> — Olivier Bilodeau</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** USA 2021  
🔗 **Link:** [https://github.com/GoSecure/pyrdp](https://github.com/GoSecure/pyrdp)  
📝 **Description:** PyRDP is a Remote Desktop Protocol (RDP) monster-in-the-middle (MITM) tool and library useful in intrusion testing and malware research. Its out of the box offensive capabilities can be divided in three broad categories: client-side, MITM-side and server-side. On the client-side PyRDP can actively steal any clipboard activity, crawl mapped drives and collect all keystrokes. On the MITM-side PyRDP records everything on the wire in several formats (logs, JSON events), allows the attacker to take control of an active session and performs a pixel perfect recording of the RDP screen. On the server-side, on-logon PowerShell or cmd injection can be performed when a legitimate client connects. On the malware research side, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It can replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation or to generate IOCs. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads. Over the last year, we implemented several features that we are going to uncover in this brand-new arsenal workshop: improved file interception and crawling, dynamic certificate cloning, CredSSP/NLA support with private certificate and key, dynamic NLA redirection, NTLMSSP hash logging, and more.

</details>

<details><summary><strong>Racketeer: Prototyping Ransomware Operations</strong> — Dimitry Snezhkov</summary>

**Track:** Malware Offense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/dsnezhkov/racketeer](https://github.com/dsnezhkov/racketeer)  
📝 **Description:** A toolkit for security teams to simulate and test detection of common ransomware operations in a controlled manner against company assets and network endpoints. It uses an agent/server architecture running on Windows endpoints with cross-platform command-and-control capabilities.

</details>

<details><summary><strong>Zuthaka: Collaborative C2 Development Framework</strong> — Lucas Bonastre, Alberto Herrera Yañez</summary>

**Track:** Malware Offense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/pucarasec/zuthaka](https://github.com/pucarasec/zuthaka)  
📝 **Description:** A collaborative free open-source Command & Control development framework that allows developers to concentrate on the core function and goal of their C2. Zuthaka presents a simplified API for fast and clear integration of C2s and provides a centralized management for multiple C2 instances through a unified interface for Red Team operations.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Counterfit: Attacking Machine Learning in Blackbox Settings</strong> — Will Pearce, Raja Sekhar Rao Dheekonda</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/azure/counterfit](https://github.com/azure/counterfit)  
📝 **Description:** Counterfit is a generic automation layer for assessing the security of machine learning systems, consolidating multiple adversarial frameworks into a single tool to test ML model resilience against attacks.

</details>

<details><summary><strong>Git Wild Hunt: A Tool for Hunting Leaked Credentials</strong> — Rod Soto, Jose Hernandez</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/josehelps/git-wild-hunt](https://github.com/josehelps/git-wild-hunt)  
📝 **Description:** Git Wild Hunt is a Python tool that searches GitHub repositories for exposed credentials and secrets, leveraging GitHub's advanced search functionality with regex pattern matching to identify API keys, tokens, and private keys.

</details>

<details><summary><strong>Joern: An Interactive Shell for Code Analysis</strong> — Vickie Li, Fabian Yamaguchi, Suchakra Sharma</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/joernio/joern](https://github.com/joernio/joern)  
📝 **Description:** Joern is an award-winning open-source platform for robust query-based analysis of C/C++. It enables mining large code bases for vulnerabilities using a Scala-based domain-specific query language and provides the reference implementation for code property graphs. With its fuzzy parsing approach, it is specifically suited for machine learning applications. Joern serves as the fundament for the commercial SAST and code exploration products at ShiftLeft. The Code Property Graph (CPG) is an intermediate code representation designed for code querying. The core idea it promotes is to merge multiple different program representations into a joint graph data structure and allowing queries to be formulated as graph traversals. In its initial form as presented in 2014, the CPG makes available syntactical information, control flow information and data flow for C/C++ programs. It was later further generalized to host multiple different programming languages, and higher-level code representations. Important Links Joern Documentation: https://docs.joern.io Joern query database: https://queries.joern.io Joern Community: https://discord.gg/AUzy45EHdf Demo preparation: Download VLC v3.0.12 source and extract in a convenient directory > wget http://get.videolan.org/vlc/3.0.12/vlc-3.0.12.tar.xz > tar -xvf vlc-3.0.12.tar.xz Download Joern and install > wget https://github.com/joernio/joern/releases/latest/download/joern-install.sh > chmod +x ./joern-install.sh > sudo ./joern-install.sh

</details>

<details><summary><strong>Magpie: An Open Source CSPM Built to Scale</strong> — Mark Curphey, Jason Nichols</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/blinue/magpie](https://github.com/blinue/magpie)  
📝 **Description:** An open-source Cloud Security Posture Management (CSPM) tool designed to help organizations discover, inventory, and assess the security configuration of their cloud resources at scale.

</details>

<details><summary><strong>PingCastle: An Active Directory Auditing Tool</strong> — Vincent Le Toux</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/netwrix/pingcastle](https://github.com/netwrix/pingcastle)  
📝 **Description:** So many tools that exist to assess Active Directory security, and yet, it is impossible to have an overview of all. PingCastle has been designed to tackle these difficulties and get results fast and without any requirements. Healthcheck mode is the most well-known mode that gives vulnerability reports in minutes regarding major AD vulnerabilities. But what if the most important point was to convince the management that AD security is not that simple? PingCastle is more than a vulnerability scanner. This demo will include scanners, cartography and secret tricks.

</details>

<details><summary><strong>Principal Mapper (PMapper): A Tool for Identifying Unique AWS Account/Organization Permissions Risks</strong> — Erik Steringer</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/nccgroup/Pmapper](https://github.com/nccgroup/Pmapper)  
📝 **Description:** A security analysis tool that models IAM Users and Roles in an AWS account as a directed graph to identify privilege escalation risks and unauthorized access paths. It simulates AWS authorization behavior locally to detect when principals could gain unintended access through intermediate roles.

</details>

<details><summary><strong>remote-method-guesser: A Java RMI Vulnerability Scanner</strong> — Tobias Neitzel</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/qtc-de/remote-method-guesser](https://github.com/qtc-de/remote-method-guesser)  
📝 **Description:** remote-method-guesser (rmg) is a Java RMI vulnerability scanner that checks for common misconfigurations on Java RMI endpoints. It combines well known techniques for RMI enumeration with detection capabilities for lesser known attack vectors that are often missed. Apart from detecting RMI vulnerabilities, remote-method-guesser can perform attack operations for each supported vulnerability type. The following list shows some of it's currently supported operations: * List available bound names and their interface class names * List codebase locations (if exposed by the remote server) * Check for known vulnerabilities (enabled class loader, missing JEP290, JEP290 bypasses, localhost bypass (CVE-2019-2684)) * Identify existing remote methods by using a bruteforce (wordlist) approach * Call remote methods with user specified arguments (no manual coding required) * Call remote methods with ysoserial gadgets within the arguments * Call remote methods with a client specified codebase (remote class loading attack) * Perform DGC, registry and activator calls with ysoserial gadgets or a client specified codebase * Perform bind, rebind and unbind operations against an RMI registry * Bypass registry deserialization filters by using An Trinhs registry bypass * Enumerate the unmarshalling behavior of java.lang.String * Create Java code dynamically to invoke remote methods manually

</details>

<details><summary><strong>The WiFi Kraken Lite</strong> — Mike Spicer</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** D4rkm4tter has been obsessed with monitoring wireless networks and has built hardware to meet the challenges of scanning and testing in the most busy and client dense environments. The WiFi-Kraken Lite contends with these issues in a smaller package without sacrificing any monitoring performance. This project is the results of years of research into the most effective way to scan and audit wireless in a single box that can be easily deployed or used as a hardened terminal in the most rugged conditions. The WiFi-Kraken Lite consists of a single-board computer which connects 12 wireless radios that enables scanning and auditing WiFi, Bluetooth, LoRaWAN and other commonly used wireless protocols. The number of wireless devices is growing as well as the way those devices are being connected. Having an all-in-one wireless monitoring solution will give you the ability to track this data across these bands and give you the best picture of what's happening in the air around you. This demonstration will provide you the information so that you can build your own all-in-one monitoring device. You will also gain an overview of capture technologies including Kismet that will help you perform this type of analysis in your own environments. Finally once the data is capture, you will get an understanding of efficient data processing using tools like Wireshark and d4rkm4tter's own PCAPinator tool.

</details>

<details><summary><strong>trapfuzzer</strong> — Sili luo</summary>

**Track:** Vulnerability Assessment · **Event:** USA 2021  
🔗 **Link:** [https://github.com/hac425xxx/trapfuzzer](https://github.com/hac425xxx/trapfuzzer)  
📝 **Description:** Breakpoint mechanism based coverage-guided binary fuzzing tools for Windows and Linux platforms. Binary instrument by breakpoint, in specific scenarios, this method is faster than dynamorio. At present, more than 200 vulnerabilities have been found in WPS office, foxitpdf and other software

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Attack Surface Framework</strong> — Mauricio Espinosa, Prajwal Panchamahalkar</summary>

**Track:** Network Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/vmware-labs/attack-surface-framework](https://github.com/vmware-labs/attack-surface-framework)  
📝 **Description:** Attack Surface Framework (ASF) discovers and monitors external and internal network assets, acting as an attack surface watchdog by enumerating services, tracking changes, and executing targeted security tests through a unified web interface.

</details>

<details><summary><strong>Cloud Sniper</strong> — Nicolás Rivero Corvalán, Matías Marenchino, Santiago Friquet, Lucho Carranza Berra</summary>

**Track:** Malware Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/cloud-sniper/cloud-sniper](https://github.com/cloud-sniper/cloud-sniper)  
📝 **Description:** Cloud Sniper is a platform designed to manage Cloud Security Operations, intended to respond to security incidents by accurately analyzing and correlating cloud artifacts. It is meant to be used as a Cloud Security Operations platform to detect and remediate security incidents by showing a complete visibility of the company's cloud security posture. It introduces a centralized Incident and Response platform, which executes automatic actions, by learning from the analysts' expert knowledge. To do it, only native cloud artifacts and open source technologies are implemented. In this way, the community can extend the project with different security use cases. Cloud Sniper receives and processes security feeds, providing an automatic response mechanism to protect the cloud infrastructure. To detect attackers' advanced TTPs, Cloud Sniper Analytics module correlates IOCs providing enhanced security findings to the security analyst. With this platform, you get a complete and comprehensive management system of the security incidents. At the same time, an advanced security analyst can integrate Cloud Sniper with external forensic or incident-and-response tools to ingest new security feeds. The platform automatically deploys and provides cloud-based integration with all native resources, in a fully modularized manner, making it very easy to extend for the community. Cloud Sniper introduces an analytics module to analyze data, metrics and telemetry generated on the cloud. This first version analyzes VPC flows to detect beaconing patterns. As part of the platform, we have developed two modules to complement it: * Cloud Droid (Incident and Response Simulations): Currently, incident and response teams develop different mechanisms to detect attacks, leaving aside the testing phase. Although each automation is tested before implementation, it is not constantly monitored. Droid proposes an automated testing model in which controlled actions are expected to be triggered to perform security incident simulations. * Cloud Lusat (Internal Threat Intelligence Feeds, Inventory and Compliance Data Collection): It aims to process information based on threat intelligence feeds, generate an inventory and check the compliance of different cloud resources.

</details>

<details><summary><strong>Kraker</strong> — Ivan Iushkevich</summary>

**Track:** Cryptography · **Event:** USA 2021  
🔗 **Link:** [https://github.com/zzzteph/kraker](https://github.com/zzzteph/kraker)  
📝 **Description:** Kraker is a distributed password brute-force system that allows you to run and manage the hashcat on different servers and workstations, focused on ease of use. There were two main goals during the design and development: to create the most simple tool for distributed hash cracking and make it fault-tolerant.

</details>

<details><summary><strong>LUDA: Large URLs Dataset Analyzer for Security</strong> — Jordan Garzon, Asaf Nadler</summary>

**Track:** Network Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/akamai/luda](https://github.com/akamai/luda)  
📝 **Description:** What interesting stuff can we find by looking only at URLs without the actual HTTP traffic ? Well, quite a lot. Hackers often do not reinvent the wheel. They buy existing malwares or phishing that use the same scheme for HTTP communication. Techniques to randomize URLs , like DGA, often apply on the domain part". But what about the rest? In this talk, we present LUDA - Large URLs Dataset Analyzer for security. It works in two modes: Malware or Phishing. The first will detect similarities between C2 communication and cluster them by families. The last will apply the same clustering with an additional layer of " brand " detection. Both of them can automatically extract regexes, using Genetic algorithm, and can be deployed for inline detections. This powerful tool already supports integration with various public malicious repositories like PhishTank, URLHaus , Virus Total as well as dozens more. As opposed to similar projects , this tool is focused only on security. It includes specific options like automatic false positive cleaning. We will demo how we can run LUDA on public datasets with the two modes and show how it succeeds to get quality insights from large datasets. Finally we will show what are the current threat families found on real traffic data taken from Akamai Secure Web Gateway.

</details>

<details><summary><strong>PurpleSharp 2.0: Active Directory Attack Simulations</strong> — Mauricio Velazco</summary>

**Track:** Network Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/mvelazc0/PurpleSharp](https://github.com/mvelazc0/PurpleSharp)  
📝 **Description:** A C# adversary simulation tool that executes ATT&CK techniques to generate attack telemetry in monitored Windows environments. It enables security teams to simulate adversary techniques within Active Directory environments to test and improve detection capabilities.

</details>

<details><summary><strong>Rapid Data Exploration With Apache Drill</strong> — Charles Givre</summary>

**Track:** Data Forensics/Incident Response · **Event:** USA 2021  
🔗 **Link:** [https://github.com/cgivre/data-exploration-with-apache-drill](https://github.com/cgivre/data-exploration-with-apache-drill)  
📝 **Description:** Training materials and code for rapid data exploration using Apache Drill, a distributed SQL query engine that enables analysts to query and analyze diverse data sources using standard ANSI SQL for forensics and incident response investigations.

</details>

<details><summary><strong>REW-sploit: Dissecting Metasploit Attacks</strong> — Cesare Pizzi</summary>

**Track:** Data Forensics/Incident Response · **Event:** USA 2021  
🔗 **Link:** [https://github.com/rew-sploit/rew-sploit_docs](https://github.com/rew-sploit/rew-sploit_docs)  
📝 **Description:** Metasploit and Cobalt Strike are wildly used tool for red-teams, pen-testers and sometimes malicious actors. They deliver a lot of ready-to-use exploits facilitating work of the attacker. But who thinks about the poor blue-team members? They are left alone. It looks automation is for attackers only! But now, there is a hope: REW-sploit is a new tool with the aim to help defenders in analyzing Metasploit (and in some form Cobalt Strike) based attacks. Leveraging some well know frameworks it can emulate payloads, extracts crypto keys and correlate PCAP dumps to get extra info about what is going on. Automation is now for defenders too!

</details>

<details><summary><strong>Slips: A Machine-Learning Based, Free-Software, Network Intrusion Prevention System</strong> — Sebastian Garcia, Kamila Babayeva</summary>

**Track:** Network Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/stratosphereips/StratosphereLinuxIPS](https://github.com/stratosphereips/StratosphereLinuxIPS)  
📝 **Description:** Slips is a behavioral-based intrusion prevention system, and the first free software to use machine learning to detect attacks in the network. It is a modular system that profiles the behavior of IP addresses and performs detections in time windows. Slips' modules detect a range of attacks both to and from the protected device. Slips connects to other Slips using P2P, and exports alerts to other systems. Slips works in several directionality modes. The concept of home network is not used to choose which detection to apply, but to choose which profile to analyze. The user can choose to detect attacks coming *to* or going *from* these profiles. This makes it easy to protect your network but also to focus on infected computers inside your network. Among its modules, Slips includes the download/manage of external Threat Intelligence feed (including our laboratory's own TI feed), whois/asn/geocountry enrichment, a LSTM neural net for malicious behavior detection, port scanning detection (vertical and horizontal) on flows, long connection detection, etc. The decisions to block profiles or not are based on ensembling algorithms. The P2P module connects to other Slips to share detection alerts. Slips can read packets from the network, pcap, Suricata, Zeek, Argus and Nfdump, and can output alerts files and summaries. Having Zeek as a base tool, Slips can correctly build a sorted timeline of flows combining all Zeek logs. Slips can send alerts using the STIX/TAXII protocol. More importantly, the Kalipso Node.js interface allows the analysts to see the profiles' behaviors and detections performed by Slips modules directly in the console. Kalipso displays the flows of each profile and time window and compares those connections in charts/bars. It also summarizes the whois/asn/geocountry information for each IP that communicates with a protected device.

</details>

<details><summary><strong>tshark + ELK: Network Traffic Monitoring and Analysis</strong> — Martin Kacer</summary>

**Track:** Network Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/h21lab/tsharkvm](https://github.com/h21lab/tsharkvm)  
📝 **Description:** This project builds virtual machine for network traffic monitoring and analysis. It uses ELK (Elasticsearch, Logstash, Kibana) to process Wireshark decoded output (by using tshark -T ek ndjson output). The virtual appliance is built using vagrant, with pre-installed and pre-configured ELK stack. https://www.h21lab.com/tools/tshark-elasticsearch https://github.com/H21lab/tsharkVM

</details>

<details><summary><strong>Tsurugi Linux Project the Right DFIR Tool in the Wrong Time</strong> — Giovanni Rattaro, Marco Giorgi</summary>

**Track:** Data Forensics/Incident Response · **Event:** USA 2021  
🔗 **Link:** [https://github.com/project-tsurugi](https://github.com/project-tsurugi)  
📝 **Description:** Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools. As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident). And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes. After more than a year since the last release, a Tsurugi Linux special BLACK HAT EDITION with this major release will be shared with the participants before the public release.

</details>

<details><summary><strong>Using Dorothy to Test Okta SSO Visibility and Detection</strong> — David French</summary>

**Track:** Network Defense · **Event:** USA 2021  
🔗 **Link:** [https://github.com/elastic/dorothy](https://github.com/elastic/dorothy)  
📝 **Description:** A security testing tool that simulates attacker actions in Okta environments to help organizations evaluate their monitoring and detection capabilities. It maps simulated activities to MITRE ATT&CK tactics like persistence, defense evasion, and discovery.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>ARP Covert Channel Attacks by 8bit Microcomputer #2</strong> — Michihiro Imaoka</summary>

**Track:** Hardware/Embedded · **Event:** USA 2021  
🔗 **Link:** [https://github.com/imaoca/botchipTools](https://github.com/imaoca/botchipTools)  
📝 **Description:** Introduces a method of embedding information in the padding part of ARP and performing secret communication with only one small 8-bit microcomputer. The transmitter uses an 8-bit microcomputer called Atmega328P. A 10BASE-T Ethernet frame is generated using only the GPIO of the microcomputer without using a dedicated chip such as an Ethernet controller. By using this method, it is possible to perform a covert channel attack with a smaller and cheaper method than the conventional method.

</details>

<details><summary><strong>Capture the Signal: Running Wireless IoT CTFs, Remotely!</strong> — Federico Maggi, Marco Balduzzi, Jonathan Andersson</summary>

**Track:** Internet Of Things · Hardware/Embedded · **Event:** USA 2021  
🔗 **Link:** [https://github.com/blackvs/awesome-cts](https://github.com/blackvs/awesome-cts)  
📝 **Description:** The famous DEFCON CTF is one of the thousands Capture the Flag (CTFs) contests that, since many years, have become the "lifeblood" of the cybersecurity community. CTF players reverse-engineer vulnerable services in traditional IT applications (like web and binary) to score points. Given the increased adoption of wireless-connected devices and pervasive, interconnected networks of so-called "IoT systems," since 2018 our teams of researchers have been promoting an RF-specific version of traditional CTFs, in which contestants are asked to reverse engineer radio-based protocols as opposed to traditional network communications. We called our contest the Capture the Signal (CTS) (https://www.trendmicro.com/cts/). This activity is also known as "blind signal analysis" as the signals' specification are unknown to the attacker. Each radio signal corresponds to a challenge. The challenges are organized by difficulty levels, and each solved challenge unlocks the next one. In other words, the flag concealed in each signal represents the clue to the next radio signal (e.g., the tuning frequency or any other radio parameters). The more points are scored, the closer the contestant is to win. In normal circumstances, we've hosted the game on site at conferences world-wide, where radio signals are distributed "over the air", and participant are asked to use software-defined radio equipment to interact with the challenges. However, due the diverse local regulations in terms of wireless transmissions, we designed and implemented a containerized solution that eliminates the complexity of deploying physical radio transmitters, using an RF-over-IP broadcasting technique instead. With this framework, we can easily deploy CTS contests in countries with strict wireless regulation and remotely, backed by any cloud provider that offer container services.

</details>

<details><summary><strong>USBsamurai: One Cable To Pwn'em All</strong> — Luca Bongiorni</summary>

**Track:** Hardware/Embedded · **Event:** USA 2021  
🔗 **Link:** Not Available  
📝 **Description:** During the last years, hardware implants have become a popular attack vector in air-gapped environments such as industrial networks: Stuxnet (2010), Operation Copperfield (2017), and the recent ransomware attack that has led to a shutdown in a US natural gas facility are only some notable cases. In parallel, in an effort to raise the bar of red-teaming operations, security researchers have been designing and releasing powerful open-source devices with the intent to make Red-Teaming operations even more interesting and disruptive. Smoothing the path to new TTPs and improving old ones. As a result, hardware implants should always be included in the threat modeling of an industrial facility. During this talk, after a bit of history of hardware implants, will be presented a new hacking device: USBsamurai. A remotely-controlled USB HID injecting cable that costs less than 15 USD to produce from off-the-shelf components (a cable and a USB radio transceiver) that can be used to compromise targets remotely (i.e. over a 2.4GHz undetectable protocol) in the stealthiest way ever seen & also bypass Air-Gapped Environments like a boss! This presentation will be quite technical, tailored for an ICS security audience. Come to this talk to start preparing for the next wave of attacks that can pass undetected by most of the existing security solutions available on the market. Finally, I'll conclude the talk with practical, actionable countermeasures to prevent and detect HID attacks, and conclude by explaining how to approach a forensics analysis in presence of USB implants.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Bringing the X86 Complete RE Experience to Smart Contract</strong> — ZiQiao Kong, ChenXu Wu, KaiJern Lau</summary>

**Track:** Reverse Engineering · **Event:** USA 2021  
🔗 **Link:** [https://github.com/qilingframework/qiling](https://github.com/qilingframework/qiling)  
📝 **Description:** Currently there is more than 2 Trillion USD market cap for the crypto currency market, DeFi alone is more than 100 Billion. With the popularity of the DeFi market, smart contracts again become the playground of hackers and security researchers. Token "robbery" became the most problematic issue for both investors and crypto currency exchange. Ethereum Virtual Machine (EVM) is still the most widely used architect to support the core of smart contracts such as Polkadot, EVM and soon Cardano blockchain. Emulators built around EVM are merely good for development purposes. Most of the EVM analysis engines are just debugging tools based on symbolic execution. Unfortunately, these engines are just simple tools that do not encourage and support us to develop tools on top of them. During Black Hat Asia, Arsenal 2021, we presented "Qiling: Smart Analysis for Smart Contract" [1] and explained the foundation of Qiling's EVM engine. In Blackhat USA Arsenal 2021, we would like to take this opportunity to demonstrate the full capabilities and tools that we build on top of the Qiling's EVM engine. That brings the complete traditional X86 reverse engineering experience to the smart contract space. - Real time EVM debugger, with step into, step over and memory stack modification capabilities - Full emulation of multi cross contract instrumentation - Ultra fast emulation with pre-set environment variable - Fully automated reapply and verify latest smart contract attack to all existing contract on a exchange or chain - Make symbolic execution to work with Qiling EVM engine to provide a more in depth emulation - Added a fully functional LLVM Intermediate Representation(IR). It allow a users to build a ultra fast fuzzer on-top of Qiling Framework. To demonstrate the power of our framework and tools. We prepared some case study and demo on how we can rebuild the entire blockchain and verify the currently existing smart contract against the latest attack being discovered in the wild in the matters on few lines of code. Once the talk ends, we will release the code and tools into the Qiling github repo, as usual. References: [1] Black Hat Arsenal 2021: https://www.blackhat.com/asia-21/arsenal/schedule/index.html#qiling-smart-analysis-for-smart-contract-22643

</details>

<details><summary><strong>FileInsight-plugins: Decoding Toolbox of McAfee FileInsight Hex Editor for Malware Analysis</strong> — Nobutaka Mantani</summary>

**Track:** Reverse Engineering · **Event:** USA 2021  
🔗 **Link:** [https://github.com/nmantani/FileInsight-plugins](https://github.com/nmantani/FileInsight-plugins)  
📝 **Description:** FileInsight-plugins is a large set of plugins for McAfee FileInsight hex editor. It adds many capabilities such as decode, decryption, decompression, searching XOR-ed text strings, scanning with a YARA rule, code emulation, disassembly, and more! It is useful for various kinds of decoding tasks in malware analysis (such as extracting malware executable files from malicious document files, deobfuscation of malicious scripts). Currently, FileInsight-plugins has 110 plugins. The plugins provide the following functions and many other functions. - Calculation of hash values (CRC32, MD5, SHA1, SHA256, ssdeep, imphash, impfuzzy) - Search for XORed, bit-rotated text strings and byte arrays - XOR while incrementing / decrementing XOR key (rolling XOR) - Encode and decode of BASE16, BASE32, BASE58, BASE64, BASE85 with custom tables - Encryption and decryption (AES, ARC2, ARC4, Blowfish, ChaCha20, DES, Salsa20, TEA, Triple DES, XTEA) - Compression and decompression (aPLib, Bzip2, Deflate, Gzip, LZ4, LZMA, LZNT1, LZO, PPMd, QuickLZ, XZ, Zstandard) - Detection of embedded files in a file - Extraction of text strings of ASCII and UTF-16 with auto decode of hex string and BASE64 strings - Scanning with YARA and highlighting regions that match YARA rules - Showing file metadata - Parsing file structure (Gzip, RAR, ZIP, ELF, PE, MBR partition table, BMP, GIF, JPEG, PNG, Windows shortcut) - Code emulation of shellcodes and executable files (Windows (x64, x86) and Linux (x64, x86, ARM, ARM64, MIPS)) with API call tracing and capturing memory dumps - Disassembly (x64, x86, ARM, ARM64, MIPS, PowerPC, PowerPC64, SPARC) - Opening data with other tools such as CyberChef, IDA, and VSCode (customizable with JSON config file). - Visualization (Bitmap, Byte histogram, Entropy graph) FileInsight-plugins is a tool that I develop privately, not professionally developed by the organization I belong to. Links: - GitHub repository: https://github.com/nmantani/FileInsight-plugins/ - Documents of use cases: https://github.com/nmantani/FileInsight-plugins/wiki

</details>

<details><summary><strong>Packet Sender</strong> — Dan Nagle</summary>

**Track:** Reverse Engineering · **Event:** USA 2021  
🔗 **Link:** [https://github.com/dannagle/PacketSender](https://github.com/dannagle/PacketSender)  
📝 **Description:** Packet Sender is a free open-source (GPLv2) cross-platform (Windows, Mac, Linux) tool used daily by security researchers, college students, and professional developers to troubleshoot and reverse engineer network-based devices. Its core features are crafting and listening for UDP, TCP, and SSL/TLS packets via IPv4 or IPv6. It can listen simultaneously on any number of ports while sending to any UDP, TCP, SSL/TLS packet server. Many deliberate design features help Packet Sender's success: It can send and reply; it supports IPv4, IPv6, general, or IP-specific binding; it can run completely portable (for thumb drives); it can operate entirely in userland; it has very few build dependencies (to be able to support nearly all the Linux distros); and it has a very responsive and easy to use GUI with good defaults and ASCII/HEX translator to immediately send/receive packets within seconds of first launching.

</details>

<details><summary><strong>ParseAndC: A Universal Parser and Data Visualization Tool for Security Testing</strong> — Parbati Kumar Manna</summary>

**Track:** Reverse Engineering · **Event:** USA 2021  
🔗 **Link:** [https://github.com/intel/parseandc](https://github.com/intel/parseandc)  
📝 **Description:** A Python-based tool that parses C structure and variable declarations, then maps them onto binary data files to visualize how data is organized in memory. It provides both a GUI for interactive exploration and a batch mode for automated analysis.

</details>

<details><summary><strong>Play with Fire: Uncovering Fairplay DRM and Obfuscation for Fun and Profit</strong> — Junzhi Lu, Xindi Wang, Ju Zhu</summary>

**Track:** Reverse Engineering · **Event:** USA 2021  
🔗 **Link:** [https://github.com/Axinom/drm-fairplay-integration-sample](https://github.com/Axinom/drm-fairplay-integration-sample)  
📝 **Description:** Apple has introduced Fairplay DRM into App Store apps since 2013. For a long time before, a jailbroken IOS device is necessary for decrypting DRM protected app, which brings many problems for security researchers and malware analysts. And Apple's property DRM implementation and other components are highly protected with LLVM-based obfuscation, the lack of review and research may also leaves the vulnerability lasting. With the release of highly iOS-similar Apple Silicon device, we are able to explore more secrets of hardware and software on Apple platforms. My work will cover on three parts: firstly, how Fairplay DRM works and how to make a DRM decryption system on M1 Mac without breaking the system; secondly, possible attack surface of FairplayIOKit; and lastly, what methods Apple uses to obfuscate their property software and attack the weakness.

</details>

<details><summary><strong>Tracee: Linux Runtime Security and Forensics Using eBPF</strong> — Yaniv Agman, Roi Kol</summary>

**Track:** Reverse Engineering · **Event:** USA 2021  
🔗 **Link:** [https://github.com/aquasecurity/tracee](https://github.com/aquasecurity/tracee)  
📝 **Description:** Tracee is a runtime security and forensics tool for Linux. It is composed of tracee-ebpf, which collects OS events, and tracee-rules, which is the runtime security detection engine. Tracee-ebpf is capable of tracing all processes in the system or a group of processes according to some given filters. The set of events to trace can be selected by the user and include the following: 1. System calls 2. LSM hooks (security_file_open, security_bprm_check, cap_capable, ...) 3. Internal kernel functions (vfs_write, commit_creds, ...) 4. Special events and alerts (magic_write, mem_prot_alert, ...) Other than tracing, Tracee-ebpf is also capable of capturing files written to disk or memory (e.g. "fileless" malwares), and extracting binaries that are dynamically loaded to an application's memory (e.g. when a malware uses a packer). Using these capabilities, it is possible to automatically collect forensic artifacts for later investigation. Tracee-Rules, is a rule engine that helps you detect suspicious behavioral patterns in streams of events. It is primarily made to leverage events collected with Tracee-eBPF into a Runtime Security solution. Tracee supports authoring rules in Golang or in Rego.

</details>

---
