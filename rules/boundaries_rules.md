# 边界规则

- **版本**：v2.0-draft
- **定位**：固定 `project / phase / plan / task` 四层边界要求，防止 AI 在边界不清时扩散执行。

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
3. 若执行中发现边界失真，应转入 `maintenance_recovery_sop.md`。
