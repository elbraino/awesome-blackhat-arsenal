# USA 2016
---
📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal 2016** event held in **USA**.
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
---
## 🌐 Web/AppSec or Red Teaming
<details><summary><strong>.NET Security Guard</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Philippe Arteau](https://img.shields.io/badge/Philippe%20Arteau-informational)

🔗 **Link:** [.NET Security Guard](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** .NET Security Guard is a code analyzer using the brand new Roslyn API, a framework built to develop analyzers, refactorings tools and build tools. It allows developers to scan their C# and VB.net code for potential vulnerabilities directly from Visual Studio. The analyzers are able to find a wide range of vulnerabilities from injection flaws to cryptographic weaknesses. Example of vulnerable applications will be analyzed in a live demonstration.

</details>

<details><summary><strong>V3SPA: A Tool for Visually Analyzing and Diffing SELinux Security Policies</strong></summary>

![Category: 🌐 Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec%20or%20Red%20Teaming-blue) ![Robert Gove](https://img.shields.io/badge/Robert%20Gove-informational)

🔗 **Link:** [V3SPA: A Tool for Visually Analyzing and Diffing SELinux Security Policies](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** SELinux policies have enormous potential to enforce granular security requirements, but the size and complexity of SELinux security policies makes them challenging for security engineers and analysts to determine whether the implemented policy meets an organization's security requirements. Furthermore, as system complexity increases, so does the difficulty in assessing differential system modifications without requiring a ground up re-verification. Presently, policy analysts and developers primarily use text-based tools such as sediff, grep, and vi to develop and analyze policies. This can be challenging, however, because policies are often composed of tens or hundreds of thousands of rules, which can be difficult to sift through in text-based tools. Some GUI tools exist, such as apol, but these tools do not incorporate visualizations, which can represent dense information compactly and speed up analysis by offloading cognitive processes to the human visual system. In addition, the GUI tools do not support important tasks such as diffing two versions of a policy.To address the challenges in developing and maintaining SELinux security policies, we developed V3SPA (Verification, Validation and Visualization of Security Policy Abstractions). V3SPA creates an abstraction of the underlying security policy using the Lobster domain-specific language, and then tightly integrates exploratory controls and filters with visualizations of the policy to rapidly analyze the policy rules. V3SPA includes several novel analysis modes that change the way policy authors and auditors build and analyze SELinux policies. These modes include:1. A mode for differential policy analysis. This plugin shows analysts a visual diff of two versions of a security policy, allowing analysts to clearly see changes made. Using dynamic query filters, analysts can quickly answer questions such as, "What are the changes that affect passwd_t?"2. A mode for analyzing information flow, identifying unexpected sets of permissions, and examining the overall design of the policy. This plugin allows users to see the entire policy at once, filter down to see only the components of interest, and execute reachability queries both from and to specified domains.As part of our demonstration at Black Hat Arsenal, we will introduce attendees to V3SPA, which we will make freely available online. During our demonstration we will give detailed explanations of V3SPA's algorithms and visualizations, and we will show how V3SPA can be used to assess whether a policy configuration correctly maps to security goals.

</details>

---
## 🌐 Web/AppSec
<details><summary><strong>A Black Path Toward The Sun</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Ben Lincoln](https://img.shields.io/badge/Ben%20Lincoln-informational)

🔗 **Link:** [A Black Path Toward The Sun](https://github.com/nccgroup/ABPTTS)  
📝 **Description:** Web application servers and appliances are often one of the most highly-visible entry points into an organization or high-security network. If the server is misconfigured or hosting vulnerable code, existing tools can frequently be used by attackers to convert it into a gateway to the internal network. However, taking full advantage of such a system typically requires a network-level connection between the attacker and the web application server. For example, an internet-facing Linux web application server may have network-level connectivity to an internal Windows domain controller, but appropriate client tools may not function correctly when used via a web shell or similar interface. An interactive session (SSH, RDP, et cetera) on the vulnerable system, or port-forwarding to allow direct connectivity to internal services from the attacker's system becomes necessary. If the organization responsible for the server has done everything else correctly (including blocking tunneling via ICMP/DNS), then there may be no additional network-level connectivity possible in either direction between the attacker and the web application server. This closes off SSH, RDP, and similar interactive remote access, and prevents the use of port-forwarding agents such as Meterpreter.This presentation provides a solution to this problem - A Black Path Toward The Sun, a tool (released as open source in conjunction with the presentation) which tunnels TCP traffic through the web application server using the server's existing HTTP/HTTPS interface. That is, a JSP/WAR/ASPX file is deployed on the server (just as a web shell would be), and a Python script is executed on the attacker's system which performs TCP port-forwarding through that deployed server-side component. The tool also incorporates novel measures to make the network communication challenging to detect using traditional IDS/IPS/WAF-type systems. Java/JSP and ASP.NET editions of the server-side component will be included in the initial open source release, but porting the component to other web application servers should be straightforward.

</details>

<details><summary><strong>Browser Exploitation Framework (BeEF)</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Christian Frichot](https://img.shields.io/badge/Christian%20Frichot-informational)

🔗 **Link:** [Browser Exploitation Framework (BeEF)](https://github.com/beefproject/beef/wiki/References)  
📝 **Description:** The little browser hacking framework that could; BeEF (Once again voted in the top 5 security tools on ToolsWatch.org) is back again for another hands on JavaScript-filled arsenal session of insanity. If you've seen people talk about BeEF, and haven't gotten around to getting your hands dirty, then now is the perfect time to look under the cover and see how hook.js works. While the framework itself is hanging together with duct tape, Ruby and JavaScript, the capabilities of BeEF have been slowly marching forward year by year, with new features being added almost as quickly as new HTML5 APIs are added to browsers. Two of the larger additions to the framework have been the Autorun Rules Engine (ARE) and the Network Extension, the brain-children of @antisnatchor and @_bcoles. But BeEF isn't just about client-side testing, it's also a great tool if you need to quickly PoC JavaScript-based payloads.This session will cover the following:Hands on with the Autorun Rules Engine (clever scheduling and automation of multiple payloads)Network Extension (just how much local network can a browser see?)Having fun with CSRFSo you think HttpOnly & Secure flags really help?Attendees will hopefully have a better appreciation of how BeEF works, and how custom modules and extensions can be developed to meet any custom requirements you may have.

</details>

<details><summary><strong>BurpBUddy</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Tom Steele](https://img.shields.io/badge/Tom%20Steele-informational)

🔗 **Link:** [BurpBUddy](https://github.com/tomsteele/burpbuddy)  
📝 **Description:** BurpBuddy is a tool originally released in 2014. Arsenal will mark the release of version 3, which will be complete rewrite and will provide SmÃ¶rgÃ¥sbord of new functionality. Including the ability to quickly share your entire Burp state, request/response, issues etc with your team.BurpBuddy is a plugin for BurpSuite Pro that exposed the Extender API over a HTTP and WebSocket Interface. Allowing you to use call endpoints using plain-old JSON as well as develop your own event-driven plugins. By operating in this manner, you can now write your own plugins for Burp in any language you want! Go, Node (aka JavaScript), Erlang, Haskell, whatever is popular on Hacker News this week, or even plain old shell scripts with curl, if it has an HTTP library you're in business. We will discuss the functionality of the API, and have plenty client demonstrations written in various languages. Some practical and some that are just awesome for the sake of being awesome.

</details>

<details><summary><strong>Certbot</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Brad Warren](https://img.shields.io/badge/Brad%20Warren-informational)

🔗 **Link:** [Certbot](https://github.com/bmw)  
📝 **Description:** The majority of the world's Web traffic is still unencrypted and sent using the insecure HTTP. Despite SSL/TLS having existed for decades, it has seen limited adoption on modern webservers. This is largely due to the plethora of obstacles one must over come to enable HTTPS. The process of obtaining a certificate can be expensive and convoluted. Additionally, creating a secure TLS configuration is difficult, especially when it must be constantly updated in response to new attacks against the protocol and implementations of it.To attempt to solve this problem, EFF, Mozilla Cisco, Akamai, IdenTrust, and a team from the University of Michigan have created Let's Encrypt, a free and automated certificate authority. Since the project entered beta in October of last year, the CA has issued millions of certificates making it one of the largest certificate authorities in the world today.Earlier this year, EFF unveiled Certbot, a free and open source tool which can be used to set up HTTPS on a webserver in the matter of seconds. Certbot communicates to the Let's Encrypt CA through a protocol called ACME allowing for automated domain validation and certificate issuance. In this session, I plan to show how easy it is to use Certbot to enable HTTPS with certificates from Let's Encrypt as well as answer any questions you may have about the project.

</details>

<details><summary><strong>HL7deep</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Michael Hudson](https://img.shields.io/badge/Michael%20Hudson-informational)

🔗 **Link:** [HL7deep](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Health Level Seven International (HL7), ANSI-accredited standards developing organization dedicated to providing a comprehensive framework and related standards for the exchange, integration, sharing, and retrieval of electronic health information that supports clinical practice and the management, delivery and evaluation of health services.Target - HL7deep is a tool able to exploit different vulnerabilities in popular medical management platforms used in a host of services, obtaining remote access, assisting surgeries and electronic health records (EHR).

</details>

<details><summary><strong>myBFF</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Kirk Hayes](https://img.shields.io/badge/Kirk%20Hayes-informational)

🔗 **Link:** [myBFF](https://github.com/rapid7/myBFF)  
📝 **Description:** myBFF is a new open source tool which combines fingerprinting and brute forcing against some common web applications, including Citrix, HP, Juniper, and MobileIron, to add intelligence to password guessing. Better yet, this tool is modular, allowing the easy expansion of the tool to include not only other web applications, but also other services. The best part is that the tool will do more than just tell you if a credential pair is valid! You don't want to miss this tool!

</details>

<details><summary><strong>Otaku</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Yoshinori Matsumoto](https://img.shields.io/badge/Yoshinori%20Matsumoto-informational) ![Ryoma Teraoka](https://img.shields.io/badge/Ryoma%20Teraoka-informational)

🔗 **Link:** [Otaku](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** We've developed a tool gathering attack vectors against web application such as XSS, SQLi, CSRF, etc. First, We prepared a web server as a decoy based on a famous CMS, WordPress, and built Mod Secrity to collect all logs regarding to HTTP requests including POST body data. Generally speaking, a decoy web server needs web access to some degree as to attract users and attackers. We deployed a system named OTAKU-BOT which automatically collects and posts random information about Japanese ANIME and MANGA(cartoon) into the decoy web server. Very characteristic point of this system is that we can find whether Japanese ANIME is likely to be targeted or not by attackers. (or No correlation between them).Furthermore, We developed another web application "WP Portal", which visualizes these attacks in a real-time. This application enable us to monitor attack trend. WP Portal also has a vulnerability scanner for WordPress. You can start the scanner and view vulnerability reports on WP Portal.Dictionary Files for the scanner is created from honeypots and are updating daily. We will demonstrate this bot and the visualization tool. Participants can got attack vectors via WP Portal! Furthermore, our demo will show honeypots, a website, and analysis of attacks against WordPress.

</details>

<details><summary><strong>Rainmap lite</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Paulino Calderon](https://img.shields.io/badge/Paulino%20Calderon-informational)

🔗 **Link:** [Rainmap lite](https://github.com/cldrn)  
📝 **Description:** Responsive web application that allows users to launch Nmap scans from their mobiles/tablets/web browsers! Unlike it's predecessor [1], Rainmap-lite does not require special services (RabbitMQ, PostgreSQL, Celery, supervisor, etc) to make it easy to install on any server. You simply need to install the Django application and add the cron polling task to set up a new scanning server. Nmap scans on the road for everyone!Features:Easily launch Nmap scans with a few clicks.Responsive interface runs smoothly from your phone/tablet.Reports delivered by email in all formats.View reports from your web browser.Schedule scans.Dozens of scanning profiles to choose from.Easy to install/set up. Share results with your team.[1] Rainmap - https://nmap.org/rainmap/Demo: https://youtu.be/3oNegHPBd3oGithub:https://github.com/cldrn/rainmap-lite"

</details>

<details><summary><strong>SkyPhenomena</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Wen Tao Tang](https://img.shields.io/badge/Wen%20Tao%20Tang-informational) ![Zhang Lu](https://img.shields.io/badge/Zhang%20Lu-informational) ![Li Fu](https://img.shields.io/badge/Li%20Fu-informational) ![RenXu Ye](https://img.shields.io/badge/RenXu%20Ye-informational)

🔗 **Link:** [SkyPhenomena](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** SkyPhenomen aims to monitor the web threat and weakness in web respect of a company by simulating the hacker's penetrating ideas,it mainly includes the following features:First Stage -- asset gathering:1. Domain gathering. Including DNS zone transfer, brother domains, sub-domian bruteforcing, web crawler gathering, search engine, github, etcâ¦2. Port scanning and middleware fingerprint recognition3. Site carwl and web application fingerprint recognitionSecond Stage -- information associating:1. IP addresses locating and confirming C class network segment which belonging to the target.2. Generating customized user&password dicts base on public information gathered in the previous stage and other leak databases.3. The third party threat information base on relavent keyword matching and target site employee's relation at GitHub or other source platform.Last stage -- vulnerability discovery:1. Scanning common vulnerability in web service and interfaces(SQLi,XSS,RCE,etcâ¦).2. Scanning universal vulnerability in collected fingerprints.3. Automatic bruteforcing of middlewares,web applications that need authentication and form of background login page,base on the customized dicts.4. Scanning sensitive files and folders in web service with high accuracy and compatibility.

</details>

<details><summary><strong>The Pappy Proxy</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Rob Glew](https://img.shields.io/badge/Rob%20Glew-informational)

🔗 **Link:** [The Pappy Proxy](https://github.com/roglew/guppy-proxy)  
📝 **Description:** The Pappy Proxy is an open source intercepting proxy that takes a slightly different approach to testing websites than existing proxies such as Burp Suite and ZAP due to its console-based interface. The console interface and powerful history search make it extremely easy to find interesting requests in history and to discover promising areas for further testing. Along with standard features such as an interceptor and a repeater, Pappy allows users to generate most of the boilerplate needed for a Python attack script for more complex attacks. Pappy also has numerous other features such as response streaming, automatically modifying requests and responses on the fly, and support for upstream proxies.

</details>

<details><summary><strong>WATOBO - The Web Application TOol BOx</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Andreas Schmidt](https://img.shields.io/badge/Andreas%20Schmidt-informational)

🔗 **Link:** [WATOBO - The Web Application TOol BOx](https://github.com/siberas/watobo/blob/master/watobo.gemspec)  
📝 **Description:** WATOBO is a security tool for testing web applications. It is intended to enable security professionals to perform efficient (semi-automated) web application security audits. Most important features are:WATOBO has Session Management capabilities! You can define login scripts as well as logout signatures. So you don't have to login manually each time you get logged out.WATOB can act as a transparent proxy (requires nfqueue)WATOBO can perform vulnerability checks out of the boxWATOBO can perform checks on functions which are protected by Anti-CSRF-/One-Time-TokensWATOBO supports Inline De-/Encoding, so you don't have to copy strings to a transcoder and back again. Just do it inside the request/response window with a simple mouse click.WATOBO has smart filter functions, so you can find and navigate to the most interesting parts of the application easily.WATOBO is written in (FX)Ruby and enables you to easily define your own checksWATOBO runs on Windows, Linux, MacOS ... every OS supporting (FX)RubyWATOBO is free software ( licensed under the GNU General Public License Version 2WATOBO is written in (FX)Ruby and was initially released in May 2010 as an open source project on SourceForge (https://watobo.sourceforge.net).

</details>

<details><summary><strong>Web Service Security Assessment Tool (WSSAT)</strong></summary>

![Category: 🌐 Web/AppSec](https://img.shields.io/badge/Category:%20🌐%20Web/AppSec-blue) ![Mehmet Yalcin YOLALAN](https://img.shields.io/badge/Mehmet%20Yalcin%20YOLALAN-informational) ![Salih TALAY](https://img.shields.io/badge/Salih%20TALAY-informational)

🔗 **Link:** [Web Service Security Assessment Tool (WSSAT)](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/webapp_security/wssat.md)  
📝 **Description:** WSSAT is an open source web service security scanning tool which provides a dynamic environment to add, update or delete vulnerabilities by just editing its configuration files. This tool accepts WSDL address list as input file and performs both static and dynamic tests against the security vulnerabilities. It also makes information disclosure controls.Objectives of WSSAT are to allow organizations:Perform their web services security analysis at onceSee overall security assessment with reportsHarden their web servicesWSSAT's main capabilities include:Dynamic Testing:Insecure Communication - SSL Not UsedUnauthenticated Service MethodError Based SQL InjectionCross Site ScriptingXML BombExternal Entity Attack - XXEXPATH Injection Verbose SOAP Fault MessageStatic Analysis:Weak XML Schema: Unbounded OccurrencesWeak XML Schema: Undefined NamespaceWeak WS-SecurityPolicy: Insecure TransportWeak WS-SecurityPolicy: Insufficient Supporting Token ProtectionWeak WS-SecurityPolicy: Tokens Not ProtectedInformation Leakage:Server or development platform oriented information disclosureWSSAT's main modules are:ParserVulnerabilities LoaderAnalyzer/AttackerLoggerReport GeneratorThe main difference of WSSAT is to create a dynamic vulnerability management environment instead of embedding the vulnerabilities into the code. More information can be found here: https://github.com/YalcinYolalan/WSSAT.

</details>

---
## 🔵 Blue Team & Detection
<details><summary><strong>Accelerating Cyber Hunting Project ASGARD</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joshua Patterson](https://img.shields.io/badge/Joshua%20Patterson-informational) ![Michael Wendt](https://img.shields.io/badge/Michael%20Wendt-informational)

🔗 **Link:** [Accelerating Cyber Hunting Project ASGARD](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Rethinking the cyber security problem as a data-centric problem led Accenture Labs Cyber Security team to use best of breed open source big-data tools and emerging technologies to accelerate detection, response, and hunting. Project ASGARD, utilizing new approaches such as graph databases and analysis, GPUs, and Spark, exploits the connected nature of cyber security data to give cyber analyst more efficient and effective tools to combat evolving cyber threats. ASGARD allows organization to store more data than ever, while still gaining 2-3 orders of magnitude more speed and performance than traditional SIEMS. In this talk you can watch us analyze data real-time, learn more about our cluster and architecture, and see how we've integrated leading big data technologies to outperform expensive appliances with a fraction of the cost. In addition, we will demonstrate how advanced data science can be used to identify threats and accelerate cyber analysis, instead of just adding more noise.

</details>

<details><summary><strong>Aktaion</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joseph Zadeh](https://img.shields.io/badge/Joseph%20Zadeh-informational) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational)

🔗 **Link:** [Aktaion](https://github.com/srihari-humbarwadi/ransomware-detection-with-deep-learning/blob/master/README.md)  
📝 **Description:** Crypto Ransomware has become a popular attack vector used by malicious actors to quickly turn infections into profits. From a defensive perspective, the detection of new ransomware variants relies heavily on signatures, point solution posture and binary level indicators of compromise (IOC). This approach is inefficient at protecting targets against the rapid changes in tactics and delivery mechanisms typical of modern ransomware campaigns. We propose a novel approach for blending multiple signals (called micro behaviors) to detect ransomware with more flexibility than using IOC matching alone.The goal of the approach is to provide expressive mechanisms for detection via contextual indicators and micro behaviors that correlate to attacker tactics, even if they evolve with time. The presenters will provide open source code that will allow users and fellow researchers to replicate the use of these techniques. We will conclude with a focus on how to tie this approach to active defense measures and existing infrastructure.This tool will be applied to PCAPS and will then mine and display relationships of Micro Behaviors particular to ransomware traffic. Built with Spark notebook https://github.com/andypetrella/spark-notebook we are leveraging Apache Spark (https://spark.apache.org/) for scalable data processing and MlLib for an anlalytics API (https://spark.apache.org/mllib/). The notebook will provide an interface for the ingestion of heterogenous data and the ability to build a combination of behavior based risk indictors combined with classic signatures. Prototype examples of different risk profiles will be demonstrated with the API via spark notebook but the libraries themselves should be usable in any Java backed code base.

</details>

<details><summary><strong>AMIRA: Automated Malware Incident Response and Analysis</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Jakub Sendor](https://img.shields.io/badge/Jakub%20Sendor-informational)

🔗 **Link:** [AMIRA: Automated Malware Incident Response and Analysis](https://github.com/jjsendor)  
📝 **Description:** Even for a larger incident response team handling all of the repetitive tasks related to malware infections is a tedious task. Our malware analysts have spent a lot of time chasing digital forensics from potentially infected Mac OS X systems, leveraging open source tools, like OSXCollector. Early on, we have automated some part of the analysis process, augmenting the initial set of digital forensics collected from the machines with the information gathered from the threat intelligence APIs. They helped us with additional information on potentially suspicious domains, URLs and file hashes. But our approach to the analysis still required a certain degree of configuration and manual maintenance that was consuming lots of attention from malware responders.Enter automation: turning all of your repetitive tasks in a scripted way that will help you deal faster with the incident discovery, forensic collection and analysis, with fewer possibilities to make a mistake. We went ahead and turned OSXCollector toolkit into AMIRA: Automated Malware Incident Response and Analysis service. AMIRA turns the forensic information gathered by OSXCollector into actionable response plan, suggesting the infection source as well as suspicious files and domains requiring a closer look. Furthermore, we integrated AMIRA with our incident response platform, making sure that as little interaction as necessary is required from the analyst to follow the investigation. Thanks to that, the incident response team members can focus on what they excel at: finding unusual patterns and the novel ways that malware was trying to sneak into the corporate infrastructure.

</details>

<details><summary><strong>Arsenal Theater Demo: Aktaion</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joseph Zadeh](https://img.shields.io/badge/Joseph%20Zadeh-informational) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational)

🔗 **Link:** [Arsenal Theater Demo: Aktaion](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Crypto Ransomware has become a popular attack vector used by malicious actors to quickly turn infections into profits. From a defensive perspective, the detection of new ransomware variants relies heavily on signatures, point solution posture and binary level indicators of compromise (IOC). This approach is inefficient at protecting targets against the rapid changes in tactics and delivery mechanisms typical of modern ransomware campaigns. We propose a novel approach for blending multiple signals (called micro behaviors) to detect ransomware with more flexibility than using IOC matching alone.The goal of the approach is to provide expressive mechanisms for detection via contextual indicators and micro behaviors that correlate to attacker tactics, even if they evolve with time. The presenters will provide open source code that will allow users and fellow researchers to replicate the use of these techniques. We will conclude with a focus on how to tie this approach to active defense measures and existing infrastructure.This tool will be applied to PCAPS and will then mine and display relationships of Micro Behaviors particular to ransomware traffic. Built with Spark notebook https://github.com/andypetrella/spark-notebook we are leveraging Apache Spark (https://spark.apache.org/) for scalable data processing and MlLib for an anlalytics API (https://spark.apache.org/mllib/). The notebook will provide an interface for the ingestion of heterogenous data and the ability to build a combination of behavior based risk indictors combined with classic signatures. Prototype examples of different risk profiles will be demonstrated with the API via spark notebook but the libraries themselves should be usable in any Java backed code base.

</details>

<details><summary><strong>Arsenal Theater Demo: SIEMonster</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Chris Rock](https://img.shields.io/badge/Chris%20Rock-informational)

🔗 **Link:** [Arsenal Theater Demo: SIEMonster](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** SIEMonster is a turnkey, open source, enterprise grade, multi node clustered Security Incident and Event Management (SIEM), built on scalable, zero cost components. SIEMonster can be used to immediately identify threats in your organization and used for correlation alert matches over selected periods of time.SIEMonster is the compilation of the best open source framework presentations from Black Hat and DEFCON and developed into a SIEM for all organizations as a viable 'like for like' alternative to commercial SIEM solutions. The product can be rolled out in 15 minutes to an existing organization both locally in the customers Data Center via VM image or Amazon AWS AMI images. SIEMonster comes with supporting build and maintenance documentation that most open source solutions lack.SIEMonster has the following benefits:Fully open source, scalable SIEM in 2,4,8,16 nodes and beyond configurationsNo license restrictions, on node or data limitationsOpen community for additional featuresAlready running in corporate companiesCompletely freeOn-premise hosted security analytics and SIEM open SOC or cloud hostedInstant incident alerting via Dashboard, email, SMS or console view via a secure portal, and integration with Slack/HipChat using Graylog streams.Provides continuous cyber security monitoring to identify, mitigate and respond to internal and external risks in real time using AlertaFull ISMS suite of documentation, including detailed designs, build guides, maintenance instructions, tutorial videos and standard operating procedures, etc.Full integration with OSSEC Wazuh fork for host intrusion detection and PCI DSS ruleset incorporated into ElasticThreat intelligence using open-source OSINT Critical stack and intelligence feeds with no subscription charges.Incorporate your existing vulnerability scans into the dashboard (OpenVas, McAfee, Nessus)Fully automated Open-source incident response ticketing system for incident recording, raising tickets to other operators show the next shift security analysts current issues.

</details>

<details><summary><strong>Arsenal Theater Demo: Subgraph OS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![David Mirza Ahmad](https://img.shields.io/badge/David%20Mirza%20Ahmad-informational)

🔗 **Link:** [Arsenal Theater Demo: Subgraph OS](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Subgraph OS is a desktop operating system with built-in privacy and security features that make it resistant to attacks against the endpoint, especially those that involve exploitation of software vulnerabilities. The kernel is hardened with grsecurity + PaX, and key applications run in sandbox environments implemented using Linux containers, seccomp bpf, and desktop isolation. Subgraph OS also includes an application firewall and integration with Tor.

</details>

<details><summary><strong>Cuckoodroid 2.0</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Idan Revivo](https://img.shields.io/badge/Idan%20Revivo-informational)

🔗 **Link:** [Cuckoodroid 2.0](https://github.com/idanr1986/cuckoodroid-2.0)  
📝 **Description:** To combat the growing problem of Android malware, we present a new solution based on the popular open source framework Cuckoo Sandbox to automate the malware investigation process. Our extension enables the use of Cuckoo's features to analyze Android malware and provides new functionality for dynamic and static analysis. Our framework is an all in one solution for malware analysis on Android. It is extensible and modular, allowing the use of new, as well as existing, tools for custom analysis.The main capabilities of our CuckooDroid include:Dynamic Analysis - based on Dalvik API hookingStatic Analysis - Integration with AndroguardEmulator Detection PreventionVirtualization Managers that support the popular virtualization solutions (VMware,Virtualbox, Esxi, Xen, and Kvm) and now also android emulator.Traffic AnalysisIntelligence Gathering - Collecting information from Virustotal, Google Play etc.Behavioral Signatures in cuckoodroid 2.0New capabilities that will be presented in Black Hat for the first time:Integration with cuckoo 2.0New user interfaceAndroid x86 supportAutomatic unpackingintegration with MaltegoNew Behavioral SignaturesDropped filesMalware Configuration ExtractionsExamples of well-known malware will be used to demonstrate the framework capabilities and its usefulness in malware analysis.

</details>

<details><summary><strong>DET</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Saif El-Sherei](https://img.shields.io/badge/Saif%20El-Sherei-informational)

🔗 **Link:** [DET](https://github.com/sensepost/DET)  
📝 **Description:** DET aims to provide a framework to assist with exfiltrating data using either one or several channels. Social media has become extremely popular in recent attacks such as HammerToss, campaign uncovered by FireEye in July 2015. Several tools are also publicly available allowing you to remotely access computers through "legitimate" services such as Gmail (GCat) or Twitter (Twittor). Often gaining access to a network is just the first step for a targeted attacker. Once inside, the goal is to go after sensitive information and exfiltrate it to servers under their control. To prevent this from occuring, a whole industry has popped up with the aim of stopping exfiltration attacks. However, often these are expensive and rarely work as expected. With this in mind, I created the Data Exfiltration Toolkit (DET) to help both penetration testers testing deployed security devices and those admins who've installed and configured them, to ensure they are working as expected and detecting when sensitive data is leaving the network.

</details>

<details><summary><strong>Elastic Handler</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![David Cowen](https://img.shields.io/badge/David%20Cowen-informational)

🔗 **Link:** [Elastic Handler](https://github.com/devgc/ElasticHandler/blob/master/scripts/ExternalDeviceExample.py)  
📝 **Description:** Elastic Handler is a DFIR specific replacement for the LogstashElastic Handler allows you to take all the tools you currently run and make their output better by doing the following:It allows you to define a mapping from the CSV/TSV/Etc output you are getting now into JSON so that ES can ingest itIt allows you to normalize all of the data you are feeding in so that your column names are suddenly the same allowing cross reporting searching and correlation.It lets you harness the extreme speed of Elastic Search to do the heavy listing in your correlationIt lets you take a unified view of your data/report to automate that analysis and create spreadsheets/etc. that you would have spent a day on previouslyThe idea here is to let computers do what can be automated so you can spend more time using what makes humans special. What I mean by that is your analyst brains and experience to spot patterns, trends and meaning from the output of the reports. In the GitHub repository there are several mappings provided for the tools, we call out most like; Tzworks tools, Shellbag explorer, our link parser, Mandiant's Shimcache parser, etc. But the cool thing about this framework is that to bring in another report, all you have to do is generate two text files to define your mapping, there is no code involved.

</details>

<details><summary><strong>eXpose</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Joshua Saxe](https://img.shields.io/badge/Joshua%20Saxe-informational)

🔗 **Link:** [eXpose](https://github.com/joshsaxe/eXposeDeepNeuralNetwork)  
📝 **Description:** From hiding their tools in innocuous-looking file paths to creating registry keys that hide malicious commands to inviting users to visit deceptive URLs, attackers frequently use deception to penetrate and hide on our networks. Currently our community uses URL blacklists and rule-based detection mechanisms to detect such deception. The eXpose deep neural network, which we will be releasing as free software simultaneously with Blackhat USA 2016, goes beyond these simple methods to provide artificial intelligence driven detection of these objects, detecting upwards of 90% of previously unseen malicious URLs, malicious file paths, and malicious registry keys at low false positive rates.eXpose's approach is based on recent advances in deep learning research, and uses neural network primitives such as character-level embeddings, heterogenously-sized convolutional filters, dropout, and batch normalization to achieve a high detection rate. We compared eXpose to conventional machine learning methods and found that eXpose achieves a significant boost in detection accuracy. In our presentation we will explain how eXpose works, demonstrate how to use it both from the command line and as a Python module, demonstrate its ability to detect new malicious URLs, file paths, and registry keys, and challenge our audience to beat eXpose at guessing which previously-unseen objects are malicious or not.

</details>

<details><summary><strong>FLOSS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Moritz Raabe](https://img.shields.io/badge/Moritz%20Raabe-informational)

🔗 **Link:** [FLOSS](https://github.com/mandiant/flare-floss/blob/master/pyproject.toml)  
📝 **Description:** The FireEye Labs Obfuscated String Solver (FLOSS) is an open source tool that automatically detects, extracts, and decodes obfuscated strings in Windows Portable Executable (PE) files. Malware analysts, forensic investigators, and incident responders can use FLOSS to quickly extract sensitive strings to identify indicators of compromise (IOCs). Malware authors encode strings in their programs to hide malicious capabilities and impede reverse engineering. Even simple encoding schemes defeat the 'strings' tool and complicate static and dynamic analysis. FLOSS uses advanced static analysis techniques, such as emulation, to deobfuscate encoded strings.FLOSS is extremely easy to use and works against a large corpus of malware. It follows a similar invocation as the 'strings' tool. Users that understand how to interpret the strings found in a binary will understand FLOSS's output. FLOSS extracts higher value strings, as strings that are obfuscated typically contain the most sensitive configuration resources â including C2 server addresses, names of dynamically resolved imports, suspicious file paths, and other IOCs. I will describe the computer science that powers the tool, and why it works. I will also show how to use FLOSS and demonstrate the decoding of strings from a wide variety of malware families.

</details>

<details><summary><strong>gopassivedns</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Philip Martin](https://img.shields.io/badge/Philip%20Martin-informational)

🔗 **Link:** [gopassivedns](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Passive DNS is an awesome data source. A growing number of companies out there will sell you access to huge repos of historical lookups across the internet. That data can be hugely helpful in detecting or responding to a security incident...but what about the DNS lookups that happen in your own backyard? gopassivedns is a network-capture based DNS logger, written in Go, designed to be run anywhere and everywhere you expect to see DNS lookups. It uses gopacket to deal with libpcap and packet processing. It outputs JSON logs to a number of log sinks (files, kafka, flumed, etc) and stats via statsd. Come, learn and never miss another DNS lookup again.

</details>

<details><summary><strong>HoneyPy & HoneyDB</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Phillip Maddux](https://img.shields.io/badge/Phillip%20Maddux-informational)

🔗 **Link:** [HoneyPy & HoneyDB](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** HoneyPy is a low interaction honeypot with the capability to be more of a medium interaction honeypot. HoneyPy is written in Python and is intended to be easy to: deploy, extend functionality with plugins, and apply custom configurations. The level of interaction is determined by the functionality of its plugins. Plugins can be created to emulate UDP or TCP based services. All activity is logged to a file by default, but posting honeypot activity to Twitter, a Slack channel, or a web service endpoint can be configured as well. HoneyPy is ideal as a production honeypot on an internal network or as a research honeypot on the Internet.HoneyDB is a web site dedicated to publishing honeypot data from HoneyPy sensors on the Internet. It also offers honeypot data for download via a REST API. Web site users can also log into HoneyDB and maintain a ThreatBin, which is custom list of honeypot session data bookmarked by the user. Future features include consolidated threat information from other honeypot Twitter accounts, and expanding the API.

</details>

<details><summary><strong>Kung Fu Malware</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Pablo San Emeterio](https://img.shields.io/badge/Pablo%20San%20Emeterio-informational) ![RomÃ¡n RamÃ­rez](https://img.shields.io/badge/RomÃ¡n%20RamÃ­rez-informational)

🔗 **Link:** Not Available  
📝 **Description:** Focusing on Windows operating systems, we've developed an agent to try to activate some techniques that malware usually include to avoid being detected by a sandbox or malware analyst, emulating malware analysis computer inside a common PC. This agent would add a new layer of protection without interacting with the malware, because current malware will not run their malicious payload in a sandbox or while being debbuged. As we know the different malware families implement anti-reversing, anti-debuging and anti-virtualization characteristics along with other techniques such as to detect well known process and windows. Malware writers implement these techniques to prevent the execution of malicious code within a laboratory that could help researchers in their analysis and eradication.Some of those are:Detecting when a program is being debugged.Detecting when a program is running in a virtual machine, by reading some registry keys or locating some files or processes used by the virtualization technology.The detection programs used by malware analysts such as wireshark, IDA or process explorer.The proliferation of those techniques and strategies has brought us to a new solution; pretend the behavior of a malware analysis device and / or sandbox, by using some of the techniques explained above, in order to prevent the execution of the malicious code.

</details>

<details><summary><strong>LAMMA</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ajit Hatti](https://img.shields.io/badge/Ajit%20Hatti-informational)

🔗 **Link:** [LAMMA](https://github.com/smxlabs/LAMMA-beta)  
📝 **Description:** LAMMA (beta) is a Framework for Vulnerability Assessment & auditing of cryptography, PKI and related implementations. Developed in Python, LAMMA is a command line utility, built with the focus of automating the Crypto-Assessment for large infrastructures. The framework is highly extendable and allows usres to write and integrate their own plugins seamlessly.LAMMA (beta) supports 4 modules which have many plugins for very specific purpose.1. REMOTE - Module scans remote Hosts for SSL/TLS configuration, and reports any gap, vulnerabilities discovered with unique features like Time-Line-analysis of server Certificate, Deep mining of certificates and TLS/SSL session parameters.2. CRYPTO - This Module checks the various crypto primitives generated by any underlying framework for Quality, backdoor & sanity. Few of Primary Checks :Quality Test for Random Number GeneratedSanity Checks for shared Prime numbers in multiple RSA keysSafe and Strong Prime testShared modulus test & MalSha, Malformed Digest Test3. TRUST - Module checks various trust and key stores for - insecure Private keys and un-trusted certificates. Here are few novel feature of LAMA framework.Extract Prime number and Modulus from Private keys for sanity and strength checkTrack Private Keys across the network for insecure storage & Track multiple instancesFind and list List pinned & un-trusted certificates & Public Key, and track their presence4. SOURCE - Module helps to enforce "Cryptography Review Board" recommendations of your organisation. This module scans source code for use of insecure and weak schemes likeMD*/SHA/SHA1 hashesECB/CBC block cipher moderand() or /dev/rand functions or back-doored schemes in use like Dual_EC_DRBG, p224r1, secp384r1

</details>

<details><summary><strong>LOG-MD</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Michael Gough](https://img.shields.io/badge/Michael%20Gough-informational) ![Brian Boettcher](https://img.shields.io/badge/Brian%20Boettcher-informational)

🔗 **Link:** [LOG-MD](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** LOG-MD is designed for Windows based systems to audit log and advanced audit policy settings and guide users to enable and configure the audit settings based on industry audit standards like CIS, USGCB, AU ACSC and the 'Windows Logging Cheat Sheets' to help push and encourage moving security and detection of audit logging forward. LOG-MD was also designed to gather the artifacts from malicious activity, referred to as "Malicious Discovery", more easily than the standard methods many professionals use today. LOG-MD is designed to speed up the investigation of a suspect system, or help validate it is good, and to speed up evaluating malware in a lab environment.Malicious Discovery is a challenge for many and the Mean Time to Detection (MTTD) from a compromise or worse yet, a breach is still close to a year for most companies. LOG-MD is designed to help small, medium, large, and enterprise businesses improve their Malicious Discovery with a tool that can be run manually or distributed across the environment.LOG-MD replaces or augments several security and forensic tools that have not been updated in years, combing many features professionals rely on, into one easy to use tool. LOG-MD audits the system at each run for audit log related settings, and harvests security related log events. LOG-MD performs hashes of the full filesystem and compares it to a baseline or Master-Digest of trusted files to reduce files that need to be investigated. LOG-MD performs a full baseline of the registry and compares it to a trusted baseline, and searches for special artifacts like the null byte character used in registry keys to hide malware artifacts and large registry keys where malware hides. LOG-MD also harvests PowerShell activity and can harvest optional Sysmon and Windows Logging Service (WLS) events as well for more detailed analysis of system activity. LOG-MD utilizes whitelists to filter down the results of known good and trusted results to make Malicious Discovery easier and faster. In addition LOG-MD can take the artifact details of IP addresses and perform a WhoIs lookup to gain ownership and country information and run files and IP's through VirusTotal for artifact evaluation. Additionally, special artifacts hunting and reporting are being added to LOG-MD as malware authors create them, what we refer to as Malware Management, which is what LOG-MD is based on.

</details>

<details><summary><strong>Maltese (Malware Traffic Emulating Software)</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Sasi Siddharth](https://img.shields.io/badge/Sasi%20Siddharth-informational)

🔗 **Link:** [Maltese (Malware Traffic Emulating Software)](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** In most cases, malware communicates with a Command and Control (C&C) server in order to download updates or additional modules, receive commands, exfiltrate data, etc. The DNS system plays an important role in C&C communication: In order to hide their C&C servers from detection, common modern malware families employ Domain-Generation Algorithms (DGA) rather than hard-coded addresses to find their C&C servers. Furthermore, some malware families provide a back-channel and exfiltrate data in specially crafted DNS requests, thereby abusing the fact that DNS traffic is often not firewalled.Due to the importance of the DNS in malware's C&C communication, recent malware detection systems try to detect malware based on anomalies in DNS request patterns. As one would expect, the suppliers of such detection systems claim that their solutions work as a catch-all for any malware that abuses the DNS system as part of its operation. But, prior to deploying any malware detector, one needs to test these claims by evaluating the effectiveness of the detector. Also, when a new malware variant is detected in the wild, it is important for security teams to verify that their deployed solutions can detect them.One way of accomplishing the above tasks is to execute real malware samples and observe the results of the detector. However, this is infeasible in a production network, as there is always a risk of the malware causing damage. Furthermore, malware samples often do not execute on demand, and therefore testing may be difficult. In our contribution, we describe a tool and a framework for evaluating the effectiveness of DNS-based malware detectors using emulation. We propose the following approach: We emulate the DNS traffic patterns of a given malware family, inject it into a network, and observe whether the malware detector reports an infection. The injected traffic is completely benign and, therefore, testing poses no risk to the network. The generation of DNS traffic patterns is based on information published by various members of the security community. From malware analysis, typically, one or more of the following artifacts may be found for a given malware â a list of domains generated, a network packet capture (PCAP) of the malicious traffic, or a Domain Generation Algorithm (DGA) that is published by another researcher.Our tool enables security professionals to utilize any of these three artifacts in an easy, quick, and configurable manner for generating DNS traffic patterns. The tool is implemented in Python and will be made available free of charge, and we are also exploring an open source license. Our presentation will demo an evaluation infrastructure, and discuss use cases in order to help the audience gain more confidence in their security deployments. The tool is built using a plugin-based architecture, and we will also discuss ways in which the audience may contribute new plugins to the tool.

</details>

<details><summary><strong>OBJECTIVE-SEE'S OS X SECURITY TOOLS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [OBJECTIVE-SEE'S OS X SECURITY TOOLS](https://github.com/objective-see/FileMonitor)  
📝 **Description:** Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of OS X malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer he's written various OS X security tools that he now shares online (always free!), via his personal website objective-see.com. So come watch as RansomWhere? generically detects OS X ransomware, KnockKnock flags persistent OS X malware, BlockBlock provides runtime protection of persistence locations, and much more. Our Macs will remain secure!

</details>

<details><summary><strong>rastrea2r</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ismael Valenzuela](https://img.shields.io/badge/Ismael%20Valenzuela-informational)

🔗 **Link:** [rastrea2r](https://github.com/aboutsecurity)  
📝 **Description:** Ever wanted to turn your AV console into an Incident Response & Threat Hunting machine? Rastrea2r (pronounced "rastreador" - hunter- in Spanish) is a multi-platform open source tool that allows incident responders and SOC analysts to triage suspect systems and hunt for Indicators of Compromise (IOCs) across thousands of endpoints in minutes. To parse and collect artifacts of interest from remote systems (including memory dumps), rastrea2r can execute sysinternal, system commands and other 3rd party tools across multiples endpoints, saving the output to a centralized share for automated or manual analysis. By using a client/server RESTful API, rastrea2r can also hunt for IOCs on disk and memory across multiple systems using YARA rules. As a command line tool, rastrea2r can be easily integrated within McAfee ePO, as well as other AV consoles and orchestration tools, allowing incident responders and SOC analysts to collect forensics evidence and hunt for IOCs without the need for an additional agent, with 'gusto' and style!The latest version of Rastrea2r can be found at: https://github.com/aboutsecurity/rastrea2r

</details>

<details><summary><strong>SIEMonster</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Chris Rock](https://img.shields.io/badge/Chris%20Rock-informational)

🔗 **Link:** [SIEMonster](https://github.com/siemonster/docs/blob/master/source/overview.rst)  
📝 **Description:** SIEMonster is a turnkey, open source, enterprise grade, multi node clustered Security Incident and Event Management (SIEM), built on scalable, zero cost components. SIEMonster can be used to immediately identify threats in your organization and used for correlation alert matches over selected periods of time.SIEMonster is the compilation of the best open source framework presentations from Black Hat and DEFCON and developed into a SIEM for all organizations as a viable 'like for like' alternative to commercial SIEM solutions. The product can be rolled out in 15 minutes to an existing organization both locally in the customers Data Center via VM image or Amazon AWS AMI images. SIEMonster comes with supporting build and maintenance documentation that most open source solutions lack.SIEMonster has the following benefits:Fully open source, scalable SIEM in 2,4,8,16 nodes and beyond configurationsNo license restrictions, on node or data limitationsOpen community for additional featuresAlready running in corporate companiesCompletely freeOn-premise hosted security analytics and SIEM open SOC or cloud hostedInstant incident alerting via Dashboard, email, SMS or console view via a secure portal, and integration with Slack/HipChat using Graylog streams.Provides continuous cyber security monitoring to identify, mitigate and respond to internal and external risks in real time using AlertaFull ISMS suite of documentation, including detailed designs, build guides, maintenance instructions, tutorial videos and standard operating procedures, etc.Full integration with OSSEC Wazuh fork for host intrusion detection and PCI DSS ruleset incorporated into ElasticThreat intelligence using open-source OSINT Critical stack and intelligence feeds with no subscription charges.Incorporate your existing vulnerability scans into the dashboard (OpenVas, McAfee, Nessus)Fully automated Open-source incident response ticketing system for incident recording, raising tickets to other operators show the next shift security analysts current issues.

</details>

<details><summary><strong>Subgraph OS</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![David Mirza Ahmad](https://img.shields.io/badge/David%20Mirza%20Ahmad-informational)

🔗 **Link:** [Subgraph OS](https://github.com/dma)  
📝 **Description:** Subgraph OS is a desktop operating system with built-in privacy and security features that make it resistant to attacks against the endpoint, especially those that involve exploitation of software vulnerabilities. The kernel is hardened with grsecurity + PaX, and key applications run in sandbox environments implemented using Linux containers, seccomp bpf, and desktop isolation. Subgraph OS also includes an application firewall and integration with Tor.

</details>

<details><summary><strong>Threat Scanner</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Brian Codde](https://img.shields.io/badge/Brian%20Codde-informational)

🔗 **Link:** [Threat Scanner](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Threatscanner is an endpoint IOC scanner. It consumes OpenIOC and Yara rules and scans Windows machines, matching the rules. It produces a report for any matches detailing all the information about the matched items. In addition, it details the logic path used to arrive at the match - showing which predicates in the rule matched and which were missed. The system has many performance optimizations; such as aggregating rules so each potential item is only evaluated once regardless of the number of rules tested. This means that the running time for a single rule roughly matches the running time for 1000s of rules.

</details>

<details><summary><strong>Visual Network and File Forensics Using Rudra</strong></summary>

![Category: 🔵 Blue Team & Detection](https://img.shields.io/badge/Category:%20🔵%20Blue%20Team%20&%20Detection-cyan) ![Ankur Tyagi](https://img.shields.io/badge/Ankur%20Tyagi-informational)

🔗 **Link:** [Visual Network and File Forensics Using Rudra](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** A typical approach towards investigating intrusion incidents is to collect files that might have been dropped from a compromised server. These files could be extracted from network traffic or if we are lucky they could be obtained from the compromised system itself. An analyst can then use her expertise to re-create the attack scenario and understand possible vectors. Depending on her skills, this process might prove easy or extremely difficult. Our aim is to provide a framework that provides a common ground for forensic analysis of network traffic and dropped files using intuitive visualization of structural properties of network traffic and data files, combined with the proven methods of behavioral heuristics.This talk aims to help users understand how to visually classify streaming data such as a network traffic buffer for an active TCP connection or chunked data read from a file on disk. Both these objects under analysis could be considered a binary blobs which could be rendered as an image highlighting the binary structure embedded within them. When this approach is combined with statistical file-format independent properties (like the theoretical minsize, compression ratio, entropy, etc.) and certain file-format specific properties (like the Yara rules matching on parsed HTTP payload or heuristics rules matching on the sections of a PE file), it provides a completely new perspective into the analysis process.Additionally, we want to emphasize on the fact that the most important aspect of analysis process is to quickly correlate attributes and identify patterns. The approach we propose is to minimize the noise and highlight significant behavior using heuristics targeted specifically towards structural pattern identification. The visual representation of the input file provides a concise overview of file's data patterns and the way they are combined together. One glimpse of this visual representation is enough to quickly classify a file as suspicious.In this talk, we will focus on presenting a framework that can help users with forensic analysis of intrusion artifacts using a novel visual analysis approach. This framework could be used to create standalone utilities or to enhance in-house analysis tools via the native API. For quick analysis, users could consume the framework output directly through the packaged commandline tool or via an external log analytic tool like Splunk.

</details>

---
## 📱 Mobile Security
<details><summary><strong>Android-InsecureBankv2</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Dinesh Shetty](https://img.shields.io/badge/Dinesh%20Shetty-informational)

🔗 **Link:** [Android-InsecureBankv2](https://github.com/dineshshetty/Android-InsecureBankv2)  
📝 **Description:** Ever wondered how different attacking a Mobile application would be, from a traditional web application? Gone are the days when knowledge of just SQL Injection or XSS could help you land a lucrative high-paying InfoSec job. Watch as Dinesh walks you through his new and shiny updated custom application, "Android-InsecureBank" and some other source code review tools, to help you understand some known and some not so known Android Security bugs and ways to exploit them.This presentation will cover Mobile Application Security attacks that will get n00bs as well as 31337 attendees started on the path of Mobile Application Penetration testing. Some of the vulnerabilities in the Android InsecureBank application that will be discussed (but not limited to) are:Flawed broadcast receiversWeakauthorization mechanismRootdetection andbypassLocalencryption issuesVulnerableactivitycomponentsInsecure content provider accessInsecurewebview implementationWeakcryptography implementationApplicationpatchingSensitive information in memoryExpect to see a lot of demos, tools, hacking and have loads of fun.

</details>

<details><summary><strong>AndroidTamer</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Anant Shrivastava](https://img.shields.io/badge/Anant%20Shrivastava-informational)

🔗 **Link:** [AndroidTamer](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/mobile_hacking/androidtamer.md)  
📝 **Description:** AndroidTamer started out as a VirtualMachine for Android (security) Professional, we are slowly making Android Tamer a single point of Reference for Android Professionals. We will be demoing multiple projects that we have created under AndroidTamer umbrella,AndroidTamer Debian based VM Customized to the core debian 8 based virtual machine environment with preloaded tools for usage in Android PentestingAndroid-emulator customised for pentesting (both x86 and arm version) Customized emulator to be used in place of a device in both x86 and arm version which can be coupled with Tamer VM.Most extensive Tools Documentation https://tools.androidTamer.com: hosts the most extensive single location documentation for largest array of tools needed for android security.DEB / YUM Repository for tools / software distribution. https://repo.androidtamer.com: Only repository which is actively maintained and support both debian and Redhat distributions.Knowledge Base https://kb.Androidtamer.com: contains various documentation around android which is useful to many people around the world. includes our very famous "Android Security Enhancement" sheet.All this will be part of the jam packed demo's that will be presented at Black Hat USA Arsenal.

</details>

<details><summary><strong>AVLInsight Mobile Threat Intelligence Platform</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Tom Pan](https://img.shields.io/badge/Tom%20Pan-informational)

🔗 **Link:** [AVLInsight Mobile Threat Intelligence Platform](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** AVLInsight Mobile Threat Intelligence Platform that aggregate multiple threat intelligence sources and several analysis tools to help mobile threat researchers easier to analyze mobile threat activities, find the relations between them. AVLInsight Mobile Threat Intelligence Platform will open multiple sources to researchers: mobile malware information source, mobile OSINT source, structured mobile TTP source. Mobile researchers can search keyword in each source which they expected, or can link to the other source for search the relations.AVL Insight also provides a set of threat analysis tools: Smaliviewer for malware sample static analysis and RMS for dynamic analysis, Spoof Apps Analysis Tool, and a graphic threat analysis tool supported TTP analysis. We will demonstrate AVLInsight with several mobile threats to show how to discover these kinds of threats and the relations between them.

</details>

<details><summary><strong>Burp Extension for Non-HTTP Traffic</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Josh Huston](https://img.shields.io/badge/Josh%20Huston-informational)

🔗 **Link:** [Burp Extension for Non-HTTP Traffic](https://github.com/voidism/Input_Method_auto-Modifier/blob/master/EnWordBase.json)  
📝 **Description:** The Burp Non-HTTP proxy is specifically designed to help in testing thick client and mobile applications. It adds to BurpSuite a DNS server to help test applications that are difficult to route through proxies and adds interceptors to manipulate/mangle binary and non-HTTP protocols.The tool stores traffic in a sqlite database that can be exported or imported to save and analyze later. It can intercept and modify traffic automatically based on rules you assign or it can be modified manually as the traffic hits the proxy server. The tool also support SSL/TLS and signs certificates based on Burps CA certificate. If your testing on a mobile device that already has Burp's CA cert then the traffic will be seamlessly decrypted without errors into the tool for you to mangle before sending it on to the outgoing server.This tool arouse out of the need to test applications that were switching to more realtime protocols in both mobile applications and some web based Silverlight applications I had been testing. I wrote this tool as an easy extension to add to burp that would also be platform/OS independent vs some other tools out there that did similar functions.

</details>

<details><summary><strong>Droid-FF: Android Fuzzing Framework</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Anto Joseph](https://img.shields.io/badge/Anto%20Joseph-informational)

🔗 **Link:** [Droid-FF: Android Fuzzing Framework](https://github.com/antojoseph/droid-ff)  
📝 **Description:** Droid-FF is the very first Android fuzzing framework which helps researchers find memory corruption bugs written in c /c ++ â It comes as a VM which is ready to go and easy to work with. Why Droid-FF ? Native code is preferred over JIT languages due to their memory efficiency and speed, but security bugs within native code can result in exploits that can take over the Android system . The goal of the fuzzer is help researchers find security bugs by fuzzing Android.What does it do?Data Generation Currently includes Peach, with some pre-populated pit files, which helps in generating data be it "dex,ttf,png,avi,mp4" etcApproaches a . Dumb fuzzing: From a large input section of valid data , the fuzzer generates new data with mutations in place. b. Intelligent Fuzzing: We create a file format representation of the target data and let the fuzzer generate data which is structurally valid, but has invalid data in sections.Fuzzing System The fuzzing system is an automated program which runs the dataset against the target program and deals with any error conditions that can possibly happen. It also maintains state so that we could resume the fuzzing from the right place in an event of a crash.Advanced Triage System In the event of a valid crash, the triage system collects the tombstone files which contains the dump of the registers and system state with detailed information. It also collects valid logs and the file responsible for the crash and moves it to the triage database. The triage database runs scripts on the data derived from crashes, like the type pf the crash, for eg : SIGSEGV, the PC address at this crash and checks for any duplicate, if found, the duplicate entry is removed and is moved to crashes for investigation.What we're using during this lab? The android system which we are going to fuzz is an Engineering build from AOSP which has symbols, thus in an event of a crash, it will be much easier to triage the crash. The system supports fuzzing real devices, emulators , and images running on virtual box. How Efficient is this Framework? We ran the fuzzer in Intelligent fuzzing mode with mp4 structure fed in for 14 hours on the stagefright binary and it was able to reproduce 3 crashes which were exploitable ( CVE's) and lots of un-interesting crashes mostly dude to out of memory, duplicates or null pointers.Goals of the FrameworkMake Fuzzing Easy and available for allCompletely open source and extensibleMake android eco-system more secure

</details>

<details><summary><strong>Koodous</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Francisco LÃ³pez](https://img.shields.io/badge/Francisco%20LÃ³pez-informational) ![Fernando Denis RamÃ­rez](https://img.shields.io/badge/Fernando%20Denis%20RamÃ­rez-informational)

🔗 **Link:** Not Available  
📝 **Description:** Koodous is a collaborative web platform for Android malware research that combines the power of online analysis tools with social interactions between the analysts over a vast APK repository (at this time, more than 10 million). It also features an Android antivirus app and a public API.Some of the features included in the tool:Navigate the repository using advanced search expressions (developer's certificate and name, hash, package name, etc.) to locate samples of interest.For each sample we provide a set of information: metadata, strings, static and dynamic analysis, etc. This set grows with new features. Also, you can download, tag, comment and vote any sample.As an analyst, you will be able to create Yara rulesets. This rules will be run automatically against any new sample that enter the system (or any other sample on-demand) and you will be notified if a new match occurs. The rules can be set as private, public or social.The Android app detects any threat detected by the community installed in an Android device. Also, it is possible to link the app with your analyst account to create a personal antivirus.There is a free-to-use API and open source Python modules in case you want to interact with the system programmatically.And it is totally free! The presenter will make a live demo of all this features. More information at: https://koodous.com/

</details>

<details><summary><strong>Shevirah</strong></summary>

![Category: 📱 Mobile Security](https://img.shields.io/badge/Category:%20📱%20Mobile%20Security-yellow) ![Georgia Weidman](https://img.shields.io/badge/Georgia%20Weidman-informational)

🔗 **Link:** [Shevirah](https://github.com/georgiaw)  
📝 **Description:** Shevirah is a suite of testing tools for assessing and managing the risk of mobile devices in the enterprise and testing the effectiveness of enterprise mobility management solutions. Shevirah allows security teams to integrate mobility into their risk management and penetration testing programs. Given only a phone number, testers can design a simulated attack campaign against Android and iOS base mobile devices; execute phishing, client side, remote attacks, and extensive post exploitation capabilities to gauge the security of the users, devices, applications, and security infrastructure around mobility. The free version demoed here comes complete with professional features such as a full GUI and reporting capabilities as well as the traditional command line interface for the more purist hackers.

</details>

---
## Others
<details><summary><strong>AppMon</strong></summary>

![Category: Others](https://img.shields.io/badge/Category:%20Others-lightgrey) ![Nishant Das Pattanaik](https://img.shields.io/badge/Nishant%20Das%20Pattanaik-informational)

🔗 **Link:** [AppMon](https://github.com/dpnishant)  
📝 **Description:** AppMon is an automated framework for monitoring and tampering system API calls of native apps on iOS, Mac OS X and Android apps (upcoming). You may call it the GreaseMonkey for native mobile apps. ;-) AppMon is my vision is to make become the Mac OS X/iOS/Android equivalent of the this project apimonitor and GreaseMonkey. This should become a useful tool for the mobile penetration testers to validate the security issues report by a source code scanner and by inspecting the APIs in runtime and monitoring the app's overall activity and focus on things that seem suspicious. You can also use pre-defined user-scripts to modify the app's functionality/logic in the runtime e.g. spoofing the DeviceID, spoofing the GPS co-ordinates, faking In-App purchases, bypassing TouchID etc.In the current release, we have the ability to hook both the Apple's CoreFoundation API's as well as the Objective-C methods (even if its done in a Swift app via the bridging header).

</details>

---
## 🟣 Red Teaming / Embedded
<details><summary><strong>Arsenal Theater Demo: BSOD HD: An FPGA-Based HDMI Injection and Capture Tool</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational) ![Zoz Brooks](https://img.shields.io/badge/Zoz%20Brooks-informational)

🔗 **Link:** [Arsenal Theater Demo: BSOD HD: An FPGA-Based HDMI Injection and Capture Tool](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** BSODomizer HD is an open source, FPGA-based, covert electronic device that injects and captures HDMI signals. Currently a proof-of-concept design, this much anticipated follow-up to the original BSODomizer released in 2008 (www.bsodomizer.com) improves on the graphics interception and triggering features, and can capture screenshots of any non-HDCP target up to 1080p resolution. Uses of the tool include penetration testing, video display calibration, mischievous acts, or as a reference design for exploration into the mystical world of FPGAs.Co-developed by Joe Grand (aka Kingpin) of Grand Idea Studio and Zoz of Cannytrophic Design.

</details>

<details><summary><strong>Arsenal Theater Demo: CAN Badger</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Javier Vazquez Vidal](https://img.shields.io/badge/Javier%20Vazquez%20Vidal-informational) ![Henrik Ferdinand Noelsche](https://img.shields.io/badge/Henrik%20Ferdinand%20Noelsche-informational)

🔗 **Link:** [Arsenal Theater Demo: CAN Badger](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** The car hacking topic is really hot at the moment, and many vulnerabilities affecting entire fleets are found from time to time. But is this all that there is regarding this topic? We want to introduce the CAN Badger, a tool designed to ease the way a vehicle is reversed. It is a hardware tool, not just an interface connected to a PC.Like its predecessor, the ECU Tool, the CAN Badger is able to handle the Security in ECUs in an easy way, as well as provide verbose information on what's going on in the buses. Want to learn how to approach vehicle electronics security in a practical way? Come and visit us at Arsenal!

</details>

<details><summary><strong>Arsenal Theater Demo: ChipWhisperer</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Colin O'Flynn](https://img.shields.io/badge/Colin%20O'Flynn-informational)

🔗 **Link:** [Arsenal Theater Demo: ChipWhisperer](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** ChipWhisperer is the world's first complete open-source (hardware+software+documentation) toolchain for advanced embedded hardware security analysis such as side-channel power analysis and glitching attacks. In 2016 the software has been completely overhauled to improve the modular design and make it easier than ever for researchers to develop their own plug-ins.We'll be demoing some of the previous open-source hardware (such as the ChipWhisperer-Lite which was a Kickstarter during 2015) along with brand-new hardware, and the release of overhauled software tools with improved API, performance, and features. Don't miss your chance to see ChipWhisperer in action!

</details>

<details><summary><strong>Arsenal Theater Demo: Highway to the Danger Drone</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Francis Brown](https://img.shields.io/badge/Francis%20Brown-informational) ![Dan Petro](https://img.shields.io/badge/Dan%20Petro-informational) ![David Latimer](https://img.shields.io/badge/David%20Latimer-informational)

🔗 **Link:** [Arsenal Theater Demo: Highway to the Danger Drone](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Do you feel the needâ¦ the need for speed? Then check out our brand new penetration testing drone. This Raspberry Pi based copter is both cheap and easy to create on your own, making it the first practical drone solution for your pentesting needs. Drones have emerged as the prevailing weapon of choice in modern warfare, so it's only logical that we'd also explore the potential applications of this formidable tool in cyber warfare. While there have been presentations before on weaponizing drones for the purposes of pentesting, these efforts were not easily replicated by anyone other than experienced drone aficionados with several thousands of dollars to spend â ultimately resulting in somewhat clunky, partial solutions. Conditions have finally matured enough to where pentesters who are inexperienced with drones can get up and running fairly quickly and spending only a couple hundred dollars on a Raspberry Pi based drone copter solution. Our talk will be aimed at this target audience, helping equip pentesters with drone tools of the future.In this talk, we'll demonstrate how this drone can be used to perform aerial recon, attack wireless infrastructure and clients, land on a target facility roof, and serve as a persistent backdoor. In fact, we'll show you how to attack 'over the air' protocols such as RFID, ZigBee, Bluetooth, Wi-Fi, and more. We'll even demo a special edition "RickMote Danger Drone" that you can use to patrol your neighborhood and rickroll Google Chromecast-connected TVs.Additionally, we will showcase the best-of-breed in hardware and software that you'll need. This will include the release of our custom Raspberry Pi SD card image, parts list, 3D print objects, and necessary instructions for you to create a Danger Drone of your own. We'll also be giving away a fully functional Danger Drone to one lucky audience member - guaranteed to leave your friends feeling peanut butter and jealous! This DEMO-rich presentation will benefit both newcomers and seasoned professionals of drone and physical penetration testing fields. Someone better call Kenny Loggins, because you're in the Danger Drone.â¦No, no boys, there's two 'O's in Bishop Fox.

</details>

<details><summary><strong>Arsenal Theater Demo: WarBerryPi Troops Deployment in Red Teaming Scenarios</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Yiannis Ioannides](https://img.shields.io/badge/Yiannis%20Ioannides-informational)

🔗 **Link:** [Arsenal Theater Demo: WarBerryPi Troops Deployment in Red Teaming Scenarios](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** What if the only requirements for taking down a corporate network are a bit of smooth talking, 60 minutes and $35? Traditional hacking techniques and corporate espionage have evolved. Advanced attacks nowadays include a combination of social engineering, physical security penetration and logical security hacking. It is our job as security professionals to think outside the box and think about the different ways that hackers might use to infiltrate corporate networks. The WarBerryPi is a customized RaspBerryPi hacking dropbox which is used in Red Teaming engagements with the sole purpose of performing reconnaissance and mapping of an internal network and providing access to the remote hacking team.The outcome of these red teaming exercises is the demonstration that if a low cost microcomputer loaded with python code can bypass security access controls and enumerate and gather such a significant amount of information about the infrastructure network which is located at; then what dedicated hackers with a large capital can do is beyond conception.

</details>

<details><summary><strong>BSOD HD: An FPGA-Based HDMI Injection and Capture Tool</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational) ![Zoz Brooks](https://img.shields.io/badge/Zoz%20Brooks-informational)

🔗 **Link:** [BSOD HD: An FPGA-Based HDMI Injection and Capture Tool](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** BSODomizer HD is an open source, FPGA-based, covert electronic device that injects and captures HDMI signals. Currently a proof-of-concept design, this much anticipated follow-up to the original BSODomizer released in 2008 (www.bsodomizer.com) improves on the graphics interception and triggering features, and can capture screenshots of any non-HDCP target up to 1080p resolution. Uses of the tool include penetration testing, video display calibration, mischievous acts, or as a reference design for exploration into the mystical world of FPGAs.Co-developed by Joe Grand (aka Kingpin) of Grand Idea Studio and Zoz of Cannytrophic Design.

</details>

<details><summary><strong>CAN Badger</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Javier Vazquez Vidal](https://img.shields.io/badge/Javier%20Vazquez%20Vidal-informational) ![Henrik Ferdinand Noelsche](https://img.shields.io/badge/Henrik%20Ferdinand%20Noelsche-informational)

🔗 **Link:** [CAN Badger](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** The car hacking topic is really hot at the moment, and many vulnerabilities affecting entire fleets are found from time to time. But is this all that there is regarding this topic? We want to introduce the CAN Badger, a tool designed to ease the way a vehicle is reversed. It is a hardware tool, not just an interface connected to a PC.Like its predecessor, the ECU Tool, the CAN Badger is able to handle the Security in ECUs in an easy way, as well as provide verbose information on what's going on in the buses. Want to learn how to approach vehicle electronics security in a practical way? Come and visit us at Arsenal!

</details>

<details><summary><strong>NetDB - The Network Database Project</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Bertin Bervis](https://img.shields.io/badge/Bertin%20Bervis-informational) ![James Jara](https://img.shields.io/badge/James%20Jara-informational)

🔗 **Link:** [NetDB - The Network Database Project](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** NetDB is an Internet of things Search engine created in 2014 by Bertin Bervis and James Jara. Using agents(crawlers) distributed in several countries, Netdb is scanning all Internet searching randomly 24 hours a day, indexing and parsing data based on responses. For each device, we are storing all banners and fingerprints but we are focused mostly in SSL Information of the device.We will cover basic information about our architecture, query builder, API and enterprise access and finally about the future of NetDB with Machine learning plus IoT infosecurity.

</details>

<details><summary><strong>Rapid Bluetooth Low Energy Testing with BLE-replay and BLESuite</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Greg Foringer](https://img.shields.io/badge/Greg%20Foringer-informational) ![Taylor Trabun](https://img.shields.io/badge/Taylor%20Trabun-informational)

🔗 **Link:** [Rapid Bluetooth Low Energy Testing with BLE-replay and BLESuite](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** In order to optimize testing with Bluetooth Low Energy (BLE) peripherals, we have created user-friendly tools that enable BLE packet replay, fuzzing, and on-the-fly scripted communications. BLE-replay is a Python tool for recording, modifying, replaying, and fuzzing writes to Bluetooth Low Energy (BLE) peripherals. It can be used for testing or reversing application layer interactions between a mobile application and a BLE peripheral. This tool is useful if an application writes some characteristics on the BLE device in order to configure/unlock/disable some feature. You want to quickly capture the relevant information from a packet log into a human-readable format and mess around with it from a laptop. It is the first tool built upon our new BLESuite library.BLESuite is a Python library that enables application layer communication between a host machine and a BLE device. The library greatly simplifies the scripting of BLE activity. It provides a simple connection manager and supports scanning advertisements, service discovery, smart scanning of all services/characteristics/descriptors, and sync/async read/write. We will also demonstrate the BLESuiteCLI, which provides quick access to all of these features from the command line.

</details>

<details><summary><strong>WALB (Wireless Attack Launch Box)</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Keiichi Horiai](https://img.shields.io/badge/Keiichi%20Horiai-informational) ![Kazuhisa Shirakami](https://img.shields.io/badge/Kazuhisa%20Shirakami-informational)

🔗 **Link:** [WALB (Wireless Attack Launch Box)](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** The purpose of the WALB (Wireless Attack Launch Box) is to test or demonstrate the security issue of wireless devices. It can be used to evaluate the impact of GPS spoofing, fake ADS-B and others. WALB is a Raspberry Pi and HackRF based lunch box size portable RF signal generator. It can include the real time signal generation module for GPS, ADS-B and others. Therefor it does not require huge storage space for longer duration of the simulation time. You can choose any predefined scenario of GPS spoofing, fake ADS-B and power level settings from menu on LCD screen. By preparing any 8 bit signed I/Q binary file, it is possible to generate arbitrary signal within the frequency range available on HackRF.

</details>

<details><summary><strong>WarBerryPi Troops Deployment in Red Teaming Scenarios</strong></summary>

![Category: 🟣 Red Teaming / Embedded](https://img.shields.io/badge/Category:%20🟣%20Red%20Teaming%20/%20Embedded-purple) ![Yiannis Ioannides](https://img.shields.io/badge/Yiannis%20Ioannides-informational)

🔗 **Link:** [WarBerryPi Troops Deployment in Red Teaming Scenarios](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** What if the only requirements for taking down a corporate network are a bit of smooth talking, 60 minutes and $35? Traditional hacking techniques and corporate espionage have evolved. Advanced attacks nowadays include a combination of social engineering, physical security penetration and logical security hacking. It is our job as security professionals to think outside the box and think about the different ways that hackers might use to infiltrate corporate networks. The WarBerryPi is a customized RaspBerryPi hacking dropbox which is used in Red Teaming engagements with the sole purpose of performing reconnaissance and mapping of an internal network and providing access to the remote hacking team.The outcome of these red teaming exercises is the demonstration that if a low cost microcomputer loaded with python code can bypass security access controls and enumerate and gather such a significant amount of information about the infrastructure network which is located at; then what dedicated hackers with a large capital can do is beyond conception.

</details>

---
## 🔴 Red Teaming
<details><summary><strong>Arsenal Theater Demo: CrackMapExec</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Marcello Salvati](https://img.shields.io/badge/Marcello%20Salvati-informational)

🔗 **Link:** [Arsenal Theater Demo: CrackMapExec](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** CrackMapExec is fully open-source and hosted on Github: it aims to be a one-stop-shop for all of your offensive Active Directory needs by combining the power of Python, Powersploit and the Impacket library!Taking inspiration from previous tools such as:smbexecsmbmapcredcrackIt allows you to quickly and efficiently import credentials from Empire and Metasploit, replay credentials, pass-the-hash, execute commands, powershell payloads, spider SMB shares, dump SAM hashes, the NTDS.dit, interact with MSSQL databases and lots more in a fully concurrent pure Python script that requires no external tools and is completely OpSec safe! (no binaries are uploaded to disk!).

</details>

<details><summary><strong>Arsenal Theater Demo: FakeNet-NG</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Peter Kacherginsky](https://img.shields.io/badge/Peter%20Kacherginsky-informational)

🔗 **Link:** [Arsenal Theater Demo: FakeNet-NG](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** FakeNet-NG is a next generation dynamic network analysis tool for malware analysts and penetration testers. FakeNet-NG was inspired by the original FakeNet tool developed by Andrew Honig and Michael Sikorski. FakeNet-NG implements all the old features and many new ones; plus, it is open source and designed to run on modern versions of Windows. FakeNet-NG allows you to intercept and redirect all or specific network traffic while simulating legitimate network services. Using FakeNet-NG, malware analysts can quickly identify malware's functionality and capture network signatures. Penetration testers and bug hunters will find FakeNet-NG's configurable interception engine and modular framework highly useful when testing application's specific functionality and prototyping PoCs. During the tool session attendees will learn the following practical skills:Use FakeNet-NG to mimic common protocols like HTTP, SSL, DNS, SMTP, etc.Configure FakeNet-NG's listeners and interception engine to defeat malware and target specific application functionality.Perform interception on the analysis, secondary or gateway hosts.Use process tracking functionality to identify which processes are generating malicious network activity and dynamically launch services in order to interact with a process and capture all of its network traffic.How to use FakeNet-NG's detailed logging and PCAP capture capabilities.Quickly develop a custom protocol listener using FakeNet-NG's modular architecture. (Includes live malware demo).Bring your Windows analysis Virtual Machine for the demo. The hands-on section of this session will analyze real world malware samples to tease out network-based signatures as well as demonstrate how it can be used to perform security assessments of thick client applications. The challenges start at a basic level and progress until you dive into how to extend FakeNet-NG by writing modules in Python.

</details>

<details><summary><strong>Arsenal Theater Demo: Faraday</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Federico Kirschbaum](https://img.shields.io/badge/Federico%20Kirschbaum-informational)

🔗 **Link:** [Arsenal Theater Demo: Faraday](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Since collaborative pentesting is more common each day and teams become larger, sharing the information between pentesters can become a difficult task. Different tools, different formats, long outputs (in the case of having to audit a large network) can make it almost impossible. You may end up with wasted efforts, duplicated tasks, a lot of text files scrambled in your working directory. And then, you need to collect that same information from your teammates and write a report for your client, trying to be as clear as possible.The idea behind Faraday is to help you to share all the information that is generated during the pentest, without changing the way you work. You run a command, or import a report, and Faraday will normalize the results and share that with the rest of the team in real time. Faraday has more than 50 plugins available (and counting), including a lot of common tools. And if you use a tool for which Faraday doesn't have a plugin, you can create your own. During this presentation we're going release Faraday v2.0.0 with all the new features that we were working on for the last couple of months.

</details>

<details><summary><strong>Arsenal Theater Demo: ShinoBOT</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Shota Shinogi](https://img.shields.io/badge/Shota%20Shinogi-informational)

🔗 **Link:** [Arsenal Theater Demo: ShinoBOT](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** ShinoBOT Suite is a malware/target attack simulator framework for pentest, education. The new version becomes "suiter" than the previous version.It includes those new features, components. You can now test your security performance against ransomware with it. ShinoLocker behaves just like a real ransomware but does not ask for any money to get the crypt key.1) ShinoLocker (Ransomware Simulator)Get the Crypto key from serverScan files to encryptEncrypt -Ask decryption keyDecryptUninstall itself2) ShinoBuilder (Full customization for ShinoBOT)Anti dynamic analysisExtremely Targeted Attack *You can make a malware that works only on your specific environment.C&C URL (for ShinoProxy)Polymorphic function3) ShinoC2 (ShinoBOT's Server)SSL support (Thanks Let's Encrypt Project)DNS TunnelingC2 communication can be done by just DNS4) ShinoStuxnet(tentative)ICS malware simulator.Scan ICS/SCADA system.Talks some ICS protocols.

</details>

<details><summary><strong>autoDANE</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Dane Goodwin](https://img.shields.io/badge/Dane%20Goodwin-informational)

🔗 **Link:** [autoDANE](https://github.com/danegoodwin)  
📝 **Description:** autoDANE: Automatic Domain Admin & Network ExploitationautoDANE is a tool to automate the process of mapping and compromising internal networks. It is available at https://github.com/sensepost/autoDANE Given the prevalence of Microsoft Active Directory domains as the primary means of managing large corporate networks globally; one of the first goals of any internal penetration test is to get Domain Administrator (DA) level access. In demonstration of how common a goal and practise this is, a plethora of tools and techniques exists to assist with this process, from the initial "in" through to to elevation of privilege and eventually extracting and cracking all domain credentials.However, the overall process followed is still manual and time consuming. Even where tools exist, the orchestration from one to the next is manual. The time required both detracts from potentially more dangerous attacks that may be specific to the organisation under assessment, as well as limits those who know of their organisation's vulnerabilities to those with offensive security skills or willing to pay for an assessment. Observing this, we decided to construct a framework for automating such activities. This framework orchestrates the industries currently favoured tools to get DA on internal networks.The goal for the project is to get Domain Admin rights as quickly as possible, so that analysts can start an internal assessment as a privileged user, rather than finishing as one. This will allow analysts to spend time on engagements emulating real life hacking scenarios, such as going after business critical applications, while still comprehensively assessing the internal network. Combining the software vulnerabilities, as well as a realistic idea of how people with malicious or criminal intent might reach them, will provide organisations the information they need to actually improve their defensive posture.For Arsenal, several updates have been made and will be released:Detailed scope definition and proportionality limitsSupport for adding hosts/ranges during runtimeDomain pivot tables-a list of which credentials worked where and which users are in which groupsDetailed filtering and full-text searching across tool-run logsOne click RDP to hosts with confirmed credentialsSQL Server discoveryBasic password cracking when hashes are pulled

</details>

<details><summary><strong>Automated Penetration Testing Toolkit (APT2)</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational)

🔗 **Link:** [Automated Penetration Testing Toolkit (APT2)](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/vulnerability_assessment/apt2.md)  
📝 **Description:** Nearly every penetration test begins the same way; run a NMAP scan, review the results, choose interesting services to enumerate and attack, and perform post-exploitation activities. What was once a fairly time consuming manual process, is now automated!Automated Penetration Testing Toolkit (APT2) is an extendable modular framework designed to automate common tasks performed during penetration testing. APT2 can chain data gathered from different modules together to build dynamic attack paths. Starting with a NMAP scan of the target environment, discovered ports and services become triggers for the various modules which in turn can fire additional triggers. Have FTP, Telnet, or SSH? APT2 will attempt common authentication. Have SMB? APT2 determines what OS and looks for shares and other information. Modules include everything from enumeration, scanning, brute forcing, and even integration with Metasploit. Come check out how APT2 will save you time on every engagement.

</details>

<details><summary><strong>BinProxy</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Ryan Koppenhaver](https://img.shields.io/badge/Ryan%20Koppenhaver-informational)

🔗 **Link:** [BinProxy](https://github.com/nccgroup/BinProxy)  
📝 **Description:** BinProxy is a tool for understanding and manipulating binary network traffic; it's designed to provide straightforward and useful out-of-the box functionality, with a convenient, powerful environment for developers and penetration testers to build protocol-specific extensions.The core functionality of BinProxy is an intercepting TCP proxy. With no coding, users can view and edit intercepted traffic as text or a hex dump, but the real power of the tool comes from protocol-specific parser classes (built with Ruby and the BinData gem) that present higher-level representations of a protocol. BinProxy comes with a few sample parsers, and a number of utility methods that allow users to easily create their own.The tool also supports pluggable filters to unwrap TLS, act as a SOCKS proxy, or perform other pre- or post-processing of messages. The demo will also include a simple "BinProxy in a box" setup with a dedicated wireless router.

</details>

<details><summary><strong>BloodHound</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Andy Robbins](https://img.shields.io/badge/Andy%20Robbins-informational)

🔗 **Link:** [BloodHound](https://github.com/ly4k/BloodHound)  
📝 **Description:** Active Directory domain privilege escalation is a critical component of most penetration tests and red team assessments, but standard methodology dictates a manual and often tedious process â gather credentials, analyze new systems we now have admin rights on, pivot, and repeat until we reach our objective. Then -- and only then -- we can look back and see the path we took in its entirety. But that may not be the only, nor shortest path we could have taken.By combining the concept of derivative admin (the chaining or linking of administrative rights), existing tools, and graph theory, we have developed a capability called BloodHound, which can reveal the hidden and unintended relationships in Active Directory domains. BloodHound is operationally-focused, providing an easy-to-use web interface and PowerShell ingestor for memory-resident data collection and offline analysis.BloodHound offers several advantages to both attackers and defenders. Otherwise invisible, high-level organizational relationships are exposed. Most possible escalation paths can be efficiently and swiftly identified. Simplified data aggregation accelerates blue and red team analysis. BloodHound has the power and the potential to dramatically change the way you think about and approach Active Directory domain security.

</details>

<details><summary><strong>Brosec</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Gabe Marshall](https://img.shields.io/badge/Gabe%20Marshall-informational)

🔗 **Link:** [Brosec](https://github.com/gabemarshall)  
📝 **Description:** Brosec is a terminal based reference utility designed to help infosec bros and broettes with useful (yet sometimes complex) payloads and commands that are often used during work as infosec practitioners. Brosec's most popular use cases is the ability to generate one-liner reverse shells (python, perl, powershell, etc) payloads that get copied to are then copied to the clipboard.

</details>

<details><summary><strong>CodexGigas Malware DNA Profiling Search Engine</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Luciano Martins](https://img.shields.io/badge/Luciano%20Martins-informational) ![Rodrigo Cetera](https://img.shields.io/badge/Rodrigo%20Cetera-informational) ![Javier Bassi](https://img.shields.io/badge/Javier%20Bassi-informational)

🔗 **Link:** [CodexGigas Malware DNA Profiling Search Engine](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** CodexGigas is a malware profiling search engine that allows malware hunters and analysts to really interrogate the internals of malware and perform searches over a large number of file characteristics. For instance, instead of relying on file-level hashes, we can compute other features such as imported functions, strings, constants, file segments, code regions, or anything that is defined in the file type specification, and that provides us with more than 142 possible searchable patterns, that can be combined.Similar to human fingerprints, every malware has its own unique digital fingerprint that differentiates it from others. As a result, malware will always attempt to hide its true self by deleting or changing this information to avoid detection by antivirus companies and malware researchers.Since malware developers go to great lengths to obfuscate their characteristics, it is often difficult for by researchers and malware analysts to identify multiple characteristics and correlation points. By analyzing malware internals, the algorithm is able to build characteristic families to which a new sample can be categorized and therefore identified for specific behavior, enabling early detection of new malware by comparing against existing malware. CodexGigas engine, framework, analysis plugins, and the web portal, will be released as open source at Black Hat.Come to see how CodexGigas could be used to enhance your malware hunting. Link: https://twitter.com/codexgigassys

</details>

<details><summary><strong>CrackMapExec</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Marcello Salvati](https://img.shields.io/badge/Marcello%20Salvati-informational)

🔗 **Link:** [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec/blob/master/pyproject.toml)  
📝 **Description:** CrackMapExec is fully open-source and hosted on Github: it aims to be a one-stop-shop for all of your offensive Active Directory needs by combining the power of Python, Powersploit and the Impacket library!Taking inspiration from previous tools such as:smbexecsmbmapcredcrackIt allows you to quickly and efficiently import credentials from Empire and Metasploit, replay credentials, pass-the-hash, execute commands, powershell payloads, spider SMB shares, dump SAM hashes, the NTDS.dit, interact with MSSQL databases and lots more in a fully concurrent pure Python script that requires no external tools and is completely OpSec safe! (no binaries are uploaded to disk!).

</details>

<details><summary><strong>Ebowla</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Travis Morrow](https://img.shields.io/badge/Travis%20Morrow-informational)

🔗 **Link:** [Ebowla](https://github.com/Genetic-Malware/Ebowla/blob/master/LICENSE.md)  
📝 **Description:** Dropping a payload or malware onto a target is usually not an issue given the variety of vulnerable software in use. Your challenge is keeping the payload from working and spreading to unintended targets, eventually leading to reverse engineers, crowdsourced or professional, who pick apart your work, and start an industry to stop your success. Inspiration for the tool came from the effective use of environmental keying in Gauss malware (2012) that, to this day, has prevented the reverse engineering community around the world from determining the purpose and use of all operational modules used in various industry attacks [https://securelist.com/blog/incidents/33561/the-mystery-of-the-encrypted-gauss-payload-5/].Our framework, Ebowla [https://github.com/Genetic-Malware/Ebowla], implements techniques above and beyond those found in Gauss or Flashback to keep your payload from detection and analysis. Currently we support three protection mechanisms: AES file based keying, AES environmental based keying, and One Time Pad (closer to a digital book cipher) based off a known file on the target's system. The protected payloads are generated with either a stand-alone python or golang in-memory loader for the target system.

</details>

<details><summary><strong>FakeNet-NG</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Peter Kacherginsky](https://img.shields.io/badge/Peter%20Kacherginsky-informational)

🔗 **Link:** [FakeNet-NG](https://github.com/mandiant/flare-fakenet-ng)  
📝 **Description:** FakeNet-NG is a next generation dynamic network analysis tool for malware analysts and penetration testers. FakeNet-NG was inspired by the original FakeNet tool developed by Andrew Honig and Michael Sikorski. FakeNet-NG implements all the old features and many new ones; plus, it is open source and designed to run on modern versions of Windows. FakeNet-NG allows you to intercept and redirect all or specific network traffic while simulating legitimate network services. Using FakeNet-NG, malware analysts can quickly identify malware's functionality and capture network signatures. Penetration testers and bug hunters will find FakeNet-NG's configurable interception engine and modular framework highly useful when testing application's specific functionality and prototyping PoCs. During the tool session attendees will learn the following practical skills:Use FakeNet-NG to mimic common protocols like HTTP, SSL, DNS, SMTP, etc.Configure FakeNet-NG's listeners and interception engine to defeat malware and target specific application functionality.Perform interception on the analysis, secondary or gateway hosts.Use process tracking functionality to identify which processes are generating malicious network activity and dynamically launch services in order to interact with a process and capture all of its network traffic.How to use FakeNet-NG's detailed logging and PCAP capture capabilities.Quickly develop a custom protocol listener using FakeNet-NG's modular architecture. (Includes live malware demo).Bring your Windows analysis Virtual Machine for the demo. The hands-on section of this session will analyze real world malware samples to tease out network-based signatures as well as demonstrate how it can be used to perform security assessments of thick client applications. The challenges start at a basic level and progress until you dive into how to extend FakeNet-NG by writing modules in Python.

</details>

<details><summary><strong>FingerPrinTLS</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Lee Brotherston](https://img.shields.io/badge/Lee%20Brotherston-informational)

🔗 **Link:** [FingerPrinTLS](https://github.com/salesforce/ja3)  
📝 **Description:** FingerprinTLS is a tool which leverages TLS client fingerprinting techniques to passively identify clients realtime via a network tap or offline via pcap files. This allows network administrators to identify clients with TLS enabled malware installed, rogue installations of cloud storage solutions, unauthorised Tor connections, etc. Organisations which expose APIs can determine if unwanted clients, such as attack tools are accessing their APIs. The tool has an internal database of fingerprints which have already been discovered and automates the process of adding your own. FingerprinTLS is distributed as an opensource project and has been tested to work on Linux, OS X, and BSD based systems.

</details>

<details><summary><strong>Halcyon</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Sanoop Thomas](https://img.shields.io/badge/Sanoop%20Thomas-informational)

🔗 **Link:** [Halcyon](https://github.com/s4n7h0)  
📝 **Description:** Halcyon is the first IDE specifically focused on Nmap Script (NSE) Development. This research idea was originated while writing custom Nmap Scripts for Enterprise Penetration Testing Scenarios. The existing challenge in developing Nmap Scripts (NSE) was the lack of a development environment that gives easiness in building custom scripts for real world scanning, at the same time fast enough to develop such custom scripts. Halcyon is free to use, java based application that comes with code intelligence, code builder, auto-completion, debugging and error correction options and also a bunch of other features like other development IDE(s) has. This research was started to give better development interface/environment to researchers and thus enhance the number of NSE writers in the information security community.Halcyon IDE can understand Nmap library as well as traditional LUA syntax. Possible repetitive codes such as web crawling, bruteforcing etc., is pre-built in the IDE and this makes easy for script writers to save their time while developing majority of test scenarios.Following are the features provided by Halcyon IDE:Improved user interfaceCode intelligence workspaceSingle click configurationCode generatorScan settingsPost script development actions

</details>

<details><summary><strong>King Phisher</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

🔗 **Link:** [King Phisher](https://github.com/rsmusllp/king-phisher)  
📝 **Description:** What differentiates King Phisher from other phishing tools is the focus it has on the requirements of consultants needing a tool for penetration testing. It was built from the ground up with a heavy emphasis on flexibility to allow pentesters to tailor their attack for their current assessment. It also includes unique features not included in other phishing tools such as the ability to craft calendar invite messages.King Phisher is an open source tool for testing and promoting user awareness by simulating real world phishing attacks. It features an easy to use, yet very flexible architecture allowing full control over both emails and server content. King Phisher can be used to run campaigns ranging from simple awareness training to more complicated scenarios in which user aware content is served for harvesting credentials and drive by attacks.

</details>

<details><summary><strong>NetNeedle</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![John Ventura](https://img.shields.io/badge/John%20Ventura-informational)

🔗 **Link:** [NetNeedle](https://github.com/optiv/netneedle/blob/master/cmdquit.c)  
📝 **Description:** We believe that hiding a needle in a haystack is easier if the needle looks like hay. NetNeedle provides encrypted control channels and chat sessions that are disguised to look like other common network activity. It only transmits "decoy" data in the  "payload " section of any packet, so forensic analysts will only see packets that look identical to ordinary ping or HTTP GET requests. The actual data is encoded in IP headers in fields that typically contain random values. This tool was originally written to demonstrate network based steganography principals. However, it is usable in real world circumstances, and can assist in penetration testing within restricted network environments.In addition to evasion features, penetration testers can use NetNeedle to maintain control over servers in environments with highly restrictive access lists. Because this tool subverts expectations surrounding network traffic, it enables users to set up back doors that use simple ICMP packets or TCP ports that are already in use. Administrators who believe that their systems are safe due to access control lists based on a "principle of least privilege" or who believe that ICMP ping is harmless will find themselves sadly mistaken.

</details>

<details><summary><strong>NetSec-Framework</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Josh Ewing](https://img.shields.io/badge/Josh%20Ewing-informational)

🔗 **Link:** [NetSec-Framework](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** NetSec-Framework is a super lightweight Python CLI for performing network auditing tests. The CLI utilizes Arpspoof, Ettercap, sslstrip, tcpdump and Nmap. A user is able to copy/paste this script into any vanilla Debian-based system, install dependencies, configure iptables rules, port forwarding and execute MiTM attacks without leaving the CLI. It also includes an assisted Nmap wrapper for network scanning with an explanation of each scan type. The framework also has features that allow the user to install most Kali Linux tools at the users request in an easy menu based system.The goal was to make network auditing more intuitive for an engineer just getting into security testing and make it easier for those who want to use certain Kali tools on the fly.

</details>

<details><summary><strong>Nishang: The Goodness of Offensive PowerShell</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Nikhil Mittal](https://img.shields.io/badge/Nikhil%20Mittal-informational)

🔗 **Link:** [Nishang: The Goodness of Offensive PowerShell](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** In this presentation, you will see live demonstrations of how PowerShell can be used to execute different attacks. Techniques like advanced client side attacks (UAC avoidance, bypassing firewalls etc), trust abuse of Active Directory and SQL Servers, webshells, white-listing bypass, retrieving system secrets in clear and more will be demonstrated.An updated Black Hat version of Nishang will be released! Come and learn a very interesting vector of attacks.

</details>

<details><summary><strong>ShinoBOT</strong></summary>

![Category: 🔴 Red Teaming](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming-red) ![Shota Shinogi](https://img.shields.io/badge/Shota%20Shinogi-informational)

🔗 **Link:** [ShinoBOT](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/red_team/shinobot.md)  
📝 **Description:** ShinoBOT Suite is a malware/target attack simulator framework for pentest, education. The new version becomes "suiter" than the previous version.It includes those new features, components. You can now test your security performance against ransomware with it. ShinoLocker behaves just like a real ransomware but does not ask for any money to get the crypt key.1) ShinoLocker (Ransomware Simulator)Get the Crypto key from serverScan files to encryptEncrypt -Ask decryption keyDecryptUninstall itself2) ShinoBuilder (Full customization for ShinoBOT)Anti dynamic analysisExtremely Targeted Attack *You can make a malware that works only on your specific environment.C&C URL (for ShinoProxy)Polymorphic function3) ShinoC2 (ShinoBOT's Server)SSL support (Thanks Let's Encrypt Project)DNS TunnelingC2 communication can be done by just DNS4) ShinoStuxnet(tentative)ICS malware simulator.Scan ICS/SCADA system.Talks some ICS protocols.

</details>

---
## 🔍 OSINT
<details><summary><strong>DataSploit</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Sudhanshu Chauhan](https://img.shields.io/badge/Sudhanshu%20Chauhan-informational) ![Shubham Mittal](https://img.shields.io/badge/Shubham%20Mittal-informational) ![Nutan Kumar Panda](https://img.shields.io/badge/Nutan%20Kumar%20Panda-informational)

🔗 **Link:** [DataSploit](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Overview:Performs automated OSINT on a domain / email / username / phone and find out relevant information from different sources.Useful for Pen-testers, Cyber Investigators, Product companies, defensive security professionals, etc.Correlates and collaborate the results, show them in a consolidated manner.Tries to find out credentials, api-keys, tokens, subdomains, domain history, legacy portals, etc. related to the target.Available as single consolidating tool as well as standalone scripts.Available in both GUI and Console."Data! Data! Data! I can't make bricks without clay". This quote by fictional detective Sherlock Holmes certainly suits every InfoSec professional's daily struggle. Irrespective of whether you are attacking a target or defending one, you need to have a clear picture of the threat landscape before you get in. This is where DataSploit comes into the picture. Utilizing various Open Source Intelligence (OSINT) tools and techniques that we have found to be effective, DataSploit brings them all into one place, correlates the raw data captured and gives the user, all the relevant information about the domain / email / phone number / person, etc. It allows you to collect relevant information about a target which can expand your attack/defence surface very quickly. Sometimes it might even pluck the low hanging fruits for you without even touching the target and give you quick wins. Of course, a user can pick a single small job (which do not correlates obviously), or can pick up the parent search which will launch a bunch of queries, call other required scripts recursively, correlate the data and give you all juicy information in one go.Created using our beloved Python, MongoDb and Django, DataSploit simply requires the bare minimum data (such as domain name, email ID, person name, etc.) before it goes out on a mining spree. Once the data is collected, firstly the noise is removed, after which data is correlated and after multiple iterations it is stored locally in a database which could be easily visualised on the UI provided. The sources that have been integrated are all hand picked and are known to be providing reliable information. We have used them previously during different offensive as well as defensive engagements and found them helpful.Worried about setup? Well, there are two major requirements here:1. Setting up the db, django, libraries, etc. We have got a script which will automate this for you, so can just go ahead and shoot the OSINT job.2. Feeding specific API keys for few specific sources. We are going to have a knowledge base where step by step instructions to generate these API keys will be documented. Sweet deal?Apart from this, in order to make it more useful in daily life of a pen-tester, we are working to make the tool as an extension of the other tools that pen-testers commonly use such as Burp Suite, Maltego etc. so that you can feel at home during the usage.

</details>

<details><summary><strong>Enumall - The Ultimate Subdomain Tool</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Jason Haddix](https://img.shields.io/badge/Jason%20Haddix-informational) ![Leif Dreizler](https://img.shields.io/badge/Leif%20Dreizler-informational)

🔗 **Link:** [Enumall - The Ultimate Subdomain Tool](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Enumall leverages the Kali Linux distribution and the wildly popular recon-ng framework to find hidden gems in application assessments, asset discovery work, and OSINT engagements. These gems are acquisitions and subdomains. This isn't just your standard DNS tool. Enumall pulls possible subdomains and acquisitions from Google, Yahoo, Bing, Baidu, Netcraft, Shodan, techcrunch and more! It gives a standard output that inter-operates with several tools (one of which we will be demo'ing is Eyewitness for further detailed discovery!). In addition, Enumall also has the largest and most curated DNS bruteforce list on the internet. Come by and let us show you how you can use Enumall to supercharge your bug hunting and find ripe subdomains and acquisitions!

</details>

<details><summary><strong>Maltego VirusTotal</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Christian Heinrich](https://img.shields.io/badge/Christian%20Heinrich-informational) ![Karl Hiramoto](https://img.shields.io/badge/Karl%20Hiramoto-informational)

🔗 **Link:** [Maltego VirusTotal](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** VirusTotal is a free service that analyzes suspicious files and URLs and facilitates the quick detection of all kinds of malware. Maltego is an open source intelligence and forensics application that offers gathering and mining of VirusTotal's Public API in a easy to understand format.

</details>

<details><summary><strong>pDNSego</strong></summary>

![Category: 🔍 OSINT](https://img.shields.io/badge/Category:%20🔍%20OSINT-lightgrey) ![Christian Heinrich](https://img.shields.io/badge/Christian%20Heinrich-informational) ![Eric Ziegast](https://img.shields.io/badge/Eric%20Ziegast-informational)

🔗 **Link:** Not Available  
📝 **Description:** Passive DNS (pDNS) provides near real-time detection of cache poisoning and fraudulent changes to domains registered for trademarks, etc by answering the following questions: Where did this DNS Record point to in the past? What domains are hosted on a specific nameserver? What domains resolve into a given network? What subdomains exist below a certain domain name? pDNSego is a set of Maltego Transforms that perform link analysis of pDNS datasets based on a Fully Qualified Domain Name (FQDN), IP Address, Name Server (NS) or Mail eXchange (MX) DNS Record.

</details>

---
## ⚙️ Miscellaneous / Lab Tools
<details><summary><strong>Dradis Framework</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [Dradis Framework](https://github.com/etdsoft)  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, Burp and Metasploit. Started in 2007 and with over 2000 code commits the Dradis Framework project has been growing ever since. Dradis is the best tool to consolidate the output of different scanners, add your manual findings and evidence and have all the engagement information in one place.Come to see the latest Dradis release in action. It's loaded with updates including new tool, connectors (Metasploit, Brakeman, ...), full REST API coverage, testing methodologies and lots of interface improvements (issue tagging, UX improvements and much more). Come and find out why Dradis is being downloaded over 300 times every week. This year we will make sure to bring enough stickers for everyone!

</details>

<details><summary><strong>Highway to the Danger Drone</strong></summary>

![Category: ⚙️ Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20⚙️%20Miscellaneous%20/%20Lab%20Tools-gray) ![Francis Brown](https://img.shields.io/badge/Francis%20Brown-informational) ![Dan Petro](https://img.shields.io/badge/Dan%20Petro-informational) ![David Latimer](https://img.shields.io/badge/David%20Latimer-informational)

🔗 **Link:** [Highway to the Danger Drone](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Do you feel the needâ¦ the need for speed? Then check out our brand new penetration testing drone. This Raspberry Pi based copter is both cheap and easy to create on your own, making it the first practical drone solution for your pentesting needs. Drones have emerged as the prevailing weapon of choice in modern warfare, so it's only logical that we'd also explore the potential applications of this formidable tool in cyber warfare. While there have been presentations before on weaponizing drones for the purposes of pentesting, these efforts were not easily replicated by anyone other than experienced drone aficionados with several thousands of dollars to spend â ultimately resulting in somewhat clunky, partial solutions. Conditions have finally matured enough to where pentesters who are inexperienced with drones can get up and running fairly quickly and spending only a couple hundred dollars on a Raspberry Pi based drone copter solution. Our talk will be aimed at this target audience, helping equip pentesters with drone tools of the future.In this talk, we'll demonstrate how this drone can be used to perform aerial recon, attack wireless infrastructure and clients, land on a target facility roof, and serve as a persistent backdoor. In fact, we'll show you how to attack 'over the air' protocols such as RFID, ZigBee, Bluetooth, Wi-Fi, and more. We'll even demo a special edition "RickMote Danger Drone" that you can use to patrol your neighborhood and rickroll Google Chromecast-connected TVs.Additionally, we will showcase the best-of-breed in hardware and software that you'll need. This will include the release of our custom Raspberry Pi SD card image, parts list, 3D print objects, and necessary instructions for you to create a Danger Drone of your own. We'll also be giving away a fully functional Danger Drone to one lucky audience member - guaranteed to leave your friends feeling peanut butter and jealous! This DEMO-rich presentation will benefit both newcomers and seasoned professionals of drone and physical penetration testing fields. Someone better call Kenny Loggins, because you're in the Danger Drone.â¦No, no boys, there's two 'O's in Bishop Fox.

</details>

---
## 🔴 Red Teaming / AppSec
<details><summary><strong>Faraday</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Federico Kirschbaum](https://img.shields.io/badge/Federico%20Kirschbaum-informational)

🔗 **Link:** [Faraday](https://github.com/fedek)  
📝 **Description:** Since collaborative pentesting is more common each day and teams become larger, sharing the information between pentesters can become a difficult task. Different tools, different formats, long outputs (in the case of having to audit a large network) can make it almost impossible. You may end up with wasted efforts, duplicated tasks, a lot of text files scrambled in your working directory. And then, you need to collect that same information from your teammates and write a report for your client, trying to be as clear as possible.The idea behind Faraday is to help you to share all the information that is generated during the pentest, without changing the way you work. You run a command, or import a report, and Faraday will normalize the results and share that with the rest of the team in real time. Faraday has more than 50 plugins available (and counting), including a lot of common tools. And if you use a tool for which Faraday doesn't have a plugin, you can create your own. During this presentation we're going release Faraday v2.0.0 with all the new features that we were working on for the last couple of months.

</details>

<details><summary><strong>Scout2</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Loic Simon](https://img.shields.io/badge/Loic%20Simon-informational)

🔗 **Link:** [Scout2](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)  
📝 **Description:** Scout2 is an open source tool that helps when assessing the security posture of AWS environments. This tool uses the AWS API to fetch configuration data for various Amazon services, including IAM, EC2, S3, RDS and CloudTrail. The gathered configuration is analyzed for known configuration weaknesses, then made available via an offline HTML report. The report provides security-oriented views of the AWS resources that were analyzed, as well as a list of security risks that were identified.Since its initial launch over two years ago, Scout2 doubled the number of services in scope and built-in security checks. If you worry that access to your AWS account -- and the resources it holds -- may not be secure enough, stop by and learn how you can easily identify security gaps. The presenter will demo multiple use cases, including use and comparison of various rulesets, customization of a ruleset, and creation of a new rule.

</details>

<details><summary><strong>ThreadFix</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Dan Cornell](https://img.shields.io/badge/Dan%20Cornell-informational)

🔗 **Link:** [ThreadFix](https://github.com/dancornell)  
📝 **Description:** ThreadFix is an application vulnerability management platform that helps automate many common application security tasks and integrate security and development tools. It allows organizations to create a consolidated view of their applications and vulnerabilities, prioritize application risk decisions based on data, and translate vulnerabilities to developers in the tools they are already using.

</details>

<details><summary><strong>Voyeur</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Juan Garrido](https://img.shields.io/badge/Juan%20Garrido-informational)

🔗 **Link:** [Voyeur](https://github.com/silverhack/voyeur/blob/master/Common/Vars.ps1)  
📝 **Description:** VOYEUR's main purpose is to automate several tasks of an Active Directory build review or security assessment. Also, the tool is able to create a fast (and pretty) Active Directory report. The tool is developed entirely in PowerShell (a powerful scripting language) without dependencies like Microsoft Remote Administration tools. (Just .Net Framework 4.0 and Office Excel if you want a useful and pretty report). The generated report is a perfect starting point for well-established forensic, incident response team, security consultants or security researchers who want to quickly analyze threats in Active Directory Services.Main FeaturesReturn a huge number of attributes on computers, users, containers/OUs, groups, ACL, etc...Search for locked accounts, expired password, no password policy, etc...Return a list of all privileged account in domain. (The script search in SID value instead in a group name)Return a list of group's modification (Users added/deleted for a specific group, etc...)Multi-Threading supportPlugin SupportUsage scenariosAble for using on local or remote computerAble for using on joined machine or workgroup machineReportingSupport for exporting data driven to several formats like CSV, XML or JSON.Office SupportSupport for exporting data driven to EXCEL format. The script also support table style modification, chart creation, company logo or independent language support. At the moment only Office Excel 2010 and Office Excel 2013 are supported by the tool.

</details>

<details><summary><strong>Vulnreport - Pentesting Management and Automation</strong></summary>

![Category: 🔴 Red Teaming / AppSec](https://img.shields.io/badge/Category:%20🔴%20Red%20Teaming%20/%20AppSec-red) ![Tim Bach](https://img.shields.io/badge/Tim%20Bach-informational)

🔗 **Link:** [Vulnreport - Pentesting Management and Automation](https://github.com/salesforce/vulnreport/blob/master/app.json)  
📝 **Description:** Vulnreport is designed to accelerate management of penetration tests and security code reviews/audits, as well as generation of useful vulnerability reports. Using Vulnreport, security researchers can automate almost all of the overhead involved with penetration testing so that they can devote more time to the fun stuff - finding vulns. Vulnreport takes care of tracking vulnerabilities on your tests, providing a simple UI for managing them, and running analytics on what you're finding and where you're spending your time.Vulnreport is also a platform that can be extended and hooked into whatever other management and vulnerability assessment tools are part of your process. Hook it up to your automated testing frameworks and watch the vuln data flow into your reports like magic.This demo will walk through the upsides of automating this part of your pentesting process as well as show how the Salesforce Product Security team uses Vulnreport to save hundreds of engineer-hours per year. We will be open-sourcing and making the tool available for you and your teams to use, customize, and contribute to during the conference.

</details>

---