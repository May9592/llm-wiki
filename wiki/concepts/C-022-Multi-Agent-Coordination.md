---
type: concept
id: "C-022"
created_at: 2026-04-08
related:
  - [[C-020-AI-Agent|AI Agent]]
  - [[C-021-Agentic-Workflow|Agentic Workflow]]
sources:
  - [[S-014-Agency-Agents集合]]
---

# Multi-Agent Coordination（多代理协同）

## 定义
多个专业 AI Agent 协同工作，通过分工合作完成复杂任务的机制。

## 协同模式

### 1. 串行协同
代理按顺序执行，每个代理的输出成为下一个代理的输入。
**示例**：Backend Architect（设计）→ Frontend Developer（实现）→ Evidence Collector（测试）

### 2. 并行协同
多个代理同时工作，各自负责不同方面。
**示例**：UI Designer + UX Researcher + Brand Guardian 同时设计产品界面

### 3. 层级协同
一个主代理协调多个子代理。
**示例**：Agents Orchestrator 协调 8 个部门代理完成产品发现

### 4. 功能协同
根据任务动态选择代理。
**示例**：根据代码类型自动选择 Frontend/Backend/Mobile Developer

## 真实场景示例

**初创 MVP 构建**：
1. Frontend Developer - React 应用
2. Backend Architect - API 和数据库
3. Growth Hacker - 用户获取计划
4. Rapid Prototyper - 快速迭代
5. Reality Checker - 质量把关

**企业功能开发**：
1. Senior Project Manager - 范围和任务规划
2. Senior Developer - 复杂实现
3. UI Designer - 设计系统和组件
4. Experiment Tracker - A/B 测试
5. Evidence Collector - 质量验证

## 协同挑战
- **冲突解决**：代理间意见不一致时的决策机制
- **上下文传递**：代理间信息共享的有效性
- **责任边界**：明确每个代理的职责范围

## 相关概念
- [[C-020-AI-Agent|AI Agent]]：协同的基本单元
- [[C-021-Agentic-Workflow|Agentic Workflow]]：单个代理的工作流程

## 来源
- [[S-014-Agency-Agents集合|S-014: Agency Agents集合]]
