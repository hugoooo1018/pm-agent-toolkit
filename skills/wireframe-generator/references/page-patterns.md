# Page patterns

常见页面的结构骨架。**不是死板模板**——PRD 是兜底，若 PRD 描述和 pattern 不一致，以 PRD 为准。

## 列表页

```
<container>
  <section class="advertiser-card section">
    <span class="label">板块：广告主信息</span>
    <div class="wf-text heading">主对象名称</div>
  </section>

  <div class="main-grid">
    <section class="list-column section">
      <span class="label">板块：左列名</span>
      <div class="column-header">
        <button class="btn small">新增 X</button>
      </div>
      <div class="card-list">
        <!-- item-card × 3-5 -->
      </div>
    </section>

    <section class="list-column section">
      <span class="label">板块：右列名</span>
      <div class="column-header">
        <button class="btn small">新增 Y</button>
      </div>
      <div class="card-list">
        <!-- account-card × 3-5 -->
      </div>
    </section>
  </div>
</container>
```

**约定**：
- 卡片数量按 PRD；PRD 未指定时 3-5 之间
- 可点击字段用 `.brand-name`（B 类深灰），点击行为由 PRD 说明
- 外链按钮文字加 `↗`（如"前往 Meta ↗"）

## 详情页

```
<container>
  <section class="breadcrumb section">
    <span class="label">板块：面包屑</span>
    <div class="wf-text medium">返回 X / 当前对象名</div>
  </section>

  <section class="info-card section">
    <span class="label">板块：对象信息</span>
    <div class="info-card-actions">
      <button class="btn outline small">编辑</button>
    </div>
    <div class="wf-text heading">对象主字段</div>
    <div class="wf-text long">字段 URL</div>
    <div class="wf-text short">统计字段</div>
  </section>

  <section class="table-section section">
    <span class="label">板块：子列表</span>
    <div class="table-header">
      <div class="search-group">
        <div class="wf-text long search-box">搜索框</div>
        <button class="btn outline small">搜索</button>
      </div>
      <button class="btn small">新增子项</button>
    </div>
    <div class="wf-table">
      <div class="wf-table-row wf-table-header-row">
        <!-- 表头列 -->
      </div>
      <!-- 数据行 × 3-5 -->
    </div>
  </section>
</container>
```

**约定**：
- 搜索框占位文字按 PRD 自由描述（如"搜索框"、"按商品名称/编号搜索"）
- MVP 不分页 → 数据行直接占位即可
- 操作列固定 120px（`grid-template-columns` 最后一列）；表头为纯文字样式（不使用实心灰块）
- `.search-group` 把搜索框 + 搜索按钮视觉绑成一组

## 表单弹窗

```
<div class="modal-overlay">
  <div class="modal-dialog section">
    <span class="label">板块：弹窗名</span>
    <div class="modal-title">弹窗标题</div>

    <div class="form-row">
      <div class="form-label">字段 1 *</div>
      <div class="wf-text long form-input">字段 1 输入框</div>
    </div>
    <!-- 更多 form-row -->

    <div class="modal-actions">
      <button class="btn outline">取消</button>
      <button class="btn">主动作</button>
    </div>
  </div>
</div>
```

**约定**：
- 必填字段的 `.form-label` 末尾加 ` *`
- 按钮顺序：取消（outline）在左，主动作（实心）在右
- 主动作文案按 PRD（"创建品牌" / "保存更改" 等）

## 确认对话框（destructive）

```
<div class="modal-overlay">
  <div class="modal-dialog modal-confirm section">
    <span class="label">板块：删除确认</span>
    <div class="modal-title">确认删除？</div>
    <div class="wf-text long">确认删除商品"{名称}"？此操作不可恢复。</div>
    <div class="modal-actions">
      <button class="btn outline">取消</button>
      <button class="btn btn-danger">删除</button>
    </div>
  </div>
</div>
```

**约定**：
- `.modal-confirm` 覆写宽度（比表单弹窗窄）
- 危险按钮用 `.btn-danger`
- 提示文本里的占位变量用 `{变量名}`

## 空态

**首选做法：不独立成页**。嵌在 `.list-column` 里，原本 `.card-list` 的位置用 `.empty-state` 代替。

```
<section class="list-column section">
  <span class="label">板块：品牌列表（空态）</span>
  <div class="column-header">
    <button class="btn small">新增品牌</button>
  </div>
  <div class="empty-state">
    <div class="empty-icon wf-box"></div>
    <div class="wf-text heading empty-title">No brands yet</div>
    <div class="wf-text long">Add your first brand to get started.</div>
    <button class="btn">新增品牌</button>
  </div>
</section>
```

**何时独立成页**：仅当 PRD 明确把空态作为独立页面描述。否则不生成独立文件，在报告 "Skipped" 栏记录。

## 非典型页面

PRD 描述不匹配以上 pattern 时（如顶部是地图、表格里嵌缩略图等）：**按 PRD 字面描述拼装 primitive，不强套模板**。自主布局决策写进 HTML 顶部注释。
