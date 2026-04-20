# Core Boundary Rules

- Prefer the smallest coherent change.
- Do not introduce speculative abstractions or opportunistic redesigns.
- Do not let task or sub-plan execution quietly redefine project or phase boundaries.
- Keep starter-owned baseline assets under `.dev_sop/core/*`.
- Keep project-generated rule files under `.dev_sop/project-rules/*`.
- Keep project-generated task specs under `.dev_sop/project-specs/*`.
- Keep project-generated facts under `.dev_sop/project-facts/*`.
- Keep current-state recovery assets under `.dev_sop/control/*`.
- Keep copied-project working directories at the repository root rather than inside `.dev_sop/*`.
- Use root `product/` for final product outputs or deliverables.
- Use root `dev/` for in-progress development artifacts, drafts, or intermediate outputs.
- Use root `sandbox/` only when a disposable test or experiment environment is needed.
- Do not scatter ad hoc root `test*`, `tmp*`, or `playground*` directories when `sandbox/` is the intended isolated workspace.
- Keep shipped-system, product, architecture, operations, and user-facing documentation outside `.dev_sop/`.
- Do not silently relax project hard rules from a task spec.
- Do not reintroduce removed legacy adapter surfaces or old mixed roots into the mainline package except in historical upgrade notes.
