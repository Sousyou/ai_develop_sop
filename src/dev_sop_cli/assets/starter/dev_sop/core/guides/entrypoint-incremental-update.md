# Entrypoint Incremental Update

Use this guide when upgrading `AGENTS.md` and `CLAUDE.md` in copied projects that may already contain project-local instructions.

The goal is to keep these files plain Markdown while still allowing future SOP updates to be applied incrementally.

## Core Rule

Do not replace `AGENTS.md` or `CLAUDE.md` wholesale when the target project already contains local instructions.
Instead, update them as section-based text documents.

The pure CLI path assumes the project is already standardized onto the canonical heading structure.
If a project has legacy free-form entrypoints, normalize it once before relying on future command-line upgrades.

## Canonical Source

When upgrading a copied project, use these source files from the SOP repository as the canonical installed entrypoint texts:

- `scripts/packaged-AGENTS.md`
- `scripts/packaged-CLAUDE.md`

These files represent what a copied project's root entrypoints should look like after installation.

## Managed Sections

Treat these sections as starter-managed:

For `AGENTS.md`:

- `## Codex Reading Order`
- `## Precedence Contract`
- `## Source Of Truth`
- `## Codex Notes`

For `CLAUDE.md`:

- `## Claude Code Reading Order`
- `## Claude Code Notes`

For both files:

- `## Project Local Notes`
  This section is project-owned and should be preserved.

## Incremental Merge Rules

1. Read the target project's current `AGENTS.md` and `CLAUDE.md`.
2. Read the canonical source files from the SOP repository.
3. Replace the bodies of matching starter-managed sections with the canonical source content.
4. Preserve unknown or project-specific sections that do not conflict with the new contract.
5. For standardized projects, keep the canonical heading order and move preserved project-specific guidance into `## Project Local Notes`.
6. If a local note is actually a durable operating rule, prefer moving it into `.dev_sop/project-rules/*` and leave only a short pointer in the entrypoint file.
7. Keep the files plain Markdown. Do not add HTML comments, sentinels, JSON metadata, or machine-only markers.

## When Full Replacement Is Acceptable

Whole-file replacement is acceptable only when one of these is true:

- the target file is clearly still starter-owned and has no project-local additions
- the target file is a near-copy of an older starter version and the local project has no meaningful entrypoint customizations
- the human explicitly approves overwriting local entrypoint content

If there is any uncertainty, preserve local text and report the ambiguity.

## Validation

After an incremental update:

- `AGENTS.md` still points to `.dev_sop/*` rather than to source-repo-only paths
- `CLAUDE.md` remains consistent with `AGENTS.md`
- preserved project-local notes are still present
- managed sections contain only starter-managed text; project-local notes stay under `## Project Local Notes` or separate custom headings
- no source-repo-only paths such as `product/*` appear in the copied project's entrypoint files
- the entrypoint headings remain readable, stable, and easy to diff in plain text
