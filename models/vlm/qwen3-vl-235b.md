# Qwen3-VL-235B-A22B

> **可靠度：A** | **调研日期：2026-04-05**

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Qwen3-VL-235B-A22B-Instruct |
| **发布方** | 阿里巴巴通义实验室 |
| **参数量** | 235B 总参数 / **22B 激活参数**（MoE） |
| **支持的模态** | 文本 + 图像 + 视频 + 多图 + 交错图文 |
| **许可协议** | Tongyi Qianwen License（可商用） |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct |
| **ModelScope** | https://modelscope.cn/models/Qwen/Qwen3-VL-235B-A22B-Instruct |
| **发布日期** | **2025-09-23** |
| **技术报告** | 2025-09-22（Qwen 官方博客） |

## 核心能力

- **235B MoE 架构**：22B 激活参数即可达到顶级效果，推理成本可控
- **256K 超长上下文**：支持 256K token 窗口，可处理长文档、图表理解
- **原生视频理解**：支持小时级长视频，具备时间推理能力
- **空间智能**：增强三维布局、图表、场景理解
- **多语言 OCR**：支持 32+ 语言文档识别

## Benchmark 参考

| Benchmark | 成绩 | 来源 |
|-----------|------|------|
| MMMU | ~74% | 官方 GitHub |
| MathVista | ~71% | 官方 GitHub |
| OCRBench | ~870 | 官方 |

## 许可证与商用合规

✅ **Tongyi Qianwen License — 可商用**，需遵守输出合规条款

## 入选理由

Qwen 系列开源视觉语言最强旗舰，MoE 架构兼顾性能与成本，256K 上下文在长文档和视频理解场景具有明显优势。
