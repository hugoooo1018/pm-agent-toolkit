# rules/ — Agent-neutral PM 知识

本目录是**不依赖任何 Agent 框架**的 PM 知识资产。每个文件都应能被复制粘贴到任意 LLM 的系统提示词里直接使用。

## 纯净度要求（CI 会自动检查）

rules/ 下任何文件：

- ❌ frontmatter 不含 `related_skills` / `applies_rules`（那是 Skill 的字段）
- ❌ body 不出现 `/skill-name`、`skills/...`、`SKILL.md` 等 Claude Code 专属引用
- ❌ 不提"Read 工具"、"Stage 0/1/2"等 Claude Code 内部术语
- ✅ 描述能力时用抽象名（"原型图能力"而非 "wireframe-generator"）
- ✅ 可引用 `../templates/`（templates/ 也是 agent-neutral 资产）
- ✅ 可引用同级 `*.md`（rule 之间可相互引用）

## Frontmatter schema

```yaml
---
name: <kebab-case>              # 必填，与文件名（去扩展名）一致
description: <一句话概括>        # 必填
scope: <领域标签>                # 必填，如 prd-writing
version: <semver>                # 必填，如 0.2.0
---
```

## Body 结构建议

Rule 没有固定 body 模板，但推荐含：

- **定位 / 何时使用**
- **核心原则 / 硬约束**
- **怎么做**（步骤、清单、示例）
- **反例 / 不做的事**
- **延伸阅读**（其他相关 Rule / Template）

## 新增 Rule 的流程

1. 在 `rules/` 下建 `<name>.md`
2. 按 schema 填 frontmatter
3. 写 body，严守纯净度
4. 跑 `python scripts/validate_frontmatter.py`
5. 在 `CLAUDE.md` 的 Rules 列表追加一行（这是 Claude Code 绑定，不违反 Rule 纯净）
6. 本文件"当前 Rules"段追加

## 当前 Rules

- **[prd-writer](prd-writer.md)** — PRD Writer 角色定义 + 11 条核心写作原则 + 基础三要素 + 工作流情境编排
- **[prd-clarification](prd-clarification.md)** — 5 维度需求澄清框架 + 准入 checklist
- **[prd-paradigm](prd-paradigm.md)** — 7/10 章骨架、L1/L2/L3 三层结构、Always/Ask/Never 硬规则
- **[prd-quality-checklist](prd-quality-checklist.md)** — 6 维度质量判据 + P 类原则自查（评审与自查共用真源）

## 设计原则

- **少而精**：加 Rule 要有"这是跨场景通用原则"的明确理由，否则放 docs/
- **单向引用**：Rule → Rule 之间可引用；Rule → Skill **从不反向引用**
- **版本化**：break 时升主版本；加字段/补充升次版本
- **fork 友好**：别人 fork 本仓库改成自己公司的风格时，只需改本目录 + `templates/`，`skills/` 和 `adapters/` 的绑定层不用大动
