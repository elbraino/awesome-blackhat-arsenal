# Europe 2021
---
📍 41 tools demonstrated at **Black Hat Arsenal Europe 2021**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (3)
- [🌐 Web/AppSec](#-webappsec) (6)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (2)
- [📱 Mobile Security](#-mobile-security) (1)
- [🔍 OSINT](#-osint) (2)
- [🔴 Red Teaming](#-red-teaming) (12)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (3)
- [🔵 Blue Team & Detection](#-blue-team--detection) (9)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (1)
- [🧠 Reverse Engineering](#-reverse-engineering) (1)
- [🧠 Social Engineering / General](#-social-engineering--general) (1)
---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Cluster Fuzz, Introduction to Car Hacking With Real Car Hardware</strong> — Ian Tabor</summary>

**Track:** Arsenal Lab · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/google/clusterfuzz](https://github.com/google/clusterfuzz)  
📝 **Description:** A scalable fuzzing infrastructure that finds security and stability issues in software. It powers Google OSS-Fuzz and enables automated vulnerability detection across open-source projects.

</details>

<details><summary><strong>Disrupting OT and IoT by Exploiting TCP/IP Stacks</strong> — Stanislav Dashevskyi, Daniel dos Santos</summary>

**Track:** Arsenal Lab · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/Forescout/project-memoria-detector](https://github.com/Forescout/project-memoria-detector)  
📝 **Description:** A project that investigates vulnerabilities in IoT smart devices by testing denial-of-service and deauthentication attacks to evaluate their security protocols and communication vulnerabilities.

</details>

<details><summary><strong>Packet Carving for SATCOMs Hackers</strong> — James Pavur</summary>

**Track:** Arsenal Lab · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/ssloxford/gsextract](https://github.com/ssloxford/gsextract)  
📝 **Description:** Tools for satellite communications security research, including GSExtract for converting satellite radio captures of internet traffic using Generic Stream Encapsulation (GSE) over DVB-S into usable pcap files.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>AppsecStudy: Open-Source eLearning Management System for Information Security</strong> — Ivan Iushkevich</summary>

**Track:** Web AppSec · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/zzzteph/appsec.study](https://github.com/zzzteph/appsec.study)  
📝 **Description:** Because preventing vulnerability is less costly than redeveloping the complete application, infosec education and training become more and more actual. As a result, developers can greatly reduce the risk and expense from cyber attacks in the future by creating secure code. In addition, training the team based on the security assessment results to correct actual errors provides ongoing protection for existing and future products. Since studying is impossible without a practical part, providing hands-on lab training for developing teams is a necessary step. AppsecStudy - an open-source platform for seminars, training, and organizing courses for practical information security for developers and IT specialists. This tool has all the built-in basic requirements needed for organizing normal and productive training.

</details>

<details><summary><strong>crawlergo: A Powerful Browser Crawler for Web Vulnerability Scanners</strong> — Zhu Siyu</summary>

**Track:** Web AppSec · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/Qianlitp/crawlergo](https://github.com/Qianlitp/crawlergo)  
📝 **Description:** crawlergo is a browser crawler that uses chrome headless mode for URL collection. It dynamically finds all URL requests contained in a web page through powerful automated intelligent analysis and de-duplication, providing comprehensive and high quality input for subsequent web vulnerability scanning.

</details>

<details><summary><strong>LazyCSRF: A More Useful CSRF PoC Generator on BurpSuite</strong> — Taichi Kotake</summary>

**Track:** Web AppSec · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/tkmru/lazyCSRF](https://github.com/tkmru/lazyCSRF)  
📝 **Description:** Burp Suite is an intercepting HTTP Proxy, and it is the defacto tool for performing web application security testing. The feature of Burp Suite that I like the most is `Generate CSRF PoC`. However, the function to automatically determine the content of the request is broken, and it tries to generate PoCs using `form` even for PoCs that cannot be represented by `form`, such as JSON parameters and PUT requests. In addition, multibyte characters that can be displayed in Burp Suite itself are often garbled in the generated CSRF PoC. These were the motivations for creating LazyCSRF. I have implemented a feature to solve them. It has the following features: - Automatically switch to PoC using XMLHttpRequest - In case the parameter is JSON - In case the request is a PUT/PATCH/DELETE - Support displaying multibyte characters (like Japanese) - Generating CSRF PoC with Burp Suite Community Edition (of course, it also works in Professional Edition) https://github.com/tkmru/lazyCSRF

</details>

<details><summary><strong>PyGoat</strong> — Shaik Ajmal R, Ade Yoseman Putra</summary>

**Track:** Web AppSec · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/adeyosemanputra/pygoat](https://github.com/adeyosemanputra/pygoat)  
📝 **Description:** PyGoat - Intentionally vuln web Application Security in django. our roadmap build intentionally vuln web Application in django. The Vulnerability can based on OWASP top ten • A1:2017-Injection • A2:2017-Broken Authentication • A3:2017-Sensitive Data Exposure • A4:2017-XML External Entities (XXE) • A5:2017-Broken Access Control • A6:2017-Security Misconfiguration • A7:2017-Cross-Site Scripting (XSS) • A8:2017-Insecure Deserialization • A9:2017-Using Components with Known Vulnerabilities • A10:2017-Insufficient Logging & Monitoring

</details>

<details><summary><strong>vAPI: Vulnerable Adversely Programmed Interface (OWASP API Top 10)</strong> — Tushar Kulkarni</summary>

**Track:** Web AppSec · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/roottusk/vapi](https://github.com/roottusk/vapi)  
📝 **Description:** vAPI is a Vulnerable Interface in a Lab like environment that mimics the scenarios from OWASP API Top 10 and helps the user understand and exploit the vulnerabilities according to OWASP API Top 10 2019. The lab is divided into 10 exercises that sequentially demonstrate the vulnerabilities and give a flag if exploited successfully.

</details>

<details><summary><strong>Xsstools: The XSS Exploitation Framework</strong> — Lucas Philippe</summary>

**Track:** Web AppSec · Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/yeswehack/xsstools](https://github.com/yeswehack/xsstools)  
📝 **Description:** An XSS development framework that provides JavaScript libraries for building cross-site scripting exploits, including tools for data exfiltration, payload generation, request manipulation, and clickjacking attacks.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Dependency Combobulator</strong> — Moshe Zioni</summary>

**Track:** Code Assessment · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/apiiro/combobulator](https://github.com/apiiro/combobulator)  
📝 **Description:** An open-source, modular framework designed to detect and prevent dependency confusion attacks by evaluating packages across different sources and package management systems like npm and Maven.

</details>

<details><summary><strong>KICS: Keeping Infrastructure-as-Code Secure</strong> — Ori Bendet</summary>

**Track:** Code Assessment · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/Checkmarx/kics](https://github.com/Checkmarx/kics)  
📝 **Description:** Infrastructure as Code (IaC) makes deploying cloud or container configurations scalable and faster. If you are launching a microservice into a Kubernetes cluster, or even building an entire AWS virtual infrastructure, IaC can automate the deployment. By building repeatable templates you can also ensure that deployments happen exactly as you design, every time. However, errors in infrastructure configuration are now regarded as the second biggest cause of data breaches. There are many ways to give adversaries an advantage through security misconfigurations. Overly permissive storage volumes, unauthenticated database access, or ports left open to the internet have all been a cause of compromise. The solution? Treat your infrastructure code the same as your application code. During your build process, use tools to scan for infrastructure misconfigurations. When you find them raise alerts or even break the build. In this session, we will discuss common types of IaC misconfigurations, and demonstrate a free, open source security tool that developers can build into their pipelines to help protect infrastructure from compromise.

</details>

---
## 📱 Mobile Security
<details><summary><strong>A Privilege Rules-Based Vulnerabilities Scan Tool for Android Apps</strong> — Li Jiang</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/JiangLi23/A-privilege-rules-based-Vulnerabilities-scan-tool-for-Android-Apps](https://github.com/JiangLi23/A-privilege-rules-based-Vulnerabilities-scan-tool-for-Android-Apps)  
📝 **Description:** In the development of software, the system is often designed on a good architecture to ensure the security of the system, which reduces the risk of being attacked. However, due to business requirements, some "privilege rules" often exist in some key security protection processes, such as some privilege userid lists, privilege url lists, or special paths, etc. These privilege configurations disrupt the original security process, and pull down the security level, become a new attack surface (intrusion into the original secure system through attack privilege rules). It is more difficult for us to attack the system directly, but it will be easier to attack the system through the vulnerabilities in the privilege rules, and even the vulnerabilities in these privilege rules already exist widely. Because of the above attack risks, we develope a tool called "privilege rules bug hunter"(PBH) to detect the vulnerability of privilege rules in software. Data flow graph (DFG) and Control flow graph(CFG) enable us to better understand the inherent logic in software. However, there are so many control flows and data flows when identifying the privilege rules. How to distinguish the normal logic and find out the privilege rules accurately is a challenge. We will combine DFG, CFG and taint analysis methods to find out the risk: 1) generate a graph with the help of DFG and CFG , and use graph similarity information to classify. 2) The software is tested dynamically by online data, and the path information of runtime is recorded by hook to help identify the privilege paths of the graph in 1). 3) Collecting the information of privilege rules and looking for common vulnerabilities(such as xss etc) to reache the control of the whole system. In this talk, we found the risk of privilege rules in a software , which broke the normal flow of software security architecture and introduce new risks. At the same time, based on the software analysis method, a tool is implemented to detect the vulnerability of privilege rules. We use the developed tool in Android Software Security testing, and find many privilege URLs and paths are configured into the software with high permissions. At the same time, there are a large number of n-days in the websites where these URLs exist.

</details>

---
## 🔍 OSINT
<details><summary><strong>CrowdSec: The Open-Source & Participative IPS</strong> — Philippe Humeau</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/crowdsecurity/crowdsec](https://github.com/crowdsecurity/crowdsec)  
📝 **Description:** An open-source security platform that detects malicious behavior through log analysis and HTTP request inspection, leveraging crowdsourced threat intelligence to provide community-driven protection against malicious IPs.

</details>

<details><summary><strong>iKy – OSINT TOOL</strong> — Kenn Bro</summary>

**Track:** OSINT - Open Source Intelligence · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/kennbroorg/iKy](https://github.com/kennbroorg/iKy)  
📝 **Description:** iKy is an Open Source project. From an e-mail or other selectors (username, twitter, instagram, etc) it tries to collect data to later convert them into visual information OSINT tools are many and varied. But with iKY it was sought, apart from a good performance, an attractive graphic visual supported by the fact that neuroscientifically the brain interprets images better and faster than numbers and letters

</details>

---
## 🔴 Red Teaming
<details><summary><strong>aDLL: adventure Dynamic Link Library</strong> — Roberto Aranda Castañeda</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/ideaslocas/aDLL](https://github.com/ideaslocas/aDLL)  
📝 **Description:** Adventure of Dynamic Link Library (aDLL) is a console tool for the analysis of binaries and focused on the automatic detection of possible DLL Hijacking cases in Windows systems. The purpose of the tool is to analyse every DLL that an executable will load in memory, anticipating the Windows DLL search order and identifying those DLLs that are missing from the expected directory. That may lead in the replacement of the legitimate DLL by a malicious one if the directory has misconfigured permissions.

</details>

<details><summary><strong>AttackForge: Pentest Management Platform</strong> — Fil Filiposki, Stas Filshtinskiy</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/attackforge](https://github.com/attackforge)  
📝 **Description:** AttackForge.com is Community Pentest Management Platform that supports workflows for pentesting & collaboration between engineering & security teams. AttackForge.com equips pentesters with the following: - Dedicated workspace for penetration testing projects. You can invite other pentesters or engineers to your workspace and assign their roles. You can store all information/entry criteria/logs/etc. - Assign methodologies/checklists to each project. AttackForge includes pre-built methodologies for convenience. - Professional automated reporting. Fully customizable report templates using AttackForge ReportGen tool. AttackForge includes a styled base template to get started fast or you can use your own templates. - Vulnerability library pre-loaded with 1300+ vulnerabilities. You can add your own. - Import vulnerabilities from tools such as Nessus, BURP, Qualys, Netsparker, Acunetix, Nexpose, OpenVAS, ZAP. RESTful API for custom imports & generic CSV importer. - Build AttackChains and map to MITRE ATT&CK Framework. - Project management support including calendar, daily tracking, retesting tracking, and others. - Integration with DevOps tools like JIRA & ServiceNow. - Custom themes including "The Matrix" for the full Hacker experience Come check out the new features we have not yet presented to public!

</details>

<details><summary><strong>CQPrivilegeExcalation Toolkit: Effective Tools for Windows Privilege Escalation Gamers</strong> — Paula Januszkiewicz, Mike Jankowski-Lorek</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/geeksniper/windows-privilege-escalation](https://github.com/geeksniper/windows-privilege-escalation)  
📝 **Description:** CQURE PE Toolkit is focused on Windows Privilege Escalation tactics and techniques created to help improve every privilege escalation game. This toolkit guides you through the process of exploiting a bug or design flaw in an operating system or software to gain elevated privileges to resources that are normally highly protected. Once you will know what to look for and what to ignore, Privilege Escalation will be so much easier. This powerful toolkit is useful for those who are interested in penetration testing and professionals engaged in pen-testing working in the areas of database, system, network, or application administration. Among published presented tools are CQSecretsDumper, CQNTDSDTDecrypter, CQLsassSecretsDumper, CQCreateProcessWithParent, and many more.

</details>

<details><summary><strong>DNSStager: A Tool to Hide Your Payload in DNS</strong> — Mohammad Askar</summary>

**Track:** Malware Offense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/mhaskar/DNSStager](https://github.com/mhaskar/DNSStager)  
📝 **Description:** A Python-based tool that hides and transfers payloads using DNS by creating a malicious DNS server that delivers encoded payloads through DNS queries. It generates custom agents in C or GoLang that retrieve, decode, and execute the payloads.

</details>

<details><summary><strong>HazProne</strong> — Staford Titus S</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/stafordtituss/HazProne](https://github.com/stafordtituss/HazProne)  
📝 **Description:** HazProne is a Cloud Pentesting Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand aws resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!

</details>

<details><summary><strong>Kubestriker: A Blazing Fast Security Auditing Tool</strong> — Vasant Kumar Chinnipilli</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/vchinnipilli/kubestriker](https://github.com/vchinnipilli/kubestriker)  
📝 **Description:** Kubestriker performs numerous in depth checks on kubernetes infrastructure to identify any misconfigurations which make organisations an easy target for attackers and safeguards against potential attacks on Kubernetes clusters.

</details>

<details><summary><strong>Nebula: A Case Study in Penetrating Something as Soft as a Cloud</strong> — Bleon Proko</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/gl4ssesbo1/Nebula](https://github.com/gl4ssesbo1/Nebula)  
📝 **Description:** Nebula is a cloud C2 Framework, which at the moment offers reconnaissance, enumeration, exploitation, post exploitation on AWS, but still working to allow testing other Cloud Providers and DevOps Components. It started as a project to unify all Cloud + DevOps Pentest and Security Techniques for a better assessment of the Infrastructures. It is build with modules for each provider and each functionality. As of April 2021, it only covers AWS, but is currently an ongoing project and hopefully will continue to grow to test GCP, Azure, Kubernetes, Docker, or automation engines like Ansible, Terraform, Chef, etc.

</details>

<details><summary><strong>on the fly</strong> — Pablo Gonzalez, Luis Eduardo Alvarez</summary>

**Track:** Network Attacks · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/Telefonica/on-the-fly](https://github.com/Telefonica/on-the-fly)  
📝 **Description:** The 'on-the-fly' tool intends to give the pentester an 'all-in-one' tool by deploying different functionalities applicable across the three domains of work: IoT, ICS & IT. The present work introduces a new framework in which enough functionalities will be provided to discover, evaluate, and audit technologies from the three mentioned domains.

</details>

<details><summary><strong>Pentest Collaboration Framework</strong> — Ilya Shaposhnikov, Sergey Bliznyuk, Maksim Lebedev, Sofia Marakhovich</summary>

**Track:** Network Attacks · **Event:** Europe 2021  
🔗 **Link:** [https://gitlab.com/invuls/pentest-projects/pcf](https://gitlab.com/invuls/pentest-projects/pcf)  
📝 **Description:** Pentest Collaboration Framework - An opensource, cross-platform and portable toolkit that allows you to exchange information on the penetration testing process. It also contains a model of differentiation of rights for use by several teams or independent researchers. One of latest major updates from previous Black Hat conference is a new feature - issue templates library which allow pentesters to create issues much more faster!

</details>

<details><summary><strong>RedHerd Framework</strong> — Mario D'Amico, Giovanni Pecoraro, Simon Pietro Romano</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/redherd-project/redherd-framework](https://github.com/redherd-project/redherd-framework)  
📝 **Description:** RedHerd is a collaborative serverless framework for orchestrating a geographically distributed set of assets in order to simulate/conduct complex offensive cyberspace operations. The design and implementation of RedHerd perfectly fit the Open Systems Architecture design pattern, thanks to the adoption of both open standards and wide-spread open source software components. The framework allows to seamlessly deploy a ready-to-use infrastructure that can be adopted for effective conduct, simulation and training purposes, by reliably joining a real-world cyberspace battlefield in which red and blue teams challenge each other to reach their goals. These elements lead to the Offensive Cyberspace Operations as a Service (OCOaaS) paradigm, which involves a complete software solution, locally set up, remotely deployed or Cloud-based, offering a layer of abstraction placed in front of the operative infrastructure and tools. In this way, the operational actors have the opportunity to focus on the task execution, while ignoring all of the collateral activities. In addition, OCOaaS provides a flexible and quickly deployable solution to reduce costs. The RedHerd framework is a practical implementation of this model empowering the approach with strong orchestration capabilities and other additional features.

</details>

<details><summary><strong>SMERSH</strong> — Mike Houziaux</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/matro7sh/Smersh](https://github.com/matro7sh/Smersh)  
📝 **Description:** It's a collaborative open source tool to manage pentest campaigns. You can install it via Docker ( it includes an Angular front end with a symfony API ) There is also a python client for the bearded ones. The graphical interface allows you to add your scope and vulnerabilities and exchange information with your hacker partners in a Quick and easy way (also possible to generate report).

</details>

<details><summary><strong>WhoC: Peeking Under the Hood of CaaS Offerings</strong> — Yuval Avrahami</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/twistlock/whoc](https://github.com/twistlock/whoc)  
📝 **Description:** A container image that extracts the underlying container runtime and sends it to a remote server, exploiting the exposure of runtimes through /proc/self/exe to reveal what container infrastructure CaaS providers use.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Kubernetes Goat: Interactive Kubernetes Security Learning Playground</strong> — Madhu Akula</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/madhuakula/kubernetes-goat](https://github.com/madhuakula/kubernetes-goat)  
📝 **Description:** Kubernetes Goat is a "vulnerable by design" Kubernetes Cluster environment to practice and learn about Kubernetes Security. It has step by step detailed guide and digital book on how to get started with Kubernetes Goat by exploring different vulnerabilities in Kubernetes Cluster and Containerized environments. Also, it has scenarios taken from the real-world vulnerabilities and maps the Kubernetes Goat scenarios. The complete documentation and instruction to practice Kubernetes Security for performing security assessments, pentesting, and in general Kubernetes Security. As a defender you will see how we can learn these attacks, misconfigurations to understand and improve your cloud-native infrastructure security posture. Some of the high-level scenarios include, but are not limited to 1. Sensitive keys in code-bases 2. DIND (docker-in-docker) exploitation 3. SSRF in K8S world 4. Container escape to access host system 5. Docker CIS Benchmarks analysis 6. Kubernetes CIS Benchmarks analysis 7. Attacking private registry 8. NodePort exposed services 9. Helm v2 tiller to PwN the cluster 10. Analysing crypto miner container 11. Kubernetes Namespaces bypass 12. Gaining environment information 13. DoS the memory/CPU resources 14. Hacker Container preview 15. Hidden in layers 16. RBAC Least Privileges Misconfiguration 17. KubeAudit - Audit Kubernetes Clusters 18. Sysdig Falco - Runtime Security Monitoring & Detection 19. Popeye - A Kubernetes Cluster Sanitizer 20. Secure network boundaries using NSP

</details>

<details><summary><strong>LaiFu: A Modern Protocol Fuzzing Framework Based on Scapy</strong> — Yu Zhou, Jie Hong, Zhaobin Gui, Qilian Chen</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/secdev/awesome-scapy](https://github.com/secdev/awesome-scapy)  
📝 **Description:** As a protocol tester, we often use scapy to interact with the protocol because it is able to craft or decode packets easily and it implements a wide number of protocols. However, the fuzz function supported by scapy can not fuzz protocols sufficiently and effectively. Testers often need to write additional fuzzing code based on other fuzzing frameworks such as Peach and Boofuzz. According to the current situation, we design a protocol fuzzing tool named "LaiFu". LaiFu framework allows testers to use scapy to specify protocol formats directly. We designed the corresponding mutation algorithm according to the various field types of scapy's packet. Meanwhile, we also provide a tool to show the coverage of fuzzing target in real time. Testers only need to put each data packet as a node into the graph and then start the fuzzing test. Another advantage is that LaiFu makes many protocols already implemented by scapy to be fuzzable. We are going to open source this tool to assist testers or developers to test their code and make protocol fuzzing easy and effective.

</details>

<details><summary><strong>The Vulnerability Complete Definition Library</strong> — Wish Wu</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/antgroup-skyward/TheVulnerabilityCompleteDefinitionLibrary](https://github.com/antgroup-skyward/TheVulnerabilityCompleteDefinitionLibrary)  
📝 **Description:** More and more security researchers treat source code as a database and use code patterns to search or query potential vulnerabilities. At the Black Hat 2021 USA conference, the 360 ​​Alpha Lab team disclosed how to use code patterns to find 11 CVEs on Chrome, and developed a 0day exploit based on this. The code pattern is essentially a set of conditions for the code, and the code that satisfies certain conditions is very likely to have vulnerabilities. However, the industry does not seem to have a publicly available tool that can accurately describe or define the necessary and sufficient conditions for a specific vulnerability. Although CodeQL (https://securitylab.github.com/tools/codeql/) is already trying to convert the vulnerability described in natural language in Common Weakness Enumeration (https://cwe.mitre.org/) into query sentences , But most of its query conditions are sufficient and non-essential conditions to form a specific vulnerability, that is, it does not include all the circumstances that form this vulnerability. These query sentences avoid the conditions that CodeQL is difficult to process or describe to improve the success rate of the query. And I personally think that the grammatical rules of SQL often cannot intuitively describe the constraints of the code and the code running process, and a large number of built-in query processes also make the learning cost higher. Therefore, I have developed a complete definition library for vulnerabilities and believe that this library has two main advantages. First, this library can describe constraints with syntax, design ideas, and keywords similar to the code used by developers, which makes this tool have a lower learning cost. Second, this library is designed to describe the necessary and sufficient conditions for the formation of vulnerabilities. The necessary and sufficient conditions here is used to describe all possible situations that form the vulnerabilities. We should not artificially modify the search conditions to make it easier for the algorithm of the search program to search for results, but should let the search algorithm determine by itself how to search can speed up the display of results. This library is developed based on LLVM's AST (Abstract Syntax Tree) and the constraint solver STP (Simple Theorem Prover), and supports the description of constraints on objects such as control flow, data flow, value size, variable relations, variable types, variable names, etc. The library will also contain a batch of vulnerability definitions I wrote and a simple search algorithm. I will use a simple example to demonstrate how the algorithm finds a vulnerability in a specific situation based on the vulnerability definition. All source code will be hosted on github, you can download and study by yourself.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>An Open Stack for Threat Hunting in Hybrid Cloud With Connected Observability</strong> — Xiaokui Shu, Frederico Araujo, Teryl Taylor, Jiyong Jang</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/opencybersecurityalliance/kestrel-lang](https://github.com/opencybersecurityalliance/kestrel-lang)  
📝 **Description:** We present a cloud-native threat hunting architecture built on open-source technologies. The security architecture integrates SysFlow and Kestrel to provide connected endpoint observability, edge analytics, and a cyber-reasoning stack that enables threat hunters to quickly and uniformly perform threat hunting and investigation across cloud and premise environments. This facilitates a new threat discovery methodology in which declarative hunting flows automate the search for behavioral attack patterns and indicators of compromise in telemetry data streams that are automatically tagged with attack TTPs. We show how these two open-source frameworks can deploy and scale natively on cloud environments to discover attacks and security breaches against cloud services and container infrastructures. SysFlow is an open observability framework that lifts and normalizes the representation of system activities into a compact entity-relational format that records workload behaviors by connecting single-event and volumetric flow representations of process control flows, file interactions, and network communications. It drastically reduces data footprints over existing approaches and is particularly suitable for large scale cloud-wide monitoring and forensic investigation of sophisticated cyber-attacks that may not be discovered for long periods of time. Kestrel is a threat hunting language for creating composable, reusable, and shareable hunt flows. It brings two key innovations to the security community: (i) a composable way of expressing hunting knowledge for threat hypothesis development and reasoning over entity-relational data abstractions, and (ii) an open-source language runtime to compute how to perform hunting steps and execute them in a distributed fashion at the local hunting site, remote data sources, and in the cloud. We will demonstrate through live threat hunting scenarios how the two open-source projects can help create a powerful open platform for gaining operational awareness and alleviating key pain points in integrating security solutions into a "single-pane-of-glass" for effective and shareable threat hunting in the cloud.

</details>

<details><summary><strong>DejaVu ++</strong> — Bhadresh Patel, Harish Ramadoss</summary>

**Track:** Malware Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/worldveil/dejavu](https://github.com/worldveil/dejavu)  
📝 **Description:** DejaVu is an open source deception framework which can be used to deploy decoys across the infrastructure. This could be used by the defender to deploy multiple interactive (Server and Client) decoys strategically across the network and cloud. We have done massive updates to our platform (now DejaVu ++) and are excited to present these at Blackhat Europe. Some key updates: 1. Decentralized architecture to support enterprise orgs 2. Video recording of attacker's movement, record attacker's activity 3. Highly interactive decoys to engage the attacker and reveal attacker motivation and TTP 4. Integrated IDS for enriched alerts 5. Full packet capture of attacker's interaction with the decoy for forensic analysis. 6. Cloud Ready decoys - Now blue team can deploy DejaVu instance on AWS infra - Configure decoy personality to mimic the environment - AWS breadcrumbs 7. Dashboard with monitoring and analysis - Full lifecycle of event can be drilled into by an analyst 8. New decoys - Email and client side decoys to detect Spear Phishing - RDP Interactive and Non-Interactive - Interactive SSH - Detect MITM attacks : ARP Poisoning, Responder, SSDP - HONEYCOMB (To capture events from Honey Docs) - Beaconing Documents - ICS/SCADA Decoys - Modbus and S7COMM 9. Personalized threat inteligiance - Deploy customised decoys on DMZ to detect targeted threats 10. Logging Capability - Ship logs to SIEM or other platforms using Syslog capability https://github.com/bhdresh/Dejavu

</details>

<details><summary><strong>In0ri</strong> — Nguyen Hoang, Manh Pham, Dong Duong</summary>

**Track:** Network Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/J4FSec/In0ri](https://github.com/J4FSec/In0ri)  
📝 **Description:** Have you ever wondered how many ways there are to detect a defacement attack? - Based on hash - Based on signature - Differential comparison - Machine learning Well, quite a lot. Nowadays, machine learning have really developed, with increasing agility and accuracy, this is a new approach in Cyber Security in general which can adapt to new attack techniques. In this talk, we will be presenting In0ri - a defacement detection system utilizing image-classification convolutional neural network. There's two ways to deploy and use In0ri: - Running off crontab by periodically visiting the URL. - Internal agent running off the web server With the first method, we can directly check if a path has been defaced or not. As a system administrator, we can use the second method to check a local website with an internal Agent. In0ri the first source machine learning project to detect defacement attacks, we will show the process of installing, training and running In0ri. After that, we will show how it succeeds to get high quality of detecting the deface attacks by using deep learning.

</details>

<details><summary><strong>Mobile Malware Mimicking Framework</strong> — Max Kersten</summary>

**Track:** Malware Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)  
📝 **Description:** Mobile Security Framework (MobSF) is an automated, all-in-one mobile application security testing platform that performs static and dynamic analysis for Android, iOS, and Windows apps, with CI/CD integration via APIs.

</details>

<details><summary><strong>pwnSpoof</strong> — Simon Gurney, Daniel Oates Lee, Peter Holroyde</summary>

**Track:** Network Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/punk-security/pwnspoof](https://github.com/punk-security/pwnspoof)  
📝 **Description:** A Python tool that generates realistic spoofed log files for common web servers with customizable attack scenarios, useful for cybersecurity training exercises and CTF competitions.

</details>

<details><summary><strong>RIoTPot: A Modular Hybrid-Interaction IoT/OT Honeypot</strong> — Emmanouil Vasilomanolakis, Shreyas Srinivasa, Abhimanyu Rawat</summary>

**Track:** Malware Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/aau-network-security/riotpot](https://github.com/aau-network-security/riotpot)  
📝 **Description:** A modular hybrid-interaction honeypot focused on emulating IoT and OT protocols, functioning as a proxy service that routes incoming attacks to various internal and external honeypot services.

</details>

<details><summary><strong>RPC-FireWall</strong> — Sagie Dulce</summary>

**Track:** Network Defense · Malware Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/zeronetworks/rpcfirewall](https://github.com/zeronetworks/rpcfirewall)  
📝 **Description:** A security tool that audits and filters Remote Procedure Call (RPC) traffic on Windows servers to protect against lateral movement attacks and RPC-based exploits by monitoring and blocking potentially malicious RPC requests.

</details>

<details><summary><strong>SMBeagle: SMB Share Hunter</strong> — Daniel Oates-Lee, Chris Morris</summary>

**Track:** Network Defense · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/punk-security/smbeagle](https://github.com/punk-security/smbeagle)  
📝 **Description:** A cross-platform SMB file share auditing tool that scans networks for accessible files and reports their read/write permissions, with findings exportable to CSV or Elasticsearch.

</details>

<details><summary><strong>Wireshark Forensics Toolkit</strong> — Rishikesh Bhide</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/rjbhide/wireshark-forensics-plugin](https://github.com/rjbhide/wireshark-forensics-plugin)  
📝 **Description:** Wireshark is the most widely used network traffic analyzer. It is an important tool for both live traffic analysis & forensic analysis for forensic/malware analysts. Even though Wireshark provides incredibly powerful functionalities for protocol parsing & filtering, it does not provide any contextual information about network endpoints. For a typical analyst, who has to comb through GBs of PCAP files to identify malicious activity, it's like finding a needle in a haystack. Wireshark Forensics Toolkit is a cross-platform Wireshark plugin that correlates network traffic data with threat intelligence, asset categorization & vulnerability data to speed up network forensic analysis. It does it by extending Wireshark native search filter functionality to allow filtering based on these additional contextual attributes. It works with both PCAP files and real-time traffic captures. This toolkit provides the following functionality - Loads malicious Indicators CSV exported from Threat Intelligence Platforms like MISP and associates it with each source/destination IP from network traffic - Loads asset classification information based on IP-Range to Asset Type mapping which enables filtering incoming/outgoing traffic from a specific type of assets (e.g. filter for 'Database Server', 'Employee Laptop' etc) - Loads exported vulnerability scan information exported from Qualys/Nessus map IP to CVEs. - Extends native Wireshark filter functionality to allow filtering based severity, source, asset type & CVE information for each source or destination IP address in network logs

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>UART Brute Forcing</strong> — Andrew Blyth</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2021  
🔗 **Link:** Not Available  
📝 **Description:** A Python script that brute-forces login credentials via a serial (UART) connection on embedded devices.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>IDA2Obj: An Innovative Tool for Static Binary Instrumentation</strong> — Mickey Jin</summary>

**Track:** Reverse Engineering · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/jhftss/IDA2Obj](https://github.com/jhftss/IDA2Obj)  
📝 **Description:** As well known, object files are generated by c/c++ compiler or assembler from source code, and linked into an executable binary. But now, I can directly dump multiple object files just from one executable binary (exe, dll, ...) by using this tool. What's more amazing is that they can be linked again to a new binary, which is almost same as the old one ! It is designed mainly for SBI (Static Binary Instrumenation), to collect code coverage and integrate with popular fuzzing engines (AFL, honggfuzz, ...). Of course, it is faster than all of the DBI solutions.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>RAT Exploitation Tool for Social Networks</strong> — Omar Alibrahim, Basel Alothman</summary>

**Track:** Human Factors · **Event:** Europe 2021  
🔗 **Link:** [https://github.com/jawaharputti/TheFatRat-a-Massive-Exploiting-Tool](https://github.com/jawaharputti/TheFatRat-a-Massive-Exploiting-Tool)  
📝 **Description:** As we all know, many risks are involved with social networks such as impersonation, social-engineering, and data breach. To demonstrate these attacks, we developed an innovative tool that can hijack and remotely control social network accounts by combining the powers of social engineering with malicious third party apps. We built a private app store of phishing apps, with genres, that a bad actor can choose from to gain RAT control over victim accounts. To enable this, our tool manages oauth tokens within a single web console, allowing the hacker to exercise the functions of the victim accounts. To this end, we discuss other features and extensions of our tool, such as social engineering chat bots, crawlier bots, password crackers, and visualization tools for social network analytics.

</details>

---
