---
type: summary
source: "[[raw/articles/xuanyustudioLocalMiniDrama 🎬 开源本地 AI 短剧 & 漫剧生成工具 —— 从故事到成片一站式完成，数据不出本机，短剧工作流管理平台，高灵活度，AI真人剧，AI漫剧本地搞定。 Open-source local AI short drama maker story → storyboard → video, fully offline, your data stays yours. 纳米流水线.md|原始文档]]"
compiled_at: 2026-04-08
status: done
---

# S-008: LocalMiniDrama 本地短剧生成工具

## TL;DR
一个真正能本地离线运行、开箱即用、素材不上云的开源 AI 短剧生成工具，用纯 JavaScript 从零搭建，接入自己的 AI API 即可生成完整短剧。

## 核心结论

1. **真正的本地离线运行** - 数据不出本机，素材不上云，完全自控
2. **完整创作流程** - 故事生成 → 剧本编辑 → 角色生成 → 场景生成 → 道具生成 → 分镜生成 → 图片/视频生成 → 合成视频
3. **多 AI 服务商支持** - 支持阿里云 DashScope、火山引擎 Volcengine、可灵 Kling AI、Google Gemini、Vidu 等多家视频模型
4. **一键流水线** - 补全并生成智能跳过已有内容，失败自动重试，实时进度展示
5. **完全开源可二次开发** - MIT 许可证，纯 JavaScript 编写

## 关键证据

### 技术栈
- 前端：Vue 3 + Vite + Element Plus + Pinia + Axios
- 后端：Node.js + Express + SQLite (better-sqlite3)
- 桌面：Electron 28 + electron-builder
- 语言：纯 JavaScript（无 TypeScript）

### 核心功能亮点
- **工程导出/导入**：完整打包工程为 ZIP（含图片、视频、文字、配置）
- **素材库**：全局角色/场景/道具库，跨项目复用
- **分镜精细编辑**：图片/视频提示词可全文编辑
- **AI 配置**：图片、视频、文本三类模型独立配置
- **多集剧本生成**：支持 1-6 集一次性生成

### 最新版本特性 (v1.2.3)
- 分镜解说旁白（narration）：AI 为每镜输出独立解说字段
- 导出解说 SRT：按分镜顺序与时长累计时间轴导出字幕
- AI 并发生成：支持图片/视频并发（默认各 3 路）

## 概念提取

- [[C-022-LocalMiniDrama|LocalMiniDrama]]：本地短剧生成工具
- [[C-023-纳米流水线|纳米流水线]]：项目的别名
- [[C-024-即梦|即梦]]：字节旗下的图生视频模型

## 疑点/待验证

1. 实际生成的短剧质量如何
2. 不同视频模型的效果对比
3. 与 Seedance API 的成本差异

## 术语表

| 术语 | 定义 |
|------|------|
| 纳米流水线 | LocalMiniDrama 项目的别称 |
| 即梦 | 字节旗下的图生视频模型 |
| 分镜解说旁白 | 与角色对白分离的解说音轨，便于后期 TTS |
|连贯帧模式| 视频帧连贯性模式，确保视频流畅 |
