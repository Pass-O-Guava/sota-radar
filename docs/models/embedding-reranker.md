# 🔢 Embedding & Reranker 模型

> **数据来源**：MTEB 官方排行榜 + HuggingFace  | **可靠度评级**：A（以 MTEB / CMTEB 官方评测为准）

---

## 📊 MTEB 排行榜（英文）

| 模型 | 开发方 | 发布日期 | 许可证 | MTEB 得分 | 备注 |
|------|--------|----------|--------|-----------|------|
| **NV-Embed-v2** | NVIDIA | 2025-08 | NVIDIA License ⚠️ | **69.32** | MTEB 持续第一 |
| bge-m3 | 北京AI Lab | 2024-02 | Apache 2.0 | ~63.0 | 多语言+多功能 |
| 其他 | — | — | — | <69 | — |

---

## 📊 CMTEB 排行榜（中文）

| 模型 | 开发方 | 发布日期 | 许可证 | CMTEB 得分 | 备注 |
|------|--------|----------|--------|-----------|------|
| **Youtu-Embedding** | 腾讯优图 | 2025-08 | 🔒专有 | **77.58** | CMTEB 第一 |
| **Qwen3-VL-Embedding** | 阿里巴巴 | 2026-01 | ✅开源（Apache 2.0） | MMEB-V2: 77.8 | 多模态 #1 |

---

## 逐模型详情

### 1. NV-Embed-v2 🆕
| 字段 | 内容 |
|------|------|
| **开发方** | NVIDIA |
| **发布日期** | **2024-08（v2）** |
| **许可证** | ⚠️ NVIDIA License（非商业默认，申请后可商用） |
| **MTEB** | **69.32（#1）** |
| **基础模型** | Llama-3.1-8B微调 |
| **亮点** | MTEB 排行榜持续第一；大规模微调embedding模型 |
| **HuggingFace** | https://huggingface.co/nvidia/NV-Embed-v2 |

---

### 2. Qwen3-VL-Embedding 🆕
| 字段 | 内容 |
|------|------|
| **开发方** | 阿里巴巴（Qwen Team） |
| **发布日期** | **2026-01（HuggingFace 首发）** |
| **许可证** | **✅ Apache 2.0（开源可商用）** |
| **MMEB-V2** | **77.8（#1）** |
| **模态** | 多模态：文本+图像+视频 |
| **语言** | 30+ 语言 |
| **亮点** | 开源多模态 Embedding 第一；可处理图像和视频检索 |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B |

---

### 3. bge-m3
| 字段 | 内容 |
|------|------|
| **开发方** | 北京人工智能研究院（BAAI） |
| **发布日期** | **2024-02** |
| **许可证** | **✅ Apache 2.0（开源可商用）** |
| **MTEB** | ~63.0 |
| **3M 特性** | Multi-functionality · Multi-linguality · Multi-granularity |
| **亮点** | 最早的开源多语言 MTEB 方案；支持100+语言 |
| **HuggingFace** | https://huggingface.co/BAAI/bge-m3 |

---

### 4. Youtu-Embedding 🆕
| 字段 | 内容 |
|------|------|
| **开发方** | 腾讯优图实验室 |
| **发布日期** | **2025-08** |
| **许可证** | 🔒专有（腾讯云 API） |
| **CMTEB** | **77.58（#1）** |
| **亮点** | 中文语义检索 CMTEB 第一；腾讯云直接调用 |
| **现状** | 仅通过腾讯云 API 提供，不开源权重 |

---

## 💡 选型指南

| 场景 | 推荐 | 理由 |
|------|------|------|
| 中文语义检索（API） | **Youtu-Embedding** | CMTEB 77.58，中文第一 |
| 英文语义检索（API） | **NV-Embed-v2** | MTEB 69.32，持续第一 |
| 开源多模态 Embedding | **Qwen3-VL-Embedding** | Apache 2.0，MMEB-V2 77.8 |
| 开源多语言（可商用） | **bge-m3** | Apache 2.0，100+语言 |

---

*数据来源：MTEB 官方排行榜 / HuggingFace / 腾讯云官方 | 2026-04-05 调研核实*
