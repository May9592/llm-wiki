---
type: summary
source: "[[raw/articles/llm-wiki.md]]"
compiled_at: 2026-04-08
status: done
---

# S-001: LLM Wiki - 个人知识库构建方法论

## TL;DR
Karpathy 提出的 LLM Wiki 模式：让 LLM 增量构建持久化 Wiki，而非每次查询都从原始文档重新检索。知识被编译一次并持续维护。

## 核心结论

### RAG 的根本问题
- 每次查询都从零开始检索，没有知识积累
- 综合多文档时需反复查找和拼凑
- 没有交叉引用和矛盾标记

### LLM Wiki 的核心差异
- **持久化 Wiki**：Markdown 文件互相链接，持续更新
- **增量编译**：新内容集成到现有 Wiki，而非重新索引
- **AI 维护**：LLM 负责摘要、交叉引用、一致性维护
- **人类角色**：负责素材选取、方向把控、提问

### 三层架构
1. **Raw sources**（原始素材）：不可变的文档集合
2. **Wiki**（知识库）：LLM 生成的结构化内容
3. **Schema**（规范）：告诉 LLM 如何维护 Wiki

## 关键证据

### 适用场景
- Personal：目标、健康、自我提升追踪
- Research：深度研究主题，构建演进论点
- Reading：阅读书籍时构建角色/主题/情节网络
- Business/Team：内部 Wiki，从 Slack/会议/文档中提炼知识

### 三个核心操作
- **Ingest**：处理新源 → 摘要 + 更新实体页 + 更新索引
- **Query**：搜索相关页面 → 综合回答 → 可存回 Wiki
- **Lint**：健康检查 → 矛盾检测 + 孤岛页面 + 缺失交叉引用

## 概念提取
- [[C-001-RAG|RAG]]
- [[C-002-LLM-Wiki|LLM Wiki]]
- [[C-003-增量编译|增量编译]]
- [[C-004-持久化知识库|持久化知识库]]

## 疑点/待验证
- 实际使用中 Wiki 规模上限是多少？
- 如何处理冲突的知识更新？

## 术语表
| 术语 | 定义 |
|------|------|
| RAG | Retrieval-Augmented Generation，检索增强生成 |
| Incremental Wiki | 增量构建的持久化知识库 |
| Schema | 配置文件，定义 Wiki 结构和维护规范 |
