# 🔒 许可证与商用合规指南

> 选型第一步：确认能否商用。本文档提供快速判断依据。

---

## 快速判断流程

```
这个模型能商用吗？

├─ 是否开源权重？
│   ├─ YES → 看具体许可证
│   └─ NO  → ❌ 通常不可商用（除非API平台授权）
│
├─ 许可证类型？
    ├─ MIT / Apache 2.0 / BSD / DeepSeek License / Tongyi Qianwen
    │   └─ ✅ 通常可商用（见具体条款）
    │
    ├─ Llama License
    │   └─ ⚠️ 需申请（Meta官方授权）
    │
    ├─ CC BY-NC-SA（非商业+相同方式共享）
    │   └─ ❌ 不可商用
    │
    └─ 专有模型（API调用）
        └─ ⚠️ 仅API平台授权范围内可用
```

---

## 许可证速查表

| 许可证 | 商用 | 代表模型 | 注意事项 |
|--------|------|---------|---------|
| **MIT** | ✅ | Kimi K2.5, GLM-5, MiniMax M2.5, Phi-4-Multimodal, InternVL3.5 | 无附加条件 |
| **Apache 2.0** | ✅ | InternVL3.5, Mistral Small 3, Show-o2, CogVLM2-Video, Step-3.5-Flash | 无附加条件 |
| **Tongyi Qianwen** | ✅ | Qwen3-VL, Qwen3-Omni, Qwen3.5系列, Qwen3-Coder-Next | 需遵守输出合规条款 |
| **DeepSeek License** | ✅ | DeepSeek-R1, DeepSeek-V3, Janus-Pro | 需遵守使用政策 |
| **BSD** | ✅ | MiniCPM-V 4.5 | 无附加条件 |
| **Gemma Terms** | ⚠️ | Gemma 3 | 需阅读Google使用条款 |
| **Llama License** | ⚠️需申请 | Llama 3.x | 需向Meta申请商业授权 |
| **CC BY-NC-SA** | ❌ | SALMONN, video-SALMONN | 禁止商用 |
| **NVIDIA Open** | ⚠️ | Cosmos-Reason2 | 需阅读NVIDIA条款 |
| **🔒 专有** | ❌ | GLM-5V-Turbo, MiniMax M2.7 | 仅API授权范围内 |

---

## 按场景选型（仅列可商用）

| 场景 | 推荐模型 | 许可证 |
|------|---------|--------|
| 商业产品集成 | Kimi K2.5, GLM-5, MiniMax M2.5 | MIT / Apache 2.0 |
| 企业内部署 | InternVL3.5, Qwen3-VL, DeepSeek-V3 | Apache 2.0 / Tongyi Qianwen |
| 学术研究 | 所有开源模型 | — |
| 对外SaaS服务 | Kimi K2.5, GLM-5, MiniMax M2.5, Qwen3-Coder-Next | MIT / Apache 2.0 |
| ❌ 不可商用 | SALMONN, Llama 3.x（未申请）| CC BY-NC-SA / Llama |

---

## 商用合规注意事项

1. **API调用模式**（如 GLM-5V-Turbo、MiniMax M2.7）：仅在平台授权范围内使用，不可将模型权重用于商业产品
2. **Llama License**：即使模型权重可下载，商用仍需向 Meta 单独申请授权
3. **输出合规**：部分许可证（如 Tongyi Qianwen）要求遵守输出内容合规条款
4. **数据隐私**：部署到自有服务器时，需确保输入数据处理符合所在地区法规

---

*本表基于2026年4月各模型官方许可证信息，实际情况请以各模型官方License文件为准。*
