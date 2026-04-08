# Graphify 命令行使用指南

> **重要提示**: Graphify 有两种使用方式
> 1. **命令行工具** - 只支持 `query` 命令
> 2. **Claude Code Skill** - 支持 `query`, `path`, `explain` 等完整功能

## ❌ 常见错误

### 错误 1: 使用不存在的命令
```bash
# ❌ 命令行工具不支持这些命令
graphify path "KnowledgeCompiler" "SummaryGenerator"
graphify explain "DataPipeline"
# 输出: error: unknown command 'path'
```

### 错误 2: 中文查询无结果

### 错误 1: 中文查询无结果
```bash
# ❌ 这不会工作
graphify query "这个代码库的主要模块是什么？"
# 输出: No matching nodes found
```

### 错误 2: 目录不正确
```bash
# ❌ 如果不在正确的目录
cd /some/other/place
graphify query "modules"
# 输出: Error: No graph found
```

## ✅ 方式1: 命令行工具（仅 query）

### 支持的命令
```bash
graphify query "<question>" [options]

选项:
  --dfs              使用深度优先搜索（默认广度优先）
  --budget N         限制输出 token 数（默认 2000）
  --graph <path>     指定图谱文件路径（默认 graphify-out/graph.json）
```

### 正确的查询示例
```bash
# ✅ 查询主要模块
graphify query "main modules"

# ✅ 查询数据处理
graphify query "data processing pipeline"

# ✅ 查询用户服务
graphify query "user service repository"

# ✅ 查询算法
graphify query "graph algorithms"

# ✅ 查询 API
graphify query "API service handler"

# ✅ 使用深度优先搜索
graphify query "pipeline" --dfs

# ✅ 限制输出
graphify query "class" --budget 1000
```

### 在哪里执行
```bash
# 必须在包含 graphify-out 目录的地方
cd /Users/meijie/project/Vault/raw/code
# 或指定图谱路径
graphify query "modules" --graph /Users/meijie/project/Vault/raw/code/graphify-out/graph.json
```

## ✅ 方式2: Claude Code Skill（完整功能）

在 Claude Code 中使用，支持所有功能：

```bash
# 在 Claude Code 对话中输入
/graphify query "main modules"
/graphify path "KnowledgeCompiler" "SummaryGenerator"
/graphify explain "DataPipeline"
```

### Skill 功能对比

| 功能 | 命令行工具 | Claude Code Skill |
|------|-----------|-------------------|
| query 查询 | ✅ 支持 | ✅ 支持 |
| path 路径查找 | ❌ 不支持 | ✅ 支持 |
| explain 解释 | ❌ 不支持 | ✅ 支持 |
| --dfs 选项 | ✅ 支持 | ✅ 支持 |
| --budget 选项 | ✅ 支持 | ✅ 支持 |

## 📝 推荐的查询命令

### 了解架构
```bash
# 主要组件
graphify query "main classes"

# 核心功能
graphify query "core functions"

# 数据流
graphify query "data flow"
```

### 查找设计意图
```bash
# 查找重要注释
graphify query "IMPORTANT"

# 查找技术债务
graphify query "HACK"

# 查找待办事项
graphify query "TODO"
```

### 跨语言查询
```bash
# Python 代码
graphify query "Python class"

# Go 代码
graphify query "Go handler"

# JavaScript 代码
graphify query "API service"
```

## 🔧 高级用法

### 指定图谱路径
```bash
# 使用特定的图谱文件
graphify query "modules" --graph raw/code/graphify-out/graph.json
```

### 限制输出
```bash
# 限制返回的节点数
graphify query "class" --limit 10
```

### 使用 DFS 遍历
```bash
# 深度优先搜索
graphify query "pipeline" --dfs
```

## 💡 实用技巧

### 1. 先读取报告
在查询前，先阅读生成的报告：
```bash
cat raw/code/graphify-out/GRAPH_REPORT.md
```

### 2. 使用节点 ID
如果知道确切的节点 ID：
```bash
graphify explain "KnowledgeCompiler"
```

### 3. 组合查询
先用宽泛查询，再用具体查询：
```bash
# 第一步：宽泛查询
graphify query "pipeline"

# 第二步：基于结果的具体查询
graphify explain "DataPipeline"
```

## 🌐 中文内容的处理

虽然查询需要用英文，但图谱中包含中文内容：

1. **设计意图注释**（中文）会被提取
2. **节点标签**可能包含中文
3. **查询关键词**需要用英文

示例：
```bash
# 注释中有中文 "数据处理流水线 - 协调整个处理流程"
# 但查询要用英文：
graphify query "pipeline coordinator"
```

## 📊 可用的图谱文件

```bash
# 查看所有图谱文件
ls -lh raw/code/graphify-out/

# 主要文件：
# - GRAPH_REPORT.md    人类可读的报告
# - graph.json         可查询的图谱数据
# - cache/             SHA256 缓存目录
```

## 🆘 故障排除

### 问题 1: "No matching nodes found"
**解决**: 使用英文关键词，尝试更通用的术语

### 问题 2: "No graph found"
**解决**: 确保在正确的目录，或使用 `--graph` 参数指定路径

### 问题 3: 命令不存在
**解决**:
```bash
# 检查安装
which graphify

# 如果没有安装
pip install graphifyy -q --break-system-packages
```

### 问题 4: 权限错误
**解决**:
```bash
# 使用完整路径
/Users/meijie/.local/bin/graphify query "modules"
```

## 📖 快速参考卡片

| 想知道... | 使用命令... | 示例 |
|-----------|------------|------|
| 主要模块 | `graphify query "main modules"` | 英文关键词 |
| 节点关系 | `graphify path "A" "B"` | 精确节点名 |
| 节点详情 | `graphify explain "NodeName"` | 大小写敏感 |
| 设计意图 | `graphify query "IMPORTANT HACK"` | 注释标记 |

---

**最后更新**: 2026-04-08
**Graphify 版本**: 0.3.12
**语言支持**: 查询用英文，内容支持中文
