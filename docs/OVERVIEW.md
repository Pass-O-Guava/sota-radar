# 📋 SOTA Radar 完整模型列表（2026-04-05 最终版）

> **分类原则**：按「许可证类型 + 模态」双重维度分类，开源/闭源绝不混列  
> **数据截止**：2026-04-05 | **来源**：HuggingFace + ModelScope + 官方博客 实地核查

---

## 分类总览

| 分类 | 总数 | 闭源 | 开源 |
|------|------|------|------|
| 🅐 闭源文本与推理模型 | **11** | 11 | — |
| 🅐 开源文本大模型 | 10 | — | 10 |
| 🅱 闭源 VLM | 3 | 3 | — |
| 🅱 开源 VLM | 13 | — | 13 |
| 🎧 音频-语言模型 | 3 | 0 | 3 |
| 🎬 视频理解模型 | 2 | 0 | 2 |
| 🎨 图像生成模型 | 1 | 1 | 1 |
| ⚡ 编程/推理专项 | 1 | 1 | 1 |
| 🔮 多模态统一模型 | 2 | 0 | 2 |
| 🔢 Embedding & Reranker | 4 | 1 | 3 |
| **合计** | **50** | **14** | **36** |

---

## 🅐 闭源文本与推理模型（11个）🔒专有

| # | 模型 | 开发商 | 发布日期 | MMLU | 亮点 |
|---|------|--------|----------|------|------|
| 1 | **GPT-4.5** | OpenAI | 2025-02-27 | ~93.8% | 通过无监督学习规模化提升；先向ChatGPT Pro用户开放 |
| 2 | **o4-mini** | OpenAI | 2025-04-16 | 80.1% | 高性价比推理；AIME 92.7% |
| 3 | **GPT-5** | OpenAI | 2025-08-07 | 92.5% | 最强旗舰，推理+Agent；支持thinking模式 |
| 4 | **Claude Sonnet 4.5** | Anthropic | 2025-09-29 | 89.1% | 发布时全球最佳编码模型；HumanEval 97.6%持续领先 |
| 5 | **Claude Opus 4.5** | Anthropic | 2025-11-24 | ~90.8% | 发布时全球第一SWE-bench；Chrome和Excel原生集成 |
| 6 | **Claude Opus 4.6** | Anthropic | 2026-02-05 | ~90.8% | 200K Elo领先（Artificial Analysis）；SWE-bench 80.8% |
| 7 | **Claude Sonnet 4.6** | Anthropic | 2026-02-17 | ~89% | 性价比最优；OSWorld 94% |
| 8 | **Grok 4.20** | xAI | 2026-02-17 | ~87% | 2M上下文行业最大；原生实时搜索集成 |
| 9 | **Gemini 3.1 Pro** | Google DeepMind | 2026-02-19 | ~91% | GPQA 94.3%（人类最后考试领先）；ARC-AGI-2领先 |
| 10 | **GPT-5.4** | OpenAI | 2026-03-05 | — | GPT-5.4 Thinking版本；专业工作83%（超越人类基准） |
| 11 | **Gemini 3.1 Flash Live** | Google DeepMind | 2026-03-26 | — | Google最高质量音频+语音模型；实时对话延迟<1秒 |

**详细数据** → [`models/text/proprietary-text.md`](./models/text/proprietary-text.md)

---

## 🅐 开源文本大模型（10个）✅可商用

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
| 1 | **Qwen3.6-Plus**  | 阿里巴巴 | 2026-04-02 | tongyi_qianwen | 最新旗舰；1M上下文 |
| 2 | **GLM-5.1** [HF](待确认（zai-org/GLM-5）) | 智谱AI/Z.ai | 2026-03-27 | mit | SWE-bench Verified 77.8%（开源最高）；LMArena Text/Code Arena双第一 |
| 3 | **Mistral Small 4** [HF](https://huggingface.co/mistralai/mistral-small-2603) | Mistral AI | 2026-03-16 | apache_2 | 119B MoE混合模型；统一instruct+reasoning+coding多模态 |
| 4 | **Qwen3.5 系列** [HF](https://huggingface.co/Qwen/Qwen3.5) | 阿里巴巴 | 2026-02-24 | qwen35_license | 0.8B~35B全规格覆盖；MoE+稠密双路线 |
| 5 | **GLM-5** [HF](https://huggingface.co/zai-org/GLM-5) | 智谱AI/Z.ai | 2026-02-11 | mit | MIT许可证开源；200K上下文 |
| 6 | **Step-3.5-Flash** [HF](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | StepFun AI | 2026-02-02 | unknown | 196B总参数稀疏MoE；极速推理 |
| 7 | **DeepSeek-V3** [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3) | DeepSeek | 2025-01-28 | deepseek_license | 671B总/37B激活MoE；基础LLM最强 |
| 8 | **DeepSeek-R1** [HF](https://huggingface.co/deepseek-ai/DeepSeek-R1) | DeepSeek | 2025-01-20 | deepseek_license | 强化学习驱动推理突破；AIME~86% |
| 9 | **Llama 3.3** [HF](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | Meta | 2024-12 | llama_license | 70B；历史版本 |
| 10 | **Qwen2.5 系列** [HF](https://huggingface.co/Qwen/Qwen2.5) | 阿里巴巴 | 2024-09 | tongyi_qianwen | 0.5B~72B全规格；历史版本 |

**详细数据** → [`models/text/open-text.md`](./models/text/open-text.md)

---

## 🅱 闭源 VLM（3个）🔒专有

| # | 模型 | 开发商 | 发布日期 | MMMU-Pro | 亮点 |
|---|------|--------|----------|----------|------|
| 1 | **GPT-4o** | OpenAI | 持续更新 | ~70.7% | 多模态全能；持续迭代更新 |
| 2 | **GLM-5V-Turbo** | 智谱AI/Z.ai | 2026-04-01 | 61.7% | 视觉编程；原生代码生成 |
| 3 | **Claude Sonnet 4.6（vision）** | Anthropic | 2026-02-17 | 83.58% | MMMU-Pro 83.58%（所有VLM最高）；原生视觉+计算机使用 |

**详细数据** → [`models/vlm/closed-vlm.md`](./models/vlm/closed-vlm.md)

---

## 🅱 开源 VLM（13个）✅可商用

| # | 模型 | 开发方 | 发布日期 | MMMU-Pro | 许可证 | 亮点 |
|---|------|--------|----------|----------|--------|------|
| 1 | **Gemma 4 E2B** [HF](https://huggingface.co/google/gemma-4) | Google DeepMind | 2026-04-02 | — | apache_2 | Apache 2.0首次（历史性转变）；2.3B有效参数/5.1B总参 |
| 2 | **Gemma 4 E4B** [HF](https://huggingface.co/google/gemma-4) | Google DeepMind | 2026-04-02 | — | apache_2 | 4.5B有效参数/8B总参；E4B=Edge 4B |
| 3 | **Gemma 4 26B-A4B** [HF](https://huggingface.co/google/gemma-4) | Google DeepMind | 2026-04-02 | — | apache_2 | MoE: 3.8B激活/25.2B总参；Apache 2.0 |
| 4 | **Gemma 4 31B** [HF](https://huggingface.co/google/gemma-4) | Google DeepMind | 2026-04-02 | ~55% | apache_2 | 旗舰开源VLM；Apache 2.0 |
| 5 | **Qwen3.5-397B-A17B** [HF](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | 阿里巴巴 | 2026-02-16 | — | qwen35_license | 397B总/17B激活MoE；原生视觉-语言训练 |
| 6 | **MiniMax M2.5** [HF](https://huggingface.co/blog/mlabonne/minimax-m25) | MiniMax | 2026-02-12 | — | apache_2 | Apache 2.0开源；SWE-bench 80.2% |
| 7 | **Kimi K2.5** [HF](https://huggingface.co/moonshotai/Kimi-K2.5) | Moonshot AI | 2026-01-27 | 78.5% | mit | MIT完全开源；MMMU-Pro 78.5% |
| 8 | **LLaVA-CoT**  | PKU | 2025（ICCV） | 超越Gemini-1.5-pro | mit | 视觉链式推理；ICCV 2025 |
| 9 | **GLM-4.6V** [HF](https://huggingface.co/THUDM/GLM-4V-9B) | 智谱AI | 2025-12-08 | — | apache_2 | MathVista开源SOTA；原生工具调用 |
| 10 | **Qwen3-VL-235B-A22B** [HF](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) | 阿里巴巴 | 2025-09-23 | 78.7% | apache_2 | 235B总/22B激活MoE；256K上下文 |
| 11 | **InternVL3.5** [HF](https://huggingface.co/OpenGVLab/InternVL3_5-8B) | 上海AI Lab | 2025-08-25 | 77.7% | mit | 开源VLM综合最强；Cascade RL控幻觉 |
| 12 | **Phi-4-Multimodal**  | 微软 | 2025-02-26 | — | mit | 语音+图+文三模态；MIT许可证 |
| 13 | **DeepSeek-VL2**  | DeepSeek | 2024-12-13 | 61.3% | deepseek_license | MoE性价比 |

**详细数据** → [`models/vlm/open-vlm.md`](./models/vlm/open-vlm.md)

---

## 🎧 音频-语言模型（3个）✅可商用

| # | 模型 | 开发方 | 发布日期 | 类型 | 亮点 |
|---|------|--------|----------|------|------|
| 1 | **MAI-Transcribe-1** | Microsoft | 2026-04-02 | mai-transcribe-1 | 高质量语音转文字；Microsoft内部训练 |
| 2 | **MAI-Voice-1** | Microsoft | 2026-04-02 | mai-voice-1 | 1秒生成60秒音频；高质量语音合成 |
| 3 | **Qwen3-ASR-0.6B** | 阿里巴巴 | 2026-01-29 | qwen3-asr | 语音识别；0.6B/1.7B双规格 |

---

## 🎬 视频理解模型（2个）✅可商用

| # | 模型 | 开发方 | 发布日期 | 亮点 |
|---|------|--------|----------|------|
| 1 | **SenseNova-MARS** | 商汤科技 | 2026-01-29 | 多模态Agent推理；动态视觉推理 |
| 2 | **Cosmos-Reason2** | NVIDIA | 2025-12-19 | 物理AI推理；2B/8B/72B多规格 |

---

## 🎨 图像生成模型（1个）

| # | 模型 | 开发方 | 发布日期 | 亮点 |
|---|------|--------|----------|------|
| 1 | **MAI-Image-2** | Microsoft | 2026-04-02 | 高质量图像生成；Microsoft MAI系列 |

---

## ⚡ 编程/推理专项（1个）

| # | 模型 | 开发方 | 发布日期 | SWE-bench | 亮点 |
|---|------|--------|----------|-----------|------|
| 1 | **Qwen3-Coder-Next** | 阿里巴巴 | 2026-02-04 | >70% | 80B MoE / 3B激活；28 AA Index |

---

## 🔮 多模态统一模型（2个）

| # | 模型 | 开发方 | 发布日期 | 亮点 |
|---|------|--------|----------|------|
| 1 | **Qwen3-Omni** | 阿里巴巴 | 2025-12 | 全模态+语音输出；原生端到端多模态 |
| 2 | **DeepSeek Janus-Pro** | DeepSeek | 2025-01-27 | 理解+生成统一 |

---

## 🔢 Embedding & Reranker（4个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
| 1 | **Qwen3-VL-Embedding** | 阿里巴巴 | 2026-01 | apache_2 | 多模态Embedding(text+图+视频)；MMEB-V2 #1 |
| 2 | **Youtu-Embedding** | 腾讯优图 | 2025-08 | proprietary | CMTEB #1；中文语义检索最强 |
| 3 | **NV-Embed-v2** | NVIDIA | 2024-08 | nvidia | MTEB #1持续领先；Llama-3.1-8B微调 |
| 4 | **bge-m3** | 北京AI Lab | 2024-02 | apache_2 | 3M：多功能+多语言+多粒度；100+语言 |

---

*SOTA Radar · 数据每日自动更新 · 来源：HuggingFace / ModelScope / 官方博客*
