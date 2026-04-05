# Auto Research 调研报告：Skill 自我进化落地方案

> **调研日期**：2026-04-05
> **调研目标**：Karpathy Auto Research 能否应用于 SOTA Greedy Research Skill 自我进化
> **结论**：可以落地，有三条可行路径，最简方案本周可跑通

---

## 一、Karpathy Auto Research 核心原理

**一句话总结**：给 AI agent 一个可量化的反馈指标 + 一个可以修改的代码/策略文件，让它围绕这个指标不断循环改进。

**原始架构**（用于 ML 训练）：
```
Agent 读取 training_code.py
    ↓
修改代码（改变超参/架构/数据策略）
    ↓
运行 5 分钟训练 → 获得 eval_loss
    ↓
eval_loss 下降 → 保留改动
eval_loss 上升 → 撤销改动
    ↓
循环 → 直到 eval_loss 收敛
```

**关键前提**：必须有**机械可测的指标**（eval_loss、Benchmark 分数、拦截率），否则无法判断"改进了还是改差了"。

---

## 二、我们的痛点：Skill 进化缺少什么

| Karpathy Auto Research 要求 | 我们的现状 | 差距 |
|---------------------------|-----------|------|
| 可量化反馈指标 | 质检拦截率/P0拒绝次数 | ✅ 已有 |
| 可修改的策略文件 | SKILL.md | ✅ 已有 |
| 执行→反馈→改进的闭环 | 无自动闭环，靠手动 | ❌ 缺失 |
| 自动判断"改进了还是改差了" | 无自动判断 | ❌ 缺失 |

**结论**：我们缺少的是"闭环机制"，不是技术。

---

## 三、三条落地路径

### 路径 A：每日自审 Cron（最简，**本周可跑通**）

原理：参考 "Nightly Self-Improvement Cron" 模式，在每天晚间 cron 后自动触发。

```
每日 cron 完成任务
    ↓
Skill 自审子智能体启动
    ↓
读取本次 cron 执行日志（git commit 历史 + 飞书通报记录）
识别本次执行中的"拦截案例"和"失误"
    ↓
分析 SKILL.md 现有内容
找出：哪条规则没有阻止本次失误？
    ↓
更新 SKILL.md（追加：本次教训）
git commit + push
    ↓
飞书通报："Skill 自审完成，本周更新 X 条"
```

**优点**：实现简单，本周可上线
**缺点**：被动进化（只在出问题时才更新）

---

### 路径 B：量化驱动 Auto-Evolve（中期，Karpathy 模式原版移植）

原理：定义可直接量化的指标，建立自动化评估循环。

**指标定义**：

| 指标 | 量化方式 | 目标 |
|------|---------|------|
| 调研报告通过率 | 每次提交 → 一次通过的比例 | 60% → 90% |
| P0 拦截率 | P0 拒绝数 / 总提交数 | 逐月下降 |
| 自检通过率 | 自检不通过→打回的比例 | 80% → 95% |
| 文档同步准确率 | 数字不一致次数 / 总更新次数 | 0% |

**Auto-Evolve 循环**：
```
每个 cron 周期结束后
    ↓
量化本次执行的关键指标
    ↓
指标下降（变差）？
  → 读取 SKILL.md
  → 分析是哪个环节导致
  → 提出 1～3 条具体修改建议
  → 更新 SKILL.md 对应章节
  → 用新的 SKILL 跑下一轮验证
    ↓
指标上升（变好）？
  → 记录"有效改动"，强化对应规则
```

**优点**：真正实现 Auto Research 精神
**缺点**：指标定义需要磨合，上线需要 2 周

---

### 路径 C：反馈驱动 Skill 进化（长期，最接近 Karpathy 原版）

原理：让 agent 在每次执行后，主动写下"本次哪里做得不好 + 为什么 + 下次怎么改"，并将这些反思积累起来形成进化。

```
每次 cron 执行后
    ↓
子智能体生成"执行反思报告"：
  - 本次调研 X 个模型，质检拦截了 Y 个
  - 拦截原因分类：SOTA无证据 / 日期模糊 / 许可证未核实
  - 调研员犯了哪类错误？
  - SKILL.md 哪条规则没有阻止这个问题？
    ↓
反思报告存入 docs/_evolution/YYYY-MM.json
    ↓
每周聚合：
  - 本周最高频失误类型
  - 最高频失误 → 对应的 SKILL.md 章节
  - 提出修改措辞/新增规则/删除无效规则
    ↓
更新 SKILL.md → 提交 git → 通知调研团队
```

**优点**：积累式进化，长期越来越精准
**缺点**：需要维护反思数据库，复杂度最高

---

## 四、最优推荐：路径 A + 路径 B 混合

**立即上线（路径 A）**：
- 建立每日 Skill 自审 cron
- 每次 cron 后自动检查 SKILL.md 是否需要更新
- 输出简短的"Skill 自审报告"

**3 周后升级（路径 B）**：
- 在路径 A 的数据积累基础上，定义量化指标
- 建立指标追踪表
- 让进化决策有数据支撑

---

## 五、落地计划

### 第 1 步：建立 Skill 自审 Skill（路径 A）

新建文件：
- `skills/skill-self-review/SKILL.md` — 自审 Skill
- `docs/_evolution/` — 进化记录目录

自审 Skill 每次执行做的事情：
1. 读取本次 cron 的 git commit 历史
2. 读取飞书通报记录（如果有）
3. 识别"本次出现的问题"
4. 对照 SKILL.md，输出"需要更新的条款"
5. 更新 SKILL.md 并 commit

### 第 2 步：建立每日 Skill 自审 Cron

在每日晚间 cron 后自动触发（或合并到晚间 cron 的最后一步）。

### 第 3 步：积累数据，定义指标（路径 B）

建立 `docs/_evolution/metrics.json`：
```json
{
  "date": "2026-04-12",
  "period": "week1",
  "total_submissions": 8,
  "p0_rejections": 3,
  "p1_issues": 2,
  "pass_rate": "62.5%",
  "top_failure_type": "SOTA无Benchmark证据",
  "skill_updates_made": 1
}
```

### 第 4 步：建立自动进化判断

当连续 2 周"同一失误类型"出现 ≥3 次 → 自动触发 SKILL.md 对应章节更新。

---

## 六、可参考的开源项目

| 项目 | 适用性 | 链接 |
|------|--------|------|
| karpathy/autoresearch | 核心原理参考 | github.com/karpathy/autoresearch |
| MaximeRobeyns/self_improving_coding_agent | Skill 自我改进模式 | github.com/MaximeRobeyns/... |
| gianfrancopiana/openclaw-autoresearch | OpenClaw+AutoResearch | github.com/gianfrancopiana/openclaw-autoresearch |
| SE-Agent | 轨迹级自我进化 | github.com/JARVIS-Xs/SE-Agent |

---

## 七、结论

**可以落地。** Karpathy Auto Research 的核心不是高深技术，而是一个设计理念：

> **"让 agent 围绕可量化的目标，通过执行→反馈→修改的循环，不断逼近目标"**

我们可以在 SOTA Greedy Research Skill 上应用同样的模式：
- 可量化指标：质检拦截率（P0 拒绝次数 / 总提交数）
- 可修改的策略文件：SKILL.md
- 闭环：cron → 自审 → 更新 SKILL → 下一轮验证

**建议本周先跑通路径 A**，用最简单的方式把"执行→反馈→改进"的循环建立起来，数据积累充分后再升级路径 B。
