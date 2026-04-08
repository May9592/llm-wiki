---
type: summary
source: "[[raw/articles/FunAudioLLMCosyVoice Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability..md|原始文档]]"
compiled_at: 2026-04-08
status: done
---

# S-010: CosyVoice 多语言语音合成

## TL;DR
Fun-CosyVoice 3.0 是一个基于大语言模型的高级文本转语音系统，在内容一致性、说话人相似度和韵律自然度方面超越前代，专为野外零样本多语言语音合成设计。

## 核心结论

1. **多语言支持** - 覆盖 9 种常见语言（中、英、日、韩、德、西、法、意、俄），18+ 中文方言/口音，支持多语言/跨语言零样本语音克隆
2. **发音修复（Inpainting）** - 支持中文拼音和英文 CMU 音素的发音修复，提供更高可控性，适合生产使用
3. **低延迟流式推理** - 双流支持（文本输入流和音频输出流），延迟低至 150ms 且保持高质量音频输出
4. **指令支持** - 支持语言、方言、情感、语速、音量等多种指令控制
5. **全栈能力** - 提供推理、训练和部署的完整能力

## 关键证据

### 评测表现
| 模型 | test-zh CER ↓ | test-zh SS ↑ | test-en WER ↓ | test-en SS ↑ | test-hard CER ↓ |
|------|--------------|-------------|--------------|-------------|----------------|
| Fun-CosyVoice3-0.5B-2512 | 1.21 | 78.0 | 2.24 | 71.8 | 6.71 |
| Fun-CosyVoice3-0.5B-2512_RL | 0.81 | 77.4 | 1.68 | 69.5 | 5.44 |
| Human | 1.26 | 75.5 | 2.14 | 73.4 | - |

### 技术特点
- 基于 LLM 的 TTS 系统
- 支持文本规范化（数字、特殊符号等）
- 支持 vLLM 加速推理
- 支持 TensorRT-LLM 部署（相比 huggingface transformers 实现 4 倍加速）

## 概念提取

- [[C-028-CosyVoice|CosyVoice]]：多语言大语音生成模型
- [[C-029-零样本语音克隆|零样本语音克隆]]：无需训练即可克隆语音
- [[C-030-发音修复|发音修复（Inpainting）]]：精确控制特定词发音

## 疑点/待验证

1. 实际部署的资源需求
2. 与其他 TTS 模型的效果对比
3. 不同语言的支持质量差异

## 术语表

| 术语 | 定义 |
|------|------|
| 零样本语音克隆 | 无需训练即可用 5 秒音频克隆语音 |
| 发音修复 | 精确控制特定词的发音方式 |
| 双流支持 | 同时支持文本流输入和音频流输出 |
| RL | Reinforcement Learning，强化学习 |
