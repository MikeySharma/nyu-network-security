## CS 6823: Network Security - Class Summary

**Instructor:** Professor Philip Mack

**Date:** Monday, January 27, 2025

**Introduction:**

This comprehensive summary covers the first class of the Spring 2025 Network Security course.  The primary learning objective is to equip students with the knowledge and skills to understand and address the complexities of network security in today's interconnected world. Professor Mack, a seasoned cybersecurity professional with 20 years of experience, aims to empower students to analyze real-world security incidents, engage in informed discussions about cybersecurity, and apply practical skills using tools like Nmap and Metasploit.  The course will cover both offensive and defensive aspects of network security, including hacking techniques, network protocols, cryptographic algorithms, attack and defense methods, and advanced topics like firewalls, TLS, and wireless security. The instructor emphasizes the ethical implications of the skills taught, strictly forbidding unauthorized use on any system.

**Key Topics:**

* **Instructor Background:** Professor Mack provided a detailed overview of his extensive experience in cybersecurity, including roles as a cybersecurity officer at a major international organization, Security Operations Center (SOC) manager for a US agency, cybersecurity lead at the Department of Defense, and network communications specialist at the New York Stock Exchange.  He also highlighted his educational background, holding a master's degree from New York University, obtained through a DoD scholarship. This background emphasizes the practical, real-world focus of the course.

* **Course Overview and Objectives:** The course aims to provide a deep understanding of network security principles, enabling students to analyze network architectures, discuss security strategies, and understand real-world security breaches. The objective extends beyond theoretical knowledge to include practical skills, such as using penetration testing tools, understanding vulnerabilities, and exploiting and mitigating them.

* **Ethical Considerations:**  The instructor strongly emphasized the ethical boundaries of the skills taught.  Students are explicitly prohibited from using these techniques on systems without explicit permission.  The course focuses on responsible and ethical hacking practices.

* **Network Security vs. Other Computer Science Disciplines:**  A core concept discussed was the unique nature of network security compared to other computer science fields. While other disciplines often focus on *positive requirements* (how to build or implement something), cybersecurity emphasizes *negative requirements* (how to prevent undesired actions).  This shift in perspective requires a different mindset, focusing on potential vulnerabilities and how to mitigate them.  The example of securing a database against unauthorized access illustrated this complexity.

* **TCP Three-Way Handshake and Sync Flood Attack:** The class delved into the mechanics of the TCP three-way handshake (SYN, SYN-ACK, ACK) and how it can be exploited through a SYN flood attack.  The small size of SYN packets (40 bytes) makes them easy to generate in large volumes, overwhelming a server's resources.  The concept of SYN cookies as a mitigation technique was introduced, where the server delays resource allocation until a valid response containing the SYN cookie is received.

* **TCP Reset Attack:** Another key topic was the TCP reset attack, a technique used to disrupt existing TCP connections. The attacker injects a specially crafted TCP reset packet into the communication stream, causing the connection to terminate.  The importance of correctly identifying the sequence and acknowledgment numbers was highlighted.  A bonus challenge for Lab 1 involves automating this attack.

**Exercises & Discussions:**

* **Weekly Bonus Exercise 1 (Question 1):** Students brainstormed ways to hack a database account, assuming forgotten credentials.  Various techniques were discussed, including:
    * **Brute force:** Trying different password combinations.
    * **Default password check:** Exploiting default passwords.
    * **SQL Map:** Using tools to extract information from unsecured databases.
    * **Credential stuffing:** Reusing passwords leaked from other websites.
    * **John the Ripper:** Cracking password hashes.
    * **Sniffing:** Capturing network traffic to obtain credentials.
    * **SQL injection:** Exploiting vulnerabilities in database queries.
    * **Phishing:** Tricking users into revealing their credentials.
    * **Token spoofing/Replay attack:** Stealing and reusing authentication tokens.
    * **Dictionary attack/Rainbow tables:** Using precomputed tables to crack passwords.
    * **Exploiting password reset procedures:** Using social engineering or other techniques to reset passwords.

* **Weekly Bonus Exercise 1 (Question 2):** Students considered the outcome of sending a TCP reset packet with incorrect sequence/acknowledgment numbers. The answer: the packet is ignored.

* **Weekly Bonus Exercise 1 (Exercise 3):** Students were instructed to join the Slack workspace, introduce themselves, and share relevant information.

* **Weekly Bonus Exercise 1 (Exercise A):** Students were tasked with analyzing a recent cybersecurity news article about a hack and providing their insights.

* **Muddiest Points:** Students were encouraged to document any unclear concepts or questions from the class.

**Important Announcements:**

* **Textbook:** *Internet Security: A Hands-on Approach*, 3rd Edition by Renning Du is required.  The Amazon link was provided.  The 3rd edition is necessary due to a new chapter not present in the 2nd edition.

* **Course Website:** Brightspace is the primary platform for course materials, including the syllabus, lecture slides, assigned readings, and announcements.

* **Seed Labs:** Seed Labs is the virtual environment used for lab assignments. Setup options include:
    * **VirtualBox:** For relatively new computers (within the last 6 years).
    * **VMware Workstation:** For Apple Silicon Macs.
    * **Cloud Options:** DigitalOcean (recommended for beginners, with $200 credit via GitHub Student Developer Pack) or Microsoft Azure (for experienced cloud users, with $100 credit).

* **Grading:**
    * Homeworks & Quizzes (3 homeworks, 1 quiz): 10%
    * Lab Assignments (Seed Labs): 40%
    * Midterm Exam: 25%
    * Final Exam: 25%
    * Bonus Exercises: 2%

* **Assignments:**
    * **Homework 1 (Immersive Labs):** Due two days after the final exam (May 12, 2025).  Registration must be done through a specific link using the NYU email address.
    * **Lab 1 (Seed Labs):** Due February 16, 2025.  Early submission bonus (5% for 5 days early) and late submission penalty (1% per day) apply.  Bonus points are available for automating parts of the lab.

* **Exams:**  Midterm exam on March 15, 2025 (Saturday), and final exam on May 10, 2025 (Saturday).  Start time between 10 AM and 12 PM, with a 2-hour duration.  The exam format (open book/notes, proctored, use of Lockdown Browser) will be announced later.

* **Class Schedule:** Primarily Mondays, with a shift to Tuesday for President's Day week.  Spring break on March 24, 2025.  The full schedule is available on Brightspace.

* **Communication:**  Slack is the preferred communication method.  Email and Brightspace messages are also acceptable.  Appointments can be made for one-on-one Zoom meetings.

* **Excused Absence Form:**  Students must fill out this form for any absence related to illness, family obligations, or work emergencies.

* **Academic Honesty:** The course follows a three-strike policy for academic dishonesty and plagiarism.  Generative AI tools like ChatGPT are permitted for learning and understanding concepts, but submitting AI-generated work is considered academic dishonesty.  AI is strictly prohibited during exams.

**Final Takeaways:**

This class provided a foundational understanding of network security principles and introduced key concepts related to network attacks and defenses. Students should prioritize setting up their Seed Labs environment and starting on Lab 1.  It's crucial to review networking fundamentals, programming concepts, and Linux commands if needed. Engaging with the Immersive Labs exercises and staying active on Slack will further reinforce learning.  This course promises to be challenging but rewarding, providing valuable skills for a career in cybersecurity.  Remember to budget sufficient time for the lab assignments and actively participate in class discussions and exercises.