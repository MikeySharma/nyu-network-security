## Cs. 6, 8, 2, 3 Network Security - Midterm Review

**Instructor:** Professor Philip Mack

**Date:** Monday, March 10th, 2025 (Week 7)

**Learning Objectives:** This midterm review session aims to reinforce key concepts covered in the first six weeks of the Network Security course, focusing on topics likely to appear on the midterm exam. The instructor adopts a practical approach, using real-world examples, lab exercises, and problem-solving activities to solidify student understanding.

**Teaching Approach:** Professor Mack uses a conversational style, engaging students through questions, discussions, and practical exercises. He emphasizes the importance of understanding the underlying principles of network security concepts and their practical applications.

**Topics Covered:** The review session covers a range of essential network security topics, including Denial-of-Service (DoS) attacks, port scanning, DNS vulnerabilities, risk assessment, cryptography (Diffie-Hellman and RSA), and block cipher modes of operation. These topics are crucial for understanding common network security threats and developing effective defense mechanisms.


### Key Topics

**1. Denial-of-Service (DoS) Attacks**

* **Subtopic: SYN Flood Attack:** This attack exploits the TCP three-way handshake by flooding the target server with SYN packets, exhausting its connection queue and preventing legitimate connections.

* **Mitigation: SYN Cookies:**  An ingenious defense mechanism where the server generates a unique "cookie" based on the client's IP address, port, and other parameters. This cookie is embedded in the SYN-ACK packet. Upon receiving the ACK, the server recalculates the cookie. A match validates the connection, mitigating the SYN flood.

    * **SYN Cookie Calculation (Apache):** `Md5(IP_source, IP_destination, Port_source, Port_destination, Current_time, Magic_number)` - The first 32 bits of the MD5 hash are used as the initial sequence number (B) in the SYN-ACK.

* **Mitigation: Reverse Path TCP Connection:** Ubuntu reserves 25% of sockets for previously known IP addresses, ensuring some availability for legitimate connections during a SYN flood attack.

* **Subtopic: TCP Reset Attack:**  An attacker intercepts and analyzes network traffic between two hosts (Alice and Bob). By sending a TCP RST packet with the correct sequence number, the attacker can terminate the connection.

    * **Sequence Number Selection:**  The attacker copies the sequence number from the last observed packet (either Alice to Bob or Bob to Alice) and uses it in the RST packet.  Attacking the server-side (Bob) is more effective for session hijacking attacks, as explained below.

* **Subtopic: Session Hijacking:**  After terminating a connection with a TCP RST attack, the attacker can inject malicious commands into the communication stream by sending packets with the correct sequence and acknowledgment numbers.

    * **Telnet Session Hijacking:**  This attack is effective only when targeting the server-side (Bob) because only the server executes commands. Sending commands to the client-side (Alice) will only display them on the screen without execution.
    * **Reverse Shell:**  A more sophisticated attack where the attacker sets up a listener on their machine and sends a command to the server (Bob), instructing it to establish a connection back to the attacker's listener. This provides the attacker with a remote shell on the server.

**2. Port Scanning**

* **TCP Port Scanning:**

    * **Open Port:**  A SYN packet sent to an open port elicits a SYN-ACK response.
    * **Closed Port:** A SYN packet sent to a closed port results in a RST packet.
    * **Filtered Port (Rejected):**  A firewall may reject the SYN packet by sending an ICMP Destination Unreachable message.
    * **Filtered Port (Dropped):** A firewall may silently drop the SYN packet without any response.

* **UDP Port Scanning:** Significantly more challenging than TCP scanning due to UDP's connectionless nature.

    * **Open Port:** A UDP packet sent to an open port may elicit a response depending on the application running on that port (e.g., a DNS response for port 53).
    * **Closed Port:**  An ICMP Destination Unreachable message indicates a closed UDP port.
    * **Open/Filtered:**  No response could mean either a dropped packet by a firewall or a malformed packet/incorrect protocol.  Nmap classifies this as open/filtered.
    * **ICMP Rate Limiting:**  OS limitations on ICMP Destination Unreachable messages (1 per second in Linux, 2 per second in Windows) make UDP scanning very slow.

**3. DNS Vulnerabilities**

* **DNS Spoofing (Local Network):**  An attacker on the same local network can intercept DNS requests and respond faster than the legitimate DNS server, redirecting the victim to a malicious website. This requires matching the transaction ID and port number of the DNS request.
* **DNS Spoofing (Remote Server):**  An attacker can attempt to spoof DNS responses from authoritative DNS servers, potentially poisoning DNS caches and affecting a larger number of users.

**4. Risk Assessment**

* **Qualitative Risk Assessment:**  Uses a risk matrix (e.g., 5x5 matrix used by DoD) to categorize risks based on likelihood and impact.  Employs the Delphi technique, where multiple experts independently assess risks to reach a consensus.

* **Residual Risk:**  The risk that remains after mitigation efforts. It's not necessarily the absolute lowest possible risk but the risk remaining after implementing feasible security measures.

* **Quantitative Risk Assessment:** Uses numerical values to assess risk.

    * **Asset Value (AV):**  The monetary value of the asset.
    * **Single Loss Expectancy (SLE):** The cost of a single incident.
    * **Annualized Rate of Occurrence (ARO):**  How often the incident is expected to occur per year.
    * **Annualized Loss Expectancy (ALE):**  `ALE = SLE * ARO`

**5. Cryptography**

* **Diffie-Hellman Key Exchange:** Allows two parties to establish a shared secret key over an insecure channel without prior communication.

    * **Steps:**  Alice chooses public parameters `g` and `n`, and a secret number `a`. Bob chooses a secret number `b`. They exchange calculated values (`A = g^a mod n`, `B = g^b mod n`) and compute the shared secret key `K = A^b mod n = B^a mod n`.

* **RSA Key Generation:**

    * **Steps:**
        1. Choose two large prime numbers, `p` and `q`.
        2. Calculate `n = p * q`.
        3. Calculate `Φ(n) = (p-1) * (q-1)`.
        4. Choose an encryption key `e` such that `1 < e < Φ(n)` and `gcd(e, Φ(n)) = 1` (relatively prime).
        5. Calculate the decryption key `d` such that `ed mod Φ(n) = 1`.
        6. Public key: `(n, e)`. Private key: `(n, d)`.

**6. Block Cipher Modes of Operation**

* **Purpose:** To ensure that encrypting the same plaintext block multiple times produces different ciphertext blocks.  This is achieved by chaining blocks together and incorporating an Initialization Vector (IV).

* **Modes:** CBC, CFB, OFB, PCBC. Students should be familiar with the diagrams and calculations involved in each mode.  The visual method and mathematical formulas can be used to understand and solve problems.

### Exercises & Discussions

The instructor presented several exercises (A-D) related to residual risk, TCP/UDP port scanning responses, DNS spoofing scenarios, Diffie-Hellman calculations, and RSA key generation.  Detailed solutions and explanations were provided for some of these exercises, while others were left for students to complete independently as practice for the midterm exam.  The instructor emphasized the importance of providing clear explanations and justifications for answers, especially in open-ended questions.

### Important Announcements

* **Midterm Exam:** Saturday, March 15th, 1 PM - 3 PM Eastern Time (2 hours).
* **Coverage:**  All topics except Lesson 4, slides 41 onward. Includes homeworks 1 & 2, labs 1 & 2, reading materials, slides, and video lectures.
* **Format:** Open book, open notes, open VM, open internet.  Individual work, no AI assistance allowed.
* **Grading:**  Unauthorized collaboration or plagiarism will result in a zero.
* **Time Limit:** Strict 2-hour limit, timer does not stop.
* **Absences:**  Proper documentation required (doctor's note, professional documentation). Submit medical documentation to Student Advocacy.
* **Lab 2 Grades:**  Will be returned by Friday.

### Final Takeaways

* Review sample midterm problems under timed conditions.
* Redo labs and homework assignments to ensure proficiency.
* Review lecture slides and videos to solidify understanding.
* Understand the practical applications of the concepts discussed.
* Practice using Wolfram Alpha for calculations.
* Prepare clear and detailed explanations for exam questions.


**Motivational Note:**  Network security is a critical field, and the concepts covered in this course are essential for protecting digital assets.  By diligently reviewing the material and practicing the exercises, you will be well-prepared for the midterm exam and gain valuable skills for a successful career in cybersecurity.  Remember, the effort you put in today will pay off in the long run. Good luck!