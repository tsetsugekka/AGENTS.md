# AGENTS.md

![Rule groups](https://img.shields.io/badge/AGENTS.md-8%20rule%20groups-2563eb)
![Languages](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![Maintenance](https://img.shields.io/badge/continuously%20maintained-verified-7c3aed)

[中文](README.md) · [日本語](README.ja.md) · **English**

> One global operating guide split into eight independently reusable `AGENTS.md` rule groups for multi-agent collaboration, model routing, temporary files, temporary Caffeine keep-awake behavior, Telegram notifications, GitHub publishing, API keys, network fetching, and anonymous document metadata.

## What this repository is

An `AGENTS.md` file is a durable operating agreement for Codex and other coding agents at a project boundary. Each split file owns one stable topic, so it can be adopted on its own or combined with the other groups as needed.

Together, the rule groups define:

- how to choose multi-agent execution and models for different task complexity;
- where temporary files belong, how to clean them up, and how to protect the project root;
- how temporary Caffeine/keep-awake mode can reduce interruption risk during long tasks and Computer Use, and where its security limits are;
- when a long-running task may send a Telegram notification and the one-notification limit;
- branch, commit, and pre-publish checks for GitHub changes;
- persistence and non-disclosure rules for API keys used by local Skills;
- throttling, batching, and failure handling for repeated network fetching;
- anonymous metadata and delivery checks for document artifacts.

## The eight rule groups

| File | Primary focus | Best used on its own when you need… |
|---|---|---|
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | Multi-agent delegation, Luna/Sol/Terra/Astra model routing, and primary-agent review | Independent subtasks or work with different complexity levels |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | Temporary directories, end-of-task cleanup, and root structure | A clean project tree and explicit file lifecycles |
| [`temporary-caffeine-mode-for-long-running-tasks/AGENTS.md`](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) | Temporary keep-awake behavior for long tasks, Computer Use interruption risk, and security boundaries | Long tasks that need continuous execution or foreground interaction |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | Long-task stop notifications, interaction checks, one-shot markers, and credentials | Important results that may need to reach a user away from Codex |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | Target branches, publishing authorization, and pre-commit checks | A repository with a controlled GitHub release flow |
| [`api-key-persistence-for-local-skills/AGENTS.md`](api-key-persistence-for-local-skills/AGENTS.md) | Local Skill key storage, the MX exception, and output redaction | Local Skills that call external APIs |
| [`network-scraping-discipline/AGENTS.md`](network-scraping-discipline/AGENTS.md) | Request pacing, aggregate endpoints, and rate-limit handling | Tasks that repeatedly access network data sources |
| [`anonymous-document-artifact-metadata/AGENTS.md`](anonymous-document-artifact-metadata/AGENTS.md) | Anonymous author fields and path privacy for Office/PDF artifacts | Generating or converting documents, spreadsheets, slides, or PDFs |

## How to combine them

The eight files are thematic rule groups, not mutually exclusive configurations. A practical composition is:

1. Start with `temporary-files-and-project-structure-hygiene` for the baseline file lifecycle.
2. Add `temporary-caffeine-mode-for-long-running-tasks` when a long task or Computer Use benefits from uninterrupted execution.
3. Add `multi-agent-delegation-and-model-routing` when parallel work is useful.
4. Add `github-publish-discipline` whenever the task changes GitHub state.
5. Add the API-key and network-fetching rules when external APIs or data sources are involved.
6. Add the anonymous-metadata rules when creating Office, PDF, or other packaged artifacts.
7. Add Telegram notification rules only when meaningful long-task reminders are actually needed.

## Usage notes

- These files are the eight top-level rule groups from the same global guide; each file preserves the complete meaning of its corresponding group.
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
