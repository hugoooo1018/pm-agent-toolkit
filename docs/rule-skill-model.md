# Rule 与 Skill 的分工原理

本文档解释本仓库"分层双栈 → 三层架构"的演进理由，以及 Rule 和 Skill 之间究竟如何分工。

## 先说结论

| 维度 | Rule | Skill |
|---|---|---|
| **定位** | Agent-neutral 的 PM 知识资产 | Claude Code 的绑定层 |
| **可被谁消费** | 任何 Agent（Claude Code / Cursor / Windsurf / 自建 / 任意 LLM） | 仅 Claude Code |
| **加载时机** | session 启动，常驻上下文 | 被触发时按需加载 |
| **触发方式** | 全局适用，无需触发 | description 匹配 / `/skill-name` |
| **内容** | 原则 / 方法论 / 范式 / 判据 | Claude Code 的 workflow 绑定 |
| **纯净度** | 零 Claude Code 特征（CI 检查） | 可自由使用 Claude Code 特性 |
| **引用方向** | 不反向引用 Skill | Skill → Rule 单向引用 |

## 为什么要分开

### 问题：现有社区仓库都把两者混在 SKILL.md 里

看看主流 PM skills 仓库（pm-skills / Product-Manager-Skills / lenny-skills），它们的每个 SKILL.md 同时塞了：

- 原则（什么是好 PRD）
- 方法论（怎么做）
- 工作流（按什么步骤执行）
- 特定 Agent 的触发绑定

混在一起带来三个问题：

1. **原则重复**：每个 skill 都抄一遍"PRD 要有指标"
2. **无法跨 Agent**：SKILL.md 是 Claude Code 专用格式
3. **演进割裂**：原则更新时要改一堆 skill

### 解法：把知识和绑定剥离

- **知识归 Rule**（`rules/*.md`）：纯文本的 PM 知识，不关心是谁在读
- **绑定归 Skill**（`skills/*/SKILL.md`）：Claude Code 的触发 + 工作流编排，引用 Rule 不重抄

加上 `adapters/` 层（其他 Agent 的绑定）和 `templates/` 层（骨架），就形成了本仓库的**三层架构**（详见 [architecture.md](architecture.md)）。

## 真实案例：PRD 工作流

本仓库的 PRD 场景：

```
rules/prd-writer.md              ← 主角色 Rule（常驻）
  ├─ 基础三要素（用户场景/指标/风险）
  ├─ 11 条核心写作原则（INVEST/Gherkin/追溯矩阵/SOT/...）
  └─ 工作流情境编排（不提具体 skill 名）

rules/prd-clarification.md       ← 方法论 Rule
  └─ 5 维度澄清 + 准入 checklist

rules/prd-paradigm.md            ← 范式 Rule
  └─ 7/10 章骨架、L1/L2/L3、Always/Ask/Never

rules/prd-quality-checklist.md   ← 判据 Rule
  └─ 6 维度 + P 类原则（自检与评审共用）

templates/logic-labs-style/      ← opinionated 骨架
  └─ 可直接复制的模板

skills/prd-paradigm/             ← Claude Code 绑定
skills/wireframe-generator/      ← Claude Code 绑定
skills/prd-review/               ← Claude Code 绑定

adapters/cursor/.cursorrules     ← Cursor 绑定（从 rules/ 拼装）
adapters/generic-system-prompt/  ← 任意 LLM 绑定
```

**关键观察**：

1. **Rule 不知道 Skill 存在**：rules/ 下没有任何文件提到 `wireframe-generator` 或 `/prd-review`
2. **Skill 不重抄 Rule**：skills/prd-paradigm/SKILL.md 只有 40 行，内容全在 rules/ 和 templates/
3. **同一份 checklist** 被 prd-review 和作者自检共用（`rules/prd-quality-checklist.md`）
4. **其他 Agent 零改动接入**：复制 `.cursorrules` 到 Cursor 项目即可，无需安装任何 skill

## Rule 的 CI 纯净度检查

为了保证 Rule 真的 agent-neutral，本仓库的 `.github/workflows/validate.yml` 会做：

```bash
# 扫描 rules/ 下（排除 README.md）是否含 Claude Code 残留
find rules -name '*.md' -not -name 'README.md' -exec \
  grep -Hn 'skills/\|SKILL\.md\|/prd-review\|/prd-paradigm\|/wireframe-generator' {} \;
```

命中任一即 CI 失败。确保 Rule 真的能被其他 Agent 直接消费。

## 什么时候写成 Rule、什么时候写成 Skill？

**写成 Rule**（放 `rules/`）：

- 跨工作流通用的原则
- 形式是"永远要 / 永远不要"
- 改一次后，所有相关流程都该自动跟随
- 可被任意 Agent 消费
- 方法论或判据本身（而非"Claude 具体怎么执行"）

**写成 Skill**（放 `skills/`）：

- 有明确输入输出的 Claude Code 工作流
- 需要触发识别（description 匹配）
- 需要流程编排（多步 + 工具调用）
- 包含 Claude Code 特定的交互方式

**判断不清时** 放 `rules/`，只在 Rule 层不够用时才建 Skill。

## 数据流

```
用户输入
   ↓
Agent（Claude Code / Cursor / 任意）在 session 启动时加载 Layer 1（rules/）
   ↓
Agent 通过 Layer 2（skills/ 或 adapters/）识别应做什么
   ↓
Agent 按 rules/ 原则 + templates/ 骨架生成 Markdown PRD
   ↓
可选：Layer 3（integrations/）推送到飞书等
```

Rule 是常驻的"宪法"，Skill 是需要时召唤的"行政工具"。

## 不引入的概念

- **Hooks**：自动化工具事件。本仓库 v0.2 不需要
- **Commands**：显式 slash command。Skill 的 description 触发已够用
- **Subagents**：独立上下文的执行单元。单 session 够用
- **Rule 之间的强制依赖**：允许 Rule 互相引用，但不做强制 lint

等规模扩大（rules > 10、skills > 5、用户需要不同 PRD 风格共存）时再考虑引入。

## 延伸

- [architecture.md](architecture.md) — 三层架构详解
- [opinionated.md](opinionated.md) — opinionated 声明
- [prd-workflow.md](prd-workflow.md) — PRD 完整工作流
- [integration-guide.md](integration-guide.md) — 接入新 Agent / 新产出去向
