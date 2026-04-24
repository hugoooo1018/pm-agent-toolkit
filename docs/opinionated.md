# Opinionated 声明

本仓库是**有立场的**工具包。本文档坦诚说明哪些部分是通用的、哪些是某家公司的风味、如何按你的团队改写。

## 什么是通用的

这些内容基于业界共识，放之任何 PM 团队皆适用：

- **三层指标体系**（北极星 / 输入 / 护栏）— 源自 Amplitude、Intercom 等公司实践
- **INVEST 用户故事原则** — 敏捷社区共识
- **Given-When-Then 验收标准（Gherkin）** — BDD 行业标准
- **追溯矩阵**（问题 → Outcome → 功能 → AC → 指标）— 通用需求工程方法
- **SOT（业务对象）机械对齐** — DDD / 领域建模的自然要求
- **PRD 写业务意图不写技术实现** — PRD-vs-tech-spec 的常识

这些内容在 `rules/prd-writer.md` 和 `rules/prd-quality-checklist.md` 里，基本可以放之四海。

## 什么是"logic-labs 风味"

以下是基于 logic-labs 一线实践的具体选择，带有公司偏好：

### 1. PRD 骨架

- **7 章模块级骨架**（`templates/logic-labs-style/module-prd-7-chapter.md`）— 章节编号、顺序、命名都是公司约定
- **10 章功能级骨架** — 包含"追溯矩阵"等公司约定的章节

**其他公司可能偏好的风格**：

- Amazon：PR-FAQ（Press Release + FAQ）
- Intercom：RFC-style（Request For Comments）
- Atlassian：One-pager PRD
- Google：Design Doc with Tenets

### 2. L2 功能三形态

把所有功能切成"操作型 / 页面型 / 执行型"三类，各有固定模板。这是 logic-labs 的分类。

**其他公司可能切法**：

- 按用户旅程切（Discovery / Activation / Retention）
- 按 CRUD 切（Create / Read / Update / Delete）
- 按事件切（Event-driven pattern）

### 3. 写作硬规则

- "约束与边界" 只能装"业务边界"和"数据影响"两类
- 核心业务术语全文加粗且每次出现形式完全一致
- 字段表固定 4 列（字段 / 必填 / 校验规则 / 校验失败提示）
- 优先级只出现 P0/P1，P2 塞第七章未来规划
- 列表组件必须给"空状态"

这些是 logic-labs 在多次事故后沉淀的红线，不一定适合你的团队。

### 4. 术语直引

- Mermaid 节点文字必须等于正文术语
- 字段命名遵循 `field-naming.md` 规范
- 中英文对照用 `**中文（English）**` 形式

这些是文档一致性要求，公司通常会有自己的约定。

## 如何按你的团队改写

### 轻改（保留框架，换内容）

改 `templates/logic-labs-style/` 下的骨架即可：

```bash
# 复制一份作为起点
cp -R templates/logic-labs-style templates/your-company-style

# 改骨架、改章节命名、改字段表列数
```

然后在 `rules/prd-paradigm.md` 和 `rules/prd-writer.md` 里更新指引：引用你的新模板风格，或两者并存供选择。

### 中改（换范式）

如果你要从"模块级 7 章"改成"Amazon PR-FAQ"：

1. 新建 `templates/amazon-pr-faq/` 放 PR-FAQ 骨架
2. 改写或新增 `rules/prd-paradigm.md` 解释 PR-FAQ 的写法（what / who / why / how）
3. `CLAUDE.md` 的 Rules 清单增加你的范式 Rule

### 大改（换理论基础）

INVEST / Gherkin / 追溯矩阵是本仓库的理论基石。如果你的团队不用这些：

1. 改 `rules/prd-writer.md` 的 P1–P11 原则
2. 改 `rules/prd-quality-checklist.md` 的 6 维度判据
3. 记得同步 `CHANGELOG.md` 和自测

### 不改的部分

- `rules/prd-clarification.md` 的 5 维度澄清框架（很通用）
- 三层指标体系（已经是业界最大公约数）
- Git 分支、PR 规范、CI lint 脚本

## 为什么不做多风格模板共存

本仓库首版只给 `logic-labs-style` 一份模板。理由：

- **认知成本**：给 3 种风格反而让 PM 选择困难
- **维护成本**：每个风格都要配完整的 rule + template + example
- **社区共创更好**：欢迎 fork 加你的风格并 PR，大家一起扩展

## 我们不是唯一标准

本仓库的 opinionation 来自一家公司的实践。它可能不适合你。有几种你可以做的选择：

1. **不认同** → fork 后全改
2. **部分认同** → 保留 rules/ 的原则层，改 templates/ 的具体骨架
3. **完全认同** → 直接用

三种都 OK。

---

## 本文档的维护

当你添加或修改了公司特有的规则/模板/风格，请同步更新本文档，让下一个贡献者知道"哪些可改 / 哪些别碰"。
