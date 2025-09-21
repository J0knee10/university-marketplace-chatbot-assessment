# Process Log

### 1. Understanding the problem. 
Based on background context, I understood that the issue was improving a chatbot not creating the chatbot. I have to create a system that when the Author creates or edits the bot, it needs to call a function to test if the chatbot breaks. If not broken, we can push a notification for a human reviewer to update the chatbot, if broken, don't push and continue working on it. If the chatbot breaks halfway without any updates, roll back to the last commit that was working.
- When the Author edits the chatbot, a function tests whether it breaks.  
- If tests pass, the system notifies a human reviewer to approve updates.  
- If tests fail, changes are rejected and the last good version is retained (rollback).  

---

### 2. Workflow
Step by step analysis, figure out which file to start first. According to the requirements I should start with prompt.md first which is suppose to shape the chatbot in XML format. So i am assuming that it takes certain parse phrase to view the data after in string format. prompt-analysis.md is just the explanation of prompt.md. testing-framework.md explains how to run test and testFramework.py is the code that calls the AI model and tests it against test-cases.json and checks back with prompt.md to ensure that the chatbot is working. automation-concept.py implements the code that checks the result from testFramework.py and decides whether to push further for human reviewer or to reject the changes. update-process.md explains how to update the chatbot and documentation. Finally marketplace-insights.md about the industry and pain points.
Step-by-step analysis to figure out the starting point:  
1. `prompt.md` shapes the chatbot using structured format.  
2. `prompt-analysis.md` explains the reasoning behind `prompt.md`.  
3. `test-cases.json` contains golden test scenarios for validation.  
4. `testFramework.py` executes these tests.  
5. `testing-framework.md` documents the testing approach.  
6. `automation-concept.py` automates testing and review notifications.  
7. `update-process.md` describes safe update workflows.  
8. `marketplace-insights.md` captures domain knowledge and informs prompt design.  
9. `README.md` summarizes the system, assumptions, and reflections.

---

### 3. Task 1 – Prompt Design
**Components:** `prompt.md` and `prompt-analysis.md`

- Created `prompt.md` with:  
  - Role and tone of the assistant (helpful, clear, safety-aware).  
  - Step-by-step instructions for common flows (e.g., creating listings, reporting scams).  
  - Escalation triggers and structured outputs (JSON where needed).  
  - Examples of good responses for each major category.

- Wrote `prompt-analysis.md` to justify design decisions:  
  - Balance of brevity vs. detail.  
  - Escalation vs. self-help.  
  - How safety rules map to escalation flows.

---

### 4. Task 2 – Golden Test Design & Testing Framework
**Components:** `test-cases.json`, `testFramework.py`, `testing-framework.md`

- **Golden Test Design:**  
  - Covered navigation, transactions, safety, escalation, and edge cases.  
  - Each test case includes `id`, `category`, `input`, `expected_elements`, `success_criteria`, `edge_case`.  
  - Ensures coverage for normal flows and failure/vague scenarios.

- **Testing Framework:**  
  - Drafted `testFramework.py` to:  
    - Load `prompt.md` and `test-cases.json`.  
    - Use a stub `AI_model()` function (to be replaced with OpenAI API later).  
    - Loop through test cases, verify `expected_elements` in responses, print pass/fail summary.  
    - Supports script execution or import into automation.  

- **Documentation:**  
  - `testing-framework.md` explains workflow, components, and how to run tests.

---

### 5. Task 3 – Automation & Update Process
**Components:** `automation-concept.py`, `update-process.md`

- Planned and implemented `automation-concept.py`:  
  - Computes a hash of `prompt.md` to detect edits.  
  - Runs `testFramework.py` automatically.  
  - If tests pass, **notifies a human reviewer** for approval.  
  - If tests fail, no changes are pushed.  
  - Stores last known good hash for rollback.  
  - (Future) Integrate with CI/CD for PR gating.

- `update-process.md`:  
  - Documents workflow for safe prompt updates.  
  - Specifies roles (Author, Reviewer, Maintainer, Automation Bot).  
  - Covers planning changes, running tests, reviewer approval, and rollback.

---

### 6. Task 4 – Marketplace Insights & Final Documentation
**Components:** `marketplace-insights.md`, `README.md`

- `marketplace-insights.md`:  
  - Captures research, trends, and user pain points.  
  - Highlights safety and trust challenges, seasonal patterns, and integration needs.  
  - Informs prompt design and golden test scenarios.

- `README.md`:  
  - Provides overview of the system and approach.  
  - Includes instructions for reviewing each component.  
  - Lists assumptions about the university marketplace.  
  - Contains time breakdown, next steps, personal reflection, alternative approaches, and user experience insights.

- Considerations for future implementation:  
  - Real model API integration.  
  - Extended golden tests for edge cases and seasonal trends.  
  - CI/CD integration for automated testing and reviewer notifications.  
  - Logging and analytics dashboard for escalation and issue tracking.