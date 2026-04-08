---
type: summary
source: "[[raw/articles/openaicodex-plugin-cc Use Codex from Claude Code to review code or delegate tasks..md]]"
compiled_at: 2026-04-08
status: done
---

# S-005: Codex Plugin for Claude Code

## TL;DR
在 Claude Code 中使用 OpenAI Codex 进行代码审查或任务委托的插件。

## 核心结论

### 主要命令
| 命令 | 功能 |
|------|------|
| `/codex:review` | 标准代码审查 |
| `/codex:adversarial-review` | 可挑战的方向性审查 |
| `/codex:rescue` | 委托任务给 Codex |
| `/codex:status` | 查看运行中的任务 |
| `/codex:result` | 查看已完成任务的输出 |
| `/codex:cancel` | 取消后台任务 |
| `/codex:setup` | 检查 Codex 安装和认证 |

### 安装
```bash
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

## 关键证据

### Adversarial Review 的使用场景
- 发布前挑战实现方向，而非代码细节
- 审查设计选择、权衡取舍、隐藏假设
- 针对特定风险区域进行压力测试（auth、数据丢失、竞态条件等）

### Codex Rescue 的使用场景
- 调查 bug
- 尝试修复
- 继续之前的 Codex 任务
- 使用更小模型更快/更便宜地完成任务

### 配置继承
- 使用相同的 Codex 安装
- 使用相同的本地认证状态
- 使用相同的仓库 checkout 和环境
- 拾取相同的 Codex 配置（`~/.codex/config.toml` 和 `.codex/config.toml`）

## 概念提取
- [[C-014-Codex|Codex]]
- [[C-015-Adversarial-Review|Adversarial Review]]
- [[C-016-Code-Review|Code Review]]

## 疑点/待验证
- 实际使用中 review gate 是否会造成 Claude/Codex 循环？

## 术语表
| 术语 | 定义 |
|------|------|
| Adversarial Review | 可挑战的方向性代码审查，质疑实现和设计 |
| Review Gate | 在操作前自动运行 Codex 审查的机制 |
