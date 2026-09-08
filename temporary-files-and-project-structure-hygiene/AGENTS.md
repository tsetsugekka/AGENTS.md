# Temporary files and project structure hygiene

- Put session scratch files, diagnostics, downloads, and intermediates in the system temporary directory, preferably a task directory from `mktemp -d`. If repository-local scratch is necessary, reuse an existing ignored directory and keep incidental files out of version control.
- Before completion, remove task-created temporary artifacts known to have no future use. Report the location and purpose of anything deliberately retained for debugging, handoff, or requested reuse. Do not delete pre-existing, unfamiliar, or ambiguously owned files just because they look temporary; cleanup targets must be task-created or confirmed disposable.
- Inspect existing structure and documentation before adding a root-level directory; reuse existing locations and add only necessary, durable responsibilities.
