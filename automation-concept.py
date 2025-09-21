"""
automation-concept.py
Prototype for prompt testing and reviewer notification (no auto-deploy).
"""

import subprocess
from pathlib import Path
import hashlib
import sys

PROMPT = Path("prompt.md")
LAST_HASH_FILE = Path(".prompt_hash")

def get_hash(file):
    return hashlib.md5(file.read_bytes()).hexdigest()

def run_tests():
    return subprocess.call([sys.executable, "testFramework.py"])

def notify_reviewer(result):
    if result == 0:
        print("[NOTIFY] Tests passed ✅ — Reviewer action required for deployment.")
        # Call API to send email/Slack notification here
    else:
        print("[NOTIFY] Tests failed ❌ — Reviewer must investigate before merging.")
        # Call API to send email/Slack notification here

def main():
    current_hash = get_hash(PROMPT)
    last_hash = LAST_HASH_FILE.read_text().strip() if LAST_HASH_FILE.exists() else ""

    if current_hash != last_hash:
        print("[INFO] Detected change in prompt.md")
        result = run_tests()
        notify_reviewer(result)
        if result == 0:
            # Save hash only after successful test run
            LAST_HASH_FILE.write_text(current_hash)
    else:
        print("[INFO] No changes detected.")

if __name__ == "__main__":
    main()
