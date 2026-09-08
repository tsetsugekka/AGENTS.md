# Telegram notify-on-stop

- When the user explicitly requests an end-of-task notification, create the one-shot marker `${HOME}/.codex/notify_on_stop_once`.
- Without an explicit request, only after at least 15 minutes of actual execution with no new user message in the current task may a notification be sent at the agent's discretion for meaningful completion, failure, blockage, or required user action; skip routine progress and low-impact results, with at most one notification per task.
- “Interaction” means only new messages in the current task; do not inspect keyboard/mouse activity, lock/sleep state, OS sessions, cameras, microphones, or other presence signals. If a new message arrives after creating a discretionary marker, remove it unless the user explicitly requested notification.
- Do not enable notifications automatically every turn; the Stop hook sends only when `CODEX_NOTIFY=1` and the marker exists, then deletes the marker. Read credentials only from `TG_BOT_TOKEN` and `TG_CHAT_ID`; never write tokens to files.
