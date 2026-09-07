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
- For difficult but bounded work with manageable context, first evaluate `gpt-6-astra` with `low` or `medium` reasoning effort: use `low` for moderate complexity with controlled risk, and `medium` for more complex bounded reasoning. Long context, importance, or a former Sol tier alone does not require `high`; use a higher Astra effort only when the reasoning depth, risk, or observed result requires it.
- Keep `gpt-5.6-sol` with `high` or `xhigh` as a horizontal alternative when Sol has a clear domain-fit, availability, cost, latency, or deliberate-delegation advantage. Do not treat it as the default route for difficult work or for sub-agent delegation.
- For high-importance, ambiguous, high-risk, or higher-reliability work, use the Astra effort that matches the actual reasoning need, increasing to `high` or `xhigh` only when warranted. Use `gpt-5.6-terra` with `high` reasoning effort when implementation reliability or tool execution is the main concern.
- Treat `gpt-6-astra` with `low` or `medium` and `gpt-5.6-sol` with `high` or `xhigh` as overlapping migration options. Choose by domain fit, overall difficulty, importance, ambiguity, context length, cost, and required reliability; do not mechanically substitute based on a single benchmark or one difficult substep.
- Apply the same routing criteria to primary and delegated work. An Astra primary agent may delegate a well-bounded subtask to `gpt-5.6-sol` with `high` or `xhigh` only when that explicit advantage exists; Astra remains the coordinator and final reviewer.
- Work that exceeds Astra `low`/`medium` should normally move to a higher Astra effort. Use Sol (`high`/`xhigh`) only when a clear alternative-route reason exists; ambiguous requirements, cross-source synthesis, complex UI recovery, high-stakes interpretation, or irreversible operations still require task-level judgment rather than mechanical splitting.
- If a task becomes materially harder than its initial classification, the primary agent may re-route it to a stronger model rather than forcing a lower-capability agent through repeated failed attempts.

### Review and completion
- Sub-agent output is provisional evidence or a work product, not an automatic source of truth. The primary agent must review it against the repository, authoritative sources, tests, and the user's requested outcome.
- The primary agent remains responsible for final scope, conflict resolution, integration, verification, user-facing explanation, and delivery.
- If a sub-agent encounters a blocker or needs user authorization, the primary agent should consolidate the issue and present one clear request rather than forwarding fragmented coordination messages.
