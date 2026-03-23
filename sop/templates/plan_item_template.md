# Plan Item 标注格式

- **版本**：v1.0
- **状态**：正式模板
- **所属层级**：执行层辅助模板
- **定位**：定义 `main plan` 中单个 `plan item` 的标准标注格式。
- **适用范围**：用于统一表达执行步骤、依赖、状态、完成标准、结果与回滚信息。

---

## 1. 文档目标

本文件用于回答以下问题：

1. `plan item` 应如何被标准化表达。
2. 如何让执行层中的“步骤”真正做到明确、可推进、可审查。
3. 如何在单个步骤层面支持结果判断、阻塞处理与回滚语义。

本文件是模板文档，不替代 `plan`、`task` 或 `phase` 的定义文档。

---

## 2. 使用原则

`plan item` 应遵循以下原则：

1. 面向步骤，而不是面向完整执行日志。
2. 面向主线推进，而不是替代 `task` 的实现细节。
3. 必须同时表达目标、边界、依赖、状态和完成标准。
4. 必须能支持 review、阻塞、延后、取消与回滚。

---

## 3. 标准标注格式

每个 `plan item` 至少应包含以下字段：

### 3.1 基础信息

- `item id`：
- `parent main plan id`：
- `item name`：
- `item type`：`implementation / analysis / validation / review / recovery / integration`
- `item status`：`planned / ready / active / review_pending / done / blocked / deferred / rolled_back / cancelled`
- `sequence order`：

### 3.2 目标与边界

- `item goal`：
- `item non-goals`：
- `item boundary`：
- `why this item exists`：

### 3.3 依赖与输入

- `dependencies`：
- `required inputs`：
- `entry conditions`：
- `whether sub plan is allowed`：`yes / no`

### 3.4 完成与判定

- `completion criteria`：
- `review criteria`：
- `expected outputs`：
- `failure or block conditions`：

### 3.5 当前执行结果

- `current result summary`：
- `produced outputs`：
- `known issues`：
- `why current status is this status`：

### 3.6 恢复与回滚

- `rollback scope`：
- `rollback trigger`：
- `rollback action guidance`：
- `defer or cancel conditions`：

### 3.7 交接信息

- `return to main plan action`：
- `candidate follow-up items`：
- `items explicitly not absorbed here`：

---

## 4. 推荐填写说明

### 4.1 `item name`

应写成“当前步骤的结果性表述”或“当前步骤的明确动作表述”，避免模糊标题。

较好示例：

- 跑通分数显示闭环
- 验证资源加载路径是否稳定
- 整合候选方案并输出选择结论

较差示例：

- 做一下优化
- 继续推进
- 处理一些问题

### 4.2 `item type`

建议只使用以下类型：

- `implementation`
- `analysis`
- `validation`
- `review`
- `recovery`
- `integration`

避免随意扩展类型名。

### 4.3 `item non-goals`

这一项非常关键，用于防止单个步骤自然扩边界。

例如：

- 不在本步骤中补 UI 美化
- 不在本步骤中重构相邻模块
- 不在本步骤中扩展新玩法

### 4.4 `completion criteria`

必须写成可以判断的标准，而不是“差不多完成”。

### 4.5 `review criteria`

用于说明主线 review 时到底看什么，不要求写实现细节，但必须写判断点。

### 4.6 `rollback scope`

用于明确当前步骤出错时，允许撤销到什么范围。

它不是 git 命令，而是执行语义边界。

### 4.7 `items explicitly not absorbed here`

用于明确：

- 哪些相关问题即使被发现，也不自动并入当前步骤
- 哪些新问题应回到 `main plan` 决定

这是防止步骤失控的重要字段。

---

## 5. 模板示例

```md
# Plan Item

- item id: PI-003
- parent main plan id: MP-002
- item name: 跑通分数显示闭环
- item type: implementation
- item status: ready
- sequence order: 3

## Goal And Boundary

- item goal: 在最小玩法闭环中补充分数显示，使玩家能看到即时得分反馈。
- item non-goals:
  - 不补正式视觉资源
  - 不扩展排行榜
  - 不重构 UI 框架
- item boundary:
  - 仅处理当前分数显示逻辑与基础展示位置
- why this item exists:
  - 分数反馈是 MVP 可玩体验中的必要可感知结果

## Dependencies And Inputs

- dependencies:
  - 核心吃食物逻辑已稳定
- required inputs:
  - 当前得分计算逻辑
  - 可用的基础 UI 容器
- entry conditions:
  - 得分计算结果可被正常读取
- whether sub plan is allowed: no

## Completion And Review

- completion criteria:
  - 玩家得分变化时能稳定看到分数更新
- review criteria:
  - 分数更新逻辑正确
  - 不影响主循环表现
- expected outputs:
  - 可用的分数显示闭环
- failure or block conditions:
  - 若当前 UI 容器无法承接展示，则进入 blocked

## Current Result

- current result summary:
  - 尚未开始执行
- produced outputs:
  - none
- known issues:
  - none
- why current status is this status:
  - 前置条件已满足，可以进入执行

## Rollback And Recovery

- rollback scope:
  - 撤销本步骤新增的分数显示逻辑与展示接线
- rollback trigger:
  - 若分数显示引入主循环异常或结果不正确
- rollback action guidance:
  - 回退当前分数显示接线，保留既有得分计算逻辑
- defer or cancel conditions:
  - 若当前阶段被纠错到不再要求体验反馈，可 defer 或 cancel

## Handover

- return to main plan action:
  - 执行完成后进入 review_pending，等待 main plan 决定是否标记 done
- candidate follow-up items:
  - 补充分数变化的基础视觉反馈
- items explicitly not absorbed here:
  - 不把排行榜、结算页、音效提示并入当前步骤
```

---

## 6. 何时必须创建或更新

以下情况通常应创建或更新 `plan item`：

1. `main plan` 被正式准备或重建
2. 当前主线需要新增一个明确步骤
3. 某个步骤状态发生变化
4. 某个步骤被阻塞、延后、取消或回滚

以下情况通常不单独创建新的 `plan item`：

1. 只是单个 `task` 内部的小动作
2. 只是一条实现备注
3. 只是 review 中发现的微小修辞调整

---

## 7. 使用限制

`plan item` 不是：

1. 完整的 `task` 执行记录
2. `main plan` 本身
3. `phase` 定义文档
4. 直接等同于 `sub plan`

它是主线中的一个可推进步骤对象。

---

## 8. 当前结论

`plan item` 的作用可以先按如下方式确定：

- 它是 `main plan` 中的标准步骤单元
- 它用于承载步骤目标、边界、依赖、状态和完成标准
- 它支持结果记录、阻塞处理、延后、取消与回滚
- 它是“步骤明确、结果明确、支持回滚”在执行层的核心载体

后续若需演进，应在不破坏“步骤对象而非执行流水”的职责边界前提下继续细化。
