# templates/ — PRD 骨架模板

本目录收录**可直接复制填写**的 PRD 骨架。不同风格放在不同子目录。

## Opinionated 声明

当前仓库首版只提供 **logic-labs-style**，基于 logic-labs 一线 PM 实践沉淀。它有以下鲜明取向：

- 7 章模块级骨架（编号/顺序固定）
- L1/L2/L3 三层结构
- L2 按"操作型 / 页面型 / 执行型"三形态分类
- 字段表固定 4 列
- 核心术语全文加粗且每次出现形式完全一致

这套范式适合：**多人协作、严格结构化、长期维护**的 PRD。

不适合：战略级 PRD、一页纸 PRD、Amazon PR-FAQ 式产品。

**欢迎 fork 加入其他风格**（详见 `../docs/opinionated.md`）。

## 目录

### `logic-labs-style/`

- [module-prd-7-chapter.md](logic-labs-style/module-prd-7-chapter.md) — 模块级 PRD 骨架
- [feature-prd-10-chapter.md](logic-labs-style/feature-prd-10-chapter.md) — 功能级 PRD 骨架
- [L2-operational.md](logic-labs-style/L2-operational.md) — 操作型功能模板
- [L2-page.md](logic-labs-style/L2-page.md) — 页面型功能模板
- [L2-execution.md](logic-labs-style/L2-execution.md) — 执行型功能模板
- [field-naming.md](logic-labs-style/field-naming.md) — 字段命名规范
- [mermaid-styles.md](logic-labs-style/mermaid-styles.md) — 架构图 / 流程图样式
- [pitfalls.md](logic-labs-style/pitfalls.md) — 常踩坑清单（反例库）

## 使用方式

### 方式 A：手动复制

```bash
# 模块级
cp templates/logic-labs-style/module-prd-7-chapter.md docs/business/<module>/<module>-prd-v1.md

# 功能级
cp templates/logic-labs-style/feature-prd-10-chapter.md docs/business/<module>/<feature>-prd.md
```

复制后按 `rules/prd-paradigm.md` 的规则填写。

### 方式 B：Agent 辅助

让 Agent（Claude Code / Cursor / 其他）读本目录模板 + `rules/` 后生成首版草稿，你做 reviewer。

## 新增风格模板

想加新风格（Amazon PR-FAQ / Intercom RFC 等）？步骤见 `../CONTRIBUTING.md`。

核心要求：

1. 新建 `templates/<style-name>/` 目录
2. 含 `README.md` 说明来源、适用场景、与 logic-labs-style 的差异
3. 骨架文件**可直接复制**（不要只放原则说明，那是 `rules/` 的职责）
4. 在本文件"目录"段追加入口
