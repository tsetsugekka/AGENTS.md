# Multi-agent delegation and model routing
- Multi-agent execution is allowed. When a task contains independent, bounded subtasks that can make useful progress in parallel, Codex may delegate them to sub-agents at its discretion.
- For mechanical, well-specified work with little ambiguity, prefer `gpt-5.6-luna` with `high` reasoning effort.
- For repetitive work that still requires meaningful language-model judgment, prefer `gpt-5.6-luna` with `xhigh` reasoning effort.
- For difficult or high-complexity work, choose an appropriate stronger agent, such as `gpt-5.6-sol` with `high` reasoning effort or `gpt-5.6-terra` with `high` reasoning effort, based on the task's reasoning, reliability, and implementation needs.
- Do not delegate merely to create activity: keep tightly coupled or very small tasks with the primary agent when coordination overhead would outweigh the benefit.
- The primary agent remains responsible for scoping delegated work, reviewing sub-agent results, resolving conflicts, and delivering one coherent final result.
