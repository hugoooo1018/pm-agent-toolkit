# 安全政策

## 报告漏洞

pm-agent-toolkit 本身是纯文本 + Python lint 脚本，没有运行时组件，安全风险面有限。但如果你发现了以下情况，请**不要**开公开 issue，而是通过邮件私下告知：

- Python 脚本（`scripts/validate_frontmatter.py`）存在代码执行 / 路径穿越漏洞
- CI 配置（`.github/workflows/validate.yml`）存在被利用风险
- 任何可能泄露使用者 PRD 内容的行为

**联系方式**：hugoooo1018@users.noreply.github.com

收到后 48 小时内回复，商定披露时间。

## 本仓库的数据安全边界

- 本仓库**不收集**任何用户数据
- 本仓库**不发送**任何网络请求（除非你手动运行 `integrations/lark/` 里的命令）
- 所有 Agent 集成（Claude Code / Cursor / lark-cli 等）的安全性由各自生态负责，本仓库不代管凭证

## 支持的版本

- v0.2.x — 当前版本，接受安全修复
- v0.1.x — 不再维护

升级到最新版见 [CHANGELOG.md](CHANGELOG.md)。
