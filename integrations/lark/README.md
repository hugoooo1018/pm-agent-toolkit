# 飞书集成

把生成好的 PRD Markdown 推送到飞书文档 / 飞书知识库。

## 场景

- PRD 写完，要发到飞书与 reviewer 共享
- 把 PRD 挂到飞书知识库的产品文档空间
- 把 PRD 附带的原型图（JPG / HTML）一并上传

本集成**不负责 PRD 写作**，那是 `skills/` / `rules/` 的职责。本集成只关心**产出之后**。

## 前置条件

### 方式 A：命令行（lark-cli）

用户本地已安装 [lark-cli](https://github.com/larksuite/lark-cli)（或等价工具）并完成 `lark-cli auth login`。

### 方式 B：Agent 内置 Skill（Claude Code）

使用系统已有的 `lark-doc` skill（若你的 Claude Code 环境已安装）。它封装了创建/更新飞书文档、上传图片等能力。

## 使用示例

### 创建一篇新的飞书文档

```bash
# 方式 A
lark-cli docs create \
  --from-md examples/daily-signin-feature/04-prd-final.md \
  --title "每日签到 PRD v1.0" \
  --folder "产品文档/PRD/2026-Q2"
```

```
# 方式 B（Claude Code 会话中）
把 examples/daily-signin-feature/04-prd-final.md 发到飞书，
放在"产品文档/PRD/2026-Q2"文件夹下，标题"每日签到 PRD v1.0"
```

Claude Code 会自动识别意图并调用 `lark-doc` skill。

### 更新已有文档

```bash
lark-cli docs update \
  --doc-token <doc_token> \
  --from-md examples/daily-signin-feature/04-prd-final.md \
  --mode replace
```

`--mode` 可选 `replace` / `append` / `prepend`。

### 上传原型图资源

```bash
# 给已存在的飞书文档追加原型图
lark-cli docs upload-image \
  --doc-token <doc_token> \
  --image path/to/wireframe.html \
  --inline-at "§5.1"
```

或者让 Claude Code 用 `lark-doc` skill 处理。

## 推荐的 PRD 在飞书的组织方式

```
飞书知识库：产品中心
  └── PRD
      ├── 2026-Q1
      ├── 2026-Q2
      │   ├── 每日签到 PRD v1.0
      │   └── 收藏夹重构 PRD v0.3
      └── 归档
```

- 每份 PRD 一个文档
- 按季度分文件夹
- 废弃或上线半年以上的挪到"归档"

## 生命周期与飞书的对应

本 toolkit 定义的 PRD 状态（见 `../../lifecycle/states.md`）与飞书操作的对应：

| PRD 状态 | 建议操作 |
|---|---|
| Draft | 仅自己可见的文档，别人看不到 |
| In Review | 开启评论权限，分享给 reviewer |
| Approved | 锁编辑，打 `[Approved]` 标签 |
| In Development | 附研发 ticket 链接 |
| Shipped | 顶部加"已上线"标签 + 实际指标与目标对比 |
| Deprecated | 挪到"归档"文件夹 |

状态变化是手动的。未来可以考虑写个 lark-cli 脚本自动化（超出 v0.2 范围）。

## 不做的事

- **不造轮子**：所有文档 API 交互都用现有的 lark-cli / lark-doc skill
- **不存 token**：认证靠上游工具，本集成零凭证管理
- **不做双向同步**：飞书改了不回传到 Git；Git 改了也不自动同步飞书（单向推为主）

## 可能用到的常见 lark-cli 子命令

```
lark-cli docs create       # 创建文档
lark-cli docs update       # 更新文档
lark-cli docs get          # 读取文档
lark-cli docs search       # 搜索文档
lark-cli docs upload-image # 上传图片
lark-cli wiki create-space # 创建知识空间
lark-cli wiki add-node     # 往知识空间加节点
```

具体以你本地 lark-cli 的版本为准，执行 `lark-cli docs --help` 查看。

## 未来可能扩展

- `integrations/confluence/` — 推到 Confluence 空间
- `integrations/notion/` — 同步到 Notion 数据库
- `integrations/docusaurus/` — 写入 Docusaurus 项目的 `docs/business/` 目录（Git 提交）

上述都不在 v0.2 范围内。
