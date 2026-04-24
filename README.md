<div align="center">

# 🧠 pm-agent-toolkit

**面向产品经理的 Agent 工具包 —— 把一句话需求沉淀成工业级 PRD**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)](CHANGELOG.md)
[![CI](https://github.com/hugoooo1018/pm-agent-toolkit/actions/workflows/validate.yml/badge.svg)](https://github.com/hugoooo1018/pm-agent-toolkit/actions)
[![Made for Claude Code](https://img.shields.io/badge/Made%20for-Claude%20Code-D97757.svg)](https://docs.claude.com/en/docs/claude-code)
[![Cross Agent](https://img.shields.io/badge/Cross--Agent-Cursor%20%7C%20Windsurf%20%7C%20GPT-success.svg)](adapters/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[简介](#) · [快速上手](#快速上手) · [架构](#三层架构) · [端到端示例](examples/daily-signin-feature/) · [文档](docs/) · [贡献](CONTRIBUTING.md)

</div>

---

融合 **Agent Rule**（可跨 Agent 消费的 PM 知识层）和 **Agent Skill**（Claude Code 绑定层）两种抽象。一次编写知识，多处消费 —— Claude Code、Cursor、任意 LLM 都能用。

## 特点

- **三层架构**：知识层 / 绑定层 / 集成层显式分离，互不污染
- **跨 Agent**：`rules/` 纯粹的 PM 知识资产，可被 Claude Code / Cursor / 任意 LLM 消费
- **端到端**：需求澄清 → 按范式生成 → 线框图 → 自检 → 独立评审 → 推送飞书，全流程闭环
- **opinionated 但可 fork**：范式基于 logic-labs 一线 PM 实践，明确声明公司风味，便于定制

---

## Opinionated 声明

本仓库的 PRD 范式来自 **logic-labs 实践**，有特定"公司口味"：

- 7 章模块级 + 10 章功能级骨架
- L1/L2/L3 三层结构
- L2 功能三形态（操作型 / 页面型 / 执行型）
- 字段表固定 4 列
- 核心术语全文加粗且每次出现形式完全一致

如果你团队风格不同，欢迎 **fork 后改写 `templates/` 和 `rules/prd-paradigm.md`**。`rules/` 里 INVEST / Gherkin / 三层指标等原则是通用的，可以保留。详见 [docs/opinionated.md](docs/opinionated.md)。

---

## 三层架构

```
┌────────────────────────────────────────────────────────────┐
│ 知识层（agent-neutral）                                    │
│   rules/        — PM 原则、方法论                          │
│   templates/    — PRD 骨架（opinionated）                  │
│   lifecycle/    — PRD 生命周期状态                         │
└────────────────────────────────────────────────────────────┘
                    ↑                    ↑
┌────────────────────────┐    ┌──────────────────────────┐
│ 绑定层：Claude Code    │    │ 绑定层：其他 Agent       │
│   skills/              │    │   adapters/              │
│     ├─ prd-paradigm    │    │     ├─ cursor/           │
│     ├─ wireframe-      │    │     └─ generic-system-   │
│     │    generator     │    │         prompt/          │
│     └─ prd-review      │    │                          │
└────────────────────────┘    └──────────────────────────┘
                    ↓
┌────────────────────────────────────────────────────────────┐
│ 集成层（产出去向）                                         │
│   integrations/lark/  — 用飞书 CLI 发 PRD 到飞书文档       │
└────────────────────────────────────────────────────────────┘
```

---

## 目录

```
rules/                # Agent-neutral PM 知识（核心资产）
  ├─ prd-writer.md             角色 + 11 条核心原则
  ├─ prd-clarification.md      5 维度需求澄清
  ├─ prd-paradigm.md           7/10 章骨架 + L1/L2/L3
  └─ prd-quality-checklist.md  6 维度质量判据

templates/            # opinionated PRD 骨架
  └─ logic-labs-style/         模块级 7 章 + 功能级 10 章 + L2 三形态 + 命名/样式规范

skills/               # Claude Code 绑定层（3 个薄壳 skill）
  ├─ prd-paradigm/             按范式生成章节
  ├─ wireframe-generator/      线框图
  └─ prd-review/               独立深度评审

adapters/             # 其他 Agent 接入
  ├─ cursor/.cursorrules       直接复制到 Cursor 项目
  └─ generic-system-prompt/    任意 LLM 的系统提示词

integrations/         # 产出去向
  └─ lark/                     飞书 CLI 接入指南

lifecycle/            # PRD 生命周期定义
  └─ states.md                 Draft/Review/Approved/InDev/Shipped/Deprecated

examples/             # 端到端示例
  └─ daily-signin-feature/     一句话输入 → 澄清 → PRD → 评审 → 终版

docs/                 # 深度文档
  ├─ architecture.md           三层架构详解
  ├─ opinionated.md            opinionated 声明 + fork 指南
  ├─ glossary.md               术语表
  ├─ integration-guide.md      接入新 Agent / 新产出去向
  ├─ prd-workflow.md           完整 PRD 工作流
  └─ rule-skill-model.md       Rule 与 Skill 的分工原理

scripts/              # 工具脚本
  └─ validate_frontmatter.py   CI lint

.github/workflows/    # CI
  └─ validate.yml              frontmatter + Rule 纯净度检查

CLAUDE.md             # Claude Code 入口
CONTRIBUTING.md       # 贡献指南
CHANGELOG.md          # 版本变更
LICENSE               # MIT
```

---

## 快速上手

### 如果你用 Claude Code

```bash
cd pm-agent-toolkit
claude
# 然后：帮我写一份 <你的功能> 功能的 PRD
```

Claude 会按照 `CLAUDE.md` 激活的 Rules，自动引导你走 clarification → paradigm → review 流程。

完整示例见 [examples/daily-signin-feature/](examples/daily-signin-feature/)。

### 如果你用 Cursor

```bash
cp adapters/cursor/.cursorrules /path/to/your/project/
```

Cursor 会在该项目自动加载规则。

### 如果你用其他 LLM（ChatGPT / Claude Projects / 自建 Agent）

打开 [adapters/generic-system-prompt/prd-writer-system-prompt.md](adapters/generic-system-prompt/prd-writer-system-prompt.md)，复制全文粘贴到目标系统的系统提示词框即可。

### 如果你只想看范式骨架

直接复制 [templates/logic-labs-style/](templates/logic-labs-style/) 下的模板填写。`rules/prd-paradigm.md` 讲解填写规则。

---

## 与其他 PM skills 仓库的对比

| 仓库 | 结构 | Rule 层 | 跨 Agent | 端到端示例 | 生命周期 |
|---|---|---|---|---|---|
| [pm-skills](https://github.com/pawel-huryn/pm-skills) | 多 plugin | ❌ | ❌ | ❌ | ❌ |
| [Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 单 marketplace | ❌ | ❌ | ❌ | ❌ |
| [lenny-skills](https://github.com/RefoundAI/lenny-skills) | 扁平 | ❌ | ❌ | ❌ | ❌ |
| **pm-agent-toolkit** | **三层架构** | **✅** | **✅** | **✅** | **✅** |

---

## 贡献

欢迎 PR。特别鼓励：

- 新的 PRD 风格模板（Amazon PR-FAQ / Intercom RFC 等，放 `templates/<style>/`）
- 新的 Agent adapter（Windsurf / Cline / GPT Assistants 等，放 `adapters/<agent>/`）
- 端到端示例（放 `examples/<scenario>/`）
- 文档错误 / 术语补充

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 许可

[MIT](LICENSE) © 2026 Hugo
