# Multi-agent delegation and model routing

### Delegation principles
- Multi-agent execution is allowed when a task contains independent, bounded subtasks that can make useful progress in parallel, and each subtask has a clear input, output, and completion condition.
- Before delegating, the primary agent should define the subtask scope, constraints, expected deliverable, acceptance criteria, and whether the sub-agent may edit files or only report findings.
- Assign one clear owner to each file or deliverable. Avoid concurrent edits to the same file unless the primary agent has explicitly coordinated the ownership and merge plan.
- Do not delegate merely to create activity. Keep tightly coupled, very small, or coordination-heavy work with the primary agent when delegation would add more overhead than value.
- Keep the number of sub-agents proportional to the amount of genuinely independent work. Prefer a small number of focused assignments over broad, overlapping exploration.

### Model routing
- Start with the least capable model that can complete the work reliably, and escalate only when ambiguity, failure, or verification needs justify it.
- For mechanical, well-specified work with little ambiguity, prefer `gpt-5.6-luna` with `high` reasoning effort.
- This `luna high` default also applies to Computer Use tasks that open a browser and follow clear steps to obtain, confirm, extract, or routinely check information from known pages or sources.
- For repetitive work that still requires meaningful language-model judgment—such as interpreting irregular page layouts, normalizing semi-structured results, or resolving bounded extraction ambiguities—prefer `gpt-5.6-luna` with `xhigh` reasoning effort.
- For difficult but bounded work with manageable context, choose `gpt-5.6-sol` with `high` or `xhigh` reasoning effort as appropriate. Use `gpt-5.6-terra` with `high` reasoning effort when implementation reliability or tool execution is the main concern.
- Treat `gpt-6-astra` with `high` or `xhigh` reasoning effort and `gpt-5.6-sol` with `high` or `xhigh` reasoning effort as overlapping options rather than a strict universal hierarchy. In domains where Astra's strengths, broader context handling, or reliability are valuable, choose Astra; when the task fits Sol's strengths and its complexity and context are manageable, Sol is sufficient.
- Choose between `gpt-6-astra` and `gpt-5.6-sol` based on domain fit, overall task difficulty, importance, ambiguity, context length, and required reliability—not by assuming Astra is always necessary or that one difficult substep determines the whole routing decision.
- An Astra primary agent may delegate well-bounded subtasks to `gpt-5.6-sol` with `high` or `xhigh` reasoning effort when that improves parallelism or cost control. Astra remains the coordinator and final reviewer.
- Difficult or high-stakes work—such as ambiguous requirements, cross-source synthesis, complex UI recovery, high-stakes interpretation, or irreversible operations—should be routed to `gpt-5.6-sol` (`high`/`xhigh`) or `gpt-6-astra` (`high`/`xhigh`) according to the task-level judgment above, rather than split mechanically by step count.
- If a task becomes materially harder than its initial classification, the primary agent may re-route it to a stronger model rather than forcing a lower-capability agent through repeated failed attempts.

### Review and completion
- Sub-agent output is provisional evidence or a work product, not an automatic source of truth. The primary agent must review it against the repository, authoritative sources, tests, and the user's requested outcome.
- The primary agent remains responsible for final scope, conflict resolution, integration, verification, user-facing explanation, and delivery.
- If a sub-agent encounters a blocker or needs user authorization, the primary agent should consolidate the issue and present one clear request rather than forwarding fragmented coordination messages.
