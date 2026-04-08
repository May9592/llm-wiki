---
type: summary
source: "[[raw/articles/Karpathy 最新分享：用 LLM 搭建个人知识库，告别 RAG 的低效循环.md]]"
compiled_at: 2026-04-08
status: done
---

# S-002: Karpathy 知识库实践指南

## TL;DR
基于 Karpathy 的 llm-wiki 方法论，使用 Obsidian + Claude 构建个人知识库的完整实操指南。

## 核心结论

### RAG 的低效循环
- 每次提问都从头搜寻知识
- 综合多文档时现场找碎片、现场拼
- 没有知识沉淀和积累

### 实操工具链
1. **Obsidian Web Clipper**：网页素材采集
2. **图片本地化**：Ctrl+Shift+D 快捷键下载附件
3. **Graph View**：可视化的知识图谱
4. **Git 版本管理**：自动备份和完整历史
5. **Dataview**（可选）：元数据查询
6. **Marp**（可选）：Markdown 幻灯片
7. **qmd**（可选）：本地 Markdown 搜索引擎

### 配置要点
- 附件存储路径：当前文件夹下的 `attachments/`
- 下载快捷键：Ctrl+Shift+D
- Git 自动提交间隔：10 分钟

## 关键证据

### Graph View 两个核心用途
1. **Lint 健康检查**：发现孤岛页面
2. **知识盲区发现**：灰色幽灵节点提醒缺失专页

### 为什么这套方法有效
> 维护知识库最痛苦的不是阅读和思考，而是记录。更新交叉引用、保持摘要最新、标注新旧矛盾、维护一致性。AI 不会厌倦，不会忘记，一次操作可以碰十五个文件。维护成本趋近于零。

## 概念提取
- [[C-002-LLM-Wiki|LLM Wiki]]
- [[C-005-Obsidian-Web-Clipper|Obsidian Web Clipper]]
- [[C-006-Graph-View|Graph View]]
- [[C-007-双向链接|双向链接]]

## 疑点/待验证
- Dataview 和 Marp 的实际使用频率如何？

## 术语表
| 术语 | 定义 |
|------|------|
| Graph View | Obsidian 的图谱视图，展示页面间链接关系 |
| 双向链接 | [[链接]] 格式的内部引用 |
| 幽灵节点 | 被多次提及但没有独立页面的概念 |
