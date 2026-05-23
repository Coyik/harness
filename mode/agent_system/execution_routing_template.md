# Execution Routing / Collaboration Modes Template

本模板承载长期执行路线、模式读取面、wake conditions 与 anti-stall routing。
它不是项目真值层，不覆写 `AGENTS.md`、`current_committed_plan`、`current_state` 或 `current_task_handoff`。
它也不是默认恢复入口；只有在需要协作模式边界、角色分工、wake conditions 或 anti-stall 时才继续读。

## 推荐结构

```markdown
# Execution Routing / Collaboration Modes

更新时间：`YYYY-MM-DD UTC`

本文件承载长期执行路线、模式读取面、wake conditions 与 anti-stall routing。
它不是项目真值层，不覆写 `AGENTS.md`、`current_committed_plan`、`current_state` 或 `current_task_handoff`。
它也不是默认恢复入口；只有在需要协作模式边界、角色分工、wake conditions 或 anti-stall 时才继续读。

## 1. Standard Resume Order

- 标准恢复顺序：`AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`
- 只有在需要模式路由、双窗口分工、wake conditions 或 anti-stall 时，才继续读本文件。
- 若本文件与 `current_task_handoff` 在当前 task pointer / status 上不一致，按 `current_task_handoff` 为准。
- 若本文件在 active lane / blocker / allowed moves 上比 `current_state` 更激进或更宽，按 `current_state` 收口。

## 2. Collaboration Mode Routing

| 模式 | 必须先读 | 默认动作 |
| --- | --- | --- |
| `单窗口执行模式` | `AGENTS -> current_committed_plan -> current_state -> INDEX -> current_task_handoff` | 单执行者直接推进当前主线 |
| `Reviewer + Planner / Executor` | `AGENTS -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`，再按角色补 `runtime_contract` / `domain_review_rubric` / prompts | `reviewer + planner` 负责判断主线，`executor` 负责实现与证据 |
| `Debate 模式` | `AGENTS -> current_committed_plan -> current_state -> INDEX`，必要时补 `current_task_handoff` 与 debate prompts | 先做问题收敛，不直接实现 |
| `Conductor 模式` | `AGENTS -> current_committed_plan -> current_state -> INDEX -> current_task_handoff -> runtime_contract` | 按 task 单元、quality gate、clean-context 续接推进 |

## 3. Mode Boundaries And AGENT TEAM Capability

- `AGENT TEAM` 不是协作模式本身；它只是可挂接在当前模式上的条件化能力。
- `Reviewer + Planner / Executor` 是默认显式双窗口模式，不等于自动并行 widening。
- `Debate` 默认不直接实现，除非用户明确 reroute。
- `Conductor` 负责任务编排、quality gate 与 clean-context 续接，不把用户一句话自动升格为全面并行。
- 只有 owner、write set 与 verification surface 都能拆清时，才允许附加 `AGENT TEAM`。

## 4. Current Long-Running Route

- current_route_stage：
- next_route_stage：
- blocked_branches_not_to_reopen：
- route_exit_condition：

## 5. Collaboration Wake Conditions

- wake `Reviewer + Planner / Executor` when：
- wake `Debate` when：
- wake `Conductor` when：
- attach `AGENT TEAM` only when：

## 6. Fallbacks

- 若 `INDEX` 未及时同步，仍按 `current_committed_plan` 与 `current_state` 收口，不直接从旧 `latest_report` 外推新动作。
- 若 `current_task_handoff` 只记录 landed checkpoint 而非 active task，不能把它自动升级成新的 executing task。
- 若多次出现同类路由失配、层级漂移或承载面缺口，把问题追加到 `agent_architecture_issue_ledger`；不要为了修一次偏差就把本文件扩写成第二套 `AGENTS`。
- 若工具面不支持真实双窗口，仍按对应角色顺序在同一代理内执行，不回退成无角色协作。
```

## 维护规则

- `execution_routing` 只在模式路由、wake / anti-stall、冲突裁决或 escalation 规则变化时更新。
- 默认恢复首链始终是 `AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`。
- 真实仓库里始终是 repo-local actual path wins；在这个模板仓库里，示例路径以 `mode/...` 为准。
- 若 `current_state` 与本文件冲突，按 `current_state` 收口。
- 若 `current_committed_plan` 与本文件冲突，按 `current_committed_plan` 收口。
- `agent_architecture_issue_ledger` 只记录架构反馈和 redesign trigger，不反向改写本文件的当前路线。
- 不要把本文件抬升成第二份 `AGENTS` 或默认 resume surface。

## 不该放进来什么

- 当前 task 的逐步进展
- 六字段批准步正文
- 完整验证日志
- 报告正文
- 第二套 `AGENTS` 宪法
