# ⚡ 编程/推理专项模型

> **数据来源**：官方 GitHub + HuggingFace + 第三方评测  | **可靠度评级**：A/B/C
> **说明**：部分模型同时出现在其他分类（如 o4-mini 在闭源文本类），此处以编程/推理专项视角为主。

---

## 📊 横向对比

| 模型 | 开发方 | 发布日期 | 许可证 | SWE-bench | HumanEval | AIME | 定价 |
|------|--------|----------|--------|-----------|-----------|------|------|
| **Mistral Small 4** 🆕 | Mistral AI | 2026-03-16 | ✅开源（Apache 2.0） | — | — | — | — |
| **Qwen3-Coder-Next** | 阿里巴巴 | 2026-02-04 | ✅开源（Tongyi） | >70% | — | — | — |
| **DeepSeek-R1** | DeepSeek | 2025-01-20 | ✅开源 | 超越 o1 | — | **~86%** | — |
| **MiniMax M2.5** | MiniMax | 2026-02-12 | ✅开源（Apache 2.0） | **80.2%** | — | — | $1/h |
| **o4-mini** | OpenAI | 2025-04-15 | 🔒专有 | ~68.1% | ~99% | 92.7% | $1.1/1M |
| **Grok 4.20 reasoning** | xAI | 2026-03 | 🔒专有 | — | — | — | $2/1M |
| **Claude Sonnet 4.6** | Anthropic | 2026-02-17 | 🔒专有 | 79.6% | ~96% | — | $3/1M |

---

## 逐模型详情

### 1. Mistral Small 4 🆕
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-03-15/16** |
| **许可证** | **Apache 2.0（✅开源可商用）** |
| **架构** | 119B MoE，混合专家模型 |
| **上下文** | 128K |
| **亮点** | 统一instruct+reasoning+coding多模态；Apache 2.0开源；NVIDIA Build首发 |
| **HuggingFace** | https://huggingface.co/mistralai/mistral-small-2603 |

---

### 2. Qwen3-Coder-Next
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-03/04** |
| **许可证** | Tongyi Qianwen License（✅可商用） |
| **架构** | 80B 总参数 MoE / 3B 激活参数 |
| **SWE-Bench** | >70%（SWE-Agent Eval）|
| **AA Index** | 28（Artificial Analysis） |
| **τ²-Bench** | ~80% |
| **亮点** | 动态稀疏 MoE；128K 上下文；支持 OpenClaw/Claude Code/Cline |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-Coder-Next |

---

### 3. DeepSeek-R1
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-01-20**（R1-0528 更新：2025-05） |
| **许可证** | DeepSeek License（✅可商用） |
| **架构** | 671B 总参数 MoE / 37B 激活参数 |
| **AIME 2024** | ~86%（开源最强） |
| **亮点** | 强化学习驱动推理能力突破；蒸馏版以小博大；开源推理分水岭 |
| **HuggingFace** | https://huggingface.co/deepseek-ai/DeepSeek-R1 |

---

### 4. MiniMax M2.5
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-12** |
| **许可证** | **Apache 2.0（✅开源可商用）** |
| **SWE-bench Verified** | **80.2%** |
| **亮点** | 开源编程 SOTA；$1/小时（50 tokens/s）；接近 Claude Opus 4.6 水平；Agentic RL |
| **HuggingFace** | https://huggingface.co/blog/mlabonne/minimax-m25 |

---

### 5. o4-mini
| 字段 | 内容 |
|------|------|
| **发布日期** | **2025-04-15** |
| **许可证** | 🔒专有（API） |
| **SWE-bench** | ~68.1% |
| **AIME 2025** | **92.7%** |
| **HumanEval** | ~99% |
| **定价** | $1.10/1M 输入，$4/1M 输出 |
| **亮点** | OpenAI 高性价比推理模型；Codeforces SOTA；完整工具访问 |

---

### 6. Grok 4.20 reasoning
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-03（Beta）** |
| **许可证** | 🔒专有（API） |
| **上下文** | **2M tokens（行业最大）** |
| **Artificial Analysis Index** | 40/100（reasoning 模式） |
| **非幻觉率** | **78%（世界纪录）** |
| **定价** | $2/1M 输入，$6/1M 输出 |
| **亮点** | 2M 超长上下文；原生实时搜索集成；比 Grok 4 思考 token 减少 40% |

---

### 7. Claude Sonnet 4.6
| 字段 | 内容 |
|------|------|
| **发布日期** | **2026-02-17** |
| **许可证** | 🔒专有（API） |
| **SWE-bench Verified** | 79.6% |
| **OSWorld** | 94% |
| **HumanEval** | ~96% |
| **定价** | $3/1M 输入，$15/1M 输出 |
| **亮点** | 性价比最高的编程 Agent 模型；OSWorld 94%（Anthropic 内部保险基准最高） |

---

## 💡 选型指南

| 场景 | 推荐 | 理由 |
|------|------|------|
| 开源可商用编程 | **MiniMax M2.5** | Apache 2.0，SWE-bench 80.2%，$1/h |
| 开源推理能力 | **DeepSeek-R1** | AIME ~86%，开源推理标杆 |
| 编程开源性价比 | **Qwen3-Coder-Next** | 80B MoE，3B 激活，支持多种 IDE |
| 闭源编程综合 | **Claude Sonnet 4.6** | $3/1M，SWE-bench 79.6%，OSWorld 94% |
| 数学推理性价比 | **o4-mini** | $1.1/1M，AIME 92.7% |
| 超长上下文推理 | **Grok 4.20** | 2M tokens，78% 非幻觉率 |

---

*数据来源：各模型官方 GitHub / HuggingFace / Artificial Analysis | 2026-04-05 调研核实*
