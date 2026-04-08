---
type: summary
source: "[[raw/articles/RVC-BossGPT-SoVITS 1 min voice data can also be used to train a good TTS model! (few shot voice cloning).md|原始文档]]"
compiled_at: 2026-04-08
status: done
---

# S-011: GPT-SoVITS 少样本语音克隆

## TL;DR
只需 1 分钟语音数据即可训练高质量 TTS 模型的少样本语音克隆工具，支持中英日韩粤语，推理速度快（4090 上 RTF=0.014）。

## 核心结论

1. **零样本/少样本 TTS** - 5 秒样本即可体验，1 分钟训练数据微调可获得更好效果
2. **跨语言支持** - 支持与训练数据集不同的语言推理，目前支持英、日、韩、粤语和中文
3. **快速推理** - V2ProPlus 在 4090 上 RTF=0.014（1400 字约 4 分钟，推理时间 3.36 秒）
4. **集成 WebUI 工具** - 包含语音伴奏分离、自动训练集分割、中文 ASR、文本标注等工具
5. **多版本迭代** - v1/v2/v2Pro/v3/v4/V2ProPlus 各版本针对不同场景优化

## 关键证据

### 版本特点对比
| 版本 | 特点 |
|------|------|
| v1/v2/v2Pro | 适合平均音频质量训练集，效果不错 |
| v3/v4 | 音色相似度更高，但倾向参考音频而非整体训练集 |
| V2ProPlus | 超越 v4 性能，保持 v2 硬件成本和速度 |

### 性能数据
- 4060Ti: RTF=0.028
- 4090: RTF=0.014
- M4 CPU: RTF=0.526

### 功能特性
- 零样本语音转换（5s）/少样本语音转换（1min）
- TTS 语速控制
- 语音伴奏分离（UVR5）
- 自动训练集分割
- ASR 自动标注

## 概念提取

- [[C-031-GPT-SoVITS|GPT-SoVITS]]：少样本语音克隆工具
- [[C-032-RTF|RTF]]：Real-Time Factor，实时因子，衡量 TTS 推理速度
- [[C-033-UVR5|UVR5]]：人声伴奏分离模型

## 疑点/待验证

1. 不同语言的实际效果差异
2. 训练数据质量对效果的影响
3. 与 CosyVoice 的效果对比

## 术语表

| 术语 | 定义 |
|------|------|
| RTF | Real-Time Factor，实时因子，越小速度越快 |
| UVR5 | 人声伴奏分离模型 |
| ASR | Automatic Speech Recognition，自动语音识别 |
| Zero-shot | 零样本学习，无需训练即可使用 |
