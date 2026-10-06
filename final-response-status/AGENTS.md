# Final response status

- End every final response with its actual status on a separate line at the very end, never on the same line as the body: 🔴Awaiting choice, 🔴Awaiting discussion, 🟥Blocked and interrupted, 🟡Awaiting confirmation, 🟡Partially complete, 🟢Progressing smoothly, or 🟩Complete. Briefly explain unfinished work or blockers in the body, and do not present a pause or partial completion as full completion.
- The local Stop hook additionally checks for a missing status label; it does not judge whether completion is truthful. See [README.md](README.md) for its execution contract.
