# PRD 生命周期状态

PRD 不是"写完就结束"的文件，而是一个活的资产。本文件定义它的 6 个状态和转换规则。

## 状态一览

```
Draft ──▶ In Review ──▶ Approved ──▶ In Development ──▶ Shipped ──▶ Deprecated
                │           │                │              │
                └─→ Draft   └─→ Draft        └─→ Draft      │
                                                            └─→ Deprecated
```

| 状态 | 中文 | 含义 | 主要动作 |
|---|---|---|---|
| `Draft` | 草稿 | 作者正在写或改 | 自由编辑 |
| `In Review` | 评审中 | 已发给 reviewer，等反馈 | 接收评论，不改正文 |
| `Approved` | 已批准 | 所有关键 reviewer 签过 | 冻结正文 |
| `In Development` | 开发中 | 研发已接手 | 跟踪进度，重大变更走 Amendment |
| `Shipped` | 已上线 | 功能已发布 | 写上线小结，对比指标 |
| `Deprecated` | 已废弃 | 功能下线或被替代 | 标注废弃原因 |

## 状态定义细则

### Draft（草稿）

- **谁可进入**：作者自己
- **可见范围**：仅作者 + 可选的早期咨询对象
- **可改内容**：全文任何部分
- **进入条件**：新建 PRD，或从 In Review 打回
- **离开条件**：作者主动发起评审

### In Review（评审中）

- **谁可进入**：作者主动发起
- **可见范围**：指定的 reviewer + 业务关键干系人
- **可改内容**：只允许修复明显拼写错误，结构/内容改动需退回 Draft
- **进入条件**：所有 Draft 阶段 TODO 已补、自检报告 pass（或至少 risk-only）
- **离开条件**：
  - → Approved：所有必签 reviewer 签过
  - → Draft：收到重大反馈需要重写

### Approved（已批准）

- **谁可进入**：必签 reviewer 全部同意
- **可见范围**：全组或更大范围
- **可改内容**：**不可改**。需改动走 Amendment 流程（见下方）
- **进入条件**：
  - 自检 pass
  - 独立评审通过
  - 必签人签字（产品负责人 / 技术负责人 / 设计负责人，视公司而定）
- **离开条件**：
  - → In Development：研发 kickoff
  - → Draft：Amendment 触发

### In Development（开发中）

- **谁可进入**：研发 kickoff 会议后
- **可见范围**：全体协作方
- **可改内容**：**不可改**。所有变更走 Amendment
- **进入条件**：研发排入 sprint
- **离开条件**：
  - → Shipped：功能上线
  - → Deprecated：项目取消

### Shipped（已上线）

- **谁可进入**：功能发布后
- **可见范围**：全员可查阅
- **可改内容**：只允许追加**上线小结**章节（第 11 章或 Appendix）
- **进入条件**：功能已在生产环境启用
- **上线小结至少含**：
  - 实际上线时间
  - 北极星指标与目标对比（几周后回填）
  - 上线过程遇到的问题
  - 下一步优化建议
- **离开条件**：
  - → Deprecated：功能下线 / 被替代

### Deprecated（已废弃）

- **谁可进入**：产品/技术团队决策
- **可见范围**：归档可查
- **可改内容**：不可改
- **进入条件**：
  - 功能已下线
  - 被其他 PRD 替代
  - 长期不维护（一般 6-12 个月）
- **标注要求**：
  - 顶部加 "⚠️ DEPRECATED — <原因>" 横幅
  - 链接替代者（如有）
- **离开条件**：无（终态）

## Amendment 流程（Approved 后的变更）

Approved / In Development 阶段需要改动 PRD 时：

1. **不直接改 PRD**
2. 在 PRD 末尾追加一节 `## Amendment <序号>`：
   ```markdown
   ## Amendment 1 — 2026-05-15

   **变更原因**：{为什么需要改}

   **原文**：{原章节引用 + 原文字}

   **改为**：{新文字}

   **影响评估**：{指标 / 研发工期 / 其他模块}

   **签批**：{再次签批的 reviewer}
   ```
3. 必要时将状态临时转回 Draft 以做全文级调整，改完再重新评审

这套 Amendment 机制保留历史变更可追溯，避免"谁改的不知道"。

## 状态转换触发器

| 触发场景 | 状态变化 |
|---|---|
| 作者新建 PRD | → Draft |
| 作者自检 pass，发给 reviewer | Draft → In Review |
| Reviewer 提出重大修改 | In Review → Draft |
| 所有必签人同意 | In Review → Approved |
| 研发 kickoff | Approved → In Development |
| Approved/InDev 阶段重大需求变更 | In Development → Draft（带 Amendment） |
| 功能生产上线 | In Development → Shipped |
| 功能下线或被替代 | Shipped → Deprecated |

## 在文档里怎么标状态

推荐在 PRD 顶部 frontmatter（或第一行）显式标注：

```markdown
---
prd_status: In Development
prd_version: 1.2
last_updated: 2026-05-01
owner: @xiuqi
reviewers:
  - @alice (Product)
  - @bob (Tech)
  - @carol (Design)
---
```

Agent 在读取 PRD 时可据此调整行为（Draft 可建议大改，Approved 只建议 Amendment）。

## 不做的事

- **不做状态自动化**：当前版本不做基于 git 状态 / CI / ticket 系统的自动转换
- **不做工作流 enforcement**：状态定义是约定，不是硬性 gate
- **不对接 JIRA/Linear 的工单状态**：那是 MCP 生态的事

未来若要加自动化，可扩展为：
- 用飞书文档的审批流对接 In Review → Approved
- 用 git tag 打 `prd-shipped-<feature>` 对接 Shipped
- 用 Docusaurus version 对接 Amendment

这些都超出 v0.2 范围。
