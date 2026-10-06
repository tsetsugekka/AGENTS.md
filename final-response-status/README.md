# Final response status hook

[中文说明](README.zh-CN.md)

[AGENTS.md](AGENTS.md) defines the status semantics; [check_final_status.py](check_final_status.py) only checks the label format. It reads the Stop event JSON from stdin and checks `last_assistant_message`. The last nonempty line must contain only one of seven statuses: 🔴Awaiting choice, 🔴Awaiting discussion, 🟥Blocked and interrupted, 🟡Awaiting confirmation, 🟡Partially complete, 🟢Progressing smoothly, or 🟩Complete. Inline labels, the old bracket format, and added punctuation or Markdown emphasis are not accepted. Empty messages and unrelated events are skipped.

Output is `{}` when no warning is needed, otherwise a `systemMessage`. It never restarts the agent, calls a model, stores messages, accesses the network, or judges actual completion. Requires Python 3 standard library.

## Install and disable

Copy this directory to `~/.codex/hooks/final-response-status/`. Merge the following entry into the `hooks.Stop` array of `~/.codex/hooks.json`; do not overwrite existing entries:

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/final-response-status/check_final_status.py\"","timeout":3,"statusMessage":"Checking final response status"}]}
```

Review and trust the new definition through `/hooks`. Do not edit trust records. To disable, disable this entry or remove only this configuration entry.

## Verification

Test synthetic Stop events with all seven valid labels, inline labels, misplaced labels, wrong colors or shapes, the old format, empty messages, and unrelated events; validate the merged JSON. Local tests do not prove the host has loaded or triggered the hook. Confirm actual triggering separately after trust approval.

The checker displays warnings in English and accepts the seven colored labels from either the English rule or its Chinese source.
