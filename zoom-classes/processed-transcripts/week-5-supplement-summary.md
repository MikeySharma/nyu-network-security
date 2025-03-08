## CS H2, H3 Network Security - Lecture 5: Cryptography - Summary

**Instructor:** Professor Philip Mac

**Date:** (Date not explicitly mentioned in the transcript)

**Learning Objectives:**

* Understand fundamental cryptographic concepts, including plain text, ciphertext, algorithms, and keys.
* Explore the history of cryptography, from Caesar ciphers to Enigma machines.
* Learn about symmetric key cryptography, including block ciphers, AES, and block chaining.
* Understand public key cryptography and its application in RSA.
* Learn how to generate RSA keys.
* Explore the concept of session keys and the Diffie-Hellman key exchange.
* Apply these concepts through various exercises and examples.

**Instructor's Teaching Approach:**

Professor Mac utilizes a pre-recorded video lecture format, incorporating pauses for individual exercises and problem-solving activities. The emphasis is on self-learning and understanding the concepts before moving on to the next topic.  The instructor uses a combination of historical examples, definitions, algorithms, and practical exercises to explain complex cryptographic concepts.

**Overview of Topics Covered:**

This lecture covers the fundamentals of cryptography, starting with basic definitions and historical context.  It then delves into symmetric and public key cryptography, exploring different algorithms and their applications.  The lecture also introduces message integrity, digital signatures, and the importance of key exchange using Diffie-Hellman.  The relevance of these topics lies in their crucial role in securing modern communication systems and protecting sensitive data.

---

### Key Topics:

**1. Introduction to Cryptography:**

* **Plaintext:** Unencrypted text, readable and understandable.
* **Ciphertext:** Encrypted text, unreadable without the decryption key.
* **Algorithm:** A set of rules or steps for encrypting and decrypting data.
* **Key:** A secret value used in conjunction with the algorithm to encrypt or decrypt data.
* **Example:** AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm.  The algorithm is public, but the key is kept secret.

**2. History of Cryptography:**

* **Caesar Cipher:** One of the earliest ciphers, based on shifting letters in the alphabet.
    * **Example:** A shift of +3 would encrypt "HELLO" as "KHOOR".
* **Zimmerman Telegram (WWI):** An example of early cryptographic use in warfare, where numbers represented words in a secret book.  This cipher was eventually broken due to plaintext-ciphertext pairs being revealed.
* **Enigma Machine (WWII):** A sophisticated encryption machine using rotating rotors to change the encryption algorithm with each keypress.  The lecture highlights the complexity of this machine and the difficulty in breaking its encryption.

**3. Goals of Cryptography:**

* **Confidentiality:** Ensuring that only authorized users can read messages.
* **Integrity:** Protecting messages from alteration during transit.
* **Authentication:** Verifying the identity of the sender and receiver.
* **Non-repudiation:** Preventing denial of message sending (origin) or the time of sending (time).

**4. Cryptographic Terminology:**

* **Alice, Bob, and Trudy:** Common placeholders used to represent communicating parties (Alice and Bob) and an attacker (Trudy).
* **M:** Represents the plaintext message.
* **K:** Represents the key.  K<sub>a</sub>M denotes message M encrypted with key a.

**5. Simple Encryption Scheme:**

* Involves simple substitution of one letter for another.  The example in the transcript appears to be flawed, but the intended concept is explained.

**6. Polyalphabetic Encryption Scheme:**

* A substitution cipher where the substitution changes with each letter based on a key.
* **Example:** Using a table with plaintext on one axis and the key on the other. The ciphertext is found at the intersection of the plaintext letter and the corresponding key letter.  The lecture provides detailed examples of encryption and decryption using this scheme.

**7. Vigenère Cipher:**

* Similar to a polyalphabetic cipher, but using a keyword to generate a repeating keystream. The Enigma machine can be viewed as a complex implementation of this concept.

**8. One-Time Pad:**

* Considered the perfect encryption scheme, using a truly random key that is as long as the message and used only once.  Practical limitations are discussed, such as the difficulty of securely sharing the one-time pad.

**9. Breaking Cryptographic Schemes:**

* **Ciphertext-only attack:** Attacker only has access to ciphertext.
* **Known-plaintext attack:** Attacker has access to both plaintext and ciphertext.
* **Chosen-plaintext attack:** Attacker can choose plaintext and obtain corresponding ciphertext.

**10. Types of Cryptography:**

* **Symmetric Key Cryptography:** Uses the same key for encryption and decryption.  Challenges include secure key exchange.
* **Public Key Cryptography:** Uses two keys – a public key for encryption and a private key for decryption.  Enables secure communication without prior key exchange.
* **Hash Functions:** One-way functions that produce a fixed-size output (hash) from any input.  Used for data integrity checks and digital signatures.

**11. Symmetric Key Cryptography (Detailed):**

* **Stream Ciphers:** Encrypt data one bit at a time.
* **Block Ciphers:** Encrypt data in fixed-size blocks (e.g., AES with 128-bit blocks).
    * **Block Chaining (CBC):**  A technique to avoid identical ciphertext blocks when encrypting identical plaintext blocks.  The lecture provides a detailed explanation of CBC with examples and diagrams.

**12. Public Key Cryptography (Detailed):**

* **RSA (Rivest-Shamir-Adleman):** A widely used public-key algorithm.
    * **Key Generation:**  The lecture provides a five-step process for generating RSA keys, including choosing prime numbers, calculating n and phi, selecting e and d, and forming the public and private keys.  Detailed examples are worked through, illustrating the calculations involved.
    * **Modular Arithmetic:**  The lecture explains the use of modular arithmetic in RSA and provides examples of how to perform these calculations efficiently.

**13. Session Keys and Diffie-Hellman Key Exchange:**

* **Diffie-Hellman:**  A method for securely exchanging keys over an insecure channel without prior shared secrets.  The lecture explains the steps involved in the Diffie-Hellman exchange with a detailed example.

---

### Exercises & Discussions:

The lecture includes several exercises interspersed throughout, focusing on applying the concepts learned.  These exercises cover Caesar ciphers, simple substitution ciphers, polyalphabetic ciphers, block ciphers, and modular arithmetic.  Professor Mac encourages students to pause the video and attempt the exercises before continuing.  Detailed solutions and explanations are provided for each exercise.

---

### Important Announcements:

* Homework assignment associated with this lecture should be completed.
* Additional resources, such as readings and links for further research, are mentioned but not explicitly listed in the transcript.

---

### Final Takeaways:

This lecture provides a comprehensive overview of fundamental cryptographic concepts.  Key takeaways include understanding the different types of cryptography, the importance of key management, the workings of various algorithms, and the practical applications of cryptography in securing communication.

**Follow-up Actions:**

* Complete the associated homework assignment.
* Review the lecture slides and notes.
* Explore the additional resources mentioned by the instructor.
* Practice the exercises and examples to solidify understanding.
* Research and explore related topics like digital signatures and message authentication codes.

**Motivational Note:**

Cryptography is a fascinating and essential field in today's digital world.  By understanding these principles, you gain a deeper appreciation for the security measures that protect our information and enable secure communication.  Continue exploring and learning to become more proficient in this critical area.