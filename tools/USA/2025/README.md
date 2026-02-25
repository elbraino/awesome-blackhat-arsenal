# USA 2025
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2025** event held in **USA**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Contents
- [☁️ Cloud Security](#☁️-cloud-security)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🤖 AI, ML & Data Science](#🤖-ai,-ml-data-science)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🔵 Blue Team & Detection
<details><summary><strong>StegoScan</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Luke Bower](https://img.shields.io/badge/Luke%20Bower-informational)

🔗 **Link:** [StegoScan](https://github.com/LCBOWER33/StegoScan)  
📝 **Description:** Bad actors have long used hidden information in many forms, for malicious purposes, continuously evolving their methods over time. To counter these threats, our detection software must also evolve, ensuring effective identification and mitigation. Heading these threats is stenography, the practice of concealing messages or content within other non-suspicious data. Previously steganography detection tools have focused on limited sets of file types at a surface level and require manual processing leading to unknown extents of undetected illicit content, and potentially wasteful labor. Which is why a better solution had to be developed: StegoScan.py is a powerful, next-generation tool that automates steganography detection in websites, web servers, and local directories, by integrating AI-driven object and deep file text recognition analysis. StegoScan.py is a comprehensive tool that is capable of scanning and scraping websites across a broad range of formats simultaneously with deep file extraction.

The tool boasts website and web server scanning capabilities, making it invaluable for security researchers monitoring illicit data exchanges or law enforcement tracking cybercriminals. A single command can analyze entire domains or IP ranges, retrieving and inspecting suspicious media and documents for hidden communications. Whether it's detecting covert exchanges in dark web marketplaces, identifying embedded propaganda in misinformation campaigns, or revealing concealed instructions within terrorist networks, StegoScan.py offers visibility into steganographic threats. Stegoscan.py integrates numerous AI models that enhance text detection by overcoming the former challenges of noise, distortions, and unconventional fonts, allowing forensic analysts, cybersecurity professionals, and law enforcement agencies to extract text from compromised media with increased confidence.

By combining multiple steganalysis techniques into a toolkit, StegoScan.py provides a detailed and multi-layered analysis of files, offering security teams, digital forensics experts, and cybersecurity researchers a cutting-edge solution to an evolving digital threat. As steganography techniques become more sophisticated, traditional tools fall short—StegoScan.py ensures organizations stay ahead of bad actors by detecting what others miss. This is accomplished by automatically scanning websites, organizing tests, utilizing AI to remove the need for manual inspection, and combining many mainstream tools and tests to ensure detection across a wide range of files and steganography techniques. In testing, StegoScan was able to scan a website and find hidden messages embedded in an image that was embedded in a pdf linked to the original webpage. This shows the depth and abilities that this tool offers, whereas operating with a previously developed workflow the user would have had to download the PDF manually, extract the suspected images and then run individual tests to uncover the stenography.

</details>

<details><summary><strong>MissionEvasion</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Zeus Chan](https://img.shields.io/badge/Zeus%20Chan-informational) ![Weihan Goh](https://img.shields.io/badge/Weihan%20Goh-informational)

🔗 **Link:** [MissionEvasion](https://github.com/LightningGod7/MissionEvasion)  
📝 **Description:** MissionEvasion is a proof-of-concept tool designed to demonstrate advanced process injection techniques that adapt to evolving Windows security mechanisms. Initially built on Process Hollowing, MissionEvasion now incorporates a modern Process Overwriting technique to bypass new mitigations introduced in Windows 11 24H2, particularly restrictions on executing payloads from MEM_PRIVATE regions. The tool walks through each step of the injection chain—mapping, section writing, relocation patching, and process restoration—with clear source code for red team research, education, and experimentation.

</details>

<details><summary><strong>GhostBeacon: Hunting for Rogue APs in 802.11 Networks</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Anıl Çelik](https://img.shields.io/badge/Anıl%20Çelik-informational) ![Emre Odaman](https://img.shields.io/badge/Emre%20Odaman-informational)

🔗 **Link:** [GhostBeacon: Hunting for Rogue APs in 802.11 Networks](https://github.com/ccelikanil/GhostBeacon)  
📝 **Description:** Wireless networks (802.11) are indispensable in today's communication systems. However, their inherent vulnerabilities generally pose significant security threats. Specifically, detecting Rogue (Fake) Access Points and Hidden Access Points can be very challenging, as these unauthorized entities can facilitate malicious activities once they infiltrate a network. This study addresses these issues by providing a solution named GhostBeacon, an innovative tool that is designed to detect such malicious access points effectively. GhostBeacon mainly consists of two primary modules: the Rogue (Fake) Access Point Spotter, which analyses Beacon Frames using couple of parameters to identify Rogue Access Points; and the Hidden Access Point Spotter, which analyses Probe Request/Response frames to uncover access points with hidden SSIDs. Experimental tests show that GhostBeacon achieves a detection success rate of up to 99% for Rogue Access Points and nearly 100% for Hidden Access Points. These results highlight this project's potential to enhance wireless network security by mitigating unauthorized access and the subsequent risk of harmful network activities.

</details>

<details><summary><strong>PolarDNS - Specialized DNS server for penetration testing and vulnerability research</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ivan Jedek](https://img.shields.io/badge/Ivan%20Jedek-informational)

🔗 **Link:** [PolarDNS - Specialized DNS server for penetration testing and vulnerability research](https://github.com/oryxlabs/PolarDNS)  
📝 **Description:** PolarDNS is a specialized authoritative DNS server written in Python, which allows the operator to produce fully custom DNS responses, suitable for DNS protocol security testing and vulnerability research.

PolarDNS can be used for testing of:

- DNS resolvers (server-side)
- DNS clients
- DNS libraries
- DNS parsers and dissectors
- any software handling DNS information

It supports both UDP and TCP protocols, and it gives the operator full control over the DNS protocol layer.

PolarDNS server can produce variety of non-standard and non-compliant DNS responses, DNS responses violating the RFC specifications, including highly abnormal and malformed DNS responses.

This can be useful for:

- Functional testing
- RFC compliance
- Vulnerability research

</details>

<details><summary><strong>BUDA (Behavioral User-driven Deceptive Activities Framework)</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Federico Pacheco](https://img.shields.io/badge/Federico%20Pacheco-informational) ![Diego Staino](https://img.shields.io/badge/Diego%20Staino-informational)

🔗 **Link:** [BUDA (Behavioral User-driven Deceptive Activities Framework)](https://github.com/Base4Security/BUDA)  
📝 **Description:** BUDA is an experimental framework designed to enhance deception operations by adding realistic traces of human to deception activities. It automates the simulation of realistic user behaviors within decoy environments. BUDA recreates normal activity patterns in your environment, enhancing deception strategies through the generation of automated and realistic digital footprints. It also enables consistency in the generation of cyber deception operations by automating the process of generating and executing deception tasks.
It achieves this through the integration of strategic narratives, dynamic user profiles, and automated activity simulation. BUDA can also leverage real-env data for context and integrate Language Models (LLMs) for assisted generation of profiles and activities.

</details>

<details><summary><strong>Q-TIP (QR Code Threat Inspection Platform)</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rushikesh D. Nandedkar](https://img.shields.io/badge/Rushikesh%20D.%20Nandedkar-informational)

🔗 **Link:** [Q-TIP (QR Code Threat Inspection Platform)](https://github.com/1nod3/Q-TIP)  
📝 **Description:** **Abstract:**

Q-TIP – QR Threat Inspection Protocol is an innovative, multi-layered cybersecurity tool designed to combat the emerging threat of QR code-based phishing attacks. By combining robust QR code decoding, comprehensive static URL analysis (including redirection chain tracking, WHOIS lookups, and SSL certificate validation), and advanced visual forensics using OpenCV, Q-TIP offers a granular, data-driven assessment of phishing risks. Additionally, the tool integrates threat intelligence from a continuously updated phishing artifacts database and implements suspicious file detection by securely downloading and analyzing files with malicious extensions. Its modular, scalable design supports both single-image and batch processing, generating detailed forensic reports in TXT and HTML formats that explicitly enumerate the reasons behind each phishing verdict.

**Takeaways:**

- **Comprehensive Analysis:** Q-TIP leverages multiple layers of analysis to assess QR code threats with high accuracy.
- **Robust Reporting:** Detailed, actionable reports provide clear insights into the factors contributing to a phishing verdict.
- **Scalable & Modular:** Designed for both enterprise and research applications, with support for real-time and batch processing.
- **Future-Ready:** The platform is built to evolve with integrated real-time threat intelligence, machine learning enhancements, and dynamic file forensics to safeguard millions against phishing attacks.

This abstract encapsulates Q-TIP's promise to revolutionize QR code phishing detection through technical rigor, innovative methodologies, and forward-thinking design—making it a compelling solution for Black Hat USA Arsenal 2025.

</details>

<details><summary><strong>SHELLSILO</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tarek Ahmed](https://img.shields.io/badge/Tarek%20Ahmed-informational)

🔗 **Link:** [SHELLSILO](https://github.com/nixpal/shellsilo)  
📝 **Description:** While Windows System Calls have become a popular method for evading antivirus detection, they present considerable challenges beyond simple shellcode encryption/decryption. Unlike Linux, executing Windows System Calls often necessitates extensive setup, due to the need for specific C structures, which makes the code more complex and prone to errors compared to typical API calls. As a result, many developers turn to high-level languages like C to avoid the complexities of Assembly, particularly in malware development.

SHELLSILO addresses these challenges by offering an innovative solution for System Call shellcode generation. By interpreting basic C syntax, it seamlessly converts code into x86 and x64 Assembly and, ultimately, shellcode. This process encompasses various constructs such as while loops, if statements, variables, structures, and System Call invocations. SHELLSILO significantly streamlines the shellcode creation process by automating tasks like parsing, formatting, and initialization.

One of SHELLSILO's standout features is its ability to simplify quick modifications. Users can easily adjust variables or individual lines in the original C code, making the process of generating System Call shellcode more accessible and efficient. With SHELLSILO, the intricacies of System Call shellcode generation are simplified, offering a powerful tool that enhances cybersecurity practices.

</details>

<details><summary><strong>Azazel System: Tactical Delaying Action via the Cyber-Scapegoat Gateway</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Makoto SUGITA](https://img.shields.io/badge/Makoto%20SUGITA-informational)

🔗 **Link:** [Azazel System: Tactical Delaying Action via the Cyber-Scapegoat Gateway](https://github.com/01rabbit/azazel-zero)  
📝 **Description:** Azazel System is a portable cybersecurity gateway designed to implement tactical delaying actions by leveraging cyber-scapegoat deception. Unlike traditional honeypots that passively observe attacks or decoy servers that mislead adversaries, Azazel actively absorbs, controls, and delays attacks, providing defenders with critical response time.

Built on a Raspberry Pi 5 (8GB) hybrid architecture, Azazel System integrates:

Real-time intrusion monitoring (Suricata)
Network delay and redirection mechanisms (tc, iptables)
Deception techniques using OpenCanary
Automated log forwarding and adversary classification (Fluent Bit, MITRE ATT&CK)
Azazel System is designed for low-cost, high-performance cyber defense, making it highly adaptable for deployment in public Wi-Fi, untrusted network infrastructures, or high-risk security environments. Inspired by military delaying tactics, it manipulates attacker behavior, disrupting their operations while preserving valuable response time for defenders.

</details>

<details><summary><strong>Next-Generation Post-Exploitation in Cobalt Strike</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Santos Salinas](https://img.shields.io/badge/Santos%20Salinas-informational)

🔗 **Link:** [Next-Generation Post-Exploitation in Cobalt Strike](https://github.com/Cobalt-Strike)  
📝 **Description:** Recent advances in Windows AI/ML APIs now enable the direct integration of AI/ML models into post-exploitation DLLs, allowing them to run within active Cobalt Strike sessions for enhanced on-target classification. This work presents two examples of such integration. The first leverages a custom-trained model to detect passwords in text extracted from documents. The second adapts an open-source embedding model into a compatible format, enabling semantic search capabilities within the target environment.

</details>

<details><summary><strong>TCP Fingerprint Firewall / Recon Shield</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Vlad Iliushin](https://img.shields.io/badge/Vlad%20Iliushin-informational) ![Ken Webster](https://img.shields.io/badge/Ken%20Webster-informational)

🔗 **Link:** [TCP Fingerprint Firewall / Recon Shield](https://github.com/NikolaiT/zardaxt)  
📝 **Description:** TCP Fingerprint Firewall is a high-performance, eBPF-based network security tool that leverages TCP fingerprinting to detect and block malicious and promiscuous network scanners with high speed and accuracy. This open-source solution combines the power of XDP (eXpress Data Path) for inline packet processing with MuonFP's advanced TCP fingerprinting capabilities, allowing security professionals to identify and block reconnaissance activities before they can map your network infrastructure.
Unlike traditional firewalls that operate on simple port/IP rules, TCP Fingerprint Firewall uses MuonFP-based fingerprints - subtle TCP header characteristics that identify scanning tools like Nmap, ZMap, and Masscan, as well as specific operating systems or device fingerprints.
The innovative pattern matching engine supports wildcards, allowing both precise fingerprint targeting and broader pattern recognition with minimal performance overhead.

</details>

<details><summary><strong>ProcessInjection</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Chirag Savla](https://img.shields.io/badge/Chirag%20Savla-informational)

🔗 **Link:** [ProcessInjection](https://github.com/3xpl01tc0d3r/ProcessInjection)  
📝 **Description:** ProcessInjection is a robust, open-source framework crafted in C# to explore a wide array of process injection techniques, tailored for red teaming, purple teaming, and endpoint security validation. The current version delivers a solid foundation with classic methods such as DLL Injection, traditional shellcode injection, process hollowing, and APC Queue injection, all implemented using C#'s powerful P/Invoke and D/Invoke capabilities for seamless interaction with Windows APIs. It also integrates three evasion techniques—Parent Process ID Spoofing, XOR encryption, and AES encryption—to enhance stealth and flexibility.
Set for a major update at Black Hat USA 2025, ProcessInjection will unveil an advanced suite of techniques, including Process Ghosting, Kernel Callback Table Injection, PE Injection, Thread Execution Hijacking, alongside direct and indirect syscall implementations, and more. This all-encompassing toolkit empowers security professionals to emulate sophisticated adversary behaviors, enabling rigorous testing and fortification of endpoint defenses against modern, evolving threats.

</details>

<details><summary><strong>IronJump</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Andrew Bindner](https://img.shields.io/badge/Andrew%20Bindner-informational)

🔗 **Link:** [IronJump](https://github.com/schlpr0k/IronJump)  
📝 **Description:** IronJump is an automated SSH bastion management system that provides secure, automated, and scalable remote access control in IT, OT, and cloud environments. Built entirely in Bash, IronJump enables rapid deployment of jump hosts, enforces strict authentication policies, and streamlines user and endpoint management through a centralized bastion architecture. Initially designed for security consultants to perform penetration testing remotely, the project can be easily adapted to any task that requires remote management, such as consulting, network-based operations (honeypot, monitoring, taping, troubleshooting), pentesting, architecture assessments, troubleshooting in low-resource or restricted environments, and even everyday IT and OT administration in segregated networks. A simplified command-line GUI navigates administrators of all skill levels through the complexities of bastion management, endpoint deployment, and strict user management. Gain SSH access to a fully configured host in any target environment in as little as 5 minutes. Perfect for drop boxes, Remote Access Terminals (RATs), network monitors, quick remote access, security testing, or troubleshooting.

</details>

<details><summary><strong>Realtic</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sohan Simha Prabhakar](https://img.shields.io/badge/Sohan%20Simha%20Prabhakar-informational) ![Samarth Bhaskar Bhat](https://img.shields.io/badge/Samarth%20Bhaskar%20Bhat-informational) ![Danindu Gammanpilage](https://img.shields.io/badge/Danindu%20Gammanpilage-informational)

🔗 **Link:** [Realtic](https://github.com/Realtek-OpenSource)  
📝 **Description:** Realtic is a flexible cybersecurity tool with a graphical user interface built on top of PyQt. By combining several specialist tools into a single, integrated program, it simplifies cryptographic operations and vulnerability evaluations. The design places a high value on efficiency and simplicity, which makes it perfect for security enthusiasts and professionals who want to perform rapid scans and analysis without having to deal with multiple different command-line tools.

</details>

<details><summary><strong>Windows Fast Forensics With Yamato Security's Hayabusa</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Zach Mathis](https://img.shields.io/badge/Zach%20Mathis-informational) ![Fukusuke Takahashi](https://img.shields.io/badge/Fukusuke%20Takahashi-informational) ![Akira Nishikawa](https://img.shields.io/badge/Akira%20Nishikawa-informational)

🔗 **Link:** [Windows Fast Forensics With Yamato Security's Hayabusa](https://github.com/Yamato-Security/hayabusa)  
📝 **Description:** Hayabusa (隼) is an advanced open-source threat hunting and log analysis tool designed to accelerate Windows event log detection, triage, and investigation. Developed by Yamato Security, Hayabusa empowers defenders by providing a fast, efficient, and extensible approach to parsing, analyzing, and detecting malicious activity within Windows Event Logs (EVTX).

Unlike traditional SIEM-based detection methods, Hayabusa is lightweight, command-line-driven, and optimized for both real-time and forensic analysis. The tool utilizes an extensive library of Sigma-based detection rules to identify threats, ensuring analysts can quickly surface malicious behaviors, persistence mechanisms, lateral movement, and other suspicious activity.

Security teams, forensic investigators, and threat hunters can leverage Hayabusa to process large-scale event log data at high speed, providing deep visibility into endpoint activity without relying on complex log ingestion pipelines. Whether used for incident response, DFIR investigations, or proactive threat hunting, Hayabusa delivers a practical, efficient, and highly adaptable solution for defenders.

Key Features:

- Blazing-fast Windows event log parsing – Processes large EVTX datasets efficiently.
- Sigma rule integration – Detects attacker behavior based on a robust rule set.
- Forensic timeline creation – Extracts key forensic artifacts for investigations.
- Portable and lightweight – CLI-based tool with minimal dependencies.
- Cross-platform support – Runs on Windows, Linux, and macOS.
- JSON & CSV output formats – Easily integrates with existing security workflows.
As a community-driven and actively maintained tool, Hayabusa continues to evolve, offering cutting-edge detections for emerging threats, including APT activity, ransomware, and LOLBins (Living Off the Land Binaries).

Attendees at Black Hat Arsenal will get an exclusive deep dive into Hayabusa's threat hunting capabilities, new features, and real-world use cases for enhancing Windows log-based security investigations.

</details>

<details><summary><strong>Microsoft-Extractor-Suite</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joey Rentenaar](https://img.shields.io/badge/Joey%20Rentenaar-informational)

🔗 **Link:** [Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite)  
📝 **Description:** A PowerShell module for acquisition of data from Microsoft 365 and Azure for Incident Response and Cyber Security purposes.

</details>

<details><summary><strong>vet: Proactive Guardrails against Malicious OSS using Code Analysis</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Abhisek Datta](https://img.shields.io/badge/Abhisek%20Datta-informational)

🔗 **Link:** [vet: Proactive Guardrails against Malicious OSS using Code Analysis](https://github.com/safedep/vet)  
📝 **Description:** vet is a tool for identifying risks in open source software supply chain. It helps security teams setup policy driven guardrails against vulnerable & malicious code from open sources. Using an in-built code analysis engine, vet is able to identify contextual risks arising due to OSS dependencies specific to an application's code base including protection against malicious "code" coming from open source ecosystems.

</details>

<details><summary><strong>Nova Rule: The Prompt Pattern Matching</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Thomas Roccia](https://img.shields.io/badge/Thomas%20Roccia-informational)

🔗 **Link:** [Nova Rule: The Prompt Pattern Matching](https://github.com/fr0gger/nova-framework)  
📝 **Description:** With the widespread adoption of LLMs and Generative AI, individuals and organizations are leveraging these technologies daily, whether for customer support automation, code generation, or business automation. But with increased adoption comes new security risks. The attack surface is expanding, and security teams still lack clear strategies for detecting malicious GenAI activity.

How do you identify threat actor activity in your AI system?
How do you detect malicious prompt usage?
How can threat intelligence teams hunt for adversarial GenAI behavior?

That's where NOVA comes in.

NOVA is an early-stage tool for prompt hunting, designed to detect malicious or policy-violating prompts within GenAI systems. If your organization runs an AI-powered service, you might need a way to monitor, analyze, and detect specific prompt patterns before they lead to abuse, data leaks, or security incidents.

</details>

<details><summary><strong>AutoC</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Itzhak Chimino](https://img.shields.io/badge/Itzhak%20Chimino-informational) ![Bar Haim](https://img.shields.io/badge/Bar%20Haim-informational)

🔗 **Link:** [AutoC](https://github.com/barvhaim/AutoC)  
📝 **Description:** AutoC is an automated tool designed to extract and analyze Indicators of Compromise (IoCs) from open-source threat intelligence sources, providing real-time insights to enhance cybersecurity efforts.

</details>

<details><summary><strong>Timesketch: AI-Powered Super Timeline Analysis</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Diana Kramer](https://img.shields.io/badge/Diana%20Kramer-informational) ![Janosch Köpper](https://img.shields.io/badge/Janosch%20Köpper-informational)

🔗 **Link:** [Timesketch: AI-Powered Super Timeline Analysis](https://github.com/google/timesketch)  
📝 **Description:** Timesketch is a leading free open-source software (licensed under Apache-2.0) for collaborative forensic-timeline analysis, with more than 2.6k stars on GitHub. In this arsenal, we announce and showcase Timesketch AI extension designed to drastically speedup (human) analysts, identify compromise root cause analysis and improve incident reaction time.

The complexity and volume of security data to process in an incident can be overwhelming to analysts. This onslaught of data often leads to investigations with increased risk of errors, delayed effective response to threats, and hindrance of effective remediation.

With this new AI extension, Timesketch is pioneering a new investigation approach, leveraging the latest advancements in reinforcement learning, thinking, and tool use to automatically extract facts and conclusions from vast amounts of unstructured logs. Timesketch reports the AI results respecting the investigation mindset, creating an investigation plan and helping with consistent investigations.

This new Timesketch release goes beyond its novel AI algorithm, it also fundamentally reimagines the UX to optimize for AI and responders collaboration. In particular the new UI view centers the analysis on a series of investigative questions and AI insights. This new workflow empowers analysts to quickly refine and verify the facts highlighted by the AI analysis.

Last but not least, the new Timesketch's API is vendor agnostic and allows practitioners to use any model providers of their choosing.

The demo will showcase how AI driven investigations in Timesketch:
- Autonomously analyzes timelines, creates and answers investigative questions, identifies key events and patterns, and finds the root (or common) cause of various compromise types.
- Provides interactive review, empowering analysts to seamlessly verify, edit, and refine AI-generated findings, ensuring accuracy through clear links to supporting facts and emphasizing the crucial role of human validation.
- Facilitates collaborative timeline analysis by integrating with Timesketch's collaborative environment, where analysts work together on AI-powered investigations.

</details>

<details><summary><strong>DNSForge – Intercept Credentials on Windows Networks</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Apurva Goenka](https://img.shields.io/badge/Apurva%20Goenka-informational)

🔗 **Link:** [DNSForge – Intercept Credentials on Windows Networks](https://github.com/AonCyberLabs/DNSForge)  
📝 **Description:** DNSForge is a network penetration testing tool that introduces a novel tactic to intercept and manipulate name resolution requests made to the authoritative DNS server in an internal network environment. DNSForge achieves interception and reuse of Windows user credentials without any user interaction. While existing poisoning attacks target fallback protocols (such as LLMNR and NBT-NS) or DNS over IPv6, DNSForge employs manipulations on layer 2 to target the primary DNS protocol over IPv4. This enables the tool to bypass current mitigations against existing poisoning attacks as it imitates a legitimate response to name resolutions requests over DNS. Hence, the non-interactive, vulnerable-by-design and seemingly legitimate elements of this attack ensure higher success rates as compared to traditional poisoning attacks.

</details>

<details><summary><strong>YAMAGoya: Userland Threat Hunting Tool for YARA and SIGMA</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational) ![Tomoya Kamei](https://img.shields.io/badge/Tomoya%20Kamei-informational)

🔗 **Link:** [YAMAGoya: Userland Threat Hunting Tool for YARA and SIGMA](https://github.com/JPCERTCC/YAMAGoya)  
📝 **Description:** Traditional endpoint security solutions often rely on proprietary detection engines and kernel-level drivers, posing two major challenges: (1) inability to utilize community-driven YARA and SIGMA signatures directly, and (2) potential OS instability or vulnerabilities introduced by complex kernel drivers. As a result, analysts struggle to utilize YARA/SIGMA rules for memory scanning and behavior-based threat hunting.
YAMAGoya addresses these challenges by providing a userland-centric approach that fully supports YARA and SIGMA, including YARA-based memory scanning, without requiring kernel drivers. It enables detection and correlation over multiple events involving files, processes, registry changes, network connections and PowerShell scripts. Once anomalous behavior is detected, YAMAGoya can terminate offending processes or block suspicious communication, enabling rapid incident containment.
YAMAGoya offers a safer, flexible, and more transparent alternative to traditional kernel-dependent endpoint solutions. This tool can be easily implemented while seamlessly leveraging YARA and SIGMA. This session invites security engineers to experience a userland-only model for hunting evolving threats.

</details>

<details><summary><strong>GDIOCSpider - Extracting and Identifying IOCs from the GDriveverse</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Noah Dunn](https://img.shields.io/badge/Noah%20Dunn-informational)

🔗 **Link:** [GDIOCSpider - Extracting and Identifying IOCs from the GDriveverse](https://github.com/newtnewtnewt/GDIOCSpider)  
📝 **Description:** Google Drive in recent years has become one of the most abused platforms for threat actors to conduct illegal and malicious activity. Threat actors use Google accounts to launch, store, and log malware, effectively turning Drive into a command and control center. On the side of legal and ethical activity, Google Drive remains a popular platform for security researchers to store these artifacts in summarized write-ups and spreadsheets of malicious and illegal activity observed. Much like an archaeologist looks for artifacts providing clues of the history of civilization, security researchers look for Indicators of Compromise (IOCs), which are clues to what a threat actor has done. Security engineers have worked across decades to build out tooling to analyze hard drives and network resources; however, similar advances to analyze Google Drive resources have remained underdeveloped. Along the same line, tools that aggregate and summarize collections of records on IOCs stored in Google Drive by researchers are also lacking.
The GDIOCSpider (Google Drive IOC Spider) provides a tool for both of these use cases. This open-source, configurable, Python tool is capable of crawling through an entire Google Drive, analyzing its file contents, and searching for various defined IOC (Indicators of Compromise) types to extract. This tool outputs a summary of all discovered artifacts across all files, erasing the need for security researchers to manually sift through cloud stores. Supplementing the compromised account use case, the same tool can be used to aggregate IOCs collected in personal or corporate Google Drive accounts in the form of case records gathered by security researchers. This 'environment agnostic' approach is how GDIOCSpider enables security researchers to perform efficient IOC research in Google Drive.

</details>

<details><summary><strong>Volatility 3</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Andrew Case](https://img.shields.io/badge/Andrew%20Case-informational) ![Dave Lassalle](https://img.shields.io/badge/Dave%20Lassalle-informational)

🔗 **Link:** [Volatility 3](https://github.com/volatilityfoundation/volatility3)  
📝 **Description:** Since being announced at Black Hat USA 2007, the open source Volatility Memory Analysis Framework has become the industry standard tool to perform advanced memory forensics in support of incident response, malware analysis, and digital forensics. In Spring 2025, a complete rewrite of the framework, Volatility 3, was officially released as a replacement of the previous framework version. In this Black Hat Arsenal session, attendees will learn about all the new features of the framework, including many new malware detection capabilities as well as API and feature enhancements to support large-scale, modern investigations. The session will also let attendees interact with several of the core developers of the project to facilitate discussion of desired new features and capabilities.

</details>

<details><summary><strong>Luminaut: Casting Light on Shadow Cloud Deployments</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Brittney Argirakis](https://img.shields.io/badge/Brittney%20Argirakis-informational) ![Chapin Bryce](https://img.shields.io/badge/Chapin%20Bryce-informational)

🔗 **Link:** [Luminaut: Casting Light on Shadow Cloud Deployments](https://github.com/luminaut-org/luminaut)  
📝 **Description:** Shadow IT and forgotten proof-of-concept environments frequently become the weak links attackers exploit—unmonitored, undocumented, and outside standard security controls. Whether it's a forgotten cloud instance left open to the internet or a testing environment quietly turned into a production system, these deployments often fly under the radar until they become part of an incident. Once discovered, accurately scoping the environment is critical to identifying existing resources, active services, and their exposure to the internet.
Our open-source tool, Luminaut, scans cloud environments to identify services exposed to the internet, providing critical context from the inside out to jumpstart your investigation. Within minutes, Luminaut will highlight exposed IP addresses and associated compute and networking resources, layering on a timeline from cloud audit logging and context from external scanners. Whether working an incident for an enterprise security team or responding to a customer's AWS or Google Cloud environment, Luminaut helps answer critical scoping questions—what is exposed, where it's running, and how long it has been there—giving investigators a head start on triage, root cause analysis, and informing stakeholders. Arsenal attendees will leave with a free, ready-to-use tool that empowers them to rapidly assess and mitigate cloud exposure in real-world investigations.

</details>

<details><summary><strong>Inlook Email Analysis</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Lucas Betts](https://img.shields.io/badge/Lucas%20Betts-informational)

🔗 **Link:** [Inlook Email Analysis](https://github.com/Lucas-Betts-UoA/Inlook-Email-Analysis)  
📝 **Description:** Inlook is a plugin-based email analysis tool designed to process email with very easy to design and customise functionality. We developed it for the Secret Lab (research team at the University of Auckland School of Computer Science). It allows for flexible and repeatable analysis workflows by sharing a single file (and the tool, of course).

</details>

<details><summary><strong>SmuggleShield - Protection Against HTML Smuggling</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dhiraj Mishra](https://img.shields.io/badge/Dhiraj%20Mishra-informational)

🔗 **Link:** [SmuggleShield - Protection Against HTML Smuggling](https://github.com/RootUp/SmuggleShield)  
📝 **Description:** SmuggleShield is an advanced browser extension for Chrome and Edge that leverages machine learning to safeguard users against HTML smuggling attacks. By utilizing AI-driven models, the tool analyzes incoming web requests and content patterns across URLs in real time, identifying and blocking suspicious files with high precision. This innovative approach ensures adaptive detection of novel attack techniques while minimizing false positives.

The extension supports cross-platform functionality on Windows and macOS and provides detailed logs of blocked content for security audits and forensic analysis. SmuggleShield's blend of machine learning and robust browser integration establishes it as a cutting-edge solution to combat emerging threats in web security.

</details>

<details><summary><strong>Replay security telemetry with Logstory</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dan Dye](https://img.shields.io/badge/Dan%20Dye-informational)

🔗 **Link:** [Replay security telemetry with Logstory](https://github.com/chronicle/logstory)  
📝 **Description:** Logstory is an open-source Python tool that replays security telemetry in various standard formats from numerous vendors. Its primary function is to update timestamps from the various and diverse security log formats, while preserving the temporal relationships between the events. This allows for accurate and repeatable demonstration and testing of security detections and response workflows. The project includes scenarios that have been used internally at Google to exercise Google SecOps. Those scenarios are now published in a cloud storage bucket, so they may be downloaded and replayed with the Logstory utility to any SIEM.

</details>

<details><summary><strong>SigmaOptimizer: LLM-Enhanced Detection Rule Workflow – From Creation to Validation</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Yusuke Nakajima](https://img.shields.io/badge/Yusuke%20Nakajima-informational)

🔗 **Link:** [SigmaOptimizer: LLM-Enhanced Detection Rule Workflow – From Creation to Validation](https://github.com/YusukeJustinNakajima/SigmaOptimizer)  
📝 **Description:** Sigma rules are critical for threat detection, but creating effective rules often involves manual, time-consuming processes and requires a deep understanding of threats. Recently, LLM-based Sigma rule creation from threat report is a hot topic in cybersecurity, offering automation benefits but facing key challenges:

Accuracy and Reliability
- Without real-world log analysis, LLM-generated rules risk hallucination and may not accurately reflect malicious behavior, making them unreliable.

Detection Delay
- Threat reports are typically published some time after an attack occurs, resulting in a delay in detection. This time lag increases the risk of incidents occurring before adequate detection measures can be established.

SigmaOptimizer is a revolutionary tool that automates the entire workflow of Sigma rule generation, validation, and optimization by leveraging real-world logs and LLM. This Arsenal session introduces SigmaOptimizer, highlighting its capabilities in automatically generating robust Sigma rules from actual log data, validating syntax, testing detection effectiveness, and checking false positives. The tool further strengthens detection by supporting command obfuscation, ensuring rules remain resilient against evasion techniques.

SigmaOptimizer also seamlessly integrates with MITRE Caldera, enabling users to effortlessly experiment with various attack techniques. This integration empowers users to quickly generate realistic attack logs and automatically produce corresponding Sigma rules, enhancing threat coverage and reducing manual effort.

Participants will gain insights into effectively automating threat detection processes, significantly enhancing their Threat Hunting, SOC operations, and forensic investigations. Live demonstrations will showcase automated rule generation, obfuscation handling, MITRE Caldera integration, and practical evaluation using SigmaOptimizer's integrated validation framework.

</details>

<details><summary><strong>Detect malicious software packages with GuardDog</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Christophe Tafani-Dereeper](https://img.shields.io/badge/Christophe%20Tafani-Dereeper-informational) ![Andrew Krug](https://img.shields.io/badge/Andrew%20Krug-informational)

🔗 **Link:** [Detect malicious software packages with GuardDog](https://github.com/DataDog/guarddog)  
📝 **Description:** GuardDog is a project to identify malware in npm and PyPI packages. It works by scanning packages source code with Semgrep, looking for known-malicious patterns, and by analyzing package metadata through a heuristics engine.

</details>

<details><summary><strong>Dispatch: Evasive Payload Delivery</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mike Brown](https://img.shields.io/badge/Mike%20Brown-informational)

🔗 **Link:** [Dispatch: Evasive Payload Delivery](https://github.com/m8sec/Dispatch)  
📝 **Description:** Dispatch is an evasive payload delivery server built to enhance stealth and operational security during engagements. It provides an intuitive web UI with dynamic access controls, automatic URL expiration, and flexible file management, ensuring payloads stay secure and accessible only to authorized users. With built-in evasion techniques and adaptable deployment options, Dispatch helps operators maintain covert and controlled payload delivery, reducing exposure to defensive countermeasures.

</details>

---
## ☁️ Cloud Security
<details><summary><strong>OAuthSeeker: Weaponizing OAuth Phishing for Red Team Simulations</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Adam Crosser](https://img.shields.io/badge/Adam%20Crosser-informational)

🔗 **Link:** [OAuthSeeker: Weaponizing OAuth Phishing for Red Team Simulations](https://github.com/praetorian-inc/oauthseeker)  
📝 **Description:** OAuthSeeker is a cutting-edge red team tool designed to simulate OAuth phishing attacks, specifically targeting Microsoft Azure and Office365 users. This tool facilitates the creation, management, and execution of phishing campaigns without requiring advanced technical skills. By leveraging malicious OAuth applications, OAuthSeeker allows offensive security engineers to perform targeted phishing attacks to compromise user identities and gain access to Microsoft Graph API and Azure resources. With features like an administrative control panel, token refresh capabilities, and customizable skins for user-facing components, OAuthSeeker provides an effective solution for testing security defenses against a common but often overlooked attack vector.

The tool is very easy to deploy with only a single pre-compiled Go binary with zero-external dependencies and includes built-in support for LetsEncrypt. The documentation is highly detailed and outlines all the possible attack paths where this capability could be used during real-world red team engagements. The installation process is incredibly streamlined requiring only a single command to deploy a new instance of the application.

</details>

<details><summary><strong>Cloud Offensive Breach and Risk Assessment (COBRA)</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Harsha Koushik](https://img.shields.io/badge/Harsha%20Koushik-informational) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational)

🔗 **Link:** [Cloud Offensive Breach and Risk Assessment (COBRA)](https://github.com/PaloAltoNetworks/cobra-tool)  
📝 **Description:** Cloud Offensive Breach and Risk Assessment (COBRA) is an open-source tool designed to empower users to simulate attacks within multi-cloud environments, providing a comprehensive evaluation of security controls. COBRA automates the testing of various threat vectors, including external and insider threats, lateral movement, and data exfiltration, helping organizations identify security posture weaknesses.

With our latest enhancements, COBRA now extends its capabilities to on-premise attack simulations, enabling organizations to assess hybrid cloud security risks. The tool supports lateral movement from cloud to on-prem, allowing security teams to test cross-environment attack scenarios. Additionally, COBRA introduces EDR evasion and pivoting techniques, helping organizations evaluate their endpoint detection and response effectiveness. These new features further strengthen COBRA's ability to assess an organization's detection and response capabilities across cloud and on-prem infrastructures.

</details>

<details><summary><strong>msInvader: Automating Adversary Simulation in M365 and Azure</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

🔗 **Link:** [msInvader: Automating Adversary Simulation in M365 and Azure](https://github.com/mvelazc0/msInvader)  
📝 **Description:** msInvader is an adversary simulation tool built for blue teams, designed to simulate adversary techniques within M365 and Azure environments. This tool generates attack telemetry, aiding teams in building, testing, and enhancing detection analytics. By implementing multiple authentication mechanisms, including OAuth flows for compromised user scenarios and service principals, msInvader mirrors realistic attack conditions. It interacts with Exchange Online using the Graph API, EWS, and REST API, providing comprehensive simulation capabilities. This session will explore msInvader's technical features, demonstrating its application in improving security defenses through detailed adversary simulations.

</details>

<details><summary><strong>HoneyBee: Misconfigured App Generator</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Yaara Shriki](https://img.shields.io/badge/Yaara%20Shriki-informational) ![Gili Tikochinski](https://img.shields.io/badge/Gili%20Tikochinski-informational)

🔗 **Link:** [HoneyBee: Misconfigured App Generator](https://github.com/yaaras/honeybee)  
📝 **Description:** Ever felt stuck reinventing Dockerfiles or wondering how to secure your cloud-based applications? HoneyBee fixes that by using LLMs to generate misconfigured-by-design Dockerfiles and Docker Compose manifests for popular cloud apps. Think of it as a handy catalog of pitfalls, drawn from real-world cloud scenarios, ready for you to deploy and learn from. HoneyBee makes spinning up realistic honeypots or testing detection rules (like Nuclei) simple and fast, no matter which cloud provider you're on.

At the same time, it's remarkably flexible. Want to add your own misconfigurations or support a lesser-known cloud service? Just drop in a few details, and HoneyBee's prompts will guide you through creating a custom setup. By automating the nitty-gritty of container builds, you can focus on exploring the actual vulnerabilities, fine-tuning your detection logic, and educating your team on cloud security best practices. No more wrestling with complex syntax or half-baked containers - HoneyBee gives you fully working examples tailored to your needs, so you can deepen your security insights without the usual Docker hassle.

</details>

<details><summary><strong>RansomWhen??? I Never Even Noticed It…</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Bleon Proko](https://img.shields.io/badge/Bleon%20Proko-informational)

🔗 **Link:** [RansomWhen??? I Never Even Noticed It…](https://github.com/Permiso-io-tools/RansomWhen)  
📝 **Description:** RansomWhen is an open-source tool from Permiso's P0 Labs that detects AWS KMS-based ransomware TTPs in CloudTrail logs. It identifies abuse of AWS Key Management Service features that attackers can leverage to encrypt S3 bucket data as part of ransomware operations, and enumerates identities possessing privilege combinations corresponding to these attack techniques.

</details>

<details><summary><strong>CloudLens</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Gaurav Joshi](https://img.shields.io/badge/Gaurav%20Joshi-informational) ![Hare Krishna Rai](https://img.shields.io/badge/Hare%20Krishna%20Rai-informational) ![Malkit Singh](https://img.shields.io/badge/Malkit%20Singh-informational)

🔗 **Link:** [CloudLens](https://github.com/one2nc/cloudlens)  
📝 **Description:** CloudLens is a powerful, open-source tool designed for Red Teamers, penetration testers, and security professionals seeking deep visibility into AWS cloud workloads. Designed to uncover active services across multiple regions—such as EC2, S3, IAM, CloudTrail, RDS, Lambda, KMS, Config, and GuardDuty—it operates securely with minimal permissions, requiring only read-only AWS keys. Built using Node.js, React, and the AWS SDK for JavaScript, CloudLens aggregates complex workload data into a clear, region-wise dashboard, empowering offensive security teams, enabling them to map cloud attack surfaces efficiently.

</details>

<details><summary><strong>Cloud Log Fast Forensics with Yamato Security's Suzaku</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Zach Mathis](https://img.shields.io/badge/Zach%20Mathis-informational) ![Fukusuke Takahashi](https://img.shields.io/badge/Fukusuke%20Takahashi-informational) ![Akira Nishikawa](https://img.shields.io/badge/Akira%20Nishikawa-informational)

🔗 **Link:** [Cloud Log Fast Forensics with Yamato Security's Suzaku](https://github.com/Yamato-Security/suzaku)  
📝 **Description:** Suzaku (朱雀) is an open-source cloud threat hunting and log analysis tool designed to enhance AWS and Azure security investigations. Developed by Yamato Security, Suzaku brings blazing-fast detection, forensics, and triage capabilities to cloud environments, helping security teams uncover malicious activity, misconfigurations, and threats within cloud logs.

Inspired by the success of Hayabusa for Windows Event Logs, Suzaku applies the same powerful threat detection approach to cloud environments, leveraging Sigma-based rules to detect attacker techniques in AWS and Azure logs. Suzaku helps defenders quickly process massive cloud log datasets, enabling quick detection and forensic analysis for incident response and proactive threat hunting.

Key Features:

- Multi-cloud support – Works with AWS and Azure logs.
- High-speed log processing – Parses large-scale cloud logs efficiently, reducing detection time.
- Sigma rule integration – Uses community-driven and custom detection rules for cloud-specific attack techniques.
- Forensic timeline generation – Maps attacker actions for incident response and DFIR investigations.
- Lightweight and extensible – CLI-based, with JSON and CSV output for easy integration into SIEMs and SOAR tools.
- Detection of cloud-specific threats – Identifies misconfigurations, privilege escalations, API abuses, persistence mechanisms, and unusual user activity.

As cloud threats continue to evolve, Suzaku provides security teams with a flexible, scalable, and powerful tool for detecting compromised cloud accounts, adversary tactics (MITRE ATT&CK for Cloud), and suspicious API calls.

Attendees at Black Hat Arsenal will get an in-depth look at Suzaku's cloud security capabilities, including real-world case studies, live threat detection demonstrations, and new features for cloud-native investigations.

</details>

<details><summary><strong>Halberd : Multi-Cloud Agentic Attack Tool</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Arpan Abani Sarkar](https://img.shields.io/badge/Arpan%20Abani%20Sarkar-informational)

🔗 **Link:** [Halberd : Multi-Cloud Agentic Attack Tool](https://github.com/vectra-ai-research/Halberd)  
📝 **Description:** Halberd is a comprehensive security testing tool designed for attack emulation across AWS, Azure, Microsoft 365, Entra ID, and GCP environments. The latest release introduces the "Halberd Attack Agent", an advanced LLM-driven orchestration layer that enables programmatic execution of complex attack chains through natural language interfaces. Halberd implements a complete attack lifecycle—from initial reconnaissance to persistence - via 100+ MITRE ATT&CK-aligned techniques.
Designed to democratize security testing, Halberd's intuitive web interface eliminates technical barriers, enabling teams of all skill levels to simulate sophisticated adversary techniques with unprecedented ease.

</details>

<details><summary><strong>Spotter – Universal Kubernetes Security Scanner & Policy Enforcer</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Madhu Akula](https://img.shields.io/badge/Madhu%20Akula-informational)

🔗 **Link:** [Spotter – Universal Kubernetes Security Scanner & Policy Enforcer](https://github.com/spotter-application/spotter)  
📝 **Description:** Spotter is a groundbreaking open-source tool or solution designed to secure Kubernetes clusters throughout their lifecycle. Built on the native tooling of Kubernetes by leveraging CEL (Common Expression Language) for policy definitions, we can define unified security scanning across development, CLI, CI/CD, Admission Controllers, deployments, runtime, and continuous monitoring. Its unique approach enables both enforcement and monitoring modes, ensuring that policies can be applied consistently and mapped directly to industry standards such as CIS, MITRE ATT&CK, etc.

Spotter provides extreamly high flexbility across all Kubernetes phases, providing an innovative approach that no other open-source or commercial solution can replicate. It seamlessly bridges security, DevOps, and platform teams, effectively solving the real-world challenges faced by day-to-day operations.

</details>

<details><summary><strong>AWS CloudTrail Navigator</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![David Cowen](https://img.shields.io/badge/David%20Cowen-informational) ![Evan Anderson](https://img.shields.io/badge/Evan%20Anderson-informational)

🔗 **Link:** [AWS CloudTrail Navigator](https://github.com/aws/aws-cloudtrail-processing-library)  
📝 **Description:** The CloudTrail Log Explorer is a Python-based GUI application designed to simplify the process of discovering, downloading, and managing AWS CloudTrail logs. It provides an intuitive graphical interface built with Tkinter, allowing users to easily authenticate with AWS, assume roles, and transfer logs from S3 buckets.
Features

AWS Authentication: Supports authentication via AWS profiles or direct API keys.
Role Management: Automatically detects and assumes AWS IAM roles, preventing redundant role assumptions.
Log Discovery: Scans and identifies CloudTrail logs within specified date ranges.
Log Transfer: Efficiently downloads CloudTrail logs from S3 buckets using multiprocessing.
Resume Capability: Allows resuming interrupted transfers without rescanning the entire bucket.
Error Logging and Tracking: Comprehensive logging of errors and failed transfers, with detailed reports.
User-Friendly GUI: Real-time progress updates, error notifications, and easy access to logs.

</details>

<details><summary><strong>DetentionDodger: Finding rusted links on the chains of fate</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Bleon Proko](https://img.shields.io/badge/Bleon%20Proko-informational)

🔗 **Link:** [DetentionDodger: Finding rusted links on the chains of fate](https://github.com/permiso-io-tools/detentiondodger)  
📝 **Description:** DetentionDodger is a tool that automates enumeration of AWS accounts for IAM users with leaked credentials. It analyzes users under the AWSCompromisedKeyQuarantineV2 policy, determines their effective privileges, and assesses the potential impact of compromised credentials on the account.

</details>

<details><summary><strong>Generate datasets for common cloud attacks with Grimoire</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Christophe Tafani-Dereeper](https://img.shields.io/badge/Christophe%20Tafani-Dereeper-informational) ![Andrew Krug](https://img.shields.io/badge/Andrew%20Krug-informational)

🔗 **Link:** [Generate datasets for common cloud attacks with Grimoire](https://github.com/DataDog/grimoire)  
📝 **Description:** Grimoire is a "REPL for detection engineering" that allows you to generate datasets of cloud audit logs for common attack techniques. It currently supports AWS.

</details>

<details><summary><strong>Kubernetes Security Scanner</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Krishna Priya](https://img.shields.io/badge/Krishna%20Priya-informational)

🔗 **Link:** [Kubernetes Security Scanner](https://github.com/farhanashrafdev/GenAI-Kubernetes-Security-Scanner)  
📝 **Description:** This is a comprehensive security scanning tool for Kubernetes clusters that identifies security issues, misconfigurations, and potential vulnerabilities. I built this tool while i was studying for CKS and i have found it really useful for real world workloads. It has the following features.

1 . Cluster Setup and Hardening
Locks down the foundation: CIS‑aligned configs, safe admission plugs, tight RBAC, and restrictive network policies.

CIS Benchmark Checker – drift & remediation

Admission Controller Checker – PSP/PSA, webhooks

RBAC Checker – wild‑card verbs, risky bindings

Network Policy Checker – open namespaces, default‑allow rules

2 . System Hardening
Fortifies nodes and runtimes—kernel params, kubelet flags, containerd/Docker, and gVisor isolation.

Node Security Checker – OS & kubelet hygiene

Runtime Security Checker – seccomp, AppArmor, privilege creep

gVisor Checker – runtime‑class wiring, sandbox health

3 . Minimize Microservice Vulnerabilities
Applies least‑privilege to pods: security contexts, resource limits, PDBs, and secrets hygiene.

Container Security Checker – capabilities, limits, image trust

Pod Security Checker – priority/QoS, disruption budgets

Secrets Management Checker – encryption, rotation, exposure

4 . Supply Chain Security
Admits only trusted code via image signatures, SBOM validation, and CVE detection.

Image Security Checker – signatures, vuln scan, registry posture

SBOM Checker – dependency CVEs, license red flags

5 . Runtime Security
Maintains live visibility with audit pipelines and Falco rules for instant threat detection.

Audit Checker – policy coverage, backend integrity

Falco Checker – rule quality, alert wiring, violation monitoring

</details>

<details><summary><strong>AzDevRecon - Azure DevOps Enumeration Tool</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Raunak Parmar](https://img.shields.io/badge/Raunak%20Parmar-informational)

🔗 **Link:** [AzDevRecon - Azure DevOps Enumeration Tool](https://github.com/TROUBLE-1/AzDevRecon)  
📝 **Description:** AzDevRecon is a web-based enumeration tool designed for offensive security professionals, red teamers, and penetration testers to assess Azure DevOps security. It enables security teams to uncover misconfigurations, exposed secrets, and security gaps by leveraging Personal Access Tokens (PATs) and Access Tokens (with aud=499b84ac-1321-427f-aa17-267ca6975798, including those obtained via Managed Identity).

This tool allows testers to enumerate projects, repositories, pipelines, builds, and user permissions, providing critical insights into potential attack vectors. With a user-friendly web interface, AzDevRecon streamlines the reconnaissance process, enabling efficient identification of security flaws such as hardcoded credentials, privilege escalation paths, and misconfigured access controls.

By utilizing AzDevRecon, penetration testers can efficiently enumerate Azure DevOps environments even in scenarios where a GUI is not available.

</details>

<details><summary><strong>Nebula: a modular and efficient open-source multi-cloud offensive toolkit</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Elgin Lee](https://img.shields.io/badge/Elgin%20Lee-informational) ![Tanishq Rupaal](https://img.shields.io/badge/Tanishq%20Rupaal-informational) ![Zach Grace](https://img.shields.io/badge/Zach%20Grace-informational) ![Hengrui Wang](https://img.shields.io/badge/Hengrui%20Wang-informational) ![Andrew Chang](https://img.shields.io/badge/Andrew%20Chang-informational)

🔗 **Link:** [Nebula: a modular and efficient open-source multi-cloud offensive toolkit](https://github.com/slackhq/nebula)  
📝 **Description:** Nebula is a multi-cloud offensive security testing toolkit that enables security engineers to efficiently identify vulnerabilities and misconfigurations across AWS, Azure, and GCP environments. While existing cloud security tools focus on single providers or specific use cases, Nebula provides a unified framework for conducting comprehensive security assessments across multiple cloud providers and accounts simultaneously.

The framework offers specialized reconnaissance, analysis, and exploitation modules, allowing security engineers to enumerate resources across regions, detect public-facing assets, and discover exposed secrets. Its intelligent API handling and concurrent processing capabilities make it particularly effective for large-scale cloud security assessments that would be time-consuming or impractical with existing tools.

Nebula is built in Go with a modular architecture inspired by the Metasploit Framework, which emphasizes extensibility and code reuse. Security engineers can quickly develop custom modules to test new cloud services or implement novel attack techniques. The framework's composable pipeline pattern enables efficient concurrent execution of complex security assessments while abstracting away cloud API interaction and data processing challenges.
Key features include automatic multi-region enumeration, specialized scanners for public resources, integrated secret detection via Nosey Parker, and a simplified interface for cloud API interactions. Whether conducting routine security assessments or responding to incidents, Nebula provides the flexibility and performance needed for modern cloud security testing.

The toolkit has been field-tested in real-world engagements, where it has successfully identified critical attack paths including privilege escalation opportunities, exposed secrets, and publicly accessible resources that evaded detection by traditional cloud security solutions.

Key Capabilities:

1. Multi-Cloud Support: Unified interfaces for AWS, Azure, and GCP with provider-specific optimizations
2. Comprehensive Resource Enumeration: Concurrent scanning across multiple regions and resource types to provide a comprehensive summary of resources in an environment
3. Public Asset Detection: Specialized scanners for identifying publicly accessible cloud resources that create potential entry points
4. Secret Detection: Integration with Nosey Parker for identification of unprotected secrets in cloud environment
5. IAM Analysis: Advanced permission assessment to identify privilege escalation paths and excessive permissions
6. Service-Specific Security Checks: Targeted assessment modules for high-risk services (EC2, Azure VMs, S3, Azure Key Vaults, Lambda, etc.)
7. Efficient Parallel Processing: Composable pipeline pattern that automatically enables high-performance scanning
8. Extensible Output: Supports multiple output formats including JSON, Markdown tables, and console output

</details>

<details><summary><strong>Peirates</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Jay Beale](https://img.shields.io/badge/Jay%20Beale-informational)

🔗 **Link:** [Peirates](https://github.com/inguardians/peirates)  
📝 **Description:** Peirates is a penetration testing tool for Kubernetes, focused on privilege escalation and lateral movement. It has an interactive interface, wherein the penetration tester chooses actions from the techniques that Peirates encodes. Some of the techniques in Peirates will give you administrative access to the cluster in one-shot. Others are intended to get you tokens for an increasing number of service accounts that you can use to move laterally, steal secrets, and chain together to achieve the goals of your penetration test.

</details>

<details><summary><strong>SquarePhish 2.0 - Turning QRCodes into Single Sign On Primary Refresh Tokens</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Nevada Romsdahl](https://img.shields.io/badge/Nevada%20Romsdahl-informational) ![Kam Talebzadeh](https://img.shields.io/badge/Kam%20Talebzadeh-informational)

🔗 **Link:** [SquarePhish 2.0 - Turning QRCodes into Single Sign On Primary Refresh Tokens](https://github.com/nromsdahl/squarephish2)  
📝 **Description:** SquarePhish is an advanced phishing tool that uses a technique combining the OAuth 2.0 Device Code Authentication Flow and QR codes. Version 2.0 of the tool introduces phishing for Primary Refresh Tokens, Microsoft's Single Sign-On token. This token gives attackers broad access to Microsoft cloud resources.
In the demo, we will cover QR codes, Device Code OAuth 2.0 Flow, FOCI tokens, Primary Refresh Tokens, and putting it all together for advanced phishing attacks. The intent of our tool is to give red teamers and organizations a way to test detection and prevention capabilities.

</details>

<details><summary><strong>Emulate cloud-native attacks with Stratus Red Team</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: ☁️ Cloud Security](https://img.shields.io/badge/Category:%20☁️%20Cloud%20Security-blue) ![Christophe Tafani-Dereeper](https://img.shields.io/badge/Christophe%20Tafani-Dereeper-informational) ![Andrew Krug](https://img.shields.io/badge/Andrew%20Krug-informational)

🔗 **Link:** [Emulate cloud-native attacks with Stratus Red Team](https://github.com/DataDog/stratus-red-team)  
📝 **Description:** What attacks are used by threat actors in cloud environments? How to reproduce them easily to ensure that our threat detection mechanisms are working as expected?

Stratus Red Team provides a solution to these two questions. With support for AWS, Azure, Google Cloud, Entra ID Kubernetes, it allows threat detection and cloud security engineering team to reproduce common cloud attacks in a self-contained manner, along with actionable detection insights.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Effective Security Code Reviews in Visual Studio - Introducing Static Analysis Hero (SAH)</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational) ![Dustin Born](https://img.shields.io/badge/Dustin%20Born-informational)

🔗 **Link:** [Effective Security Code Reviews in Visual Studio - Introducing Static Analysis Hero (SAH)](https://github.com/usdAG/sah)  
📝 **Description:** Static Analysis Hero (SAH) is an extension to Visual Studio Code dedicated to identifying software vulnerabilities and enhancing static source code analysis. Its main features fall into two categories: 1. code scanning (identify vulnerabilities) and 2. integrated documentation (managing vulnerabilities).
Code scanning for vulnerable patterns and potential security vulnerabilities is based on semgrep/opengrep as well as built-in regular expressions. Semgrep scans can be started from the tool directly using all available (or custom) rulesets. Results are automatically imported into SAH. Furthermore, SAH includes pre-defined regex rulesets for multiple languages and frameworks – but can also easily be extended with custom rulesets for specific project requirements.
For documentation of findings (either identified by code scanning or manual analysis), SAH allows commenting, bookmarking, prioritization and exporting/importing of findings. The documentation features are intended to enable a more streamlined process during code reviews, as analysts do not have to switch between different tools for performing the analysis and documentation of results. Finally, the state of a project can be exported for collaboration, e.g. to share the current state of a project with your team members.
Overall, the functionality of SAH integrates perfectly with the power of VS Code as an IDE – which is essential for efficient navigation in large code bases. It also integrates nicely with other plugins such as linting and programming language specific extensions. SAH is fully open-source and does not require an internet connection or user account.

SAH is intended to be used by developers and security professionals alike, who seek to identify software vulnerabilities in source code and follow-up on them in a structured manner. More specifically, we use SAH during code reviews for our clients, but also during penetration tests on web applications, APIs, desktop applications and the like whenever we get access to source code.

</details>

<details><summary><strong>Revealing 2MS: Secrets Detection and the Developer's Role in Supply Chain Security</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ori Ron](https://img.shields.io/badge/Ori%20Ron-informational) ![Tal Folkman](https://img.shields.io/badge/Tal%20Folkman-informational)

🔗 **Link:** [Revealing 2MS: Secrets Detection and the Developer's Role in Supply Chain Security](https://github.com/Checkmarx/2ms)  
📝 **Description:** Secrets belong in vaults, not in source code. Too Many Secrets (2MS) is a fast and reliable open-source CLI tool to help security teams and developers detect and remediate exposed secrets before they lead to security breaches. With support for scanning internal communication platforms, content management systems, and code repositories, 2MS proactively prevents credential leaks and strengthens security posture.

</details>

<details><summary><strong>Surfactant - Modular Framework for File Information Extraction and SBOM Generation</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational)

🔗 **Link:** [Surfactant - Modular Framework for File Information Extraction and SBOM Generation](https://github.com/llnl/Surfactant)  
📝 **Description:** Surfactant is a modular framework for extracting file information from filesystems and generating Software Bills of Materials (SBOMs). It identifies vendors and libraries associated with files, establishes relationships between software components, and supports system-level vulnerability impact analysis for IoT, Smart Grid, and ICS devices. Features include a terminal UI, archive decompression, interactive relationship visualizations, and package identification without a package manager.

</details>

<details><summary><strong>DAPper - Identifying Software Packages and Uncovering Implicit Dependencies</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ryan Mast](https://img.shields.io/badge/Ryan%20Mast-informational) ![Micaela Gallegos](https://img.shields.io/badge/Micaela%20Gallegos-informational)

🔗 **Link:** [DAPper - Identifying Software Packages and Uncovering Implicit Dependencies](https://github.com/LLNL/dapper)  
📝 **Description:** DAPper (Dependency Analysis Project) is an open-source tool to uncover software dependencies – both explicit and implicit – by analyzing source code and system-level data. Unlike most dependency analysis tools that rely on package managers, DAPper identifies dependencies in C/C++ codebases, which typically lack a standardized package registry. It also detects subprocess execution in source code across multiple languages, revealing hidden dependencies that might otherwise go unnoticed.
These features in DAPper are powered by a set of datasets mapping file names to packages across ecosystems like Debian/Ubuntu, NuGet (Windows/.NET), PyPI, and Docker Hub. These datasets, along with tools for generating them, are released as open source, enabling broader use for software inventory analysis/system enumeration, vulnerability impact assessments, and system audits. These datasets can be particularly useful for recognizing packages on systems that lack package manager metadata, such embedded Linux systems or Windows support software used to monitor/manage/configure devices.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>ROP ROCKET: Advanced Framework for Return-Oriented Programming</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational) ![Shiva Kusuma](https://img.shields.io/badge/Shiva%20Kusuma-informational)

🔗 **Link:** [ROP ROCKET: Advanced Framework for Return-Oriented Programming](https://github.com/Bw3ll/ROP_ROCKET)  
📝 **Description:** ROP ROCKET is a groundbreaking, next-generation tool for Return-Oriented Programming (ROP), boasting unparalleled capabilities. This tool introduces several innovative techniques, including a novel approach to invoking Heaven's Gate via ROP, which facilitates the transition from x86 to x64 architecture, and invoking Windows syscalls via ROP to evade Data Execution Prevention (DEP), eliminating the need for less stealthy Windows API functions.

The focal point of this tool is automatic ROP chain generation—constructing complete ROP exploits. Moreover, with this tool, we pioneer several new ROP techniques, including both x86 and x64 Heaven's Gate and using Windows syscalls to bypass DEP. To overcome DEP, we automate chain generation for Windows syscalls NtAllocateVirtualMemory and NtProtectVirtualMemory. In addition, ROP ROCKET can avoid the need to bypass DEP by chaining multiple APIs together to achieve shellcode-like functionality.

For Black Hat Arsenal 2025, we will unveil support for building ROP chains for many new WinAPIs: WinExec, DeleteFileA, CreateToolhelp32Snapshot, URLDownloadToFileA, OpenProcess, Process32First, Process32Next, RegSetKeyValueA, RegCreateKeyA, WriteProcessMemory, HeapCreate, OpenSCManagerA, CreateServiceA, ShellExecuteA, CreateRemoteThread, VirtualAllocEx, TerminateProcess, and CreateProcessA. All will be available via automatic ROP chain construction using patterns with PUSHAD or a combination of PUSHAD coupled with mov dereferences, or the sniper approach.

One of the features of ROP ROCKET is the sheer diversity of possibilities in creating these chains, allowing unique and unusual combinations that traditionally might not be achievable by ROP chain automation. The tool uses extensive emulation to evaluate the fitness of individual ROP gadgets, allowing unusual or longer ROP gadgets to be used. It also builds, emulates, and debugs parts of some ROP chains internally to solve certain problems, allowing for ROP chains to be built with the mov dereference or sniper approach, rather than relying simply on the PUSHAD approach. Distances to certain function parameters can also be dynamically calculated and readjusted with emulation.

Sometimes a ROP chain is feasible only if a ROP gadget's address is free of bad bytes. With ROP ROCKET, we provide a way to obfuscate gadgets, allowing the gadget address to be pushed onto the stack, decoded, and executed at runtime.

ROP ROCKET is built for performance, utilizing multiprocessing to harness a dozen or more cores. It also stores discovered gadgets from previously examined binaries, giving persistence across sessions. With all possible ROP gadgets—our raw ingredients—identified, ROP chains can be formed in seconds.

While ROP can be a complex topic, ROP ROCKET provides powerful capabilities to users. New for Black Hat Arsenal 2025, the tool will support over 100 patterns for different WinAPIs or syscalls, far exceeding the capabilities of other ROP generation tools.

</details>

<details><summary><strong>Automating Red Team Operations in Windows AD with Local LLM and Multi AI Agents</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yu Terada](https://img.shields.io/badge/Yu%20Terada-informational)

🔗 **Link:** [Automating Red Team Operations in Windows AD with Local LLM and Multi AI Agents](https://github.com/ErdemOzgen/RedAiRange)  
📝 **Description:** Modern Red Team assessments in Windows Active Directory (AD) environments often involve navigating a vast array of machines, accounts, making them highly resource-intensive. To streamline these engagements, I developed a prototype automated penetration testing tool that leverages local Large Language Models (LLMs) and specialized AI Agents. Because AD environments often contain large amounts of confidential data, this solution can operate entirely within a closed environment, mitigating the risk of data leakage. I verified that the system runs effectively on a single PC.

A fundamental challenge with local LLMs is that they often lack sufficient domain-specific knowledge, particularly with regard to attacker tools and methodologies. I address this limitation by restricting the set of utilized tools (e.g., Mimikatz, Psexec, PowerView) and designing specialized Agents for each. I also enhance the models' reasoning with Retrieval-Augmented Generation (RAG) pipelines that focus on typical AD attack paths. Each Agent is based on the ReAct model and logs its thought process and executed commands to visualize the flow of reasoning.

Beyond the immediate goal of reducing the effort required for Red Team operations, this research also examines a future threat vector. I anticipate that adversaries will soon embed local LLMs into malware, enabling offline attacks on isolated machines—such as web-isolated hosts or local networks. These attacks do not generate network traffic, thereby evading detection by security appliances that monitor outbound traffic. To evaluate the potential efficacy of local AI-driven automation—given that most Windows devices are equipped only with a CPU—this tool will be tested using a model that runs on the CPU.

</details>

<details><summary><strong>OffensiveSwift</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Hare Sudhan Muthusamy](https://img.shields.io/badge/Hare%20Sudhan%20Muthusamy-informational)

🔗 **Link:** [OffensiveSwift](https://github.com/Teach2Breach/offensiveswift)  
📝 **Description:** Red teamers often rely on command-line tools for macOS testing, making them highly detectable by endpoint security solutions. OffensiveSwift is a modern offensive framework built entirely in Swift, offering a native approach to macOS adversary emulation. It leverages Swift's direct access to macOS APIs—without invoking traditional shell commands—to minimize observable traces and lower its detection footprint.

Highlights:

- Standalone Binary: Compiles directly into a standalone binary with no external dependencies.
- Reduced Detections: Uses macOS APIs for a more stealthy and efficient operation.
- Flexible TTP Chaining: Provides programmatic interfaces that seamlessly chain TTPs into complex adversary simulations.
- Modular Design: Supports both individual technique testing and the creation of full emulation campaigns.

</details>

<details><summary><strong>Introducing RAVEN - Discovering and Analyzing CI/CD Vulnerabilities in Scale</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Elad Pticha](https://img.shields.io/badge/Elad%20Pticha-informational) ![Alex Ilgayev](https://img.shields.io/badge/Alex%20Ilgayev-informational)

🔗 **Link:** [Introducing RAVEN - Discovering and Analyzing CI/CD Vulnerabilities in Scale](https://github.com/CycodeLabs/raven)  
📝 **Description:** As the adoption of CI/CD practices continues to grow, securing these pipelines has become increasingly important. However, identifying vulnerabilities in CI/CD pipelines can be daunting, especially at scale. In this talk, we present our tooling, which we have released as open-source software, enabling us to uncover hundreds of vulnerabilities in the CI/CD pipelines of popular open-source projects.

RAVEN (Risk Analysis and Vulnerability Enumeration for CI/CD) is a powerful security tool designed to perform massive scans for GitHub Actions CI workflows and digest the discovered data into a Neo4j database. With RAVEN, we were able to identify and address potential security vulnerabilities in some of the most popular repositories hosted on GitHub, including FreeCodeCamp, Fluent UI by Microsoft, Bazel by Google, and much more.
This tool provides a reliable and scalable solution for security analysis, enabling users to query the database and gain insights about their codebase's security posture.

</details>

<details><summary><strong>Tengu Marauder: Combining Robotics and Cybersecurity</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Alex Thach](https://img.shields.io/badge/Alex%20Thach-informational)

🔗 **Link:** [Tengu Marauder: Combining Robotics and Cybersecurity](https://github.com/Lexicon121/Tengu-Marauder)  
📝 **Description:** The Tengu Marauder, derived from a previous security drone project, is a portable wheeled robot equipped with an ESP32 Marauder, currently in its testing phase. Designed for simplicity and efficiency, the Tengu Marauder serves as an alternative and interactive tool for WiFi network security testing. Its capabilities include WiFi scanning, deauthentication attacks, packet sniffing, and other wireless security tests. The compact design ensures ease of construction and maintenance using readily available parts and straightforward code integration. Essentially an advanced RC robot, the Tengu Marauder operates headless via XBee, providing a fun and engaging platform for testing the security of network-controlled devices over WiFi, such as IoT smart home devices and smaller WiFi-controlled drones like the Ryze Tello. This project would not have been possible without the support of local Philadelphia security organizations and the overall security community.

</details>

<details><summary><strong>MORF – Mobile Reconnaissance Framework</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Amrudesh Balakrishnan](https://img.shields.io/badge/Amrudesh%20Balakrishnan-informational) ![Himanshu Kumar Das](https://img.shields.io/badge/Himanshu%20Kumar%20Das-informational) ![Abhishek JM](https://img.shields.io/badge/Abhishek%20JM-informational)

🔗 **Link:** [MORF – Mobile Reconnaissance Framework](https://github.com/amrudesh1/MORF)  
📝 **Description:** MORF is a versatile, lightweight, and platform-independent offensive mobile security tool that aids security professionals and developers in detecting sensitive information within mobile applications. Often referred to as a "Swiss army knife" for mobile app security, MORF utilizes heuristics-based methods to quickly discover keys, secrets, and other crucial data. Its extensible plugin framework accommodates custom rules and integrations, making it adaptable to specific projects or organizational needs for both Android and iOS environments.

</details>

<details><summary><strong>SCCMHunter</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Garrett Foster](https://img.shields.io/badge/Garrett%20Foster-informational)

🔗 **Link:** [SCCMHunter](https://github.com/garrettfoster13/sccmhunter)  
📝 **Description:** SCCMHunter is a post-exploitation tool built to streamline identifying, profiling, and attacking SCCM related assets in an Active Directory domain.

In this update, SCCMHunter has received additions to the recon module for site system profiling, the admin module has been extended for more post-exploitation commands, and a new relay module has been built for credential relaying.

The presentation will include a walkthrough of the tool and it's various modules and a demonstrations of how to use the modules for SCCM hierarchy takeover

</details>

<details><summary><strong>Sickle - Payload Development Framework</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Milton Valencia](https://img.shields.io/badge/Milton%20Valencia-informational)

🔗 **Link:** [Sickle - Payload Development Framework](https://github.com/wetw0rk/sickle-pdk)  
📝 **Description:** This presentation explores Sickle, a modular and extensible payload development framework designed for offensive security professionals and red teamers. Sickle enhances exploit development by providing a structured approach to crafting highly sophisticated payloads for the modern landscape.

Attendees will gain insight into Sickle's dynamic payload generation and multi-stage execution capabilities. The talk will cover key features such as customizable shellcode, and integration with existing exploitation frameworks.

A live demonstration will showcase how Sickle can be used to generate and deploy payloads tailored to specific target environments, emphasizing its adaptability in real-world engagements.

By the end of the session, participants will understand how to leverage Sickle to craft advanced payloads while adhering to ethical and legal considerations in penetration testing and red teaming.

</details>

<details><summary><strong>Warhead: Stealthy Payload Execution via Atom Tables</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Vishal Thakur](https://img.shields.io/badge/Vishal%20Thakur-informational) ![John Lopes](https://img.shields.io/badge/John%20Lopes-informational)

🔗 **Link:** [Warhead: Stealthy Payload Execution via Atom Tables](https://github.com/malienist/warhead)  
📝 **Description:** Warhead is an offensive security tool that leverages Windows Atom Tables to store, retrieve, and execute payloads in a stealthy manner. This technique enables adversaries to place a payload in the Atom Table, use a legitimate process to extract it, and execute it in memory—bypassing traditional detection mechanisms. The first version of Warhead, to be released at Black Hat Arsenal 2025, provides security researchers and red teamers with a novel approach to payload delivery and execution that evades modern security defenses.

</details>

<details><summary><strong>Utilizing Native Messaging API for Covert Command and Control (C3)</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Efstratios Chatzoglou](https://img.shields.io/badge/Efstratios%20Chatzoglou-informational)

🔗 **Link:** [Utilizing Native Messaging API for Covert Command and Control (C3)](https://github.com/efchatz/Covert-C2)  
📝 **Description:** Covert C2 is an advanced command and control framework that leverages the browser Native Messaging API alongside lightweight evasion techniques to establish covert communications. It uses a decentralized infrastructure where compromised machines autonomously connect to the C2 server, supports post-exploitation and lateral movement operations, and achieves near-zero detection rates against modern EDR solutions.

</details>

<details><summary><strong>Java Chains: Make Java Vulnerability Exploit brilliant again</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Xiaohang Zhang](https://img.shields.io/badge/Xiaohang%20Zhang-informational) ![Qiyuan Li](https://img.shields.io/badge/Qiyuan%20Li-informational)

🔗 **Link:** [Java Chains: Make Java Vulnerability Exploit brilliant again](https://github.com/vulhub/java-chains)  
📝 **Description:** This tool focuses on the Java security domain, dedicated to providing comprehensive Java vulnerability payload generation and exploitation capabilities. It supports practical utilization in various real-world scenarios, covering payload generation for common vulnerabilities like Java deserialization and Hessian deserialization, as well as exploitation of vulnerabilities such as JNDI injection and RMI deserialization.

</details>

<details><summary><strong>RedInfraCraft : Automate Complex Red Team Infra</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yash Bharadwaj](https://img.shields.io/badge/Yash%20Bharadwaj-informational) ![Manish Gupta](https://img.shields.io/badge/Manish%20Gupta-informational)

🔗 **Link:** [RedInfraCraft : Automate Complex Red Team Infra](https://github.com/redteamoperations/red-infra-craft)  
📝 **Description:** RedInfraCraft is a powerful FOSS solution for automating the deployment of powerful red team infrastructures. It streamlines the setup and management of :

- Individual Red Team Components (C2, Payload, Redirector Server etc.)
- On-premise / Cloud services re-director support
- Complete Red Team Infrastructure (Redirector Load Balancer C2, Payload server, phishing server etc)
- Phishing Operations
- Infrastructure deployment support in AWS, Azure & GCP Cloud including multi-cloud support.

Dilute your time to setup Red Team Infrastructure in 5 minutes with RedInfraCraft

</details>

<details><summary><strong>SAMLSmith</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Eric Woodruff](https://img.shields.io/badge/Eric%20Woodruff-informational) ![Tomer Nahum](https://img.shields.io/badge/Tomer%20Nahum-informational)

🔗 **Link:** [SAMLSmith](https://github.com/Semperis/SAMLSmith)  
📝 **Description:** SAMLSmith is the go-to tool for penetrating SAML applications with response forging. An evolution of the original tooling developed for proof-of-concept of SAML response forging in Entra ID, SAMLSmith takes further research around SAML response forging and combines it into a tool crafted for offensive scenarios.

While far from new, enterprises continue to not prioritize the security of how SaaS applications integrate or understand best practices for securing them. With many factors at play, SAML response forging can range from extremely difficult to near impossible for a SOC to detect.

SAMLSmith has a lot of tricks up its sleeve, including:
- Multiple identity provider response forging
- AD FS specific response forging mode
- SAML request processing
- InResponseTo support

SAMLSmith can be used in several response forging scenarios where the private key material can be obtained. In demonstration of use, we'll explore using SAMLSmith for performing a Golden SAML attack against AD FS. Further, we'll demonstrate the use of SAMLSmith that ties into new research around response forging, penetrating certain types of SaaS applications with even more stealth.

Using SAMLSmith requires a certain level of knowledge about the target environment, much of which can be gained with other commonly known and used tools that perform reconnaissance against the targeted identity provider.

</details>

<details><summary><strong>DeadMatter: Offset Independent Credential Extraction Tool</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Demetris Papapetrou](https://img.shields.io/badge/Demetris%20Papapetrou-informational) ![Vasilis Sikkis](https://img.shields.io/badge/Vasilis%20Sikkis-informational)

🔗 **Link:** [DeadMatter: Offset Independent Credential Extraction Tool](https://github.com/qsecure-labs/deadmatter)  
📝 **Description:** DeadMatter is a specialized tool written in C#, designed to extract sensitive information such as password hashes of active logon sessions, from memory dumps. It employs carving techniques to retrieve credentials from various file types such as process or full memory dumps, either in raw or minidump format, decompressed hibernation files, virtual machine memory files, or other types of files that may contain logon credentials.

This tool is particularly useful for penetration testers, red teamers, and forensic investigators, as it facilitates the analysis of system security vulnerabilities and aids in digital forensic investigations. DeadMatter can be very useful to pentesters and red teamers during their engagements, since they often have to deal with EDR and AV software detecting and/or blocking their attempts to dump the LSASS process memory in the minidump format. The alternative of dumping and exfiltrating a full memory dump is often not an option. As a result, DeadMatter was created to fill the gap and allow the offensive team to parse the memory dump files directly on the victim machine, in order to extract NTLM hashes on the spot.

</details>

<details><summary><strong>BOAZ: Development of a Multilayered Evasion Tool and Methodology</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Thomas Xuan Meng](https://img.shields.io/badge/Thomas%20Xuan%20Meng-informational)

🔗 **Link:** [BOAZ: Development of a Multilayered Evasion Tool and Methodology](https://github.com/thomasxm/BOAZ)  
📝 **Description:** BOAZ (Bypass, Obfuscate, Adapt, Zero-Trust) evasion was inspired by the concept of multi-layered approach which is the evasive version of defence-in-depth first proposed by at BH USA14 [1]. BOAZ was developed to provide greater control over combinations of evasion methods, enabling more granular evaluations against antivirus and EDR. It is designed to bypass both before and during execution detections that span signature, heuristic and behavioural detection techniques [2].

BOAZ supports both x86/x64 binary (PE) or raw payload as input and output EXE or DLL. It has been tested on separated Window-11 Enterprise, Windows-10 and windows Server 2022 VMs (version: 22H2, 22621.1992) with 14 Desktop AVs and 7 EDRs installed include Windows Defender, Norton, BitDefender, Sophos and ESET. The design of BOAZ evasion is modular, so users can add their own toolset or techniques to the framework. One advantage of this approach is that if a specific technique's signature become known to antivirus, researchers can easily adjust the technique to verify it and either improve or target a new technique to that detection. This process is described as a query-modify-query attack process, where the attacker can improve based on the feedback from black-box engines until their sample is fully undetectable (FUD) [3].

BOAZ is written in C++ and C and uses Python3 as the main linker to integrate all modules. There have been significant improvements implemented since its inception. The new features of the BOAZ evasion tool, set to be released at BH Asia 2025, include two novel process injection primitives, along with newly implemented loaders and behavioural evasion techniques. There will be a major update to the BH USA 2025 version, including some new anti-forensic techniques and more new process injection threadless execution primitives.

</details>

<details><summary><strong>wish: An AI-Powered Natural Language Shell for Penetration Testing</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sho Nakatani](https://img.shields.io/badge/Sho%20Nakatani-informational)

🔗 **Link:** [wish: An AI-Powered Natural Language Shell for Penetration Testing](https://github.com/SecDev-Lab/wish)  
📝 **Description:** wish is an AI-driven shell environment that translates natural language input into executable shell commands, streamlining penetration testing workflows. Traditional penetration testing heavily relies on memorizing commands or copying and pasting from references, which can be inefficient. wish enables security professionals to focus on strategy and situational awareness rather than syntax recall.

Beyond simple command translation, wish integrates a built-in knowledge base that provides contextual recommendations based on previous executions, making it a powerful assistant for both novice and expert penetration testers. It also seamlessly interacts with C2 frameworks, enabling post-exploitation activities such as privilege escalation, lateral movement, and persistence setup through natural language instructions. With its modular design, wish can be extended to support additional tools, making it a flexible and scalable solution for modern penetration testing workflows.

</details>

<details><summary><strong>EntraGoat - A Deliberately Vulnerable Entra ID Environment</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Tomer Nahum](https://img.shields.io/badge/Tomer%20Nahum-informational) ![Jonathan Elkabas](https://img.shields.io/badge/Jonathan%20Elkabas-informational)

🔗 **Link:** [EntraGoat - A Deliberately Vulnerable Entra ID Environment](https://github.com/Semperis/EntraGoat)  
📝 **Description:** EntraGoat is a deliberately vulnerable environment designed to simulate real-world security misconfigurations and attack scenarios in Microsoft Entra ID (formerly Azure Active Directory). Security professionals, researchers, and red teamers can leverage EntraGoat to gain hands-on experience identifying and exploiting identity and access management (IAM) vulnerabilities, privilege escalation paths, and other security flaws specific to cloud-based Entra ID environments.
EntraGoat is tailored specifically to help security practitioners understand and mitigate the risks associated with cloud identity infrastructures. The project provides a CTF-style learning experience, covering a range of misconfigurations, insecure policies, token abuses, and attack paths commonly exploited in real-world Entra ID breaches.
By using EntraGoat, security teams can enhance their skills in Entra ID security, validate detection and response capabilities, and develop effective hardening strategies.

</details>

<details><summary><strong>Penelope shell handler</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Christodoulos Lamprinos](https://img.shields.io/badge/Christodoulos%20Lamprinos-informational) ![Carlos Marquez](https://img.shields.io/badge/Carlos%20Marquez-informational)

🔗 **Link:** [Penelope shell handler](https://github.com/brightio/penelope)  
📝 **Description:** Penelope is a shell handler designed to be easy to use and intended to replace netcat when exploiting RCE vulnerabilities. It is compatible with Linux and macOS and requires Python 3.6 or higher. It is a standalone script that does not require any installation or external dependencies, and it is intended to remain this way.

Among the main features are:

* Auto-upgrade shells to PTY (realtime resize included)
* Logging interaction with the targets
* Download files/folders from targets
* Upload local/remote files/folders to targets
* Run scripts on targets and get output on a local file in real time.
* Port Forwarding
* Spawn shells on multiple tabs and/or hosts
* Maintain X amount of active shells per host no matter what
* Multiple sessions
* Multiple listeners
* Can be imported by python3 exploits and get shell on the same terminal

Penelope can work in conjunction with metasploit exploits by disabling the default handler with `set DisablePayloadHandler True`

Currently only Unix shells are fully supported. There is only basic support for Windows shells (netcat-like interaction + logging) and the rest of the features are under way.

</details>

<details><summary><strong>Metasploit's Latest Attack Capability and Workflow Improvements</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational) ![Jack Heysel](https://img.shields.io/badge/Jack%20Heysel-informational)

🔗 **Link:** [Metasploit's Latest Attack Capability and Workflow Improvements](https://github.com/mchklt/PFE)  
📝 **Description:** Metasploit continues to expand support for Active Directory Certificate Services (AD CS) attacks, as well as its protocol relaying capability and attack workflows for evergreen vulnerabilities. This year, we added support for SMB-to-LDAP relaying and SMB-to-HTTP relaying, as well as support to identify and exploit a number of AD CS flaws (i.e., ESC vulnerabilities). We've also added the new "PoolParty" process injection capability to Windows Meterpreter sessions, along with support for System Center Configuration Manager (SCCM) attack workflows.


This demo will focus on obtaining an LDAP session via SMB relaying, which can then be used to identify ESC vulnerabilities through Metasploit's expanded ldap_vulnerable_cert_finder module. Using the results from the vulnerable cert finder module, we will demonstrate how to detect and exploit ESC15 (the newest ESC vulnerable certificate template flaw) in order to obtain a certificate that can be used to open a Windows Meterpreter session. While opening the Meterpreter session we will demonstrate using Sysmon how the Windows Meterpreter no longer makes calls to CreateRemoteThread and instead uses the PoolParty injection technique to more effectively inject into the target process.

Going back to our LDAP session, we will run a query to identify SCCM servers in the target Active Directory environment. Once identified, we will demonstrate Metasploit's new SCCM attack workflow, which leverages new SMB-to-HTTP relaying capabilities. Using Metasploit's SMB-to-HTTP relay server, we will relay an NTLM authentication attempt for a newly created computer account to the SCCM HTTP authentication server. After successfully authenticating, we will retrieve Network Access Account (NAA) credentials from the SCCM server, as these are often found in domain environments with higher privileges than they require making them a prime target for lateral movement.

</details>

<details><summary><strong>From Recon to Pwn: MSSQL Exploitation with MSSqlPwner</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nimrod Haim Levy](https://img.shields.io/badge/Nimrod%20Haim%20Levy-informational)

🔗 **Link:** [From Recon to Pwn: MSSQL Exploitation with MSSqlPwner](https://github.com/ScorpionesLabs/MSSqlPwner)  
📝 **Description:** MSSqlPwner is a sophisticated penetration testing arsenal specifically engineered to dominate Microsoft SQL Server environments. Leveraging the extensive capabilities of the Impacket toolkit, MSSqlPwner arms penetration testers with a powerful suite of exploitation techniques, including authentication attacks using Kerberos tickets, NTLM hashes, and clear-text credentials. This versatile tool excels at advanced maneuvers such as NTLM relay attacks, Kerberos and NTLM password bruteforcing, and even direct password extraction via LDAP integration—transforming standard SQL servers into strategic entry points for escalating privileges and lateral network infiltration.

</details>

<details><summary><strong>Crucible C2: Offensive Security Reforged</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jonathan Owens](https://img.shields.io/badge/Jonathan%20Owens-informational)

🔗 **Link:** [Crucible C2: Offensive Security Reforged](https://github.com/DragoQCC/CrucibleC2)  
📝 **Description:** Crucible is an extensible, multi-user, cross-platform framework designed for post-exploitation, command and control operations, penetration testing, and red teaming.

It consists of a per-operator client application, a shared teamserver, and supports language-agnostic implants and plugins.

With this release of Crucible, modern extensibility is achieved through in-memory .NET plugins or gRPC-based plugins, enabling remote communication with external applications regardless of language, allowing extensibility that fits both the operator's skill set and needs.

</details>

<details><summary><strong>Glato: GitLab Attack Toolkit</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Elgin Lee](https://img.shields.io/badge/Elgin%20Lee-informational) ![Matthew Jackoski](https://img.shields.io/badge/Matthew%20Jackoski-informational) ![John Stawinski](https://img.shields.io/badge/John%20Stawinski-informational) ![Mason Davis](https://img.shields.io/badge/Mason%20Davis-informational)

🔗 **Link:** [Glato: GitLab Attack Toolkit](https://github.com/praetorian-inc/glato)  
📝 **Description:** CI/CD pipelines are a too often overlooked aspect of the attack surface for many large organizations. Recent tooling has enabled engineers, researchers, and attackers to search GitHub for CI/CD vulnerabilities, but other DevOps platforms, like GitLab, have been left underserved.

Glato (GitLab Attack Toolkit) is an enumeration and attack framework that empowers both blue and red teamers in identifying and exploiting vulnerabilities within GitLab instances.
Glato works across all GitLab environments, including GitLab CE, EE, and GitLab Cloud. The tool is field-tested, having identified attack paths to GitLab Admin, Domain Admin, and Cloud Admin in multiple engagements with real Fortune 500 organizations.

GitLab's CI/CD ecosystem can contain configuration vulnerabilities that expose organizations to token privilege escalation, sensitive data exposure, and arbitrary code execution on self-hosted runners. Glato's enumeration module leverages a personal access token or session cookies to systematically map all accessible repositories, groups, and instance-level resources. Through recursive pipeline workflow analysis, it identifies misconfigurations and vulnerable CI/CD pipelines that create attack paths within and beyond the GitLab environment.

Security practitioners can deploy Glato's attack module to securely exploit these misconfigurations with features including encrypted variable exfiltration via Poisoned Pipeline Execution (PPE) attacks, secrets dumping, and self-hosted runner compromise. The tool's architecture ensures auditability and operational security through selective targeting and clean exfiltration methods.

Glato has already been used in secure assessments and Red Team engagements to escalate privileges and compromise entire cloud environments.


Key Features:
1. Token/Cookie Authentication Analysis: Evaluates permissions and scope of GitLab tokens or session cookies
2. Comprehensive Enumeration: Discovers accessible projects, groups, and resources with their permission levels
3. Branch Protection Analysis: Identifies misconfigurations that could lead to code execution
4. Secret Discovery: Enumerates secrets from multiple sources, including CI/CD variables
5. Runner Enumeration: Identifies potentially accessible self-hosted runners
6. Poisoned Pipeline Execution: Enables secure CI/CD pipeline exploitation with encrypted secrets exfiltration
7. Quality-of-Life Features: Proxy support, SSL verification control, request throttling, cookie-based authentication for SSO environments, and detailed reporting options

Glato provides security professionals with a systematic approach to evaluate GitLab environments and identify CI/CD pipeline risks before malicious actors can exploit them.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Bitor: Open Source Scalable Security Scanning Platform</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Ralph May](https://img.shields.io/badge/Ralph%20May-informational)

🔗 **Link:** [Bitor: Open Source Scalable Security Scanning Platform](https://github.com/bitorscanner/Bitor)  
📝 **Description:** Orbit is a self-hosted, open source security scanning platform designed to deliver scalable, efficient, and collaborative vulnerability assessments. Built with a modern Go-based backend and a SvelteKit/Tailwind CSS front end, Orbit integrates seamlessly with multiple cloud providers and the Nuclei scanning tool. It empowers security teams to manage large-scale scans, triage findings collaboratively, and harness enriched target data to drive actionable insights.

</details>

<details><summary><strong>Dvora</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Ofri Ouzan](https://img.shields.io/badge/Ofri%20Ouzan-informational)

🔗 **Link:** [Dvora](https://github.com/jfrog/Dvora)  
📝 **Description:** Dvora is an open-source Python tool that enhances SAST detection by identifying custom implementations of dangerous functions (e.g., strcpy) in compiled ELF binaries. It uses a Unicorn-based emulation engine to run individual functions across multiple architectures and a rule set that maps function behavior to well-known function names, then adds discovered symbols to the ELF's symbol section to improve subsequent SAST analysis.

</details>

<details><summary><strong>OWASP Faction - PenTesting Automation Framework</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Summitt](https://img.shields.io/badge/Josh%20Summitt-informational)

🔗 **Link:** [OWASP Faction - PenTesting Automation Framework](https://github.com/factionsecurity/faction)  
📝 **Description:** OWASP FACTION is an open-source solution for streamlined security assessment workflows and enhancing collaboration within your teams. In addition, It's robust and extendable so it can integrate within diverse environments.

FACTION's key benefits are that it cuts reporting time down to more than half for manual pen-tests, keeps tabs on all outstanding vulnerabilities with custom alerts based on your SLAs, becomes the hub of shared information for your assessments enabling other teammates to replay attacks you share, facilitates large scale assessment scheduling that typically becomes hard to manage when your teams are doing more than 100 assessments a year, and is fully extendable with REST APIs and FACTION Extensions.

</details>

<details><summary><strong>SimpleRisk: Governance, Risk Management & Compliance</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

🔗 **Link:** [SimpleRisk: Governance, Risk Management & Compliance](https://github.com/simplerisk)  
📝 **Description:** Security professionals make risk-based decisions every day—whether it's assessing web application vulnerabilities, defending against malware, or securing physical assets. While risk management is conceptually simple, many practitioners struggle due to inadequate tools. Large enterprises can afford expensive GRC solutions, but most professionals are stuck wrestling with spreadsheets—an inefficient, frustrating process prone to errors.

Facing these same challenges while building a risk management program from scratch at a $1B/year company, Josh Sokol sought a better solution. With no budget for enterprise GRC, he built one himself.

SimpleRisk is a free, open-source solution for Governance, Risk Management, and Compliance (GRC). Built on open technologies and licensed under MPL 2.0, it deploys in minutes, offering risk professionals a powerful yet flexible platform to manage control frameworks, policies, audits, and risk mitigation strategies. With dynamic reporting, configurable risk formulas, and continuous development, SimpleRisk delivers enterprise-grade risk management without enterprise-grade costs.

SimpleRisk: making risk management simple.

</details>

<details><summary><strong>Damn Vulnerable Browser Extension (DVBE): Unmask the risks of your Browser Supplements</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Abhinav Khanna](https://img.shields.io/badge/Abhinav%20Khanna-informational)

🔗 **Link:** [Damn Vulnerable Browser Extension (DVBE): Unmask the risks of your Browser Supplements](https://github.com/infosecak/dvbe)  
📝 **Description:** In the continuous evolving world of Browser Extensions, security remains a big concern. As the demand of the feature-rich extensions increases, priority is given to functionality over robustness, which makes way for vulnerabilities that can be exploited by malicious actors. The danger increases even more for organizations handling sensitive data like banking details, PII, confidential org reports etc.

Damn Vulnerable Browser Extension (DVBE) is an open-source vulnerable browser extension, designed to shed light on the importance of writing secure browser extensions and to educate the developers and security professionals about the vulnerabilities and misconfigurations that are found in the browser extensions, how they are found & how they impact business. This built-to-be vulnerable extension can be used to learn, train & exploit browser extension related vulnerabilities.

</details>

<details><summary><strong>Frogy 2.0 - Automated external attack surface analysis toolkit</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Chintan Gurjar](https://img.shields.io/badge/Chintan%20Gurjar-informational)

🔗 **Link:** [Frogy 2.0 - Automated external attack surface analysis toolkit](https://github.com/iamthefrogy/frogy2.0)  
📝 **Description:** Frogy 2.0 is an automated external reconnaissance and Attack Surface Management (ASM) toolkit designed to map out an organization's entire internet presence. It identifies assets, IP addresses, web applications, and other metadata across the public internet and then smartly prioritizes them from P0 (most attractive) to P4 (least attractive) from a bug bounty hunter's perspective.

</details>

<details><summary><strong>Varunastra: Securing the Depths of Docker V2</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Devang Solanki](https://img.shields.io/badge/Devang%20Solanki-informational)

🔗 **Link:** [Varunastra: Securing the Depths of Docker V2](https://github.com/Devang-Solanki/Varunastra)  
📝 **Description:** Varunastra is a Docker security tool that detects and helps mitigate vulnerabilities across Docker containers and images. Key features include secret detection, CVE scanning, dependency confusion prevention, asset extraction, SAST scans of source code, and HTML report generation.

</details>

<details><summary><strong>search_vulns: Simplifying the Surprising Complexity of Finding Known Vulnerabilities</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Dustin Born](https://img.shields.io/badge/Dustin%20Born-informational) ![Matthias Göhring](https://img.shields.io/badge/Matthias%20Göhring-informational)

🔗 **Link:** [search_vulns: Simplifying the Surprising Complexity of Finding Known Vulnerabilities](https://github.com/ra1nb0rn/search_vulns)  
📝 **Description:** The use of third-party software in organizations has increased dramatically in recent years. Meanwhile, new vulnerabilities are published daily. Thus, it is crucial to continuously monitor the security of third-party software. This requires efficient and precise tools to match specific software versions against known vulnerabilities.

To determine a tool to utilize in pentests, we evaluated six tools for retrieving known vulnerabilities: nvdtools, cve-search, CVE Quick Search, Snyk-DB, VulDB and Rapid7-DB.

Surprisingly, we found all to be lacking in some way, identifying mainly three types of problems: tool precision and recall, input restrictions and the lack of exporting functionalities. First, they returned inaccurate results or utilized only one source of information, e.g., lacking information about exploits. Second, they usually require users to adhere to a certain input format like CPEs. This makes them difficult and error-prone to use. Third, meaningfully exporting results was generally not possible.

To address these limitations, we developed search_vulns, which uses text comparison techniques and CPEs in combination to return high-quality results, while not imposing any input restrictions. Moreover, it returns consistent results despite product rebranding and can automatically generate CPEs that have yet to be published. Together with its custom logic for version comparison, this further enhances the quality of search_vulns' results. As it utilizes multiple data sources, unlike most other tools, its results include information about known exploits, backpatches and software recency. Finally, search_vulns provides a fine-granular export of results in different formats.

In conclusion, search_vulns represents a significant improvement over existing tools and benefits various kinds of security analysts in finding known vulnerabilities given only a software name and version. A public web application is available for typical users, while its CLI can be utilized in automated offline workflows. Thus, it has numerous applications in pentests, audits, vulnerability scanners, CI/CD pipelines, SAST or SBOM-analysis.

</details>

<details><summary><strong>Kubernetes Goat - A Hands-on Interactive Kubernetes Security Playground</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Madhu Akula](https://img.shields.io/badge/Madhu%20Akula-informational)

🔗 **Link:** [Kubernetes Goat - A Hands-on Interactive Kubernetes Security Playground](https://github.com/madhuakula/kubernetes-goat)  
📝 **Description:** Kubernetes Goat is an interactive, intentionally vulnerable Kubernetes security playground. It provides hands-on scenarios covering common misconfigurations, real-world attack patterns, and container security challenges within a Kubernetes cluster, designed to help security practitioners learn offensive and defensive Kubernetes security techniques.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>HTTP Raider - The ultimate tool for HTTP hacking</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Martin Doyhenard](https://img.shields.io/badge/Martin%20Doyhenard-informational)

🔗 **Link:** [HTTP Raider - The ultimate tool for HTTP hacking](https://github.com/OWASP/raider)  
📝 **Description:** Modern websites have become a tangled mess of intricate network architectures—creating fertile ground for serious, protocol-level vulnerabilities that traditional tools often overlook.
As web applications continue to grow in complexity, we see the rise of critical vulnerabilities like smuggling, first-request routing, and cache poisoning/deception and the need for a tool that treats HTTP as what it really is: a stream based protocol.

While security professionals rely on HTTP proxies to intercept, analyze, and manipulate traffic, most of these solutions abstract away the stream-based nature of the protocol. By presenting request-response pairs as isolated transactions, they hide crucial details such as persistent connections, pipelining and geo-routing, making it difficult to fully understand how data truly flows—or to uncover advanced attack vectors.

To address these challenges, I developed HTTP Raider, an open source Burp Suite extension that helps you explore and exploit your target's underlying protocol logic with ease. It surfaces hidden details like persistent connections and pipelining, and provides absolute clarity on what's happening under the hood, empowering you to take your attacks further and exploit critical vulnerabilities that would otherwise remain undetected.

Additionally, HTTP Raider leverages error- and timing-based analyses to detect concealed proxies, caching layers, and cloud infrastructures—offering a holistic view of the network infrastructure.Through a drag-and-drop interface, users can model the flow of messages across multiple components, predicting how traffic is transformed and routed.

By removing the guesswork inherent in conventional proxies and empowering testers with a low-level view of HTTP, this tool ultimately promotes true protocol mastery—enabling researchers to discover and exploit critical vulnerabilities that would otherwise remain undetected.

</details>

<details><summary><strong>Open-Source API Firewall by Wallarm - Advanced Protection for REST and GraphQL APIs</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Satinder Khasriya](https://img.shields.io/badge/Satinder%20Khasriya-informational)

🔗 **Link:** [Open-Source API Firewall by Wallarm - Advanced Protection for REST and GraphQL APIs](https://github.com/wallarm/api-firewall)  
📝 **Description:** The API Firewall ensures strict API request and response validation, adhering to both OpenAPI and GraphQL schemas. By employing a positive security model, it enhances API security by allowing only the traffic that meets a predetermined API specification for requests and responses, effectively blocking all other traffic. It's designed to work in cloud-native environments with a huge amount of traffic and is optimized for near-zero latency.

The key features of Wallarm's API Firewall are:
Endpoint Security: Secure REST and GraphQL API endpoints by blocking non-compliant requests/responses
Data Breach Prevention: Stop API data breaches by blocking malformed API responses
Shadow API Discovery: Discover Shadow API endpoints
Specification Adherence: Block attempts to use request/response parameters not specified in an OpenAPI specification
Token Validation: Validate JWT access tokens and other OAuth 2.0 tokens using introspection endpoints
Security Enhancements: Denylist compromised API tokens, keys, and cookies
Wide Range Attacks Protection: The API Firewall supports ModSecurity Rules and OWASP Core RuleSet v3/v4
Monitoring: Graphs and metrics of traffic processed by the API Firewall to provide full information about the protected API status and attacks attempts

The latest update of the API Firewall includes a new user interface that simplifies configuration, improves the control over the traffic processed by the API Firewall and sent to the protected API, and support for ModSecurity rules, enabling integration with the OWASP Common Rule Set (CRS) to enhance the protection capabilities against common web attacks. It also offers API rate limiting for specified endpoints to prevent API abuse, customizable response actions for each endpoint, and additional graphs and metrics to improve traffic monitoring and attack analysis.

This product is open-source and can be found on DockerHub, where it has impressively reached 1 billion downloads.

</details>

<details><summary><strong>GraphQL Armor: Open Source Highly Customizable GraphQL Security Middleware</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tristan Kalos](https://img.shields.io/badge/Tristan%20Kalos-informational) ![Antoine Carossio](https://img.shields.io/badge/Antoine%20Carossio-informational)

🔗 **Link:** [GraphQL Armor: Open Source Highly Customizable GraphQL Security Middleware](https://github.com/escape-technologies/graphql-armor)  
📝 **Description:** With our open-source tool GraphQL Armor we want to take GraphQL security to the next level. GraphQL Armor is a dead-simple yet highly customizable security middleware for various GraphQL server engines. It offers advanced protection against common vulnerabilities like query depth, complexity, and rate limiting.

The key features of GraphQL Armor are:
- Query depth and cost limiting to mitigate denial-of-service (DoS) attacks
- Rate-limiting and automatic request blocking for abusive clients
- Protection against batch attacks and nested query exploits
- Field obfuscation to limit API exposure
- Seamless integration with major GraphQL frameworks

We want to show security engineers and developers with a security mindset how to make sure their GraphQL APIs are secure. This tool is open source and can be found on npm, where it has impressively reached 94k weekly downloads.

</details>

<details><summary><strong>WebSocket Turbo Intruder</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Zakhar Fedotkin](https://img.shields.io/badge/Zakhar%20Fedotkin-informational)

🔗 **Link:** [WebSocket Turbo Intruder](https://github.com/Hannah-PortSwigger/WebSocketTurboIntruder)  
📝 **Description:** Websites are increasingly adopting WebSockets for business critical functionality, but security tools have failed to keep up. As a result, WebSocket security testing is so painful that this ever-expanding attack surface is largely overlooked.

WebSocket Turbo Intruder is an open-source solution which makes attacks pain-free with automatic message correlation, timing and content analysis, and battle-tested matching and filtering capabilities. It also enables advanced, multi-step attack sequences thanks to an underlying Python API providing infinite customisability. It seamlessly integrates into Burp Suite, and also runs as a standalone CLI tool - ideal for launching attacks from a high-bandwidth VPS.

Under the hood, it is powered by a high-performance WebSocket engine developed from scratch for security testing, capable of sending tens of thousands of messages per second - perfect for large-scale bruteforce attacks, and triggering race conditions. The custom engine also allows the use of malformed messages, letting you exploit protocol-level implementation flaws, including a modern spin on the classic Ping-of-Death.

You can even scan WebSockets with your existing HTTP scanning tools, thanks to a convenient HTTP adapter. It is time to unlock the WebSocket goldmine.

</details>

<details><summary><strong>WAFSmith - LLM-based Rule Management Framework to Create Rules that Simply Work</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Kee Hock Tan](https://img.shields.io/badge/Kee%20Hock%20Tan-informational) ![Sean Yeoh](https://img.shields.io/badge/Sean%20Yeoh-informational)

🔗 **Link:** [WAFSmith - LLM-based Rule Management Framework to Create Rules that Simply Work](https://github.com/tankeehock/wafsmith)  
📝 **Description:** Rule management has been a challenging issue that enterprises face to maintain a highly effective WAF. Poor maintenance of WAF rulesets results in productivity loss and reduced WAF effectiveness which ultimately translates to an enlarged attack surface. WAFSmith was developed to reduce the friction of rule management by leveraging the capabilities of intelligent AI agents to perform tasks to reduce the cognitive burden placed upon human operators. It is a highly advanced LLM-based agent that can perform payload extraction, rule writing, testing, and deployment. Evaluation performed with proven rulesets such as ModSecurity's CRS, shows significant security improvements introduced by WAFSmith, demonstrating real-world impact. The methodology adopted by WAFSmith proved to be robust and reliable which can be easily retrofitted to suit other rule-management use cases such as IDPS Rules. WAFSmith is designed to enhance Blue Team's cyber defense investments through a high degree of intelligent operations in the domain of rule management. The by-products in the development of WAFSmith such as the Prompts and ModSecurity rules serve as valuable contributions to the Open-Source community.

</details>

<details><summary><strong>APIDetector v3 - Advanced Swagger Endpoint Scanner with Real-time Web Interface</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Filipi Pires](https://img.shields.io/badge/Filipi%20Pires-informational) ![Rafael Brinhosa](https://img.shields.io/badge/Rafael%20Brinhosa-informational)

🔗 **Link:** [APIDetector v3 - Advanced Swagger Endpoint Scanner with Real-time Web Interface](https://github.com/brinhosa/apidetector)  
📝 **Description:** APIDetector v3 is an advanced, high-performance tool built for identifying and validating exposed Swagger/OpenAPI endpoints across domains and subdomains. Designed specifically for security professionals and developers, APIDetector v3 provides a modern web interface offering real-time results, interactive dashboards, automated screenshot captures, and intelligent false-positive detection.

Having been successfully presented at BlackHat Arsenal 2024, this new iteration introduces significant enhancements, including real-time result visualization, flexible bulk domain scanning via file uploads, and substantial user experience improvements using Tailwind CSS and Alpine.js. APIDetector v3 greatly simplifies API endpoint vulnerability assessment, speeding up penetration tests and vulnerability scanning processes.

</details>

<details><summary><strong>DefectDojo OWASP Edition</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Matt Tesauro](https://img.shields.io/badge/Matt%20Tesauro-informational)

🔗 **Link:** [DefectDojo OWASP Edition](https://github.com/DefectDojo/django-DefectDojo)  
📝 **Description:** The DefectDojo platform for scalable and flexible unified vulnerability management, ASPM, and DevSecOps is the culmination of a decade-plus of open-source work. Currently in v2.44 as of this writing, DefectDojo was designed by cybersecurity professionals frustrated with ever-ballooning amounts of data and difficulty streamlining workflows for cybersecurity professionals frustrated with ever-ballooning amounts of data and difficulty streamlining workflows.

DefectDojo addresses a number of key pain points, particularly with tool integration to streamline workflows, deduplication and consolidation of findings to avoid alert fatigue, and data organization features that adapt to a team's needs rather than the other way around. For example, the OWASP Edition supports integrations with 200+ commonly-used tools and integration with Jira.

Recognized on the Open Source Security Index as one of the most-popular and fastest-growing open-source software solutions, DefectDojo is also an OWASP Flagship Project. It continues to receive regular updates from both the company and community – capitalizing on the collective wisdom of the cybersecurity community around the world to help all professionals. To date, DefectDojo has over 38 million downloads on the OWASP Edition alone.

</details>

<details><summary><strong>Blackdagger: Cyber Workflow Automation Framework</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Mahmut Erdem Ozgen](https://img.shields.io/badge/Mahmut%20Erdem%20Ozgen-informational) ![Ata Seren](https://img.shields.io/badge/Ata%20Seren-informational) ![Elif Basar Ozgen](https://img.shields.io/badge/Elif%20Basar%20Ozgen-informational) ![Muhammed Alparslan Akyildiz](https://img.shields.io/badge/Muhammed%20Alparslan%20Akyildiz-informational)

🔗 **Link:** [Blackdagger: Cyber Workflow Automation Framework](https://github.com/erdemozgen/blackdagger)  
📝 **Description:** Blackdagger is an innovative workflow automation framework specifically designed to simplify and accelerate cybersecurity operations across DevOps, DevSecOps, MLOps, MLSecOps, and Continuous Automated Red Teaming (CART). At its core, Blackdagger reduces complexity and manual overhead by leveraging a novel declarative YAML-based Directed Acyclic Graph (DAG) approach, enabling users to intuitively define automation pipelines, clearly visualize task dependencies, and minimize extensive scripting or coding typically required by traditional cronbased schedulers and orchestration platforms. A user-friendly built-in Web UI further empowers users by providing easy, real-time management, monitoring, and execution of workflows.

Blackdagger's ecosystem includes several integrated tools and workflow suites, creating a comprehensive cybersecurity automation framework:
- Blackcart: A specialized Docker container optimized for Continuous Automated Red Teaming (CART) and DevSecOps pipeline tasks.
- Blackdagger YAMLs: Pre-tested example workflows, demonstrating real-world DevSecOps and CART use-cases, facilitating quick adoption and adaptation.
- Blackdagger Github Infra: A suite of advanced workflows utilizing GitHub Actions infrastructure for enhanced defense evasion techniques, scalability, and performance.
- Blackdagger Web Kit (BWK): A browser extension integrating all core functionalities, enabling direct interaction and execution of Blackdagger workflows from within the browser.

During this Arsenal session, attendees will see practical demonstrations of Blackdagger's capabilities, including rapid deployment of DevSecOps and CART workflows, pipeline visualization, and streamlined security task automation in action.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Plaguards: Open Source PowerShell Deobfuscation and IOC Detection Engine for Blue Teams.</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Nadia](https://img.shields.io/badge/Nadia-informational) ![Bertrand Redondo Mulyono](https://img.shields.io/badge/Bertrand%20Redondo%20Mulyono-informational) ![Nicolas Saputra Gunawan](https://img.shields.io/badge/Nicolas%20Saputra%20Gunawan-informational) ![Satya Kusuma](https://img.shields.io/badge/Satya%20Kusuma-informational) ![Yohan Muliono](https://img.shields.io/badge/Yohan%20Muliono-informational)

🔗 **Link:** [Plaguards: Open Source PowerShell Deobfuscation and IOC Detection Engine for Blue Teams.](https://github.com/baycysec/plaguards)  
📝 **Description:** Plaguards is an open-source PowerShell deobfuscation and IOC detection engine built for blue teams. It automates static deobfuscation of obfuscated PowerShell scripts commonly used in malware and ransomware attacks, extracts embedded Indicators of Compromise (IOCs) such as IP addresses and URLs, and generates templated PDF reports cross-referencing findings with threat intelligence.

</details>

<details><summary><strong>Decompiler for HarmonyOS NEXT</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Xiaoyu He](https://img.shields.io/badge/Xiaoyu%20He-informational)

🔗 **Link:** [Decompiler for HarmonyOS NEXT](https://github.com/jd-opensource/arkdecompiler)  
📝 **Description:** HarmonyOS NEXT is the next generation operating system developed by Huawei. It completely removes the Android AOSP code and is incompatible with Android applications. In addition, it has developed a new operating system kernel, which will cover more than one billion devices in the future. Because HarmonyOS NEXT has a new compiler, interpreter, file format and instruction set architecture, it makes the previous program analysis tools invalid. In addition, the information and documents of the new system are very limited, which makes it difficult for security analysts to conduct security analysis and risk assessment quickly and effectively.

To solve this problem, we read the source code of ArkCompiler, the compiler of HarmonyOS NEXT. We summarized the detailed process of ArkCompiler compilation. It takes arkTS (a variant of typescript) as input, translates it into Panda Bytecode, and finally executes it in the ecma virtual machine. It is also designed to support JIT and AOT functions. In addition, we also have a deep understanding of its AST, IR, assembly, executable files, and the design ideas of compilation optimization design.

Based on this, we developed the ArkCompiler decompilation tool named arkdecompiler, which takes Panda Binary File as input, parses Panda Bytecode, and then translates it into Panda IR. After having IR, we can do various analyses. Based on IR, we reversely construct the native arkTS AST tree, and then we traverse the AST tree and translate it into native arkTS source code. At present, we have implemented support for common binary operation instructions.

To be more specifically, we will talk about:
- ArkCompiler's overall process and key components such as AST, IR, bytecode.
- How to translate Panda Bytecode into Panda IR using existing components of ArkCompiler.
- How to automatically reverse build the ArkTS AST tree based on Panda IR.
- After having the AST tree, how do we convert it into ArkTS source code.

In order to demonstrate the capabilities of our framework and tools, we prepared some cases, including a demo written in arkTS, compiled into Panda Bytecode using ArkCompiler, and restored to native ArkTS code using our tool Arkcompiler.

In order to allow more people to participate, quickly improve the project and make it more powerful, so as to improve the efficiency of security analysts, we will release the source code of the tool. In the future, we hope that our work can make the HarmonyOS system and its applications more secure.

</details>

<details><summary><strong>ParseAndC 4.0 - The Final Cut</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Parbati Kumar Manna](https://img.shields.io/badge/Parbati%20Kumar%20Manna-informational)

🔗 **Link:** [ParseAndC 4.0 - The Final Cut](https://github.com/intel/ParseAndC)  
📝 **Description:** This is the 4.0 (and Final) version of the ParseAndC tool (whose 1.0, 2.0 and 3.0 versions were presented in the Black Hat Arsenal 2021/2022/2023 (SecTor) and DEFCON 2021). The 1.0 version was capable of mapping any C structure(s) to any datastream, and then visually displaying the 1:1 correspondence between the variables and the data in a very colorful, intuitive display so that it was very easy to understand which field had what value. In 2.0 version, we introduced dynamic structures which essentially expanded the C language semantics (not syntax) so that now C structures alone had the same power as full-fledged C programs. In 3.0 version, we completed the parsing part of the tool by adding a ton of new or missing features that cover various quirks of C language so that the tool now worked on ANY production C code.

What problems are we solving in this new 4.0 version?

The main problem we solve is that often there is a huge gap between the way any data is stored, and the way it needs to be displayed to make sense to the end-users. While writing a parser, after you "parse" (read in) the data, for "simple" kind of data you can display the data just like that without any manipulation (for example, the integer variable "PacketSizeBytes" can be displayed just like that, and people will immediately understand its value. However, often there are other type of not-so-simple data where just by displaying the data in the native format, it does not convey the real measure of what the data represents. For example, suppose an integer stores the number of seconds since a certain event. Just seeing 465827 sec doesn't give a proper sense of how long the time is, but converting it to a human-readable 5 days 9 hrs 23 min 47 sec does. So, for such cases, merely proper "parsing" (reading in) the data is not enough - we also need to write additional code (either within the Parser itself, or pipe the native format into yet another shell script) to display the value in a custom format. In C, the only two native ways to store data are integer and float, but we need this custom format for many other cases. Some examples:

- Suppose an int represents a memory address, and you would rather see its value displayed in Hex format.
- Suppose an int represents a mask, and you would rather see its value in the binary format.
- Support an int stores the Unix timestamp of a certain event. Just seeing how many seconds have passed since 1/1/1970 is not very telling, it would make far more sense if we convert it to a human-readable YYYY-MM-DD HH-MM-SS or something like that.
- Suppose a float contains the temperature of the chip in Kelvin, but the user of the tool would rather see the unit in Fahrenheit.
- Suppose an int contain the # of days since a particular Sunday, and instead of knowing the day count, the user would rather want to know which day of the week (Sun/Mon/Tue etc.) it is because that's all he/she cares about.
- Suppose an int contains the IPv4 protocol number, but instead of just displaying the numeric protocol numbers like 1/6/17/46, , you would rather display the corresponding protocol names like ICMP/TCP/UDP/RSVP etc.
- Suppose an int actually represents the 4 octets of an IP address, and the user rather see it in the A.B.C.D format.
- It is a char array, and instead of seeing their numeric values, the user would rather see their corresponding ASCII chars.
- The number(s) are coded in certain encoding (say Binary-Coded-Decimal or Base-64), and the user would want to see the decoded values.

C offers printf for doing certain limited manipulations while displaying the data via format string, but that's it. For example, it cannot automatically display the #sec into day:HH:MM:SS format. For each of those custom display manipulation, one would need to write extra code in the Parser, or pipe the parsed data (in native format) to yet another shell script that will manipulate the native data into custom display format. This process is laborious and error prone. Why? Since the code for manipulating the variable value is located in a different place than where the variable is declared, chances are high that coders will make cut-and-paste errors (use wrong variable names or attributes etc.).

Here, we CO-LOCATE the output display format of the data in the same place where they are declared, and the beauty is that, we do it without breaking the C syntax. We optionally annotate every variable declaration with a "format" or "TAG", where the TAG tells how the variable will be displayed. And since we are not allowed to break the existing C syntax, we put this TAG within the C comment that starts on same line of the variable declaration. A C preprocessor usually discards the comments, but our tool also parses the comments, and if it finds any custom display tag annotation, it will display it accordingly.

To recap on the new capabilities of this tool, earlier the tool used to display the data in the native C formats (integers and floating points), but in current version 4.0 we now have the ability to display the internally stored data into ANY output format we like. For most common type of display formats, this tool gives builtin formats, and for others, it gives the users a way specify it dynamically. You will no longer need to pipe the output to yet another Python/Perl/SED/TR/AWK/Shell script to display the data in the intended format. In other words, this tool is now your ONE-STOP-SHOP for parsing and interpreting the data you are getting from your testing. ANY AND ALL KIND OF TESTING - SW, FW OR HW, Security- or non-Security testing.

The output formats (TAG) that have been added are:

(Reviewer - please note that in this submission, I am using {FORMAT} and {/FORMAT} while in real-life the "{" and "}" would be replaced by "less-than-symbol" and "greater-than-symbol" for this tool. The reason I am forced to do this is because this Black Hat submission website has input sanitization rules which treats them as valid HTML tags and starts interpreting it.

1) Built-in formats: HEX, OCT, BIN, DEC, PERCENT – to display the data as Hexadecimal, Octal, Binary, Decimal, and Percent. So, if you declare a variable like int I; /* {FORMAT} BIN {/FORMAT}*/, then in the output its value would get displayed in binary.
2) Built-in Time formats: MILLISECONDS, SECONDS, UNIXDATETIME, EXCELDATETIME – to display the time into a human readable format involving year, month, day, hour, minute, second etc. (fully customizable). For example, if we have a declaration like int TS; /* {FORMAT} UNIXDATETIME {/FORMAT} */, then the tool will treat this TS variable as a unix timestamp and display its value as YYYY-MM-DD HH:mm:SS. It is extremely flexible, for example, if you give {FORMAT} UNIXDATETIME("Date is MM/DD/YY, and time is HH-mm-SS"){/FORMAT}, for TS=1741977744, your output will be "Date is 03/14/25, and time is 18-42-24" (basically exactly the supplied argument string, with its various tokens like MM, DD, YY etc. replaced with the corresponding values.). Please note that Microsoft Excel stores the timestamp in a different way (a float representing the number of full and fractional days since Dec 31, 1899), and we handle it.
3) BCD format: To decode data encoded in Binary-Coded-Decimal. This tool provides built-in support for ALL varieties of BCD (viz. "8 4 2 1 (XS-0)" ,"7 4 2 1" ,"Aiken (2 4 2 1)" ,"Excess-3 (XS-3)" ,"Excess-6 (XS-6)" ,"Jump-at-2 (2 4 2 1)" ,"Jump-at-8 (2 4 2 1)" ,"4 2 2 1 (I)" ,"4 2 2 1 (II)" ,"5 4 2 1" ,"5 2 2 1" ,"5 1 2 1" ,"5 3 1 1" ,"White (5 2 1 1)" ,"5 2 1 1" ,"Magnetic tape" ,"Paul" ,"Gray" ,"Glixon" ,"Ledley" ,"4 3 1 1" ,"LARC" ,"Klar" ,"Petherick (RAE)" ,"O'Brien I (Watts)" ,"5-cyclic" ,"Tompkins I" ,"Lippel" ,"O'Brien II" ,"Tompkins II" ,"Excess-3 Gray" ,"6 3  2  1 (I)" ,"6 3  2  1 (II)" ,"8 4  2  1" ,"Lucal" ,"Kautz I" ,"Kautz II" ,"Susskind I" ,"Susskind II")
4) BASE64 format: To decode data encoded in Base-64 format. Obviously, this only works on array because we are talking about converting 8-bits into 6-bits.
5) PRINTF format: Basically, giving the user the full power of the C function printf(), and much more. We have also incorporated the more powerful features from other languages in this. For example, Python allows "+" to concatenate strings, and "*" to repeat strings, which we allow here in printf format string specification.
6) ENUM format: If the code has enum in it, the tool automatically displays the corresponding enum literals instead of the variable values (this is massively helpful). In addition, even if the C struct did not have any enum declared, here we can allow an display enum to be declared specifically for that variable. Combining the C enum and C switch statements, where we depending on the value of the data, we display a certain literal instead. For example. Suppose we store the privilege level of a device driver in an integer called Ring, and instead of displaying 0 and 3, we want display "KMD" and "UMD". In our tool, we just declare it as int Ring; /* {FORMAT} ENUM("KMD"=0, "UMD"=3) {/FORMAT} */, it will display it accordingly.
7) POSTPROCESS format: This is the most powerful where you can pretty much write any code based on the stored value. You no longer need to pipe the output to yet another script. For example, if variable temp stores the temperature in Kelvin but we want to display it in Fahrenheit, then int tempKelvin; /* {FORMAT} POSTPROCESS((tempKelvin-273.15)*1.8+32) {/FORMAT}*/ will do the job.

We also introduce the "_X_" operator within these formats. Most of the errors in parser writing happens due to cut-and-paste error (if a C struct has 20 fields, there is no way the coder is going to freshly type the 20 printf statements to display their values - the coder is going to type it once for one variable, and then for the rest 19 variables he/she is going to simply copy the first printf statement, and do the necessary changes. However, many a times the coders forget to make the necessary changes. For example, suppose a very simple struct has two int variables "height" and "weight", two words that differ by a single character. While printing their values, a coder can easily make the following mistake:

printf("height is %d", height);
printf("weight is %d", height);

To avoid these kind of errors, in this 4.0 version, we introduce the "_X_" operator. During runtime, this _X_ will get substituted with the corresponding variable name. For example, look at the struct below which our tool will understand just fine:

struct S {
int height; // {FORMAT} PRINTF("%d",_X_) {/FORMAT}
int weight; // {FORMAT} PRINTF("%d",_X_) {/FORMAT}
};

Another great feature we add is that all these TAGs or formats can be applied one after another on the same variable. So, suppose a variable contains a unix timestamp, and we are only interested in knowing how many days were in that month, and we want the display that many "=" symbols. For example, suppose we know that the timestamp corresponds to a day in the month of December. Since December has 31 days, we want to display "===============================". We can achieve this very elegantly here:

int TimeStamp; /* {FORMAT} UNIXDATETIME("MM") {/FORMAT}
{FORMAT} POSTPROCESS(int(_X_)) {/FORMAT}
{FORMAT} ENUM(31=1,28,31,30,31,30,31,31,30,31,30,31) {/FORMAT}
{FORMAT} PRINTF(_X_*"=") {/FORMAT} */

The first {FORMAT} UNIXDATETIME("MM") {/FORMAT} extracts the date in the MM form (two-digit numeric string).
The second {FORMAT} POSTPROCESS(int(_X_)) {/FORMAT} converts that two-digit numeric string to a number (for example, converting a "09" to 9)
The third {FORMAT} ENUM(31=1,28,31,30,31,30,31,31,30,31,30,31) {/FORMAT} tells how many days to display for that month (observe that month starts from 1, not 0).
The fourth {FORMAT} PRINTF{_X_*"="} simply prints that many "=" symbols.

This is essentially equivalent of writing sequential code, line after line. The output from previous format gets fed into the next format. This way, you can pretty much write ANY code to custom display your variable RIGHT where the variable declaration is happening. So, the chances of messing it up is indeed very low. And, it is Turing-complete.

Last but not the least, whenever we print a custom display value, we display BOTH the original (native) value and the manipulated (formatted) value. You can see it on the console and in the CSV file. So, we are actually not changing the internal value.

Just click on the "Run Demo" button and see for yourself.

This tool is extremely portable – it's a single Python 2MB text file, is cross-platform (Windows/Mac/Unix), and also works in the terminal /batch mode without GUI or Internet connection. The tool is self-contained - it doesn't import anything, to the extent that it implements its own C compiler (front-end) from scratch!!

This tool is useful for both security- and non-security testing alike (reverse engineering, network traffic analyzing, packet processing etc.). It is currently being used at Intel widely. The author of this tool led many security hackathons at Intel and there this tool was found to be very useful.

</details>

<details><summary><strong>rev.ng decompiler</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Alessandro Di Federico](https://img.shields.io/badge/Alessandro%20Di%20Federico-informational) ![Pietro Fezzardi](https://img.shields.io/badge/Pietro%20Fezzardi-informational)

🔗 **Link:** [rev.ng decompiler](https://github.com/revng/revng)  
📝 **Description:** rev.ng is a static binary analysis framework based on LLVM and QEMU.

Key features:

* Full-fledged decompiler, that emits syntactically valid C.
* Large architecture support (x86-64 x86, ARM, AArch64, MIPS and s390x).
* Ideal environment for deobufscation thanks to the off-the-shelf availability of the LLVM -O2 optimization pipeline.
* Support for static code analysis using symbolic execution (KLEE or clang-static-analyzer) or CodeQL.
* Automatic recovery of data structures exploiting information across the whole program.
* Scripting interface for Python and TypeScript.

</details>

<details><summary><strong>elfspirit</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Song Magic](https://img.shields.io/badge/Song%20Magic-informational)

🔗 **Link:** [elfspirit](https://github.com/secnotes/elfspirit)  
📝 **Description:** ELFSPIRIT is a comprehensive static analysis and injection framework designed to parse, manipulate, patch, and camouflage ELF files. With elfspirit, you can explore the intricacies of the ELF format and have the freedom to finely manipulate every byte within the ELF file.

</details>

<details><summary><strong>SHAREM: Modernizing Shellcode Analysis for Today's Threats</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational) ![Tate Forcella](https://img.shields.io/badge/Tate%20Forcella-informational) ![William Lochte](https://img.shields.io/badge/William%20Lochte-informational)

🔗 **Link:** [SHAREM: Modernizing Shellcode Analysis for Today's Threats](https://github.com/bw3ll/sharem)  
📝 **Description:** Shellcode is omnipresent, a constant part of the exploitation and malware ecosystem. Injected into process memory, there are innumerable possibilities. Yet until recently, analysis techniques were severely lacking. We present SHAREM, an NSA-funded shellcode analysis framework with stunning capabilities that have revolutionized how we approach the analysis of shellcode.

SHAREM can emulate shellcode, identifying more than 30,000 WinAPI functions as well as 99% of Windows syscalls. This emulation data can also be ingested by its own custom disassembler, allowing for functions and parameters to be identified in the disassembly for the first time ever. The quality of disassembly produced by SHAREM is virtually flawless, markedly superior to what is produced by leading disassemblers. In comparison, IDA Pro or Ghidra might produce a vague "CALL EDX," as opposed to identifying what specific function and parameters is being called, a highly non-trivial task when dealing with shellcode.

One obstacle with analyzing shellcode can be obfuscation, as an encoded shellcode may be a series of indecipherable bytes—a complete mystery. SHAREM can easily overcome this, presenting the fully decoded form in the disassembler, unlocking all its secrets. Without executing the shellocode, emulation can be used to help fully deobfuscate the shellcode. In short, a binary shellcode – or even the ASCII text representing a shellcode – could be taken and quickly analyzed, to discover its true, hidden functionality.

One game-changing innovation is complete code coverage. With SHAREM, we ensure that all code is executed, capturing function calls and arguments that would otherwise be impossible to get. This is done by taking a series of snapshots of memory and CPU register context; these are restored if a shellcode ends with unreached code. In practical terms, this means if a shellcode ordinarily would prematurely terminate, we might miss out several malicious functions. Complete code coverage allows us to rewind and restart at specific points we should not be able to reach, discovering all functionality.

New to be unveiled at Arsenal, SHAREM will now optionally integrate AI to help resolve what exactly is going on. The previously enumerated APIs and parameters—along with disassembly and discovered artifacts--can be analyzed to identify malicious techniques, which may be found in MITRE ATT&CK framework.

The ease and simplicity of SHAREM is breathtaking, especially comparison to how much time and effort similar analysis would require otherwise. What might previously require expertise and take extended time for analysis can now be reduced to seconds. SHAREM represents a game-changing shift in our capability to analyze shellcode in a highly efficient manner, documenting every possible clue – whether it be functions, parameters, or artifacts.

For reverse engineers of all kinds, SHAREM is a must-see presentation.

</details>

<details><summary><strong>ShadowSeek: Combining Ghidra and Large Language Models for Advanced Binary Analysis</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Mohammed Tanveer](https://img.shields.io/badge/Mohammed%20Tanveer-informational)

🔗 **Link:** [ShadowSeek: Combining Ghidra and Large Language Models for Advanced Binary Analysis](https://github.com/Luis-Varona/shadowseek)  
📝 **Description:** This paper presents a novel integration between Ghidra, the NSA's open-source reverse engineering tool, and Large Language Models (LLMs) via a web-based interface. We introduce ShadowSeek, a system that enhances Ghidra's powerful binary analysis capabilities with the reasoning capabilities of modern LLMs. Our system enables users to interactively query, analyze, and understand binary files through natural language, significantly reducing the expertise barrier for complex reverse engineering tasks. We demonstrate how this integration improves binary analysis workflows through automated function explanation, vulnerability detection, and optimization recommendation. ShadowSeek represents a significant step forward in making advanced reverse engineering tools more accessible while preserving their analytical power

</details>

<details><summary><strong>ARC – Artifact Reuse Comparator</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Rushikesh D. Nandedkar](https://img.shields.io/badge/Rushikesh%20D.%20Nandedkar-informational)

🔗 **Link:** [ARC – Artifact Reuse Comparator](https://github.com/1nod3/ARC)  
📝 **Description:** ARC (Artifact Reuse Comparator) is a state-of-the-art static analysis tool that disassembles Windows PE files (executables and DLLs), extracts various code artefacts (functions, basic blocks, API calls, sliding-window fingerprints), and compares them across binaries to detect reuse—even in obfuscated samples. ARC stores these artefacts in an SQLite database and generates detailed TXT and HTML reports. Additionally, ARC features control flow graph (CFG) visualization, providing analysts with both high-level and granular views of code similarity. Its modular design and extensibility make it an essential tool for malware analysis and reverse engineering.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>Chasing Your Tail NG</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Matt Edmondson](https://img.shields.io/badge/Matt%20Edmondson-informational)

🔗 **Link:** [Chasing Your Tail NG](https://github.com/ArgeliusLabs/Chasing-Your-Tail-NG)  
📝 **Description:** My "Chasing Your Tail with a Raspberry Pi" talk at Blackhat 2022 blew up and the tool got featured in multiple media outlets, including Wired and the Official MagPi magazine. The tool worked great, but there was A LOT of room for improvement. I'm finally ready to release the updated version, which includes more straightforward setup, more modular configuration, and the capability to go from defense to offense by analyzing the logs obtained to try to determine information about the devices following you!

</details>

---
## 🤖 AI, ML & Data Science
<details><summary><strong>modernbertdos</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Oscar Augusto Gonzalez Lira](https://img.shields.io/badge/Oscar%20Augusto%20Gonzalez%20Lira-informational) ![Luis Cordon](https://img.shields.io/badge/Luis%20Cordon-informational)

🔗 **Link:** [modernbertdos](https://github.com/oscarGLira/modernbertdos)  
📝 **Description:** The modernbertdos Classification Tool fine-tunes a transformer-based model, ModernBERT, for multi-class classification of network traffic. It detects and classifies various traffic types, including DDoS attacks and normal traffic, using labeled datasets such as CIC-DDoS2019 and a dataset specifically crafted for SSL. The tool employs Hugging Face's Transformers library for model fine-tuning, supports early stopping, tracks key metrics (Accuracy, F1 Score, Precision, Recall), and uploads the fine-tuned model to Hugging Face for easy sharing.

</details>

<details><summary><strong>Promptfoo</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Ian Webster](https://img.shields.io/badge/Ian%20Webster-informational) ![Michael D'Angelo](https://img.shields.io/badge/Michael%20D'Angelo-informational) ![Vanessa Sauter](https://img.shields.io/badge/Vanessa%20Sauter-informational)

🔗 **Link:** [Promptfoo](https://github.com/promptfoo/promptfoo)  
📝 **Description:** Promptfoo is an offensive security tool designed to test applications built on large language models (LLMs). Leveraging the latest adversarial ML research, Promptfoo uses ablated, fine-tuned models to generate unique, adversarial payloads to find and exploit more than 50 types of vulnerabilities in LLM applications. More than 60,000 developers use Promptfoo, including at major companies like Shopify, OpenAI, Anthropic, Twilio, and DoorDash.

Promptfoo is unique in its capabilities because it uses specialized adversarial agents trained to probe specific risks in AI applications. Rather than relying on generic jailbreaks or known exploits, these agents analyze your application's unique attack surface - its specific use cases, integrated tools, data sources, and security boundaries. Promptfoo then generates targeted probes to identify vulnerabilities in your applications.

The tests cover application-level categories such as PII/data leaks, access control issues via agentic tool use, as well as model-level risks like jailbreaks/injections and other harmful outputs.

</details>

<details><summary><strong>AI Wargame</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Pedram Hayati](https://img.shields.io/badge/Pedram%20Hayati-informational) ![Davide Cioccia](https://img.shields.io/badge/Davide%20Cioccia-informational) ![Harley Wilson](https://img.shields.io/badge/Harley%20Wilson-informational)

🔗 **Link:** [AI Wargame](https://play.secdim.com/)  
📝 **Description:** Come join a fun and educational attack and defence AI wargame. You will be given an AI chatbot. Your chatbot has a secret that should always remain a secret! Your objective is to secure your chatbot to protect its secret while attacking other players' chatbots and discovering theirs. The winner is the player whose chatbot survives the longest (king of the hill). All skill levels are welcomed, even if this is your first time seeing code, securing a chatbot, or playing in a wargame.

Right at the start, there will be a briefing to show how to play in the wargame. Knowledge of the OpenAI Python SDK helps but is not a requirement. Each player has access to their chatbot source code repository where they can run, test, debug and push their changes.

</details>

<details><summary><strong>Pentest Copilot: Cursor for Pentesters</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Dhruva Goyal](https://img.shields.io/badge/Dhruva%20Goyal-informational) ![Sitaraman S](https://img.shields.io/badge/Sitaraman%20S-informational)

🔗 **Link:** [Pentest Copilot: Cursor for Pentesters](https://github.com/bugbasesecurity/pentest-copilot)  
📝 **Description:** Pentest Copilot is an open-source, AI-powered platform built to revolutionize penetration testing. Designed by bug bounty hunters, it seamlessly integrates a browser-based AI assistant with an interactive testing environment(optionally backed by a Kali Linux container). By enabling real-time command execution, context-aware automation, and dynamic checklists, Pentest Copilot creates a unified ecosystem where AI offsec automation and manual expertise work in tandem. Infosec pros can efficiently discover and exploit vulnerabilities without context-switching, ensuring precision, scalability, and efficiency in every engagement(bug bounty, professional or otherwise)

Previously a commercial tool, Pentest Copilot is now being open-sourced for the first time. The platform's agentic AI architecture leverages contextual reasoning, recursive automation loops, and adaptive decision-making to refine pentesting strategies dynamically. By preserving engagement context, optimizing tool execution, and intelligently summarizing findings, the AI enhances workflow efficiency without compromising control. We first introduced Pentest Copilot's architecture at Microsoft BlueHat and a whitepaper (https://arxiv.org/abs/2409.09493), and now, we intend to launch it as an open-source project at BlackHat Arsenal

</details>

<details><summary><strong>Patching at Scale - Using GenAI to keep up</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Yohan Guez](https://img.shields.io/badge/Yohan%20Guez-informational)

🔗 **Link:** [Patching at Scale - Using GenAI to keep up](https://github.com/aws-samples/gen-ai-cve-patching)  
📝 **Description:** Software security is constantly challenged by the difficulty of upgrading third party libraries. Codebases often lag several major versions behind, and the value of upgrading is frequently debated. A more practical approach can be backporting vulnerability fixes to the specific versions in use. Manually backporting security patches is a time-consuming, error-prone, and resource-intensive task for security and development teams. Our method utilizes LLM capabilities in combination with other techniques to efficiently streamline this process at scale, efficiently mitigating vulnerabilities across hundreds of packages by backporting thousands of fixes. Instead of requiring researchers to manually locate, isolate, and apply patches, our AI-powered system automates much of the workflow: understanding the patch, identifying the relevant code in the Git repository, applying the necessary changes, running tests, and iterating until the CVE is successfully patched and its corresponding unit tests pass. While LLMs offer a powerful new capability, they also present challenges. This talk will explore what works, what doesn't, and the advantages and disadvantages of using AI models for vulnerability backporting. We'll share real-world successes, discuss unexpected AI errors, and explain how we addressed gaps in test coverage. By collaborating with cybersecurity researchers, our AI-driven approach not only accelerates security patching but also ensures that critical fixes are applied without introducing breaking changes.

</details>

<details><summary><strong>Group alerts, events & logs into relevant attack flows</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![ezz Tahoun](https://img.shields.io/badge/ezz%20Tahoun-informational)

🔗 **Link:** [Group alerts, events & logs into relevant attack flows](https://github.com/ethansilvas/splunk-logs-and-investigations)  
📝 **Description:** The ATT&CK Flow Correlator is an open-source AI-driven tool designed to extract coordinated attack chains from noisy, heterogeneous security alert datasets. It uses a pipeline of open models — including LLMs, temporal knowledge graphs, clustering algorithms, and sequencers — to classify alerts with MITRE ATT&CK Techniques, group them into contextualized attack steps, and chain them into coherent, explainable killchains.

The tool includes modules for:

NLP-based ATT&CK technique classification (even for poorly labeled alerts),

Graph-based clustering (temporal, spatial, technical),

Sequence modeling (Markov Chains, RNNs, Transformers),

Generation of 3 actionable ticket types (False Positives, Incidents, Coordinated Attacks),

Integration-ready automation for SIEMs and SOC workflows (e.g., via Lambda, Sagemaker, SOAR).

The entire stack is cloud-native, cost-effective, and designed for accessibility — no deep ML knowledge required.

</details>

<details><summary><strong>Wabhawk/Catch - AI Powered Detection</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Walid Daboubi](https://img.shields.io/badge/Walid%20Daboubi-informational)

🔗 **Link:** [Wabhawk/Catch - AI Powered Detection](https://github.com/slrbl/unsupervised-learning-attack-detection-webhawk-catch)  
📝 **Description:** Webhawk/Catch helps automatically find web attack traces in application logs without using any preset rules. Based on the usage of unsupervised machine learning, our tool groups log lines into clusters, and detects the outliers it considers as potential attack traces.

</details>

<details><summary><strong>ThreatShield - The Intelligent way of Threat Modelling</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Satyam Nagpal](https://img.shields.io/badge/Satyam%20Nagpal-informational) ![Sayooj B Kumar](https://img.shields.io/badge/Sayooj%20B%20Kumar-informational) ![Ashwin Shenoi](https://img.shields.io/badge/Ashwin%20Shenoi-informational)

🔗 **Link:** [ThreatShield - The Intelligent way of Threat Modelling](https://github.com/threatshield/threatshield)  
📝 **Description:** ThreatShield is an AI-powered threat modeling and security analysis tool designed to automate and enhance threat modeling using OpenAI's enterprise API. It ingests raw security-relevant documents (such as PRDs, Confluence docs, architecture diagrams, meeting transcripts, and source code) and generates detailed STRIDE-based threat models. The output includes explicit threats, attack vectors, risk assessments, severity levels, and security recommendations, including a section for higher management in layman's terms.

</details>

<details><summary><strong>DataTrap - AI Based Data Driven Honeypot</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Ori Nakar](https://img.shields.io/badge/Ori%20Nakar-informational)

🔗 **Link:** [DataTrap - AI Based Data Driven Honeypot](https://github.com/ThalesGroup/dd-honeypot)  
📝 **Description:** We introduce DataTrap, an innovative and extensible honeypot system that emulates realistic behavior across TCP, HTTP, SSH, and various database protocols. Designed to simulate web applications, IoT devices, and databases, DataTrap goes beyond traditional honeypots by combining recorded payloads, metadata, and a large language model (LLM) to dynamically generate responses that closely mimic genuine application output.

This unique approach not only effectively deceives attackers but also delivers actionable insights—all while maintaining high performance, low cost of ownership, and operational efficiency. The system supports multiple applications and their different versions, and allows selective emulation of application components. Its modular architecture enables seamless extension of the network protocol layer to support additional applications and services over time.

At the heart of DataTrap is a continuously evolving dataset, which powers the LLM-based response generation. This dataset is central to the system's effectiveness and is actively maintained as part of the framework. LLM-generated responses are automatically integrated into the dataset, ensuring that the system adapts to emerging threats and stays up to date.

DataTrap is open-source, encouraging community contributions to enrich both the dataset and system capabilities. To simplify deployment, it is packaged as a Docker image, allowing users to run the honeypot system as a single container in any environment with minimal setup.

</details>

<details><summary><strong>Nemesis 2.0</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational) ![Lee Chagolla-Christensen](https://img.shields.io/badge/Lee%20Chagolla-Christensen-informational)

🔗 **Link:** [Nemesis 2.0](https://github.com/SpecterOps/Nemesis)  
📝 **Description:** Nemesis 2.0 is a ground-up rewrite of the Nemesis offensive data enrichment pipeline. We took two years of lessons learned and rebuilt Nemesis with a focus on extensibility, stability, and massively improved usability. We've narrowed the focus for Nemesis to its most used functionality: facilitating manual file triage for offensive operations. While platforms like VirusTotal revolutionized defensive file analysis, the offensive community lacks a centralized, scalable solution tailored to red team operations - exactly what Nemesis aims to be.

</details>

<details><summary><strong>Dumpsieve</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Sze Ying Tay](https://img.shields.io/badge/Sze%20Ying%20Tay-informational)

🔗 **Link:** [Dumpsieve](https://github.com/arthaud/git-dumper)  
📝 **Description:** During data leakage incident, time is taking to sieve through the data dump to identify if the leaked is relevant to the organisation. Time is crucial in investigation in order to perform impact and risk assessment for the organisation. Hence, the team has created a data dump tool named "Dumpsieve" which utilises AI to expedite the investigation.

</details>

<details><summary><strong>PERSEPTOR: Automating Detection Rule Generation with AI-Driven Threat Intelligence</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Aytek AYTEMUR](https://img.shields.io/badge/Aytek%20AYTEMUR-informational) ![Fatih ERDOGAN](https://img.shields.io/badge/Fatih%20ERDOGAN-informational)

🔗 **Link:** [PERSEPTOR: Automating Detection Rule Generation with AI-Driven Threat Intelligence](https://github.com/dipsh0v/perseptor)  
📝 **Description:** In an era of rapidly evolving cyber threats, organizations face constant challenges in detecting and mitigating sophisticated attacks.
Staying ahead of adversaries demands not only robust defense mechanisms but also intelligent systems capable of transforming raw threat data into actionable intelligence.

PERSEPTOR is a cutting-edge threat intelligence project designed to streamline the process of extracting actionable insights from diverse threat reports.
Leveraging state-of-the-art LLMs and the LangChain framework, PERSEPTOR autonomously summarizes threat reports, identifies TTPs, extracts IoCs, and generates Sigma and YARA rules using AI-driven mechanisms to minimize false positives.

The project also provides tailored query recommendations for various cybersecurity products, enhancing its practical adaptability across different operational environments.

PERSEPTOR specializes in automating detection content creation and prioritization, enabling Blue Teamers, SOC Analysts, Incident Responders, Threat Hunters, and Threat Detection Engineers to efficiently organize and implement detection rules.

Through real-time analysis, PERSEPTOR empowers these teams to effectively prioritize threats and optimize response strategies, significantly enhancing their ability to detect and mitigate emerging cyber threats.

This presentation delves into the conceptualization, development, and implementation of PERSEPTOR, highlighting its modular architecture, advanced AI-driven functionalities, and transformative impact on modern cybersecurity operations. Furthermore, the presentation will discuss the applicability of PERSEPTOR in cybersecurity operations through various use case examples.

</details>

<details><summary><strong>Dapr Agents: Agentic Workflows for Security</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Roberto Rodriguez](https://img.shields.io/badge/Roberto%20Rodriguez-informational)

🔗 **Link:** [Dapr Agents: Agentic Workflows for Security](https://github.com/dapr/dapr-agents)  
📝 **Description:** Agentic workflows represent a new frontier in how AI systems operate, moving beyond simple task completion toward iterative, dynamic processes. Unlike zero-shot prompting, where an LLM completes a single task in isolation, agentic workflows incorporate loops, branching decisions, and continuous refinement, making them particularly effective for complex domains like cybersecurity. Security workflows often demand more than linear task execution—they require sophisticated orchestration, adaptability, and collaboration between tools, agents, and functions to address challenges like incident investigation or attack path traversal.

In this talk, I will introduce Floki, an open-source framework designed to simplify the creation and orchestration of agentic workflows. Built on Dapr, Floki provides a powerful platform for researchers and developers to experiment with LLM-based autonomous agents. It enables agents to function as independent, self-contained units using Dapr's Virtual Actor pattern, eliminating concurrency concerns while seamlessly integrating into larger workflows. Floki also supports collaboration through Pub/Sub messaging, allowing agents to communicate efficiently and work together toward shared goals.

Using real-world security examples, we will explore how Floki facilitates deterministic and non-deterministic workflows, event-driven interactions, and chat-based agentic collaboration. From task chaining to fan-out/fan-in patterns, I'll demonstrate how Floki empowers researchers and practitioners to design and deploy agentic workflows that address the unique challenges of cybersecurity operations. This talk aims to provide both conceptual insights and practical guidance for advancing research and implementation in multi-agent systems.

</details>

<details><summary><strong>Harbinger: An AI-Powered Red Teaming Platform for Streamlined Operations and Enhanced Decision-Making</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Matthijs Gielen](https://img.shields.io/badge/Matthijs%20Gielen-informational) ![Idan Ron](https://img.shields.io/badge/Idan%20Ron-informational)

🔗 **Link:** [Harbinger: An AI-Powered Red Teaming Platform for Streamlined Operations and Enhanced Decision-Making](https://github.com/mandiant/harbinger)  
📝 **Description:** Tired of juggling multiple tools and struggling with data overload during red teaming engagements? Harbinger is an AI-powered platform that streamlines your workflow by integrating essential components, automating tasks, and providing intelligent insights. It consolidates data from various sources, automates playbook execution, and uses AI to suggest your next moves, making red teaming more efficient and effective. With Harbinger, you can focus on what matters most – achieving your objectives and maximizing the impact of your assessments.

</details>

<details><summary><strong>Red AI Range (RAR)</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Mahmut Erdem Ozgen](https://img.shields.io/badge/Mahmut%20Erdem%20Ozgen-informational) ![Ata Seren](https://img.shields.io/badge/Ata%20Seren-informational) ![Elif Basar Ozgen](https://img.shields.io/badge/Elif%20Basar%20Ozgen-informational) ![Muhammed Alparslan Akyildiz](https://img.shields.io/badge/Muhammed%20Alparslan%20Akyildiz-informational)

🔗 **Link:** [Red AI Range (RAR)](https://github.com/ErdemOzgen/RedAiRange)  
📝 **Description:** Red AI Range (RAR) is a comprehensive security platform designed specifically for AI red teaming and vulnerability assessment. It creates realistic environments where security professionals can systematically discover, analyze, and mitigate AI vulnerabilities through controlled testing scenarios.

As organizations increasingly integrate AI systems into critical infrastructure, the need for robust security testing has become essential. RAR addresses this need by providing a standardized framework that consolidates various AI vulnerabilities in one accessible environment for both academic research and industrial security operations.

Red AI Range enables security professionals to systematically assess and exploit vulnerabilities within AI systems through realistic, controlled attack scenarios. The platform's advanced Docker-based architecture resolves complex dependency issues inherent in AI frameworks, providing isolation, rapid environment resets, parallel testing capabilities, and simplified deployments. An intuitive management system streamlines deployment of vulnerable AI systems and security toolkits, offering straightforward controls via a user-friendly interface.

With remote agent support, teams can securely leverage distributed resources such as GPU-equipped clusters, coordinate across multiple locations, and manage testing scenarios from a centralized interface. Built-in session recording ensures comprehensive documentation, facilitates knowledge transfer, and supports stakeholder demonstrations. Suitable for corporate security teams, researchers, and educators, RedAiRange is ideal for vulnerability validation, exploration of emerging AI threats, practical skill development, and reproducible security research.

</details>

<details><summary><strong>LlamaFirewall: Guardrails for Controlling Agentic AI Systems</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Cyrus Nikolaidis](https://img.shields.io/badge/Cyrus%20Nikolaidis-informational) ![Kat He](https://img.shields.io/badge/Kat%20He-informational) ![Stephanie Ding](https://img.shields.io/badge/Stephanie%20Ding-informational) ![Sahana CB](https://img.shields.io/badge/Sahana%20CB-informational)

🔗 **Link:** [LlamaFirewall: Guardrails for Controlling Agentic AI Systems](https://github.com/meta-llama/PurpleLlama)  
📝 **Description:** Meta's AI Security team is releasing three new models under the LlamaFirewall framework, targeting a key challenge in deploying AI agents: controllability. Controllability means making sure an AI agent, even one handling sensitive data or high-stakes actions, sticks to the rules set by its developers or users. Without proper controls, an agent could stray from its goals or even be exploited, potentially leading to data leaks or unauthorized actions.

Using fine-tuning on small, pre-trained Llama models, our guardrails are more efficient and performant than previous solutions. Packaged within the LlamaFirewall framework, these compact models deliver a lightweight yet robust security layer that ensures AI agents remain safe and aligned with their intended purpose.

</details>

<details><summary><strong>All Talk, AI Action: Binary Analysis Toolkit MCP Server</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🤖 AI, ML & Data Science](https://img.shields.io/badge/Category:%20🤖%20AI,%20ML%20&%20Data%20Science-brightgreen) ![Wei-Chieh Chao](https://img.shields.io/badge/Wei-Chieh%20Chao-informational) ![Tien-Chih Lin](https://img.shields.io/badge/Tien-Chih%20Lin-informational) ![Zhao Min Chen](https://img.shields.io/badge/Zhao%20Min%20Chen-informational)

🔗 **Link:** [All Talk, AI Action: Binary Analysis Toolkit MCP Server](https://github.com/erew123/alltalk_tts)  
📝 **Description:** In the fields of cybersecurity and reverse engineering, traditional integrations of Large Language Models (LLMs) with tools like IDA Pro have faced significant challenges. Existing solutions not only heavily depend on manual intervention—requiring time-consuming, function-by-function analysis via the IDA Pro GUI—but also fail to effectively combine static and dynamic analysis. By exclusively focusing on static analysis, these methods risk overlooking crucial insights that dynamic analysis could reveal, resulting in a limited and fragmented approach.

To overcome these limitations, we propose an innovative framework centered around an MCP Server, serving as a unified interface. This approach transforms the LLM into a fully autonomous intelligent agent capable of managing a complete binary analysis workflow while drastically reducing human effort. Unlike traditional methods, our framework seamlessly integrates both static and dynamic analysis tools into a collaborative pipeline, ensuring a comprehensive examination of binary files. Additionally, utilizing the MCP Server enhances code reusability and scalability, aligning the process more closely with professional reverse engineering practices.

Key Points:
- Automation: Delegates the entire analysis process to the LLM with minimal human intervention.
- Comprehensive Analysis: Combines static and dynamic analysis to uncover deeper insights.
- Tool Reusability: Leverages a unified MCP Server interface to improve portability and scalability.

This paradigm shift in tool integration not only addresses the inherent shortcomings of traditional methods but also paves the way for a more efficient and thorough binary analysis system.

</details>

---
## 🔍 OSINT
<details><summary><strong>Ghost Scout - Phishing AI Agent</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational) ![Kieran Croucher](https://img.shields.io/badge/Kieran%20Croucher-informational) ![Rebecca Allor](https://img.shields.io/badge/Rebecca%20Allor-informational) ![Max Andreacchi](https://img.shields.io/badge/Max%20Andreacchi-informational)

🔗 **Link:** [Ghost Scout - Phishing AI Agent](https://github.com/SpecterOps/ghost_scout)  
📝 **Description:** Custom phishing emails consistently outperform generic pretexts on click-through metrics. In the past crafting custom emails to targets involved a lot of tedious OSINT to identify good targets, understand their interests and motivations, and write a customized message that would speak to them on a personal level. This method is simple, but highly effective. The only drawback is the time it takes; until now. We've written some simple OSINT tools so that an AI agent can do the OSINT grunt work for us, collect detailed profiles on our targets, and even write phishing emails for us.

</details>

<details><summary><strong>Exposor - A Contactless reconnaissance tool using internet search engines with a unified syntax</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Abdulla Abdullayev](https://img.shields.io/badge/Abdulla%20Abdullayev-informational)

🔗 **Link:** [Exposor - A Contactless reconnaissance tool using internet search engines with a unified syntax](https://github.com/abuyv/exposor)  
📝 **Description:** The attack surface of organizations is constantly evolving, making real-time discovery of exposed technologies and vulnerabilities critical for proactive security. However, conducting searches across multiple Search Engine requires understanding different query syntaxes, which can be time-consuming and inefficient.

Exposor is an open-source Contactless Reconnaissance tool that unifies searches across multiple intelligence feeds, allowing security professionals to identify exposed systems based on CPE (technology) or CVE (vulnerabilities) using a single, simplified query format. Instead of crafting queries for each platform separately, Exposor automatically maps queries to the correct syntax and retrieves results in parallel.

</details>

<details><summary><strong>Blackbird</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Lucas Antoniaci](https://img.shields.io/badge/Lucas%20Antoniaci-informational)

🔗 **Link:** [Blackbird](https://github.com/p1ngul1n0/blackbird)  
📝 **Description:** Blackbird is an OSINT tool that searches for user accounts across social networks by username and email. It supports over 500 platforms, offers a web-based interface, and provides exportable results for reconnaissance and digital footprint analysis.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Akheron Proxy - Interchip communication serial proxy</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Deral Heiland](https://img.shields.io/badge/Deral%20Heiland-informational) ![Matthew Kienow](https://img.shields.io/badge/Matthew%20Kienow-informational)

🔗 **Link:** [Akheron Proxy - Interchip communication serial proxy](https://github.com/rapid7/akheron-proxy)  
📝 **Description:** Akheron proxy is a serial communication proxy application tool designed to connect and proxy serial communication between microprocessors on a hardware circuit board. Allowing an embedded device testers to capture, decode, replay, and fuzz serial communications flowing between microprocessor on an embedded device circuit board in real time.

</details>

<details><summary><strong>WHIDBOARD: Plug it in, Set it up & Get ready to Hack!</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

🔗 **Link:** [WHIDBOARD: Plug it in, Set it up & Get ready to Hack!](https://github.com/whid-injector/WHIDBOARD)  
📝 **Description:** WHIDBOARD is the ultimate tool-suite for Hardware Hackers. It is designed to act as the perfect Swiss-Army-Knife for hacking any (I)IoT & Embedded devices. Thanks to its core controller (a.k.a. BRUSCHETTAPRO) it can support the interaction with multiple protocols (i.e. UART, SPI, I2C, JTAG & SWD) as well as different Logic Levels (i.e. 1.8V, 2.5V, 3.3V and the VREF of the target itself). Nonetheless, it also allows the hacker to enumerate (UART, JTAG & SWD) thanks to its 24 channels' Pin Enumerator feature, as well as the ability to act as a 8 channels Logic Analyzer at 24MHz.

</details>

<details><summary><strong>Minino: Multiband hacking now with GPS</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Paulino Calderon](https://img.shields.io/badge/Paulino%20Calderon-informational) ![Eduardo Contreras](https://img.shields.io/badge/Eduardo%20Contreras-informational)

🔗 **Link:** [Minino: Multiband hacking now with GPS](https://github.com/ElectronicCats/Minino)  
📝 **Description:** Minino is a Swiss Army knife for IoT hacking, designed to empower security professionals with a versatile, all-in-one toolkit for assessing and attacking IoT devices. Minino integrates WiFi, Bluetooth Low Energy (BLE), Zigbee, Thread, Matter, and a GPS module into a compact, open-source hardware solution.

IoT security is often fragmented, requiring multiple tools to assess protocols and attack vectors. Minino simplifies this process by consolidating essential offensive security functions into a single device, making it an indispensable asset for penetration testers, red teamers, and hardware hackers.

With the latest update, Minino can upload your wardriving data straight into wiggle.net and wardrive for hours with its battery saving mode.

This session will introduce real-world attack scenarios enabled by Minino, demonstrate its capabilities through live demos, and highlight its potential for uncovering new vulnerabilities. As an open-source project, Minino is built to evolve, with contributions from the security community driving continuous improvements.

</details>

<details><summary><strong>Glitch.IO - A Powerful, Fast, and Open-Source Framework for Fault Injection Attacks</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Ramiro Pareja Veredas](https://img.shields.io/badge/Ramiro%20Pareja%20Veredas-informational) ![Gabriel Gonzalez](https://img.shields.io/badge/Gabriel%20Gonzalez-informational)

🔗 **Link:** [Glitch.IO - A Powerful, Fast, and Open-Source Framework for Fault Injection Attacks](https://github.com/IOActive/Glitch.IO)  
📝 **Description:** Fault Injection (FI) attacks have been around since the late 90s but, until recently, they remained largely academic and considered not practical in the real-world. However, the popularity of these attacks has been growing for the last 10 years and today it is common to see them, not just in academia, but in security congresses and real-world attacks.

Despite this popularity, hardware hackers still do not have a reliable open-source tool for mounting FI attacks. Open-source tools already available are, either very limited, or they are just PoCs which cannot be easily adapted. Without better options, many hackers have to develop their own tools for fault injection, which requires a lot of time and deviates the effort from the actual target research.

We present Glitch.IO, a powerful, flexible and cheap glitcher that aims to be a standard in the hardware hackers toolbox.
Glitch.IO is not just a hardware able to inject glitches, it is also a software framework designed to facilitate the coding of FI test applications. It includes a library FI attacks - called "recipes" - to facilitate the reproduction of publicly known attacks.

During the presentation we will introduce the tool and demonstrate how to use a "recipe" to break the JTAG protection of a microcontroller or to characterise and bypass the Raspberry Pico 2 FI countermeasures.

</details>

<details><summary><strong>(Evil)Doggie: A modular open-source CAN bus research and penetration testing tool</strong></summary>

![USA 2025](https://img.shields.io/badge/USA%202025-black) ![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Octavio Gianatiempo](https://img.shields.io/badge/Octavio%20Gianatiempo-informational) ![Gaston Aznarez](https://img.shields.io/badge/Gaston%20Aznarez-informational)

🔗 **Link:** [(Evil)Doggie: A modular open-source CAN bus research and penetration testing tool](https://github.com/susandoggie/doggie)  
📝 **Description:** Doggie is a modular, flexible, open-source adapter that bridges the gap between a computer and a CAN Bus network using USB or Bluetooth. It was built with affordability and adaptability in mind.

Its compatibility with SocketCAN, Python-can, and other slcan-compatible software ensures seamless integration with existing CAN Bus analysis, sniffing, and injection tools on different operating systems. Doggie also supports ISO-TP, making it perfect for standard and advanced CAN Bus applications. Whether running diagnostics, experimenting with custom in-car functionalities, or performing penetration tests, Doggie provides the tools you need to succeed.

EvilDoggie is the offensive firmware variant of Doggie with a set of techniques to expand the device's capabilities for low-level CAN bus research. It implements frame, protocol, and physical attacks for CAN, including spoofing, double receive, and bus takeover attacks.

The project emphasizes modularity, allowing users to select from various hardware configurations using different microcontrollers and CAN transceivers, making it accessible and cost-effective.

</details>

---