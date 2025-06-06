# USA 2018
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2018** event held in **USA**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
---
## 🌐 Web/AppSec
<details><summary><strong>A Look at ModSec 3.0 for NGINX: A Software Web Application Firewall</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Kevin Jones](https://img.shields.io/badge/Kevin%20Jones-informational)

🔗 **Link:** [A Look at ModSec 3.0 for NGINX: A Software Web Application Firewall](https://github.com/cranelab/webapp-tech)  
📝 **Description:** Today more and more websites are becoming subject to the constant and malevolent barrage coming from malicious hackers. A websites name can be tarnished quickly by a simple breach of their application stack. Web application security is becoming more and more a crucial part of the IT infrastructure, but what exactly does a WAF do and why do you need it? In this talk we will answer those questions.

We will first take a look at how the popular and highly adopted open source proxy server known as NGINX can be combined with the long respected open source web application firewall known as ModSecurity to achieve an effective and highly secure layer for your web application stack. We will explain the detailed benefits that NGINX and ModSecurity can provide, including protection from layer 7 attacks such as XSS, SQLi and LFI. We will showcase how the combination of these technologies can automatically block traffic from known malicious IP addresses. We will cover the visibility and auditing ModSecurity can provide from its detailed log files.

Lastly, we will walk through the setup process and configurations so that after attending this session you can easily and quickly setup NGINX and ModSecurity as a effective and highly secure web application firewall.

</details>

<details><summary><strong>Astra: Automated Security Testing For REST APIs</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ankur Bhargava](https://img.shields.io/badge/Ankur%20Bhargava-informational) ![Prajal Kulkarni](https://img.shields.io/badge/Prajal%20Kulkarni-informational) ![Sagar Popat](https://img.shields.io/badge/Sagar%20Popat-informational)

🔗 **Link:** [Astra: Automated Security Testing For REST APIs](https://github.com/Surya443/NIT-Hackathon2023/blob/main/Indian%20Startup.csv)  
📝 **Description:** REST API penetration testing is complex due to continuous changes in existing APIs and addition of new APIs. Astra (Sanskrit: अस्त्र) can be used by security engineers or developers as an integral part of their process, so they can detect and patch vulnerabilities in the initial phase of the development cycle. Astra can automatically detect and test login & logout (Authentication API), which makes it easy for anyone to integrate this into CICD pipeline. Astra can take API collection as an input so this can also be used for testing APIs in stand-alone mode.

</details>

<details><summary><strong>Burp Replicator: Automate Reproduction of Complex Vulnerabilities</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Paul Johnston](https://img.shields.io/badge/Paul%20Johnston-informational)

🔗 **Link:** [Burp Replicator: Automate Reproduction of Complex Vulnerabilities](https://github.com/rajendrac3/Machine-Learning/blob/master/Apply%20Naive%20Bayes%20on%20Amazon%20reviews/Naive%20Bayes.ipynb)  
📝 **Description:** Developers often struggle to reproduce vulnerabilities discovered during pen tests. This is especially true for complex issues that need to bypass JavaScript validation, work with multi-step forms, handle dynamic CSRF tokens and more. This does not fit well with agile development where the ability to quickly reproduce problems enables efficient test driven development. Replicator solves this issue by allowing a pen tester to create a reproduction script that a developer can use on their system. Complex vulnerabilities can be confirmed with a single click, allowing the developer to stay in their productive coding flow. The tool is fully integrated with Burp Suite, making the script greatly easier to produce than a shell script, and keeping the tester in productive flow.

</details>

<details><summary><strong>OWASP JoomScan Project</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Babak Amin Azad](https://img.shields.io/badge/Babak%20Amin%20Azad-informational) ![Mohammad Reza Espargham](https://img.shields.io/badge/Mohammad%20Reza%20Espargham-informational) ![Vahid Behzadan](https://img.shields.io/badge/Vahid%20Behzadan-informational)

🔗 **Link:** Not Available  
📝 **Description:** OWASP Joomla! Vulnerability Scanner (JoomScan) is an open source project, developed with the aim of automating the task of vulnerability detection and reliability assurance in Joomla CMS deployments. Implemented in Perl, this tool enables seamless and effortless scanning of Joomla installations, while leaving a minimal footprint with its lightweight and modular architecture. It not only detects known offensive vulnerabilities, but also is able to detect many misconfigurations and admin-level shortcomings that can be exploited by adversaries to compromise the system. Furthermore, OWASP JoomScan provides a user-friendly interface and compiles the final reports in both text and HTML formats for ease of use and minimization of reporting overheads.
OWASP JoomScan is included in Kali Linux distributions.

Source Code: https://github.com/rezasp/joomscan

</details>

<details><summary><strong>OWASP Offensive Web Testing Framework</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Viyat Bhalodia](https://img.shields.io/badge/Viyat%20Bhalodia-informational)

🔗 **Link:** [OWASP Offensive Web Testing Framework](https://github.com/owtf/owtf/blob/develop/SECURITY.md)  
📝 **Description:** OWASP OWTF is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST so that pentesters will have more time to

See the big picture and think out of the box
More efficiently find, verify and combine vulnerabilities
Have time to investigate complex vulnerabilities like business logic/architectural flaws
Perform more tactical/targeted fuzzing on seemingly risky areas
Demonstrate true impact despite the short timeframes we are typically given to test

OWTF is highly configurable and anybody can trivially create simple plugins or add new tests in the configuration files without having any development experience.

</details>

<details><summary><strong>ThreatPlaybook</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Abhay Bhargav](https://img.shields.io/badge/Abhay%20Bhargav-informational) ![Sharath Kumar](https://img.shields.io/badge/Sharath%20Kumar-informational)

🔗 **Link:** Not Available  
📝 **Description:** Threat Modeling is currently performed as a 'static' exercise, where the security team creates threat models as documents. These documents tend to be largely unused by anyone after the threat model and ends up being a static document. ThreatPlaybook is a "Threat Modeling as Code" framework, where you can capture Threat Models in a "playbook style" manner. Once you do, you can automatically generate diagrams, use the Threat Models to run application security automation like Vulnerability Scanning, etc.

The key benefits of ThreatPlaybook is that you can:
* Codify Threat Models for Iterative Threat Modeling
* Use Threat Models and Security Test Cases to launch targeted application security automation that can be used in a CI/CD environment or by pen testers who want to automate several tasks in their "Pentest Pipeline"
* Auto-generate Process Flow Diagrams from Codified Threat Models
* Capture Security Test Cases linked to Threat Modeling
* Generate reports correlating Threat Models to Vulnerabilities, Security Test Cases and so on.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>ADA: Android Dynamic Analysis Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Anelkaos *](https://img.shields.io/badge/Anelkaos%20*-informational)

🔗 **Link:** Not Available  
📝 **Description:** ADA analyzes the dynamic behavior of an Android application in runtime. ADA discovers the attack surface that is not shown during the static analysis and performs a rapid vulnerability assessment of the application.

ADA discovers the best attack path to follow to compromise the application. The automated dynamic analysis is focused on discovering the security measures implemented in the application. In this way, ADA shows the best attack path to compromise the application. Some of the features that ADA detects are whether the application uses certificate pinning, JNI libraries, SQL database discovery, KeyStores identification, hardware-backed KeyStore (TEE), etc.

</details>

<details><summary><strong>Adversarial Robustness Toolbox for Machine Learning Models - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Irina Nicolae](https://img.shields.io/badge/Irina%20Nicolae-informational)

🔗 **Link:** [Adversarial Robustness Toolbox for Machine Learning Models - ARSENAL THEATER DEMO](https://gist.github.com/standardgalactic/7f03809c56f4b098b95a50ada32cd02c)  
📝 **Description:** Adversarial attacks of machine learning systems have become an undisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). Adversarial attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defence methods for machine learning models. It provides an implementation for many state-of-the-art methods for attacking and defending machine learning. Through ART, the attendees will (re)discover how to attack and defend machine learning systems.

</details>

<details><summary><strong>Archery: Open Source Vulnerability Assessment and Management - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational)

🔗 **Link:** [Archery: Open Source Vulnerability Assessment and Management - ARSENAL THEATER DEMO](https://github.com/google-research-datasets/gap-coreference/blob/master/gap-test.tsv)  
📝 **Description:** Archery is an open-source vulnerability assessment and management tool that helps developers and pentesters to perform scans and manage vulnerabilities. Archery uses popular open-source tools to perform comprehensive scanning for web application and network. It also performs web application dynamic authenticated scanning and covers the whole applications by using selenium. The developers can also utilize the tool for implementation of their DevOps CI/CD environment.

The main capabilities of our Archery include:

Perform Web and Network Vulnerability Scanning using vulnerability scanner tools
Correlates and Collaborate all raw scans data, show them in a consolidated manner
Perform authenticated web scanning
Perform web application scanning using selenium
Automate your scanners
Vulnerability Management including Web, Network and Mobile Applications
Enable REST API's for developers to perform scanning and Vulnerability Management
Useful for DevOps teams for Vulnerability Management

</details>

<details><summary><strong>boofuzz</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Joshua Pereyda](https://img.shields.io/badge/Joshua%20Pereyda-informational)

🔗 **Link:** [boofuzz](https://github.com/jtpereyda)  
📝 **Description:** boofuzz is an open-source network protocol fuzzing framework, competing with closed source commercial products like Defensics and Peach. Inheriting from the open source tools Spike and Sulley, boofuzz improves on a long line of block-based fuzzing frameworks.

The fuzzing framework allows hackers to specify protocol formats, and boofuzz does the heavy lifting of generating mutations specific to the format. boofuzz makes developing protocol-specific "smart" fuzzers relatively easy. Make no mistake, designing a smart network protocol fuzzer is no trivial task, but boofuzz provides a solid foundation for producing quality fuzzers.

Written in Python, boofuzz builds on its predecessor, Sulley, with key features including:

Online documentation
More extensibility including support for arbitrary communications mediums
Built-in support for serial fuzzing, ethernet- and IP-layer, UDP broadcast
Much easier install experience!
Far fewer bugs

Source Code: https://github.com/jtpereyda/boofuzz

</details>

<details><summary><strong>BTA</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Joffrey CZARNY](https://img.shields.io/badge/Joffrey%20CZARNY-informational)

🔗 **Link:** [BTA](https://github.com/atktgs/BlackHat2015Arsenal)  
📝 **Description:** When it comes to the security of the information system, Active Directory domain controllers are, or should be, at the center of concerns, which are (normally) to ensure compliance with best practices, and during a compromise proved to explore the possibility of cleaning the information system without having to rebuild Active Directory. However, few tools implement this process; there are more and more offensive tools to target Active Directory and several ways exist to backdoor Active Directory.

We propose to present some possible backdoors which could be set by an intruder in Active Directory to keep administration rights. For example, how to modify the AdminSDHolder container in order to reapply rights after administrator actions. Moreover, backdoors can be implemented in Active Directory to help an intruder to gain back his privileges. Then, we will present the last features in BTA, which help to detected all mis-configurations that can be abused to bypass Administrative Forest Design Approach "ESAE", as DCsync rights, Exchange privileges...

The presentation will be organized as follows:

We begin by demonstrating some backdoors in order to keep admins rights or to help an intruder to quickly recover admins rights.
We will continue by describing all mis-configurations that can be abused to bypass ESAE design, as DCsync rights, Exchange privileges...
We conclude with a feedback on real world usage of BTA.

More information can be found on the Bitbucket repository: https://github.com/airbus-seclab/bta

</details>

<details><summary><strong>Deep Exploit</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational)

🔗 **Link:** [Deep Exploit](https://github.com/TheDreamPort/deep_exploit)  
📝 **Description:** DeepExploit is fully automated penetration tool linked with Metasploit. It identifies the status of all opened ports on the target server and executes the exploit at pinpoint using Machine Learning.

Deep Exploit's key features are the following:

Self-learning: DeepExploit can learn how to exploitation by itself (uses reinforcement learning). It is not necessary for humans to prepare learning data.
Efficiently execute exploit: DeepExploit can execute exploits at pinpoint (minimum 1 attempt) using self-learned data.
Deep penetration: If DeepExploit succeeds the exploit to the target server, it further executes the exploit to other internal servers.
Operation is very easy: Your only operation is to input one command. It is very easy!
Learning time is very fast: DeepExploit uses distributed learning by multi agents. So, we adopted an advanced machine learning model called A3C.

Current Deep Exploit's version is a beta, but it can fully automatically execute following actions:

Intelligence gathering
Threat modeling
Vulnerability analysis
Exploitation
Post-Exploitation
Reporting

By using our DeepExploit, you will benefit from the following:

For pentesters: (a) They can greatly improve the test efficiency; (b) The more pentesters use DeepExploit, DeepExploit learns how to method of exploitation using machine learning. As a result, accuracy of test can be improve.
For Information Security Officers: (c) They can quickly identify vulnerabilities of own servers. As a result, prevent that attackers attack to your servers using vulnerabilities, and protect your reputation by avoiding the negative media coverage after breach.

Because attack methods to servers are evolving day by day, there is no guarantee that yesterday's security countermeasures are safety today. It is necessary to quickly find vulnerabilities and take countermeasures. Our DeepExploit will contribute greatly to keep your safety.

Source Code:
https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit

Document:
https://github.com/13o-bbr-bbq/machine_learning_security/blob/master/DeepExploit/doc/BHUSA2018Arsenal_20180802.pdf﻿

</details>

<details><summary><strong>Halcyon IDE: For Nmap Script Developers</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Sanoop Thomas](https://img.shields.io/badge/Sanoop%20Thomas-informational)

🔗 **Link:** [Halcyon IDE: For Nmap Script Developers](https://github.com/s4n7h0/Halcyon-IDE)  
📝 **Description:** Halcyon IDE lets you quickly and easily develop Nmap scripts for performing advanced scans on applications and infrastructures with a wide range capabilities from recon to exploitation. It is the first IDE released exclusively for Nmap script development. Halcyon IDE is free and open source project (always will be) released under MIT license to provide an easier development interface for rapidly growing information security community around the world. The project was initially started as an evening free time "coffee shop" project and has taken a serious step for its developer/contributors to spend dedicated time for its improvements very actively.

Source Code: https://halcyon-ide.org﻿

</details>

<details><summary><strong>Jackhammer: One Security Vulnerability Assessment/Management Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Madhusudhan Konda](https://img.shields.io/badge/Madhusudhan%20Konda-informational) ![Rajagopal Vallopilly Reghunadhan Nair](https://img.shields.io/badge/Rajagopal%20Vallopilly%20Reghunadhan%20Nair-informational) ![Shreyas Chidambara](https://img.shields.io/badge/Shreyas%20Chidambara-informational)

🔗 **Link:** Not Available  
📝 **Description:** Jackhammer is an integrated tool suite which comes with out-of-the-box industry standard integrations. It is a first of its kind tool that combines static analysis, dynamic web app analysis, mobile security, API security, network security, CMS security, AWS/Azure security tools, docker/container security, and vulnerability manager that gives a complete glimpse into security posture of the organization. Using this suite, even senior leadership can have a comprehensive view of their organization's security.

Why was it needed?
Security, while being imperative for any organization, it is hard to comprehend by most of the developers. Security engineers need to scrutinize every service or app turning security analysis a time intensive and repetitive. What if there exists a tool that can empower everyone to test their code for vulnerabilities, automate security analysis, and show the overall security hygiene of the company?

How does it work?
Jackhammer intiates various types of scans using existing proven tools and the results are consumed by onboard vulnerability manager. Unique dashboard presents intuitive interface giving the user a holistic view of the code base. The normalized reports are instantly accessible to Developers, QAs, TPMs, and security personnel.

It can be plugged/integrated with:

CI systems and Git via hooks giving complete control over code commits
AWS/Azure account and can keep on scanning complete IP space in realtime
Additional commercial/open source tools within few minutes and manage those tools from jackhammer
Ticketing systems (like Jira)
slack/pagerduty for real time alerting in addition to SMS and emails

It creates a sandbox using dockers for every tool and scales the systems when the scan needs it and descale on completion of the scans. The spin-up and tear down is a completely automated process so no person needs to look at the resources making it inexpensive and cost-effective.

</details>

<details><summary><strong>SimpleRisk: ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

🔗 **Link:** [SimpleRisk: ARSENAL THEATER DEMO](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk, via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

Source Code: https://github.com/simplerisk

</details>

<details><summary><strong>TROMMEL - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Kyle O'Meara](https://img.shields.io/badge/Kyle%20O'Meara-informational)

🔗 **Link:** Not Available  
📝 **Description:** TROMMEL is a custom, open-source tool using Python to assist researchers during embedded device vulnerability analysis. TROMMEL sifts through embedded device files to identify potential vulnerable indicators. TROMMEL has also integrated vFeed Community Database which allows for further in-depth vulnerability analysis of identified indicators.

Source Code: https://github.com/CERTCC/trommel

</details>

<details><summary><strong>V2X Validation Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Jonathan Petit](https://img.shields.io/badge/Jonathan%20Petit-informational) ![Raashid Ansari](https://img.shields.io/badge/Raashid%20Ansari-informational)

🔗 **Link:** [V2X Validation Tool](https://github.com/ryanbgriffiths/IROS2023PaperList/blob/main/README.md)  
📝 **Description:** The V2X Validation Tool (called dsrcvt because focused on DSRC technology) facilitates penetration testing on automotive On-Board Units (OBUs) used for Vehicle-to-X communication. Currently, dsrcvt is capable of sending unsigned or signed Basic Safety Messages (BSMs) by re-signing a recorded BSM sent for automotive onboard units. Using these BSMs it tries to cause a surge in an OBU's processing power. It also attempts to bypass the security checks posed by the IEEE 1609.2 security layer. An enhanced version of dsrcvt (dsrcvt-crafter) facilitates crafting entirely custom BSMs from scratch, conforming to the IEEE 1609 standards family. dsrcvt also comes as an OBU fuzzer that can fuzz user-selected fields of a BSM to pen-test OBU implementations.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>ADRecon: Active Directory Recon</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Prashant Mahajan](https://img.shields.io/badge/Prashant%20Mahajan-informational)

🔗 **Link:** [ADRecon: Active Directory Recon](https://github.com/adrecon/ADRecon)  
📝 **Description:** ADRecon is a tool which extracts various artifacts (as highlighted below) out of an AD environment in a specially formatted Microsoft Excel report that includes summary views with metrics to facilitate analysis. The report can provide a holistic picture of the current state of the target AD environment. The tool is useful to various classes of security professionals like system administrators, security professionals, DFIR, etc. It can also be an invaluable post-exploitation tool for a penetration tester. It can be run from any workstation that is connected to the environment, even hosts that are not domain members. Furthermore, the tool can be executed in the context of a non-privileged (i.e. standard domain user) accounts. Fine Grained Password Policy, LAPS and BitLocker may require Privileged user accounts. The tool will use Microsoft Remote Server Administration Tools (RSAT) if available, otherwise it will communicate with the Domain Controller using LDAP.

The following information is gathered by the tool: Forest; Domain; Trusts; Sites; Subnets; Default Password Policy; Fine Grained Password Policy (if implemented); Domain Controllers, SMB versions, whether SMB Signing is supported and FSMO roles; Users and their attributes; Service Principal Names (SPNs); Groups and memberships; Organizational Units (OUs); ACLs for the Domain, OUs, Root Containers and GroupPolicy objects; Group Policy Object details; DNS Zones and Records; Printers; Computers and their attributes; LAPS passwords (if implemented); BitLocker Recovery Keys (if implemented); and GPOReport (requires RSAT).

Available at https://github.com/sense-of-security/ADRecon

</details>

<details><summary><strong>Armory</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Daniel Lawson](https://img.shields.io/badge/Daniel%20Lawson-informational)

🔗 **Link:** [Armory](https://github.com/depthsecurity/armory-docker/blob/master/launch_api.sh)  
📝 **Description:** Armory is a tool designed to run various existing tools, collating all of the output into a local database, and using that information for further attacks. It is extremely modular, and it is pretty easy to create custom modules and reports. Armory's purpose is to streamline client discovery and external penetration tests.

</details>

<details><summary><strong>BloodHound 1.5</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Andy Robbins](https://img.shields.io/badge/Andy%20Robbins-informational) ![Rohan Vazarkar](https://img.shields.io/badge/Rohan%20Vazarkar-informational) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational)

🔗 **Link:** [BloodHound 1.5](https://github.com/chryzsh/awesome-bloodhound)  
📝 **Description:** BloodHound is a single page Javascript web application, built on top of Linkurious, compiled with Electron, with a Neo4j database fed by a PowerShell ingestor. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory environment. BloodHound is developed by @_wald0, @CptJesus, and @harmj0y.

</details>

<details><summary><strong>Chiron: An Advanced IPv6 Security Assessment and Penetration Testing Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Antonios Atlasis](https://img.shields.io/badge/Antonios%20Atlasis-informational)

🔗 **Link:** [Chiron: An Advanced IPv6 Security Assessment and Penetration Testing Framework](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Network_Attacks.md)  
📝 **Description:** Chiron is an IPv6 Security Assessment Framework, written in Python and employing Scapy. It is comprised of the following modules:

• IPv6 Scanner
• IPv6 Local Link
• IPv4-to-IPv6 Proxy
• IPv6 Attack Module
• IPv6 Proxy
All the above modules are supported by a common library that allows the creation of completely arbitrary IPv6 header chains, fragmented or not. Suggested host OS: Linux (*BSD may also work).

Source Code: https://github.com/aatlasis/Chiron﻿

</details>

<details><summary><strong>CoffeeShot: Avoid Detection with Memory Injection</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Asaf Aprozper](https://img.shields.io/badge/Asaf%20Aprozper-informational)

🔗 **Link:** [CoffeeShot: Avoid Detection with Memory Injection](https://github.com/MinervaLabsResearch/CoffeeShot)  
📝 **Description:** For the first time ever, we are introducing a framework that utilizes the usage of Java Native Access with Java. How did we take advantage of that? Well, we used this to call to interesting Windows API's directly from Java. CoffeeShot is a framework that was designed for creating Java-based malware which bypasses most of the anti-virus vendors. CoffeeShot utilizes the features of JNA to look for a victim process, once it finds it - a shellcode will be injected directly from the Java Archive file (JAR).

Java malware like "Jrat" and "Adwind" are used by malicious adversaries day by day, more and more. Their main reason for writing malware in Java is to be evasive and avoid security products – including those that use advanced features like machine learning. To overcome the above, blue-teamers can use this framework and thereby understand their status of anti-malware weakness against Java-based malware.

On the other hand, CoffeeShot can be applied by penetration testers as well. The framework provides red-teamers a friendly toolset by allowing them to embed any shellcode in a JAR file, assisting them to avoid detection with memory injection and to PWN the target!

</details>

<details><summary><strong>DELTA: SDN Security Evaluation Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jinwoo Kim](https://img.shields.io/badge/Jinwoo%20Kim-informational) ![Seungsoo Lee](https://img.shields.io/badge/Seungsoo%20Lee-informational) ![Seungwon Shin](https://img.shields.io/badge/Seungwon%20Shin-informational) ![Seungwon Woo](https://img.shields.io/badge/Seungwon%20Woo-informational)

🔗 **Link:** [DELTA: SDN Security Evaluation Framework](https://github.com/seungsoo-lee/DELTA)  
📝 **Description:** Software-Defined Networking (SDN) allows network operators to manage the entire network in a centralized manner by separating the vendor specific control plane from legacy routers/switches. Thus, this concept provides an intelligent way to design novel network functions. However, although SDN offers significant advantages over the traditional networking, the security of SDN has not been sufficiently verified. So, here, we introduce an open source tool for systematically assessing the security of SDN called DELTA.

DELTA is a first SDN security evaluation framework, which has two primary functions; (1) It can automatically instantiate known attack cases against SDN elements across diverse environments, and (2) it can assist in uncovering unknown security problems within an SDN deployment. For replaying attack cases, our framework has a number of test cases against open source SDN controllers and all SDN-enabled switch devices (software and hardware). Also, our framework provides a protocol-aware fuzzer for OpenFlow, which is a de-facto standard protocol of SDN, in order to find new vulnerabilities.

DELTA has following main features:

Fully automatically reproduce 40 published exploits against all SDN components composed of SDN controllers, a control channel, and OpenFlow-enabled switches.
Provide a blackbox fuzzing module that randomizes OpenFlow messages.
Support for both VM-based all-in-one single machine and hardware-based environments.
Fully compatible with promising SDN controllers (ONOS, OpenDaylight, Floodlight, and Ryu).
[NEW] Support additional 7 new attacks against SDN switches (i.e., OVS, HP, and Pica8), which are discovered from DELTA fuzzing module.
[NEW] Support DISTRIBUTED controller testing and related attack cases.
[NEW] Provide a new fuzzing module that discovers security problems of REST-API implementations in SDN controllers and related attack cases.

</details>

<details><summary><strong>DSP: Docker Security Playground</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Simon Pietro Romano](https://img.shields.io/badge/Simon%20Pietro%20Romano-informational)

🔗 **Link:** [DSP: Docker Security Playground](https://github.com/DockerSecurityPlayground/DSP)  
📝 **Description:** This presentation covers the design and implementation of the Docker Security Playground (DSP), an architecture leveraging a microservices-based approach in order to build complex network infrastructures specifically tailored to the study of network security. DSP has been conceived at the outset as a tool for learning network security with a hands-on approach. A number of security labs have been already realized and made available in a public repository. The talk discusses how such labs can be fruitfully exploited by students, as well as presents the Application Programming Interface offered to programmers interested in the implementation of new labs.

</details>

<details><summary><strong>FireDrill: Adversarial Simulation Platform - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Stephan Chenette](https://img.shields.io/badge/Stephan%20Chenette-informational)

🔗 **Link:** Not Available  
📝 **Description:** AttackIQ has released a free Community Edition of it's AttackIQ FireDrill Adversarial Simulation Platform. An open platform, where contributors can create attack scenarios, share and discuss those scenarios in the community and test those scenarios using the Community Edition of our platform. All scenarios are written in python and there is an extensive development community with documentation, videos and other community members to support each other in building scenarios that help validate and test defensive technologies, processes, tools and people against Attacker TTPs. The Community edition gives you full access to the development community and scenarios that have been developed by that community. Useful for both red team/blue team exercises as well as truly being able to test, measure and improve your defensive security controls we're proud to be showcasing the AttackIQ Community Edition at Black Hat this year!

</details>

<details><summary><strong>Foxtrot C2: A Journey of Payload Delivery</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dimitry Snezhkov](https://img.shields.io/badge/Dimitry%20Snezhkov-informational)

🔗 **Link:** [Foxtrot C2: A Journey of Payload Delivery](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)  
📝 **Description:** Execution of an offensive payload may begin with a safe delivery of the payload to the endpoint itself. When secure connections in the enterprise are inspected, reliance only on transmission level security may not be enough to accomplish that goal. Foxtrot C2 serves one goal: safe last mile delivery of payloads and commands between the external network and the internal point of presence, traversing intercepting proxies, with the end-to-end application level encryption.

While the idea of end-to-end application encryption is certainly not new, the exact mechanism of Foxtrot's delivery implementation has advantages to Red Teams as it relies on a well known third party site, enjoying elevated ranking and above average domain fronting features. Payload delivery involves several OpSec defenses: sensible protection from direct attribution, active link expiration to evade consistent interception, inspection, tracking and replay activities by the defenders. Asymmetric communication channels are also planned.

And if your standalone Foxtrot agent is caught, the delivery mechanism may live on, you could still manually bring the agent back into the environment via the browser. A concept tool built on these ideas will be presented and released. It will be used as basis for our discussion.

</details>

<details><summary><strong>Ghost Tunnel: Covert Data Exfiltration Channel to Circumvent Air Gapping - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Hongjian Cao](https://img.shields.io/badge/Hongjian%20Cao-informational) ![Kunzhe Chai](https://img.shields.io/badge/Kunzhe%20Chai-informational) ![YongTao Wang](https://img.shields.io/badge/YongTao%20Wang-informational)

🔗 **Link:** Not Available  
📝 **Description:** In recent years, attacking air gapped networks through HID devices is becoming popular. The HID attack uses the USB interface to forge the user's keystrokes or mouse movement to modify the system settings and run malware. In 2009, NSA's Office of Tailored Access Operations (TAO) developed the COTTON-MOUTH – a USB hardware implant which provides a wireless bridge into a target network as well as the ability to load exploit software onto a target machine. Unlike COTTON-MOUTH, Ghost Tunnel attacks the target through the HID device only to release the payload, and it can be removed after the payload is released.

Advantages:

Covertness
HID attack device is only required to release the payload and it can be removed after that
No interference with the target's existing connection status and communications
Can bypass firewalls
Can be used to attack strictly isolated networks
Communication channel does not depend on the target's existing network connection
Cross-Platform Support
Can be used to attack any device with wireless communication module, we tested this attack on Window 7 up to Windows 10, and OSX

Source Code: https://github.com/360PegasusTeam/GhostTunnel

</details>

<details><summary><strong>hideNsneak: An Attack Obfuscation Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michelle Hodges](https://img.shields.io/badge/Michelle%20Hodges-informational) ![Mike Hodges](https://img.shields.io/badge/Mike%20Hodges-informational)

🔗 **Link:** Not Available  
📝 **Description:** hideNsneak evolved as a tool to expand evasive penetration testing capabilities. It allows users to rapidly deploy, manage, and quickly take down a distributed cloud attack infrastructure by leveraging features of large Cloud Providers and their content delivery networks. Techniques include domain fronting with multiple providers, distributed scanning, and source of attack obfuscation. Leaning on the reputation of these networks allows traffic to more easily blend in to network traffic and create difficulty in blocking attack infrastructure. Furthermore, the ephemeral nature of the tool itself provides a realistic threat simulation, which also simulates the realistic headache this type of attack causes defenders, when they try to attribute actions to certain sets of hosts.

The overview of the toolsets features will contain an explanation of the tactics and techniques in order to provide both red teamers and blue teamers alike with more insight into why this works in "modern" networks, as well as real world scenarios. Also, this tool was written in the Go programming standard in which each functionality is encapsulated in its own package. This allows for users to use the frameworks individual packages in their own projects as well as add components with relative ease. Finally, information will be provided to blue teamers in an effort to provide knowledge that can be brought back and leveraged to increase security posture.

</details>

<details><summary><strong>Humble Chameleon: Eating 2FA for Breakfast</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational)

🔗 **Link:** [Humble Chameleon: Eating 2FA for Breakfast](https://github.com/claissg/humble_chameleon)  
📝 **Description:** By creating a simple tool that performs a man-in-the-middle attack against the HTTP protocol, we can eliminate the need to manually create phishing sites. In addition, this same tool can be used to harvest session cookies from applications that require 2FA, disallow victims from logging out and killing our stolen cookies, hide phishing domains behind legitimate content, categorize phishing domains, serve malware alongside legitimate content, only serve payloads in response to whitelisted requests, and target multiple services at the same time, all without SSL warnings. *Note: This is not just a tool, but a release of a new attack methodology.

</details>

<details><summary><strong>Mallet: An Intercepting Proxy for Arbitrary Protocols</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Rogan Dawes](https://img.shields.io/badge/Rogan%20Dawes-informational)

🔗 **Link:** [Mallet: An Intercepting Proxy for Arbitrary Protocols](https://github.com/sensepost/mallet)  
📝 **Description:** This prsentation will focus on a new open-source intercepting proxy named Mallet, based on the mature and high-performance Netty framework, that wraps it with a drag and drop graph-based graphical user interface and a datastore. In doing so, we gain access to an existing library of protocol implementations, including TLS (and SNI), various compression algorithms, HTTP, HTTP/2, MQTT, REDIS, and many others, and most important, an existing community of developers creating new protocol decoders and encoders, and the associated body of knowledge in this area.

The Mallet user interface closely follows the Netty model, making it simple to construct a pipeline of encoders and decoders by dragging existing codecs, or adding your own codecs or script blocks to a palette, taking the researcher from a simple TCP intercept-and-forward proxy, to a full-blown protocol stack with scriptable processing, with every change being recorded for review and replay in a subsequent connection. As Netty supports a variety of transports, from the common TCP and UDP to SCTP, Serial Port and File, as well as native kqueue and epoll transports, Mallet can be used to intercept all sorts of data, however you may find it.

Source Code: https://github.com/SensePost/Mallet

</details>

<details><summary><strong>POLAR: Accelerating the Search for Vulnerable Functions</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ezra Caltum](https://img.shields.io/badge/Ezra%20Caltum-informational)

🔗 **Link:** Not Available  
📝 **Description:** When developing exploits for complex platforms, finding function relationships between dynamically compiled binaries and its libraries, and representing them in a Graph Database, we can quickly identify exploitation points. In this presentation, I'll discuss Graphs, Binary Relationships and Vulnerable Functions.

</details>

<details><summary><strong>PowerUpSQL: A PowerShell Toolkit for Attacking SQL Serversin Enterprise Environments</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Antti Rantasaari](https://img.shields.io/badge/Antti%20Rantasaari-informational) ![Scott Sutherland](https://img.shields.io/badge/Scott%20Sutherland-informational)

🔗 **Link:** [PowerUpSQL: A PowerShell Toolkit for Attacking SQL Serversin Enterprise Environments](https://github.com/NetSPI/PowerUpSQL)  
📝 **Description:** PowerUpSQL includes functions that support SQL Server discovery, weak configuration auditing, privilege escalation on scale, and post exploitation actions such as OS command execution. It is intended to be used during internal penetration tests and red team engagements. However, PowerUpSQL also includes many functions that can be used by administrators to quickly inventory the SQL Servers in their ADS domain and perform common threat hunting tasks related to SQL Server. This should be interesting to red, blue, and purple teams interested in automating day to day tasks involving SQL Server.

Source Code: https://github.com/netspi/powerupsql
Slides: https://bit.ly/2OxbGYy﻿
Video: https://youtu.be/UX_tBJQtqW0

</details>

<details><summary><strong>RID Hijacking: Maintaining Access on Windows Machines</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sebastián Castro](https://img.shields.io/badge/Sebastián%20Castro-informational)

🔗 **Link:** [RID Hijacking: Maintaining Access on Windows Machines](https://github.com/ustayready/tradecraft/blob/master/offensive-security/persistence/rid-hijacking.md)  
📝 **Description:** The art of persistence is (and will be...) a matter of concern when successfully exploitation is achieved. Sometimes it is pretty tricky to maintain access on certain environments, especially when it is not possible to execute common vectors like creating or adding users to privileged groups, dumping credentials or hashes, deploying a persistent shell, or anything that could trigger an alert on the victim. This statement ratifies why it's necessary to use discrete and stealthy techniques to keep an open door right after obtaining a high privilege access on the target.

What could be more convenient that only use OS resources in order to persist an access? This presentation will provide a new post-exploitation hook applicable to all Windows versions called RID Hijacking, which allows setting desired privileges to an existent account in a stealthy manner by modifying some security attributes. To show its effectiveness, the attack will be demonstrated by using a module which was recently added by Rapid7 to their Metasploit Framework, and developed by the security researcher Sebastián Castro.

</details>

<details><summary><strong>WarBerryPi - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Stella Constantinou](https://img.shields.io/badge/Stella%20Constantinou-informational) ![Yiannis Ioannides](https://img.shields.io/badge/Yiannis%20Ioannides-informational)

🔗 **Link:** Not Available  
📝 **Description:** WarBerryPi was built to be used as a hardware implant during red teaming scenarios where we want to obtain as much information as possible in a short period of time while being as stealthy as possible. The WarBerryPi also includes an intuitive interactive reporting module for viewing the results of each red teaming engagement.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>An Extensible Dynamic Analysis Framework for IoT Devices</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Heng Yin](https://img.shields.io/badge/Heng%20Yin-informational) ![Xunchao Hu](https://img.shields.io/badge/Xunchao%20Hu-informational) ![Yaowen Zheng](https://img.shields.io/badge/Yaowen%20Zheng-informational)

🔗 **Link:** Not Available  
📝 **Description:** As IoT devices are more than ever present in our society, their security is becoming an increasingly important issue. Dynamic analysis has been proved the arsenal to many security applications (e.g., malware analysis, vulnerability discovery, backdoor analysis, etc.). While several dynamic analysis systems(Avatar, FEMU, Firmadyne, etc. ) have been proposed for IoT devices, they either rely on IoT hardware(Avatar), or lack user friendly interfaces for further extension. In this talk, we will present an extensible whole-system dynamic analysis framework for IoT devices. Specifically, on top of QEMU, we build a Pintool-like framework FirmPin, which provides Just-In-Time Virtual Machine Introspection and a plugin architecture with a simple-to-use event-driven programming interface. FirmPin provides the instrumentation at basic block level, system call level and memory access level for both user level and kernel level programs. Currently, FirmPin supports ARM and MIPS and can run customized kernel from Firmadyne project.

To demonstrate the power of FirmPin, we have created two plugins - MalScalpel and FirmFuzzer. MalScalpel is able to collect the instruction trace, system call trace, and unpacked code of the monitored program(e.g., Mirai). FirmFuzzer utilizes FirmPin to collect the execution information of fuzzed IoT applications, and integrates with AFL to conduct efficient fuzzing for IoT applications. In the future, we plan to add tainting, a powerful technique for many security applications, to the system. The ultimate goal of FirmPin is to be a general analysis framework for IoT devices.

Source Code: https://github.com/DeepBitsTechnology/FirmPin﻿

</details>

<details><summary><strong>BLE CTF Project</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Ryan Holeman](https://img.shields.io/badge/Ryan%20Holeman-informational)

🔗 **Link:** [BLE CTF Project](https://github.com/hackgnar/ble_ctf)  
📝 **Description:** The purpose of BLE CTF is to teach the core concepts of Bluetooth low energy client and server interactions. While it has also been built to be fun, it was built with the intent to teach and reinforce core concepts that are needed to plunge into the world of Bluetooth hacking. After completing this CTF, you should have everything you need to start fiddling with any BLE GATT device you can find. Built to run on the esp32 microcontroller, the BLE CTF is a fully functional BLE GATT server which challenges users to utilize fundamental bluetooth communication methods. Focusing on fun and education, the CTF is the first of its kind to help teach hackers how to dive into the world of Bluetooth.

Source Code: https://github.com/hackgnar/ble_ctf

</details>

<details><summary><strong>BLEMystique: Affordable Custom BLE Target</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational)

🔗 **Link:** [BLEMystique: Affordable Custom BLE Target](https://github.com/pentesteracademy/blemystique)  
📝 **Description:** BLEMystique is an ESP32 based custom BLE target which can be configured by the user to behave like one of the multiple BLE devices i.e. Heart rate monitor, Smart Lock, Smart Bottle, Smart band, Smartwatch etc. BLEMystique allows a pentester to play with BLE side of different Smart devices with a single piece of affordable ESP32 chip.

</details>

<details><summary><strong>ChangWei: A Modern Fuzzing Framework for VxWorks System</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jiashui Wang](https://img.shields.io/badge/Jiashui%20Wang-informational) ![Wei Wang](https://img.shields.io/badge/Wei%20Wang-informational) ![Yu Zhou](https://img.shields.io/badge/Yu%20Zhou-informational)

🔗 **Link:** Not Available  
📝 **Description:** VxWorks is the industry's leading real-time operating system. It has been widely used in various industry scenarios, which require real-time, deterministic performance and, in many cases, safety and security certification. Since VxWorks has so much importance in industry, more and more people are working on security problems around it.

Fuzzing is an effective technique to discovery vulnerabilities. Feedback-guided fuzzing, such as AFL(American Fuzzy Lop), has proven its excellent ability in finding vulnerabilities of complex programs. Fuzzing tools using this technique have been widely applied to Linux, MacOS and even Windows, but never to VxWorks. According to the current situation, we design a feedback-guided fuzzing tool named "ChangWei" especially for VxWorks. We take advantage of the instrumentation API of Bochs emulator to measure and extract target coverage in a persistent fuzzing mode, and then generate input samples with the help of AFL mutation engine.

We are going to utilize this tool to assist developers to test their code and find hidden vulnerabilities before they are discovered by malicious attackers. Apart from that, we'd like anyone who has interest in this to help us optimize it and build a powerful tool for the security industry.

</details>

<details><summary><strong>Expl-iot: IoT Security Testing and Exploitation Framework</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Aseem Jakhar](https://img.shields.io/badge/Aseem%20Jakhar-informational)

🔗 **Link:** [Expl-iot: IoT Security Testing and Exploitation Framework](https://github.com/kzwkt/iot-exploit/blob/master/setup.py)  
📝 **Description:** Expl-iot is an open source flexible and extendable framework for IoT Security Testing and exploitation. It will provide the building blocks for writing exploits and other IoT security assessment test cases with ease. Expliot will support most IoT communication protocols, firmware analysis, hardware interfacing functionality and test cases that can be used from within the framework to quickly map and exploit an IoT product or IoT Infrastructure. It will help the security community in writing quick IoT test cases and exploits. The objectives of the framework are:

Easy of use
Extendable
Support for hardware, radio and IoT protocol analysis

We are currently working on the python3 version and will release it in a month. The new Alpha release is envisioned to have support for UART(serial), ZigBee, BLE, MQTT, CoAP (next version will have support for JTAG, I2C and SPI) and few miscellaneous test cases.

Source Code: https://gitlab.com/expliot_framework/expliot

</details>

<details><summary><strong>GRFICS: A Graphical Realism Framework for Industrial Control Simulations - ARSENAL THEATER DEMO</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![David Formby](https://img.shields.io/badge/David%20Formby-informational)

🔗 **Link:** [GRFICS: A Graphical Realism Framework for Industrial Control Simulations - ARSENAL THEATER DEMO](https://github.com/facebookresearch/colorlessgreenRNNs/blob/main/data/linzen_testset/subj_agr_filtered.text)  
📝 **Description:** GRFICS is a graphical realism framework for industrial control simulations designed to lower the barrier to entry for learning about ICS security. This initial version of GRFICS provides a virtual chemical process control network including everything from the plant operator's human machine interface, to a vulnerable programmable logic controller, down to a realistic chemical process simulation being visualized in the Unity 3D game engine. With GRFICS, beginners in ICS security can practice exploiting common ICS vulnerabilities and vividly see the impact of their attacks on the virtual chemical reactor.

</details>

<details><summary><strong>MQTT-PWN: Your IoT Swiss-Army Knife</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Daniel Abeles](https://img.shields.io/badge/Daniel%20Abeles-informational) ![Moshe Zioni](https://img.shields.io/badge/Moshe%20Zioni-informational)

🔗 **Link:** Not Available  
📝 **Description:** MQTT is a machine-to-machine connectivity protocol designed as an extremely lightweight publish/subscribe messaging transport and widely used by millions of IoT devices worldwide. MQTT-PWN intends to be a one-stop-shop for IoT Broker penetration-testing and security assessment operations, as it combines enumeration, supportive functions and exploitation modules while packing it all within command-line-interface with an easy-to-use and extensible shell-like environment.
Built-in abilities/modules:

Credential Brute-Forcer - configurable brute force password cracking to bypass authentication controls
Topic enumerator - establishing comprehensive topic list via continuous and accumulated sampling
Broker information grabber - obtaining and labeling data from an extensible predefined list containing known topics of interest, broker type and version and more
GPS tracker - plotting routes from devices using OwnTracks app and collecting published coordinates, battery usage, connection method etc.
Sonoff exploiter – design to extract passwords and other sensitive information off smart switches

A full circle of scenarios of attack using the tool will be demonstrated.

</details>

<details><summary><strong>WHID Injector and WHID Elite: A New Generation of HID Offensive Devices</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

🔗 **Link:** [WHID Injector and WHID Elite: A New Generation of HID Offensive Devices](https://github.com/xairy/usb-hacking)  
📝 **Description:** WHID Injector was born from the need for cheap and dedicated hardware that could be remotely controlled in order to conduct HID attacks. WHID stands for WiFi HID injector. It is a cheap but reliable piece of hardware designed to fulfill Pentesters needs related to HID Attacks, during their engagements. The core of WHID Injector is mainly an Atmega 32u4 (commonly used in many Arduino boards) and an ESP-12s (which provides the WiFi capabilities and is commonly used in IoT projects). However, during the last months, a new hardware was under R&D (i.e. WHID Elite). It replaces the Wi-Fi capabilities with a 2G baseband. Which extends its wireless capabilities to (potentially) an unlimited working range.

This cute piece of hardware is perfect to be concealed into USB gadgets and used during engagements to get remote shell over an air-gapped environment. In practice, is the dream of any Red Teamer out there. During the Arsenal presentation we will see in depth how WHID Injector and WHID Elite were designed and their functionalities. We will also look which tools and techniques Blue Teams can use to detect and mitigate this kind of attacks.

</details>

<details><summary><strong>ZigDiggity: ZigBee Pentest Toolkit</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Francis Brown](https://img.shields.io/badge/Francis%20Brown-informational) ![Matthew Gleason](https://img.shields.io/badge/Matthew%20Gleason-informational)

🔗 **Link:** [ZigDiggity: ZigBee Pentest Toolkit](https://github.com/BishopFox/zigdiggity)  
📝 **Description:** Introducing ZigDiggity, an entire suite of new ZigBee penetration testing tools to be released by Francis Brown and Matthew Gleason exclusively at Black Hat USA – Arsenal 2018. We'll be publicly releasing a FREE set of ZigBee hacking tools designed specifically for use by security professionals. We will showcase the best-of-breed in both hacking hardware and software (ZigDiggity) that you'll need to build a complete ZigBee penetration toolkit. Each of the key concepts/tools will be accompanied with live hacking demonstrations that will be both exciting as well as educational, including:

ZigBee – disabling home security system door/window alarms via ZigBee DoS attacks
Scaling this same home ZigBee attack to an entire neighborhood by equipping Bishop Fox's DangerDrone with the ZigBee Hacking gear and new ZigDiggity toolset.

We'll also be giving away a fully functional Danger Drone to one lucky audience member, fully equipped and loaded with ZigDiggity hacking capabilities – guaranteed to leave your friends feeling peanut butter and jealous!

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>ANWI (All New Wireless IDS): The $5 WIDS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rishikesh Bhide](https://img.shields.io/badge/Rishikesh%20Bhide-informational) ![Sanket Karpe](https://img.shields.io/badge/Sanket%20Karpe-informational)

🔗 **Link:** Not Available  
📝 **Description:** ANWI is a new type of Wireless Intrusion Detection System which is based on a low cost WiFi module (ESP8266) and can be deployed at physical perimeter of the coverage area. It allows organizations which can't afford expensive WIDS solutions to protect their networks at fraction of the cost involved.

ANWI provides three layers of protection:

Detect the most commonly used WiFi attacks including Evil Twin, Jamming using de-authentication frames, attacks conducted using commonly used WiFi attack frameworks
Block unauthorized WiFi Access Points created in organization premises
Secure organizations AP by performing WiFi Geo-Fencing to prevent access outside of designated perimeter

ANWI supports standalone as well as managed mode for sending alerts. It also has ability to use separate radio for sending alerts as added resiliency.ANWI aims to fulfill the need of WIDS which is inexpensive yet can protect against most of the possible attacks. It is easy to setup and deploy and works on "fire and forget principle". Once the sensors have been configured they can be deployed across the perimeter. The sensors send heartbeat signal and in case any of the sensors goes offline an alert is generated by server. The current production version includes all the above features.

</details>

<details><summary><strong>Art of Dancing with Shackles: Best Practice of App Store Malware Automatic Hunting System</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ju Zhu](https://img.shields.io/badge/Ju%20Zhu-informational) ![Lilang Wu](https://img.shields.io/badge/Lilang%20Wu-informational) ![Moony Li](https://img.shields.io/badge/Moony%20Li-informational)

🔗 **Link:** [Art of Dancing with Shackles: Best Practice of App Store Malware Automatic Hunting System](https://github.com/lilang-wu/iOS-AppStore-Malware-Automatic-Hunting-System)  
📝 **Description:** We all know the iOS system from Apple to be one of the most secure among all popular operating systems. From a technical view, the protection feature of sandbox gardened application, runtime code signing check, hardware level application code packing protection and so forth, and Apple Store security check policy is extremely strict - before any application is released on Apple Store.

However, this is bad news for security vendors, for the defense protection solution has no chance being granted sufficient privilege to detect and defeat attacks in deep level, when end user suffered real APT attack such as PEGASUS. Our tools is aimed at introducing the tricks and lessons of Apple Store apps automatic crawling and security sandbox automatic analysis systems for security researchers and security vendors in the world.

Source Code: https://github.com/dongyangwu/iOS-AppStore-Malware-Automatic-Hunting-System

</details>

<details><summary><strong>Bro: Do You Bro? Beginner to Expert</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Seth Hall](https://img.shields.io/badge/Seth%20Hall-informational)

🔗 **Link:** [Bro: Do You Bro? Beginner to Expert](https://github.com/bro/broctl/blob/master/CHANGES)  
📝 **Description:** The Bro Network Security Monitor is an open-source framework that gives total visibility over network traffic in real-time. Since most cyber attacks cross the network (and hosts themselves can be compromised), threat hunters and incident responders typically rely on network data as a vital source of truth, to reconstruct what really happened (or is happening now) in their environment. Bro is perhaps the best and most widely used tool for network traffic analysis. Join us to learn more about Bro with Seth Hall, longtime Bro developer, and see a demo where he will provide a comprehensive overview of Bro, from introduction to advanced custom scripting.

</details>

<details><summary><strong>CHIRON: Home-Based Network Analytics & Machine Learning Threat Detection Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joseph Zadeh](https://img.shields.io/badge/Joseph%20Zadeh-informational) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational)

🔗 **Link:** Not Available  
📝 **Description:** CHIRON is a home analytics based on ELK stack combined with Machine Learning threat detection framework AKTAION. CHIRON parses and displays data from P0f, Nmap, and BRO IDS. CHIRON is designed for home use and will give great visibility into home internet devices (IOT, Computers, Cellphones, Tablets, etc).

CHIRON is integrated with AKTAION which detects exploit delivery ransomware/phishing. Aktaion will run every 4 hours against bro logs and it has a benign training data set that it compares against environment data set, once AKTAION finishes it produces files with exploit microbehaviors that can be seen in a visualizations by going into the visualization menu and selecting them.

</details>

<details><summary><strong>Cloud Security Suite: One Stop Tool for AWS/GCP/Azure Security Audit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Divya John](https://img.shields.io/badge/Divya%20John-informational) ![Jayesh Chauhan](https://img.shields.io/badge/Jayesh%20Chauhan-informational) ![Shivankar Madaan](https://img.shields.io/badge/Shivankar%20Madaan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Nowadays, cloud infrastructure is pretty much the de-facto service used by large/small companies. Most of the major organizations have entirely moved to cloud. With more and more companies moving to cloud, the security of cloud becomes a major concern. While AWS, GCP & Azure provide you protection with traditional security methodologies and have a neat structure for authorization/configuration, their security is as robust as the person in-charge of creating/assigning these configuration policies. As we all know, human error is inevitable and any such human mistake could lead to catastrophic damage to the environment.

Few vulnerable scenarios:

Your security groups/policies, password policy or IAM policies are not configured properly
S3 buckets and Azure blobs are world-readable
Web servers supporting vulnerable ssl ciphers
Ports exposed to public with vulnerable services running on them
If root credentials are used
Logging or MFA is disabled
And many more such scenarios...

Knowing all this, audit of cloud infrastructure becomes a hectic task! There are a few open source tools which help in cloud auditing but none of them have an exhaustive checklist. Also, collecting, setting up all the tools and looking at different result sets is a painful task. Moreover, while maintaining big infrastructures, system audit of server instances is a major task as well. CS Suite is a one stop tool for auditing the security posture of the AWS/GCP/Azure infrastructures and does OS audits as well. CS Suite leverages current open source tools capabilities and has custom checks added into one tool to rule them all.

</details>

<details><summary><strong>CQSysmonToolkit: Advanced System Monitoring Toolkit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Paula Januszkiewicz](https://img.shields.io/badge/Paula%20Januszkiewicz-informational)

🔗 **Link:** Not Available  
📝 **Description:** Our toolkit has proven to be useful in the 25000 computers environment. It relies on a free Sysmon deployment and its goal is to boost information delivered by the original tool. CQSysmon Toolkit allows you to extract information about what processes have been running in the operating system, get their hashes and submit them into Virus Total for the forensic information about the malware cases. It also allows to extract information into spreadsheet about what types of network connections have been made: what is the destination IP address, which process was responsible for it and who is the owner of IP. The toolkit also allows to extract information about the current system configuration and compare it with the other servers and much more that allows to become familiar of what is going on in your operating system. There is a special bonus tool in a toolkit that allows to bypass some parts of the Sysmon with another tool that allows to spot that situation so that everything stays in control. CQSysmon Toolkit allows you to established detailed monitoring of the situation on your servers and it is a great complement to the existing forensic tools in your organization.

</details>

<details><summary><strong>CyBot: Open-Source Threat Intelligence Chat Bot (Full Circle)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tony Lee](https://img.shields.io/badge/Tony%20Lee-informational)

🔗 **Link:** [CyBot: Open-Source Threat Intelligence Chat Bot (Full Circle)](https://github.com/avinashshenoy97/awesome-python-1/blob/master/README.md)  
📝 **Description:** Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to debut the end result of our research (a chat bot that we affectionately call CyBot) at Black Hat Arsenal Vegas 2017. To build on that momentum we also brought CyBot to Black Hat Europe and Asia to gather more great feedback and ideas from an enthusiastic international crowd. This year's Black Hat Vegas will allow us to share new features that stemmed from Black Hat Asia feedback as well as lessons learned from the global collaboration effort.

Best of all, if you know even a little bit of Python, you can help our collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!

</details>

<details><summary><strong>DARWIN: Real World Use Cases for Covert Wireless</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Arun Mane](https://img.shields.io/badge/Arun%20Mane-informational) ![Rushikesh D. Nandedkar](https://img.shields.io/badge/Rushikesh%20D.%20Nandedkar-informational)

🔗 **Link:** Not Available  
📝 **Description:** DARWIN is a result of an evolution of our covert channel research, where we considered use case of covert channel to facilitate an unmanaged chat in the local radio periphery. DARWIN can be divided into three parts viz., 1. Scripts for covert traffic 2. Mechanism to consume and push the data on terminal (presently we are considering terminal for input and output of the chat messages) 3. Integration (to consume the input from terminal and fit it into the requisite location in IEEE 802.11/IEEE 802.15.4 data link layer frame to ship it over the air and vice versa).

</details>

<details><summary><strong>Deep Information Retrieval for Malware Searching System</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Hyeongjin Byeon](https://img.shields.io/badge/Hyeongjin%20Byeon-informational) ![Junyeon Weon](https://img.shields.io/badge/Junyeon%20Weon-informational) ![Uijung Chung](https://img.shields.io/badge/Uijung%20Chung-informational) ![Wonkyung Lee](https://img.shields.io/badge/Wonkyung%20Lee-informational)

🔗 **Link:** Not Available  
📝 **Description:** More than 300,000 new malware samples are generated everyday, and it is well known that traditional malware detection based on file hash and rules is very vulnerable to variants. It is also getting harder to categorize unknown malware samples because the cost of finding similar samples is increasing. Therefore, the necessity of malware information retrieval system has emerged. Several attempts have been researched to perform this task, but they have limitations in terms of polymorphism, complexity, ambiguity, novelty and so on.

This research seeks to remedy these problems by introducing a deep metric learning method and proposes a new malware retrieval system which has learned a semantic similarities of malware samples. This system could retrieve information from perceptually similar samples as well as structurally similar samples. It could deal with new samples rapidly and roles as a good feature extractor for another tasks like malware classification or categorization. This approach can be easily adapted to other neural network models because it doesn't change the structure of the original network.

In this presentation, we describe the problems that arise when creating a malware retrieval system, and how we solve them. Also we visualize the embedding vectors of malware samples and show the retrieval results to prove the synchronization between our perception on malware and embedding space.

</details>

<details><summary><strong>DeepViolet: SSL/TLS Scanning API & Tools</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Milton Smith](https://img.shields.io/badge/Milton%20Smith-informational)

🔗 **Link:** [DeepViolet: SSL/TLS Scanning API & Tools](https://github.com/spoofzu/DeepViolet/blob/master/src/main/java/com/mps/deepviolet/api/CipherSuiteUtil.java)  
📝 **Description:** DeepViolet TLS/SSL scanner is an information gathering tool to test TLS/SSL configuration on secure web servers. DeepViolet is an API written in Java. Two proof of concept tools implement the API to demonstrate DeepViolet running from the command line or alternatively from a desktop application. Features of DeepViolet include enumeration of web server cipher suites, display X.509 certificate metadata, examine X.509 certificate trust chains, user configurable ciphersuite naming conventions and more. DeepViolet is an OWASP open source project written to help educate the technical community around TLS/SSL and strengthen knowledge of security protocols while strengthen security of web applications. DeepViolet project is always looking for volunteers.

Source Code: https://github.com/spoofzu/DeepViolet

</details>

<details><summary><strong>DejaVu: An Open Source Deception Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Bhadreshkumar Patel](https://img.shields.io/badge/Bhadreshkumar%20Patel-informational) ![Harish Ramadoss](https://img.shields.io/badge/Harish%20Ramadoss-informational)

🔗 **Link:** [DejaVu: An Open Source Deception Framework](https://github.com/bhdresh/Dejavu)  
📝 **Description:** Deception techniques - if deployed well - can be very effective for organizations to improve network defense and can be a useful arsenal for blue teams to detect attacks at very early stage of cyber kill chain. But the challenge we have seen is deploying, managing and administering decoys across large networks is still not easy and becomes complex for defenders to manage this over time. Although there are a lot of commercial tools in this space, we haven't come across open source tools which can achieve this.

With this in mind, we have developed DejaVu which is an open source deception framework which can be used to deploy across the infrastructure. This could be used by the defender to deploy multiple interactive decoys (HTTP Servers, SQL, SMB, FTP, SSH, client side – NBNS) strategically across their network on different VLAN's. To ease the management of decoys, we have built a web-based platform which can be used to deploy, administer and configure all the decoys effectively from a centralized console. Logging and alerting dashboard displays detailed information about the alerts generated and can be further configured on how these alerts should be handled. If certain IP's like in-house vulnerability scanner, SCCM etc. needs to be whitelisted, this can be configured which effectively would mean very few false positives.

Alerts only occur when an adversary is engaged with the decoy, so now when the attacker touches the decoy during reconnaissance or performs authentication attempts this raises a high accuracy alert which should be investigated by the defense. Decoys can also be placed on the client VLAN's to detect client side attacks such as responder/LLMNR attacks using client side decoys. Additionally, common attacks which the adversary uses to compromise such as abusing Tomcat/SQL server for initial foothold can be deployed as decoys, luring the attacker and enabling detection.

</details>

<details><summary><strong>EKTotal</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Keita Nomura](https://img.shields.io/badge/Keita%20Nomura-informational) ![Rintaro Koike](https://img.shields.io/badge/Rintaro%20Koike-informational)

🔗 **Link:** Not Available  
📝 **Description:** "EKTotal" is an integrated analysis tool that can automatically analyze the traffic of Drive-by Download attacks. The proposed software package can identify four types of Exploit Kits such as RIG and Magnitude, and more than ten types of attack campaigns such as Seamless and Fobos. EKTotal can also extract exploit codes and malware. The proposed heuristic analysis engine is based on Exploit Kit tracking research conducted since 2017, and is known as team "nao_sec". EKTotal provides a user-friendly web interface and powerful automated analysis functions. Thus, EKTotal can assist SOC operators and CSIRT members and researchers.

Drive-by download attacks are still actively conducted. Such attacks are continually changing and becoming more complex. At the beginning of 2017, attack campaigns targeting compromised websites were widespread. However, majority of the current attack campaigns are based on malvertising. Furthermore, in March 2018, several Exploit Kits began to exploit the critical vulnerability named CVE-2018-4878, which in turn is a significant threat. Various tools are available for analyzing malicious traffic. However, it's necessary to employ a combination of such tools or possess their knowledge for analyzing malicious traffic. Hence, EKTotal has been developed for conducting security analysis in a simplified manner.

EKTotal is an all-in-one malicious traffic analysis and processing tool that functions by submitting files of "pcap" or "saz" format. After identifying the attack campaign and associated Exploit Kit through multiple filters, EKTotal extracts the obfuscated exploit code from the traffic data, deobfuscates it, and decrypts the encrypted malware. For example, in the case of RIG Exploit Kit, EKTotal deobfuscates multiple obfuscated JavaScript codes, extracts all exploit codes and malware decryption keys, and thereby decrypts the malware encrypted with RC4.

</details>

<details><summary><strong>Eventpad: Rapid and Cost Effective Malware Analysis Using Visual Analytics</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Bram Cappers](https://img.shields.io/badge/Bram%20Cappers-informational)

🔗 **Link:** Not Available  
📝 **Description:** The analysis of malware behavior in network activity and event logs is a costly and time-consuming task. Even with automated techniques, inspection of network traffic in tools such as Wireshark is often tedious and overwhelming due to the many packet details.

We need faster techniques to speedup the discovery of malware activity and gain insight in our event logs by combining machine learning and visualization together. To this end we developed "Eventpad - the notepad editor for event data", a tool that enables analysts to quickly analyze network traffic by exploiting the human mind. Eventpad is a visual analytics tool that enables analysts to visually inspect system events as blocks on a screen. Just like a notepad editor find&replace, conditional formatting, and rewrite functionality can be used to accurately search and highlight system vulnerabilities in these block collections. Together with automated techniques such as clustering and multiple sequence alignment analysts can quickly drill down and extract nontrivial patterns and threat indicators from network conversations and event logs.

We demonstrate how we can use Eventpad to quickly discover patterns in PCAP DPI traffic. In particular, we give live demos on how we can use the tool to discover protocol misusage in VoIP traffic and reverse engineer Ransomware viruses in back office environments.

</details>

<details><summary><strong>Firmware Audit: Platform Firmware Security Automation for Blue Teams and DFIR</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Lee Fisher](https://img.shields.io/badge/Lee%20Fisher-informational) ![Paul English](https://img.shields.io/badge/Paul%20English-informational)

🔗 **Link:** [Firmware Audit: Platform Firmware Security Automation for Blue Teams and DFIR](https://github.com/viktorbezdek/awesome-github-projects)  
📝 **Description:** The first major release of our platform firmware security automation tool, Firmware Audit, aka: fwaudit. fwaudit automates the running and forensic hashing of output and firmware blobs for a variety of platform firmwares and across a variety of FOSS tools. fwaudit provides a pre-composed profiles for defense, exploration and forensics, to reduce the risk of bricking and maximize operational uptime.

</details>

<details><summary><strong>Hunting Wargames with Arthur and Merlin in IOC-Land</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Lior Kolnik](https://img.shields.io/badge/Lior%20Kolnik-informational)

🔗 **Link:** Not Available  
📝 **Description:** APT reports and IOC updates are flowing in, piling up in your inbox. You forward them to your IR team, or curate and compile a digest if you are lucky enough to have a budget for a dedicated threat intel team. Everyone talks about tracking bad guys and creating threat intel, but - how many organizations are equipped to consume threat intel today? Everyone is pitching new IOCs but is how many are really catching?

The real question is - if you got all the answers to the APT riddle right now, would you be able to scope and respond effectively?
Do you have the tools and process in place, and trained your people to be able to leverage threat intel the moment it becomes available, and how can you know for sure that you are prepared and it will all work at the moment of truth?
And how do you verify that your queries, rules and IOC scans would actually find anything?

This presentation will release a new automated system for testing the IOC consumption capability of an enterprise. Borrowing a page or two from modern software development and computer science theory, this system is built in the model of a prover (Merlin) and a verifier (Arthur).

The presentation will include a live demo of the system on a real environment. Finally, the code to implement this process will be open sourced on Github, so that the community can use it, expand on the initial features and contribute their improvements.

</details>

<details><summary><strong>Kemon: An Open-Source Pre and Post Callback-Based Framework for macOS Kernel Monitoring</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yu Wang](https://img.shields.io/badge/Yu%20Wang-informational)

🔗 **Link:** [Kemon: An Open-Source Pre and Post Callback-Based Framework for macOS Kernel Monitoring](https://github.com/karteum/starred)  
📝 **Description:** If third-party vendors want to add new features to the macOS kernel, such as antivirus capabilities, ransomware blocking, data breach auditing, behavior monitoring and so on, they usually need the support of the system's exported interfaces. At present, only two known official interfaces are available, they are Kernel Authorization subsystem and Mandatory Access Control framework. Unfortunately, neither of them are suitable for today's kernel development tasks. The Kernel Authorization KPIs was designed thirteen years ago and it is clear that it lacks the necessary maintenance and upgrades. For example, there are only seven file operation related notification callbacks available, which are obviously not enough. For each notification callback (KAUTH_SCOPE_FILEOP), we cannot modify the return results. For some specific callback functions, the input parameters lack critical context information. As for the Mandatory Access Control framework, Apple directly claims that third parties should not use these private interfaces, this mechanism is not part of the KPI.

In order to bring about some changes, I'd like to introduce you to Kemon, an open source Pre and Post-operation based kernel callback framework. With the power of Kemon, we can easily implement LPC communication monitoring, MAC policy filtering, kernel driver firewall, etc. In general, from an attacker's perspective, this framework can help achieve more powerful Rootkit. From the perspective of defense, Kemon can help construct more granular monitoring capabilities. I also implemented a kernel fuzzer through this framework, which helped me find many vulnerabilities, such as: CVE-2017-7155, CVE-2017-7163, CVE-2017-13883, etc.

Source Code: https://github.com/didi/kemon
Documentation: https://github.com/didi/kemon/blob/master/doc/Kemon

</details>

<details><summary><strong>Learn How to Build Your Own Utility to Monitor Malicious Behaviors of Malware on macOS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Kai Lu](https://img.shields.io/badge/Kai%20Lu-informational)

🔗 **Link:** [Learn How to Build Your Own Utility to Monitor Malicious Behaviors of Malware on macOS](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/L-SM-TH.md)  
📝 **Description:** The landscape of macOS malware has changed dramatically in the past couple of years. Threats are becoming more complex, more varied, and more numerous. As a malware analyst or security researcher, having a powerful dynamic analysis utility is vital to be effective and efficient. This utility can enable us to understand malware capabilities and quickly analyze the malicious behaviors of malware.

Want to know how to build your own arsenal? I will detail the implementation to monitor kinds of malicious behaviors of malware on macOS. The capabilities of the utility cover monitoring process execution with command line arguments, file system events (including all common file operations, such as open, read, write, delete, rename operations), dylib loading event, network activities (including UDP, TCP, ICMP, DNS query and response).

The Mandatory Access Control Framework is the substrate on top of which all of Apple's securities, both macOS and iOS, are implemented. I will discuss how to monitor process execution, file system events, and dylib loading events using MACF on macOS. Next, I'll provide the details for monitoring network activities using Socket Filters. The utility can also record some basic info including process name, parent process name, pid, ppid, uid besides the specific details for each event. For DNS response, this utility can parse the data of DNS response and record the IP:URL mappings.

The utility consists of two parts, one is the KEXT(core component) in kernel, the other one is a client program in user space, which involves the communication between kernel space and user space. After discussing some communication mechanisms, I'll choose the kernel control API, which is a socket-based API that allows you to communicate with and receive broadcast notifications from the KEXT. The client program is intended to receive the data from the KEXT and display it to users.

In this presentation, I provide an advanced solution to monitor kinds of malicious behaviors of malware in kernel on macOS. I will also provide all involved key technical details for the implementation of monitoring all common malicious behaviors of malware on macOS. This utility is designed to dynamically analyze the malicious behaviors of malware on macOS, helping analysts or security researchers more efficiently analyze malware. You can build your own utility for fun!

Source Code: https://fortinetweb.s3.amazonaws.com/fortiguard/research/fortiappmonitor_1.0.0_release.pkg

Presentation:

https://fortinetweb.s3.amazonaws.com/fortiguard/research/Learn_How_to_Build_Your_Own_Utility_to_Monitor_Malicious_Behaviors_of_Malware_on%20macOS_KaiLu.pdf

</details>

<details><summary><strong>LogonTracer</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational) ![Tomoaki Tani](https://img.shields.io/badge/Tomoaki%20Tani-informational)

🔗 **Link:** [LogonTracer](https://github.com/t-tani)  
📝 **Description:** LogonTracer is a tool to investigate malicious logon by visualizing and analyzing Windows Active Directory event logs. Event log analysis is a key element in DFIR. In the lateral movement phase of APT incidents, analysis Windows Active Directory event logs is crucial since it is one of the few ways to identify compromised hosts. At the same time, examining the logs is usually a painful task because Windows Event Viewer is not a best tool. Analysts often end up exporting entire logs into text format, then feeding them to other tools such as SIEM. However, SIEM is neither a perfect solution to handle the increasing amount of logs.

We would like to introduce a more specialized event log analysis tool for incident responders. It visualizes event logs using network analysis and machine learning so as to show the correlation of accounts and hosts. Proven with our on the ground response experience, most importantly it is an open source tool.

</details>

<details><summary><strong>MaliceIO</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Josh Maine](https://img.shields.io/badge/Josh%20Maine-informational)

🔗 **Link:** [MaliceIO](https://github.com/gunguy831/malice-1)  
📝 **Description:** Malice's mission is to be a free open source version of VirusTotal that anyone can use at any scale from an independent researcher to a fortune 500 company.

Source Code: https://github.com/maliceio/malice

</details>

<details><summary><strong>Memhunter: A Live Alternative to Volatility Memory Forensic Plugins</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Marcos Oviedo](https://img.shields.io/badge/Marcos%20Oviedo-informational)

🔗 **Link:** [Memhunter: A Live Alternative to Volatility Memory Forensic Plugins](https://github.com/marcosd4h/memhunter)  
📝 **Description:** Memhunter automates the hunting of memory resident malware, improving the threat hunter analysis process and remediation times. The tool detects and reports memory-resident malware living on endpoint processes. Memhunter only works on Windows at the moment, and it detects known malicious memory injection techniques. The detection process is performed through live analysis and without needing memory dumps. The tool was designed as a replacement of memory forensic volatility plugins such as malfind and hollowfind. The idea of not requiring memory dumps helps on performing the memory resident malware threat hunting at scale, without manual analysis, and without the complex infrastructure needed to move dumps to forensic environments.

In order to find footprints left by malware code injection techniques, memhunter relies on a set of memory inspection heuristics and ETW trace collection. Once a suspicious process gets identified, the tool filters out false-positives through Yara Rules analysis and VirusTotal queries. This down-selection process helps the tool to reduce the number of false positives, leaving only known-bad processes. The tool then gets forensic information on the remaining set of suspicious findings and report them back to the analyst for remediation steps.

The tool itself is a self-contained binary which can be run on the endpoint to conduct the memory hunting. The idea of a self-contained binary helps on reducing the footprint, the dependencies needed, and improving the deployability of the tool. The binary contains a set of embedded "hunters" plugins, each one in charge of performing a specific heuristic detection. It also contains the ability to register the binary as an ETW collection service, which will augment the findings of next runs by providing contextual information on the attack. The down-selection is performed through libyara and VirusTotal client functionality.

Source Code: https://github.com/marcosd4h/memhunter

</details>

<details><summary><strong>MLPdf: An Effective Machine Learning Based Approach for PDF Malware Detection</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jason Zhang](https://img.shields.io/badge/Jason%20Zhang-informational)

🔗 **Link:** [MLPdf: An Effective Machine Learning Based Approach for PDF Malware Detection](https://github.com/emintham/Papers)  
📝 **Description:** Due to the popularity of portable document format (PDF) and increasing number of vulnerabilities in major PDF viewer applications, malware writers continue to use it to deliver malware via web downloads, email attachments and other methods in both targeted and non-targeted attacks. The topic on how to effectively block malicious PDF documents has received huge research interests in both cyber security industry and academia with no sign of slowing down.

In this work, we propose and demonstrate a novel approach based on a multilayer perceptron (MLP) neural network model, termed MLPdf, for the detection of PDF based malware. More specifically, the MLPdf model uses a backpropagation algorithm with stochastic gradient decent search for model update. A group of high quality features are extracted from two real-world datasets which comprise around 105000 benign and malicious PDF documents. Evaluation results indicate that the proposed MLPdf approach exhibits excellent performance which significantly outperforms all evaluated eight well known commercial anti-virus scanners with a much higher true positive rate (TPR) of 95.12% achieved while maintaining a very low false positive rate of 0.08%. Of the evaluated commercial AV scanners, the best scanner only has a TPR of 84.53%, which is over 10% lower than the proposed MLPdf model. In the demonstration, we will first manually analyze a malicious PDF document , then show how it can be automatically detected by the proposed ML approach.

Presentation: https://github.com/cyberML/MLPdf/blob/master/BlackHatUSA2018_MLPdf_slides.pdf
Paper: https://arxiv.org/abs/1808.06991

</details>

<details><summary><strong>MLSploit: Resilient ML Platform - Advanced Deep Learning Analytic Platform Made Easy for Every Security Researcher</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Evan Yang](https://img.shields.io/badge/Evan%20Yang-informational) ![Li Chen](https://img.shields.io/badge/Li%20Chen-informational)

🔗 **Link:** Not Available  
📝 **Description:** Deep learning (DL) and machine learning (ML) had been proved to be effective tools to analyze or detect malware. To help security experts to apply cutting-edge ML technologies effortlessly, we designed a large scale DL analytic platform uniquely for security researches. This platform has a ML pipeline web interface which can guide users through each pipeline steps. Its novel feature analysis tool enables feature study and manipulation for adversarial ML evasive attack. The performances of classifiers can be compared and optimized and then used for prediction. The RESTful interface of this platform was developed to enable connections between external applications. Also it is possibly to productize this platform to become an cloud service.

Security analyst can upload either static or dynamic malware dataset to storage, i.e. big data Hadoop file system, and start the analysis. Or if backend sandbox is hooded, binaries can be uploaded for processing and then apply the output for inference. The ML pipeline supports several popular open source libraries, such as Scikit-Learn, big data Spark ML and deep learning Keras/Theano/Tensorflow. The slow DL training can be accelerated in a loosely connected backend worker, such as Intel Xeon Phi or GPGPU machines. The outputs are presented at web pages in several tables or in 2-D or 3-D interactive JavaScript diagrams for clear visualization. All the outputs, such as feature coefficient etc., can be downloaded for other usages. Also the prediction page can be used for ensemble inference or extended to be a test bed to demo new algorithm or adversarial attacks and defences. We will demo ransomware analysis on this platform and the perturbation attack against pre-trained image convolution neural network classifiers. We believe via this platform the security researches and analysis can be accelerated greatly.

</details>

<details><summary><strong>Objective-See's MacOS Security Tools</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [Objective-See's MacOS Security Tools](https://github.com/objective-see/FileMonitor)  
📝 **Description:** Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of macOS malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer, he's written various macOS security tools that he now shares online (always free!), via objective-see.com.

Come watch as DoNotDisturb detects physical access attacks, LuLu blocks malware attempting to communicate with C&C servers, OverSight detect webcam spying, and much more. Our Macs will remain secure!

</details>

<details><summary><strong>PA Toolkit: Wireshark Plugins for Pentesters</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational)

🔗 **Link:** [PA Toolkit: Wireshark Plugins for Pentesters](https://github.com/pentesteracademy/patoolkit)  
📝 **Description:** Wireshark is the most basic tool that anyone thinks of when network traffic analysis is mentioned. Wireshark is beyond doubt, a wonderful tool which is available free of cost to the community and is well maintained. It is also modular and allows the user to add more functionality in form of C/Lua plugins. There are some good dissectors and plugins available for Wireshark which make user's life easy but when we talk the plugins related to attack detection or macro analysis from the security point of view, there is not much available. Our PA Toolkit is such an attempt to extend the functionality of Wireshark from a micro-analysis tool and protocol dissector to the macro analyzer and threat hunter.

PA toolkit is a collection of Wireshark plugins which enables a pentester to get insights for multiple network protocols like WiFi, VoIP, ARP, DNS, DHCP, SSL etc. This eliminates the need for a separate software/framework to detect basic attacks. The plugins are easy to add and are platform independent.

</details>

<details><summary><strong>Performing Live Forensics Without Killing Your Evidence</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![John Moran](https://img.shields.io/badge/John%20Moran-informational)

🔗 **Link:** [Performing Live Forensics Without Killing Your Evidence](https://github.com/muellerzr/Practical-Deep-Learning-For-Coders/blob/master/05a_NLP.ipynb)  
📝 **Description:** In a threat landscape characterized by targeted attacks, file-less malware and other advanced hacking techniques, the days of relying solely on traditional "dead box" forensics for investigations are, well… dead. Live forensics, a practice considered a dangerous and dark art just a decade ago, has now become the de-facto standard. However, many CSIRT teams still struggle with this type of threat hunting.

This session will discuss the benefits, pitfalls to avoid and best practices for performing live box forensics as a threat hunting tool. The presenter will also introduce a free and publicly available command line tool for Windows that automates the execution and data acquisition from other live forensics tools in a more secure, easier to maintain manner.

</details>

<details><summary><strong>rastrea2r (reloaded!): Collecting & Hunting for IOCs with Gusto and Style</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ismael Valenzuela](https://img.shields.io/badge/Ismael%20Valenzuela-informational) ![Sudheendra Bhat](https://img.shields.io/badge/Sudheendra%20Bhat-informational)

🔗 **Link:** Not Available  
📝 **Description:** Rastrea2r (pronounced "rastreador" - hunter- in Spanish) is a multi-platform open source tool that allows incident responders and SOC analysts to triage suspect systems and hunt for Indicators of Compromise (IOCs) across thousands of endpoints in minutes. To parse and collect artifacts of interest from remote systems (including memory dumps), rastrea2r can execute sysinternal, system commands and other 3rd party tools across multiples endpoints, saving the output to a centralized share for automated or manual analysis. By using a client/server RESTful API, rastrea2r can also hunt for IOCs on disk and memory across multiple systems using YARA rules. As a command line tool, rastrea2r can easily integrate with AV consoles and SOAR tools, allowing incident responders and SOC analysts to collect forensics evidence and hunt for IOCs without the need for an additional agent, with 'gusto' and style!

Source Code: https://github.com/rastrea2r/rastrea2r
Presentation: https://github.com/rastrea2r/rastrea2r/blob/master/presentations/BH%20Arsenal%20rastrea2r%202018.pdf

</details>

<details><summary><strong>RedHunt OS (VM): A Virtual Machine for Adversary Emulation and Threat Hunting</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sudhanshu Chauhan](https://img.shields.io/badge/Sudhanshu%20Chauhan-informational)

🔗 **Link:** Not Available  
📝 **Description:** The ultimate aim of any security exercise (offensive or defensive) is to make the organization more resilient and adaptive towards modern adversaries. RedHunt OS (Virtual Machine) aims to provide defenders a platform containing the toolset to emulate adversaries and on the other hand arm them with advanced logging and monitoring setup to actively hunt such adversaries. The project aims to provide a one stop shop which defenders can quickly spin up and practice blue team exercises in the presence as well as absence of an active attacker. Similarly, red team can utilize the platform to identify and understand the footprints they leave behind during a red team exercise. Both the teams can utilize the setup to become better at what they do ultimately leading to better security.

Source Code: https://github.com/redhuntlabs/RedHunt-OS/﻿

</details>

<details><summary><strong>wpa-sec: The Largest Online WPA Handshake Database</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Alex Stanev](https://img.shields.io/badge/Alex%20Stanev-informational)

🔗 **Link:** Not Available  
📝 **Description:** Started as pet project in 2011, wpa-sec collects WPA handshake captures from all over the world. Contributors use client script to download handshakes and special crafted dictionaries to initiate attack against PSKs. With more than 115 GB captures from 240,000 submissions, collected samples represent invaluable source for wireless security research. This includes:

Many improvements for emerging wireless security tools like hcxtools suite (https://github.com/ZerBea/hcxtools)
Identified default PSK key generation algorithms, used by various ISPs. Those, along with fixes for current implementations get in RouterKeygen project (https://github.com/routerkeygen/routerkeygenPC). Many more to come, based on current research activities
Performance optimizations for WPA crackers
Identified some linux kernel driver bugs

Live installation: https://wpa-sec.stanev.org
GitHub: https://github.com/RealEnder/dwpa﻿
Presentation: https://alex.stanev.org/presentations/en/BlackHatUSA2018_DEFCON26-PHV_wpa-sec_AlexStanev.pdf

</details>

---
## Others
<details><summary><strong>ChipWhisperer</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Colin O'Flynn](https://img.shields.io/badge/Colin%20O'Flynn-informational)

🔗 **Link:** [ChipWhisperer](https://github.com/colinoflynn)  
📝 **Description:** ChipWhisperer - the favorite open-source toolchain for including both hardware & software. Now upgraded to include a major API shift with Python-centric scripting, plus many new targets with hardware AES accelerators. The scripting capability means you are able to automatically build firmware images for different targets or with different compiler settings, and perform attacks on them. This opens up the potential for continuous-integration (C.I.) usage of ChipWhisperer, which will be pushed further with the release of ChipWhisperer-Lint.

</details>

<details><summary><strong>Damn Vulnerable iOS App: Swift Edition</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Prateek Gianchandani](https://img.shields.io/badge/Prateek%20Gianchandani-informational)

🔗 **Link:** [Damn Vulnerable iOS App: Swift Edition](https://github.com/prateek147)  
📝 **Description:** Damn Vulnerable iOS App (DVIA) is an iOS application that is damn vulnerable. Its main goal is to provide a platform to mobile security enthusiasts/professionals or students to test their iOS penetration testing skills in a legal environment. This project is developed and maintained by @prateekg147. The vulnerabilities and solutions covered in this app are tested up to iOS 11. DVIA is free and open source and it has both a Swift and Objective-C version. This is a completely new version of Damn Vulnerable iOS App - completely rewritten in Swift 4.0.

The following vulnerabilities are covered:

Local Data Storage
Jailbreak Detection
Excessive Permissions
Runtime Manipulation
Anti Anti Hooking/Debugging
Binary Protection
Touch/Face ID Bypass
Phishing
Side Channel Data Leakage
IPC Issues
Broken Cryptography
Webview Issues
Network Layer Security
Application Patching
Sensitive Information in Memory
Data Leakage to Third parties

</details>

<details><summary><strong>JTAGulator: Uncovering the Achilles Heel of Hardware Security - ARSENAL THEATER DEMO</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational)

🔗 **Link:** Not Available  
📝 **Description:** Five years after its original release, JTAGulator continues to be the de facto open source tool for identifying interfaces commonly used for hardware hacking, such as JTAG and UART, from test points, vias, component pads, or connectors on a target product. The tool can save a significant amount of time, particularly for those who don't have the resources required for traditional reverse engineering processes, and bridges the gap between gaining physical access to circuitry and exploiting it. Black Hat Arsenal USA 2018 will mark the release of a new firmware version and and Joe will provide demonstrations of the tool's updated features.

</details>

<details><summary><strong>Mafia: Mobile Security Automation Framework for Intelligent Auditing</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ankur Bhargava](https://img.shields.io/badge/Ankur%20Bhargava-informational) ![Mohan Kallepalli](https://img.shields.io/badge/Mohan%20Kallepalli-informational) ![Sagar Popat](https://img.shields.io/badge/Sagar%20Popat-informational)

🔗 **Link:** Not Available  
📝 **Description:** Mobile applications are critical when it comes to vulnerabilities in production environment. The only option to remove a product issue is to force update the app, which isn't a good user experience, especially when the app download size is high. With this project, we aim to automate the manual security testing and leverage developers with a tool which helps them identify bugs well in advance. The goal of MAFIA is to perform end to end security testing for a given mobile app and create a self serve tool for developers and security engineers.

</details>

<details><summary><strong>Micro-Renovator: Bringing Processor Firmware up to Code</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Matt King](https://img.shields.io/badge/Matt%20King-informational)

🔗 **Link:** [Micro-Renovator: Bringing Processor Firmware up to Code](https://github.com/mathew-fleisch/def-con-schedule/blob/master/docs/conference.json)  
📝 **Description:** The mitigations for Spectre highlighted a weak link in the patching process for many users: firmware (un)availability. While updated microcode was made publicly available for many processors, end-users are unable to directly consume it. Instead, platform and operating system vendors need to distribute firmware and kernel patches which include the new microcode. Inconsistent support from those vendors has left millions of users without a way to consume these critical security updates, until now. Micro-Renovator provides the ability to apply microcode updates without modifying either platform firmware or the operating system, through simple (and reversible) modifications to the EFI boot partition.

Source Code: https://github.com/syncsrc/MicroRenovator

</details>

<details><summary><strong>OpticSpy: Finding Data in Light Waves</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational)

🔗 **Link:** Not Available  
📝 **Description:** OpticSpy is an open source hardware module for experimenting with optical data transmissions. It captures, amplifies, and converts an optical signal from a visible or infrared light source into a digital form that can be analyzed or decoded with a computer.

With OpticSpy, hardware hackers can search for optical covert channels, which intentionally exfiltrate data in a way undetectable to the human eye, explore signals from remote controls and other consumer electronic devices that send information through light, or discover Li-Fi networks and Visible Light Communication (VLC) systems.

</details>

<details><summary><strong>Project Interceptor: Owning Anti-Drone Systems with Nanodrones - ARSENAL THEATER DEMO</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![David Melendez](https://img.shields.io/badge/David%20Melendez-informational)

🔗 **Link:** Not Available  
📝 **Description:** This tool provides a new vision about drone protection against anti-drone systems, using WiFi side/hidden channel communication, fallback control by variable modulation radio with SDR, and hacking capabilities. All embedded into a hand-sized aircraft to make detection and mitigation a pain, called "Project Interceptor". This drone is based on Vocore2, the smallest Linux board available.

Taking into account all the anti-drone process stages, this small aircraft, is designed to make much more difficult detection, due to a hand-sized design, very low radar signature, and very flexible radio signatures, combined with a fallback SDR based communication protocol, keeping most hacking capabilities of any other drone, at a very low cost ($70).

</details>

<details><summary><strong>TumbleRF: RF Fuzzing Made Easy</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Matt Knight](https://img.shields.io/badge/Matt%20Knight-informational) ![Ryan Speers](https://img.shields.io/badge/Ryan%20Speers-informational)

🔗 **Link:** [TumbleRF: RF Fuzzing Made Easy](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Wireless.md)  
📝 **Description:** We are pleased to introduce TumbleRF, an open source Python framework for fuzzing arbitrary RF technologies down to the PHY. While fuzzing has long been relied on by security researchers to identify software bugs, applying fuzzing methodologies to RF and hardware systems has historically been challenging due to siloed tools and the limited capabilities of commodity RF chipsets.

We created the TumbleRF host-based fuzzing orchestration framework to address these shortfalls by defining core fuzzing logic while abstracting a hardware interface API that can be mapped for compatibility with any RF driver. Thus, supporting a new radio involves merely extending an API, rather than writing a protocol-specific fuzzer from scratch. In addition to enabling traditional MAC-centric fuzzing workflows, TumbleRF's flexibility allows attackers to fuzz and characterize PHY state machines if paired with a Software Defined Radio or a sufficiently flexible commodity radio.

Attendees can expect to leave this presentation with an understanding of how RF and hardware physical layers actually work, and the security issues that lie latent in these designs. Additionally attendees will be empowered to pursue RF vulnerabilities in an automated fashion, which in turn will drive the development and adoption of more secure systems.

</details>

<details><summary><strong>Walrus: Make the Most of Your Card Cloning Devices</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Daniel Underhay](https://img.shields.io/badge/Daniel%20Underhay-informational) ![Matthew Daley](https://img.shields.io/badge/Matthew%20Daley-informational)

🔗 **Link:** [Walrus: Make the Most of Your Card Cloning Devices](https://github.com/TeamWalrus/Walrus)  
📝 **Description:** Walrus enables you to use your existing contactless card cloning devices with your Android device. Using a simple interface, cards can be read into a wallet to be written or emulated later.

Designed for physical security assessors, Walrus has features that will help you in your next red team engagement.

As an example, Walrus can be used to tap into the power of the Tastic RFID Thief long range card reader, allowing for walk-by cloning of a victim's access card in a matter of seconds. The cloned card can then quickly be emulated or written to a blank card via an attached Proxmark.

</details>

---
## 🔍 OSINT
<details><summary><strong>DataSploit 2.0</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Kunal Agarwal](https://img.shields.io/badge/Kunal%20Agarwal-informational) ![Shubham Mittal](https://img.shields.io/badge/Shubham%20Mittal-informational)

🔗 **Link:** Not Available  
📝 **Description:** An #OSINT Framework to perform various recon techniques on Companies, People, Phone Number, Bitcoin Addresses, etc., aggregate all the raw data, and give data in multiple formats.
Details:

Performs OSINT on a domain / email / username / phone and find out information from different sources
Correlate and collaborate the results, show them in a consolidated manner
Tries to find out credentials, api-keys, tokens, subdomains, domain history, legacy portals, etc. related to the target
Use specific script / launch automated OSINT for consolidated data
Performs Active Scans on collected data
Generates HTML, JSON reports along with text files

New Features:

Active Modules
Well parsed JSON and HTML Reports
BitCoin Address OSINT
More in-depth Social Media Searches
Basic Vulnerability checks on Subdomains
Subdomain Takeover, etc.
DB Support
Support for Multiple Alternative API Keys

</details>

<details><summary><strong>Desenmascara.me: How to Track Online Counterfeiters</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Emilio Casbas](https://img.shields.io/badge/Emilio%20Casbas-informational)

🔗 **Link:** Not Available  
📝 **Description:** What is one of the biggest examples of online fraud being massively underestimated?: Online counterfeiters. This fraud captured the attention of two bigs intelligence providers by publishing a joint report titled: "Why Retailers Are Losing The Fight Against Online Counterfeiting."

However, security vendors providing protections against C2, malware and any kind of malicious domains still do not provide protection against online counterfeiters. In the rare cases when they do, they do it by playing the cat-and-mouse game (not scalable) and they confuse online counterfeiters with phishing even when is a totally different threat with different goals. Therefore, the goal of the online tool presented here: desenmascara.me is to raise awareness of this increasing online fraud with real examples of any major brand.

</details>

<details><summary><strong>Dradis Framework: Learn How to Cut Your Reporting Time in Half - ARSENAL THEATER DEMO</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** Not Available  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration framework for corporate and consulting teams. It can import from over 19 popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007 (yup, we've been helping 1000s of InfoSec pros for 11 years), Dradis Framework has been growing ever since. Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.

Come see the latest Dradis release in action. It's loaded with updates including better communication and notifications, new tool connectors, additional REST API coverage, cleaner and faster UI and much more. Find out why Dradis is being downloaded over 400 times every week and is loved by students preparing different certifications and experienced professionals alike. Be sure to check it out before we run out of our popular stickers! Btw, did you know Dradis is the only security tool with its own jingle? You've got to see this.

</details>

<details><summary><strong>Social Mapper: Social Media Correlation Through Facial Recognition</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Jacob Wilkin](https://img.shields.io/badge/Jacob%20Wilkin-informational)

🔗 **Link:** [Social Mapper: Social Media Correlation Through Facial Recognition](https://github.com/Greenwolf/social_mapper)  
📝 **Description:** Social Mapper is a Open Source Intelligence Tool that uses facial recognition to correlate social media profiles across different sites on a mass scale. It takes an automated approach to searching popular social media sites for targets names and pictures to accurately detect and group a person's presence, outputting the results into report that a human operator can quickly review. Social Mapper has a variety of uses in the security industry, for example the automated gathering of large amounts of social media profiles for use on targeted phishing campaigns. Facial recognition aids this process by removing false positives in the search results, so that reviewing this data is quicker for a human operator.

Social Mapper supports the following social media platforms:

LinkedIn
Facebook
Twitter
GooglePlus
Instagram
VKontakte
Weibo
Douban

Social Mapper takes a variety of input types such as:

An organization's name
A folder full of named images
A CSV file with names and url's to images online

</details>

<details><summary><strong>WhiteRabbit: Combining Threat Intelligence, Public Blockchain Data, and Machine Learning to go Down the "Dirty Money" Rabbit Hole</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Nicolas Kseib](https://img.shields.io/badge/Nicolas%20Kseib-informational) ![Olivia Thet](https://img.shields.io/badge/Olivia%20Thet-informational)

🔗 **Link:** Not Available  
📝 **Description:** WhiteRabbit will be used to demonstrate how machine learning models can be used on a merged dataset combining cyber related contextual information with Bitcoin (BTC) transaction data. The model can be used by both private and public sectors security professionals, working in the cryptocurrency field, to deny business for certain BTC addresses or, build legal cases to return illegally stolen coins.

To build the dataset, we collected a list of BTC addresses involved in illegal activities. Using these addresses as a starting point, we navigated along the chain, and reconstructed a cluster of connected "dirty" addresses. We used rules such as First-In-First-Out (FIFO) to label them. These labeling techniques can be used to tag certain BTC addresses that fall within this path as "dirty" addresses because they handled money acquired through illegal activities. We can then take this a step further and analyze the characteristic behavioral elements of these addresses. This behavioral analysis will allow us to determine the features representing this malicious behavior and use them within a machine learning model classifying new BTC addresses.

Our model-building approach is based on a three part framework: The first part is to collect a set of BTC addresses and classify them as "clean" or "dirty" to use them as our ground truth. The second part is to test the classification models using this dataset and propose decision metrics to optimally pick a model. In this part, we will also discuss ideas about how to compute expensive, but important features obtained from transaction data stored on a graph database. In the third part, we will show how to use the obtained optimal model to predict if an address is "dirty". Finally, we will discuss our challenges when solving this problem and propose solutions to overcome them.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>OWASP Dependency-Check</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Jeremy Long](https://img.shields.io/badge/Jeremy%20Long-informational)

🔗 **Link:** [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck)  
📝 **Description:** With the number of critical vulnerabilities in FOSS libraries that have affected so many applications over the last few years - Software Composition Analysis is a critical component to maintaining the security of your custom application. From Struts to Spring to jackson-databind, etc. the list of libraries that have had vulnerabilities that lead to remote code execution in the applications using the libraries goes on and on. As does the list of sites that have been compromised by these vulnerabilities. OWASP dependency-check is an open source Software Composition Analysis tool that provides a solution the `OWASP Top 10 2017: A9 - Using Components with Known Vulnerabilities`.

</details>

<details><summary><strong>Puma Scan</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Eric Johnson](https://img.shields.io/badge/Eric%20Johnson-informational) ![Eric Mead](https://img.shields.io/badge/Eric%20Mead-informational)

🔗 **Link:** [Puma Scan](https://github.com/pumasecurity/puma-scan)  
📝 **Description:** Puma Scan provides real-time, continuous source code analysis for .NET applications with over 50 security-focused rules targeting insecure deserialization, injection, weak cryptography, cross-site request forgery, misconfiguration, and many more insecure coding patterns. Puma Scan displays vulnerabilities in Visual Studio as spell check errors and compiler warnings to prevent engineers from committing vulnerabilities into code repositories.

DevSecOps teams can use Puma Scan's command line interface to enable security scanning in continuous integration pipelines (e.g. Jenkins, TFS), monitor code for security issues, and verify security thresholds are met during each build.
Come see live demonstrations of the Puma hunting source code for vulnerabilities and walk away with an open-source (MPL v2.0) static analysis engine to help secure your .NET applications.

</details>

<details><summary><strong>SCoDA: Smart COntract Defender and Analyzer</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![AJIT HATTI](https://img.shields.io/badge/AJIT%20HATTI-informational)

🔗 **Link:** Not Available  
📝 **Description:** SCoDA (Smart Contract Defender and Analyzer) module in LAMMA tool, written in python for solidity based smart contract scanning. The tools is a unified and python ported version of various other scanners and vulnerabilities reported on Ethereum Platform.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Snake: The Malware Storage Zoo</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Alex Kornitzer](https://img.shields.io/badge/Alex%20Kornitzer-informational)

🔗 **Link:** [Snake: The Malware Storage Zoo](https://github.com/WithSecureLabs/snake)  
📝 **Description:** Snake is a malware storage zoo that was built out of the need for a centralized and unified storage solution for malicious samples that could seamlessly integrate into the investigation pipeline. Snake utilizes a plugin system to provide extensive static analysis capability along with interface capability to allow interaction with 3rd party platforms, such as Cuckoo. Snake adheres to the RESTful API philosophy and as a result allows for seamless interaction with 3rd party tools from within a single UI. It provides enough information to allow analysts to quickly and efficiently pivot to the most suitable tools for the task at hand.

</details>

---