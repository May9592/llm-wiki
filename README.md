# 个人知识库

基于 Karpathy "LLM Knowledge Bases" 工作流构建的个人知识库系统。

## 快速开始

1. **摄取内容**：将文章/播客/论文放入 `raw/` 对应目录
2. **触发编译**：当 raw/ 新增 5-10 篇时，让 Claude 执行编译
3. **查询知识**：在 Obsidian 中搜索或询问 Claude
4. **健康检查**：每周运行一次健康检查

> 💡 **新手指南**：查看 [使用指南](USER_GUIDE.md) 了解所有可用指令

## 目录说明

```
raw/       原始资料（只读）
wiki/      知识库（LLM 维护）
outputs/   运行时输出
publish/   成品内容
```

## 相关文档

- [实施方案](IMPLEMENTATION_PLAN.md)
- [编译规范](CLAUDE.md)
