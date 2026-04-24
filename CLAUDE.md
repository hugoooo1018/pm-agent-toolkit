# pm-agent-toolkit — Claude Code 入口

本文件是 **Claude Code 的绑定入口**。其他 Agent 请看 `adapters/` 目录或 `README.md`。

## 三层架构速览

本仓库采用三层架构，详见 [docs/architecture.md](docs/architecture.md)：

```
知识层（agent-neutral）    rules/ + templates/ + lifecycle/
绑定层（agent-specific）    skills/（Claude Code）+ adapters/（其他 Agent）
集成层（产出去向）          integrations/（目前仅飞书）
```

## 激活中的 Rules

Session 启动时以下 Rule 默认生效（从 [rules/](rules/) 目录加载）：

- **[prd-writer](rules/prd-writer.md)** — PRD Writer 角色 + 11 条核心写作原则 + 基础三要素 + 工作流情境编排
- **[prd-clarification](rules/prd-clarification.md)** — 5 维度需求澄清框架 + 准入 checklist
- **[prd-paradigm](rules/prd-paradigm.md)** — 7/10 章骨架、L1/L2/L3、Always/Ask/Never 硬规则
- **[prd-quality-checklist](rules/prd-quality-checklist.md)** — 6 维度质量判据（自检与评审共用）

## 可用的 Skills（3 个）

按 description 自动触发或 `/skill-name` 显式调用：

| Skill | 职责 | 典型触发 |
|---|---|---|
| [prd-paradigm](skills/prd-paradigm/SKILL.md) | 按范式生成/改写 PRD 章节 | "帮我写 PRD"、"按范式补一个功能点" |
| [wireframe-generator](skills/wireframe-generator/SKILL.md) | 低保真 HTML 线框图 | "画一下这个页面的线框图" |
| [prd-review](skills/prd-review/SKILL.md) | 独立深度评审 | "评审 PRD"、"检查 PRD" |

## 典型工作流

```
用户输入（一句话需求）
  ↓
按 rules/prd-clarification.md 做 5 维度澄清 → 输出需求理解总结
  ↓
激活 prd-paradigm skill → 按 templates/default-style/ 的骨架展开章节
  ↓（按需）
激活 wireframe-generator skill → 生成线框图
  ↓
按 rules/prd-quality-checklist.md 自检（作者视角）
  ↓
激活 prd-review skill → 独立评审（reviewer 视角）
  ↓
产出 Markdown PRD → 通过 integrations/lark/ 发布到飞书
```

**松耦合**：每环可跳过、可反复。详见 [docs/prd-workflow.md](docs/prd-workflow.md) 与 [examples/daily-signin-feature/](examples/daily-signin-feature/)。

## 给 Claude 的关键指引

1. **写 PRD 前必过澄清**：除非用户明说"不澄清直接写"，否则触发 `prd-clarification` 流程
2. **章节生成用 paradigm**：`prd-paradigm` skill 会读 `templates/default-style/` 的骨架
3. **产出路径由用户指定**：不要假设 `docs/business/` 这种目录结构
4. **交付后建议下一步**：画线框图 / 找人评审 / 补 SOT / 推送飞书
5. **`rules/` 是单向源**：改规则只改 `rules/`；`skills/` 和 `adapters/` 只引用不重抄

## 贡献

- 新增 Rule → 先读 [rules/README.md](rules/README.md)（严守 agent-neutral 纯净度）
- 新增 Skill → 先读 [skills/README.md](skills/README.md)
- 新增 Adapter / Integration → 先读 [docs/integration-guide.md](docs/integration-guide.md)
- 完整贡献指南 → [CONTRIBUTING.md](CONTRIBUTING.md)
