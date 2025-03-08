## Comprehensive Summary of Network Security Class (Week 6)

**Subject:** Network Security (CS 6, 8, 2, 3)
**Instructor:** Professor Philip Mack
**Date:** March 3rd, 2025 (Week 6)

**Learning Objectives:** This week's class aimed to deepen students' understanding of Distributed Denial of Service (DDoS) attacks, Domain Name System (DNS) security vulnerabilities, and malware persistence techniques. The instructor employed a combination of lectures, real-world examples, diagrams, and interactive exercises to facilitate learning.

**Topics Covered:**

* **Distributed Denial of Service (DDoS) Attacks:** Focusing on DNS amplification/reflection attacks and NTP amplification attacks.
* **Domain Name System (DNS) Security:** Exploring DNS vulnerabilities and cache poisoning.
* **Malware Persistence:** Examining techniques attackers use to maintain access to compromised systems.
* **Covert Channels and Steganography:**  Introducing methods for hiding data within network traffic, specifically focusing on Covert TCP.


**Key Topics Breakdown:**

### 1. Distributed Denial of Service (DDoS) Attacks

* **Subtopic 1.1: DNS Amplification/Reflection Attacks:** This attack exploits the DNS protocol to amplify traffic directed at a victim.  The attacker sends DNS queries to open DNS resolvers, spoofing the source IP address as the victim's. The resolvers then send large responses to the victim, overwhelming their network.
    * **Real-world example:** TXT records, which can be up to 512 bytes, are often used in these attacks.  The attacker sends a small query (e.g., 60-80 bytes) to numerous DNS resolvers, resulting in a much larger response directed at the victim.
    * **Diagram:** The instructor used a diagram illustrating the attacker, DNS resolvers, and the victim, showing the flow of small queries and amplified responses.
    * **Mitigation:** The instructor emphasized that DDoS protection services (e.g., Cloudflare, Akamai) are often the only effective defense against these bandwidth attacks.

* **Subtopic 1.2: NTP Amplification Attacks:** Similar to DNS amplification, this attack leverages the Network Time Protocol (NTP). Small requests to NTP servers trigger much larger responses, which are then directed at the victim.
    * **Example:**  A 48-byte NTP request can elicit a 48KB response.
    * **Mitigation:**  Similar to DNS amplification attacks, DDoS protection services are crucial.


### 2. Domain Name System (DNS) Security

* **Subtopic 2.1: How DNS Works:** The instructor detailed the recursive nature of DNS resolution, explaining how a client's request traverses from local DNS servers to root servers and various namespaces.
    * **Diagram:** A diagram illustrated the DNS hierarchy and the flow of queries and responses.
    * **Concept: Caching:** The instructor explained how DNS servers cache responses to improve performance, which can be exploited in cache poisoning attacks.

* **Subtopic 2.2: DNS Cache Poisoning:**  This attack involves injecting false information into a DNS server's cache.  Subsequent queries for the poisoned domain will return the incorrect information, directing users to malicious websites.
    * **Scenarios:** The instructor presented several scenarios involving poisoning at different stages of the DNS resolution process, highlighting the increasing impact of poisoning higher-level caches.
    * **Example:** Attacker on a local network (e.g., Starbucks Wi-Fi) can easily poison the cache for a single user or even for all users of a particular DNS server.
    * **Conditions for Cache Poisoning:**
        1. **Speed:** Attacker's response must arrive before the legitimate response.
        2. **Spoofing:** Attacker must spoof the IP address of the authoritative DNS server.
        3. **Matching:** Attacker must match the transaction ID and port number of the original query.


### 3. Malware Persistence

* **Definition:**  Techniques used by attackers to maintain access to a compromised system even after a reboot or other disruptive event.
* **Techniques:**
    * **Registry Keys (Windows):** Adding malware to startup services.
    * **Startup Services (Mac OS X, Linux):** Similar mechanisms exist on other operating systems.
    * **Trojan Horses:** Malware disguised as legitimate software.
    * **Rootkits:** Malware designed to evade forensic analysis (user-mode and kernel-mode).
    * **Hidden Partitions:** Storing malware on a hidden partition.
    * **MBR Infection:** Infecting the Master Boot Record to ensure persistence.
    * **Bios Infection:** Infecting the BIOS, surviving OS reinstalls.
    * **Firmware Overwriting:** Modifying firmware to maintain persistence.
    * **External Devices:** Hiding malware on USB drives or external hard drives.
    * **Compromising other network devices:** Jumping back into the target system from another infected device.


### 4. Covert Channels and Steganography

* **Covert Channels:** A communication channel hidden within another channel.
* **Steganography:** The art and science of hiding messages within other data.
* **Covert TCP:** A program that hides data within IP and TCP packets.
    * **Methods:**
        1. **IP ID Method:** Hiding data in the IP Identification field (16 bits).
        2. **Sequence Number Method:** Hiding data in the TCP sequence number (32 bits).
        3. **ACK Number Method:** Hiding data in the TCP acknowledgment number, involving a third-party "innocent bystander" (32 bits).
            * **Diagram:** The instructor used a diagram illustrating the three-host setup and the flow of packets in the ACK number method.
* **Other Hiding Places in TCP Header:** The instructor discussed other potential locations for hiding data, such as the reserved bits and source port, while acknowledging that some fields (like the window size) are critical for proper TCP operation.



**Exercises & Discussions:**

* **Exercise 1:** Tracing the steps of a DNS request, considering an empty cache scenario.
* **Exercise 2:** Analyzing an Nmap command (`nmap -sS -O 10.10.10.10`) to determine the type of scan (TCP SYN scan), target ports (top 1000 common ports), and additional functionality (OS detection).
* **Exercise 3:** Brainstorming ways malware can survive an operating system wipe.
* **Exercise 4:**  Discussing reasons why attackers maintain persistence on compromised hosts.
* **Exercise 5:** Explaining the three functions of Covert TCP and identifying other potential data hiding places within the TCP header.
* **Exercise 6:** This exercise was cancelled by the instructor.


**Important Announcements:**

* **Midterm Exam:**
    * Date: March 15th (next Saturday)
    * Topics: All material covered up to and including this week's class (Lessons 1-5, Homeworks 1-2, Labs 1-2).
    * Format: Open book, open internet, but no collaboration and no AI tools allowed.
    * Sample midterms will be released the following day.
* **Midterm Review Class:** Next Monday. Students are encouraged to complete all assignments and readings before the review class.
* **Lab 2:** Due yesterday (March 2nd).
* **Lesson 3 Supplemental Video:**  Covers Nessus and Metasploit. Students should watch this video.
* **Lesson 5:** Asynchronous video on cryptography (released today).  Related to Homework 2.
* **Homework 2:** Due next Thursday, March 14th. Covers cryptography.
* **TA Office Hours:**  Tomorrow (Tuesday) at either 6 PM or 8 PM. Another session later in the week (TBA).


**Final Takeaways:**

* DDoS attacks, particularly those leveraging DNS and NTP amplification, pose a significant threat.  Understanding their mechanics and mitigation strategies is crucial.
* DNS is a fundamental internet protocol with inherent security vulnerabilities.  Cache poisoning can have widespread consequences.
* Malware employs various persistence techniques to maintain access to compromised systems.  Recognizing these techniques is essential for effective incident response.
* Covert channels and steganography enable hidden communication. Understanding these methods helps identify and prevent data exfiltration.

**Follow-up Actions:**

* Review the lesson materials, especially the diagrams and examples.
* Complete Homework 2 and watch the Lesson 3 supplemental video.
* Prepare questions for the midterm review class.
* Explore additional resources on DNS security, DDoS mitigation, and malware analysis.

**Motivational Note:**  Network security is a constantly evolving field. By staying informed and practicing the concepts learned in this class, you can contribute to a safer and more secure online environment.  Don't be discouraged by the complexity of these attacks; with knowledge and diligence, you can effectively defend against them.