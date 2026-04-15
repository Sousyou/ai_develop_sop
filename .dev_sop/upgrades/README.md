# Dev SOP Upgrades

This directory stores version-targeted upgrade notes for copied-project SOP upgrades.
Each upgrade note should be actionable enough that an AI agent can execute it directly inside a copied project.

## Naming

Store each upgrade note as:

`vX.Y.Z.md`

Each file documents how to upgrade to that target version.

## How To Use

1. read the copied project's `.dev_sop/VERSION.md`
2. compare it with the source starter's `.dev_sop/VERSION.md`
3. apply each newer upgrade note in ascending version order
4. preserve project-local SOP customizations unless the upgrade note explicitly replaces them
5. validate the SOP asset changes
6. update the copied project's `.dev_sop/VERSION.md`

If you want to hand the upgrade work to another AI agent, start from `.dev_sop/doc/templates/sop-upgrade-agent-prompt-template.md`.
That template assumes the AI is already running inside the target project repository and upgrades to the latest source SOP version by default.
It embeds the source SOP path as `F:\ai_develop_sop` because that is the local default in this starter repository.
If the source repository lives elsewhere or runs on another platform, replace that path before using the prompt.
If the upgrade changes `AGENTS.md`, adapters, or other AI entrypoints, start a fresh Codex thread after the upgrade before relying on the new rules.

## Scope

Upgrade notes in this directory are for SOP assets only.
They are not a project release log and not an application change history.

## Authoring Rule

Write each upgrade note as an execution document, not just a summary.
Prefer these sections when they help:

- target version
- applies to
- end-state contract
- required changes
- preserve rules
- validation
- completion rule
