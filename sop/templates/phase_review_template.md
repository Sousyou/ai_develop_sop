# Phase Review 标注格式

- **版本**：v1.0
- **状态**：正式模板
- **所属层级**：决策层辅助模板
- **定位**：定义每轮 `main plan` 收口后，当前 `phase` 执行 `Phase Review` 时的标准标注格式。
- **适用范围**：用于统一表达阶段审查结果、下一步决策和沉淀建议。

---

## 1. 文档目标

本文件用于回答以下问题：

1. `Phase Review` 应如何标准化表达。
2. 如何把一轮 `main plan` 的结果转化为阶段结论和下一步动作。
3. 如何在阶段审查时同步处理纠错、沉淀和上报判断。

本文件是模板文档，不直接替代 `phase`、`plan` 或 `task` 的定义文档。

---

## 2. 使用原则

`Phase Review` 应遵循以下原则：

1. 面向阶段判断，不面向实现流水账。
2. 面向当前 `phase`，不直接越权改写 `project`。
3. 一次 review 必须输出明确结论，不能只保留开放讨论。
4. 必须同时覆盖执行结果、阶段状态、下一步和沉淀建议。

---

## 3. 标准标注格式

每个 `Phase Review` 至少应包含以下字段：

### 3.1 基础信息

- `review id`：
- `phase id`：
- `phase name`：
- `source main plan id`：
- `review status`：`draft / completed / confirmed`
- `reviewed at`：

### 3.2 本轮执行结论

- `execution result type`：`completed / partially_completed / blocked / failed / cancelled`
- `what was completed`：
- `what was not completed`：
- `key evidence or outputs`：
- `blocking issues`：

### 3.3 阶段判断

- `phase goal progress`：
- `phase boundary still valid`：`yes / no / partially`
- `phase definition needs correction`：`yes / no`
- `phase exit condition status`：`met / partially_met / unmet`
- `should phase continue`：`yes / no`

### 3.4 下一步决策

- `next decision type`：`continue phase / correct phase / launch main plan / retry current path / rebuild main plan / pause phase / exit phase / raise to project / register candidate`
- `why this decision`：
- `suggested next action`：
- `whether user decision is required`：`yes / no`

### 3.5 纠错结论

- `phase corrections needed`：
- `plan corrections needed`：
- `stale assumptions or conclusions`：

### 3.6 沉淀与上报结论

- `project fact candidates`：
- `skill candidates`：
- `SOP candidates`：
- `whether project escalation is needed`：`yes / no`

### 3.7 交接信息

- `carry-forward issues`：
- `items explicitly not carried forward`：
- `notes for next main plan or next phase`：

---

## 4. 推荐填写说明

### 4.1 `execution result type`

建议只使用以下五种值：

- `completed`
- `partially_completed`
- `blocked`
- `failed`
- `cancelled`

避免自定义新的结果状态。

### 4.2 `phase boundary still valid`

用于判断当前阶段是否已经出现边界失真。

如果是 `no` 或 `partially`，通常应进入：

- `correct phase`
- `rebuild main plan`
- `raise to project`

其中之一。

### 4.3 `next decision type`

这一项必须是本次 `Phase Review` 的核心输出。  
不能只写“待观察”或“继续看看”。

### 4.4 `items explicitly not carried forward`

用于明确：

- 哪些问题不能默认带入下一轮继续拖延
- 哪些临时妥协必须重新确认

这对控制阶段内 scope 漂移很重要。

---

## 5. 模板示例

```md
# Phase Review

- review id: PR-003
- phase id: PHASE-002
- phase name: 跑通最小 MVP
- source main plan id: MP-002
- review status: completed
- reviewed at: 2026-03-23

## Execution Result

- execution result type: completed
- what was completed:
  - 核心移动逻辑已稳定
  - 死亡与重开流程已跑通
- what was not completed:
  - 未补充正式视觉资源
- key evidence or outputs:
  - MVP 核心可玩闭环可稳定运行
- blocking issues:
  - 无阻塞性问题

## Phase Judgment

- phase goal progress: 当前阶段目标已基本达成。
- phase boundary still valid: yes
- phase definition needs correction: no
- phase exit condition status: met
- should phase continue: no

## Next Decision

- next decision type: exit phase
- why this decision: 当前阶段目标是跑通最小 MVP，该目标已达到，继续补体验会越过阶段边界。
- suggested next action: 进入 `transition_pending` 并生成下一阶段请求。
- whether user decision is required: no

## Corrections

- phase corrections needed: none
- plan corrections needed: none
- stale assumptions or conclusions: none

## Candidate Writeback

- project fact candidates:
  - 最小可玩闭环已跑通
- skill candidates:
  - MVP 核心闭环验证流程
- SOP candidates:
  - Phase Review 输出格式
- whether project escalation is needed: no

## Handover Notes

- carry-forward issues:
  - 当前 UI 仍是原型级表现
- items explicitly not carried forward:
  - 不将视觉资源缺失误记为当前 phase 未完成
- notes for next main plan or next phase:
  - 下一阶段建议聚焦基础体验建设，而不是扩展新玩法
```

---

## 6. 何时必须生成

以下情况应生成 `Phase Review`：

1. 当前 `main plan` 收口
2. 当前 `phase` 需要决定是否继续下一轮执行
3. 当前 `phase` 需要决定是否纠错、退出、暂停或上报问题

以下情况通常不单独生成：

1. 单个 `task` 刚完成，但 `main plan` 尚未收口
2. 普通执行日志更新

---

## 7. 使用限制

`Phase Review` 不是：

1. 单个 `task` 的复盘报告
2. 当前 `main plan` 的完整执行日志
3. `project` 层正式改写文档
4. 下一阶段请求本身

它是当前阶段控制器对一轮执行结果做出的标准化阶段判断。

---

## 8. 当前结论

`Phase Review` 的作用可以先按如下方式确定：

- 它是 `phase` 的标准审查动作
- 它用于把 `main plan` 的结果转化为阶段判断和下一步决策
- 它同步承担纠错判断、沉淀建议和上报判断
- 它是 `phase` 生命周期从执行走向继续、纠错、阻塞或退出的核心枢纽

后续若需演进，应在不破坏当前字段集合与阶段审查职责边界的前提下继续细化。
