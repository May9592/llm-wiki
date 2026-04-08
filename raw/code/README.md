# Code Examples for Graphify Demo

这是一个用于展示 **Graphify 知识图谱功能**的代码示例集合。

## 📁 文件列表

| 文件 | 语言 | 描述 | 主要展示 |
|------|------|------|----------|
| `knowledge_compiler.py` | Python | 知识库编译器 | 设计意图、模块协调 |
| `data_processor.py` | Python | 数据处理流水线 | 设计模式、数据流 |
| `algorithms.py` | Python | 图算法实现 | 算法、数据结构 |
| `api_service.js` | JavaScript | RESTful API 服务 | 异步编程、中间件 |
| `types.ts` | TypeScript | 类型定义 | 类型系统、接口 |
| `web_server.go` | Go | Web 服务器 | 并发、接口设计 |
| `config.yaml` | YAML | 应用配置 | 配置管理 |

## 🎯 设计意图标记

所有代码都包含了丰富的设计意图注释，用于展示 Graphify 的自动提取功能：

- **NOTE**: 一般性说明
- **IMPORTANT**: 重要设计原则
- **HACK**: 临时解决方案或已知问题
- **TODO**: 计划改进的地方
- **WHY**: 设计决策的原因

## 🔍 代码特点

### 1. 多语言支持
展示 Graphify 对不同编程语言的支持：
- Python (3 个文件)
- JavaScript/Node.js
- TypeScript
- Go
- YAML 配置文件

### 2. 多种编程模式
- **面向对象**: 类、继承、接口
- **函数式**: 高阶函数、纯函数
- **并发**: goroutine、async/await
- **设计模式**: 工厂、策略、中间件

### 3. 丰富的关系类型
- 函数调用关系
- 类继承关系
- 模块依赖关系
- 数据流关系

## 🚀 使用方法

### 生成知识图谱

```bash
# 基础运行（仅 AST 分析，无 LLM 成本）
cd raw/code
graphify . --no-viz

# 生成可视化
graphify . --html
```

### 查询知识图谱

**命令行方式**（仅支持 query）：
```bash
cd raw/code

# 查询主要模块（使用英文关键词）
graphify query "main modules"
graphify query "data processing"
graphify query "user service"
graphify query "graph algorithms"

# 深度优先搜索
graphify query "pipeline" --dfs
```

**Claude Code 方式**（完整功能）：
```bash
# 在 Claude Code 对话中
/graphify query "数据处理流程"
/graphify path "DocumentReader" "SummaryGenerator"
/graphify explain "UserRepository"
```

### 示例查询

```bash
# 了解架构
graphify query "这个代码库的主要模块是什么？"

# 查找设计意图
graphify query "为什么使用 dataclass 而不是普通类？"

# 发现技术债务
graphify query "代码中有哪些 HACK 和 TODO？"

# 跨语言关系
graphify query "Python 和 Go 代码中都有哪些用户管理功能？"
```

## 📊 预期结果

运行 Graphify 后，你应该能看到：

### 节点类型
- **45+ 个类/函数节点**
- **7 个文件节点**
- **多个设计意图节点**

### 关系类型
- **调用关系**: 函数和方法调用
- **包含关系**: 文件包含类/函数
- **继承关系**: 类继承和接口实现
- **设计意图**: rationale_for 关系

### 社区划分
Leiden 算法应该能识别出以下社区：
- **数据处理**: data_processor.py 中的类
- **算法实现**: algorithms.py 中的图算法
- **API 服务**: api_service.js 和 web_server.go
- **类型系统**: types.ts 中的接口和类
- **知识管理**: knowledge_compiler.py

## 🎓 学习价值

这些示例展示了：
1. **生产级代码**: 包含错误处理、日志、配置等
2. **最佳实践**: 设计模式、代码组织、命名规范
3. **文档化**: 丰富的注释说明设计意图
4. **可维护性**: 清晰的结构和模块化

## 📝 代码统计

```
Language      Files    Lines    Code    Comments
------------  ------  ------  ------  --------
Python            3     800     500       300
JavaScript        1     350     250       100
TypeScript        1     450     300       150
Go                1     400     280       120
YAML              1     250     250         0
------------  ------  ------  ------  --------
Total             7    2250    1580       670
```

## 🔗 相关文档

- `[[../../GRAPHIFY_USER_GUIDE|Graphify 用户指南]]`
- `[[../../GRAPHIFY_TEST_REPORT|测试报告]]`
- `[[../../wiki/summaries/S-016-Graphify知识图谱工具完整指南|S-016: Graphify 指南]]`

---

**创建时间**: 2026-04-08
**用途**: Graphify 功能演示和测试
**状态**: ✅ 可用于生成知识图谱
