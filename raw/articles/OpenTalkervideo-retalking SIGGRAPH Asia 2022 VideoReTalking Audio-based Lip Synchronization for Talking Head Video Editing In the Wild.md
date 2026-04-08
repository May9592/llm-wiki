---
type: "article"
source_url: "https://github.com/OpenTalker/video-retalking"
author:
published:
ingested_at: 2026-04-08
tags:
  - "clippings"
---
# OpenTalker/video-retalking: [SIGGRAPH Asia 2022] VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild

> [原文链接](https://github.com/OpenTalker/video-retalking)

## 摘要

## VideoReTalking Audio-based Lip Synchronization for Talking Head Video Editing in the Wild

Kun Cheng <sup>*,1,2</sup>   [Xiaodong Cun <sup>*,2</sup>](https://vinthony.github.io/)   [Yong Zhang <sup>2</sup>](https://yzhang2016.github.io/yongnorriszhang.github.io/)   [Menghan Xia <sup>2</sup>](https://menghanxia.github.io/)   [Fei Yin <sup>2,3</sup>](https://feiiyin.github.io/)    
[Mingrui Zhu <sup>1</sup>](https://web.xidian.edu.cn/mrzhu/en/index.html)   [Xuan Wang <sup>2</sup>](https://xuanwangvc.github.io/)   [Jue Wang <sup>2</sup>](https://juewang725.github.io/)   [Nannan Wang <sup>1</sup>](https://web.xidian.edu.cn/nnwang/en/index.html)

  

<sup>1</sup> Xidian University   <sup>2</sup> Tencent AI Lab   <sup>3</sup> Tsinghua University

  
***[SIGGRAPH Asia 2022 Conference Track](https://sa2022.siggraph.org/)***  
  
[![](https://camo.githubusercontent.com/17d2a1f5e26333cf61344f7d7fdf17263eed7ecfd93735e4c8f0dc52330bc5c1/68747470733a2f2f6f70656e74616c6b65722e6769746875622e696f2f766964656f2d726574616c6b696e672f7374617469632f696d616765732f7465617365722e706e67)](https://camo.githubusercontent.com/17d2a1f5e26333cf61344f7d7fdf17263eed7ecfd93735e4c8f0dc52330bc5c1/68747470733a2f2f6f70656e74616c6b65722e6769746875622e696f2f766964656f2d726574616c6b696e672f7374617469632f696d616765732f7465617365722e706e67)

  
We present VideoReTalking, a new system to edit the faces of a real-world talking head video according to input audio, producing a high-quality and lip-syncing output video even with a different emotion. Our system disentangles this objective into three sequential tasks:

  
(1) face video generation with a canonical expression  
(2) audio-driven lip-sync and  
(3) face enhancement for improving photo-realism.

  
Given a talking-head video, we first modify the expression of each frame according to the same expression template using the expression editing network, resulting in a video with the canonical expression. This video, together with the given audio, is then fed into the lip-sync network to generate a lip-syncing video. Finally, we improve the photo-realism of the synthesized faces through an identity-aware face enhancement network and post-processing. We use learning-based approaches for all three steps and all our modules can be tackled in a sequential pipeline without any user intervention.

  

[![pipeline](https://github.com/OpenTalker/video-retalking/raw/main/docs/static/images/pipeline.png?raw=true)](https://github.com/OpenTalker/video-retalking/blob/main/docs/static/images/pipeline.png?raw=true)  
*Pipeline*

## Results in the Wild （contains audio）

Results\_in\_the\_wild.mp4<video src="https://private-user-images.githubusercontent.com/4397546/224310754-665eb2dd-aadc-47dc-b1f9-2029a937b20a.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU2MzUyMTMsIm5iZiI6MTc3NTYzNDkxMywicGF0aCI6Ii80Mzk3NTQ2LzIyNDMxMDc1NC02NjVlYjJkZC1hYWRjLTQ3ZGMtYjFmOS0yMDI5YTkzN2IyMGEubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MDhUMDc1NTEzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZDE5ODc5ZTQxZjBkNWZiN2VhNGVlMDllZjgxNTJhOWZlOGI3MWVkMTRlMTk0NTA3MmQ5NWM1YmIzOWY0MjE3ZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.yq3u3mMzV_a4yKbxGuBHFS0mZ0b310RbV7AOfqSuwwM" controls="controls"></video>

## Environment

```
git clone https://github.com/vinthony/video-retalking.git
cd video-retalking
conda create -n video_retalking python=3.8
conda activate video_retalking

conda install ffmpeg

# Please follow the instructions from https://pytorch.org/get-started/previous-versions/
# This installation command only works on CUDA 11.1
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt
```

## Quick Inference

#### Pretrained Models

Please download our [pre-trained models](https://drive.google.com/drive/folders/18rhjMpxK8LVVxf7PI6XwOidt8Vouv_H0?usp=share_link) and put them in `./checkpoints`.

#### Inference

```
python3 inference.py \
  --face examples/face/1.mp4 \
  --audio examples/audio/1.wav \
  --outfile results/1_1.mp4
```

This script includes data preprocessing steps. You can test any talking face videos without manual alignment. But it is worth noting that DNet cannot handle extreme poses.

You can also control the expression by adding the following parameters:

`--exp_img`: Pre-defined expression template. The default is "neutral". You can choose "smile" or an image path.

`--up_face`: You can choose "surprise" or "angry" to modify the expression of upper face with [GANimation](https://github.com/donydchen/ganimation_replicate).

## Citation

If you find our work useful in your research, please consider citing:

```
@misc{cheng2022videoretalking,
        title={VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild}, 
        author={Kun Cheng and Xiaodong Cun and Yong Zhang and Menghan Xia and Fei Yin and Mingrui Zhu and Xuan Wang and Jue Wang and Nannan Wang},
        year={2022},
        eprint={2211.14758},
        archivePrefix={arXiv},
        primaryClass={cs.CV}
  }
```

## Acknowledgement

Thanks to [Wav2Lip](https://github.com/Rudrabha/Wav2Lip), [PIRenderer](https://github.com/RenYurui/PIRender), [GFP-GAN](https://github.com/TencentARC/GFPGAN), [GPEN](https://github.com/yangxy/GPEN), [ganimation\_replicate](https://github.com/donydchen/ganimation_replicate), [STIT](https://github.com/rotemtzaban/STIT) for sharing their code.

## Related Work

- [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN (ECCV 2022)](https://github.com/FeiiYin/StyleHEAT)
- [CodeTalker: Speech-Driven 3D Facial Animation with Discrete Motion Prior (CVPR 2023)](https://github.com/Doubiiu/CodeTalker)
- [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation (CVPR 2023)](https://github.com/Winfredy/SadTalker)
- [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing (CVPR 2023)](https://github.com/Carlyx/DPE)
- [3D GAN Inversion with Facial Symmetry Prior (CVPR 2023)](https://github.com/FeiiYin/SPI/)
- [T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations (CVPR 2023)](https://github.com/Mael-zys/T2M-GPT)

## Disclaimer

This is not an official product of Tencent.

```
1. Please carefully read and comply with the open-source license applicable to this code before using it. 
2. Please carefully read and comply with the intellectual property declaration applicable to this code before using it.
3. This open-source code runs completely offline and does not collect any personal information or other data. If you use this code to provide services to end-users and collect related data, please take necessary compliance measures according to applicable laws and regulations (such as publishing privacy policies, adopting necessary data security strategies, etc.). If the collected data involves personal information, user consent must be obtained (if applicable). Any legal liabilities arising from this are unrelated to Tencent.
4. Without Tencent's written permission, you are not authorized to use the names or logos legally owned by Tencent, such as "Tencent." Otherwise, you may be liable for your legal responsibilities.
5. This open-source code does not have the ability to directly provide services to end-users. If you need to use this code for further model training or demos, as part of your product to provide services to end-users, or for similar use, please comply with applicable laws and regulations for your product or service. Any legal liabilities arising from this are unrelated to Tencent.
6. It is prohibited to use this open-source code for activities that harm the legitimate rights and interests of others (including but not limited to fraud, deception, infringement of others' portrait rights, reputation rights, etc.), or other behaviors that violate applicable laws and regulations or go against social ethics and good customs (including providing incorrect or false information, spreading pornographic, terrorist, and violent information, etc.). Otherwise, you may be liable for your legal responsibilities.
```

[![](https://camo.githubusercontent.com/2b93fc458524d5ba126399a74892ac7277488ec7774e543fe355bdbb814b9651/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d4f70656e54616c6b65722f766964656f2d726574616c6b696e67)](https://github.com/OpenTalker/video-retalking/graphs/contributors)

## 核心观点


## 术语/概念


## 疑问/待验证