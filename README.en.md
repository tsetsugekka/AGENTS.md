# AGENTS.md

![Rule groups](https://img.shields.io/badge/AGENTS.md-10%20rule%20groups-2563eb)
![Languages](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![Maintenance](https://img.shields.io/badge/continuously%20maintained-verified-7c3aed)

[中文](README.md) · [日本語](README.ja.md) · **English**

> One global operating guide split into ten independently reusable `AGENTS.md` rule groups for multi-agent collaboration, model routing, temporary files, temporary Caffeine keep-awake behavior, Telegram notifications, GitHub publishing, API keys, network fetching, anonymous document metadata, and development documentation and task continuity.

## What this repository is

An `AGENTS.md` file is a durable operating agreement for Codex and other coding agents at a project boundary. Each split file owns one stable topic, so it can be adopted on its own or combined with the other groups as needed.

Together, the rule groups define:

- how to choose multi-agent execution and models for different task complexity, first evaluating Astra low/medium and using Sol high/xhigh only for a clear alternative-route reason;
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

- `README.md`: project purpose, entry points, directory responsibilities, required configuration, usage and maintenance procedures, and actual build, verification, and deployment commands as a successor's navigation;
- `SPEC.md`: the currently effective scope, behavior, interfaces and data contracts, key constraints, and acceptance criteria;
- `CHANGELOG.md`: meaningful feature, behavior, interface, and operational-maintenance changes and their impact by date or version, distinguishing unreleased from released changes;
- `TASK.md`: the current task and unfinished work, including objectives, scope, status, next steps, dependencies or blockers, decisions needed from the user, owners, and completion criteria;
- `CASE-STUDY.md`: real failures, rework, or erroneous judgments with reusable value, including evidence, causes, fixes, verification, and prevention lessons; state clearly when there are no real cases.

Each responsibility may use a single Markdown file or indexed directories split by module or topic. CASE-STUDY may be one Markdown file or a `case-study/` directory (or existing equivalent), with one Markdown per case and a directory README or existing index for navigation.

Reuse existing equivalent files or sections and follow the project's conventions. Keep one clear source for current rules, task status, and historical evidence, linking from other documents instead of maintaining duplicate content. Update affected documents in the same task when requirements, implementation status, or acceptance conclusions change; before ending, pausing, or handing off, write unfinished items, blockers, and next steps back to the unified task entry point.

## The ten rule groups

| File | Primary focus | Best used on its own when you need… |
|---|---|---|
| [`final-response-status/AGENTS.md`](final-response-status/AGENTS.md) | Label the actual status at the end of each final response and explain unfinished work or blockers | Tasks that need an explicit completion status |
| [`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md) | Development documentation continuity and the five responsibilities of README, SPEC, CHANGELOG, TASK, and CASE-STUDY | Development projects needing ongoing maintenance or cross-session handoff, and involving multi-module collaboration, external services/deployment, phased delivery, or complex business constraints |
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | Multi-agent delegation, Luna/Sol/Terra/Astra model routing, and primary-agent review | Independent subtasks or work with different complexity levels |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | Temporary directories, end-of-task cleanup, and root structure | A clean project tree and explicit file lifecycles |
| [`temporary-caffeine-mode-for-long-running-tasks/AGENTS.md`](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) | Temporary keep-awake behavior for long tasks, Computer Use interruption risk, and security boundaries | Long tasks that need continuous execution or foreground interaction |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | Long-task stop notifications, interaction checks, one-shot markers, and credentials | Important results that may need to reach a user away from Codex |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | Target branches, publishing authorization, and pre-commit checks | A repository with a controlled GitHub release flow |
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

- These files are the ten top-level rule groups from the same global guide; each file preserves the complete meaning of its corresponding group.
- Before copying a group into another project, check that its paths, tools, credential store, and platform assumptions apply.
- The Caffeine rule can reduce interruption risk from idle sleep, display sleep, or some screensaver behavior, but it cannot guarantee protection against manual locking, managed lock policies, session switching, or logout; never use it to change password or other system security settings.
- Never place API keys, tokens, cookies, personal data, production data, or real private configuration in a public repository.
- If a project has stricter local rules, follow its source-of-truth instructions and the user's current request.

## Maintenance

- Keep exactly one corresponding `AGENTS.md` in each rule-group directory, with the directory name matching the rule-group title.
- When a rule changes, edit the relevant file and update the index and explanation in all three README languages.
- Before pushing, check Markdown, absolute paths, secrets, and unintended generated files.
- Keep commits focused and distinguish rule changes, README changes, and repository metadata changes.

## Topics

`AGENTS.md` · `codex` · `ai-agents` · `agent-instructions` · `multi-agent` · `prompt-engineering` · `workflow-automation`

## License

No license file is included by default. Add an explicit license only after the maintainer has chosen the intended reuse terms.
