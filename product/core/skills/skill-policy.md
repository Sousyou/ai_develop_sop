# Skill Policy

A skill is a reusable workflow, not just a useful prompt.

## Skill surface

- Keep reusable shipped skills under `.dev_sop/core/skills/*`.
- Do not create a second project-local skill tree.
- If a copied project needs a local operating change, prefer updating `.dev_sop/project-rules/*`.

## Create or update a skill when

- the workflow repeats
- the inputs and outputs are recognizable
- the workflow reduces repeated reasoning work
- the workflow can be reused outside a single one-off task
