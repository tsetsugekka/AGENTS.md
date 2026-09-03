# GitHub publish discipline
- This applies to all future Codex work, not only stock-related skills or a single repository.
- Do not create, switch to, or push a new working branch unless the user explicitly asks for a branch, PR, draft PR, or experimental branch.
- For direct requests such as "commit", "push", "publish to GitHub", "update GitHub", or "发布到 GitHub", default to the repository's intended target branch, usually `main`.
- Before staging or committing, run `git branch --show-current` and confirm it is the intended target branch. If it is not, switch or fast-forward to the target branch before committing.
- If an old temporary branch is already checked out, do not keep using it by inertia. Either move the work onto the target branch when safe, or ask the user before publishing from that branch.
- After a temporary branch has been merged into the target branch and is no longer needed, delete the local and remote temporary branch.
