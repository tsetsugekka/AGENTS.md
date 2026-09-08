# Temporary files and project structure hygiene

- Put session temporary files, diagnostics, downloads, and intermediates in the system temporary directory, preferably a task directory created with `mktemp -d`; if repository-local temporary storage is necessary, reuse an ignored temporary directory and avoid polluting version control.
- Before completion, clean up temporary artifacts created by this task that are known to be no longer needed; report the location and purpose of anything retained for debugging or handoff. Do not delete pre-existing, unfamiliar, or ambiguously owned files based on appearance alone.
- Before adding a subdirectory at the project root, inspect the existing structure and documentation and prefer reuse; add directories only for genuinely necessary long-term responsibilities.
