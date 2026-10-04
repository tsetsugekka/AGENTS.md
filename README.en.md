# AGENTS.md · Pick the rules your agent needs

[中文](README.md) · [日本語](README.ja.md) · **English**

Make it clear when an agent should act, what it should read, which boundaries it must respect, and what a trustworthy handoff requires.

This catalog contains **12 independent topics**, each in Chinese and English. **It is not a configuration package to install wholesale.**

## Start here

1. Choose only the topics you need from the table.
2. Pick one language and read the scope, dependencies, and limitations.
3. Merge frequent rules into your persistent instructions; use on-demand reading for less frequent topics. Preserve existing project constraints rather than replacing the entire file.
4. Check paths and companion documents. Copying rules does not install skills, hooks, or tools, or grant operational authority.

## Rule catalog

| Topic | What it covers | Rules |
| --- | --- | --- |
| Response status | Make completion, unfinished work, and blockers explicit | [中文](final-response-status/AGENTS.zh-CN.md) · [English](final-response-status/AGENTS.md) |
| Delegation & model routing | Independent subtasks, eight model/effort combinations, sensible waiting and review | [中文](multi-agent-delegation-and-model-routing/AGENTS.zh-CN.md) · [English](multi-agent-delegation-and-model-routing/AGENTS.md) |
| Development docs & continuity | Responsibilities of README / SPEC / CHANGELOG / TASK / CASE-STUDY and on-demand instructions | [中文](development-documentation-and-task-continuity/AGENTS.zh-CN.md) · [English](development-documentation-and-task-continuity/AGENTS.md) |
| Frontend design | Design-skill roles, compact layouts, and app-like mobile workflows | [中文](frontend-design/AGENTS.zh-CN.md) · [English](frontend-design/AGENTS.md) |
| Temporary files & structure | Temporary artifact cleanup, existing-file protection, and stable project roots | [中文](temporary-files-and-project-structure-hygiene/AGENTS.zh-CN.md) · [English](temporary-files-and-project-structure-hygiene/AGENTS.md) |
| Browser tabs | Reuse task tabs, promptly close unneeded pages, and protect the user's existing tabs | [中文](browser-tab-hygiene/AGENTS.zh-CN.md) · [English](browser-tab-hygiene/AGENTS.md) |
| Keep-awake for long tasks | Temporary Caffeine use, cleanup, and security limits | [中文](temporary-caffeine-mode-for-long-running-tasks/AGENTS.zh-CN.md) · [English](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) |
| Telegram notifications | Useful end-of-task notifications, triggers, and the once-per-task limit | [中文](telegram-notify-on-stop/AGENTS.zh-CN.md) · [English](telegram-notify-on-stop/AGENTS.md) |
| GitHub publishing | Branches, scope isolation, and preserving other changes; no automatic publishing authorization | [中文](github-publish-discipline/AGENTS.zh-CN.md) · [English](github-publish-discipline/AGENTS.md) |
| Credential handling | Safe input, persistence, and non-disclosure for local Skill credentials | [中文](api-key-persistence-for-local-skills/AGENTS.zh-CN.md) · [English](api-key-persistence-for-local-skills/AGENTS.md) |
| Network fetching | Pacing, batching, and rate limits; distinguish internal operations | [中文](network-scraping-discipline/AGENTS.zh-CN.md) · [English](network-scraping-discipline/AGENTS.md) |
| Anonymous document metadata | Remove identity fields and local paths; inspect final deliverables | [中文](anonymous-document-artifact-metadata/AGENTS.zh-CN.md) · [English](anonymous-document-artifact-metadata/AGENTS.md) |

## Two ways to adopt a topic

**Merge directly** for frequently applicable rules. Integrate the chosen text into your `AGENTS.md`, `CLAUDE.md`, or other actual instruction file. Check model, tool, and platform assumptions first; renaming a file does not guarantee compatibility.

**Read on demand** for long, infrequently needed topics. Save the complete text as ordinary Markdown, keeping an explicit trigger, path, and necessary safety boundaries in the root instructions. For example, save the design topic to `docs/FRONTEND-DESIGN.md` and add:

```markdown
Before interface design, redesign, or frontend work involving an interface,
read docs/FRONTEND-DESIGN.md. Do not read it for other tasks.
```

Adjust paths relative to your instruction file and include required companion documents. A link alone does not guarantee reading. Do not load the same rule both in full and on demand, or give an on-demand document a root-instruction filename your runtime automatically loads.

Public topics retain their complete text; you need not reproduce the author's local directory structure. Keep general constraints and safety boundaries in the entry point, and load long task-specific details on demand. Short rules and content explicitly requested to remain always loaded need not be split.

## Before adopting

- **Source:** Chinese comes from the local Chinese source and its explicitly referenced details, with private content excluded. English is a faithful translation, not a separate rule set; Chinese is not back-translated.
- **Design:** `finesse-ui`, Taste's `redesign-existing-projects`, and `impeccable` must be available in your environment. This repository neither bundles those skills nor enables design hooks.
- **Model routing:** These are preferences by purpose and cost, not a universal performance ranking. Your runtime must support the chosen models and reasoning levels.
- **Keep-awake:** It cannot guarantee protection against manual or managed locking and must not bypass passwords or security policies.
- **Publishing and credentials:** The author's automatic commit, push, and deployment authorization is excluded, as are personal credentials, account configuration, and private paths.
- **Scope:** Resolve conflicts with existing project rules before adoption. Copying these rules does not expand authority. Choose one language to avoid duplicate loading.

## Optional hooks: distinguish rules from implementation

| Companion | Current status |
| --- | --- |
| [Final-response status checker](final-response-status/README.md) | Checks label format, not actual completion; does not restart the agent |
| [Telegram notifications](telegram-notify-on-stop/README.md) | The included legacy script does not meet the current task-isolation and result-summary contract; do not enable it as an implementation of the new rules |

Follow each README for installation, trust, and verification. Passing script tests does not establish actual triggering or message delivery.

## Maintenance and reuse

Each topic maintains `AGENTS.zh-CN.md` and `AGENTS.md`; the three READMEs guide selection. Update the Chinese source first, then synchronize public text and translations. Do not create competing sources for the same fact.

No license is currently included, so open-source permission is not implied. Confirm reuse terms before redistribution.
