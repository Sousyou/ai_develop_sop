# Next Phase Request 标注格式

- **版本**：v1.0
- **状态**：正式模板
- **所属层级**：决策层辅助模板
- **定位**：定义当前 `phase` 完成后，用于生成下一阶段请求的标准标注格式。
- **适用范围**：用于 `phase` 进入 `transition_pending` 后，统一产出 `next_phase_request`。

---

## 1. 文档目标

本文件用于回答以下问题：

1. 当前 `phase` 完成后，下一阶段请求应如何标准化表达。
2. 如何让下一阶段请求既能承接 `project` 路径，又不直接跳过审查自动激活。
3. 如何在交接时明确阶段成果、遗留问题、进入条件与风险。

本文件是模板文档，不直接替代 `phase`、`plan` 或 `task` 的定义文档。

---

## 2. 使用原则

`next_phase_request` 应遵循以下原则：

1. 面向交接，不面向实现细节。
2. 面向下一阶段，不回写当前执行流水账。
3. 面向判断输入，不直接等于下一 `phase` 已激活。
4. 既要说明为什么进入下一阶段，也要说明为什么现在可以进入。

---

## 3. 标准标注格式

每个 `next_phase_request` 至少应包含以下字段：

### 3.1 基础信息

- `request id`：
- `source phase id`：
- `source phase name`：
- `request status`：`draft / proposed / reviewed / accepted / rejected`
- `created at`：

### 3.2 推荐下一阶段

- `recommended next phase name`：
- `recommended next phase goal`：
- `recommended next phase type`：
- `why this is the next phase`：

### 3.3 与 `project` 的对应关系

- `project path reference`：
- `how this next phase advances project`：
- `why it should happen before other candidate phases`：

### 3.4 当前阶段交接摘要

- `what current phase completed`：
- `what current phase did not complete`：
- `key outputs for next phase`：
- `phase exit condition result`：

### 3.5 下一阶段进入条件

- `entry conditions`：
- `entry conditions status`：`met / partially_met / unmet`
- `missing prerequisites`：

### 3.6 风险与遗留问题

- `open risks`：
- `known blockers`：
- `carry-over issues`：
- `items that must not be silently inherited`：

### 3.7 建议的启动方式

- `suggested first decision`：
- `suggested first review focus`：
- `suggested first main plan direction`：
- `whether project review is needed first`：`yes / no`

### 3.8 沉淀与上报信息

- `project fact candidates`：
- `skill candidates`：
- `SOP candidates`：

---

## 4. 推荐填写说明

### 4.1 `recommended next phase name`

应写成阶段结果，而不是动作清单。

较好示例：

- 建立基础视觉体验
- 进入产品化准备阶段

较差示例：

- 继续做功能
- 补点东西

### 4.2 `recommended next phase goal`

应用一句话说明下一阶段结束后，项目会进入什么新状态。

### 4.3 `project path reference`

应用于说明该阶段在整体 `project` 路径中的位置，例如：

- 位于 MVP 完成后的基础体验增强阶段
- 位于差异化玩法之前的产品化准备阶段

### 4.4 `phase exit condition result`

应明确写出当前阶段退出条件是：

- 已满足
- 部分满足
- 有条件满足

避免只写“差不多完成”。

### 4.5 `entry conditions status`

建议只使用以下三种值：

- `met`
- `partially_met`
- `unmet`

避免自由发挥状态名。

### 4.6 `items that must not be silently inherited`

用于明确：

- 哪些遗留问题不能被默认带入下一阶段继续拖延
- 哪些临时妥协必须在下阶段启动前重新确认

这一项对防止阶段切换时的问题隐藏很重要。

---

## 5. 模板示例

```md
# Next Phase Request

- request id: NPR-001
- source phase id: PHASE-002
- source phase name: 跑通最小 MVP
- request status: proposed
- created at: 2026-03-23

## Recommended Next Phase

- recommended next phase name: 建立基础视觉体验
- recommended next phase goal: 让产品从功能原型进入基础可体验状态。
- recommended next phase type: experience-enhancement
- why this is the next phase: 核心玩法已跑通，当前主要缺口已从玩法可行性转向体验可用性。

## Project Alignment

- project path reference: 位于 MVP 完成后、差异化玩法扩展前。
- how this next phase advances project: 为后续玩法扩展和产品化提供稳定体验基线。
- why it should happen before other candidate phases: 若继续扩玩法而不补体验，后续验证成本会升高。

## Source Phase Handover

- what current phase completed:
  - 已完成核心移动与碰撞逻辑
  - 已完成死亡与重开流程
- what current phase did not complete:
  - 未补充正式视觉资源
  - 未处理新手提示体验
- key outputs for next phase:
  - 已稳定的最小可玩版本
  - 已确认的核心交互流程
- phase exit condition result: met

## Entry Conditions

- entry conditions:
  - 核心玩法已稳定
  - 当前主循环无阻塞性 bug
- entry conditions status: met
- missing prerequisites: none

## Risks And Carry-over

- open risks:
  - 当前 UI 架构较原型化
- known blockers:
  - 无
- carry-over issues:
  - 分数反馈表现较弱
- items that must not be silently inherited:
  - 不得把“临时原型资源”直接视为长期可接受方案

## Suggested Start

- suggested first decision: 先确认基础视觉体验的边界，不把差异化玩法并入当前阶段。
- suggested first review focus: 核心体验缺口和最低资源替换范围。
- suggested first main plan direction: 先补核心视觉反馈，再补基础状态提示。
- whether project review is needed first: no

## Candidate Writeback

- project fact candidates:
  - 核心玩法最小闭环已稳定跑通
- skill candidates:
  - MVP 核心玩法闭环验证流程
- SOP candidates:
  - phase 完成后生成 next_phase_request 的交接规则
```

---

## 6. 何时必须生成

以下情况应生成 `next_phase_request`：

1. 当前 `phase` 已进入 `completed`
2. 当前 `phase` 已进入 `transition_pending`

以下情况通常不生成：

1. 当前 `phase` 仍在 `active`
2. 当前 `phase` 只是一次普通 `Phase Review`
3. 当前问题仍属于当前 `phase` 内部纠错

---

## 7. 使用限制

`next_phase_request` 不是：

1. 下一阶段的正式激活命令
2. 下一阶段的完整执行计划
3. 当前阶段的详细复盘报告
4. `project` 层正式改写文档

它只是阶段交接和下一阶段提议的标准化输入。

---

## 8. 当前结论

`next_phase_request` 的作用可以先按如下方式确定：

- 它是 `phase` 完成后的标准交接对象
- 它用于把当前阶段结果转化为下一个阶段的候选输入
- 它强调项目路径对齐、进入条件、遗留问题和启动建议
- 它支持自动生成，但不等于自动激活下一 `phase`

后续若需演进，应在不破坏“交接对象而非激活命令”的职责边界前提下继续细化。
