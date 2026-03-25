# Document Routing Matrix Standard

- **Version**: `v2.0`
- **Status**: official standard
- **Role**: defines where each information type should be written

---

## Purpose

This standard answers:

1. where a piece of information belongs
2. when to write product docs versus SOP governance docs
3. when to write `rules` versus `standards`
4. where long-term goals and current goals should go

---

## Decision Order

When routing information, check in this order:

1. is it about the product itself or about how AI works
2. is it a stable fact, a process rule, a hard standard, or runtime instance state
3. is it cross-project and long-term, or current-project and immediate
4. is it a long-term goal or a current high-frequency goal

---

## Routing Matrix

| Information type | Default destination | Note |
| --- | --- | --- |
| Product architecture, modules, run instructions, integration instructions | product docs roots | describes the product itself |
| Long-term stable project goal, long-term boundary, top-level constraints | `runtime/project_charter.md` | low-frequency stable definition |
| High-frequency current goal, current scope, current validation target | `runtime/current_target.md` | current target only |
| Confirmed stable conclusions | `facts/*` | stable facts only |
| Workflow model, layer roles, formal process definitions | `ai_project_sop.md` / `sop/*` | formal SOP body |
| Execution guardrails and mandatory checks | `rules/*` | process restrictions |
| Cross-project hard standards | `standards/*` | stable baseline standards |
| Current-project hard standard deltas | `ai_runtime_standards.md` | runtime standards |
| Current-project flow deltas | `ai_runtime_sop.md` | runtime process deltas |
| Scratch notes and temporary one-off records | scratch roots | not authoritative |

---

## Key Boundaries

1. product docs answer what the system is and how it works
2. SOP docs answer how AI should organize work
3. `rules` answer what process constraints must be obeyed
4. `standards` answer what hard unified constraints artifacts must satisfy
5. `facts` are stable conclusions, not temporary goals
6. `project_charter` is long-term; `current_target` is high-frequency

---

## Default Anti-Mixing Rules

1. do not use `ai_runtime_sop.md` for stable product facts
2. do not use `ai_runtime_standards.md` for process requirements
3. do not use `facts/*` for temporary plans
4. do not use product `README` as a substitute for `project_charter` or `current_target`
5. do not promote raw external plans directly into long-term rules or facts
