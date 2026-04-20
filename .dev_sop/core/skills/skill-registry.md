# Shared Skill Registry

Keep this registry in sync with the files in `.dev_sop/core/skills/`.
Use it for reusable shipped skills only.

| Name | Purpose | Trigger | Inputs | Outputs | Status |
|---|---|---|---|---|---|
| `plan-to-spec` | Convert a plan or phase slice into one or more narrow task specs | A plan or phase slice exists and work is about to move into implementation | plan or phase slice, current context, constraints, risks, and repository rules | one or more specs with scope, rule binding, checklist, done condition, validation, and write-back guidance | active |
| `design-whitebox-tests` | Decide whether and how to add white-box protection | A task touches complex internal logic or regression-sensitive code | task spec, bug context, internal logic details | white-box test decision, protected logic targets, regression guidance | active |
| `session-closeout` | Decide what durable updates, if any, should happen after a slice completes | A task or slice is finishing and control-surface, fact, rule, or skill write-back may be needed | completed task or slice, current control surface state, any decision or experiment outcome, and candidate reusable context | targeted control-surface updates, optional fact updates, optional rule updates, optional shared-skill updates, or an explicit no-write-back outcome | active |
