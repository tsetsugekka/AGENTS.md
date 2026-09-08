# Multi-agent delegation and model routing

- Delegate only independent subtasks with clear boundaries that can run in parallel and offer more benefit than coordination cost; define inputs, scope, constraints, deliverables, acceptance criteria, and editing permissions. Keep the number of agents proportional to independent work and avoid overlapping exploration.
- Assign one owner to each file or deliverable; do not edit the same file concurrently without coordinating ownership and a merge plan.
- Primary and sub-agents use the same routing for their respective scopes, starting with the least capable model that can complete the work reliably:
  - `gpt-5.6-luna high`: mechanical, well-specified tasks, including Computer Use that follows clear steps to obtain, confirm, and extract information from known pages.
  - `gpt-5.6-luna xhigh`: repetitive tasks requiring some judgment, such as extracting information from irregular pages or semi-structured content.
  - `gpt-6-astra low`: moderate complexity with controlled risk; `medium`: more complex work with clear boundaries. These replace the previous default `gpt-5.6-sol high/xhigh` route, without constituting a performance guarantee.
  - For complex reasoning or insufficient actual performance, raise Astra to `high`, then `xhigh` if necessary; do not automatically escalate because of long context, importance, step count, or a single benchmark, or let an inadequate model fail repeatedly.
  - `gpt-5.6-sol high/xhigh`: an alternative only for clear domain fit, Astra unavailability, or actual cost/latency advantages, not the default escalation when Astra is insufficient.
  - `gpt-5.6-terra high`: an option when implementation reliability or tool execution is the main risk.
- The primary agent must review sub-agent results against actual files, sources, and appropriate verification; it owns scope, integration, conflicts, and final delivery, and consolidates blockers or authorization needs into one clear request. Delegation does not expand authority.
