# Europe 2023
---
📍 61 tools demonstrated at **Black Hat Arsenal Europe 2023**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [⚙️ Miscellaneous / Lab Tools](#-miscellaneous--lab-tools) (3)
- [🌐 Web/AppSec](#-webappsec) (4)
- [🌐 Web/AppSec or Red Teaming](#-webappsec-or-red-teaming) (2)
- [📱 Mobile Security](#-mobile-security) (3)
- [🔍 OSINT](#-osint) (3)
- [🔴 Red Teaming](#-red-teaming) (16)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (11)
- [🔵 Blue Team & Detection](#-blue-team--detection) (14)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (2)
- [🧠 Reverse Engineering](#-reverse-engineering) (3)
---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Drone Remote ID Spoofer and Low Cost Receiver Application</strong> — Llorenç Romá Alvarez</summary>

**Track:** Arsenal Lab · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/cyber-defence-campus/droneRemoteIDSpoofer](https://github.com/cyber-defence-campus/droneRemoteIDSpoofer)  
📝 **Description:** Get hands-on with us as we dive into the world of drone defense where we will monitor and spoof drones in real-time. We will show how to monitor various Remote IDs including popular proprietary and open formats. Next we will spoof fake drone Remote IDs which can be customized to appear as multiple drones and pilots in specific areas. No experience required – just an open mind.

</details>

<details><summary><strong>Hands-on Firmware Extraction, Exploiration, and Emulation</strong> — Quentin Kaiser, Florian Lukavsky</summary>

**Track:** Arsenal Lab · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/onekey-sec/firmware-workshop](https://github.com/onekey-sec/firmware-workshop)  
📝 **Description:** Join us for this hands-on demo of Unblob, the flexible firmware extractor. In this Arsenal lab session, we will extract firmware from an EV charger, dig into the firmware, and eventually emulate it so we can interact with the services in real-time. Unblob works on both hardware and downloadable versions of firmware so we have a target rich environment. No prior experience needed, this session is appropriate for all skillsets and we are looking forward to see you there.

</details>

<details><summary><strong>Rapid Fire: Flipper vs. All the Things</strong> — Pavlo Zhovner</summary>

**Track:** Arsenal Lab · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)  
📝 **Description:** Join CEO and co-creator of Flipper Devices, Pavlo Zhovner, for a rapid fire session of hack all the things. Get hands-on with flipper zero trying it out against various *approved* targets. This ultra flexible device is able to read, copy, and emulate RFID and NFC tags, radio remotes, iButton, and digital access keys, along with a GPIO interface. We are looking forward to seeing you soon.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Akto - Open Source API Security Tool</strong> — Ankush Jain</summary>

**Track:** Web AppSec · Vulnerability Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/akto-api-security/akto](https://github.com/akto-api-security/akto)  
📝 **Description:** We released Open source Akto in Feb '23 & we have 310 stars on Github. This tool is mainly focuses on solving the problems below: - Tough api inventory for both testers, compliance and developers - Testing with complex chained apis - Multi step authentication, refresh/access token etc. - Automated testing of APIs - Both OWASP Top 10 and some business logic tests Our tool Akto focuses on solving the above problems by providing: 1. Provide automated API inventory - 1.a) Automated - Akto can populate inventory automatically from traffic sources like Burp Proxy, Postman or even Chrome HAR files. 1.b) All formats - Akto also covers different formats of APIs such as JSON, GraphQL, gRPC, JSONP, forms. 2. Inspects traffic & provides alerts on suspicious apis - 2.a) Sensitive data - Akto comes with an in-built library for sensitive data patterns. Akto can tell which APIs are sharing sensitive data such as SSN, email, Phone number etc. Users can add their own patterns too. 2.b) Alerts - Users can set up daily alerts using Slack and Webhooks to get alerts about new sensitive data/APIs found 3. Automated API testing which covers OWASP Top 10 & some business logic testing 3.a) OWASP Coverage - Akto has 130+ tests to cover for OWASP Top 10 3.b) Business logic tests - Akto also supports business logic tests such as BOLA, Broken Function Level Authorization, Broken Authentication etc. 3.c) Add your own - Users can also add their own tests. This tool will be very interesting for: - Bugbounty Hunters - has a blackbox feature where complex apis can be uploaded from Burp history & can be useful for chained requests. - Pentesters & testing teams in appsec - getting accurate api collection is complex & time consuming. Provides a one stop solution for getting the inventory. Tests like BOLA and BFLA will be especially interesting for them. - Blue teamers/infra security - Getting an automated API inventory and getting alerts for any new sensitive APIs. They can also get a view of all sensitive PII data being shared across all their services and across all their APIs. They can check unauthenticated APIs, download the swagger file and use it in other security apps too.

</details>

<details><summary><strong>HAWK Eye - PII & Secret Detection tool for your Servers, Database, Filesystems, Cloud Storage Services</strong> — Rohit Kumar</summary>

**Track:** Web AppSec · Human Factors · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/rohitcoder/hawk-eye](https://github.com/rohitcoder/hawk-eye)  
📝 **Description:** HAWK Eye is a powerful Command-Line Interface (CLI) tool designed to enhance data source security by detecting and protecting Personally Identifiable Information (PII) across various platforms. Inspired by the precision and vision of majestic birds of prey, HAWK Eye swiftly scans multiple data sources, including S3, MySQL, Redis, Firebase, filesystem, and Google Cloud Storage (GCS), for potential data breaches and cyber threats. With data breaches becoming more prevalent, organizations need robust security measures to safeguard sensitive information. HAWK Eye provides a comprehensive solution, capable of seamlessly integrating with different data sources to identify and protect PII. Its extensible architecture allows developers to contribute new commands, empowering the tool to address evolving security needs. Future Roadmap: HAWK Eye is continuously evolving, and we have an exciting roadmap ahead! Our plans include adding support for more than 20+ additional data sources, such as MongoDB, Jira, and ticketing services. These integrations will enable HAWK Eye to detect PII and secrets from a diverse range of applications, ensuring comprehensive data source security for users.

</details>

<details><summary><strong>Revealing 2MS: New Secrets Detection Open Source, the Connection to Supply Chain Attacks, and The Developer's Responsibility</strong> — Harush Kadouri Jossef, Tzachi Zorenshtain</summary>

**Track:** Web AppSec · Code Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/Checkmarx/2ms](https://github.com/Checkmarx/2ms)  
📝 **Description:** Too many secrets (2ms) is a command line tool written in Go language and built over gitleaks. 2ms is capable of finding secrets such as login credentials, API keys, SSH keys and more hidden in code, content systems, chat applications and more. https://github.com/checkmarx/2ms

</details>

<details><summary><strong>Security Attacks as Software Tests: Building dev-oriented AppSec challenges with Play open source SDK</strong> — Pedram Hayati</summary>

**Track:** Web AppSec · Vulnerability Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/secdim/play-sdk](https://github.com/secdim/play-sdk)  
📝 **Description:** This talk focuses on the unique process of transforming security attacks into software tests for building secure programming challenges using an open-source SDK, 'Play'. A practical workshop where we explore the mechanics of choosing real-world-inspired security vulnerabilities, and transforming them into cloud-native apps with integrated security tests which can then be played as challenges. These challenge provides a new dimension to the traditional Capture The Flag experiences, emphasizing not just the identification but the remediation of vulnerabilities

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Defending GitHub Actions: Unmasking Attack Vectors and Verifying Integrity with eBPF</strong> — Weinberger Mor</summary>

**Track:** Code Assessment · Web AppSec · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/cilium/ebpf](https://github.com/cilium/ebpf)  
📝 **Description:** GitHub Actions has gained immense popularity as a powerful tool for software development and release. However, this popularity has also attracted bad actors, In this session, we will delve into the active risks that attackers leverage to abuse and attack GitHub Actions, shedding light on their techniques and exploits. In response, we will show an OSS Runtime Security solution, which introduces the concept of profiling with eBPF the CI\CD runtime environment, we will demonstrated how it can prevent and alert on malicious behaviour, and create a build profile of the environment

</details>

<details><summary><strong>promptmap</strong> — Utku Sen</summary>

**Track:** Code Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/utkusen/promptmap](https://github.com/utkusen/promptmap)  
📝 **Description:** Prompt injection is a type of security vulnerability that can be exploited to control the behavior of a ChatGPT instance. By injecting malicious prompts into the system, an attacker can force the ChatGPT instance to do unintended actions. promptmap is a tool that automatically tests prompt injection attacks on ChatGPT instances. It analyzes your ChatGPT rules to understand its context and purpose. This understanding is used to generate creative attack prompts tailored for the target. promptmap then run a ChatGPT instance with the system prompts provided by you and sends attack prompts to it. It can determine whether the prompt injection attack was successful by checking the answer coming from your ChatGPT instance.

</details>

---
## 📱 Mobile Security
<details><summary><strong>AndroCop: One Click Forensic Investigation & Data Extraction Tool</strong> — Abhinand N, Aswin M Guptha, Varun Nair</summary>

**Track:** Android, iOS and Mobile Hacking · Data Forensics/Incident Response · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** AndroCop is a powerful and streamlined tool for in-depth forensic analysis and data extraction from Android devices, delivering rapid insights and efficient data export. The application, written in Java, streamlines the process of forensic investigation and data retrieval, eliminating the need for external utilities. With a single click, AndroCop aggregates and exports a diverse array of data, encompassing call records, text messages, contacts, application usage records, device information, image captures, and screenshots. The tool enriches forensic investigation by facilitating the identification of potentially harmful Android applications, deciphering app usage patterns, extracting valuable call history insights, and revealing visited locations. Moreover, AndroCop helps users to export forensic findings and data in multiple formats such as PDFs, XLSX spreadsheets, and CSV files. All the gathered information, along with images and other related data, will be consolidated into a singular ZIP file, streamlining the process of smooth data transmission. The gathered content is placed in the AndroCop directory within the internal storage, prepared for effortless transfer whenever required. AndroCop is also designed to be user-friendly, with a simple and intuitive interface that makes it easy to use for both novice and experienced users. It helps users quickly extract and analyze data from Android devices, making it an important addition to any forensic investigator's toolkit.

</details>

<details><summary><strong>Mobile Security Framework - MobSF</strong> — Ajin Abraham</summary>

**Track:** Android, iOS and Mobile Hacking · Exploitation and Ethical Hacking · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)  
📝 **Description:** Mobile Security Framework - MobSF is an automated mobile application security testing environment designed to help security engineers, researchers, developers, and penetration testers to identify security vulnerabilities, malicious behaviors and privacy concerns in mobile applications using static and dynamic analysis. It supports all the popular mobile application binaries and source code formats built for Android and iOS devices. In addition to automated security assessment, it also offers an interactive testing environment to build and execute scenario based test/fuzz cases against the application. Visit our Arsenal station to witness: * Brand new MobSF iOS Dynamic Analyzer * Live Pentest of Android/iOS apps * Solving Mobile app CTF challenges * Reverse engineering and runtime analysis of Mobile malware * How to shift left and integrate MobSF/mobsfscan in your build pipeline

</details>

<details><summary><strong>MORF - Mobile Reconnaissance Framework</strong> — Amrudesh Balakrishnan, Abhishek JM, Himanshu Das</summary>

**Track:** Android, iOS and Mobile Hacking · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/amrudesh1/morf](https://github.com/amrudesh1/morf)  
📝 **Description:** MORF - Mobile Reconnaissance Framework is a powerful, lightweight, and platform-independent offensive mobile security tool designed to help hackers and developers identify and address sensitive information within mobile applications. It is like a Swiss army knife for mobile application security, as it uses heuristics-based techniques to search through the codebase, creating a comprehensive repository of sensitive information it finds. This makes it easy to identify and address any potentially sensitive data leak. One of the prominent features of MORF is its ability to automatically detect and extract sensitive information from various sources, including source code, resource files, and native libraries. It also collects a large amount of metadata from the application, which can be used to create data science models that can predict and detect potential security threats. MORF also looks into all previous versions of the application, bringing transparency to the security posture of the application. The tool boasts a user-friendly interface and an easy-to-use reporting system that makes it simple for hackers and security professionals to review and address any identified issues. With MORF, you can know that your mobile application's security is in good hands. Overall, MORF is a Swiss army knife for offensive mobile application security, as it saves a lot of time, increases efficiency, enables a data-driven approach, allows for transparency in the security posture of the application by looking into all previous versions, and minimizes the risk of data breaches related to sensitive information, all this by using heuristics-based techniques.

</details>

---
## 🔍 OSINT
<details><summary><strong>!CVE: A New Platform for Unacknowledged Cybersecurity !Vulnerabilities</strong> — Hector Marco, Samuel Arevalo</summary>

**Track:** OSINT - Open Source Intelligence · Vulnerability Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://www.notcve.org/](https://www.notcve.org/)  
📝 **Description:** In the ever-evolving cybersecurity landscape, the identification and acknowledgment of vulnerabilities through the Common Vulnerabilities and Exposures (CVE) system play a crucial role. However, vendor discretion in determining whether a security issue warrants a CVE assignment often results in overlooked vulnerabilities that pose significant risks. This presentation introduces the !CVE initiative, a groundbreaking platform that addresses this critical gap by identifying, tracking, and sharing unacknowledged cybersecurity vulnerabilities. Our presentation begins with an overview of the CVE system and the challenges security researchers face in dealing with unacknowledged vulnerabilities. We discuss real-world examples of security issues ignored by vendors and explore the potential consequences of these hidden threats. We then delve into the !CVE platform, detailing its mission, features, and collaborative approach to empower the security community. Through case studies, we demonstrate the value of the !CVE initiative in strengthening the cybersecurity ecosystem, highlighting the significance of addressing vulnerabilities not recognized by vendors. We also showcase the reporting process, expert panel, and public availability of !CVE reports, fostering a transparent and inclusive environment for vulnerability tracking and sharing. Join us in exploring the world of unacknowledged cybersecurity vulnerabilities and learn how the !CVE initiative is bridging the gap between vendor discretion and community-driven security efforts. By raising awareness and fostering collaboration, we can create a more secure and resilient digital landscape for all.

</details>

<details><summary><strong>Mantis - Asset Discovery at Scale</strong> — Prateek Thakare, Praveen Kanniah, Bharath Kumar</summary>

**Track:** OSINT - Open Source Intelligence · Web AppSec · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/PhonePe/mantis](https://github.com/PhonePe/mantis)  
📝 **Description:** Mantis is an asset inventory framework that has the capability to distribute a single scan across multiple machines, provides easy customization, dashboard support, and advanced alerting capabilities. We have not reinvented the wheel. Rather, we have tried to design an architecture that provides the essential features for a framework that involves the complexity of integrating multiple tools that are outside our control. Our key differentiators include: - Recon Automation - Asset Discovery (subdomain, certificates) - Tech Recon - Scan - Secrets Scanning (JS, WaybackUrls, Github - experimental) - Identifying Phishing domains - Misconfigurations - Distribute a single scan and fasten your scan speeds by 2x. - Understanding scan efficiency and failure points of a scan drilled down at a subdomain level - Adding new tools in no time - Advanced Alerting based on - Teams - Apps - Assets/Findings - User Tagging - Default Dashboard support (AppSmith) - Integration with DNS services (Route53) - Workflow Customisation (choose tools and modules you want to run) - Automated Scheduled Scans

</details>

<details><summary><strong>Octopii v2</strong> — Owais Shaikh, Umair Nehri</summary>

**Track:** OSINT - Open Source Intelligence · Human Factors · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/redhuntlabs/Octopii](https://github.com/redhuntlabs/Octopii)  
📝 **Description:** Today, given the number of services that collect Personal Identifiable Information (PII) for purposes such as 'KYC' (Know Your Customer) documents, bureaus keeping records of people, small businesses keeping records of their employees, and so on, PII faces a wide variety of threats. With increasing security breaches, protecting valuable data such as Personal Identifiable Information must be the top priority of all organizations. The first step in accomplishing this is to identify the exposure of such assets. This is why we created Octopii, an AI-powered Personally Identifiable Information (PII) scanner that uses Optical Character Recognition (OCR), regular expression lists and Natural Language Processing (NLP) to search public-facing locations for Government ID, addresses, emails etc in images, PDFs and documents.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>AtlasReaper: Sowing Chaos and Reaping Rewards in Confluence and Jira</strong> — Craig Wright</summary>

**Track:** Malware Offense · Web AppSec · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/werdhaihai/atlasreaper](https://github.com/werdhaihai/atlasreaper)  
📝 **Description:** AtlasReaper is a .NET command-line tool developed for offensive security purposes, primarily focused on reconnaissance and keyword searching on Confluence and Jira instances. AtlasReaper also provides various features that are helpful for tasks such as credential farming and social engineering. AtlasReaper was designed to be run from Command and Control (C2) to reduce the network overhead incurred from establishing a SOCKS proxy. The tool leverages Atlassian REST APIs to query metadata and content from the target Confluence and Jira. Read operations include search, listspaces, listpages, listissues, listattachments, and listusers. Any attachments that look interesting can be downloaded. It is also possible to dump all of the data for offline processing. AtlasReaper extends its functionality with write operations, enabling users to attach files, create deceptive links, and comment on issues within Confluence or Jira. It is also contains functionality to embed images. Embedding 1x1 pixel images hosted on external servers enables stealthy NetNTLMv2 hash harvesting in Active Directory environments. The tool also facilitates targeted user engagement by @ mentioning victims on pages.

</details>

<details><summary><strong>CQPenetrationTesting Toolkit: A Powerful Toolset That All Pentesters Want to Have</strong> — Paula Januszkiewicz, Mike Jankowski-Lorek</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** CQ Penetration Testing Toolkit supports you in performing complex penetration tests, shows you their possible application, and highlights the situations in which they apply. It guides you through the process of gathering intel about network, workstations, and servers, and showcases common techniques for antimalware avoidance and bypass, lateral movement, and credential harvesting. The toolkit also allows decrypting RSA keys and EFS-protected files as well as blobs and objects protected by DPAPI and DPAPI NG. This powerful toolkit is useful for those who are interested in penetration testing and professionals engaged in pen-testing who work in the areas of databases, systems, networks, or application administration.

</details>

<details><summary><strong>Democratizing Attack Techniques in the Cloud withThe DeRF</strong> — Kat Traxler</summary>

**Track:** Exploitation and Ethical Hacking · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/vectra-ai-research/derf](https://github.com/vectra-ai-research/derf)  
📝 **Description:** DeRF (Detection Replay Framework) is an "Attacks As A Service" framework, allowing the emulation of offensive techniques and generation of repeatable detection samples from a UI - without the need for End Users to install software, use the CLI or possess credentials in the target environment. Notable built-in attack modules are listed below with a complete list of all built-in attack techniques in The DeRF documentation. o	AWS | EC2 Steal Instance Credentials o	AWS | Retrieve a High Number of Secrets Manager secrets. o	AWS | Stop CloudTrail o	AWS | Execute Commands on EC2 Instance via User Data o	AWS | EC2 Download User Data o	AWS | EC2 Share EBS Snapshot o	GCP | Impersonate Service Account Similar to other tools focused on detection generation, the DeRF deploys and manages the target cloud infrastructure, which is manipulated to simulate attacker techniques. Terraform is used to manage all resources, deploying (and destroying) hosted attack techniques and target infrastructure in under 3 minutes. While a bring-your-own-Infrastructure (BYOI) model isn't currently supported, maintaining The DeRF infrastructure costs less than $10/month for Google Cloud and $5/month for AWS. The tool's convenient deployment model means you can use it as needed rather than continuously running 24/7. Check out the deployment guide for more details. The initial release of The DeRF encompasses a wide range of prevalent cloud attack techniques, providing your organization with ample resources for training, controls testing, and executing on attack scenarios. However, as needs evolve, you may need to expand beyond the initial set and introduce your own custom attack modules. With The DeRF, this process is simplified. All attack techniques are defined as Google Cloud Workflows, which can be deployed as additional terraform modules within your forked version of the codebase.

</details>

<details><summary><strong>Docker Exploitation Framework</strong> — Emmanuel Law, Rohit Pitke</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/DockerExploitationFramework/DockerExploitationFramework](https://github.com/DockerExploitationFramework/DockerExploitationFramework)  
📝 **Description:** Docker Exploitation Framework is a cross-platform framework that is focused on attacking container environment (think kubernetes, docker etc). It can identify vulnerabilities, misconfigurations, and potential attack vectors. It also helps to automate different stages of a successful kill-chain through features such as: - Vulnerability Scanning - Container breakouts - Pod2Pod Lateral movement - File layers deep inspection and extraction - Attack Surface discovery and mapping - Privilege Escalation etc It uses a agent/server architecture. The agents are modular and are designed to be portable with minimal dependencies for maximum compatibility in restricted containers. This is a tool created for pentesters and red teamers.

</details>

<details><summary><strong>Echidna: Penetration Test Assist & Collaboration Tool</strong> — Yu Terada, Soya Aoyama, Kazuhisa Shirakami</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/crytic/echidna](https://github.com/crytic/echidna)  
📝 **Description:** Echidna is a tool designed to support teams or beginners in conducting penetration testing. While there are many tools available to assist or automate penetration testing, mastering them requires knowledge of numerous commands and techniques, making it challenging for beginners to learn and carry out penetration testing. Furthermore, when conducting penetration tests in a team, each member tends to work independently, which can lead to duplication of work and lack of visibility of progress for managers and beginners. Therefore, we developed Echidna, which visualizes and shares the terminal console of penetration testers, and recommends the next command based on each situation.

</details>

<details><summary><strong>EntraID Guest to Corp Data Dump with powerpwn</strong> — Michael Bargury, Lana Salameh, Inbar Raz</summary>

**Track:** Exploitation and Ethical Hacking · Malware Offense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/mbrg/power-pwn](https://github.com/mbrg/power-pwn)  
📝 **Description:** EntraID guest accounts are widely used to grant external parties limited access to enterprise resources, with the assumption that these accounts pose little security risk. As you're about to see, this assumption is dangerously wrong. powerpwn is an offensive security toolset for Microsoft 365 focused on Power Platform. It allows you to achieve the full potential of a guest in EntraID by exploiting a series of undocumented internal APIs and common misconfiguration for collecting privileges, and using those for data exfiltration and actions on target, leaving no traces behind. The tool operates by leveraging shared credentials shared over Power Platform, a low-code / no-code platform built into Office365. PowerGuest allows gaining unauthorized access to sensitive business data and capabilities including corporate SQL servers and Azure resources. Furthermore, it allows guests to create and control internal business applications to move laterally within the organization. All capabilities are fully operational with the default Office 365 and Azure AD configuration.

</details>

<details><summary><strong>go-exploit: An Exploit Framework for Go</strong> — Jacob Baines</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/vulncheck-oss/go-exploit](https://github.com/vulncheck-oss/go-exploit)  
📝 **Description:** go-exploit is an exploit development framework for Go. The framework helps exploit developers create small, self-contained, portable, and consistent exploits. Many proof-of-concept exploits rely on interpreted languages with complicated packaging systems. They implement wildly differing user interfaces, and have limited ability to be executed within a target network. Some exploits are integrated into massive frameworks that are burdened by years of features and dependencies which overwhelm developers and hinder the attacker's ability to deploy the exploits from unconventional locations. To overcome these challenges, go-exploit offers a lightweight framework with minimal dependencies, written in Go—a language renowned for its portability and cross-compilation capabilities. The framework strikes a balance between simplicity for rapid proof-of-concept development and the inclusion of sophisticated built-in features for operational use.

</details>

<details><summary><strong>HardeningMeter</strong> — Ouzan Ofri, Yotam Perkal</summary>

**Track:** Malware Offense · Malware Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/OfriOuzan/HardeningMeter](https://github.com/OfriOuzan/HardeningMeter)  
📝 **Description:** HardeningMeter is an open-source Python tool carefully designed to comprehensively assess the security hardening of binaries and systems. Its robust capabilities include thorough checks of various binary exploitation protection mechanisms, including Stack Canary, RELRO, randomizations (ASLR, PIC, PIE), None Exec Stack, Fortify, ASAN, NX bit. This tool is suitable for all types of binaries and provides accurate information about the hardening status of each binary, identifying those that deserve attention and those with robust security measures. The genesis of HardeningMeter stems from extensive research into the dynamic cat-and-mouse game between attackers and defenders when exploiting binaries. While certain binary hardening measures are designed to thwart binary exploitation, resourceful attackers continue to find ways to circumvent these protections. HardeningMeter is a wake-up call that raises awareness of the critical need to protect against binary exploitation, monitors vulnerable binaries that lack critical hardening, and promotes a broader understanding of the offensive research landscape. HardeningMeter's uniqueness lies in its precision, which is based on a deep understanding of binary structures, exploitation techniques, and hardening mechanisms. It supports all binary file types, including executables, dynamic executables, dynamic shared objects, relocatables, and statically linked files. The tool offers a significant benefit to users, each check that the tool performs is documented in detail to allow users to dive into the inner workings of binary hardening. Users can gain a deeper understanding of the underlying concepts, explore the intricacies of binary exploitation protection mechanisms, and expand their knowledge in this important area. Moreover, users can set the output to receive tailored recommendations on which binary files require heightened attention and monitoring. We hope to contribute to the cybersecurity community and benefit from their ideas and perceptions to extend our features and make HardeningMeter a better tool that supports systems other than Linux in the future.

</details>

<details><summary><strong>Malicious NFTs</strong> — Jubilian Ho Hong Yi</summary>

**Track:** Exploitation and Ethical Hacking · Web AppSec · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/Vagebondcur/Malicious-NFT](https://github.com/Vagebondcur/Malicious-NFT)  
📝 **Description:** Web3 stands as a dynamic technology harboring significant potential for diverse business opportunities and applications. As web3's technological landscape continues to evolve, malicious actors are similarly driven to explore novel and innovative methods to exploit these technologies. A notable example of such exploitative endeavors involves the realm of Malicious NFTs.

</details>

<details><summary><strong>peetch - an eBPF based networking tool</strong> — Guillaume Valadon</summary>

**Track:** Network Attacks · Reverse Engineering · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/quarkslab/peetch](https://github.com/quarkslab/peetch)  
📝 **Description:** peetch is a collection of tools aimed at experimenting with different aspects of eBPF to bypass TLS protocol protections.

</details>

<details><summary><strong>Power Automate C2: Stealth Living-Off-the-Cloud C2 Framework</strong> — Tomoaki Tani, Hiroki Hada, Rintaro Fujita</summary>

**Track:** Exploitation and Ethical Hacking · Data Forensics/Incident Response · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/NTT-Security-Japan/pac2](https://github.com/NTT-Security-Japan/pac2)  
📝 **Description:** PowerAutomate C2 is a framework designed to emulate "Living Off the Cloud" attacks, leveraging only legitimate functions in PowerAutomate. The battlefield has shifted from the endpoint to the cloud in evolving cyber warfare. This shift can increase the wealth of useful information the cloud offers, making it a more lucrative target for attackers. This transition introduces a new tactic, "Living Off the Cloud," which has become increasingly prevalent in cyber-attacks. PowerAutomate, a powerful cloud-based automation platform also known as the "New PowerShell", allows for the execution of these "Living Off the Cloud" attacks. PowerAutomate is particularly attractive to attackers as it enables stealth activities. One characteristic is a client-free execution which carries out an attack that leaves no logs on the client and completes entirely in the cloud. It ensures no traces are left on the endpoint, network devices, or within the Office 365 environment. Despite this, continuous access to PowerAutomate on the victim's user profile is required to execute and manage the flow of an attack. PowerAutomate provides a connector known as PowerAutomate Management to address this challenge. This connector allows for managing the flow itself, thus eliminating the need for persistent access to the victim's user profile. In this presentation, we introduce the concept and demonstration of PowerAutomate C2, which utilizes the basic functions of PowerAutomate and exclusively employs the PowerAutomate Management connector. PowerAutomate C2 is built on a Python-based platform, enabling control over PowerAutomate's flow without a GUI-based low-code interface. This approach also facilitates the remote creation and deletion of flows with no logs, even after access to PowerAutomate is lost. For C2 communication, we have implemented support for HTTP(S) and storage services like Dropbox, enhancing the flexibility and stealth of the operation. We also alert the risk of improper permission to use PowerAutomate Management.

</details>

<details><summary><strong>ROP ROCKET: Advanced Framework for Return-Oriented Programming</strong> — Bramwell Brizendine</summary>

**Track:** Exploitation and Ethical Hacking · Reverse Engineering · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/bw3ll/rop_rocket](https://github.com/bw3ll/rop_rocket)  
📝 **Description:** ROP ROCKET is a revolutionary, next-generation tool for return-oriented programming, with unprecedented capabilities. This tool provides multiple, novel techniques, including generating Heaven's Gate ROP gadgets, allowing the user to switch from x86 to x64, as well as a novel technique to invoke Windows syscalls, as a means to bypass Data Execution Prevention (DEP), as opposed to having to use far less stealthy Windows API functions. This tool not only discovers x86 and x64 ROP gadgets, but it provides automatic chain generation for several techniques, including both x86 and x64 Heaven's Gate, the Windows syscalls NtAllocateVirtualMemory and NtProtectVirtualMemory, and "shellcodeless" ROP chains involving System as well as UrlDownloadToFileA and CreateProcessA. This tool uses extensive emulation internationally, both to be able to evaluate individual gadgets, and find other less optimal ROP gadget candidates. This powerful emulation will also execute and evaluate parts of a complete ROP chain, in order to determine how to dynamically generate pointers used as some function parameters. Sometimes a ROP chain could be possible if only some ROP gadget did not have bad bytes contained in its address. With ROCKET, we provide a way to "obfuscate" gadgets, allowing the gadget address to be decoded and executed at runtime. This happens automatically, but can also be done manually. ROP ROCKET is built for performance, as it utilizes multiprocessing, allowing a dozen or more cores to be used. The normally time-extensive process of finding ROP gadgets can be dramatically reduced. Additionally, the tool provides persistence for binaries already examined, so it will "remember" the gadgets already found, if you need to come back to it. That saves the trouble of having to restart the ROP gadget analysis. While ROP can be a complex topic, this tool provides some fresh techniques, guaranteeing that ROP ROCKET of great interest to exploit developers.

</details>

<details><summary><strong>Route53Sweep: Empowering AWS Route53 Security with Automated Scanning & Comprehensive Inventory Management</strong> — Divyanshu Shukla, Anjali Singh Shukla</summary>

**Track:** Network Attacks · Network Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/aws-samples/amazon-route-53-resolver-dns-firewall-automation-examples](https://github.com/aws-samples/amazon-route-53-resolver-dns-firewall-automation-examples)  
📝 **Description:** Route53Sweep uses the AWS Route53 service to improve the management of Route53 security providing a innovative solution to DNS Security. AWS Route53-managed resources like domains, subdomains, DNS records, and related services are all secured and protected by this, which also adopts a comprehensive approach to DNS security management. Organizations can easily track changes to their AWS Route53 resources with Route53Sweep, as well as automate procedures for scanning public IPs and fixing them. Organizations can increase their security and dependability with Route53Sweep, freeing them up to concentrate on other important business operations. Key Topics: Addressing the Urgent Need: We investigate the escalating security issues surrounding AWS Route53 and the necessity of specialized scanning software like Route53Sweep. To protect organizations from potential threats, we emphasize the value of ongoing monitoring and keeping a complete inventory of Route53 assets. Route53Sweep Unleashed: Learn more about our cutting-edge tool's inner workings and how it effectively makes use of a variety of open source tools such as the Nuclei engine, Anew, Httpx, and Notify. The combination of these open-source components with Route53Sweep improves vulnerability scanning capabilities and makes asset discovery and monitoring in real time easier. A Unique Approach: We are proud of our "Desi Jugaad" spirit, which embodies ingenuity and resourcefulness. This idea is embodied by Route53Sweep, which offers an unusual but effective way to automate AWS Route53 security management. Our tool ensures user friendliness while streamlining scanning, automating inventory management, and reducing common security issues. Mitigating Critical Security Issues: Learn how Route53Sweep handles important security issues like NXDomain, Subdomain Takeovers & External Vulnerability Scanning. We demonstrate how our tool enables businesses to proactively address these issues and fortify their security defenses. Real-Time Alerting with Slack: Take a glimpse at the power of Slack integration, which enables real-time alerting for discovered assets and vulnerabilities. Organizations are kept informed and ready to act quickly in case of threats thanks to Route53Sweep. Live Demonstration: It presents a interactive, live demonstration of Route53Sweep in use. Discover how the tool manages AWS Route53 assets, identifies vulnerabilities, and performs all of these tasks in a simple and effective way.

</details>

<details><summary><strong>SCADAsploit: a Command & Control for OT. How to break an ICS system</strong> — Omar Morando</summary>

**Track:** Exploitation and Ethical Hacking · Smart Grid/Industrial Security · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/RapidScada/scada](https://github.com/RapidScada/scada)  
📝 **Description:** SCADAsploit is the only C2 (Command & Control) framework targeting OT systems. Its powerful arsenal of pre- and post-exploitation modules for SCADA/PLC systems makes it a unique tool in Adversary Simulation operations in the OT and IoT environment. Its modular client/server architecture, which can be controlled remotely with a super-secure connection, provides modules dedicated to penetration testing, vulnerability scanning, asset discovery, and pre- and post-exploitation. SCADAsploit boasts a robust client/server architecture that ensures seamless communication and collaboration between your team members. This scalable framework enables the efficient distribution of tasks and enhances your offensive capabilities, allowing you to penetrate even the most complex OT environments. But it is even more than that. Thanks to its flexibility and inherent EDR evasion capability, SCADAsploit is also an effective and powerful tool for traditional IT infrastructures.

</details>

<details><summary><strong>The Metasploit Framework's Payload Improvements</strong> — Spencer McIntyre</summary>

**Track:** Exploitation and Ethical Hacking · Network Attacks · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)  
📝 **Description:** Memory corruption vulnerabilities are becoming less common than their more reliable command execution counterparts. In the last year, two-thirds of the exploits Metasploit released resulted in OS command execution in some way as opposed to direct execution of injected code. Metasploit has made multiple improvements to its command payloads to keep pace with these exploitation trends. These updates make it easier for module authors to deliver a wider variety of second-stage payloads and grant users greater flexibility in selecting their delivery mechanism. This arsenal demonstration will cover the latest improvements to Metasploits payloads, command stagers, and Meterpreter. The audience will see how these payloads can be used, customized and how the exploit development process has improved.

</details>

<details><summary><strong>When World War II meets CDNs: A New Class of Pulsing DDoS Attack</strong> — Jianjun Chen, Run Guo, Yihang Wang, Keran Mu, Baojun Liu, Xiang Li, Chao Zhang, Haixin Duan, Jianping Wu</summary>

**Track:** Network Attacks · Web AppSec · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** Content Delivery Networks (CDNs) are commonly believed to offer their customers protection against denial of service (DoS) attacks. However, our research reveals a novel architecture vulnerability in CDNs, enabling attackers to turn globally distributed CDN Infrastructure into powerful DDoS amplifiers. In this talk, we draw the analogy to a military tactic used in World War II and introduce a new class of pulsing denial-of-service attacks. We demonstrate how CDNs can be exploited to concentrate low-rate attacking requests into short, high-bandwidth pulse waves, resulting in a pulsing DDoS attack to saturate targeted TCP services periodically. We tested five leading CDN vendors and found all of them are susceptible to this attack. By mounting an attack against our own Web site, we show that attackers can use it to achieve peak bandwidths over 1000 times greater than their upload bandwidth, seriously degrading the performance and availability of target services. We have reported our findings to all tested CDNs and received positive feedback. As this problem is rooted in the inherent nature of CDN forwarding networks, it is difficult to eliminate entirely. We discuss possible mitigation strategies for this emerging threat. We believe it is important that CDN operators and their customers be aware of this attack so that they can protect themselves accordingly.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Artificial Intelligence Phishing Email Detector</strong> — Waqar Ahmed</summary>

**Track:** Vulnerability Assessment · Human Factors · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** An artificial intelligence-based phishing email detector that analyses emails and its content, vocabulary, sender, subject etc and detects if it's a phishing email even if it was not flagged as one by an email gateway based on the analysis of collection of phishing emails.

</details>

<details><summary><strong>Attack Knowledge Base for Automotive</strong> — Tien-Chih Lin</summary>

**Track:** Vulnerability Assessment · Internet Of Things · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** Ensuring cybersecurity in the automotive sector is more crucial than ever, especially with the rising intricacies and susceptibilities of vehicle-connected systems. The ISO/SAE 21434 standard serves as a beacon in this endeavor. However, compliance with this standard reveals discernible information disparities across its V-model phases: Concept & Design, Implementation, and Verification & Validation. Addressing these gaps is paramount for cohesive vehicle cybersecurity. To tackle these hurdles, we introduce the "Attack Knowledge Base for Automotive." Inspired and aligned with the ATT&CK framework, this tool aids in seamless compliance with the ISO/SAE 21434 standard. We will demonstrate its efficacy in delivering a thorough and objective outcome during Threat Analysis and Risk Assessment (TARA). Moreover, it bridges information lacunas across the lifecycle, enabling the red team to synergize insights from earlier stages with our Attack Knowledge Base, ensuring holistic automotive cybersecurity.

</details>

<details><summary><strong>BucketLoot - An Automated S3-compatible Bucket Inspector</strong> — Umair Nehri, Owais Shaikh</summary>

**Track:** Vulnerability Assessment · Exploitation and Ethical Hacking · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/redhuntlabs/BucketLoot](https://github.com/redhuntlabs/BucketLoot)  
📝 **Description:** BucketLoot is an automated S3-compatible Bucket inspector that can help users extract assets, flag secret exposures and even search for custom keywords as well as Regular Expressions from publicly-exposed storage buckets by scanning files that store data in plain text.

</details>

<details><summary><strong>CATSploit</strong> — Keisuke Kito, Yusuke Isaka, Kiyoto Kawauchi</summary>

**Track:** Vulnerability Assessment · Exploitation and Ethical Hacking · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/catsploit/catsploit](https://github.com/catsploit/catsploit)  
📝 **Description:** CATSploit is an automated penetration testing tool using Cyber Attack Techniques Scoring (CATS) method that can be used without pentester. Currently, pentesters implicitly made the selection of suitable attack techniques for target systems to be attacked. CATSploit uses system configuration information such as OS, open ports, software version collected by scanner and calculates a score value for capture eVc and detectability eVd of each attack techniques for target system. By selecting the highest score values, it is possible to select the most appropriate attack technique for the target system without hack knack(professional pentester's skill) .

</details>

<details><summary><strong>CloudPathSniffer: Detect and Visualize Abnormal Lateral Movements in Cloud</strong> — Ayberk Halaç</summary>

**Track:** Vulnerability Assessment · Data Forensics/Incident Response · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/ayberkhalac/cloudpathsniffer](https://github.com/ayberkhalac/cloudpathsniffer)  
📝 **Description:** CloudPathSniffer is an open-source, straightforward, and extensible Cloud Anomaly Detection Tool explicitly crafted to assist security teams in uncovering hard-to-see risks and undetected attackers within their control plane of cloud environments. In the dynamic environment of cloud security, the invisibility of temporary credentials has consistently posed a risk, making identifying and tracing potential malicious activity a challenging endeavor. Unlike traditional tools, CloudPathSniffer boasts a unique capability that sets it apart: It can effectively track temporary credentials and attack paths made by them. Beyond monitoring, it reveals vulnerabilities concealed within logs and creates a comprehensive attack schema. Utilizing graphics-based visualization, it offers a simplified interpretation of lateral movements within data. By seamlessly integrating these insights into a graph database alongside your credentials, CloudPathSniffer provides an unmatched defense strategy, ensuring every detail is meticulously addressed.

</details>

<details><summary><strong>DetectiveSQ: A Extension Auditing Framework</strong> — Jeswin Mathai, Shourya Pratap Singh</summary>

**Track:** Vulnerability Assessment · Code Assessment · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** In the modern digital realm, internet browsers, particularly Chrome, have transcended traditional boundaries, becoming hubs of multifunctional extensions that offer everything from AI-integrated chatbots to sophisticated digital wallets. This surge, however, comes with an underbelly of cyber vulnerabilities. Hidden behind the guise of innovation, malicious extensions lurk, often camouflaged as benign utilities. These deceptive extensions not only infringe upon user privacy and security but also exploit users with unasked-for ads, skewed search results, and misleading links. Such underhanded strategies, targeting the unsuspecting user, have alarmingly proliferated. Addressing this conundrum, we present DetectiveSQ - an advanced command-line interface designed to rigorously audit Chrome extensions. At its core, DetectiveSQ is engineered to be compatible with both Manifest V2 (MV2) and Manifest V3 (MV3) architecture, ensuring a wide-ranging applicability across extensions of different generations. Through an intricate examination of permissions - delving deep into how they're invoked and utilized within the extension's codebase - DetectiveSQ brings forth potential security and privacy breaches. The tool not only assesses permissions but also correlates them with actual behaviors, scripts, and external calls, offering a holistic evaluation. DetectiveSQ will be open source and made available after the talk.

</details>

<details><summary><strong>Introducing RAVEN: Discovering and Analyzing CI/CD Vulnerabilities in Scale</strong> — Elad Pticha, Oreen Livni Shein</summary>

**Track:** Vulnerability Assessment · Code Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/CycodeLabs/raven](https://github.com/CycodeLabs/raven)  
📝 **Description:** As the adoption of CI/CD practices continues to grow, securing these pipelines has become increasingly important. However, identifying vulnerabilities in CI/CD pipelines can be daunting, especially at scale. In this talk, we present our tooling, which we intend to release as open-source software to the public that helped us uncover hundreds of vulnerabilities in popular open-source projects' CI/CD pipelines. RAVEN (Risk Analysis and Vulnerability Enumeration for CI/CD) is a powerful security tool designed to perform massive scans for GitHub Actions CI workflows and digest the discovered data into a Neo4j database. With RAVEN, we were able to identify and address potential security vulnerabilities in some of the most popular repositories hosted on GitHub, including FreeCodeCamp (the most popular project on GitHub), Storybook (One of the most popular frontend frameworks), Fluent UI by Microsoft, and much more. This tool provides a reliable and scalable solution for security analysis, enabling users to query the database and gain valuable insights into their codebase's security posture.

</details>

<details><summary><strong>MetaHub: Automating Ownership, Context and Impact Assessments in Security Findings</strong> — Gabriel Alejandro Soltz</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/gabrielsoltz/metahub](https://github.com/gabrielsoltz/metahub)  
📝 **Description:** Security findings from automated sources such as CSPMs, software vulnerability scanners, or compliance scanners often overwhelm security teams with excessive, generic, context-less information. You may have heard countless times that context in security is key, so why don't these tools provide you with more of it? Simply put, they were not designed to do so. This shortcoming means that determining ownership and impact can be time-consuming, leading to critical vulnerabilities going unnoticed, and causing unnecessary noise or friction between security teams and other departments. My proposed demo introduces MetaHub, a tool designed to address these issues by automating the three essential stages of security finding assessment: owner determination, contextualization, and impact definition. Leveraging metadata through MetaChecks, MetaTags, MetaTrails, and MetaAccount, MetaHub provides a detailed, context-aware assessment of each finding. By integrating MetaHub, teams can significantly reduce false positives, streamline the detection and resolution of security findings, and strategically tailor their scanner selection to minimize unnecessary noise. The ability to concentrate on meaningful, high-impact issues will be the primary focus of the demo. MetaHub relies on the ASFF format for ingesting security findings and can consume data from AWS Security Hub or any ASFF-supported scanner like Prowler, ElectricEye, or Inspector. This compatibility means you can continue using the scanners you already rely on but add what's missing to those findings: Ownership, Context, and Impact. MetaHub also generates powerful visual reports and is designed for use as a CLI tool or within automated workflows, such as AWS Security Hub custom actions or AWS Lambda functions. The automation of context, ownership, and impact is not commonly addressed by open-source tools; MetaHub introduces a solution to this problem that aims to be agnostic to the source scanner.

</details>

<details><summary><strong>OpenSecDevOps (OSDO)</strong> — Rafael Otal Simal, Antonio Jose Juanilla Hernandez</summary>

**Track:** Vulnerability Assessment · Code Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/opensecdevops/osdo](https://github.com/opensecdevops/osdo)  
📝 **Description:** Join us to easily build a fortified software development lifecycle (SDLC) using open source tools. Find out how these powerful resources can improve the security of your software applications and improve your development process. We'll explore popular open source tools like Gitlab, Harbor, defectdojo... Seamlessly integrating them into your workflow to enforce strong security policies, detect vulnerabilities, and ensure compliance with industry best practices. Through hands-on exercises and real-world examples, you'll learn how to mitigate security risks, harden your code, and adopt security best practices, resulting in secure, scalable, and resilient software applications. Don't miss this transformative opportunity to unlock the potential of open source tools in your SDLC and strengthen your organization's overall security posture. All the information will be published on opensecdevops.com for the community to use and improve on the day of the presentation, in addition to integrating the different tools, an app will be shown to facilitate said integration according to your needs.

</details>

<details><summary><strong>SupplyShield: Protecting your software supply chain</strong> — Akhil Mahendra, Hritik Vijay</summary>

**Track:** Vulnerability Assessment · Code Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/supplyshield/supplyshield](https://github.com/supplyshield/supplyshield)  
📝 **Description:** SupplyShield is a comprehensive supply chain security framework aimed at defending against the increasingly sophisticated attacks posed by software supply chain vulnerabilities. With numerous organizations hosting hundreds of micro-services and thousands of builds occurring daily, effectively monitoring the software supply chain to construct the final application becomes a complex challenge. This is where SupplyShield can assist any organization in seamlessly integrating this framework into their Software Development Lifecycle (SDLC) to ensure software supply chain security. The current framework version is predominantly designed for the AWS environment. Any organization utilizing AWS infrastructure can seamlessly implement this framework with minimal effort via AWS CloudFormation templates to enhance the security of their supply chain. The framework mainly focuses on generating and maintaining a Software Bill of Materials (SBOM) and performing Software Composition Analysis (SCA) for all the micro-services within an organization. The scans are event-driven, targeting the final micro-service image pushed into AWS ECR. As a result, it generates an SBOM of base image binaries and 3rd-party packages introduced by developers, and performs SCA on top of that. This approach provides a comprehensive view of the software components involved in the overall development of a micro service. Built with scalability in mind, SupplyShield is capable of generating an SBOM and performing SCA in a CI/CD environment where thousands of builds take place daily. SupplyShield enables the rapid detection of zero-day vulnerabilities, such as the log4j exploit, even for organizations with over 100 micro-services, significantly reducing the Mean Time To Detect (MTTD) to mere minutes. This significantly simplifies the tasks of both security engineers and developers in identifying and managing patches for events like the log4j vulnerability. The framework also offers a dashboard for developers and security engineers, presenting relevant metrics and actionable insights.

</details>

<details><summary><strong>Wabhawk/Catch - Unsupervised Machine Learning Detection</strong> — Walid Daboubi</summary>

**Track:** Vulnerability Assessment · Network Defense · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** Webhawk/Catch helps automatically finding web attack traces in HTTP logs without using any preset rules. Based on the usage of Unsupervised Machine Learning, Catch groups log lines into clusters, and detects the outliers that it considers as potentially attack traces. The tool takes as input a raw HTTP log file (Apache, Nginx..) and returns a report with a list of findings. Catch uses PCA (Principal Component Analysis) technique to select the most relevant features (Example: user-agent, IP address, number of transmitted parameters, etc.. ). Then, it runs DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm to get all the possible log line clusters and anomalous points (potential attack traces). Advanced users can fine tune Catch based on a set of options that help optimising the clustering algorithm (Example: minimum number of points by cluster, or the maximum distance between two points within the same cluster). The current version of Webhawk/Catch generates an easy-to-read HTML report which includes all the findings, and the severity of each one.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>AI VPN: A Free-Software AI-Powered Network Forensics Tool</strong> — Veronica Valeros, Sebastian Garcia</summary>

**Track:** Network Defense · Data Forensics/Incident Response · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/stratosphereips/AIVPN](https://github.com/stratosphereips/AIVPN)  
📝 **Description:** The AI VPN is an AI-based traffic analysis tool to detect and block threats, ensuring enhanced privacy protection automatically. It offers modular management of VPN accounts, automated network traffic analysis, and incident reporting. Using the free-software IDS system, Slips, the AI VPN employs machine learning and threat intelligence for comprehensive traffic analysis. Multiple VPN technologies, such as OpenVPN and Wireguard, are supported, and in-line blocking technologies like Pi-hole provide additional protection. The AI VPN was built to help journalists, activists and NGOs against targeted digital attacks. The goal of the tool is to provide an easy-to-use, fast, automated service to perform network forensics on any type of device without physical access to it. The user seamlessly connects to the Internet as with any other VPN while the traffic analysis and reporting happens on the AI VPN server. The AI VPN is designed as a modular collection of micro-services using Docker technology. The AI VPN currently has ten modules taking care of the following functionalities: management, database, communication, VPNs, PiHole, Slips and reporting.

</details>

<details><summary><strong>Ares</strong> — Autumn Skerritt</summary>

**Track:** Cryptography · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/ares-emulator/ares](https://github.com/ares-emulator/ares)  
📝 **Description:** Ares is the next generation of automatic cipher cracking, built by the same people that brought you Ciphey. Give it some encoded text and Ares will tell you what it's encoded with and what the plaintext is. It's 8800% faster than the previous iteration Ciphey.

</details>

<details><summary><strong>BlueHound</strong> — Dekel Paz, Sagie Dulce</summary>

**Track:** Network Defense · Vulnerability Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/zeronetworks/BlueHound](https://github.com/zeronetworks/BlueHound)  
📝 **Description:** BlueHound helps blue teams pinpoint the security issues that actually matter. By combining information about user permissions, network access and unpatched vulnerabilities, BlueHound reveals the paths attackers would take if they were inside your network

</details>

<details><summary><strong>CNAPPgoat: A Multicloud Open-Source Tool for Deploying Vulnerable-by-Design Cloud Resources</strong> — Noam Dahan, Igal Gofman</summary>

**Track:** Network Defense · Vulnerability Assessment · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/tenable/cnappgoat](https://github.com/tenable/cnappgoat)  
📝 **Description:** CNAPPgoat is a CLI tool designed to deploy vulnerable-by-design cloud infrastructure. The tool is designed to modularly provision intentionally vulnerable components in cloud environments with simple commands: launch a container with a crypto-miner installed, spawn a machine with a vulnerable image, create a public IAM role, and many more scenarios. These capabilities empower defenders to test their protective strategies, tools, and procedures, and for offensive professionals to refine their skills and tooling. Instead of trusting their systems and procedures to prevent risk, they can manufacture risk in a controlled environment to verify that they actually do. CNAPPgoat supports modular deployment of various vulnerable scenarios and is a multi-cloud tool. CNAPPgoat is built on Pulumi and supports multiple programming languages. It operates as a CLI tool, requiring no specific IaC expertise, enabling a wide range of professionals to deploy and monitor environments. CNAPPgoat helps: * Security professionals create sandboxes to test their teams, procedures, and protocols * Pentesters use it to provision a "shooting range" to test their skills at exploiting the scenarios and developing relevant capabilities * Security teams benchmark CNAPP solutions against known environments to prove their ability to deliver what they promise * Instructors create vulnerable environments for hands-on workshops or chalk talks * Educators create learning environments where cloud infrastructure risks can be explored, understood - and avoided

</details>

<details><summary><strong>CrowdSec - the network effect of cybersecurity</strong> — Laurence Jones</summary>

**Track:** Data Forensics/Incident Response · Network Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/crowdsecurity/crowdsec](https://github.com/crowdsecurity/crowdsec)  
📝 **Description:** Discover CrowdSec, an open-source and collaborative intrusion prevention and detection system relying on IP behavior analysis and IP reputation. CrowdSec analyzes visitor behavior & provides an adapted response to all kinds of attacks. The solution also enables users to protect each other. Each time an IP is blocked, all community members are informed, so they can also block it. Already used in 160+ countries, the solution builds a crowd-sourced CTI database to secure individuals, companies, institutions etc. The recent release of CrowdSec Security Engine 1.5 brings new features to the table: - Polling API Integration - Real-time decisions management - New Blocklist API and Premium Blocklists - Kubernetes audit acquisition - S3 audit acquisition - Auditd support - CrowdSec CTI API helpers - AWS Cloudtrail Scenarios

</details>

<details><summary><strong>FalconHound, automatic attack path detection and enrichment for blue teams</strong> — Olaf Hartong</summary>

**Track:** Network Defense · Data Forensics/Incident Response · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/FalconForceTeam/FalconHound](https://github.com/FalconForceTeam/FalconHound)  
📝 **Description:** For a long time, BloodHound has been the go-to tool for many red teams to uncover possible lateral movement paths in an environment. Fortunately, there are blue teams that also use it to great value. However, there are a lot of teams that struggle to use it due to lack of time or knowledge. On top of that, keeping the information in the BloodHound database up-to-date and using it for automatic detection and enrichment is often not implemented. Introducing FalconHound, a toolkit that integrates with Microsoft Sentinel, Defender for Endpoint, the Azure Graph API, Neo4j and the BloodHound API to get the most out of your data. Some of its features allow it to track sessions, changes to the environment, alerts, and incidents on your entities and much, much more. All in near-real time! This additional bi-directional context allows you to make better decisions and focus on the most important alerts and incidents. Allowing you, for instance, to run new path calculations frequently based on modifications, sessions or alerts and respond to these attacks which are very hard to detect without this information.

</details>

<details><summary><strong>Honeyscanner: a vulnerability analyzer for Honeypots</strong> — Emmanouil Vasilomanolakis, Aristofanis Chionis Koufakos, Shreyas Srinivasa, Ricardo Yaben</summary>

**Track:** Network Defense · Exploitation and Ethical Hacking · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/honeynet/honeyscanner](https://github.com/honeynet/honeyscanner)  
📝 **Description:** Honeypots are now considered a well-studied cyber-deception mechanism that can assist in defending networks as well as identifying new attack trends. However, recent research has shown that honeypots may also be vulnerable to attacks; especially fingerprinting identification ones. Moreover, many open-source honeypots lack an external security analysis and are often deployed with their default settings. We present honeyscanner, an open-source vulnerability analyzer for honeypots. It is designed to automatically attack a given honeypot, to determine if the honeypot is vulnerable to specific types of cyber-attacks. The analyzer uses a variety of attacks, ranging from identifying vulnerable software libraries to DoS, and fuzzing attacks. In the end, an evaluation report is provided to the honeypot administrator, including advice on how to enhance the security of the honeypot.

</details>

<details><summary><strong>Malicious Executions: Unmasking Container Drifts and Fileless Malware with Falco</strong> — Lorenzo Susini, Stefano Chierici</summary>

**Track:** Malware Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/falcosecurity/falco](https://github.com/falcosecurity/falco)  
📝 **Description:** Containers are the most popular technology for deploying modern applications. SPOILER ALERT: bypassing well-known security controls is also popular. In this talk, we explain how to use the recent updates in Falco, a CNCF open-source container security tool, to detect drifts and fileless malware in containerized environments. As a best practice, containers should be considered immutable. Early this year, Falco introduced new features to detect container drift via OverlayFS, which can spot if binaries are added or modified after the container's deployment. New binaries are often a sign of an ongoing attack. Of course, attackers can also use more advanced evasion techniques to stay hidden. By using in-memory, fileless execution, attackers can bypass most of the security controls such as drift detection and still reach their goals with no stress. To combat fileless attacks, Falco has also added memfd-based fileless execution thanks to its visibility superpowers on Linux kernel system calls. Combining Falco's existing runtime security capabilities with these two new detection layers forms the foundation of a defense in depth strategy for cloud-native workloads. We will walk you through real-world scenarios based on recent threats and malware, demoing how Falco can help detect and respond to these malicious behaviors and comparing both drift and fileless attack paths.

</details>

<details><summary><strong>Mitre Attack Flow Detector</strong> — Ezzeldin Tahoun</summary>

**Track:** Data Forensics/Incident Response · AI, ML & Data Science · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/ezztahoun/attack_flow_detector](https://github.com/ezztahoun/attack_flow_detector)  
📝 **Description:** Using correlation and clustering models, turn tons of alerts into mitre attack flows. The model finds the attack flows, using its ability to evaluate alerts temporal proximity, kill chain sequentiality, shared entities and similar attributes to other alerts of interest, among others. In real time this model can save your operations endless hours of correlating incidents and finding noteworthy attack flows, that if not detected in time would lead to breaches.

</details>

<details><summary><strong>Packing-Box: Breaking Detectors & Visualizing Packing</strong> — Alexandre D'Hondt, Charles-Henry Bertrand Van Ouytsel, Axel Legay, Romain Jennes, Sébastien Martinez Balbuena</summary>

**Track:** Malware Defense · Reverse Engineering · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/packing-box/docker-packing-box](https://github.com/packing-box/docker-packing-box)  
📝 **Description:** This Docker image is an experimental toolkit gathering analyzers, detectors, packers, tools and machine learning mechanics for making datasets of packed executables and training machine learning models for the static detection of packing. It aims to support PE, ELF and Mach-O executables and to study the best static features that can be used in learning-based static detectors. Furthermore, it currently additional functionalities to focus on supervised and unsupervised learning but also on adversarial learning for breaking static detectors and detection models. https://raw.githubusercontent.com/packing-box/docker-packing-box/main/docs/material/bheu23-packingbox.pdf

</details>

<details><summary><strong>Slips: A machine-learning based, free-software, P2P Network Intrusion Prevention System</strong> — Sebastian Garcia, Alya Gomaa</summary>

**Track:** Network Defense · Malware Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/stratosphereips/StratosphereLinuxIPS](https://github.com/stratosphereips/StratosphereLinuxIPS)  
📝 **Description:** For the last 7 years we developed Slips, a behavioral-based intrusion prevention system, and the first free-software network IDS using machine learning. Slips profiles the behavior of IP addresses and performs detections inside each time window in order to also *unblock* IPs. Slips has more than 20 modules that detect a range of attacks both to and from the protected device. It is an network EDR with the capability to also protect small networks. Slips consumes multiple packets and flows, exporting data to SIEMs. More importantly, Slips is the first IDS to automatically create a local P2P network of sensors, where instances share detections following a trust model resilient to adversaries.. Slips works in several directionality modes. The user can choose to detect attacks coming *to* or going *from* these profiles, or both. This makes it easy to protect your network but also to focus on infected computers inside your network, which is a novel technique. Among its modules, Slips includes the download/manage of external Threat Intelligence feed (including our laboratory's own TI feed), whois/asn/geocountry enrichment, a LSTM neural net for malicious behavior detection, port scanning detection (vertical and horizontal) on flows, long connection detection, etc. The decisions to block profiles or not are based on ensembling algorithms. The P2P module connects to other Slips to share detection alerts. Slips can read packets from the network, pcap, Suricata, Zeek, Argus and Nfdump, and can output alerts files and summaries. Having Zeek as a base tool, Slips can correctly build a sorted timeline of flows combining all Zeek logs. Slips can send alerts using the STIX/TAXII protocol. Slips web interface allows to clearly see the detections and behaviors, including threat inteligence enhancements. The interface can show multiple Slips runs, summarize whois/asn/geocountry information and much more.

</details>

<details><summary><strong>SSH into any device from anywhere with ZERO Open Network ports</strong> — Colin Constable, Anthony Prakash</summary>

**Track:** Network Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/atsign-foundation/noports](https://github.com/atsign-foundation/noports)  
📝 **Description:** SSH to Any Device with No Ports Open Make your devices reachable while eliminating network attack surfaces & reducing administrative overhead. Atsign's patent pending core technology is engineered to deliver the following benefits: Addressability Atsign's core technology uses identifiers which replace the need to manage IP addresses. If you remember the atSign (Atsign's version of an address), you can look up the IP address and port in the atDirectory which manages this information for you. Reachability ‍Atsign's core technology provides each device with its own microserver which makes it reachable from anywhere on the internet. No open ports (no network attack surface) on the device Connections are always made from the device to the microserver, meaning that no ports ever need to be opened on devices using this technology. End-to-end encrypted Information is automatically encrypted on the edge devices before it is sent over Atsign's control plane. Zero Trust Atsign's technology is designed such that cryptographic keys are only stored at the edge device. No third party or intermediary ever possesses the decryption keys which are required to access the information. You don't need to trust any of the microservers, because they never see information in the clear. In other words, sending information using Atsign's control plane requires no open ports and is fully edge-to-edge encrypted, all without needing to know the IP address of the device!

</details>

<details><summary><strong>TSURUGI LINUX - the sharpest weapon in your DFIR arsenal</strong> — Giovanni Rattaro, Marco Giorgi</summary>

**Track:** Data Forensics/Incident Response · OSINT - Open Source Intelligence · **Event:** Europe 2023  
🔗 **Link:** Not Available  
📝 **Description:** Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools. As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident). And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes. A special Tsurugi Linux BLACKHAT EDITION will be shared only with the participants.

</details>

<details><summary><strong>YAWNING-TITAN</strong> — Chris McCarthy, Czar Echavez</summary>

**Track:** Network Defense · Malware Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/dstl/YAWNING-TITAN](https://github.com/dstl/YAWNING-TITAN)  
📝 **Description:** YAWNING-TITAN is an abstract, graph based cyber-security simulation environment that supports the training of intelligent agents for autonomous cyber operations. YAWNING-TITAN focuses on providing a fast simulation to support the development of defensive autonomous agents who face off against probabilistic red agents. YAWNING-TITAN has been designed with the following things in mind: • Simplicity over complexity; • Minimal Hardware Requirements; • Operating System agnostic; • Support for a wide range of algorithms; • Enhanced agent / policy evaluation support; • Flexible environment and game rule configuration; • Generation of evaluation episode visualisations (gifs). YAWNING-TITAN contains a small number of specific, self-contained OpenAI Gym environments for autonomous cyber defence research, which are great for learning and debugging; it also provides a flexible, highly configurable generic environment which can be used to represent a range of scenarios of increasing complexity and scale. The generic environment only needs a network topology and a settings file to create an OpenAI Gym compliant environment which enables open research and enhanced reproducibility. When training and evaluating an agent, YAWNING-TITAN can be run from either a command-line interface, or a graphical user interface (GUI). The GUI allows the underlying Python to be executed without need for a command line interface or knowledge of the python language. The GUI also integrates with a customised version Cytoscape JS which has been extended to work directly with YAWNING-TITAN, and allows users to directly interface with network topologies that subsequently updates a database of stored networks. Both the command-line interface and the GUI provide read-outs throughout agent training and evaluation, as well as generation of a final summary.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>GDBFuzz: Embedded Fuzzing with Hardware Breakpoints</strong> — Max Eisele</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/boschresearch/gdbfuzz](https://github.com/boschresearch/gdbfuzz)  
📝 **Description:** In this tool demo, we will present GDBFuzz, a new open source fuzzer that leverages hardware breakpoints and program analysis to test embedded systems. Existing fuzzers for embedded devices most often run on an emulation of the code, but GDBFuzz runs on the device itself. This allows GDBFuzz to fuzz devices which do not have emulations. Its integration with Ghidra allows it to fuzz closed-source applications. All the tool needs is access to the commonly used GDB remote protocol. We will explain how GDBFuzz combines hardware breakpoints with control flow relationships to guide fuzzing exploration. We will also detail its underlying analyses and techniques that were recently published at the academic conference ISSTA. GDBFuzz detected three previously unknown bugs in open-source embedded software that were confirmed by the vendors. GDBFuzz is the first tool allowing to fuzz embedded systems at scale. To demonstrate the fuzzer's ease of use and efficiency, we will run an interactive demo on multiple devices (including ARM and MSP430 processors). At the end of the session, attendees will know how to use GDBFuzz to test their own embedded systems.

</details>

<details><summary><strong>ICS Forensics Tools</strong> — Ori Perez, Maayan Shaul</summary>

**Track:** Smart Grid/Industrial Security · Data Forensics/Incident Response · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/microsoft/ics-forensics-tools](https://github.com/microsoft/ics-forensics-tools)  
📝 **Description:** Open Source ICS Forensics Toolkit This cutting-edge toolkit is designed for in-depth analysis of Industrial PLC metadata and project files, providing an essential resource for cybersecurity experts in the industrial control systems (ICS) sector. Our ICS Forensics Tools stand out by enabling thorough investigation of ICS environments, aiding in the detection of anomalies and compromised devices during critical incident responses or routine checks. This exciting arsenal presentation will not only introduce the new protocols but also feature live demonstrations that showcase its capabilities in real-time scenarios. Attendees will receive a concise, user-friendly forensics guide to leverage the full potential of the tool effectively. And there's more – attendees will have exclusive, immediate access to this groundbreaking tool right as the session begins. Don't miss out on this opportunity to enhance your ICS forensics capabilities with our latest open-source solution! https://github.com/microsoft/ics-forensics-tools

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>SafeNet - Securing Your Network From Your Research</strong> — David El</summary>

**Track:** Reverse Engineering · Network Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/cyberark/SafeNet](https://github.com/cyberark/SafeNet)  
📝 **Description:** In the world of Cyber Security and especially malware research and reverse engineering, we often put ourselves and our PCs at constant risk, and a common method to mitigate this is by using a Virtual Machine and while this method is great for keeping our PCs safe, it does not address a larger issue - our network. This is true especially now, with the rise in popularity of remote and hybrid work where we have to research on networks that lack corporate-level protection solutions like our homes! SafeNet is a solution to keep our research labs and dirty virtual machines connected to the internet, all while segregating them from our local network and keeping it safe, ensuring that we can continue researching while staying as safe as possible.

</details>

<details><summary><strong>Tracing Golang Windows API calls with gftrace</strong> — Leandro Fróes</summary>

**Track:** Reverse Engineering · Malware Defense · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/leandrofroes/gftrace](https://github.com/leandrofroes/gftrace)  
📝 **Description:** gftrace is a Windows API tracing tool that abuses the way that the Golang runtime works to monitor all the API calls performed by Go applications. The project is a command line tool that only requires the user to specify what Windows functions to trace. Since the tool was designed to work with Go applications specifically it provides a very clean output based on the calls the main package performs and filters all the noise the Go runtime produces. The tool is also very portable and reliable since it works with several (if not all) Go versions and only interacts with the Go runtime, without touching any Windows API call. gftrace can be very handy for fast malware triage and reverse engineering in general, specially when it comes to obfuscated, stripped and/or trojanized samples.

</details>

<details><summary><strong>Unblob: A Firmware Extraction Framework</strong> — Quentin Kaiser, Florian Lukavsky</summary>

**Track:** Reverse Engineering · Internet Of Things · **Event:** Europe 2023  
🔗 **Link:** [https://github.com/onekey-sec/unblob](https://github.com/onekey-sec/unblob)  
📝 **Description:** One of the major challenges of embedded security analysis is the sound and safe extraction of arbitrary firmware. Specialized tools that can extract information from those firmwares already exists, but we wanted something smarter that could identify both start offset of a specific chunk (e.g. filesystem, compression stream, archive) and end offset. We stick to the format standard as much as possible when deriving these offsets, and we clearly define what we want out of identified chunks (e.g., not extracting meta-data to disk, padding removal). This strategy helps us feed known valid data to extractors and precisely identify unidentified chunks, turning unknown unknowns into known unknowns. Given the modular design of unblob and the ever expanding repository of supported formats, unblob could be used in areas outside of embedded security such as data recovery, memory forensics, or malware analysis. unblob has been developed with the following objectives in mind: * Accuracy - chunk start offsets are identified using battle tested rules, while end offsets are computed according to the format's standard without deviating from it. We minimize false positives as much as possible by validating header structures and discarding overflowing chunks. * Security - unblob does not require elevated privileges to run. It's heavily tested and has been fuzz tested against a large corpus of files and firmware images. We rely on up-to-date third party dependencies that are locked to limit potential supply chain issues. We use safe extractors that we audited and fixed where required (e.g., path traversal in ubi_reader, path traversal in jefferson, integer overflow in Yara). * Extensibility - unblob exposes an API that can be used to write custom format handlers and extractors in no time. * Speed - we want unblob to be blazing fast, that's why we use multi-processing by default, make sure to write efficient code, use memory-mapped files, and use Hyperscan as high-performance matching library. Computation intensive functions are written in Rust and called from Python using specific bindings.

</details>

---
