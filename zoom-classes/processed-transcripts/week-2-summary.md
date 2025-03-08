## Cs. 6,823 Network Security - Class Summary

**Instructor:** Professor Philip Mack

**Date:** Monday, February 3rd, 2025

**Learning Objectives:**

* Understand the complexities of real-world network attacks and the shared responsibility among various parties.
* Grasp the core concepts of network security, including CIA (Confidentiality, Integrity, Availability), authenticity, and non-repudiation.
* Learn about risk management strategies: avoidance, mitigation, transfer, and acceptance.
* Differentiate between qualitative and quantitative risk assessment methods.
* Gain practical experience with session hijacking and reverse shell attacks through Lab 1.

**Instructor's Teaching Approach:** Professor Mack uses a combination of real-world case studies, interactive discussions, practical exercises, and in-class polls to engage students and facilitate a deeper understanding of network security concepts. He encourages active participation and critical thinking.

**Topics Covered:**

* Real-world case study of a Wired magazine writer's account compromise.
* Introduction to core security concepts (CIA, authenticity, non-repudiation).
* Multi-factor authentication (MFA) and its limitations.
* Risk management strategies and trade-offs.
* Qualitative and quantitative risk assessment.
* Detailed explanation of Lab 1 tasks, including session hijacking and reverse shell attacks.

---

### Key Topics

**1. Case Study: Wired Magazine Writer Account Compromise (2012)**

This case study detailed the attack on Matt Honan, a Wired writer with the Twitter handle @mat. The attacker exploited vulnerabilities across multiple systems (Amazon, Apple, Google, Twitter) by leveraging social engineering and weak security practices.

* **Attacker's Approach:**
    * Obtained personal information via WHOIS lookup.
    * Exploited Apple's account recovery process by obtaining the last four digits of the victim's credit card from Amazon.
    * Used the recovered Apple account to reset the victim's Gmail and subsequently the Twitter account.
    * Wiped the victim's devices using Find My iPhone.

* **Key Takeaways:**
    * Chain of vulnerabilities across multiple systems.
    * Importance of strong security practices and user awareness.
    * Shared responsibility among different entities.

**2. Core Security Concepts**

* **CIA Triad:**
    * **Confidentiality:** Protecting sensitive information from unauthorized access.
    * **Integrity:** Ensuring data accuracy and preventing unauthorized modification.
    * **Availability:** Guaranteeing reliable access to data and services.

* **Authenticity:** Verifying the origin of data.  Example: Verifying the sender of an email.

* **Non-Repudiation:** Preventing denial of involvement in a transaction or communication. Example: Using digital signatures.

**3. Multi-Factor Authentication (MFA)**

MFA adds an extra layer of security, but it's not foolproof.

* **MFA Bypass Techniques:**
    * SIM swapping
    * MFA fatigue
    * Session hijacking (cookie stealing)
    * MFA man-in-the-middle (AItM) attacks
    * Exploiting voice call verification

**4. Risk Management**

Risk management involves identifying, assessing, and mitigating potential threats.

* **Four Strategies:**
    * **Avoidance:** Eliminating the risk altogether. Example: Not launching a website with sensitive data.
    * **Mitigation:** Reducing the likelihood or impact of the risk. Example: Implementing strong passwords, encryption, and monitoring.
    * **Transfer:** Shifting the risk to a third party. Example: Purchasing insurance or using a third-party vendor like Stripe.
    * **Acceptance:** Acknowledging and accepting the residual risk after mitigation efforts.

**5. Risk Assessment**

* **Quantitative Risk Assessment:** Uses numerical data to calculate risk. Example: Calculating the annualized loss expectancy (ALE) for fire damage.

* **Qualitative Risk Assessment:** Relies on expert judgment and subjective evaluation. Example: Using the Delphi technique and a risk matrix.

---

### Exercises & Discussions

* **Exercise 1 (Bonus):**  Analyze the Wired writer case study and discuss responsibility among involved parties.
* **Exercise 2 (Bonus):** Provide examples of threat, risk, vulnerability, and exploit.
* **Exercise 3 (In-class):** Assess the risk of an employee losing a laptop with customer data.
* **Exercise 4 (In-class):** Re-assess the risk with additional information about data sensitivity and security measures.
* **Exercise 5 (In-class):** Share reliable cybersecurity news sources.
* **Exercise A (Homework):** Explain the difference between qualitative and quantitative risk assessment.
* **Muddle Points (Optional):** List any unclear concepts and plan for the next week.

---

### Important Announcements

* **Lab 1 Due Date:** February 16th (with flexible submission options).
* **5% Bonus:** For early Lab 1 submission (5 days early).
* **5% Bonus each:** For automating tasks 2 and 3 in Lab 1.
* **Homework 1:** Due date not specified, but expected to achieve 100%.
* **TA Office Hours:** Tuesdays, 6-7 PM (tentative).
* **Communication:** Use Slack for questions outside of TA office hours.
* **Recommended Resource:** GitHub Student Pack (for free DigitalOcean credits).

---

### Final Takeaways

* Security is a continuous process, not a product.
* Attackers only need to find one vulnerability, while defenders must protect against all.
* Risk management is crucial for effective cybersecurity.
* Understanding the shared responsibility model in cloud environments is essential.

**Follow-up Actions:**

* Review CIA triad, authenticity, and non-repudiation concepts.
* Research different MFA bypass techniques.
* Practice risk assessment using both qualitative and quantitative methods.
* Explore different cybersecurity news sources.
* Complete Lab 1 and Homework 1.

**Motivational Note:**  Cybersecurity is a constantly evolving field. Stay curious, keep learning, and apply what you've learned to protect yourself and your organization from emerging threats.  The skills and knowledge you gain in this course will be invaluable in today's digital landscape.