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

## Paired project sync folders
- This project treats the following two folders as paired working locations:
  - Local: `<local-project-root>`
  - OneDrive: `<synced-cloud-project-root>`
- Skills under `.agents/skills/` are project-scoped skills, following the Codex/OpenAI skill location convention.
- Keep these skills in this project and sync them with OneDrive under the normal `.agents/skills/` sync rule. Do not install them globally or publish them as public skill packages unless the user explicitly asks.
- If updating a project skill, update the local project copy first; the synced cloud copy is synchronized from local and is not the authoritative source.
- Do not put client secrets, OneDrive credentials, private meeting recordings, raw transcripts with sensitive content, or personal information into reusable skill instructions.
- Only the following project subfolders need to be kept in sync between Local and OneDrive:
  - `00_自分のタスクと資料/`
  - `01_SQL関連/`
  - `02_会議議事録/`
  - `03_チームメンバー作成資料/`
  - `04_顧客提供資料/`
  - `90_開発/`
  - `99_背景資料/`
  - `docs/`
  - `.agents/skills/`
  - `task/`
- When creating, updating, or saving project files under those subfolders, update both locations in the same turn and verify the corresponding file or folder exists on both sides before final response.
- For synchronization conflicts, the local project is authoritative.
- When syncing, follow Local exactly. If a file or folder exists only on OneDrive and not locally, treat it as unnecessary and delete it from OneDrive during sync unless the user explicitly says to recover or inspect that OneDrive-only item.
- If OneDrive still has older folder names, report the directory-level mismatch before creating duplicate folders or deleting/renaming OneDrive folders.
- If a same-named file differs, prefer the Local copy unless the user explicitly says otherwise.
- If a file already exists on both sides but differs only in Office metadata/customXml/[trash] content, say so; this is usually not a business-content change.
- After reporting conflicts, sync from the local project to OneDrive when the user asks to resolve them.
- Other folders do not need to be synced by default. `outputs/` is a local scratch/build-output area, and `05_竹原さんSQLデータ/` plus `06_同期対象外ファイル/` are local-only unless the user explicitly asks to sync them.
- `AGENTS.md` itself does not need to be synced to the OneDrive folder; keep the canonical copy in the local project root.
- Formal final deliverables should generally be saved under `00_自分のタスクと資料` using the filename format `yymmdd_xxxx` or `yyyymmdd_xxxx` when the user specifies an 8-digit date.
- For multi-file deliverables under `00_自分のタスクと資料`, create a dated task folder following the existing month-folder pattern, for example `00_自分のタスクと資料/YYYYMM/YYYYMMDD_テーマ名/`, and place the related files inside it instead of leaving them loose in the month folder.
- For file placement, save executable SQL files under `01_SQL関連/`; save Markdown notes, task background, investigation memos, and non-SQL documentation under `task/` unless another project rule or explicit user instruction says otherwise.
- For almost every substantive task, create an experience/log Markdown file under `task/` capturing the purpose, decisions, assumptions, output locations, and caveats so the work remains reusable as project knowledge.
- Treat `outputs/` as temporary scratch only. Do not leave final deliverables there; after copying/moving useful artifacts to the formal location, delete no-longer-needed temporary or duplicate files from `outputs/`.
- If the synced cloud path is not found, inspect the configured cloud-storage root and resolve the actual synced folder path before saving.
- Keep generated deliverables in the corresponding subfolder on both sides when the same subfolder exists, for example `00_自分のタスクと資料`.
