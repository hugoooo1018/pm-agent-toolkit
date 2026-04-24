# Design system

Wireframe 的视觉规范 + 可复用组件清单。生成 HTML 时用这里的 class，**不自造新名字**。

## 核心原则

> **灰度深浅 = 被动展示 → 主动交互；C/D 跳出灰块系统。**

## 4 大组件类别

### A. 只读（展示数据）

用于展示数据，用户不可交互。以浅-中灰体系为主；其中**表头列名为纯文字样式**（透明底，不使用实心灰块）。

```html
<div class="wf-text long">品牌 URL</div>
<div class="wf-text medium">Meta 广告账户 ID</div>
<div class="wf-text short">商品数量</div>
<div class="wf-text heading">广告主名称</div>
<div class="wf-box">产品截图 / 主视觉图</div>
```

| Class | 颜色 | 用途 |
|---|---|---|
| `.wf-text`（`.short` 40% / `.medium` 70% / `.long` 100%） | `#d0d0d0` 浅灰 | 字段值占位 |
| `.wf-text.heading` | `#999` 中灰（60% 宽，大字号） | 页面主字段 |
| `.wf-box` | `#e8e8e8` 虚线边 | 图片/图表占位 |
| 表格表头文字 `.wf-table-header-row` 内的 `.wf-text` | 透明底 + `#444` 加粗文字 | 列名（仅文字，不使用实心灰块） |

**挑宽度**：字段名短（ID、时间、数量）→ short；中（Meta 广告账户 ID）→ medium；URL/长值 → long；页面主字段 → heading。

### B. 交互

用户可点/输入。统一深灰 `#7a7a7a`；危险动作 `#a06060`。**不分子类**——按钮、link 字段、输入框都在这一类。

```html
<!-- link-style 字段（字段值本身可点） -->
<div class="brand-name">品牌名称 1</div>

<!-- 按钮 -->
<button class="btn">新增品牌</button>             <!-- 主动作 -->
<button class="btn outline">编辑</button>         <!-- 次动作 -->
<button class="btn small">新增广告账户</button>   <!-- small 变体 -->
<button class="btn outline small">前往 Meta ↗</button>  <!-- 外链 -->
<button class="btn btn-danger">删除</button>      <!-- 危险 -->

<!-- 输入框 -->
<div class="wf-text long form-input">品牌名称输入框</div>
```

| Class | 颜色 | 用途 |
|---|---|---|
| `.brand-name` | `#7a7a7a` 实底白字 | link 字段（现仅视觉，不再挂交互标记） |
| `.btn` | `#7a7a7a` 实底白字 | 主动作 |
| `.btn.outline` | 透明 + `#7a7a7a` 虚线边 | 次动作 |
| `.btn.btn-danger` | `#a06060` 实底白字 | 危险动作（删除等） |
| `.btn.small` | 缩小的 padding/字号 | size 变体 |
| `.wf-text.form-input` | `#e8e8e8` + 虚线边 | 输入框占位（派生自 `.wf-text`） |

**外链按钮末尾加** `↗`。**按钮顺序**：弹窗里取消（outline）在左，主动作（实心）在右。

### C. 静态 UI 文案（硬编码标签）

页面会渲染，但不是数据也不是交互元素本体。**不用灰块**，普通文字。

```html
<div class="modal-title">新增品牌</div>
<div class="form-label">品牌名称 *</div>
```

| Class | 颜色 | 用途 |
|---|---|---|
| `.modal-title` | `#333` 加粗 | 弹窗标题 |
| `.form-label` | `#555` 普通字 | 表单字段左侧 label |

必填字段的 `.form-label` 末尾加 ` *`（半角空格+星号）。

### D. 不展示（文档元信息）

前端真 UI 不渲染，仅给文档读者/后端看。**最浅灰 + 虚线 + 斜体**，与 A/B/C 彻底区分。

```html
<section class="list-column section">
  <span class="label">板块：品牌列表</span>
  <!-- 区域内容 -->
</section>
```

| Class | 颜色 | 用途 |
|---|---|---|
| `.label` | `#f3f3f3` 虚线斜体 | 板块注释，文案固定前缀"板块：" |

---

## 色谱（从浅到深）

```
#f3f3f3  D  .label (板块注释，虚线+斜体)
#e8e8e8  A  .wf-box / B .form-input （虚线边）
#d0d0d0  A  .wf-text (常规字段)
#eee     A  `.wf-table-header-row`（表头行容器底色）
#999     A  .wf-text.heading (主字段)
#7a7a7a  B  .brand-name / .btn / .btn.outline 边框
#a06060  B  .btn.btn-danger
```

**字段文字颜色**随底色：浅底 `#555` / 中底 `#333` / 深底 `#fff`；表头文字统一 `#444`。

---

## 分类 4 步法（给新组件归类）

1. 文档元信息、前端不渲染 → **D**
2. 硬编码 UI 标签、没数据字段 → **C**
3. 用户能点/输入/触发 → **B**
4. 其它 → **A**

---

## 容器 / 布局组件

以下 class 是**布局**，不直接属于 A/B/C/D（它们不表达数据，只搭骨架）：

| Class | 用途 |
|---|---|
| `.container` | 外层容器，max-width 1100px |
| `.section` | `position: relative`，给 `.label` 提供定位上下文 |
| `.main-grid` | 两列布局（1fr 1fr） |
| `.list-column` / `.item-card` / `.account-card` | 列表页卡片容器 |
| `.info-card` / `.table-section` / `.wf-table` / `.wf-table-row` | 详情页信息卡 + 表格 |
| `.modal-overlay` / `.modal-dialog` / `.modal-confirm` / `.form-row` | 弹窗框架 |
| `.search-group` | 搜索框 + 搜索按钮的紧凑视觉组 |
| `.empty-state` | 列表空态 |
| `.breadcrumb` | 面包屑 |

各组件的具体结构见 `page-patterns.md`。

---

## 间距 / 字号 / 边框

| 属性 | 值 |
|---|---|
| 容器 padding | `32px` |
| 分区 padding | `32px 24px 24px`（顶部留给 `.label`） |
| 卡片 padding | `14px 16px` |
| 字段块 padding | `4px 10px`（常规）/ `6px 12px`（heading） |
| 卡片之间 gap | `12px` |
| 分区之间 margin | `16px`-`24px` |
| 容器边 | `1px solid #ccc` |
| 分区/信息卡 边 | `1px dashed #aaa` |
| 卡片 边 | `1px dashed #bbb` |
| 字段块圆角 | `2px` |
| 卡片圆角 | `3px` |
| 容器/分区圆角 | `4px` |
| `.wf-text` 字号 | 12px（heading 14px、brand-name 13px） |
| `.btn` 字号 | 12px（small 11px） |
| `.label` 字号 | 10px |

## 响应式

`@media (max-width: 768px)`：两列转单列、表单行纵向堆叠、account-card 纵向布局。具体规则在 `_wireframe.css` 里。
