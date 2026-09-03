# Web Hub Codex Instructions

## Directory Governance

- `PROJECT_STRUCTURE.md` is the canonical directory policy. Follow its root whitelist, page ownership, temporary-file lifecycle, reusable-script boundary, and project-Skill reproducibility rules.
- Do not create a new top-level directory or ordinary root file unless the user explicitly requests or approves that structural change. When approved, update both `PROJECT_STRUCTURE.md` and the project structure checker in the same task.
- Every product page must have one clear numbered owner directory. Use `0x` for account/admin/system, `1x` for Dashboard Services, `3x` for Dashboard Tools, `5x` for Dashboard Demos, and `80+` for non-page areas. Product subroutes stay inside their owner directory.
- Every numbered page must maintain the DTM-style `docs/READMECHS.md`, `docs/SPEC.md`, and `docs/CHANGELOG.md` trio. Treat SPEC as current behavior, READMECHS as maintenance/deployment guidance, and CHANGELOG as history; update the relevant documents with code or operational changes.
- Put task-only downloads, generated screenshots, experiments, extracted copies, and uncertain artifacts in `99_Temporary/YYYYMMDD-topic/` or system `/tmp`. Promote useful artifacts to their owner directory and delete obsolete temporary content before finishing.
- `91_ProjectTools/` is only for reusable cross-page or repository-wide tools. Page-specific scripts belong to that numbered page; one-off scripts belong in `99_Temporary/` until deliberately promoted.
- Keep reproducible project Skills under `92_ProjectSkills/<skill-name>/` with complete `SKILL.md`, `README.md`, and any required relative `scripts/`, `references/`, `assets/`, or `agents/`. Never leave the only authoritative Skill copy in a temporary directory or generated ZIP.
- `MOVED_PATHS.md` is a compatibility index, not a daily inventory. Consult it only when continuing an older conversation or when an expected path is missing. Update it only when an existing file or directory is moved or renamed; do not read or update it for ordinary file creation.
- After structural changes, run `node 91_ProjectTools/check-project-structure.mjs`.

## Production Deploy Discipline

- Never print or commit production-host SSH/SFTP passwords, Google client secrets, session secrets, password hashes, or live local secret files.
- `LOCAL_DEPLOY_SECRETS.md` is local only and must stay ignored by Git.
- Use SFTP whitelist manifests for deploys. Do not recursively upload the whole repository, full `dist`, `.env`, databases, user data, cache directories, upload directories, or `node_modules`.
- Upload new hashed assets before uploading the new live `index.html`.
- After verifying the live page, run old asset cleanup:
  1. `node 91_ProjectTools/cleanup-remote-assets.mjs <target>`
  2. If the list only contains older hash assets: `node 91_ProjectTools/cleanup-remote-assets.mjs <target> --apply`
  3. Final verification: `node 91_ProjectTools/cleanup-remote-assets.mjs <target>` must report `delete=0`.
- Asset cleanup must keep current live `index.html` assets and the previous mtime release cluster. Delete only older hash `.js`, `.css`, and `.map` files, one file at a time. Never delete the assets directory, `index.html`, JSON, PHP, databases, user uploads, or cache files.

## Page Permission Handoff

- New protected pages must follow `01_Account/PAGE_PERMISSION_CONTRACT.md`.
- The account system owns login, roles, role-based page permission storage, and the protected-entrypoint contract. Each numbered page owns its protected entrypoint source; production manifests deploy it to the existing public route.
- Each page owns its own page-specific permission keys and must enforce them inside page UI and page APIs.
- Do not invent global permission levels for all pages. Define `permissions` per page in `01_Account/private/app/config.php`.
- Protected page entrypoints should inject `window.DEMO_SITE_AUTH.pagePermission`; page threads should read that value instead of inferring behavior from account roles.
- If another Codex thread is building a page, hand it the contract file and the exact page permission keys before it edits page behavior.
- Page access is configured on roles/user groups, not on individual users. Users inherit page permissions from their assigned role.

## Unified API Credential Store

- API keys used by production PHP, cron and Python programs have one server-side private store: `<server-private-config>/api_secrets.env`. Its directory must be mode `700` and the file mode `600`; never put it in Git, `www/`, deploy manifests, logs or test fixtures.
- Canonical key names are `GEMINI_API_KEY`, `OPENAI_API_KEY`, `SERPER_API_KEY`, and `TWITTERAPI_IO_API_KEY`. Do not introduce provider aliases, `*_FILE` variables, or per-provider key files. Google OAuth client credentials are login infrastructure and remain in private Account configuration, outside this API key store.
- AI Hub Bearer tokens are per-user access credentials, not production-host-to-provider API keys. Keep only their hashes in AI Hub private storage; the user's local Agent connection file may hold that user's token and must remain ignored, mode `0600`, and outside `api_secrets.env`.
- Every PHP and Python caller must resolve a canonical key only from `api_secrets.env`, then return an explicit safe “not configured” result. Use `01_Account/private/app/api_secrets.php` for PHP and `01_Account/tools/api_secrets.py` for Python. Do not read, export, or pass API keys through process environment variables.
- API status UIs may expose only the canonical variable name and one of `managed_private_config` or `unconfigured`. Never expose values, private paths, raw provider responses, or upstream error bodies.
- When adding an API provider, update the canonical allowlists in both shared resolvers, every consuming page/worker, the protected admin API-status registry and test, owner `READMECHS.md`/`SPEC.md`/`CHANGELOG.md`, and the exact SFTP whitelist. Add credentials to the unified private file before deploying readers that require them; verify safe configuration source and provider connectivity, then remove legacy per-key files in the same maintenance change.

## Production Mail And Account Notifications

- Do not commit mailbox passwords, API keys, mail secrets, password hashes, or live `site_settings.json` / `users.json` data.
- Production mail sending uses a real server mailbox as `From`; configure it from environment variables or private `config.local.php`, never in public files.
- Site name, public base URL, From email, and From display name are infrastructure settings. Keep them in environment variables or private `config.local.php`; do not expose them as editable admin UI fields.
- New self-registration requires email verification unless private config explicitly disables it. Pending users must not be auto-logged in.
- Verification tokens are stored only as hashes in the private user data file and must expire.
- Cron jobs should use `01_Account/tools/run-cron-with-alert.sh`; it sends mail only on non-zero exit status.
- Cron success, no-op, or lock-skip cases should not send mail. Logs must not include passwords, API keys, user data, or raw secrets.

## Codex Skill Boundary

- The project-local AI Hub Skill is installed at `92_ProjectSkills/ai-hub/SKILL.md`. It is project-only and public-safe; its runtime `ai-hub.local.json` is ignored and must never be committed.
- `.claude/skills/ai-hub` is a symlink to `92_ProjectSkills/ai-hub/`, added only so Claude Code's own `skills/` auto-discovery can find and invoke this same Skill. It is Claude-Code-only; Codex does not read `.claude/` paths and is unaffected. `92_ProjectSkills/ai-hub/` remains the single authoritative source — never create a second real `SKILL.md` copy under `.claude/`.
- AI Hub or skill-package web pages under `10_AIHub/public/` are product features, not automatically local Codex skills.
- Do not install, publish, or infer additional Codex skills from web-hub files unless a real `SKILL.md` exists or the user explicitly asks to create one.
- If a future web-hub-specific Codex skill is added, keep it under `92_ProjectSkills/<skill-name>/` and document whether it is project-only, private, or public-safe.
