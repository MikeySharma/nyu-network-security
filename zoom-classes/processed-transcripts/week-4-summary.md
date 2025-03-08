## CS 6.823 Network Security Class Summary - Week 4

**Instructor:** Professor Philip Mack
**Date:** Tuesday, February 18, 2025

**Learning Objectives:** This class aimed to solidify students' understanding of network reconnaissance and scanning techniques, focusing on practical applications through Lab 2, which covers TCP and UDP attacks. The instructor employed a combination of lecture, interactive Q&A, real-world examples, and hands-on exercises to facilitate learning.

**Topics Covered:** The class primarily focused on Lab 2, covering TCP attacks, sniffing, spoofing, traceroute implementation, and port scanning techniques (TCP and UDP).  The instructor also briefly revisited topics from the previous week, including DNS zone transfers and open-source intelligence tools.  These topics are crucial for understanding network vulnerabilities and developing effective security measures.


### Key Topics:

1. **Lab 2 Overview & Logistics:**

    * **Lab 1 Due Date & Late Submission Policy:**  Original due date was February 16th. Late submissions are accepted until February 26th with a 1% deduction per day, up to a maximum of 10%.  Students facing personal or health issues should contact Student Advocacy for extensions. Professional reasons require direct communication with the professor.
    * **Lab 2 Release & Due Date:** Released recently, due on March 2nd. A 5% bonus is awarded for submissions up to 5 days early. A 10% deduction applies for submissions up to 10 days late.
    * **Lab 2 Grading:** Grading for Lab 1 will commence after the submission deadline and is expected to be completed within a week.
    * **Office Hours:** Available with Anubath at 8 PM on the day of the lecture.
    * **Recommended Resource:** The instructor recommended Professor Wei Ling Du (Kevin Du)'s book and Udemy courses for supplementary learning. These resources provide hints and context for the lab exercises.

2. **Lab 2 Tasks:**

    * **Task 1: Sniffing and Filtering:** This task focuses on using Scapy's `sniff` function and BPF filters to capture specific network traffic.  The instructor emphasized the importance of mastering filters to avoid capturing unnecessary packets and ensuring correct results in subsequent tasks.  Students were encouraged to test their filters in Wireshark.
    * **Task 2: Spoofing an ICMP Echo Request:** This task involves crafting and sending a spoofed ICMP echo request packet, making it appear as if Google's DNS server (8.8.8.8) is pinging the user.  This demonstrates a basic form of IP spoofing.
        * **Diagram:** The instructor used a diagram to illustrate the normal ping process (user -> Google -> user) and the spoofed ping process (attacker -> user -> Google).
    * **Task 3: Writing a Traceroute Program:**  Students are required to implement a traceroute program using Scapy. The program should send ICMP echo requests with incrementing TTL values to map the network path to a destination (Google's DNS server).
        * **Skeleton Code & Key Challenge:** Skeleton code is provided, but it lacks proper handling of situations where a hop doesn't respond. Students must address this issue to prevent the program from hanging.
        * **Diagram:** The instructor used a diagram to visualize the traceroute process and the potential for a hop not responding.
    * **Task 4: Spoofing Echo Replies:** This task involves sniffing the network for ICMP echo requests and responding with spoofed ICMP echo replies. The instructor presented three scenarios:
        * **Scenario 1: Pinging a Non-Existent IP (1.2.3.4):**  The program should respond with a spoofed reply, even though no real host exists at that address.  The expected output is one echo reply per echo request.
        * **Scenario 2: Pinging a Non-Existent Local IP (10.9.0.99):** The program should *not* respond because the local host will perform an ARP request before sending an ICMP echo request, and since the target doesn't exist, no ICMP request will be generated.
        * **Scenario 3: Pinging Google's DNS Server (8.8.8.8):** The program should respond with a spoofed reply *in addition* to the legitimate reply from Google. The expected output is two echo replies per echo request.
    * **Task 5 (Bonus): ARP Cache Poisoning:** This bonus task requires students to implement ARP cache poisoning to make the ping to 10.9.0.99 (Scenario 2 of Task 4) work.  The instructor strongly advised understanding the underlying theory of ARP cache poisoning before attempting this task.

3. **DNS Zone Transfers (Review):**

    * The instructor revisited the concept of DNS zone transfers, a vulnerability that allows attackers to retrieve all DNS records from a server.  While this is now disabled by default, it was once a common security issue.
    * **Tools:**  DnsDumpster was mentioned as a tool for discovering subdomains, although it doesn't provide an exhaustive list.
    * **Mitigation:** Split DNS, using separate internal and external DNS servers, is the standard practice for mitigating risks associated with DNS zone transfers.

4. **Service Discovery & Port Scanning:**

    * **Port Scanning Basics:** The class covered port scanning as a method for identifying open ports and running services on a host.
    * **TCP Header Review:**  The instructor presented a TCP header and emphasized the importance of familiarity with its structure.
    * **TCP Port Scanning Techniques:**
        * **TCP SYN Scan:** Sends a SYN packet and analyzes the response (SYN-ACK for open, RST for closed, ICMP Destination Unreachable for filtered/rejected, no response for filtered/dropped).  This is a fast scanning method.
        * **TCP Connect Scan:** Uses the operating system's API to establish a full three-way handshake and then close the connection. Slower than a SYN scan due to the overhead of establishing and closing connections.
        * **Other TCP Scans (FIN, NULL, Xmas):**  These scans send packets with unusual flag combinations to elicit responses that can help identify the operating system.
        * **TCP ACK Scan:** Used to probe firewall rules, particularly on stateless firewalls.  By sending an ACK packet, the scanner can determine if a port is filtered or unfiltered based on the response (RST or no response).  The instructor used a diagram to explain the mechanics of an ACK scan and how it interacts with a firewall.
    * **UDP Port Scanning:** More challenging than TCP scanning due to the connectionless nature of UDP.
        * **Responses:** Open ports typically respond with application-specific data. Closed ports may respond with an ICMP Destination Unreachable message.  No response can indicate a filtered port or an improperly formatted request.


### Exercises & Discussions:

* **Exercise 1:** List three tools discussed in the last lesson (Maltego, Creepy, Aggra Database, Shodan, Google Search filtering, Google Hacking, DnsDumpster).
* **Exercise 2:** Explain the three steps in the TCP three-way handshake (SYN, SYN-ACK, ACK).
* **Exercise 3:** What are the four possible responses to a TCP SYN scan? (SYN-ACK, RST, ICMP Destination Unreachable, No Response).
* **Exercise 4:** In UDP scanning, what are the three responses and their meanings? (Application-specific response, ICMP Destination Unreachable, No Response).
* **Exercise A:** Explain the difference between a TCP SYN scan and a TCP Connect scan. Provide a scenario where each would be useful. (SYN scan is faster and stealthier, suitable for quick reconnaissance. Connect scan is more reliable but slower, useful for accurate port state determination when stealth is not a primary concern).


### Important Announcements:

* **Lab 2 Due Date:** March 2nd.
* **Early Submission Bonus:** 5% for submitting Lab 2 up to 5 days early.
* **Bonus Task:** 5% for completing the ARP cache poisoning task in Lab 2.
* **TA Office Hours:**  8 PM Eastern Time on the day of the lecture.
* **Course Schedule & Updates:** Refer to Brightspace for the most up-to-date information.


### Final Takeaways:

This class provided a deep dive into practical network scanning and reconnaissance techniques.  Students gained valuable experience in using Scapy for crafting and sending packets, analyzing network traffic, and exploiting vulnerabilities.  Understanding the different types of TCP and UDP scans, as well as the nuances of firewall behavior, is crucial for both attackers and defenders.

### Follow-up Actions:

* **Complete Lab 2:**  Focus on understanding the BPF filters and handling edge cases in the traceroute implementation.
* **Review TCP and UDP Header Structures:** Ensure a solid understanding of these fundamental protocols.
* **Explore Nmap:** Experiment with different scan types and analyze the results.
* **Read about ARP Cache Poisoning:**  Prepare for the bonus task in Lab 2.


### Motivational Note:

Network security is a constantly evolving field.  The skills and knowledge you're gaining in this course are highly valuable and will serve you well in your future endeavors.  Keep exploring, keep learning, and stay curious!