# AI 产品研发团队 · 工作规范

## 团队架构

```
@pm（项目经理）
 └── @coordinator（协调员）
      ├── @researcher（调研员）
      ├── @reviewer（质检员）
      ├── @archiver（归档员）
      ├── @self-review（自审员）
      └── @designer/@engineer（设计 & 实现）
```

## 信息源优先级

| 优先级 | 来源 | 用途 |
|--------|------|------|
| T0（必须） | HuggingFace 官方页 + ModelScope 官方页 | 参数量/许可证/模态/链接 |
| T1（优先） | 官方 GitHub / 官方博客 | 发布日期/版本/SOTA声明 |
| T2（参考） | arXiv / 官方 Leaderboard | Benchmark 数据 |
| 禁止 | 无来源标注的信息 | 任何关键字段 |

## 调研纪律

1. 数据优先，结论滞后
2. 日期精确到日，来源必须可查
3. SOTA 声明双人背书，无证据不上线
4. 每字段写完五项检查
5. 链接必须实测可访问

## 知识库结构

详见 `knowledge/` 目录
