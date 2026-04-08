# 项目 Skills 配置说明

**最后更新**: 2026-04-08  
**项目**: LLM Wiki Knowledge Base System

## 📁 目录结构

### 项目配置目录
```
.claude/
├── skills/      # 空目录 - 无项目特定 skills
├── agents/      # 空目录 - 无项目特定 agents  
├── commands/    # 空目录 - 无项目特定 commands
└── settings.json # 项目权限配置
```

### 全局配置（已安装）
```
~/.claude/
├── skills/
│   └── graphify/    # ✅ Graphify skill
│       └── SKILL.md
└── CLAUDE.md        # 全局配置文件
```

## 🔧 当前配置

### 已安装的 Skills

#### 1. Graphify Skill（全局）

**触发命令**: `/graphify`

**功能**: 将任何文件夹转换为可查询的知识图谱

**安装位置**: `~/.claude/skills/graphify/SKILL.md`

**用途**:
- 代码知识图谱构建
- 多模态内容分析（代码、文档、PDF、图片）
- AST 结构提取
- 设计意图提取
- 社区发现和分析

**使用方式**:
```bash
# 在 Claude Code 中
/graphify raw/code              # 生成图谱
/graphify raw/code --no-viz     # 只生成报告
/graphify query "main modules"  # 查询图谱
/graphify path "A" "B"          # 路径查找
/graphify explain "Node"        # 节点解释
```

### 项目规范（在 CLAUDE.md 中）

#### 核心角色
```
你是这个知识库的"编译器"
任务：将 raw/ 中的原始资料编译成 wiki/ 中的结构化知识
```

#### 主要功能
1. **逐篇摘要** - 生成文档摘要到 `wiki/summaries/`
2. **概念抽取** - 提取概念到 `wiki/concepts/`
3. **索引维护** - 更新 `wiki/indexes/`
4. **健康检查** - 每周检查知识库质量
5. **Graphify 集成** - 代码知识图谱构建

## 📊 项目配置统计

| 配置类型 | 数量 | 说明 |
|---------|------|------|
| **全局 Skills** | 1 | Graphify |
| **项目 Skills** | 0 | 无项目特定 skills |
| **项目 Agents** | 0 | 无项目特定 agents |
| **项目 Commands** | 0 | 无项目特定 commands |
| **权限配置** | 69 | Git、文件操作、Graphify 等 |

## 🧹 清理记录

### 已删除的功能
- ❌ **Discussion Processor** - 已从项目中移除
- ❌ **Problems/Solutions** - 已从项目中移除
- ❌ 相关权限配置 - 已从 `settings.json` 清理

### 当前状态
- ✅ 配置文件已清理
- ✅ 无遗留权限引用
- ✅ 项目目录结构干净

## 🎯 使用指南

### 激活 Graphify
Graphify skill 已全局安装，在 Claude Code 中直接使用：

```bash
# 生成知识图谱
/graphify raw/code

# 查询现有图谱
/graphify query "data pipeline"
/graphify path "KnowledgeCompiler" "SummaryGenerator"
/graphify explain "DataPipeline"
```

### 命令行查询
在项目目录中使用命令行工具：

```bash
cd raw/code
graphify query "main classes"
graphify query "data processing"
```

## 📝 自定义 Skills

如果需要添加项目特定的 skills：

1. 在 `.claude/skills/` 中创建 `SKILL.md`
2. 定义触发命令和功能
3. 配置权限（如需要）

**注意**: 当前项目使用全局 Graphify skill，无需额外配置。

## 🔗 相关文档

- `[[CLAUDE.md|项目规范]]` - 知识库编译规范
- `[[raw/code/README.md|代码示例说明]]` - Graphify 代码示例
- `[[raw/code/CLI_VS_SKILL.md|CLI vs Skill 对比]]` - 使用方式对比
- `[[raw/code/QUICK_REFERENCE.md|快速参考]]` - 命令速查

---

**配置状态**: ✅ 干净、最新  
**最后清理**: 2026-04-08  
**维护者**: 项目管理员
