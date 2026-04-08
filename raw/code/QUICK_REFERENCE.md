# Graphify 快速参考卡片

## 🎯 你想做什么？

### 查询代码库
```bash
# 命令行工具（在 raw/code 目录）
graphify query "main modules"
graphify query "data pipeline"
graphify query "user service"

# Claude Code（完整功能）
/graphify query "主要模块是什么？"
/graphify path "类A" "类B"
/graphify explain "类名"
```

### 查看报告
```bash
cat raw/code/graphify-out/GRAPH_REPORT.md
```

### 重新生成图谱
```bash
cd raw/code
graphify . --no-viz
```

## ❗ 重要提示

| 功能 | 命令行 | Claude Code |
|------|--------|-------------|
| 查询 | ✅ graphify query | ✅ /graphify query |
| 路径 | ❌ 不支持 | ✅ /graphify path |
| 解释 | ❌ 不支持 | ✅ /graphify explain |

## 🔑 查询关键词（英文）

| 想找... | 用这些词... |
|---------|------------|
| 主要类 | `main classes`, `core classes` |
| 函数 | `functions`, `methods` |
| 数据处理 | `data pipeline`, `processing` |
| 用户相关 | `user`, `repository`, `service` |
| 算法 | `algorithms`, `graph`, `search` |
| API | `API`, `handler`, `endpoint` |
| 设计意图 | `IMPORTANT`, `HACK`, `TODO`, `NOTE` |

## 📍 目录位置

```bash
/Users/meijie/project/Vault/raw/code/
├── *.py              # Python 代码
├── *.js              # JavaScript 代码
├── *.ts              # TypeScript 代码
├── *.go              # Go 代码
├── *.yaml            # 配置文件
├── README.md         # 说明文档
├── GRAPHIIFY_USAGE.md # 详细使用指南
└── graphify-out/     # 图谱输出
    ├── GRAPH_REPORT.md  # 分析报告
    └── graph.json       # 图谱数据
```

## 💡 常见问题速解

**Q: 中文查询没有结果？**
A: 使用英文关键词，如 `main classes` 而不是 `主要类`

**Q: 提示 "unknown command 'path'"？**
A: 命令行工具不支持 path，需要在 Claude Code 中使用

**Q: 提示 "No graph found"？**
A: 确保在正确目录，或使用 `--graph` 参数指定路径

**Q: 想看完整功能？**
A: 在 Claude Code 中使用 `/graphify` 命令

---

**完整指南**: `[[GRAPHIIFY_USAGE.md|详细使用指南]]`
**示例代码**: `[[README.md|代码示例说明]]`
