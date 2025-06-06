# Europe 2018
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2018** event held in **Europe**.
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
## Others
<details><summary><strong>APKiD: "PEiD" for Android Applications</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Eduardo Novella Lorente](https://img.shields.io/badge/Eduardo%20Novella%20Lorente-informational)

🔗 **Link:** Not Available  
📝 **Description:** APKiD is like "PEiD" for Android applications. It gives information on how an APK was built by fingerprinting compilers, packers, obfuscators, and protectors. The main idea behind the tool is to help provide context on how the APK was potentially built or changed after it was built. This is all context useful for attributing authorship and finding patterns.

Extracting information about how the APK was made, it can provide a lot of information to assess the healthiness of an Android application (e.g. malware or pirated). The framework is the combination of a bunch of Yara rules and Python wrappers that scan files within APKs. Mainly, APKiD unpacks files and explores AndroidManifest.xml, DEX and ELF files to match rules and offers results based on them. Between the 186 Yara rules, we can find 94 packers, 10 compilers and 16 obfuscators.

Features and detections:

Commercial and open-source obfuscators, packers, droppers and protectors
Anti-disassembly tricks, anti-emulation, anti-debugging APIs,...
Abnormalities in DEX structure
Compiler fingerprint potentially indicating re-packaged apps
Results in JSON format

Further information:

APKID -> https://github.com/rednaga/APKiD
Android Compiler Fingerprinting -> http://hitcon.org/2016/CMT/slide/day1-r0-e-1.pdf
Detecting Pirated and Malicious Android Apps with APKiD -> https://rednaga.io/2016/07/31/detecting_pirated_and_malicious_android_apps_with_apkid/

</details>

<details><summary><strong>CyBot: Open-Source Threat Intelligence Chat Bot (Bring the Threats)</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Tony Lee](https://img.shields.io/badge/Tony%20Lee-informational)

🔗 **Link:** Not Available  
📝 **Description:** Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to share the end result of our research (a chat bot that we affectionately call CyBot) with Black Hat attendees worldwide at the US, Europe, and Asia conferences. Each conference provided an opportunity to share the latest plugins and collect feedback and feature requests with the absolute best in the industry. This year's Black Hat Europe will allow us to continue the global collaboration effort in making incident response and threat research faster and more efficient than ever.

Best of all, if you know even a little bit of Python, you can help our collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!

</details>

<details><summary><strong>Dexter: The Friendly Forensics Expert on the Coinbase Security Team</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Hayden Parker](https://img.shields.io/badge/Hayden%20Parker-informational)

🔗 **Link:** [Dexter: The Friendly Forensics Expert on the Coinbase Security Team](https://github.com/coinbase/dexter/blob/master/doc/dexter.md)  
📝 **Description:** Sometimes you want to be able to pull forensic images off your production hosts, but you want to make sure you set that up correctly. If you don't, people might steal customer financial data or cryptocurrency private keys for hot wallets (or something else), and that would be a very bad day for you and for the cryptocurrency community. This talk introduces Dexter, a forensics tool for high security environments. Dexter makes sure that no single person can do scary forensics things, and that the scary results of the scary forensic things can only be read by people who aren't scary. I'll give an overview of the Coinbase production environment, data pipeline, and detection tooling to set the stage for when we might use Dexter. We will then walk through how Dexter works and do a demo that will totally work and not have any technical issues whatsoever.

</details>

<details><summary><strong>FACT 2.5: Firmware Analysis and Comparison Tool</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Peter Weidenbach](https://img.shields.io/badge/Peter%20Weidenbach-informational)

🔗 **Link:** Not Available  
📝 **Description:** The Firmware Analysis and Comparison Tool (FACT) is intended to automate firmware security analysis. Thereby, it shall be easy to use (web GUI), extend (plug-in system) and integrate (REST API). When analyzing Firmware, you face several challenges: unpacking, initial analysis, identifying changes towards other versions, find other firmware images that might share vulnerabilities you just found. FACT is able to automate many aspects of these challenges leading to a massive speed-up in the firmware analysis process. This means you can focus on the fun part of finding new vulnerabilities, whereas FACT does all the boring stuff for you.

</details>

<details><summary><strong>PandaWar: Hardware Security Multidimensional Attack and Defense Toolset</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![JIE FU](https://img.shields.io/badge/JIE%20FU-informational) ![Mingchuang Qin](https://img.shields.io/badge/Mingchuang%20Qin-informational) ![Kunzhe Chai](https://img.shields.io/badge/Kunzhe%20Chai-informational)

🔗 **Link:** Not Available  
📝 **Description:** This is a hardware attack and defense tool platform. It will help you quickly master and implement a variety of hardware attack methods.

It includes ultrasonic attacks, RFID attacks, power side channel attacks, and radio defense etc.

All open source, design idea, design concept, design method, code, schematic, PCB.

</details>

<details><summary><strong>Uitkyk: Identifying Malware via Runtime Memory Analysis</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Chris Le Roy](https://img.shields.io/badge/Chris%20Le%20Roy-informational)

🔗 **Link:** [Uitkyk: Identifying Malware via Runtime Memory Analysis](https://github.com/brompwnie/uitkyk)  
📝 **Description:** Uitkyk is the first Android framework that allows for its implementers to identify Android malware according to the instantiated objects on the heap for a particular process. Uitkyk does not require the APK of the application to be scanned to be present to identify malicious behaviour but instead makes use of runtime memory analysis to detect behaviour which normally cannot be identified by static analysis of Android applications. Static analysis of Android applications is the default approach utilised to identify malicious applications however static analysis has certain shortcomings which Uitkyk addresses by targeting the heap. Uitkyk can be implemented as a standalone library or standalone application on mobile devices.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>ART: Adversarial Robustness Toolbox for Machine Learning Models</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Irina Nicolae](https://img.shields.io/badge/Irina%20Nicolae-informational)

🔗 **Link:** [ART: Adversarial Robustness Toolbox for Machine Learning Models](https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Contributing)  
📝 **Description:** Adversarial attacks of machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks) or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). Adversarial attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defense methods for machine learning models. It provides an implementation for many state-of-the-art methods for attacking and defending machine learning. Through ART, the attendees will (re)discover how to attack and defend machine learning systems.

</details>

<details><summary><strong>Deep Exploit: Fully Automatic Penetration Test Tool Using Machine Learning</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational)

🔗 **Link:** [Deep Exploit: Fully Automatic Penetration Test Tool Using Machine Learning](https://github.com/TheDreamPort/deep_exploit)  
📝 **Description:** DeepExploit is fully automated penetration tool linked with Metasploit. It identifies the status of all opened ports on the target server and executes the exploit at pinpoint using Machine Learning.

Deep Exploit's key features are the following:

Efficiently execute exploit: DeepExploit can execute exploits at pinpoint (minimum 1 attempt) using self-learned data.
Deep penetration: If DeepExploit succeeds the exploit to the target server, then it further executes the exploit to other internal servers.
Self-learning: DeepExploit can learn how to exploitation by itself (uses reinforcement learning). It is not necessary for humans to prepare learning data.
Powerful intelligence gathering. To gather the information of software operated on the target server is very important for successful the exploitation. DeepExploit can identify product name and version using following methods.
+ Port scanning; Machine Learning (Analyze HTTP responses gathered by Web crawling); Google Hacking

Current Deep Exploit's version is a beta, but it can fully automatically execute following actions:

Intelligence gathering
Threat modeling
Vulnerability analysis
Exploitation
Post-Exploitation
Reporting

By using our DeepExploit, you will benefit from the following:

For pentesters:
(a) They can greatly improve the test efficiency; (b) The more pentesters use DeepExploit, DeepExploit learns how to method of exploitation using machine learning. As a result, accuracy of test can be improve.


For Information Security Officers:
(c) They can quickly identify vulnerabilities of own servers. As a result, prevent that attackers attack to your servers using vulnerabilities, and protect your reputation by avoiding the negative media coverage after breach.

Because attack methods to servers are evolving day by day, there is no guarantee that yesterday's security countermeasures are safety today. It is necessary to quickly find vulnerabilities and take countermeasures. Our DeepExploit will contribute greatly to maintaining your safety.

Presentation: https://www.slideshare.net/babaroa/deep-exploitblack-hat-europe-2018-arsenal
Source Code:: https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit

</details>

<details><summary><strong>Lucky CAT: A Distributed Fuzzing Management Framework</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Thomas Barabosch](https://img.shields.io/badge/Thomas%20Barabosch-informational)

🔗 **Link:** [Lucky CAT: A Distributed Fuzzing Management Framework](https://github.com/fkie-cad/LuckyCAT)  
📝 **Description:** Lucky CAT (Crash All the Things!) is a distributed fuzzing framework with an easy to use web interface. It allows management of fuzzing jobs on several remote machines concurrently. Lucky CAT aims to be easily usable, scaleable, extensible, and fun. To achieve this, it is built using several micro services and it relies on many open source projects. Furthermore, it offers a RESTful API to automate it or to integrate it with other tools.

Lucky CAT comes with several plugins for mutation engines (e.g. /dev/urandom, radamsa), fuzzers (afl, qemu_fuzzer, a minimalistic file fuzzer) and verifiers (local gdb exploitable, remote gdb exploitable). There are templates (in Python and C) that allow to quickly integrate, for example, new fuzzers and verifiers. Fuzzers can rely on their own mutation engine (e.g. afl) but Lucky CAT can also generate test cases for a fuzzer. This is handy when writing a fuzzer for an embedded device with limited computational resources or a small one-shot fuzzer for a custom protocol.

Its origin is the Nightmare Fuzzing Project. However, Lucky CAT goes beyond its ancestor. It is more 2018-ish using latest technologies such as RabbitMQ, Flask, MongoDB, and Python3. Lucky CAT's main objective is to automate the fuzzing process as far as possible so as to security researchers can focus on what they can best: identifying attack surfaces or writing custom fuzzers.
Therefore, future releases will focus on, amongst others, automatic deployment of fuzzers, crash notification and job summaries via email and instant messaging, and kernel core dump analysis.

Presentation: https://net.cs.uni-bonn.de/fileadmin/ag/martini/Staff/thomas_barabosch/blackhat-eu18-arsenal.pdf
Source Code: https://github.com/fkie-cad/LuckyCAT

</details>

<details><summary><strong>PingCastle: An Active Directory Security Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Vincent Le Toux](https://img.shields.io/badge/Vincent%20Le%20Toux-informational)

🔗 **Link:** [PingCastle: An Active Directory Security Tool](https://github.com/netwrix/pingcastle)  
📝 **Description:** So many tools that exist to assess Active Directory security, and yet, it is impossible to have an overview of all. PingCastle has been designed to tackle these difficulties and get results fast and without any requirements. Healthcheck mode is the most well-known mode that gives vulnerability reports in minutes regarding major AD vulnerabilities. But what if the most important point was to convince the management that AD security is not that simple? PingCastle is more than a vulnerability scanner. This demo will include scanners, cartography and secret tricks.

</details>

<details><summary><strong>Prowler: Cloud Security Assessment, Auditing, Hardening, Compliance and Forensics Readiness Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Toni de la Fuente](https://img.shields.io/badge/Toni%20de%20la%20Fuente-informational)

🔗 **Link:** [Prowler: Cloud Security Assessment, Auditing, Hardening, Compliance and Forensics Readiness Tool](https://github.com/prowler-cloud/prowler)  
📝 **Description:** Prowler helps to assess, audit and harden your AWS account configuration and resources. It also helps to check your configuration with CIS recommendations, and check if your cloud infrastructure is GDPR compliance or if you are ready for a proper forensic investigation. It is a command line tool that provides direct and clear information about configuration status related to security of a given AWS account, it performs more than 80 checks.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>ATT&CK Framework: Endpoint Detection Super Powers on the Cheap with Sysmon and Splunk</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Olaf Hartong](https://img.shields.io/badge/Olaf%20Hartong-informational)

🔗 **Link:** [ATT&CK Framework: Endpoint Detection Super Powers on the Cheap with Sysmon and Splunk](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/L-SM-TH.md)  
📝 **Description:** By using the ATT&CK framework as a basis for hunting the likelihood of catching at least part of the attackers trail is significantly increased. To make use of this rich data source I will demonstrate a Threat Hunting application which will guide your investigation along all covered ATT&CK techniques.

I will release the (Mandatory Manual Learning) ThreatHunting Splunk app I've developed, which at the time of writing contains over 80 (multi)searches and over 10 dashboards leveraging summary indexes, custom visualisations and a rich set of workflow actions.
These dashboards contain overviews, threat indicators and facilitate consecutive drilldown workflows to help the analyst determine whether this is a threat or not and also provides a whitelisting option for false positives.

Knowledge is power; the workflow has been intentionally built on generic searches to cover all attack variations, in the beginning this will generate quite some false positives. It might not appear so but this is a great thing, it will teach the hunters a great deal about their environment and therefore over time they'll be more efficient in detecting malicious behavior.

</details>

<details><summary><strong>CCAT: Cisco Config Analysis Tool</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mikhail Driagunov](https://img.shields.io/badge/Mikhail%20Driagunov-informational) ![Natalia Khodukina](https://img.shields.io/badge/Natalia%20Khodukina-informational) ![Nikita Loginov](https://img.shields.io/badge/Nikita%20Loginov-informational)

🔗 **Link:** Not Available  
📝 **Description:** CCAT is designed for finding security misconfigurations in Cisco devices. It generates a detailed report with explanations and tips on fixing the issues. We will implement an option to automatically fix those issues in one of our next updates.

Presentation: https://drive.google.com/file/d/1kEB7dEe4uIkfxWuKgGDYTJly_spEVaO-/view
GitHub: https://github.com/cisco-config-analysis-tool/ccat

</details>

<details><summary><strong>Cloud Security Suite: One Stop Tool forAWS/GCP/Azure Security Audit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jayesh Chauhan](https://img.shields.io/badge/Jayesh%20Chauhan-informational)

🔗 **Link:** Not Available  
📝 **Description:** While AWS, GCP & Azure provide protection with traditional security methodologies and have a neat structure for authorization/configuration, their security is as robust as the person in-charge of creating/assigning these configuration policies. As we all know, human error is inevitable and any such human mistake could lead to catastrophic damage to the environment.

Few vulnerable scenarios:

Your security groups/policies, password policy or IAM policies are not configured properly
S3 buckets and Azure blobs are world-readable
Web servers supporting vulnerable ssl ciphers
Ports exposed to public with vulnerable services running on them
If root credentials are used
Logging or MFA is disabled
And many more scenarios...

Knowing all this, audit of cloud infrastructure becomes a hectic task! There are a few open source tools which help in cloud auditing but none of them have an exhaustive checklist. Also, collecting, setting up all the tools and looking at different result sets is a painful task. Moreover, while maintaining big infrastructures, system audit of server instances is a major task as well.

CS Suite is a one stop tool for auditing the security posture of the AWS/GCP/Azure infrastructures and does OS audits as well. CS Suite leverages current open source tools capabilities and has custom checks added into one tool to rule them all.

</details>

<details><summary><strong>Drosera: Using Wireless Honeypot to Protect Wireless Networks</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yunfei Yang](https://img.shields.io/badge/Yunfei%20Yang-informational) ![Yongtao Wang](https://img.shields.io/badge/Yongtao%20Wang-informational) ![Hongjian Cao](https://img.shields.io/badge/Hongjian%20Cao-informational)

🔗 **Link:** Not Available  
📝 **Description:** Drosera is a wireless honeypot platform for discovering wireless intrusion attacks and intruders identification.

In wireless attacks, hackers are often attacking vulnerable wireless hotspots as a breakthrough. This means that a wireless network with obvious flaws will be the primary target for an attacker. When an attacker targets our wireless honeypot network, Drosera will record all actions before and after the attacker connects the network, including the process of attempting to connect to the network at the 802.11 frame level and further attacks after entering the honeypot network. Drosera can accurately identify the attack, and the first time to generate an alarm.

We are equipped with high-interactive Windows and Linux honeypots in the network, which simulate normal business systems to confuse the attacker and delay the attack process. They will also help us get information about the hacker like the goals, the attack methods, and the skill level.

</details>

<details><summary><strong>goKey: Reclaim Back Keys for Your Kingdom - A Vaultless Password Manager</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ignat Korchagin](https://img.shields.io/badge/Ignat%20Korchagin-informational)

🔗 **Link:** Not Available  
📝 **Description:** The password is the oldest and most widely used pillar of authentication. We use passwords everywhere: from everyday online shopping to accessing government services and managing our money. Every day, the number of online services increases and each of service most likely requires a password to use it.

On the other hand, as password-cracking techniques increase and evolve, so do the restrictions on the types of passwords we can use. It is not enough anymore to use your favourite movie as a password across all your accounts. The modern Internet threat model requires passwords to be either ridiculously long or look like random gibberish of uppercase and lowercase letters, numbers and special characters. And in NO WAY should you reuse same password on any two services. In other words, the most secure passwords are hardly memorable to ordinary people and the number of passwords you have to remember makes this task even harder.

That's where password managers kick in. Instead of remembering each password, you only have to remember the password for your password manager (the "master password"), and the password manager remembers your other passwords for you. But how? They store your other passwords in a vault (a simple encrypted database). However, as with any database, a vault requires management: you need to store it somewhere (which means more backups), sync it across all your devices (you definitely want to access your services from home/work laptops, smartphone, tablet etc). And as with any database management, there comes usability and security issues. Basically, you either have to manually update and manage the vault yourself (if you use a free open-source password manager) or rely on some kind of cloud-based service (often paid and proprietary) for that.

So it is a matter of usability vs security: either you're using a convenient proprietary password manager and have no idea if it is working as advertised, or you have more confidence in your open-source password manager, but have to deal with your vault yourself.

Wouldn't it be great to have a password manager without a vault? We would no longer have to manage vaults or rely on any third parties. This presentation introduces an open-source vaultless password manager, which does not store your passwords, but rather derives them from the master-password in a cryptographically secure manner. There is an option to generate secure cryptographic keys so that your passwords/keys are never stored anywhere, but can be reliably regenerated when needed.


Presentation: https://drive.google.com/file/d/1B5CXRaTzG8yYTW6sN9L70GW3NBLpZVJb/view?usp=sharing
GitHub: https://github.com/cloudflare/gokey

</details>

<details><summary><strong>Real-Time AD Attack Detection: Detect Attacks Leveraging Domain Administrator Privilege</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Wataru Matsuda](https://img.shields.io/badge/Wataru%20Matsuda-informational) ![Mariko Fujimoto](https://img.shields.io/badge/Mariko%20Fujimoto-informational) ![Takuho Mitsunaga](https://img.shields.io/badge/Takuho%20Mitsunaga-informational)

🔗 **Link:** [Real-Time AD Attack Detection: Detect Attacks Leveraging Domain Administrator Privilege](https://github.com/0xe7/WonkaVision)  
📝 **Description:** In Advanced Persistent Threat (APT) attacks, attackers tend to attack the Active Directory to expand infections. Attackers try to take over Domain Administrator privileges and create a backdoor called the "Golden Ticket". Attackers leverage this Golden Ticket to disguise themselves as legitimate accounts and obtain long-term administrator privilege. However, detecting attacks that use this method is quite difficult because the attackers' use of legitimate accounts and commands are not identified as anomalies.

We introduce a real-time detection tool that uses Domain Controller Event logs for detecting attack activities leveraging Domain Administrator privileges. Our tool can minimize the damages these types of attacks can cause even if the attackers maliciously take advantage of the Golden Ticket.

Our tool consists of the following steps to reduce false detection rate and support immediate incident response.

Step1 (Signature based detection): Analyze Event logs focusing on the characteristics of the attack activities.
Step2 (Machine Learning): Use unsupervised machine learning and anomaly detection in order to detect suspicious commands that attackers tend to use as outliers.
Step3 (Real-time alert): Raise real-time alerts using Elastic Stack if attack activities are detected.

We will publish our tool on GitHub and show specific algorithms that we have implemented so that visitors can customize or develop their own system. Our tool is all open sourced, enabling immediate and efficient incident responses against attacks at a reasonable cost.

Presentation: ﻿https://github.com/sisoc-tokyo/Real-timeDetectionAD/blob/master/Arsenal_eu-18-Real-time-Detection-of-Attacks-Leveraging-Domain-Administrator-Privilege.pdf

</details>

<details><summary><strong>SNDBOX: The Artificial Intelligence Malware Research Platform</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ran Dubin](https://img.shields.io/badge/Ran%20Dubin-informational) ![Ariel Koren](https://img.shields.io/badge/Ariel%20Koren-informational)

🔗 **Link:** [SNDBOX: The Artificial Intelligence Malware Research Platform](https://github.com/FOSDEM/video-meta/blob/master/fosdem2017/released.yml)  
📝 **Description:** SNDBOX is the world's first Artificial Intelligence (AI) malware research platform designed to scale up research time. Developed by researchers for researchers, SNDBOX offers never-seen-before malware analysis visibility powered by kernel mode next generation sandbox. Multiple AI detection vectors work alongside our big data malware similarity engine to reduce false positive classification errors. Behavioral signatures, multi-vector deep learning classifiers and multiple AI similarity search engines seamlessly work together to provide high visibility and data-driven explanations to scale malware research capabilities and reduce research time. Furthermore, with full access to our data, all levels of your team can leverage information necessary for complete malware remediation and new research possibilities, while sharing insights, public samples and IOC's through our community platform.

</details>

<details><summary><strong>tknk_scanner: Community-Based Integrated Malware Identification System</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Shota Nakajima](https://img.shields.io/badge/Shota%20Nakajima-informational) ![Keita Nomura](https://img.shields.io/badge/Keita%20Nomura-informational)

🔗 **Link:** Not Available  
📝 **Description:** The original code of a malware must be scanned using YARA rules after processing with a debugger (or other means) to account for obfuscated malware binaries. This is a complicated process and requires an extensive malware analysis environment. The tknk_scanner is a community-based integrated malware identification system, which aims to easily identify malware families by automating this process using an integration of open source community-based tools and freeware. The original malware code can be scanned with with your own YARA rules by submitting the malware in PE format to the scanner. tknk_scanner can thus support surface analysis performed by SOC operators, CSIRT members, and malware analysts.

</details>

<details><summary><strong>VirusTotal Graph: Investigation</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Daniel Sanchez](https://img.shields.io/badge/Daniel%20Sanchez-informational) ![Karl Hiramoto](https://img.shields.io/badge/Karl%20Hiramoto-informational)

🔗 **Link:** Not Available  
📝 **Description:** VirusTotal Graph is a free visualization tool built on top of the VirusTotal data set. It understands the relationship between files, urls, domains and ip addresses and it provides an easy interface to pivot and navigate over them. The tool is available for individual researchers and security professionals.

By exploring and expanding each of the nodes in your graph, you can build the network and see the connections across the samples you are studying. By clicking on the nodes, you can see at a glance the most relevant information for each item. You can also add labels and see an in-depth report by going to VirusTotal Public or VirusTotal Intelligence report.

The tool can also save a snapshot -as you see in your screen- of the graph, so that you can go back to your investigation any time and share your findings with other users. All saved graphs are public and linked in VirusTotal public report when the file, URL, IP address or domain appear in the graph. This intelligence benefits the entire community.

Learn more here: http://blog.virustotal.com/2018/01/virustotal-graph.html

Demo video: https://www.youtube.com/watch?v=QEqHXU04IkI&feature=youtu.be

</details>

---
## 🔴 Red Teaming
<details><summary><strong>AttackForge.com: Giving Time Back To Pentesters - More Breaking, Less Reporting</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Fil Filiposki](https://img.shields.io/badge/Fil%20Filiposki-informational) ![Stas Filshtinskiy](https://img.shields.io/badge/Stas%20Filshtinskiy-informational)

🔗 **Link:** Not Available  
📝 **Description:** Pentesters love what they do – breaking things. But there’s no denying that Penetration Testing as a practice itself is broken. Pentesters have only few days to a) learn how an entirely new system works under the hood; b) with this knowledge, learn some more so they can figure out how to break the system; c) try countless different ways to break the system or make it do things never intended or designed by the architects and developers; then d) write an executive and technical report to explain how they did it.

It feels like an impossible task for the typical <1-week project, so why on earth would you want to become or remain a pentester? When you do this week-in week-out, add on top pressures from clients, organisational bureaucracy, worrying about utilisation, fighting Word formatting, or having to constantly justify your risk ratings – it’s no wonder pentesters get burned out – fast!

We can’t fix all of these problems, but we have found a way to take some pressure off pentesters and help make communication, collaboration, transparency and reporting much easier, and reduce some of the overheads wasted on trivial tasks which all are part of a pentest project… introducing AttackForge.com.

</details>

<details><summary><strong>CoffeeShot: Memory Injection to Avoid Detection</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Asaf Aprozper](https://img.shields.io/badge/Asaf%20Aprozper-informational)

🔗 **Link:** [CoffeeShot: Memory Injection to Avoid Detection](https://github.com/MinervaLabsResearch/CoffeeShot)  
📝 **Description:** CoffeeShot is an evasion framework that designed for creating Java-based malware which bypasses most of the anti-virus vendors. The framework utilizes JNA (Java Native Access) to look for a victim process, once it finds it - a shellcode will be injected directly from the Java Archive file (JAR).

Java malware like "Jrat" and "Adwind" are used by malicious adversaries' day by day, more and more. Their main reason to write malware in Java is to be evasive and avoid security products - including those that use advanced features like machine learning. To overcome the above, blue-team members can use this framework in assessing the effectiveness of their anti-malware measures against malicious software written in Java.

On the other hand, CoffeeShot can be applied by penetration testers as well. The framework provides red-teamers a friendly toolset by allowing them to embed any shellcode in a JAR file, assisting them to avoid detection with memory injection and to PWN the target!

</details>

<details><summary><strong>iBombShell: Dynamic Remote Shell</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pablo Gonzalez Perez](https://img.shields.io/badge/Pablo%20Gonzalez%20Perez-informational) ![Álvaro Nuñez-Romero](https://img.shields.io/badge/Álvaro%20Nuñez-Romero-informational)

🔗 **Link:** [iBombShell: Dynamic Remote Shell](https://github.com/Matir/jspassphrase/blob/master/wordlist.json)  
📝 **Description:** The emergence of PowerShell within pentesting post-exploitation is important. Its flexibility, possibilities and power make this Microsoft´s command line an efficient post-exploitation tool. In scenarios where we cannot use neither install pentesting techniques this tool acquires special relevance. iBombShell gives access to a pentesting repository where the pentester could use any function oriented to the post-exploitation phase and, in some cases, exploit vulnerabilities. iBombShell is a remote pentesting Shell that loads itself automatically in memory offering unlimited tools for the pentester.

iBombShell is a tool written in PowerShell that allows post-exploitation functionalities in a shell or a prompt, anytime and in any operating system. Moreover, it allows, in some cases, the execution of vulnerability exploitation features. These features are loaded dynamically, depending on when they are needed, from a GitHub repository.

The shell is downloaded directly to memory giving access to many pentesting features and functionalities, avoiding any hard drive access. These functionalities downloaded to memory are in PowerShell function format. This execution strategy is called EveryWhere.

In addition, iBombShell allows a second way of execution called Silently. Using this execution way, an iBombShell instance (called warrior) can be launched. When the Warrior is executed over a compromised machine, it will connect to a C2 through the http protocol. From the C2, written in Python, a warrior can be controlled to dynamically load functions to the memory and to offer pentesting remote execution functionalities. All those steps are part of the post-exploitation phase.

</details>

<details><summary><strong>NetRipper: Smart Traffic Sniffing for PenetrationTesters</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ionut Gabriel Popescu](https://img.shields.io/badge/Ionut%20Gabriel%20Popescu-informational)

🔗 **Link:** Not Available  
📝 **Description:** NetRipper is a post-exploitation tool targeting Windows systems which uses API hooking in order to intercept network traffic. It also uses encryption-related functions from a low privileged user, making it able to capture both plain-text traffic and encrypted traffic before encryption/after decryption.

</details>

<details><summary><strong>OWASP Nettacker: Automated Penetration Testing Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ali Razmjoo Qalaei](https://img.shields.io/badge/Ali%20Razmjoo%20Qalaei-informational) ![Mohammad Reza Espargham](https://img.shields.io/badge/Mohammad%20Reza%20Espargham-informational) ![Abbas Naderi Afooshteh](https://img.shields.io/badge/Abbas%20Naderi%20Afooshteh-informational)

🔗 **Link:** Not Available  
📝 **Description:** OWASP Nettacker project is created to automate information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and other information. This software will utilize TCP SYN, ACK, ICMP and many other protocols in order to detect and bypass Firewall/IDS/IPS devices. By leveraging a unique method in OWASP Nettacker for discovering protected services and devices such as SCADA. It would make a competitive edge compared to other scanner making it one of the bests.

</details>

<details><summary><strong>SCAVENGER: A Post-Exploitation Scanning/Mapping Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Philip Pieterse](https://img.shields.io/badge/Philip%20Pieterse-informational)

🔗 **Link:** [SCAVENGER: A Post-Exploitation Scanning/Mapping Tool](https://github.com/brianckeegan/Trailers/blob/master/joined_data.csv)  
📝 **Description:** SCAVENGER is a multi-threaded post-exploitation scanning tool for mapping systems and finding "interesting" and most frequently used files, folders and services. Once credentials are gained, it can scan remote systems (Linux, Windows and OSX) via services like SMB and SSH to scrape that system looking for "interesting" things and then cache the result. SCAVENGER has the ability to find the newest files that have been accessed/modified/created and keep the result in an ordered database. Then, after time has passed, hours or days later the systems can be scanned again. SCAVENGER can then compare the previous list of "newest files" to the latest list of "newest files." This gives the user the ability to find the "interesting" and most frequently files used on that system, for example password files being accessed by an administrator or heavily used credit card database files.

Whilst looking for "interesting" files, folder and services, SCAVENGER scans these filenames and their content for various "interesting" phrases, for example "password" or "secret." Once detected SCAVENGER then downloads the "interesting" file to the local system. At the same time SCAVENGER also scans for Card Holder Data and also downloads the file if Card Holder Data is found.

Future features will be the addition of services like NFS, FTP and database connections. Also adding more capability of retrieving passwords from remote Linux or Windows systems, without touching to the disk of the remote system. And without reinventing the wheel using SCAVENGER as a wrapper to use on Windows systems performing more post-exploitation techniques.

Source Code: https://github.com/SpiderLabs/scavenger﻿

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>CryptGrep: Rapidly Search a Cryptographic Function to Analyze Malware</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Hiroki Hada](https://img.shields.io/badge/Hiroki%20Hada-informational) ![Tomonori Ikuse](https://img.shields.io/badge/Tomonori%20Ikuse-informational)

🔗 **Link:** Not Available  
📝 **Description:** 'CryptGrep' is an IDA python script which makes it possible to search a cryptography function to analyze malware rapidly. There are many existing implementations such as 'FindCrypt' (http://www.hexblog.com/?p=28) and 'idascope' (https://github.com/nihilus/idascope) which take an approach to find cryptographic magic number statically.

But, there are some cryptographic algorithm that doesn't use a magic number such as RC4, or malware can also hide the magic number. We needed another tool that can apply for these malware. The same malware family usually use the same cryptographic algorithm, and don't change their algorithm and implementation so frequently. Therefore, CryptGrep adopted signature based approach. Our approach also uses improved 'BinGrep' algorithm that was specialized for cryptographic function using several heuristic technique.

We created several pre-set signatures for typical malware. The usage is very simple and easy. And if you need additional signature, you can also create your original signature using your malware.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>IoT-Home-Guard: A Tool for Malicious Behavior Detection in IoT Devices</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Yuan Zhuang](https://img.shields.io/badge/Yuan%20Zhuang-informational) ![Qinghao Tang](https://img.shields.io/badge/Qinghao%20Tang-informational)

🔗 **Link:** Not Available  
📝 **Description:** IoT devices, especially secondhand devices and rental devices, are under threat of malware implant attack with physical access. Once IoT devices are compromised, hackers can turn them into snooping devices. From a defensive perspective, there are no solutions to detect Trojans in IoT devices.

We present IoT-Home-Guard, a hardware device to detect malicious behaviors of Trojans in IoT devices, such as audios/videos snoop and remote control. It consists of four parts: data flow catcher, traffic analyzing engine, device fingerprint database and a web server. Features of network traffic are extracted by traffic analyzing engine and compared with pre-built device fingerprint database to detect malicious behaviors.

In another research, we were able to implant Trojans in eight devices including smart speakers, ip cameras, routers, driving recorders and mobile translators. We collected characteristics of those devices and ran IoT-Home-Guard. All devices implanted Trojans have been detected. We believe that malicious behaviors of more devices can be identified with high accuracy after supplement of fingerprint database.

The first generation IoT-Home-Guard tool is a hardware device based on Raspberry Pi with wireless network interface controllers. We will customize new hardware in the second generation. Software part is available in our Github (https://github.com/arthastang/IoT-Home-Guard). The system can be set up with software part in laptops after essential environment configuration.

</details>

<details><summary><strong>IoT-Implant-Toolkit: Framework for Trojans Implantation Research of IoT Devices</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jiawei Cao](https://img.shields.io/badge/Jiawei%20Cao-informational) ![Qinghao Tang](https://img.shields.io/badge/Qinghao%20Tang-informational)

🔗 **Link:** Not Available  
📝 **Description:** During our Trojans implantation research for IoT devices, we found many tools outdated and not compatible with high versions. We present IoT-Implant-Toolkit, a framework for Trojans implantation research of IoT devices. It is a toolkit consisting of essential software tools on firmware modification, serial port debugging, software analysis and stable spy clients. We wrapped tools we proved useable in the framework and provided a universal call interface. Additionally, we packed useful open-source tools we developed into the framework. Each software tool acts as a plugin which can be easily added into the framework. With an easy-to-use and extensible shell-like environment, IoT-Implant-Toolkit is a one-stop-shop toolkit simplifying complex procedure of IoT malware implantation.

With IoT-Implant-Toolkit, we were able to implant Trojans in eight devices with physical access, including smart speakers, cameras, driving recorders and mobile translators. We turned them into snooping devices, which send audios or videos in real time. Our presentation will also include live demos of those implanted devices.

IoT-Implant-Toolkit is open-source at https://github.com/arthastang/IoT-Implant-Toolkit.

</details>

<details><summary><strong>IoXT Hunter: A Remote Discover & Pentest Tool for IoT Devices</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Hao Zhao](https://img.shields.io/badge/Hao%20Zhao-informational)

🔗 **Link:** Not Available  
📝 **Description:** IoXT Hunter is an open source, extendable, large-scale IoT device remote discovery and pentest tool. It is designed to discover all known IoT devices for a specified range of network addresses and to perform security testing on related IoT devices using generic or targeted payloads.

If you are a security administrator for a complex or large-scale IoT network (such as an industrial IoT network or a medical IoT network), IoXT Hunter will be your powerful tool. It can help you discover and record all your IoT device assets and perform full remote security testing of your IoT devices.

IoXT Hunter also supports writing and loading your own plugins extensions. If you are an IoT security researcher and have discovered the security vulnerabilities of a kind of IoT device. You can write the appropriate discovery and pentest scripts to scan and evaluate the status of the IoT device on the public network through the IoXT Hunter.

</details>

<details><summary><strong>RadioT Shield: A Radio Way to Protect Most of Your IoT Devices</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Hao Zhao](https://img.shields.io/badge/Hao%20Zhao-informational)

🔗 **Link:** Not Available  
📝 **Description:** RadioT Shield is an open source platform dedicated to detecting the attack of various IoT devices in a given space by radio communication data. RadioT Shield can detect a lot of radio-based IoT-related attacks, such as WIFI attacks, BLE attacks, GSM attacks, ZigBee attacks, etc. Unlike other IoT hardware and software security solutions, this system does not require any modification of the protected IoT device and does not affect the existing functionality of the device.

RadioT Shield is suitable for all IoT devices that use radio communications, even devices that are more than a decade old. It is therefore particularly suitable for scenarios with complex IoT device types and IoT networks consisting of old, non-secure IoT devices, especially industrial control IoT devices, medical IoT devices, smart home IoT devices, and more.

</details>

<details><summary><strong>RPL Attacks Framework: Attacking RPL in WSNs</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Alexandre D'Hondt](https://img.shields.io/badge/Alexandre%20D'Hondt-informational)

🔗 **Link:** [RPL Attacks Framework: Attacking RPL in WSNs](https://github.com/wannadie/mendeley-parser/blob/master/output/electrical-and-electronic-engineering/electrical-and-electronic-engineering-p.csv)  
📝 **Description:** This tool is a framework for attacking the Routing Protocol for Low power and lossy networks (RPL) implementation of Contiki for Wireless Sensor Networks (WSN).

Presentation: https://github.com/dhondta/rpl-attacks/raw/master/doc/bheu18-arsenal-presentation.pdf

</details>

<details><summary><strong>Universal Radio Hacker v2: Simulate Wireless Devices with Software Defined Radio</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Johannes Pohl](https://img.shields.io/badge/Johannes%20Pohl-informational)

🔗 **Link:** [Universal Radio Hacker v2: Simulate Wireless Devices with Software Defined Radio](https://github.com/jopohl/urh)  
📝 **Description:** Wireless communication between Internet of Things (IoT) devices is, in many cases, built upon proprietary protocols designed under size and energy constraints. Vulnerabilties in such protocols are critical, e.g. an attacker breaks into a house by hacking a wireless door lock. Software Defined Radios (SDR) offer a generic way to investigate such protocols, but require software support when it comes to demodulating and decoding messages. The Universal Radio Hacker (URH) is an open source tool to support researchers when operating with SDRs by abstracting most of the required HF basics needed for demodulation. Furthermore, it assists reverse engineering the protocol format. While this works well for stateless and undirectional protocols, there are more sophisticated protocols on the market that can not be handled without state machine.

Version 2.0 of the Universal Radio Hacker introduces a Simulation tab that allows to specify a complete HF protocol with several states and participants. It is called Simulation because URH has the ability to play the protocol from the perspective of one or more participants, i.e. URH evaluates all messages towards the simulated participant and dynamically crafts responses depending on the state and previous information. The simulation advancement complies to the easy-to-use philosophy that we also use for the basic URH. Users can see all messages of the analyzed protocol in a graphical flow graph and add new messages, edit or move them around at convenience. Message field values are dynamically derived with access to all previously sent and received information or even by using external programs, e.g. for AES encryption. Conditions, jump and pause elements in the graphical user interface allow generating complex state machines. In our presentation, we demonstrate a practical attack that shows how the simulation component of URH opens a sophisticated wireless door lock (AES encryption) with SDRs.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Kurukshetra: Playground for Interactive Security Learning</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Anirudh Anand](https://img.shields.io/badge/Anirudh%20Anand-informational) ![Mohan Kallepalli](https://img.shields.io/badge/Mohan%20Kallepalli-informational)

🔗 **Link:** Not Available  
📝 **Description:** Kurukshetra is a web framework that's developed with the aim of being the first open source framework which provides a solid foundation to host reasonably complex secure coding challenges where developers can learn secure coding practices in a hands-on manner. It is composed of two components, the backend framework written in PHP, which manages and leverages the underlying docker system to provide the secure sandbox for the challenge execution, and the frontend, which is a user facing web app providing all the necessary controls, for the admin to host and modify the challenges, and the user to execute and view the result of each of his input.

The Framework currently supports challenges written in 4 major languages including PHP, Python, NodeJS and Ruby.

</details>

<details><summary><strong>Security Code Scan: Vulnerability Patterns Detector</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Jaroslav Lobacevski](https://img.shields.io/badge/Jaroslav%20Lobacevski-informational)

🔗 **Link:** Not Available  
📝 **Description:** Security Code Scan is static code analysis tool for C# and VB.NET. It detects various security vulnerability patterns: SQL and XPath injections, Cross-Site Request Forgery (CSRF), XML eXternal Entity Injection (XXE), unsafe deserialization and many more...

It is available as Visual Studio extension (2015 and higher), but can be integrated into other editors, that support Roslyn analyzers. It is also available as NuGet package and can be integrated into continuous integration builds.

</details>

---
## 🔍 OSINT
<details><summary><strong>Maltego: "Have I Been Pwned?""PwnedPasswords" and "FullContact"</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Christian Heinrich](https://img.shields.io/badge/Christian%20Heinrich-informational)

🔗 **Link:** Not Available  
📝 **Description:** “Have I been pwned?" allows you to search across multiple data breaches to see if your email addresses or aliases has been compromised by LinkedIn, MySpace, Dropbox, etc.

"PwnedPasswords" are half a billion real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.

"FullContact" allows you to enrich a Twitter username, location, person's name, company and alias or verify an e-mail address.

Maltego is a link analysis application of technical infrastructure and/or social media networks from disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project.

The integration of "Have I been pwned?” "PwnedPasswords" and "FullContact" with Maltego presents this data in an easy to understand graph format that can be enriched with other sources.

Release:

Major Update i.e. "Have I Been Pwned?"
New tool to be released at Black Hat i.e. "FullContact"

</details>

<details><summary><strong>Squatm3: Cybersquatting Made Easy</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Davide Cioccia](https://img.shields.io/badge/Davide%20Cioccia-informational)

🔗 **Link:** Not Available  
📝 **Description:** Squatm3 is a python tool designed to enumerate available domains generated modifying the original domain name through different techniques:

Substitution attacks
Flipping attack
Homoglyph attack

Squatm3 will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks.

Presentation: https://www.dropbox.com/s/8r9t16s4x94iczu/blackhat-eu18-arsenal.pptx?dl=0

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>XSSER: From XSS to RCE 3.0</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Hans-Michael Varbaek](https://img.shields.io/badge/Hans-Michael%20Varbaek-informational)

🔗 **Link:** [XSSER: From XSS to RCE 3.0](https://github.com/Varbaek/xsser)  
📝 **Description:** This presentation demonstrates how an attacker can utilize XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes more payloads for common web apps and various other improvements too!

</details>

---