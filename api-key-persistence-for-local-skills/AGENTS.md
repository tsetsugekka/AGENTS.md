# API key persistence for local skills
- For user-approved persistent API keys used by local Codex skills, normally write a clearly marked managed block in `${HOME}/.zshenv`, unless that service already has a stricter canonical managed store.
- When adding or rotating a password, API key, token, or other credential, use a local hidden-input prompt or a confirmed interactive terminal with echo disabled so the user enters it directly. If the current tool cannot reliably accept hidden input, provide a user-run hidden-input command or a secure edit path; never ask the user to send the credential in chat or type it at an ordinary shell prompt. Keep plaintext, including hidden-input return values, out of command arguments, shell history, logs, and tool output; report only save and validation results.
- Service-specific exceptions may use a documented canonical local credential store and reader. Do not duplicate those credentials into shell profiles, `launchctl`, Keychain, skill files, or project files.
- When an installed local skill needs an API key and the variable is absent, run it through the service's approved managed-key bridge or canonical credential reader; inject the key only into that validated child process.
- Do not use macOS Keychain or `launchctl` unless the user explicitly asks for those storage mechanisms.
- Never print or reveal live API key values in replies or command output; report only presence, source label, permissions, and validation result.
- Keep skill files themselves free of live credentials.
