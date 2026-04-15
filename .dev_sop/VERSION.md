# Dev SOP Version

## Current Version
`0.4.0`

## Release Date
`2026-04-15`

## Source Of Truth
This file is the source of truth for the current Dev SOP version in this repository or in a copied project.

## Current Contract

- the SOP namespace root is `.dev_sop/`
- the recovery/control surface contains only `.dev_sop/control/CURRENT.md` and `.dev_sop/control/DOC_MAP.md`
- `.dev_sop/doc/specs/` keeps only `README.md`, starter-owned `example-*` reference specs, and project-owned real task specs
- version-targeted SOP upgrade notes live under `.dev_sop/upgrades/*`

## Upgrade Use

When upgrading SOP assets in a copied project:

1. read the copied project's `.dev_sop/VERSION.md`
2. compare it with the source starter's `.dev_sop/VERSION.md`
3. apply each newer upgrade note in `.dev_sop/upgrades/*` in ascending version order
4. preserve project-local SOP customizations unless an upgrade note explicitly replaces them
5. update the copied project's `.dev_sop/VERSION.md` only after the upgrade lands and validates

## Notes

- this version tracks the SOP package, not the product or application
- upgrade notes describe SOP asset changes, not application-code changes
