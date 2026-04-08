---
type: concept
id: "C-008"
created_at: 2026-04-08
related:
  - [[C-009-MCP|MCP]]
  - [[C-010-Inline-Edit|Inline Edit]]
  - [[C-011-Plan-Mode|Plan Mode]]
sources:
  - [[S-003-Claudian插件]]
---

# Claudian

## 定义
一个 Obsidian 插件，将 Claude Code 等 AI coding agent 嵌入到 Vault 中。

## 核心功能
- **Inline Edit**：选中文本快捷编辑，词级 diff 预览
- **Slash Commands & Skills**：`/` 和 `$` 触发可重用提示模板
- **@mention**：提及 vault 文件、子 agent、MCP 服务器
- **Plan Mode**：探索和设计后再实施（Shift+Tab）
- **MCP Servers**：连接外部工具

## 支持的 Provider
- Claude（Claude Code CLI）
- Codex（OpenAI Codex CLI）

## 安装方式
1. 手动下载 release 文件
2. 使用 BRAT 插件自动安装
3. 从源码构建

## 相关概念
- [[C-009-MCP|MCP]]：Model Context Protocol
- [[C-010-Inline-Edit|Inline Edit]]：内联编辑
- [[C-011-Plan-Mode|Plan Mode]]：计划模式

## 来源
- [[S-003-Claudian插件|S-003: Claudian插件]]
