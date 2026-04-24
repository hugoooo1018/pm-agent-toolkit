# 术语表

本仓库高频出现的专业术语，初次接触的读者可先读这里。

## 指标类

### 北极星指标（North Star Metric）

一个产品 / 功能成功要撬动的**唯一核心指标**。它同时反映用户获得的价值和业务的增长。好的北极星有"唯一、可量化、长期、领先"四个特征。

- 反例："提升活跃度"（不可量化）、"本季度发 5 个功能"（是输出不是结果）
- 正例："每周活跃广告主下单率"、"30 天留存"

### 输入指标（Input Metrics）

**直接受当前功能影响**、**能先行反映效果**的行为指标。北极星一般滞后，输入指标实时。

- 典型：注册完成率、首次使用时长、某个操作的完成率
- 数量：2–4 个

### 护栏指标（Guardrail Metrics）

防止为了优化北极星而**牺牲其他体验**的底线指标。护栏一旦恶化，即使北极星涨了也要停。

- 典型：P95 延迟、客诉率、错误率、NPS
- 数量：1–3 个

### 四要素

每个指标必须绑定：**基线值 / 目标值 / 测量周期 / 数据源**。缺任一视为失效指标。

## 用户故事类

### INVEST

用户故事质量的六项自检：

- **I**ndependent — 可独立交付
- **N**egotiable — 描述诉求而非实现
- **V**aluable — 对用户或业务有可辨识价值
- **E**stimable — 研发可估工期
- **S**mall — 颗粒度足够小（一个 sprint 可完成）
- **T**estable — 有可客观判断的验收条件

### Gherkin / Given-When-Then

验收标准（AC）的标准写法，源自 BDD（行为驱动开发）：

```
Given  <前置条件>
When   <用户动作>
Then   <期望结果>
```

每条 AC 必须覆盖三类场景：**Happy Path**（正常）、**Edge Case**（边界）、**Error Path**（异常）。

## 需求工程类

### SOT — Single Source of Truth

"唯一真源"。本仓库特指业务对象文档（通常文件名形如 `*-business-objects.md`），它定义了领域实体的字段、数据类型、约束条件，是所有 PRD 必须机械对齐的权威。

### 追溯矩阵（Traceability Matrix）

PRD 末尾的一张表，每行串联：**问题 → Outcome → 功能点 → 验收标准 → 指标**。用于验证"每个需求都有因、有果、可度量"。

### Outcome

功能成功后**用户 / 业务会发生的可观测改变**。区别于"输出"（Output，我们做了什么）。

- Output 反例："我们做了一个签到功能"
- Outcome 正例："新用户次周留存率从 22% 提升到 28%"

## PRD 结构类

### L1 / L2 / L3（本仓库约定）

模块级 PRD 的三层结构：

- **L1 模块** — 顶层业务域（如"规则管理"）
- **L2 功能** — 模块内的操作或页面
- **L3 字段 / 属性细节** — 每个字段的名称、必填、校验

### L2 三形态（本仓库约定）

所有 L2 功能被归为三类：

- **操作型** — 创建 / 编辑 / 删除 / 搜索 / 状态切换
- **页面型** — 列表页 / 详情页 / 仪表盘
- **执行型** — 手动执行 / 批处理 / 循环任务

### 约束与边界

本仓库 PRD 的专用章节，**只装两类内容**：

- 业务边界（这个功能的业务影响范围）
- 数据影响（数据层面会发生什么）

其他常见内容（前置条件 / 交互规则 / 外部依赖 / 容错规则 / MVP 不做项）应去各自归属位置，详见 `rules/prd-paradigm.md`。

## 流程类

### 生命周期状态

PRD 的状态机，详见 `lifecycle/states.md`：

- Draft（草稿）
- In Review（评审中）
- Approved（已批准）
- In Development（开发中）
- Shipped（已上线）
- Deprecated（已废弃）

### opinionated

有明确立场 / 偏好的设计。与 "unopinionated"（无偏好，完全灵活）相对。本仓库的范式部分是 opinionated 的，原则部分是 unopinionated 的。详见 `docs/opinionated.md`。

## Agent 生态类

### Agent-neutral

与具体 Agent 框架无关。本仓库的 `rules/` 层是 agent-neutral 的——可被 Claude Code / Cursor / Windsurf / 自建 Agent 等任意生态消费。

### 绑定层（Binding Layer）

把 agent-neutral 的知识翻译成特定 Agent 能消费格式的那层代码 / 文件。本仓库的 `skills/`（给 Claude Code）和 `adapters/`（给其他 Agent）都是绑定层。

### 集成层（Integration Layer）

产出（Markdown PRD）送达真实工具（飞书文档 / Confluence 等）的那层。本仓库首版仅含 `integrations/lark/`。

---

## 术语补充

看到本仓库里有术语没列出、或列出但解释不清，欢迎 PR 补充本文件。
