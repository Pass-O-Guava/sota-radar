# 🤖 SOTA 模型知识库

> **收录原则**：最近 3 个月内发布 · 附量化证据 · 商用合规标注 · 每日更新  
> **数据截止**：2026-04-05 | **模型总数**：44 个

---

## 📊 实时全览

| 模态 | 收录 | 本月新增 | 可商用 | 闭源 |
|------|------|---------|--------|------|
| 👁️ 视觉-语言（VLM） | 19 | +4 | 14 | 1 |
| 🎧 音频-语言（ALM） | 3 | +1 | 2 | 0 |
| 🎬 视频理解 | 4 | +2 | 4 | 0 |
| 🔮 多模态统一 | 5 | 0 | 5 | 0 |
| 📝 纯语言 LLM | 13 | +8 | 11 | 2 |
| **合计** | **44** | **+14** | **36** | **3** |

---

## 🆕 本月新增（2026年发布）

| 模型 | 发布方 | 日期 | 许可证 | 亮点 |
|------|--------|------|--------|------|
| **Qwen3.6-Plus** | 阿里巴巴 | 04-02 | Tongyi Qianwen | 最新旗舰，刚发布 |
| **GLM-5V-Turbo** | 智谱AI/Z.ai | 04-01 | 🔒专有 | 视觉编程，Agent |
| **GLM-5** | 智谱AI/Z.ai | 02-11 | **MIT（开源）** | Frontier级，200K上下文 |
| **Qwen3.5-397B-A17B** | 阿里巴巴 | 02-16 | Qwen3.5 License | MoE超大模型 |
| **Qwen3.5 系列** | 阿里巴巴 | 02-24 | Qwen3.5 License | 0.8B~35B全规格 |
| **Kimi K2.5** | Moonshot AI | 01-27 | **MIT（完全开源）** | 多模态Agent，MIT许可 |
| **Qwen3-Coder-Next** | 阿里巴巴 | 02-04 | Tongyi Qianwen | 编程专用，80B/3B激活 |
| **MiniMax M2.7** | MiniMax | 03-18 | 🔒专有 | 闭源旗舰 |
| **MiniMax M2.5** | MiniMax | 02-12 | Apache 2.0 | 开源编程，$1/h |
| **Step-3.5-Flash** | StepFun AI | 02-02 | 待确认 | 极速MoE |
| **Qwen3-ASR-0.6B** | 阿里巴巴 | 01-29 | Tongyi Qianwen | 语音识别 |
| **SenseNova-MARS** | 商汤科技 | 01-29 | 待确认 | 多模态Agent |
| **Cosmos-Reason2** | NVIDIA | 12-19 | NVIDIA Open | 物理AI推理 |
| **InternVL3.5-Flash** | 上海AI Lab | 10-14 | Apache 2.0 | 快速版VLM |

---

## 🏆 选型推荐

### 🔥 闭源 API（直接集成）
| 场景 | 推荐 | 理由 |
|------|------|------|
| 全能旗舰 | **GLM-5V-Turbo** | 视觉编程+Agent，2026-04-01最新 |
| 性价比编程 | **MiniMax M2.7** | $1/h，接近Claude Opus 4.6 |
| 通用的对话 | **GLM-5** (API) | MIT开源，200K上下文 |
| 视频理解 | **Kimi K2.5** | MIT开源，多模态Agent |

### 🔓 开源可部署
| 场景 | 推荐 | 理由 |
|------|------|------|
| 视觉理解综合最强 | **InternVL3.5** | Apache 2.0，Cascade RL，控幻觉 |
| 视觉理解最新 | **Kimi K2.5** | 2026-01，MIT，多模态Agent |
| 编程开源首选 | **MiniMax M2.5** | Apache 2.0，$1/h，Frontier级 |
| 基础语言模型 | **GLM-5** | MIT开源，200K上下文 |
| 超大MoE | **Qwen3.5-397B-A17B** | 397B/17B激活，商用友好 |

---

## 📂 文档结构

```
docs/
├── README.md           ← 文档索引
├── OVERVIEW.md         ← 完整模型列表（44个，全维度表格）
├── BENCHMARKS.md       ← Benchmark横向对比
├── LICENSE_GUIDE.md    ← 许可证速查 + 商用合规
└── INSIGHTS.md         ← 行业趋势洞察
models/
├── README.md           ← 模型卡索引
├── vlm/                ← 视觉语言模型（19个）
├── alm/                ← 音频语言模型（3个）
├── video/              ← 视频理解模型（4个）
├── multimodal/         ← 多模态统一模型（5个）
└── text/               ← 纯语言模型（13个）
```

---

## 📋 许可证速查

| 许可证 | 可商用 | 代表模型 |
|--------|--------|---------|
| **MIT** | ✅ | Kimi K2.5, GLM-5, MiniMax M2.5, Step-3.5-Flash |
| **Apache 2.0** | ✅ | InternVL3.5, Mistral Small 3, Show-o2, CogVLM2-Video |
| **Tongyi Qianwen** | ✅ | Qwen3-VL, Qwen3-Omni, Qwen3.5系列, Qwen3-Coder-Next |
| **DeepSeek License** | ✅ | DeepSeek-R1, DeepSeek-V3, Janus-Pro |
| **Llama License** | ⚠️需申请 | Llama 3.x |
| **CC BY-NC-SA** | ❌ | SALMONN |
| 🔒 专有 | ❌ | GLM-5V-Turbo, MiniMax M2.7 |

---

*数据来源：HuggingFace 官方页 + ModelScope 官方页 + GitHub 官方公告 | 2026-04-05 实地核查*
*本项目持续更新，欢迎提交 Issue / PR*
