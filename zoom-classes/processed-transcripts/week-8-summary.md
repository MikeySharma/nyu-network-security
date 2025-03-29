## Network Security - Class Summary

**Subject:** CS 6823 - Network Security
**Instructor:** Professor Philip Mack
**Date:** Monday, March 17th, 2025
**Week:** 8

### 1. Introduction

This lecture marked the beginning of the second half of the Network Security course, shifting the focus from offensive security techniques (covered in the first half) to defensive strategies and protections.  The learning objectives for this part of the course involve understanding how to protect networks from attacks, emphasizing defense in depth. Professor Mack adopted a practical approach, using real-world examples like Starbucks Wi-Fi vulnerabilities to illustrate the importance of network security concepts. The lecture covered several key topics, including ARP cache poisoning, the Diffie-Hellman key exchange and its vulnerabilities, message integrity, hashing algorithms, digital signatures, HMACs, and an introduction to public key infrastructure (PKI) and TLS. The relevance of these topics stems from their crucial role in modern network security and the need to understand both attack vectors and mitigation strategies.

### 2. Key Topics

**2.1 ARP Cache Poisoning**

* **Subtopic 2.1.1: ARP Protocol Overview:** ARP (Address Resolution Protocol) resolves IP addresses to MAC addresses on a local network. A host broadcasts an ARP request asking for the MAC address associated with a specific IP address. The host with that IP address responds with its MAC address in a unicast ARP reply.
* **Subtopic 2.1.2: ARP Cache Poisoning Methods:** Four methods were discussed:
    * **Gratuitous ARP Request & Unicast ARP Reply (Normal):** Standard ARP operation.
    * **Gratuitous ARP Reply (Ineffective):**  Broadcasting a fake ARP reply. This used to be effective but is now patched in most operating systems.
    * **Unicast ARP Request (Potentially Effective):** Sending a targeted ARP request to a specific host.
    * **Unicast ARP Reply (Effective):** Sending a targeted, fake ARP reply to a specific host. This is the primary method used in ARP cache poisoning attacks.
* **Subtopic 2.1.3: ARP Header Structure:** The ARP header includes source and destination MAC and IP addresses. Notably, some of this information is duplicated within the header due to the layered architecture of network protocols (Ethernet header at Layer 2, ARP header at Layer 2/3). This redundancy can be exploited in some attacks.
* **Subtopic 2.1.4: Attacker-in-the-Middle (AitM) using ARP Poisoning:** The attacker sends fake ARP replies to both the target host and the router.  The replies falsely associate the attacker's MAC address with the target host's IP address (for the router) and the router's IP address (for the target host).  This redirects traffic through the attacker.  IP forwarding on the attacker's machine bridges the connection, enabling the attacker to intercept and potentially modify the data.
* **Subtopic 2.1.5: ARP Cache Poisoning on Layer 3 Devices:**  ARP poisoning can also target layer 3 switches or any device with an ARP cache, including Linux machines configured as switches.

**2.2 Diffie-Hellman Key Exchange and its Vulnerabilities**

* **Subtopic 2.2.1: Diffie-Hellman Overview:**  Diffie-Hellman enables secure key exchange between two parties without transmitting the secret key directly.  It relies on modular arithmetic and the difficulty of computing discrete logarithms.
* **Subtopic 2.2.2: Man-in-the-Middle (AitM) Attack on Diffie-Hellman:**  An attacker can intercept the initial key exchange messages and establish separate keys with each party, effectively becoming the man-in-the-middle.  This allows the attacker to decrypt and potentially modify the communication.
* **Subtopic 2.2.3: Protecting Diffie-Hellman:**  Diffie-Hellman is vulnerable when used in plain text. It should always be protected with a digital signature algorithm like RSA to ensure authenticity and prevent modification of the exchanged values.

**2.3 Message Integrity, Hashing, Digital Signatures, and HMACs**

* **Subtopic 2.3.1: Encryption vs. Hashing:** Encryption is a two-way process, converting plaintext to ciphertext and back. Hashing is a one-way process, creating a fixed-size representation (hash) of a message.  Changes to the message result in a drastically different hash.
* **Subtopic 2.3.2: Hashing Algorithms:**
    * **MD5 (Broken):** 128-bit hash, considered insecure.
    * **SHA-1 (Broken):** 160-bit hash, also considered insecure.
    * **SHA-2 (Secure):**  Includes SHA-256 (256-bit) and SHA-512 (512-bit), currently recommended.
* **Subtopic 2.3.3: Digital Signatures:** A hash of a message encrypted with the sender's private key.  Provides authenticity, integrity, and non-repudiation.
* **Subtopic 2.3.4: HMAC (Hash-Based Message Authentication Code):**  A hash of a message encrypted with a shared symmetric key. Similar in function to a digital signature but uses a symmetric key instead of an asymmetric key pair. HMACs are faster than digital signatures.
* **Subtopic 2.3.5: Replay Attacks and Nonces:** Replay attacks involve resending a captured message. Nonces (numbers used once) can prevent replay attacks by including a unique value in each message.

**2.4 Public Key Infrastructure (PKI) and TLS (Brief Introduction)**

* These topics were introduced as crucial for secure online transactions, like shopping on Amazon.  The details of PKI and TLS will be covered in the following weeks.


### 3. Exercises & Discussions

* **Exercise A1 & A2:** Constructing ARP request and reply headers for an ARP cache poisoning attack. This exercise focused on understanding the precise content of each field in the headers, emphasizing the importance of correctly manipulating these fields for a successful attack.  Detailed solutions were provided by the instructor, highlighting the attacker's manipulation of the sender IP and MAC addresses to deceive the target hosts.
* **Exercise 0:** Completing the midterm course review.
* **Exercise 1:** Determining minimum recommended cryptographic strengths for AES, Diffie-Hellman, RSA, and SHA.
* **Exercise B:** Researching the cost of a 1-year TLS certificate.
* **Exercise C:** Explaining Diffie-Hellman's susceptibility to AitM attacks.
* **Exercises 2 & 3:** Omitted from this week's assignment.

**Discussions:**  Discussions included the OSI model in relation to ARP headers, the choice of tools for ARP cache poisoning (e.g., Ettercap), the impact of layer 3 switches on ARP poisoning, the similarity between ARP cache poisoning and DNS cache poisoning, the lack of security in ARP and DNS, the ease of performing these attacks on public Wi-Fi, the performance trade-offs of stronger encryption, the impact of quantum computing on cryptography, and the introduction of post-quantum cryptographic algorithms.

### 4. Important Announcements

* **Lab 3:** Released and due April 6th. Covers ARP cache poisoning. Auto-graded via Gradescope.  Requires uploading a settings.txt file and a Wireshark capture of the attack.  Early submission bonus (5 percentage points) available.
* **Mid-Semester Feedback:** Students were asked to complete the mid-semester course review.  Feedback was requested on what the professor should stop, start, and continue doing.  Completing the review contributed to this week's bonus points.
* **Spring Break:** No class next week. Optional assignments are available.
* **Final Exam:** Will be in May and will use Respondus Lockdown Browser + Monitor.  Students must have administrative rights to install the software.  Alternatives will be provided for students who cannot use Respondus.  Only approved resources (course slides, videos, Brightspace materials, textbook, printed notes, man pages) will be allowed.  No free internet access.


### 5. Final Takeaways

This lecture introduced crucial concepts in network security, focusing on the vulnerabilities of essential protocols like ARP and Diffie-Hellman.  Students gained a practical understanding of ARP cache poisoning and its implementation.  The discussion on cryptography highlighted the importance of choosing appropriate algorithms and the need to consider factors like performance and the evolving landscape of quantum computing.

**Follow-up Actions:**

* Complete Lab 3.
* Complete the mid-semester course review.
* Research ARP cache poisoning tools and techniques.
* Review the recommended cryptographic strengths and NIST guidelines.
* Investigate post-quantum cryptography algorithms.

**Motivational Note:**  Network security is a constantly evolving field.  By understanding the vulnerabilities and developing robust defense strategies, you can contribute to creating a more secure digital world.  The skills and knowledge gained in this course will be invaluable in protecting individuals and organizations from cyber threats. Keep exploring and practicing, and you'll become a proficient network security professional.