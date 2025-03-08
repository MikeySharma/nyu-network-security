## CS 6823: Network Security - Class Summary

**Instructor:** Professor Philip Mack
**Date:** Monday, February 24th, 2025
**Week:** 5

**Learning Objectives:** This class aimed to deepen students' understanding of network reconnaissance, focusing on the practical limitations of UDP scanning, alternative scanning methods, and the importance of secure configuration. It then transitioned to exploring various attack techniques, including IP spoofing, session hijacking, and denial-of-service attacks, emphasizing real-world implications and mitigation strategies.

**Teaching Approach:** Professor Mack employed a highly interactive approach, using real-world examples from his experience, engaging students in problem-solving exercises, and encouraging active participation through questions and discussions. He connected theoretical concepts to practical applications, emphasizing the importance of security best practices.

**Topics Covered:**

* **Review of UDP Scanning:**  Limitations and practical implications.
* **Alternative Scanning Methods:** Agent-based scanning, FTP bounce scan, idle scan (briefly mentioned).
* **Nmap Commands and Usage:**  Version scanning, OS fingerprinting, port specification.
* **Firewalk:** Traceroute with application data.
* **Zap (Z Attack Proxy):** Web application scanning and proxy functionality.
* **Attacks, Vulnerabilities, and Exploits:** Sources of vulnerabilities and common attack techniques.
* **IP Address Spoofing and Ingress Filtering:**  Challenges in preventing IP spoofing.
* **Session Hijacking:**  Methods and countermeasures.
* **Denial-of-Service (DoS) Attacks:** Various types, including sync flood and fragmentation attacks.
* **Mitigation Techniques:** Sync cookies, connection cache, dynamic ARP inspection.


### Key Topics Breakdown:

**1. Review of UDP Scanning:**

* **Three Possible Responses:**
    * **Response:** Port is open.
    * **ICMP Destination Unreachable:** Port is closed.
    * **No Response:** Several possibilities including firewall, network error, malformed packet, wrong service, or ICMP rate limiting.
* **ICMP Rate Limiting:**  UDP scanning is slow due to ICMP destination unreachable messages being limited to one per second (Linux) or two per second (Windows). This limitation exists to mitigate DDoS attacks leveraging ICMP.
* **Practical Implications:** Full UDP scans on all 65,535 ports are impractical, taking a minimum of 18 hours.  This leads to many UDP ports being routinely unscanned, making them attractive for malware.

**2. Alternative Scanning Methods:**

* **Remote Scanning (Traditional):** Scanning from outside the target network.  Suffers from limitations, especially with UDP.
* **Agent-Based Scanning:** Scanning from inside the target host using an installed agent.  Significantly faster and more accurate but more expensive (approximately 10x the cost).  Vendors like Nessus and Qualys offer agent-based scanning solutions.
* **FTP Bounce Scan:**  Leverages anonymous FTP servers to obfuscate the attacker's origin. Nmap logs into the FTP server and initiates connections to the target from there.
* **Idle Scan:**  Briefly mentioned but not covered in detail.

**3. Nmap Commands and Usage:**

* `-sV`: Version scanning (identifies software versions).
* `-O`: Operating system fingerprinting.
* `--top-ports <number>`: Scans the specified number of most common ports.
* `-T4`: Sets the timing template for faster scanning.
* `-oA <filename>`: Output results to a file in all formats.
* **Default Port Scanning:** Nmap scans the top 1000 most common ports if no specific ports are provided.

**4. Firewalk:**

* A tool that performs traceroute using any application protocol (not just ICMP).
* Useful for bypassing firewalls that block ICMP traceroute.

**5. Zap (Z Attack Proxy):**

* A free web application scanner and proxy.
* Intercepts traffic between browser and web server, allowing manipulation and analysis.
* Can perform basic vulnerability scanning and automated testing.

**6. Attacks, Vulnerabilities, and Exploits:**

* **Sources of Vulnerabilities:**
    * Design flaws
    * Implementation errors (e.g., buffer overflows, SQL injection)
    * Architecture issues
    * Configuration errors
    * Supply chain vulnerabilities (e.g., Log4j)
    * Mindset/culture (e.g., not adhering to least privilege)
    * People (e.g., susceptibility to phishing)
    * Standards/requirements (e.g., backwards compatibility)
* **Importance of Secure Configuration:**  Using standard configuration guides (STIGs, SRGs) is crucial for secure installation and ongoing maintenance.

**7. IP Address Spoofing and Ingress Filtering:**

* **IP Spoofing:**  Easy to perform but responses go to the spoofed address, not the attacker.
* **Ingress Filtering:**  Blocking traffic with spoofed source IP addresses that should not originate from the claimed network.
* **Implementation Challenges:** Ingress filtering is effectively implemented by Tier 1 ISPs but not by regional ISPs due to dynamic IP addressing and customer service concerns.

**8. Session Hijacking:**

* Taking over an existing TCP connection by predicting the sequence and acknowledgment numbers.
* **Limitations:** Typically allows only one command before resynchronization breaks the connection.
* **Countermeasures:** Resynchronization mechanisms in TCP.

**9. Denial-of-Service (DoS) Attacks:**

* **Sync Flood:** Flooding the target with TCP SYN packets, exhausting resources.
* **Fragmentation Attacks:** Exploiting vulnerabilities in IP fragmentation reassembly (e.g., Teardrop, Bonk).
* **Bandwidth Flooding:** Consuming all available bandwidth.

**10. Mitigation Techniques:**

* **Sync Cookies:**  A server-side defense against sync flood attacks.  The server embeds a cryptographic cookie in the SYN-ACK packet and only allocates resources upon receiving a valid ACK containing the cookie.
* **Connection Cache:** Reserving a portion of available sockets for established connections.
* **Dynamic ARP Inspection:** A security feature on managed network devices that prevents ARP cache poisoning by validating ARP packets.


### Exercises & Discussions:

* **Exercise 1:** Explain Nmap scan types (connect, SYN, FIN, NULL, Xmas, ACK).
    * **Connect Scan:**  Completes the three-way handshake, slower.
    * **SYN Scan (Stealth Scan):** Sends SYN, waits for SYN-ACK or RST, faster.
    * **FIN, NULL, Xmas Scans:** Used for OS fingerprinting.
    * **ACK Scan:**  Used to detect stateful firewalls and filtered ports.

* **Exercise 2:** How to establish command and control after session hijacking (limited to one command)?
    * **Reverse Shell:**  Instruct the target to open a connection back to the attacker.
    * **Malware Installation:**  Deploy malware that opens a listening port.
    * **Attacker-in-the-Middle (AiTM):**  Take the original client offline (e.g., ARP cache poisoning, DDoS) and impersonate them.

* **Exercise 3:** Two methods to mitigate sync flood attacks (used in Lab 1).
    * **Sync Cookies.**
    * **Connection Cache.**

* **Exercise 4:** Name and describe a DDoS attack besides sync flood.
    * Students provided various examples (bandwidth flooding, UDP flood, etc.).


### Important Announcements:

* **Lab 2 Due:** Sunday, March 2nd.
* **5% Bonus:** For submitting Lab 2 by Tuesday, February 25th.
* **5% Extra Credit:** For completing the ARP cache poisoning portion of Lab 2.
* **TA Office Hours:** Tuesday at 8 PM and another session later in the week (TBA).


### Final Takeaways:

* UDP scanning is slow and often incomplete due to ICMP rate limiting.
* Agent-based scanning is superior but expensive.
* Secure configuration is paramount and should always follow established guidelines.
* IP spoofing remains a challenge due to inconsistent ingress filtering.
* Session hijacking can be mitigated by resynchronization and AiTM countermeasures.
* DDoS attacks are a significant threat, and understanding mitigation techniques is crucial.


### Follow-up Actions:

* Review the provided resources on IP headers, TCP flags, and Nmap scan types.
* Explore the Nessus and Qualys websites to learn more about agent-based scanning.
* Research and compare different types of DDoS attacks and their mitigation strategies.


### Motivational Note:

The landscape of network security is constantly evolving. By staying informed about the latest attack techniques and mitigation strategies, you can better protect yourself and your organization from emerging threats.  Continue to explore and experiment, and never stop learning!