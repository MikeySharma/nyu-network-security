## CS 6.823 Network Security - Class Summary

**Instructor:** Professor Philip Mack

**Date:** Monday, February 3rd, 2025

**Learning Objectives:**

* Understand the complexities of real-world network attacks and the responsibilities of various parties involved.
* Grasp the core concepts of cybersecurity, including CIA (Confidentiality, Integrity, Availability), authenticity, non-repudiation, and risk management.
* Learn about different types of attacks, including denial-of-service, TCP reset, and session hijacking.
* Apply these concepts practically through lab exercises involving simulated attacks and defenses.
* Understand risk analysis and management principles, including qualitative and quantitative approaches.

**Instructor's Teaching Approach:** Professor Mack employed a highly interactive approach, using real-world case studies, thought-provoking questions, in-class polls, and practical lab exercises to illustrate key concepts. He encouraged active student participation and discussion throughout the class.

**Topics Covered:**

* Real-world case study of a complex network attack
* Introduction to cybersecurity principles (CIA, authenticity, non-repudiation)
* Risk management strategies
* Lab 1 overview and detailed explanation of tasks 3 and 4
* Risk analysis and management, including qualitative and quantitative assessments

---

### Key Topics

**1. Real-World Case Study: Matt Honan's Account Takeover (2012)**

This case study analyzed the attack on Wired writer Matt Honan, where his Twitter account, email, and devices were compromised. The attack involved exploiting vulnerabilities across multiple platforms (Google, Apple, Amazon, Twitter) through a chain of social engineering and technical exploits.

* **Attacker's Steps:**
    1. Obtained personal information through Whois lookup and social media.
    2. Used Google account recovery to identify Honan's me.com address (partially).
    3. Exploited Apple's account recovery process by obtaining the last four digits of Honan's credit card from Amazon.
    4. Called Amazon, added a new credit card, and then used this information to reset Honan's Amazon account.
    5. Accessed Amazon account to retrieve the last four digits of Honan's other credit cards.
    6. Called Apple, provided necessary information (including credit card details), and reset Honan's me.com account.
    7. Used me.com access to reset Google and Twitter accounts.
    8. Wiped Honan's devices using Find My iPhone.

* **Discussion on Responsibility:**  A class poll revealed that students attributed the most responsibility to Amazon, followed by the attacker and then the user. Professor Mack argued that while the attacker bears the primary responsibility, the companies involved also share responsibility due to their security practices and risk acceptance.  He emphasized that security is a trade-off between cost, usability, and risk.

**2. Cybersecurity Principles**

* **CIA Triad:** Confidentiality, Integrity, and Availability.
* **Authenticity:** Ensuring data originates from a verified source.
* **Non-Repudiation:** Preventing denial of sending a message or performing an action. Example: Digital signatures.

**3. Risk Management**

* **Four Strategies:**
    * **Avoidance:** Eliminating the risk entirely (e.g., not driving to avoid car accidents).
    * **Mitigation/Treatment:** Reducing the likelihood or impact of the risk (e.g., seatbelts, airbags).
    * **Transfer:** Shifting the risk to another party (e.g., insurance).
    * **Acceptance:** Acknowledging and accepting the residual risk after mitigation.

* **Examples:** Driving a car, launching a website with sensitive information.

**4. Lab 1 Overview (Tasks 3 & 4)**

* **Task 3: Session Hijacking**
    * Goal: Hijack a Telnet session between Alice and Bob by sending a malicious command (e.g., `touch virus.txt`).
    * Hint: Guess the next sequence and acknowledgment (ACK) number.  Try the current values or swap them.
    * Automation Bonus (5%): Automate the process using Python and Scapy, avoiding hardcoded values.

* **Task 4: Reverse Shell**
    * Goal: Send a command to Bob, forcing a connection back to the attacker's machine (Netcat listener).
    * This establishes a persistent connection for further commands, mimicking real-world attacks.

**5. Risk Analysis and Management (Qualitative and Quantitative)**

* **Quantitative Risk Assessment:** Uses numbers and formulas to assess risk.
    * **Single Loss Expectancy (SLE):** Cost of a single incident.
    * **Annualized Rate of Occurrence (ARO):** How often the incident occurs per year.
    * **Annualized Loss Expectancy (ALE):** SLE * ARO
    * **Example:** Calculating the cost-benefit of a fire alarm system.

* **Qualitative Risk Assessment:**  Uses subjective judgment and expert opinions when numerical data is unavailable.
    * **Risk Matrix:**  A visual representation of risk based on likelihood and consequence.
    * **Delphi Technique:**  Gathering anonymous expert opinions to reach consensus on risk assessment.
    * **Example:** Assessing the risk of a buggy software application.

---

### Exercises & Discussions

* **Weekly Bonus Exercise 2:**
    * Question 1: Identify the parties involved in the Matt Honan attack and discuss their responsibilities.
    * Question 2: Who is ultimately responsible for the attack?

* **Exercise 2:** Provide examples of threat, risk, vulnerability, and exploit.

* **Exercise 3 & 4:** Assess the risk of an employee losing a laptop with customer data, considering different scenarios and mitigation strategies.

* **Exercise 5:** Share resources for staying updated on cybersecurity news.

* **Exercise A (Homework):** Explain the difference between qualitative and quantitative risk assessment with examples.

* **Muddle Points (Optional):**  Identify confusing topics and plan for next week's learning.

---

### Important Announcements

* **Lab 1 Due Date:** February 16th (with flexible submission options: +5% for 5 days early, -1 point per day for up to 10 days late).
* **Homework 1:** Using Immersive Labs (expected 100%).
* **TA Office Hours:** Tuesdays, 6-7 PM (tentative).
* **Communication:** Use Slack for questions outside of office hours.
* **Lab 1 Bonus:** 5% each for automating tasks 2 and 3.
* **Cloud Lab Setup:**  Use GitHub Student Pack ($200 credit for DigitalOcean) and NYU VPN.

### Additional Resources

* Wikipedia (for CIA triad, etc.)
* Textbook (for Netcat information)

---

### Final Takeaways

* Security is a continuous process, not a one-time product purchase.
* Attackers only need to find one vulnerability, while defenders must protect against all.
* Risk management is crucial for effective cybersecurity.
* Mfa is essential but not foolproof.  Various attack vectors exist (SIM swapping, MFA fatigue, session hijacking, MITM).
* Continuous monitoring and defense in depth are essential security practices.

### Follow-up Actions

* Review the concepts of CIA, authenticity, non-repudiation, and risk management.
* Complete Lab 1 and Homework 1.
* Research and explore different cybersecurity news sources.
* Reflect on the Matt Honan case study and consider the implications for personal and organizational security.

### Motivational Note

Cybersecurity is a constantly evolving field, and staying informed and proactive is crucial.  By applying the principles and techniques learned in this class, you can contribute to a more secure digital world. Don't be afraid to experiment and learn from your mistakes in the lab environment.  This hands-on experience will be invaluable as you progress in your cybersecurity journey.