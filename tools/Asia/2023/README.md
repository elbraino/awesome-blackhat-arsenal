# Asia 2023
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2023** event held in **Asia**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [⚙️ Miscellaneous / Lab Tools](#⚙️-miscellaneous-lab-tools)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🧠 Social Engineering / General
<details><summary><strong>AiCEF: An AI-powered Cyber Exercise Content Generation Framework</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Constantinos Patsakis](https://img.shields.io/badge/Constantinos%20Patsakis-informational) ![Alexandros Zacharis](https://img.shields.io/badge/Alexandros%20Zacharis-informational) ![Razvan Gavrila](https://img.shields.io/badge/Razvan%20Gavrila-informational)

🔗 **Link:** Not Available  
📝 **Description:** The core idea of AiCEF, is to harness the intelligence that is available from online and MISP reports, as well as threat groups' activities, arsenal etc., from, e.g., MITRE, to create relevant and timely cybersecurity exercises. To this end, we have developed a specialised ontology called Cyber Exercise Scenario Ontology (CESO), which extends STIX [2]. The core idea is to map reports; both from online resources and MISP, via a common ontology to graphs. This way, we abstract the events from the reports in a machine-readable form. The produced graphs can be infused with additional intelligence, e.g. the threat actor profile from MITRE, also mapped in our ontology. While this may fill gaps that would be missing from a report, one can also manipulate the graph to create custom and unique models. Finally, we exploit transformer-based language models like GPT to convert the graph into text that can serve as the scenario of a cybersecurity exercise.
We have tested and validated AiCEF with a group of experts in cybersecurity exercises, and the results clearly show that AiCEF significantly augments the capabilities in creating timely and relevant cybersecurity exercises in terms of both quality and time.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>APKHunt | OWASP MASVS Static Analyzer</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Sumit Kalaria](https://img.shields.io/badge/Sumit%20Kalaria-informational) ![Mrunal Chawda](https://img.shields.io/badge/Mrunal%20Chawda-informational)

🔗 **Link:** [APKHunt | OWASP MASVS Static Analyzer](https://github.com/Cyber-Buddy/APKHunt)  
📝 **Description:** APKHunt is a comprehensive static code analysis tool for Android apps that is based on the OWASP MASVAS framework. The OWASP MASVS (Mobile Application Security Verification Standard) is the industry standard for mobile app security. APKHunt is intended primarily for mobile app developers and security testers, but it can be used by anyone to identify and address potential security vulnerabilities in their code.

With APKHunt, mobile software architects or developers can conduct thorough code reviews to ensure the security and integrity of their mobile applications, while security testers can use the tool to confirm the completeness and consistency of their test results. Whether you're a developer looking to build secure apps or an infosec tester charged with ensuring their security, APKHunt can be an invaluable resource for your work.

Key features of APKHunt:
- Scan coverage: Covers most of the SAST (Static Application Security Testing) related test cases of the OWASP MASVS framework.
- Optimised scanning: Specific rules are designed to check for particular security sinks, resulting in an almost accurate scanning process.
- Low false-positive rate: Designed to pinpoint and highlight the exact location of potential vulnerabilities in the source code.
- Output format: Results are provided in a TXT file format for easy readability for end-users.

Current Limitation:
- Supporting OS/Language: Capable of scanning the source code of an android APK file and is only supported on Linux environments.

Upcoming Features:
- Scanning of multiple APK files at the same time
- More output format such as HTML
- Integration with third-party tools

</details>

<details><summary><strong>SCodeScanner (SourceCodeScanner)</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Utkarsh Agrawal](https://img.shields.io/badge/Utkarsh%20Agrawal-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Backdoor Pony: Evaluating Backdoor Attacks and Defenses in Different Domains</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Stefanos Koffas](https://img.shields.io/badge/Stefanos%20Koffas-informational)

🔗 **Link:** Not Available  
📝 **Description:** Outsourced training and crowdsourced datasets lead to a new threat for deep
learning models: the backdoor attack. In this attack, the adversary inserts a
secret functionality in a model, activated through malicious inputs. Backdoor
attacks represent an active research area due to diverse settings where they
represent a real threat. Still, there is no framework to evaluate existing
attacks and defenses in different domains. Only a few toolboxes have been
implemented, but most of them focus on computer vision and are difficult
to use. To bridge this gap, we present Backdoor Pony, a framework for
evaluating attacks and defenses in different domains through a user-friendly
GUI.

</details>

<details><summary><strong>CQ PrivilegeEscalation Toolkit: Effective Tools for Windows Privilege Escalation Gamers</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Paula Januszkiewicz](https://img.shields.io/badge/Paula%20Januszkiewicz-informational) ![Mike Jankowski-Lorek](https://img.shields.io/badge/Mike%20Jankowski-Lorek-informational)

🔗 **Link:** Not Available  
📝 **Description:** CQURE PE Toolkit is focused on Windows Privilege Escalation tactics and techniques created to help to improve every privilege escalation game. This toolkit guides you through the process of exploiting a bug or design flaw in an operating system or software to gain elevated privileges to resources that are normally highly protected. Once you know what to look for and what to ignore, Privilege Escalation will become so much easier. This powerful toolkit is tremendously useful for those who are interested in penetration testing and professionals engaged in pen-testing who work in the areas of databases, systems, networks, or application administration.

</details>

<details><summary><strong>GodPotato: As Long as You Have the ImpersonatePrivilege Permission, Then You are the SYSTEM!</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![yichen zhang](https://img.shields.io/badge/yichen%20zhang-informational) ![Linhong Cao](https://img.shields.io/badge/Linhong%20Cao-informational)

🔗 **Link:** Not Available  
📝 **Description:** Based on the history of Potato privilege escalation for 6 years, from the beginning of RottenPotato to the end of JuicyPotatoNG, I discovered a new technology by researching DCOM, which enables privilege escalation in Windows 2012 - Windows 2022, now as long as you have "ImpersonatePrivilege" permission. Then you are "NT AUTHORITY\SYSTEM", usually WEB services and database services have "ImpersonatePrivilege" permissions.



Potato privilege escalation is usually used when we obtain WEB/database privileges. We can elevate a service user with low privileges to "NT AUTHORITY\SYSTEM" privileges.
However, the historical Potato has no way to run on the latest Windows system. When I was researching DCOM, I found a new method that can perform privilege escalation. There are some defects in rpcss when dealing with oxid, and rpcss is a service that must be opened by the system. , so it can run on almost any Windows OS, I named it GodPotato

</details>

<details><summary><strong>Interactive Kubernetes Security Learning Playground - Kubernetes Goat</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Madhu Akula](https://img.shields.io/badge/Madhu%20Akula-informational)

🔗 **Link:** [Interactive Kubernetes Security Learning Playground - Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat)  
📝 **Description:** Kubernetes Goat is an interactive Kubernetes security learning playground. It has intentionally vulnerable by design scenarios to showcase the common misconfigurations, real-world vulnerabilities, and security issues in Kubernetes clusters, containers, and cloud native environments.

It's tough to learn and understand Kubernetes security safely, practically, and efficiently. So here we come to solve this problem not only for security researchers but also to showcase how we can leverage it for attackers, defenders, developers, DevOps teams, and anyone interested in learning Kubernetes security. We are also helping products & vendors to showcase their product or tool's effectiveness by using these playground scenarios and also help them to use this to educate their customers and organizations. This project is a place to share knowledge with the community in well-documented quality content in hands-on scenario approaches.

</details>

<details><summary><strong>KernelGoat</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Shivankar Madaan](https://img.shields.io/badge/Shivankar%20Madaan-informational)

🔗 **Link:** [KernelGoat](https://github.com/Rnalter/KernelGoat)  
📝 **Description:** "KernelGoat is a 'Vulnerable by Design' Linux kernel environment to learn and practice Kernel security issues"

</details>

<details><summary><strong>Mr.SIP: The Ultimate SIP-Based Penetration Testing Tool for VoIP Systems</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ismail Melih Tas](https://img.shields.io/badge/Ismail%20Melih%20Tas-informational) ![Neslisah Topcu](https://img.shields.io/badge/Neslisah%20Topcu-informational)

🔗 **Link:** Not Available  
📝 **Description:** Mr.SIP is a cutting-edge penetration testing tool designed specifically for VoIP systems. It is the most advanced and comprehensive offensive security tool available in the market for VoIP systems. Developed to assist security experts and system administrators in assessing the security of their VoIP systems and evaluating potential risks, Mr.SIP Pro offers a wide range of features to aid in this process.

Mr.SIP Pro enables users to discover VoIP servers and active users on the network, intercept and manipulate call data, crack user passwords, and identify and report on security vulnerabilities, exploits, and misconfigurations. It also provides a framework for creating advanced, stateful attack scenarios, such as stateful TDoS (Telephony Denial of Service) attacks. Additionally, it allows users to test the server's protocol stack for undiscovered zero-day vulnerabilities by sending irregular messages. With Mr.SIP Pro, security experts and system administrators can have complete visibility and control over their VoIP systems, enabling them to proactively identify and mitigate potential threats.

</details>

<details><summary><strong>Osiris-Framework: A Scalable Tool for Penetration Testing and Vulnerability Assessment on Cross-Platform Systems</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Luis Eduardo Jacome Valencia](https://img.shields.io/badge/Luis%20Eduardo%20Jacome%20Valencia-informational) ![Samir Sanchez Garnica](https://img.shields.io/badge/Samir%20Sanchez%20Garnica-informational)

🔗 **Link:** Not Available  
📝 **Description:** Abstract—Osiris-Framework V1.337 is an open-source project designed to assist security researchers in penetration testing and vulnerability assessment exercises through unique features such as 0-days and helpers, custom-made modules, and the ability to provide valuable information about vulnerabilities in a specific target. Additionally, the framework can be executed in multi-platform systems which allows security researchers to perform audits from geographically widespread locations.

</details>

<details><summary><strong>Remove-Signature</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yuya Chudo](https://img.shields.io/badge/Yuya%20Chudo-informational)

🔗 **Link:** Not Available  
📝 **Description:** Remove-Signature is a tool designed to automate the process of generating a payload that can bypass anti-virus detection.

During red team testing, red team operators often need to prepare a payload that will not be detected by anti-virus software in order to be successful. One way to do this is to identify where the signatures used by anti-virus software are located in the payload, and then modifies bytes of the locations so that the modified payload will not be detected as malicious. This process can be time-consuming.

Remove-Signature aims to automate this process by identifying the signatures in the payload, and modifying a single byte of the signatures location in a way that will bypass anti-virus detection, while still maintaining the functionality of the payload. The tool understands the PE file format and only makes modifications that will not affect the payload's functionality. Unlike other existing tools that can only identify signatures, Remove-Signature is able to automatically generate a modified payload that can evade anti-virus detection.

The use of Remove-Signature can help to reduce the workload of red team operators and allow them to focus on other aspects of the red team engagement.

</details>

<details><summary><strong>SharpToken: Windows Token Stealing Expert</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![yichen zhang](https://img.shields.io/badge/yichen%20zhang-informational)

🔗 **Link:** Not Available  
📝 **Description:** During red team lateral movement, we often need to steal the permissions of other users. Under the defense of modern EDR, it is difficult for us to use Mimikatz to obtain other user permissions, and if the target user has no process alive, we have no way to use "OpenProcessToken" to steal Token.


SharpToken is a tool for exploiting Token leaks. It can find leaked Tokens from all processes in the system and use them. If you are a low-privileged service user, you can even use it to upgrade to "NT AUTHORITY\SYSTEM" privileges, and you can switch to the target user's desktop to do more without the target user's password. ..

</details>

<details><summary><strong>tty2web</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Vlatko Kosturjak](https://img.shields.io/badge/Vlatko%20Kosturjak-informational)

🔗 **Link:** [tty2web](https://github.com/kost/tty2web/blob/master/LICENSE)  
📝 **Description:** tty2web can take any console program and convert it into a web application. It provides a proper console for your shell needs directly inside your browser, which means programs like vim, mc, or any program that needs tty will work as expected by default. Features include support for both bind and reverse mode, which is useful for penetration testing and NAT traversal, bidirectional file transfer, reverse SOCKS 5 functionality by emulating the regeorg interface, and API support for executing commands (imagine having a RESTful interface to your operating system shell). It supports collaboration and sharing between teams, is multiplatform, and runs well on Unix/Linux-based OSs running container payloads. It is based on gotty but has been heavily improved for security and penetration tester needs.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Build Your Own Reconnaissance System with Osmedeus Workflow Engine</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ai Ho](https://img.shields.io/badge/Ai%20Ho-informational)

🔗 **Link:** [Build Your Own Reconnaissance System with Osmedeus Workflow Engine](https://github.com/j3ssie/osmedeus)  
📝 **Description:** Osmedeus is a is a workflow framework designed to perform reconnaissance, with a focus on identifying the attack surface and conducting security testing on the specified target, including vulnerability scanning, port scanning, and content discovery

</details>

<details><summary><strong>GCPGoat : A Damn Vulnerable GCP Infrastructure</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Shantanu Kale](https://img.shields.io/badge/Shantanu%20Kale-informational) ![Rishappreet Singh Moonga](https://img.shields.io/badge/Rishappreet%20Singh%20Moonga-informational) ![Ravi Verma](https://img.shields.io/badge/Ravi%20Verma-informational) ![Govind Krishna](https://img.shields.io/badge/Govind%20Krishna-informational)

🔗 **Link:** Not Available  
📝 **Description:** GCPGoat is a vulnerable by design infrastructure on GCP featuring the latest released OWASP Top 10 web application security risks (2021) and other misconfiguration based on services such as IAM, Storage Bucket, Cloud Functions and Compute Engine. GCPGoat mimics real-world infrastructure but with added vulnerabilities. It features multiple escalation paths and is focused on a black-box approach.

</details>

<details><summary><strong>Gerobug: Open-Source Private (Self-Managed) Bug Bounty Platform</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Billy Sudarsono](https://img.shields.io/badge/Billy%20Sudarsono-informational) ![Felix Alexander](https://img.shields.io/badge/Felix%20Alexander-informational) ![Jessica Geofanie Ganadhi](https://img.shields.io/badge/Jessica%20Geofanie%20Ganadhi-informational) ![Yohan Muliono](https://img.shields.io/badge/Yohan%20Muliono-informational)

🔗 **Link:** Not Available  
📝 **Description:** Are you a company, planning to have your own bug bounty program, with minimum budget? We got you!

We are aware that some organizations have had difficulty establishing their own bug bounty program.
If you know what you're doing, using a third-party managed platform usually comes with a hefty price tag and increased security concerns.
However, creating your own independently run platform will take time and effort.

GEROBUG FEATURES:
Homepage
This should be the only page accessible by public, which contains Rules and Guidelines for your bug bounty program.

Email Parser
Bug Hunter will submit their findings by email, which Gerobug will parse, filter, and show them on dashboard.

Auto Reply and Notification
Bug Hunter's inquiries will be automatically replied and notified if there any updates on their report.
Company will also be notified via Slack if there any new report.

Report Management
Manage reports easily using a kanban model.

Report Filtering and Flagging
Reports from Bug Hunter will be filtered and flagged if there are duplicate indication.

Email Blacklisting
Gerobug can temporarily block and release emails that conducted spam activity

Auto Generate Certificate
We can generate certificate of appreciations for bug hunters so you don't have to ;)

Hall of Fame / Wall of fame / Leaderboard
Yeah we have it too

</details>

<details><summary><strong>N3XT G3N WAF 2.0</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Pengfei Yu](https://img.shields.io/badge/Pengfei%20Yu-informational) ![Bosen Zhang](https://img.shields.io/badge/Bosen%20Zhang-informational)

🔗 **Link:** Not Available  
📝 **Description:** Previously, we introduced N3XT G3N WAF (NGWAF) 1.0 at BHUSA 2022. The novel WAF 3.0 tool that seeks to relieve complex and difficult WAF detection mechanism with detection utilising a Sequential Neural Network (SNN) and traps attackers through a custom honeypotted environment. These assets are all dockerised for scalability.

However, further experiments have proven that a SNN may not be the most optimal when it comes down to contextualised defence as it processes information in a step by step and sequential manner. It gets relatively cumbersome and ineffective detecting chained or contexualised attacks. Both of which are extremely common in today's attacks.

Thus, we took another approach by swapping out our "brains". We revamped the SNN and went with a Recurrent Neural Network (RNN). The RNN is a much better choice for contextualised defense as the output of each layer is fed back as the input of the same layer. Thus, this allows the network to maintain a "memory" of the data it has processed. Our latest model is a RNN with a bi-directional LSTM module, it has an accuracy of 0.995 and a f1 score of 0.993.

We have also upgraded NGWAF's scalability in model deployment, model maintenance and the overall detection pipeline. This is all done with cloudifying the operations of the entire Machine Learning detection module. As compared to version 1.0 where users have to install and run the entire framework on their local system, NGWAF 2.0 has employed Infrastructure-as-Code (IaC) scripts, which auto-deploys the machine learning model's training & maintenance pipeline onto AWS resources (Sagemaker). The detection module has also been shifted from local deployment to AWS Sagemaker where we are able to standardise the hardware utilised for the ML model. This also allows further decoupling of the detection module from the rest of the system and allow for greater customisability.

BHUSA 2022 - Version 01: (https://www.blackhat.com/us-22/arsenal/schedule/index.html#nxt-gn-waf-ml-based-waf-with-retraining-and-detainment-through-honeypots-26609)

</details>

<details><summary><strong>reNgine: An Open-Source Automated Reconnaissance/Attack Surface Management tool</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Yogesh Ojha](https://img.shields.io/badge/Yogesh%20Ojha-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>CANalyse 2.0 : A Vehicle Network Analysis and Attack Tool</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Kartheek Lade](https://img.shields.io/badge/Kartheek%20Lade-informational)

🔗 **Link:** [CANalyse 2.0 : A Vehicle Network Analysis and Attack Tool](https://github.com/canalyse/CANalyse-2.0)  
📝 **Description:** CANalyse is a software tool built to analyse the log files in a creative powerful way to find out unique data sets automatically and inject the refined payload back into vehicle network. It can also connect to simple interfaces such as Telegram for remote control. Basically, while using this tool you can provide your bot-ID and be able to use the tool's inbuilt IDE over the internet through telegram.

CANalyse uses python-can library to sniff vehicle network packets and analyse the gathered information and uses the analysed information to command & control certain functions of the vehicle. CANalyse can be installed inside a raspberry-PI, to exploit the vehicle through a telegram bot by recording and analysing the vehicle network.

</details>

<details><summary><strong>ICS Forensics Tool</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Ori Perez](https://img.shields.io/badge/Ori%20Perez-informational) ![yogev shitrit](https://img.shields.io/badge/yogev%20shitrit-informational)

🔗 **Link:** Not Available  
📝 **Description:** ICS Forensics Tools is an open source forensic toolkit for analyzing Industrial PLC metadata and project files. Microsoft ICS Forensics Tools enables investigators to identify suspicious artifacts on ICS environment for detection of compromised devices during incident response or manual check. ICS Forensics Tools is open source, which allows investigators to verify the actions of the tool or customize it to specific needs, currently support Siemens S7.

</details>

---
## Others
<details><summary><strong>canTot: A CAN Bus Hacking Framework for Car Hacking</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Jay Turla](https://img.shields.io/badge/Jay%20Turla-informational)

🔗 **Link:** [canTot: A CAN Bus Hacking Framework for Car Hacking](https://github.com/shipcod3/canTot)  
📝 **Description:** canTot is a CAN Bus hacking framework that focuses on known CAN Bus vulnerabilities or fun CAN Bus hacks. It is a Python-based CLI framework based on sploitkit and is easy to use because it is similar to working with Metasploit. It can also be used as a guide for pentesting vehicles and learning python for Car Hacking the easier way. This is not to reinvent the wheel of known CAN fuzzers, car exploration tools like caring caribou, or other great CAN analyzers out there. But to combine all the known vulnerabilities and fun CAN bus hacks in automotive security.

</details>

<details><summary><strong>Elkeid -- Open-sourced Cloud Workload Protection Platform</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Enzhe Lu](https://img.shields.io/badge/Enzhe%20Lu-informational) ![Yue Chen](https://img.shields.io/badge/Yue%20Chen-informational) ![Alkene Pan](https://img.shields.io/badge/Alkene%20Pan-informational) ![Pengbo Yao](https://img.shields.io/badge/Pengbo%20Yao-informational)

🔗 **Link:** Not Available  
📝 **Description:** Ekeid is an open-source solution that is derived from ByteDance's internal best practices, which can meet the security requirements of various workloads such as hosts, containers, container clusters, and Serverless. With the unified design and integration of HIDS, Container Security, RASP, and K8S auditions all into one platform to meet the complex security requirements of different workload capacities in the current industry. At the same time, it can also implement multi-component capability association. The most valuable part is that each component of Elkeid has passed ByteDance's massive data and years of practical testing.

</details>

<details><summary><strong>Introducing the Operating System for Automotive Security Testing: A Hands-on Demonstration</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![RAVI RAJPUT](https://img.shields.io/badge/RAVI%20RAJPUT-informational)

🔗 **Link:** [Introducing the Operating System for Automotive Security Testing: A Hands-on Demonstration](https://github.com/MinghuiChen43/awesome-trustworthy-deep-learning/blob/master/FULL_LIST.md)  
📝 **Description:** Automotive security is a critical concern as vehicles become more connected and autonomous. To ensure the security of these systems, specialized operating systems are needed for testing and evaluating their vulnerabilities.

Our presentation introduces a new operating system for automotive security testing, designed specifically for this purpose. This operating system includes a range of tools and features that are essential for testing the security of automotive systems, such as support for different communication protocols and hardware interfaces. In particular, it includes tools for testing BLE, WiFi, and automotive ethernet, as well as a CAN testing setup.

In addition to these features, the operating system includes automation tools and a test lab to allow attendees to practice and apply their knowledge. This makes it an ideal platform for hands-on learning and experimentation.

By using this operating system, attendees will be able to test the security of their automotive systems and identify potential vulnerabilities. They will also gain practical experience in using the tools and techniques needed to secure these systems and prevent attacks.

Overall, our presentation provides a valuable resource for anyone interested in securing the increasingly complex and connected systems found in modern vehicles. By understanding the capabilities and limitations of this operating system, attendees will be better equipped to secure their own automotive systems and prevent vulnerabilities.

</details>

<details><summary><strong>MemTracer: Hunting for Forensic Artifacts in Memory</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![May Alsaif](https://img.shields.io/badge/May%20Alsaif-informational)

🔗 **Link:** Not Available  
📝 **Description:** MemTracer is a tool that offers live memory analysis capabilities, allowing digital forensic practitioners to discover and investigate stealthy attack traces hidden in memory.
Advanced persistence threat (APT) adversaries use stealthy attack tactics that only leave volatile short-lived memory evidence. The reflective Dynamic-Link Library (DLL) load technique is considered one of the stealthiest attack techniques. Reflective DLL load allows adversaries to load malicious code directly into memory, rather than loading a file from the disk. Thus, reflective
DLL load leaves no digital evidence present on the disk. The malicious DLL continues to execute as long as the compromised process is running. Terminating a compromised process leads to the removal of the malicious DLL from memory, and the release of the memory region back to the pool for reallocation. Therefore, memory needs to be examined periodically in order to detect the existence of a malicious DLL that loaded reflectively into memory.
Loading DLL reflectively produces an unusual memory region's characteristics that can indicate its existence. The MemTracer tool was developed to efficiently scan memory regions to detect reflective DLL loading symptoms. Mainly, MemTracer aims to detect native .NET framework DLLs that are loaded reflectively. Additionally, MemTracer provides the ability to search for a specific loaded DLL by name, which can retrieve the list of processes that have abnormally loaded the specified module for further investigation.

</details>

<details><summary><strong>PoC Attack Against Flying Drone</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Kelvin Wong](https://img.shields.io/badge/Kelvin%20Wong-informational)

🔗 **Link:** [PoC Attack Against Flying Drone](https://github.com/lidq92/arxiv-daily)  
📝 **Description:** Advancements in UAV technology are opening new opportunities and applications in various fields of life. However, these advancements are also causing new challenges in terms of security, adaptability, and consistency. Especially the small drones are even suffering from architectural issues and the definition of security and safety issues.


Most of the UAS system are using 2.4 or 5.8Ghz for remote connection and video transmission. Counter UAS units always purchase very expensive anti-drone or detection system, eg drone gun. To review the applicability, our team developed an open-source hand crafted device to achieve the task. During the demonstration, DJI smart drone and some custom-made FPV drone will be the target of the attack

</details>

<details><summary><strong>Prediction System for Lateral Movement Based on ATT&CK Using Sysmon</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Yukihiro Kozai](https://img.shields.io/badge/Yukihiro%20Kozai-informational) ![Koki Watarai](https://img.shields.io/badge/Koki%20Watarai-informational) ![Takuho Mitsunaga](https://img.shields.io/badge/Takuho%20Mitsunaga-informational)

🔗 **Link:** [Prediction System for Lateral Movement Based on ATT&CK Using Sysmon](https://github.com/LeThiHongMinh/MITRE-review-papers)  
📝 **Description:** This tool converts Windows logs collected by Sysmon into MITER ATT&CK Technique and allows us to refer to attack types and progress based on the ATT&CK structure.
In a company network, when we detect that a device has been infected with malware, it is not easy to find other infected devices, and we consume a lot of human resources and time. With this tool, we can grasp the possibility of infection to other devices and the progress of attack using ATT&CK and statistical methods based on the Sysmon log.
Furthermore, this tool automatically converts aggregated Sysmon logs into ATT&CK Technique using Atomic Red Team's library. The converted information is visualized in a list format or colored in the ATT&CK Matrix.
It is beneficial when significant and chaotic logs can be transformed into a clear cybersecurity knowledge base format in a few moments. The tool is also helpful for real-world anomaly detection and cybersecurity learning.
We will provide this tool as a Web application and publish its source code on GitHub.

</details>

<details><summary><strong>Purple Knight</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Jacqueline Young](https://img.shields.io/badge/Jacqueline%20Young-informational)

🔗 **Link:** [Purple Knight](https://github.com/IBM/db2-jupyter/blob/master/Db2_11.1_Features/generate_json.ipynb)  
📝 **Description:** Business applications on-premises and in the cloud rely on Active Directory (AD) and Azure Active Directory for authentication, making it a critical piece of IT infrastructure. But securing Active Directory is difficult given its constant flux, its sheer number of settings, and the increasingly sophisticated threat landscape. This creates potential exploitable Indicators of Exposure in AD, and if you have or had a bad actor in your AD you will want to understand the Indicators of Compromise (IOCs) which is the evidence an attacker is there. In this session, we will talk about the Purple Knight freeware tool by Semperis which helps organizations understand the security posture of their hybrid Active Directory as it pertains to IOEs and IOCs.

</details>

<details><summary><strong>RTHunter:the High-Accuracy Reverse Symbol Recovery and Vulnerability Scanning Tool</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Minghang Shen](https://img.shields.io/badge/Minghang%20Shen-informational) ![Chaoyang Lin](https://img.shields.io/badge/Chaoyang%20Lin-informational) ![Minghao Lin](https://img.shields.io/badge/Minghao%20Lin-informational) ![Qi Fan](https://img.shields.io/badge/Qi%20Fan-informational)

🔗 **Link:** [RTHunter:the High-Accuracy Reverse Symbol Recovery and Vulnerability Scanning Tool](https://github.com/MinghaoLin2000/MinghaoLin2000.github.io/blob/master/index.md)  
📝 **Description:** RTOS (Real-Time Operating Systems) are widely used in critical fields such as aerospace, transportation, communication infrastructure, medical devices, oil industry, and industrial robots due to their reliability and stability. However, the real-time nature of RTOS makes the analysis threshold high, resulting in limited security research tools compared to time-sharing operating systems.


RTHunter is an efficient RTOS reverse symbol recovery and vulnerability scanning tool. It collects a large number of RTOS projects and mainstream network framework projects in multiple versions, builds a firmware resource library covering dozens of mainstream RTOS systems, and builds thousands of function features and historical vulnerability function features through trace-based information methods. And by solving the slow recognition speed and accuracy problem of bindiff through trace-based fuzzy feature matching method. RTHunter can achieve more than 50% recognition accuracy on mainstream RTOS routers, and has found supply chain vulnerabilities affecting multiple brands and dozens of RTOS devices through recorded vulnerability features. RTHunter can also use personal reverse information to fill the entire database and form a custom efficient tool.

</details>

<details><summary><strong>ThreatSeeker - Threat Hunting via Windows Event Logs</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ashish Bhangale](https://img.shields.io/badge/Ashish%20Bhangale-informational) ![G Khartheesvar](https://img.shields.io/badge/G%20Khartheesvar-informational) ![Arafat Ansari](https://img.shields.io/badge/Arafat%20Ansari-informational)

🔗 **Link:** [ThreatSeeker - Threat Hunting via Windows Event Logs](https://github.com/ine-labs/ThreatSeeker)  
📝 **Description:** Threat hunting using Windows logs is essential for identifying and mitigating potential security threats within an organization's network. It can be a time-consuming and painstaking process due to a large amount of data that needs to be collected and analyzed. The threat-hunting process could be repetitive. However, this process can be improved through custom scripts and tools.

In this talk, we will introduce ThreatSeeker, a windows log analysis framework that allows a threat hunter to find the common threats on the machine quickly. This tool also helps a threat hunter to detect APT movements. ThreatSeeker will allow a user to detect the following attacks:

- Suspicious account behavior
- User Creation and Added/Removed User to Admin group
- Brute Force Attack Detection on SMB, RDP, WinRM, etc.
- Brute Force Attack Detection
- Detection of malicious executable
- Detection of PTH Attack
- Suspicious service creation
- Installed Service with the executable in Suspicious locations
- Detection of Modifying, Starting, Disabling, and Stopping Service
- Detection of special privileges assigned
- Suspicious Command Auditing
- Powershell with Suspicious Argument
- PowerShell Downloads
- Execution of Suspicious executable,, i.e., rundll32.exe, sc.exe, mshta.exe, wscript.exe, cscript.exe
- Suspicious Windows Registry Modification, Addition
- Many More...

All the code and deployment scripts will be made open-source after the talk.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>CureIAM: The Ultimate Solution to Least Privilege Principle Enforcement on GCP</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Kenny Gotama](https://img.shields.io/badge/Kenny%20Gotama-informational) ![Rohit Sehgal](https://img.shields.io/badge/Rohit%20Sehgal-informational)

🔗 **Link:** Not Available  
📝 **Description:** CureIAM is an easy-to-use, reliable, and performant engine that enables DevOps and security teams to quickly clean up over-permissioned IAM accounts on GCP infrastructure. By leveraging GCP IAM Recommender APIs and the Cloudmarker framework, CureIAM automatically enforces least privilege principle on a daily basis, and helps to ensure that only the necessary permissions are granted to GCP accounts.

Key Features

- Config driven workflow for easy customization
- Scalable and production-grade design
- Embedded scheduling for daily enforcement
- Plugin-driven architecture for additional functionality
- Track actionable insights and records actions for audit purposes
- Scoring and enforcement of recommendations to ensure safety and security

</details>

<details><summary><strong>eBPFShield: Advanced IP-Intelligence & DNS Monitoring using eBPF</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sagar Bhure](https://img.shields.io/badge/Sagar%20Bhure-informational)

🔗 **Link:** [eBPFShield: Advanced IP-Intelligence & DNS Monitoring using eBPF](https://github.com/sagarbhure/eBPFShield)  
📝 **Description:** eBPFShield is a powerful security tool that utilizes eBPF and Python to provide real-time IP-Intelligence and DNS monitoring. By executing in kernel space, eBPFShield avoids costly context switches, making it a high-performance solution for detecting and preventing malicious behavior on your network. The tool offers efficient monitoring of outbound connections and comparison with threat intelligence feeds, making it an effective solution for identifying and mitigating potential threats. The tool includes features such as DNS monitoring, IP-Intelligence, and the ability to pull down public threat feeds.

Additionally, it includes a roadmap for future developments such as support for IPv6, automated IP reputation analysis using Machine Learning algorithms, and integration with popular SIEM systems for centralized monitoring and alerting.

eBPFShield is especially useful for companies and organizations that handle sensitive information and need to ensure the security of their networks. It's an efficient solution to monitor and protect servers from potential threats and it can help to prevent data breaches and other cyber attacks.

</details>

<details><summary><strong>Forecasting ATT&CK Flow by Recommendation System Based on APT</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Masaki Kuwano](https://img.shields.io/badge/Masaki%20Kuwano-informational) ![Koki Watarai](https://img.shields.io/badge/Koki%20Watarai-informational) ![Takuho Mitsunaga](https://img.shields.io/badge/Takuho%20Mitsunaga-informational)

🔗 **Link:** Not Available  
📝 **Description:** Our tool is to forecast undetected ATT&CK techniques based on collaborative filtering and graph databases.
PCs and servers are generating massive logs daily, on the other hand, SOCs analysts are required to detect and respond quickly to cyber-attacks. However, it will take a lot of time to detect cyber-attacks if SOC analysts do not have clues. Conventional log analysis tools such as SIEM can detect attacks but cannot predict the next attack from the information already obtained. Recommendation systems often used in e-commerce sites can predict future purchasing behavior by analyzing the user's purchase history. Replacing with ATT&CK, each attacker group can be considered a user, and techniques attackers use can be regarded as a user's purchase history.
Using this tool, the logs are mapped to ATT&CK techniques by uploading log files to create a technique usage history of the attacker (adversary) currently conducting an ongoing attack. The adversary's technique usage history and past APT attack data are used for collaborative filtering to predict which techniques the adversary may use in the future. This visualization is　displayed together with the ATT&CK tactic, enabling you to see the attack flow in stages of progression. In addition, search queries of SIEM associated with forecasted ATT&CK technique are outputted. SOC analysts can consider attacks quickly and comprehensively by using queries.
The source code of this tool and an example analysis will be shown on GitHub. It is available as a web application.

</details>

<details><summary><strong>Post-Quantum Cryptography Library</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sagar Bhure](https://img.shields.io/badge/Sagar%20Bhure-informational) ![Shain Singh](https://img.shields.io/badge/Shain%20Singh-informational)

🔗 **Link:** Not Available  
📝 **Description:** This library provides a convenient way for developers to integrate post-quantum cryptography into their applications, helping to protect sensitive information from potential quantum computing attacks. We present f5oqs_sdk, a Python 3 library that wraps the liboqs C library, which is part of the Open Quantum Safe (OQS) project. The OQS project aims to develop and prototype quantum-resistant cryptography. The f5oqs_sdk offers a unified API for post-quantum key encapsulation and digital signature schemes, as well as a collection of open-source implementations of post-quantum cryptography algorithms. It also provides support for alternative RNGs through the randombytes[] functions. The library is available on PyPI and can be easily installed with pip. The paper provides a brief overview of the installation process and usage of the library, along with examples of how to use the API.

f5oqs_sdk is a powerful tool for developers who want to integrate post-quantum cryptography into their applications. It provides a unified and easy-to-use API for implementing quantum-resistant cryptography, helping to protect sensitive information from potential quantum computing attacks.

</details>

<details><summary><strong>PurpleSharp: Automated Adversary Simulation</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>PyExfil - A Python Data Exfiltration & C2 Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yuval Nativ](https://img.shields.io/badge/Yuval%20Nativ-informational)

🔗 **Link:** Not Available  
📝 **Description:** PyExfil is a python data exfiltration package. It is currently an open source package allowing everyone to download, use and edit the code. It has several modules classified in 4 types of data exfiltration purposes. It is designed to enable Security personnel to test their Data Leakage Prevention mechanisms by attempting to leak various types of data and examine alerting and prevention mechanisms employed in their infrastructure.

</details>

<details><summary><strong>StegoWiper+: A Powerful and Flexible Active Attack for Disrupting Stegomalware and Advanced Stegography</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Alfonso Muñoz](https://img.shields.io/badge/Alfonso%20Muñoz-informational) ![Manuel Urueña](https://img.shields.io/badge/Manuel%20Urueña-informational)

🔗 **Link:** [StegoWiper+: A Powerful and Flexible Active Attack for Disrupting Stegomalware and Advanced Stegography](https://github.com/mindcrypt/stegowiper)  
📝 **Description:** Over the last 10 years, many threat groups have employed stegomalware or other steganography-based techniques to attack organizations from all sectors and in all regions of the world. Some examples are: APT15/Vixen Panda, APT23/Tropic Trooper, APT29/Cozy Bear, APT32/OceanLotus, APT34/OilRig, APT37/ScarCruft, APT38/Lazarus Group, Duqu Group, Turla, Vawtrack, Powload, Lokibot, Ursnif, IceID, etc.Our research shows that most groups are employing very simple techniques (at least from an academic perspective) and known tools to circumvent perimeter defenses, although more advanced groups are also using steganography to hide C&C communication and data exfiltration. We argue that this lack of sophistication is not due to the lack of knowledge in steganography (some APTs have already experimented with advanced algorithms) but simply because organizations are not able to defend themselves, even against the simplest steganography techniques.

During the demonstration we will show the practical limitations of applying existing automated steganalysis techniques for companies that want to prevent infections or information theft by these threat actors. For this reason, we have created stegoWiper, a tool to blindly disrupt any image-based stegomalware, attacking the weakest point of all steganography algorithms: their robustness. We'll show that it is capable of disrupting all steganography techniques and tools (Invoke-PSImage, F5, Steghide, openstego, ...) employed nowadays. In fact, the more sophisticated a steganography technique is, the more disruption stegoWiper produces. Moreover, our active attack allows us to disrupt any steganography payload from all the images exchanged by an organization by means of a web proxy ICAP (Internet Content Adaptation Protocol) service, in real time and without having to identify which images contain hidden data first.

After our presentation at BlackHat USA 2022 Arsenal we have been working on supporting, disrupting, state-of-the-art advanced algorithms available in the academic literature, based on matrix encryption, wet-papers, etc. (e.g. Hill, J-Uniward, Hugo). Especially we have paid attention to the YASS algorithm (https://pboueke.github.io/CryptoStego/) resistant to numerous active attacks and commercial CDR-type software. Finally our tool is able to defeat them.

</details>

<details><summary><strong>Unprotect Project: Malware Evasion Techniques</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Thomas Roccia](https://img.shields.io/badge/Thomas%20Roccia-informational)

🔗 **Link:** [Unprotect Project: Malware Evasion Techniques](https://github.com/fr0gger)  
📝 **Description:** Malware evasion consists of techniques used by malware to bypass security in place, circumvent automated and static analysis as well as avoiding detection and harden reverse engineering. There is a broad specter of techniques that can be used. In this talk we will review the history of malware evasion techniques, understand the latest trends currently used by threat actors and bolster your security analysis skills by getting more knowledge about evasion mechanisms.

We will present the latest major update of the Unprotect Project an open-source documentation about malware evasion techniques. The goal will be to present the project and see how we can leverage it for use cases, including threat intelligence, malware analysis, strengthen security, train people, and extend the Mitre ATT&CK matrix. Over the years it has become a well renowned place for security researchers. During this talk we will review some of the most important update.

This presentation can benefit both Blue and Red Team as it will provide knowledge and information on how malware can bypass your security in place and stay under the radar. You will learn about the intrinsic mechanisms used by attackers to compromise you without you even realizing it!

</details>

<details><summary><strong>White Phoenix - Beating Intermittent Encryption</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ari Novick](https://img.shields.io/badge/Ari%20Novick-informational) ![Amir Landau](https://img.shields.io/badge/Amir%20Landau-informational)

🔗 **Link:** [White Phoenix - Beating Intermittent Encryption](https://github.com/mittidesai/Stock-Market-Prediction/blob/master/120_clusters)  
📝 **Description:** Intermittent Encryption (aka Partial Encryption) is a new trend in the world of ransomware. It's been adopted by many notorious groups such as BlackCat Ransomware, Play Ransomware and more. Altogether, the groups using intermittent encryption have successfully targeted hundreds of organizations in 2022 alone. However, even though intermittent encryption has its advantages, it leaves much of the content of targeted files unencrypted. In this talk, we will demonstrate a tool that uses this limitation to recover valuable data, such as text and images from documents encrypted by these groups, allowing the victims to recover some of their lost data.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Deepfake Detection with Faceless</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Manh Pham](https://img.shields.io/badge/Manh%20Pham-informational) ![Dong Duong](https://img.shields.io/badge/Dong%20Duong-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Hands-on RFID: Sniff it, crack it, clone it</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Kelvin Wong](https://img.shields.io/badge/Kelvin%20Wong-informational) ![Dennis Goh](https://img.shields.io/badge/Dennis%20Goh-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>KICS - Your IaC Secure Now!</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Nuno Oliveira](https://img.shields.io/badge/Nuno%20Oliveira-informational) ![Joao Reigota](https://img.shields.io/badge/Joao%20Reigota-informational)

🔗 **Link:** Not Available  
📝 **Description:** KICS stands for Keeping Infrastructure as Code Secure. It is open source and is a must-have for any cloud native project to find security vulnerabilities, compliance issues, and infrastructure misconfigurations early in the development cycle of the underlying infrastructure-as-code (IaC).

KICS supports about 20 different technologies including Terraform, Cloudformation, Kubernetes, Docker, over several cloud providers like AWS, Microsoft Azure or Google Cloud. It is the only open-source project that has achieved any Center for Internet Security (CIS) certification.

KICS is fully customizable and extensible by the addition of rules for new vulnerabilities. It is available as a Docker image, and is paired in multiple platforms to leverage its integration on the development life-cycle and the DevSecOps mentality of its users. Gitlab has chosen KICS as its default IaC scanner; it is also available in ArgoHub, as a hook in TerraformCloud or as a Github Action for Github workflows.

One of the most recent features of KICS is auto remediation. With this feature KICS goes full cycle in preventing vulnerable code from going into production by scanning the code, exposing the issues, and automatically remediating them. Such a feature is both available from the CLI interface, or via a plugin for the Visual Studio Code editor, where we bring together auto-remediation and real-time scanning. As the developer writes IaC scripts, KICS automatically looks for vulnerabilities, proposes fixes and remediates them. By the time the IaC scripts are finished, developers are rest assured that it is safe to go into production. This is shift-left security brought to its splendor.

</details>

<details><summary><strong>Nightingale: Docker for Pentesters</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Raja Nagori](https://img.shields.io/badge/Raja%20Nagori-informational)

🔗 **Link:** [Nightingale: Docker for Pentesters](https://github.com/RAJANAGORI/Nightingale)  
📝 **Description:** Have you ever been encounter where you configured the security virtual envieonment in the virtualbox and after someday the VM got crashed. All your configuration, tool setup, important information about the taget, POC's and what not, all will be gone and you can't recover the same.

With the same problem, I created the Nightingale based on the docker technology which provides you the exact security environment where you can expreicne the tools which a pentesters required at the time of pentesting. Adding to this, you no need to worry about your data, configuration and all other important. Nightingale will automatically restore the configuration once the new container will be up.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>uftrace: Dynamic Function Tracing Tool for C/C++/Rust programs</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Kim MinJeong](https://img.shields.io/badge/Kim%20MinJeong-informational) ![Honggyu Kim](https://img.shields.io/badge/Honggyu%20Kim-informational)

🔗 **Link:** Not Available  
📝 **Description:** uftrace is a function tracing tool that helps in the analysis of C/C++/Rust programs. It hooks into the entry and exit of each function, recording timestamps as well as the function's arguments and return values. uftrace is capable of tracing both user and kernel functions, as well as library functions and system events providing an integrated execution flow in a single timeline.

Initially, uftrace only supported function tracing with compiler support. However, it now allows users to trace function calls without recompilation by analyzing instructions in each function prologue and dynamically and selectively patching those instructions.

Users can also write and run scripts for each function entry and exit using python/luajit APIs to create custom tools for their specific purposes.

uftrace offers various filters to reduce the amount of trace data and provides visualization using Chrome trace viewer and flame graphs, allowing for a big picture view of the execution flow.

uftrace was open sourced in 2016 and has been developed at https://github.com/namhyung/uftrace.

</details>

---