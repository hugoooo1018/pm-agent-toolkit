# Changelog

本项目采用语义化版本（[SemVer](https://semver.org/lang/zh-CN/)）。

## [0.2.0] - 2026-04-24

### 架构重构：三层模型

整个仓库从"Claude Code plugin"升级为"PM 知识工具包"。新增三层架构：

1. **知识层**（`rules/` + `templates/` + `lifecycle/`）— Agent-neutral，可被任意 Agent 消费
2. **绑定层**（`skills/` + `adapters/`）— Claude Code / Cursor / 通用 system prompt
3. **集成层**（`integrations/`）— 产出去向（目前仅飞书 CLI）

### 变更

#### 新增

- `rules/prd-clarification.md`、`rules/prd-quality-checklist.md`、`rules/prd-paradigm.md`（从 skill 升格）
- `templates/default-style/`（原本在 skills/prd-paradigm 下）
- `adapters/cursor/.cursorrules`、`adapters/generic-system-prompt/*.md`
- `integrations/lark/README.md`
- `lifecycle/states.md`
- `examples/daily-signin-feature/` 端到端 5 文件
- `scripts/validate_frontmatter.py`
- `.github/workflows/validate.yml`
- `LICENSE`（MIT）、`CONTRIBUTING.md`、`.gitignore`
- `docs/architecture.md`、`docs/opinionated.md`、`docs/glossary.md`、`docs/integration-guide.md`

#### 变更

- Rule 层全面 **agent-neutral**：frontmatter 去 `related_skills`，body 去所有 Claude Code 特征引用
- `rules/pm-doc-standards.md` 合并进 `rules/prd-writer.md`"基础三要素"节
- `skills/prd-paradigm/` 瘦身为绑定层，原则与模板迁出
- `skills/prd-review/SKILL.md` 的 `applies_rules` 更新为新 Rule
- `CLAUDE.md` 与 `README.md` 重写，突出三层架构与 opinionated 声明
- `.claude-plugin/plugin.json` 版本升至 0.2.0

#### 删除

- `skills/prd-clarification/`、`skills/prd-self-checker/`（升格为 Rule）
- `rules/pm-doc-standards.md`（合并）
- `docs/templates/skill-example-draft-prd.md`
- `agents/`、`commands/`、`hooks/` 空目录

### 不兼容变动

- 如果你 fork 了 0.1.x 版本并扩展了自己的 skill / rule，升级时需要：
  - 删除 Rule frontmatter 的 `related_skills`
  - 检查 Rule body 是否含 `/skill-name` 或 `skills/` 路径，改为抽象描述
  - 原 `skills/prd-paradigm/templates/` 的模板路径改为 `templates/default-style/`

---

## [0.1.0] - 2026-04-24

### 首次发布

- 搭好"分层双栈"骨架（`rules/` + `skills/`）
- 迁移并整合 3 份外部资产：`prd-paradigm`、`wireframe-generator`、`prd-review-cn`
- 基于 SKILL01-v4 提炼出 `prd-writer` Rule + `prd-clarification` + `prd-self-checker` Skill
- 建立 PRD 工作流：PRD Writer Rule 编排 5 个 Skill 的松耦合调用
