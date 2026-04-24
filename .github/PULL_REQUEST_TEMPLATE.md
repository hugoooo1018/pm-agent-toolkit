## 改了什么

简要描述 PR 的改动。

## 为什么改

解决了什么问题 / 支持了什么场景。

## 影响范围

- [ ] 仅文档（docs/ / README / CHANGELOG）
- [ ] 新增 Rule（rules/）
- [ ] 修改已有 Rule
- [ ] 新增 Skill / Adapter / Integration / Template 风格
- [ ] Breaking change（要同步更新 CHANGELOG 的 Unreleased 段）

## 自检清单

- [ ] 本地跑过 `python scripts/validate_frontmatter.py`，全绿
- [ ] 新增 Rule 的话，没带 Claude Code 特征（`rules/README.md` 纯净度要求）
- [ ] 新增 Skill 的话，`applies_rules` 指向真实存在的 Rule
- [ ] 文档 / 示例 / CHANGELOG 已相应更新
- [ ] 如果改了原则性内容，更新了对应 adapter（`adapters/cursor/.cursorrules` 等）

## 相关 issue

Closes #<issue 编号>（若无可留空）
