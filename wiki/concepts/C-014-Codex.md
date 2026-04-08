---
type: concept
id: "C-014"
created_at: 2026-04-08
related:
  - [[C-015-Adversarial-Review|Adversarial Review]]
  - [[C-016-Code-Review|Code Review]]
sources:
  - [[S-003-Claudian插件]]
  - [[S-005-Codex插件集成]]
---

# Codex

## 定义
OpenAI 的 AI coding agent，类似 Claude Code。

## 特点
- 支持 ChatGPT 订阅或 OpenAI API key
- 可在 Claude Code 中通过插件使用
- 具有代码审查、任务委托等功能

## 与 Claude Code 的集成
- 通过 `/codex:` 系列命令使用
- 共享本地认证和配置
- 可在 Claude 和 Codex 之间转移任务

## 相关概念
- [[C-015-Adversarial-Review|Adversarial Review]]：Codex 的挑战式审查
- [[C-016-Code-Review|Code Review]]：代码审查

## 来源
- [[S-003-Claudian插件|S-003: Claudian插件]]
- [[S-005-Codex插件集成|S-005: Codex插件集成]]
