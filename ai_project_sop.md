# AI 项目 SOP 总纲

- **版本**：v2.0
- **状态**：正式版
- **定位**：作为当前新版 SOP 的总导航，定义新工作流主模型、文档体系、使用顺序与全局原则。
- **适用范围**：后续所有使用 AI 参与创建、开发、维护和治理的工程项目。

---

## 1. 文档目标

本文件用于回答以下问题：

1. 当前新版 SOP 的主框架是什么。
2. 项目中的决策层与执行层如何划分。
3. `Project - phase - plan - task` 各自负责什么。
4. 项目初始化、执行、回写、纠偏与 skill 沉淀应如何进入对应文档。
5. 各类治理动作应进入哪些文档与入口。

本文件只负责总导航与总原则，不承载单层对象的全部细节定义，也不替代模板文档与规则文档。

---

## 2. 当前总框架

当前新版 SOP 采用：

- 决策层：`project -> phase`
- 执行层：`plan -> task`

其中：

- `project` 是低频、稳定、最高权威的项目定义层。
- `phase` 是高频、当前阶段唯一控制器，负责阶段治理与阶段审查。
- `plan` 是当前阶段下的执行主线编排层。
- `task` 是执行层中的最小可控执行单元。

这套结构的目标不是增加更多文档层级，而是把：

- 最终目标
- 当前阶段
- 执行主线
- 最小执行单元

彻底分开，从而解决 scope 漂移、任务失控、主线缺失和结论沉淀困难的问题。

---

## 3. 四层主模型

### 3.1 `project`

负责：

- 定义最终产品目标与高层路径
- 定义长期边界
- 定义顶层约束
- 记录跨阶段稳定事实
- 承接全局级调整建议

不负责：

- 当前阶段执行排序
- 当前 `plan` 主线
- 单个 `task` 实现细节

当前正式入口：`sop/core/project_layer.md`

### 3.2 `phase`

负责：

- 定义当前阶段目标、非目标与交付边界
- 作为当前阶段唯一控制器
- 吸收 `project` 变化并对当前阶段做一致性纠错
- 发起并监管 `main plan`
- 执行 `Phase Review`
- 判断是否上报 `project` 事实、登记 `skill candidate` 或 `SOP candidate`

不负责：

- `project` 的正式最终定义改写
- 单个 `task` 的实现细节

当前正式入口：`sop/core/phase_layer.md`

### 3.3 `plan`

负责：

- 作为当前 `phase` 下的执行编排层
- 维护当前 `main plan`
- 管理 `plan item` 顺序、状态和重排
- 在必要时派生 `sub plan`
- 接收执行回流并做主线决策

不负责：

- 定义 `project` 长期目标
- 定义 `phase` 边界
- 替代 `task` 的完整执行细节

当前正式入口：`sop/core/plan_layer.md`

### 3.4 `task`

负责：

- 作为最小可控执行单元
- 承载单一目标、明确边界、明确验证
- 产出结果、异常与未做事项
- 支持回滚与回主线

不负责：

- 改写 `phase` 边界
- 改写 `main plan` 顺序
- 自行扩展为新的执行主线

当前正式入口：`sop/core/task_layer.md`

---

## 4. 核心流转

当前新版 SOP 的主执行链为：

`project -> current phase -> current main plan -> task`

回流链为：

`task -> main plan / sub plan -> current phase -> project`

其中必须遵守以下核心约束：

1. 任一时刻只能有一个 `current phase`
2. 一个 `phase` 在任一时刻只能有一个当前生效的 `main plan`
3. `task` 完成后必须先回流到所属 `plan`
4. `project` 的变更必须先由当前 `phase` 审阅，不能直接打穿执行层
5. 并行只允许发生在执行层，不允许发生在 `project` 或 `phase` 层

当前正式入口：`sop/core/workflow_transition_rules.md`

---

## 5. 生命周期视角

虽然整体仍然保留“初始化、执行、回写、纠偏、沉淀”的治理需求，但这些内容不再以旧版线性任务视角为主，而是映射到四层模型中：

### 5.1 项目初始化

目标：

- 明确 `project`
- 明确当前 `phase`
- 建立最小治理骨架
- 建立后续 `plan` 与 `task` 的入口

当前入口：`sop/processes/project_bootstrap_sop.md`

### 5.2 阶段执行

目标：

- 由 `phase` 发起或接纳 `main plan`
- 由 `plan` 驱动执行主线
- 由 `task` 完成最小执行闭环

当前入口：

- `sop/core/phase_layer.md`
- `sop/core/plan_layer.md`
- `sop/core/task_layer.md`

### 5.3 审查与交接

目标：

- 每轮 `main plan` 收口后执行 `Phase Review`
- `phase` 判断是否继续、纠错、暂停、退出或上报问题
- 阶段完成后生成 `next_phase_request`

当前模板入口：

- `sop/templates/phase_review_template.md`
- `sop/templates/next_phase_request_template.md`

### 5.4 事实回写

目标：

- 将稳定事实按层级与类型回写到合适文档
- 不把过程噪音误写成长期事实

当前入口：`sop/processes/fact_writeback_sop.md`

### 5.5 维护与纠偏

目标：

- 处理 scope 漂移
- 处理过度设计
- 处理 facts 与实现失真
- 处理执行主线失效

当前入口：`sop/processes/maintenance_recovery_sop.md`

### 5.6 技能沉淀

目标：

- 将重复、稳定、可验证的流程沉淀为 skill
- 由 `phase` 负责候选判断，由 skill 层负责正式登记与模板化

当前入口：

- `skills/skill_policy.md`
- `skills/skill_registry.md`
- `skills/skill_template.md`

---

## 6. 文档体系

当前新版 SOP 文档体系建议划分为以下几层。

### 6.1 总纲层

- `ai_project_sop.md`

### 6.2 核心定义层

- `sop/core/project_layer.md`
- `sop/core/phase_layer.md`
- `sop/core/plan_layer.md`
- `sop/core/task_layer.md`
- `sop/core/workflow_transition_rules.md`

### 6.3 模板层

- `sop/templates/phase_review_template.md`
- `sop/templates/next_phase_request_template.md`
- `sop/templates/plan_item_template.md`
- `sop/templates/task_template.md`

### 6.4 执行层辅助设计

- `sop/design/main_plan_state_design.md`

### 6.5 流程型子 SOP

- `sop/processes/project_bootstrap_sop.md`
- `sop/processes/project_init_artifacts.md`
- `sop/processes/fact_writeback_sop.md`
- `sop/processes/maintenance_recovery_sop.md`

### 6.6 规则层

- `rules/*`

### 6.7 facts 层

- `facts/*`

### 6.8 skill 层

- `skills/skill_policy.md`
- `skills/skill_registry.md`
- `skills/skill_template.md`

### 6.9 跨项目标准层

- `standards/standards_index.md`
- `standards/*`

### 6.10 运行时流程层

- `ai_runtime_sop.md`

### 6.11 运行时标准层

- `ai_runtime_standards.md`

---

## 7. 非 `sop_develop` 项目的入口与运行时补充

对于非 `sop_develop` 类型项目，`AGENTS.md`、`ai_project_sop.md`、`ai_runtime_sop.md` 与 `ai_runtime_standards.md` 分别承担不同职责，必须明确区分，不得混用。

### 7.1 `AGENTS.md` 的职责

`AGENTS.md` 是项目入口门，而不是主规范正文。

它负责：

1. 判定当前项目类型。
2. 决定当前项目应进入哪条工作流。
3. 当项目类型已经确定且不属于 `sop_develop` 时，强制引导 AI 进入对应的正式项目工作流。
4. 要求 AI 先进入 `ai_project_sop.md`，并以其作为主规范文档。

`AGENTS.md` 不负责：

1. 重复承载 `project` 层的正式定义。
2. 重复承载 `phase` 层的正式定义。
3. 重复承载 facts、rules、templates 的正文内容。
4. 直接替代 `ai_project_sop.md`、`ai_runtime_sop.md` 或 `ai_runtime_standards.md`。

### 7.2 `ai_project_sop.md` 的职责

`ai_project_sop.md` 是当前项目工作流的主规范文档。

它负责：

1. 定义 AI 如何按照 SOP 执行开发。
2. 定义 `Project - phase - plan - task` 主模型。
3. 定义决策层与执行层的职责边界。
4. 定义权威文档、模板、facts、rules、standards 与子 SOP 的读取链路。
5. 定义非 `sop_develop` 类型项目应如何结合运行时补充进入正式开发流程。

这意味着 `ai_project_sop.md` 不只是描述结构，还必须描述：

- AI 应按什么顺序进入文档体系
- AI 应如何从入口进入执行
- AI 应如何根据层级对象、模板、规则、标准和 facts 推进开发

### 7.3 `ai_runtime_sop.md` 的职责

`ai_runtime_sop.md` 是非 `sop_develop` 项目的运行时补充流程文档。

它在非 `sop_develop` 项目开发中生效，主要用于承载该项目对主 SOP 的流程微调，以及存档真实项目运行过程中暴露出的 SOP 反馈信息。

它负责：

1. 沉淀该真实项目运行过程中发现的 SOP 待修改项。
2. 记录该项目相对主 SOP 需要采用的流程微调。
3. 记录暂时只属于该项目、尚未上升为全局 SOP 的流程调整。
4. 为后续 SOP 迭代提供来自真实项目运行期的反馈来源。

典型内容包括：

- 当前项目对主 SOP 的局部流程微调
- 当前项目的专项 review 或专项验收补充流程
- 当前真实项目暴露出的 SOP 缺口与待修订项

`ai_runtime_sop.md` 不负责：

1. 替代 `ai_project_sop.md` 成为全局主规范。
2. 直接改写 `project`、`phase`、`plan`、`task` 的正式定义。
3. 直接取代 rules、facts 或 templates 的正式职责。
4. 自动成为所有项目通用规则。

### 7.4 `ai_runtime_standards.md` 的职责

`ai_runtime_standards.md` 是非 `sop_develop` 项目的运行时补充标准文档。

它在非 `sop_develop` 项目开发中生效，主要用于承载当前项目相对正式标准的标准增量，以及存档真实项目运行过程中暴露出的标准反馈信息。

它负责：

1. 记录当前项目直接生效的标准。
2. 引用当前项目需要继承的正式跨项目标准。
3. 记录当前项目额外新增且必须遵循的项目级标准增量。
4. 记录暂时只属于该项目、尚未上升为正式 `standards/` 的标准调整。
5. 为后续标准审核与升级提供来源。

典型内容包括：

- 当前项目对正式标准的项目级补充
- 当前项目对正式标准的项目级收缩
- 当前项目临时增加但必须立即生效的标准增量
- 当前真实项目暴露出的标准调整项

`ai_runtime_standards.md` 不负责：

1. 替代 `standards/` 成为正式跨项目标准源。
2. 替代 `rules/` 成为执行护栏正文。
3. 替代 `facts/` 成为稳定事实正文。
4. 替代 `ai_runtime_sop.md` 承载流程型要求。

### 7.5 跨项目标准层与运行时标准层

`standards/` 与 `ai_runtime_standards.md` 的关系固定如下：

- `standards/`：正式跨项目标准层
- `ai_runtime_standards.md`：当前项目运行时生效标准层

其中：

1. `standards/` 承载已经审核通过、具备跨项目复用价值的稳定标准。
2. `ai_runtime_standards.md` 承载当前项目当前必须遵循的标准集合。
3. 当前项目新增标准应先在 `ai_runtime_standards.md` 中生效。
4. 只有当这些标准经过审核、去项目化并验证可跨项目复用后，才进一步升级进入 `standards/`。

### 7.6 `common` 项目的进入顺序

当项目类型已经确定，且 `project_type == common` 时，AI 必须按以下顺序进入正式工作流：

1. 先通过 `AGENTS.md` 完成项目类型判定。
2. 进入 `ai_project_sop.md`，建立主工作流理解。
3. 先读取 `ai_runtime_sop.md` 与 `ai_runtime_standards.md`，建立当前项目运行时补充理解。
4. 以 `ai_project_sop.md` 为主规范，结合运行时补充进入 `project / phase / plan / task` 工作链路。
5. 在真实项目运行过程中，将项目级新增流程与 SOP 待修改项沉淀到 `ai_runtime_sop.md`。
6. 将当前项目新增且必须遵循的标准沉淀到 `ai_runtime_standards.md`。

### 7.7 四者的主从关系

在非 `sop_develop` 项目中，四者关系固定如下：

- `AGENTS.md`：入口门
- `ai_project_sop.md`：主规范
- `ai_runtime_sop.md`：运行时扩展规范
- `ai_runtime_standards.md`：运行时生效标准

其中：

- `AGENTS.md` 决定应进入哪条非 `sop_develop` 正式项目工作流
- `ai_project_sop.md` 决定 AI 应如何按 SOP 执行开发
- `ai_runtime_sop.md` 决定当前项目额外需要遵守哪些运行时补充流程，并记录后续应反馈回主 SOP 的待修订项
- `ai_runtime_standards.md` 决定当前项目实际应遵循哪些运行时补充标准，并记录后续应反馈回正式标准层的新增标准项

### 7.8 运行时规范与标准的升级原则

`ai_runtime_sop.md` 与 `ai_runtime_standards.md` 中沉淀的内容，默认都只对当前项目生效。

只有当这些内容经过重复验证、边界稳定、具备跨项目复用价值时，才应进一步判断是否需要升级。

这意味着：

1. `ai_runtime_sop.md` 可以作为真实项目的流程实验层。
2. `ai_runtime_standards.md` 可以作为真实项目的标准实验层。
3. `ai_project_sop.md` 仍然是正式主规范层。
4. `standards/` 仍然是正式跨项目标准层。
5. 运行期经验应先在项目中验证，再决定是否升级为通用 SOP 或通用标准。

---

## 8. 当前使用顺序

在项目中，建议按以下顺序使用：

1. 先通过 `AGENTS.md` 完成项目入口判定。
2. 再读本文件，建立整体认知。
3. 若当前项目类型为 `common`，先读取 `ai_runtime_sop.md` 与 `ai_runtime_standards.md`。
4. 新项目启动时，进入 `sop/processes/project_bootstrap_sop.md`。
5. 若需要理解层级对象，依次阅读：
   - `sop/core/project_layer.md`
   - `sop/core/phase_layer.md`
   - `sop/core/plan_layer.md`
   - `sop/core/task_layer.md`
6. 若需要理解跨层流转，阅读 `sop/core/workflow_transition_rules.md`。
7. 若需要实际落地阶段审查与交接，阅读：
   - `sop/templates/phase_review_template.md`
   - `sop/templates/next_phase_request_template.md`
8. 若需要细化执行层步骤与任务，阅读：
   - `sop/design/main_plan_state_design.md`
   - `sop/templates/plan_item_template.md`
   - `sop/templates/task_template.md`
9. 若需要事实沉淀、恢复纠偏或 skill 进入条件，再进入对应子 SOP、facts 层与规则层。
10. 若需要理解正式跨项目标准，先进入 `standards/standards_index.md`，再按需进入对应标准文档。

---

## 9. 全局原则

---

后续所有项目都应遵守以下原则：

### 9.1 最小实现优先

优先完成当前阶段明确需要的最小可运行实现，不为未来预埋不必要结构。

### 9.2 单目标推进

无论是 `phase`、`plan item` 还是 `task`，都应尽量保持单一核心目标，避免把多个独立目标塞进一个执行对象中。

### 9.3 先定义验证，再开始执行

在进入实现或执行前，先明确如何判断完成，避免无边界推进。

### 9.4 稳定事实必须回写

凡是已经确认、会持续影响后续判断的结论，不应只留在对话中，必须沉淀到文档。

### 9.5 发现漂移必须纠偏

一旦出现 scope 漂移、过度设计、事实失真或主线失控，不应继续硬做，而应先进入纠偏流程。

### 9.6 文档分层管理

不同类型的信息必须写入对应位置：

- 总原则写入总纲
- 对象定义写入层级定义文档
- 流转规则写入跨层规则文档
- 标准输入输出写入模板文档
- 跨项目正式标准写入 `standards/*`
- 当前项目运行时生效标准写入 `ai_runtime_standards.md`
- 稳定事实写入 facts 文档
- 执行护栏写入 `rules/*`

### 9.7 先约束，再放大

项目的首要目标不是让 AI 一开始做更多事，而是先建立清晰边界、稳定主链、稳定审查和稳定沉淀，再逐步放大自动化能力。

### 9.8 完整设计，但避免过度设计

SOP 和对象模型应覆盖真实治理需求，但不应为了理论完整性而引入低价值层级、稀有状态或平台化复杂度。

---

## 10. 与其他顶层入口的关系

- `AGENTS.md`：负责项目入口判定与工作流分流。
- `ai_project_type.md`：负责定义当前支持的项目类型及其入口差异。
- `ai_runtime_sop.md`：负责承载当前正式项目的流程型运行时补充。
- `ai_runtime_standards.md`：负责承载当前正式项目的标准型运行时补充。

---

## 11. 最终结论

当前新版 AI 项目 SOP 的核心目标是：

> **以 `Project - phase - plan - task` 为主模型，用决策层与执行层分离的方式，建立可治理、可审查、可回流、可沉淀的 AI 项目工作流。**

本文件是当前项目 SOP 的总入口。后续所有项目都应以本文件为总导航，进入对应的层级定义、模板、事实、规则与子 SOP。
