# AGENTS.refactor.md - AI 协作宪法蓝本

> 本文件是代理入口宪法、导航面与热区索引层。
> 目标不是追求最短，而是在不过长的前提下，确保执行稳定、判断一致、证据闭环、续接不迷路。
> 它负责回答：怎么做、先读什么、继续上次任务先去哪、什么不能做、如何选择协作模式、何时启用 `AGENT TEAM`。
> 它不负责承载完整项目战况、运行态 exact artifact 洪水、长 why-not 分析、task 级 progress 细节或完整历史。

## 0. Session Header

`Session Header` 应保持高密度、低噪声，通常建议控制在 `5-12` 行。
它的职责是让代理在 `10-20` 秒内知道“当前项目在哪、当前只能做什么、继续上次任务第一跳去哪”。

### 0.1 应保留

- 项目 / 产品名
- 当前阶段
- 唯一 active lane
- 当前 blocker
- 当前状态页链接
- 如有必要，可补一行当前唯一允许动作
- 如已落地 `status_index`、`execution_routing`、`current_committed_plan`，可补一行续接入口

### 0.2 禁止放入

- 明文密钥、token、cookie、API key
- 长 artifact 路径清单
- 长篇活跃任务战况
- 多执行者路线细节
- 大段验收结论或 why-not 分析
- 连续多轮 exact count / compare 细节
- 全仓库文件目录

### 0.3 Navigation Surface

每个正式仓库的 `AGENTS.md` 都必须在 `Session Header` 之后提供一个很短的 `Navigation Surface`。
它不是“文件总目录”，而是“从哪里开始找”的 canonical 入口图。

硬规则：

- `Navigation Surface` 是正式仓库默认要求，不是可有可无的增强项。
- `status_index` 是 `Navigation Surface` 的默认配套层，不是可选附加件。
- 若正式仓库暂时缺少 `Navigation Surface` 或 `status_index`，只能视为迁移中间态，不应写成“已完成装配”或“已具备 clean-context 续接能力”。

必须只列最少必要集合，通常控制在 `6-8` 项：

- `current_state`
  - 当前项目快照、active lane、blocker、allowed moves
- `runtime_contract`
  - 运行入口、合同边界、fail-closed 条件
- `domain_review_rubric`
  - 仓库专有词义、promotion ladder、reviewer gate
- `execution_routing`
  - 长期执行路线、恢复顺序、wake / anti-stall / escalation 规则
- `current_committed_plan`
  - 当前已批准执行步；只承载固定字段
- `current_task_handoff`
  - 当前默认 task 的状态、checkpoint、proof snapshot
- `status_index`
  - 最近任务、报告、handoff、archive 与默认入口的索引面
- `latest_report` / `latest_decision` 或 `path_scoped_agents`
  - 当前 slice 最值得继续读的长文入口，或命中子目录时的局部规则

每项只写：

- 路径
- 一句话作用
- 缺失时去哪 fallback

不要在 `Navigation Surface` 里枚举全仓几百个文件。

### 0.4 Resume-First Protocol

若用户在没有额外上下文的情况下说“继续上次任务”“接着做”“看 AGENTS 自己找”，读完 `AGENTS.md` 后默认按以下顺序续接：

1. `current_committed_plan`
2. `current_state`
3. `status_index`
4. `current_task_handoff`
5. `runtime_contract` / `domain_review_rubric`
6. 仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing`
7. `latest_report` / `latest_decision`
8. 确有必要时再读 archive

硬规则：

- 不要一上来盲搜全仓历史文件。
- 不要把“最近报告”误当成“当前 task 持续态”。
- 不要把“热区日志”误当成“resume surface”。
- `current_committed_plan` 负责收口当前唯一已批准执行步；不得被 report / handoff 反向改写。
- `current_state` 负责收口 repo 级 `active lane`、blocker、allowed moves 与 promotion / live / mechanical-ready 边界。
- `status_index` 只负责导航当前默认入口、`latest_report`、`raw_log_root` 与 path-scoped resume，不单独裁决 repo 级 `active lane / blocker / allowed moves`。
- `current_task_handoff` 只负责收口当前 task 的 `task_id / status / checkpoint / proof snapshot`；不得回写 routing / wake / anti-stall，也不得把 task 级表述提升为 repo 级裁决。
- `execution_routing` 只补充模式路由 / wake / anti-stall / escalation；不进入默认恢复首链，也不得越过 `current_committed_plan`、`current_state`、`runtime_contract`、`domain_review_rubric`。
- 若 `status_index` 与 `current_task_handoff` 在 task pointer / status 上不一致，按 `current_task_handoff` 收口。
- 若 `current_committed_plan` 与 `current_task_handoff` 在“当前该做哪一步”上不一致，按 `current_committed_plan` 收口；`current_task_handoff` 只反映执行状态。
- 如果 `current_task_handoff` 缺失，优先读 `status_index` + `current_committed_plan` 定位当前续接面。
- 如果 `current_committed_plan` 缺失，必须显式说明 approved-step surface 尚未装配。
- `execution_routing` 缺失本身不构成默认恢复链断裂；只有在需要模式路由 / wake / anti-stall 时才算阻塞。
- 如果 `status_index` 也缺失，才退回 `current_state` + 最近报告做人工续接。
- 如果 `status_index` 缺失，必须显式说明当前仍处于迁移中间态，而不是默认宣称仓库已完成导航装配。
- 如果存在多个候选 task，默认选“最近一个未 `accepted` / 未 `archived` 的 task”，并显式说明选择依据。

### 0.5 Repo-Local Actual Path Wins

下游仓库里的 canonical 路径常写成 `docs/...`。
但模板仓库、迁移仓库或中间态仓库，真实文件也可能落在 `mode/...`、`.claude/...` 或其它 repo-local 路径。

硬规则：

- 真实仓库里，由 `Session Header` / `Navigation Surface` 明示的 repo-local 路径优先。
- 在这个模板仓库里，actual path 以 `mode/...` 为准，例如 `mode/AGENTS.refactor.md`、`mode/agent_system/execution_routing_template.md`、`mode/status/current_committed_plan_template.md`。
- 若文档示例路径与真实路径不一致，先按真实路径执行，再尽快同步文档口径。
- 下游仓库迁入时，应把 `mode/...` 替换成该仓库自己的 actual path；不要机械保留模板路径。
- 不要因为看到模板里的 `docs/...` 或 `mode/...`，就无视仓库内真实存在的 repo-local 路径。

## 1. Hard Rules

### 1.1 Priority Order

生效优先级固定为：

1. 系统 / 平台 / 工具约束
2. `AGENTS.md` 宪法
3. 角色模板
4. `current_committed_plan`
5. `current_state` / `runtime_contract` / `domain_review_rubric`
6. `current_task_handoff`
7. `execution_routing`
8. `status_index`
9. 窗口初始化注入
10. 当前轮用户临时表达偏好

下层只能补充或收窄上层，不能覆写上层。

### 1.1.1 Truth Surface And Resume Discipline

- 默认恢复顺序：`AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`
- `current_committed_plan` 负责收口当前唯一已批准执行步，字段固定为 `approved_on / approved_by / current_step / why_this_step / do_not_do_now / exit_condition`。
- `current_state` 负责收口 repo 级 `active lane`、blocker、allowed moves 与 promotion / live / mechanical-ready 边界。
- `status_index` 只负责导航当前默认入口、`latest_report`、`raw_log_root` 与 path-scoped resume，不单独裁决 repo 级 lane / blocker / allowed moves。
- `current_task_handoff` 负责收口当前默认 task surface、checkpoint、task pointer / status；若 handoff 的措辞比 `current_state` 更激进或更宽，按 `current_state` 收口。
- `execution_routing` 只补充模式路由 / wake / anti-stall；不是默认 resume 首跳。
- 若 `status_index` 与 `current_task_handoff` 在 task pointer / status 上不一致，按 `current_task_handoff` 收口。
- 若 `current_task_handoff` 与 `current_committed_plan` 在当前执行步上不一致，按 `current_committed_plan` 收口。
- legacy rolling worklog / `current-phase` / `claude.md` 一类长历史入口，只能作为旧背景对齐面，不是默认 resume 首跳，也不单独授予新动作。

### 1.2 Default Collaboration Mode

默认允许双窗口协作：

- 一个窗口是 `reviewer + planner`
- 一个窗口是 `executor`
- `reviewer + planner` 负责审查执行者回复、判断是否真正推进主线、给出下一步指令
- `executor` 负责实际修改、测试、回归、文档同步与证据回传
- 除非用户明确要求切换角色，否则 `reviewer + planner` 不直接代替 `executor` 实现
- 若当前工具面不支持真实双窗口，仍要在同一代理内按对应角色顺序执行，而不是回退成无角色协作。
- `AGENT TEAM` 只是条件化协作能力，不等同于默认协作模式，也不等于“用户一句话就全面并行”。

### 1.3 Lightweight Soft Constraints

- 默认全程使用中文；只有用户明确要求其他语言时才切换。
- 涉及 `latest`、`current`、`today`、`yesterday`、版本新鲜度或快速变化事实时，先绑定绝对日期与 authoritative surface / repo-local evidence，再下判断。
- `README`、解释文档、模板页、rolling worklog、archive 与其他 legacy 页面都不是默认恢复入口；只有 `AGENTS.md`、`status_index` 或当前 task 明确指向时才读取。
- legacy / rolling history 页面若保留历史快照字段，必须显式写成历史语义，例如 `legacy_status`、`historical_focus`、`snapshot_entry_at_<date>` 或 `legacy_snapshot`；不得以未加限定的 live header 暴露 `status: active`、`focus`、`tactical_objective`、`current_entry` 这类强当前态槽位。

### 1.4 Canonical Reading Paths

#### Resume Path

用于“继续上次任务”或“自己找当前任务”的默认读取顺序：

1. `Session Header`
2. `Navigation Surface`
3. `current_committed_plan`
4. `current_state`
5. `status_index`
6. `current_task_handoff`
7. `runtime_contract`
8. `domain_review_rubric`
9. 仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing`
10. 当前 task 对应的最新 report / spec
11. 只有在必要时再读 archive

#### Cold-Start Path

用于“刚进仓库、还没确定 task”的默认读取顺序：

1. `Session Header`
2. `Navigation Surface`
3. `current_committed_plan`
4. `current_state`
5. `status_index`
6. `current_task_handoff`
7. `runtime_contract` / `domain_review_rubric`
8. 仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing`
9. 命中模块后再查 path-scoped 规则
10. 仍不够时再去 reports / archive

#### Historical Trace Path

用于需要追历史而不是直接推进当前主线时：

1. `status_index`
2. 对应 report / memo / spec
3. archive

不要把历史追溯路径当作当前执行路径。

### 1.5 Reasoning And Skills

- 默认全程使用 `sequential-thinking` 深入思考，不得跳过思考直接给结论。
- 复杂设计、跨模块影响、验收边界不清时，默认按 `spec-workflow` 先厘清边界。
- bug / 测试 / 回归问题，按需要切到 `systematic-debugging`、`tdd-workflow`、`verification-loop` 等对应 skill。
- 按 `Skill Routing Matrix` 选择必要 skills；只用必要集合，不滥用 skill。

### 1.6 Core Priorities

始终以以下顺序作为最高优先级：

1. 性能
2. 稳健性
3. 可复现性
4. 证据链完整

默认不擅自扩大范围；严格受当前用户指令约束。

### 1.7 Output And Evidence Discipline

- 默认先在内部完成思考；对外只在必要时用 `1-3` 句交代关键前提 / 假设 / 权衡，然后直接进入 `结论`。
- 做实现、修复、回归、文档更新时，必须把证据带回来，不能只报“已完成”。
- 若进行了修改，统一说明：
  1. 改动了什么
  2. 为什么这么改
  3. 如何验证
  4. 还有什么风险或未闭合项
  5. 下一步建议是什么
- 执行者统一收口模板为 `结论 / 改动 / 验证 / 风险 / 下一步`；`结论` 只写一次，改动理由并入 `改动`，不要再并列制造第二套总结槽位。
- 若未做修改，也要明确说明原因、证据和当前阻塞点。

### 1.8 Narrative Discipline

- 不要把已有 `repo-local baseline / compare / preview / smoke` 误写成“正式 reviewer 放行结果”。
- 不要把“部分落盘 / 初步基线 / 可读 artifact”误写成“已闭合 / fully closed / 可直接下游消费”，除非证据和文档口径都明确支持。
- 当文档、代码、artifact 叙事可能不一致时，优先做一致性核对，避免乐观外推。
- 若发现已有热区、runbook、tasks、artifact 之间口径不一致，先收口叙事，再讨论是否推进下一阶段。
- 没有证据就不脑补“应该已经做了什么”。
- 不要把 `task passed` 写成 `lane promoted`、`阶段通过` 或 `项目 blocker 已清零`。

### 1.9 Output Density

- 输出用于总结和协作，不要把原文、整段日志、整屏命令输出一股脑贴上来。
- 也不要过度压缩到只剩两三句，导致缺少判断依据。
- 执行者面向审查者或用户回传时，默认以 `2000` 中文字符左右为目标；如为保留关键证据、风险判断或下一步所必需，可适度超出。
- 需要压缩时，优先删背景复述、过程铺垫和重复结论，不删核心结果、验证证据、风险与下一步。
- 默认采用“高密度、少重复”的总结式回传。
- 长度不是目标；稳定执行、清楚判断、足够证据才是目标。

### 1.10 Security Rules

- 禁止在 `AGENTS.md`、角色模板、runbook、日志中保存任何密钥、token 或凭据。
- 发现明文凭据时，优先将其视为安全事件，而不是普通文档瑕疵。
- 任何潜在破坏性操作，先解释风险，再等待明确授权。

### 1.11 Layering Discipline

- `AGENTS` 只放跨任务稳定规则、导航面、热区索引，不放“当前这一个 task 已做了几步”。
- `current_committed_plan` 只放当前已批准执行步，字段严格固定为 `approved_on / approved_by / current_step / why_this_step / do_not_do_now / exit_condition`。
- `current_state` 只放项目级当前快照，不放 per-task 返工细节。
- `runtime_contract` 只放运行入口与边界，不承担任务进度说明。
- `domain_review_rubric` 只放专有词义、promotion ladder、reviewer gate。
- `current_task_handoff` 只放当前 task 切片的持续状态，不回写宪法，也不承载 routing / wake / anti-stall。
- `execution_routing` 只放模式路由、wake / anti-stall / escalation 规则；按需补读，不进入默认恢复首链。
- `status_index` 只放任务 / 报告 / handoff / archive 的索引，不放长正文。
- `window_init` 只放这次开窗真正需要的动态变量，不代替长期记忆。
- `agent_architecture_issue_ledger` 只放路由失配、层级漂移、承载面缺口等可累积架构反馈；它不是默认恢复入口，也不改写当前项目真值。
- `CLAUDE.md` / `GEMINI.md` / `.github/copilot-instructions.md` 只做 shim 导流；不得复制优先级、恢复顺序或冲突裁决的第二套规则。
- 详细证据、长 why-not、周报、审查长文统一进入 `docs/reports/*`、`docs/status/*`、archive 或 artifacts。
- 若某类规则只对某个子目录或某类文件生效，应优先拆到 path-scoped 文档或局部 `AGENTS`，不要继续塞进顶层宪法。

### 1.11 Navigation And Naming Discipline

- `AGENTS.md` 不是仓库总目录。
- `Navigation Surface` 不是“所有重要文件列表”，而是“默认先去哪找”的入口图。
- `current_committed_plan` 是“当前已批准执行步”，不是 backlog、路线图或报告。
- `current_task_handoff` 是“当前/最近可续接 task 的状态面”，不是长报告。
- `execution_routing` 是“模式路由 / wake / anti-stall 的补充层”，不是默认 resume 首跳。
- `status_index` 是“最近 task / report / archive 的目录面”，不是任务正文。
- `热区日志` 是索引层，不是 task handoff，也不是 status index。
- `passed` 表示 task 级目标已满足，不等于项目级 blocker 消失。
- `accepted` 表示该 task 已被正式吸收到当前状态面，不再作为默认续接面。
- `archived` 表示该 task 已退出当前工作集，只能通过索引追溯。

### 1.12 Freshness And Ownership Discipline

每一层都应有明确更新触发条件：

- `AGENTS.md`
  - 仅在导航面、读取顺序、协作骨架、热区入口或当前主线 headline 变化时更新
- `current_state`
  - 当前阶段、active lane、blocker、allowed moves 改变时更新
- `current_committed_plan`
  - 当前批准执行步、`do_not_do_now`、退出条件变化时更新
- `runtime_contract`
  - 入口、参数、边界、failure taxonomy 改变时更新
- `domain_review_rubric`
  - 术语、promotion ladder、reviewer gate 改变时更新
- `current_task_handoff`
  - task 状态、objective、checkpoint、blocker、proof 变化时更新
- `execution_routing`
  - 模式路由、wake / anti-stall、冲突裁决、escalation 规则变化时更新
- `status_index`
  - 新 task、新 report、新 archive 或“当前默认续接 task”变化时更新
- `agent_architecture_issue_ledger`
  - 多次出现同类路由失配、层级漂移、承载面缺口，或需要记录后续重构触发条件时追加

硬规则：

- 如果下层文档还没同步，不要先在 `AGENTS.md` 中写出“好像已经同步”的新叙事。
- 若当前批准执行步变化，优先更新 `current_committed_plan`；不要只在 handoff 或 report 里悄悄改方向。
- 若 `current_task_handoff` 已 `passed` 但下一切片尚未定义，应在 `status_index` 明确写出“当前没有新的 active task”，而不是继续让旧 task 假装是默认续接面。

### 1.13 Discard / Legacy Entry Discipline

迁移旧入口时，必须先给每个 legacy 片段一个明确动作标签，再决定是否删改：

- `map`
  - 内容仍有稳定价值，且能落到唯一承载层；必须写清 `mapped-to`
- `archive`
  - 内容只保留追溯价值，不再作为默认入口；必须写清 `archived-to`
- `discard`
  - 内容重复、过时、无 consumer、会制造第二真值层，或只剩噪声；必须写清 `discarded-because`
- `escalate`
  - 内容触及安全、错误 repo 作用域、authority 冲突或叙事冲突；必须先升级处理，不能直接迁入新结构

默认判定：

- 跨任务稳定规则、repo-local reviewer gate、resume 读序，优先 `map`
- 长 why-not、旧 report、已退出当前工作集的 handoff、run 级 artifact 洪水，优先 `archive`
- 旧总目录式入口、重复 resume 说明、过时 shim、会与 `Navigation Surface` / `current_committed_plan` / `status_index` 竞争的 legacy 入口，优先 `discard`
- 明文凭据、错误 repo 路径、互相冲突的 authority 口径，必须 `escalate`

硬规则：

- 未完成 `mapped-to / archived-to / discarded-because / escalated-because` 标记前，不得删除 legacy 入口。
- `Navigation Surface` / `status_index` 缺失时，只能认定为迁移中间态；不得把“旧入口仍能凑合用”写成 blueprint 已完成。
- archive 只承接历史追溯，不得回升为默认首跳；discard 也不应另建“legacy 索引页”继续常驻导航层。

## 2. Decision Matrices

### 2.1 Collaboration Mode Matrix

| 场景 | 默认模式 | 说明 |
| --- | --- | --- |
| 需求模糊、边界不清、需要先收敛问题 | `Debate` | 先定义问题、理想态、gap 与策略；默认不直接实现 |
| 需要显式审查 / 执行分工 | `Reviewer + Planner / Executor` | 保留双窗口显式角色张力；`reviewer + planner` 不替代执行 |
| 需求已批准、要进入落地与验收编排 | `Conductor` | 走状态机调度、per-task quality gate 与 clean-context 续接 |
| 小改动、边界清晰、低风险 | `单窗口执行` | 单执行者直接推进当前主线 |

### 2.2 Skill Routing Matrix

| 场景 | 必用 Skill | 可选 Skill | 最低产出 |
| --- | --- | --- | --- |
| `pytest` / harness / 运行时异常 | `systematic-debugging` | `ai-regression-testing` | 根因、证据、回归结果 |
| 新功能 / 新 contract / 新 evaluator 规则 | `tdd-workflow` | `eval-harness` | 测试、实现、最小回归 |
| 第三方库 / API / 模型接入 | `documentation-lookup` | `verification-loop` | 官方依据、落地约束 |
| GitHub / PR / `gh` CLI | `github` | 无 | 仍需遵守 Git 宪法 |
| 外部资料与上游方案调研 | `wiki-researcher` | `documentation-templates` | 来源、约束、对齐说明 |
| 复杂设计 / 多模块改造 | `spec-workflow` | `verification-loop` | 需求、设计、任务分解 |

### 2.3 Debate Gate Matrix

进入 `Debate` 的典型信号：

- 当前问题仍停留在“症状清单”
- 理想态、对象模型、边界或生命周期未定义
- 方案之间分歧其实源于底层概念不一致
- scope 裁剪后可能把核心目标裁空
- 大家都知道“应该继续上次任务”，但没人说得清上次任务的工作单元、状态和默认入口

禁止把下列问题直接带入实现：

- 未定义工作单元
- 未定义对象模型
- 未定义主系统 / 工作台边界
- 未定义用户可见性与控制权
- 未定义“当前 task 持续态”和“历史报告”之间的区别

### 2.4 Conductor Gate Matrix

进入 `Conductor` 前必须满足：

- 需求已被批准
- 目标 scope 已明确
- 验收边界可描述
- 已知哪些需要设计评审、哪些需要真实验证
- 已知默认恢复首链 `AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff` 的落点在哪里

`Conductor` 必须拒绝的情况：

- 需求仍在争议中
- 关键对象模型缺失
- 用户可见变更未经过必要的设计判断
- 想一口气把整个需求直接交给 Dev 实现
- 当前 `current_committed_plan` / `task_handoff` / `status_index` 缺失，但仍试图假装可以 clean-context 续接

### 2.5 AGENT TEAM Capability Matrix

`AGENT TEAM` 不是协作模式本身；它只是挂接在当前协作模式上的条件化能力。
只有当任务“复杂且可以拆分为互不重叠或低耦合的子问题”时，才启用 `AGENT TEAM`。
不得把“用户提到多人 / 并行”自动翻译成“全面并行”或跳过 explicit owner 拆分。

| 条件 | 推荐处理 |
| --- | --- |
| 单文件或小改动 | 不启用 `AGENT TEAM`，保持单主代理或显式双窗口 |
| 根因未明、关键路径高度不确定 | 单主代理先调查 |
| 可拆为互不重叠写集合 | 在当前协作模式下附加 `AGENT TEAM` |
| 实现与只读回归分析可分离 | 在当前协作模式下附加 `AGENT TEAM` |
| code path 与 docs/spec path 可分离 | 可启用 `AGENT TEAM`，但必须拆清 owner / write set / verification surface |

### 2.6 AGENT TEAM Capability Flow

启用后必须遵守：

1. `Planner`：定义目标、风险、成功标准、回归范围
2. `Implementer`：做最小必要改动并补测试
3. `Analyst`：运行定向回归 / smoke，分析证据与风险
4. `Reviewer`：审查行为回归、测试缺口、边界错误与方案质量
5. 主执行者负责最终集成，不得把结论碎片化输出

硬规则：

- 蓝本不得硬编码某个具体模型版本；下游仓库若确需固定模型 / 推理档位，必须在 repo-local `AGENTS.md` 或 `execution_routing` 明示，并说明适用任务与替代策略。
- 最终必须统一收口为五部分：
  1. `结论`
  2. `改动`
  3. `验证`
  4. `风险`
  5. `下一步`

### 2.7 Mode Entry / Capability Routing

用户可以直接说“进入某种模式”，不需要重复列出角色名、文件名或完整读取顺序。
一旦用户明确说出模式名，代理必须把它视为直接路由指令，并自行按本节索引相关文件。

硬规则：

- 用户说“进入单窗口执行模式”，就按单执行者主路径自动读取，不要求用户再点名文件。
- 用户说“进入双窗口模式”，就自动切到 `Reviewer + Planner / Executor` 双角色协作读取面；是否附加 `AGENT TEAM` 只看任务能否低耦合拆分，不自动升格。
- 用户说“进入 Debate 模式”，就自动切到问题收敛路径，而不是直接开写代码。
- 用户说“进入 Conductor 模式”，就自动切到 task state / quality gate / clean-context 续接路径。
- 用户明确要求 `AGENT TEAM` 时，先保留当前主模式，再只在 owner、write set 与验证面都能拆清时启用。
- 如果用户只说“先看 AGENTS.md，自己索引相关文件”，默认按本节做模式判定与文件路由。
- 如果用户没有指定模式，默认进入 `单窗口执行模式`。
- 如果当前工具面不支持真实双窗口，仍要在同一代理内按对应角色顺序执行，而不是回退成无角色协作。

| 模式 | 用户可直接说的话 | 代理必须先读 | 默认动作 |
| --- | --- | --- | --- |
| `单窗口执行模式` | `进入单窗口执行模式` / `单窗口跑` / `先看 AGENTS.md 自己索引` | `AGENTS.md` -> `Navigation Surface` -> `current_committed_plan` -> `current_state` -> `status_index` -> `current_task_handoff` -> `runtime_contract` -> `domain_review_rubric`；仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing` | 单执行者直接推进当前主线，必要时自行调用 skills，但不额外拆角色 |
| `双窗口模式` | `进入双窗口模式` / `planner+executor` / `reviewer+executor` | 共同先读 `AGENTS.md` 和 `Navigation Surface`；`reviewer + planner` 再读 `current_committed_plan`、`current_state`、`status_index`、`current_task_handoff`、`domain_review_rubric`；`executor` 再读 `current_committed_plan`、`current_state`、`status_index`、`current_task_handoff`、`runtime_contract`；仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing` | `reviewer + planner` 负责判断主线与下一步指令，`executor` 负责实现、验证、证据回传 |
| `Debate 模式` | `进入 Debate 模式` / `先 debate` / `先收敛问题` | `AGENTS.md` -> `Navigation Surface` -> `current_committed_plan` -> `current_state` -> `status_index` -> `current_task_handoff`（若当前问题与 task 状态相关）；仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing` -> `debate_host.md` -> `debate_proposer.md` -> `debate_reviewer.md` | 先做问题定义、理想态、底层定义、四维 gap、三段式策略；未经收敛不直接进入实现 |
| `Conductor 模式` | `进入 Conductor 模式` / `按 conductor 推进` / `走 task state` | `AGENTS.md` -> `Navigation Surface` -> `current_committed_plan` -> `current_state` -> `status_index` -> `current_task_handoff` -> `runtime_contract`；仅在需要模式路由 / wake / anti-stall 时补读 `execution_routing` -> `conductor.md` | 按 task 单元、quality gate、clean-context 续接推进；优先维护 `objective / in_scope / done_when / proof` |

若用户同时指定“模式 + 任务”，代理应先进入对应模式，再在该模式的读取面内对齐当前任务，不要反过来先凭印象行动。

### 2.8 Mode Boundary Rules

- `Debate` 负责问题收敛，不把未批准议题直接推进成实现。
- `Reviewer + Planner / Executor` 是显式协作模式；`reviewer + planner` 不接管执行，`executor` 不越权改写 gate truth。
- `Conductor` 负责任务编排、quality gate 与 clean-context 续接，不等同于“自动多人并行”。
- `AGENT TEAM` 只在 owner / write set / verification surface 可明确拆分时启用；若真值边界不清或关键路径未稳，优先回到单主代理或显式双窗口协作。

## 3. Collaboration Contracts

### 3.1 Reviewer + Planner Contract

`reviewer + planner` 不是主执行者。

核心职责：

1. 审查执行者给出的结果，而不是复述它的说法
2. 判断它是否真正推进了当前主线，而不是只完成了局部动作
3. 检查它是否符合 `AGENTS.md`、当前主线目标、当前默认续接面、最近演化日志、模块稳定教训、回归矩阵和流程约束
4. 识别真正的阻断项
5. 给出“下一步发给执行者的明确指令”，要求可直接复制转发，且能推动主线继续前进
6. 如果执行者方向错了，要直接纠偏，不要模糊建议
7. 如果执行者已经达标，要明确说明“通过”，并指出下一阶段最优先事项
8. 默认不要因为表达不够漂亮、文档不够丰满、格式不够工整而卡住执行者；只有当这些问题会影响 SSOT、后续消费、阶段判断或回归控制时，才把它们视为阻断

默认审查标准：

- 不是看“是否做了工作”，而是看“是否完成了当前目标，或至少把当前目标推进到下一个明确阶段”
- 不是看“有没有跑测试”，而是看“测试是否覆盖了本次改动最主要的风险面”
- 不是看“有没有产物”，而是看“产物是否能直接作为下一阶段的可靠输入”
- 不是看“表面通过”，而是看“是否仍有未解释的 shortfall、隐藏假设、手工步骤漂移、或 consumer 侧仍需额外拼装”
- 对非阻断瑕疵，不要过度放大；对真正阻断项，不要放过
- 默认不要把同一条下一步同时写成“当前下一步”和“下一阶段建议”；若两者实为同一动作，只保留当前下一步。

### 3.2 Executor Contract

执行者进入任务后，先严格按当前模式规定的读取面和 `Resume-First Protocol` 对齐当前状态，不得跳读、不得先入为主。

执行原则：

- 始终以“性能、稳健性、可复现性、证据链完整”为最高优先级
- 全程使用 `sequential-thinking` 深入思考，不得跳过思考直接给结论
- 按 `Skill Routing Matrix` 选择必要 skills；只用必要集合，不滥用 skill
- 若任务涉及复杂设计、跨模块影响、验收边界不清，也要遵守 `spec-workflow` 的要求先厘清边界
- 命中模块后，再补读对应 `稳定模块教训`，避免重复踩坑
- 不得擅自扩大范围；严格受当前用户指令约束
- 最终统一收口为 `结论 / 改动 / 验证 / 风险 / 下一步`；必要前提只允许在开头用 `1-3` 句补充，不得再写第二轮结论摘要

执行中的纪律：

- 先确认当前任务边界，再行动
- 不要把已有 baseline / compare / preview / smoke 误写成正式 reviewer 放行结果
- 不要把部分落盘 / 初步基线 / 可读 artifact 误写成已 fully closed / 可直接下游消费
- 当文档、代码、artifact 叙事可能不一致时，优先做一致性核对，避免乐观外推
- 若发现已有热区、runbook、tasks、artifact 之间口径不一致，先收口叙事，再讨论是否推进下一阶段

## 4. Workflow Model

### 4.1 Debate

`Debate` 是问题收敛机制，不是代码生成机制。

固定角色：

- `Host`
- `Proposer`
- `Reviewer`

固定层级：

1. 问题定义 / 产品定位
2. 理想态与底层定义
3. 四维 gap analysis
4. 三段式策略与 `no-regret` 判断

Layer 2 不能省略的底层定义：

- 主系统与工作台 / 会话系统的关系
- `session` / 工作单元的生命周期
- 工作材料的对象模型
- 用户控制权与可见性边界

Host 必须在每层都声明：

- 当前层的核心问题
- 推进门槛
- 回退门槛
- 哪些是 blocker，哪些是可后置项

禁止行为：

- 把 gap analysis 退化成症状清单
- 在底层定义缺失时直接进入策略层
- 做 scope 裁剪但不映射回原始目标
- 只因为“看起来低耦合”就提前做，导致底座未定义

`Debate` 的交付物至少应包含：

- 共识化的问题定义
- 理想态 / 底层定义
- 四维 gap 分析
- 三段式策略
- scope / 非 scope
- 未决问题与谁来最终拍板

### 4.2 Conductor

`Conductor` 是状态机调度中枢，不写代码，不做设计终判。

固定职责：

- 维护 pipeline state
- 控制 dispatch
- 控制 quality gate
- 控制 context budget
- 维护 backlog / progress / acceptance 状态

默认状态机：

1. `intake`
2. `debate_required` 或 `skip_debate`
3. `planning` / 必要设计评审
4. `scheduled`
5. `executing`
6. `per_task_review`
7. `fix_same_context` 或 `next_task_fresh_context`
8. `final_review_orchestration`
9. `acceptance`
10. `done` / `blocked`

固定循环：

1. intake
2. decide `debate` or skip
3. planning / design review
4. scheduled
5. per-task execution
6. per-task diff review
7. final orchestration
8. acceptance
9. done

`Conductor` 必须坚持的 task 单元纪律：

- 一次只推进一个最小可验收 task
- 每个 task 都要显式写清 `objective / in_scope / out_of_scope / done_when / proof`
- Dev 完成一个 task 后，必须先带测试或 smoke 证据过 per-task review
- 若失败且问题仍局限在当前 task，优先原地返修，保留上下文，不要整轮重来
- 若 task 通过，下一 task 默认用新上下文继续，避免把错误上下文带到后续 task
- 当前批准执行步应写入 `current_committed_plan`，当前 task 的持续状态应写入 `current_task_handoff`，最新任务与报告位置应写入 `status_index`；`execution_routing` 只承载模式路由 / wake / anti-stall，而不是继续污染 `AGENTS`

### 4.3 Current Task Lifecycle

推荐的 task 生命周期状态：

- `planned`
- `scheduled`
- `executing`
- `blocked`
- `in_review`
- `passed`
- `accepted`
- `cancelled`
- `archived`

状态定义：

- `passed`
  - 当前 task 自身的 `done_when` 已满足
  - 但项目级 blocker 可能仍存在
- `accepted`
  - 当前 task 已被正式吸收到当前状态面
  - 不再作为默认续接面
- `archived`
  - 当前 task 只保留在 `status_index` / archive 中
  - 不应继续占据 `current_task_handoff`

硬规则：

- 一个仓库在同一时刻只能有一个默认 `current_task_handoff`。
- 若当前 handoff 已 `passed` 且下一 task 未定义，应在 `status_index` 标明“当前无新 active task”，不要让旧 handoff 假装仍是 active task。
- 若新 task 已明确开始，应轮转 `current_task_handoff`，并把旧 task 移入 `status_index`。

## 5. 稳定模块教训

本节只记录“跨多轮、跨任务仍稳定成立”的模块教训，不记录单轮任务状态。

每个模块下只保留：

- 典型踩坑
- 失败信号
- 必做验证
- 明确禁忌

不要记录：

- 本周 exact artifact path
- 本轮 owner
- 本次 commit 结论
- 临时阶段判词

## 6. Git 操作宪法

### 6.1 核心准则

1. 查询类 Git 操作可直接执行；本地普通 `git commit` 可直接执行，且默认在每完成一个有意义的小型任务后立即做一次最小边界 snapshot commit，除非用户明确禁止、或当前 worktree 含有无法安全隔离的他人改动
2. 以下 Git 操作及同等级危险变体统一按高危处理：`git commit --amend`、`git push`、`git pull`、`git merge`、`git rebase`、`git checkout`、`git restore`、`git reset`、`git clean`
3. 对上述高危 Git 操作，代理必须先将以下警示语单独成行连续输出三次，再说明具体命令、目的、风险与影响面：
   - `下面要进行高危破坏性操作，请人工确认`
   - `下面要进行高危破坏性操作，请人工确认`
   - `下面要进行高危破坏性操作，请人工确认`
4. 上述高危 Git 操作至少需要用户两次明确同意；未获双重同意前，只允许输出计划，不得执行
5. 若命中改写历史、批量回退、跨分支切换、远程同步到共享分支、`reset --hard`、`clean -fdx`、`push --force` 等特高危情形，升级为三次明确同意；未完成三确认前，不得执行
6. 任何高危 Git 动作都不因本地普通 `git commit` 已被允许而放宽

### 6.2 需要前置询问的操作

- `git commit --amend`
- `git checkout` / `git restore` / `git reset` / `git clean`
- `git push` / `git pull`
- `git merge` / `git rebase`

### 6.2.1 高危 Git 操作双确认协议

对以下操作统一适用本协议：

- `git push`
- `git pull`
- `git merge`
- `git checkout`
- `git restore`
- `git reset`
- `git clean`

执行前必须满足：

1. 代理先单独成行输出以下警示语三遍：
   - `下面要进行高危破坏性操作，请人工确认`
   - `下面要进行高危破坏性操作，请人工确认`
   - `下面要进行高危破坏性操作，请人工确认`
2. 再补充具体要执行的命令、目的、风险与影响面
3. 用户第一次明确同意
4. 代理再次确认将执行的是同一高危命令集合
5. 用户第二次明确同意
6. 只有到这一步，代理才可以真正执行

任何一步缺失，都视为未获授权。

### 6.2.2 特高危 Git 操作三确认协议

对以下操作或场景升级为三确认：

- `git commit --amend`
- `git rebase`
- `git reset --hard`
- `git clean -fd` / `git clean -fdx`
- `git checkout` 跨分支切换且 worktree 非干净
- `git push --force` / 改写远程共享分支

执行前必须满足：

1. 代理先单独成行输出以下警示语三遍：
   - `下面要进行高危破坏性操作，请人工确认`
   - `下面要进行高危破坏性操作，请人工确认`
   - `下面要进行高危破坏性操作，请人工确认`
2. 再补充具体要执行的命令、目的、风险、影响面与可逆性
3. 用户第一次明确同意
4. 代理再次确认将执行的是同一高危命令集合
5. 用户第二次明确同意
6. 代理再次确认这是特高危 Git 操作，并重申不可逆面或受影响的分支 / 历史
7. 用户第三次明确同意
8. 只有到这一步，代理才可以真正执行

任何一步缺失，都视为未获授权。

### 6.2.3 本地 Commit 执行规则

本地普通 `git commit` 可直接执行，但代理仍应：

- 在每完成一个有意义的小型任务、且验证已闭合后，默认立即做一次本地 snapshot commit，而不是等多个小任务堆积后再一次性提交
- 只在“有意义的最小边界”做本地 snapshot commit，而不是为每一行改动都机械提交
- 若当前 worktree 存在无法安全隔离的用户改动、或 repo 仍未完成基本 index/bootstrap 装配，先明确说明阻塞点，不得强行把无关内容一并提交
- 在回传中说明本次 snapshot 的范围与目的
- 不把 `git commit --amend`、`git rebase`、`push --force` 等改写历史动作伪装成“普通 commit”
- 一旦命中特高危 Git 动作，立即转入上面的双确认 / 三确认协议

### 6.3 可直接执行的查询类命令

- `git log`
- `git status`
- `git ls-files`
- `git blame`
- `git remote -v`

### 6.4 长期保留规则

- 默认采用小步本地提交；每完成一个小型闭合任务就落一次本地 snapshot
- 默认不改写旧历史
- 关键节点优先打 tag
- 临时产物优先 `.gitignore`
- 远程绑定只在用户明确要求时进行

## 7. Status Index And Hotzone Logs

### 7.1 Status Index

`status_index` 的职责是：

- 指向默认恢复首链里的 `INDEX` 落点
- 指向当前默认续接 task
- 指向最近一次 `current_committed_plan`
- 列出最近 task handoff
- 列出最近 report / memo / decision
- 指向 archive 或历史 handoff
- 按需指向 `execution_routing`

它不是长报告。
它应比 `AGENTS.md` 更细，但比 report 更短。
在正式仓库里，它是默认配套层，不是可选附加件。
若暂时缺失，只能说明仓库仍处于迁移中间态，不应被描述为“已完成装配”。

推荐每项只保留：

- 标题 / task_id
- 当前状态
- 更新时间
- 什么时候该读
- 路径

### 7.2 Hotzone Logs

- `AGENTS.md` 若保留热区日志，默认只保留最近 `20` 条
- 热区日志是索引层，不是 mini-spec
- 每条只保留：
  - 标题
  - 1 句结论
  - 1 句风险边界
  - 1 个详情链接
- exact counts、artifact paths、why-not、替代分支，统一放到 archive 或专门 memo
- 旧热区或 legacy 入口若退出默认导航层，也必须按 `mapped-to / archived-to / discarded-because / escalated-because` 标记处理，不能“先裁后归档”

热区日志不要替代 `status_index`。

推荐格式：

```markdown
- [R20-01] [YYYY-MM-DD] [Type] `Title`
  - 结论：一句话
  - 边界：一句话
  - 详情：`docs/...` 或 `specs/...`
```

## 8. 文件分层

```text
mode/AGENTS.refactor.md                         # 模板仓库宪法层、导航面、热区索引
mode/status/current_committed_plan_template.md # 当前已批准执行步模板
mode/current_state.v2.md                       # 模板仓库当前项目态占位面
mode/agent_system/status_index_template.md     # 默认恢复索引模板
mode/agent_system/current_task_handoff_template.md
                                               # 当前 task 状态模板
mode/agent_system/execution_routing_template.md # 模式路由 / wake / anti-stall 模板
mode/runtime_contract.v2.md                    # 模板仓库运行态合同占位面
mode/domain_review_rubric.v2.md                # 模板仓库 reviewer gate / 术语占位面
mode/agent_system/prompts/*.md                 # 角色模板
mode/agent_system/window_init_template.md
mode/agent_system/agent_architecture_issue_ledger_template.md
                                               # 架构问题账本模板；按需追加，不是默认恢复入口
mode/CLAUDE.md / mode/GEMINI.md / mode/.github/copilot-instructions.md
                                               # 工具特定 shim；只导向同一套核心规则
```

下游仓库迁入时，用该仓库自己的 actual path 替换上面的 `mode/...`；不要把模板路径误当正式仓库真值。

## 9. Navigation Surface 示例（模板仓库实际路径）

这个模板仓库里的 actual path 可参考下面这种最小写法；下游仓库请替换成自己的 repo-local 路径：

```markdown
## Navigation Surface

- `mode/status/current_committed_plan_template.md`
  - 作用：看当前唯一已批准执行步
  - fallback：必须显式说明 approved-step surface 仍缺失
- `mode/current_state.v2.md`
  - 作用：看当前主线、blocker、allowed moves
  - fallback：若不存在，先看最新阶段交接文档
- `mode/agent_system/status_index_template.md`
  - 作用：定位最近 task、report、archive
  - fallback：看 `mode/agent_system/README.md` 与最近日期文件
- `mode/agent_system/current_task_handoff_template.md`
  - 作用：看当前 task 状态、checkpoint、proof snapshot
  - fallback：回跳 `mode/agent_system/status_index_template.md`
- `mode/agent_system/execution_routing_template.md`
  - 作用：仅在需要模式路由 / wake / anti-stall 时补读
  - fallback：缺失时说明该补充层尚未装配
```

## 10. 冷历史归档

- 详细证据、长叙事、命令输出、why-not 分析统一进入 archive
- 默认不要逐行通读 archive
- 只有在需要追溯旧背景或命中相关模块时再检索
