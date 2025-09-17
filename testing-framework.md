# Testing Framework for UniMarket Assistant

## 1. Purpose

The testing framework ensures that **prompt changes do not break expected behaviours**.

Whenever you modify `prompt.md`, you can run all predefined scenarios (“golden tests”) automatically.  
If any test fails, you know immediately that the new prompt might have lost an instruction, a safety rule, or an escalation path.

This is the same philosophy used in software engineering: every time you change code (or a prompt), run tests so you don’t re-introduce old bugs.

---

## 2. Components

| Component | Role |
|-----------|------|
| `test-cases.json` | Stores 15+ scenarios, grouped by category. |
| `run_tests.py` (or `run_tests.js`) | Script that reads the cases, sends each input to the bot (or stub), checks for required elements or escalation flags. |
| Test report | Console output (pass/fail summary). |
| CI (optional) | GitHub Actions workflow that runs the script on each pull request. |

---

## 3. How it works

1. Load all tests from `test-cases.json`.
2. For each case:
   - Feed the `input` to the assistant (or a placeholder if you don’t have a live API).
   - Verify the answer contains every `expected_element`, or that JSON fields match for escalation.
3. Record `PASS` or `FAIL`.
4. Print a summary (e.g., `12/15 passed`).

---

## 4. Running the tests

> Example using Python:

```bash
python run_tests.py --cases test-cases.json
