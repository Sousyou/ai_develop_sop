# 边界规则

- **版本**：v2.0
- **状态**：正式规则
- **定位**：固定 `project / phase / plan / task` 四层边界要求，防止 AI 在边界不清时扩散执行。
- **适用范围**：适用于所有基于 `project / phase / plan / task` 模型的边界识别与边界锁定判断。

---

## 1. 边界层级

项目中默认存在四层边界：

1. `project` 边界
2. `phase` 边界
3. `plan` 边界
4. `task` 边界

## 2. `project` 边界

- 由项目目标、长期范围和长期不做事项共同定义。
- 变化时必须先经过当前 `phase` 审阅。

## 3. `phase` 边界

- 每个 `phase` 必须有明确目标、非目标与交付边界。
- `phase` 进入 `active` 后，边界默认锁定。

## 4. `plan` 边界

- `main plan` 只能在当前 `phase` 授权范围内编排执行。
- `sub plan` 只能处理被授权的局部问题，不得扩边界。

## 5. `task` 边界

- 每个 `task` 只承载一个核心目标。
- 必须显式定义 in-scope 与 out-of-scope。
- 新发现问题默认不自动并入当前 `task`。

## 6. 硬规则

1. 不得在边界未明确时展开大规模实现。
2. 不得用“顺手一起做掉”代替边界判断。
3. 若执行中发现边界失真，应转入 `sop/processes/maintenance_recovery_sop.md`。

---

## 7. 与其他文档的关系

- scope 控制细则见 `rules/scope_control_rules.md`。
- `phase` 与 `plan` 的边界定义见 `sop/core/phase_layer.md` 与 `sop/core/plan_layer.md`。
- 边界失真后的处理见 `sop/processes/maintenance_recovery_sop.md`。

---

## 8. 当前结论

默认情况下，边界应先被识别和锁定，再允许进入执行；一旦边界失真，应优先纠偏而不是继续推进。
