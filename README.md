# 🤖 SOTA Radar — 追踪最新开源大模型

> **每日更新** · 量化选型 · 商用合规指南  
> **数据截止**：2026-04-05 | **模型总数**：49 个 | **开源**：35 个 | **闭源**：14 个

---

## 📊 实时全览

| 分类 | 总数 | 闭源 | 开源 |
|------|------|------|------|
| 🅐 闭源文本与推理模型 | **11** | 11 | — |
| 🅐 开源文本大模型 | 9 | — | 9 |
| 🅱 闭源 VLM | 3 | 3 | — |
| 🅱 开源 VLM | 13 | — | 13 |
| 🎧 音频-语言模型 | 3 | 0 | 3 |
| 🎬 视频理解模型 | 2 | 0 | 2 |
| 🎨 图像生成模型 | 1 | 1 | 0 |
| ⚡ 编程/推理专项 | 1 | 0 | 1 |
| 🔮 多模态统一模型 | 2 | 0 | 2 |
| 🔢 Embedding & Reranker | 4 | 1 | 3 |

---

## 🏆 选型推荐

### 🔒 闭源 API 首选（2026年最新）

| 场景 | 推荐模型 | Benchmark | 定价 |
|------|---------|-----------|------|
| 最高综合智能 | **Claude Opus 4.6** | SWE-bench 80.8% / GPQA 87.4% | $15/1M输入 |
| 编程性价比首选 | **Claude Sonnet 4.6** | SWE-bench 79.6% / OSWorld 94% | **$3/1M输入** |
| GPQA 科学推理最强 | **Gemini 3.1 Pro** | GPQA **94.3%** / 1M上下文 | $2.5/1M输入 |
| 超长上下文 | **Grok 4.20** | 2M tokens 行业最大 | $2/1M输入 |
| 数学性价比 | **o4-mini** | AIME 92.7% | **$1.1/1M输入** |
| GPT 系列旗舰 | **GPT-5.4** | 专业工作83% / Agent最强 | $1.75/1M输入 |
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
| 编程最强开源 | **GLM-5.1**（**MIT**） | SWE-bench 77.8%，开源最高 |

---

## 🆕 2026年新发模型（按月倒序）

> ⚠️ 调研进行中，列表持续更新

---

### 2026年4月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Gemma 4** 🆕 | Google | **Apache 2.0** | 首个Apache 2.0 Gemma，4规格（E2B/E4B/26B/31B） |
| **MAI-Transcribe-1** 🆕 | Microsoft | 🔒专有 | 语音转文字，MAI系列首批 |
| **MAI-Voice-1** 🆕 | Microsoft | 🔒专有 | 1秒生成60秒音频 |
| **MAI-Image-2** 🆕 | Microsoft | 🔒专有 | 图像生成，MAI系列 |
| **Qwen3.6-Plus** | 阿里巴巴 | Tongyi Qianwen | 最新旗舰，1M上下文 |
| **GLM-5V-Turbo** | 智谱AI/Z.ai | 🔒专有 | 视觉编程，Agent |

---

### 2026年3月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **GPT-5.4** 🆕 | OpenAI | 🔒专有 | 专业工作83%，最强旗舰 |
| **GLM-5.1** 🆕 | 智谱AI/Z.ai | **MIT** | SWE-bench 77.8%（开源最高） |
| **Gemini 3.1 Flash Live** | Google | 🔒专有 | 实时语音旗舰，<1s延迟 |
| **Grok 4.20** | xAI | 🔒专有 | 2M上下文，推理 |
| **MiniMax M2.7** | MiniMax | 🔒专有 | 闭源旗舰，自进化Agent |

---

### 2026年2月
| 模型 | 发布方 | 许可证 | 亮点 |
|------|--------|--------|------|
| **Claude Opus 4.6** | Anthropic | 🔒专有 | GPQA 87.4%，最强智能 |
| **Claude Sonnet 4.6** | Anthropic | 🔒专有 | $3/1M，性价比最优 |
| **Gemini 3.1 Pro** | Google | 🔒专有 | GPQA 94.3%，1M上下文 |
| **GLM-5** | 智谱AI/Z.ai | **MIT** | Frontier级，MIT开源 |

---

## 📂 文档结构

```
sota-radar/
├── docs/
│   ├── _data/models.json     ← 单一数据源（所有文档从这里生成）
│   ├── OVERVIEW.md           ← 模型分类总览
│   ├── BENCHMARKS.md         ← 评测数据横向对比
│   ├── LICENSE_GUIDE.md      ← 许可证合规指南
│   └── models/
│       ├── text/
│       │   ├── proprietary-text.md  ← 闭源文本LLM
│       │   ├── open-text.md         ← 开源文本LLM
│       │   └── code-reasoning.md   ← 编程/推理专项
│       └── vlm/
│           ├── closed-vlm.md        ← 闭源VLM
│           ├── open-vlm.md          ← 开源VLM
│           └── embedding-reranker.md ← Embedding
├── README.md（你在这里）
└── models/（模型卡存档）
```

---

## 🔄 自动同步机制

- **每日 UTC 05:30**：cron 自动执行调研 + 文档同步
- **单一数据源**：`docs/_data/models.json` 为所有文档的唯一真相来源
- **强制同步**：每次更新后，OVERVIEW / BENCHMARKS / README / LICENSE_GUIDE / 分类模型卡全部同步

---

*自动更新 · SOTA Radar · 2026-04-05*
