# USA 2020
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2020** event held in **USA**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
- [🧠 Social Engineering / General](#🧠-social-engineering-general)
---
## 🧠 Social Engineering / General
<details><summary><strong>A DECEPTICON and AUTOBOT walk into a bar: A NEW Python tool for enhanced OPSEC</strong></summary>

![Category: 🧠 Social Engineering / General](https://img.shields.io/badge/Category:%20🧠%20Social%20Engineering%20/%20General-pink) ![Joe Gray](https://img.shields.io/badge/Joe%20Gray-informational)

🔗 **Link:** [A DECEPTICON and AUTOBOT walk into a bar: A NEW Python tool for enhanced OPSEC](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/AnonOpSecPrivacy.md)  
📝 **Description:** When we see the terms Natural Language Processing (NLP) or Machine Learning (ML), often, our guts are correct, and it is vendor marketing material, frequently containing FUD. After tinkering with various libraries in Python and R with the use of some OSINT and SOCMINT techniques, I have found a use for NLP and ML that is 100% FUD free in the form of a brand new, Python-based tool.

In this presentation, which goes further than the previous DECEPTICON presentation, we address topics that I have frequently spoken about in past years is disinformation, deception, OSINT, and OPSEC. When working through learning NLP and ML in Python, it dawned on me: marry these technologies with DECEPTICON for good. Enter the DECEPTICON bot. The DECEPTICON bot is a python* based tool that connects to social media via APIs to read posts/tweets to determine patterns of posting intervals and content then takes over to autonomously post for the user. What is the application you ask: people who are trying to enhance their OPSEC and abandon social media accounts that have been targeted without setting off alarms to their adversaries. Use case scenarios include public figures, executives, and, most importantly – domestic violence and trafficking victims.

</details>

---
## Others
<details><summary><strong>Apk-medit: memory search and patch tool for APK without root & android NDK</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Taichi Kotake](https://img.shields.io/badge/Taichi%20Kotake-informational)

🔗 **Link:** Not Available  
📝 **Description:** Apk-medit is a memory search and patch tool for debuggable APK without root & android NDK. It was created for mobile game security testing.


Memory modification is the easiest way to cheat in games, it is one of the items to be checked in the security test. There are also cheat tools that can be used casually like GameGuardian. However, there were no tools available for non-root devices and CUI, so apk-medit was created as a security testing tool.


Many mobile games have rooting detection, but apk-medit does not require root privileges, so memory modification can be done without bypassing the rooting detection.


GitHub: https://github.com/aktsk/apk-medit

</details>

<details><summary><strong>AutoGadgetFS: USB testing made easy</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ehab Hussein](https://img.shields.io/badge/Ehab%20Hussein-informational)

🔗 **Link:** [AutoGadgetFS: USB testing made easy](https://github.com/ehabhussein/AutoGadgetFS)  
📝 **Description:** AutoGadgetFS is an open source framework that allows users to assess USB devices and their associated hosts/drivers/software without an in-depth knowledge of the USB protocol.

The tool is written in Python 3 and uses RabbitMQ and WiFi access to enable researchers to conduct remote USB security assessments from anywhere around the globe. By leveraging ConfigFS, AutoGadgetFS allows users to clone and emulate devices quickly, eliminating the need to dig deep into the details of each implementation. The framework also allows users to create their own fuzzers on top of it. The total cost is around $10, the cost of a Raspberry Pi Zero with WiFi enabled.

</details>

<details><summary><strong>BlueRepli Plus</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Sourcell Xu](https://img.shields.io/badge/Sourcell%20Xu-informational) ![Xin Xin](https://img.shields.io/badge/Xin%20Xin-informational)

🔗 **Link:** Not Available  
📝 **Description:** Every Android phone loves Bluetooth, a short-range wireless communication technology. We can find a large number of Bluetooth devices in any public place. Many of their security issues have been exposed before, such as BlueBorne, KNOB, and BadBluetooth. Today, due to the security risks in AOSP (Android Open Source Project) and the negligence of some well-known mobile phone manufacturers, we designed a new attack idea and dug a new 0day BlueRepli (Bluetooth Replicant). At the same time, we have implemented the relevant utility tool on the customized universal hardware platform and called it BlueRepli Plus.

With BlueRepli Plus users can scan the surrounding Android phones via Bluetooth and attack any Android phones found. If the target Android phone has a BlueRepli vulnerability, the user can obtain the phone's address book, SMS message, or send a fake text message without the target feeling; if the target Android phone is not affected by the BlueRepli vulnerability, the tool allows the user to disguise as a well-known Application name or other very confusing names, to deceive the target, obtain permissions, and finally achieve the same attack effect.

</details>

<details><summary><strong>Cylons: An automated IoT security assessment platform based on OpenWRT</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Wei Wang](https://img.shields.io/badge/Wei%20Wang-informational) ![Jianqiang Wu](https://img.shields.io/badge/Jianqiang%20Wu-informational) ![Qianwei Hu](https://img.shields.io/badge/Qianwei%20Hu-informational)

🔗 **Link:** Not Available  
📝 **Description:** Smart/IoT devices these days are all about network, Internet in particular. When a box gets itself connected to the cloud, it exposes lots of attack surface as well. Hence, network assessment plays a fundamental role in IoT SDL (Security Development Lifecycle) practices. We have built a platform which aims to help security engineers to automate some common assessment workloads, black-box testing specifically.

With the help of OpenWRT, we are freed from wired/wireless network setup work, thus focusing more on traffic monitoring and parsing. Once a device got connected, Cylons can automatically accomplish tasks like:
- Packet capture, protocol parsing and logging
- Active port scan and passive port discovery
- DNS poisoning
- TCP session reset and injection
- Simple client fuzzing based on TCP injection
- TLS MITM Proxy and SNI Proxy, to detect insecure TLS validation
- TLS security check, to detect outdated ciphersuites, versions and configurations
- Sensitive strings match over clear-text traffic
- Generating knowledge graph for network endpoints

Apart from these core functions, Cylons also offers some other convenient features, such as RESTful API interface, LuCI-based WebUI and integration of SSL Labs APIs.

Performance is an inevitable challenge for any network-oriented tools. In order to achieve decent performance without compromising security, Cylons is fully written in Rust, with little "unsafe" code. Rust also enables us to easily cross-build for different targets like ARM, AARCH64 and MIPS, which shares the same goals as OpenWRT.

Cylons is still in heavy development, we are trying to bring more features and make it more powerful and robust. One major goal is to add support for radio protocol assessments, including WiFi, BLE and Zigbee.

</details>

<details><summary><strong>Mobile Security Framework - MobSF</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Ajin Abraham](https://img.shields.io/badge/Ajin%20Abraham-informational)

🔗 **Link:** [Mobile Security Framework - MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)  
📝 **Description:** Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework capable of performing static and dynamic analysis of mobile applications. MobSF support mobile app binaries (APK, IPA & APPX) along with zipped source code and provides REST APIs for seamless integration with your CI/CD or DevSecOps pipeline.The Dynamic Analyzer helps you to perform runtime security assessment and interactive instrumented tests.

</details>

<details><summary><strong>Mole: Out-of-Band Exploitation Framework</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Zach Grace](https://img.shields.io/badge/Zach%20Grace-informational)

🔗 **Link:** [Mole: Out-of-Band Exploitation Framework](https://github.com/ztgrace)  
📝 **Description:** Mole is a new open source framework for identifying and exploiting out-of-band (OOB) application vulnerabilities in applications. Mole provides an all-in-one payload generation framework and callback/payload server that streamlines the OOB payload creation and exploitation process

Mole takes inspiration from tools such as BurpSuite's Collaborator, XSS Hunter, but improves upon them in several key ways. Mole decouples the monitoring and payload generation from the testing tooling allowing for the 24x7 monitoring of OOB interaction. With this release, Mole supports the tracking of both DNS and HTTP/HTTPS interaction for all supported payload types which include XSS, XXE, PDF, and OOXML. These payloads can be generated and saved to a directory for manual testing, dynamically inserted into requests with Mole's Burp Suite Extension, or retrieved via API for custom integrations.

Mole tracks OOB interaction with customizable tracking tokens, which are stored on the callback server. When a valid token is presented to the callback server, either a pre-defined notification is sent, a custom web hook is invoked, or a payload server is invoked. The tracking token length and character set can be customized to work around exploitation constraints. During payload creation, context can be added to each tracking token through the tags feature. These tags are returned in any notifications and webhooks to easily identify which payload fired and in what context.

Mole's plugin framework allows it to be easily extended by creating custom payloads and payload servers. Plugins can specify both payload creation and server-side payload actions such as dynamically serving DTDs for an XXE payload.

</details>

<details><summary><strong>Qiling Framework: From dark to dawn -- Enlightening the analysis of the most mysterious IoT Firmware</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![KaiJern Lau](https://img.shields.io/badge/KaiJern%20Lau-informational) ![Bo Wen Sun](https://img.shields.io/badge/Bo%20Wen%20Sun-informational) ![Yu Tong](https://img.shields.io/badge/Yu%20Tong-informational) ![Tian Zhe Ding](https://img.shields.io/badge/Tian%20Zhe%20Ding-informational)

🔗 **Link:** Not Available  
📝 **Description:** With household appliances and wearable gadgets integrated with network capabilities, we are surrounded by an increasing number of IoT devices. Coming together with the popularity of IoT devices are two critical questions.

IoT devices normally come with a "call home" feature, through which users can interact with IoT devices through an App. As a result, users are typically curious about what kind of information they are sending back home.
Along with the facilitation from the "call home" feature, users are also curious about whether/how IoT devices could potentially allow hackers to gain unauthorized access and thus control the device remotely.

To answer the questions above, an analysis framework or tool is usually needed. Unfortunately, there has not yet been an effective, efficient analysis framework or tool available for answering such questions. Today, to analyze IoT devices and the corresponding applications, researchers still heavily rely upon qemu-usermode/qemu. However, it has already been demonstrated qemu-usermode/qemu is a very inefficient solution for IoT because it was designed for Linux and development boards.

In this talk, we will summarize and discuss some common IoT firmwares, which hurdle the analysis of security researchers. Followed by our analysis and discussion, we will then reveal the fundamental problems hidden behind the obstacle. As is specified in our presentation outline, these obstacles include (1) the difficulty of using primitive emulation methods to simulate IoT firmware, (2) the difficulty of using similar specification hardware and general purpose OS to emulate IoT firmware, (3) the difficulty imposed by device drivers and, (4) the concern of insufficient computation and memory resources.

Motivated by our analysis and discussion, we introduce Qiling -- a fully sandboxed, controlled and highly customized framework designed for performing the emulation for IoT devices. In this talk, we will discuss how Qiling Framework empowers security researchers to perform IoT firmware reverse engineering. To be more specifically, we will talk about

- how to emulate various CPU such as ARM, ARM Big Endian, MIPS32, MIPS32 Big Endian, ARM64, X86 and X64;
- how to emulate various OS such as Linux, MacOS, Windows, FreeBSD;
- how to simulate all stdio input and output and thus reply expected results;
- how to build all the network requests through an auto responder in virtualized network
- how to utilize the instrumentation support to redirect code execution whenever is needed
- how to fully customize emulated OS, giving researchers the ability to replace syscall or APIs with their own
- how to enable full CPU control (e.g., updating CPU registers during execution)
- how to support full gdbserver for platform and multi architecture debugging and thus allow allow researchers to use their preferred debuggers for their debugging tasks
- how to enable cross-platform and multi-architecture fuzz testing by integrating it with AFL

Along with this talk, we will share all the firmware that we have tested and will provide a live demo showcasing how easily a researcher can build an isolated testing environment to analyze, instrument, and fuzz a IoT device. In November of 2019, we have already released the source code of our Qiling Framework.

</details>

<details><summary><strong>Threagile: Agile Threat Modeling with Open-Source Tools from within Your IDE</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Christian Schneider](https://img.shields.io/badge/Christian%20Schneider-informational)

🔗 **Link:** Not Available  
📝 **Description:** If we can build software in a reliable, reproducible and quick way at any time using Pipeline-as-Code and have also automated security scans as part of it, how can we quickly capture the risk landscape of agile projects to ensure we didn't miss an important thing? Traditionally, this happens in workshops with lots of discussion and model work on the whiteboard with boxes, lines and clouds. It's just a pity that it often stops then: Instead of a living model, a slowly but surely eroding artifact is created, while the agile project evolves at a faster pace.

In order to counteract this process of decay, something has to be done continuously, something like "Threat-Model-as-Code" in the DevSecOps sense. The open-source tool Threagile implements the ideas behind this approach: Agile developer-friendly threat modeling right from within the IDE. Models editable in developer IDEs and diffable in Git, which automatically derive risks including graphical diagram and report generation with recommended mitigation actions.

The open-source Threagile toolkit can be executed as a simple docker container and runs either as a command line tool or a full-fledged server with a REST-API: Given information about your data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules and optionally your custom risk rules against the processed model. The resulting artifacts are diagrams, JSON, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state.

Agile development teams can easily integrate threat modeling into their process by maintaining a simple YAML input file about their architecture and the open-source Threagile toolkits handles the risk evaluation.

</details>

<details><summary><strong>xGitGuard: Detecting Publicly Exposed Secrets on GitHub at Scale</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Bahman Rashidi](https://img.shields.io/badge/Bahman%20Rashidi-informational)

🔗 **Link:** [xGitGuard: Detecting Publicly Exposed Secrets on GitHub at Scale](https://gist.github.com/AhnMo/dbe81133c98a75beba6227a8a57c74dc)  
📝 **Description:** Public GitHub is the most common place where developers share their code and tools that they develop (i.e., developed for an organization or themselves). Most developers and repository contributors do their best to remove sensitive information before they push their code into the GitHub. However, there are developers who often unknowingly/inadvertently neglect to remove sensitive information such as API tokens and user credentials (username & passwords) from their code prior to posting it. As a result, an organization's internal secrets and token are exposed publicly. Therefore, an unauthorized access to the secrets GitHub by bad actors can have significant consequences for organizations. In order to address the issue, we offer xGitGuard, a full-fledge AI-based tool that detects organizations' secrets and user credentials posted on the public GitHub in a scalable and timely-manner fashion. xGitGuard, takes advantage of a new text processing algorithm that can find secrets within files with a high level of accuracy. This can significantly help operations to take proper actions in timely manner.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>ARP covert channel attacks by 8bit microcomputer</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michihiro Imaoka](https://img.shields.io/badge/Michihiro%20Imaoka-informational)

🔗 **Link:** Not Available  
📝 **Description:** Introduces a method of embedding information in the padding part of ARP and performing secret communication with only one small 8-bit microcomputer. The transmitter uses an 8-bit microcomputer called Atmega328P. A 10BASE-T Ethernet frame is generated using only the GPIO of the microcomputer without using a dedicated chip such as an Ethernet controller. By using this method, it is possible to perform a covert channel attack with a smaller and cheaper method than the conventional method.

Since this attack can be performed with a single inexpensive and small microcomputer, it can be hidden and operated inside devices that can be connected to various networks. This lecture introduces some attack scenarios, discusses various attack methods that use this attack method, and discusses their defense methods.

</details>

<details><summary><strong>Cotopaxi: IoT Protocols Security Testing Toolkit</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Jakub Botwicz](https://img.shields.io/badge/Jakub%20Botwicz-informational) ![Mariusz Księżak](https://img.shields.io/badge/Mariusz%20Księżak-informational)

🔗 **Link:** Not Available  
📝 **Description:** Cotopaxi is a set of tools for security testing of Internet of Things devices using specific network IoT/IIoT/M2M protocols (e.g. AMQP, CoAP, DTLS, HTCPCP, mDNS, MQTT, MQTT-SN, QUIC, SSDP).

</details>

<details><summary><strong>Kouba: Industrial Pentesting</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Paula de la Hoz](https://img.shields.io/badge/Paula%20de%20la%20Hoz-informational)

🔗 **Link:** Not Available  
📝 **Description:** Introduction to Industrial security: brief introduction to industrial cyber-attacks and why it's important to protect OT infrastructures. In this part I'll introduce the importance of industrial security, speak about Stuxnet and other dangerous attacks that had impact in industrial sector, and some prevention tips.

Introduction to Kouba: proposing a simple methodology that includes enumeration, footprinting and automatic exploitation with open tools. Presenting the advantages of using Debian with these specific tools* instead of Kali, and how to apply public key/password encryption and magic-wormhole using the scripts for securely exporting encrypted logs out of the virtual machine.

Choosing open hardware for attacks: Once we have footprinted the devices and machines in the OT, in case we have physical access to the infrastructure, there are some things to look for regarding to physical security, such as USB ports, RTU (remote terminal units) details or DNP3 protocol serial communication. Using Arduino nano, pro mini, leonardo and attiny85 for designing either badusb or specific tools; RPI4/3/ZERO; ATMega2560 customizable PLC (PLDuino); S232 shield (for UNO), multi-protocols shield; Radio modules and others.

* The system includes Redpoint and other nmap scripts, Kamerka, Aztarma, PLCinject, S7Scan, ISF, etc as well as Python 2.7 and 3, git, xfce4 terminal, Docker and Vagrant for needed virtualization, Celery and Redis for Kamerka, openssl, clang and other few compiling tools.

</details>

<details><summary><strong>MUD-Visualizer</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Vafa Andalibi](https://img.shields.io/badge/Vafa%20Andalibi-informational)

🔗 **Link:** [MUD-Visualizer](https://github.com/iot-onboarding/mud-visualizer)  
📝 **Description:** Manufacturer Usage Description (MUD) is a recently introduced IETF standard designed to protect IoT devices and networks by isolating IoT device based on the information that define the behavior of that device. The standard defines a straight-forward method to implement a defensive mechanism based on the rules that are introduced by manufacturer of the device. MUD-Files are the core component of the MUD standard and contain the access control information of IoT devices. However, MUD-Files may contain possibly hundreds of access control rules. As a result, reading and validating these files is a challenge; and determining how multiple IoT devices interact is difficult for the developer and infeasible for the consumer. MUD-Visualizer is a tool that provides a visualization of any number of MUD-Files and is designed to enable developers to produce correct MUD-Files by providing format corrections, integrating them with other MUD-Files, and identifying conflicts through visualization. MUD-Visualizer is scalable and its core task is to merge and illustrate ACEs for multiple devices; both within and beyond the local area network.

</details>

<details><summary><strong>UFO: A Security Verification Tool for IoT Device Firmware</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Tsungta Tsai](https://img.shields.io/badge/Tsungta%20Tsai-informational)

🔗 **Link:** Not Available  
📝 **Description:** UFO is an IoT firmware security assessment tool that helps firmware developers or security researchers assess the security level of IoT device firmware.

UFO profiles the IoT firmware in many surfaces, like known vulnerabilities, sensitive data, cracked passwords, and hidden backdoors. It saves penetration testers time to gather information and help create attack vectors. Meanwhile, as a handy tool, UFO exposes vulnerabilities as early as possible to mitigate attacks from IoT malware like the notorious Mirai, which also collected default passwords of IoT devices from firmware. We did leverage UFO to pwn two COTS network cameras by discovering their backdoors and default passwords.

Main features of UFO are:
- Known 3rd Party Suite CVE Risk Report: Post-scan report based on the Common Vulnerability Scoring System (CVSS) which is an open industry standard for assessing the severity of computer system security vulnerabilities.
- Sensitive Data Statistics: Assessment of the email, IP, URL, private or password vulnerabilities.
- Cracked Passwords and Certificates Review: Check if your passwords or certificates are vulnerable.
- Shell Dependency Backdoor Paths: Produces a visual guide of backdoor paths.

A full circle of scenarios of using UFO to analysis IoT firmware will be demonstrated.

Among the above features, the source code used to trace shell dependency has been released on Github: https://github.com/dayanuyim/shdep.

The promotional video: https://youtu.be/0XupD3PAbuo

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>ATT&CK Simulator</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Tim Frazier](https://img.shields.io/badge/Tim%20Frazier-informational) ![Dave Herrald](https://img.shields.io/badge/Dave%20Herrald-informational) ![Kyle Champlin](https://img.shields.io/badge/Kyle%20Champlin-informational)

🔗 **Link:** Not Available  
📝 **Description:** This project provides a set of tooling for repeatedly executing and detecting adversary techniques in order to improve detection engineering. This project uses the MITRE ATT&CK Enterprise techniques taxonomy and the MITRE ATT&CK navigator web app. Once set up, you will be able to repeatedly execute specific techniques, observe the resulting events, and refine your detection rules and methodology.

</details>

<details><summary><strong>Botnet Simulation Framework (BSF)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Leon Böck](https://img.shields.io/badge/Leon%20Böck-informational) ![Shankar Karuppayah](https://img.shields.io/badge/Shankar%20Karuppayah-informational) ![Jens Keim](https://img.shields.io/badge/Jens%20Keim-informational) ![Emmanouil Vasilomanolakis](https://img.shields.io/badge/Emmanouil%20Vasilomanolakis-informational)

🔗 **Link:** Not Available  
📝 **Description:** In the arms race between botmasters and defenders, the botmasters have the upper hand, as defenders have to react to actions and novel threats introduced by botmasters. The Botnet Simulation Framework (BSF) addresses this problem by leveling the playing field. It allows defenders to get ahead in the arms race by developing and evaluating new botnet monitoring techniques and countermeasures. This is crucial, as experimenting in the wild will interfere with other researchers and possibly alert botmasters.

BSF allows realistic simulation of peer-to-peer botnets to explore and study the design and impact of monitoring mechanisms and takedown attempts before being deployed in the wild. BSF is a discrete event botnet simulator that provides a set of highly configurable (and customizable) botnet features including:
- realistic churn behavior
- variable bot behavior
- monitoring mechanisms (crawlers and sensors)
- anti-monitoring mechanisms

Moreover, BSF provides an interactive visualization module to further study the outcome of a simulation. BSF is aimed at enabling researchers and defenders to study the design of the different monitoring mechanisms in the presence of anti-monitoring mechanisms [1,2,3]. Furthermore, this tool allows the users to explore and understand the impact of design choices of botnets seen to date.

[1] Leon Böck, Emmanouil Vasilomanolakis, Jan Helge Wolf, Max Mühlhäuser: Autonomously detecting sensors in fully distributed botnets. Computers & Security 83: 1-13 (2019)
[2] Leon Böck, Emmanouil Vasilomanolakis, Max Mühlhäuser, Shankar Karuppayah: Next Generation P2P Botnets: Monitoring Under Adverse Conditions. RAID 2018: 511-531
[3] https://www.blackhat.com/eu-17/briefings.html#i-trust-my-zombies-a-trust-enabled-botnet

</details>

<details><summary><strong>capa: Automatically Identify Malware Capabilities</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Moritz Raabe](https://img.shields.io/badge/Moritz%20Raabe-informational) ![William Ballenthin](https://img.shields.io/badge/William%20Ballenthin-informational)

🔗 **Link:** [capa: Automatically Identify Malware Capabilities](https://github.com/mandiant/capa/releases/)  
📝 **Description:** capa is an open-source tool that detects capabilities in programs to reduce the time-to-triage and make malware analysis more accessible. Anyone dealing with potentially malicious programs and especially forensic, intelligence, and malware analysts can use capa to understand a sample's capabilities, role (downloader, backdoor, etc.), and any suspicious or unique functionality.
capa takes automated malware triage to the next level going from simply saying "this is probably bad" to providing a concise description of what a program actually does. This report provides critical, decision-making information to anyone dealing with malware.

capa uses a new algorithm that reasons over the features found in a file to identify its capabilities. The lowest level features range from disassembly tricks to coding constructs, while intermediate features include references to recognized strings or API calls. Users compose rules that train capa how to reason about features – and even the significance of other rules. This makes it easy for the community to extend the tool's abilities.

We will describe how and why our tool works. We will also show to use it to enhance every malware analysis workflow. Furthermore, you will learn how to develop capability detections that extend capa.

</details>

<details><summary><strong>CQForensic: The Efficient Forensic Toolkit</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Paula Januszkiewicz](https://img.shields.io/badge/Paula%20Januszkiewicz-informational) ![Mike Jankowski-Lorek](https://img.shields.io/badge/Mike%20Jankowski-Lorek-informational)

🔗 **Link:** Not Available  
📝 **Description:** CQForensic Toolkit enables you to perform detailed computer forensic examinations. It guides you through the information gathering process providing data for analysis and extracting the evidence. CQForensic can build an attack timeline, extract information from the USN journal, recover files, also from MFT, decrypt user's and system's stored secrets, like encrypted data, extract information from Prefetch and from Remote Desktop Session cache, extract information from the configuration of the used for administration tools. It also contains toolkit for memory analysis, it extracts information from memory dumps, including the PowerShell commands, complete files, including making them consistent if they were corrupted, like sensitive EVTX files. Our biggest CQKawaii implements custom-made machine learning algorithms to extract from the large logs the anomalies. During Black Hat Europe, we would like to announce five new tools, including CQKawaii. CQForensic is a very practical toolkit for forensic investigators.

</details>

<details><summary><strong>Gargamel</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Viliam Kacala](https://img.shields.io/badge/Viliam%20Kacala-informational)

🔗 **Link:** Not Available  
📝 **Description:** Gargamel is a Windows tool for acquiring the forensic evidence from remote Windows or Linux machines using several different methods.

The program is able to download the following content from remote Windows machine:
- Windows Event Logs in evt and evtx format,
- dump of memory,
- specified files described with the support of expansions (*,?),
- output of commands specified in a text file,
- registry,
- state of firewall,
- state of network interfaces,
- logged on users,
- running processes,
- active network connections,

When targeting the remote Linux machine, the program will download:
- content of /var/log/directory
- specified files described with the support of expansions (*,?),
- output of commands specified in a text file,
- state of firewall,
- state of network interfaces,
- logged on users,
- running processes,
- active network connections,


Gargamel supports 5 connection methods, naming PowerShell remoting, WMI, PsExec, RDP and SSH (with SCP).

</details>

<details><summary><strong>ioc2rpz: Where Threat Intelligence Meets DNS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Vadim Pavlov](https://img.shields.io/badge/Vadim%20Pavlov-informational)

🔗 **Link:** [ioc2rpz: Where Threat Intelligence Meets DNS](https://github.com/Homas/ioc2rpz)  
📝 **Description:** DNS is the control plane of the Internet with unprecedented detailed views on applications, devices and even transferred data going in and out of a network. 80% of malware uses DNS to communicate with Command & Control for DNS data exfiltration/infiltration and phishing attacks using lookalike domains. Response Policy Zones or DNS Firewall is a feature which allows us to apply security policies on DNS. Commercial DNS Firewall feeds providers usually do not allow users to generate their own feeds. Cloud only DNS service providers do not provide feeds for on-prem DNS.

ioc2rpz is a DNS server which automatically creates, maintains and distributes DNS Firewall feeds from various local (files, DB) and remote (http, ftp, rpz) sources. This enables easy integrations with Threat Intel providers and Threat Intelligence Platforms. The feeds can be distributed to any open source and commercial DNS servers which support RPZ, e.g. ISC BIND, PowerDNS, Infoblox, BlueCat, Efficient IP etc. With ioc2rpz you can create your own feeds, actions and prevent undesired communications before they happen.

https://ioc2rpz.net is a community portal which is powered by ioc2rpz where you can try several free DNS Firewall feeds.

RpiDNS is a new feature integrated into ioc2rpz.gui which includes an installation script and a web interface to monitor and manage local secure DNS services.

</details>

<details><summary><strong>JVMXRay</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Milton Smith](https://img.shields.io/badge/Milton%20Smith-informational)

🔗 **Link:** [JVMXRay](https://github.com/spoofzu/jvmxray)  
📝 **Description:** JVMXRay is technology for monitoring access to system resources within the Java Virtual Machine at runtime. Since JVMXRay integrates with virtual machine, no code changes to the application are required for operation. An ancillary benefit of no code required is that the technology provides insight into 3rd party libraries used by your application and commercial software where no source code is available. JVMXRay is designed with application security emphasis but it's beneficial for other areas like software quality processes and diagnostics. JVMXRay may be extended to work with many technologies like OWASP Dependency Check and other tools.

</details>

<details><summary><strong>MSTICpy: The Security Analysis Swiss Army Knife</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Pete Bryan](https://img.shields.io/badge/Pete%20Bryan-informational) ![Ian Hellen](https://img.shields.io/badge/Ian%20Hellen-informational) ![Ashwin Patil](https://img.shields.io/badge/Ashwin%20Patil-informational)

🔗 **Link:** Not Available  
📝 **Description:** MSTIC Jupyter and Python Security Tools (MSTICpy) is a Python library of security investigation tools developed by the Microsoft Threat Intelligence Center (MSTIC) to assist and support security analysts conducting security investigations and threat hunting.

The library provides features to collect data from a range of data sources, to enrich the data with Threat Intelligence and OSINT, to analyse the data using ML and data analysis techniques, and to visualise the output of this analysis for quick and easy comprehension.

Rather than a single tool MSTICpy is a Swiss Army knife for security investigations.

</details>

<details><summary><strong>PurpleSharp: Adversary Simulation for the Blue Team</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

🔗 **Link:** [PurpleSharp: Adversary Simulation for the Blue Team](https://github.com/mvelazc0/PurpleSharp)  
📝 **Description:** Defending enterprise networks against attackers continues to present a difficult challenge for blue teams. Prevention has fallen short; improving detection & response capabilities has proven to be a step in the right direction. However, without the telemetry produced by adversary behavior, building and testing detection capabilities will be a challenging task. Executing adversary simulations in monitored environments produces the telemetry that allows security teams to identify gaps in visibility as well as build, test and enhance detection analytics

PurpleSharp is an open source adversary simulation tool written in C# that executes adversary techniques against Windows Active Directory environments. The resulting telemetry can be leveraged to measure and improve the efficacy of a detection engineering program. PurpleSharp executes different behavior across the attack lifecycle following the MITRE ATT&CK Framework's tactics: execution, persistence, privilege escalation, credential access, lateral movement, etc.

PurpleSharp executes simulations on remote hosts by leveraging administrative credentials and native Windows services/features such as Server Message Block (SMB), Windows Management Instrumentation (WMI), Remote Procedure Call (RPC) and Named Pipes.

PurpleSharp can assist blue teams in the following use cases:

- Verify prevention controls ( are Lsass dumps being blocked ? )
- Build new detection controls ( build a detection rule for T1117)
- Test/verify existing detection controls (are we really detecting process injection ?)
- dentify gaps with existing detection analytics ( broken logic, lack of coverage, etc. )
- Identify gaps in visibility ( broken agents, broken event pipelines, etc. )
- Train the SOC with credible simulations

</details>

<details><summary><strong>ROADtools and ROADrecon</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Dirk-jan Mollema](https://img.shields.io/badge/Dirk-jan%20Mollema-informational)

🔗 **Link:** [ROADtools and ROADrecon](https://github.com/dirkjanm/ROADtools)  
📝 **Description:** ROADtools is a framework to interact with Azure AD. It currently consists of a library (roadlib) and the ROADrecon Azure AD exploration tool.

ROADlib is a library that can be used to authenticate with Azure AD or to build tools that integrate with a database containing ROADrecon data. The database model in ROADlib is automatically generated based on the metadata definition of the Azure AD internal API.

ROADrecon is a tool for exploring information in Azure AD from both a Red Team and Blue Team perspective. In short, this is what it does:

- Uses an automatically generated metadata model to create an SQLAlchemy backed database on disk.
- Use asynchronous HTTP calls in Python to dump all available information in the Azure AD graph to this database.
- Provide plugins to query this database and output it to a useful format.
- Provide an extensive interface built in Angular that queries the offline database directly for its analysis.

ROADrecon also provides a built-in plugin to export it's data to a custom version of BloodHound with Azure AD capabilities.

Both ROADtools and ROADrecon are completely free and open source software.

</details>

<details><summary><strong>S-TIP: Seamless Threat Intelligence Platform</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Koji Yamada](https://img.shields.io/badge/Koji%20Yamada-informational) ![Toshitaka Satomi](https://img.shields.io/badge/Toshitaka%20Satomi-informational) ![Ryusuke Masuoka](https://img.shields.io/badge/Ryusuke%20Masuoka-informational)

🔗 **Link:** Not Available  
📝 **Description:** S-TIP is an open-source platform for those who analyze threats and share the results with CSIRT etc.

There are a variety of CTI (Cyber Threat Intelligence) in the world. "Human CTI" is knowledge of cyberattacks to be consumed by people through social media, email, and other channels. "System CTI" is cyber attack-related knowledge that is consumed by systems in a format that can be understood by computers, namely STIX.

However, there were barriers between Human CTI and System CTI. There were divided and could not be utilized from the other realm. For example, security operators need intensive manual labor to convert a new threat report for human readers into CTI in a machine-readable format for automated defense.

S-TIP solves this problem by integrating Human CTI and System CTI seamlessly through its STIX database to bring down those barriers. When a user creates a new post, it is automatically converted to the STIX file and saved into the database. The system can trigger automated defense by consuming the STIX file. These processes can be done transparently while a user is unaware of the conversion.

Main features of S-TIP are:
1. CTI Element Extractor: Human posts to the social media UI of S-TIP are automatically captured as STIX data.
2. CTI Graph Analytics View: The STIX data can be associated with other pieces of CTI. This mechanism makes it much easier for users to grasp the whole picture of the cyberattack quickly.
3. Integration with Other Platforms: The STIX data can be readily consumed by security tools like MISP, Splunk, JIRA, and Slack.
4. STIX/TAXII - Compliant: Collects CTI from open STIX / TAXII servers on the Internet like AlienVault OTX.

These features support a more predictive and proactive response.

Available at : https://github.com/s-tip

</details>

<details><summary><strong>SmogCloud: Expose Yourself Without Insecurity - Cloud Breach Patterns</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Rob Ragan](https://img.shields.io/badge/Rob%20Ragan-informational) ![Oscar Salazar](https://img.shields.io/badge/Oscar%20Salazar-informational)

🔗 **Link:** Not Available  
📝 **Description:** Do you know what is internet accessible in your AWS environments? The answer and methodology of how you arrive at the answer may be the difference between missing critical exposures and complete situational awareness. Dynamic and ephemeral exposures are being created on an unprecedented level and your old generation of tools, techniques, and internet scanners can't find them. Let us show you how to find them and what it means for the future of unwanted exposures. A comprehensive asset inventory is step one to any capable security program. What does having an accurate inventory mean to an AWS administrator and ongoing security engineering effort?

Our approach involves leveraging AWS security services and metadata to translate the raw configuration into patterns of targetable services that a security team can utilize for further analysis.

In this presentation we will look at the most pragmatic ways to continuously analyze your AWS environments and operationalize that information to answer vital security questions. Demonstrations include integration between IAM Access Analyzer, Tiros Reachability API, and Bishop Fox CAST Cloud Connectors, along with a new open source tool SmogCloud to find continuously changing AWS internet-facing services.

Key Takeaways:
+ Learn how to continuously maintain an inventory of AWS services and understand their internet-exposures
+ Discover how to leverage automation from AWS Access Analyzer and a freely available open source tool from Bishop Fox to operationalize exposure testing
+ See practical demonstrations of how engineering and security teams can determine impact of their security group configurations

</details>

<details><summary><strong>soc-faker: A python package for use in generating fake data for SOC and security automation</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Josh Rickard](https://img.shields.io/badge/Josh%20Rickard-informational)

🔗 **Link:** [soc-faker: A python package for use in generating fake data for SOC and security automation](https://github.com/swimlane/soc-faker)  
📝 **Description:** soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.

</details>

<details><summary><strong>SYNwall: A Zero-Configuration (IoT) Firewall</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Cesare Pizzi](https://img.shields.io/badge/Cesare%20Pizzi-informational)

🔗 **Link:** Not Available  
📝 **Description:** A lots of words has been spent in the last years about IoT security: but instead of thinking to deploy a new device, let's try to stay on what we already have: we have a TCP/IP stack. And what we don't want to have? Complicated and cumbersome security configurations.

The aim of SYNwall is to build an easy to configure, no new hardware, low footprint, lightweight and multi-platform security layer on TCP/IP: with a one way OTP authentication, SYNwall can make every device more secure and resilient to the real world networking reconnaissance and attacks.

If we think at some of the IoT installations (may be directly internet exposed, in difficult environments, with no support infrastructure available), the possibility to have an on-board and integrated way to control access, can make a huge difference in terms of security.

The device will became virtually unaccessible to anyone who don't have the proper OTP key, blocking all the communications at the very first level of it: the SYN packet. No prior knowledge of who need to access is required at this point, making configuration and deploy a lot easier.

</details>

<details><summary><strong>vPrioritizer: Learn to say NO to almost every vulnerability (art of risk prioritisation…)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Pramod Rana](https://img.shields.io/badge/Pramod%20Rana-informational)

🔗 **Link:** [vPrioritizer: Learn to say NO to almost every vulnerability (art of risk prioritisation…)](https://github.com/varchashva)  
📝 **Description:** As suggested by vulndb and cve, on a daily basis, approximately 50 new vulnerabilities become known to industry and even if an organization considers the impact rate of 10%, it’s still very challenging to manage it effectively and it’s safe to assume that count is going to increase furthermore. So with this amount organization is focusing (or should focus) on reducing the risk rather than eliminating it.

In current era, vulnerability management is (almost) equal to risk prioritisation because

- Resources (skillset and time) is limited in every organisation
- Environment is changing too fast and too frequently (ROI is less in analysis and remediation of a vulnerability if affected asset is not going to be live for a longer time - small attack surface)
- Attack surface is increasing exponentially in diversity (which again comes down to prioritisation)
- Remember the 80/20 rule - 20% of vulnerabilities bring 80% of risk

So what is risk? How do we calculate it? What are the factors contributing to risk?

1. CVSS (historically used) - No
2. Asset Criticality - No
3. Asset Accessibility - No
4. Exploit Applicability - No
5. Exploit Availability - No
6. Ease of Exploitation - No
7. Attack Surface - No
8. All of the Above - Yes

Theoretically, the above approach looks appropriate to adopt but practically it’s not possible to do it manually for every vulnerability affecting every asset by every organisation.

To overcome the above challenges I have prepared an open-source framework, vPrioritizer, which gives us ability to assess the risk on different layers such as (and hence comprehensive control on granularity of each component of risk):

- We can assign significance on per asset basis
- We can assess severity on per vulnerability basis
- At the same time, we can adjust both factors at asset & vulnerability relationship level
- On top of that, community analytics provides insights as suggested risk

This framework enables us to understand the contextualized risk pertaining to each asset by each vulnerability across the organization. It’s community based analytics provides a suggested risk for each vulnerability identified by vulnerability scanners and further strengthens risk prioritization process. So at any point of time teams can make an effective and more informed decision, based on unified and standardized data, about what (vulnerability/ties) they should remediate (or can afford not to) on which (asset/s).

</details>

---
## 🔴 Red Teaming
<details><summary><strong>ATTPwn</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Pablo Gonzalez](https://img.shields.io/badge/Pablo%20Gonzalez-informational) ![Francisco Ramirez Vicente](https://img.shields.io/badge/Francisco%20Ramirez%20Vicente-informational)

🔗 **Link:** Not Available  
📝 **Description:** ATTPwn is a computer security tool designed to emulate adversaries. The tool aims to bring emulation of a real threat into closer contact with implementations based on the techniques and tactics from the MITRE ATT&CK framework. The goal is to simulate how a threat works in an intrusion scenario, where the threat has been successfully deployed. It is focused on Microsoft Windows systems through the use of the Powershell command line. This enables the different techniques based on MITRE ATT&CK to be applied. ATTPwn is designed to allow the emulation of adversaries as for a Red Team exercise and to verify the effectiveness and efficiency of the organization's controls in the face of a real threat.

</details>

<details><summary><strong>AutoRDPwn: The Shadow Attack Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Joel Gámez](https://img.shields.io/badge/Joel%20Gámez-informational)

🔗 **Link:** [AutoRDPwn: The Shadow Attack Framework](https://github.com/JoelGMSec/AutoRDPwn)  
📝 **Description:** AutoRDPwn is a post-exploitation framework created in Powershell, designed primarily to automate the Shadow attack on Microsoft Windows computers. This vulnerability (catalogued as a feature by Microsoft) allows a remote attacker to view the desktop of his victim without his consent, and even control it on demand, using native tools of the operating system itself.

Thanks to the additional modules, it is possible to obtain a remote shell through Netcat, dump system hashes with Mimikatz, load a remote keylogger and much more. All this, through a totally intiutive menu in seven different languages.

In this talk, we will briefly review the most common remote desktop attacks and the big difference the Shadow attack makes to them. Afterwards, we will make different live demonstrations, in which all the functionalities of the tool will be put into practice. Some of them are the following:

- UAC, AMSI and Windows Defender Bypass
- Remote Shell using native system and third party tools
- Obtaining hashes and pass the hash
- Remote execution without credentials via SMB, WMI and WinRM
- Shadow attack on different operating systems (both desktop and server versions)
- Miscellaneous (remote keylogger, one-line execution, pivoting and more)

</details>

<details><summary><strong>C2 Matrix: Comparison of Command and Control Frameworks</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Jorge Orchilles](https://img.shields.io/badge/Jorge%20Orchilles-informational) ![Bryson Bort](https://img.shields.io/badge/Bryson%20Bort-informational)

🔗 **Link:** [C2 Matrix: Comparison of Command and Control Frameworks](https://github.com/jesusgavancho/TryHackMe_and_HackTheBox/blob/master/Intro%20to%20C2.md)  
📝 **Description:** Command and Control is one of the most important tactics in the MITRE ATT&CK matrix as it allows the attacker to interact with the target system and realize their objectives. Organizations leverage Cyber Threat Intelligence to understand their threat model and adversaries that have the intent, opportunity, and capability to attack. Red Team, Blue Team, and virtual Purple Teams work together to understand the adversary Tactics, Techniques, and Procedures to perform adversary emulations and improve detective and preventive controls.

The C2 Matrix was created to aggregate all the Command and Control frameworks publicly available (open-source and commercial) in a single resource to assist teams in testing their own controls through adversary emulations (Red Team or Purple Team Exercises). Phase 1 lists all the Command and Control features such as the coding language used, channels (HTTP, TCP, DNS, SMB, etc.), agents, key exchange, and other operational security features and capabilities. This allows more efficient decisions making when called upon to emulate and adversary TTPs.

It is the golden age of Command and Control (C2) frameworks. Learn how these C2 frameworks work and start testing against your organization to improve detective and preventive controls.

The C2 Matrix currently has 41 command and control frameworks documented in a Google Sheet, web site, and questionnaire format.

For Blackhat, C2 Matrix will release phase 2 of the project which involves mapping each C2 to MITRE ATT&CK and correlate with known adversaries. This will allow much quicker selection of which C2s to use for a given adversary or threat scenarios.

</details>

<details><summary><strong>Covenant: .NET Command and Control</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ryan Cobb](https://img.shields.io/badge/Ryan%20Cobb-informational)

🔗 **Link:** [Covenant: .NET Command and Control](https://github.com/cobbr/Covenant)  
📝 **Description:** Covenant is a .NET command and control platform and web application that aims to highlight the attack surface of the .NET Framework and .NET Core, make the use of offensive .NET tradecraft easier, and serve as a collaborative platform for red teamers.

Covenant is multi-platform, multi-user, provides an intuitive web application interface, and is extendible through an API.

Covenant includes multiple built-in implants that utilize the traditional .NET Framework and .NET Core, which gives Covenant multi-platform implants that run on Windows, Linux, and MacOS. Additionally, Covenant allows operators to edit and add additional custom implants.

Covenant includes built-in support for custom and complex command and control routing. The platform includes built-in outbound listeners, including an HTTP and TCP listener, and peer-to-peer SMB communications over named pipes, which allows for complex implant networking. The platform also includes a protocol for adding new, custom communication protocols that gives the operator complete control over how the command and control traffic appears on the wire.

Covenant includes tons of built-in tasks based on libraries such as SharpSploit and GhostPack, and uses dynamic C# compilation and ConfuserEx obfuscation on tasks and payloads.

Covenant also has an emphasis on implant and network communication security to protect the data accessed by implants. Covenant implements an Encrypted Key Exchange protocol between implants and listeners to achieve forward secrecy for new implants and enforces SSL certificate pinning for implants.

In the age of EDR and threat hunting, red teamers need flexible, robust, and intuitive command and control platforms. Red teamers need the ability to collaborate with teammates, customize implant behavior and command and control traffic, track artifacts, and quickly adapt for defensive technologies. In this demo, you'll be shown how to accomplish this with Covenant.

</details>

<details><summary><strong>DeepSea Phishing Gear</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dimitry Snezhkov](https://img.shields.io/badge/Dimitry%20Snezhkov-informational)

🔗 **Link:** [DeepSea Phishing Gear](https://github.com/dsnezhkov)  
📝 **Description:** Introducing DeepSea, the phishing gear you will want to take with you on your next offensive expedition. 

It is designed to help Red Team operators and teams with the tactical delivery of opsec-tight, flexible email phishing campaigns carried out in a portable manner on the outside as well as on the inside 
of a perimeter. 

Have you ever wanted to seamlessly operate with external and internal email providers; quickly re-target connectivity parameters per campaign; flexibly add headers, targets, attachments, correctly format and inline email templates, images and multipart messages; use content templates for personalization; clearly separate artifacts and content delivery for multiple (parallel or sequential) phishing campaigns; get actionable context help and deploy with minimal dependencies? 

In this session, we will show how you can do this and more in a portable, one binary cross platform setup, with less than 50 lines in a configuration file. 

With DeepSea, you will be able to keep campaign persistence with DNS tricks and an embedded email server used for running advanced two-way threaded campaigns you have always wanted. Catch and respond to those often missed inquiry emails, solidifying pretext and pacifying your marks.

Whether you plan on executing phishing campaigns deep on the inside of the perimeter, or bounce across multiple email providers for an external stealthy campaign delivery, DeepSea is very likely able to help.

</details>

<details><summary><strong>Dynamic Labs: Windows & Active Directory Exploitation</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Rohan Durve](https://img.shields.io/badge/Rohan%20Durve-informational)

🔗 **Link:** Not Available  
📝 **Description:** If you are after red-team training, there are multiple excellent courses and online resources for practising adversary simulation. That's not the primary motivation behind Alfa labs.

Alfa labs allows:
- Blue/red teamers to test or demonstrate specific attacks/attack-paths (e.g. when GMSA edges were introduced into BloodHound).
- Beginners to take a structured approach to learning Active Directory weaknesses (which have largely been practically accessible if you build your own lab, during workshops w/ limited spaces or commercial training).
- Replicate any technical issues and confirm your results

Therefore, stop by and spin up your own lab to practise your Windows Active Directory tools, techniques and procedures (TTPs) in isolation, or red-team your way through the dynamically-built Alfa labs.

</details>

<details><summary><strong>Mística: Anything is a tunnel if you're brave enough - Covert channels for everyone!</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Carlos Fernández](https://img.shields.io/badge/Carlos%20Fernández-informational) ![Raúl Caro Teixidó](https://img.shields.io/badge/Raúl%20Caro%20Teixidó-informational)

🔗 **Link:** Not Available  
📝 **Description:** From exposing internal network ports in restricted environments to the internet to controlling a meterpreter implant via DNS, everything is possible with protocol encapsulation.

To prove this, we have developed Mística, a tool that allows us to finely tune how we want to create a tunnel over protocols like HTTP, DNS and more, and combine this encapsulation with custom applicatrions like io, shell or port redirection.

Mística allows to embed data into other protocol fields, with the goal of establishing a bi-directional channel for arbitrary communications. Mística has a modular design, built around a custom transport protocol, called SOTP (Simple Overlay Transport Protocol). Data is encrypted, chunked and put into SOTP packets. SOTP packets are encoded and embedded into the desired field of the application protocol, and sent to the other end.

During this talk, we will talk about how to quickly design and create covert channels over different protocols and for different purposes. This is both useful for red teams that need new ways to hide their traffic and blue teams that want to easily test their monitoring capabilities.

We will do several demos, where we showcase how encapsulation works and how we can end up tunneling a RAT (meterpreter, in this case) connection over DNS. We will also showcase how to expose any port over the desired covert channel to combine it with tools like Evil-WinRM, for instance.

Mística is available at https://github.com/IncideDigital/Mistica under the GPLv3 license

</details>

<details><summary><strong>NovAttack: Cyber Attack Simulation for Perimeter Security</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Mustafa Altinkaynak](https://img.shields.io/badge/Mustafa%20Altinkaynak-informational)

🔗 **Link:** Not Available  
📝 **Description:** The NovAttack platform requires minimal setup time and few resources to implement. We love open source. So NovAttack is open source, it will remain open source.

NovAttack simulates real cyber attacks, focusing on the following attack categories.

### Features / Test Capabilities

- IPS / IDS / Firewall
- Malware Download
- Content Filtering
- DLP (Data Loss Protection)
- WAF (Web Application Firewall) / Roadmap

### How does NovAttack work?

NovAttack advocates the open source philosophy. Uses the capabilities of python and libraries. All communication is prepared with API.

NovAttack simulates cyber attacks with its point-to-point connection. Thus, it reduces the amount of false positive. Attack vectors in it can be edited and updated.

- You can provide continuous cyber attack simulation by adding current malware to NovAttack.
- You can develop DLP vectors specific to your organization, such as credit card leak). NovAttack provides continuous analysis for you.
- You can test your institution's content or URL filter.

</details>

<details><summary><strong>Overlord: Red Teaming Automation</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Vasilis Sikkis](https://img.shields.io/badge/Vasilis%20Sikkis-informational) ![Evangelos Nikolaou](https://img.shields.io/badge/Evangelos%20Nikolaou-informational)

🔗 **Link:** Not Available  
📝 **Description:** Overlord provides a python-based console CLI which is used to build Red Teaming infrastructure in an automated way. The user has to provide inputs by using the tool’s modules (e.g. C2, Email Server, HTTP web delivery server, Phishing server etc.) and the full infra / modules and scripts will be generated automatically on a cloud provider of choice. Currently supports AWS and Digital Ocean.

Links:
- GitHub repository - https://github.com/qsecure-labs/overlord
- A demo infrastructure - https://blog.qsecure.com.cy/posts/overlord/
- Full documentation of the tool - https://github.com/qsecure-labs/overlord/wiki

Acknowledgments:
This project could not be created without the awesome work for Marcello Salvati @byt3bl33d3r with the RedBaron Project. That is the reason why we are referencing the name of RedBaron on our project as well.
As Marcello stated on his acknowledgments, further thanks to:
1. @_RastaMouse's two serie's blogpost on 'Automated Red Team Infrastructure Deployment with Terraform' Part 1 and 2
2. @bluscreenofjeff's with his amazing Wiki on Read Team Infrastucture
3. @spotheplanet's blog post on Red team infrastructure

</details>

<details><summary><strong>Routopsy: Routing Protocol Vulnerability Analysis and Exploitation</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Szymon Ziolkowski](https://img.shields.io/badge/Szymon%20Ziolkowski-informational) ![Tyron Kemp](https://img.shields.io/badge/Tyron%20Kemp-informational)

🔗 **Link:** Not Available  
📝 **Description:** Routopsy is a new network attack toolkit that leverages a "virtual router" in a Docker container to scan for and attack various networking protocols and misconfigurations. Vulnerabilities include overly broad configured network statements within routing protocols, unauthenticated or plaintext authentication for protocols such as OSPF and HSRP, and the lack of passive interface usage within routing protocols.

Routopsy was designed in a way that will allow users to trivially perform attacks without requiring extensive networking knowledge. Attacks include the injection of new routes, discovery of new networks and gateway takeover attacks which ultimately could lead to Person-in-the-Middle attacks. Additionally, a fully-fledged router interface is also available for more experienced users and for more advanced attacks.

Internally, Routopsy leverages a "virtual router" which has been around for a number of years, is well maintained and supports a variety of protocols. Once the scan phase of Routopsy is complete a simple configuration is loaded within the virtual router and used to attack the target protocol.

</details>

<details><summary><strong>Starkiller: Threat Emulation Platform for Red Teams and Penetration Testers</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Anthony Rose](https://img.shields.io/badge/Anthony%20Rose-informational)

🔗 **Link:** [Starkiller: Threat Emulation Platform for Red Teams and Penetration Testers](https://github.com/sponsors/BC-SECURITY)  
📝 **Description:** The ultimate goal for any security team is to increase resiliency within an organization and adapt to the modern threat. Starkiller aims to provide red teams with a platform to emulate Advanced Persistent Threat (APT) tactics. Starkiller is a frontend for the post-exploitation framework, PowerShell Empire, which incorporates a multi-user GUI application that interfaces with a remote Command and Control (C2) server. Empire is powered by Python 3 and PowerShell and includes many widely used offensive security tools for Windows, Linux, and macOS exploitation. The framework's flexibility to easily incorporate new modules allows for a single solution for red team operations. Both red and blue teams can utilize Starkiller to emulate and defend against the most used APT attack vectors.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Carnivore: Microsoft External Attack Tool</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Chris Nevin](https://img.shields.io/badge/Chris%20Nevin-informational)

🔗 **Link:** [Carnivore: Microsoft External Attack Tool](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Active_Directory.md)  
📝 **Description:** Carnivore is a username enumeration and password spraying tool for Microsoft services (Skype for Business, ADFS, RDWeb, Exchange and O365). It includes new post compromise functionality for Skype for Business (pulling the internal address list and user presence), and a new method for smart detection of the username format. Carnivore originally began as an on-premises Skype for Business enumeration/spray tool as, these days, organizations have often locked down their implementations of Exchange, however, Skype for Business has been left externally accessible, and does not seem to have received as much attention from penetration tests.

</details>

<details><summary><strong>FuzzCube</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Anto Joseph](https://img.shields.io/badge/Anto%20Joseph-informational)

🔗 **Link:** [FuzzCube](https://github.com/antojoseph/fc)  
📝 **Description:** Fuzzing over the ages has improved in tooling, logic, and process, but is still a number-crunching problem! You are improving your odds by throwing more CPU power at it.

How do we make it happen without hacking through custom solutions that cannot be reused? Enter FuzzCube - Batteries Included! FuzzCube comes with State Sharing Features, Mutation Engines and Crash Verification tools that you could leverage in your projects. It leverages Kubernetes for its infrastructure orchestration capabilities. Using Kubernetes operators, we abstract the complexity of deploying a fuzzing infrastructure with distributed high throughput workloads, fault tolerance, storage orchestration, and high scalability. We will practise distributed fuzzing in the era of Cloud Native Computing and use our new skills to find some 0days ;)

</details>

<details><summary><strong>macOS Bluetooth Analysis Suite (mBAS)</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Yu Wang](https://img.shields.io/badge/Yu%20Wang-informational)

🔗 **Link:** [macOS Bluetooth Analysis Suite (mBAS)](https://github.com/mathew-fleisch/def-con-schedule/blob/master/docs/conference.json)  
📝 **Description:** mBAS is a set of Bluetooth tools for macOS platforms, including Bluetooth HCI request sniffer, fuzzer and Broadcom firmware SoC tools, etc. Among them, the HCI fuzzer helped me discover many Bluetooth kernel vulnerabilities, such as CVE-2020-3892, CVE-2020-3893, CVE-2020-3905, CVE-2020-3907, CVE-2020-3908 and CVE-2020-3912. With these tools, we can better understand the design and implementation of Bluetooth subsystem of macOS and other platforms.

</details>

<details><summary><strong>Zelos: Applying Emulation to Cross Architecture Root Cause Analysis</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Kevin Valakuzhy](https://img.shields.io/badge/Kevin%20Valakuzhy-informational)

🔗 **Link:** Not Available  
📝 **Description:** Zelos (Zeropoint Emulated Lightweight Operating System) is a python-based binary emulation platform that omits the cumbersome setup of virtual machines, yet provides instrumentation capabilities missing in user-space emulation. While it is built on top of the QEMU powered Unicorn CPU emulator, Zelos provides the operating system details required to fully emulate binary execution from loading, down to system calls. We quickly found use for Zelos as a dynamic instrumentation tool that could unpack malware, categorize and report malicious behavior, as well as extract domains from Domain Generation Algorithms (DGA). The myriad of uses we uncovered drove us to develop a plugin system to encourage extensions.

In this demo, in addition to highlighting Zelos's core dynamic analysis features, we'll showcase a new plugin released at BlackHat which provides automated root cause analysis (RCA), a method of identifying causes of crashes, through data flow analysis. Applications of automated RCA range from helping developers locate and fix bugs to triaging crashes generated through fuzzing. Existing techniques for identifying root cause through data flow analysis may require recompilation of binaries to insert instrumentation, integration of multiple tools, or collecting execution traces. Using Zelos, identifying the root cause can be as simple as providing the binary with the crashing input. We will highlight how we perform architecture agnostic dataflow analysis by utilizing QEMU's internal assembly code representation and show how easy RCA can be, even without source code.

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Deoptfuscator: Automated Deobfuscation of Android Bytecode using Compilation Optimization</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Gyoosik Kim](https://img.shields.io/badge/Gyoosik%20Kim-informational) ![Geunha You](https://img.shields.io/badge/Geunha%20You-informational) ![Seong-je Cho](https://img.shields.io/badge/Seong-je%20Cho-informational)

🔗 **Link:** Not Available  
📝 **Description:** Code obfuscation is a technique that makes programs harder to understand. Malware writers widely the obfuscation technique to evade detection from anti-malware software, or to deter reverse engineering attempts for their malicious code. Typical obfuscation techniques applied to Android malicious apps include identifier renaming, string encryption, control-flow obfuscation, and Java reflection (API hiding). If we de-obfuscate the obfuscated code and restore it to the original code before obfuscation was applied, we can analyze the obfuscated malware effectively and efficiently.

Therefore, we have developed Deoptfuscator, an effective tool for de-obfuscating the Android applications that have been transformed using control-flow obfuscation mechanisms. That is, it can reverse the control-flow obfuscation of Android APKs.

The features of Deoptfuscator are as follows:
- Deoptfuscator can detect obfuscation traces (especially, opaque predicates) utilizing the optimization approach of Android ART's ahead-of-time (AOT) compiler. It effectively optimizes the control flow of an obfuscated app using ReDex as well as the detected obfuscation traces.
- If the obfuscated Android app can run on a device, the de-obfuscated app reversed by Deoptfuscator can run on the device too.
- Deoptfuscator can reverse the control-flow obfuscation techniques of DexGuard that other de-obfuscation tools haven't.
- If Deoptfuscator is used in conjunction with other de-obfuscators such as DeGuard that can reverse identifier renaming of Android APKs, it can be a more powerful de-obfuscation tool.



This research was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT (no. 2018R1A2B2004830)

</details>

<details><summary><strong>Stantinko deobfuscation arsenal</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Vladislav Hrčka](https://img.shields.io/badge/Vladislav%20Hrčka-informational)

🔗 **Link:** Not Available  
📝 **Description:** Stantinko is a malware family, which has been active since at least 2012, and has been gradually improving its code obfuscation techniques to hinder analysis and detection – especially in its recent versions. The half-million-strong Stantinko botnet has been used by its operators for various cybercriminal activities, including click fraud, ad injection, social network fraud, password stealing attacks, and cryptomining.

Stantinko's custom obfuscation techniques can be divided into four categories: control-flow flattening, string obfuscation, do-nothing code, and dead code, strings and resources. The techniques are employed in both x86 and x64 versions of the malware and we'll focus particularly on the first two.

These control-flow-flattening loops generally merge multiple functions into one. They transform the control flow to a form that is hard to read and the execution order of basic blocks is unpredictable without extensive analysis.

Stantinko's string obfuscation technique resembles construction of strings on the stack, but it additionally uses standard C functions for string manipulation with various decoy words and sentences to compose the final string.

These enhancements to the otherwise common obfuscations are what make them unique and turn ordinary reverse engineering methods to deal with the techniques useless.

</details>

---
## 🔍 OSINT
<details><summary><strong>KubiScan: Searching for Risky Pods and Permissions in Kubernetes Cluster</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Eviatar Gerzi](https://img.shields.io/badge/Eviatar%20Gerzi-informational)

🔗 **Link:** [KubiScan: Searching for Risky Pods and Permissions in Kubernetes Cluster](https://github.com/cyberark/KubiScan)  
📝 **Description:** KubiScan is a tool that was created to search for risky Pods which contain a privileged service account tokens that can be used for privilege escalation or even compromising the cluster. It can also show you all the risky roles, rolebindings, users and privileged pods in the Kubernetes Cluster and other cool stuff.

</details>

<details><summary><strong>Manuka: A modular, scalable OSINT honeypot targeting pre-attack reconnaissance techniques</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Eugene Lim](https://img.shields.io/badge/Eugene%20Lim-informational) ![Kee Hock Tan](https://img.shields.io/badge/Kee%20Hock%20Tan-informational) ![Bernard Lim](https://img.shields.io/badge/Bernard%20Lim-informational) ![Kenneth Tan](https://img.shields.io/badge/Kenneth%20Tan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Manuka is an Open-source intelligence (OSINT) honeypot that monitors reconnaissance attempts by threat actors and generates actionable intelligence for Blue Teamers. It creates a simulated environment consisting of staged OSINT sources, such as social media profiles and leaked credentials, and tracks signs of adversary interest, closely aligning to MITRE's PRE-ATT&CK framework. Manuka gives Blue Teams additional visibility of the pre-attack reconnaissance phase and generates early-warning signals for defenders.

Although they vary in scale and sophistication, most traditional honeypots focus on networks. These honeypots uncover attackers at Stage 2 (Weaponization) to 7 (Actions on Objectives) of the cyber kill chain, assuming that attackers are already probing the network.

Manuka conducts OSINT threat detection at Stage 1 (Reconnaissance) of the cyber kill chain. Despite investing millions of dollars into network defenses, organisations can be easily compromised through a single Google search. One recent example was hackers exposing corporate meetings, therapy sessions, and college classes through Zoom calls left on the open Web. Enterprises need to detect these OSINT threats on their perimeter but lack the tools to do so.

Manuka is built to scale. Users can easily add new listener modules and plug them into the Dockerized environment. They can coordinate multiple campaigns and honeypots simultaneously to broaden the honeypot surface. Furthermore, users can quickly customize and deploy Manuka to match different use cases. Manuka's data is designed to be easily ported to other third-party analysis and visualization tools in an organisation's workflow.

Designing an OSINT honeypot presents a novel challenge due to the complexity and wide range of OSINT techniques. However, such a tool would allow Blue Teamers to "shift left" in their cyber threat intelligence strategy.

</details>

<details><summary><strong>Token-Hunter & Gitrob: Hunting for Secrets</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Greg Johnson](https://img.shields.io/badge/Greg%20Johnson-informational)

🔗 **Link:** Not Available  
📝 **Description:** Secrets like API tokens, encryption keys, and passwords are a keystone in the development world. They facilitate important functionality not only in the software that developers build, but also in the deployment, maintenance, integration, and security of both closed and open-source projects. Many companies providing services on the internet offer API tokens in multiple flavors that allow interaction with their systems, as does GitLab. Token-Hunter and Gitrob are complementary tools developed, augmented, and heavily used by GitLab's red team to support their engagements and, most importantly, find those exposed secrets and demonstrate their abuse!

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>Semgrep: a code-aware grep for finding vulnerabilities and enforcing secure defaults</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Clint Gibler](https://img.shields.io/badge/Clint%20Gibler-informational) ![Isaac Evans](https://img.shields.io/badge/Isaac%20Evans-informational)

🔗 **Link:** Not Available  
📝 **Description:** Semgrep is a tool for easily detecting and preventing bugs and anti-patterns in your codebase. It combines the convenience of grep with the correctness of syntactical and semantic search.

Semgrep is fast (scans 100Ks LOC in seconds), supports multiple languages (JavaScript, Python, Golang, Java, C), and is easy to customize, so that users can create high value org-specific or project-specific checks without spending weeks learning a complicated DSL.

Semgrep works by parsing source code into an abstract syntax tree (AST), then allows users to supply patterns that fuzzily match the interesting code patterns. Because it's source code aware, its checks are higher signal than regexes (i.e., it's easy to match function calls, and not match text in comments, multi-line calls, or strings), but because it isn't doing interprocedural dataflow analysis, it doesn't take hours to run and won't make assumptions that result in hundreds of false positives requiring triage.

https://github.com/returntocorp/semgrep

</details>

---