# Temporary Caffeine mode for long-running tasks
- For a task expected to run for a substantial period—including Computer Use that requires an unlocked, interactive foreground session—Codex may temporarily enable an available Caffeine or keep-awake mode when uninterrupted execution materially improves reliability.
- Caffeine may reduce interruptions caused by idle system sleep, display sleep, or some screensaver behavior, but it does not guarantee protection against manual locking, managed lock policies, session switching, logout, or other system events.
- Use the narrowest available scope and only for the duration of the active task. Do not bypass password requirements, security policies, automatic screen-lock settings, or persistent system startup settings.
- Disable the temporary keep-awake mode when the task completes, fails, is blocked, is paused, the user resumes interaction, or it is otherwise no longer needed. Do not leave a background keep-awake process running after the task.
- If the platform cannot safely provide a temporary mode with a reliable cleanup path, continue without changing system sleep behavior.
