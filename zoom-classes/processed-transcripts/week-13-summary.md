## Comprehensive Summary of Network Security Class

**Subject:** CS 6, 8, 2, 3 - Network Security
**Instructor:** Professor Philip Mack
**Date:** Monday, April 28th, 2025 (Week 13)

**Learning Objectives:** This lecture aimed to reinforce understanding of network security principles, focusing on DHCP and ARP attacks, mitigation techniques, and an introduction to wireless security (802.11).  The instructor employed a combination of conceptual explanations, real-world examples, and protocol analysis to convey the material.

**Topics Covered:** The class covered DHCP attacks, mitigation strategies (DHCP snooping), ARP attacks and defenses, IP source guard, spanning tree protocol (STP) and related attacks, 802.1x authentication, and an introduction to 802.11 wireless security, including terminology, frame structure, and the evolution of Wi-Fi security protocols.  These topics are crucial for understanding vulnerabilities in network infrastructure and implementing appropriate security measures.

---

### **Key Topics:**

**1. DHCP Attacks and Mitigation:**

* **DHCP Review:** DHCP (Dynamic Host Configuration Protocol) is a four-message protocol (Discover, Offer, Request, Acknowledge) used to assign IP addresses and other network parameters to devices joining a network.  Its inherent lack of security makes it vulnerable to attacks.

* **Rogue DHCP Server Attack:**
    * An attacker (Trudy) sets up a rogue DHCP server on the network.
    * When a client broadcasts a DHCP Discover message, Trudy's rogue server responds with a DHCP Offer before legitimate servers.
    * The client accepts Trudy's offer, receiving a malicious IP configuration (e.g., wrong default gateway, DNS server, or web proxy). This enables man-in-the-middle attacks.
    * Trudy can increase the likelihood of being the first responder by using attacks like ARP cache poisoning to prevent legitimate DHCP servers from replying.

* **DHCP Starvation Attack:**
    * Trudy floods the network with DHCP Discover messages using spoofed MAC addresses.
    * This exhausts the DHCP server's IP address pool, preventing legitimate clients from obtaining IP addresses and effectively denying them network access.

* **DHCP Snooping (Mitigation):**
    * **Feature 1: Trusted/Untrusted Ports:** Designates switch ports as either trusted (connected to DHCP servers) or untrusted (connected to clients). Untrusted ports can only send DHCP Discover and Request messages, while trusted ports can only send DHCP Offer and Acknowledge messages.
    * **Feature 2: DHCP Snooping Binding Table:**  The switch maintains a table of DHCP bindings (MAC address, IP address, lease time, VLAN, interface), enabling tracking and analysis of DHCP activity.
    * **Feature 3: MAC Address Verification:**  DHCP snooping verifies that the source MAC address in the Ethernet header matches the client hardware address (CHADDR - MAC address) in the DHCP header, preventing MAC address spoofing during DHCP transactions.

* **Alternative Mitigation (Port Blocking):** If DHCP snooping isn't available, blocking port 68 (DHCP client port) on the client-side of the network can prevent rogue DHCP server attacks.


**2. ARP Attacks and Defenses:**

* **ARP Review:** ARP (Address Resolution Protocol) resolves IP addresses to MAC addresses. A client broadcasts an ARP request for the MAC address of a specific IP. The device with that IP responds with its MAC address.

* **ARP Cache Poisoning:**
    * Trudy sends spoofed ARP replies to both the target host and the router.
    * Trudy tells the router that the target host's MAC address is Trudy's MAC address.
    * Trudy tells the target host that the router's MAC address is Trudy's MAC address.
    * This positions Trudy in the middle of all communication between the target host and the router, enabling eavesdropping and manipulation.
    * **IP Forwarding:**  Trudy enables IP forwarding on her machine to act as a bridge and maintain the flow of traffic between the target and the router, making the attack less noticeable.
    * **Bi-directional Poisoning:**  It is crucial to poison the ARP cache on both sides (router and target) to create a stable attack and avoid detection by switches that detect loops.

* **Dynamic ARP Inspection (DAI) (Defense):**
    * Requires DHCP snooping to be enabled.
    * DAI checks each ARP packet against the DHCP snooping binding table.
    * If the ARP packet's IP-to-MAC mapping doesn't match the binding table, the packet is dropped, preventing ARP cache poisoning.

* **MAC and IP Address Spoofing:** Spoofing MAC and IP addresses is extremely easy using tools like Scapy, highlighting the vulnerability of layer 2 and 3 protocols.

* **IP Source Guard (IPSG) (Defense):**
    * A premium feature on high-end Cisco devices.
    * Relies on the DHCP snooping binding table.
    * Checks every IP packet against the table to ensure the source IP and MAC address match a valid DHCP lease.
    * Extremely resource-intensive, requiring significant CPU and memory.


**3. Spanning Tree Protocol (STP) and Attacks:**

* **STP Review:** STP prevents loops in redundant network topologies by dynamically disabling redundant links, creating a loop-free tree structure.  This prevents network storms caused by circulating packets.

* **BPDU Attacks:** BPDU (Bridge Protocol Data Unit) messages are used by STP.  These messages lack security, making STP vulnerable.
    * **Root Bridge Attack:** An attacker sends spoofed BPDUs with a higher priority and bandwidth, claiming to be the root bridge. This redirects traffic through the attacker, enabling man-in-the-middle attacks.

* **STP Defenses:**
    * **BPDU Guard:**  Disables ports that receive BPDUs from unauthorized devices, preventing rogue devices from influencing the spanning tree topology.
    * **Root Guard:** Prevents designated ports from becoming the root port, ensuring that the legitimate root bridge remains in control.


**4. 802.1x Authentication:**

* **Overview:** 802.1x provides port-based network access control, requiring devices to authenticate before gaining access to the network. This is commonly used for Wi-Fi authentication.

* **Process:**
    * **Supplicant (Client):** The device requesting network access.
    * **Authenticator (Switch/AP):** Controls access to the network.
    * **Authentication Server (RADIUS):** Verifies the supplicant's credentials.
    * The supplicant initiates authentication with the authenticator.
    * The authenticator acts as an intermediary, relaying authentication information between the supplicant and the authentication server.
    * The authentication server verifies the credentials (username/password, certificate, etc.).
    * If authentication is successful, the authenticator grants network access to the supplicant.

* **EAP-TTLS (Example):** Creates a TLS tunnel between the supplicant and the authentication server before transmitting credentials, protecting them from eavesdropping.


**5. 802.11 Wireless Security:**

* **802.11 (Wi-Fi):** The IEEE standard for wireless LANs, analogous to 802.3 (Ethernet) for wired networks.

* **Terminology:**
    * **SSID (Service Set Identifier):** The network name (e.g., "NYU").
    * **BSSID (Basic Service Set Identifier):** The MAC address of the access point (AP).

* **802.11 Frame Structure:**  Contains three MAC addresses: Destination, Source, and Router. The Router address facilitates roaming between APs.

* **Wi-Fi Security Protocols:**
    * **WEP (Wired Equivalent Privacy):** Insecure due to a flawed implementation of the RC4 stream cipher.
    * **WPA (Wi-Fi Protected Access) / WPA1:** Improved upon WEP but still deprecated.
    * **WPA2:**  Uses AES encryption and is considered secure if a strong password is used. Vulnerable to offline brute-force attacks if a weak password is chosen.
    * **WPA3:**  Addresses the offline brute-force vulnerability of WPA2 and offers enhanced security.

* **Mac Address Randomization:** A privacy feature that changes the device's MAC address periodically to prevent tracking. However, many enterprises disable this for auditing and security investigation purposes.


---

### **Exercises & Discussions:**

* **Exercise 1:** Locating and understanding the course evaluation process.  Emphasis on the importance of student feedback for university rankings and professor evaluations.
* **Exercise 2:** Reviewing a previously discussed exercise about potential security issues with provided network information (repeated from the previous week).

---

### **Important Announcements:**

* **Lab 4:** Due date was yesterday (Sunday), but a 6-day extension is available.  Covers firewalls, an important topic for the final exam.  Students are encouraged to review Lesson 7 before completing the lab.
* **Weekly Bonus Exercise (Exercise 11):** Due May 1st. Covers firewall video content.
* **Final Exam:** Saturday, May 10th, between 10 AM and 12 noon. Sample questions will be released tomorrow, and students should dedicate approximately 2 hours per day to reviewing them.  Answers will be released on Thursday, May 8th.
* **Final Review Class:** Next Monday.  Students are encouraged to complete their studying before the review class.

---

### **Final Takeaways:**

* Layer 2 protocols are inherently insecure due to their age and lack of built-in security features.
* Understanding DHCP and ARP attacks and their mitigations is crucial for network security.
* Keeping Wi-Fi equipment updated and using strong passwords are essential for wireless security.
* 802.1x provides robust authentication for network access.

**Follow-up Actions:** Review Lesson 7 (Firewalls), complete Lab 4, complete the weekly bonus exercise (11), begin reviewing the sample final exam questions, and prepare for the final review class next Monday.

**Motivational Note:** Network security is a constantly evolving field.  By staying informed about new threats and mitigation techniques, you can contribute to building more secure and resilient networks.  Apply the knowledge gained in this class to protect yourself and your organization from cyberattacks.