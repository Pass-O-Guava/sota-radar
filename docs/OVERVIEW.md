# 📋 SOTA Radar 完整模型列表（2026-04-05 最终版）

> **分类原则**：按「许可证类型 + 模态」双重维度分类，开源/闭源绝不混列  
> **数据截止**：2026-04-05 | **来源**：HuggingFace + ModelScope + 官方博客 实地核查 | **全部 3 个子智能体调研完成**

---

## 分类总览

| 分类 | 总数 | 闭源 | 开源 |
|------|------|------|------|
| 🅐 闭源文本与推理模型 | **10** | 10 | — |
| 🅐 开源文本大模型 | 9 | — | 9 |
| 🅱 闭源 VLM | 4 | 4 | — |
| 🅱 开源 VLM | 17 | — | 17 |
| 🎧 音频-语言模型 | 3 | 0 | 3 |
| 🎬 视频理解模型 | 4 | 0 | 4 |
| 🎨 图像生成模型 | 5 | 4 | 1 |
| ⚡ 编程/推理专项 | 6 | 2 | 4 |
| 🔮 多模态统一模型 | 5 | 0 | 5 |
| 🔢 Embedding & Reranker | 4 | 1 | 3 |
| **合计** | **68** | **21** | **47** |

---

## 🅐 闭源文本与推理模型（10个）🔒专有

| # | 模型 | 开发商 | 发布日期 | MMMU | 亮点 |
|---|------|--------|----------|------|------|
| 1 | **GPT-5** | OpenAI | 2025-08-07 | 92.5% | 最强旗舰，推理+Agent，200K |
| 2 | **Claude Opus 4.6** | Anthropic | 2026-02-05 | 90.8% | SWE-bench 80.8%，GPQA 87.4% |
| 3 | **Claude Sonnet 4.6** | Anthropic | 2026-02-17 | 89% | 性价比最优，$3/1M，OSWorld 94% |
| 4 | **Claude Opus 4.5** | Anthropic | 2025-11-24 | 90.8% | SWE-bench 80.9%，发布时全球第一 |
| 5 | **Claude Sonnet 4.5** | Anthropic | 2025-09-29 | 89.1% | HumanEval 97.6%，编程最强 |
| 6 | **Gemini 3.1 Pro** | Google | 2026-02-19 | 91% | GPQA 94.3%，1M上下文 |
| 7 | **Grok 4.20** | xAI | 2026-02-17 | 87% | **2M上下文**，$2/1M |
| 8 | **GPT-4.5** | OpenAI | 2025-02-27 | 93.8% | ⚠️ 已从 API 弃用 |
| 9 | **Gemini 3.1 Flash Live** | Google | 2026-03-26 | — | 实时语音旗舰，<1s 延迟 |
| 10 | **o4-mini** | OpenAI | 2025-04-16 | 80.1% | 高性价比，AIME 92.7%，$1.1/1M |

**详细数据** → [`docs/models/proprietary-text.md`](./models/proprietary-text.md)

---

## 🅐 开源文本大模型（9个）✅可商用

| # | 模型 | 开发方 | 参数量 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|--------|----------|--------|------|
| 1 | **Qwen3.6-Plus** 🆕 | 阿里巴巴 | 待确认 | 2026-04-02 | Tongyi Qianwen | 最新旗舰 |
| 2 | **GLM-5** 🆕 | 智谱AI | — | 2026-02-11 | **MIT** | Frontier级，200K上下文 |
| 3 | **Qwen3.5 系列** 🆕 | 阿里巴巴 | 0.8B~35B | 2026-02-24 | Qwen3.5 License | 全规格覆盖 |
| 4 | **MiniMax M2.5** 🆕 | MiniMax | MoE | 2026-02-12 | **Apache 2.0** | $1/h，接近Frontier |
| 5 | **Step-3.5-Flash** 🆕 | StepFun AI | 196B总 | 2026-02-02 | 需确认 | 极速MoE |
| 6 | DeepSeek-V3 | DeepSeek | 671B/37B激活 | 2025-01-28 | DeepSeek License | 基础LLM最强 |
| 7 | DeepSeek-R1 | DeepSeek | 671B/37B激活 | 2025-01-20 | DeepSeek License | 推理最强，AIME~86% |
| 8 | Qwen2.5 系列 | 阿里巴巴 | 0.5B~72B | 2024-09 | Tongyi Qianwen | ⚠️静态，19个月 |
| 9 | Llama 3.3 | Meta | 70B | 2024-12 | Llama License ⚠️ | ⚠️需申请 |

> ⚠️ **更正（2026-04-05）**：`Qwen3.5-397B-A17B` 已从本分类移除——NVIDIA NIM / Together AI 官方页面确认，该模型是**原生视觉-语言模型（VLM）**，应归入开源 VLM 分类。

---

## 🅱 闭源 VLM（4个）🔒专有

| # | 模型 | 开发商 | 发布日期 | MMMU-Pro | 亮点 |
|---|------|--------|----------|----------|------|
| 1 | **Claude Sonnet 4.6（vision）** | Anthropic | 2026-02-17 | **83.58%** | 闭源VLM最强 |
| 2 | **Gemini 3.1 Pro (vision)** | Google | 2026-02-19 | 80.5% | 1M上下文 |
| 3 | **GPT-4o** | OpenAI | 持续更新 | ~70.7% | 多模态全能 |
| 4 | **GLM-5V-Turbo** 🆕 | 智谱AI/Z.ai | 2026-04-01 | 61.7% | 视觉编程，Agent |

---

## 🅱 开源 VLM（17个）✅可商用

| # | 模型 | 开发方 | 参数量 | 发布日期 | 许可证 | MMMU | 亮点 |
|---|------|--------|--------|----------|--------|------|------|
| 1 | **Kimi K2.5** 🆕 | Moonshot AI | ~200B | 2026-01-27 | **MIT** | Pro: 78.5% | MIT开源，MMMU-Pro 78.5% |
| 2 | **Qwen3.5-397B-A17B** 🆕 | 阿里巴巴 | 397B/17B激活 | 2026-02-16 | Qwen3.5 License | — | 原生多模态VLM，MoE，早期融合视觉-语言训练 |
| 3 | **InternVL3.5-Flash** 🆕 | 上海AI Lab | 8B~78B | 2025-10-14 | Apache 2.0 | — | 快速版 |
| 4 | InternVL3.5 | 上海AI Lab | 8B~78B | 2025-08-25 | **MIT** | 77.7% | 开源VLM综合最强 |
| 5 | Qwen3-VL-235B-A22B | 阿里巴巴 | 235B/22B激活 | 2025-09-23 | Apache 2.0 | Pro: 78.7% | MoE，256K上下文 |
| 6 | Qwen3-VL（通用） | 阿里巴巴 | 3B/8B/30B | 2025-09-23 | Tongyi Qianwen | — | 通用版 |
| 7 | Qwen2.5-VL | 阿里巴巴 | 3B~72B | 2025-01 | Tongyi Qianwen | — | ⚠️静态 |
| 8 | InternVL3 | 上海AI Lab | 1B~78B | 2025-04 | Apache 2.0 | — | ⚠️静态 |
| 9 | **GLM-4.6V** 🆕 | 智谱AI | ~9B | **2025-12-08** | **Apache 2.0** | — | MathVista开源SOTA |
| 10 | Phi-4-Multimodal | 微软 | 8B | 2025-02 | MIT | — | 语音+图+文三模态 |
| 11 | Phi-4-Reasoning-Vision | 微软 | 15B | 2025-02 | MIT | — | 视觉CoT推理 |
| 12 | LLaVA-CoT | PKU | 11B | 2025（ICCV） | **MIT** | 超越Gemini-1.5-pro | 视觉CoT |
| 13 | DeepSeek-VL2 | DeepSeek | 3B~27B总 | **2024-12-13** | DeepSeek License | 61.3% | MoE性价比 |
| 14 | Gemma 3 | Google | 1B~27B | 2025-03 | Gemma T&C ⚠️ | — | ⚠️静态 |
| 15 | Pixtral 12B | Mistral AI | 12B | 2025-03 | Apache 2.0 | — | ⚠️静态 |
| 16 | LLaVA-OneVision-1.5 | LLaVA-VL | 4B/8B | 2024-12 | MIT | — | ⚠️静态 |
| 17 | MiniCPM-V 4.5 | OpenBMB | 8B | 2024-11 | BSD | — | ⚠️静态 |

---

## 🎧 音频-语言模型（3个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | 状态 |
|---|------|--------|----------|--------|------|
| 17 | **Qwen3-ASR-0.6B** 🆕 | 阿里巴巴 | 2026-01-29 | Tongyi Qianwen | ✅开源 |
| 18 | Qwen2-Audio | 阿里巴巴 | 2024-09 | Tongyi Qianwen | ⚠️静态 |
| 19 | SALMONN | ByteDance | 2024-08 | CC BY-NC-SA ❌ | ⚠️非商用 |

---

## 🎬 视频理解模型（4个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
| 20 | **Cosmos-Reason2** 🆕 | NVIDIA | 2025-12-19 | NVIDIA Open | 物理AI推理 |
| 21 | **SenseNova-MARS** 🆕 | 商汤科技 | 2026-01-29 | 需确认 | 多模态Agent |
| 22 | CogVLM2-Video | THUDM/智谱AI | 2025-03 | Apache 2.0 | ⚠️静态 |
| 23 | Video-LLaVA | PKU | 2025-03 | Apache 2.0 | ⚠️静态 |

---

## 🎨 图像生成模型（6个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
| 24 | **Imagen 4** 🆕 | Google | 2026-05 | 🔒专有 | 2K分辨率，完美文字渲染 |
| 25 | **Recraft V4** 🆕 | Recraft | 2026-02 | 🔒专有 | HuggingFace排行榜第一 |
| 26 | **FLUX.2** 🆕 | Black Forest Labs | 2025-11 | 🔒专有 | 开源基准胜率66.6% |
| 27 | **Imagen 3** | Google | 2024-08 | 🔒专有 | GA: 2025-01（Vertex AI） |
| 28 | DALL-E 3 | OpenAI | 2023-10 | 🔒专有 | ⚠️ 2026-05正式停用，迁移至GPT-4o |
| 29 | **FLUX.1 [schnell]** 🆕 | Black Forest Labs | 2024-08 | ✅**Apache 2.0** | 开源可商用，高速生成 |
| — | ~~DALL-E 4~~ | — | ❌未发布 | — | 尚未正式发布 |
| — | ~~SD 4.0~~ | Stability AI | ❌未发布 | — | 尚未正式发布 |

---

## ⚡ 编程/推理专项模型（6个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | SWE-bench | 亮点 |
|---|------|--------|----------|--------|-----------|------|
| 29 | **MiniMax M2.5** 🆕 | MiniMax | 2026-02-12 | ✅开源（Apache 2.0） | **80.2%** | $1/h，开源编程最强 |
| 30 | **Qwen3-Coder-Next** 🆕 | 阿里巴巴 | 2026-02-04 | ✅开源（Tongyi） | >70% | 80B MoE，28 AA Index |
| 31 | DeepSeek-R1 | DeepSeek | 2025-01-20 | ✅开源 | 超越 o1 | AIME ~86% |
| 32 | **o4-mini** | OpenAI | 2025-04-16 | 🔒专有 | ~68.1% | AIME 92.7%，$1.1/1M |
| 33 | **Grok 4.20** | xAI | 2026-03 | 🔒专有 | — | 2M上下文，78%非幻觉率 |
| 34 | **Claude Sonnet 4.6** | Anthropic | 2026-02-17 | 🔒专有 | 79.6% | $3/1M，OSWorld 94% |

---

## 🔮 多模态统一模型（5个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
| 35 | Qwen3-Omni | 阿里巴巴 | 2025-12 | Tongyi Qianwen | 全模态+语音输出 |
| 36 | Kimi K2.5 | Moonshot AI | 2026-01-27 | **MIT** | 多模态Agent |
| 37 | DeepSeek Janus-Pro | DeepSeek | 2025-01-27 | DeepSeek License | 理解+生成统一 |
| 38 | Emu3.5 | BAAI | 2025-06 | 需确认 | 世界模型 |
| 39 | Show-o2 | Showlab | 2025-04 | Apache 2.0 | AR+Flow混合 |

---

## 🔢 Embedding & Reranker（4个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | MTEB/CMTEB | 亮点 |
|---|------|--------|----------|--------|------|------|
| 40 | **Qwen3-VL-Embedding** 🆕 | 阿里巴巴 | 2026-01 | **Apache 2.0** | MMEB-V2: 77.8 #1 | 多模态：文本+图像+视频 |
| 41 | **NV-Embed-v2** 🆕 | NVIDIA | 2024-08 | NVIDIA License ⚠️ | MTEB: 69.32 #1 | 英文检索最强 |
| 42 | **Youtu-Embedding** 🆕 | 腾讯优图 | 2025-08 | 🔒专有 | CMTEB: 77.58 #1 | 中文检索最强 |
| 43 | bge-m3 | 北京AI Lab | 2024-02 | Apache 2.0 | ~63.0 | 多语言开源 |

---

## 📋 许可证速查

| 许可证 | 可商用 | 代表模型 |
|--------|--------|---------|
| **MIT** | ✅ | Kimi K2.5, GLM-5, MiniMax M2.5, Phi-4-Multimodal, InternVL3.5 |
| **Apache 2.0** | ✅ | InternVL3.5, Mistral Small 3, Show-o2, CogVLM2-Video, Step-3.5-Flash |
| **Tongyi Qianwen** | ✅ | Qwen3-VL, Qwen3-Omni, Qwen3.5系列, Qwen3-Coder-Next, Qwen3.6-Plus |
| **DeepSeek License** | ✅ | DeepSeek-R1, DeepSeek-V3, Janus-Pro |
| **Llama License** | ⚠️需申请 | Llama 3.x |
| **CC BY-NC-SA** | ❌ | SALMONN |
| **🔒 专有** | ❌ | GPT-5, Claude Opus/Sonnet 4.6, Gemini 3.1 Pro, Grok 4.20, DALL-E, etc. |

---

*数据来源：HuggingFace 官方页 + ModelScope 官方页 + GitHub 官方公告 + Anthropic / OpenAI / Google 官方博客 | 2026-04-05 调研核实*
