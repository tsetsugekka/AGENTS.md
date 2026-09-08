# Temporary Caffeine mode for long-running tasks

- For long tasks, including Computer Use requiring an unlocked foreground session, a minimally scoped keep-awake mode may be enabled temporarily when it materially improves reliability; enable it only when it can be used safely and reliably cleaned up.
- It can only reduce interruption risks from idle sleep, display sleep, or some screensavers; it cannot guarantee protection against manual or managed locking, session switching, logout, and similar events. Do not bypass passwords, security policies, automatic screen-lock settings, or persistent startup settings.
- Disable it on completion, failure, blockage, pause, resumed user interaction, or when no longer needed; leave no background keep-awake process running.
