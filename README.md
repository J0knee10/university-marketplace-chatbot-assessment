# UniMarket Assistant - Chatbot System

## 1. Introduction
UniMarket Assistant is a university marketplace support chatbot designed to help students, faculty, and clubs buy, sell, and trade items safely and efficiently.  
The system is structured to:
- Provide clear instructions for common marketplace flows.
- Detect safety and policy issues and escalate when necessary.
- Validate changes through automated golden tests before updates.

**Approach Overview:**  
We built a modular system with:
1. A structured prompt (`prompt.md`) with role, tone, conditional logic, and output schema.
2. Golden tests (`test-cases.json`) to validate prompt functionality.
3. A testing framework (`testFramework.py`) to automatically check responses.
4. Automation (`automation-concept.py`) for testing on prompt updates, with rollback support.
5. Documentation (`prompt-analysis.md`, `update-process.md`, `marketplace-insights.md`) to guide contributors and reviewers.

---

## 2. Reviewing Components

| Component | Purpose | How to Review |
|-----------|--------|---------------|
| `prompt.md` | Defines chatbot behaviour | Check structure, role clarity, and conditional logic |
| `prompt-analysis.md` | Explains reasoning behind prompt | Ensure design decisions align with requirements |
| `test-cases.json` | Golden tests for validation | Verify coverage of scenarios (navigation, safety, escalation, edge cases) |
| `testFramework.py` | Runs tests against prompt | Run locally or integrate with CI/CD, verify pass/fail summary |
| `automation-concept.py` | Detects changes and notifies reviewer | Modify prompt, check console messages, ensure last-good hash stored |
| `update-process.md` | Step-by-step update workflow | Ensure instructions align with automation and review process |
| `marketplace-insights.md` | Context and research | Validate that trends, pain points, and seasonal patterns are incorporated |

---

## 3. Assumptions About the University Marketplace
- Users are primarily students with `.edu` accounts; faculty/staff also participate.
- Safety is paramount: all meet-ups are recommended on campus.
- Payments are restricted to approved channels; sensitive info is never requested.
- Students have limited budgets and prefer mobile-first solutions.
- Seasonal trends influence item availability (textbooks, furniture, graduation items).

---

## 4. Time Breakdown of Effort
| Task | Time Allocated |
|------|----------------|
| Prompt Design & Engineering | 45 min |
| Golden Test Design & Testing Framework | 30 min |
| Automation & Update Process | 20 min |
| Marketplace Domain Research | 15 min |
| Documentation & Reflection | 20 min |

---

## 5. Next Steps for Real Project
1. Integrate the real AI model via API in `testFramework.py`.  
2. Connect `automation-concept.py` to a CI/CD pipeline (e.g., GitHub Actions/Emails API) for PR gating.  
3. Extend golden tests with more edge cases and seasonal scenarios.  
4. Implement logging and dashboards for escalation frequency and issue types.  
5. Continuously update insights (`marketplace-insights.md`) to reflect campus trends.

---

## 6. Personal Reflection
The most challenging component was **prompt design**:
- Balancing brevity with sufficient detail for safety and escalation.
- Structuring the output schema to be consistent and easy to validate via tests.
- Ensuring the prompt remained flexible for new marketplace scenarios without breaking golden tests.

---

## 7. Alternative Approaches Considered
1. **Rule-based responses only** – rejected: not scalable, hard to maintain as marketplace grows.  
2. **No structured output (free text only)** – rejected: makes automated testing and escalation unreliable.  
3. **Auto-deploy without human review** – rejected: risk of unsafe or broken behaviour reaching students.

---

## 8. Experience With University Marketplaces
- As a buyer: frequent challenges with finding the products I want quickly, ensuring seller trust, and avoiding scams.  
- As a seller: difficulty posting items efficiently, ensuring clear pricing, and meeting buyers safely.  
- Hard to differentiate spam/scams to the real sellers.
- Random people outside of the university are somehow able to join the system and sell their items
- Insights informed prompt design, safety rules, and edge-case scenarios in golden tests.

---

## 9. How to Run
1. Update `prompt.md` or `test-cases.json`.  
2. Run golden tests:
```bash
python testFramework.py --cases test-cases.json
```
3. Check automation-concept.py output/notification/email to reviewer
4. If approved, update the main branch following update-process.md

---