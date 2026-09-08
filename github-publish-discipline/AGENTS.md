# GitHub publish discipline

- Apply to all work. Do not create, switch to, or push a new working branch unless the user explicitly requests a branch, PR, draft PR, or experimental branch.
- Direct commit, push, or GitHub publish/update requests default to the intended target branch, usually `main`; confirm with `git branch --show-current` before staging or committing.
- If on an old temporary branch, safely move work to the target branch or fast-forward as appropriate; otherwise ask before publishing. Do not continue by inertia. Delete local and remote temporary branches after merging when no longer needed.
