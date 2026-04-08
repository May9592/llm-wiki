---
type: summary
source: "[[raw/articles/harry0703MoneyPrinterTurbo 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM..md|原始文档]]"
compiled_at: 2026-04-08
status: done
---

# S-007: MoneyPrinterTurbo 一键短视频生成

## TL;DR
一个完整的 MVC 架构短视频自动化生成工具，只需提供主题或关键词即可全自动生成文案、素材、字幕、背景音乐并合成高清视频。

## 核心结论

1. **完整的自动化工作流** - 从文案到成片全自动，支持 AI 自动生成文案或自定义文案
2. **多模型支持** - 支持 OpenAI、Moonshot、Azure、通义千问、Google Gemini、Ollama、DeepSeek、MiniMax、文心一言等多种 LLM 接入
3. **批量生成能力** - 支持批量视频生成，可一次生成多个视频选择最满意的
4. **灵活的配置选项** - 支持多种视频尺寸、语音合成、字幕样式、背景音乐等配置
5. **国内用户友好** - 推荐使用 DeepSeek 或 Moonshot（国内可直接访问）

## 关键证据

### 技术架构
- 完整的 MVC 架构，代码结构清晰，易于维护
- 支持 API 和 Web 界面两种使用方式
- 支持 Docker 部署、Windows 一键启动包、本地部署等多种安装方式

### 功能特性
- 支持中文和英文视频文案
- 支持多种语音合成，可实时试听
- 支持字幕生成，可调整字体、位置、颜色、大小、描边
- 支持背景音乐，随机或指定音乐文件，可设置音量
- 视频素材来源高清且无版权，也可使用本地素材

### 语音合成
- 支持 edge 和 whisper 两种字幕生成方式
- edge：速度快，性能好，质量可能不稳定
- whisper：速度慢，质量更可靠，需下载约 3GB 模型文件

## 概念提取

- [[C-020-MoneyPrinterTurbo|MoneyPrinterTurbo]]：一键短视频生成工具
- [[C-021-MVC架构|MVC 架构]]：项目采用的设计模式

## 疑点/待验证

1. 实际生成视频的质量如何
2. 不同 LLM 提供商对生成效果的影响
3. 批量生成的效率如何

## 术语表

| 术语 | 定义 |
|------|------|
| MVC 架构 | Model-View-Controller 设计模式，分离数据、界面和逻辑 |
| Pexels | 免费高清视频素材平台 |
| ImageMagick | 图片处理软件，用于视频合成 |
| Whisper | OpenAI 的语音识别模型 |
