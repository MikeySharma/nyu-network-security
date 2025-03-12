## CS H2, H3: Network Security - Cryptography

**Instructor:** Professor Philip Mac

**Date:** (Date not explicitly mentioned in the transcript)

**Learning Objectives:**

* Understand the fundamentals of cryptography, including basic definitions and historical context.
* Learn about symmetric-key cryptography and its application in algorithms like AES.
* Explore public-key cryptography and its importance in secure online communication.
* Grasp the concept of message integrity and digital signatures.
* Learn about different cryptographic attack types and the importance of key security.
* Understand modular arithmetic and its application in RSA key generation.
* Learn how to generate RSA keys and use them for encryption and decryption.
* Understand the concept of session keys and the Diffie-Hellman key exchange protocol.

**Instructor's Teaching Approach:** The instructor utilizes a pre-recorded video lecture format, encouraging students to pause and engage with exercises throughout the presentation. The exercises are for self-assessment and are not collected. The instructor emphasizes the importance of reviewing lecture slides beforehand.  The lecture uses a combination of definitions, examples, historical anecdotes, and step-by-step problem-solving to explain complex cryptographic concepts.

**Topics Covered:**

The lecture covers a broad range of cryptography topics, including basic cryptography definitions, symmetric-key cryptography (with a focus on AES and block ciphers), public-key cryptography (RSA), message integrity, and the Diffie-Hellman key exchange. These topics are highly relevant to network security, enabling secure communication, data integrity, and user authentication in online interactions.

---

### Key Topics:

**1. Introduction to Cryptography:**

* **Plaintext:** Unencrypted text, readable and understandable.
* **Ciphertext:** Encrypted text, unreadable without the decryption key.
* **Cipher:** The algorithm and key used for encryption/decryption.
* **Algorithm:** The set of rules or steps for encryption/decryption (e.g., AES).
* **Key:** The secret value used in conjunction with the algorithm.
* **Importance of Key Secrecy:** The algorithm (like AES) can be public, but the key must be kept secret for security.

**2. Historical Ciphers:**

* **Julius Caesar Cipher:** A simple substitution cipher where each letter is shifted a fixed number of positions down the alphabet.
    * **Example:** With a right shift of 3, "HELLO" becomes "KHOOR".
* **Zimmerman Telegram (WWI):** An example of early cryptography where numbers represented words using a secret codebook.
    * **Vulnerability:**  Revealing plaintext and ciphertext pairs can compromise the key.

**3. Modern Cryptography (AES):**

* **AES (Advanced Encryption Standard):** A widely used symmetric-key encryption algorithm.
* **Key Sizes:** 128-bit, 192-bit (less secure than 128-bit), 256-bit.
* **Strength of AES:**  Proven to be robust over time, but plaintext/ciphertext pairs compromise security.

**4. Goals of Cryptography:**

* **Confidentiality:** Ensuring only authorized users can read messages.
* **Integrity:** Preventing unauthorized alteration of messages during transit.
* **Authentication:** Verifying the identity of communicating parties.
* **Non-repudiation:** Proving message origin (origin) and time (time).

**5. Simple Encryption Scheme:**

* **Substitution Cipher:** Replacing each letter with another.
* **Example:**  (The transcript example has errors, but the concept is explained).

**6. Polyalphabetic Encryption Scheme:**

* **Substitution with Changing Key:** Uses a table (Vigenère cipher) where the key changes for each letter.
* **Example:** Plaintext: "NYU", Key: "CONCEPT". Ciphertext is determined by finding the intersection of the plaintext letter row and the key letter column in the Vigenère table.
* **Decryption:** Reverse process using the same table and key.

**7. Enigma Machine:**

* **Hardware Cipher:** Used multiple rotors (wheels) to implement a complex polyalphabetic cipher. Each keypress changed the rotor positions, altering the encryption.

**8. One-Time Pad:**

* **Theoretically Perfect Encryption:** Uses a truly random key (pad) of the same length as the message.
* **Key is Used Only Once:** Prevents reuse and pattern analysis.
* **Practical Challenges:** Sharing and securing the one-time pad is difficult.

**9. Cryptanalysis (Breaking Ciphers):**

* **Ciphertext-only attack:** Attacker only has access to ciphertext.
* **Known-plaintext attack:** Attacker has ciphertext and corresponding plaintext.
* **Chosen-plaintext attack:** Attacker can choose plaintext and obtain corresponding ciphertext.

**10. Types of Cryptography:**

* **Symmetric-key cryptography:** Same key for encryption and decryption (e.g., AES).
* **Public-key cryptography:** Separate keys for encryption and decryption (e.g., RSA).
* **Hash functions:** One-way functions that produce a fixed-size output (hash) from variable-length input.

**11. Characteristics of Good Ciphers:**

* **Confusion:** Changing one bit in the key drastically changes the ciphertext.
* **Diffusion:** Changing one bit in the plaintext drastically changes the ciphertext.

**12. Symmetric-Key Cryptography (Block Ciphers):**

* **Block Ciphers:** Operate on fixed-size blocks of data (e.g., AES with 128-bit blocks).
* **Padding:** Adds extra data to messages that are not multiples of the block size.
* **Example (3-bit block cipher):** Uses a lookup table to map 3-bit input blocks to 3-bit output blocks.

**13. Block Cipher Modes of Operation (Cipher Block Chaining - CBC):**

* **CBC:**  Adds the previous ciphertext block to the current plaintext block before encryption to avoid identical ciphertext blocks for identical plaintext blocks.
* **Initialization Vector (IV):** A non-secret value used to encrypt the first block in CBC mode.
* **Example:** Step-by-step walkthrough of CBC encryption and decryption using a 3-bit block cipher.
* **Mathematical representation of CBC:**  Ciphertext<sub>i</sub> = Encrypt(Plaintext<sub>i</sub> XOR Ciphertext<sub>i-1</sub>), where Ciphertext<sub>0</sub> = IV.

**14. Public-Key Cryptography (RSA):**

* **RSA:** A widely used public-key cryptography algorithm.
* **Modular Arithmetic:** Essential for RSA key generation.
* **Key Generation Steps:**
    1. Choose two large prime numbers, p and q.
    2. Calculate n = p * q.
    3. Calculate phi(n) = (p-1) * (q-1).
    4. Choose e such that 1 < e < phi(n) and e is relatively prime to phi(n).
    5. Calculate d such that (d * e) mod phi(n) = 1.
* **Public Key:** (n, e)
* **Private Key:** (n, d)
* **Example:** Step-by-step calculation of RSA keys using small prime numbers.
* **Why RSA Works:** Difficulty of factoring large numbers makes it computationally hard to derive the private key from the public key.

**15. Session Keys (Diffie-Hellman Key Exchange):**

* **Diffie-Hellman:**  Allows two parties to establish a shared secret key over an insecure channel.
* **Steps:**
    1. Alice and Bob agree on public values g and n.
    2. Alice chooses a secret a and calculates A = g<sup>a</sup> mod n.
    3. Bob chooses a secret b and calculates B = g<sup>b</sup> mod n.
    4. Alice sends A to Bob, and Bob sends B to Alice.
    5. Alice calculates the shared key K = B<sup>a</sup> mod n.
    6. Bob calculates the shared key K = A<sup>b</sup> mod n.
* **Example:** Step-by-step calculation of a shared key using Diffie-Hellman.


---

### Exercises & Discussions:

The lecture includes several exercises involving Julius Caesar cipher, polyalphabetic cipher, block cipher, and CBC mode. The instructor encourages students to pause the video and attempt these exercises before proceeding. Detailed solutions are provided in the transcript and summarized above. Common mistakes include confusion between encryption and decryption directions in substitution ciphers and incorrect application of the CBC algorithm.

---

### Important Announcements:

* Homework assignment associated with this lecture is to be completed.
* Additional resources are mentioned in the reading materials, especially regarding public-key cryptography.

---

### Final Takeaways:

* Cryptography is essential for secure communication and data protection.
* Different types of cryptography serve different purposes (confidentiality, integrity, authentication).
* Key management and security are paramount for the effectiveness of any cryptographic system.
* Understanding modular arithmetic is crucial for grasping public-key cryptography concepts.
* The Diffie-Hellman key exchange is a powerful method for establishing secure communication channels.


**Follow-up Actions:**

* Review the lecture slides and notes.
* Complete the associated homework assignment.
* Explore additional resources provided in the reading materials.
* Practice solving more cryptography problems.


**Motivational Note:**  Cryptography is a fascinating and crucial field in today's interconnected world. By mastering these concepts, you are equipping yourself with the knowledge to protect information and ensure secure communication. Keep practicing, and you'll become proficient in this essential skillset.