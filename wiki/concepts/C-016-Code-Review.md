---
type: concept
id: "C-016"
created_at: 2026-04-08
related:
  - [[C-014-Codex|Codex]]
  - [[C-015-Adversarial-Review|Adversarial Review]]
sources:
  - [[S-005-Codex插件集成]]
---

# Code Review (代码审查)

## 定义
对代码变更进行系统性检查的过程。

## 类型
1. **标准 Review**：只读，检查代码质量
2. **Adversarial Review**：可控制，质疑方向和设计

## 使用时机
- 多文件变更时建议后台运行
- 发布前审查
- 分支对比（使用 `--base <ref>`）

## 相关概念
- [[C-014-Codex|Codex]]：提供代码审查功能
- [[C-015-Adversarial-Review|Adversarial Review]]：挑战式审查

## 来源
- [[S-005-Codex插件集成|S-005: Codex插件集成]]
