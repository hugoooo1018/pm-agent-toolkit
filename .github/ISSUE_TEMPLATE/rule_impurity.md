---
name: Rule 纯净度问题
about: 发现 rules/ 下的文件含 Claude Code 残留或其他 agent-specific 特征
title: "[Purity] "
labels: purity
assignees: ''
---

## 文件位置

`rules/<name>.md` 第 X 行

## 违规内容

引用原文（或截图），标出违反 agent-neutral 纯净度的具体字串。

## 违反了哪条约定？

参见 `rules/README.md` 的"纯净度要求"和 `docs/architecture.md` 的"Rule 层纯净度"。

- [ ] 出现了 `skills/` 或 `/skill-name` 路径
- [ ] 出现了 `SKILL.md` / `Read 工具` 等 Claude Code 术语
- [ ] frontmatter 含 `related_skills` / `applies_rules`
- [ ] 其他 agent-specific 特征

## 建议修正

如何改写成 agent-neutral 形式？
