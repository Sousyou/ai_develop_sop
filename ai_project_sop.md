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

当前正式入口：`project_layer.md`

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

当前正式入口：`phase_layer.md`

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

当前正式入口：`plan_layer.md`

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

当前正式入口：`task_layer.md`

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

当前正式入口：`workflow_transition_rules.md`

---

## 5. 生命周期视角

虽然整体仍然保留“初始化、执行、回写、纠偏、沉淀”的治理需求，但这些内容不再以旧版线性任务视角为主，而是映射到四层模型中：

### 5.1 项目初始化

目标：

- 明确 `project`
- 明确当前 `phase`
- 建立最小治理骨架
- 建立后续 `plan` 与 `task` 的入口

当前入口：`project_bootstrap_sop.md`

### 5.2 阶段执行

目标：

- 由 `phase` 发起或接纳 `main plan`
- 由 `plan` 驱动执行主线
- 由 `task` 完成最小执行闭环

当前入口：

- `phase_layer.md`
- `plan_layer.md`
- `task_layer.md`

### 5.3 审查与交接

目标：

- 每轮 `main plan` 收口后执行 `Phase Review`
- `phase` 判断是否继续、纠错、暂停、退出或上报问题
- 阶段完成后生成 `next_phase_request`

当前模板入口：

- `phase_review_template.md`
- `next_phase_request_template.md`

### 5.4 事实回写

目标：

- 将稳定事实按层级与类型回写到合适文档
- 不把过程噪音误写成长期事实

当前入口：`fact_writeback_sop.md`

### 5.5 维护与纠偏

目标：

- 处理 scope 漂移
- 处理过度设计
- 处理 facts 与实现失真
- 处理执行主线失效

当前入口：`maintenance_recovery_sop.md`

### 5.6 技能沉淀

目标：

- 将重复、稳定、可验证的流程沉淀为 skill
- 由 `phase` 负责候选判断，由 skill 层负责正式登记与模板化

当前入口：

- `skill_policy.md`
- `skill_registry.md`
- `skill_template.md`

---

## 6. 文档体系

当前新版 SOP 文档体系建议划分为以下几层。

### 6.1 总纲层

- `ai_project_sop.md`

### 6.2 核心定义层

- `project_layer.md`
- `phase_layer.md`
- `plan_layer.md`
- `task_layer.md`
- `workflow_transition_rules.md`

### 6.3 模板层

- `phase_review_template.md`
- `next_phase_request_template.md`
- `plan_item_template.md`
- `task_template.md`

### 6.4 执行层辅助设计

- `main_plan_state_design.md`

### 6.5 流程型子 SOP

- `project_bootstrap_sop.md`
- `project_init_artifacts.md`
- `fact_writeback_sop.md`
- `maintenance_recovery_sop.md`

### 6.6 规则层

- `rules/*`

### 6.7 facts 层

- `docs/facts/*`

### 6.8 skill 层

- `skill_policy.md`
- `skill_registry.md`
- `skill_template.md`

---

## 7. 当前使用顺序

在项目中，建议按以下顺序使用：

1. 先读本文件，建立整体认知。
2. 新项目启动时，进入 `project_bootstrap_sop.md`。
3. 若需要理解层级对象，依次阅读：
   - `project_layer.md`
   - `phase_layer.md`
   - `plan_layer.md`
   - `task_layer.md`
4. 若需要理解跨层流转，阅读 `workflow_transition_rules.md`。
5. 若需要实际落地阶段审查与交接，阅读：
   - `phase_review_template.md`
   - `next_phase_request_template.md`
6. 若需要细化执行层步骤与任务，阅读：
   - `main_plan_state_design.md`
   - `plan_item_template.md`
   - `task_template.md`
7. 若需要事实沉淀、恢复纠偏或 skill 进入条件，再进入对应子 SOP、facts 层与规则层。

---

## 8. 全局原则

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
- 稳定事实写入 facts 文档
- 执行护栏写入 `rules/*`

### 9.7 先约束，再放大

项目的首要目标不是让 AI 一开始做更多事，而是先建立清晰边界、稳定主链、稳定审查和稳定沉淀，再逐步放大自动化能力。

### 9.8 完整设计，但避免过度设计

SOP 和对象模型应覆盖真实治理需求，但不应为了理论完整性而引入低价值层级、稀有状态或平台化复杂度。

---

## 9. 最终结论

当前新版 AI 项目 SOP 的核心目标是：

> **以 `Project - phase - plan - task` 为主模型，用决策层与执行层分离的方式，建立可治理、可审查、可回流、可沉淀的 AI 项目工作流。**

本文件是当前项目 SOP 的总入口。后续所有项目都应以本文件为总导航，进入对应的层级定义、模板、事实、规则与子 SOP。
