# Blueprint Runtime Alignment Freeze

更新时间：`2026-04-18 UTC`

## 1. 这份冻结说明记录什么

本文件冻结本轮从 `VLM_Bench`、`CGen`、`Cangjie` 三个项目实例回灌到 `harness` 蓝本的协作层结论。
它不是研究长文，也不是迁移 checklist；它只回答：

- 哪些蓝本规则已经被三项目实战验证
- 蓝本本轮到底改了什么
- 之后新项目应该默认继承什么行为

## 2. 本轮冻结结论

### 2.1 默认恢复链

蓝本默认恢复顺序冻结为：

`AGENTS.md -> docs/status/current_committed_plan.md -> docs/current_state.v2.md -> docs/status/INDEX.md -> docs/status/current_task_handoff.md`

不再采用 `handoff-first`、`current-phase-first`、`README-first` 或 rolling worklog first 的默认顺序。

### 2.2 Truth Surface 分工

本轮冻结后的分工是：

- `current_committed_plan`
  - 收口当前唯一已批准执行步，不被 report / handoff 反向改写
- `status_index`
  - 只负责导航当前默认 task surface、`latest_report`、`raw_log_root` 与 path-scoped resume
- `current_state`
  - 收口 repo 级 `active lane`、blocker、allowed moves、promotion / live / mechanical-ready 边界
- `current_task_handoff`
  - 收口当前默认 task surface、checkpoint、task pointer / status
- README / rolling worklog / legacy `current-phase`
  - 只作旧背景对齐，不是默认 resume 首跳，也不单独授予新动作

### 2.3 协作模式边界

蓝本中的主协作模式现在冻结为：

- `Debate`
- `Reviewer + Planner / Executor`
- `Conductor`
- `单窗口执行`

同时冻结以下边界：

- `AGENT TEAM` 不是协作模式本身；它只是可挂接在当前主模式上的条件化能力
- `Reviewer + Planner / Executor` 是显式双窗口模式，不等于“用户一句话就全面并行”
- `Conductor` 负责任务编排、quality gate 与 clean-context 续接，不自动升级为多人并行
- 只有 owner、write set 与 verification surface 都能拆清时，才允许附加 `AGENT TEAM`

### 2.4 legacy / explain surface 语义

若仓库保留 `README`、rolling worklog、legacy `current-phase` 等历史 / 解释页面：

- 页面顶部必须先声明 `resume_surface=false` 或等价降级语义
- 必须显式指向 live truth surfaces
- 不得继续暴露未加限定的 live header，如 `status: active`、`focus`、`tactical_objective`、`current_entry`

### 2.5 `passed` handoff 的语义

若当前 `current_task_handoff` 已 `passed` 且下一切片尚未冻结：

- 它应被理解为 `latest landed checkpoint / default task surface`
- `status_index` 必须明确写出“当前无新 active task”
- 不允许继续把旧 handoff 伪装成 active executing task

### 2.6 Prompt 与窗口装配顺序

蓝本中的 `planner_reviewer`、`executor`、`conductor` prompt，以及 `agent_system/README.md` 推荐装配顺序，都必须与上面的默认恢复链一致。

任何新项目若还保留：

- `handoff-first`
- `current-phase-first`
- `README-first`
- 旧 README / runbook 抢入口

都只能算迁移中间态，不能写成 blueprint 已完整落地。

## 3. Git 宪法更新

本轮同步冻结了更细的 Git 规则：

- 查询类 Git 命令可直接执行
- 本地 `git commit` 可直接执行，且鼓励按有意义的最小边界做小步 snapshot
- 以下 Git 操作统一按高危处理，仍必须人工复核：
  - `git push`
  - `git pull`
  - `git merge`
  - `git rebase`
  - `git checkout`
  - `git restore`
  - `git reset`
  - `git clean`
  - 任何改写历史、回退、切分支、远程同步动作
- 对上述高危 Git 动作，代理必须先把 `下面要进行高危破坏性操作，请人工确认` 单独成行说三遍，再说明详情与风险
- 上述高危 Git 动作继续要求用户明确同意两次后才能执行

这意味着蓝本现在支持“高频本地快照提交”这类更实用的协作模式，但没有放松危险 Git 操作的人工闸门，反而把高危动作的提示与双确认流程写得更硬。

## 4. 本轮改动落点

本轮冻结对应的蓝本承载面是：

- `mode/AGENTS.refactor.md`
- `mode/agent_system/README.md`
- `mode/agent_system/execution_routing_template.md`
- `mode/agent_system/current_state_template.md`
- `mode/agent_system/status_index_template.md`
- `mode/agent_system/current_task_handoff_template.md`
- `mode/agent_system/blueprint_migration_mapping.md`
- `mode/agent_system/migration_checklist.md`
- `mode/agent_system/prompts/planner_reviewer.md`
- `mode/agent_system/prompts/executor.md`
- `mode/agent_system/prompts/conductor.md`

## 5. 证据基础

本轮冻结基于以下已完成实例验证：

- `VLM_Bench`
  - 协作层作为首个重构目标完成验证，并已具备 `AGENTS + current_committed_plan + current_state + INDEX + current_task_handoff` 的稳定恢复链
- `CGen`
  - 已验证 rolling worklog `claude.md` 可以降级为历史面，不再与 live truth 竞争入口
- `Cangjie`
  - 冷启动 blind-resume 压测通过，验证新上下文不会再把 `passed checkpoint` 误判成 active executing task，也不会把 legacy `current-phase` 抬回默认 authority
- `harness`
  - 蓝本自身已补齐主骨架、execution routing template、prompt、mapping、checklist 的同构约束与测试锁定

## 6. 非目标

这份冻结说明不负责：

- 回写三项目实例的业务状态
- 代替 `blueprint_migration_mapping.md`
- 代替 `migration_checklist.md`
- 给未来项目自动授权危险 Git 操作

## 7. 后续默认动作

若未来再新开项目仓：

1. 先用本蓝本生成 `AGENTS/current_state/status_index/current_task_handoff/prompt` 层
2. 默认采用 `current_committed_plan -> current_state -> INDEX -> current_task_handoff` 的恢复链
3. 默认把 `README`、rolling worklog 与 legacy 页面视为 explain/history surfaces，而不是 live truth
4. 若用户没有显式开启本地 snapshot commit standing authorization，就不要擅自做 `git commit`
5. 若命中危险 Git 操作，继续走人工复核
