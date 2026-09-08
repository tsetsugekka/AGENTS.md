# API key persistence for local skills

- Store user-approved persistent local Skill API keys in a clearly marked managed block in `${HOME}/.zshenv`, unless the service has a stricter canonical store. Use Keychain or `launchctl` only when explicitly requested.
- Receive passwords, keys, and tokens through a local hidden-input prompt or reliable interactive terminal with echo disabled, passing values directly to the established store/authentication flow. If reliable hidden input is unavailable, give the user a hidden-input command or secure edit path to run themselves.
- Never request credentials in chat or at an ordinary shell prompt. Keep plaintext out of command arguments, history, logs, tool output, replies, and Skill files; report only presence, source label, permissions, and save/validation results.
- For service-specific stores, use the documented canonical reader and do not duplicate credentials into shell profiles, `launchctl`, Keychain, Skill files, or project files. If a Skill's key variable is absent, use its approved managed-key bridge or canonical reader, injecting only into the validated child process.
