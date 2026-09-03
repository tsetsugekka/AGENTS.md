# AGENTS.md

![Guides](https://img.shields.io/badge/AGENTS.md-7%20guides-2563eb)
![README](https://img.shields.io/badge/README-中文%20%7C%20日本語%20%7C%20English-16a34a)
![Safety](https://img.shields.io/badge/public--safe-reviewed-7c3aed)

> A curated collection of seven practical, public-safe `AGENTS.md` instruction sets for Codex and other agentic coding workflows.

本仓库把七套经过公开安全清理的项目级 `AGENTS.md` 集中在一起。它们覆盖市场数据、知识管理、云端同步、招聘资料、Web 产品、实验性工具和 Skill 发布边界等真实工作流。

このリポジトリは、公開向けに安全性を確認した 7 つのプロジェクト用 `AGENTS.md` をまとめたものです。市場データ、ナレッジ管理、クラウド同期、採用資料、Web 製品、実験的ユーティリティ、Skill 公開境界などを扱います。

This repository collects seven public-safe, project-scoped `AGENTS.md` files covering market data, knowledge work, cloud synchronization, recruiting materials, web products, experimental utilities, and Skill release boundaries.

## Contents / 目录 / 目次

- [中文说明](#中文说明)
- [日本語](#日本語)
- [English](#english)
- [Guide map](#guide-map)
- [Safety and provenance](#safety-and-provenance)
- [Usage](#usage)
- [Maintenance](#maintenance)

## 中文说明

### 这是什么

`AGENTS.md` 是放在项目边界内、供 Codex 或其他 coding agent 读取的持久化工作说明。它不只是提示词，还可以明确：

- 哪些目录允许创建文件，哪些目录属于临时区、归档区或敏感区；
- 如何区分源文件、可复用脚本、交付物、缓存和一次性中间文件；
- 哪些操作需要用户明确授权，例如发布、部署、交易、删除或访问外部服务；
- 凭据、Cookie、个人资料、候选人资料和生产数据必须放在哪里、哪些地方绝不能出现；
- 多 Agent 如何分工，以及主 Agent 如何复核和整合子 Agent 的结果；
- 什么时候更新文档、测试、部署清单和变更记录。

这七份文件不是一套必须原样套用的模板，而是七种已经在实际项目中验证过的治理思路。使用时应从最接近目标项目的一份开始，再根据项目实际目录和风险边界调整。

### 核心理念

1. **先确认边界，再执行操作**：先检查项目结构、Git 状态和授权范围，再读写或发布。
2. **可复现优先**：明确权威源、输出位置、脚本边界和同步方向，避免临时副本成为事实来源。
3. **默认最小暴露**：不把密钥、Cookie、个人资料、生产数据或本机路径带入代码、日志和公开仓库。
4. **临时文件有生命周期**：临时内容进入专用临时目录；任务结束时清理已确认无用的文件。
5. **主 Agent 负责最终质量**：子 Agent 可以并行工作，但最终范围、冲突处理、验证和交付由主 Agent 负责。

## 日本語

### このリポジトリについて

`AGENTS.md` は、プロジェクトの境界で Codex などの coding agent に読み込ませる持続的な作業規約です。単なるプロンプトではなく、次のような運用上の契約を明示します。

- 作成してよいディレクトリ、アーカイブ、キャッシュ、一時領域、機密領域；
- ソース、再利用可能なスクリプト、成果物、キャッシュ、中間生成物の区別；
- 公開、デプロイ、削除、外部サービス利用など、明示的な承認が必要な操作；
- API キー、Cookie、個人情報、候補者資料、本番データの保管境界；
- マルチエージェントの分担と、主エージェントによるレビュー・統合；
- ドキュメント、テスト、デプロイリスト、変更履歴を更新する条件。

7 ファイルは、そのまま全プロジェクトに適用するテンプレートではありません。対象プロジェクトの構造とリスクに最も近いガイドを選び、必要な部分だけを適応してください。

### 設計原則

- **境界を確認してから実行する**：構造、Git 状態、権限範囲を先に確認します。
- **再現性を守る**：正本、出力先、スクリプトの責務、同期方向を明確にします。
- **公開範囲を最小化する**：秘密情報、個人情報、本番データ、ローカル固有パスを公開物に含めません。
- **一時ファイルを管理する**：専用の一時領域を使い、不要になったものを安全に削除します。
- **最終責任は主エージェントにある**：サブエージェントの結果をレビューし、整合した成果物にまとめます。

## English

### What this is

An `AGENTS.md` file is a durable, project-scoped operating agreement for Codex and other coding agents. It can define much more than style preferences:

- which directories may receive new files and which are temporary, retained, archived, or sensitive;
- how to separate source files, reusable scripts, deliverables, caches, and intermediate output;
- which actions require explicit authorization, such as publishing, deployment, deletion, trading, or external-service access;
- where credentials, cookies, personal data, candidate material, and production data must never appear;
- how multi-agent work is split and how the primary agent reviews and integrates results;
- when documentation, tests, deployment manifests, and changelogs must be updated.

These seven files are patterns, not universal drop-in templates. Select the guide closest to the target project, then adapt names, directories, and controls to the project’s actual structure and risk profile.

### Design principles

1. **Check boundaries before acting**: inspect project structure, Git state, and authorization scope first.
2. **Optimize for reproducibility**: identify the source of truth, output location, script boundary, and sync direction.
3. **Minimize exposure by default**: keep secrets, cookies, personal data, production data, and machine-specific paths out of public artifacts.
4. **Give temporary files a lifecycle**: use a dedicated temporary area and remove only files confirmed disposable.
5. **Keep final accountability with the primary agent**: sub-agents may work in parallel, but the primary agent owns scope, review, conflict resolution, verification, and delivery.

## Guide map

Each directory contains exactly one file named `AGENTS.md`. The directory names are neutral public labels; they are not local filesystem paths.

| Guide | Primary focus | Best starting point when you need… |
|---|---|---|
| [`01-market-workspace/AGENTS.md`](01-market-workspace/AGENTS.md) | Market-data operations, production publishing, API credential boundaries, model routing | A data-heavy or deployment-sensitive project with strict credential handling |
| [`02-price-announcer/AGENTS.md`](02-price-announcer/AGENTS.md) | Experimental utility scope and publish guardrails | A small local utility that should stay outside the main release flow |
| [`03-knowledge-workspace/AGENTS.md`](03-knowledge-workspace/AGENTS.md) | Controlled roots, retained data, research, temporary work, managed-key bridges | A knowledge or research workspace with many data lifecycles |
| [`04-sync-workspace/AGENTS.md`](04-sync-workspace/AGENTS.md) | Paired local/cloud folders, authoritative source, conflict handling, retention | A project synchronized with OneDrive or another cloud folder |
| [`05-recruiting-workspace/AGENTS.md`](05-recruiting-workspace/AGENTS.md) | Fixed categories, candidate-data privacy, temporary-file cleanup, project Skills | A recruiting or HR workflow handling sensitive personal material |
| [`06-web-hub/AGENTS.md`](06-web-hub/AGENTS.md) | Page ownership, permission handoff, deployment whitelists, API and mail boundaries | A multi-page Web product with protected routes and production deploys |
| [`07-market-skills/AGENTS.md`](07-market-skills/AGENTS.md) | Private source vs. public release, global installs, cleaned exports | A repository that maintains reusable market-related Skills |

### Cross-guide capability matrix

| Capability | Guides that emphasize it |
|---|---|
| Multi-agent delegation and review | `01`, `06`, and the shared operating style used across the collection |
| Temporary-file placement and cleanup | `01`, `03`, `04`, `05`, `06`, `07` |
| Public/private release boundary | `01`, `03`, `05`, `06`, `07` |
| Cloud synchronization and conflict resolution | `04` |
| Candidate or personal-data protection | `05` |
| Protected Web pages and deployment safety | `06` |
| API credential storage and non-disclosure | `01`, `03`, `06` |

## Safety and provenance

The seven files were derived from project-scoped working instructions and prepared as public-safe copies. The public versions intentionally remove or generalize:

- absolute local paths and home-directory names;
- organization, account, and machine identifiers;
- private repository URLs and production-host paths;
- credential locations that would identify a real private environment;
- other details that are operationally useful only inside the original workspace.

The rules and intent are preserved where possible. The local source files remain the authoritative versions for their original projects; this repository is a curated public reference, not a bidirectional mirror.

Do not place API keys, tokens, cookies, private exports, candidate records, production databases, or deployment secrets in this repository. If a future change adds sensitive material, remove it before committing and rotate the exposed credential when necessary.

## Usage

1. Pick the guide whose operating model matches your project.
2. Copy its `AGENTS.md` into the target project boundary, or extract only the relevant sections.
3. Replace generic placeholders with project-local names only in a private project copy.
4. Review the resulting rules against the actual directory structure, tooling, permissions, and deployment process.
5. Keep temporary work in a dedicated temporary directory and keep secrets outside version control.

For a new project, start with the smallest applicable guide. Add rules when they encode a real, recurring boundary; avoid turning `AGENTS.md` into a general task log or a copy of every project document.

## Maintenance

- Keep each guide self-contained and valid Markdown.
- Update the README guide map when a guide is added, removed, renamed, or materially changes focus.
- Preserve the seven-file layout unless a deliberate release changes the collection size.
- Re-run a public-safety scan before every push; in particular, check for secrets, absolute paths, personal identifiers, private URLs, logs, and generated data.
- Prefer focused commits that explain whether a change updates a rule, a public-safe redaction, the README, or repository metadata.

## Topics

`AGENTS.md` · `codex` · `ai-agents` · `agent-instructions` · `prompt-engineering` · `developer-tools` · `workflow-automation` · `public-safe`

## License

No license file is included by default. Add an explicit license only when the maintainer has chosen the intended reuse terms.
