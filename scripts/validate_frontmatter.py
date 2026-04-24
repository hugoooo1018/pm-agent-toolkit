#!/usr/bin/env python3
"""pm-agent-toolkit frontmatter 校验脚本

校验规则：
- 所有 rules/*.md 和 skills/**/SKILL.md 可解析 YAML frontmatter
- 必填字段齐全（name / description / version）
- name 与文件/文件夹名一致
- Rule 层纯净度：rules/*.md frontmatter 不含 related_skills/applies_rules
- Skill 的 applies_rules 引用的 rule 必须存在于 rules/ 下

用法：
    python scripts/validate_frontmatter.py

退出码：
    0 — 全通过
    1 — 有错误
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: 缺少 pyyaml，请 `pip install pyyaml`", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = ROOT / "rules"
SKILLS_DIR = ROOT / "skills"

FM_START = "---"
RULE_REQUIRED = {"name", "description", "version"}
SKILL_REQUIRED = {"name", "description", "version"}
RULE_FORBIDDEN = {"related_skills", "applies_rules"}


class ValidationError(Exception):
    pass


errors: list[str] = []
warnings: list[str] = []


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    """返回 (frontmatter dict, body)"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith(FM_START):
        raise ValidationError(f"{path}: 缺少 frontmatter")
    parts = text.split(FM_START, 2)
    if len(parts) < 3:
        raise ValidationError(f"{path}: frontmatter 未闭合")
    fm_text, body = parts[1], parts[2]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        raise ValidationError(f"{path}: YAML 解析失败 — {e}")
    if not isinstance(fm, dict):
        raise ValidationError(f"{path}: frontmatter 必须是 dict")
    return fm, body


def validate_rule(path: Path, known_rule_names: set[str]) -> None:
    try:
        fm, _ = parse_frontmatter(path)
    except ValidationError as e:
        errors.append(str(e))
        return

    missing = RULE_REQUIRED - set(fm)
    if missing:
        errors.append(f"{path}: Rule frontmatter 缺字段 {missing}")

    forbidden = RULE_FORBIDDEN & set(fm)
    if forbidden:
        errors.append(f"{path}: Rule frontmatter 含禁止字段 {forbidden}（Rule 层应 agent-neutral）")

    expected_name = path.stem
    if fm.get("name") != expected_name:
        errors.append(f"{path}: name='{fm.get('name')}' 与文件名 '{expected_name}' 不一致")


def validate_skill(path: Path, known_rule_names: set[str]) -> None:
    try:
        fm, _ = parse_frontmatter(path)
    except ValidationError as e:
        errors.append(str(e))
        return

    missing = SKILL_REQUIRED - set(fm)
    if missing:
        errors.append(f"{path}: Skill frontmatter 缺字段 {missing}")

    # name 应与父目录名一致
    expected_name = path.parent.name
    if fm.get("name") != expected_name:
        errors.append(f"{path}: name='{fm.get('name')}' 与目录名 '{expected_name}' 不一致")

    # applies_rules 必须指向真实存在的 rule
    applies = fm.get("applies_rules") or []
    if isinstance(applies, list):
        for r in applies:
            if r not in known_rule_names:
                errors.append(f"{path}: applies_rules 引用的 rule '{r}' 在 rules/ 下不存在")
    else:
        errors.append(f"{path}: applies_rules 必须是列表")


def main() -> int:
    if not RULES_DIR.exists():
        errors.append(f"{RULES_DIR} 不存在")
    if not SKILLS_DIR.exists():
        errors.append(f"{SKILLS_DIR} 不存在")

    # 第一遍：收集所有 rule 名
    known_rule_names: set[str] = set()
    rule_files = sorted(p for p in RULES_DIR.glob("*.md") if p.name != "README.md")
    for rf in rule_files:
        known_rule_names.add(rf.stem)

    # Rule 校验
    for rf in rule_files:
        validate_rule(rf, known_rule_names)

    # Skill 校验
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    for sf in skill_files:
        validate_skill(sf, known_rule_names)

    # 输出
    print(f"扫描：{len(rule_files)} Rule / {len(skill_files)} Skill")
    if warnings:
        print("\n⚠️  警告：")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print("\n❌ 错误：")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\n✅ 全通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
