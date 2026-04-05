# 🤖 SOTA Radar — 追踪最新开源大模型

> **每日更新** · 量化选型 · 商用合规指南  
> **数据截止**：2026-04-05 | **模型总数**：68 个 | **开源**：47 个 | **闭源**：21 个 | ⚠️含分类更正

---

## 📊 实时全览

| 分类 | 总数 | 闭源 | 开源 |
|------|------|------|------|
| 🅐 闭源文本与推理模型 | **10** | 10 | — |
| 🅐 开源文本大模型 | 8 | — | 8 |
| 🅱 闭源 VLM | 4 | 4 | — |
| 🅱 开源 VLM | 17 | — | 17 |
| 🎧 音频-语言模型 | 3 | 0 | 3 |
| 🎬 视频理解模型 | 4 | 0 | 4 |
| 🎨 图像生成模型 | 6 | 5 | 1 |
| ⚡ 编程/推理专项 | 6 | 2 | 4 |
| 🔮 多模态统一模型 | 5 | 0 | 5 |
| 🔢 Embedding & Reranker | 4 | 1 | 3 |

---

## 🏆 选型推荐

### 🔒 闭源 API 首选（2026年最新）

| 场景 | 推荐模型 |  Benchmark | 定价 |
|------|---------|-----------|------|
| 最高综合智能 | **Claude Opus 4.6** | SWE-bench 80.8% / GPQA 87.4% | $15/1M输入 |
| 编程性价比首选 | **Claude Sonnet 4.6** | SWE-bench 79.6% / OSWorld 94% | **$3/1M输入** |
| GPQA 科学推理最强 | **Gemini 3.1 Pro** | GPQA **94.3%** / 1M上下文 | $2.5/1M输入 |
| 超长上下文 | **Grok 4.20** | 2M tokens 行业最大 | $2/1M输入 |
| 数学性价比 | **o4-mini** | AIME 92.7% | **$1.1/1M输入** |
| GPT 系列旗舰 | **GPT-5** | MMLU 92.5% / Agent 最强 | $1.75/1M输入 |
| 实时语音助手 | **Gemini 3.1 Flash Live** | 实时延迟 <1s | 标准费率 |

### 🔓 开源可部署首选

| 场景 | 推荐模型 | 亮点 |
|------|---------|------|
| 视觉理解综合最强 | **InternVL3.5**（Apache 2.0） | Cascade RL，控幻觉，MMMU ~75% |
| 开源多模态 Agent | **Kimi K2.5**（**MIT**） | 2026-01，MIT 完全开源 |
| 编程开源性价比 | **MiniMax M2.5**（**Apache 2.0**） | $1/h，接近 Frontier 级 |
| 基础语言模型开源 | **GLM-5**（**MIT**） | 200K 上下文，MIT 开源 |
| 超大 MoE 开源 | **Qwen3.5-397B-A17B** | 397B/17B 激活，商用友好 |
| 推理最强开源 | **DeepSeek-R1** | AIME ~86%，开源推理标杆 |

---

## 🆕 2026年新发模型（按月倒序）

> ⚠️ 调研进行中，列表持续更新

---

### 2026年4月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Qwen3.6-Plus** 🆕 | 阿里巴巴 | Tongyi Qianwen | 最新旗舰，1M上下文 |
| **GLM-5V-Turbo** 🆕 | 智谱AI/Z.ai | 🔒专有 | 视觉编程，Agent |

---

### 2026年3月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Gemini 3.1 Flash Live** | Google | 🔒专有 | 实时语音旗舰，<1s延迟 |
| **Grok 4.20** | xAI | 🔒专有 | 2M上下文，推理 |
| **MiniMax M2.7** 🆕 | MiniMax | 🔒专有 | 闭源旗舰 |

---

### 2026年2月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Claude Opus 4.6** | Anthropic | 🔒专有 | GPQA 87.4%，最强智能 |
| **Claude Sonnet 4.6** | Anthropic | 🔒专有 | $3/1M，性价比最优 |
| **Gemini 3.1 Pro** | Google | 🔒专有 | GPQA 94.3%，1M上下文 |
| **GLM-5** 🆕 | 智谱AI/Z.ai | **MIT** | Frontier级，200K上下文 |
| **MiniMax M2.5** 🆕 | MiniMax | **Apache 2.0** | $1/h，编程开源 |
| **Qwen3.5-397B-A17B** 🆕 | 阿里巴巴 | Qwen3.5 License | MoE超大模型 |
| **Qwen3.5 系列** 🆕 | 阿里巴巴 | Qwen3.5 License | 0.8B~35B全规格 |
| **Qwen3-Coder-Next** 🆕 | 阿里巴巴 | Tongyi Qianwen | 80B MoE编程专项 |
| **Step-3.5-Flash** 🆕 | StepFun AI | 待确认 | 196B稀疏MoE |
| **Recraft V4** 🆕 | Recraft | 🔒专有 | HuggingFace排行榜第一 |

---

### 2026年1月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Kimi K2.5** 🆕 | Moonshot AI | **MIT** | 开源多模态Agent |
| **Qwen3-ASR-0.6B** 🆕 | 阿里巴巴 | Tongyi Qianwen | 语音识别，52语言 |
| **SenseNova-MARS** 🆕 | 商汤科技 | 待确认 | 多模态Agent推理 |
| **Qwen3-VL-Embedding** 🆕 | 阿里巴巴 | **Apache 2.0** | 多模态Embedding第一 |

---

### 2025年12月及更早
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Qwen3-Omni** | 阿里巴巴 | Tongyi Qianwen | 全模态+语音输出 |
| **Cosmos-Reason2** | NVIDIA | NVIDIA Open | 物理AI推理 |
| **FLUX.2** | Black Forest Labs | 🔒专有 | 开源基准胜率66.6% |
| **InternVL3.5-Flash** | 上海AI Lab | Apache 2.0 | VLM快速版 |
| **GPT-5** | OpenAI | 🔒专有 | 推理+Agent旗舰 |
| **DeepSeek-R1** | DeepSeek | DeepSeek License | 推理开源标杆 |
| **DeepSeek-V3** | DeepSeek | DeepSeek License | 基础LLM最强 |

---

## 📂 文档结构

```
docs/
├── README.md              ← 首页（本文档）
├── OVERVIEW.md            ← 67个模型完整列表
├── BENCHMARKS.md          ← Benchmark横向对比
├── LICENSE_GUIDE.md       ← 许可证速查 + 商用合规
├── INSIGHTS.md            ← 2026年行业趋势洞察
├── FLYWHEEL.md           ← 数据飞轮机制
└── models/
    └── proprietary-text.md ← 闭源模型详细数据卡
models/
├── vlm/  ·  alm/  ·  video/  ·  multimodal/  ·  text/
```

---

## ⏰ 定时更新机制

- **早间扫描**：每日 09:00（北京时间）— 亚洲发布动态
- **晚间扫描**：每日 21:00（北京时间）— 欧美发布动态
- 每次扫描自动更新文档 → GitHub 推送 → 飞书报告

---

*数据来源：HuggingFace + ModelScope + 官方博客 实地核查 | 欢迎提交 Issue*
*GitHub：https://github.com/Pass-O-Guava/sota-radar*
