---
lang: zh
skill: prd-review
examples:
  - { id: dim1-ex1, dimension: 1, title: "UI 细节漏进字段表" }
  - { id: dim1-ex2, dimension: 1, title: "跨模块业务规则混入属性列表" }
  - { id: dim1-ex3, dimension: 1, title: "原型图章节承担业务规则说明" }
  - { id: dim2-ex1, dimension: 2, title: "校验、输出、约束混在一串 bullet" }
  - { id: dim2-ex2, dimension: 2, title: "同类章节结构不一致" }
  - { id: dim3-ex1, dimension: 3, title: "同实体字段在不同视图顺序不一" }
  - { id: dim3-ex2, dimension: 3, title: "同类页面 UI 控件顺序不一" }
  - { id: dim4-ex1, dimension: 4, title: "技术术语软删除无业务解释" }
  - { id: dim4-ex2, dimension: 4, title: "匹配语义模糊" }
  - { id: dim4-ex3, dimension: 4, title: "主观判断词" }
  - { id: dim4-ex4, dimension: 4, title: "自动同步未定义时机" }
  - { id: dim5-ex1, dimension: 5, title: "行为描述与业务规则矛盾" }
  - { id: dim5-ex2, dimension: 5, title: "原型有页面但功能详述未覆盖" }
  - { id: dim5-ex3, dimension: 5, title: "同一指标两处公式不同" }
  - { id: dim5-ex4, dimension: 5, title: "全局规则在多处重复" }
  - { id: dim6-ex1, dimension: 6, title: "PRD 自创字段别名" }
  - { id: dim6-ex2, dimension: 6, title: "PRD 引用了 business-objects 未定义的字段" }
  - { id: dim6-ex3, dimension: 6, title: "类型或必填性静默不同" }
---

# 反面例子 — 违反 checklist 的模式

此文件为 `prd-review` skill 提供一个"可识别的形状"库——清晰违反某个维度的片段。Stage 1 遇到候选问题不确定时，跳到对应维度小节，对照 Detection cue 判断。

每条例子包含三个机器可用字段：
- **Input** — 逐字引用一段应被标出的 PRD 文本
- **Detection cue** — 识别此模式的信号
- **Violates** — 违反了 checklist 哪一条
- **Positive rewrite** — 同内容的"好"写法应该是什么样

例子来源：(A) `docs/business/PRD_Check_List.md` 中的「具体表现形式」bullet，部分逐字引用；(B) 按项目 `docs/business/rule/` 和 `docs/business/customer/` 下真实 PRD 的表达形态再造——在本代码库扫真实 PRD 时会遇到形态非常相似的文字，但不一定是逐字引用。

## Table of Contents

- [维度 1 — 内容失焦](#维度-1--内容失焦)
- [维度 2 — 结构组织](#维度-2--结构组织)
- [维度 3 — 顺序一致性](#维度-3--顺序一致性)
- [维度 4 — 歧义表述](#维度-4--歧义表述)
- [维度 5 — 前后自洽](#维度-5--前后自洽)
- [维度 6 — 字段对齐](#维度-6--字段对齐)

---

## 维度 1 — 内容失焦

### Example 1 — UI 细节漏进字段表

**Input:**
> | 字段 | 说明 |
> |---|---|
> | Rule 名称 | 必填，**只读胶囊标签，hover 态出现删除图标** |

**Detection cue:**
- 出现在"字段定义""属性表"章节内
- 含 UI 呈现词汇：胶囊、chip、hover、icon、tooltip、badge、toast、modal、红点

**Violates:** 维度 1 ①——UI 呈现混入对象说明

**Positive rewrite:**
字段表只保留业务属性（必填、校验、错误提示）。UI 细节移到「原型图说明」章节。

### Example 2 — 跨模块业务规则混入属性列表

**Input:**
> Rule 属性：
> - name：字符串，必填
> - strategy_list：该 Rule 下的 Strategy 列表；**按创建时间升序评估，命中即停**

**Detection cue:**
- 出现在属性列表或属性 bullet 里
- 句子描述的是行为 / 评估顺序，不是数据结构

**Violates:** 维度 1 ②——业务规则混入属性列表

**Positive rewrite:**
属性列表只写："strategy_list：该 Rule 下的 Strategy 列表"。评估顺序放到「业务规则」章节。

### Example 3 — 原型图章节承担业务规则说明

**Input（Rule 列表页原型下方）:**
> 列表下方备注："一旦该 Rule 下某个 Strategy 命中，即停止评估，不再检查其他 Strategy。"

**Detection cue:**
- 文本出现在原型图截图说明 / "原型图"章节下
- 内容描述的是业务策略，不是 UI 展示

**Violates:** 维度 1 ②——原型图章节反向承担业务规则说明

**Positive rewrite:**
把这条规则移到「业务规则」章节。原型图说明只描述用户看到什么。

---

## 维度 2 — 结构组织

### Example 1 — 校验、输出、约束混在一串 bullet

**Input:**
> 创建 Rule：
> - 手机号必填
> - 成功后跳转详情页
> - 邮箱必须是合法格式
> - Rule 名称在同一 Strategy 下唯一
> - 失败则停留在表单并显示错误

**Detection cue:**
- 一条扁平 bullet 列表
- 输入校验、提交结果、业务约束平铺，未按类型分组

**Violates:** 维度 2 ①——信息平铺堆放，未按类型或层次分组

**Positive rewrite:**
拆成字段表（按字段写校验）、「成功后」块、「失败后」块——遵循 [PRD Writer Rule](../../../rules/prd-writer.md) P8/P9 的操作类功能模板。

### Example 2 — 同类章节结构不一致

**Input**：同一 PRD 下两个并列章节：
> **创建表单**：（散文描述交互）字段：name、owner、created_at。
>
> **编辑表单**：字段列表：name、created_at、owner。然后散文描述交互。

**Detection cue:**
- 同类章节（创建 vs 编辑、列表 vs 详情）内容顺序或格式不同
- 读者要反复切换才能对比

**Violates:** 维度 2 ②——同类章节使用不一致的结构模板

**Positive rewrite:**
两个表单都遵循：触发 → 自动填充 → 字段表 → 成功后 → 失败后。字段顺序两处保持一致。

---

## 维度 3 — 顺序一致性

### Example 1 — 同实体字段在不同视图顺序不一

**Input:**
> Rule 列表页列："**名称 / 状态 / 创建人 / 创建时间**"
> Rule 详情页分块："**名称 / 创建时间 / 状态 / 创建人**"

**Detection cue:**
- 同一实体（Rule），两个视图（列表、详情）
- 字段顺序无理由地不同

**Violates:** 维度 3 ②——字段在同一实体的不同视图顺序不一

**Positive rewrite:**
选定一个基准顺序（业务主流程顺序：名称 → 状态 → 创建人 → 创建时间），全局使用。

### Example 2 — 同类页面 UI 控件顺序不一

**Input:**
> Rule 列表：筛选器 = 状态、创建人、创建时间。操作按钮 = 编辑、停用、删除。
> Strategy 列表：筛选器 = 创建时间、状态、创建人。操作按钮 = 停用、编辑、删除。

**Detection cue:**
- 两个同类列表页
- 筛选器或操作按钮顺序不同

**Violates:** 维度 3 ③——UI 控件在同类页面顺序不一

**Positive rewrite:**
两页共享：筛选器 = 状态 → 创建人 → 创建时间；操作按钮 = 编辑 → 停用 → 删除。

---

## 维度 4 — 歧义表述

### Example 1 — 技术术语"软删除"无业务解释

**Input:**
> 停用 Rule 采用**软删除**。

**Detection cue:**
- 业务侧 PRD 出现"软删除 / 硬删除 / 级联删除 / tombstone"等词
- 无括号说明数据是否保留、能否恢复、是否可见

**Violates:** 维度 4 ①——技术术语泄露到业务描述中

**应当追问：**
- 停用后，Rule 在列表里还能看到吗？还能编辑吗？能恢复吗？
- 历史引用这条 Rule 的数据是否保留？
- 停用状态保留多久？

**Positive rewrite（澄清后）:**
"停用 Rule 后，它从当前列表中隐藏，但可在「已停用」标签下查询 90 天。历史评估引用此 Rule 的数据不变。停用 90 天内可重新启用，之后永久删除。"

### Example 2 — 匹配语义模糊

**Input:**
> 支持 Rule 名称的**模糊搜索**。

**Detection cue:**
- 单独出现"模糊搜索 / partial match / 模糊匹配"
- 未说明是前缀、包含、分词还是拼音

**Violates:** 维度 4 ②——业务术语表述模糊（匹配方式未定义）

**应当追问：**
- 前缀匹配、子串包含、分词匹配，还是拼音模糊？
- 是否区分大小写？
- 返回条数上限？

**Positive rewrite:**
"对 Rule 名称做前缀匹配，不区分大小写，最多返回 50 条。"

### Example 3 — 主观判断词

**Input:**
> Rule 详情页显示**相关**的 Strategy。

**Detection cue:**
- 主观词：相关 / 类似 / 合适 / 及时 / 合理
- 无可判定的测试标准

**Violates:** 维度 4 ②——使用主观判断词

**应当追问：**
- "相关"的关系怎么定义？同 owner？同标签？通过外键关联？
- 最多显示几条？
- 排序规则？

**Positive rewrite:**
"显示最多 5 条直接引用此 Rule 的 Strategy，按最近活跃时间降序排列。"

### Example 4 — "自动同步"未定义时机

**Input:**
> Meta 广告账户数据**自动同步**自 Meta API。

**Detection cue:**
- "自动同步 / 实时 / 及时更新" 等词，无时机、频率、冲突处理

**Violates:** 维度 4 ②——时机或频率未定义

**应当追问：**
- 定时拉（多久一次）？事件驱动？手动触发？
- API 失败或返回冲突时如何处理？
- 可接受的滞后时间？

**Positive rewrite:**
"Meta 广告账户数据每 30 分钟轮询一次。Meta API 返回错误时，保留上一次成功的快照，并在记录上标注「Stale since [时间戳]」。下一次成功拉取后清除该标记。"

---

## 维度 5 — 前后自洽

### Example 1 — 行为描述与业务规则矛盾

**Input:**
> 流程："某 Strategy 命中后，继续评估下一条 Rule。"
> 业务规则表："仅执行 Strategy 命中的那一条 Rule，不再评估其他 Rule。"

**Detection cue:**
- 两个章节对同一行为描述出相反结果

**Violates:** 维度 5 ①——行为描述与业务规则矛盾

**处理方式：** 问哪个是对的，另一个对齐。

### Example 2 — 原型有页面但功能详述未覆盖

**Input:**
- 原型图册里有 "Rule 详情页"
- 功能列表里没有 "查看 Rule 详情" 这项

**Detection cue:**
- 一张原型图没有对应功能点（或反之）

**Violates:** 维度 5 ②——原型图与功能详述无强映射关系

**处理方式：** 要么补上功能点，要么删除孤立原型页。

### Example 3 — 同一指标两处公式不同

**Input:**
> 业务规则："Rule 命中率 = 命中次数 / 评估次数"
> 数据口径："Rule 命中率 = 命中次数 / (评估次数 - 跳过次数)"

**Detection cue:**
- 同一指标名，两处分母 / 公式不同

**Violates:** 维度 5 ④——数据口径前后不一致

**处理方式：** 选定一个唯一真源，全文引用。

### Example 4 — 全局规则在多处重复

**Input（三个不同功能章节各写一遍）:**
> "任何列表页的删除操作需要二次确认弹窗。"

**Detection cue:**
- 同一规则在多个功能标题下逐字或近逐字重复
- 没有指向某个唯一定义位置

**Violates:** 维度 5 ⑤——全局规则在多处重复展开

**处理方式：** 在业务规则章节定义一次；每个使用它的功能写 "详见业务规则 §X"。

---

## 维度 6 — 字段对齐

### Example 1 — PRD 自创字段别名

**Input:**
> `customer-business-objects.md` 定义：**品牌名称**
> PRD 写："Brand Name 字段必填。"

**Detection cue:**
- PRD 文本用的词（中英文变体、casing 改动、别名）与同域 `*-business-objects.md` 的权威名字不完全一致

**Violates:** 维度 6——字段名偏离 business-objects 真源

**处理方式：** PRD 中用完全一致的权威名字。若真想换名字，先改 business-objects 文档。

### Example 2 — PRD 引用了 business-objects 未定义的字段

**Input:**
> PRD 写："Rule 支持 `priority` 属性（1–100）。"
> `rule-business-objects.md` 未提及 priority。

**Detection cue:**
- PRD 出现的字段在 business-objects 里无定义
- 没有同步更新 business-objects

**Violates:** 维度 6——PRD 与 business-objects 不同步

**处理方式：** 要么先把 `priority` 加到 business-objects，要么从 PRD 里删掉。

### Example 3 — 类型或必填性静默不同

**Input:**
> `rule-business-objects.md`：`rule_name` 是 string、必填、最长 50 字符。
> PRD 功能："Rule 名称：可选，无长度限制。"

**Detection cue:**
- 同字段名两处都出现
- 必填 / 类型 / 长度 / 格式无注释地不同

**Violates:** 维度 6——约束漂移

**处理方式：** 权威源（business-objects）为准；更新 PRD；若要改 business-objects 需写明理由。
