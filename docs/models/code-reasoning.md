# ⚡ 编程/推理专项模型

> **数据来源**：官方 GitHub + HuggingFace + 第三方评测  | **可靠度评级**：A/B/C
> **说明**：部分模型同时出现在其他分类（如 o4-mini 在闭源文本类），此处以编程/推理专项视角为主。

---

## 📊 横向对比

| 模型 | 开发方 | 发布日期 | 许可证 | SWE-bench | AIME | 定价 |
|------|--------|----------|--------|-----------|------|------|
| **MiniMax M2.7** 🆕 | MiniMax | 2026-03-18 | 🔒闭源 | — | — | $0.2~2/M |
| **Mistral Small 4** | Mistral AI | 2026-03-16 | ✅开源（Apache 2.0） | — | — | — |
| **Qwen3-Coder-Next** | 阿里巴巴 | 2026-02-04 | ✅闭源（Tongyi） | >70% | — | — |
| **MiniMax M2.5**（历史） | MiniMax | 2026-02-12 | ✅开源（Modified MIT） | **80.2%** | — | $1/h |
| **Claude Sonnet 4.6** | Anthropic | 2026-02-17 | 🔒闭源 | 79.6% | — | $3/1M |
| **DeepSeek-R1** | DeepSeek | 2025-01-20 | ✅开源 | 超越o1 | **~86%** | — |
| **o4-mini** | OpenAI | 2025-04-15 | 🔒闭源 | ~68% | 92.7% | $1.1/1M |

---

## 逐模型详情

### 1. MiniMax M2.7 🆕 ⭐ 闭源综合最强（编程专项）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-03-18** |
| **许可证** | 🔒闭源（MiniMax API专有） |
| **架构** | 自研，Self-Evolution（自我进化）训练框架 |
| **上下文** | 1M tokens |
| **MM Claw** | 62.7%（接近Claude Sonnet 4.6水平） |
| **SWE-Pro** | **56.22%** |
| **Vals Index** | **59.58%** |
| **亮点** | **首个自我进化AI**：模型分析自身失败案例，自动修改训练框架，迭代自身训练代码（行业首创）；203人团队实现对3000人Anthropic的追赶 |
| **备注** | 非开源，通过MiniMax API调用；MiniMax M2.5（开源版）已降为历史版本 |

---

### 2. Mistral Small 4 🆕
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-03-16** |
| **许可证** | **Apache 2.0（✅开源可商用）** |
| **架构** | 119B MoE，混合专家模型 |
| **上下文** | 128K |
| **亮点** | 统一instruct+reasoning+coding多模态；NVIDIA Build首发 |
| **HuggingFace** | https://huggingface.co/mistralai/mistral-small-2603 |

---

### 3. Qwen3-Coder-Next
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-04** |
| **许可证** | 🔒闭源（Tongyi Qianwen License，API调用） |
| **架构** | 80B 总参数 MoE / 3B 激活参数 |
| **SWE-Bench** | >70%（SWE-Agent Eval）|
| **AA Index** | 28（Artificial Analysis） |
| **τ²-Bench** | ~80% |
| **亮点** | 动态稀疏 MoE；128K 上下文；支持 OpenClaw/Claude Code/Cline |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-Coder-Next |

---

### 4. MiniMax M2.5（历史版本）
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-12** |
| **许可证** | **Modified MIT（✅开源可商用，需署名）** |
| **SWE-bench Verified** | **80.2%** |
| **亮点** | 开源编程 SOTA；$1/小时（50 tokens/s）；Agentic RL |
| **现状** | ⚠️ MiniMax M2.7（闭源，2026-03-18）已发布；M2.5降为历史版本 |
| **HuggingFace** | 需从官方 HuggingFace 页面下载 |

---

### 5. Claude Sonnet 4.6
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-17** |
| **许可证** | 🔒闭源（API） |
| **SWE-bench Verified** | 79.6% |
| **OSWorld** | 94% |
| **HumanEval** | ~96% |
| **定价** | $3/1M 输入，$15/1M 输出 |
| **亮点** | 性价比最高的编程 Agent 模型；OSWorld 94% |

---

### 6. DeepSeek-R1
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-01-20** |
| **许可证** | 🔒闭源（DeepSeek License，API调用） |
| **AIME 2024** | ~86%（开源最强） |
| **亮点** | 强化学习驱动推理能力突破；开源推理分水岭 |
| **HuggingFace** | https://huggingface.co/deepseek-ai/DeepSeek-R1 |

---

### 7. o4-mini
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-04-15** |
| **许可证** | 🔒闭源（API） |
| **SWE-bench** | ~68% |
| **AIME 2025** | **92.7%** |
| **HumanEval** | ~99% |
| **定价** | $1.10/1M 输入，$4/1M 输出 |

---

## 💡 选型指南

| 场景 | 推荐 | 理由 |
|------|------|------|
| 闭源编程综合最强 | **MiniMax M2.7** | 2026-03-18最新发布，MM Claw 62.7%，自我进化技术 |
| 开源可商用编程 | **MiniMax M2.5（历史）** | Modified MIT，SWE-bench 80.2%，$1/h |
| 开源推理能力 | **DeepSeek-R1** | AIME ~86%，开源推理标杆 |
| 编程性价比最优 | **Claude Sonnet 4.6** | $3/1M，SWE-bench 79.6%，OSWorld 94% |
| 数学推理性价比 | **o4-mini** | $1.1/1M，AIME 92.7% |

---

*数据来源：各模型官方页面 + Artificial Analysis | 2026-04-07 调研核实*
