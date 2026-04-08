# Graph Report - raw/code  (2026-04-08)

## Corpus Check
- Small corpus

## Summary
- 45 nodes · 73 edges · 7 communities detected
- Extraction: 60% EXTRACTED · 40% INFERRED · 0% AMBIGUOUS · INFERRED: 29 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `KnowledgeCompiler` - 13 edges
2. `SummaryGenerator` - 10 edges
3. `ConceptExtractor` - 7 edges
4. `DocumentReader` - 5 edges
5. `main()` - 3 edges
6. `Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa` - 1 edges
7. `解析 Markdown 的 YAML frontmatter` - 1 edges
8. `保存摘要到 wiki/summaries/` - 1 edges
9. `# TODO: 支持更多格式（PDF, DOCX等）` - 1 edges
10. `# IMPORTANT: 保持原文不变，只读不写` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "文档与设计意图"
Cohesion: 0.18
Nodes (10): Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa, # TODO: 使用 NLP 技术改进概念提取, # HACK: 简单实现 - 取第一段或第一个标题, # IMPORTANT: 模板应该可配置, # TODO: 改进例子查找算法, # HACK: 简单实现 - 基于共现, # TODO: 支持更多格式（PDF, DOCX等）, # HACK: 简单实现 - 实际应该从现有文件中获取最大编号 (+2 more)

### Community 1 - "摘要生成模块"
Cohesion: 0.39
Nodes (1): SummaryGenerator

### Community 2 - "文档读取模块"
Cohesion: 0.4
Nodes (2): DocumentReader, 解析 Markdown 的 YAML frontmatter

### Community 3 - "概念提取模块"
Cohesion: 0.53
Nodes (1): ConceptExtractor

### Community 4 - "核心编译器"
Cohesion: 0.6
Nodes (2): KnowledgeCompiler, main()

### Community 5 - "输出格式化"
Cohesion: 0.67
Nodes (1): 保存摘要到 wiki/summaries/

### Community 6 - "编译执行"
Cohesion: 0.67
Nodes (0): 

## Knowledge Gaps
- **12 isolated node(s):** `Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa`, `解析 Markdown 的 YAML frontmatter`, `保存摘要到 wiki/summaries/`, `# TODO: 支持更多格式（PDF, DOCX等）`, `# IMPORTANT: 保持原文不变，只读不写` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `KnowledgeCompiler` connect `核心编译器` to `文档与设计意图`, `文档读取模块`, `输出格式化`, `编译执行`?**
  _High betweenness centrality (0.298) - this node is a cross-community bridge._
- **Why does `SummaryGenerator` connect `摘要生成模块` to `文档与设计意图`, `文档读取模块`?**
  _High betweenness centrality (0.239) - this node is a cross-community bridge._
- **Why does `ConceptExtractor` connect `概念提取模块` to `文档与设计意图`, `文档读取模块`?**
  _High betweenness centrality (0.150) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `main()` (e.g. with `KnowledgeCompiler` and `.compile()`) actually correct?**
  _`main()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Knowledge Base Compiler 编译知识库的核心模块，负责将原始资料转换为结构化知识。  主要功能： - 读取原始文档（articles, pa`, `解析 Markdown 的 YAML frontmatter`, `保存摘要到 wiki/summaries/` to the rest of the system?**
  _12 weakly-connected nodes found - possible documentation gaps or missing edges._