---
type: summary
source: "[[raw/articles/modelscopeFunClip Open-source, accurate and easy-to-use video speech recognition & clipping tool, LLM based AI clipping intergrated..md|原始文档]]"
compiled_at: 2026-04-08
status: done
---

# S-013: FunClip 视频语音识别剪辑

## TL;DR
完全开源、本地部署的自动化视频剪辑工具，基于阿里通义语音实验室的 Paraformer 模型进行语音识别，支持 LLM 智能剪辑。

## 核心结论

1. **工业级 ASR 模型** - 集成 Paraformer-Large，超过 1300 万次下载，可准确预测时间戳
2. **热词定制** - 集成 SeACo-Paraformer 热词定制功能，可指定实体词、名字等作为热词
3. **说话人识别** - 集成 CAM++ 说话人识别模型，可按说话人 ID 剪辑特定说话人的片段
4. **LLM 智能剪辑** - 支持使用大语言模型（qwen、GPT 等）进行智能剪辑
5. **多段自由剪辑** - 支持多段自由剪辑，自动返回完整视频 SRT 字幕和目标片段 SRT 字幕

## 关键证据

### 核心功能
- 语音识别：基于 FunASR Paraformer 系列
- 热词定制：增强特定词汇识别效果
- 说话人识别：自动识别并标注说话人
- 智能剪辑：LLM 自动提取剪辑时间戳
- 字幕生成：自动生成 SRT 格式字幕

### 技术栈
- FunASR：语音识别框架
- Paraformer-Large：工业级中文 ASR 模型
- SeACo-Paraformer：热词定制模型
- CAM++：说话人识别模型
- Gradio：交互界面

### 使用方式
1. 本地 Gradio 服务
2. ModelScope Space 在线体验
3. 命令行使用

## 概念提取

- [[C-036-FunClip|FunClip]]：视频语音识别剪辑工具
- [[C-037-Paraformer|Paraformer]]：阿里非自回归端到端语音识别模型
- [[C-038-热词定制|热词定制]]：增强特定词汇识别效果的技术

## 疑点/待验证

1. 英文识别的效果如何
2. LLM 剪辑的准确性
3. 多说话人场景的识别准确度

## 术语表

| 术语 | 定义 |
|------|------|
| Paraformer | 阿里非自回归端到端语音识别模型 |
| 热词定制 | 指定某些词作为热词，增强识别效果 |
| 说话人识别 | 识别并区分不同说话人的技术 |
| SRT 字幕 | SubRip 格式的字幕文件 |
