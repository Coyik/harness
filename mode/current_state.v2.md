# Current State v2

更新时间：`YYYY-MM-DD`

本文件是蓝本仓库的项目态占位面。
下游新项目必须把它实例化为该仓库自己的 `docs/current_state.v2.md`，不得保留其它项目的 active lane、blocker、allowed moves 或 artifact 路径。

## 0. Alignment Rules

- 默认恢复顺序：`AGENTS.md -> docs/status/current_committed_plan.md -> docs/current_state.v2.md -> docs/status/INDEX.md -> docs/status/current_task_handoff.md`
- `current_committed_plan` 收口当前唯一已批准执行步。
- 本文件收口项目级 `active lane / blocker / allowed moves / promotion`。
- `status_index` 只负责导航。
- `current_task_handoff` 只负责当前 task 状态；若它比本文件更激进或更宽，按本文件收口。
- `execution_routing` 只在需要模式路由、wake / anti-stall 或升级机制时补读。

## 1. Headline

- 当前阶段：
- 唯一 active lane：
- 当前 blocker：
- 当前唯一主线目标：

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
  - 只在需要旧背景时读取；不是默认恢复入口

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

- 项目热区入口：`AGENTS.md`
- 当前批准计划：`docs/status/current_committed_plan.md`
- 状态索引 / 续接入口：`docs/status/INDEX.md`
- 当前 task 交接面：`docs/status/current_task_handoff.md`
- 最近一次 authoritative report：
- 当前 canonical artifact / dashboard：

## 更新规则

只有当“项目级当前快照”发生变化时才更新本文件。
不要在这里记录 per-task 返工过程、长 artifact 洪水、完整命令输出或其它项目的历史真值。
