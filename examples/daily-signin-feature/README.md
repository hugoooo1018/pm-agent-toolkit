# 端到端示例：每日签到功能 PRD

本示例演示从**一句话需求**到**可交付 PRD**的完整工作流。5 个文件按顺序阅读，5 分钟能懂整个 toolkit 的输出形态。

## 阅读顺序

| # | 文件 | 内容 | 对应工作流环节 |
|---|---|---|---|
| 00 | [brief.md](00-brief.md) | 用户原始一句话输入 | 输入 |
| 01 | [clarification.md](01-clarification.md) | 2 轮澄清对话 + 需求理解总结 | `rules/prd-clarification.md` |
| 02 | [prd-v0.1.md](02-prd-v0.1.md) | 按 10 章骨架生成的初版 PRD | `rules/prd-paradigm.md` + `templates/default-style/` |
| 03 | [review-report.md](03-review-report.md) | 独立评审报告（8 个 finding） | `skills/prd-review/` |
| 04 | [prd-final.md](04-prd-final.md) | 修完问题的终版 PRD | 作者修复后 |

## 涵盖的原则演示

| 原则 | 演示位置 |
|---|---|
| P1 三层指标 + 四要素 | 02/04 第六章 |
| P2 INVEST | 02/04 第三章 |
| P3 Gherkin 三场景覆盖 | 02/04 第七章 |
| P4 追溯矩阵 | 02/04 第九章 |
| P5 SOT 对齐（降级模式） | 03 finding F6.1 + 04 第六章 |
| P6 禁用技术术语 | 04 全文（用"签到记录"而非"表/字段 ID"） |
| P7 按模块拆解 | 02/04 第四章（4 模块） |
| P9 字段表 4 列 | 04 第六章 |
| 6 维度质量判据 | 03 评审报告逐维度扫描 |

## 不涵盖的

本示例选的是**功能级 PRD（10 章）**，没演示模块级 7 章骨架。模块级的例子可参考 `templates/default-style/module-prd-7-chapter.md` 的骨架本身。

## 可复用性

这份 PRD 的结构、修改流程、各环节的输出形态，可作为其他 PRD 工作的模板。换需求/换领域时：

- 保留流程（clarification → paradigm → review → self-check）
- 保留结构（10 章骨架 + 追溯矩阵 + 指标四要素）
- 改具体内容

## 如何用 Claude Code 复现

```bash
cd pm-agent-toolkit
claude
```

然后：

```
我想做一个 <你的功能> 功能让用户 <目标>。
```

Claude 会按照本仓库的 rules 引导你走一遍 clarification → paradigm → review，产出类似本示例的完整 PRD。
