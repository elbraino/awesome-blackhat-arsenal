# Asia 2021
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2021** event held in **Asia**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Adversarial Threat Detector</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational)

🔗 **Link:** [Adversarial Threat Detector](https://github.com/gyoisamurai/Adversarial-Threat-Detector)  
📝 **Description:** In recent years, deep learning technology has been developing, and various systems using deep learning are spreading in our society, such as face recognition, security cameras (anomaly detection), and ADAS (Advanced Driver-Assistance Systems).

On the other hand, there are many attacks that exploit vulnerabilities in deep learning algorithms. For example, the Evasion Attacks are an attack that causes the target classifier to misclassify the Adversarial Examples into the class intended by the adversary. The Exfiltration Attacks are an attack that steals the parameters and train data of a target classifier. If your system is vulnerable to these attacks, it can lead to serious incidents such as face recognition being breached, allowing unauthorized intrusion, or information leakage due to inference of train data.

So we released a vulnerability scanner called "Adversarial Threat Detector" (a.k.a. ATD), which automatically detects vulnerabilities in deep learning-based classifiers.

ATD contributes to the security of your classifier by executing the four cycles of "Detecting vulnerabilities (Scanning & Detection)", "Understanding vulnerabilities (Understanding)", "Fixing vulnerabilities (Fix)", and "Check fixed vulnerabilities (Re-Scanning)".

1. Detecting vulnerabilities（Scanning & Detection）
ATD automatically executes a variety of attacks against the classifier and detects vulnerabilities.

2. Understanding vulnerabilities (Understanding)
When a vulnerability is detected, ATD will generate a countermeasure report (HTML style) and a replay environment (ipynb style) of the vulnerabilities. Developers can understand the vulnerabilities by referring to the countermeasure report and the replay environment.

3. Fixing vulnerabilities (Fix)
ATD automatically fixes detected vulnerabilities.

4. Check fixed vulnerabilities (Re-Scanning)
The ATD checks fixed vulnerabilities of the fixed classifier.

Our "Adversarial Threat Detector" will contribute greatly to keep your safety.

</details>

<details><summary><strong>Demystifying the State of Kubernetes Cluster Security - The Cloud Native Way</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Vasant Chinnipilli](https://img.shields.io/badge/Vasant%20Chinnipilli-informational) ![Rupali Dash](https://img.shields.io/badge/Rupali%20Dash-informational)

🔗 **Link:** Not Available  
📝 **Description:** Attackers always get better with new attack techniques, so our threat modelling and defense mechanisms needs to level up.

The security of the Kubernetes cluster, of course, cannot be achieved in a single process. There are many moving parts within the Kubernetes cluster that must be properly secured.

Kube-striker performs numerous in depth checks on kubernetes infra to identify the security misconfigurations and challenges that devops/developers are likely to encounter when using Kubernetes.

Kube-striker is Platform agnostic and works equally well across more than one platform such as self hosted kubernetes, EKS, AKS, GKE etc.

</details>

---
## Others
<details><summary><strong>AOP-Based Runtime Security Analysis Toolkit</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Juhu Nie](https://img.shields.io/badge/Juhu%20Nie-informational) ![Hao Zhao](https://img.shields.io/badge/Hao%20Zhao-informational)

🔗 **Link:** Not Available  
📝 **Description:** We will release an open source runtime security analysis toolkit, aosanalyzer, for Android application. This tool is mainly used to find application security vulnerabilities and privacy leaks that are difficult to find by static APK analysis. The aosanalyzer uses aspect-oriented programming in security technology to insert code into critical paths of the application to record the runtime information (e.g., the stack trace, parameters, UI events, etc.), and then produces a report with security issues highlights. These critical paths are configurable and the aosanalyzer tool includes a default configuration. Developers and security researchers can observe the detailed runtime information of the application to find vulnerability and privacy leak issues without requiring any modification of the APK. Relying on this tool, we have discovered dozens of security vulnerabilities due to lack of parameter validation and privacy leaks issues.

</details>

<details><summary><strong>Drone Monitoring and Takedown System (DMTS)</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Pengfei Yu](https://img.shields.io/badge/Pengfei%20Yu-informational) ![Anders Soh](https://img.shields.io/badge/Anders%20Soh-informational) ![Yong Wen Chan](https://img.shields.io/badge/Yong%20Wen%20Chan-informational)

🔗 **Link:** Not Available  
📝 **Description:** The rise of commercial drones/Unmanned Aerial Vehicles (UAV) has dramatically changed several industries and our daily lives. This emergence is also challenging our concept of safety, security, privacy and regulation. With their ability to amass data and transport loads, drones are changing our views about our physical environment. Commercial drones are now used for surveying, inspecting and imaging with more technological advancements being pushed out by active communities of hobbyists and enthusiasts. Although their commercial use has been criticised by both individuals and activist organisations, this tension presents unique challenges to integration in the current public, government and private sectors. Recent incidents regarding drone disruptions and malicious activities has further cemented the fact that there is a lack in control and regulation of drones. Thus, we created DMTS as an automated drone-to-drone solution that hopefully helps to alleviate our regulatory and physical security needs.

</details>

<details><summary><strong>LIFARS IOC-Checker + Log-Checker = Accelerate Your DFIR With the Power of Threat Intelligence</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Viliam Kacala](https://img.shields.io/badge/Viliam%20Kacala-informational) ![Ladislav Baco](https://img.shields.io/badge/Ladislav%20Baco-informational)

🔗 **Link:** Not Available  
📝 **Description:** IocChecker is a new utility to find indicators of compromise.
It is a full-stack application comprising a CLI probe, DB backend, and a Web admin console.
IOCs are defined using a custom tree-based JSON format with the support of conversion from/to MISP.
It searches IOCs using the following criteria also with the support of regular expressions:
- Filename/hash,
- Running process name/hash,
- Windows registry name/value,
- DNS address,
- Open network connections by name/IP,
- Certificate name,
- Process mutex.

LogChecker is a new Windows and Linux tool for scanning log files, developed by LIFARS. It extracts IP addresses, domain names, and hashes from the input file. Findings are checked in the YETI Threat Intelligence database. It supports Windows EVTX logs, text-based logos, or any plaintext files. Output can be in CSV format for better human readability or in JSON for computer processing.

</details>

<details><summary><strong>Project Enigma: Detecting Indicators of Compromise Through Ram Analysis, Event Logs and Malware Machine Learning</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Kevin Tan](https://img.shields.io/badge/Kevin%20Tan-informational) ![Patrick Kang Wei Sheng](https://img.shields.io/badge/Patrick%20Kang%20Wei%20Sheng-informational) ![Wei Han Goh](https://img.shields.io/badge/Wei%20Han%20Goh-informational)

🔗 **Link:** [Project Enigma: Detecting Indicators of Compromise Through Ram Analysis, Event Logs and Malware Machine Learning](https://github.com/amysen/BR_Algothon/blob/master/auth_index.csv)  
📝 **Description:** The team has developed an integrated solution to aid DFIR investigators by swiftly and effectively determining indicators of compromise (IOC) when responding to cyber security incidents, to steer and guide follow up investigations in the right direction. The solution consists of a hardware Bash Bunny for data triage and our software with a trilogy of modules - a security event log analyzer, a PE static analyzer, and an IOC detector. This integrated solution aims to provide automation whenever possible, reducing manual labor and associated errors that may come with it.

</details>

<details><summary><strong>Scared: A Side-Channel Attacks Framework</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Benjamin Timon](https://img.shields.io/badge/Benjamin%20Timon-informational)

🔗 **Link:** [Scared: A Side-Channel Attacks Framework](https://github.com/Hsword/Awesome-Machine-Learning-System-Papers/blob/main/README.md)  
📝 **Description:** Side-channel attacks regularly get under the spotlight with large scale exploits such as Spectre, Meltdown or very recently the side-channel exploit on the Google Titan security key.

In the background, side-channel attacks have been studied and evaluated in embedded products for more than 20 years. Today, the state-the-art includes multiple attack techniques and countermeasures. Still, open resources on side-channel attacks are limited and it is sometimes challenging to get started with this topic which involves a mix of cryptography, security and data science.

With Scared, our objective is to provide an intuitive Python framework implementing the state-of-the-art side-channel attacks and optimized for analysis of large datasets.

In addition, the project includes a growing set of Python notebooks which provide an easy entry point to the project with examples of how to use the library and apply it on CTF challenges.

Whether you want to learn more about side-channel attacks, do research, or solve some CTF challenges, Scared provides the right framework for you.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>CANalyse: A Vehicle Network Analysis and Attack Tool</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Kartheek Lade](https://img.shields.io/badge/Kartheek%20Lade-informational)

🔗 **Link:** [CANalyse: A Vehicle Network Analysis and Attack Tool](https://github.com/KartheekLade/CANalyse)  
📝 **Description:** CANalyse is a software tool built to analyze the log files to find out unique data sets automatically and able to connect to simple attacker interfaces such as Telegram. Basically, while using this tool you can provide your bot-ID and be able to use the tool over the internet through telegram. It is made to be installed inside a raspberry-PI and able to exploit the vehicle through a telegram bot by recording and analyzing the data logs, it is like a hardware implant planted inside a car which acts as a bridge between the Telegram bot and the Vehicle's network.

</details>

<details><summary><strong>CDK: Zero Dependency Container Penetration Toolkit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Yue Xu](https://img.shields.io/badge/Yue%20Xu-informational) ![Zebin Zhou](https://img.shields.io/badge/Zebin%20Zhou-informational)

🔗 **Link:** Not Available  
📝 **Description:** CDK is an open-sourced container penetration toolkit, offering stable exploitation in cloud-native docker/k8s/serverless deployments. It comes with many powerful tools and exploits without any OS dependency, helps you to escape container and takeover K8s cluster easily.

</details>

<details><summary><strong>Empire: Post-Exploitation Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Anthony Rose](https://img.shields.io/badge/Anthony%20Rose-informational) ![Jake Krasnov](https://img.shields.io/badge/Jake%20Krasnov-informational)

🔗 **Link:** [Empire: Post-Exploitation Framework](https://github.com/txuswashere/Pentesting-Windows/blob/main/README.md)  
📝 **Description:** Empire is a Command and Control (C2) framework powered by Python 3 that supports Windows, Linux, and macOS exploitation. It leverages many widely used offensive security tools through PowerShell, Python 3, and C# agents. At the same time, it offers cryptologically-secure communications and flexible modular architecture that links Advanced Persistent Threats (APTs) Tactics, Techniques, and Procedures (TTPs) through the MITRE ATT&CK database.

Empire has evolved significantly since its introduction in 2015 and has become one of the most widely used open-source C2 platforms. Through this time, Empire has advanced from a single user experience to allowing multiple user operations through an API with Empire acting as a teamserver. Currently, 2 different applications are available to connect to the Empire teamserver: Empire Command Line Interface (CLI) and Starkiller.

The Empire CLI is built from the ground up as a replacement to the embedded legacy CLI and gives users a familiar feel of the legacy CLI, but is portable and connects through the Empire API. While Starkiller is a cross-platform UI available in Linux, Windows, and macOS powered by ElectronJS.

The framework's flexibility to easily incorporate new modules allows for a single solution for red team operations with the aim for Empire to provide an easy-to-use platform for emulating APTs. Customization is essential to any successful red team operation, which has driven the expansion of user plugins. These plugins allow any custom program to run side-by-side with the Empire teamserver. In addition, the commonality between other C2 platforms allows profiles and modules to be easily dropped in without the need for additional development. These features allow both red and blue teams to easily emulate and defend against the APT attack vectors.

</details>

<details><summary><strong>OWFuzz: WiFi Protocol Fuzzing Tool Based on OpenWiFi</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Hongjian Cao](https://img.shields.io/badge/Hongjian%20Cao-informational)

🔗 **Link:** [OWFuzz: WiFi Protocol Fuzzing Tool Based on OpenWiFi](https://github.com/alipay/Owfuzz/blob/main/README.md?plain=1)  
📝 **Description:** Generally, when using WiFi Fuzzing Tool to test the security of WiFi protocol, you need a WiFi USB dongle that supports monitor mode and set the WiFi USB dongle to monitor mode to listen and inject arbitrary WiFi frames. However, many WiFi USB dongles fail to meet our expectations. For example, some are not stable enough in monitor mode and often get stuck, which leads to the interruption of the fuzzing process. And some, we don't have complete control over some frame fields.

OWFuzz is a WiFi protocol testing tool using OpenWiFi. OpenWiFi is an open-source WiFi protocol stack based on SDR that is fully compatible with Linux mac80211. It's driver takes advantage of the Linux kernel's supports (mac80211, cfg80211) for WiFi high MAC, so it can provide an interface to the application layer like a common WiFi USB dongle. In The hardware part, CSMA/CA protocol and other functions of WiFi low MAC layer are implemented on FPGA. It supports monitoring and injection of arbitrary WiFi frames，The application layer software can also directly communicate with the OpenWiFi driver/FPGA/RF underlying functions through nl80211, which provides users with great autonomous and controllable ability. OWFuzz is the first to use OpenWiFi platform (Xilinx ZC706 dev board + FMCOMMS3) to implements a WiFi protocol fuzzing test framework, which supports the fuzzing test of all WiFi frames and the interactivity testing of WiFi protocols.

This research introduces a comprehensive overview of the OWFuzz. We will introduce its architecture, implementation (arbitrary frame and protocol interactivity fuzzing test), and how it works. And finally we will have a video demonstration.

</details>

<details><summary><strong>Red Kube</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Or Azarzar](https://img.shields.io/badge/Or%20Azarzar-informational)

🔗 **Link:** [Red Kube](https://github.com/KaplanOpenSource/israeli-opensource-companies)  
📝 **Description:** Red Kube is a red team cheat sheet based on kubectl commands to Asses the Kubernetes Cluster Security Posture.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>FalconEye: Windows Process Injection Techniques - Catch Them All</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rajiv Kulkarni](https://img.shields.io/badge/Rajiv%20Kulkarni-informational) ![Rex Guo](https://img.shields.io/badge/Rex%20Guo-informational) ![Sushant Paithane](https://img.shields.io/badge/Sushant%20Paithane-informational)

🔗 **Link:** Not Available  
📝 **Description:** Process injection (PI) in Windows has been a well-known security topic for many years. It is used to gain more stealth because it does not create additional processes in the system that could attract unwanted attention from the defender. It is also used to bypass security products that have limited visibility into the injection behaviors. Since PI techniques use legitimate windows APIs, detecting them becomes a challenging task.

FalconEye provides comprehensive detection for true PI techniques in real-time. True PIs inject into target processes which are already running. Pre-execution injections such as AppInit and process hollowing are not in scope. To the best of our knowledge, we analyzed all the publicly known PI techniques and our tool is able to detect all of them without false positives during our testing.

We identify PI behavior invariants that are unique compared to benign program behaviors but are common between various PI techniques. Based on the behavior invariants, we divide PI detections into three classes:
(1) Stateless detection
(2) Stateful detection
(3) Floating code detection

We propose a comprehensive detection algorithm to detect these behavior invariants classes. Our detection algorithm relies on two instrumentation primitives:
(1) System call interception
(2) Kernel callbacks

Based on our testing, the detection is compatible with Windows 10 1903 and previous versions. Evaluation results show that the detection is effective and has low overhead. Additionally, the generic detection mechanisms are also proven to detect newer PI techniques.



GitHub - rajiv2790/FalconEye

</details>

<details><summary><strong>Identify iOS Malicious Code Based on MachO File Structure</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Shijie Cao](https://img.shields.io/badge/Shijie%20Cao-informational)

🔗 **Link:** [Identify iOS Malicious Code Based on MachO File Structure](https://gist.github.com/LucaMell/bb7fa6c7ff58f5869b793e7ba85a187d?short_path=897e916)  
📝 **Description:** iOS Malicious Bit Hunter is a malicious plug-in detection engine for iOS applications. It can analyze the head of the macho file of the injected dylib dynamic library based on runtime, and can perform behavior analysis through interface input characteristics to determine the behavior of the dynamic library feature. The program does not rely on the jailbreak environment and can be used on the AppStore.

</details>

<details><summary><strong>Suricata: An Open-Source IDS/IPS/NSM Engine</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Josh Stroschein](https://img.shields.io/badge/Josh%20Stroschein-informational) ![Peter Manev](https://img.shields.io/badge/Peter%20Manev-informational)

🔗 **Link:** Not Available  
📝 **Description:** Suricata is a free and open-source, mature, fast, and robust network threat detection engine. The Suricata engine is capable of real-time intrusion detection (IDS), inline intrusion prevention (IPS), network security monitoring (NSM), and offline PCAP processing.

Suricata inspects the network traffic using a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats. With standard input and output formats like YAML and JSON integrations with tools like existing SIEMs, Splunk, Logstash/Elasticsearch, Kibana, and other database become effortless.

Suricata's fast-paced community driven development focuses on security, usability, and efficiency.

The Suricata project and code are owned and supported by the Open Information Security Foundation (OISF), a non-profit foundation committed to ensuring Suricata's development and sustained success as an open source project.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Ghidra-EVM: Reversing Smart Contracts with Ghidra</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Antonio de la Piedra](https://img.shields.io/badge/Antonio%20de%20la%20Piedra-informational)

🔗 **Link:** Not Available  
📝 **Description:** In the last few years, attacks on deployed smart contracts in the Ethereum blockchain have ended up in a significant amount of stolen funds due to programming mistakes. Since smart contracts, once compiled and deployed, are complex to modify and update different practitioners have suggested the importance of reviewing their security in the blockchain where only Ethereum Virtual Machine (EVM) bytecode is available. In this respect, reverse engineering through disassemble and decompilation can be effective.

Ghidra-EVM is a Ghidra module for reverse engineering smart contracts. It can be used to download Ethereum Virtual Machine (EVM) bytecode from the Ethereum blockchain and disassemble and decompile the smart contract. Further, it can analyze creation code, find contract methods and locate insecure instructions.

</details>

<details><summary><strong>Qiling: Smart Analysis for Smart Contract</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![KaiJern Lau](https://img.shields.io/badge/KaiJern%20Lau-informational) ![ChenXu Wu](https://img.shields.io/badge/ChenXu%20Wu-informational) ![ZiQiao Kong](https://img.shields.io/badge/ZiQiao%20Kong-informational)

🔗 **Link:** Not Available  
📝 **Description:** Ethereum Virtual Machine (EVM) is the most widely used architect to support the core of smart contracts. Many existing EVM emulators are just debugging tools based on symbolic execution. Unfortunately, these engines are just simple tools that do not encourage and support us to develop tools on top of them.

To raise the bar, we extended Qiling [1] to support EVM smart contracts (so Qiling is not just limited to analyze machine binary code, but also works for smart contracts) . Our framework offers some key features as follows.

- Analyze smart contracts only with their bytecode, without requiring source codes.
- Can instrument smart contracts at various level: instruction, code, event and activity
- Rule based dynamic smart contract analysis
- Not just limited to EVM smart contracts, but is also compatible with other EVM based smart contracts, supporting modern smart contract requirements.

In this talk, we will present our instrument-able EVM based smart contract framework. With our framework, users will be able to build all kinds of tools on top of it. For example, one could develop a scanner to test the corresponding smart contracts and even perform an automated analysis against smart contracts.

To demonstrate the power of our framework, we built an ultra-fast fuzzer for smart contract, using coverage guided technique. We extended the traditional binary fuzzer named AFL for this. Our fuzzer can efficiently discover typical vulnerabilities in EVM smart contracts, without requiring contract source code.

</details>

---
## 🔍 OSINT
<details><summary><strong>GitDorker: I'm in Your GitHub Dorking All Your Secrets</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Omar Bheda](https://img.shields.io/badge/Omar%20Bheda-informational)

🔗 **Link:** Not Available  
📝 **Description:** GitDorker is a tool that utilizes the GitHub Search API and an extensive list of GitHub dorks that I've compiled from various sources to provide an overview of sensitive information stored on GitHub given a search query.

The primary purpose of GitDorker is to provide the user with a clean and tailored attack surface to begin harvesting sensitive information on GitHub. GitDorker can be used with additional tools such as GitRob or Trufflehog on interesting repos or users discovered from GitDorker to produce best results.

</details>

<details><summary><strong>Quark Engine: Storyteller of Android Malware</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![JunWei Song](https://img.shields.io/badge/JunWei%20Song-informational) ![KunYu Chen](https://img.shields.io/badge/KunYu%20Chen-informational) ![YuShiang Dang](https://img.shields.io/badge/YuShiang%20Dang-informational) ![IokJin Sih](https://img.shields.io/badge/IokJin%20Sih-informational)

🔗 **Link:** Not Available  
📝 **Description:** Quark is one of the most popular analysis engines for hunting threat intelligence inside the APK files. Since it is rule-based, you can use the ones built-in or customize as needed.

With ideas decoded from criminal law, Quark has its unique angles for malware analysis. We developed a Dalvik bytecode loader that has tainted analysis inside but also defeats the obfuscation techniques used against reverse engineering. And surprisingly, the loader matches perfectly the design of our malware scoring system.

Features/Progress in recent versions of Quark:
1. Public Reports: AhMyth RAT and Roaming Mantis. And we give out all detection rules used in the reports
2. Call Graphs for behavior detected
3. Behavior Classification
4. New Strategy for Generating Rules
5. Open-Sourced all codes for rule generation
6. Python Binding APIs: Made Quark easy to be integrated.
7. Integrated to Intel Owl, BlackArch Linux, Pithus/Bazaar and APKLAB

In recent versions of Quark, we put huge efforts into making it more useful and practical. We have public reports that analyze classic samples like AhMyth RAT and Roaming Mantis. And we gave out all detection rules used in these reports!

In those reports, we show how users can use new features of Quark to quickly realize how the malware works. For example, malware analysts now can use Quark to generate call graphs of each behavior detected. And we also provide a feature that can automatically classify the detected behaviors in APK so as to boost up the storytelling of malware.

Moreover, to make Quark a more practical tool to use, we developed a new strategy for generating detection rules. The new strategy improves the effectiveness of the rules and efficiency of the generating process. Even better, we open-sourced all codes for everyone.

With the usefulness of Quark, we now have developed python binding APIs for integration with other open-source projects. Now you can use Quark in projects like Intel Owl, BlackArch Linux, Pithus/Bazaar, and APKLAB. We'll be demonstrating how Quark enriches our partners during the presentation.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>KICS</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Erez Yalon](https://img.shields.io/badge/Erez%20Yalon-informational) ![Ori Bendet](https://img.shields.io/badge/Ori%20Bendet-informational)

🔗 **Link:** [KICS](https://github.com/bashis/The-Federation-WWE-Roster-Viewer/blob/master/Resources%20(READ%20README!)/wrestlers/wrestlergen/last.txt)  
📝 **Description:** KICS is an open-source solution for static code analysis of Infrastructure as Code. It finds security vulnerabilities, compliance issues, and infrastructure misconfigurations in the following Infrastructure as Code solutions: Terraform, Kubernetes, Docker, AWS CloudFormation, Ansible. And more to come. Over 1000 rules are already available.

</details>

---
## 🧠 Social Engineering / General
<details><summary><strong>SniperPhish: The Web-Email Spear Phishing Toolkit</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Gem George](https://img.shields.io/badge/Gem%20George-informational)

🔗 **Link:** [SniperPhish: The Web-Email Spear Phishing Toolkit](https://github.com/GemGeorge/SniperPhish)  
📝 **Description:** Spear Phishing campaigns are commonly used to test employees' awareness in a company/organization. This exercise involves mostly the combination of phishing emails and websites. An effective campaign requires sophisticated methods starting from designing a phishing website to executing payload at the target in an undetectable manner. A platform is required to send emails to targeted users and tracking campaign progress. This basically involves the use of a mail server (to send email) and a web server (to host phishing website). To collect campaign data, these two domains need to be considered. Precisely, the campaign required to track email delivery status and the data submitted in the phishing website.

Usually, the data from these two domains can be collected easily, but it is more challenging and time-consuming when these data are to be consolidated and address questions such as which victim in the mail submitted data through the website. SniperPhish comes in handy here so that the data is tracked centrally, and displays the consolidated data in its dashboard.

SniperPhish is an advanced Web-Email spear-phishing toolkit developed in PHP to conduct professional phishing assessments. The abstract idea behind this toolkit is to simulate, combine, and centrally track all campaigns that involve email and phishing websites. SniperPhish supports tracking data from web site containing n number of pages. The data submitted in the phishing website containing multiple pages are tracked sequentially with email campaigns. The advanced customization in the report generation module helps to customize column fields and export in multiple outputs. In addition to the core campaign module, SniperPhish also provides additional functionalities such as hosting phishing websites, payload generation, encryption options, and options to convert payloads to FUD using different methods (eg: conversion to reflective DLL/PE).

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Threagile: The Open-Source Agile Threat Modeling Toolkit</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Christian Schneider](https://img.shields.io/badge/Christian%20Schneider-informational)

🔗 **Link:** [Threagile: The Open-Source Agile Threat Modeling Toolkit](https://github.com/cschneider4711)  
📝 **Description:** The open-source tool Threagile enables agile teams to create a threat model directly from within the IDE using a declarative approach: Given information about the data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules, which can be extended with custom risk rules, against the processed model. The resulting artifacts are graphical diagrams, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state. DevSecOps pipelines can be enriched with Threagile as well to process the JSON output.

</details>

---