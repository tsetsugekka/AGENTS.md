# API key persistence for local skills

- By default, store user-approved persistent API keys for local Skills in a clearly marked managed block in `${HOME}/.zshenv`; follow a service's stricter canonical storage location when one exists. Do not use Keychain or `launchctl` unless requested.
- Prefer receiving passwords, keys, and tokens through a local hidden-input prompt or a reliable interactive terminal with echo disabled, passing them directly to the prescribed storage/authentication flow. If the tool cannot interact reliably, have the user enter them with hidden input in their own terminal or securely edit the designated file.
- Do not ask users to send credentials in chat or enter them at an ordinary shell prompt; plaintext must not enter command arguments, history, logs, tool output, replies, or Skill files. Report only presence, source labels, permissions, and save/validation results.
