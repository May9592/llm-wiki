---
type: summary
source: "[[raw/articles/OpenTalkervideo-retalking SIGGRAPH Asia 2022 VideoReTalking Audio-based Lip Synchronization for Talking Head Video Editing In the Wild.md|原始文档]]"
compiled_at: 2026-04-08
status: done
---

# S-012: VideoReTalking 音视频同步

## TL;DR
SIGGRAPH Asia 2022 论文实现，根据输入音频编辑真实世界说话人视频的面部，生成高质量、唇同步的输出视频，甚至支持不同表情。

## 核心结论

1. **三阶段流水线** - (1) 标准表情面部视频生成 (2) 音频驱动唇同步 (3) 面部增强提升真实感
2. **野外环境适用** - 可处理真实世界的说话人视频，无需人工对齐
3. **表情控制** - 可通过参数控制表情（neutral、smile、surprise、angry）
4. **全学习方案** - 所有三个步骤都使用基于学习的方法，无需用户干预
5. **身份保持** - 使用身份感知的面部增强网络保持说话人身份

## 关键证据

### 技术流程
1. 表情编辑网络：将每帧表情修改为标准表情模板
2. 唇同步网络：根据音频生成唇同步视频
3. 面部增强网络：提升合成面部的照片级真实感

### 支持的表情
- neutral（默认）
- smile
- surprise
- angry（上半脸）

### 技术依赖
- Wav2Lip：音频驱动唇同步
- PIRenderer：面部表情编辑
- GFP-GAN/GPEN：面部增强
- GANimation：上半脸表情控制

## 概念提取

- [[C-034-VideoReTalking|VideoReTalking]]：音视频唇同步工具
- [[C-035-唇同步|唇同步]]：音频与嘴部动作的同步技术

## 疑点/待验证

1. 极端姿态的处理效果
2. 中文支持的准确度
3. 实际部署的难度

## 术语表

| 术语 | 定义 |
|------|------|
| 唇同步 | 音频与嘴部动作的同步技术 |
| 说话人视频 | 包含人物说话的视频 |
| 表情模板 | 用于标准化面部表情的参考模板 |
