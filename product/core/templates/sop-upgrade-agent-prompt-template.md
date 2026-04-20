# SOP Upgrade Agent Prompt Template

Use this template to hand a copied project's SOP upgrade to an AI agent.
This is a prompt scaffold, not a durable project document.
This template assumes all repositories are available on the same local machine.

The source SOP repository path is typically:

`[SOURCE_SOP_REPO_PATH] = F:\ai_develop_sop`

Replace only the target-project placeholder before sending the prompt.

## Copyable Prompt

```text
[SOURCE_SOP_REPO_PATH] = F:\ai_develop_sop
[TARGET_PROJECT_PATH] = [path-to-target-project]

Use the source Dev SOP repository at `[SOURCE_SOP_REPO_PATH]` as the authoritative reference.
Treat `[TARGET_PROJECT_PATH]` as the target project to upgrade.
Work inside `[TARGET_PROJECT_PATH]`.

Goal:
Upgrade the target project's SOP assets to the latest Dev SOP version defined by `[SOURCE_SOP_REPO_PATH]\product\VERSION.md`.

Follow this procedure:
1. Read `[SOURCE_SOP_REPO_PATH]\product\VERSION.md`.
2. Read the relevant upgrade notes under `[SOURCE_SOP_REPO_PATH]\product\upgrades\`.
3. Read the current project's `.dev_sop/VERSION.md` if it exists.
4. If the current project has no version file, infer the closest starting structure from its current SOP layout and state that assumption explicitly before editing.
5. Determine which upgrade notes apply, then apply them in ascending version order until the project reaches the latest source version.
6. Treat each upgrade note as the contract for its own target version. Use the source repo's current files only as the final end-state reference.
7. For `AGENTS.md` and `CLAUDE.md`, do a pure-text incremental update rather than a blind overwrite:
   - read `[SOURCE_SOP_REPO_PATH]\product\core\guides\entrypoint-incremental-update.md`
   - use `[SOURCE_SOP_REPO_PATH]\scripts\packaged-AGENTS.md` as the canonical installed `AGENTS.md`
   - use `[SOURCE_SOP_REPO_PATH]\scripts\packaged-CLAUDE.md` as the canonical installed `CLAUDE.md`
   - preserve project-local sections and notes
   - if the target file is legacy and lacks stable headings, rewrite it into the canonical heading order and move preserved project-local text into `## Project Local Notes`
   - only replace the whole file if it is clearly still starter-owned and has no meaningful local additions
8. Preserve:
   - project-owned real task specs under `.dev_sop/project-specs/*`
   - project-owned facts under `.dev_sop/project-facts/*`
   - project-owned rules under `.dev_sop/project-rules/*`
   - project-local SOP customizations that do not conflict with the target version
   - project-local notes kept in `AGENTS.md` or `CLAUDE.md`
   - starter-owned `example-*` reference specs under `.dev_sop/core/examples/specs/` when they remain part of the package
9. Remove or rewrite only the SOP assets that the applicable upgrade notes make obsolete.
10. Keep edits scoped to SOP assets and required entrypoint or reference updates. Do not modify product or application code.
11. Validate:
    - the current project's `.dev_sop/VERSION.md` exists and matches the latest source version after the upgrade
    - root `product/` and `dev/` exist as directories
    - if the applicable upgrade note requires a sandbox, root `sandbox/` exists as a directory
    - isolated test work is routed into `sandbox/` rather than ad hoc root `test*` directories when the upgrade note requires that normalization
    - required upgrade files and directories exist
    - live SOP path references match the target structure
    - preserved project-owned specs and local customizations are still intact
    - `AGENTS.md` and `CLAUDE.md` do not contain source-repo-only paths such as `product/*`
12. Update the current project's `.dev_sop/VERSION.md` only after the upgrade validates.
13. If the upgrade changes `AGENTS.md`, `CLAUDE.md`, or other active AI entrypoints, tell me to start a fresh Codex or Claude Code thread before using the upgraded SOP.

Report back with:
- a concise summary of the upgrade
- files changed
- preserved local customizations
- preserved entrypoint-local notes
- validation performed
- ambiguities, conflicts, or follow-up items that still need human review

If you cannot safely determine whether a spec, entrypoint note, or SOP customization is project-owned, preserve it and call out the ambiguity explicitly.
```

## Notes

- The source repository stores the canonical product tree under `product/*`.
- Copied projects should still end up with the installed SOP namespace under `.dev_sop/*`.
- The packaged installed entrypoints should be taken from `scripts/packaged-AGENTS.md` and `scripts/packaged-CLAUDE.md`, not from the source repository's own root `AGENTS.md` and `CLAUDE.md`.
