# AI Project SOP

- **Version**: `v2.1`
- **Status**: official
- **Role**: master navigation and master principles for the SOP

---

## Purpose

This file defines:

1. the overall workflow model
2. how decision and execution layers are separated
3. what `project`, `phase`, `plan`, and `task` each own
4. where initialization, execution, writeback, correction, and skill accumulation go
5. how AI should enter the system with minimal context first

This file is the master navigation document. It does not replace layer definitions, rules, templates, or standards.

---

## Overall Model

The SOP uses:

- decision layer: `project -> phase`
- execution layer: `plan -> task`

Roles:

- `project`: low-frequency, highest-authority, long-term direction and constraints
- `phase`: high-frequency current controller aligned to the current target
- `plan`: execution orchestration under the current phase, with `external_plan_preferred` by default
- `task`: smallest controllable execution unit

The goal is not to add paperwork. The goal is to separate:

- long-term direction
- current stage control
- execution ordering
- minimal execution units

so the workflow resists drift, over-expansion, and context loss.

---

## Core Flow

Main execution chain:

`project -> current phase -> current main plan -> task`

Return flow:

`task -> main plan / sub plan -> current phase -> project`

Global constraints:

1. only one `current phase` may be active at a time
2. one phase may have only one active `main plan` at a time
3. tasks must return to their plan after completion
4. project-level changes must be reviewed through the current phase, not punched directly into execution
5. parallelism belongs only in the execution layer

---

## Lifecycle View

### Initialization

Goal:

- define `project`
- define `project_charter`
- define `current_target`
- define the current `phase`
- establish the minimum governance skeleton

Entry:

- `sop/processes/project_bootstrap_sop.md`
- `sop/processes/project_init_artifacts.md`

### Phase Execution

Goal:

- let `phase` start or accept a `main plan`
- let `plan` drive execution
- let `task` close minimal loops

Entry:

- `sop/core/phase_layer.md`
- `sop/core/plan_layer.md`
- `sop/core/task_layer.md`

### Review And Handoff

Goal:

- run a `Phase Review` after each main-plan closure
- decide continue / correct / pause / exit / escalate
- produce `next_phase_request` when needed

Templates:

- `sop/templates/phase_review_template.md`
- `sop/templates/next_phase_request_template.md`

### Fact Writeback

Goal:

- write stable facts into the right layer
- avoid promoting process noise into long-term facts

Entry:

- `sop/processes/fact_writeback_sop.md`
- `rules/writeback_rules.md`

### Maintenance And Recovery

Goal:

- handle scope drift
- handle over-design
- handle facts-vs-implementation mismatch
- handle broken execution mainlines

Entry:

- `sop/processes/maintenance_recovery_sop.md`

### Skill Accumulation

Goal:

- move repeated, stable, testable patterns into skills

Entry:

- `skills/skill_policy.md`
- `skills/skill_registry.md`
- `skills/skill_template.md`

---

## Document System

Suggested layers:

1. master navigation: `ai_project_sop.md`
2. core definitions: `sop/core/*`
3. templates: `sop/templates/*`
4. execution design helpers: `sop/design/*`
5. process SOPs: `sop/processes/*`
6. rules: `rules/*`
7. facts: `facts/*`
8. skills: `skills/*`
9. cross-project standards: `standards/*`
10. runtime flow layer: `ai_runtime_sop.md`, `runtime/project_charter.md`, `runtime/current_target.md`
11. runtime standards layer: `ai_runtime_standards.md`, `runtime/*`
12. injected-project entry layer: host `AGENTS.md`, `project_entry.md`, `ai_project_quickstart.md`

---

## Injected Common Project Entry

For injected `common` projects, the default low-token path is:

`host AGENTS.md -> project_entry.md -> runtime/entry_state.md -> runtime/session_brief.md -> ai_project_quickstart.md`

Only expand further when needed.

`ai_project_sop.md` remains the full spec, not the default first read for every session.

---

## Core Operating Principles

1. align boundaries before implementation
2. align validation before execution
3. write back stable facts
4. correct drift before pushing deeper
5. route information to the correct document layer
6. prefer external plans first in normal execution
7. separate `project_charter` from `current_target`

---

## Conclusion

The SOP is a layered governance system, not a linear checklist.
Use the low-token entry by default, then open deeper layers only when the current problem requires them.
