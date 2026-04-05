#!/usr/bin/env python3
import json

with open('docs/_data/models.json', 'r') as f:
    data = json.load(f)

models = data['models']
existing_ids = {m['id'] for m in models}

new_models = []

# 1. Gemma 4 (April 2, 2026) - Apache 2.0 open multimodal
gemma4_models = [
    {
        "id": "gemma-4-e2b",
        "name": "Gemma 4 E2B",
        "developer": "Google DeepMind",
        "category": "open_vlm",
        "release_date": "2026-04-02",
        "license": "apache_2",
        "context_window": "32K",
        "benchmarks": {
            "mmlu_pro": "~52%",
            "math_vision": "~35%"
        },
        "pricing": "",
        "highlights": ["Apache 2.0首次（历史性转变）", "2.3B有效参数/5.1B总参", "手机到工作站全场景", "原生多模态"],
        "use_cases": ["边缘设备AI", "移动端推理", "轻量级多模态任务"],
        "hf_url": "https://huggingface.co/google/gemma-4",
        "notes": "首个Apache 2.0开源Gemma模型，E2B=Edge 2B"
    },
    {
        "id": "gemma-4-e4b",
        "name": "Gemma 4 E4B",
        "developer": "Google DeepMind",
        "category": "open_vlm",
        "release_date": "2026-04-02",
        "license": "apache_2",
        "context_window": "32K",
        "benchmarks": {
            "mmlu_pro": "~58%",
            "math_vision": "~42%"
        },
        "pricing": "",
        "highlights": ["4.5B有效参数/8B总参", "E4B=Edge 4B"],
        "use_cases": ["边缘设备AI", "本地部署"],
        "hf_url": "https://huggingface.co/google/gemma-4",
        "notes": "E4B=Edge 4B，Apache 2.0"
    },
    {
        "id": "gemma-4-26b",
        "name": "Gemma 4 26B-A4B",
        "developer": "Google DeepMind",
        "category": "open_vlm",
        "release_date": "2026-04-02",
        "license": "apache_2",
        "context_window": "32K",
        "benchmarks": {
            "mmlu_pro": "~66%",
            "livecodebench": "~53%",
            "math_vision": "~50%"
        },
        "pricing": "",
        "highlights": ["MoE: 3.8B激活/25.2B总参", "Apache 2.0", "超越更大模型"],
        "use_cases": ["高效推理", "服务器端部署"],
        "hf_url": "https://huggingface.co/google/gemma-4",
        "notes": "MoE架构，3.8B激活参数"
    },
    {
        "id": "gemma-4-31b",
        "name": "Gemma 4 31B",
        "developer": "Google DeepMind",
        "category": "open_vlm",
        "release_date": "2026-04-02",
        "license": "apache_2",
        "context_window": "32K",
        "benchmarks": {
            "mmlu_pro": "~72%",
            "aime_2026": "~36%",
            "gpqa_diamond": "~48%",
            "livecodebench_v6": "~62%",
            "math_vision": "~59%",
            "mmmup_pro": "~55%"
        },
        "pricing": "",
        "highlights": ["旗舰开源VLM", "Apache 2.0", "超越更大竞品", "MMMU-Pro ~55%"],
        "use_cases": ["最强开源VLM", "综合推理"],
        "hf_url": "https://huggingface.co/google/gemma-4",
        "notes": "Gemma 4系列旗舰，Apache 2.0开源"
    },
]

# 2. GLM-5.1 (March 27, 2026 API, weights April 6-7)
glm51 = {
    "id": "glm-51",
    "name": "GLM-5.1",
    "developer": "智谱AI/Z.ai",
    "category": "open_llm",
    "release_date": "2026-03-27",
    "license": "mit",
    "context_window": "200K",
    "benchmarks": {
        "swe_bench_verified": "77.8%",
        "livecodebench": "52.0%",
        "coding_score": "45.3",
        "terminal_bench_2": "56.2pts"
    },
    "pricing": "",
    "highlights": ["SWE-bench Verified 77.8%（开源最高）", "LMArena Text/Code Arena双第一", "华为Ascend芯片训练", "增量升级（聚焦编程+推理）"],
    "use_cases": ["编程", "Agent", "推理"],
    "hf_url": "待确认（zai-org/GLM-5）",
    "notes": "API 2026-03-27上线；权重预计2026-04-06~07开源；94.6% Claude Opus 4.6编程性能"
}

# 3. GPT-5.4 (March 5, 2026)
gpt54 = {
    "id": "gpt-54",
    "name": "GPT-5.4",
    "developer": "OpenAI",
    "category": "closed_llm",
    "release_date": "2026-03-05",
    "license": "proprietary",
    "context_window": "200K",
    "benchmarks": {
        "professional_work": "83%",
        "swe_bench": "~75%",
        "humaneval": "~97%"
    },
    "pricing": "$1.75/1M输入（API）；ChatGPT Pro $200/月",
    "highlights": ["GPT-5.4 Thinking版本", "专业工作83%（超越人类基准）", "桌面导航超越人类表现", "最强编程+Agent"],
    "use_cases": ["专业工作", "Agent工作流", "高级推理"],
    "hf_url": "",
    "notes": "ChatGPT Plus/Pro/Edu可用；最强旗舰型号之一"
}

# 4. Microsoft MAI models (April 2, 2026)
mai_transcribe = {
    "id": "mai-transcribe-1",
    "name": "MAI-Transcribe-1",
    "developer": "Microsoft",
    "category": "alm",
    "release_date": "2026-04-02",
    "license": "proprietary",
    "pricing": "",
    "highlights": ["高质量语音转文字", "Microsoft内部训练"],
    "use_cases": ["会议转写", "语音字幕", "语音控制"],
    "hf_url": "",
    "notes": "Microsoft MAI系列首批模型之一"
}

mai_voice = {
    "id": "mai-voice-1",
    "name": "MAI-Voice-1",
    "developer": "Microsoft",
    "category": "alm",
    "release_date": "2026-04-02",
    "license": "proprietary",
    "pricing": "",
    "highlights": ["1秒生成60秒音频", "高质量语音合成"],
    "use_cases": ["语音生成", "配音", "TTS"],
    "hf_url": "",
    "notes": "极速语音生成模型，MAI系列"
}

mai_image = {
    "id": "mai-image-2",
    "name": "MAI-Image-2",
    "developer": "Microsoft",
    "category": "image_generation",
    "release_date": "2026-04-02",
    "license": "proprietary",
    "pricing": "",
    "highlights": ["高质量图像生成", "Microsoft MAI系列"],
    "use_cases": ["图像生成", "艺术创作"],
    "hf_url": "",
    "notes": "Microsoft MAI图像生成模型，MAI系列"
}

# Add all new models (dedup by id)
all_new = gemma4_models + [glm51, gpt54, mai_transcribe, mai_voice, mai_image]
added = []
for m in all_new:
    if m['id'] not in existing_ids:
        models.append(m)
        added.append(m['name'])

# Update metadata
import datetime
data['_last_updated'] = str(datetime.date.today())
data['_updated_by'] = 'SOTA Radar Cron (自动调研)'

with open('docs/_data/models.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(added)} new models:")
for name in added:
    print(f"  + {name}")
print(f"Total models now: {len(models)}")
