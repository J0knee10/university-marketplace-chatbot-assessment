"""
testFramework.py
Golden test runner for UniMarket Assistant.
Validates chatbot prompt against predefined scenarios.
"""

import json
import argparse
import re
import sys

def AI_model(prompt, user_input):
    """
    Placeholder for chatbot call.
    Replace this with actual API call (e.g., OpenAI/Anthropic).
    """
    return f"[STUB RESPONSE] input='{user_input}' | prompt preview='{prompt[:40]}...'"


def validate_response(response: str, expected_elements: list) -> list:
    """
    Checks if all expected elements appear in the chatbot response (case-insensitive).
    Returns a list of missing elements (empty if all found).
    """
    missing = []
    response_lower = response.lower()
    for el in expected_elements:
        # allow partial matches (word presence) rather than exact phrase
        if not re.search(re.escape(el.lower()), response_lower):
            missing.append(el)
    return missing


def run_tests(prompt_file: str, cases_file: str, show_fails: bool = False) -> int:
    """
    Runs all golden test cases and prints a summary.
    Returns exit code 0 if all pass, else 1.
    """
    prompt = open(prompt_file, encoding="utf-8").read()
    tests = json.load(open(cases_file, encoding="utf-8"))["test_cases"]

    total = len(tests)
    passed = 0

    print(f"[INFO] Running {total} golden tests...\n")

    for case in tests:
        case_id = case.get("id", "unknown")
        case_input = case["input"]
        expected = case["expected_elements"]

        try:
            response = AI_model(prompt, case_input)
            missing = validate_response(response, expected)

            if missing:
                print(f"[FAIL] {case_id} – missing: {', '.join(missing)}")
                if show_fails:
                    print(" ↳ Response:", response, "\n")
            else:
                print(f"[PASS] {case_id}")
                passed += 1

        except Exception as e:
            print(f"[ERROR] {case_id}: {e}")

    print(f"\nSummary: {passed}/{total} tests passed")

    return 0 if passed == total else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run golden tests for UniMarket Assistant")
    parser.add_argument("--prompt", default="prompt.md", help="Path to system prompt file")
    parser.add_argument("--cases", default="test-cases.json", help="Path to test cases JSON")
    parser.add_argument("--show-fails", action="store_true", help="Show full response on failures")
    args = parser.parse_args()

    sys.exit(run_tests(args.prompt, args.cases, args.show_fails))
