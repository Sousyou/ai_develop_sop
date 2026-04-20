# Core Workflow Rules

- Start from a plan, a phase slice, an existing task spec, or a clearly scoped task request.
- If a plan or phase slice exists, derive or refine one or more task specs before implementation.
- Default flow: `plan -> spec -> implementation -> validation -> closeout`.
- Use a written plan only when the plan should become a durable artifact worth re-reading, sharing, or handing off.
- Keep longer work explicit as `project_target -> current_target -> phase -> plan -> task` when that hierarchy adds clarity.
- If iterating within the same reviewable slice, refine the existing spec instead of creating parallel specs.
- If the primary outcome, boundary, or validation path changes, create a new dated spec before implementation.
- A task may skip spec creation only when it is already effectively spec-complete and trivially narrow.
- Treat `trivially narrow` as all of:
  - one primary reviewable outcome
  - obvious and tightly bounded allowed edits
  - obvious lightweight validation
  - no unresolved phase, dependency, or decision boundary
  - no meaningful write-back or closeout ambiguity
- Before implementation, bind the spec to the applicable baseline rules, project rules, and any approved exceptions.
- Validate explicitly after implementation, including any stronger project-specific validation gates.
