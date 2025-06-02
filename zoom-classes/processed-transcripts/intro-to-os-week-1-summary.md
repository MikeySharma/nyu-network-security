## Operating Systems - Summer Cyber Fellows Class Summary

**Instructor:** Aspen Olmsted
**Date:** May 26, 2024

### 1. Introduction

This summary encapsulates the key points discussed in the introductory session of the Operating Systems class for the Summer Cyber Fellows program. Aspen Olmsted, the instructor, has been teaching this course since its inception. The class is designed to fit within a 12-week schedule, shorter than the fall and spring semesters.

**Learning Objectives:**

*   Understand the fundamental concepts of operating systems.
*   Apply these concepts to real-world problems, particularly in cybersecurity.
*   Develop skills in C programming for operating system implementations.
*   Conduct research and contribute solutions to operating system-related challenges.

**Teaching Approach:**

The instructor employs a practical and hands-on approach, combining theoretical knowledge with practical implementation through programming labs and a research paper. The course emphasizes active learning, peer interaction, and problem-solving.

**Topics Covered:**

*   Course content overview: textbook, recorded lectures, quizzes, discussion prompts, programming labs, and research paper.
*   Detailed explanation of each component, including grading criteria and deadlines.
*   Introduction to C programming for operating systems.
*   Guidance on research paper development, including topic selection, methodology, and formatting.

### 2. Key Topics

#### 2.1. Course Content Overview

The course comprises several components, each designed to enhance understanding and application of operating system concepts.

*   **Textbook:**
    *   The primary textbook is the Tanenbaum Operating Systems book.
    *   Any version of the book is acceptable, allowing students to use older, used copies.
    *   Students are encouraged to read sections that align with the lecture topics for deeper understanding.
*   **Recorded Lectures:**
    *   A series of recorded lectures are available for students to review the material at their own pace.
*   **Quizzes:**
    *   Quizzes are designed as learning tools rather than strict assessments.
    *   Students can take quizzes multiple times, with each attempt presenting a randomized set of 5 questions.
    *   Questions often require problem-solving and detailed implementation, necessitating the use of paper, pencil, or tools like Excel.
    *   All necessary information to answer the questions is provided within the quiz itself.
    *   The instructor offers to answer one of each type of question on the discussion board.
*   **Discussion Prompts:**
    *   Four discussion prompts are scheduled throughout the semester to encourage peer interaction.
    *   Full credit is awarded for responding to the prompt and engaging with two different peers.
*   **Programming Labs:**
    *   Programming labs are a significant component of the course, providing hands-on experience in C programming.
    *   Two course assistants (CAs) are available to assist students with these labs.
*   **Research Paper:**
    *   The research paper aims to provide an alternative perspective on operating systems by solving a relevant problem.
    *   Students are encouraged to choose a domain they are familiar with and identify opportunities for improvement through abstraction.

#### 2.2. Quizzes: Detailed Explanation

*   **Open Book/Open Resource:** Quizzes are designed to encourage deeper engagement with the material rather than rote memorization.
*   **Unlimited Takes:** Students have unlimited attempts to complete each quiz, promoting continuous learning and improvement.
*   **Randomized Questions:** Each attempt presents a different set of questions, ensuring a comprehensive understanding of the material.
*   **Implied Implementation:** Questions often require students to apply concepts from the textbook and lectures to practical scenarios.
*   **Instructor Support:** The instructor is willing to help with one of each type of question to clarify any confusion.

#### 2.3. Discussion Prompts: Detailed Explanation

*   **Scheduled Prompts:** Discussion prompts are scheduled in weeks 2, 4, 6, and 8.
*   **Full Credit Criteria:** To receive full credit, students must respond to the prompt and reply to two peers.
*   **Grading Schedule:** The instructor grades the discussion prompts twice during the semester, providing ample opportunity for participation.

#### 2.4. Programming Labs: Detailed Explanation

*   **Language:** Programming labs are conducted in C, the language commonly used for operating system development.
*   **Course Assistants:** Two CAs are available to provide assistance with the programming labs.
*   **Gradescope:**
    *   Students upload their solutions to Gradescope, an automated grading system.
    *   Gradescope uses Docker sessions to compile and test the submitted code.
    *   Students receive immediate feedback on their submissions.
    *   Grades are synchronized from Gradescope to Brightspace.
*   **First Week Assignments:**
    *   The first week involves writing two simple C programs: "Hello World" and a leap year checker.
    *   These assignments are designed to ensure students can compile and test C code.
*   **Compiler:** The GNU C Compiler (GCC) is recommended, but any ANSI C-compliant compiler should work.
*   **Installation Options:**
    *   Students can install a Linux VM or use an online C compiler like onlinegdb.com.
    *   Instructions for installing GCC on Windows are also available.
*   **Online Resources:**
    *   The instructor recommends several online resources for learning C, including onlinegdb.com, W3Schools, and the O'Reilly Online platform via the NYU Library.
*   **Subsequent Labs:**
    *   After the first week, students work on four more detailed labs: CPU scheduling, memory allocation, virtual memory management, and disk scheduling.
    *   Students submit a single file containing function implementations for each lab.
    *   Offline testing is encouraged using a local C compiler and a provided header file (oslabs.h).

##### 2.4.1. Sample Main.c (Driver File)

```c
#include "oslabs.h"
#include <stdio.h>

int main() {
    // Example process setup
    struct PCB process1;
    process1.process_id = 1;
    process1.arrival_time = 0;
    process1.total_cycles = 10;
    process1.executed_cycles = 0;
    process1.priority = 1;

    // Example usage of handle_process_arrival (assuming preemptive scheduling)
    struct PCB *result = handle_process_arrival_pp(&process1, NULL, 5);

    if (result != NULL) {
        printf("Process ID: %d\n", result->process_id);
    } else {
        printf("No process running.\n");
    }

    return 0;
}
```

##### 2.4.2. Support Functions Example

```c
// Example support function to set up PCB structure
void setup_pcb(struct PCB *pcb, int process_id, int arrival_time, int total_cycles, int executed_cycles, int priority) {
    pcb->process_id = process_id;
    pcb->arrival_time = arrival_time;
    pcb->total_cycles = total_cycles;
    pcb->executed_cycles = executed_cycles;
    pcb->priority = priority;
}
```

#### 2.5. Research Paper: Detailed Explanation

*   **Goal:** The research paper aims to provide students with a different perspective on operating systems.
*   **Definition of Operating System:** The instructor defines an operating system as a layer of abstraction between hardware (or a lower layer of the operating system) and software.
*   **Domain Selection:** Students are encouraged to choose a domain they are familiar with and identify problems that can be improved with a layer of abstraction.
*   **Due Date:** All work is due by August 10th, with some scaffolding activities scheduled after this date.
*   **Scientific Method:** The instructor emphasizes the use of the scientific method in research, including hypothesizing, researching, modifying, testing, and disseminating.
*   **Cybersecurity Relevance:** Cybersecurity problems are highlighted as relevant operating system problems, particularly concerning confidentiality, integrity, and availability.
*   **Key Questions:** Students are encouraged to consider what an operating system is, what future operating systems might look like, and whether platforms like Salesforce can be considered operating systems.
*   **Vertical Market Specialization:** The instructor suggests that future operating systems may become more specialized for specific markets or domains.
*   **Leveraging Domain Experience:** Students are encouraged to leverage their unique domain experiences to identify and solve problems.
*   **Limiting Scope:** The instructor advises students to limit the scope of their research to a manageable level, given the 2-page extended abstract format.
*   **Group Work:** Group work is allowed, but each student must be the primary author on a paper, ensuring individual contributions.
*   **Authorship:** The first author is the principal investigator, secondary authors are collaborators, and the supervising author is typically the professor.

##### 2.5.1. Research Paper Sections

1.  **Introduction:** Introduce the problem and explain why it is difficult to solve.
2.  **Related Research:** Discuss what others have done to address the problem, citing relevant peer-reviewed papers.
3.  **Motivating Example:** Provide a concrete scenario illustrating the problem.
4.  **Hypothesis and Empirical Evidence:** Present a hypothesis and provide empirical evidence to support it.
5.  **Conclusions and Future Work:** Summarize the findings and suggest future directions.
6.  **References:** List all cited sources.

##### 2.5.2. Research Paper Format

*   The paper should be formatted using the IEEE template, available in Microsoft Word or LaTeX.
*   LaTeX is not required for this course.
*   The template provides the necessary formatting for extended abstracts, conference papers, and journal papers.

##### 2.5.3. Peer Review

*   The course uses a peer review system to assist students in the research process.
*   Students submit their work and review the submissions of their peers.
*   Participation in peer review is essential for receiving full credit.
*   Submission dates are synchronous, with submissions due on Sunday nights and peer reviews due the following Wednesday.

##### 2.5.4. Research Paper Scaffolding

*   **Week 4:** Choose a domain and cite three papers related to that domain.
*   **Week 5:** Define a specific problem and hypothesis, explaining how it differs from current solutions.
*   **Week 6:** Develop a sample way to measure the hypothesis, such as a metric in a chart or table.
*   **Week 9:** Write the related research section, citing three peer-reviewed papers.
*   **Week 10:** Write the introduction section.
*   **Week 11:** Write the empirical evidence section.
*   **Week 12:** Prepare and record a 10-12 minute presentation and finalize the 2-page paper.

##### 2.5.5. Gathering Empirical Evidence

Students can gather empirical evidence through:

1.  **Simulation:** Writing code to simulate the proposed solution.
2.  **Modeling:** Creating models (e.g., UML, BPMN, threat models) to demonstrate the improvement.
3.  **Scanning:** Using vulnerability scanners to assess the system before and after implementing the solution.
4.  **Open Data Sources:** Analyzing publicly available data to support the hypothesis.

##### 2.5.6. Example Hypothesis

*   Problem: Ticketmaster's transaction scheduling can lead to deadlocks and availability issues.
*   Hypothesis: Dividing transactions into synchronous and asynchronous categories can reduce deadlocks and increase availability.
*   Metric: Measure the number of concurrent users in the current and proposed solutions.

### 3. Exercises & Discussions

*   The class involves discussions on Brightspace, where students can post questions, share resources, and interact with peers.
*   The instructor encourages students to use the discussion board to ask questions about quizzes and programming labs.
*   The course assistants also have a Slack channel where students can seek help with programming labs.
*   Peer review is an integral part of the research paper process, providing students with feedback and insights from their peers.

### 4. Important Announcements

*   **Assignments and Deadlines:** All work is due by August 10th, with specific deadlines for each component of the research paper.
*   **Grading Criteria:** Grading is based on participation, completion of assignments, and the quality of the research paper.
*   **Additional Resources:** The instructor recommends several online resources for learning C and conducting research.
*   **Course Schedule Updates:** The instructor will provide regular updates via announcements on Brightspace.
*   **Next Webinar:** The next webinar is scheduled for June 8th.

### 5. Final Takeaways

#### 5.1. Key Learnings

*   A comprehensive understanding of operating system concepts and their applications.
*   Practical skills in C programming for operating system implementation.
*   Experience in conducting research and contributing solutions to operating system-related challenges.
*   Enhanced problem-solving and critical-thinking abilities.

#### 5.2. Follow-Up Actions

*   Review the recorded lectures and textbook chapters to reinforce understanding.
*   Start working on the programming labs and seek help from the course assistants as needed.
*   Begin brainstorming ideas for the research paper and start conducting literature review.
*   Participate actively in the discussion board and peer review activities.

#### 5.3. Motivational Note

The instructor encourages students to embrace their unique domain experiences and apply what they learn in the course to solve real-world problems. By leveraging their skills and knowledge, students can make meaningful contributions to the field of operating systems and cybersecurity.