# Multi-agent delegation and model routing

- Delegate only independent, bounded subtasks that can progress in parallel and justify their coordination cost. Define inputs, scope, constraints, deliverables, acceptance criteria, and editing permission; keep agent count proportional to independent work and avoid overlapping exploration.
- Assign one owner per file or deliverable; coordinate ownership and merging before allowing concurrent edits.
- Apply the same routing to primary and delegated work, starting with the least capable model that can reliably complete each scope:
  - `gpt-5.6-luna high`: mechanical, well-specified work, including Computer Use following clear steps to obtain, confirm, extract, or check information from known pages.
  - `gpt-5.6-luna xhigh`: repetitive work needing judgment, such as irregular layouts, semi-structured normalization, or bounded extraction ambiguity.
  - `gpt-6-astra low`: moderate complexity with controlled risk; `medium`: more complex but bounded work. These replace the default `gpt-5.6-sol high/xhigh` route, without guaranteeing performance.
  - For complex reasoning or insufficient results, raise Astra to `high`, then `xhigh` if needed. Do not escalate solely for long context, importance, step count, or one benchmark, or let an inadequate model fail repeatedly.
  - `gpt-5.6-sol high/xhigh`: an alternative only for clear domain fit, Astra unavailability, or demonstrated cost/latency advantage; not the default escalation from Astra or delegation target.
  - `gpt-5.6-terra high`: an option when implementation reliability or tool execution is the main risk.
- The primary agent reviews delegated results against actual files, authoritative sources, and appropriate verification; it owns scope, integration, conflicts, and delivery, and consolidates blockers or authorization needs into one clear request. Delegation does not expand authority; high-risk actions retain their authorization and verification requirements.
