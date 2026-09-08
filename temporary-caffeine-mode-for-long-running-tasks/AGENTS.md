# Temporary Caffeine mode for long-running tasks

- For long tasks, including Computer Use needing an unlocked foreground session, temporarily enable the narrowest keep-awake mode when it materially improves reliability and can be safely used and reliably cleaned up.
- It may reduce idle system/display sleep and some screensaver interruptions, but cannot guarantee protection from manual or managed locking, session switching, logout, or other system events. Do not bypass passwords, security policies, automatic screen-lock settings, or persistent startup settings.
- Disable it on completion, failure, blockage, pause, resumed user interaction, or when no longer needed; leave no background keep-awake process running.
