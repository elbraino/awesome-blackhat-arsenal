# USA 2015
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2015** event held in **USA**.
Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.

## 📚 Table of Contents
- [Others](#others)
- [⚙️ Miscellaneous / Lab Tools](#⚙️-miscellaneous-lab-tools)
- [🌐 Web/AppSec](#🌐-webappsec)
- [🌐 Web/AppSec or Red Teaming](#🌐-webappsec-or-red-teaming)
- [📱 Mobile Security](#📱-mobile-security)
- [🔍 OSINT](#🔍-osint)
- [🔴 Red Teaming](#🔴-red-teaming)
- [🔴 Red Teaming / AppSec](#🔴-red-teaming-appsec)
- [🔵 Blue Team & Detection](#🔵-blue-team-detection)
- [🟣 Red Teaming / Embedded](#🟣-red-teaming-embedded)
- [🧠 Reverse Engineering](#🧠-reverse-engineering)
---
## 🔴 Red Teaming
<details><summary><strong>Active Directory Backdoors: Myth or Reality BTA: Open-Source Tool for AD Analysis</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Joffrey Czarny](https://img.shields.io/badge/Joffrey%20Czarny-informational)

🔗 **Link:** Not Available  
📝 **Description:** When it comes to the security of the information system, Active Directory domain controllers are, or should be, at the center of concerns, which are (normally) to ensure compliance with best practices, and during a compromise proved to explore the possibility of cleaning the information system without having to rebuild Active Directory. However, few tools implement this process and several ways exist to backdoor Active Directory. We propose to present some possible backdoors which could be set by an intruder in Active Directory to keep administration rights. For example, how to modify the AdminSDHolder container in order to reapply rights after administrator actions. Moreover, backdoors can be implemented in Active Directory to help an intruder to gain back his privileges. Then, we will present BTA, an audit tool for Active Directory databases, and our methodology for verifying the application of good practices and the absence of malicious changes in these databases.The presentation will be organized as follows:- We begin by describing the stakes around the Active Directory, centerpiece of any information system based on Microsoft technologies.- We will continue by demonstrating some backdoors in order to keep admins rights or to help an intruder to quickly recover admins rights.- We will present BTA and the methodology developed to analysis Active Directory.We conclude with a feedback on real world usage of BTA.More information can be found on the Bitbucket repository https: //bitbucket.org/iwseclabs/bta

</details>

<details><summary><strong>Backdoor Factory (BDF) and BDFProxy</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Joshua Pitts](https://img.shields.io/badge/Joshua%20Pitts-informational)

🔗 **Link:** [Backdoor Factory (BDF) and BDFProxy](https://github.com/secretsquirrel/the-backdoor-factory)  
📝 **Description:** The Backdoor Factory (BDF), first released in 2013, is an open source framework for patching PE, ELF, and Mach-O binaries with payloads or shellcode.  Combine that with BDFProxy, a tool based on mitmProxy and BDF to MitM patch binaries during download over HTTP, pentesters can bring unique attack capabilities to red teaming engagements and other testing engagements. BDF/BDFProxy is included in multiple operating systems and frameworks including Kali-Linux, Veil-Evasion, BlackArch Linux, and MITMf.The presenter will demo multiple use cases, from red teaming, testing OS security, cover framework internals, writing custom scripts, and new features.

</details>

<details><summary><strong>CapTipper</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Omri Herscovici](https://img.shields.io/badge/Omri%20Herscovici-informational)

🔗 **Link:** [CapTipper](https://github.com/omriher/CapTipper)  
📝 **Description:** CapTipper is a python tool to analyze, explore, and revive HTTP malicious traffic. CapTipper sets up a web server that acts exactly as the server in the PCAP file and contains internal tools, with a powerful interactive console, for analysis and inspection of the hosts, objects, and conversations found.The tool provides the security researcher with easy access to the files and the understanding of the network flow, and is useful when trying to research exploits, pre-conditions, versions, obfuscations, plugins, and shellcodes.Feeding CapTipper with a drive-by traffic capture (e.g. of an exploit kit) displays the user with the REQUEST_URI's that were sent and metadata responses. The user can at this point browse to http://127.0.0.1/[URI] and receive the response back to the browser. In addition, an interactive shell is launched for deeper investigation using various commands such as hosts, hexdump, info, ungzip, body, client, dump, and more.

</details>

<details><summary><strong>Exploit Pack</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Juan Sacco](https://img.shields.io/badge/Juan%20Sacco-informational)

🔗 **Link:** [Exploit Pack](https://github.com/jsacco)  
📝 **Description:** Exploit Pack use an advanced software-defined interface that supports rapid reconfiguration to adapt exploit codes to the constantly evolving threat environment. Our technologies allow you to rapidly tests and defend against hostile remote targets.The mission of Exploit Pack is to process and exploit security issues, gain access and report incidents in a technical report to help you defend against hostile systems. We have successfully demonstrated our capabilities to detect, track, identify and negate security flaws.Website:http://exploitpack.com

</details>

<details><summary><strong>Linux-Inject</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Tyler Colgan](https://img.shields.io/badge/Tyler%20Colgan-informational)

🔗 **Link:** [Linux-Inject](https://github.com/maxcompston/inject-hook-linux)  
📝 **Description:** Have you ever wanted to inject code into a Linux process, but found yourself lacking an easy way to do it? Ever wished Linux had a system call, like CreateRemoteThread on Windows? Linux-Inject is the tool you were wishing for! It can load a shared object inside another process, in much the same way Windows lets you load DLLs in other processes. It does this by attaching to the target process with ptrace and overwriting part of its address space with a custom loader. Once the target process has executed the loader, Linux-Inject restores the target's overwritten memory and register state and sends it on its merry way. At that point, it's up to you to wreak whatever havoc you'd like within the target process via the newly loaded shared object. Linux-Inject supports x86, x86_64, and ARM.

</details>

<details><summary><strong>Mana</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dominic White](https://img.shields.io/badge/Dominic%20White-informational)

🔗 **Link:** [Mana](https://github.com/sensepost/hostapd-mana)  
📝 **Description:** Mana Toolkit is a Wi-Fi rogue access point toolkit whose purpose is getting as many clients connected, and getting as many credentials from their connections. It was first presented at Defcon 22 last year (https://youtu.be/i2-jReLBSVk). It started as an attempt to get KARMA attacks working again, but ended up going much further. We will be extending it even further for Arsenal.It implements several patches to hostapd that:- Implement our improved KARMA attacks- Implement EAP credential interception (freeradius-wpe style, but built in)- Auto crack 'n add, where EAP credentials are cracked automatically to get the client to connect to a fake network with EAPAdditionally, it includes several configurations and scripts to gather credentials:- Firelamb - Our reimplementation of firesheep in python to grab cookies- Sslstrip-hsts - Leonardo NVE's HSTS bypass implementation- Certificate side loading - To attempt to load malicious certificates to better intercept SSL connections- Captive portal social engineering - Attempts to gather creds with fake captive portal, or google pages- Fake-internet - To fool various devices into thinking they are onlineFor Arsenal, we'll be improving the EAP functionality quite significantly, and adding the ability to target specific devices, as well as several bug fixes.More information can be found in the slides: http://www.slideshare.net/sensepost/improvement-in-rogue-access-points-sensepost-defcon-22

</details>

<details><summary><strong>MITMf</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Marcello Salvati](https://img.shields.io/badge/Marcello%20Salvati-informational)

🔗 **Link:** [MITMf](https://github.com/byt3bl33d3r/MITMf)  
📝 **Description:** The current state of Man-In-The-Middle tools is abysmal, most of them just don't work, are completely outdated or require a lot of time and effort to get working.MITMf brings to the table a one-stop-shop for offensive Man-In-The-Middle attacks, while improving and updating existing techniques.Written in Python, it's designed to be modular, customizable and extendible: anyone can write a custom plugin for their own needs.Currently the following plugins are available:- Responder - LLMNR, NBT-NS and MDNS poisoner- SSLstrip+ - Partially bypass HSTS- Spoof - Redirect traffic using ARP Spoofing, ICMP Redirects or DHCP Spoofing and modify DNS queries- Sniffer - Sniffs for various protocol login and authorized attempts- BeEFAutorun - Autoruns BeEF modules based on clients OS or browser type- AppCachePoison - Perform app cache poison attacks- SessionHijacking - Performs session hijacking attacks, and stores cookies in a firefox profile- BrowserProfiler - Attempts to enumerate all browser plugins of connected clients- CacheKill - Kills page caching by modifying headers- FilePwn - Backdoor executables being sent over http using bdfactory- Inject - Inject arbitrary content into HTML content- JavaPwn - Performs drive-by attacks on clients with out-of-date java browser plugins- Jskeylogger - Injects a javascript keylogger into clients webpages- Replace - Replace arbitary content in HTML content- SMBAuth - Evoke SMB challenge-response auth attempts- Upsidedownternet - Flips images 180 degrees

</details>

<details><summary><strong>Nishang - The Black Hat Version</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![None](https://img.shields.io/badge/None-informational)

🔗 **Link:** [Nishang - The Black Hat Version](https://github.com/samratashok/nishang)  
📝 **Description:** Nishang is a framework which enables using PowerShell for Penetration Testing and Offensive Security. In the Black Hat edition, many interesting scripts and payloads will be released, as well as live demos of some work in progress will be done. Techniques like running shellcode in memory, using Gmail for code execution, SSID names for command execution, network relays, and more will be discussed.Come to see how PowerShell and Nishang could be used to enhance your Penetration Test.

</details>

<details><summary><strong>Nsearch</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Juan Jacobo TibaquirÃ¡](https://img.shields.io/badge/Juan%20Jacobo%20TibaquirÃ¡-informational)

🔗 **Link:** Not Available  
📝 **Description:** Nsearch is a tool that helps you find scripts that are used nmap (nse) it can be searched using the name, category author or combining the parameters. It is also possible to see the documentation of the scripts found, the principal programing is python. You can save your favorites scripts into a db table and set a rank. The tool has an auto installer script for debian (ubuntu, mint, kali linux), Red Hat (Fedora, CentOS), and MacOX. Nsearch is still under developing, the next features for adding are:- Launch nmap from the application using your own list of scripts favorites as a parameters- Release a version for windows- Release a GUI

</details>

<details><summary><strong>SpeedPhishing Framework (SPF)</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational)

🔗 **Link:** [SpeedPhishing Framework (SPF)](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/phishing/spf.md)  
📝 **Description:** SPF is an open source simple email phishing tool/framework which can assist penetration testers in quickly deploying phishing exercises in minimal time. The tool, when provided minimal input (such as just a domain name), can automatically search for potential targets, deploy multiple phishing websites, craft and send phishing emails to the targets, record the results, generate a basic report, among other more advanced tasks.Features include:- Written in Python- Can be run fully Automated- Automated Target Identification- Profiling of Target Company- Hosting of Templated and Dynamical y Generated Phishing Websites- Sending of Emails- Collection of Phishing results- Verification of ResultsThe presenter will demo multiple use cases, cover framework internals, and new features.

</details>

<details><summary><strong>WireEdit</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Michael Sukhar](https://img.shields.io/badge/Michael%20Sukhar-informational)

🔗 **Link:** Not Available  
📝 **Description:** Text editors give us means to manipulate text documents without knowing the character encoding schemes and formatting mechanisms. Vector graphics editors allow us to edit vector based pictures without understanding the underlying vector math.We love Wireshark. It does a fantastic job capturing, decoding and analyzing network packets. But what if you want to edit them?WireEdit is a WYSIWYG editor for network packets. It allows editing network packets at any stack layer without knowing anything about their syntax and encoding rules.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>Bearded</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Viacheslav Bakhmutov](https://img.shields.io/badge/Viacheslav%20Bakhmutov-informational)

🔗 **Link:** [Bearded](https://github.com/leoliu0/name_matching/blob/master/surname.txt)  
📝 **Description:** Bearded is an open source Security Automation platform. The platform allows Development, QA, and Security team members to perform automated web security scans with a set of tools (w3af, sslyze, nmap, arachni etc), and re-execute those scans as needed. All tools can be executed in the cloud in docker containers. Bearded has a default web interface which integrates all core options and makes it possible to manage large pentests easily.Similar to owtf or minion, but using docker containers and scalable for clouds.

</details>

<details><summary><strong>Burp-hash</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Scott Johnson](https://img.shields.io/badge/Scott%20Johnson-informational) ![Tim MalcomVetter](https://img.shields.io/badge/Tim%20MalcomVetter-informational) ![Matt South](https://img.shields.io/badge/Matt%20South-informational)

🔗 **Link:** [Burp-hash](https://github.com/burp-hash/burp-hash)  
📝 **Description:** Burp-hash is a Burp Suite plugin. Many applications will hash parameters, such as ID numbers and email addresses for use in secure tokens, like session cookies. The plugin will passively scan requests looking for hashed values. Once a hashed value is found, it is compared to a table of parameters already observed in the application to find a match. The plugin keeps a lookout for parameters, such as usernames, email addresses, and ID numbers. It also keeps a lookout for hashes (SHA, MD5, etc). It hashes new data and compares to observed hashes. The user receives a notification if any hashes match. This automates the process of trying to guess common parameters used in the generation of hashes observed in an application.

</details>

<details><summary><strong>CuckooSploit</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![David Oren](https://img.shields.io/badge/David%20Oren-informational)

🔗 **Link:** [CuckooSploit](https://github.com/davidoren/CuckooSploit)  
📝 **Description:** CuckooSploit is an environment for comprehensive, automated analysis of web-based exploits, based on Cuckoo sandbox.The framework accepts URL or a PCAP file, and works at three levels:Exploitation Process - Detecting the core components of the exploitation process (ROP chains, shellcodes, and heap sprays) for when exploitation takes place but fails to launch payload for several reasons, along with immediate successful post-exploitation phenomena (example, process creation).Full Flow Emulation - Implementing the approach of full web emulation, rather than emulation of a single file at a time, since many exploits served by Exploit Kits do not work out of the web-page context (require configurations and/or arguments).Web Flow Detection  Redirection sequence chains, JavaScript obfuscations, evasion techniques.By using full web emulation on different combinations of OS/browser/plugin version, CuckooSploit increases the rate of malicious URL detection and presents a reliable verdict and, in some cases, CVE identification.

</details>

<details><summary><strong>OWASP Broken Web Applications VM v12</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Chuck Willis](https://img.shields.io/badge/Chuck%20Willis-informational)

🔗 **Link:** Not Available  
📝 **Description:** The Open Web Application Security Project (OWASP) Broken Web Applications project (www.owaspbwa.org) provides a free and open source virtual machine loaded with web applications containing security vulnerabilities. This session will showcase the project VM and exhibit how it can be used for training, testing, and experimentation by people in a variety of roles.Demonstrations will cover how the project can be used by penetration testers who discover and exploit web application vulnerabilities, by developers and others who prevent and defend against web application attacks, and by individuals who respond to web application incidents.  New features and applications in the recently released version 1.2 of the VM will also be highlighted.

</details>

<details><summary><strong>OWASP Distributed Web Honeypots Project</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ryan Barnett](https://img.shields.io/badge/Ryan%20Barnett-informational)

🔗 **Link:** [OWASP Distributed Web Honeypots Project](https://github.com/SpiderLabs/owasp-distributed-web-honeypots/blob/master/README.md)  
📝 **Description:** The goal of the Distributed Web Honeypot (DWH) Project is to identify emerging attacks against web applications and report them to the community. This may include automated scanning activity, probes, as well as, targeted attacks against specific web sites or applications. The scope of this project has recently been expanded to include deployment of both standard web application honeypots and/or open proxy honeypots. Project participants may choose whether they want to run their honeypot as an open proxy or a stand-alone sensor. During the Black Hat Arsenal Demos, participants will be able to view live attack data within the central console server. We are also seeking participants who would like to join the project and deploy sensors.

</details>

<details><summary><strong>PixelCAPTCHA - A Unicode Based CAPTCHA Scheme</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Gursev Singh Kalra](https://img.shields.io/badge/Gursev%20Singh%20Kalra-informational)

🔗 **Link:** [PixelCAPTCHA - A Unicode Based CAPTCHA Scheme](https://github.com/salesforce/pixel-captcha-project/blob/master/demo-webapp/src/main/java/com/salesforce/pixelcaptcha/demo/unused/TestCaptchaGenerator.java)  
📝 **Description:** The demo will discuss a new visual CAPTCHA scheme that leverages the 64K Unicode code points from the Basic Multilingual Plane (plane 0) to construct the CAPTCHAs that can be solved with 2 to 4 mouse clicks. We will discuss the design principles, the security mechanisms and its various features.There will be demonstrations for the various CAPTCHA configurations and the use cases. The proposed PixelCAPTCHA scheme will be released as an open source Java library along with a demo website.

</details>

<details><summary><strong>Reissue Request Scripter (Burp Plugin)</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![None](https://img.shields.io/badge/None-informational)

🔗 **Link:** [Reissue Request Scripter (Burp Plugin)](https://github.com/snoopysecurity/awesome-burp-extensions)  
📝 **Description:** This Burp plugin has one focus built script to replay HTTP request with various scripting language. It supports Python, Ruby, Perl, PHP, Powershell, and JavaScript. It is the swiss knife of the custom HTTP web exploits.This plugin starts where other automated tools reach their limit. It integrates itself well with "python-paddingoracle" tool to create custom padding oracle attack. It can be used to build quickly malicious JavaScript request for XSS payload. It can be used along sqlmap to exploit second order SQL injection.The BH Arsenal demo will focus on the most common usage: Padding Oracle, SQLi and XSS payload.The Burp plugin is available for download on GitHub and on the Burp App Store:- https://github.com/h3xstream/http-script-generator- https://pro.portswigger.net/bappstore/ShowBappDetails.aspx?uuid=6e0b53d8c801471c9dc614a016d8a20d

</details>

<details><summary><strong>SAMLyze</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Jon Barber](https://img.shields.io/badge/Jon%20Barber-informational)

🔗 **Link:** Not Available  
📝 **Description:** Have you ever been faced with a Security Assertion Markup Language (SAML) Service Provider and dreaded the development effort required to attack it? Have you ever crafted custom SAML payloads and wondered why no one had written this tool before? SAMLyze is a new tool that makes pentesting SAML Service Providers fast and easy. It streamlines the attack process by providing preconfigured payloads for testing against XXE, DTD and automatically performs a variety of SAML validations. The web interface makes configuration of custom assertions and modification of any SAML response values simple. Additionally, the SAMLyze workflow allows for integration with web proxies such as Burp Suite and Zed Attack Proxy.

</details>

<details><summary><strong>SecLists</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Jason Haddix](https://img.shields.io/badge/Jason%20Haddix-informational) ![Daniel Miessler](https://img.shields.io/badge/Daniel%20Miessler-informational)

🔗 **Link:** [SecLists](https://github.com/danielmiessler/SecLists)  
📝 **Description:** If you have been in the industry a little while you start to realize that tools are only as good as their fuzz lists. Great lists are the secret sauce behind mapping, bruteforcing, web exploitation, etc.The SecLists project is a collection of multiple types of lists used during security assessments. List types include usernames, passwords, URLs, sensitive data grep strings, fuzzing payloads, mapping/discovery, and many more. Our goals are to enable a security tester to pull this repo onto a new testing box and have access to every type of list that may be needed. This makes security testers less reliant on one tool and more empowered to write their own (or use the one of their choice).Come check out this project and we will walk you through several usages for the seclists project using your favorite proxies (Burp + ZAP, ++) and show how you can use it to enhance your current testing methodology!

</details>

<details><summary><strong>Sqlchop</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Yusen Chen](https://img.shields.io/badge/Yusen%20Chen-informational)

🔗 **Link:** [Sqlchop](https://github.com/chaitin/sqlchop)  
📝 **Description:** This awesome new tool, sqlchop, is a new SQL injection detection engine, using a pipeline of smart recursive decoding, lexical analysis and semantic analysis. It can detect SQL injection query with extremely high accuracy and high recall with 0day SQLi detection ability, far better than nowadays' SQL injection detection tools, most of which based on regex rules. We proposed a novel algorithm to achieve both blazing fast speed and accurate detection ability using SQL syntax analysis.I will provide a web interface to demonstrate our new engine. And some CTF-like SQL injection challenge. Hackers are welcomed to have a try.We will prepare gifts and bonus for those who bypass our engine successfully.

</details>

<details><summary><strong>WATOBO - The WebApplication ToolBox</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Andreas Schmidt](https://img.shields.io/badge/Andreas%20Schmidt-informational)

🔗 **Link:** [WATOBO - The WebApplication ToolBox](https://github.com/siberas/watobo/blob/master/watobo.gemspec)  
📝 **Description:** WATOBO is a security tool for testing web applications. It is intended to enable security professionals to perform efficient (semi-automated) web application security audits.Most important features are:- Powerful session management capabilities! You can define login scripts as well as logout signatures. So you don't have to login manually each time you get logged out.- Can act as a transparent proxy (requires nfqueue)- Vulnerability checks (SQLinjectin, XSS, LFI) out of the box- Handles Anti-CSRF-/One-Time-Tokens- Supports inline de-/encoding, so you don't have to copy strings to a transcoder and back again. Just do it inside the request/response window with a simple mouse click.- Smart filter functions, so you can find and navigate to the most interesting parts of the application easily.- Is written in (FX) Ruby and enables you to easily define your own checks- Runs on Windows, Linux, MacOS every OS supporting (FX) Ruby- Is free software (licensed under the GNU General Public License Version 2)

</details>

---
## 🔍 OSINT
<details><summary><strong>Breachego</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Christian Heinrich](https://img.shields.io/badge/Christian%20Heinrich-informational)

🔗 **Link:** Not Available  
📝 **Description:** Maltego Remote Transforms for Abusix, haveibeenpwned and BreachAlarm to perform link analysis and intrusion detection of compromised aliases, e-mail addresses, domains, plaintext and hashed passwords posted to Pastebin, Slexy, QuickLeak, Pastie, and Ghostbin.

</details>

<details><summary><strong>Intrigue</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Jonathan Cran](https://img.shields.io/badge/Jonathan%20Cran-informational)

🔗 **Link:** [Intrigue](https://gist.github.com/jcran?direction=asc&sort=created)  
📝 **Description:** Whether you're a penetration tester hunting easy targets, a bug bounty hunter looking to find bugs faster, or in charge of security for an enterprise network ... you need OSINT baked into your security processes. Join us for the world-wide release of Intrigue, an API-first framework for intelligence gathering and vulnerability discovery. The author will demo Intrigue, detail its architecture, and present results from IG experiments. Attendees will walk away with a scalable open-source framework for OSINT.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Chellam</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Vivek Ramachandran](https://img.shields.io/badge/Vivek%20Ramachandran-informational)

🔗 **Link:** [Chellam](https://github.com/atktgs/BlackHat2015Arsenal)  
📝 **Description:** Chellam is a Wi-Fi IDS/Firewall for Windows. Chellam can detect Wi-Fi attacks, such as Honeypots, Evil Twins, Mis-association, and Hosted Network based backdoors etc., against a Windows based client without the need of custom hardware or drivers.The tool also allows you to create Firewall like rule sets for Wi-Fi networks and create alerts etc. when there is a rule mismatch.

</details>

<details><summary><strong>CuckooDroid - An Automated Malware Analysis Framework</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Idan Revivo](https://img.shields.io/badge/Idan%20Revivo-informational) ![Ofer Caspi](https://img.shields.io/badge/Ofer%20Caspi-informational)

🔗 **Link:** Not Available  
📝 **Description:** To combat the growing problem of Android malware, we present a new solution based on the popular open source framework Cuckoo Sandbox to automate the malware investigation process. Our extension enables the use of Cuckoo's features to analyze Android malware and provides new functionality for dynamic and static analysis. Our framework is an all in one solution for malware analysis on Android. It is extensible and modular, allowing the use of new, as well as existing, tools for custom analysis.The main capabilities of our CuckooDroid include:- Dynamic Analysis - based on Dalvik API hooking- Static Analysis - Integration with Androguard- Emulator Detection Prevention- Virtualization Managers that support the popular virtualization solutions (VMware,Virtualbox, Esxi, Xen, and Kvm) and now also android emulator.- Traffic Analysis- Intelligence Gathering - Collecting information from Virustotal, Google Play etc.- Behavioral SignaturesExamples of well-known malware will be used to demonstrate the framework capabilities and its usefulness in malware analysis.

</details>

<details><summary><strong>Digital Disease Tracking Tool</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Efrain Ortiz](https://img.shields.io/badge/Efrain%20Ortiz-informational)

🔗 **Link:** [Digital Disease Tracking Tool](https://github.com/atktgs/BlackHat2015Arsenal)  
📝 **Description:** Today's digital ecosystem is harboring digital diseases that are increasingly resistant to antiviral measures. Many information security professionals continue to address the malware (digital disease pathogen) threat by focusing on antiviral methods and the re-imaging of infected hosts. The prevalence of infection is not conducive to the old reactive vaccination paradigm of one antidote signature for all. Can we learn from epidemiologists and how they investigate biological diseases? How do we enable more people to help in this digital medical crisis? We know there aren't enough people working on the digital disease problem, so how do we increase the numbers? This Digital Disease Control Web-Based Tracking app is an alpha proof of concept visualization tool, inspired by epidemiology, to enable entry level technicians to enter the security field.

</details>

<details><summary><strong>ElastAlert</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Quentin Long](https://img.shields.io/badge/Quentin%20Long-informational)

🔗 **Link:** [ElastAlert](https://github.com/Yelp/elastalert/blob/master/setup.py)  
📝 **Description:** ElastAlert is a simple framework for alerting on anomalies, spikes, or other patterns of interest from data in Elasticsearch. It works by combining Elasticsearch with two types of modular components, rule types and alerts. Elasticsearch is periodically queried and the data is passed to the rule type, which determines when a match is found. When a match occurs, it is given to one or more alerts, which take action based on the match.

</details>

<details><summary><strong>Noriben</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Brian Baskin](https://img.shields.io/badge/Brian%20Baskin-informational)

🔗 **Link:** [Noriben](https://github.com/Rurik)  
📝 **Description:** Noriben is an open-source system monitoring tool that allows for quick and simplified tracking of malware activity. By wrapping its operation around Microsoft SysInternals Process Monitor, Noriben uses a comprehensive set of filters to generate very succinct reports that provide the required indicators to create Indicators of Compromise (IoC) alerts.Requirements:- Windows-based system with SysInternals Procmon.exe- Python 2.7.9 or 3.x.- Optional Python Requests and a VirusTotal public API key for VT lookups- Optional Python lib-yara for automated Yara scanningNoriben takes large volumes of system activity and filters out the background noise of system activity and legitimate operations. By focusing solely on important API calls, for file creation, registry operations, and network connections, Noriben creates a simple and straightforward report that features only the indicators that a security analyst or malware analyst cares about. Along with collecting indicators, Noriben will process all created or modified files through a collection of provided Yara signatures and detail any results. It will also submit any file hash to VirusTotal to collect its virus score.As Noriben runs in the background during live operation, it is also suitable to acquire activity while malware is being actively debugged by an analyst. This allows for the collection of artifacts not found during normal operation in standard sandboxes.Within 60 seconds an analyst can get a good handle on a malware's capability and determine if it's a new variant of a known family or something completely new and requiring reverse engineering. Noriben is currently in sophomore stages of development and is deployed in a number of malware analysis labs, including those run by federal law enforcement agencies and defense contractors, relying on its output simplicity to help analysts create actionable intelligence.

</details>

<details><summary><strong>Objective-Sees OS X Security Tools</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [Objective-Sees OS X Security Tools](https://github.com/objective-see/FileMonitor)  
📝 **Description:** Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of OS X malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer he's written various OS X security tools that he now shares online (always free!), via his personal website objective-see.com. So come watch as KnockKnock generically detects persistent OS X malware, DHS reveals hijacked applications, and BlockBlock provides runtime protection of persistence locations. Our Macs will remain secure!

</details>

<details><summary><strong>Openioc_Scan</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Takahiro Haruyama](https://img.shields.io/badge/Takahiro%20Haruyama-informational)

🔗 **Link:** [Openioc_Scan](https://github.com/TakahiroHaruyama/openioc_scan)  
📝 **Description:** Indicator of Compromise (IOC) is a piece of information that can be used to search for or identify potentially compromised systems. Forensic investigators can define and share IOC files according to some standards or rules such as OpenIOC and YARA. Currently, many IOCs are available on the Internet, but most of the IOCs cannot be used for memory forensics because they are composed of indicators dependent on disk or live response data.Two years ago, I introduced "volatile IOCs" based on RAM evidence only at SANS DFIR Summit 2013. We can detect malware in memory images using them faster than using disk-based traditional IOCs. Besides, we can define indicators based on not only metadata like file paths but also malware functions such as code injection sign, imported functions, unpacked codes, and so on. However, in order to scan threats using volatile IOCs, we needed to use a closed-source tool based on OpenIOC standard. I could not improve it even if there were some limitations in the tool.That's why I implemented "openioc_scan" as a plugin for Volatility Framework which is an open-source memory forensic tool. In this demonstration, I explain how to use it and details of the implementation. Furthermore, I also show the results of considerations about IOCs to detect unknown malware in RAM by focusing on generic traits of malware.

</details>

<details><summary><strong>Osxcollector</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ivan Leichtling](https://img.shields.io/badge/Ivan%20Leichtling-informational)

🔗 **Link:** [Osxcollector](https://github.com/Yelp/osxcollector)  
📝 **Description:** We use Macs a lot at Yelp, which means that we see our fair share of Mac-specific security alerts. Host based detectors will tell us about known malware infestations or weird new startup items. Network based detectors see potential C2 callouts or DNS requests to resolve suspicious domains. Sometimes our awesome employees just let us know, "I think I have like Stuxnet or conficker or something on my laptop." When alerts fire, our incident response team's first goal is to "stop the bleeding"  to contain and then eradicate the threat. Next, we move to "root cause the alert"  figuring out exactly what happened and how we'll prevent it in the future. One of our primary tools for root causing OS X alerts is OSXCollector. OSXCollector is an open source forensic evidence collection and analysis toolkit for OS X. It was developed in-house at Yelp to automate the digital forensics and incident response (DFIR) our crack team of responders had been doing manually.

</details>

<details><summary><strong>peepdf</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jose Miguel Esparza](https://img.shields.io/badge/Jose%20Miguel%20Esparza-informational)

🔗 **Link:** [peepdf](https://github.com/jesparza/peepdf)  
📝 **Description:** peepdf is a Python tool to explore PDF files in order to find out if the file can be harmful or not. The aim of this tool is to provide all the necessary components that a security researcher could need in a PDF analysis without using 3 or 4 tools to make all the tasks. With Peepdf it's possible to see all the objects in the document showing the suspicious elements, supports all the most used filters and encodings, it can parse different versions of a file, object streams and encrypted files. With the installation of PyV8 and Pylibemu it provides Javascript and shellcode analysis wrappers too. Apart of this it's able to create new PDF files and to modify/obfuscate existent ones.

</details>

<details><summary><strong>Pestudio</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Marc Ochsenmeier](https://img.shields.io/badge/Marc%20Ochsenmeier-informational)

🔗 **Link:** [Pestudio](https://github.com/jnwilson/MalwareExercises/blob/master/pestudio/pestudio/changes_log.txt)  
📝 **Description:** Pestudio is a unique tool that allows you to perform an initial assessment of a malware without even infecting a lab system or studying its code.Malicious executable often attempts to hide its malicious behavior and to evade detection. In doing so, it generally presents anomalies and suspicious patterns. The goal of Pestudio is to detect these anomalies, provide Indicators and score the Trust for the executable being analyzed. Since the executable file being analyzed is never started, you can inspect any unknown or malicious executable with no risk.Pestudio has been in the top 10 list of "Best Security Tool" in 2013 and 2014 by the readers of ToolsWatch.org.

</details>

<details><summary><strong>Rudra - The Destroyer of Evil</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ankur Tyagi](https://img.shields.io/badge/Ankur%20Tyagi-informational)

🔗 **Link:** [Rudra - The Destroyer of Evil](https://github.com/7h3rAm/rudra)  
📝 **Description:** Rudra provides a framework for automated inspection of network capture files. It extends upon another tool called flow inspect and adds subsequent file-format aware analytics to its feature set. It consumes network capture files as input and passes them through a file type-specific analysis chain. In this chain, the file is operated upon by individual modules like:- FileID - Populates metadata like file entropy, compression ratio, hashes, bitrate, average packet rate, duration, etc.- Libnids - Handles IP defragmentation and TCP reassembly- ProtoID - Custom-made, minimal, regex-based protocol identification module (currently supports HTTP/SMTP/FTP/IMAP/POP3 identification)- Heuristics Engine - Uses a stochastic model based flow scanning engine to detect network traffic abnormalities- Yara Scan - Uses Yara's file scanning features to identify malicious network streams- Shellcode Scan - Uses Libemu to emulate and identify x86 shellcode- Regex Scan - Helps to identify and extract useful pieces of information (hashes, email addresses, private API keys, password DBs, etc.) from network traffic flows- Entropy visualization wih graphing support- DNS/Whois/GeoIP (with Google Maps API v3 integration) modulesEach of these modules sends a report JSON that is then collated to provide a highly verbose summary of the capture file. The analyst has an option of requesting the report in any one of the supported formats (JSON, HTML, PDF).The framework provides command-line based interactive interface that exposes a file analysis object. This object can be used to scan files and generate reports. This architecture also allows quick embedding within third-party tools and applications. Most of the analysis modules accept configuration options and as such provide a faster alternative to directly tweaking codebase.With the above listed modules and features in place, the project is still under development. There are plan to extend its functionality beyond capture files to include binary and document formats with the first public release.

</details>

<details><summary><strong>Sphinx</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Takehiro Takahashi](https://img.shields.io/badge/Takehiro%20Takahashi-informational)

🔗 **Link:** [Sphinx](https://github.com/hiro4848/sphinx)  
📝 **Description:** Sphinx is a highly scalable open source security monitoring tool that offers real-time auditing and analysis of host activities. It works by having clients forward various types of event logs including process execution with cryptographic signature (MD5 hash), network activity, dll/driver loading, as well as miscellaneous system events to a Sphinx server where each event is recorded and analyzed.With Sphinx, you can quickly find an answer to questions like:- Can we get a list of every event that happened on machine X between date Y and date Z?- Can we graphically trace what happened on my computer in the last 10 minutes because I feel there's something weird going on?- Who has run a piece of malware whose existence cannot be detected by our existing Anti-Virus product on our network?Give me a list of program executions as well as dll loads whose reputation is questionable or bad:- Is there Office application making outbound connection to China?- Are there any dlls injected into explorer.exe whose digital signature does not belong to Microsoft?You can build both simple and complex queries to search for threats. These queries can be run recurrently, and send alerts whenever there's a hit.

</details>

<details><summary><strong>TARDIS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Travis Smith](https://img.shields.io/badge/Travis%20Smith-informational)

🔗 **Link:** [TARDIS](https://github.com/Tripwire/TARDIS)  
📝 **Description:** Tripwire Automated Reconnaissance and Deep Inspection System (TARDIS) is a framework which ties together threat feed data such as STIX and vulnerability scan data and references log repositories for indicators of compromise(IoC).  Threat feeds and log repositories contain mountains of data that can be difficult to manage.  TARDIS pulls relevant data from each and outputs the filtered data which matters to information security operation teams.  During Arsenal, we'll show live attacks, exploits and detection mechanisms with TARDIS.  Learn how to integrate the tool into your existing infrastructure and how to add value through additional threat feed data.

</details>

<details><summary><strong>TriForce</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![David Cowen](https://img.shields.io/badge/David%20Cowen-informational)

🔗 **Link:** [TriForce](https://github.com/Jpja/BTC-and-XCP-Passphrase-Tools/blob/master/bulk-register-assets.html)  
📝 **Description:** Triforce is both a free and commercial product that allows an analyst to reconstruct past activity on a system down to the granular file change thanks to file system journaling forensics. New this year we've discovered even more data sources and can now go back up to 5 years in real world tests of individual granular file system changes.Learn how to:- Reverse Wipes- See what was uploaded and downloaded to dropbox- Discover the attackers toolkit- Discover the actual infection vector- Profile malware- See what attachments have been opened and when and more!

</details>

<details><summary><strong>UTIP - Unstructured Threat Intelligence Processing</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Elvis Hovor](https://img.shields.io/badge/Elvis%20Hovor-informational)

🔗 **Link:** [UTIP - Unstructured Threat Intelligence Processing](https://github.com/atktgs/BlackHat2015Arsenal)  
📝 **Description:** UTIP is an open-source solution that automates phases of threat data extraction from unstructured sources, and maps extracted elements to the STIX standard. By utilizing UTIP, security analysts and practitioners can:- Focus on analysis, instead of spending time parsing text in a document- Apply customized contextualization and prioritization filters to the extraction process- Increase automated communication (M2M) by converting ingested data into structured format- Perform higher order analysis on data extracted from these documents, and determine trends otherwise unattainableThe solution utilizes Scrumblr and Sketchy (open-source provided by Netflix) to scrape advisories, the OpenNLP stack for natural language processing, and a few machine learning techniques. The underlying web platform runs on Django, with D3 (JS framework) utilized to visualize insights drawn.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>CTF Tools</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Yan Shoshitaishvili](https://img.shields.io/badge/Yan%20Shoshitaishvili-informational)

🔗 **Link:** [CTF Tools](https://github.com/zardus)  
📝 **Description:** There are a lot of tools written for security research and CTFs, but fairly few gain enough traction to be packaged and distributed by the likes of Ubuntu, or even Kali. Worse, when they *are* packaged, the packaged versions are often hopelessly outdated. This is unfortunate, and causes most researchers to have to spend time tracking down, compiling, configuring, and installing these tools. Also, when a computer has to be reinstalled the process generally has to be done again.There is a need for a central repository of such tools to track them and allow security researchers to easily install them (without screwing up the whole host system!). This is the story of such a repository.I've gone through the list of tools I've used in CTFs and in my research I have found the ones that are not adequately packaged, and created a central place for install scripts. The build system works with simple shell scripts (for easier contribution of packages) and installs everything under ~/tools (or, really, any other directory), without any global system changes (except for apt-getting dependencies from official repositories).As far as I can tell, this is the first repository of obscure security research tools, and I think it'll be a useful thing for the community at large.

</details>

<details><summary><strong>Heybe - Pentest Automation Toolkit</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Bahtiyar Bircan](https://img.shields.io/badge/Bahtiyar%20Bircan-informational) ![Gokhan Alkan](https://img.shields.io/badge/Gokhan%20Alkan-informational)

🔗 **Link:** Not Available  
📝 **Description:** Heybe is Penetration Testing Automation Kit. It consists of modules that can be used to fully automate each step of pen-tests and make them most effective. With Heybe you can own all systems in a target company in matter of minutes. Heybe was first released during Black Hat USA 2014 Arsenal. This is new and updated version with some new modules.Heybe modules:Fener: Fast network discovery tool optimized for speed. Fener leverages several networking tools to discover all hosts within target network. Fener leverages automated active and passive discovery techniques to discover targets.Crowbar (Prevoiusly Levye): Brute force tool. Levye is used for automating brute forcing process against common and not so common protocols like openvpn and VNC.NetworK9 (Previously DepDep): Post exploitation tool. NK9 is a merciless sentinel which will seek sensitive files containing critical info leaking through your network.SeeS: High precision social engineering tool. Sees is used for performing tail-made social engineering campaigns with high success ratio.ADHunter: MS Active Directory takeover tool. It cane used to automate and speed up active directory attacks and give the keys to the kingdom in minutes.More information about Heybe modules can be found at following links:http://www.toolswatch.org/2014/05/new-tool-depdep-v1-0-determine-critical-data-in-network-sharing-released/http://www.galkan.net/2014/03/how-to-determine-critical-data-in-netwok-sharing.htmlhttp://blackarch.org/tools.html

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>D1c0m-X</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michael Hudson](https://img.shields.io/badge/Michael%20Hudson-informational)

🔗 **Link:** [D1c0m-X](https://github.com/atktgs/BlackHat2015Arsenal)  
📝 **Description:** DICOM (Digital Imaging and Communications in Medicine) is recognized worldwide for the exchange of medical tests, designed for handling, display, storage, printing, and transmission standard. It includes defining a file format and a network communication protocol.Target:D1c0m-X is a tool that is responsible for searching the TCP / IP port Robot surgery or x-rays, CT scans, MRI or other medical device that use this protocol, and once found, check if the firmware is vulnerable, if not vulnerable, try to exploit the same way using scripts, which are intended to block the connection between the server and the Robot, making a DDOS or accessing the System.Before launching the attack, D1c0m-X also explores the possibility of an intrusion through the Corporative Web of the Hospital or Clinic, if the intrusion is achieved, we proceed to interact with shell console, applying different vulnerabilities, such as SQLI, Default password, etc.Finally, the DUMP of critical information of Patients, Doctors and Staff is automated.

</details>

<details><summary><strong>Kautilya</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Nikhil Mittal](https://img.shields.io/badge/Nikhil%20Mittal-informational)

🔗 **Link:** [Kautilya](https://github.com/samratashok)  
📝 **Description:** Kautilya is a framework which enables using Human Interface Devices (HIDs) in Penetration Testing. Kautilya is capable of generating ready-to-use payloads for a HID. In the Black Hat edition, new payloads will be added and live demos will be shown.Come and learn techniques like dumping system secrets in plain, data, executing shellcode in memory, installing backdoors, dropping malicious files and much more using nothing but a HID capable of mimicking a keyboard.

</details>

<details><summary><strong>YARD Stick One</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Michael Ossmann](https://img.shields.io/badge/Michael%20Ossmann-informational) ![Taylor Streetman](https://img.shields.io/badge/Taylor%20Streetman-informational)

🔗 **Link:** [YARD Stick One](https://github.com/eq-3/occu/blob/master/WebUI/www/rega/licenseinfo.htm)  
📝 **Description:** YARD Stick One is a sub-1 GHz wireless transceiver controlled directly from your computer. It uses the same radio circuit as the popular IM-Me. The radio functions that are possible by customizing IM-Me firmware are now at your fingertips when you attach YARD Stick One to a computer via USB.YARD Stick One (Yet Another Radio Dongle) comes with RfCat firmware installed, courtesy of atlas. RfCat allows you to control the wireless transceiver from an interactive Python shell or your own program running on your computer. The device also has CC Bootloader installed, so you can upgrade RFCat or install your own firmware without any additional programming hardware.Featuring an external antenna connector, transmit and receive amplification, and plenty of expansion options, YARD Stick One is the most powerful CC1111 board available. Unlike previous devices based on the CC1111 transceiver, it operates effectively over the entire frequency range of the transceiver IC, and it is open source hardware.

</details>

---
## Others
<details><summary><strong>Damn Vulnerable iOS App (DVIA)</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Prateek Gianchandani](https://img.shields.io/badge/Prateek%20Gianchandani-informational)

🔗 **Link:** [Damn Vulnerable iOS App (DVIA)](https://github.com/prateek147)  
📝 **Description:** Damn Vulnerable iOS App (DVIA) is an iOS application that is damn vulnerable. The main goal is to provide a platform to mobile security enthusiasts/professionals or students to test their iOS penetration testing skills in a legal environment. This application covers all the common vulnerabilities found in iOS applications (following OWASP top 10 mobile risks) and contains several challenges that the user can try. This application also contains a section where a user can read various articles on iOS application security.Vulnerabilities and Challenges Include:- Insecure Data Storage- Jailbreak Detection- Runtime Manipulation- Piracy Detection- Sensitive information in memory- Transport Layer Security (http, https, cert pinning)- Client Side Injection- Information Disclosure- Broken Cryptography- Security Decisions via Untrusted input- Side channel data leakage- Application PatchingThe new version of DVIA will include vulnerabilities, like Brute forcing login screens, touch id bypass, insecure apple watch sync, insecure data storage, and vulnerabilities in extensions, etc.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Dradis Framework 3.0</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [Dradis Framework 3.0](https://github.com/etdsoft)  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 15 popular tools, including Nessus, Qualys, and Burp. Started in 2007, the Dradis Framework project has been growing ever since.Dradis is the best tool to consolidate the output of different scanners, add your manual findings and evidence and have all the engagement information in one place.Come to see Dradis 3.0 in action. Three years after our last official release, we've got a new version of the app that is ready for you to use and enjoy packed with new features (download-and-run packages, node properties, HTTP API, PDF reports), and new tool connectors (Acunetix, NTO spider).Come and check it out before we run out of stickers!

</details>

<details><summary><strong>Lynis</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Michael Boelen](https://img.shields.io/badge/Michael%20Boelen-informational)

🔗 **Link:** [Lynis](https://github.com/mboelen)  
📝 **Description:** Most of us have performed some level of system hardening, using checklists or custom scripts. The next level is to keep the security defenses of your systems compliant with your baselines. Lynis is an open source tool to help you with this goal. It is portable, flexible and specialized on Linux/Unix based systems. It performs an in-depth health check of your systems and tells you what additional steps you can take to lock them down. In this demo, we will see how easy it is to use, yet flexible enough to support much more than initially is visible.

</details>

---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>FindSecurityBugs</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Philippe Arteau](https://img.shields.io/badge/Philippe%20Arteau-informational)

🔗 **Link:** [FindSecurityBugs](https://github.com/find-sec-bugs/find-sec-bugs)  
📝 **Description:** FindSecurityBugs is a plugin for the Java static analysis tool FindBugs. This plugin consists of set rules that focus only on security weaknesses. It can be use by developers or security analysts to find vulnerabilities in their code.The plugin can identify weaknesses in Java web applications, Scala web applications and Android mobile applications. The assessment can be done in an IDE, such as Eclipse, or IntelliJ. It can also be configured in continuous integration environment, such as SonarQube.The demonstrations at BH Arsenal will focus on the integration in IntelliJ and SonarQube. Example of vulnerable applications will be scanned and basic code review methodology will be presented.FindSecurityBugs has already received some attention from the security community. It is integrated in the SWAMP code review service funded by the DHS. The OWASP Top 10 describe the tool as "the most promising" from the open source alternatives. It is used in the academia for security laboratories and the commercial sector. Finally, it was used with success in the code review of the Norwegian Voting System in 2013.The tool is released under LGPL and it is available for download at http://h3xstream.github.io/find-sec-bugs/

</details>

---
## 🧠 Reverse Engineering
<details><summary><strong>Preeny</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![None](https://img.shields.io/badge/None-informational)

🔗 **Link:** Not Available  
📝 **Description:** Preeny [1] helps you pwn noobs by making it easier to interact with binaries locally. It provides many different LD_PRELOAD binaries that implement a wide range of capabilities. Preeny can keep a binary from using ptrace, forking, or sending signals. It can override the random seed to disable randomness, suspend programs at startup (for debugging/analysis), patch binaries at load time, and can even convert network applications to be able to interact on the commandline. It's been used enable AFL to fuzz nginx [2], and has been used in a lot of reverse engineering, malware analysis, and exploitation work.The demo will go through Preeny's capabilities, discuss the addition of new functionality to Preeny, and detail scenarios where Preeny comes in handy.

</details>

<details><summary><strong>The Volatility Framework</strong></summary>

![Category: 🧠 Reverse Engineering](https://img.shields.io/badge/Category:%20🧠%20Reverse%20Engineering-orange) ![Michael Ligh](https://img.shields.io/badge/Michael%20Ligh-informational)

🔗 **Link:** [The Volatility Framework](https://github.com/volatilityfoundation/volatility/wiki/Volatility-Documentation-Project/92de893f43450b49a2ed39ddb68415d0fb87e464)  
📝 **Description:** The Volatility Framework is a completely open collection of tools, implemented in Python under the GNU General Public License, for the extraction of digital artifacts from volatile memory (RAM) samples of Windows, Linux, Mac OS X, and Android systems. After last year's Arsenal, we're excited to come back and demo an entirely different set of features, such as:- Extracting injected code and defeating anti-reversing tricks. In particular, we'll repair a PE file whose header(s) have been erased from memory.- How to reverse engineer PlugX and determine what system memory it manipulates to hide its persistence mechanism. We'll use what we learn to design a new Volatility plugin that detects the rootkit trick.- Using the new unified output rendering engine to consume and process large sets of memory artifacts in JSON, SQL, and other formats. In short, you'll learn how to build analysis tools on top of the Volatility Framework.

</details>

---
## 📱 Mobile Security
<details><summary><strong>QARK - Android Application SCA and Exploit Tool</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Tony Trummer](https://img.shields.io/badge/Tony%20Trummer-informational) ![Tushar Dalvi](https://img.shields.io/badge/Tushar%20Dalvi-informational)

🔗 **Link:** [QARK - Android Application SCA and Exploit Tool](https://github.com/syselement/ine-notes/blob/main/emapt/emapt-references.md)  
📝 **Description:** Introducing QARK (Quick Android Review Kit), a new tool designed with both red and blue teams in mind. QARK will perform static code analysis on Android applications, by decompiling them, parsing their manifests, and finally tokenizing the underlying Java code to allow full source-to-sink mapping.Unlike other tools QARK will also automatically create customized ADB commands to demonstrate vulnerabilities and probably coolest of all, it can create customized Proof-of-Concept apps to exploit the vulnerabilities it finds.

</details>

---