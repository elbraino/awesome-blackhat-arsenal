# Europe 2024
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2024** event held in **Europe**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Contents
- [Others](#others)
- [⚙️ Miscellaneous / Lab Tools](#⚙️-miscellaneous-lab-tools)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🔵 Blue Team & Detection
<details><summary><strong>Active Directory Cyber Deception using Huginn</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rohan Durve](https://img.shields.io/badge/Rohan%20Durve-informational) ![Paul Laine](https://img.shields.io/badge/Paul%20Laine-informational)

🔗 **Link:** Not Available  
📝 **Description:** Huginn helps realise strategic adversary deception concepts from the MITRE Engage framework and the European Central Bank's cyber resilience report using novel techniques and an open-source program.

We demonstrate creation and monitoring of the following decoy assets during this presentation:
- Certificate Templates (ESC4 & ESC1)
- Computer Object Take-over via RBCD
- Decoy Users
- Decoy Object ACLs
- Retrieve GMSA Passwords

Our objectives are to:
- Reduce the security posture requirements for engaging in cyber deception.
- Balance the intrinsic asymmetry of cyber-attacks by raising high-fidelity alerts around advanced attacker activity.
- Impose cost by embedding high-value deception artefacts within critical attack paths.

</details>

<details><summary><strong>Clear NDR - Community</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Peter Manev](https://img.shields.io/badge/Peter%20Manev-informational)

🔗 **Link:** [Clear NDR - Community](https://github.com/ChanChiChoi/tiny-crawler/blob/master/paperMeta4arxiv/arxiv-0801.txt)  
📝 **Description:** For the last decade, SELKS has been the go-to open source platform for network security professionals, combining Suricata's power with an all-in-one toolkit. Now, we're unveiling its revolutionary successor: Clear NDR™ - Community from Stamus Networks.

This isn't just an upgrade; it's a complete reimagining of what open source network security can be. We've rebuilt the platform from the ground up, focusing on:

Streamlined User Experience: An intuitive interface that makes complex threat hunting and incident response accessible to both seasoned analysts and newcomers alike.
Commercial-Grade Performance: Leveraging the architecture of our Stamus Security Platform, Clear NDR - Community delivers the speed and scalability required for modern, high-traffic networks.
Feature Parity: Inherit many of the advanced features previously exclusive to our commercial platform, including
100% Open Source Commitment: Clear NDR - Community remains completely free to use, modify, and distribute. We believe in the power of community collaboration to drive innovation in network security.
In this talk, Stamus Networks Co-Founder Peter Manev will dive into the technical details of Clear NDR - Community, showcasing its capabilities through real-world scenarios. We'll also discuss our vision for the future of open source network security and how you can get involved in shaping this exciting new platform.

Whether you're a long-time SELKS user, a security enthusiast, or simply curious about the future of network defense, this session will provide a comprehensive introduction to Clear NDR - Community and its potential to transform the way you protect your networks.

Key Takeaways:

Discover the key advancements in Clear NDR - Community compared to SELKS
Learn how to leverage its powerful features for enhanced threat detection and response
Understand the benefits of open source in the network security landscape
Gain insights into how you can contribute to and benefit from the Clear NDR - Community edition

</details>

<details><summary><strong>Cloud Console Cartographer: Tapping Into Mapping &gt; Slogging Thru Logging</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Andi Ahmeti](https://img.shields.io/badge/Andi%20Ahmeti-informational) ![Daniel Bohannon](https://img.shields.io/badge/Daniel%20Bohannon-informational)

🔗 **Link:** Not Available  
📝 **Description:** Event logs are a fundamental resource for security professionals seeking to understand the activity occurring in an environment. Cloud logs serve a similar purpose as their on-premise counterparts, though differing significantly in format and granularity between cloud providers. While most cloud CLI tools provide a one-to-one correlation between an API being invoked and a single corresponding API event being generated in cloud log telemetry, browser-based interactive console sessions differ profoundly across cloud providers in ways that obfuscate the original actions taken by the user.

For example, an interactive AWS console session produces 300+ CloudTrail events when a user clicks IAM->Users. These events are generated to support the numerous tiles and tables in the AWS console related to the user's clicked action but are never explicitly specified by the user (e.g. details concerning potential user groups, MFA devices, login profiles or access keys and their usage history for each IAM user in the paginated results). This backend behavior presents significant challenges for security analysts and tooling seeking to differentiate API calls explicitly invoked by a user from secondary API invocations merely supporting the AWS console UI.

Since March 2023 the presenters have developed a solution to this challenge and are proud to demo and release the open-source Cloud Console Cartographer framework (including a full CLI and supplemental GUI visualizer) as part of this presentation.

The presenters will demonstrate the extent of the console logging problem and the technical challenges and capabilities required to solve it, showcasing the tool's usefulness in translating real-world examples of malicious console sessions produced by notable cloud threat actors during first-hand incident response investigations.

Come and learn how the open-source Cloud Console Cartographer framework can provide clarity for threat hunters and detection engineers alike, helping defenders stop slogging through logging while putting the "soul" back in "console."

</details>

<details><summary><strong>defender2yara: Translating Microsoft Defender Antivirus Signatures into YARA Rules</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tomoaki Tani](https://img.shields.io/badge/Tomoaki%20Tani-informational)

🔗 **Link:** [defender2yara: Translating Microsoft Defender Antivirus Signatures into YARA Rules](https://github.com/t-tani)  
📝 **Description:** Defender2yara is a Python-based utility that converts Microsoft Defender Antivirus Signatures (VDM) into YARA rules. This tool addresses the limitations of black-box signatures, which often lack the context information of the detection essential for researchers. The YARA rules generated by this tool provide information on how Microsoft Defender detects threats, which statical features are focused on for the detection and the context of the threat classification. Defender2yara enables security professionals to create YARA rules from the latest or manually provided Microsoft Defender's signature database by bridging the gap between Microsoft's proprietary signature formats and the widely adopted human-readable YARA rule.

Key features of defender2yara include the ability to translate strings and hex byte patterns, integrate threat-scoring logic into YARA conditions, and download the latest signature databases. The tool supports exporting YARA rules into a single file or files organized by malware family, optimizing scanning efficiency with some techniques such as file header checks. Users can also specify paths for database files, ensuring flexibility in various environments.

The presentation will discuss the motivation behind defender2yara, focusing on the challenges of black-box signatures and the need for customizable detection mechanisms. It will provide an overview of Microsoft Defender's signature database structure, detailing VDM file components like strings, hex byte patterns, and threat-scoring logic.

Additionally, the architecture of defender2yara will be explored, with a high-level overview and detailed breakdown of the modules, including signature parsing and YARA rule generation. Example usage scenarios will be showcased for Blue Teams, emphasizing threat-hunting by customizing detection rules. This involves using defender2yara to create tailored YARA rules from the latest signatures, enhancing their ability to detect specific threats.

For Red Teams, the presentation will cover analyzing YARA rules to identify detection gaps and crafting evasive techniques for penetration testing and red teaming exercises.

</details>

<details><summary><strong>DICOMHawk: a honeypot for medical devices</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Emmanouil Vasilomanolakis](https://img.shields.io/badge/Emmanouil%20Vasilomanolakis-informational) ![Georgios Theodoridis](https://img.shields.io/badge/Georgios%20Theodoridis-informational)

🔗 **Link:** https://github.com/open-dicom/awesome-dicom  
📝 **Description:** DICOM is a standard that is broadly used for the storage and transmission of medical devices. DICOM has been targeted by attackers with millions of patient record data being at risk. For instance, researchers in BlackHat Europe 2023 revealed security issues with DICOM that lead to more than 3,800 DICOM servers accessible via the internet with many leaking health and personal information.

In this arsenal presentation, we demonstrate DICOMHawk, an open-source python-based honeypot that is tailored for the DICOM protocol. With DICOMHawk we offer security practitioners and research a tool to be able to understand the attack landscape, lure attackers in, as well as understand Internet-level scanners such as Shodan. Among other properties, DICOMHawk offers various operations for a realistic DICOM server environment, the ability to comprehensively log DICOM associations, messages and events to understand incoming attacks, and a user-friendly web interface. Lastly, the honeypot is easily extendable via custom handlers.

</details>

<details><summary><strong>Falco to the Rescue: Sniffing Out Sneaky Supply Chain Attacks in Your CI/CD Pipeline!</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Stefano Chierici](https://img.shields.io/badge/Stefano%20Chierici-informational) ![Lorenzo Susini](https://img.shields.io/badge/Lorenzo%20Susini-informational)

🔗 **Link:** Not Available  
📝 **Description:** The increasing sophistication and frequency of supply chain attacks necessitate reevaluating current security practices. This talk explains how to use Falco, a CNCF open-source runtime security tool, to detect threats and malicious behaviors inside your CI/CD pipelines.
Continuous Integration and Continuous Deployment (CI/CD) pipelines are essential for modern software development, enabling rapid code integration, testing, and deployment. Deep visibility inside the CI/CD pipelines is critical to ensuring that the code released into production environments is secure and trustworthy. SolarWinds, CodeCov, and the recent xz-utils supply chain attacks could all have been detected by shifting further left well-known runtime security practices, starting by observing the behavior of the build and deploy servers.
With its exceptional visibility into Linux kernel system calls, Falco can be seamlessly integrated into CI/CD workflows to monitor the CI/CD server's runtime behavior. By providing valuable information on runtime events, such as malicious connections and file accesses, Falco becomes a reliable ally in detecting anomalous behavior in continuous integration pipelines.

We will walk you through real-world scenarios based on recent CI/CD threats, demoing how Falco can be used in GitHub Actions pipelines to detect malicious behaviors.

</details>

<details><summary><strong>findmytakeover - find dangling domains in a multi cloud environment</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Aniruddha Biyani](https://img.shields.io/badge/Aniruddha%20Biyani-informational)

🔗 **Link:** [findmytakeover - find dangling domains in a multi cloud environment](https://github.com/anirudhbiyani)  
📝 **Description:** findmytakeover detects dangling DNS record in a multi cloud environment. It does this by scanning all the DNS zones and the infrastructure present within the configured cloud service provider either in a single account or multiple accounts and finding the DNS record for which the infrastructure behind it does not exist anymore rather than using wordlist or bruteforcing DNS servers.

</details>

<details><summary><strong>msInvader: Simulating Adversary Techniques in M365 and Azure</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

🔗 **Link:** [msInvader: Simulating Adversary Techniques in M365 and Azure](https://github.com/mvelazc0/msInvader)  
📝 **Description:** msInvader is an adversary simulation tool built for blue teams, designed to simulate adversary techniques within M365 and Azure environments. This tool generates attack telemetry, aiding teams in building, testing, and enhancing detection analytics. By implementing multiple authentication mechanisms, including OAuth flows for compromised user scenarios and service principals, msInvader mirrors realistic attack conditions. It interacts with Exchange Online using the Graph API, EWS, and REST API, providing comprehensive simulation capabilities. This session will explore msInvader's technical features, demonstrating its application in improving security defenses through detailed adversary simulations.

</details>

<details><summary><strong>Packing-Box: Improving Detection of Executable Packing</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Alexandre D'Hondt](https://img.shields.io/badge/Alexandre%20D'Hondt-informational) ![Charles-Henry Bertrand Van Ouytsel](https://img.shields.io/badge/Charles-Henry%20Bertrand%20Van%20Ouytsel-informational) ![Axel Legay](https://img.shields.io/badge/Axel%20Legay-informational) ![Alex Van Mechelen](https://img.shields.io/badge/Alex%20Van%20Mechelen-informational)

🔗 **Link:** Not Available  
📝 **Description:** This Docker image is an experimental toolkit gathering analyzers, detectors, packers, tools and machine learning machinery for making datasets of packed executables and training machine learning models for the static detection of executable packing applied to multiple formats (including PE, ELF and Mach-O) and for studying the best features that can be used in learning-based static detectors. Furthermore, it currently holds various functionalities to focus on supervised, unsupervised or even adversarial learning and is constantly being improved for extending its capabilities.

</details>

<details><summary><strong>Streamlining Suricata Signature Writing: Mastering the Art with Suricata Language Server</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Eric LEBLOND](https://img.shields.io/badge/Eric%20LEBLOND-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Syntax analysis for malware detection with Linguado</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Guzmán Cernadas](https://img.shields.io/badge/Guzmán%20Cernadas-informational) ![Marcos Carro](https://img.shields.io/badge/Marcos%20Carro-informational)

🔗 **Link:** [Syntax analysis for malware detection with Linguado](https://github.com/Caralludo/linguado)  
📝 **Description:** Linguado is a tool that measures how similar are two or more abstract syntax trees generated from various source codes. To achieve this, the program follows these steps:
1. With the library ANTLR4, the program generates the abstract syntax tree of each source code.
2. With the abstract syntax trees, it generates a graph which we can work with.
3. Once we have the graphs, it calculates the Weisfeiler-Lehman matrix.
4. From the Weisfeiler-Lehman matrix the program calculates the mean and the standard deviation. The mean and the standard deviation are the measures that we use to know how similar the abstract syntax trees are.

</details>

<details><summary><strong>Traceeshark - Interactive System Tracing & Runtime Security using eBPF</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ofek Shaked](https://img.shields.io/badge/Ofek%20Shaked-informational) ![Asaf Eitani](https://img.shields.io/badge/Asaf%20Eitani-informational)

🔗 **Link:** Not Available  
📝 **Description:** Traceeshark brings the world of Linux runtime security monitoring and advanced system tracing to the familiar and ubiquitous network analysis tool Wireshark.

It is now possible, using Wireshark, to record an immense variety of system events using Aqua Security's eBPF based runtime security tool Tracee, and analyze them interactively.

Tracee is a runtime security and forensics tool for Linux, utilizing eBPF technology to trace systems and applications at runtime, analyze collected events to detect suspicious behavioral patterns, and capture forensics artifacts. Up until now, a typical workflow using Tracee involved running Tracee from the CLI, perform some activity, stop Tracee, dump its logs to a file, and analyze the file using command line tools or scripting languages. Analyzing packets captured by Tracee was done separately, and in general the entire process was very manual.

Now, events generated by Tracee can be analyzed interactively using Wireshark's advanced capabilities, which include interactive filtering, displaying statistics and performing advanced data aggregations. Traceeshark also provides the ability to capture events using Tracee directly from Wireshark and have them stream in like a network capture. Another game-changing feature is the ability to analyze system events side by side with network packets generated by Tracee that contain rich context about the system process and container they belong to.

The combination of Tracee's wide use in the security industry and its advanced system tracing and forensic capabilities, together with Wireshark's universal popularity in the entire IT industry, its maturity and ease of use, opens up a whole new world of capabilities for dynamic malware analysis, forensics, kernel hacking and more.

</details>

<details><summary><strong>VelLMes, a high-interaction AI based deception framework.</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sebastian Garcia](https://img.shields.io/badge/Sebastian%20Garcia-informational) ![Muris Sladic](https://img.shields.io/badge/Muris%20Sladic-informational)

🔗 **Link:** Not Available  
📝 **Description:** VelLMes is the first free-software AI-based deception framework that can create digital-twins of Linux shells (SSH), SMTP, POP, HTTP and MYSQL protocols.

It is based on new deception research that uses fine-tuned and trained LLMs to create high-interaction honeypots that look exactly like your production servers. When attackers connect to a VelLMes SSH, they can not distinguish it from a real Linux shell. The LLM creates in real time, and depending on the commands of the attacker, the complete structure of the simulated computer, including file contents, output of all commands, connection to the Internet (simulated), users, and more.

VelLMes key features are:
The content from a previous session can be carried over to a new session to ensure consistency.
It uses a combination of techniques for prompt engineering, including chain-of-thought.
Uses prompts with precise instructions to address common LLM problems.
More creative file and directory names for Linux shells
In the Linux shell the users can "move" through folders
Response is correct also for non-commands for all services
It can simulate databases and their relations in the MySQL honeypot.
It can create emails with all the necessary header info in the POP3 honeypots.
It can respond to HTTP GET requests

VelLMes was evaluated and tested in its generative capabilities and deception capabilities with human penetration tester professionals to see if they can recognize the honeypot. Most attackers do not realize this is deception, and it performs much better than other deception technologies we have compared against.

VelLMes can bring a new perspective to your deception technology in your company.

</details>

<details><summary><strong>WeakpassJS - a collection of tools for generation, bruteforce and hashcracking</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ivan Iushkevich](https://img.shields.io/badge/Ivan%20Iushkevich-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>ACVTool 2024 MultiDex</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Aleksandr Pilgun](https://img.shields.io/badge/Aleksandr%20Pilgun-informational)

🔗 **Link:** [ACVTool 2024 MultiDex](https://github.com/pilgun/acvtool)  
📝 **Description:** ACVTool is a sophisticated bytecode instrumentation tool designed for highlighting instruction coverage in Android apps. In 2024, ACVTool received a major update unlocking smali coverage analysis for modern Android apps. Now, ACVTool supports complex Multidex and Multi-APK applications that you can pull right from your Android device. With ACVTool we highlight exact bytecode instruction (in smali representation) executed when running a particular feature, e.g. to see the actually running code behind a tap of a button. To further depict selected app behavior, ACVTool may partially shrink not executed code. ACVTool works on 3rd-party Android apps without source code, and it does not require a rooted device.

</details>

<details><summary><strong>Analyzing Modern Windows Shellcode with SHAREM</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational)

🔗 **Link:** [Analyzing Modern Windows Shellcode with SHAREM](https://github.com/Bw3ll/JOP_ROCKET)  
📝 **Description:** Shellcode is omnipresent, a constant part of the exploitation and malware ecosystem. Injected into process memory, there are limitless possibilities. Yet until recently, analysis techniques were severely lacking. We present SHAREM, an NSA-funded shellcode analysis framework with stunning capabilities that will revolutionize how we approach the analysis of shellcode.

SHAREM can emulate shellcode, identifying more than 25,000 WinAPI functions as well as 99% of Windows syscalls. This emulation data can also be ingested by its own custom disassembler, allowing for functions and parameters to be identified in the disassembly for the first time ever. The quality of disassembly produced by SHAREM is virtually flawless, markedly superior to what is produced by leading disassemblers. In comparison, IDA Pro or Ghidra might produce a vague "call edx," as opposed to identifying what specific function and parameters is being called, a highly non-trivial task when dealing with shellcode.

One obstacle with analyzing shellcode can be obfuscation, as an encoded shellcode may be a series of indecipherable bytes—a complete mystery. SHAREM can easily overcome this, presenting the fully decoded form in the disassembler, unlocking all its secrets. Without executing the shellocode, emulation can be used to help fully deobfuscate the shellcode. In short, a binary shellcode – or even the ASCII text representing a shellcode – could be taken and quickly analyzed, to discover its true, hidden functionality.

One game-changing innovation is complete code coverage. With SHAREM, we ensure that all code is executed, capturing function calls and arguments that might otherwise be impossible to get. This is done by taking a series of snapshots of memory and CPU register context; these are restored if a shellcode ends with unreached code. In practical terms, this means if a shellcode ordinarily would prematurely terminate, we might miss out several malicious functions. Complete code coverage allows us to rewind and restart at specific points we should not be able to reach, discovering all functionality.
SHAREM will now integrate AI to help resolve what exactly is going on. The enumerated APIs and parameters can be analyzed to identify malicious techniques, which could be found in MITRE ATT&CK framework and elsewhere. This helps reduce the human analysis effort required. Additionally,

SHAREM can use AI to rename functions based on functionality. AI is also used to provide detailed text descriptions of how each WinAPI or syscall is used within the shellcode, especially as it pertains to MITRE. There is much more to be seen with the new AI-enhanced capabilities.

The ease and simplicity of SHAREM is breathtaking, especially comparison to how much time and effort similar analysis would require otherwise. SHAREM represents a major shift in our capability to analyze shellcode in a highly efficient manner, documenting every possible clue – whether it be functions, parameters, secrets, or artifacts.

For reverse engineers of all kinds, SHAREM is a must-see presentation.

</details>

<details><summary><strong>ByteCodeLLM - Framework for Converting Executable to Source using Open-source Tools and a Fine-tuned LLM Model</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Amir Landau](https://img.shields.io/badge/Amir%20Landau-informational) ![David El](https://img.shields.io/badge/David%20El-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Mothra: A Ghidra EVM Extension</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Yuejie Shi](https://img.shields.io/badge/Yuejie%20Shi-informational) ![Chia Cheng Tsai](https://img.shields.io/badge/Chia%20Cheng%20Tsai-informational)

🔗 **Link:** Not Available  
📝 **Description:** Recent years have witnessed the rise of cyber-attacks targeting Ethereum and EVM-based blockchains. Many of these attacks have involved the deployment of malicious EVM-compatible smart contracts to facilitate the hacks. One notable example is the use of "callee" smart contracts in flash loan attacks, which have resulted in substantial financial losses since early 2020. These malicious smart contracts are typically scripted in high-level languages (e.g., Solidity and Vyper), compiled into EVM bytecode, and deployed by bad actors without source code verification, making forensic analysis challenging.

To better understand the malicious smart contracts, EVM decompilers (e.g., EtherVM [1], Dedaub [2]) are commonly used by security researchers to convert EVM bytecode into high-level languages. However, the lack of interactive functionalities on existing decompilers makes comprehensive analysis difficult. Specifically, these tools do not allow for illustrating control flow graphs, adding comments, patching contract bytecode, and other interactive features. Notably, IDA Pro [3] and Ghidra [4], renowned for their robust interactive user interfaces and reverse engineering capabilities within the security research community, do not inherently support EVM. While plugins like the IDA EVM plugin [5] and Ghidra EVM plugin [6] have been developed to bridge this gap, they still have limitations, such as incomplete support for the 256-bit machine word size and limited decompilation capabilities.

We present Mothra, a Ghidra extension designed to address the aforementioned limitations. By integrating with Ghidra, Mothra facilitates the disassembly, CFG visualization, and decompilation of smart contracts. Moreover, Mothra analyzes EVM bytecode to uncover the internals of smart contract such as smart contract metadata, external functions, function signatures, and calling references of internal functions. This empowers Ghidra with enhanced functionality tailored for reverse engineering EVM-based smart contracts.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Agneyastra - Firebase Misconfiguration Detection Toolkit</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Bhavarth Karmarkar](https://img.shields.io/badge/Bhavarth%20Karmarkar-informational) ![Devang Solanki](https://img.shields.io/badge/Devang%20Solanki-informational)

🔗 **Link:** Not Available  
📝 **Description:** Firebase, a versatile platform by Google, powers countless web and mobile applications with its extensive suite of services including real-time databases, authentication, cloud storage, and hosting. Its ubiquity and ease of use make it a popular choice among developers, but also a prime target for misconfigurations that can lead to significant security vulnerabilities.

Agneyastra, a mythological weapon bestowed upon by the Agni (fire) Dev (god) is a divine weapon associated with the fire element. Presenting Agneyastra, a cutting-edge tool designed to empower bug bounty hunters and security professionals with unparalleled precision in detecting Firebase misconfigurations. With its comprehensive checks covering all of Firebase services, an intelligent correlation engine, and automated report generation, Agneyastra ensures that no vulnerability goes unnoticed, turning the tides in your favor.

Key Features:

1. Checks for Misconfiguration in all the Firebase services.
2. Intelligent Correlation Engine.
3. POC and Report Creation.

</details>

<details><summary><strong>Blackdagger</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Mahmut Erdem Ozgen](https://img.shields.io/badge/Mahmut%20Erdem%20Ozgen-informational) ![Regaip Kurt](https://img.shields.io/badge/Regaip%20Kurt-informational) ![Onurhan Erdogdu](https://img.shields.io/badge/Onurhan%20Erdogdu-informational) ![Ata Seren](https://img.shields.io/badge/Ata%20Seren-informational)

🔗 **Link:** Not Available  
📝 **Description:** Blackdagger represents a significant advancement, offering a comprehensive solution for orchestrating complex workflows in DevOps, DevSecOps, MLOps, MLSecOps, and Continuous Automated Red Teaming (CART) environments.

At its core, Blackdagger simplifies the management and execution of intricate workflows through its user-friendly approach and powerful functionality. Leveraging a declarative YAML format, Blackdagger enables users to define automation pipelines using a Directed Acyclic Graph (DAG), facilitating clear and concise expression of task dependencies and execution logic.

What sets Blackdagger apart is its simplicity and versatility. Unlike traditional cron-based schedulers or workflow orchestration platforms, Blackdagger eliminates the need for extensive scripting or coding. With a built-in Web UI, users can easily manage, rerun, and monitor automation pipelines in real-time, streamlining the workflow management process. Additionally, Blackdagger offers native Docker support, enabling seamless integration with containerized environments, and a versatile toolset for task execution, including making HTTP requests and executing commands over SSH.
Blackdagger stands out due to its comprehensive features aimed at simplifying and enhancing automation workflow management.

Highlights of Blackdagger

* Single binary file installation
* Declarative YAML format for defining DAGs
* Web UI for visually managing, rerunning, and monitoring pipelines
* Use existing programs without any modification
* Self-contained, with no need for a DBMS
* Suitable for Continuous Red Teaming (CART)
* Suitable for DevOps and DevSecOps
* Suitable for MLOps and MLSecOps

</details>

<details><summary><strong>BugHog: A powerful framework for pinpointing bug lifecycles in web browsers</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Gertjan Franken](https://img.shields.io/badge/Gertjan%20Franken-informational)

🔗 **Link:** [BugHog: A powerful framework for pinpointing bug lifecycles in web browsers](https://github.com/DistriNet/BugHog)  
📝 **Description:** BugHog is a comprehensive framework designed to identify the complete lifecycle of browser bugs, from the code change that introduced the bug to the code change that resolved the bug. For each bug's proof of concept (PoC) integrated in BugHog, the framework can perform automated and dynamic experiments using Chromium and Firefox revision binaries.

Each experiment is performed within a dedicated Docker container, ensuring the installation of all necessary dependencies, in which BugHog downloads the appropriate browser revision binary, and instructs the browser binary to navigate to the locally hosted PoC web page. Through observation of HTTP traffic, the framework determines whether the bug is successfully reproduced. Based on experiment results, BugHog can automatically bisect the browser's revision history to identify the exact revision or narrowed revision range in which the bug was introduced or fixed.

BugHog has already been proven to be a valuable asset in pinpointing the lifecycle of security bugs, such as Content Security Policy bugs.

</details>

<details><summary><strong>CVE Half-Day Watcher: Hunting Down Vulnerabilities Before the Patch Drops</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Mor Weinberger](https://img.shields.io/badge/Mor%20Weinberger-informational) ![Yakir Kadkoda](https://img.shields.io/badge/Yakir%20Kadkoda-informational)

🔗 **Link:** Not Available  
📝 **Description:** Defenders and attackers often simplify vulnerabilities into '0-day' or '1-day' categories, neglecting the nuanced gray areas where attackers thrive. In this session, we'll explore critical flaws we've uncovered in the open-source vulnerability disclosure process and introduce our tool to detect open-source projects that are at risk from these flaws. We'll reveal how vulnerabilities can be exploited prior to receiving patches and official announcements, posing significant risks for users. Our comprehensive analysis of GitHub (including issues, pull requests, and commit messages) and NVD metadata will illuminate vulnerabilities that don't neatly fit into the conventional '0-day' or '1-day' classifications but instead fall into 'Half-Day' or '0.75-Day' periods – moments when vulnerabilities are known but not yet fully disclosed or patched. Furthermore, we'll spotlight the techniques employed to identify these vulnerabilities, showcasing various scenarios and vulnerabilities discovered through this method. During this session, we'll introduce an open-source tool designed to detect such vulnerabilities and emphasize the window of opportunity for attackers to exploit this information and develop exploits. Our objective is to aid practitioners in identifying and mitigating issues throughout their vulnerability disclosure lifecycle.

</details>

<details><summary><strong>FZAI Fuzzer - Behind AI Lines: Disrupting LLM Alignment to Build Bombs, Leading to Enhanced Security</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Eran Shimony](https://img.shields.io/badge/Eran%20Shimony-informational) ![Shai Dvash](https://img.shields.io/badge/Shai%20Dvash-informational)

🔗 **Link:** Not Available  
📝 **Description:** Who would have thought that asking LLMs to build bombs could enhance their security? Hold that thought. As these models become integral to our everyday digital tools—resembling a new operating system—they lack many of the security features we've come to expect. But here's where we turn the tables: understanding and disrupting their core alignments.

Our approach uses our deep experience as vulnerability researchers and applies zero-day research strategies to Generative AI. We've developed a systematic method to break into all the most updated LLM models and are excited to share our new open-source fuzzing infrastructure. This tool doesn't just jailbreak LLMs efficiently—it also helps us create detection-based solid solutions that improve LLM security.

</details>

<details><summary><strong>MPT: Pentest In Action!</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Jyoti Raval](https://img.shields.io/badge/Jyoti%20Raval-informational)

🔗 **Link:** [MPT: Pentest In Action!](https://github.com/RohitLearner/Youtube_India_Data_Exploration/blob/master/preprocessedtest2019.csv)  
📝 **Description:** Security penetration testing is becoming as necessary and as usual a practice as software testing. Most, if not all, organisations either have their own penetration testing team or they utilise third-party pentesters.

Imagine any fast-paced organisation developing multiple product lines and planning to release each of them from time to time. It becomes challenging for the organisation's security team to efficiently manage all of these pentest activities running and effectively produce security assessment reports and track them.

Because of such volume of work, the numbers of pentesters in organisations are increasing to keep up. Each pentester is doing multiple pentests. The next cycle of a previous pentest can get assigned to another pentester. Each pentesting cycle has issues and recurring issues. And above all, managing all these using Excel worksheets is nightmare.

A pentesting activity knowledge base is kind of must. A single-pane-of-glass view to all pentests running, and the issues identified, is a necessity for everyone involved in the security review cycle.

To solve these challenges, I have developed a solution called Managing Pentest (MPT): Pentest in Action.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>AI Wargame</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational) ![Davide Cioccia](https://img.shields.io/badge/Davide%20Cioccia-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>MACOBOX - The all-in-one hacking toolbox for hardware penetration testing.</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Matteo Mandolini](https://img.shields.io/badge/Matteo%20Mandolini-informational) ![Giuseppe Compare](https://img.shields.io/badge/Giuseppe%20Compare-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>PIZZABITE and BRUSCHETTABOARD: The Hardware Hacking Toolkit</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Android BugBazaar: Your mobile appsec playground to Explore, Exploit, Excel</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Amit kumar](https://img.shields.io/badge/Amit%20kumar-informational) ![Vedant Wayal](https://img.shields.io/badge/Vedant%20Wayal-informational)

🔗 **Link:** [Android BugBazaar: Your mobile appsec playground to Explore, Exploit, Excel](https://github.com/payatu/BugBazaar)  
📝 **Description:** Ever felt frustrated of installing multiple apps to learn and practice Android pentesting? BugBazaar is all in one mobile application designed to serve as a hands-on learning platform for mobile application security enthusiasts. Created intentionally with over 30 vulnerabilities and 10+ features, BugBazaar provides a real-world environment for users to explore, practice, and enhance their mobile app security and penetration testing skills.
Whether you're a security enthusiast, a developer looking to understand vulnerabilities, a beginner entering the mobile app security arena, or a professional seeking skill refinement, BugBazaar has something for everyone. With a diverse range of vulnerabilities, from "Remote Code Execution through insecure Dynamic Code Loading" to "One Click Account Takeover via deeplink," BugBazaar covers an array of scenarios and vulnerabilities commonly found in mobile applications.
Cherry on the top is BugBazaar gets frequent updates with latest vulnerabilities to keep up with current mobile applications security landscape.

</details>

<details><summary><strong>Damn Vulnerable Browser Extension (DVBE) - Knowing the risks of your Browser Supplements</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Abhinav Khanna](https://img.shields.io/badge/Abhinav%20Khanna-informational) ![Krishna Chaganti](https://img.shields.io/badge/Krishna%20Chaganti-informational)

🔗 **Link:** Not Available  
📝 **Description:** In the ever expanding world of Browser Extensions, security remains a big concern. As the demand of the feature-rich extensions increases, priority is given to functionality over robustness, which makes way for vulnerabilities that can be exploited by malicious actors. The danger increases even more for organizations handling sensitive data like banking details, PII, confidential org reports etc.

Damn Vulnerable Browser Extension (DVBE) is an open-source vulnerable browser extension, designed to shed light on the importance of writing secure browser extensions and to educate the developers and security professionals about the vulnerabilities and misconfigurations that are found in the browser extensions, how they are found & how they impact business. This built-to-be vulnerable extension can be used to learn, train & exploit browser extension related vulnerabilities.

</details>

<details><summary><strong>GitArmor: policy as code for your GitHub environment</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Davide Cioccia](https://img.shields.io/badge/Davide%20Cioccia-informational) ![Stefan Petrushevski](https://img.shields.io/badge/Stefan%20Petrushevski-informational)

🔗 **Link:** Not Available  
📝 **Description:** DevOps security does not only mean protecting the code, but also safeguarding the entire DevOps platform against supply chain attacks, integrity failures, pipelines injections, outsider permissions, worst practices, missing policies and more.

DevOps platforms like GitHub can easily grow in repos, actions, tokens, users, organizations, issues, PRs, branches, runners, teams, wiki, making admins' life impossible. This means also lowering the security of such environment.

GitArmor is a policy as code tool, that helps companies,teams and open-source creators, evaluate and enforce their GitHub (only for now) security posture at repository or organization level. Using policies defined using yml, GitArmor can run as CLI, GitHub action or GitHub App, to unify visibility into DevOps security posture and strengthen resource configurations as part of the development cycle.

</details>

<details><summary><strong>Open Source Tool to Shift Left Security Testing by Leveraging AI</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Shivam Rawat](https://img.shields.io/badge/Shivam%20Rawat-informational) ![Shivansh Agrawal](https://img.shields.io/badge/Shivansh%20Agrawal-informational)

🔗 **Link:** Not Available  
📝 **Description:** **Shift left** means conducting security testing earlier in the software and application development phases. In traditional DevOps, the stages typically flow like this: Plan > Code > Build > Test > Deploy > Monitor.

Detecting critical security issues during the development phase is much more cost-effective since fixing vulnerabilities at later stages can be significantly more expensive. One approach to achieving this is through **source code analysis** using AI to detect vulnerabilities early. This includes monitoring whether new vulnerabilities are being introduced in pull requests.

At Akto, we have developed an open-source tool that can perform all the above in a shift-left manner. I have built this tool in the last one year and want to showcase it's capability.

Akto's source code scanning can detect:

- All the APIs currently defined in the source code
- All the parameters of those APIs
- The authentication mechanisms

This method allows for pinpointing the exact location where a security fix is needed and detecting any new vulnerabilities being added through continuous integration and continuous deployment (CI/CD) processes.

This is my main project and I will love to present my work to audience at BlackHat.

</details>

<details><summary><strong>Secret Magpie</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Alexander Brozych](https://img.shields.io/badge/Alexander%20Brozych-informational) ![Simon Gurney](https://img.shields.io/badge/Simon%20Gurney-informational)

🔗 **Link:** Not Available  
📝 **Description:** Secret Magpie is a secret scanning tool that leverages Gitleaks and TruffleHog as a backend for bulk scanning git repositories within organizations such as GitHub, Bitbucket, Azure DevOps, etc in order to produce machine readable and human friendly output. Secret Magpie is able to provide a web based UI for quickly filtering through the results from the backend tools to help with quickly eliminating false positives and identifying the most likely place secrets will be found.

</details>

<details><summary><strong>Tabby: Simplifying the Art of Java Vulnerability Hunting</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Baizhu Wang](https://img.shields.io/badge/Baizhu%20Wang-informational) ![Xingchen Chen](https://img.shields.io/badge/Xingchen%20Chen-informational)

🔗 **Link:** Not Available  
📝 **Description:** Tabby is an automated vulnerability discovery ecosystem specifically designed for Java, aimed at enhancing the efficiency of security researchers in identifying vulnerabilities in third-party dependencies and commercial applications. It introduces a phased taint analysis algorithm based on code property graphs, ensuring both scalability and repeatability throughout the analysis process. The ecosystem consists of four main components:

- Tabby Core: The heart of Tabby, this component leverages a taint analysis engine to transform code into graph data. It supports custom plugins, allowing users to inject their own logic into processes such as function identification and call edge creation, enabling precise recognition of specific code patterns.
- Tabby-Path-Finder: Utilizes Neo4j's powerful graph traversal capabilities to perform inter-procedural taint analysis on graph databases.
- Tabby-Vul-Finder: Imports tainted data into the graph database and supports configurable automated vulnerability discovery, streamlining the detection process.
- Tabby-Intellij-Plugin: Integrates with IntelliJ IDEA to provide quick navigation from graph data to code, significantly improving the efficiency of vulnerability analysis.

With Tabby, you can uncover a wide range of Java-related vulnerabilities, including classic web vulnerabilities (such as those involving various frameworks and servlets), Netty-style RPC vulnerabilities, and diverse deserialization exploitation chains. The art of Java vulnerability hunting is simplified into cypherized database queries. To date, Tabby has helped discover over 100 zero-day vulnerabilities, with CVEs filed for several open-source projects, including XStream and Dubbo.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Campus as a Living Lab: An Open-World Hacking Environment</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Weihan Goh](https://img.shields.io/badge/Weihan%20Goh-informational) ![Steven Wong](https://img.shields.io/badge/Steven%20Wong-informational)

🔗 **Link:** [Campus as a Living Lab: An Open-World Hacking Environment](https://github.com/loire/IntregrativeHealthConcept/blob/master/data/OneHealth.tsv)  
📝 **Description:** The ASEAN Bug Bounty Beta Edition is a groundbreaking initiative dedicated to enhancing cybersecurity across the Southeast Asian region. Held in July 2024, we invited skilled and passionate vulnerability researchers to collaborate in identifying vulnerabilities within the Singapore Institute of Technology (SIT) Campus as a Living Lab - a real-world, cyber-physical environment that is our university in sunny Singapore.

Unlike other bug bounty events where the rules of engagement limits you to only particular applications or systems, our bug bounty allowed vulnerability researchers to roam and find vulnerabilities in an open-world campus across our living lab - including its network, hosted IoT prototypes, smart lighting system, and intelligent building management system. We also opened up our Living Lab Operating System proof-of-concept - this manages control and access of living lab assets such as lift systems and sensor devices, our Data Lake, which provides data sinking and logging capabilities for the living lab, as well as a preview version of our Virtual Campus metaverse modelled after our new campus in northeast Singapore.

With the success of our bug bounty event, we look to bring this playground to a wider audience at Black Hat Europe, where you can look forward to testing your vulnerability research skills almost freely on a real-world environment. We may even have some special guests contributing additional platforms to the environment for you to try.

</details>

<details><summary><strong>Cloud Offensive Breach and Risk Assessment (COBRA)</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Harsha Koushik](https://img.shields.io/badge/Harsha%20Koushik-informational) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational)

🔗 **Link:** [Cloud Offensive Breach and Risk Assessment (COBRA)](https://github.com/PaloAltoNetworks/cobra-tool)  
📝 **Description:** Cloud Offensive Breach and Risk Assessment (COBRA) is an open-source tool designed to empower users to simulate attacks within multi-cloud environments, offering a comprehensive evaluation of security controls. By automating the testing of various threat vectors including external and insider threats, lateral movement, and data exfiltration, COBRA enables organizations to gain insights into their security posture vulnerabilities. COBRA is designed to conduct simulated attacks to assess an organization's ability to detect and respond to security threats effectively.

</details>

<details><summary><strong>DarkWidow: Customizable Dropper Tool Targeting Windows</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Soumyanil Biswas](https://img.shields.io/badge/Soumyanil%20Biswas-informational)

🔗 **Link:** [DarkWidow: Customizable Dropper Tool Targeting Windows](https://github.com/reveng007/DarkWidow)  
📝 **Description:** This is a customizable Dropper Tool targeting Windows machines.

The capabilities it possesses are:
1. Indirect Dynamic Syscall
2. SSN + Syscall address sorting via Modified TartarusGate approach
3. Remote Process Injection via APC Early Bird (MITRE ATT&CK TTP: T1055.004) to cut off telemetry catching by EDR
4. Spawns a sacrificial Process as the target process
5. ACG(Arbitrary Code Guard)/BlockDll mitigation policy on spawned process
6. PPID spoofing (MITRE ATT&CK TTP: T1134.004)
7. Api resolving from TIB (Directly via offset (from TIB) -> TEB -> PEB -> resolve Nt Api) (MITRE ATT&CK TTP: T1106)
8. Cursed Nt API/ Dll hashing
9. If blessed with Admin privilege:
Disables Event Log via killing all threads of svchost.exe, i.e. killing the whole process (responsible svchost.exe)
10. Synthetic Frame Thread Stack Spoofing

This tool performed a successful Execution of payload and provided Crystal clear Event Log against Sophos XDR enabled Environment.

</details>

<details><summary><strong>distribRuted - Distributed Attack Framework (Botnet as a Service)</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Melih Tas](https://img.shields.io/badge/Melih%20Tas-informational) ![Numan Ozdemir](https://img.shields.io/badge/Numan%20Ozdemir-informational)

🔗 **Link:** Not Available  
📝 **Description:** Penetration testing tools often face limitations such as IP blocking, insufficient computing power, and time constraints. However, these challenges can be overcome by executing these tests across a distributed network of hundreds of devices. Organizing such a large-scale attack efficiently is complex, as the number of nodes increases, so does the difficulty in orchestration and management.

distribRuted provides the necessary infrastructure and orchestration for distributed attacks. This framework allows developers to easily create and execute specific distributed attacks using standard application modules. Users can develop their attack modules or utilize pre-existing ones from the community. With distribRuted, automating, managing, and tracking a distributed attack across hundreds of nodes becomes straightforward, thereby enhancing efficiency, reducing time and costs, and eliminating a Single Point of Failure (SPoF) in penetration testing.

</details>

<details><summary><strong>FaceGSM: A Targeted FGSM Attack Framework for Face Recognition Embedding Models</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Delbert Giovanni Lie](https://img.shields.io/badge/Delbert%20Giovanni%20Lie-informational) ![Clintswood Clintswood](https://img.shields.io/badge/Clintswood%20Clintswood-informational) ![Clario Adorabell Johan](https://img.shields.io/badge/Clario%20Adorabell%20Johan-informational) ![Chrisando Ryan Pardomuan Siahaan](https://img.shields.io/badge/Chrisando%20Ryan%20Pardomuan%20Siahaan-informational) ![Yohan Muliono](https://img.shields.io/badge/Yohan%20Muliono-informational)

🔗 **Link:** Not Available  
📝 **Description:** Our faces are being scanned every day: to unlock phones, to establish KYC identity, and perhaps to board many flights. Truth be told, with great adoption comes even greater threats lurking. Since the dawn of facial recognition technology, many adversarial techniques to fool facial recognition models have come to their inception: Fast Gradient Sign Method (FGSM), Deepfake, Projected Gradient Descent (PGD), and many more. The bad news is, to exploit facial recognition technology is no walk in the park. One must have both AI proficiency and hacking finesse to actually pull it off flawlessly.

But not with FaceGSM. As the name implies, FaceGSM utilizes the FGSM approach to create a subtle layer of semi-invincible pixels. When applied to an image of a person's face, this layer will make the model to misidentify the face as someone else.

What the name does not imply, however, is that you don't even need to know what an FGSM is to exploit a facial recognition model using FaceGSM framework. With just access to a facial recognition model and the target's face of your choice, FaceGSM will attempt to understand the construction of the model, apply image pre-processing accordingly, and then generate layers of perturbation pixels that could make a facial recognition model to misclassify your face into your target's face.

</details>

<details><summary><strong>Genzai - The IoT Security Toolkit</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Syed UmairUddin Nehri](https://img.shields.io/badge/Syed%20UmairUddin%20Nehri-informational)

🔗 **Link:** Not Available  
📝 **Description:** With a widespread increase in the adoption of IoT or Internet of Things devices, their security has become the need of the hour. Cyberattacks against IoT devices have grown rapidly and with platforms like Shodan, it has become much easier to scroll through the entire internet and look for just the right target which an attacker wants. To combat such threats it has become necessary for individuals and organisations to secure their IoT devices but when it becomes harder to keep track of them, the chances of unpatched loopholes increase.

To address this concern and give the users a better visibility of their assets, introducing Genzai! Genzai helps users keep track of IoT device-related web interfaces, scan them for security flaws and scan against custom policies for vendor-specific or all cases.
Tool features:
- Identify the IoT product deployed on a target
- Bruteforce panels for vendor-specific and generic/common password lists to look for default creds
- Use pre-defined templates/payloads to look for vulnerabilities

</details>

<details><summary><strong>GoatPen: Hack, Hone, Harden</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational) ![Shantanu Shirish Kale](https://img.shields.io/badge/Shantanu%20Shirish%20Kale-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Halberd : Cloud Security Testing Tool</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Arpan Abani Sarkar](https://img.shields.io/badge/Arpan%20Abani%20Sarkar-informational)

🔗 **Link:** Not Available  
📝 **Description:** Halberd is an open-source security testing tool to proactively assess cloud threat detection by executing a comprehensive array of attack techniques across multiple platforms (Entra ID, M365, Azure and AWS) reducing the need for multiple tools while enabling cross-platform attack path testing.

Leveraging Halberd, security teams can swiftly & easily execute attack techniques to generate telemetry and validate their controls and detection & response capabilities via a simple intuitive web interface. Halberd aims to reduce the friction to perform effective and continuous security testing by providing an easy to deploy and executable library of attack techniques. Halberd also provides additional capabilities to automate testing and testing with attack playbooks making it easier to chain and emulate

</details>

<details><summary><strong>Kitsune: One C2 to control them all</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Joel Gámez Molina](https://img.shields.io/badge/Joel%20Gámez%20Molina-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>level_up! : Web3 Security WarGames</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pablo Gonzalez Perez](https://img.shields.io/badge/Pablo%20Gonzalez%20Perez-informational) ![Alvaro Nuñez-Romero](https://img.shields.io/badge/Alvaro%20Nuñez-Romero-informational)

🔗 **Link:** Not Available  
📝 **Description:** As we navigate the increasingly interconnected digital landscape, the dawn of Web3, or the decentralized web, marks a significant leap forward in internet technology. Powered by blockchain technology and smart contracts, Web3 promises unparalleled levels of decentralization, transparency, and user empowerment. However, with these new opportunities come novel challenges, and none are more pressing than security. While the decentralized nature of Web3 eliminates single points of failure characteristic of Web2 applications, it also introduces a unique set of vulnerabilities that require attention.

From exploitable smart contract code to sophisticated re-entrancy attacks, Web3's security threats pose significant financial and reputational risks, as demonstrated by high-profile hacking incidents in recent years. This underscores the critical need for a deep understanding of Web3 security. As a result, designing, developing, and operating secure Web3 applications and platforms have become essential skills in today's rapidly evolving digital terrain. Simply building on top of blockchain technologies is no longer enough; developers, cybersecurity experts, and even end-users must now grasp the fundamental principles of securing these systems to ensure a safe and trustworthy online environment.

The level_up! project is an open-source initiative aimed at teaching about security in Web3. It provides a platform featuring a system of challenges, categorized by difficulty level, where various Web3 concepts are presented, and points are earned upon successfully overcoming these challenges. The goal is learning. Users register on the platform and can deploy multiple SmartContracts. Each challenge might comprise one or more SmartContracts.

</details>

<details><summary><strong>Matildapp: Multi Analysis Toolkit (by IdeasLocas) on DAPPs</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pablo Gonzalez](https://img.shields.io/badge/Pablo%20Gonzalez-informational) ![Javier Alvarez](https://img.shields.io/badge/Javier%20Alvarez-informational)

🔗 **Link:** Not Available  
📝 **Description:** Web3 is a paradigm that has burst into the digital world with force. Millions of transactions are performed on different types of blockchain. The importance of smart contracts on blockchain, such as Ethereum, is gaining greater relevance due to the finances being managed. A single error or security breach can cost millions of dollars, making cybersecurity a vital factor. This paper introduces the tool Madildapp, which enables conducting DAST and SAST tests to evaluate the security of smart contracts and other elements within the Web3 value chain (such as DAPPs themselves). It is an innovative tool that aggregates different types of tests oriented towards different types of elements, including bytecode, pure source code, and the contract in its own execution through dynamic tests. Madildapp is an all-in-one modular implementation that will help the community to improve the tool.

</details>

<details><summary><strong>Morion - A Tool for Experimenting with Symbolic Execution on Real-World Binaries</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Damian Pfammatter](https://img.shields.io/badge/Damian%20Pfammatter-informational)

🔗 **Link:** [Morion - A Tool for Experimenting with Symbolic Execution on Real-World Binaries](https://github.com/cyber-defence-campus/morion)  
📝 **Description:** Morion (https://github.com/cyber-defence-campus/morion) is a proof-of-concept (PoC) tool to experiment with symbolic execution and to investigate the current limitations of this technique when applied to real-world binaries. Morion utilizes Triton (https://github.com/JonathanSalwan/Triton) as its underlying symbolic execution engine and operates in two distinct execution modes: (1) Tracing: Record concrete execution traces (concrete initial register/memory values, as well as a sequence of assembly instructions) of a target binary (optionally in a cross-platform remote setup). (2) Symbolic Execution: Analyze collected program traces by executing them symbolically.

Morion's modular design facilitates the seamless integration of custom symbolic analysis passes. It currently includes passes for detecting and analyzing control-flow and memory hijacking conditions, reasoning about code coverage, as well as assisting with the generation of ROP chains. Currently, Morion's implementation is restricted to ARMv7 binaries. However, the tool can be easily extended to support other architectures compatible with its underlying symbolic execution engine Triton.

To highlight some of Morion's capabilities, a detailed write-up (https://github.com/cyber-defence-campus/netgear_r6700v3_circled) has been created that demonstrates how the tool can assist in the process of exploit generation. The targeted vulnerability corresponds to CVE-2022-27646, a known stack buffer overflow affecting NETGEAR R6700v3 routers (in version 10.04.120_10.0.91). Along with demonstrating Morion's main functionalities, the write-up provides a comprehensive explanation - including setup, emulation, tracing, symbolic execution, vulnerability description and exploit generation - allowing the interested reader to follow along.

</details>

<details><summary><strong>Nebula - 3 years of kicking *aaS and taking usernames</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Bleon Proko](https://img.shields.io/badge/Bleon%20Proko-informational)

🔗 **Link:** [Nebula - 3 years of kicking *aaS and taking usernames](https://gist.github.com/kunalj101/ad1d9c58d338e20d09ff26bcc06c4235?permalink_comment_id=3484437)  
📝 **Description:** Nebula is a Cloud Penetration Testing framework. It is build with modules for each provider and each functionality. It covers AWS, Azure (both Graph and Management API, which includes Entra, Azure Subscription based resources and Office365) and DigitalOcean.
Currently covers:
- Public Reconnaissance
- Phishing
- Brute-force and Password Spray
- Enumeration of internal resources after initial access
- Lateral Movement and Privilege Escalation
- Persistence

</details>

<details><summary><strong>NotPacked++: Evading Static Packing Detection</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Alexandre D'Hondt](https://img.shields.io/badge/Alexandre%20D'Hondt-informational) ![Jaber Ramhani](https://img.shields.io/badge/Jaber%20Ramhani-informational) ![Charles-Henry Bertrand Van Ouytsel](https://img.shields.io/badge/Charles-Henry%20Bertrand%20Van%20Ouytsel-informational) ![Axel Legay](https://img.shields.io/badge/Axel%20Legay-informational)

🔗 **Link:** Not Available  
📝 **Description:** NotPacked++ is an adversarial weaponized tool to alter a packed executable to evade static packing detection. It is designed to be used by malware analysts to test the effectiveness of their detection mechanisms and to improve their detection capabilities. It is also useful for red teamers to test the effectiveness of their evasion techniques, and highlight potential weaknesses of a target's security mechanisms.

</details>

<details><summary><strong>Pandora: Exploit Password Management Software To Obtain Credential From Memory</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Efstratios Chatzoglou](https://img.shields.io/badge/Efstratios%20Chatzoglou-informational) ![Vyron Kampourakis](https://img.shields.io/badge/Vyron%20Kampourakis-informational) ![Zisis Tsiatsikas](https://img.shields.io/badge/Zisis%20Tsiatsikas-informational)

🔗 **Link:** [Pandora: Exploit Password Management Software To Obtain Credential From Memory](https://github.com/efchatz/pandora)  
📝 **Description:** Passwords comprise one of the cornerstones of cybersecurity since the early ages, with a plethora of attacks focusing on secretly acquiring user's passwords. Password management software (PM) has been developed as a key weapon for counteracting such attacks. However, despite the various protections implemented by this kind of software, misconfigurations and user's mistakes may still lead to sensitive data leaks.
In this context, the current presentation details on a newly developed red teaming tool called Pandora (https://github.com/efchatz/pandora). Specifically, Pandora can acquire end-user's credentials from 18 well-known PM implementations, ranging from MS Windows 10 desktop applications to browser plugins. The only requirement for Pandora is for the PM to be up-and-running, enabling the tool to dump the PM's processes. In more detail, after the tool is executed in the host machine, it will dump the PM's processes, analyze them and extract any user credentials it finds.
For a methodological viewpoint, Pandora is based on each PM implementation. Basically, most PMs store their entries/master credentials in plaintext format within the corresponding memory processes. To this end, Pandora comprises different autonomous scripts based on each PM implementation.
After following a CVD process, most vendors responded that such issues are out of their scope, since the attacker needs local access, or the AV/EDR may be able to impede such attacks. Overall, until now, only two vendors have acknowledged the problem and one has already reserved a CVE ID, namely CVE-2023-23349 (Kaspersky).

</details>

<details><summary><strong>Penelope shell handler</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Christodoulos Lamprinos](https://img.shields.io/badge/Christodoulos%20Lamprinos-informational) ![Carlos Marquez](https://img.shields.io/badge/Carlos%20Marquez-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>pwnobd: Offensive cybersecurity toolkit for vulnerability analysis and penetration testing of OBD-II devices.</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ignacio Gutiérrez Gómez](https://img.shields.io/badge/Ignacio%20Gutiérrez%20Gómez-informational) ![Roberto Gesteira Miñarro](https://img.shields.io/badge/Roberto%20Gesteira%20Miñarro-informational)

🔗 **Link:** Not Available  
📝 **Description:** The research field of vehicle cybersecurity has experienced a significant growth in interest due to the attack surface that the information systems comprising a vehicle provides and the ever-expanding body of regulations that provide special focus on cybersecurity on vehicular systems. Of particular interest is the attack surface exposed by OBD dongles, wireless devices that connect to the vehicle's diagnostic port, whose access to the vehicle's CAN buses could potentially be exploited by adversaries.

From an offensive security perspective, while it is possible to operationalize attacks in an ad-hoc manner, the resulting proof-of-concept programs may end constrained to a single vulnerable device model, further complicating scalable testing of the same vulnerability type against multiple devices; thus, extensible software frameworks can help the researcher develop and launch device-agnostic exploits, progressing towards operational implementations of attacks faster and more cost-effectively.

We reveal pwnobd, a Python-based offensive framework providing researchers with a common toolbox that allows for automation of simple attacks and provides assistance in the development of more complex attacks, deployable through an operator-ready command-line tool. A hardware demonstration platform will be provided on-site on the conference for the interested public to experiment with attacks that can be performed using this tool.

</details>

<details><summary><strong>RedCloud OS : Cloud Adversary Simulation Operating System</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yash Bharadwaj](https://img.shields.io/badge/Yash%20Bharadwaj-informational) ![Manish Kumar Gupta](https://img.shields.io/badge/Manish%20Kumar%20Gupta-informational)

🔗 **Link:** Not Available  
📝 **Description:** RedCloud OS is a Debian based Cloud Adversary Simulation Operating System for Red Teams to assess the security of leading Cloud Service Providers (CSPs). It includes tools optimised for adversary simulation tasks within Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

Enterprises are moving / have moved to Cloud Model or Hybrid Model and since security testing is a continuous procedure, operators / engineers evaluating these environments must be well versed with updated arsenal. RedCloud OS is an platform that contains:

- Custom Attack Scripts
- Installed Native Cloud Provider CLI
- 25+ Multi-Cloud Open-Source Tools
- Tools Categorization as per MITRE ATT&CK Tactics
- Support Multiple Authentication Mechanisms
- In-Built PowerShell for Attacking Azure Environment
- Ease to configure credentials of AWS, Azure & GCP & much more...

Inside each CSP, there are three sub-categories i.e, Enumeration, Exploitation, and Post Exploitation. OS categorises tools & our custom scripts as per the above mentioned sub-categories.

</details>

<details><summary><strong>Silver SAML Forger: Tooling to craft forged SAML responses from Entra ID</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Eric Woodruff](https://img.shields.io/badge/Eric%20Woodruff-informational) ![Tomer Nahum](https://img.shields.io/badge/Tomer%20Nahum-informational)

🔗 **Link:** Not Available  
📝 **Description:** Silver SAML Forger is a tool developed to PoC SAML response forging, also known as Silver SAML and Golden SAML attacks, against applications federated to Entra ID for authentication using the SAML standard. The tool goes along with research into the vulnerabilities that can present in cloud identity providers, such as Entra ID, where if an attacker has access to the private key material Entra ID uses for SAML response signing, that the target applications may be susceptible to these forging attacks.

While Entra ID protects the private key if generated internally, as it cannot be exported, in the real-world organizations follow bad habits that may leave sensitive private key material available to an attacker. These sorts of habits have been observed by the research team that developed the Silver SAML Forger. Using this tool in combination with tools such as Burp Suite, you can demonstrate forging access to a target application. If the application supports certain types of SAML integrations, the identity provider will have no visibility into the authentication – you could think of these attacks as Kerberos Golden-ticket type attacks.

The tool requires the signing certificate to use, the username that is target for impersonation, and some basic federation information about the target application that can be derived from a few different methods.

</details>

<details><summary><strong>SkyScalpel: Making & Breaking {"Policy": "Obf\u0075scA**Tion"} in the Cloud</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Abian Morina](https://img.shields.io/badge/Abian%20Morina-informational) ![Daniel Bohannon](https://img.shields.io/badge/Daniel%20Bohannon-informational)

🔗 **Link:** Not Available  
📝 **Description:** Cloud security professionals today must understand the role policies play in access management for all identities in their organizations – humans and machines alike. However, calculating an identity's effective permissions is complex due to policy inheritance (e.g. managed policies inherited from groups, roles and Service Control Principal, each with their own potential inline policies). But is a firm grasp on permissions calculation sufficient?

Obfuscation of cloud policies, remote administration command scripts and various permissions parameters is an oft-overlooked attack vector with implications at several stages of the detection engineering pipeline. When "Allow" becomes "Al\u006Cow" and "iam:PassRole" becomes "iam:P*ole", are current detections evaded? Some obfuscation techniques are detectable in runtime events during creation but silently sanitized upon storage and/or later retrieval by corresponding APIs. Other techniques persist into the storage of created entities (e.g. IAM policies). These obfuscation scenarios can evade string-based detections, break policy rendering pages in Management Consoles, and even selectively overwrite policy contents of an attacker's choosing based on the defender's viewing method. Additionally, we identified subtle differences between official cloud provider tooling (CLI, SDKs, Management Console) that complicate the generation and detection of these obfuscation scenarios.

In this Arsenal session we will showcase obfuscation, deobfuscation, and detection scenarios using SkyScalpel – our brand new, fully custom open-source JSON tokenizer and syntax tree parser. SkyScalpel includes highly configurable randomized JSON-level obfuscation (Unicode encoding, insignificant whitespace packing, and selective special characters like \b and  ), policy-level obfuscation at the syntactical and functional levels (e.g., wildcard expansion of ActionNames), and deobfuscation and detection mechanisms for all aforementioned obfuscation capabilities.

Come see how SkyScalpel enables surgical precision in cloud offense and defense.

</details>

<details><summary><strong>TrailShark: Unraveling AWS API and Service Interactions</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ofek Itach](https://img.shields.io/badge/Ofek%20Itach-informational) ![Yakir Kadkoda](https://img.shields.io/badge/Yakir%20Kadkoda-informational)

🔗 **Link:** Not Available  
📝 **Description:** TrailShark Capture Utility is a tool designed to integrate AWS CloudTrail logs directly into Wireshark. This integration allows for near-real-time analysis of AWS API calls, providing invaluable insights for debugging, security and research. With TrailShark, you can capture and examine the internal API calls triggered by AWS services, better understand what is "running under the hood", consequently shedding light on potential vulnerabilities and security flaws.

</details>

<details><summary><strong>[X-Post] A Post Exploitation Toolkit for High Value Systems</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![linhong Cao](https://img.shields.io/badge/linhong%20Cao-informational) ![Yichen Zhang](https://img.shields.io/badge/Yichen%20Zhang-informational)

🔗 **Link:** [[X-Post] A Post Exploitation Toolkit for High Value Systems](https://github.com/doujiang-zheng/Awesome-Graph-Learning-Papers-List)  
📝 **Description:** The topic discussed the post-exploitation research on high-value systems such as email servers, gateway devices, documents, enterprise knowledge management and collaboration platforms, single sign-on platforms, defect tracking platforms, IT operations management software, domain management team building, code repository management, etc.Targeting various applications, it was achieved by deploying highly covert plugins and leveraging deprecated functionalities to hijack the runtime web container request processing logic and implant highly concealed persistent backdoors in memory. These memory-implanted backdoors serve as loaders to execute effective payloads directly in memory, with both the backdoor code logic and functional payloads operating within memory.

In-depth analysis of the code logic for different applications led to the exploration of solutions for challenges encountered during the runtime execution of payloads in memory. These challenges included multiple class loader loading, bypassing system file verification protection, and context decoupling for functional code extraction, among other issues.

The implementation enabled the execution of effective payloads in memory without initiating additional network requests to the target or writing files to disk. This allowed for the covert execution of payloads in memory under highly concealed attack scenarios, facilitating the extraction of high-value system information, such as email retrieval, plaintext password recording, operations data acquisition, obtaining arbitrary login credentials under unknown passwords, domain controller information retrieval, single sign-on hijacking, and trace cleaning operations.

Subsequently, existing web shell management tools were utilized to encrypt and transmit data, achieving traffic-side concealment. This approach aims to achieve a more comprehensive, covert, and long-term post-exploitation information gathering and deep penetration in real-world attack scenarios.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>CyberSky Sentinel: Advanced Drone Signal Detection tool using USRP</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jie Fu](https://img.shields.io/badge/Jie%20Fu-informational) ![Kai Zhang](https://img.shields.io/badge/Kai%20Zhang-informational) ![Weichao Zhou](https://img.shields.io/badge/Weichao%20Zhou-informational)

🔗 **Link:** Not Available  
📝 **Description:** Drone signal detection tools are critical for ensuring security and regulatory compliance across diverse environments. This tool is named "CyberSky Sentinel," an embedded system designed for cost-effectiveness and efficiency, harnessing the capabilities of the USRP (Universal Software Radio Peripheral) to detect and analyze drone signals.

</details>

<details><summary><strong>RF Swift: a swifty toolbox for all wireless assessments</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Sébastien Dudek](https://img.shields.io/badge/Sébastien%20Dudek-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>Fabric: automating cybersecurity reporting</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Sergey Polzunov](https://img.shields.io/badge/Sergey%20Polzunov-informational)

🔗 **Link:** [Fabric: automating cybersecurity reporting](https://github.com/traut)  
📝 **Description:** Fabric is an open-source CLI tool and a configuration language for automating cybersecurity reporting. Taking inspiration from Terraform, we built a reporting-as-code DevSecOps tool that automates data collation and content rendering. By automating operational reporting, Fabric saves security teams time, formalizes communications, and improves stakeholder management.

</details>

---
## 🔍 OSINT
<details><summary><strong>Grappling for Evil in the Cloud</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Andi Ahmeti](https://img.shields.io/badge/Andi%20Ahmeti-informational)

🔗 **Link:** Not Available  
📝 **Description:** Cloudgrapple is a purpose-built tool designed for effortless querying of high-fidelity and single-event detections related to well-known threat actors in popular cloud environments such as AWS and Azure. Leveraging the capabilities of cloudgrep in the background—an established tool developed by Cado Security, explicitly designed to do what its name suggests—the tool is crafted with our Tactics, Techniques, and Procedures (TTPs). This integration enables users to query for and gather the latest threat intelligence, making Cloudgrappler a robust asset for any organization keen on assessing potential security incidents and determining the impact of an attack

</details>

<details><summary><strong>TSURUGI Linux - the sharpest weapon in your DFIR arsenal</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Giovanni Rattaro](https://img.shields.io/badge/Giovanni%20Rattaro-informational) ![Marco Giorgi](https://img.shields.io/badge/Marco%20Giorgi-informational)

🔗 **Link:** Not Available  
📝 **Description:** Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
A special Tsurugi Linux BLACKHAT EDITION will be shared only with the participants.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>MaskerLogger</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Eyal Paz](https://img.shields.io/badge/Eyal%20Paz-informational) ![Tamar Galer](https://img.shields.io/badge/Tamar%20Galer-informational)

🔗 **Link:** Not Available  
📝 **Description:** None

</details>

<details><summary><strong>Open Source GoTestWAF by Wallarm: New Features</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Claus Lohmar](https://img.shields.io/badge/Claus%20Lohmar-informational)

🔗 **Link:** Not Available  
📝 **Description:** GoTestWAF is a well-known open-source tool for evaluating Web Application Firewalls (WAFs), Runtime Application Self-Protection (RASPs), Web Application and API Protection (WAAP), and other security solutions by simulating attacks on the protected applications and APIs. The tool supports an extensive array of attack vectors, evasion techniques, data encoding formats, and runs tests across various protocols, including traditional web interfaces, RESTful APIs, WebSocket communications, gRPC, and GraphQL. Upon completion of the tests, it generates an in-depth report grading efficiency of solution and mapping it against OWASP guidelines.

The recently added features to the GoTestWAF are:
Vendor Identification/Fingerprinting: With session handling improvements, GoTestWAF can automatically identify security tools/vendors and highlights findings in the report.
OWASP Core Rule Set Testing: A script is added to generate test sets from the OWASP Core Rule Set regression testing suite. These vectors are not available by default and require additional steps as outlined in the readme.
Regular Expressions for WAF Response Analysis: Regular expressions can be used to analyze WAF responses.
Cookie Handling: GoTestWAF can consider cookies during scanning and update the session before each request. This allows scanning hosts that require specific WAF-specific cookies, as otherwise, requests are blocked.
Email Report Sending: GoTestWAF interactively prompts for an email address to send the report.
New Placeholders: Numerous new placeholders have been added, listed in the readme's "How It Works" section.

</details>

<details><summary><strong>SCAGoat - Exploiting Damn Vulnerable SCA Application</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Hare Krishna Rai](https://img.shields.io/badge/Hare%20Krishna%20Rai-informational) ![Gaurav Joshi](https://img.shields.io/badge/Gaurav%20Joshi-informational) ![Prashant Venkatesh](https://img.shields.io/badge/Prashant%20Venkatesh-informational)

🔗 **Link:** [SCAGoat - Exploiting Damn Vulnerable SCA Application](https://github.com/harekrishnarai/Damn-vulnerable-sca)  
📝 **Description:** SCAGoat is a deliberately insecure web application designed for learning and testing Software Composition Analysis (SCA) tools. It offers a hands-on environment to explore vulnerabilities in Node.js and Java Springboot applications, including actively exploitable CVEs like CVE-2023-42282 and CVE-2021-44228 (log4j). This application can be utilized to evaluate various SCA and container security tools, assessing their capability to identify vulnerable packages and code reachability. As part of our independent research, the README includes reports from SCA tools like semgrep, snyk, and endor labs. Future research plans include incorporating compromised or malicious packages to test SCA tool detection and exploring supply chain attack scenarios.

</details>

---
## Others
<details><summary><strong>MORF - Mobile Reconnaissance Framework</strong></summary>

![Europe 2024](https://img.shields.io/badge/Europe%202024-blue) ![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Amrudesh Balakrishnan](https://img.shields.io/badge/Amrudesh%20Balakrishnan-informational) ![Abhishek JM](https://img.shields.io/badge/Abhishek%20JM-informational) ![Himanshu Das](https://img.shields.io/badge/Himanshu%20Das-informational)

🔗 **Link:** Not Available  
📝 **Description:** MORF - Mobile Reconnaissance Framework is a powerful, lightweight, and platform-independent offensive mobile security tool designed to help hackers and developers identify and address sensitive information within mobile applications. It is like a Swiss army knife for mobile application security, as it uses heuristics-based techniques to search through the codebase, creating a comprehensive repository of sensitive information it finds. This makes it easy to identify and address any potentially sensitive data leak.

One of the prominent features of MORF is its ability to automatically detect and extract sensitive information from various sources, including source code, resource files, and native libraries. It also collects a large amount of metadata from the application, which can be used to create data science models that can predict and detect potential security threats. MORF also looks into all previous versions of the application, bringing transparency to the security posture of the application.

The tool boasts a user-friendly interface and an easy-to-use reporting system that makes it simple for hackers and security professionals to review and address any identified issues. With MORF, you can know that your mobile application's security is in good hands.

Overall, MORF is a Swiss army knife for offensive mobile application security, as it saves a lot of time, increases efficiency, enables a data-driven approach, allows for transparency in the security posture of the application by looking into all previous versions, and minimizes the risk of data breaches related to sensitive information, all this by using heuristics-based techniques.

</details>

---
