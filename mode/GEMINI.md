# GEMINI Shim

本文件是 Gemini 兼容 shim，不自立规则，不承担项目日志、项目指南或状态快照职责。

## 标准恢复顺序

下游仓库应把这些路径替换为自己的 repo-local actual path：

1. `AGENTS.md`
2. `docs/status/current_committed_plan.md`
3. `docs/current_state.v2.md`
4. `docs/status/INDEX.md`
5. `docs/status/current_task_handoff.md`
6. 当前 task 若仍需 authority / report，再按 `INDEX` 指针继续
7. 只有在需要模式路由、wake / anti-stall 或升级机制时，才补读 `docs/agent_system/execution_routing.md`

正式规则与模板入口在：

- `mode/AGENTS.refactor.md`
- `mode/agent_system/execution_routing_template.md`
- `mode/status/current_committed_plan_template.md`
- `mode/current_state.v2.md`
- `mode/agent_system/status_index_template.md`
- `mode/agent_system/current_task_handoff_template.md`
- `mode/agent_system/agent_architecture_issue_ledger_template.md`（按需；不是默认恢复入口）

## 不要做的事

- 不要把本文件当任务日志追加面。
- 不要绕过标准恢复顺序，直接凭旧日志恢复上下文。
- 不要让 rolling worklog / legacy log 覆写 `current_committed_plan`、`current_state` 或 `current_task_handoff`。

repo-local actual path wins；下游仓库应替换成自己的实际路径。
