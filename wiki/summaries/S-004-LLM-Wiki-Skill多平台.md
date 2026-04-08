---
type: summary
source: "[[raw/articles/sdyckjq-labllm-wiki-skill 基于 Karpathy llm-wiki 方法论的个人知识库构建 Skill，支持多平台！.md]]"
compiled_at: 2026-04-08
status: done
---

# S-004: llm-wiki-skill - 多平台知识库构建工具

## TL;DR
基于 Karpathy 的 llm-wiki 方法论，为 Claude Code、Codex、OpenClaw 等 agent 提供统一的个人知识库构建系统。

## 核心结论

### 与 Karpathy 原版的核心区别
知识被 **编译一次，持续维护**，而非每次查询都从原始文档重新推导。

### 支持的平台
- **Claude Code**：`~/.claude/skills/llm-wiki`
- **Codex**：`~/.codex/skills/llm-wiki`
- **OpenClaw**：`~/.openclaw/skills/llm-wiki`

### 安装命令
```bash
bash install.sh --platform claude  # Claude Code
bash install.sh --platform codex   # Codex
bash install.sh --platform openclaw  # OpenClaw
```

## 关键证据

### 来源边界分类
| 分类 | 当前来源 | 处理方式 |
|------|----------|----------|
| 核心主线 | PDF/本地 PDF、Markdown/文本/HTML、纯文本粘贴 | 直接进入主线 |
| 可选外挂 | 网页文章、X/Twitter、微信公众号、YouTube、知乎 | 自动提取，失败时回退手动 |
| 手动入口 | 小红书 | 用户手动粘贴 |

### 外挂对应关系
- `baoyu-url-to-markdown`：网页文章、X/Twitter、知乎
- `wechat-article-to-markdown`：微信公众号
- `youtube-transcript`：YouTube

### 核心功能
- 零配置初始化
- 智能素材路由（根据 URL 域名自动选择提取方式）
- 内容分级处理（长文完整整理，短文简化）
- 批量消化
- 结构化 Wiki（自动生成摘要、实体页、主题页）
- 知识库健康检查
- Obsidian 兼容

## 概念提取
- [[C-002-LLM-Wiki|LLM Wiki]]
- [[C-012-baoyu-url-to-markdown|baoyu-url-to-markdown]]
- [[C-013-智能素材路由|智能素材路由]]

## 疑点/待验证
- 实际使用中各外挂的稳定性如何？

## 术语表
| 术语 | 定义 |
|------|------|
| 素材路由 | 根据 URL 域名自动选择最佳内容提取方式 |
| 批量消化 | 一次性处理整个文件夹的多个文件 |
