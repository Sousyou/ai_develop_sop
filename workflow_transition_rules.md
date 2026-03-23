# 四层工作流流转规则

- **版本**：v1.0
- **状态**：正式定义
- **所属层级**：跨层流转规则
- **定位**：定义 `Project - phase - plan - task` 四层工作流之间的主链流转、回流关系与变更传播规则。
- **适用范围**：作为当前新版 SOP 中四层工作流的正式跨层流转骨架。

---

## 1. 文档目标

本文件用于回答以下问题：

1. `project`、`phase`、`plan`、`task` 四层之间如何形成稳定闭环。
2. `project` 修改后如何向下传递，而不直接打穿执行层。
3. 为什么 `phase` 必须唯一，以及唯一 `phase` 如何承接当前执行主线。
4. `task` 完成后应如何回流到 `plan`，避免继续沿局部上下文深入。
5. 执行层的并行应出现在哪一层，不应出现在哪一层。

本文件不替代四层定义文档，而是专门负责跨层流转规则。

---

## 2. 流转总原则

四层工作流遵循以下总原则：

1. 方向自上而下传递：`project -> phase -> plan -> task`
2. 结果自下而上回流：`task -> plan -> phase -> project`
3. 并行只允许发生在执行层，不允许发生在阶段层和目标层。
4. 上层负责定义与裁决，下层负责执行与反馈。
5. 任意层出现变化时，不应跳过中间层直接改写更下层。

---

## 3. 主执行链

标准主执行链如下：

`project -> current phase -> current main plan -> task`

其职责分别为：

- `project`：定义最终目标、长期边界、顶层约束和全局事实。
- `current phase`：定义当前阶段闭环、阶段目标、非目标和交付边界。
- `current main plan`：定义当前阶段下的执行主线、顺序、状态和整合逻辑。
- `task`：完成当前一步的最小可控执行闭环。

要求：

- 任何具体执行都必须能追溯到当前 `main plan`
- 任何 `main plan` 都必须能追溯到当前唯一 `phase`
- 任何 `phase` 都必须能追溯到当前 `project`

---

## 4. 唯一 `phase` 规则

在任一时刻，只允许存在一个当前生效的 `phase`。

### 4.1 规则定义

- `phase` 是唯一阶段主线容器
- 不允许多个 `phase` 并行推进
- 不允许在未关闭旧 `phase` 的情况下正式激活新 `phase`

### 4.2 治理目的

本规则用于确保：

- 当前阶段边界唯一
- 当前执行主线唯一归属
- 所有 `plan` 和 `task` 都能明确挂载到同一个当前阶段

### 4.3 并行限制

并行能力只允许出现在：

- `main plan -> sub plan`
- `plan -> task`

不允许出现在：

- `project` 并行
- `phase` 并行
- 多个 `main plan` 并行作为多个主执行世界

---

## 5. `phase` 生命周期与边界锁规则

为了确保 `phase` 既完整可控，又不过度设计，跨层流转应承认并遵守 `phase` 的生命周期状态。

建议采用以下状态：

- `proposed`
- `ready`
- `active`
- `reviewing`
- `correcting`
- `blocked`
- `completed`
- `transition_pending`

### 5.1 生命周期治理要求

- 只有 `active` 的 `phase` 才能承接正式执行
- `phase` 进入 `active` 后，边界默认锁定
- 边界变更只能经 `reviewing`、`correcting` 或上浮 `project`
- `phase` 完成后必须先进入 `transition_pending`，而不是直接切换到下一 `phase`

### 5.2 scope 漂移控制要求

执行过程中发现的边界外内容：

- 不得直接并入当前 `phase`
- 应记录为候选项
- 由当前 `phase` 在 `reviewing` 或 `correcting` 中决定去向

---

## 6. `project` 修改的单向传递规则

`project` 修改后，不得直接改写 `plan` 或 `task`。

标准传递路径如下：

`project 修改 -> current phase 审阅 -> phase 判断是否调整 -> 如需调整则重新发起 plan`

### 6.1 第一步：确认 `project` 修改

当用户或系统确认以下变化时，可视为 `project` 修改：

- 最终产品目标变化
- 长期边界变化
- 顶层约束变化
- 跨多个 `phase` 生效的全局事实变化

### 6.2 第二步：交给当前 `phase` 审阅

当前唯一 `phase` 必须审阅这次 `project` 修改，判断：

1. 当前阶段目标是否仍然成立
2. 当前阶段边界是否仍然成立
3. 当前阶段输出是否仍然是通往新 `project` 目标的有效路径

### 6.3 第三步：输出 `phase` 审阅结论

`phase` 审阅结论只能是以下两类之一：

1. `phase 无需调整`
2. `phase 需要调整`

### 6.4 第四步：基于 `phase` 结论处置执行层

如果 `phase 无需调整`：

- 当前 `main plan` 可继续执行
- 仅记录本次 `project` 修改对当前 `phase` 无直接影响

如果 `phase 需要调整`：

- 当前 `phase` 必须先对阶段定义、阶段内既有结论和当前执行主线做一致性纠错
- 当前 `phase` 必须更新目标、边界或阶段状态定义
- 当前 `main plan` 必须明确进入以下之一：
  - `continue`
  - `freeze`
  - `cancel`
  - `rebuild`
- 若执行主线已不再适配新的 `phase`，则必须重新发起 `main plan`

---

## 7. `phase` 到 `plan` 的激活规则

`phase` 不是执行层入口，`plan` 才是。

因此：

- 一个 `phase` 在进入执行前，必须有一个当前生效的 `main plan`
- 没有 `main plan` 的 `phase` 只能视为已定义但未进入执行

### 7.1 `main plan` 的唯一性

在任一时刻，一个 `phase` 只能有一个当前生效的 `main plan`。

### 7.2 `main plan` 的创建触发

以下情况应创建或重建 `main plan`：

1. 一个新 `phase` 被激活
2. 当前 `phase` 目标已明确，但尚无执行主线
3. `project` 修改经 `phase` 审阅后判定需要重建执行主线
4. 当前 `main plan` 已失效、完成或被取消

### 7.3 `main plan` 的两种进入方式

当前工作流必须兼容以下两种方式：

1. 当前 `phase` 自发发起 `main plan`
2. 外部直接输入一个候选 `plan`

但无论哪种方式，都必须先经过当前 `phase` 审查。

### 7.4 外部输入 `plan` 的接纳条件

外部直接输入的 `plan` 只有在同时满足以下条件时，才可被接纳为当前 `main plan`：

1. 与当前 `phase` 目标一致
2. 不突破当前 `phase` 边界
3. 可作为当前唯一生效执行主线
4. 不与已存在的生效 `main plan` 冲突

若未通过审查，则：

- 不得直接成为当前 `main plan`
- 应被退回、改写、延后或拒绝

---

## 8. `phase` 对 `main plan` 的治理责任

`phase` 是当前 `main plan` 生命周期的拥有者。

这意味着：

- `phase` 决定何时发起新的 `main plan`
- `phase` 监控并记录每轮 `main plan` 的执行结果
- `phase` 基于执行结果决定是否继续下一轮、重试、重建、暂停或上报问题

每轮 `main plan` 收口后，当前 `phase` 都应执行一次 `Phase Review`，作为阶段治理层的标准动作。

---

## 9. `phase` 完成与下一阶段请求

`phase` 在进入 `completed` 后，必须进入 `transition_pending`，并自动生成 `next_phase_request`。

标准标注格式见：`next_phase_request_template.md`

### 9.1 自动生成要求

`next_phase_request` 至少应包含：

1. 推荐下一个 `phase`
2. 推荐理由
3. 与 `project` 路径的关系
4. 当前阶段输出如何支撑下阶段
5. 当前遗留问题
6. 下阶段进入条件判断

### 9.2 控制要求

- 自动生成请求
- 不自动跳过审查直接激活下一 `phase`
- 由后续确认流程决定下一阶段是否进入 `ready`

---

## 10. `main plan` 与 `sub plan` 的流转位置

`sub plan` 是执行层手段，不是阶段层对象。

因此标准关系如下：

`current main plan -> sub plan -> task`

要求：

- 只有 `main plan` 可以决定是否派生 `sub plan`
- `sub plan` 不得改变 `phase` 边界
- `sub plan` 不得直接响应 `project` 修改
- `sub plan` 完成后必须回到 `main plan`

---

## 11. `task` 的标准回流规则

`task` 完成后，必须回流到所属 `plan`，不得自然延伸为下一个 `task`。

标准回流链如下：

`task -> sub plan / main plan -> current phase（必要时） -> project（必要时）`

### 11.1 `task` 回流的最小内容

每个 `task` 在结束时至少要返回：

- 输出结果
- 明确未做事项
- 异常或阻塞
- 新发现的问题
- 候选后续项

### 11.2 `task` 的回流归属

如果 `task` 属于 `main plan`：

- 直接返回 `main plan`

如果 `task` 属于 `sub plan`：

- 先返回 `sub plan`
- `sub plan` 收口后再返回 `main plan`

---

## 12. `task` 返回后 `main plan` 的标准动作

这是整个工作流中最关键的闭环动作之一。

每个 `task` 返回后，`main plan` 至少必须执行一次明确决策，不能直接沿上下文继续推进。

`main plan` 可执行的标准动作包括：

1. 标记当前 `plan item` 继续推进
2. 标记当前 `plan item` 已完成
3. 标记当前 `plan item` 阻塞
4. 将当前 `plan item` 置为待 review 或待确认
5. 根据回流结果重排顺序
6. 按需派生 `sub plan`
7. 结束、冻结、取消或重建当前 `main plan`

要求：

- `task` 完成不等于自动开始下一个 `task`
- 必须先经过一次 `main plan` 级决策
- 这一步是阻断局部连续深入的主要控制点

---

## 13. `Phase Review` 的标准职责

每轮 `main plan` 收口后，`phase` 必须执行一次 `Phase Review`。

标准标注格式见：`phase_review_template.md`

`Phase Review` 至少要回答以下问题：

1. 当前 `phase` 目标是否更接近完成？
2. 本轮 `main plan` 属于 `completed`、`partially_completed`、`blocked`、`failed` 还是 `cancelled`？
3. 当前阶段定义、边界或既有结论是否需要纠错？
4. 当前阶段是否已经满足退出条件？
5. 是否应发起下一轮 `main plan`？
6. 是否应重试、重建、暂停或上报问题？
7. 是否形成了需要上报或登记的稳定结论？

`Phase Review` 至少应输出以下四类结论：

- `执行结论`
- `阶段结论`
- `下一步结论`
- `沉淀结论`

---

## 14. `phase` 接收执行层回流的条件

不是所有执行层结果都需要上浮到 `phase`。

只有在以下情况出现时，执行结果才应上浮到 `phase`：

1. 当前阶段目标可能无法达成
2. 当前阶段边界需要修改
3. 当前阶段交付定义需要重述
4. 当前 `main plan` 已无法支撑阶段推进

如果问题仍可在 `main plan` 层解决，则不应上浮到 `phase`。

---

## 15. `phase` 的知识审查与上报责任

`phase` 直接管理执行层，因此它应成为知识审查与上报的基础层。

每轮 `Phase Review` 后，`phase` 都应判断是否形成了以下候选沉淀项：

### 15.1 `project` 事实上报

当结果形成跨多个 `phase` 持续有效的稳定事实时，应上报 `project` 层。

### 15.2 `skill candidate`

当某类流程已经重复出现、边界稳定、可验证且可复用时，应登记为 `skill candidate`。

### 15.3 `SOP candidate`

当执行中暴露出稳定的流程缺口、反复出现的治理问题或应被固化的流程改进时，应登记为 `SOP candidate`。

要求：

- `phase` 负责审查和上报建议
- `phase` 不直接等同于正式改写 `project`、正式发布 `skill` 或直接修改正式 `SOP`

---

## 16. `project` 接收回流的条件

不是所有 `phase` 变化都需要上浮到 `project`。

只有在以下情况出现时，才应上浮到 `project`：

1. 最终产品目标需要修改
2. 长期边界需要修改
3. 顶层约束需要修改
4. 出现跨多个 `phase` 持续有效的全局事实

如果问题只影响当前阶段或当前执行主线，则不应上浮到 `project`。

---

## 17. 四层闭环总图

完整闭环可概括为：

### 17.1 主链

`project -> current phase -> current main plan -> task`

### 17.2 执行层并行链

`current main plan -> sub plan -> task`

### 17.3 回流链

`task -> sub plan / main plan -> current phase -> project`

### 17.4 变更传播链

`project 修改 -> current phase 审阅 -> phase 结论 -> main plan 继续 / 冻结 / 取消 / 重建`

### 17.5 阶段交接链

`reviewing -> completed -> transition_pending -> next_phase_request`

---

## 18. 当前工作流下的硬规则

在当前版本中，以下规则建议视为硬规则：

1. 任一时刻只能有一个 `current phase`
2. `project` 修改必须先经过 `phase` 审阅，不能直接打穿到执行层
3. 每个 `task` 返回后，必须先经过一次 `main plan` 决策，不能直接顺势继续
4. `phase` 进入 `active` 后，边界默认锁定
5. `phase` 完成后必须先生成 `next_phase_request`，不能直接跳到下一个 `phase`

---

## 19. 当前结论

这套跨层流转规则可以先按如下方式确定：

- `project` 负责定义方向，`phase` 负责吸收并解释方向变化，`plan` 负责执行主线，`task` 负责最小落地。
- `phase` 必须唯一，并且不允许并行；并行只能存在于执行层。
- `phase` 采用完整但克制的生命周期设计，以支持阶段激活、边界锁定、阶段审查、阶段纠错、阻塞处理、完成交接和下一阶段请求生成。
- `project` 变化采用单向向下传递模式，由当前 `phase` 先审阅、纠错，再决定是否重建 `plan`。
- `phase` 是 `main plan` 生命周期的拥有者，每轮 `main plan` 收口后必须执行一次 `Phase Review`。
- `task` 完成后的回流，必须先由 `main plan` 做一次显式主线决策，才能进入下一步。
- `phase` 是知识审查与上报的基础层，负责判断是否需要上报 `project` 事实、登记 `skill candidate` 或 `SOP candidate`。

本版本先作为讨论基线，后续可继续细化：

1. `main plan` 与 `plan item` 的状态机
2. `Phase Review` 与 `next_phase_request` 的字段映射
3. `sub plan` 的最小记录模板
4. 四层工作流与现有 SOP 文档体系的映射方式
