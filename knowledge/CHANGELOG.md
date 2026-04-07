# 变更日志 SOTA Radar

## v0.4 — 2026-04-07 三团队自查整改

### P0 修复（12个模型全面重写）

- Qwen3-VL-235B-A22B：修正发布日期 2025-09-23；移除 SOTA 标注（GLM-5V-Turbo MMMU 79% 已超越）
- GLM-5V-Turbo：保留 VLM SOTA（MMMU ~79%）
- Kimi K2.5 / QWQ-32B / GLM-5-9B-0414：移除 SOTA 标注，降级为特色模型
- GLM-4-9B-Chat：修正发布日期 2024-01-25（历史参考模型）
- Janus-Pro-7B：修正发布方为 DeepSeek AI（非字节跳动）
- Step-3.5-Flash：补全缺失字段，标注待核实项

所有模型：frontmatter 规范化（published_date/indexed_date 分离），更新时间精确到分钟，文件结构清理完成。

### 质检结果：22问题（10 P0 / 7 P1 / 5 P2）

### 待执行缺口

- Embedding 分类完全缺失（待入库）
- 闭源 VLM 缺失（GPT-4o / Claude 3.5 Sonnet / Gemini 2.0 Flash）
- 自进化 SOP 完善（self-review.md / archiver.md）
