# Facts 索引

- **版本**：v2.0-draft
- **定位**：记录 facts 文档分工、使用顺序与新增 facts 入口的登记规则。

---

## 1. 当前 facts 文档

| 文档 | 作用 |
| --- | --- |
| `docs/facts/project_scope.md` | 记录 `project` 与当前 `phase` 的范围摘要 |
| `docs/facts/facts_index.md` | 维护 facts 文档分工与新增入口规则 |
| `docs/facts/golden_cases.md` | 记录关键验证样例与行为判断标准 |

## 2. 与正式模板的关系

以下模板作为正式入口单独维护，不再由 facts 目录承载：

- `task_template.md`
- `plan_item_template.md`
- `phase_review_template.md`
- `next_phase_request_template.md`

## 3. 新增 facts 文档规则

仅在以下条件同时满足时新增 facts 文档：

1. 某类事实已经稳定并重复出现。
2. 现有文档已不适合继续承载。
3. 新文档具备持续复用价值。

## 4. 登记要求

新增 facts 文档后，必须在本文件中补充：

- 文档路径
- 文档作用
- 适合承载的事实类型
