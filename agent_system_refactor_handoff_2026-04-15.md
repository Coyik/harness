# Agent System Refactor Handoff

更新时间：`2026-04-16`
当前状态：`已完成三项目 .v2 实填与新版 AGENTS.md 替换；旧版已备份；当前进入后续日常维护阶段`

## 1. 本轮结论

围绕以下三个项目的新 agent system 重构，本轮已经完成从“蓝本 + 实填”到“正式替换旧版 `AGENTS.md`”的收口：

- `/volume/wzhang/cky-workspace/my_projects/VLM_Bench`
- `/volume/wzhang/cky-workspace/my_projects/CGen`
- `/volume/wzhang/cky-workspace/my_projects/Cangjie`

当前默认入口已经切换为：

- `AGENTS.md`：入口宪法、协作骨架、热区索引
- `docs/current_state.v2.md`：项目级当前快照
- `docs/runtime_contract.v2.md`：运行合同
- `docs/domain_review_rubric.v2.md`：仓库专有词义与 reviewer gate
- `docs/status/current_task_handoff.md`：当前任务持续态

## 2. 本轮实际修改

### 2.1 三个项目都已完成旧版备份与新版替换

每个项目都已执行：

- 备份旧版 `AGENTS.md` 到 `AGENTS.md.bak.20260416.before-refactor`
- 将补齐后的 `AGENTS.refactor.md` 覆盖为正式 `AGENTS.md`

当前备份文件如下：

- `/volume/wzhang/cky-workspace/my_projects/VLM_Bench/AGENTS.md.bak.20260416.before-refactor`
- `/volume/wzhang/cky-workspace/my_projects/CGen/AGENTS.md.bak.20260416.before-refactor`
- `/volume/wzhang/cky-workspace/my_projects/Cangjie/AGENTS.md.bak.20260416.before-refactor`

### 2.2 新版 `AGENTS` 入口已补成“可直接落盘”的正式版

这轮没有直接把原始蓝本生拷成正式入口，而是先补了三类最关键的正式入口信息，再替换：

1. 标题已从纯蓝本口径改为正式 `AGENTS` 宪法口径
2. `Session Header` 已改成各项目当前真实状态，而不是“应该如何填写”的模板说明
3. 热区入口已改成“当前热区索引”，不再保留空的最近 `20` 条日志模板

因此，新的 `AGENTS.md` 现在更像稳定入口，而不是未实填的骨架文件。

### 2.3 `Cangjie` 在替换前做了最小同步

替换前发现 `Cangjie` 新体系内部存在状态回退：

- 旧 `AGENTS.md` 已经写到 `Phase07 P1-14`
- 但 `docs/current_state.v2.md`、`docs/runtime_contract.v2.md`、`docs/status/current_task_handoff.md` 还停在 `P1-8`

为避免替换后新入口反而把状态降回旧事实，这轮已先做最小同步：

- `docs/current_state.v2.md` 已同步到 `P1-14 alternating-reopen bounded stability`
- `docs/runtime_contract.v2.md` 已同步到 `P1-14` 对应 consume surface 与 `TOTAL: 14 / PASSED: 14 / FAILED: 0`
- `docs/status/current_task_handoff.md` 已同步到 `P1-14` landed 任务态

## 3. 当前真实状态

### 3.1 CGen

- 当前 active lane 仍是 `520-task evidence consolidation / provider-extension supplement closure`
- 当前 task 仍未收口；`teacherB supplement` 还不是完成态
- 新入口已经明确要求：只允许在不改 `520` 题协议、评分公式和 toolchain / API 合同的前提下继续补齐 live supplement 与结果汇总

### 3.2 VLM_Bench

- 当前 active lane 仍是 `Calibration Track v1` 的 `T2 / Phase A`
- canonical raw truth 仍是 `raw_release_ready=false + closure_state=selected_only_gap_open`
- `Wave 0` preflight 仍是 `reviewer_hold + not_cleared_for_control_based_scale_out`
- 新入口已经明确要求：只沿 `consumer_handoff / output_root` 和统一 `glm + model_revision` gate 继续推进，不重开 raw/source/prompt 主线

### 3.3 Cangjie

- 当前正式 checkpoint 仍是 `P22 / 311/311 live passed`
- `direct P23 mechanical-ready = No` 仍未改写
- 当前 continuation lane 是 `Phase07 Telegram UI Incubation`
- 当前 Telegram consume entry 已同步为 `P1-14 alternating-reopen bounded stability`
- 当前 lane 仍是 `exploratory-only`，不得误写成 promoted / live / mechanical-ready

## 4. 当前设计判断

### 4.1 已确认有效的承载分层

这套分层现在已经不是试运行判断，而是当前正式默认结构：

- `AGENTS.md` 只承载跨任务稳定规则、热区索引、当前入口判断
- `current_state.v2.md` 承载项目级快照
- `runtime_contract.v2.md` 承载运行合同
- `domain_review_rubric.v2.md` 承载仓库专有术语、promotion ladder 和 reviewer gate
- `current_task_handoff.md` 承载当前 task 的持续状态与 clean-context 接续面

### 4.2 原版 `AGENTS.md` 的强约束已经保留

原版高价值内容没有被简单删除，而是已经在新版体系中保留并重新分层，包括：

- 热区读取顺序
- 输出与证据纪律
- baseline / compare / preview / smoke 不得误写成正式放行
- reviewer / executor 的角色张力
- Git 宪法
- 长日志另存、热区只保留索引

## 5. 仍需记住的风险与注意事项

### 5.1 不要把“完成替换”误写成“后续不再需要同步”

当前替换动作已经完成，但以后如果项目主线继续变化，仍需要优先同步：

1. `docs/current_state.v2.md`
2. `docs/runtime_contract.v2.md`
3. `docs/domain_review_rubric.v2.md`
4. `docs/status/current_task_handoff.md`

只有这些下层文档口径稳定后，才需要视情况调整 `AGENTS.md` 的 `Session Header` 和热区索引。

### 5.2 `VLM_Bench` 的旧备份应视为敏感文件

旧版 `/volume/wzhang/cky-workspace/my_projects/VLM_Bench/AGENTS.md` 中存在明文 API key。

这轮按要求做了原样备份，因此：

- 备份文件保留了旧内容
- 后续处理该备份时应按敏感文件对待
- 新版正式 `AGENTS.md` 已不再沿用这类写法

### 5.3 `Cangjie` 已做最小同步，但不要据此外推更大范围重构已完成

这轮只同步了会影响正式入口判断的 `P1-14` 相关状态页与 handoff。
没有借此重写更多历史 report，也没有改写 `Phase07` 的边界判断。

## 6. 后续继续时的默认读取顺序

下一轮若继续维护这套系统，默认先读：

1. 目标项目的 `AGENTS.md`
2. `docs/current_state.v2.md`
3. `docs/runtime_contract.v2.md`
4. `docs/domain_review_rubric.v2.md`
5. `docs/status/current_task_handoff.md`

只有在这些入口文档不足以回答问题时，再继续下钻：

- `docs/reports/*`
- `specs/*`
- `artifacts/*`
- archive / 旧 handoff

## 7. 一句收口

这次 agent system 改造已经完成三个阶段：

1. 蓝本搭建
2. `.v2` 实填
3. 正式替换旧版 `AGENTS.md`

当前不再处于“是否替换”的讨论阶段，而是已经进入“按新入口体系继续维护项目状态”的阶段。
