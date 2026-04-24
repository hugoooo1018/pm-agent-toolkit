# adapters/ — 非 Claude Code 的 Agent 接入

本目录把知识层（`../rules/`）翻译成不同 Agent 生态能消费的格式。

## 为什么有这一层

`rules/` 是 agent-neutral 的 PM 知识资产，但各 Agent 生态消费知识的方式不同：

| Agent | 消费方式 | 本仓库绑定位置 |
|---|---|---|
| Claude Code | `SKILL.md` + `CLAUDE.md` | `../skills/` |
| Cursor | `.cursorrules`（单文件） | `cursor/.cursorrules` |
| Windsurf | `.windsurfrules` | 待加 |
| Cline | `.clinerules/*.md` | 待加 |
| OpenAI GPT Assistants | Instructions（单文本框） | 用 `generic-system-prompt/` |
| Claude Projects (claude.ai) | Project Instructions | 用 `generic-system-prompt/` |
| 自建 Agent | System prompt | 用 `generic-system-prompt/` |

## 当前 Adapters

### `cursor/` — Cursor IDE

把所有 Rule 合成一份 `.cursorrules`，复制到你的 Cursor 项目根目录即可。

**使用**：

```bash
cp adapters/cursor/.cursorrules /path/to/your/project/
```

Cursor 会在该项目所有会话里自动加载这份规则。

### `generic-system-prompt/` — 通用 LLM 系统提示词

一份纯文本系统提示词，可粘贴到：

- OpenAI GPT Assistants 的 Instructions 框
- Claude Projects 的 Project Instructions
- ChatGPT 自定义 GPT 的 Instructions
- 任意 LLM API 的 `system` 字段

**使用**：打开 `generic-system-prompt/prd-writer-system-prompt.md`，复制全文（不含 frontmatter）粘贴到目标位置。

## 新增 Adapter

想为 Windsurf / Cline / 其他 Agent 做适配？步骤：

1. 在 `adapters/<agent-name>/` 建目录
2. 读 `../rules/` 下所有 Rule，按目标 Agent 的规范拼装
3. 写 `README.md` 说明如何使用
4. 本文件"当前 Adapters"段追加入口

详见 `../docs/integration-guide.md`。

## 同步策略

Rule 更新后，adapter 文件需要手动同步（当前版本不做自动生成）。

未来计划：加 `scripts/build_adapters.py` 从 rules/ 自动生成各 adapter，并用 hash 检查保持同步。

## 纯度要求

Adapter 文件**不应自造新内容**。它只是 Rule 的翻译/拼装。有任何需要补充的 PM 知识，加到 `rules/` 里，让所有 adapter 受益。
