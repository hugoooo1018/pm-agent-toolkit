# 贡献指南

欢迎为 pm-agent-toolkit 贡献。本文档说明如何新增/修改 Rule、Skill、Template 与 Adapter。

## 开始之前

- 本仓库有明确的**三层架构**（知识 / 绑定 / 集成），贡献前请读 [docs/architecture.md](docs/architecture.md)
- 本仓库是 **opinionated** 的（基于作者个人实践），详见 [docs/opinionated.md](docs/opinionated.md)；大改动前先开 issue 讨论
- 不清楚术语先查 [docs/glossary.md](docs/glossary.md)

## 新增或修改 Rule

Rule 是 **agent-neutral** 的 PM 知识资产。任何 Agent 都能读，所以要严守纯净度：

- ❌ **不要**在 Rule 里提具体的 skill 名（如 `/prd-review`、`skills/prd-paradigm/`）
- ❌ **不要**提 Claude Code 专属概念（SKILL.md / Read 工具 / Stage 0 等）
- ❌ **不要**在 frontmatter 加 `related_skills` 或 `applies_rules`（这是 Skill 的字段）
- ✅ 描述能力时用抽象名："需要原型图能力" 而非 "调用 wireframe-generator"
- ✅ 模板引用可以保留（`templates/` 也是 agent-neutral 资产）

**流程**：

1. 在 `rules/` 下建或修改 `<name>.md`
2. frontmatter 最少含 `name` / `description` / `scope` / `version`
3. 过一遍 `python scripts/validate_frontmatter.py`
4. 如果新增 Rule，在 `CLAUDE.md` 的"激活中的 Rules"列表追加一行

## 新增或修改 Skill

Skill 是 **Claude Code 的绑定层**。可以自由使用 Claude Code 特性。

- frontmatter 必含 `name` / `description` / `type` / `version`
- 推荐含 `applies_rules`（单向指向 `rules/` 下的某个 Rule）
- 不要在 Skill 里重抄原则；通过 "Rule References" 段引用 Rule
- 遵循 Claude Code 官方 SKILL.md 规范

**流程**：

1. 在 `skills/<name>/SKILL.md` 新建
2. frontmatter + body 完整
3. 过 lint
4. 在 `CLAUDE.md` 和 `skills/README.md` 的清单里追加

## 新增模板风格

当前仓库只含 `templates/default-style/`。欢迎新增其他 PRD 风格（Amazon PR-FAQ、Intercom RFC 等）：

1. 建 `templates/<style-name>/`
2. 含 `README.md` 说明来源、适用场景、与 default-style 的差异
3. 在 `rules/prd-paradigm.md` 明确声明"本范式是一种选择，见 templates/ 其他风格"

## 新增 Adapter（接入其他 Agent）

**Adapter 把 rules/ 翻译成特定 Agent 能消费的格式**。

示例：Cursor 的 `.cursorrules`、Windsurf 的配置、OpenAI Assistants 的 instructions。

**流程**：

1. 建 `adapters/<agent-name>/`
2. 文件内容从 `rules/` 拼装而来（手动或脚本）
3. 含 `README.md` 说明如何使用（复制到哪儿、如何激活）
4. 保持与 `rules/` 的语义对等，不要在 Adapter 里自创新内容

## PR 规范

- PR 标题用英文或中文均可，简洁清楚
- PR 正文至少说清：**改了什么 / 为什么 / 影响范围**
- Breaking change 在标题加 `[BREAKING]`，并更新 `CHANGELOG.md`
- CI 必须绿（frontmatter lint）

## 本地验证

```bash
# 跑 lint
python scripts/validate_frontmatter.py

# 结构检查
find . -type f -not -path './.git/*' -not -name '.DS_Store' | sort
```

## 报 issue

欢迎报：

- Rule 不够纯净、含 Claude Code 残留
- 模板与真实 PRD 脱节的地方
- 想新增的 Skill / Adapter / Template 风格
- 文档错误或术语歧义

不欢迎：

- 无痛点的风格大改（先开 discussion）
- 单纯为加 skill 而加 skill

## 许可

所有贡献按 MIT 许可发布。提交即视为同意。
