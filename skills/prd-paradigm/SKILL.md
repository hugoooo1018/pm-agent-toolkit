---
name: prd-paradigm
description: 按 PRD 范式生成或审查段落/章节。用户说"写 PRD / 新建模块 PRD / 补充功能点 / 按范式生成章节 / 检查 PRD 结构"时触发。可用于模块级（整 7 章 PRD）或功能级（10 章中的模块详述章节）。
type: workflow
applies_rules:
  - prd-writer
  - prd-paradigm
  - prd-quality-checklist
version: 0.2.0
---

# prd-paradigm（Claude Code 绑定）

本 skill 是 Claude Code 的**绑定层**。它不自带范式内容——所有规则与骨架都在知识层：

- **范式规则** → `../../rules/prd-paradigm.md`
- **写作原则** → `../../rules/prd-writer.md`
- **骨架模板** → `../../templates/logic-labs-style/`
- **质量自检** → `../../rules/prd-quality-checklist.md`

## 触发时机

- 新建一份模块级 PRD（整份 7 章骨架）
- 向已有 PRD 追加或修改功能点
- 按范式审查已有 PRD 的章节结构
- 功能级 PRD 写到"功能模块详述"章节时被调用

## 执行流程

### 第 1 步：读取知识层

按需并行读取：

- `rules/prd-writer.md` — 角色与原则
- `rules/prd-paradigm.md` — 范式硬规则（Always/Ask/Never）
- `templates/logic-labs-style/module-prd-7-chapter.md` 或 `feature-prd-10-chapter.md` — 骨架
- `templates/logic-labs-style/L2-operational.md` / `L2-page.md` / `L2-execution.md` — L2 形态模板（按需）
- `templates/logic-labs-style/field-naming.md` / `mermaid-styles.md` — 命名与样式规范
- 用户提供的业务对象文档（`*-business-objects.md`）若存在

### 第 2 步：确认产出位置

产出路径由**用户指定**，本 skill 不假设仓库布局。常见约定（供参考）：

- 模块级：`<repo>/<prd-dir>/<module>/<module>-prd.md`
- 业务对象：`<repo>/<prd-dir>/<module>/<module>-business-objects.md`
- 原型图：`<repo>/<prd-dir>/<module>/assets/<page>.jpg`

如用户未指定，先问一次。

### 第 3 步：按骨架生成

- 选择模板（模块级 7 章 / 功能级 10 章）
- 按章节顺序填写，严守 `rules/prd-paradigm.md` 的 Always/Ask/Never
- 核心术语首次出现加粗 + 中英文配对
- 需要用户确认的地方（新模块归属 / 跨模块规则同步 / MVP 不做项）**主动问**，不要假设

### 第 4 步：交付 + 自检

交付时附一份简短自检（按 `rules/prd-quality-checklist.md` 的 P 类原则快速过一遍），标注：

- 哪些章节自动填充
- 哪些留了 `[待 <角色> 确认]` 的 TODO
- 建议下一步（画线框图 / 找人评审）

## 不做的事

- **不重抄范式原则** — 引用 `rules/prd-paradigm.md` 即可
- **不假设产出路径** — 由用户指定
- **不自动推送到飞书** — 那是 `integrations/lark/` 的职责
- **不做深度质量评审** — 那是 `prd-review` skill 的职责

## 输出形态

Markdown 文档。不写 `*.review.md` 或 `*.draft.md` 副本——单一产出路径，避免漂移。
