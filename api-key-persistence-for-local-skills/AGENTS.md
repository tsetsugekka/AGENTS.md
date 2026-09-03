# API key persistence for local skills

- For user-approved persistent API keys used by local Codex skills, normally write a clearly marked managed block in `${HOME}/.zshenv`, unless that service already has a stricter canonical managed store.
- `MX_APIKEY` is the exception: its canonical local source is `${HOME}/.config/daytrading_monster/api_secrets.env`, read through `${HOME}/Documents/ForCodex/DTM/scripts/dtm_api_secrets.py`. Do not duplicate it into shell profiles, `launchctl`, Keychain, skill files, or project files.
- When an installed `mx-*` skill needs `MX_APIKEY` and the variable is absent, run its Python entry point through `${HOME}/.codex/mx_data/run_with_managed_key.py`; the bridge may inject the key only into that validated `mx-*` child process.
- Do not use macOS Keychain or `launchctl` unless the user explicitly asks for those storage mechanisms.
- Never print or reveal live API key values in replies or command output; report only presence, source label, permissions, and validation result.
- Keep skill files themselves free of live credentials.
