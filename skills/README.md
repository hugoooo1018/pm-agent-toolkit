# skills/ — Claude Code 绑定层

本目录是 Claude Code 专用的 Skill 绑定。职责是：把知识层（`rules/` + `templates/`）翻译成 Claude Code 能触发的工作流。

## 设计原则

- **薄壳**：Skill 不重抄 Rule 原则，只做绑定与流程编排
- **单向依赖**：Skill → Rule 单向引用（frontmatter 的 `applies_rules` 字段）
- **零自造内容**：所有写作原则、骨架、判据都在 `rules/` 和 `templates/`
- **可触发**：description 写清楚触发场景，让 Claude 能自动识别

## Frontmatter schema

```yaml
---
name: prd-paradigm               # 必填，与目录名一致
description: <触发场景说明>       # 必填
type: workflow                   # 必填：component / interactive / workflow
applies_rules:                   # 可选，单向指向 rules/
  - prd-writer
  - prd-paradigm
allowed-tools: Read, Glob, Grep  # 可选
version: 0.2.0                   # 必填
---
```

## 当前 Skills（3 个）

| Skill | 职责 | 触发词 | 依赖 Rule |
|---|---|---|---|
| [prd-paradigm](prd-paradigm/SKILL.md) | 按范式生成/改写 PRD 章节 | "写 PRD"、"按范式补功能点"、"检查 PRD 结构" | prd-writer / prd-paradigm / prd-quality-checklist |
| [wireframe-generator](wireframe-generator/SKILL.md) | 从 PRD 文本生成低保真 HTML 线框图 | "生成 wireframe"、"画线框图"、"把原型图改成 HTML" | — |
| [prd-review](prd-review/SKILL.md) | 独立评审 PRD，多轮澄清 + 结构化报告 | "评审 PRD"、"检查 PRD"、"PRD 质量检查" | prd-writer / prd-quality-checklist |

## 旧版删除的 Skill 去哪了？

0.1.x 版本的 skill 在 0.2.0 有调整：

- **prd-clarification** → 升格为 `rules/prd-clarification.md`（方法论，agent-neutral）
- **prd-self-checker** → 合并进 `rules/prd-quality-checklist.md`（与独立评审共享同一份判据）

理由：这两者是**跨 Agent 通用的方法论**，不应锁在 Claude Code 的 skill 里。升格后，Cursor / Windsurf / 任意 Agent 都能消费。

## 新增 Skill 的流程

1. 在 `skills/<name>/` 下建 `SKILL.md`
2. frontmatter 与 body 完整
3. body 里**引用 rules/**，不重抄原则
4. 在 `CLAUDE.md` 的 Skills 清单追加一行
5. 更新本文件的 "当前 Skills" 表

## 与其他 Agent 生态的对应关系

本目录是 Claude Code 的绑定。其他 Agent 的绑定在：

- **Cursor** → `adapters/cursor/.cursorrules`
- **通用系统提示词** → `adapters/generic-system-prompt/prd-writer-system-prompt.md`
- 未来其他 → `adapters/<agent-name>/`

所有绑定层消费同一份 `rules/` 和 `templates/`。
