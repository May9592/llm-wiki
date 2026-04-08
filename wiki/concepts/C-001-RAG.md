---
type: concept
id: "C-001"
created_at: 2026-04-08
related:
  - [[C-002-LLM-Wiki|LLM Wiki]]
  - [[C-003-增量编译|增量编译]]
sources:
  - [[S-001-LLM知识库方法论]]
  - [[S-002-Karpathy知识库实践指南]]
---

# RAG (Retrieval-Augmented Generation)

## 定义
检索增强生成。一种让 LLM 在回答问题时从文档库中检索相关片段的技术模式。

## 核心问题
- 每次查询都从零开始检索，没有知识积累
- 综合多文档时需反复查找和拼凑
- 没有交叉引用和矛盾标记
- 知识没有被"编译"，只是被临时检索

## 适用场景
- NotebookLM
- ChatGPT 文件上传
- 传统 RAG 系统

## 相关概念
- [[C-002-LLM-Wiki|LLM Wiki]]：RAG 的替代方案
- [[C-003-增量编译|增量编译]]：LLM Wiki 的核心机制

## 来源
- [[S-001-LLM知识库方法论|S-001: LLM知识库方法论]]
- [[S-002-Karpathy知识库实践指南|S-002: Karpathy知识库实践指南]]
