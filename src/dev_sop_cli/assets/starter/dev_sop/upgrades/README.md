# Dev SOP Upgrades

This directory stores version-targeted upgrade notes for copied-project SOP upgrades.
The current line starts from the stable CLI baseline at `1.0.0`.

## Naming

Store each future upgrade note as:

`vX.Y.Z.md`

Each file documents how to upgrade from the current installed baseline to that target version.

## How To Use

1. read the copied project's `.dev_sop/VERSION.md`
2. compare it with the source starter's current package version
3. apply each newer upgrade note in ascending version order
4. preserve project-local SOP customizations unless an upgrade note explicitly replaces them
5. use each upgrade note as the contract for its own version step
6. validate the SOP asset changes
7. update the copied project's `.dev_sop/VERSION.md`

If you want to hand the upgrade work to another AI agent, start from `.dev_sop/core/templates/sop-upgrade-agent-prompt-template.md` and use the current upgrade note as the version-specific contract.

## Scope

Upgrade notes in this directory are for SOP assets only.
They are not a project release log and not an application change history.

## Baseline

- `1.0.0` is the first stable baseline for pure command-line SOP updates
- later starter-managed changes must bump the package version instead of mutating `1.0.0`
