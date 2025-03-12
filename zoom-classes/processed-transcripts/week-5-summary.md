## Cs. 6,823 Network Security Class Summary

**Instructor:** Professor Philip Mack

**Date:** Monday, February 24th, 2025 (Week 5)

**Learning Objectives:**

* Deepen understanding of network reconnaissance techniques, focusing on UDP scanning limitations and alternatives.
* Explore various attack strategies, including IP spoofing, session hijacking, and denial-of-service techniques.
* Understand the importance of secure configuration practices and the use of configuration guides.
* Analyze the complexities of IP fragmentation and related vulnerabilities.
* Learn mitigation strategies against SYN flood attacks.

**Instructor's Teaching Approach:** Professor Mack employed a highly interactive approach, incorporating real-world examples, case studies, student exercises, and open discussions to facilitate a comprehensive understanding of the topics.  He frequently asked questions to encourage critical thinking and engagement.

**Overview of Topics Covered:**

This class revisited network reconnaissance, specifically UDP scanning challenges, and then delved into various attack vectors, mitigation strategies, and the crucial role of secure system configuration. The topics are highly relevant to understanding modern network security threats and developing effective defense mechanisms.


## Key Topics

### 1. Network Reconnaissance: UDP Scanning

* **UDP Scanning Responses:**  Three possible responses to a UDP scan were reviewed:
    * **Open Port:** A response indicates an open port (e.g., DNS response on port 53).
    * **Closed Port:** An ICMP Destination Unreachable message signifies a closed port.
    * **No Response:**  Ambiguous, indicating a firewall, network error, improperly formatted packet, or wrong service probed (e.g., sending a DNS packet to an SNMP port).  Also can indicate reaching the ICMP destination unreachable limit.

* **ICMP Destination Unreachable Limit:**  Limited to one per second (Linux) or two per second (Windows) to mitigate DDoS attacks.  This limit significantly impacts UDP scanning speed.  The rationale behind this limit was explained through a DDoS attack scenario where an attacker sends a broadcast request and spoofs the source IP, flooding the victim with ICMP Destination Unreachable responses.

* **UDP Scanning Challenges:** The ICMP rate limit makes full UDP scans (65,535 ports) extremely slow (minimum 18 hours).  Consequently, many scanners only check the top 1,000 UDP ports by default.  This leaves high-numbered UDP ports less scrutinized, making them attractive for malware.

* **Remote vs. Agent-Based Scanning:** Two scanning approaches were contrasted:
    * **Remote Scanning:** Traditional method, scanning from outside the target.  Slow for UDP, but cheaper.
    * **Agent-Based Scanning:**  Scanning from inside the host using an agent (e.g., Nessus, Qualys).  Faster and more accurate, but significantly more expensive (approximately 10x).  The instructor recommended exploring NYU's Cyber Badges program for free training on these tools.

* **TCP Scanning Review:** Four possible TCP scan responses were briefly reviewed (open, closed, ICMP Destination Unreachable, no response).

* **FTP Bounce Scan:**  Nmap technique to scan a target indirectly through an anonymous FTP server.  This obscures the attacker's origin.  A diagram illustrating this process was shown.

* **IP Header:**  Students were encouraged to familiarize themselves with the IP header fields (source/destination IP, etc.) using resources like Wikipedia.

* **Nmap Commands:** Several Nmap commands were discussed:
    * `-sV`: Version scanning (identifies software versions).
    * `-O`: Operating system fingerprinting.
    * `--top-ports`: Scans the most common ports.
    * `-T4`: Sets the scanning speed.
    * `-oA`: Specifies the output file.

* **Nmap Default Ports:**  Nmap scans the top 1,000 most common ports by default if no ports are specified, although the exact list is not readily available.  The instructor emphasized the importance of explicitly defining ports for accurate scanning.

* **Firewalk:** A tool that performs traceroute with application data, effectively using any TCP/UDP port for the traceroute. This can be useful for bypassing firewalls that block ICMP traceroutes.  It was noted that Linux uses UDP for traceroute by default.

* **ZAP (Zed Attack Proxy):** A free web application security scanner and proxy that intercepts traffic between browser and server, allowing manipulation and vulnerability analysis.  Burp Suite was mentioned as a commercial alternative.


### 2. Attacks, Vulnerabilities, and Exploits

* **Cyber Kill Chain:**  The class focused on the exploitation phase of the cyber kill chain.

* **Sources of Vulnerabilities:**  An interactive discussion explored various vulnerability sources:
    * **Design:**  Architectural flaws.
    * **Implementation:**  Coding errors (e.g., buffer overflows, SQL injection).
    * **Configuration:** Misconfigurations (e.g., weak passwords, unnecessary services).  STIGs (Standard Technical Implementation Guides) and SRGs (Security Requirements Guides) were emphasized as crucial resources for secure configuration.
    * **Supply Chain:** Vulnerabilities introduced through third-party components (e.g., Log4j).
    * **Mindset/Culture:**  Poor security practices (e.g., excessive admin privileges).
    * **People:**  Susceptibility to social engineering (e.g., phishing).
    * **Standards/Requirements:**  Vulnerabilities arising from backwards compatibility or proprietary standards.

* **IP Address Spoofing:**  Spoofing the source IP address is easy (demonstrated in labs), but responses go to the real IP.  Mitigation techniques were discussed:
    * **Egress Filtering:** Blocking spoofed traffic leaving a network (rarely implemented).
    * **Ingress Filtering:** Blocking spoofed traffic entering a network (more common, implemented by Tier 1 ISPs but not regional ISPs due to complexities with dynamic IP addresses and customer service concerns).  A diagram illustrated how ingress filtering works and its limitations.

* **Session Hijacking:**  Taking over an existing TCP connection by guessing the sequence and acknowledgment numbers.  Only works once due to resynchronization attempts.  Wireshark can reveal session hijacking attempts through red and black lines indicating failed resynchronization.

* **Maintaining Command and Control (Post-Hijacking):** Several techniques were discussed to maintain command and control after a successful session hijack:
    * **Reverse Shell:**  Establish a connection back to the attacker (as done in Lab 4 using Netcat).
    * **Malware Installation:**  Install malware that opens a port for the attacker.
    * **Attacker-in-the-Middle (AitM):**  Disrupt communication between client and server (e.g., using ARP cache poisoning) to intercept and manipulate traffic.


### 3. Denial of Service (DoS) Attacks

* **Fragmentation Attacks:** Exploiting the complexity of IP fragmentation.  Several examples were given:
    * **Ping of Death:**  Oversized ping packets crashing systems.
    * **Teardrop/NewTear/Bonk/SynDrop:**  Manipulating fragment offsets and flags to cause crashes.

* **SYN Flood:**  Flooding the target with TCP SYN packets to exhaust resources.  Mitigation techniques:
    * **SYN Cookies:**  Encoding connection information in the initial sequence number.  Reduces resource consumption during the handshake.
    * **Connection Cache:**  Reserving a portion of sockets for established connections.


## Exercises & Discussions

* **Exercise 1:** Explain Nmap scan types (connect, SYN, FIN, NULL, Xmas, ACK).
* **Exercise 2:** How to establish command and control after a one-time session hijack.
* **Exercise 3:**  Two methods to mitigate SYN flood attacks (SYN cookies, connection cache).
* **Exercise 4:** Name and describe a DDoS attack besides SYN flood.

**Common Mistakes/Challenges:** Students initially struggled with the nuances of UDP scanning and the implications of the ICMP rate limit.  Understanding the complexities of IP fragmentation also presented a challenge.

**Solutions and Explanations:**  Professor Mack provided detailed explanations and diagrams to clarify the concepts, addressing student questions and highlighting the reasoning behind each step in the exercises.


## Important Announcements

* **Lab 2 Due Date:** Sunday, March 2nd.
* **Bonus:** 5% for submitting Lab 2 by Tuesday, February 25th.
* **Extra Credit:** 5% for implementing ARP cache poisoning in Lab 2.
* **TA Office Hours:** Tuesday at 8 PM and another session later in the week (TBA).
* **Supplemental Video:** Metasploit and Nessus scanning (already posted).


## Final Takeaways

* UDP scanning is significantly slower than TCP scanning due to ICMP rate limits.
* Agent-based scanning offers better visibility but comes at a higher cost.
* Secure system configuration is paramount and requires adherence to established guidelines (STIGs/SRGs).
* IP fragmentation is a complex process susceptible to various attacks.
* SYN flood attacks can be mitigated using SYN cookies and connection caching.

**Follow-up Actions:**

* Review IP header structure on Wikipedia.
* Explore NYU Cyber Badges program for Nessus/Qualys training.
* Research different types of DDoS attacks.
* Practice Nmap commands and analyze scan results.

**Motivational Note:** Understanding the techniques used by attackers is crucial for building robust defenses.  By actively engaging with the material and practicing the concepts learned in class, you can enhance your network security skills and contribute to a safer online environment.