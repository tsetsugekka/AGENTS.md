# Personal Codex Preferences

## Telegram notify-on-stop
- Reply to the user in Chinese by default.
- When the user explicitly asks to be notified after the current task, create the one-shot marker file `${HOME}/.codex/notify_on_stop_once`.
- Do not enable Telegram notifications automatically for every turn. The Stop hook sends only when `CODEX_NOTIFY=1` and the one-shot marker exists, then deletes the marker.
- Telegram credentials must be read from `TG_BOT_TOKEN` and `TG_CHAT_ID`; never write tokens into files.

## GitHub publish discipline
- This applies to all future Codex work, not only stock-related skills or a single repository.
- Do not create, switch to, or push a new working branch unless the user explicitly asks for a branch, PR, draft PR, or experimental branch.
- For direct requests such as "commit", "push", "publish to GitHub", "update GitHub", or "发布到 GitHub", default to the repository's intended target branch, usually `main`.
- Before staging or committing, run `git branch --show-current` and confirm it is the intended target branch. If it is not, switch or fast-forward to the target branch before committing.
- If an old temporary branch is already checked out, do not keep using it by inertia. Either move the work onto the target branch when safe, or ask the user before publishing from that branch.
- After a temporary branch has been merged into the target branch and is no longer needed, delete the local and remote temporary branch.

## Direct production and GitHub publish exception
- If the user asks for an initial or first-time update, and the project worktree has no unrelated or concurrently running changes, Codex may directly publish to the production host and GitHub without asking for another confirmation.
- Before using this exception, inspect `git status --short` and confirm the pending changes are only the current task's intended files.
- If there are unrelated modified or untracked files, do not use this exception. Explain the blocker and ask before staging, committing, pushing, or deploying.
- Direct production publishing still must follow the repository's documented deploy process and must not overwrite protected live data unless the user explicitly requested that.
- When Codex has changed code that affects live behavior and the user asks to publish or update, publish both the relevant code and the corresponding docs to GitHub and the production host by default. Do not publish docs alone unless the user explicitly asks for a docs-only publish.

## Patch and hotfix authorization
- Do not introduce patch-style fixes without the user's explicit approval. This includes frontend compatibility shims that override generated output, one-off repair scripts, direct edits to generated or production artifacts, narrowly hardcoded exceptions, and other temporary hotfixes that bypass the normal source-of-truth workflow.
- By default, fix the authoritative source data or generator and regenerate affected artifacts through the repository's documented workflow. If a patch appears necessary, explain its scope and downstream risks and wait for the user's approval before applying it.
- The use of Codex's `apply_patch` editing tool for ordinary source-controlled edits is not itself a patch-style fix under this rule; the restriction concerns the implementation approach and operational behavior.

## Production host network access preference
- For documented production-host SSH/SFTP operations in this repository, prefer requesting non-sandbox execution first instead of trying the sandbox first and then retrying after DNS/network failure.
- This preference applies to read-only checks, deploy helper scripts, cleanup helper scripts, and other documented production-host operations that need network access.
- Still respect Codex approval requirements, production-data protection rules, and the existing `LOCAL_DEPLOY_SECRETS.md` secret-handling discipline. Never print or commit production-host credentials.

## Production API credential policy
- The canonical API credential/configuration names are `GEMINI_API_KEY`, `GEMINI_MODEL`, `GEMINI_LITE_MODEL`, `TWITTERAPI_IO_API_KEY`, `OPENAI_API_KEY`, `OPENAI_DRAWDOWN_MODEL`, `OPENAI_TRANSLATION_MODEL`, `MX_APIKEY`, `MOOMOO_APP_KEY`, `MOOMOO_SIGN_ALGORITHM`, and `MOOMOO_PRIVATE_KEY_PATH`. Do not introduce aliases such as `GOOGLE_API_KEY`, `GEMINI_TRANSLATION_MODEL`, `X_ACCOUNTS_GEMINI_MODEL`, `MOOMOO_PRIVATE_KEY_B64`, per-job model flags, or per-job key files.
- The single persistent production source is `<server-private-config>/api_secrets.env`, outside the web root. Its directory must be mode `700` and the file mode `600`; it contains only canonical `NAME=value` entries and must never be committed, uploaded to `www/`, logged, or printed. API credentials and model/config values must not be read from same-name process environment variables. Local operator tools use the equivalent per-machine managed file, never shell profiles.
- The standard model assignment is `GEMINI_MODEL=gemini-3.6-flash` for core market narratives, PTS market themes, and long-chart interpretation; `GEMINI_LITE_MODEL=gemini-3.5-flash-lite` for translation, Rating summaries, PTS individual rise reasons, ordinary X relevance/title/ticker classification, and narrative text compression; `OPENAI_DRAWDOWN_MODEL=gpt-5.6-luna` for one-time web-grounded Chinese copy when a new 10% Drawdown event is deterministically detected; and `OPENAI_TRANSLATION_MODEL=gpt-5.6-luna` for pure translation without web tools, the one-time translation fallback, and one same-input Structured Outputs fallback when the initial Gemini Market narrative result fails transport, JSON, or full business validation. Narrative validation errors may be logged safely but must not be added to the OpenAI fallback prompt. Model names live in `api_secrets.env`, not scraper defaults, `config.md`, CLI flags, or browser code. Gemini 3.5+ requests must not send deprecated `temperature`, `top_p`, or `top_k` sampling parameters.
- Split-file credentials are limited to two documented exceptions. The moomoo private key body and the Google Drive read-only service-account JSON belong in separate managed private files. Each parent directory must be mode `700` and each credential file mode `600`. `api_secrets.env` stores only the moomoo private-key path, AppKey, and signing algorithm; it must not duplicate the Google JSON. Never store either private-key body in `api_secrets.env`, an environment variable, logs, PHP responses, the repository, or the web root.
- Python consumers must use the shared secrets reader; PHP consumers must use the site-owned server-side secrets endpoint. Never duplicate parsing in a scraper, cron wrapper, page, or endpoint. Multiple programs may read the one file concurrently. Every writer must create a complete mode-`600` temporary file in the same mode-`700` directory and atomically rename it over the target; never truncate the live file in place.
- After all runtime readers verify a migration, remove legacy per-API key files and shell-profile exports; do not retain them as fallback credential sources.
- `/supervisor/` must list every configured external API, its canonical configuration names, and non-secret model names. Connection tests execute only server-side after admin authorization, same-origin POST validation, and per-session rate limiting. Responses may return only masked configuration state, model name, result category, and timestamp—never keys, private paths, signatures, request headers, or upstream response bodies. Direct requests to the PHP configuration reader must return 404.
- A new API requires: choosing one collision-free canonical `UPPER_SNAKE_CASE` name; adding it to both shared readers and the managed store; migrating every consumer away from direct environment/file parsing; adding a masked server-side status/test in `/supervisor/`; updating deployment extras and verification scripts; adding tests for file permissions and environment-variable rejection; and documenting the purpose, model if any, consumers, and migration in `docs/API_CONFIGURATION.md`, affected `docs/SPEC.md`, `docs/READMECHS.md`, changelogs, and this policy when the convention changes.
- Before building any browser bundle, scan Vite/Webpack `define`, client environment prefixes, frontend source, static JSON, and generated assets. No browser code may receive a credential or call a credentialed upstream API directly; browsers consume only site-owned sanitized data/API responses.

## Documentation sync discipline
- When code or operational behavior changes, update the relevant project docs in the same task by default; do not wait for a separate user request.
- For PTS changes involving `scraper.py`, cron timing, data files, cache structure, SEO behavior, deployment protection, or output semantics, update `pts-analysis/docs/SPEC.md`, `pts-analysis/docs/CHANGELOG.md`, and, when maintenance steps or operator guidance changed, `pts-analysis/docs/READMECHS.md`.
- For cross-project deployment, production-data protection, or repository-wide maintenance rules, update `PROJECT_MAINTENANCE.md`.
- If a change is purely internal and no doc update is needed, mention that decision explicitly in the final response.

## Project-local Codex skills
- `skills/themes-maintenance/SKILL.md` is a project-local maintenance skill. Keep it tracked and published with its private source repository; do not leave edits only in a temporary worktree or a global install copy.
- When changing `skills/themes-maintenance/SKILL.md`, commit and push that skill update to the repository's intended branch, normally `main`, unless the user explicitly asks not to publish.
- Do not install `themes-maintenance` globally by default. It is tightly coupled to this repository, its `/themes` data ownership rules, production quote flow, and project docs.
- The repository copy is authoritative. If another copy of `themes-maintenance` appears in a temporary worktree, system temporary directory, or `~/.codex/skills`, treat it as a disposable or stale copy unless the user explicitly says otherwise.
- Never put production quote data, production-host credentials, local secret files, live auth data, or private run logs inside a project skill.
