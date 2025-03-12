## Comprehensive Summary of Network Security Class

**Subject:** Network Security (CS 6, 8, 2, 3)
**Instructor:** Professor Philip Mack
**Date:** March 3rd, 2025 (Week 6)

**Learning Objectives:** This class aimed to deepen students' understanding of network security threats and defense mechanisms, focusing on DDoS attacks, DNS vulnerabilities, and malware persistence. The instructor employed a combination of lectures, real-world examples, interactive discussions, and practical exercises to achieve these objectives.

**Overview of Topics Covered:** The class covered several critical network security topics, including DDoS attacks (specifically DNS amplification/reflection and NTP amplification), DNS functioning and vulnerabilities (including DNS cache poisoning), malware persistence techniques, covert channels (with a focus on Covert TCP), and reverse shells. These topics are highly relevant in today's interconnected world, where network security breaches pose significant threats to individuals and organizations.

### Key Topics:

**1. DDoS Attacks:**

* **Subtopic 1: DNS Amplification/Reflection Attack:** This attack leverages the DNS protocol's inherent characteristics to overwhelm a victim with amplified traffic.
    * **Mechanism:** The attacker sends a small DNS query (e.g., for a TXT record) to numerous public DNS servers, spoofing the victim's IP address as the source. The DNS servers then send large responses to the victim, amplifying the attacker's initial query.
    * **Amplification Factor:** The amplification factor is the ratio of the response size to the query size.  For TXT record queries, this can be significant (e.g., a 60-byte query eliciting a 512-byte response).
    * **Reflection:** The attack is termed "reflection" because the DNS servers unwittingly become accomplices in the attack, reflecting the amplified traffic towards the victim.
    * **Real-world Impact:**  DNS amplification attacks are among the most common and potent DDoS attack vectors.
    * **Mitigation:**  DDoS protection services (e.g., Cloudflare, Akamai) are typically required to mitigate these attacks, as they can handle the massive bandwidth involved and filter malicious traffic.

* **Subtopic 2: NTP Amplification Attack:**  Similar to DNS amplification, this attack exploits the Network Time Protocol (NTP).
    * **Mechanism:** Attackers send small NTP requests to vulnerable NTP servers, spoofing the victim's IP address. The servers then respond with much larger time synchronization data, flooding the victim.
    * **Amplification Factor:** NTP amplification can be even greater than DNS amplification (e.g., a 48-byte request resulting in a 48kB response).
    * **Real-world Impact:**  NTP amplification attacks have been responsible for significant DDoS incidents.
    * **Mitigation:** Similar to DNS amplification, DDoS protection services are crucial for mitigation.

**2. DNS Functioning and Vulnerabilities:**

* **Subtopic 1: DNS Resolution Process:** The instructor detailed the recursive nature of DNS resolution, involving queries to root servers, top-level domain (TLD) servers, and authoritative name servers. Caching at each level was explained to highlight performance optimization. The instructor also mentioned the role of home routers in the process.
    * **Visual Aid:** A diagram illustrating the DNS resolution process was used, showing the flow of queries and responses between the user's computer, router, ISP's DNS server, root servers, TLD servers, and authoritative name servers.
* **Subtopic 2: DNS Cache Poisoning:** This attack involves injecting false information into a DNS server's cache.
    * **Mechanism:** The attacker intercepts or spoofs a DNS response, providing a fake IP address for a specific domain. Subsequent queries to the poisoned DNS server will direct users to the attacker's server.
    * **Impact:** Depending on which step in the resolution process is poisoned, the attack can affect a single user or a large number of users relying on the same DNS server.
    * **Example:** The instructor presented scenarios where different steps in the DNS resolution process were poisoned, illustrating the varying impact.
    * **Conditions for Successful Poisoning:** The attacker must respond faster than the legitimate DNS server, spoof the correct IP address, and use the correct transaction ID and port number.
    * **Mitigation:** DNSSEC (DNS Security Extensions) and DNS over HTTPS (DoH) or DNS over TLS (DoT) are emerging technologies to enhance DNS security. VPNs can also help protect against DNS cache poisoning by routing DNS queries through the VPN tunnel.

**3. Malware Persistence:**

* **Definition:**  Persistence refers to malware's ability to remain on a system even after a reboot or other attempts to remove it.
* **Techniques:**
    * **Startup Services:** Malware can add itself to the operating system's startup services (e.g., via registry keys in Windows).
    * **Hidden Partitions/MBR Infection:** Malware can hide in hidden partitions or infect the Master Boot Record (MBR), surviving operating system reinstallation.
    * **BIOS/Firmware Infection:** In some cases, malware can infect the BIOS or firmware, making it extremely difficult to remove.
    * **External Devices:** Malware can reside on external devices like USB drives, re-infecting the system when the device is plugged in.
* **Example:** The instructor used the example of Lab 1, Task 4, where students established a reverse shell, and explained how attackers would aim for persistence after gaining access.

**4. Covert Channels:**

* **Definition:** A covert channel is a communication pathway hidden within another channel, often used to transmit data secretly.
* **Example: Covert TCP:** This program allows hiding data within IP and TCP packets.
    * **IP ID Method:** Hiding data in the IP Identification field.
    * **Sequence Number Method:** Hiding data in the TCP Sequence Number field.
    * **Acknowledgment Number Method:** Hiding data in the TCP Acknowledgment Number field, involving a third party (innocent bystander).  The instructor provided a detailed explanation of this method using a diagram.
* **Other Hiding Places:** The instructor discussed other potential locations within the TCP header for hiding data, such as the reserved bits and the source port, while acknowledging the checksum is often not checked anymore due to NAT.

**5. Reverse Shells:**

* **Definition:** A reverse shell is a technique where the compromised machine initiates a connection back to the attacker's machine.
* **Popularity:** Reverse shells are favored by attackers because they bypass firewalls that typically allow outbound connections.
* **Example:**  The instructor referenced Lab 1, Task 4, where students created a reverse shell.


### Exercises & Discussions:

* **Exercise 1:**  Tracing the steps of a DNS request for www.newyorktimes.com, assuming no prior internet activity.
* **Exercise 2:**  Analyzing an Nmap command (`nmap -sS -O 10.10.10.10`) to determine the type of scan (TCP SYN scan), ports scanned (top 1000), and additional features (OS detection). The instructor emphasized the importance of specifying port ranges in Nmap scans.
* **Exercise 3:**  Discussing how malware can survive an operating system wipe, including BIOS/firmware infection, hidden partitions, MBR infection, and infection of other network devices.
* **Exercise 4:**  Brainstorming reasons why attackers maintain persistence on a compromised host, including botnet activity, espionage, using the host as a proxy, pivoting to other hosts on the network, and data exfiltration.
* **Exercise 5:**  Explaining the three methods of Covert TCP and identifying three alternative places to hide data within the TCP header.


### Important Announcements:

* **Midterm Exam:** Scheduled for next Saturday, March 15th.  Covers all material up to and including this week's class. Open book and open internet, but no collaboration or AI usage allowed. Sample midterms will be provided.
* **Midterm Review Class:** Scheduled for next Monday. Students are encouraged to complete all assignments and readings before the review.
* **Assignments:** Lab 2 was due yesterday. Homework 2 (on cryptography, related to Lesson 5) is due next Thursday, March 14th.  Lesson 5 (asynchronous video on cryptography) has been released.
* **TA Office Hours:** Tentatively scheduled for Tuesday at 6 PM or 8 PM, with another session later in the week.
* **Additional Resources:** Lesson 3 supplemental video on Nessus and Metasploit, weekly note slides on Brightspace.


### Final Takeaways:

* Understanding DDoS attacks, DNS vulnerabilities, and malware persistence techniques is crucial for network security.
* Practical tools like Nmap and techniques like covert channels play significant roles in both attack and defense.
* Maintaining good security practices, such as using VPNs and keeping software updated, is essential for mitigating risks.

**Follow-up Actions:**

* Review the assigned readings and videos.
* Complete Homework 2 and any outstanding labs.
* Prepare questions for the midterm review class.

**Motivational Note:** The knowledge and skills gained in this class are invaluable in today's digital landscape. By understanding the tactics and techniques used by attackers, you are better equipped to defend against them and contribute to a more secure online environment.  Keep exploring and learning!