# ai_develop_sop

> A portable SOP engine for long-running AI-assisted software development.

## Overview

`ai_develop_sop` is a documentation-first governance framework for projects where AI participates in:

- long-running implementation
- staged planning and review
- fact writeback
- recovery and correction
- rule and standard accumulation

The core model is:

- Decision layer: `project -> phase`
- Execution layer: `plan -> task`

## Injection Model

This repository can be used in two ways:

1. as the SOP design repository itself
2. as a complete SOP engine injected into another project

When injected into another project, the expected structure is:

```text
<host-project>/
|- AGENTS.md
|- ai_develop_sop/
|  |- project_entry.md
|  |- ai_project_quickstart.md
|  |- ai_project_sop.md
|  |- ai_project_type.md
|  |- ai_runtime_sop.md
|  |- ai_runtime_standards.md
|  |- ai_sop_init.bat
|  |- ai_sop_init.ps1
|  |- runtime/
|  |- sop/
|  |- rules/
|  |- facts/
|  |- skills/
|  `- standards/
`- product code / docs
```

The host-project `AGENTS.md` stays intentionally thin.
It only bootstraps AI into `ai_develop_sop/project_entry.md`.

All SOP governance assets stay under `ai_develop_sop/`.
The source-repository entry remains `ai_develop_sop/AGENTS.md`.

## Quick Start For Injection

1. Copy `ai_develop_sop/` into the target project root.
2. Run `ai_develop_sop/ai_sop_init.bat`.
3. Let the script generate the host-project `AGENTS.md`.
4. If the host project has no `README.md`, let the script generate a thin bootstrap README.
5. Enter through the generated host-project `AGENTS.md`.

Re-running `ai_sop_init.bat` resets the init-generated host bootstrap `AGENTS.md` and runtime files back to template state.
It does not reset `ai_develop_sop/AGENTS.md` itself.
For a brand-new injected project, `ai_sop_init.bat` creates a usable default `common` runtime immediately.

## What This Repository Provides

This is not a prompt collection.
It is a complete SOP engine that provides:

- workflow governance
- project-type routing
- injected-project entry
- low-token startup entry
- initialization bootstrap scripts
- rules and standards systems
- runtime supplements for real projects
- templates and recovery processes
- fact writeback processes
- skill accumulation structure

## Default Startup Path

For injected `common` projects, the default low-token startup path is:

`host AGENTS.md -> project_entry.md -> runtime/entry_state.md -> runtime/session_brief.md -> ai_project_quickstart.md`

`runtime/session_brief.md` is a derived runtime digest. During normal operation it should be co-updated whenever its source runtime documents change.
