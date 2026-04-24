# 三层架构

## 为什么要分三层

一个"好的 Agent 工具包"要回答三个问题：

1. **内容是什么？**（知识层）
2. **谁能消费？**（绑定层）
3. **产出到哪去？**（集成层）

大多数开源 agent skills 只回答了第 2 个——只对某个特定 Agent（Claude Code）做了绑定。这让它们的知识资产被锁死在一个生态里。本仓库显式分开这三层。

## 三层模型

```
┌──────────────────────────────────────────────────────────────┐
│  Layer 1: 知识层（Agent-neutral）                            │
│  ─────────────────────────────────                           │
│  rules/       — PM 原则、方法论（零 Claude Code 特征）       │
│  templates/   — PRD 骨架模板（opinionated）                  │
│  lifecycle/   — PRD 状态定义                                 │
│                                                              │
│  这层的每个文件都应该能被剪切板复制到任何 Agent 的系统提示词 │
└──────────────────────────────────────────────────────────────┘
                        ↑                 ↑
        ┌───────────────┘                 └────────────────┐
        │                                                  │
┌──────────────────────────┐           ┌─────────────────────┐
│  Layer 2a: Claude Code  │           │  Layer 2b: Adapters │
│  ─────────────────────  │           │  ────────────────── │
│  skills/                │           │  adapters/cursor/   │
│   ├─ prd-paradigm/      │           │  adapters/generic-  │
│   ├─ wireframe-         │           │    system-prompt/   │
│   │    generator/       │           │                     │
│   └─ prd-review/        │           │  从 rules/ 拼装出   │
│                         │           │  各 Agent 能吃的格式│
│  Claude Code 专用绑定   │           │                     │
└──────────────────────────┘           └─────────────────────┘
                        │                 │
                        └─────────┬───────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  Layer 3: 集成层（产出去向）                                 │
│  ─────────────────────────                                   │
│  integrations/lark/  — 把 Markdown PRD 推到飞书文档          │
│                                                              │
│  不做 JIRA/Linear/Figma 等重工集成——那是 MCP 生态的事       │
└──────────────────────────────────────────────────────────────┘
```

## 数据流

用户启动一次 PRD 写作任务：

```
输入（一句话需求）
   │
   ▼
Agent（Claude Code / Cursor / 任意）
   │  1. 读 Layer 1（rules/ + templates/）
   │  2. 通过 Layer 2 的绑定识别该做什么
   │  3. 生成 Markdown PRD
   ▼
Markdown PRD 草稿
   │
   ▼（可选）
Layer 3 推送（lark-cli）
   │
   ▼
飞书文档 / 其他协作平台
```

## 各层的职责边界

| 层 | 职责 | 不做的事 |
|---|---|---|
| 知识层（rules/） | 写作原则、方法论 | 不提具体工具名、不写执行流程 |
| 知识层（templates/） | 可直接复制的骨架 | 不含 agent 指令 |
| 知识层（lifecycle/） | 状态定义 | 不实现状态转换自动化 |
| 绑定层（skills/） | Claude Code 触发、流程编排 | 不重抄 Rule 原则（引用即可） |
| 绑定层（adapters/） | 给其他 Agent 用的静态格式 | 不实现运行时逻辑 |
| 集成层（integrations/） | 产出去向的接入说明 | 不写真实对接代码（用现有 CLI） |

## 三层各自的"纯净度"标准

### 知识层的纯净度

**rules/ 下任一文件，都应能被复制粘贴到任何 LLM 的系统提示词里使用，不需要任何改动。**

实操标准（CI 会自动检查）：

- frontmatter 不含 `related_skills` / `applies_rules`
- body 不含 `/skill-name`、`skills/`、`SKILL.md`、`Read 工具` 等 Claude Code 特征
- 描述能力时用抽象名（"原型图能力"）而非具体工具（"wireframe-generator"）

### 绑定层的纯净度

**skills/ 下的 SKILL.md 可以自由用 Claude Code 特性，但不该重复 rules/ 的内容。**

实操标准：

- body 有 `## Rule References` 段引用 rules/
- 写"读 rules/prd-paradigm.md 然后按 templates/default-style/ 的骨架生成"这种绑定语句
- 不把 Rule 原则再抄一遍

### 集成层的纯净度

**integrations/ 下只写"怎么用"，不实现"做什么"。**

实操标准：

- 只有 README.md，没有可执行代码
- 复用已有生态工具（lark-cli、mcp-* 等）
- 给出具体的命令示例

## 与社区其他仓库的对比

| 仓库 | 层次清晰度 | 跨 Agent | 集成层 |
|---|---|---|---|
| pm-skills (Paweł) | 扁平 skill 列表 | ❌ 仅 Claude Code | ❌ |
| Product-Manager-Skills (Dean) | 单 marketplace | ❌ 仅 Claude Code | ❌ |
| lenny-skills (RefoundAI) | 最扁平 | ❌ 仅 Claude Code | ❌ |
| **pm-agent-toolkit（本仓库）** | **三层显式** | **✅ rules/ 是 agent-neutral** | **✅ lark** |

## 什么时候该新增一层文件？

- 新增**原则 / 方法论** → `rules/`
- 新增**可复制的 PRD 骨架** → `templates/<style>/`
- 新增 **Claude Code 触发入口** → `skills/`
- 新增**其他 Agent 的绑定** → `adapters/<agent>/`
- 新增**产出去向** → `integrations/<destination>/`
- 新增**用例 / 端到端示范** → `examples/`
- 新增**给维护者/消费者看的说明** → `docs/`

## 延伸阅读

- [docs/opinionated.md](opinionated.md) — 为什么这么 opinionated
- [docs/rule-skill-model.md](rule-skill-model.md) — Rule 和 Skill 的分工原理
- [docs/prd-workflow.md](prd-workflow.md) — 实战工作流
- [docs/integration-guide.md](integration-guide.md) — 怎么接入新的 Agent 或新的产出去向
