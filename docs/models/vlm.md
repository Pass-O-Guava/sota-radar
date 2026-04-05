# 👁️ 视觉-语言模型（VLM）完整数据

> **数据来源**：官方 GitHub + HuggingFace + MMMU/MathVista 官方排行榜 | **可靠度**：A/B/C
> **注**：MMMU 标准版（满分65）与 MMMU-Pro（满分120）难度不同，跨版本对比需谨慎

---

## 📊 横向对比（开源 + 闭源）

### 开源 VLM

| 模型 | 开发方 | 发布日期 | 许可证 | MMMU | MMMU-Pro | MathVista | 亮点 |
|------|--------|----------|--------|------|----------|-----------|------|
| **Kimi K2.5** 🆕 | Moonshot AI | 2026-01-27 | **MIT** | — | **78.5%** | **90.1%** | MIT开源，多模态Agent |
| **InternVL3.5** | 上海AI Lab | 2025-08-25 | **MIT** | 77.7% | — | 82.7% | 开源VLM综合最强 |
| **Qwen3-VL-235B-A22B** | 阿里巴巴 | 2025-09-23 | **Apache 2.0** | 68.1% | 78.7% | 领先 | MoE，256K上下文 |
| **GLM-4.6V** 🆕 | 智谱AI | **2025-12-08** | **Apache 2.0** | — | — | **SOTA** | MathVista开源SOTA |
| **LLaVA-CoT** | PKU | 2025（ICCV） | **MIT** | 超越Gemini-1.5-pro | — | — | 视觉CoT，ICCV 2025 |
| **Phi-4-Multimodal** | 微软 | 2025-02-26 | **MIT** | — | — | — | 语音+图+文三模态 |
| **DeepSeek-VL2** | DeepSeek | **2024-12-13** | DeepSeek License | 61.3% | — | 79.0% | MoE性价比 |

### 闭源 VLM

| 模型 | 开发方 | 发布日期 | 许可证 | MMMU-Pro | 亮点 |
|------|--------|----------|--------|----------|------|
| **Claude Sonnet 4.6** | Anthropic | 2026-02-17 | 🔒专有 | **83.58%** | 闭源VLM综合最强 |
| **Gemini 3.1 Pro** | Google | 2026-02-19 | 🔒专有 | 80.5% | 1M上下文，视觉+文本 |
| **GPT-4o** | OpenAI | 2024-05-13 | 🔒专有 | ~70.7% | 多模态全能，持续更新 |
| **GLM-5V-Turbo** | 智谱AI | 2026-04-01 | 🔒专有 | 61.7% | 视觉编程，Agent |

---

## ⚠️ 重要更正

- **InternVL3.5 许可证**：应为 **MIT**，非 Apache 2.0
- **GLM-4.6V**：2025-12-08 有重大更新，MathVista 开源 SOTA
- **DeepSeek-VL2**：发布日期应为 2024-12-13（而非2025-03）
- **Claude Sonnet 4.6 VLM benchmark**：MMMU-Pro 83.58%——超过所有开源 VLM

---

## 逐模型详情

### 1. Kimi K2.5 🆕（开源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-01-27** |
| **许可证** | **MIT（Modified MIT，完全开源可商用）** |
| **MMMU-Pro** | **78.5%** |
| **MathVista** | **90.1%** |
| **亮点** | 开源多模态 Agent；MIT 许可证；HuggingFace 直接下载；视觉 Agent swarm |
| **HuggingFace** | https://huggingface.co/moonshotai/Kimi-K2.5 |

---

### 2. InternVL3.5（开源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-08-25** |
| **许可证** | **MIT** |
| **MMMU** | **77.7%** |
| **MathVista** | 82.7% |
| **上下文** | 128K |
| **亮点** | Cascade RL 控幻觉；开源 VLM 综合最强；Apache 2.0 变体可选 |
| **HuggingFace** | https://huggingface.co/OpenGVLab/InternVL3_5-8B |

---

### 3. Qwen3-VL-235B-A22B（开源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-09-23** |
| **许可证** | **Apache 2.0** |
| **MMMU** | 68.1%（标准）/ **78.7%（Pro）** |
| **参数量** | 235B 总参数 / 22B 激活（MoE） |
| **上下文** | **256K** |
| **亮点** | 最大 VLM 之一；超强视频理解；原生多图+交错图文 |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct |

---

### 4. GLM-4.6V（开源，重大更新）🆕
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-12-08（重大更新版本）** |
| **许可证** | **Apache 2.0** |
| **MathVista** | **开源 SOTA** |
| **亮点** | 原生工具调用；131K 上下文；数学推理 VLM 最强 |
| **HuggingFace** | https://huggingface.co/THUDM/GLM-4V-9B |

---

### 5. LLaVA-CoT（开源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025（ICCV 2025）** |
| **许可证** | **MIT** |
| **MMMU** | 超越 Gemini-1.5-pro |
| **亮点** | 视觉链式推理；ICCV 2025 录用；多步推理可视化 |
| **HuggingFace** | https://huggingface.co/WEATHERISHERE/LLaVA-CoT |

---

### 6. Claude Sonnet 4.6（闭源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-17** |
| **许可证** | 🔒专有（API） |
| **MMMU-Pro** | **83.58%（所有 VLM 中最高）** |
| **定价** | $3/1M 输入，$15/1M 输出 |
| **亮点** | 闭源 VLM 绝对领先；原生视觉+计算机使用 |

---

### 7. Gemini 3.1 Pro（闭源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-19** |
| **许可证** | 🔒专有（API） |
| **MMMU-Pro** | **80.5%** |
| **上下文** | **1M tokens** |
| **亮点** | 超长上下文；视频理解+视觉联合处理 |

---

### 8. GLM-5V-Turbo（闭源）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-04-01** |
| **许可证** | 🔒专有（API） |
| **MMMU-Pro** | 61.7% |
| **MathVista** | 71.3% |
| **亮点** | 视觉编程；原生代码生成；Agent 工程优化 |

---

## 💡 VLM 选型指南

| 场景 | 推荐 | 理由 |
|------|------|------|
| 开源综合最强 | **InternVL3.5（MIT）** | MMMU 77.7%，Cascade RL 控幻觉 |
| 开源最新+MIT | **Kimi K2.5（MIT）** | MMMU-Pro 78.5%，MathVista 90.1% |
| 视频+超长上下文 | **Qwen3-VL-235B（Apache 2.0）** | 256K，MoE，性价比 |
| 数学推理开源 | **GLM-4.6V（Apache 2.0）** | MathVista 开源 SOTA |
| 闭源 VLM 最强 | **Claude Sonnet 4.6** | MMMU-Pro 83.58% |
| 超长上下文闭源 | **Gemini 3.1 Pro** | 1M tokens |
| 视觉编程 | **GLM-5V-Turbo** | Agent 优化，代码生成 |

---

*数据来源：MMMU 官方排行榜 / 各模型 GitHub / HuggingFace | 2026-04-05 调研核实*
