#!/usr/bin/env python3
"""Final-response-status hook: warn only, without restarting or storing text."""
import json
import re
import sys


def check(payload):
    if not isinstance(payload, dict) or payload.get("hook_event_name") != "Stop":
        return {}
    message = payload.get("last_assistant_message")
    if not isinstance(message, str) or not message.strip():
        return {}
    # Accept user-defined short status labels and optional Markdown emphasis.
    if re.search(r"(?:【[^【】\n]{1,16}】|\[[^\[\]\n]{1,40}\])(?:\*\*|__)?[。.!！]?\s*$", message):
        return {}
    return {"systemMessage": "The final response is missing a trailing [status] label; this warning does not imply completion."}


if __name__ == "__main__":
    try:
        result = check(json.load(sys.stdin))
    except (ValueError, TypeError):
        result = {}
    print(json.dumps(result, ensure_ascii=False))
