# 集成指南

本文档说明如何：

1. 接入新的 **Agent**（消费 rules/）
2. 接入新的**产出去向**（Markdown PRD 流向真实工具）

## 接入新 Agent

### 原则

每个 Agent 都是通过"把 rules/ 里的知识翻译成它能消费的格式"来集成，**不需要改 rules/ 本身**。

### 步骤

1. 在 `adapters/<agent-name>/` 建目录
2. 读 rules/ 下全部 Rule
3. 按目标 Agent 的规范把 Rule 内容拼装成它支持的格式
4. 写一份 `README.md` 说明如何使用

### 常见 Agent 的接入格式

| Agent | 配置文件 | 要点 |
|---|---|---|
| Claude Code | `skills/<name>/SKILL.md` + `CLAUDE.md` | 用官方 SKILL.md 规范；CLAUDE.md 列出激活 rule |
| Cursor | `.cursorrules`（单文件） | 把 rules/ 内容合并成一份纯文本，开头说明身份 |
| Windsurf | `.windsurfrules` | 格式接近 Cursor |
| Cline | `.clinerules/*.md` | 支持多文件，可按 rules/ 文件数拆分 |
| GPT Assistants (OpenAI) | Instructions 字段 | 单文本框，拼成完整 system prompt |
| Claude Projects (claude.ai) | Project Instructions | 同上 |
| 自建 Agent | 系统提示词 | 用 `adapters/generic-system-prompt/` 的模板 |

### 示例：给 Cursor 做适配

本仓库 `adapters/cursor/.cursorrules` 就是一份现成的适配。它的生成逻辑：

```
# .cursorrules 的内容 =
  [rules/prd-writer.md 的 body（去掉 frontmatter）]
+ [rules/prd-paradigm.md 的 body]
+ [rules/prd-clarification.md 的 body]
+ [rules/prd-quality-checklist.md 的 body]
+ 顶部加一段说明 "你是一个 PRD Writer Agent，遵守以下原则..."
+ 底部加一段说明 "写 PRD 时参考 templates/default-style/ 的骨架"
```

手动拼装即可，不需要脚本（未来若自动化可加到 `scripts/build_adapters.py`）。

### 自检

新 adapter 做完后，自问：

- 这个 agent 在消费我的 adapter 时，能看到和 Claude Code 一样的 PRD 知识吗？
- 它能写出与本仓库 skills 产出**质量相当**的 PRD 吗？
- 如果 rules/ 更新了，我的 adapter 会不会漂移？（未来可加校验脚本）

---

## 接入新产出去向

### 本仓库的定位

Markdown 是本仓库的**唯一产出格式**。产出后送到哪儿，由 integrations/ 层负责。

### 原则

- **不做真实 API 对接**（那是 MCP 生态的事）
- **只写指南 + 命令示例**
- **复用已有工具**

### 常见去向

| 去向 | 推荐方式 | 目录 |
|---|---|---|
| 飞书文档 | `lark-cli` 或 `lark-doc` skill | `integrations/lark/`（已做） |
| Confluence | atlas-confluence MCP | 待做 |
| Notion | notion MCP | 待做 |
| GitHub Wiki | 直接 git push markdown | 可 inline 在 README |
| Docusaurus | 文件直接放 `docs/business/` 目录 | 可 inline |
| JIRA / Linear | 相应 MCP 把 PRD 拆成 ticket | 待做（高级） |

### 新增去向的步骤

1. 建 `integrations/<destination>/README.md`
2. 内容至少含：
   - 场景（什么时候用）
   - 前置（需要装什么）
   - 命令示例（3–5 行 bash 即可）
   - 常见坑
3. 不要写包装脚本。如果必须写，放在 `scripts/<destination>/` 并在 README 说清楚

### 示例：飞书文档集成的最小实现

```bash
# 前置：已装 lark-cli 并完成 auth login
lark-cli docs create \
  --from-md examples/daily-signin-feature/04-prd-final.md \
  --title "每日签到 PRD v1.0" \
  --folder "产品文档/PRD"
```

就这么简单。所有复杂度交给 lark-cli 自己。

---

## FAQ

**Q：为什么不做真实的 JIRA 集成？**

A：MCP 生态已经有 [mcp-jira](https://github.com/mcp-use/mcp-jira) 等成熟方案。重造轮子浪费精力。本仓库的价值在**知识层**（PRD 内容质量），不在对接管道。

**Q：为什么 adapters/ 下只给静态文件，不做脚本自动生成？**

A：首版优先保证"每个 adapter 人工 review 过、真的能用"。自动生成脚本可以在有 5+ adapter 后再加（模板化收益才明显）。

**Q：rule 更新后，adapters/ 会不会过时？**

A：会。需要手动同步，或加 CI 脚本对比 rules/ hash 与 adapters/ hash。首版用人工维护。

**Q：我能不能只用 Cursor 不用 Claude Code？**

A：完全可以。`adapters/cursor/.cursorrules` 是独立可用的，`templates/` 和 `rules/` 都是你的。`skills/` 可以忽略。
