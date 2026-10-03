# Telegram Stop hook

[AGENTS.md](AGENTS.md) defines when notification is appropriate and the current notification contract. [telegram_notify_on_stop.py](telegram_notify_on_stop.py) is a legacy implementation using an empty marker and generic stop message. It does not satisfy the current rules for task isolation, not-ready/ready records, or redacted result summaries. Do not enable this script directly under the current rules; provide a matching implementation when adopting them. A stop notification is not proof of task completion. [中文说明](README.zh-CN.md).

## Current rule contract

A one-shot notification record must be bound to the current task and initially not ready. Before ending, the agent prepares a redacted summary containing the task name, actual status, brief result or blocker, and required user action, then marks it ready. The Stop hook sends only ready records, consumes them after success, and saves a redacted receipt. This repository does not yet provide a matching implementation, so no new record path, schema, or installation command is defined here.

## Existing legacy script behavior

- Runs only with `CODEX_NOTIFY=1` and `~/.codex/notify_on_stop_once` present.
- Reads `TG_BOT_TOKEN` and `TG_CHAT_ID` from the environment. Never place their values in this repository or hook configuration.
- Sends a generic stop message, not chat, code, or project content. This public copy uses English notification text.
- Consumes the marker only after Telegram confirms success; failures retain the marker. Writes a mode-600 redacted receipt to `~/.codex/notify_on_stop_receipt.json`.
- Reads event JSON from stdin and emits machine-readable JSON. Requires Python 3 standard library and network access to Telegram. The request timeout is 8 seconds.

## Legacy installation and disable instructions

The following describes the legacy setup, not an installation compatible with the current rules.

Copy this directory to `~/.codex/hooks/telegram-notify-on-stop/`. Merge this entry into the `hooks.Stop` array of `~/.codex/hooks.json`, preserving unrelated entries. If a Telegram notifier is already configured, replace that entry rather than running two notifiers:

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/telegram-notify-on-stop/telegram_notify_on_stop.py\"","timeout":15,"statusMessage":"Sending Telegram stop notification"}]}
```

Review and trust through `/hooks`; do not edit trust records. Provide credentials through your approved local credential workflow. Enable the environment flag only when intended; the agent creates or cancels the marker according to AGENTS.md. Disable this hook through `/hooks`, or remove only its configuration entry. Without a marker it does not send.

## Verification and limits

Use mocked network calls to test success, failure and marker consumption without sending a message. A real delivery test requires an authorized notification and confirmation of the redacted receipt and actual receipt by the user. Hook registration alone does not establish successful delivery.

The existing marker is user-wide, not isolated per task: concurrent tasks can consume the same marker. Do not treat it as a per-task delivery guarantee. The hook does not enforce the discretionary 15-minute or once-per-task decisions. Legacy script tests do not establish that the current rule contract is implemented.
