# Codex Market Skills Instructions

## Private local source and public release boundary
- This local repository is the private working source for market-related Codex skills. It may contain instructions, workflows, or references that are not meant for the public GitHub release.
- The public GitHub repository is a cleaned release target, not a full mirror of this local working source. Do not push the entire local tree to GitHub by default.
- Before publishing any market skill, export only the intended public-safe files, then scan README files, `SKILL.md`, references, scripts, examples, and assets for private paths, account names, API keys, tokens, cookies, logs, screenshots, or non-public data source details.
- Keep the public README and repository metadata free of private identity and local machine paths.

## Global install policy
- Global installs under `~/.codex/skills` may symlink to this local repository when the skill is intended for everyday cross-project use.
- Current market skills intended to be globally available include the stock move reason, theme strength, survey heat, macro/news, calendar, strategist, sentiment, technical, and US gamma workflows.
- If adding a new global market skill, prefer a symlink from `~/.codex/skills/<skill-name>` to `skills/<skill-name>` so the installed copy stays in sync with this private local source.
- Do not globally install one-off experiments, private account-specific workflows, or temporary research prompts unless the user explicitly asks.

## Maintenance discipline
- Treat `skills/` in this repository as authoritative for local market-skill behavior.
- Do not treat temporary worktree or system temporary-directory copies as authoritative.
- If a skill changes in a way that should be public, update the cleaned public release deliberately; if it is private-only, keep it local.
