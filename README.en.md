# AGENTS.md

![Rule groups](https://img.shields.io/badge/AGENTS.md-10%20rule%20groups-2563eb)
![Languages](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![Maintenance](https://img.shields.io/badge/continuously%20maintained-verified-7c3aed)

[中文](README.md) · [日本語](README.ja.md) · **English**

> Selected public sections of a Chinese global operating guide, faithfully translated with private content excluded, form ten independently reusable English `AGENTS.md` rule groups. This repository is not a complete copy of the global guide.

## What this repository is

An `AGENTS.md` file is a durable operating agreement for Codex and other coding agents at a project boundary. Each split file owns one stable topic, so it can be adopted on its own or combined with the other groups as needed.

Together, the rule groups define:

- the actual status at the end of each final response, with unfinished work or blockers;
- how to delegate well-bounded subtasks worth running in parallel, start with the least capable model that can reliably complete the task, and have the primary agent review the results;
- where temporary files belong, how to clean them up, and how to protect the project root;
- how temporary Caffeine/keep-awake mode can reduce interruption risk during long tasks and Computer Use, and where its security limits are;
- when a long-running task may send a Telegram notification and the one-notification limit;
- branch, commit, and pre-publish checks for GitHub changes;
- persistence and non-disclosure rules for API keys used by local Skills;
- throttling, batching, and failure handling for repeated network fetching;
- anonymous metadata and delivery checks for document artifacts;
- documentation and continuity for development projects that need ongoing maintenance or cross-session handoff, and involve any of multi-module collaboration, external services or deployment, phased delivery, or complex business constraints: maintain README, SPEC, CHANGELOG, TASK, and CASE-STUDY with distinct responsibilities for navigation, the current contract, change history, task status, and reusable cases.

## Development documentation and task continuity

Use [`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md) when a development project needs ongoing maintenance or cross-session handoff, and involves any of multi-module collaboration, external services or deployment, phased delivery, or complex business constraints. One-off small changes do not require the full set. The five document responsibilities are:

- `README.md`: purpose, entry points, and operations;
- `SPEC.md`: current behavior, contracts, and acceptance criteria;
- `CHANGELOG.md`: important changes and release status;
- `TASK.md`: the current task, unfinished items, blockers, and next steps;
- `CASE-STUDY.md`: evidence, causes, fix verification, and reusable lessons from real errors; do not invent cases when none exist.

Each responsibility may use a single Markdown file or indexed directories split by module or topic. When cases become numerous, use a `case-study/` directory (or existing equivalent), with one Markdown per case and a directory README or existing index for navigation.

Prefer existing documents, names, and directories. Read relevant documents before starting, and update only affected content when making changes. Before ending, pausing, or handing off, write unfinished work back to the task entry point. Maintain one authoritative source for each fact or status, with links elsewhere. Distinguish current specifications, unimplemented plans, historical records, implementation, verification, release, and operational acceptance. Documentation updates do not expand authority and must not put credentials or internal records into public artifacts.

## The ten rule groups

| File | Primary focus | Best used on its own when you need… |
|---|---|---|
| [`final-response-status/AGENTS.md`](final-response-status/AGENTS.md) | Label the actual status at the end of each final response and explain unfinished work or blockers | Tasks that need an explicit completion status |
| [`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md) | Development documentation continuity and the five responsibilities of README, SPEC, CHANGELOG, TASK, and CASE-STUDY | Development projects needing ongoing maintenance or cross-session handoff, and involving multi-module collaboration, external services/deployment, phased delivery, or complex business constraints |
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | Multi-agent delegation, Luna/Sol/Terra/Astra model routing, and primary-agent review | Independent subtasks or work with different complexity levels |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | Temporary directories, end-of-task cleanup, and root structure | A clean project tree and explicit file lifecycles |
| [`temporary-caffeine-mode-for-long-running-tasks/AGENTS.md`](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) | Temporary keep-awake behavior for long tasks, Computer Use interruption risk, and security boundaries | Long tasks that need continuous execution or foreground interaction |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | Long-task stop notifications, interaction checks, one-shot markers, and credentials | Important results that may need to reach a user away from Codex |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | Branch discipline, scope isolation, staging-state protection, and publishing checks | A repository with a controlled GitHub release flow |
| [`api-key-persistence-for-local-skills/AGENTS.md`](api-key-persistence-for-local-skills/AGENTS.md) | Local Skill key storage, service-specific exceptions, and output redaction | Local Skills that call external APIs |
| [`network-scraping-discipline/AGENTS.md`](network-scraping-discipline/AGENTS.md) | Request pacing, aggregate endpoints, and rate-limit handling | Tasks that repeatedly access network data sources |
| [`anonymous-document-artifact-metadata/AGENTS.md`](anonymous-document-artifact-metadata/AGENTS.md) | Anonymous author fields and path privacy for Office/PDF artifacts | Generating or converting documents, spreadsheets, slides, or PDFs |

## How to combine them

The ten files are thematic rule groups, not mutually exclusive configurations. A practical composition is:

1. Start with `temporary-files-and-project-structure-hygiene` for the baseline file lifecycle.
2. Add `temporary-caffeine-mode-for-long-running-tasks` when a long task or Computer Use benefits from uninterrupted execution.
3. Add `multi-agent-delegation-and-model-routing` when parallel work is useful.
4. Add `github-publish-discipline` whenever the task changes GitHub state.
5. Add the API-key and network-fetching rules when external APIs or data sources are involved.
6. Add the anonymous-metadata rules when creating Office, PDF, or other packaged artifacts.
7. Add Telegram notification rules only when meaningful long-task reminders are actually needed.
8. Add the development-documentation and task-continuity rule when a development project needs ongoing maintenance or cross-session handoff, and involves multi-module collaboration, external services or deployment, phased delivery, or complex business constraints; maintain the five document responsibilities for navigation, the current specification, change history, task status, and reusable cases.

## Usage notes

- The English rules faithfully express the selected public sections, with private content excluded; all three READMEs introduce the same ten rule groups.
- Before copying a group into another project, check that its paths, tools, credential store, and platform assumptions apply.
- The Caffeine rule can reduce interruption risk from idle sleep, display sleep, or some screensaver behavior, but it cannot guarantee protection against manual locking, managed lock policies, session switching, or logout; never use it to change password or other system security settings.
- Never place API keys, tokens, cookies, personal data, production data, or real private configuration in a public repository.
- If a project has stricter local rules, follow its source-of-truth instructions and the user's current request.

## Maintenance

- Keep exactly one corresponding `AGENTS.md` in each rule-group directory, with the directory name matching the rule-group title.
- The Chinese source is the sole source of rules. Update it first, faithfully translate the affected public content, and synchronize all three READMEs; do not independently add to or change the rules in English.
- Before pushing, check Markdown, absolute paths, secrets, and unintended generated files.
- Keep commits focused and distinguish rule changes, README changes, and repository metadata changes.

## Topics

`AGENTS.md` · `codex` · `ai-agents` · `agent-instructions` · `multi-agent` · `prompt-engineering` · `workflow-automation`

## License

No license file is included by default. Add an explicit license only after the maintainer has chosen the intended reuse terms.
