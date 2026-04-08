# Claude 知识库编译规范

## 角色
你是这个知识库的"编译器"。你的任务是将 `raw/` 中的原始资料编译成 `wiki/` 中的结构化知识。

## 核心原则

### 分层原则
- `raw/` - 原始资料，只读，不修改
  - `articles/` - 文章、论文
- `wiki/` - 编译产物，由你维护
  - `summaries/` - 文档摘要
  - `concepts/` - 概念条目
- `outputs/` - 运行时输出
  - `qa/` - 问答归档
  - `research/` - 研究笔记

### 增量编译
只处理 `raw/` 中新增或变更的内容。通过 `ingested_at` 字段识别新内容。

### 可追溯性
每个知识条目必须包含来源引用，格式：`[[wiki/summaries/S-编号-标题|S-编号: 标题]]`

## 编译流程

### 1. 逐篇摘要
对 `raw/` 中的新文档生成摘要，存入 `wiki/summaries/`

**输出格式**：参考 `templates/summary.md`

**命名规范**：`S-{编号}-{标题}.md`，编号从 001 开始

**必须包含**：
- TL;DR（一句话总结）
- 核心结论（3-5 点）
- 关键证据
- 概念提取（双向链接）
- 疑点/待验证

### 2. 概念抽取
从摘要中提取概念，存入 `wiki/concepts/`

**输出格式**：参考 `templates/concept.md`

**命名规范**：`C-{编号}-{名称}.md`，编号从 001 开始

**判断标准**：
- 专业术语/技术概念
- 反复出现的关键词
- 值得独立解释的观点

**必须包含**：
- 清晰定义
- 核心特征
- 具体例子
- 来源引用

### 3. 索引维护
自动更新 `wiki/indexes/` 中的索引文件

**All-Sources.md**：所有已处理的原始资料清单
**All-Concepts.md**：所有概念条目的索引
**Glossary.md**：术语对照表

## 问答输出规范

当用户对知识库提出复杂问题时：
1. 先查询 `wiki/indexes/` 定位相关内容
2. 阅读相关摘要和概念
3. 生成结构化回答
4. 将问答结果存入 `outputs/qa/`

**输出格式**：参考 `templates/qa.md`

## 健康检查规范

每周执行一次健康检查，输出到 `outputs/health/Health-{YYYY-MM-DD}.md`

**检查项目**：

1. **一致性检查**
   - 同一概念在多处定义是否冲突
   - 相同结论是否有矛盾

2. **完整性检查**
   - 概念条目是否缺定义
   - 摘要是否缺核心结论
   - 是否有空白模板

3. **孤岛检测**
   - 入链出链少于 2 的笔记
   - 建议应该建立的链接

## 命名规范

| 类型 | 前缀 | 编号 | 示例 |
|------|------|------|------|
| 摘要 | S | 001-999 | S-001-RAG入门.md |
| 概念 | C | 001-999 | C-001-检索增强生成.md |
| 问答 | QA | YYYY-MM-DD | QA-2026-04-08-RAG边界.md |
| 健康报告 | Health | YYYY-MM-DD | Health-2026-04-08.md |

### 4. Graphify 集成（代码知识图谱）

支持代码文件的知识图谱构建，增强知识库的完整性。

#### 目录结构
- `raw/code/` - 代码文件（Python, JavaScript, TypeScript 等）
- `wiki/graphify/structure/` - 代码结构信息
- `wiki/graphify/reports/` - 图谱分析报告

#### 触发方式
当检测到 `raw/code/` 中有新代码时：
1. 运行 `/graphify ./raw/code --no-viz`
2. 分析生成的 `GRAPH_REPORT.md`
3. 提取关键概念和关系
4. 与现有概念体系集成

#### 提取内容
- **类和函数结构** - 通过 AST 分析
- **设计意图** - 从注释中提取 (NOTE, IMPORTANT, HACK, TODO)
- **调用关系** - 函数间的依赖关系
- **跨文件引用** - import 和 require 关系

#### 集成到 Wiki
将代码概念转换为 Wiki 概念条目：
- 代码类 → `C-XXX-类名.md`
- 重要函数 → `C-XXX-函数名.md`  
- 设计模式 → `C-XXX-模式名.md`

#### 使用场景
- 理解代码库结构
- 追踪设计决策
- 发现代码与文档的对应关系

## 双向链接规范

### 路径规则（重要）
Obsidian Wiki Links 默认从 Vault 根目录查找文件。因此链接必须包含相对于根目录的完整路径。

### 正确格式

| 引用类型 | 格式 | 示例 |
|----------|------|------|
| 摘要 | `[[wiki/summaries/S-编号-标题\|显示文本]]` | `[[wiki/summaries/S-001-LLM知识库方法论\|S-001: LLM知识库方法论]]` |
| 概念 | `[[wiki/concepts/C-编号-名称\|显示文本]]` | `[[wiki/concepts/C-001-RAG\|C-001: RAG]]` |
| 原始文档 | `[[raw/articles/文件名\|显示文本]]` | `[[raw/articles/llm-wiki.md\|原始文档]]` |

### Frontmatter 中的链接
```yaml
sources:
  - [[wiki/summaries/S-001-LLM知识库方法论]]
  - [[wiki/summaries/S-002-Karpathy知识库实践指南]]
related:
  - [[wiki/concepts/C-002-LLM-Wiki|LLM Wiki]]
```

### 正文中的链接
```markdown
## 来源
- [[wiki/summaries/S-001-LLM知识库方法论|S-001: LLM知识库方法论]]

## 相关概念
- [[wiki/concepts/C-002-LLM-Wiki|LLM Wiki]]：相关说明
```

### 链接格式说明
- `[[文件路径]]` - 基本链接，显示文件名
- `[[文件路径|显示文本]]` - 带别名的链接，显示自定义文本
- 显示文本可以包含冒号、空格等任意字符

## 注意事项

1. **不要修改 raw/ 中的任何文件**
2. **保持客观，摘要要准确反映原文**
3. **不确定的内容标注为"待验证"**
4. **每次编译前先读取 CLAUDE.md**
5. **新增支持**：Graphify 集成时，代码文件放在 `raw/code/` 目录
