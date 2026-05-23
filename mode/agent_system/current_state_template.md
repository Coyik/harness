# Current State Template

这个文件承载“项目级当前快照”。
它回答的是“项目现在在哪、唯一主线是什么、哪些动作现在允许”，而不是“这个 task 已返工几轮”。

## 推荐结构

```markdown
# Current State

更新时间：`YYYY-MM-DD`

## 0. Alignment Rules

- 默认恢复顺序：`AGENTS.md -> docs/status/current_committed_plan.md -> docs/current_state.v2.md -> docs/status/INDEX.md -> docs/status/current_task_handoff.md`
- `docs/status/current_committed_plan.md` 负责当前唯一已批准执行步；若本文件与其在 `current_step / do_not_do_now / exit_condition` 上不一致，按 `current_committed_plan` 收口，并把本文件视为待同步快照。
- `docs/status/INDEX.md` 只负责导航；若 `INDEX` 与 `current_task_handoff` 的默认 task pointer / status 不一致，按 `current_task_handoff` 收口。
- 若 `current_task_handoff` 在 `active lane`、blocker、allowed moves、promotion / live / mechanical-ready 身份上比本文件更激进或更宽，按本文件收口。
- `docs/agent_system/execution_routing.md` 只在需要模式路由、wake / anti-stall 或升级机制时补读；不得反向改写本文件。
- rolling worklog / legacy `current-phase` 只作旧背景对齐，不单独覆写当前项目态。

## 1. Headline

- 当前阶段：
- 唯一 active lane：
- 当前 blocker：
- 本周唯一主线目标：

## 2. What Is Active Now

- 当前唯一建议推进的工作：
- 当前 authoritative frozen surfaces：
  - `specs/...`
  - `docs/reports/...`
  - `artifacts/...`
- 当前 authoritative continuation-lane surfaces：
  - `specs/...`
  - `docs/reports/...`
  - `artifacts/...`
- 当前 rolling worklog / legacy history：
  - `claude.md` / `.claude/status/current-phase.md`（只在需要旧背景时读取）

## 3. Allowed Moves

- 当前允许动作 1：
- 当前允许动作 2：
- 当前允许动作 3：

## 4. Explicit Non-Goals

- 当前明确禁止动作 1：
- 当前明确禁止动作 2：
- 当前不应重开的旧方向：

## 5. Pending Decisions

- 需要用户 / PM 最终拍板的点：
- 当前仍缺的关键证据：
- 若 blocker 解除，下一步应切到：

## 6. Evidence Index

- 项目热区 SSOT：
- 状态索引 / 续接入口：
- 当前 task 交接面：
- 长历史 / 滚动工作日志：
- 最近一次 authoritative report：
- 当前 canonical artifact / dashboard：
```

## 使用原则

- 只写项目级当前快照
- 优先写“现在是什么”，而不是“过去发生了什么”
- 若需要解释为什么形成今天的状态，链接到 `docs/reports/*` 或 archive

## 什么时候更新

只在快照真的变化时更新，例如：

- 当前阶段变化
- 唯一 active lane 变化
- 当前 blocker 变化
- 当前允许动作变化
- 一个阶段正式收口并进入下一个阶段

## 不该放进来什么

- per-task 返工过程
- 长 artifact 路径洪水
- 运行时 exact flags / exact counts
- 长 why-not 分析
- 全量历史日志
- “今天这个 agent 干了什么”的流水账

## 容易混淆的相邻承载面

- `current_state`
  - 项目级当前快照
- `status_index`
  - 默认恢复导航与默认 task surface 指针
- `current_committed_plan`
  - 当前唯一已批准执行步
- `task_handoff`
  - 当前 task 的持续状态
- `window_init`
  - 本次开窗的动态变量
- `docs/reports/*`
  - 详细分析和证据
