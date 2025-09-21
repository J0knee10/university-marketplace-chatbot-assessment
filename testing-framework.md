# Testing Framework for UniMarket Assistant

## 1. Purpose

The testing framework ensures that changes to `prompt.md` do not break the chatbot’s
expected behavior. Every modification is validated against a set of **golden tests**—
predefined user scenarios that capture how the assistant should respond.  
If a test fails, it means a safety rule, escalation pathway, or guidance step may have been lost.

This approach brings software testing discipline into prompt engineering.

---

## 2. Components

| Component            | Role                                                                 |
|----------------------|----------------------------------------------------------------------|
| `prompt.md`          | Defines the chatbot’s system behavior and rules.                     |
| `test-cases.json`    | Stores 15–20 golden tests across all categories.                     |
| `testFramework.py`   | Loads the prompt and test cases, runs each input, and checks results. |
| Test Report (stdout) | Shows pass/fail results and summary count.                            |
| CI Integration       | (Optional) GitHub Actions can run tests automatically on PRs.        |

---

## 3. Test Categories

The framework covers at least **three cases per category**:

1. **Basic Navigation** — Posting items, searching, contacting sellers.  
2. **Transaction Support** — Payments, pickups, disputes.  
3. **Safety & Guidelines** — Prohibited items, scams, reporting users.  
4. **Escalation Triggers** — Threats, technical issues, policy violations.  
5. **Edge Cases** — Vague questions, multiple topics, unusual requests.

Each test case specifies:
- `id`: Unique identifier  
- `category`: One of the above  
- `input`: User message to test  
- `expected_elements`: Keywords/phrases that must appear in the response  
- `success_criteria`: Human-readable description of the test’s purpose  
- `edge_case`: Boolean to flag special handling  

---

## 4. How It Works

1. Load the chatbot’s system prompt from `prompt.md`.  
2. Read all test cases from `test-cases.json`.  
3. For each case:
   - Send the `input` to the assistant (currently a stubbed function).  
   - Check if all `expected_elements` are present in the response.  
   - Report `[PASS]` or `[FAIL]`.  
4. Print a summary of results.  
5. Exit code is `0` if all tests pass, `1` otherwise — useful for CI pipelines.

---

## 5. Running the Tests

Run locally with Python:

```bash
python testFramework.py --cases test-cases.json --prompt prompt.md
