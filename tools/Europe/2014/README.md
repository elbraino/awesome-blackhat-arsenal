# Europe 2014
---
📍 12 tools demonstrated at **Black Hat Arsenal Europe 2014**, grouped by track category. Expand a tool for its description.

See also: [all tools by track](../../BY_CATEGORY.md) · [all tools A–Z](../../BY_NAME.md) · [main index](../../../README.md)

## 📚 Contents
- [Others](#others) (7)
- [🌐 Web/AppSec](#-webappsec) (2)
- [🔴 Red Teaming / AppSec](#-red-teaming--appsec) (1)
- [🔵 Blue Team & Detection](#-blue-team--detection) (1)
- [🟣 Red Teaming / Embedded](#-red-teaming--embedded) (1)
---
## Others
<details><summary><strong>Desenmascara.me</strong> — Emilio Casbas</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** Desenmascara.me is a public resource which will extract metadata from any website (either domain name or IP address, no resource) and will explain it in a brief summary. The extraction will be totally passive, just like browsing the website, otherwise the tool couldn't be online for public use. It's based mainly on HTTP headers and metadata. Some features of the tool are: -Easy to use, only enter a website address to see what's behind the scenes -Available in English and Spanish (based on the browser language) -Testing for web application fingerprinting -Brief summary about the website configuration -Different report colors to highlight web security awareness -Some special websites will show a message showing whether they are official or fake (keep counterfeit products from circulation) -Detection of CMSs and versions (whatweb core) -Warnings about old software being exploited in the wild like joomla-1.5, RoR CVE-2013-0156... -Detection of properties file leak in Ruby on Rails. Ref: Fugas de informacion en aplicaciones ruby on rails -Warnings about OpenSSL version affected by heartbleed -Detection of hardening signs such as WAF, CDN, reverse proxy... -In case of CloudFlare protected websites, it will show the real server IP -Detection of blacklisted websites by GoogleSafeBrowsing -Detection of suspicious iframes or hidden spam -Detection of misconfiguration on robots.txt files (i.e: exposing confidential information) -Detection of defacements, directory listings, private IP address in comments... -In the case of very known websites (Forbes, EA, .gov...) will inform about known security incidents which they were victim of -Stats about general web security awareness and some details of compromised websites (i.e: Forbes compromised)

</details>

<details><summary><strong>Exploit Pack</strong> — Juan Sacco</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** Exploit Pack is an open source GPLv3 security tool; the means is fully free and you can use it for any period of time without any kind of restriction. But why? Because other security products like metasploit, canvas, or impact are so incredibly expensive that unless you sell your kidney, you will not be able to buy it. Oh I forgot to mention that they are not GPLv3? Exploit Pack is 100% GPLv3, so if you feel like coding, just checkout the code and go for it. This tool was made thinking of the end-user; it's not going to replace any other security tool on the market, but it's for sure a must-have for every security enthusiast, researcher, or paranoid user.

</details>

<details><summary><strong>Lynis</strong> — Michael Boelen</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** Lynis is a free and open source security and auditing tool. It runs on Unix, Mac and Linux based systems. Lynis helps DevOps and security professionals detect vulnerabilities and configuration management weaknesses. When running the tool, an in-depth scan of the system will be performed. Therefore it is much more thorough than network based vulnerability scanners. It starts with the boot loader and goes up to installed software packages. After the analysis, it provides the discovered findings, including hints to further secure the system.

</details>

<details><summary><strong>NFCulT</strong> — Matteo Beccaro</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** NFCulT is an ultimate android application for exploiting and researching in NFC Mifare Ultralight security. Its first focus is against transport systems, but during the time, it has been applied to research vulnerabilities in bike sharing service, etc. It also implements the following published attacks: - Lock Attack - Time Attack - Replay Attack In this presentation, we will give a short view on the tool's new features for the release 2.0, which will be released live at Black Hat Arsenal.

</details>

<details><summary><strong>PEStudio</strong> — Marc Ochsenmeier</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** PEStudio is a unique tool that allows you to perform an initial assessment of a malware without even infecting a lab system or studying its code. Malicious executable often attempts to hide its malicious behavior and to evade detection. In doing so, it generally presents anomalies and suspicious patterns. The goal of PEStudio is to detect these anomalies, provide Indicators and score the Trust for the executable being analyzed. Since the executable file being analyzed is never started, you can inspect any unknown or malicious executable with no risk. PEStudio has been ranked "4th Best 2013 Security Tool" by the readers of ToolsWatch.org.http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/

</details>

<details><summary><strong>reGeorg</strong> — Willem Mouton</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** In 2008, we released reDuh (http://research.sensepost.com/tools/web/reduh), a network-tunneling tool that allowed port forwarding via a web-shell and HTTP/S to backend services. reDuh has since become part of any attackers standard toolkit, featured in several books and notoriously described as "insidious" by HBGary in their leaked e-mails. However, when doing any sort of tunneling, targeting multiple hosts and ports can be frustrating as it requires a tunnel to be setup for each unique host:port combination. Enter reGeorg; this is a rewrite of reDuh to support a full SOCKS4/5 proxy interface. This allows one tunnel to be used to make multiple connections, including port scans. Additionally, capabilities to take advantage of HTML5 websockets (where available) have been built for faster connections. In short, if you can get a webshell up, you can use reGeorg to gain access with your favorite tool (Nmap, Metasploit, etc.) to the entire internal network range your compromised server has access to. The list of currently supported web frameworks are: ASP.NET, JSP, PHP, ASP. The list of currently supported transports are: HTTP, HTTPS, HTML5 WebSockets.

</details>

<details><summary><strong>WhatsApp Privacy Guard</strong> — Jaime Sanchez, Pablo San Emeterio</summary>

**Track:** — · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** With the PRISM scandal, we began to question whether Microsoft, Google, Apple, and Facebook were the only companies working with governments to spy on the behavior of its citizens. Will WhatsApp be one of these companies? Does WhatsApp store its user conversations? These sorts of things make us think that users are defenseless and have no current measures to ensure the privacy of content shared on these platforms. The main objective of the research is to add new layers of security and privacy to ensure that in the exchange of information between members of a conversation both the integrity and confidentiality cannot be affected by an external attacker. This is achieved through a system to anonymize and encrypt conversations and data sent via WhatsApp, so that when they reach the servers they are not in "plain text" and only readable to the rightful owners. WhatsApp Privacy Guard is a tool completely transparent to the users and we will show how this technique can be used against other IM protocols and apps.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>When You Dont Have 0days:  Client-side Exploitation for the Masses with BeEF</strong> — Michele Orrù</summary>

**Track:** Web AppSec · **Event:** Europe 2014  
🔗 **Link:** [https://github.com/beefproject/beef](https://github.com/beefproject/beef)  
📝 **Description:** A bag of fresh and juicy 0days is certainly something you would love to get as a Christmas present, but it would probably be just a dream you had one of those drunken nights. Hold on! Not all is lost! There is still hope for pwning targets without 0days. We will walk you through multiple real-life examples of client-side pwnage, from tricking the victim to take the bait, to achieving persistence on the compromised system. The examples will be highly practical and will demonstrate how you can do proper client-side exploitation effectively, simply by abusing existing functionalities of browsers, extensions, legacy features, etc. We'll delve into Chrome and Firefox extensions (automating various repetitive actions that you'll likely perform in your engagements), HTML applications (HTA), abusing User Interface expectations, (Open) Office macros and more. All the attacks are supposed to work on fully patched target software, with a bit of magic trickery as the secret ingredient. You might already know some of these exploitation vectors, but you might need a way to automate your attacks and tailor them based on the victim language, browser, and whatnot. Either way, if you like offensive security, this is for you.

</details>

<details><summary><strong>ZAP</strong> — Zakaria Rachid</summary>

**Track:** Web AppSec · **Event:** Europe 2014  
🔗 **Link:** [https://github.com/zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)  
📝 **Description:** The Zed Attack Proxy (ZAP) is currently the most active open source web application security tool and competes effectively with commercial tools. While it is an ideal tool for people new to appsec, it also has many features specifically intended for advanced penetration testing. Zack will give a quick introduction to ZAP and then dive into the more advanced features, presenting some useful scripts as well as giving an overview of where its heading.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Bluebox-ng</strong> — Jesús Pérez</summary>

**Track:** Vulnerability Assessment · **Event:** Europe 2014  
🔗 **Link:** [https://github.com/damianfral/bluebox-ng-gsick](https://github.com/damianfral/bluebox-ng-gsick)  
📝 **Description:** Bluebox-ng is a GPL VoIP/UC vulnerability scanner written using Node.js powers. My two cents is to improve security practices in these environments and to make Node.js still more awesome. During this conference, the first stable version (v0.1.0) will be presented with some bugs fixed and these cool features: - Auto VoIP/UC penetration test - Report generation - Performance enhancements

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>NAFT Online</strong> — Didier Stevens</summary>

**Track:** Data Forensics/Incident Response · **Event:** Europe 2014  
🔗 **Link:** [https://blog.didierstevens.com/programs/naft/](https://blog.didierstevens.com/programs/naft/)  
📝 **Description:** Memory forensics is the next step the forensic community has taken. With NAFT Online, you can learn memory forensics for Cisco IOS. Learn how to use the Network Appliance Forensic Toolkit with a real Cisco IOS router.

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Lights Off Hardware Demo</strong> — Javier Vazquez Vidal</summary>

**Track:** Hardware/Embedded · **Event:** Europe 2014  
🔗 **Link:** Not Available  
📝 **Description:** Are you interested in the "Lights Off! The Darkness of the Smart Meters" talk that will be presented at Black Hat Europe? Then you should check this out! Since Arsenal brings the invaluable opportunity of allowing the attendees to get a closer look at researchers work, we want to show you the real stuff. We want you to be able to see, feel and touch the process of reversing we experienced, and show you the tools we used. There will be IDA, Logic Analysers, GDB, Arduino, blown hardware (literally!) and a lot of wires!

</details>

---
