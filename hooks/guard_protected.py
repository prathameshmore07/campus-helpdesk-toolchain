#!/usr/bin/env python3
import json
import sys

def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_input = payload.get("tool_input", {})
    target_path = str(tool_input.get("file_path") or tool_input.get("path") or "")

    if "protected/" in target_path or target_path.startswith("protected"):
        print(json.dumps({
            "decision": "deny",
            "reason": "Blocked by guard-protected-folder hook: writes to protected/ are forbidden."
        }))
        sys.exit(0)

    print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
