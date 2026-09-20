# Telegram Stop hook

[AGENTS.md](AGENTS.md) decides when a notification is appropriate. [telegram_notify_on_stop.py](telegram_notify_on_stop.py) executes the notification; a stop notification is not proof of task completion.

- Runs only with `CODEX_NOTIFY=1` and `~/.codex/notify_on_stop_once` present.
- Reads `TG_BOT_TOKEN` and `TG_CHAT_ID` from the environment. Never place their values in this repository or hook configuration.
- Sends a generic stop message, not chat, code, or project content. This public copy uses English notification text.
- Consumes the marker only after Telegram confirms success; failures retain the marker. Writes a mode-600 redacted receipt to `~/.codex/notify_on_stop_receipt.json`.
- Reads event JSON from stdin and emits machine-readable JSON. Requires Python 3 standard library and network access to Telegram. The request timeout is 8 seconds.

## Install and disable

Copy this directory to `~/.codex/hooks/telegram-notify-on-stop/`. Merge this entry into the `hooks.Stop` array of `~/.codex/hooks.json`, preserving unrelated entries. If a Telegram notifier is already configured, replace that entry rather than running two notifiers:

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/telegram-notify-on-stop/telegram_notify_on_stop.py\"","timeout":15,"statusMessage":"Sending Telegram stop notification"}]}
```

Review and trust through `/hooks`; do not edit trust records. Provide credentials through your approved local credential workflow. Enable the environment flag only when intended; the agent creates or cancels the marker according to AGENTS.md. Disable this hook through `/hooks`, or remove only its configuration entry. Without a marker it does not send.

## Verification and limits

Use mocked network calls to test success, failure and marker consumption without sending a message. A real delivery test requires an authorized notification and confirmation of the redacted receipt and actual receipt by the user. Hook registration alone does not establish successful delivery.

The existing marker is user-wide, not isolated per task: concurrent tasks can consume the same marker. Do not treat it as a per-task delivery guarantee. The hook does not enforce the discretionary 15-minute or once-per-task decisions; those remain agent responsibilities under AGENTS.md.
