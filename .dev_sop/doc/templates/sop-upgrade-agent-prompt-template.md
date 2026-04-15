# SOP Upgrade Agent Prompt Template

Use this template to hand a copied project's SOP upgrade to an AI agent.
This is a prompt scaffold, not a durable project document.
This template assumes the AI is already running inside the target project repository.
The source SOP repository path is embedded in the prompt as `[SOURCE_SOP_REPO_PATH] = [F:\ai_develop_sop]`.
That value is a local default from this repository's authoring environment, not a cross-platform requirement.
If the source SOP repository moves or you run on another platform, edit that one path before sending the prompt.

## Input

### Source SOP Repository Path
Absolute local path to the source Dev SOP repository that defines the target SOP package.
Default:
`[SOURCE_SOP_REPO_PATH] = [F:\ai_develop_sop]`
Replace it with your own local SOP source path when the repository lives elsewhere.

### Target Project Context
The AI should treat the current workspace or current repository as the upgrade target.
Do not require a separate target project path in the prompt.

### Upgrade Target
By default, upgrade to the latest Dev SOP version declared in `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md`.
Do not require a manually filled target version unless you intentionally want to stop short of the latest source version.

### Upgrade Notes To Apply
Normally the applicable files under `[SOURCE_SOP_REPO_PATH]\.dev_sop\upgrades\` newer than the current project's version and up to the latest source version.

### Local Customizations To Preserve
List any project-owned SOP docs, skills, templates, or entrypoint wording that should be preserved unless directly incompatible with the target version.

### Allowed Scope
Usually:
- `.dev_sop/*`
- `README.md`
- `AGENTS.md`
- tool adapters such as `CLAUDE.md`

Only include root files when SOP path, version, navigation, or control-surface references must be updated.

### Forbidden Scope
Usually:
- product or application code
- project business docs unrelated to SOP wiring
- project task specs unrelated to the SOP package upgrade

### Validation Expectations
Specify the checks that must pass before the agent reports completion.
Examples:
- `.dev_sop/VERSION.md` matches the latest source version after the upgrade
- required control or upgrade files exist
- live SOP path references are updated
- preserved project-owned specs and local customizations remain intact

### Reporting Format
Specify how the agent should report:
- changed files
- preserved customizations
- validation performed
- remaining ambiguity or follow-up

## Execution Contract

The upgrading agent should:
- read the source repo's `.dev_sop/VERSION.md` and relevant `.dev_sop/upgrades/*.md`
- treat the current workspace repository as the target project
- read the current project's `.dev_sop/VERSION.md` if it exists
- if the current project has no version file yet, infer the closest starting structure and state that assumption explicitly
- compare the current project's version with the latest source version before editing
- use the source repo's current files as the target end-state reference
- use the source repo's upgrade notes as the migration procedure
- preserve project-owned real specs and project-local SOP customizations unless they conflict with the target contract
- keep changes narrow to SOP assets and required entrypoint or reference updates
- validate before updating the current project's `.dev_sop/VERSION.md`
- explicitly surface ambiguity when ownership or preservation is unclear

The upgrading agent should not:
- blindly replace the current project's entire `.dev_sop/` tree with the source tree
- delete project-owned real task specs under `.dev_sop/doc/specs/`
- delete starter-owned `example-*` reference specs that are still part of the package
- overwrite project-local SOP customizations without checking whether they conflict with the target version
- modify product or application code unless the request explicitly includes non-SOP work

## Copyable Prompt

```text
[SOURCE_SOP_REPO_PATH] = [F:\ai_develop_sop]

Use the source Dev SOP repository at `[SOURCE_SOP_REPO_PATH]` as the authoritative reference.
Treat the current workspace repository as the target project to upgrade.

Goal:
Upgrade the current project's SOP assets to the latest Dev SOP version defined by `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md`.

Follow this procedure:
1. Read `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md`.
2. Read the relevant upgrade notes under `[SOURCE_SOP_REPO_PATH]\.dev_sop\upgrades\`.
3. Read the current project's `.dev_sop/VERSION.md` if it exists.
4. If the current project has no version file, infer the closest starting structure from its current SOP layout and state that assumption explicitly before editing.
5. Determine which upgrade notes apply, then apply them in ascending version order until the project reaches the latest source version.
6. Use the source repo's current `.dev_sop/*`, `README.md`, `AGENTS.md`, and adapters as the end-state reference.
7. Preserve:
   - project-owned real task specs under `.dev_sop/doc/specs/`
   - project-local SOP customizations that do not conflict with the target version
   - starter-owned `example-*` reference specs that remain part of the package
8. Remove or rewrite only the SOP assets that the applicable upgrade notes make obsolete.
9. Keep edits scoped to SOP assets and required entrypoint or reference updates. Do not modify product or application code.
10. Validate:
    - the current project's `.dev_sop/VERSION.md` exists and matches the latest source version after the upgrade
    - required upgrade files and directories exist
    - live SOP path references match the target structure
    - preserved project-owned specs and local customizations are still intact
11. Update the current project's `.dev_sop/VERSION.md` only after the upgrade validates.
12. If the upgrade changes `AGENTS.md`, adapters, or other AI entrypoints, tell me to start a fresh Codex thread before using the upgraded SOP.

Report back with:
- a concise summary of the upgrade
- files changed
- preserved local customizations
- validation performed
- ambiguities, conflicts, or follow-up items that still need human review

If you cannot safely determine whether a spec or SOP customization is project-owned, preserve it and call out the ambiguity explicitly.
```

## Short Copyable Prompt

```text
[SOURCE_SOP_REPO_PATH] = [F:\ai_develop_sop]

请将当前工作仓库的 SOP 升级到 `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md` 定义的最新版本。

执行要求：
1. 当前工作仓库就是目标项目，不需要再询问项目路径。
2. 先读取 `[SOURCE_SOP_REPO_PATH]\.dev_sop\VERSION.md` 和 `[SOURCE_SOP_REPO_PATH]\.dev_sop\upgrades\*.md`，再读取当前项目的 `.dev_sop/VERSION.md`；如果当前项目没有该文件，请根据现有 SOP 结构推断起始版本，并明确说明你的判断。
3. 按版本升序应用所有需要的 upgrade note，直到当前项目达到源 SOP 的最新版本。
4. 以源仓库当前的 `.dev_sop/*`、`README.md`、`AGENTS.md`、`CLAUDE.md` 作为目标结构参考。
5. 保留项目自有的真实 task specs、项目内 SOP 本地定制，以及仍属于 starter 的 `example-*` 参考 specs。
6. 不要直接整棵覆盖当前项目的 `.dev_sop/`；不要删除归属不明确的文档，遇到歧义先保留并在结果里说明。
7. 只修改 SOP 相关资产和必要入口文档，不要修改业务代码或非 SOP 文档。
8. 完成后验证：
   - 当前项目的 `.dev_sop/VERSION.md` 已更新为最新版本
   - 必要目录和文件存在
   - 旧路径和旧结构引用已修正
   - 需要保留的 specs 和本地定制仍然存在
9. 最后输出：升级摘要、改动文件、保留的本地定制、验证结果、剩余风险或歧义。
10. 如果升级修改了 `AGENTS.md`、adapter 或其他 AI 入口文件，请明确提示我在后续继续使用前新开一个 Codex 线程。
```

## Usage Note

Before sending the prompt, change only `[SOURCE_SOP_REPO_PATH]` if the source SOP repository is no longer `F:\ai_develop_sop`.
That default path is repository-local, not part of the Dev SOP contract.
