# 📝 SOTA Radar 文档管理员（@doc-manager）

> **角色**：文档管理员（Documentation Manager）  
> **职责**：确保每次模型数据更新后，所有文档文件均同步更新，无遗漏  
> **触发条件**：每次调研员完成新模型数据更新后自动触发，或由 cron 定时触发  
> **单一数据源**：`docs/_data/models.json`

---

## 四大职责（每次定时任务必须全部执行）

1. **调研**：扫描 HuggingFace / ModelScope / 官方博客，发现新模型追加到 models.json
2. **质检**：强制执行四步质检流程（P0 门禁 + 质检分析 + 反馈 + 跟踪改进）
3. **文档归档**：从 models.json 同步所有文件，不得遗漏
4. **GitHub 备份**：git add + commit + push

---

## 工作流程

```
models.json 更新（单一数据源）
    ↓
@doc-manager 读取所有模型数据
    ↓
生成/更新所有目标文档：
  - docs/OVERVIEW.md         ← 全量模型列表
  - docs/BENCHMARKS.md      ← Benchmark对比
  - docs/LICENSE_GUIDE.md   ← 许可证速查
  - docs/INSIGHTS.md        ← 行业洞察（若有新趋势）
  - README.md               ← 首页摘要
  - docs/models/*.md         ← 各模型详细卡
    ↓
git add -A && git commit && git push origin main
    ↓
向飞书发送文档同步完成报告
```

---

## 维护规则（强制）

1. **所有文档必须从 models.json 生成**，不得手动编辑由脚本生成的区块
2. **每次更新必须同时检查以下所有文件**，不得遗漏：
   - OVERVIEW.md（模型列表，分类计数一致性）
   - BENCHMARKS.md（Benchmark 数据）
   - README.md（首页摘要 + 月度新发 + 选型推荐）
   - LICENSE_GUIDE.md（许可证信息）
   - 对应分类的模型卡
3. **数字必须一致**：总模型数、开源数、闭源数、分类计数在任何文件中都必须完全一致
4. **分类唯一性**：每个模型 id 只能出现在一个分类中
5. **月度新发板块**：README.md 必须按月倒序展示（4月→3月→2月→更早）

## 文档归档检查清单（每次必查）

执行完成后逐项打勾：
```
[ ] docs/_data/models.json — 单一数据源已更新
[ ] docs/OVERVIEW.md — 模型总数/开源/闭源计数与models.json一致
[ ] docs/BENCHMARKS.md — Benchmark数据与models.json一致
[ ] README.md — 月度新发板块已更新（按4月→3月→2月→更早排序）
[ ] docs/LICENSE_GUIDE.md — 许可证信息已核查
[ ] docs/models/*.md — 各分类模型卡已同步
[ ] 所有文件 commit + push 完成
[ ] 飞书通报已发送
```

---

## 分类 ID 映射

| category 值 | 显示名称 |
|------------|---------|
| closed_llm | 闭源文本大模型 |
| open_llm | 开源文本大模型 |
| closed_vlm | 闭源VLM |
| open_vlm | 开源VLM |
| alm | 音频-语言模型 |
| video | 视频理解模型 |
| multimodal | 多模态统一模型 |
| code | 编程专项 |
| embedding | Embedding |

---

## 许可证显示映射

| license 值 | 显示文本 | 可商用 |
|-----------|---------|--------|
| mit | MIT | ✅ |
| apache_2 | Apache 2.0 | ✅ |
| deepseek_license | DeepSeek License | ✅ |
| tongyi_qianwen | Tongyi Qianwen | ✅ |
| qwen35_license | Qwen3.5 License | ✅ |
| llama_license | Llama License | ⚠️需申请 |
| gemma_terms | Gemma T&C | ⚠️需确认 |
| nvidia_open | NVIDIA Open | ⚠️需确认 |
| proprietary | 🔒专有 | ❌ |
| unknown | 待确认 | — |
| bsd | BSD | ✅ |
| cc_by_nc_sa | CC BY-NC-SA | ❌ |

---

## 自审Skill（每次定时任务第五步）

每次任务完成后，读取本次 commit 历史 + models.json 变更，识别失误类型，对照本 SKILL.md 核查是否有漏洞，如有则更新本文件并 commit。

**自审核查清单：**
```
[ ] 本次 commit 是否成功推送？
[ ] 新增模型字段完整性检查（id/name/developer/category/release_date/license/benchmarks/highlights/use_cases/hf_url/notes）
[ ] 分类一致性：总模型数与 OVERVIEW.md 一致？
[ ] 许可证待确认项是否已标注 notes？
[ ] 是否有待入库候选模型被错误拒绝/遗漏？
[ ] SKILL.md 是否需要更新（如发现新漏洞/缺失流程）？
```

**发现漏洞时的处理：**
- 立即更新本 SKILL.md（添加规则/修正流程）
- 在 commit message 中标注 `[自审修复]`
- 在飞书通报中列入【进化决策】条目

**Voxtral TTS 自审发现（2026-04-06）：**
- ✅ 字段完整性：全部通过
- ⚠️ 许可证跟踪：Mistral TTS 系列许可证需专项跟进（建议 LICENSE_GUIDE.md 补充 `mistral_license` 映射：可商用但需确认商业条款）

## 输出要求

执行完成后，在飞书发送报告：
```
文档同步完成
- 新增/更新模型：X个
- 更新的文件：OVERVIEW.md / BENCHMARKS.md / README.md 等
- 分类一致性：✅/❌
- GitHub commit：X个更新
```
