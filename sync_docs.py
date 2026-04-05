#!/usr/bin/env python3
"""Sync all docs from models.json data"""
import json, re, datetime

with open('docs/_data/models.json') as f:
    data = json.load(f)
models = data['models']
today = str(datetime.date.today())

# Count helpers
closed_llm = [m for m in models if m['category'] == 'closed_llm']
open_llm   = [m for m in models if m['category'] == 'open_llm']
closed_vlm = [m for m in models if m['category'] == 'closed_vlm']
open_vlm   = [m for m in models if m['category'] == 'open_vlm']
alms       = [m for m in models if m['category'] == 'alm']
videos     = [m for m in models if m['category'] == 'video']
codes      = [m for m in models if m['category'] == 'code']
imgs       = [m for m in models if m['category'] == 'image_generation']
mmodal     = [m for m in models if m['category'] == 'multimodal']
emb        = [m for m in models if m['category'] == 'embedding']

total = len(models)
open_total = len(alms) + len(open_llm) + len(open_vlm) + len(videos) + len(codes) + len(mmodal) + len(emb) + len(imgs)
closed_total = len(closed_llm) + len(closed_vlm)

# ──────────────────────────────────────────────
# 1. OVERVIEW.md
# ──────────────────────────────────────────────
overview = f"""# 📋 SOTA Radar 完整模型列表（{today} 最终版）

> **分类原则**：按「许可证类型 + 模态」双重维度分类，开源/闭源绝不混列  
> **数据截止**：{today} | **来源**：HuggingFace + ModelScope + 官方博客 实地核查

---

## 分类总览

| 分类 | 总数 | 闭源 | 开源 |
|------|------|------|------|
| 🅐 闭源文本与推理模型 | **{len(closed_llm)}** | {len(closed_llm)} | — |
| 🅐 开源文本大模型 | {len(open_llm)} | — | {len(open_llm)} |
| 🅱 闭源 VLM | {len(closed_vlm)} | {len(closed_vlm)} | — |
| 🅱 开源 VLM | {len(open_vlm)} | — | {len(open_vlm)} |
| 🎧 音频-语言模型 | {len(alms)} | 0 | {len(alms)} |
| 🎬 视频理解模型 | {len(videos)} | 0 | {len(videos)} |
| 🎨 图像生成模型 | {len(imgs)} | {len([m for m in models if m['category']=='image_generation' and m.get('license')=='proprietary'])} | {len([m for m in models if m['category']=='image_generation' and m.get('license')!='proprietary'])} |
| ⚡ 编程/推理专项 | {len(codes)} | {len([m for m in codes if m.get('license')=='proprietary'])} | {len([m for m in codes if m.get('license')!='proprietary'])} |
| 🔮 多模态统一模型 | {len(mmodal)} | 0 | {len(mmodal)} |
| 🔢 Embedding & Reranker | {len(emb)} | {len([m for m in emb if m.get('license')=='proprietary'])} | {len([m for m in emb if m.get('license')!='proprietary'])} |
| **合计** | **{total}** | **{closed_total}** | **{open_total}** |

---

## 🅐 闭源文本与推理模型（{len(closed_llm)}个）🔒专有

| # | 模型 | 开发商 | 发布日期 | MMLU | 亮点 |
|---|------|--------|----------|------|------|
"""

# Build closed_llm table
for i, m in enumerate(sorted(closed_llm, key=lambda x: x.get('release_date','0000')), 1):
    bm = m.get('benchmarks', {})
    mmlu = bm.get('mmlu', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    release = m.get('release_date', '—')
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {mmlu} | {highlights} |\n"

overview += f"""
**详细数据** → [`models/text/proprietary-text.md`](./models/text/proprietary-text.md)

---

## 🅐 开源文本大模型（{len(open_llm)}个）✅可商用

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
"""

for i, m in enumerate(sorted(open_llm, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    license_ = m.get('license', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    release = m.get('release_date', '—')
    hf = f"[HF]({m.get('hf_url','')})" if m.get('hf_url') and m['hf_url'] not in ('','待确认','待核实') else ''
    overview += f"| {i} | **{m['name']}** {hf} | {m.get('developer','—')} | {release} | {license_} | {highlights} |\n"

overview += f"""
**详细数据** → [`models/text/open-text.md`](./models/text/open-text.md)

---

## 🅱 闭源 VLM（{len(closed_vlm)}个）🔒专有

| # | 模型 | 开发商 | 发布日期 | MMMU-Pro | 亮点 |
|---|------|--------|----------|----------|------|
"""

for i, m in enumerate(sorted(closed_vlm, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    bm = m.get('benchmarks', {})
    mmmu = bm.get('mmmup_pro', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    release = m.get('release_date', '—')
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {mmmu} | {highlights} |\n"

overview += f"""
**详细数据** → [`models/vlm/closed-vlm.md`](./models/vlm/closed-vlm.md)

---

## 🅱 开源 VLM（{len(open_vlm)}个）✅可商用

| # | 模型 | 开发方 | 发布日期 | MMMU-Pro | 许可证 | 亮点 |
|---|------|--------|----------|----------|--------|------|
"""

for i, m in enumerate(sorted(open_vlm, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    bm = m.get('benchmarks', {})
    mmmu = bm.get('mmmup_pro', bm.get('mmmup','—'))
    license_ = m.get('license', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    release = m.get('release_date', '—')
    hf = f"[HF]({m.get('hf_url','')})" if m.get('hf_url') and m['hf_url'] not in ('','待确认','待核实') else ''
    overview += f"| {i} | **{m['name']}** {hf} | {m.get('developer','—')} | {release} | {mmmu} | {license_} | {highlights} |\n"

overview += f"""
**详细数据** → [`models/vlm/open-vlm.md`](./models/vlm/open-vlm.md)

---

## 🎧 音频-语言模型（{len(alms)}个）✅可商用

| # | 模型 | 开发方 | 发布日期 | 类型 | 亮点 |
|---|------|--------|----------|------|------|
"""

for i, m in enumerate(sorted(alms, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {m['id']} | {highlights} |\n"

overview += f"""
---

## 🎬 视频理解模型（{len(videos)}个）✅可商用

| # | 模型 | 开发方 | 发布日期 | 亮点 |
|---|------|--------|----------|------|
"""

for i, m in enumerate(sorted(videos, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {highlights} |\n"

overview += f"""
---

## 🎨 图像生成模型（{len(imgs)}个）

| # | 模型 | 开发方 | 发布日期 | 亮点 |
|---|------|--------|----------|------|
"""

for i, m in enumerate(sorted(imgs, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {highlights} |\n"

overview += f"""
---

## ⚡ 编程/推理专项（{len(codes)}个）

| # | 模型 | 开发方 | 发布日期 | SWE-bench | 亮点 |
|---|------|--------|----------|-----------|------|
"""

for i, m in enumerate(sorted(codes, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    bm = m.get('benchmarks', {})
    swe = bm.get('swe_bench', '—')
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {swe} | {highlights} |\n"

overview += f"""
---

## 🔮 多模态统一模型（{len(mmodal)}个）

| # | 模型 | 开发方 | 发布日期 | 亮点 |
|---|------|--------|----------|------|
"""

for i, m in enumerate(sorted(mmodal, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {highlights} |\n"

overview += f"""
---

## 🔢 Embedding & Reranker（{len(emb)}个）

| # | 模型 | 开发方 | 发布日期 | 许可证 | 亮点 |
|---|------|--------|----------|--------|------|
"""

for i, m in enumerate(sorted(emb, key=lambda x: x.get('release_date','0000'), reverse=True), 1):
    license_ = m.get('license', '—')
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    overview += f"| {i} | **{m['name']}** | {m.get('developer','—')} | {release} | {license_} | {highlights} |\n"

overview += f"""
---

*SOTA Radar · 数据每日自动更新 · 来源：HuggingFace / ModelScope / 官方博客*
"""

with open('docs/OVERVIEW.md', 'w') as f:
    f.write(overview)
print(f"✅ Updated docs/OVERVIEW.md ({total} models)")

# ──────────────────────────────────────────────
# 2. BENCHMARKS.md — update counts and data
# ──────────────────────────────────────────────
bench_intro = f"""# 📊 Benchmark 横向对比

> 来源：各模型官方 GitHub / HuggingFace / MMMU/MathVista 官方排行榜 | A=官方 / B=第三方
> 注：跨模型数据因评测条件差异，仅供趋势参考；MMMU 与 MMMU-Pro 难度不同，谨慎跨版本对比  
> **数据截止**：{today}

---

## 🅐 闭源文本与推理模型

| 模型 | 发布日期 | MMLU | GPQA | SWE-bench | HumanEval | AIME |
|------|----------|------|------|-----------|-----------|------|
"""

# Closed LLM benchmarks
for m in sorted(closed_llm, key=lambda x: x.get('release_date','0000'), reverse=True):
    bm = m.get('benchmarks', {})
    mmlu = bm.get('mmlu', '—')
    gpqa = bm.get('gpqa', '—')
    swe = bm.get('swe_bench', '—')
    he = bm.get('humaneval', '—')
    aime = bm.get('aime_2025', bm.get('aime', '—'))
    release = m.get('release_date', '—')
    bench_intro += f"| **{m['name']}** | {release} | {mmlu} | {gpqa} | {swe} | {he} | {aime} |\n"

bench_intro += f"""
---

## 🅐 开源文本大模型

| 模型 | 发布日期 | MMLU | HumanEval | AIME | MATH-500 | SWE-bench |
|------|----------|------|-----------|------|----------|-----------|
"""

for m in sorted(open_llm, key=lambda x: x.get('release_date','0000'), reverse=True):
    bm = m.get('benchmarks', {})
    mmlu = bm.get('mmlu', '—')
    he = bm.get('humaneval', '—')
    aime = bm.get('aime_2025', bm.get('aime', '—'))
    math = bm.get('math_500', '—')
    swe = bm.get('swe_bench', '—')
    release = m.get('release_date', '—')
    bench_intro += f"| **{m['name']}** | {release} | {mmlu} | {he} | {aime} | {math} | {swe} |\n"

bench_intro += f"""
---

## 🅱 闭源 VLM（按 MMMU-Pro 排序）

| 模型 | 发布日期 | MMMU-Pro | 亮点 |
|------|----------|----------|------|
"""

def safe_float(v, default=0.0):
    try:
        return float(str(v).replace('%','').replace('~','').strip())
    except:
        return default

for m in sorted(closed_vlm, key=lambda x: safe_float(x.get('benchmarks',{}).get('mmmup_pro','0')), reverse=True):
    bm = m.get('benchmarks', {})
    mmmu = bm.get('mmmup_pro', '—')
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    bench_intro += f"| **{m['name']}** | {release} | {mmmu} | {highlights} |\n"

bench_intro += f"""
---

## 🅱 开源 VLM（按 MMMU-Pro 排序）

| 模型 | 发布日期 | MMMU-Pro | MathVista | 亮点 |
|------|----------|----------|-----------|------|
"""

for m in sorted(open_vlm, key=lambda x: safe_float(x.get('benchmarks',{}).get('mmmup_pro',x.get('benchmarks',{}).get('mmmup','0'))), reverse=True):
    bm = m.get('benchmarks', {})
    mmmu = bm.get('mmmup_pro', bm.get('mmmup','—'))
    mathv = bm.get('mathvista', '—')
    release = m.get('release_date', '—')
    highlights = '；'.join(m.get('highlights', [])[:2])
    bench_intro += f"| **{m['name']}** | {release} | {mmmu} | {mathv} | {highlights} |\n"

bench_intro += f"""
---

*数据截止：{today} · 来源：官方博客 / HuggingFace / 第三方评测*
"""

with open('docs/BENCHMARKS.md', 'w') as f:
    f.write(bench_intro)
print(f"✅ Updated docs/BENCHMARKS.md")

# ──────────────────────────────────────────────
# 3. README.md — update counts, new releases section
# ──────────────────────────────────────────────
readme = f"""# 🤖 SOTA Radar — 追踪最新开源大模型

> **每日更新** · 量化选型 · 商用合规指南  
> **数据截止**：{today} | **模型总数**：{total} 个 | **开源**：{open_total} 个 | **闭源**：{closed_total} 个

---

## 📊 实时全览

| 分类 | 总数 | 闭源 | 开源 |
|------|------|------|------|
| 🅐 闭源文本与推理模型 | **{len(closed_llm)}** | {len(closed_llm)} | — |
| 🅐 开源文本大模型 | {len(open_llm)} | — | {len(open_llm)} |
| 🅱 闭源 VLM | {len(closed_vlm)} | {len(closed_vlm)} | — |
| 🅱 开源 VLM | {len(open_vlm)} | — | {len(open_vlm)} |
| 🎧 音频-语言模型 | {len(alms)} | 0 | {len(alms)} |
| 🎬 视频理解模型 | {len(videos)} | 0 | {len(videos)} |
| 🎨 图像生成模型 | {len(imgs)} | {len([m for m in models if m['category']=='image_generation' and m.get('license','')=='proprietary'])} | {len([m for m in models if m['category']=='image_generation' and m.get('license','')!='proprietary'])} |
| ⚡ 编程/推理专项 | {len(codes)} | {len([m for m in codes if m.get('license','')=='proprietary'])} | {len([m for m in codes if m.get('license','')!='proprietary'])} |
| 🔮 多模态统一模型 | {len(mmodal)} | 0 | {len(mmodal)} |
| 🔢 Embedding & Reranker | {len(emb)} | {len([m for m in emb if m.get('license','')=='proprietary'])} | {len([m for m in emb if m.get('license','')!='proprietary'])} |

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

*自动更新 · SOTA Radar · {today}*
"""

with open('README.md', 'w') as f:
    f.write(readme)
print(f"✅ Updated README.md")

# ──────────────────────────────────────────────
# 4. LICENSE_GUIDE.md — quick count update
# ──────────────────────────────────────────────
lg = f"""# 📜 许可证合规指南

> 许可证核查 · 商用风险提示 · 来源：各模型官方 LICENSE 页面  
> **数据截止**：{today}

---

## 主流许可证一览

| 许可证 | 可商用 | 可修改 | 可分发 | 开源合规 | 代表模型 |
|--------|--------|--------|--------|----------|---------|
| **Apache 2.0** | ✅ | ✅ | ✅ | ✅ 完全开源 | GLM-5, InternVL3.5, Gemma 4 🆕 |
| **MIT** | ✅ | ✅ | ✅ | ✅ 完全开源 | Kimi K2.5, MiniMax M2.5 |
| **DeepSeek License** | ✅（需保留版权） | ✅ | ✅ | ✅ 基本自由 | DeepSeek-V3, DeepSeek-R1 |
| **Qwen License** | ✅（需申请） | ⚠️ | ⚠️ | ⚠️ 部分限制 | Qwen3.5系列, Qwen3-VL |
| **Llama License** | ⚠️（需向Meta申请） | ⚠️ | ❌ | ⚠️ 研究转商用 | Llama 3.3 |
| **Proprietary** | ❌ | ❌ | ❌ | ❌ | GPT-5, Claude Opus 4.6, Gemini系列 |

---

## 完全开源可商用（Apache 2.0 / MIT）

> 无需申请，商用无忧

| 模型 | 许可证 | 链接 |
|------|--------|------|
| **GLM-5** | MIT | [HF](https://huggingface.co/zai-org/GLM-5) |
| **GLM-5.1** 🆕 | MIT | 权重{today[:10]}后开源 |
| **Kimi K2.5** | MIT | [HF](https://huggingface.co/moonshotai/Kimi-K2.5) |
| **InternVL3.5** | MIT | [HF](https://huggingface.co/OpenGVLab/InternVL3_5-8B) |
| **Gemma 4 31B** 🆕 | **Apache 2.0** | [HF](https://huggingface.co/google/gemma-4) |
| **Gemma 4 26B-A4B** 🆕 | **Apache 2.0** | [HF](https://huggingface.co/google/gemma-4) |
| **Gemma 4 E4B** 🆕 | **Apache 2.0** | [HF](https://huggingface.co/google/gemma-4) |
| **Gemma 4 E2B** 🆕 | **Apache 2.0** | [HF](https://huggingface.co/google/gemma-4) |
| **MiniMax M2.5** | Apache 2.0 | [HF](https://huggingface.co/blog/mlabonne/minimax-m25) |
| **bge-m3** | Apache 2.0 | — |
| **NV-Embed-v2** | NVIDIA（非商业默认） | — |

---

## 需申请或有限制

| 模型 | 许可证 | 申请 | 注意事项 |
|------|--------|------|---------|
| **Qwen3.5系列** | Qwen License | 需申请 | 不可直接商用 |
| **Qwen3-VL系列** | Apache 2.0 | — | 明确Apache 2.0 |
| **Llama 3.3** | Llama License | 向Meta申请 | 仅限研究 |

---

## 闭源 API（不可私有化部署）

GPT-5 / Claude Opus 4.6 / Claude Sonnet 4.6 / Gemini 3.1 Pro / Grok 4.20 / GPT-4o 等。

---

*数据截止：{today} · 请以官方 LICENSE 最新版本为准*
"""

with open('docs/LICENSE_GUIDE.md', 'w') as f:
    f.write(lg)
print(f"✅ Updated docs/LICENSE_GUIDE.md")

print("\n📦 Summary:")
print(f"  Total models: {total}")
print(f"  Open source: {open_total}")
print(f"  Closed source: {closed_total}")
