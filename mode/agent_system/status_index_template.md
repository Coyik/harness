# Status Index Template

这个文件承载“最近任务、报告、handoff、archive 与默认恢复入口的索引面”。
它的目标不是复述正文，而是让 agent 快速回答：

- 当前默认应该从哪个入口继续
- 当前已批准执行步在哪
- 最近哪些报告值得看
- 历史 handoff 和 archive 在哪里

## 推荐结构

```markdown
# Status Index

更新时间：`YYYY-MM-DD HH:MM TZ`

## 1. Resume Core

- `AGENTS.md`
  - 作用：入口宪法、导航面、热区索引
- 默认恢复顺序：`AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`
- 为什么当前默认从 `INDEX` 续接：
- `current_committed_plan`
  - 作用：当前唯一已批准执行步
- `current_state`
  - 作用：当前项目快照
- `current_task_handoff`
  - 作用：当前默认 task 的状态 / checkpoint / proof snapshot
- `execution_routing`
  - 作用：仅在需要模式路由、wake、anti-stall 或 escalation 时补读
- 若本文件与 `current_task_handoff` 在 task pointer / status 上不一致，按 `current_task_handoff` 为准；本文件只作为导航层处理。
- 若 `current_task_handoff` 与 `current_committed_plan` 在当前执行步上不一致，按 `current_committed_plan` 为准。
- 若 `current_committed_plan`、`current_task_handoff` 与 `current_state` 在 `active lane / blocker / allowed moves / promotion` 上冲突，按 `current_state` 为准。
- `execution_routing` 只补充模式路由 / wake / anti-stall，不进入默认恢复首链，也不反向改写 `current_committed_plan`、`current_state` 或 `current_task_handoff`。
- repo-local actual path wins；在模板仓库里，对应文件位于 `mode/...`。

## 2. Pointer Surfaces

- `current_committed_plan`：
  - 当前批准执行步与 `do_not_do_now`
- `latest_report`：
  - 当前 slice 最值得继续读的长文入口
- `raw_log_root`：
  - 当前 task 的原始验证证据根目录
- `execution_routing`：
  - 只在需要模式路由、wake / anti-stall、或 escalation 规则时读取
- `archive/index`：
  - 需要追旧背景时再读
- `agent_architecture_issue_ledger`：
  - 只在出现路由失配、层级漂移、承载面缺口或 redesign trigger 评估时读取
- `rolling_worklog` / `rolling_phase_log`：
  - 只在需要追最近工作记录或长历史时读取；不是默认 resume 首跳
- 如果本文件仍不足以回答“当前从哪续接”：
  - 先读 `current_committed_plan` 确认当前批准执行步与 `do_not_do_now`
  - 再读 `current_state` 确认 repo 级 active lane / blocker / allowed moves
  - 再读 `current_task_handoff` 确认当前默认 task surface、checkpoint 与 proof snapshot
  - 只有在需要模式路由、wake / anti-stall 或 escalation 时，再补读 `execution_routing`
  - 仍缺旧背景时，再回跳 rolling worklog / archive

## 3. Path-Scoped Resume

- `specs/...` / `subdir/AGENTS.md`：
  - 仅在命中该子目录或该 continuation lane 时读取

## 4. Current Lane And Default Task Surface

- `active_lane`：
- `active_executing_task`：`none yet; next bounded continuation slice not frozen`
- `approved_step_surface`：`current_committed_plan`
- `default_resume_surface`：`current_task_handoff`
- `supplemental_route_surface`：`execution_routing`
- `checkpoint_task_id`：
- `checkpoint_status`：
- `handoff`：`current_task_handoff`
- `latest_state`：

## 5. Status Utilities

- `weekly_status_template` / `report_template`：
  - 周报或阶段状态模板
```

## 维护规则

- `status_index` 是索引，不是长报告。
- 当前默认续接入口、默认恢复顺序、当前批准执行步所在文件或默认 task surface 改变时必须更新。
- 新 report / 新 decision / 新 archive 创建后应补一条索引。
- 若当前 `current_task_handoff` 已 `passed` 且下一切片尚未冻结，必须显式写出“当前无新 active task”，不要继续让旧 task 假装是 executing。
- 若 `current_committed_plan` 缺失，必须显式写出 `approved-step surface missing`。
- `execution_routing` 缺失本身不构成默认恢复链断裂；只有在需要模式路由 / wake / anti-stall 时才是阻塞。
- `agent_architecture_issue_ledger` 缺失不构成恢复链断裂；只有当同类架构问题反复出现时才需要补建。
- 建议只保留最近 `5-10` 个 task / report 指针，避免再次膨胀成第二份长文档。

## 不该放进来什么

- 大段正文
- 全量命令输出
- 项目级长期规则
- 与当前主线无关的冷门历史
