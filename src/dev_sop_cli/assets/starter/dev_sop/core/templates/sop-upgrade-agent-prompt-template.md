# SOP Upgrade Agent Prompt Template

Use this template to hand a copied project's SOP upgrade to an AI agent.
This is a prompt scaffold, not a durable project document.
This template assumes the AI is already running inside the target project repository.

The source SOP repository path is embedded in the prompt as:

`[SOURCE_SOP_REPO_PATH] = [path-to-source-sop-repo]`

Replace that placeholder with the actual path to the source SOP repository before sending the prompt.

## Copyable Prompt

```text
[SOURCE_SOP_REPO_PATH] = [path-to-source-sop-repo]

Use the source Dev SOP repository at `[SOURCE_SOP_REPO_PATH]` as the authoritative reference.
Treat the current workspace repository as the target project to upgrade.

Goal:
Upgrade the current project's SOP assets to the latest Dev SOP version defined by `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md`.

Follow this procedure:
1. Read `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md`.
2. Read the relevant upgrade notes under `[SOURCE_SOP_REPO_PATH]\.dev_sop\upgrades\`.
3. Read the current project's `.dev_sop/VERSION.md` if it exists.
4. If the current project has no version file, infer the closest starting structure from its current SOP layout and state that assumption explicitly before editing.
5. Determine which upgrade notes apply, then apply them in ascending version order until the project reaches the latest source version.
6. Treat each upgrade note as the contract for its own target version. Use the source repo's current files only as the final end-state reference.
7. Preserve:
   - project-owned real task specs under `.dev_sop/project-specs/*`
   - project-owned facts under `.dev_sop/project-facts/*`
   - project-owned rules under `.dev_sop/project-rules/*`
   - project-local SOP customizations that do not conflict with the target version
   - starter-owned `example-*` reference specs under `.dev_sop/core/examples/specs/` when they remain part of the package
8. Remove or rewrite only the SOP assets that the applicable upgrade notes make obsolete.
9. Keep edits scoped to SOP assets and required entrypoint or reference updates. Do not modify product or application code.
10. Validate:
    - the current project's `.dev_sop/VERSION.md` exists and matches the latest source version after the upgrade
    - required upgrade files and directories exist
    - live SOP path references match the target structure
    - preserved project-owned specs and local customizations are still intact
11. Update the current project's `.dev_sop/VERSION.md` only after the upgrade validates.
12. If the upgrade changes `AGENTS.md`, `CLAUDE.md`, or other active AI entrypoints, tell me to start a fresh Codex or Claude Code thread before using the upgraded SOP.

Report back with:
- a concise summary of the upgrade
- files changed
- preserved local customizations
- validation performed
- ambiguities, conflicts, or follow-up items that still need human review

If you cannot safely determine whether a spec or SOP customization is project-owned, preserve it and call out the ambiguity explicitly.
```
