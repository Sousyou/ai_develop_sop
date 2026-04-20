# Skill: session-closeout

## Purpose
Close out a completed slice without turning the control surface, facts, rules, or skills into an archive of task chatter.

Use it after required validation and before reporting a task or slice as fully done when the repository uses `.dev_sop/control/*`.

## Inputs
- current task spec or completed slice
- current `.dev_sop/control/CURRENT.md`
- any new decision or experiment outcome
- any candidate fact or reusable workflow learning

## Outputs
- updated `.dev_sop/control/CURRENT.md` when current operating state changed
- updated `.dev_sop/control/DOC_MAP.md` only when document roles or reading order changed
- a project fact update under `.dev_sop/project-facts/*` when durable reusable decision rationale or experiment outcomes should be preserved
- a project rule update under `.dev_sop/project-rules/*` when the current repository's operating contract changed
- a core rule or shared skill update under `.dev_sop/core/*` only when the shared SOP package itself changed
- no write-back when nothing durable changed
