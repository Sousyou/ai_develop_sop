# Naming Conventions Standard

- **版本**：v1.0
- **状态**：正式标准
- **定位**：定义跨项目通用的命名规范基线。
- **适用范围**：所有采用本 SOP 的项目；若项目存在更严格要求，可在 `ai_runtime_standards.md` 中补充，但不得放宽本基线。

---

## 1. 标准目标

本标准用于统一以下内容：

1. 文件命名
2. 目录命名
3. 文档命名
4. 层级对象命名

---

## 2. 总体原则

### 2.1 优先语义清晰

命名的第一原则是可读、可判断、可区分，不为简短而牺牲语义。

### 2.2 优先同层一致

同一目录、同一类型对象、同一套模板内，命名风格必须保持一致。

### 2.3 优先稳定

一旦某类对象的命名模式已经进入稳定使用，不应频繁改名。

### 2.4 避免无信息缩写

除非是行业或项目内稳定共识缩写，否则不应使用仅靠上下文猜测的缩写。

---

## 3. 文件与目录命名

### 3.1 默认格式

文件与目录默认使用：

- 小写英文
- 单词之间使用下划线 `_`

例如：

- `ai_project_sop.md`
- `project_bootstrap_sop.md`
- `facts_index.md`
- `naming_conventions.md`

### 3.2 禁止混用风格

同一文档体系下，不应混用：

- `camelCase`
- `PascalCase`
- `kebab-case`
- 中文文件名

除非当前生态或框架已有明确强约束，否则默认统一为下划线风格。

### 3.3 目录名称应体现职责

目录名称应尽量直接表达职责，而不是表达模糊集合。

推荐：

- `sop/`
- `facts/`
- `rules/`
- `standards/`
- `skills/`

不推荐：

- `misc/`
- `temp/`
- `others/`

---

## 4. 文档命名

### 4.1 SOP 文档

流程型文档应优先使用 `<subject>_sop.md` 格式。

例如：

- `project_bootstrap_sop.md`
- `maintenance_recovery_sop.md`

### 4.2 模板文档

模板型文档应优先使用 `<subject>_template.md` 格式。

例如：

- `task_template.md`
- `plan_item_template.md`

### 4.3 规则文档

规则型文档应优先使用 `<subject>_rules.md` 格式。

例如：

- `workflow_rules.md`
- `validation_rules.md`

### 4.4 标准文档

标准型文档应优先使用能够直接表达标准主题的复数或集合名。

例如：

- `naming_conventions.md`

### 4.5 AI 入口文档

AI 入口或 AI 专用主文档可保留 `ai_` 前缀，用于显式表明该文档承担 AI 工作流职责。

例如：

- `ai_project_sop.md`
- `ai_project_type.md`
- `ai_runtime_standards.md`

---

## 5. 层级对象命名

### 5.1 主对象名称

正式主对象统一使用以下名称：

1. `project`
2. `phase`
3. `plan`
4. `task`

如无必要，不引入同义替换词。

例如不建议在正式文档中混用：

- `stage`
- `mission`
- `job`
- `unit`

### 5.2 派生对象名称

派生对象应在主对象名称前后增加限定词，而不是改写主对象本体。

例如：

- `main plan`
- `sub plan`
- `plan item`
- `phase review`
- `next phase request`

---

## 6. 新增命名规范的升级要求

若某项目需要增加更细的命名规则，应先写入该项目的 `ai_runtime_standards.md`，待稳定后再评估是否升级进入正式 `standards/`。

升级前至少应满足：

1. 已在真实项目中验证。
2. 边界明确。
3. 没有明显项目绑定词。
4. 对多个项目具有复用价值。

---

## 7. 当前结论

默认情况下，采用本 SOP 的项目应以“语义清晰、同层一致、下划线风格”为命名基线。
