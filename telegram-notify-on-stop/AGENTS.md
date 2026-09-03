# Telegram notify-on-stop
- Reply to the user in Chinese by default.
- When the user explicitly asks to be notified after the current task, create the one-shot marker file `${HOME}/.codex/notify_on_stop_once`.
- Codex may also create the one-shot marker at its discretion for a long-running task when the user has not interacted with Codex during that task. Treat a task as long-running after at least 15 minutes of actual execution time.
- For discretionary notifications, notify only when there is a meaningful completion, failure, blocker, or request for user action. Skip routine progress updates, low-impact results, and tasks shorter than 15 minutes. Send at most one Telegram notification per task.
- For this decision, "user interaction" means only that the user sent a new message in the current Codex task after execution began. Do not inspect keyboard or mouse activity, screen lock/sleep state, OS user-session activity, camera, microphone, or similar device-presence signals.
- If a discretionary one-shot marker was created and the user sends a new message before the task ends, remove that marker unless the user explicitly requested a Telegram notification.
- Do not enable Telegram notifications automatically for every turn. The Stop hook sends only when `CODEX_NOTIFY=1` and the one-shot marker exists, then deletes the marker.
- Telegram credentials must be read from `TG_BOT_TOKEN` and `TG_CHAT_ID`; never write tokens into files.
