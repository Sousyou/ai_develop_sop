<!-- generated_by_ai_develop_sop_runtime_init -->
# Project Mount

- `product_roots`: `fallback:project_root_except_sop_root`
- `product_docs_roots`: `none`
- `non_product_roots`: `./{{SOP_DIR_NAME}}`
- `scratch_roots`: `none`

## Notes

1. This default mount lets a newly injected project start work immediately.
2. Refine this file only when the host project has clear directory boundaries that matter in practice.
