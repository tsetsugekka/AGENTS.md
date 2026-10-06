#!/usr/bin/env python3
"""Final-response-status hook: warn only, without restarting or storing text."""
import json
import sys


def check(payload):
    if not isinstance(payload, dict) or payload.get("hook_event_name") != "Stop":
        return {}
    message = payload.get("last_assistant_message")
    if not isinstance(message, str) or not message.strip():
        return {}
    statuses = {
        "🔴Awaiting choice", "🔴Awaiting discussion", "🔴Blocked",
        "🟡Partially complete", "🟡Awaiting confirmation", "🟢Complete",
        "🔴待选择", "🔴待讨论", "🔴遇阻中断",
        "🟡阶段性完成", "🟡待确认", "🟢全部完成",
    }
    if message.rstrip().splitlines()[-1].strip() in statuses:
        return {}
    return {"systemMessage": "The final response must end with a standalone status line: 🔴Awaiting choice, 🔴Awaiting discussion, 🔴Blocked, 🟡Partially complete, 🟡Awaiting confirmation, or 🟢Complete (or the corresponding Chinese label); this warning does not imply completion."}


if __name__ == "__main__":
    try:
        result = check(json.load(sys.stdin))
    except (ValueError, TypeError):
        result = {}
    print(json.dumps(result, ensure_ascii=False))
