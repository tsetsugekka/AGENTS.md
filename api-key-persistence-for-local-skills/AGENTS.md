# API key persistence for local skills
- For user-approved persistent API keys used by local Codex skills, normally write a clearly marked managed block in `${HOME}/.zshenv`, unless that service already has a stricter canonical managed store.
- Service-specific exceptions may use a documented canonical local credential store and reader. Do not duplicate those credentials into shell profiles, `launchctl`, Keychain, skill files, or project files.
- When an installed local skill needs an API key and the variable is absent, run it through the service's approved managed-key bridge or canonical credential reader; inject the key only into that validated child process.
- Do not use macOS Keychain or `launchctl` unless the user explicitly asks for those storage mechanisms.
- Never print or reveal live API key values in replies or command output; report only presence, source label, permissions, and validation result.
- Keep skill files themselves free of live credentials.
