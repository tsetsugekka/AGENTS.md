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
- For work that would previously have used `gpt-5.6-sol` with `high` or `xhigh`, first evaluate `gpt-6-astra` with `low` or `medium`: use `low` for moderate complexity with controlled risk, and `medium` for more complex bounded reasoning. This is a routing preference, not a performance guarantee; long context or importance alone does not require `high`.
- When complex reasoning is required or Astra `low`/`medium` proves insufficient, increase Astra to `high`, and use `xhigh` only when clearly needed. High-risk work still requires appropriate authorization and verification.
- Keep `gpt-5.6-sol` with `high` or `xhigh` as a horizontal alternative only when Sol has a clear domain-fit, availability, cost, or latency advantage. Do not use it as the default upgrade path or default delegation target.
- Apply the same routing criteria to primary and delegated work. An Astra primary agent does not default to sending subtasks to Sol; Astra remains the coordinator and final reviewer.
- Use `gpt-5.6-terra` with `high` when implementation reliability or tool execution is the main concern. Adjust routing based on actual task performance, not a single benchmark or step count, and do not force a lower-capability model through repeated failures.
- If a task becomes materially harder than its initial classification, the primary agent may re-route it to a stronger model rather than forcing a lower-capability agent through repeated failed attempts.

### Review and completion
- Sub-agent output is provisional evidence or a work product, not an automatic source of truth. The primary agent must review it against the repository, authoritative sources, tests, and the user's requested outcome.
- The primary agent remains responsible for final scope, conflict resolution, integration, verification, user-facing explanation, and delivery.
- If a sub-agent encounters a blocker or needs user authorization, the primary agent should consolidate the issue and present one clear request rather than forwarding fragmented coordination messages.
