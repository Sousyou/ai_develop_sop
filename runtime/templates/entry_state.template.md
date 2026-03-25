<!-- generated_by_ai_develop_sop_runtime_init -->
# Entry State

- `initialized_at`: `{{GENERATED_AT}}`
- `project_type`: `common`
- `project_type_selected_at`: `{{GENERATED_AT}}`
- `runtime_mode`: `active`
- `default_plan_source`: `external_plan_preferred`
- `current_phase`: `bootstrap_ready`

## Notes

1. Valid `project_type` values are defined by `ai_project_type.md`.
2. Newly injected projects are initialized directly as `common` by `ai_sop_init.bat`.
3. When the project enters a new real phase, this file may update the current phase marker.
4. Re-running `ai_sop_init.bat` resets this file back to the default new-project state.
