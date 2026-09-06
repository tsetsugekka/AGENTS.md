# Temporary files and project structure hygiene
- Put session-only scratch files, diagnostics, downloads, and intermediate artifacts in the system temporary directory, preferably inside a task-specific directory created with `mktemp -d`, rather than in the project tree.
- Before completing a task, remove temporary files and directories created by that task when they are known to have no future use. If a temporary artifact must be retained for debugging, handoff, or user-requested reuse, keep it deliberately and report its location and purpose.
- Never delete pre-existing, unfamiliar, or ambiguously owned files merely because they look temporary. Cleanup is limited to targets known to have been created by the current task or otherwise confirmed disposable.
- Be cautious about creating new top-level directories in a project root. Inspect the existing structure and project documentation first, reuse an established directory when appropriate, and add a new root-level directory only when it is a durable part of the intended project structure.
- If a tool or workflow genuinely requires repository-local temporary files, use an existing ignored cache or temporary directory when available and avoid leaving incidental files in version control status.

## Temporary Caffeine mode for long-running tasks
- For a task expected to run for a substantial period, Codex may temporarily enable an available Caffeine or keep-awake mode when uninterrupted execution materially improves reliability.
- Use the narrowest available scope and only for the duration of the active task. Do not change password requirements, security policies, automatic screen-lock settings, or persistent system startup settings.
- Disable the temporary keep-awake mode when the task completes, fails, is blocked, is paused, the user resumes interaction, or it is otherwise no longer needed. Do not leave a background keep-awake process running after the task.
- If the platform cannot safely provide a temporary mode with a reliable cleanup path, continue without changing system sleep behavior.
