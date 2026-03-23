# Task 标注格式

- **版本**：v1.0
- **状态**：正式模板
- **所属层级**：执行层辅助模板
- **定位**：定义执行层中单个 `task` 的标准标注格式。
- **适用范围**：用于统一表达最小可控执行单元的目标、边界、验证、结果、回滚与回主线动作。

---

## 1. 文档目标

本文件用于回答以下问题：

1. `task` 应如何被标准化表达。
2. 如何让单个执行单元具备明确目标、明确结果和可回滚能力。
3. 如何保证 `task` 完成后能稳定回流到所属 `plan`，而不是继续沿局部上下文扩展。

本文件是模板文档，不替代 `task`、`plan` 或 `phase` 的定义文档。

---

## 2. 使用原则

`task` 应遵循以下原则：

1. 面向最小可控执行单元，不面向主线编排。
2. 面向一次闭环，不面向长期演进目标。
3. 必须同时表达目标、边界、完成标准、验证方式和回流动作。
4. 必须支持异常记录、回滚判断和未做事项声明。

---

## 3. 标准标注格式

每个 `task` 至少应包含以下字段：

### 3.1 基础信息

- `task id`：
- `parent plan id`：
- `related plan item id`：
- `task type`：`implementation / analysis / validation / review / recovery`
- `task status`：`draft / ready / in_progress / blocked / review_pending / done / cancelled / rolled_back`

### 3.2 目标与边界

- `task goal`：
- `task non-goals`：
- `task boundary`：
- `why this task exists`：

### 3.3 输入前提

- `required inputs`：
- `entry conditions`：
- `dependencies`：

### 3.4 完成与验证

- `completion criteria`：
- `validation method`：
- `expected outputs`：
- `failure or block conditions`：

### 3.5 当前结果

- `current result summary`：
- `produced outputs`：
- `known issues`：
- `explicitly not done`：
- `why current status is this status`：

### 3.6 回滚与恢复

- `rollback scope`：
- `rollback trigger`：
- `rollback action guidance`：

### 3.7 回主线信息

- `return to plan action`：
- `candidate follow-up tasks`：
- `items explicitly not absorbed here`：

---

## 4. 推荐填写说明

### 4.1 `task goal`

必须只写一个核心目标。

较好示例：

- 验证资源加载路径是否稳定
- 跑通分数更新逻辑

较差示例：

- 跑通分数逻辑并顺手优化 UI
- 处理相关问题

### 4.2 `task non-goals`

用于阻止当前 `task` 自然扩边界。

例如：

- 不处理视觉资源
- 不重构相邻模块
- 不扩展排行榜逻辑

### 4.3 `task boundary`

应用于明确：

- 允许改哪些对象
- 不允许碰哪些对象

### 4.4 `completion criteria`

必须写成可判断标准，不能只写“完成即可”。

### 4.5 `validation method`

应用于明确：

- 用什么方式判断当前 `task` 已完成
- 是运行验证、人工检查、用例确认还是 review

### 4.6 `explicitly not done`

这一项非常关键，用于在 task 收口时防止隐式扩边界。

### 4.7 `return to plan action`

必须说明当前 `task` 完成后如何回到 `main plan` 或 `sub plan`。

这项不能为空。

---

## 5. 模板示例

```md
# Task

- task id: TASK-007
- parent plan id: MP-002
- related plan item id: PI-003
- task type: implementation
- task status: ready

## Goal And Boundary

- task goal: 跑通分数更新逻辑并稳定显示最新得分。
- task non-goals:
  - 不补视觉动画
  - 不扩展排行榜
  - 不重构 UI 架构
- task boundary:
  - 仅处理分数计算结果到基础显示组件的接线
- why this task exists:
  - 当前 `plan item` 需要建立最小分数反馈闭环

## Inputs

- required inputs:
  - 当前得分计算逻辑
  - 基础 UI 容器
- entry conditions:
  - 得分结果已可读取
- dependencies:
  - 核心吃食物流程已稳定

## Completion And Validation

- completion criteria:
  - 玩家得分变化时，界面能稳定显示最新得分
- validation method:
  - 运行最小玩法流程，确认得分变化时展示同步更新
- expected outputs:
  - 可用的分数更新闭环
- failure or block conditions:
  - 若 UI 容器无法承接结果展示，则进入 blocked

## Current Result

- current result summary:
  - 尚未开始执行
- produced outputs:
  - none
- known issues:
  - none
- explicitly not done:
  - 不处理视觉反馈优化
- why current status is this status:
  - 前置条件已满足，可进入执行

## Rollback And Recovery

- rollback scope:
  - 撤销当前 task 新增的分数展示接线
- rollback trigger:
  - 若引入分数显示错误或影响主循环
- rollback action guidance:
  - 回退分数展示接线，保留既有得分计算逻辑

## Return To Plan

- return to plan action:
  - 完成后进入 review_pending，并返回 main plan 决定是否标记当前步骤完成
- candidate follow-up tasks:
  - 验证分数展示在死亡重开后是否重置正确
- items explicitly not absorbed here:
  - 不把排行榜、结算页和视觉动画并入当前 task
```

---

## 6. 何时必须创建或更新

以下情况通常应创建或更新 `task`：

1. 某个 `plan item` 需要被真正执行
2. 当前 `task` 状态发生变化
3. 当前 `task` 被阻塞、取消或回滚
4. 当前 `task` 收口并回主线

以下情况通常不单独创建新的 `task`：

1. 主线中的纯编排判断
2. 仍然只是候选步骤
3. 单个实现过程中的极小内部动作

---

## 7. 使用限制

`task` 不是：

1. `main plan`
2. `plan item`
3. `phase review`
4. 完整复盘文档

它是执行层中的最小可控执行单元。

---

## 8. 当前结论

`task` 的作用可以先按如下方式确定：

- 它是执行层最小的可控执行对象
- 它用于承载单一目标、明确边界、完成标准和验证方式
- 它支持异常记录、未做事项声明、回滚与回主线动作
- 它是“结果明确、支持回滚、强制收口”的核心载体

后续可继续细化：

1. 与 `plan item` 字段的映射
2. 与 `task_layer.md` 的字段映射
3. 与现有 facts / rules 体系的映射方式
