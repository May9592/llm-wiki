---
type: concept
id: "C-015"
created_at: 2026-04-08
related:
  - [[C-014-Codex|Codex]]
  - [[C-016-Code-Review|Code Review]]
sources:
  - [[S-005-Codex插件集成]]
---

# Adversarial Review (挑战式审查)

## 定义
一种可控制的代码审查方式，质疑实现选择和设计决策。

## 使用场景
- 发布前挑战方向，而非仅代码细节
- 审查设计选择、权衡取舍、隐藏假设、替代方案
- 针对特定风险区域压力测试：auth、数据丢失、回滚、竞态条件、可靠性

## 与标准 Review 的区别
| 标准 Review | Adversarial Review |
|-------------|-------------------|
| 只检查代码质量 | 质疑实现方向 |
| 不可控制 | 可控制 |
| 不能自定义焦点 | 可指定焦点区域 |

## 相关概念
- [[C-014-Codex|Codex]]：支持 Adversarial Review
- [[C-016-Code-Review|Code Review]]：代码审查

## 来源
- [[S-005-Codex插件集成|S-005: Codex插件集成]]
