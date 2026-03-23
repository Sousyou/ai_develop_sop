# Main Plan 与 Plan Item 状态设计

- **版本**：v1.0
- **状态**：正式辅助设计
- **所属层级**：执行层辅助设计
- **定位**：定义执行层中 `main plan` 与 `plan item` 的状态模型、最小字段、流转规则与恢复语义。
- **适用范围**：用于细化执行层，使其满足“步骤明确、结果明确、支持回滚”的目标。

---

## 1. 文档目标

本文件用于回答以下问题：

1. `main plan` 应使用什么状态模型，才能稳定承接执行主线。
2. `plan item` 应使用什么状态模型，才能把步骤管理清楚。
3. 执行层如何支持 review、阻塞、冻结、取消、回滚与重建。
4. 如何在设计完整的前提下避免把执行层做成过度复杂的流程引擎。

---

## 2. 设计原则

`main plan` 与 `plan item` 的状态设计应遵循以下原则：

1. 完整但克制：覆盖真实执行场景，但不引入低价值状态。
2. 主线优先：`main plan` 必须始终是当前阶段唯一执行主线。
3. 步骤清晰：每个 `plan item` 都要能表示当前是否可做、在做、已做、卡住或撤回。
4. 结果明确：执行后必须有可确认的状态变化。
5. 支持恢复：必须支持冻结、取消、回滚、重试和重建。

---

## 3. `main plan` 的定位

`main plan` 是当前 `phase` 下唯一生效的执行主线控制器。

它不是普通任务列表，而是负责：

- 维护主线顺序
- 推进当前步骤
- 接收执行回流
- 组织 review
- 在路径失效时进入冻结、取消或重建

---

## 4. `main plan` 的状态模型

建议 `main plan` 使用以下状态：

1. `draft`
2. `ready`
3. `active`
4. `reviewing`
5. `blocked`
6. `frozen`
7. `completed`
8. `cancelled`

### 4.1 `draft`

表示：

- 主线已被识别或输入
- 但步骤、边界或完成判据尚未准备好

### 4.2 `ready`

表示：

- 当前主线结构已准备完成
- 已与当前 `phase` 对齐
- 可以正式进入执行

### 4.3 `active`

表示：

- 当前 `main plan` 正在作为唯一执行主线运行
- 当前 `task` 和 `sub plan` 都从这里派生或回流

### 4.4 `reviewing`

表示：

- 当前一个 `plan item` 或一轮关键执行已收口
- `main plan` 正在做主线决策

### 4.5 `blocked`

表示：

- 当前主线暂时无法继续推进
- 原因可能是依赖缺失、路径不明、证据不足或结果冲突

### 4.6 `frozen`

表示：

- 当前主线被正式暂停
- 但尚未被废弃
- 等待 `phase` 纠错、用户决策或上层判断

### 4.7 `completed`

表示：

- 当前 `main plan` 的目标已完成
- 主线已自然收口

### 4.8 `cancelled`

表示：

- 当前主线被正式废弃
- 不再继续推进

---

## 5. `main plan` 的标准流转

### 5.1 主链

`draft -> ready -> active -> reviewing`

### 5.2 继续推进

`reviewing -> active`

适用于：

- 当前主线仍成立
- 下一步明确

### 5.3 阻塞

`active -> blocked`

`reviewing -> blocked`

### 5.4 冻结

`active -> frozen`

`reviewing -> frozen`

`blocked -> frozen`

### 5.5 恢复

`blocked -> active`

`frozen -> active`

### 5.6 完成

`reviewing -> completed`

### 5.7 取消

`draft / ready / active / reviewing / blocked / frozen -> cancelled`

---

## 6. `main plan` 的最小字段

每个 `main plan` 至少应具备以下字段：

1. `plan id`
2. `所属 phase`
3. `plan 名称`
4. `plan 来源`
5. `plan 目标`
6. `plan 非目标`
7. `plan 边界`
8. `当前状态`
9. `状态变更历史`
10. `plan items`
11. `当前 active item`
12. `完成判据`
13. `失败 / 阻塞判据`
14. `review 记录`
15. `回滚 / 重建记录`
16. `sub plan 派生记录`
17. `结果摘要`

其中：

- `plan 来源` 建议使用：`phase_generated / direct_input / rebuilt`

---

## 7. `plan item` 的定位

`plan item` 是 `main plan` 中的可推进步骤。

正式标注格式见：`plan_item_template.md`

它的作用不是承载完整执行细节，而是明确：

- 当前步骤是什么
- 当前步骤是否可做
- 当前步骤何时完成
- 当前步骤何时需要 review、阻塞、延后或回滚

---

## 8. `plan item` 的状态模型

建议 `plan item` 使用以下状态：

1. `planned`
2. `ready`
3. `active`
4. `review_pending`
5. `done`
6. `blocked`
7. `deferred`
8. `rolled_back`
9. `cancelled`

### 8.1 `planned`

已登记在主线中，但尚未到执行时机。

### 8.2 `ready`

依赖已满足，可以开始执行。

### 8.3 `active`

当前步骤正在执行。

### 8.4 `review_pending`

执行已完成，等待主线 review 确认。

### 8.5 `done`

当前步骤已正式完成。

### 8.6 `blocked`

当前步骤被卡住，无法继续。

### 8.7 `deferred`

当前不做，延后处理。

### 8.8 `rolled_back`

当前步骤结果已被撤销。

### 8.9 `cancelled`

当前步骤已被取消，不再继续。

---

## 9. `plan item` 的最小字段

每个 `plan item` 至少应具备以下字段：

1. `item id`
2. `item 名称`
3. `item 目标`
4. `item 非目标`
5. `顺序位置`
6. `依赖项`
7. `当前状态`
8. `完成标准`
9. `输出结果`
10. `失败 / 阻塞原因`
11. `是否允许派生 sub plan`
12. `回滚说明`

---

## 10. 执行层的恢复语义

为满足“支持回滚”的要求，执行层至少支持以下三类恢复动作：

### 10.1 `task` 级回滚

用于撤销单个执行单元的结果。

### 10.2 `plan item` 级回滚

用于撤销某一步骤已确认但后来证明不成立的结果。

典型结果：

- `plan item -> rolled_back`
- 主线回到 `reviewing`

### 10.3 `main plan` 级恢复

用于处理整条路径失效的情况。

典型动作：

- `freeze main plan`
- `cancel main plan`
- `rebuild main plan`

---

## 11. `main plan` 的标准决策动作

每次 `task` 或 `sub plan` 返回后，`main plan` 建议只做以下标准动作：

1. `continue item`
2. `complete item`
3. `block item`
4. `defer item`
5. `rollback item`
6. `spawn sub plan`
7. `reorder items`
8. `freeze main plan`
9. `complete main plan`
10. `cancel main plan`

这组动作的目标，是让执行层判断类型有限而清晰。

---

## 12. 设计边界

这份状态设计是执行层辅助设计，不等于：

1. 现在就必须把所有状态都工程化实现
2. 所有项目都必须机械使用全部状态
3. 执行层要升级成复杂流程引擎

它的作用是先把完整语义定住，再按实际需要决定落地粒度。

---

## 13. 当前结论

执行层状态设计可以先按如下方式确定：

- `main plan` 使用 `draft / ready / active / reviewing / blocked / frozen / completed / cancelled`
- `plan item` 使用 `planned / ready / active / review_pending / done / blocked / deferred / rolled_back / cancelled`
- 执行层同时支持 `task` 级、`plan item` 级和 `main plan` 级恢复动作
- 通过有限的标准决策动作，保证步骤明确、结果明确、恢复路径明确

后续可继续细化：

1. 与 `plan_layer.md` 的正式映射
2. 与 `task` 回滚语义的字段映射
3. 与 `task_template.md` 的字段映射
4. 与现有 facts / rules 体系的映射方式
