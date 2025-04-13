## Comprehensive Summary of Network Security Class (CS 6, 8, 8, 2, 3)

**Instructor:** Professor Philip Mack

**Date:** Monday, April 7th, 2025 (Week 10)

**Subject:** Network Security

**Learning Objectives:**

* Understand the importance and workings of Transport Layer Security (TLS).
* Learn the steps involved in a TLS handshake.
* Analyze the structure of TLS cipher suites.
* Understand the role of certificates and digital signatures in TLS.
* Investigate TLS session resumption.
* Explore the differences between TLS 1.2 and 1.3.

**Instructor's Teaching Approach:** Professor Mack uses a combination of lecture, real-world examples (like analyzing Amazon.com's security), diagrams, and interactive Q&A sessions to explain complex concepts. He emphasizes the practical application of theoretical knowledge and encourages active student participation.

**Topics Covered:**

* Introduction to TLS and its significance in secure online communication.
* Detailed breakdown of the ten steps in a TLS handshake.
* Structure and components of TLS cipher suites.
* Certificate validation process and the role of Certificate Authorities (CAs).
* TLS session resumption for improved performance.
* Adaptations in TLS 1.3 and its compatibility challenges.

**Key Topics (Detailed Breakdown):**

**1. Introduction to TLS:**

* TLS is a crucial technology for secure communication over the internet, enabling secure connections between clients (like web browsers) and servers without prior key exchange.
* TLS builds upon the principles of Public Key Infrastructure (PKI), allowing for authentication and encryption without physical key exchange.

**2. TLS Handshake (Ten Steps):**

Professor Mack meticulously explained each step, using a diagram resembling the SSL 4.0 handshake (but representing TLS 1.2):

| Step | Description | Encryption | Protocol Type |
|---|---|---|---|
| 1 | Client Hello: Client sends supported TLS versions, cipher suites, and other parameters to the server. | No | Handshake |
| 2 | Server Hello: Server selects the agreed-upon parameters for the TLS session. | No | Handshake |
| 3 | Certificate: Server sends its certificate and intermediate certificates to the client. | No | Handshake |
| 4 | Server Key Exchange: Server sends its Diffie-Hellman parameters (A, G, N) if Diffie-Hellman is used. These values are digitally signed using the server's private key. | No (DH values are signed) | Handshake |
| 5 | Server Hello Done: Server signals the end of its initial messages. | No | Handshake |
| 6 | Client Key Exchange: Client sends its Diffie-Hellman parameter (B) if Diffie-Hellman is used. If RSA is used, the client generates a pre-master secret (K), encrypts it with the server's public key, and sends it to the server. |  DH: No, RSA: Yes (Pre-master secret is encrypted) | Handshake |
| 7 | Change Cipher Spec: Client signals that subsequent messages will be encrypted. | No | Change Cipher Spec |
| 8 | Finished: Client sends a hash of all prior handshake messages, encrypted with the negotiated symmetric key. | Yes | Handshake |
| 9 | Change Cipher Spec: Server signals that subsequent messages will be encrypted. | No | Change Cipher Spec |
| 10 | Finished: Server sends a hash of all prior handshake messages, including the client's finished message, encrypted with the negotiated symmetric key. | Yes | Handshake |


**3. TLS Cipher Suites:**

* A cipher suite specifies the algorithms used for key exchange, bulk encryption, and message authentication (HMAC).
* **Example 1:** `TLS_DHE_RSA_WITH_AES_128_CBC_SHA256`
    * Key Exchange/Authentication: DHE (Diffie-Hellman Ephemeral) with RSA authentication.
    * Bulk Encryption: AES 128-bit in CBC (Cipher Block Chaining) mode.
    * Hashing: SHA256.
* **Example 2:** `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`
    * Key Exchange/Authentication: ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) with ECDSA (Elliptic Curve Digital Signature Algorithm) authentication.
    * Bulk Encryption: AES 256-bit in CBC mode.
    * Hashing: SHA384.
* **Example 3:** `TLS_RSA_WITH_AES_256_GCM_SHA384`
    * Key Exchange/Authentication: RSA.
    * Bulk Encryption: AES 256-bit in GCM (Galois/Counter Mode).
    * Hashing: SHA384.
* **TLS 1.3 Cipher Suites:**  Simplified format, omitting the key exchange algorithm as it's assumed to be secure.  Example: `TLS_AES_128_GCM_SHA256`.

**4. Certificate Validation:**

* The client verifies the server's certificate by checking its validity period, subject alternative names, and digital signature.
* The digital signature is validated using the public key of the issuing CA.
* This process involves traversing the certificate chain up to a trusted root CA present in the client's certificate store.

**5. TLS Session Resumption:**

* To avoid the overhead of a full handshake for every connection, TLS supports session resumption.
* The client sends a session ID, and if the server recognizes it, an abbreviated handshake is performed, skipping the certificate and key exchange steps.

**6. TLS 1.3:**

* TLS 1.3 offers improved security and performance.
* Due to compatibility issues with older devices, TLS 1.3 is often negotiated as an extension within a TLS 1.2 handshake.  The client hello indicates TLS 1.2, but an extension specifies support for 1.3.


**Exercises & Discussions:**

* **Exercise 1:** Identifying the steps where different keys (DHE parameters, AES keys, RSA keys, certificates) are exchanged or generated during the TLS handshake.  This involved analyzing the different steps and understanding which keys are transmitted and which are generated locally.
* **Exercise 2:** Determining the TLS record types for each message in the handshake and identifying which messages are encrypted.  This required understanding the different record types (handshake, change cipher spec, alert, application data) and when encryption begins.

**Important Announcements:**

* **Lab 3 (ARP Poisoning):** Due date was yesterday (April 6th, 2025), but late submissions are accepted with a 1% deduction per day (up to 10 days).
* **Homework 3 (Inspecting TLS):** Released and based on today's lesson.  Involves analyzing a Wireshark capture of a TLS handshake.
* **No Live Class Next Week (April 14th):** Asynchronous pre-recorded video on Lesson 7 (Firewalls) is already posted on Brightspace, along with bonus exercises.
* **Lab 4 (Firewalls):** Due May 7th.  5% early submission bonus and 5% bonus for extra tasks (up to 110% possible). Late submissions accepted up to 7 days (May 14th). Gradescope due date will be corrected.
* **Syllabus and Brightspace:** Students are encouraged to consult the syllabus and Brightspace for reading materials, course schedule, and updates.


**Final Takeaways:**

* TLS is a fundamental security protocol for online communication.
* Understanding the TLS handshake process is crucial for analyzing and troubleshooting network security issues.
* Cipher suites define the specific cryptographic algorithms used in a TLS session.
* Certificate validation ensures the authenticity of the server.
* TLS 1.3 offers enhanced security and performance but requires careful consideration for compatibility.

**Follow-up Actions:**

* Review the lecture video, especially the TLS handshake steps.
* Complete Homework 3 and Lab 4.
* Watch the pre-recorded video for Lesson 7 (Firewalls) and complete the associated exercises.
* Explore additional resources on TLS and PKI.

**Motivational Note:**  Understanding TLS empowers you to analyze and secure online communications.  By mastering these concepts, you contribute to a safer and more trustworthy internet experience for everyone.