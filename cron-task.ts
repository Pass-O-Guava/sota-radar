/**
 * SOTA Radar 定时调研触发器
 * 策略：触发后立即退出（< 10秒），agent 在后台 detached 进程运行
 * 避免 cron 外层超时（10分钟限制）杀死正在运行的 agent
 */
import { spawn } from 'child_process'

const TASK = `
## 角色
你是一个高效的调研协调员。立即执行以下步骤：

### Step 1: 扫描 HuggingFace/ModelScope 最新模型
扫描以下发布方最近1个月的新模型（国内：DeepSeek/智谱AI/Moonshot/阿里巴巴/MiniMax；海外：OpenAI/Anthropic/Google/Meta/xAI/Mistral/NVIDIA），提取名称/发布方/参数量/模态/许可证/发布日期/Benchmark。

### Step 2: 按 MEMORY.md 规范质检
对每条记录检查：信息源优先级/日期精确性/SOTA证据/Benchmark数据完整性。

### Step 3: 更新模型文件
将审核通过的模型写入 /workspace/sota-radar/models/ 每模型一个 markdown 文件。

### Step 4: Git 推送
git add + commit + push 到 main 分支，commit message 格式：「YYYY-MM-DD HH:MM 自动更新：新增X个模型」

### Step 5: 飞书通报
发送结果到飞书（token: cli_a91839c23978dcc7），格式：
「⚡ SOTA Radar 播报 | YYYY-MM-DD HH:MM
新增X个模型 | 拦截X个 | 总计X个
【新增】模型列表（名称 + 发布方）
【拦截】问题记录（模型 + 原因）」
`

// 启动前清理残留进程（防止连续失败）
import { execSync } from 'child_process'
try {
  execSync('pkill -f "openclaw invoke" 2>/dev/null; pkill -f "researcher.*agent" 2>/dev/null; true', { stdio: 'ignore' })
  console.log('[cleanup] 残留进程已清理')
} catch {}

async function main() { = `[${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}]`
  console.log(`${tag} SOTA Radar 定时任务触发（后台异步模式）...`)

  // 用 openclaw invoke 触发 research agent，detached 模式
  // 不等待结果，cron job 立即退出（< 10秒），agent 在后台继续跑
  const openclawBin = process.env.OPENCLAW_BIN || 'npx'

  const child = spawn(openclawBin, [
    'openclaw', 'invoke',
    '--agent', 'researcher',
    '--noninteractive',
  ], {
    stdio: 'inherit',
    detached: true,
    env: { ...process.env, OPENCLAW_TASK: TASK },
  })

  child.unref() // 确保父进程退出后子进程继续

  console.log(`${tag} Agent 已后台触发，cron job 立即返回（避免超时）`)
  process.exit(0) // 立即退出，不等待 agent
}

main().catch((err: Error) => {
  console.error('Cron trigger error:', err.message)
  process.exit(1)
})
