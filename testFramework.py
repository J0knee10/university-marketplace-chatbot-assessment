import json

def fake_model(prompt, input):
    raise NotImplementedError

def run_tests(prompt_file, cases_file):
    with open(prompt_file) as f:
        prompt = f.read()

    with open(cases_file) as f:
        tests = json.load(f)["test_cases"]

    passed = 0
    for case in tests:
        response = fake_model(prompt, case["input"])  # stub for LLM call
        if all(word.lower() in response.lower() for word in case["expected_elements"]):
            print(f"[PASS] {case['id']}")
            passed += 1
        else:
            print(f"[FAIL] {case['id']}")

    print(f"\nSummary: {passed}/{len(tests)} tests passed")

if __name__ == "__main__":
    run_tests("prompt.md", "test-cases.json")
