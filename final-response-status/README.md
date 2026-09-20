# Final response status hook

[AGENTS.md](AGENTS.md) defines the status semantics; [check_final_status.py](check_final_status.py) only checks the label format. It reads the Stop event JSON from stdin and checks `last_assistant_message`. A short trailing `[status]` or `【状态】` label is accepted, with optional Markdown emphasis. Empty messages and unrelated events are skipped.

Output is `{}` when no warning is needed, otherwise a `systemMessage`. It never restarts the agent, calls a model, stores messages, accesses the network, or judges actual completion. Requires Python 3 standard library.

## Install and disable

Copy this directory to `~/.codex/hooks/final-response-status/`. Merge the following entry into the `hooks.Stop` array of `~/.codex/hooks.json`; do not overwrite existing entries:

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/final-response-status/check_final_status.py\"","timeout":3,"statusMessage":"Checking final response status"}]}
```

Review and trust the new definition through `/hooks`. Do not edit trust records. To disable, disable this entry or remove only this configuration entry.

## Verification

Test synthetic Stop events with valid, missing, misplaced and empty status labels, plus unrelated events; validate the merged JSON. Local tests do not prove the host has loaded or triggered the hook. Confirm actual triggering separately after trust approval.

The English display text and square-bracket support match this repository's English rule; the checker also accepts the Chinese source's labels.
