---
type: concept
id: "C-012"
created_at: 2026-04-08
related:
  - [[C-013-智能素材路由|智能素材路由]]
sources:
  - [[S-004-LLM-Wiki-Skill多平台]]
---

# baoyu-url-to-markdown

## 定义
一个 URL 到 Markdown 的转换工具，通过 Chrome CDP (Chrome DevTools Protocol) 渲染网页并转换为 Markdown 格式。

## 支持的来源
- 网页文章
- X/Twitter
- 知乎

## 使用方式
作为 llm-wiki-skill 的可选外挂，自动提取网页内容。如果提取失败，系统会提示手动处理。

## 相关概念
- [[C-013-智能素材路由|智能素材路由]]：选择合适的提取工具

## 来源
- [[S-004-LLM-Wiki-Skill多平台]]
