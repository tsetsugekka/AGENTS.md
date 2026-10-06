# Automatic case studies and applicability maintenance

Read these rules when discovering reusable experience, looking up a similar issue, or updating a case. Do not load case text for unrelated tasks.

## When to record automatically

- When an error, repeated failure, unexpected limitation, important root cause and fix, or newly verified effective approach has reuse value, automatically create or update a case before finishing the task without asking each time. Ordinary successes, minor trial and error, and isolated issues with no reuse value need not be recorded individually.
- Check the relevant index first. Update an existing case for the same issue with new evidence, resolution, or an expiry explanation; create another only for different causes or applicability. An unresolved issue may be recorded with evidence and hypotheses to verify, clearly marking unknowns rather than inventing conclusions.
- Recording remains subject to current file permissions and project rules. If writing is blocked, preserve the content awaiting storage and explain; do not call a chat-only summary a persisted case.

## Archive by scope

- **Project:** Cases depending on a project's business rules, architecture, deployment, or data conventions belong in its existing CASE-STUDY document or case directory. If none exists, create an indexed `case-study/` collection consistent with the current structure.
- **Global:** Cross-project experience about tools, agents, collaboration, or general methods belongs in `case-study/` beside the global `AGENTS.md`, with one Markdown file per case and a `README.md` index. This is persistent storage, not a temporary directory; do not substitute a business-project folder for the global archive.
- **Skill-specific:** Personal experience useful only to one skill belongs in the external Private Reference case directory that skill defines. Handle publicly reusable material under its publishing rules.
- Maintain one authoritative text per case. Distill general lessons from a project case into independent global conclusions and link to the original evidence rather than copying the entire case. If the scope is uncertain, initially keep it in the project or skill closest to the facts.

## Time, evidence, and applicability

- Record the occurrence time, applicable project or tool and version/environment, issue and necessary evidence, cause or hypothesis to verify, action taken, actual verification result, reusable lesson, and last verification time. Include a timezone when a precise time is known. If the occurrence time is unknown, state “unknown” and record the first observation time instead of using the document creation date as the occurrence date.
- Maintain **issue status** (unresolved/resolved) separately from **lesson applicability** (currently applicable/needs review/obsolete), with supporting reasons. Resolving an issue does not invalidate its prevention lesson; a temporary workaround may cease to apply after an upstream fix.
- Before reuse, check the case's environment, version, last verification time, and expiry conditions. Verify current evidence for changing platform behavior, faults, or limitations before adopting the lesson. Old cases are clues, not overrides of current specifications or facts.
- When later work reveals an upstream fix, changed rules or versions, or a disproven conclusion, automatically update the relevant case and index with the change time, applicable scope, and replacement approach. Preserve evidence of the original event while removing obsolete advice from current recommendations; do not silently delete or rewrite history. Do not scan every case or set up scheduled monitoring by default.

## The collection and publication boundaries

- The index contains case titles and links, occurrence times, scopes, issue statuses, lesson applicability, and last verification times. Synchronize the relevant index when adding or updating a case. Find needed cases by topic or keyword rather than loading the entire collection into persistent context.
- Global cases are private and local by default; project cases follow project permissions and existing commit rules. Synchronizing maintenance rules does not authorize publishing actual cases. Public rule repositories or skill packages carry only maintenance rules, empty indexes, or templates. Publish actual cases only after the user specifies public release, necessary anonymization, and a permission check.
- Restrict global and skill-specific personal case directories to the current user, typically directory mode `700` and file mode `600` on POSIX systems, and exclude them from automatic synchronization and public packaging. Project cases follow existing project access rules.
- Do not retain credentials, complete private chats, authentication responses, or irrelevant identity information. Preserve the minimum evidence needed to reproduce and verify. Cross-scope references and publicly distilled lessons must not carry private project material or local absolute paths.
