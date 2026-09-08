# Telegram notify-on-stop

- When the user explicitly requests an end-of-task notification, create `${HOME}/.codex/notify_on_stop_once`.
- Without an explicit request, a discretionary notification is allowed only after at least 15 minutes of actual execution with no new user message in the current task. Notify only meaningful completion, failure, blockage, or required user action; skip routine progress and low-impact results. Send at most once per task.
- “Interaction” means only a new message in the current task, not keyboard/mouse activity, lock/sleep state, OS sessions, camera, microphone, or other presence signals. Remove a discretionary marker if a new message arrives before completion, unless notification was explicitly requested.
- Do not enable notifications every turn. The Stop hook sends only when `CODEX_NOTIFY=1` and the marker exists, then deletes it. Read credentials only from `TG_BOT_TOKEN` and `TG_CHAT_ID`; never write tokens to files.
