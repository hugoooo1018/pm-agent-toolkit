---
name: wireframe-generator
description: 基于 PRD 文字生成低保真灰度 HTML wireframe，并按约定更新 PRD 中的原型引用。
type: workflow
version: 0.2.0
---

# wireframe-generator

从 PRD 生成低保真灰度 HTML 线框图。wireframe 只管**结构和布局**；所有交互行为由 PRD 承担。

## 触发边界

- **适用**：按 `docs/business/<module>/*-prd.md` 生成/补画/替换单页或多页 wireframe；明确要求按 PRD 文本生成；把 PRD 中 `![](./assets/*.jpg)` 替换为 HTML iframe。
- **不适用**：高保真视觉稿、真实前端开发用 UI、与 PRD 无关的静态原型。
- **常见触发词**："生成 wireframe"、"画线框图"、"按 PRD 跑一遍"、"把原型图改成 HTML"、"在 <prd> 上生成原型"。

## 输入

PRD 文件路径 `docs/business/<module>/<name>-prd.md`，内含"六、页面原型图"或类似章节。可选：指定要生成的页面名。

## 工作流

1. **读 PRD 目标章节**——定位"六、页面原型图"（或类似标题），按顺序解析每个 `### <页面名>` 子段
2. **不读 .jpg**——wireframe 完全由 PRD 文字描述生成
3. **识别结构**——从 PRD bullet points 抽出区域、字段、按钮。按 A/B/C/D 四类归类（见 `references/design-system.md`）
4. **参考已有 wireframe**——同模块已有则读一份最相近类型的作为风格锚点
5. **生成 HTML**——用 `_wireframe.css` 里的 class，参考 `references/page-patterns.md` 页面骨架
6. **输出 + PRD 引用替换**（见下方"输出路径契约"）
7. **自检**（见下方"自检清单"），失败项在报告里列出

## 参考文档

- `references/design-system.md` —— 4 类组件、颜色规范、CSS class 清单、间距字号 token
- `references/page-patterns.md` —— 列表页/详情页/弹窗/确认对话框/空态的典型骨架
- `references/decisions.md` —— 锁死决策 + 必问清单 + 自主决策规则
- `templates/_wireframe.css` —— 共享 CSS canonical 模板

## 输出路径契约

对 PRD `docs/business/<module>/<name>-prd.md`，输出到：

```
docs/business/<module>/
├── <name>-prd.md              ← 更新 JPG 引用为 <AutoIframe>
├── assets/<page>.jpg          ← 永不删（保留备份）
└── wireframes/
    ├── _wireframe.css         ← 首次进入模块时从 templates/ 复制；已存在时不覆盖
    └── <page>.html            ← 新生成

static/wireframes/             ← Docusaurus 项目额外复制（判定：仓库根存在 docusaurus.config.ts/js）
├── _wireframe.css
└── <page>.html
```

**HTML 里 CSS 引用**：`<link rel="stylesheet" href="./_wireframe.css">`（同目录相对路径）。

**PRD JPG 引用替换**：
```markdown
<!-- 原 -->  ![Customer 主页](./assets/customer-homepage.jpg)
<!-- 新 -->  <AutoIframe src="/wireframes/customer-homepage.html" title="Customer 主页" />
```

PRD md 顶部需 `import AutoIframe from '@site/src/components/AutoIframe';`（已有则跳过）。

**Wireframe 文件名** = PRD 里对应 JPG 名去掉 `.jpg` + `.html`（例：`customer-homepage.jpg` → `customer-homepage.html`）。

**非 Docusaurus 项目**：跳过 static 复制和 PRD AutoIframe 替换，保持原 JPG 引用。

**三份 CSS 必须逐字一致**：`docs/business/<module>/wireframes/_wireframe.css` / `static/wireframes/_wireframe.css` / `.claude/skills/wireframe-generator/templates/_wireframe.css`。追加新 primitive 时三处同步。

## 自检清单（报告必须包含）

| 项 | 通过条件 |
|---|---|
| 源 HTML 写入 | `docs/business/<module>/wireframes/<page>.html` 存在 |
| 共享 CSS 链接 | HTML `<head>` 含 `<link rel="stylesheet" href="./_wireframe.css">`；无内联 `<style>` |
| `.wf-text` 无空块 | 不存在空内容的 `.wf-text` 节点（含仅空格/换行） |
| 字段覆盖 | PRD 本页描述的每个字段在 HTML 里出现 |
| 无交互标记 | HTML 零 `.click-chip` / `.attr-chip` / `.has-chip`（已废弃） |
| label / 板块注释就位 | 每个 section/card/dialog 左上角有 `.label`，文案以 `板块：` 开头 |
| 静态副本（Docusaurus） | `static/wireframes/<page>.html` 存在；三份 CSS 一致 |
| PRD 引用已更新 | 从 `![...](.jpg)` → `<AutoIframe src="/wireframes/...">`；AutoIframe import 存在 |
| 原 JPG 保留 | `assets/<page>.jpg` 仍存在 |
| 自主决策已注释 | HTML 顶部 `<!-- Autonomous decisions: ... -->` 说明推断项 |

失败项必须明确列出，不能静默通过。
