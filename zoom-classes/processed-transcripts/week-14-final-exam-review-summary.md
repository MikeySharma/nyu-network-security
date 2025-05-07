Okay, this is going to be a long and detailed summary, as requested!

## Class Summary: CS 6823 Network Security

**Class Subject:** CS 6823 Network Security
**Instructor Name:** Professor Philip Mack
**Date:** Monday, May 5, 2025
**Class Week:** Week 14 (Last Class - Final Review)

---

### 1. Introduction

**Learning Objectives:**
The primary learning objective for this final class session was to conduct a comprehensive review of topics covered after the midterm exam, in preparation for the upcoming final exam. A significant portion of the class was also dedicated to explaining the logistics, rules, and technical requirements for taking the final exam, including the use of Respondus Lockdown Browser and Monitor. The instructor aimed to ensure students understood what material would be on the exam, how to prepare, and what conduct was expected.

**Instructor's Teaching Approach:**
Professor Mack's approach for this session was a combination of direct instruction for exam logistics and a guided review of key concepts. For the review, he presented important topics, posed questions to stimulate student thinking (though not collected), and walked through explanations and diagrams. He emphasized understanding the "how" and "why" behind concepts rather than rote memorization, especially for topics like Diffie-Hellman where calculations were explicitly excluded from the exam. He also actively engaged with student questions and clarifications throughout the lecture.

**Topics Covered and Relevance:**
The class covered two main areas:
1.  **Final Exam Logistics:** This included the exam schedule, scope of material, open-book/open-notes policy, restrictions (no free internet, no collaboration), academic integrity (plagiarism, AI tool usage), procedures for sickness, and a detailed walkthrough of the Respondus Lockdown Browser + Monitor setup and requirements, including a mandatory practice quiz. This information is critically relevant for students to successfully and appropriately take the final exam.
2.  **Review of Post-Midterm Topics:**
    *   **Lesson 6: PKI, Message Integrity, and TLS:** Diffie-Hellman, encryption vs. hashing, playback attacks, nonces, digital signatures, HMAC, PKI concepts (CAs, certificate chains, X.509 certificates, validation), Perfect Forward Secrecy (PFS), and the TLS handshake (versions 1.2 and 1.3).
    *   **Lesson 7: IPtables Firewalls:** Firewall definitions, proxies, application gateways, and a deep dive into IPtables (input, output, forward chains, default policies, stateful rules with `conntrack`).
    *   **(Briefly Mentioned for Scope):** Lesson 8 (Layer 2 Security) and Lesson 9 (Wireless Security) are on the exam but were not specifically reviewed in this session.
    These topics are highly relevant as they form the core of modern network security practices and will be directly assessed on the final exam.

---

### 2. Key Topics

#### A. Final Exam Logistics and Academic Integrity

*   **Exam Schedule:**
    *   Date: Saturday, May 10th, 2025.
    *   Start Time: Students can start the exam anytime between 10:00 AM and 12:00 PM (noon).
    *   Duration: 2.5 hours from the moment the student starts the exam. The exam will auto-submit when the timer ends.
*   **Covered Material (Post-Midterm):**
    *   Lesson 6: PKI, Message Integrity, and TLS.
    *   Lesson 7: IPtables, Firewalls.
    *   Lesson 8: Layer 2 Security.
    *   Lesson 9: Wireless Security.
    *   Weekly Videos: 8, 9, 10, 11, 12, 13, and 14 (this review session).
    *   Pre-recorded Firewall Video.
    *   Labs: #3 and #4.
    *   Homework: #3 and the second half of Homework #1 (Immersive Labs).
    *   All associated reading materials.
*   **Exam Format and Allowed Resources:**
    *   **Open Book/Open Notes:** Students can use their physical textbook and any notes they have printed out (typed or handwritten).
    *   **No Free Internet/Collaboration:** General internet browsing is prohibited. Collaboration in any form (talking, texting, shared websites) is strictly forbidden.
    *   **Allowed Digital Resources (via Lockdown Browser):**
        *   Course slides (PDFs).
        *   Reading materials provided for the course.
        *   Man pages for any command-line tools discussed (e.g., IPtables flags – memorization not strictly needed but expected due to practice).
        *   Wikipedia (for looking up concepts, e.g., ARP).
        *   Gradescope (to review own submitted materials).
        *   *Correction by Professor:* Videos are **NOT** available during the exam.
*   **Sickness Policy:**
    *   If a student is sick on exam day, they should **not** take the exam.
    *   They must make a doctor's appointment and obtain a doctor's note.
    *   The doctor's note should be submitted to the Office of Student Advocacy.
    *   The student must also inform Professor Mack.
*   **Academic Integrity – Student Code of Conduct:**
    *   **Plagiarism:**
        *   Defined as copying anything from anywhere without attribution. This applies to both direct text and ideas.
        *   While Wikipedia is accessible, answers should **not** be copied and pasted. The professor stated that no exam questions are designed for direct copy-paste answers from sources like Wikipedia.
    *   **ChatGPT and other AI Tools:** Use of such tools is **not allowed** and will be considered plagiarism.
    *   **Collaboration:** Any form of collaboration during the exam is strictly prohibited.

#### B. Respondus Lockdown Browser + Monitor

*   **Functionality:** This software takes control of the student's computer screen, webcam, and microphone to monitor the exam environment.
*   **Installation Requirements:**
    *   Requires administrator rights to install.
    *   Linux is **not** supported.
    *   Older operating systems (e.g., Windows 7) may not be supported.
*   **Alternative Proctoring:** If Respondus doesn't work (e.g., due to OS incompatibility, company computer restrictions), students must contact Professor Mack *before the exam* to schedule an alternative proctoring session via Zoom. Students should provide their availability.
*   **Environment During Exam:**
    *   **Quiet Place:** The exam must be taken in a quiet location.
    *   **No Voices/Loud Noises:** The software flags sections with voices or other loud sounds for review by the professor. If voices are detected, the student will receive a zero on the exam. Students must inform housemates/roommates and ensure they do not enter the room or speak loudly.
*   **Electronic Devices:**
    *   No other electronic devices (second computer, phone, tablet) are allowed during the exam.
    *   **Exception:** A phone may be used *briefly and visibly* during the login screen for Gradescope if a password manager on the phone is needed. The login screen must be visible on the computer monitor when the student looks at their phone to avoid suspicion. This action will likely trigger a flag, which the professor will review.
*   **Mandatory Practice Quiz:**
    *   A practice quiz named "Practice for the final" is available on Brightspace under "Quizzes."
    *   Students **must** complete this practice quiz to test their system and familiarize themselves with the Respondus startup procedure (webcam check, environment scan, etc.).
    *   Completing this practice quiz is a prerequisite for accessing the actual final exam.
    *   The practice quiz interface will show:
        1.  Instructions.
        2.  A button to "Download Respondus Lockdown Browser" and then "Begin."
        3.  Once started, a timer (2.5 hours for the actual exam) will be visible.
        4.  Links to allowed resources (course PDFs, Wikipedia, Gradescope, IPtables man pages, sample final questions/answers) will be available within the Lockdown Browser environment.

#### C. Review Topic 1: Diffie-Hellman Key Exchange

*   **Core Concept:** Enables two parties (Alice and Bob) to establish a shared secret key (K) over an insecure channel, even if an eavesdropper (Trudy) observes all exchanged messages.
    *   Alice chooses a private key `a`, computes public key `A = G^a mod N`.
    *   Bob chooses a private key `b`, computes public key `B = G^b mod N`.
    *   (G and N are public parameters, agreed upon beforehand).
    *   Alice sends A to Bob; Bob sends B to Alice.
    *   Alice computes `K = B^a mod N`.
    *   Bob computes `K = A^b mod N`.
    *   Both arrive at the same `K = G^(ab) mod N`.
*   **Exam Focus:** No calculations required, but a deep understanding of its workings, vulnerabilities, and protections is essential.
*   **Protection of Exchanged Values (G, N, A, B):**
    *   