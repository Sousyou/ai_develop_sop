# Core Write-Back Rules

- Write back only when the information is both stable and reusable.
- Route current-state updates to `.dev_sop/control/*`.
- Route project-generated stable context to `.dev_sop/project-facts/*`.
- Route project-generated operating-rule changes to `.dev_sop/project-rules/*`.
- Route starter-owned reusable workflow changes to `.dev_sop/core/skills/*` only when the shared SOP package itself changed.
- Route starter-owned baseline-rule changes to `.dev_sop/core/rules/*` only when the shared SOP package itself changed.
- Keep repository-local backup material under `.dev_sop/_backup/*` only when it should be retained without shipping on the starter surface.
- Do not turn facts, rules, skills, backup files, or control files into an archive of task chatter.
- If the information will not matter later, cannot be reused later, or has no clear destination, do not write it back.
