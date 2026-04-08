# Graphify 使用方式对比

## 🎯 核心要点

**Graphify 有两种使用方式，功能完全不同：**

1. **命令行工具** (`graphify`) - 只能查询已存在的图谱
2. **Claude Code Skill** (`/graphify`) - 完整的图谱生成和查询功能

## 📊 功能对比表

| 功能 | 命令行工具 | Claude Code Skill |
|------|-----------|-------------------|
| **生成图谱** | ❌ 不支持 | ✅ `/graphify <path>` |
| **查询图谱** | ✅ `graphify query` | ✅ `/graphify query` |
| **路径查找** | ❌ 不支持 | ✅ `/graphify path` |
| **节点解释** | ❌ 不支持 | ✅ `/graphify explain` |
| **HTML 可视化** | ❌ 不支持 | ✅ `--html` |
| **SVG 导出** | ❌ 不支持 | ✅ `--svg` |
| **增量更新** | ❌ 不支持 | ✅ `--update` |
| **性能测试** | ✅ `graphify benchmark` | ✅ 内置 |

## 🔧 命令行工具详情

### 安装位置
```bash
which graphify
# 输出: /Users/meijie/.local/bin/graphify
```

### 可用命令
```bash
graphify --help
# Commands:
#   query       - 查询现有图谱
#   benchmark   - 性能测试
#   hook        - Git hooks 管理
#   install     - 安装技能到平台
#   claude/codex/... - 平台集成
```

### 正确使用方式

```bash
# ✅ 查询已存在的图谱
cd raw/code
graphify query "main modules"
graphify query "data pipeline"

# ✅ 使用选项
graphify query "pipeline" --dfs
graphify query "class" --budget 1000
graphify query "service" --graph path/to/graph.json

# ✅ 性能测试
graphify benchmark graphify-out/graph.json

# ✅ Git hooks 管理
graphify hook install
graphify hook status
```

### 错误示例

```bash
# ❌ 这些命令不存在
graphify . --no-viz
graphify . --html
graphify path "A" "B"
graphify explain "Node"
```

## 🤖 Claude Code Skill 详情

### 激活方式
在 Claude Code 对话中直接输入：
```bash
/graphify
```

### 可用功能

#### 生成图谱
```bash
# 基础生成
/graphify raw/code

# 只生成报告
/graphify raw/code --no-viz

# 生成可视化
/graphify raw/code --html
/graphify raw/code --svg

# 增量更新
/graphify raw/code --update

# 深度模式（更多推断）
/graphify raw/code --mode deep
```

#### 查询功能
```bash
# 查询问题
/graphify query "主要模块是什么？"
/graphify query "数据处理流程"
/graphify query "设计原则"

# 路径查找
/graphify path "KnowledgeCompiler" "SummaryGenerator"
/graphify path "DocumentReader" "DataPipeline"

# 节点解释
/graphify explain "DataPipeline"
/graphify explain "KnowledgeCompiler"
```

#### 高级功能
```bash
# 生成 Wiki
/graphify raw/code --wiki

# 导出 Neo4j
/graphify raw/code --neo4j

# 启动 MCP 服务器
/graphify raw/code --mcp

# 文件监控
/graphify raw/code --watch
```

## 🎓 使用场景

### 场景 1: 首次生成图谱

**❌ 错误做法**：
```bash
cd raw/code
graphify . --no-viz  # 命令不存在
```

**✅ 正确做法**：
在 Claude Code 中输入：
```bash
/graphify raw/code --no-viz
```

### 场景 2: 查询已存在的图谱

**方式 1: 使用命令行工具** ✅
```bash
cd raw/code
graphify query "main modules"
```

**方式 2: 使用 Claude Code** ✅
```bash
/graphify query "主要模块"
```

### 场景 3: 更新现有图谱

**❌ 错误做法**：
```bash
graphify raw/code --update  # 命令不存在
```

**✅ 正确做法**：
在 Claude Code 中输入：
```bash
/graphify raw/code --update
```

## 📁 文件结构

```bash
raw/code/
├── *.py, *.js, *.ts, *.go    # 源代码
├── graphify-out/             # 输出目录
│   ├── GRAPH_REPORT.md       # 分析报告
│   ├── graph.json            # 图谱数据（用于查询）
│   └── cache/                # SHA256 缓存
└── CLI_VS_SKILL.md           # 本文档
```

## 🔍 如何判断使用哪种方式？

### 使用命令行工具的情况：
- ✅ 图谱已经生成（graph.json 存在）
- ✅ 只需要查询信息
- ✅ 不在 Claude Code 环境中

### 使用 Claude Code Skill 的情况：
- ✅ 需要生成新图谱
- ✅ 需要更新现有图谱
- ✅ 需要可视化
- ✅ 需要路径查找或节点解释
- ✅ 在 Claude Code 对话中

## 💡 快速参考

| 任务 | 命令 | 环境 |
|------|------|------|
| 生成图谱 | `/graphify .` | Claude Code |
| 查询图谱 | `graphify query "..."` | 命令行 |
| 查询图谱 | `/graphify query "..."` | Claude Code |
| 路径查找 | `/graphify path "A" "B"` | Claude Code |
| 节点解释 | `/graphify explain "X"` | Claude Code |
| 性能测试 | `graphify benchmark` | 命令行 |

## ⚠️ 常见错误和解决方案

### 错误 1: "unknown command"
```bash
# ❌ 错误
$ graphify . --no-viz
error: unknown command '.'

# ✅ 解决
# 在 Claude Code 中使用
/graphify . --no-viz
```

### 错误 2: "No graph found"
```bash
# ❌ 错误
$ graphify query "modules"
Error: No graph found

# ✅ 解决
# 先生成图谱（在 Claude Code 中）
/graphify raw/code

# 然后查询
$ graphify query "modules"
```

### 错误 3: 在错误的目录
```bash
# ❌ 错误
$ cd /tmp
$ graphify query "modules"
Error: No graph found

# ✅ 解决
$ cd /Users/meijie/project/Vault/raw/code
$ graphify query "modules"
```

---

**最后更新**: 2026-04-08
**文档版本**: 1.0
