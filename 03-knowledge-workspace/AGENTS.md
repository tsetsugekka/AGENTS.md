# Knowledge Workspace Codex Instructions

## Root directory governance
- The workspace root is a controlled project boundary. Do not create a new root-level directory unless the user explicitly approves it and this file plus `README.md` are updated in the same task.
- Approved root-level directories are:
  - `.agents/`: Codex project configuration; project-level skills live under `.agents/skills/` for standard discovery and may be private or pinned from a public upstream.
  - `.private/`: sensitive persistent data and sensitive temporary work.
  - `data/`: retained source data, exports, and machine-readable datasets.
  - `records/`: retained recording transcripts grouped by recording date.
  - `research/`: durable notes, analyses, studies, and research deliverables.
  - `scripts/`: reusable analysis and data-processing scripts.
  - `tmp/`: disposable, non-sensitive working files.
  - `tools/`: runnable local utilities and their static application assets.
- Root-level files should normally be limited to project-wide entry points such as `AGENTS.md`, `README.md`, and `MOVED_PATHS.md`.
- Before creating anything at the root, place it in the closest approved directory. If no approved directory fits, ask the user before expanding the root structure.

## Legacy moved-path lookup
- `MOVED_PATHS.md` is a one-time migration index for paths moved during the 2026-07-16 reorganization.
- Consult it only when continuing an older workspace task/session whose referenced path no longer exists, or when a known old path fails to resolve.
- Do not read it for routine new work, do not add ordinary new files to it, and do not maintain it as a general file inventory. This avoids unnecessary lookup and token usage.
- If a future user-approved structural migration moves an existing canonical path, append only that old-to-new mapping; ordinary file creation does not belong in this index.

## Placement rules
- Put Discord channel exports under `data/discord/<export-name>/`. Discord messages, metadata, audit files, and downloaded attachments are retained source data, not temporary files.
- Put MX/market data exports under `data/market/`; keep raw JSON, descriptions, and user-usable CSV/XLSX files together by source or research batch.
- Put recording transcripts under `records/<MMDD>/`. Do not delete or rewrite original transcripts during routine cleanup.
- Put research conclusions, comparisons, dated reviews, and video-study materials under `research/`, organized first by market/topic and then by dated task when useful.
- Put repeatable code in `scripts/` or `tools/`, not inside a one-off output folder. A script tied to a project-local skill must remain at the canonical path documented by that skill.
- Keep the public `analyze-youtube-video` Skill self-contained under `.agents/skills/analyze-youtube-video/`; its bundled scripts, requirements, and tests must match the public upstream rather than being duplicated under `tools/`.
- Put general scratch work under `tmp/<task-name>/`. Put sensitive scratch work under `.private/tmp/<task-name>/`. Both temporary areas may be cleaned after useful outputs are promoted.
- Prefer ISO dates (`YYYY-MM-DD`) in new folder and file names. Preserve imported source names when renaming would weaken provenance or break internal links.

## Task folder granularity
- When one task has more than two durable files, create a named task subfolder inside the appropriate category and keep all of that task's files together there.
- One or two files may remain directly under the category folder when their ownership is unambiguous.
- Count related source, data, description, report, and reproducibility files together when deciding whether they belong to the same task.
- A task folder is the grouping boundary: do not recursively create another level merely because the task folder itself contains more than two files.
- Prefer `<YYYY-MM-DD>_<topic>/` for dated work and a concise stable task name for reusable tools or workflows.

## Cleanup and retention
- `tmp/`, `.private/tmp/`, `__pycache__/`, `*.pyc`, generated logs, and `.DS_Store` are disposable. Remove them when stale and when no process depends on them.
- Never treat `data/discord/`, `records/`, skill references, source videos, or downloaded evidence attachments as temporary.
- For generated output outside a temporary directory, verify whether it is an input, evidence, final deliverable, or reproducibility artifact before deleting it.
- When a temporary experiment becomes useful, move the durable result into `research/`, the reusable method into `scripts/` or `tools/`, and update any affected skill paths before deleting the experiment folder.

## Reproducibility discipline
- The project directory is the source of truth for private project-local skills, scripts, retained data, and research evidence. For an explicitly pinned public Skill, its public upstream is the content source of truth and the project copy is an installed runtime copy.
- When moving a file referenced by a skill or script, update all canonical paths and defaults in the same task, then run a reference scan and a lightweight execution check.
- A project-local skill should document the canonical output location it creates. New Discord exports must default to `data/discord/`, never the project root.
- Keep live credentials, browser state, cookies, raw private exports, and client data out of reusable skill instructions and scripts.

## MX Skill credential bridge
- The installed `mx-*` skills are expected to work in this project even when a fresh shell does not contain `MX_APIKEY`. Do not conclude that MX is unavailable solely because `zsh -lc` or a direct skill-script invocation reports that the environment variable is missing.
- The canonical local credential remains a managed private configuration file, with directory mode `700` and file mode `600`. Read it through the shared secrets reader; never print the value or copy it into this repository, a skill file, a command argument, a log, Keychain, `launchctl`, or a shell profile.
- When an `mx-*` Python entry point requires `MX_APIKEY`, invoke it through the restricted managed-key bridge. Use the equivalent installed entry point for `mx-search`, `mx-xuangu`, or other applicable MX skills.
- The bridge may inject the credential only into a validated child script under `${HOME}/.codex/skills/mx-*`; it must reject arbitrary scripts and must not export the credential to the parent shell.
- After a credential or bridge problem, verify with one small read-only query. For `mx-data`, require an API response such as `status=0 / message=ok` plus successfully parsed tables; for `mx-search`, require successfully parsed search results. Report only presence, managed source, permissions, status, table/result counts, and errors—never the credential.
- If verification fails, check the managed file permissions, confirm the DTM reader reports `MX_APIKEY` from `managed_file`, and then inspect the bridge. Do not ask the user for a replacement key until the canonical managed source and bridge have both been checked.
- Continue to respect each MX skill's authorization boundary: querying public market data/news is read-only, while account-backed self-selected, simulated-portfolio, or transaction-like operations require the user's explicit request.

## Project-level skills
- Skills under `.agents/skills/` are project-level installations. Private skills must not be installed globally, published to GitHub, or copied into another project unless the user explicitly asks.
- `analyze-youtube-video` is a public upstream Skill installed at project level. Keep its `SKILL.md`, `agents/`, `requirements.txt`, `scripts/`, and `tests/` aligned with the upstream package; do not maintain a workspace-only fork or a second extractor under `tools/youtube/`.
- Current private skills:
  - `discord-channel-export`
  - `gamma-sailing`
  - `summarize-recordings`
- Treat the private skills as project knowledge that may refer to private workflows, recordings, Discord exports, or trading context. Keep secrets, tokens, cookies, raw private exports, and client data out of any reusable skill package.
- If a private skill becomes broadly useful, first create a cleaned public-safe export in a separate temporary package, then review examples, paths, account names, and logs before publishing.
- Do not use temporary worktree or system temporary-directory copies as the source of truth. The project directory is authoritative.
