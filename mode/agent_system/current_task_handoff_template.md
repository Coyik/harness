# Current Task Handoff Template

这个文件承载“当前默认 task 的持久状态”。
它只负责 task state，不负责 routing / wake / anti-stall / approved-step 治理。
它的目标不是替代报告，而是让下一位 agent 在 clean-context 下知道：

- 当前 task 是什么
- 现在处于什么状态
- 已经做到哪一步
- 当前卡在哪
- 最近一条有效证据是什么

## 推荐结构

```markdown
# Current Task Handoff

更新时间：`YYYY-MM-DD HH:MM TZ`

## 1. Task Identity

- task_id：
- status：`planned | scheduled | executing | blocked | in_review | passed | accepted | cancelled | archived`
- lane：
- owner：
- reviewer：
- upstream objective / spec：

## 2. Why This Task Exists

- 当前 task 要解决的问题：
- 它属于哪个更大的 lane / phase：
- 若本 task 完成，对主线意味着什么：

## 3. Objective Snapshot

- 当前 task 目标：
- done_when：
- out_of_scope：

## 4. Current Status

- current_checkpoint：
- completed_since_last_update：
- active_blocker：
- open_questions：

## 5. Proof Snapshot

- latest_verification：
- landed_artifacts：
- latest_report_or_artifact：

## 6. Next Status Transition

- next_expected_status：
- transition_condition：
- escalated_to：
```

## 状态定义

- `executing`
  - 当前 task 仍在推进
- `blocked`
  - 当前 task 无法继续，且需要补证据或升级
- `in_review`
  - 实现或调查已完成，等待 reviewer / planner 判定
- `passed`
  - task 自身 `done_when` 已满足，但项目级 blocker 仍可能存在
- `accepted`
  - task 已被正式吸收到当前状态，不再作为默认续接面
- `archived`
  - task 只保留在 `status_index` / archive 中

## 什么时候更新

只在 task 状态真的变化时更新，例如：

- task 开始执行
- task 进入返修
- task blocker 变化
- checkpoint 前进
- task 通过 per-task review
- task 被 acceptance
- task 被新 task 取代

## 不该放进来什么

- 项目级长期规则
- 默认恢复顺序
- wake / anti-stall / escalation runbook
- 当前批准执行步或 `do_not_do_now`
- 完整周报
- 全量命令输出
- 与当前 task 无关的背景历史
- 长篇 why-not 分析

## 重要提醒

- `passed` 不等于项目已经 unblock。
- 一个仓库同一时刻应只有一个默认 `current_task_handoff`。
- 若当前 handoff 已 `passed` 且没有新 task，应在 `status_index` 明确写出“当前无新 active task”。
- `execution_routing` 承担长期恢复顺序与 anti-stall；`current_committed_plan` 承担当前批准执行步；不要把它们写回本文件。
