# Graph Report - raw/code  (2026-04-08)

## Corpus Check
- Fits in context window

## Summary
- 193 nodes · 269 edges · 9 communities detected
- Extraction: 70% EXTRACTED · 30% INFERRED · 0% AMBIGUOUS · INFERRED: 81 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `KnowledgeCompiler` - 13 edges
2. `UserEntity` - 13 edges
3. `ApiService` - 12 edges
4. `SummaryGenerator` - 10 edges
5. `main()` - 10 edges
6. `Graph` - 9 edges
7. `PathFinder` - 8 edges
8. `ConceptExtractor` - 7 edges
9. `create_sample_graph()` - 7 edges
10. `DataPipeline` - 7 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "数据处理流水线"
Cohesion: 0.06
Nodes (25): DataEnricher, DataPipeline, DataRecord, DataTransformer, DataValidator, main(), Data Processing Pipeline 多阶段数据处理流水线，展示数据转换和验证模式  Author: Demo Code Created: 2026, # HACK: 这里用简单的字符串操作做演示 (+17 more)

### Community 1 - "图算法与数据结构"
Cohesion: 0.08
Nodes (22): CommunityDetector, create_sample_graph(), Graph, GraphEdge, GraphNode, main(), PathFinder, Graph Algorithms Implementation 常用图算法的 Python 实现  展示： - 数据结构设计 - 算法实现 - 复杂度优化 - (+14 more)

### Community 2 - "Go Web 服务"
Cohesion: 0.12
Nodes (14): ApiResponse, CORSMiddleware(), CreateUserRequest, generateID(), InMemoryUserRepository, LoggerMiddleware(), main(), NewInMemoryUserRepository() (+6 more)

### Community 3 - "TypeScript 类型系统"
Cohesion: 0.1
Nodes (3): isSuccess(), UserEntity, UserService

### Community 4 - "文档读取器"
Cohesion: 0.11
Nodes (13): ConceptExtractor, DocumentReader, Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa, # TODO: 使用 NLP 技术改进概念提取, # HACK: 简单实现 - 取第一段或第一个标题, # IMPORTANT: 模板应该可配置, # TODO: 改进例子查找算法, # HACK: 简单实现 - 基于共现 (+5 more)

### Community 5 - "知识库编译器"
Cohesion: 0.31
Nodes (3): KnowledgeCompiler, main(), 保存摘要到 wiki/summaries/

### Community 6 - "Node.js API 服务"
Cohesion: 0.19
Nodes (1): ApiService

### Community 7 - "摘要生成器"
Cohesion: 0.39
Nodes (1): SummaryGenerator

### Community 8 - "HTTP 处理器"
Cohesion: 0.33
Nodes (1): UserHandler

## Knowledge Gaps
- **49 isolated node(s):** `Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa`, `解析 Markdown 的 YAML frontmatter`, `保存摘要到 wiki/summaries/`, `# TODO: 支持更多格式（PDF, DOCX等）`, `# IMPORTANT: 保持原文不变，只读不写` (+44 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `KnowledgeCompiler` connect `知识库编译器` to `文档读取器`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Why does `SummaryGenerator` connect `摘要生成器` to `文档读取器`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `main()` (e.g. with `create_sample_graph()` and `PathFinder`) actually correct?**
  _`main()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa`, `解析 Markdown 的 YAML frontmatter`, `保存摘要到 wiki/summaries/` to the rest of the system?**
  _49 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `数据处理流水线` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `图算法与数据结构` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Go Web 服务` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._