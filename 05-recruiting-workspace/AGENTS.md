# Recruit Codex Instructions

## 目录治理目标

Recruit 根目录保持稳定，只作为固定分类入口。原则上禁止未经用户明确同意在根目录新建文件夹；新的工作内容必须放入下列既有分区。若现有分区确实无法容纳，先向用户说明理由，获得同意后再新增根目录文件夹，并在同一任务中更新本文件。

根目录普通工作文件也应尽量避免。允许长期保留的根级文件仅限 `AGENTS.md`、`MOVED_FILES.md` 以及确有必要的项目级配置；不得把交付物、下载文件、截图和 AI 生成物散放在根目录。

## 固定目录

- `.agents/skills/`：Recruit 项目专用 Codex Skill 的唯一权威位置；这是官方项目级 Skill 路径，隐藏目录是有意设计。
- `01_求人票・評価基準/`：前三类招聘工作共用的求人票、JD、岗位要求和评价标准。
- `02_求人票改善/`：求人票、JD 和岗位说明改善所需的非个人化方法与 Skill 开发资料。
- `03_応募書類評価/`：结合求人票评价 Cover Letter、履历书、职务经历书等应聘资料，并提出面试设问所需的非个人化方法与 Skill 开发资料。
- `04_面接評価/`：面试评价、HRMOS 填写辅助所需的非个人化方法和 Skill 开发资料。
- `05_OKR記入支援/`：OKR 目标、Key Results、进展说明、自我评价和复盘的辅助方法。
- `80_企画・参考資料/`：Recruit 流程企划、AI 应用构想、内部提案和背景参考。
- `90_再利用資産/`：跨多个任务复用的方法、模板、检查清单和固定脚本；不存放 Skill。
- `98_アーカイブ/`：已停止活跃但因追溯或参考价值需要保留的非敏感资料。
- `99_一時作業/`：临时输入、AI 中间产物、渲染缓存、试验文件和一次性转换输出。

不要在根目录另建 `outputs/`、`output/`、`tmp/`、`temp/`、`work/`、`generated/`、`downloads/` 或以日期命名的临时文件夹。若工具默认生成这些目录，应把工具工作目录指向 `99_一時作業/YYYYMMDD_主题/`。

## 旧路径兼容

- 当较早会话、旧任务说明或历史命令引用的文件路径不存在时，再查看根目录 `MOVED_FILES.md` 寻找迁移后的路径。
- 不要在每次任务开始时例行读取该索引；只有旧路径失效时才需要读取，以避免无效上下文和 token 消耗。
- `MOVED_FILES.md` 只记录已有文件/文件夹的移动、重命名或因替代而删除，不记录普通新建文件，也不作为日常文件清单维护。
- 未来若移动可能被旧会话引用的既有路径，应在同一任务中追加一条旧路径到新路径的映射。

## 项目外敏感输入

- 履历书、职务经历书、简历、求职信、面试文字转录、面试官笔记、实际候选人评价、OKR 表格和绩效资料，默认从 Recruit 项目外拖入或作为会话附件使用。
- 不要为了方便而把这些文件复制到 `02_求人票改善/`、`03_応募書類評価/`、`04_面接評価/`、`05_OKR記入支援/`、`90_再利用資産/` 或 `98_アーカイブ/`。
- 不要为单个候选人建立 `YYYYMMDD_候補者ID/`、`input/`、`work/`、`final/` 或类似案件目录；匿名化不等于获得了在 Recruit 内保存候选人资料的许可。
- 优先直接读取项目外原文件。如果转换、OCR、Office 处理或其他工具必须生成本地副本，只能放入 `99_一時作業/YYYYMMDD_主题/`。
- 当前任务结束前必须删除上述临时副本、抽取文本、预览图和包含个人信息的中间结果；敏感资料不适用 30 天临时保留规则，也不得移入归档。
- 除非用户明确要求保存某个交付物，否则不在 Recruit 内保留候选人特定或个人绩效特定的输入、修改稿、评价结果。

## 默认交付方式

- 候选人及个人 OKR/绩效相关任务默认只采用以下交付方式：在当前对话框直接回答；按用户要求直接填写浏览器中的目标页面；或直接修改用户从项目外拖入的原文件。
- 除非用户明确要求创建或保存文件，否则不要生成 Markdown 总结、评价报告、结果文件、案件 README、候选人目录或另存版本。
- 若直接修改项目外原文件，保留原文件格式和位置；是否另存副本由用户明确指定，不得自行把副本放入 Recruit。
- 只有 OCR、Office 转换、浏览器上传或其他工具在技术上必须落盘时，才允许在 `99_一時作業/` 创建最小限度的临时文件，并在当前任务结束前删除。
- “方法沉淀”不代表每次任务都要生成文档。只有用户明确要求，或经过多次使用后确有独立复用价值且不含个人信息时，才更新既有方法资料或 Skill。

## 文件落位与命名

- 一个多文件方法、企划或非敏感资料主题使用 `YYYYMMDD_主题/` 子目录，放在最匹配的固定分区中。
- 新收到但尚未分类的非敏感项目资料可先放入当次 `99_一時作業/YYYYMMDD_主题/`，本次任务结束前完成分类。
- 最终交付物不得只存在于 `99_一時作業/`；若用户要求保存，移动到用户指定位置。
- 同一企划包含原稿、源文件和交付物时，应放在同一主题目录，并用 `README.md` 记录来源、文件关系、生成方式、最终版本和注意事项。
- 已被新版替代但仍需追溯的非敏感资料移至 `98_アーカイブ/`；可重新生成、重复或确认无用的中间物直接删除。
- `.DS_Store`、渲染缓存、锁文件和工具缓存不属于项目资料，整理时删除。

## 临时文件生命周期

- 创建临时目录时即使用可识别的日期和主题名称。
- 每项任务收尾时清理其临时目录：有长期价值的非敏感方法资料正式化，其余删除。
- 普通非敏感临时内容超过 30 天时复核；无法说明用途或可由正式源文件再生的内容删除。
- 含候选人信息、面试内容、实际 HRMOS/OKR/绩效数据的临时文件必须在当前任务结束时删除，不等待 30 天复核。
- 删除前若不确定某个非敏感文件是否为唯一原稿或唯一交付物，移入 `98_アーカイブ/待确认/` 并告知用户；敏感资料则先询问用户，不自行归档。

## AI 生成资料与方法沉淀

- AI 生成的非敏感 Office、HTML、图片或报告，应尽量同时保留可编辑源文件、关键输入和最终交付物；只含重复导出文件的深层生成树不作为长期入口。
- 能跨多个 Recruit 任务复用且已验证的方法、模板、检查清单和固定脚本放入 `90_再利用資産/`，并写清输入、输出、限制和使用方法。
- 仅服务单一企划的原稿、HTML 或生成说明跟随该企划放在 `80_企画・参考資料/`。
- 不保留无意义的 AI 尝试版本。需要保留多个版本时，在主题 `README.md` 中说明用途和当前推荐版本。

## 四条主要工作流

- 求人票改善：当前有效的求人票和评价标准保存在 `01_求人票・評価基準/`；改善方法与 Skill 开发资料放入 `02_求人票改善/`。
- 応募书类评价：方法资料放入 `03_応募書類評価/`；结合 `01_求人票・評価基準/` 中的岗位内容，评价项目外提供的 Cover Letter、履历书、职务经历书等，并提出有针对性的面试设问。
- 面试评价：方法资料放入 `04_面接評価/`；当前项目 Skill 为 `.agents/skills/hrmos-interview-eval/`；实际面试资料保持在项目外。
- OKR 辅助填写：方法、字段说明和脱敏模板放入 `05_OKR記入支援/`；实际 OKR/绩效文件保持在项目外。
- 四类任务中经过实际验证、能反复使用的方法先沉淀到 `90_再利用資産/`；触发条件、工作流、安全边界和输出格式稳定后，再制作成 `.agents/skills/` 下的项目 Skill。
- 业务目录只保存非个人化的方法资料，Skill 保存抽象后的可复用流程；不得让 Skill 依赖候选人文件、个人 OKR 文件或临时目录。

## Project-local Codex skills

- `.agents/skills/hrmos-interview-eval` is a Recruit project skill. It is installed at the project level only and should not be promoted to the user-global `$HOME/.agents/skills` directory unless the user explicitly asks.
- `.agents/skills/` is the authoritative hidden Skill directory for this Recruit workspace, following the official repo-scoped Skill convention. Do not move it to `$HOME/.agents/skills`, `.codex/skills/`, or a visible `skills/` directory unless the user explicitly asks.
- The generic, privacy-safe `hrmos-interview-eval` Skill may be published or updated on AI Hub when the user explicitly requests it. Keep Recruit-specific evaluation criteria, interview context, tenant-specific paths, and private examples inside this project; never include them in the public package.
- If the skill is updated, keep the authoritative copy under this project `.agents/skills/` directory. Do not update a temporary worktree copy and leave the project copy stale.
- Each Skill directory must keep all required `SKILL.md`, `agents/`, `references/`, `scripts/`, and `assets/` together with valid relative paths. Do not make a Skill depend on files under `99_一時作業/`, candidate/OKR source files, or an external temporary worktree.
- When a Skill is added or changed, update its local reproduction/manifest documentation and verify it from a fresh Recruit workspace session.
- Do not put candidate personal information, live HRMOS/OKR exports, credentials, cookies, private interview notes, or individual performance data into reusable Skill instructions, templates, or examples.

## 隐私与安全

- 候选人个人信息、面试原文、HRMOS 数据、实际 OKR、个人绩效信息和自我评价内容只在当前任务必要范围内处理，默认不在 Recruit 中保存。
- 凭据、Cookie、会话数据和真实账号信息不得写入项目文件或 Skill。
- 对外共享或制作通用模板前，先移除姓名、联系方式、简历内容、内部评价、个人目标和可识别的绩效信息。
