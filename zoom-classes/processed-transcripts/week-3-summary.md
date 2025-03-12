## Comprehensive Summary of Network Security Class

**Subject:** CS 6823 - Network Security
**Instructor:** Professor Philip Mack
**Date:** Monday, February 10th, 2025 (Note: Transcript mentions both 2024 and 2025. Assuming 2025 based on context)

**Introduction:**

This class focused on network reconnaissance, the first step in the cyber kill chain.  The learning objectives were to understand both technical and non-technical methods of information gathering, including open-source intelligence (OSINT) techniques like Whois lookups, DNS reconnaissance, understanding TCP/IP headers, and an introduction to Nmap.  Professor Mack employed a practical, demonstration-heavy approach, using real-world examples and live demonstrations to illustrate the concepts.  The relevance of these topics stems from the crucial role reconnaissance plays in any cyber attack, providing attackers with the necessary information to plan and execute their attacks effectively.

**Key Topics:**

1. **Logistics and Reminders:**
    * Lab 1 due Sunday, February 16th (5% bonus for submission by Tuesday, February 11th).
    * Homework 1 (Immersive Labs) due at the end of the semester (work on it weekly).
    * TA office hours: Tuesdays, 8-9 PM Eastern Time on Zoom (check Brightspace for schedule).
    * Next class on Tuesday, February 18th (due to President's Day).

2. **Weekly Bonus Exercise 3:**
    * Question 1: List three topics discussed last week (Risk Management, Qualitative and Quantitative Risk Assessment, Delphi Technique).

3. **Introduction to Exploitation and Patch Tuesday:**
    * The class will cover exploiting systems, hacking Wi-Fi, finding vulnerabilities, and using exploitation frameworks.
    * Patch Tuesday (the second Tuesday of each month) is when Microsoft releases security patches.
    * Attackers reverse-engineer these patches to identify vulnerabilities and develop exploits.
    * Many organizations have a delay in patching systems (2-4 weeks), leaving them vulnerable.
    * Example: Recent Outlook vulnerability allowing code execution via email preview pane.
    * Metasploit: A framework for exploiting known vulnerabilities.
    * **Warning:** Skills taught are only for use in controlled environments (e.g., UC Labs).  Illegal activities will result in legal consequences.

4. **Types of Attacks and Computer Crimes:**
    * Definitions of various attack types (DoS, DDoS, destruction of information, dumpster diving, eavesdropping, embezzlement, espionage, fraud, information warfare, illegal content, malicious code, masquerading, social engineering, software piracy, IP address spoofing, terrorism, theft of passwords, exploit scripts, network intrusions).

5. **Motivation for Attacks:**
    * Reasons behind cyber attacks include political motives, financial gain, and (less commonly now) fame.

6. **US Federal Crime Laws:**
    * Overview of US computer crime laws (not tested on in the course).

7. **The Cyber Kill Chain:**
    * Seven steps: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Action on Objectives.
    * Importance of breaking the chain at any point to prevent a successful attack.
    * DHS uses the cyber kill chain to evaluate security tools.

8. **Mitre Attack Framework:**
    * A taxonomy of attacker techniques, providing a comprehensive view of potential attack vectors.
    * Useful for identifying areas needing stronger security measures and detection tools.

9. **Reconnaissance (Casing the Joint):**
    * Gathering information about the target, including IP addresses, network topology, domain names, account names, operating systems, database servers, security policies, physical security, employee information, etc.
    * Additional information attackers might seek: job postings, ex-employee accounts, laptop types, website lists, DMZ systems, employee hangouts, domain expiration dates, recent mergers/acquisitions.

10. **Public Information Sources:**
    * Public databases, dumpster diving, social engineering, DNS information, physical break-ins.
    * Example: Stealing backup tapes.
    * Caller ID Spoofing: Easy to perform with an ISDN number.  Used in scams impersonating police, IRS, or ICE.  Attempts to fix this issue (e.g., verified caller badges) are not fully effective.

11. **Google Hacking:**
    * Using Google search operators to find sensitive information.
    * `site:` operator to restrict searches to a specific website (e.g., `site:nyu.edu`).
    * Example: Finding Nessus scan reports on a specific domain.
    * Nessus: A popular vulnerability scanning tool.
    * Metasploit: A framework for exploiting known vulnerabilities.
    * Exploit-DB: A database of exploits.

12. **Google Hacking Database (GHDB):**
    * A repository of Google dorks (specialized search queries) for finding vulnerabilities and sensitive information.
    * Example: Finding database credentials using `filetype:sql "insert into users values"`.

13. **Edgar Database:**
    * SEC database with filings from publicly traded companies, containing valuable information about financials, executives, legal counsel, vendors, etc.

14. **Maltego:**
    * OSINT tool that finds relationships between entities (e.g., email addresses, social media accounts, websites).
    * Uses scripts to query various online sources and build a graph of connections.
    * Powerful for background checks and competitor research.

15. **Social Media Intelligence:**
    * Tools for gathering information from social media platforms.
    * Creepy (cree.py): A tool (no longer functional) that used to map user locations based on social media posts.

16. **Whois Lookups:**
    * Tool for finding domain registration information (often obscured by privacy guards now).
    * Historically used to find contact information, but now primarily used for spam and targeted advertising.

17. **DNS Reconnaissance:**
    * DNS: Translates domain names to IP addresses.
    * ARIN: American Registry for Internet Numbers, responsible for assigning IP addresses in North and South America.
    * Live demo using ARIN and Whois to find information about NYU (IP addresses, physical addresses, email addresses, phone numbers).
    * DNS Record Types:
        * **A:** IPv4 address.
        * **AAAA:** IPv6 address.
        * **TXT:** Text records (often used for SPF email security).
        * **CNAME:** Canonical name (alias).
        * **PTR:** Pointer record (reverse lookup).
        * **NS:** Name server.
        * **MX:** Mail exchange.
    * Example: Discovering that `engineering.nyu.edu` is hosted on AWS, `brightspace.nyu.edu` is hosted by Brightspace (which uses AWS), `albert.nyu.edu` is hosted on-premise, `hosting.nyu.edu` is hosted on DigitalOcean, and `stream.nyu.edu` uses Cloudflare.
    * Cloudflare: A CDN and security service that protects against DDoS attacks.

18. **DNS Dumpster:**
    * Automated tool for performing DNS reconnaissance and visualizing relationships between domains.

19. **Traceroute:**
    * Tool that shows the path (hops) between a source and destination IP address.
    * Example: Traceroute to `nyu.edu` revealed a Palo Alto next-generation firewall (NGFW) on VLAN 3090.
    * Importance of clear naming conventions for network devices for troubleshooting purposes.

20. **Shodan:**
    * "Internet of Things" search engine (discussed next week).

**Exercises & Discussions:**

* **Exercise 2:** Finding a specific file on `nyu.edu` using Google search (solution: `site:nyu.edu "This file was generated by Nessus"`).
* **Exercise 3:** Listing ways to obtain information from a company using public sources (e.g., Edgar, ARIN, Whois, DNS Dumpster, Google Hacking).
* **Exercise 4:** Differentiating between DNS and Whois and the information each provides.  DNS translates domain names to IP addresses, while Whois provides domain registration information.

**Important Announcements:**

* Lab 1 due date and bonus.
* TA office hours.
* Next class on Tuesday.

**Final Takeaways:**

* Reconnaissance is a critical first step in the cyber kill chain.
* Numerous OSINT tools and techniques are available for gathering information about targets.
* Understanding DNS and its various record types is crucial for network reconnaissance.
* Ethical considerations and legal limitations apply to the use of these techniques.

**Follow-up Actions:**

* Research Shodan.
* Complete Exercise 4A: Explain three methods used for network reconnaissance and provide a security measure to mitigate the risk associated with each method.

**Motivational Note:**

The skills and knowledge gained in this class are powerful and can be used for both offensive and defensive security purposes.  By understanding how attackers gather information, you can better protect your own systems and networks. Continue exploring these tools and techniques responsibly and ethically, and you'll be well on your way to becoming a skilled cybersecurity professional.