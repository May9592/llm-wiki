---
type: summary
source: "[[raw/articles/YishenTuclaudian An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault.md]]"
compiled_at: 2026-04-08
status: done
---

# S-003: Claudian - Obsidian 中的 Claude Code 嵌入

## TL;DR
Claudian 是一个 Obsidian 插件，将 Claude Code 等 AI coding agent 嵌入到 Vault 中，使 Vault 成为 agent 的工作目录。

## 核心结论

### 主要功能
- **Inline Edit**：选中文本快捷编辑，词级 diff 预览
- **Slash Commands & Skills**：`/` 和 `$` 触发可重用提示模板
- **@mention**：提及 vault 文件、子 agent、MCP 服务器
- **Plan Mode**：探索和设计后再实施，Shift+Tab 切换
- **MCP Servers**：通过 Model Context Protocol 连接外部工具

### 支持的 Provider
- **Claude**：Claude Code CLI（原生安装推荐）
- **Codex**：OpenAI Codex CLI（可选）

### 安装方式
1. 手动下载 release 文件到 `.obsidian/plugins/claudian/`
2. 使用 BRAT 插件自动安装更新
3. 从源码构建（开发模式）

## 关键证据

### 核心架构
```
src/
├── core/         # Provider 中立运行时
├── providers/    # Claude/Codex 适配器
├── features/     # Chat/Inline Edit/Settings
└── shared/       # 可复用 UI 组件
```

### 隐私说明
- 发送到 API：输入、附件、图片、工具调用输出
- 本地存储：settings 和 session metadata
- 无遥测：无额外追踪

## 概念提取
- [[C-008-Claudian|Claudian]]
- [[C-009-MCP|MCP (Model Context Protocol)]]
- [[C-010-Inline-Edit|Inline Edit]]
- [[C-011-Plan-Mode|Plan Mode]]

## 疑点/待验证
- Codex provider 稳定性如何？

## 术语表
| 术语 | 定义 |
|------|------|
| MCP | Model Context Protocol，模型上下文协议 |
| Inline Edit | 内联编辑，直接在笔记中编辑文本 |
| BRAT | Beta Reviewers Auto-update Tester，Obsidian 插件自动更新工具 |
