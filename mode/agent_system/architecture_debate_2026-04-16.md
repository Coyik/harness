# Agent System Architecture Debate 2026-04-16

更新时间：`2026-04-16`
分析方式：`Debate 模式`
证据范围：

- `mode/AGENTS.refactor.md`
- `mode/agent_system/{README.md,current_task_handoff_template.md,status_index_template.md}`
- `/volume/wzhang/cky-workspace/my_projects/VLM_Bench/AGENTS.md`
- `/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/current_task_handoff.md`
- `/volume/wzhang/cky-workspace/my_projects/CGen/docs/status/current_task_handoff.md`
- `/volume/wzhang/cky-workspace/my_projects/Cangjie/docs/status/current_task_handoff.md`

## Layer 1 - 问题定义

### 当前层

- 问题定义 / 产品定位

### 本轮焦点问题

- 当前 agent system 到底缺的是什么：是“文档不够多”，还是“续接与路由没有被定义成正式能力”？

### Proposer 观点

- 当前架构的核心价值已经成立：`AGENTS + current_state + runtime_contract + domain_review_rubric + current_task_handoff` 这套分层，已经明显优于把所有内容继续堆回巨型 `AGENTS.md`。
- 但它目前更像“规则分层系统”，还不是“稳定续接系统”。
- 真正缺口不是“再加更多说明文档”，而是缺一个 canonical 的导航面与状态索引面，让 agent 能在 clean-context 下稳定回答：
  - 当前默认从哪个 task 继续
  - 当前这个 task 处于什么状态
  - 若当前 task 已结束，下一跳去哪

### Reviewer 挑战

- 现网 `AGENTS.md` 在 `Session Header` 之后直接进入 `Hard Rules`，没有 `Navigation Surface`。例如 [VLM_Bench/AGENTS.md](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/AGENTS.md:8) 到 [VLM_Bench/AGENTS.md](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/AGENTS.md:17) 之间只有 headline，没有“继续上次任务先看哪”的入口图。
- 已落地仓库里都有 `docs/status/current_task_handoff.md`，但没有看到 `docs/status/INDEX.md`。这意味着系统默认假设“当前 handoff 总能代表当前任务”，一旦 handoff `passed`、任务切换、或者报告分叉，agent 就会失去导航面。
- 这不是小瑕疵，而是系统级缺口：当 context 丢失时，代理没有正式的 `resume` 协议，只能依靠猜。

### Host 判定

- 当前架构的主问题已经收敛：它不是“分层错误”，而是“缺少把续接能力产品化的那一层”。
- 因此，本轮 Debate 的真正目标不是继续讨论文档是否应更长，而是把“导航、续接、轮转、归档”的对象模型补齐。

## Layer 2 - 理想态与底层定义

### 当前层

- 理想态与底层定义

### 本轮焦点问题

- 这套系统的主系统、工作台、工作单元、对象模型、控制权边界分别是什么？

### Proposer 观点

- 主系统：
  - 一个 repo-local 的长期记忆与执行路由系统。
  - 它由 `AGENTS`、状态页、task handoff、status index、reports、archive 组成。
- 工作台 / 会话系统：
  - 当前这一次 agent 窗口或 chat context。
  - 它是短期工作面，不应承担长期记忆。
- 工作单元：
  - `task`
  - 它应有明确生命周期：`planned -> scheduled -> executing -> in_review -> passed -> accepted -> archived`
- 工作材料对象模型：
  - `AGENTS`
    - 跨任务稳定规则、导航面、热区索引
  - `current_state`
    - 项目级当前快照
  - `runtime_contract`
    - 运行入口与边界
  - `domain_review_rubric`
    - 词义、promotion ladder、reviewer gate
  - `current_task_handoff`
    - 当前默认续接 task 的状态面
  - `status_index`
    - 最近 task / report / archive 的索引面
  - `report / decision / archive`
    - 长证据与历史
- 用户控制权与可见性边界：
  - 用户控制 lane 切换、promotion、high-risk narrative 改写。
  - agent 可在当前 scope 内更新下层文档，但不能自行把旧报告升格成当前 active truth。

### Reviewer 挑战

- 当前落地系统里，“主系统”和“工作台”还没有完全分开。
- 证据一：`current_task_handoff` 被当成当前任务状态面，但内容已经膨胀得接近 mini-report。
  - [VLM_Bench current_task_handoff](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/current_task_handoff.md:25) 到 [VLM_Bench current_task_handoff](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/current_task_handoff.md:77) 已经包含大段文件白名单、证据白名单、验证清单和路径清单。
  - [CGen current_task_handoff](/volume/wzhang/cky-workspace/my_projects/CGen/docs/status/current_task_handoff.md:25) 到 [CGen current_task_handoff](/volume/wzhang/cky-workspace/my_projects/CGen/docs/status/current_task_handoff.md:81) 也呈现同样趋势。
- 证据二：工具私有 shim 没被纳入正式入口面。
  - [CGen current_task_handoff](/volume/wzhang/cky-workspace/my_projects/CGen/docs/status/current_task_handoff.md:38) 把 `claude.md` 放进 allowed evidence，[CGen current_task_handoff](/volume/wzhang/cky-workspace/my_projects/CGen/docs/status/current_task_handoff.md:104) 也要求下一位 agent 先读它。
  - [Cangjie current_task_handoff](/volume/wzhang/cky-workspace/my_projects/Cangjie/docs/status/current_task_handoff.md:38) 把 `.claude/status/current-phase.md` 作为当前证据的一部分，[Cangjie current_task_handoff](/volume/wzhang/cky-workspace/my_projects/Cangjie/docs/status/current_task_handoff.md:95) 也要求下一位 agent 先读它。
- 如果这些 shim 继续以“task 私货”的方式存在，而不是回归 `Navigation Surface` 或 path-scoped 规则，长期会形成多套入口。

### Host 判定

- 理想态已经够清楚：
  - `AGENTS` 是入口与规则
  - `current_task_handoff` 是默认续接 task
  - `status_index` 是目录型索引
  - `report` 是长证据
- 当前最大底层定义缺失不是“还少哪个角色”，而是 `status_index` 和 task 生命周期没有被正式纳入系统对象模型。

## Layer 3 - 四维 Gap Analysis

### 当前层

- 四维 gap analysis

### 本轮焦点问题

- 当前系统距离理想态，最关键的缺口有哪些？

### Proposer 观点

#### 1. Routing Gap

- 已落地 `AGENTS.md` 没有 `Navigation Surface`。
- 结果是代理只知道“有哪些层”，不知道“默认第一跳”。

#### 2. Lifecycle Gap

- 当前系统有 `current_task_handoff`，但没有正式 `status_index`。
- 结果是 task 一旦 `passed`，系统就缺少“当前无新 active task”或“下一个默认 task 是谁”的表达能力。

#### 3. Shape Gap

- `current_task_handoff` 正在承担过多内容，逐渐变成 report + runbook + 状态页的混合体。
- 结果是它既太重，又不适合快速续接。

#### 4. Governance Gap

- 更新触发条件与 owner 规则不够外显。
- 工具私有 shim 和 repo-local path 仍然游离于主入口之外。

### Reviewer 挑战

#### A. `task status` 与 `lane status` 混写

- [VLM_Bench current_task_handoff](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/current_task_handoff.md:7) 标记 `status=passed`，但 [VLM_Bench current_task_handoff](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/current_task_handoff.md:81) 到 [VLM_Bench current_task_handoff](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/current_task_handoff.md:87) 同时明确全局 blocker 仍在。
- [Cangjie current_task_handoff](/volume/wzhang/cky-workspace/my_projects/Cangjie/docs/status/current_task_handoff.md:7) 也是 `status=passed`，但 [Cangjie current_task_handoff](/volume/wzhang/cky-workspace/my_projects/Cangjie/docs/status/current_task_handoff.md:81) 到 [Cangjie current_task_handoff](/volume/wzhang/cky-workspace/my_projects/Cangjie/docs/status/current_task_handoff.md:88) 明确说更高等级仍不能碰。
- 这不是事实错误，但缺少状态模型解释时，下一位 agent 很容易把 `passed` 误读为“当前默认继续做这个 task”或“lane 也通过了”。

#### B. `current_task_handoff` 与 report 边界不清

- 在三个项目里，handoff 都承载了大量证据与路径明细，导致“当前状态面”和“长证据面”开始重叠。
- 一旦再往里塞更多 run-level 细节，它就会退化成第二份 report。

#### C. 工具私有入口未被治理

- `claude.md`、`.claude/status/current-phase.md` 这类文件已经实质参与续接，但当前正式入口没有定义它们应如何被同步、何时优先、何时只作局部补充。

### Host 判定

当前架构最需要修的不是更多角色，而是四个明确缺口：

1. 缺 `Navigation Surface`
2. 缺 `status_index`
3. 缺 task 生命周期与 handoff 轮转规则
4. 缺 repo-local shim 的入口治理规则

## Layer 4 - 三段式策略与 No-Regret 判断

### 当前层

- 三段式策略与 `no-regret` 判断

### 本轮焦点问题

- 该怎么修，既不把系统重新做回巨型 `AGENTS`，又能稳定解决续接问题？

### Proposer 观点

#### Stage A - Blueprint Hardening

- 在蓝本里把以下能力写成硬规则：
  - `Navigation Surface`
  - `Resume-First Protocol`
  - `Repo-Local Actual Path Wins`
  - `status_index`
  - task 生命周期与 handoff 轮转规则
- 本轮已经在 `mode/AGENTS.refactor.md` 与模板文件中完成这一步。

#### Stage B - Deployed Repo Adoption

- 在每个正式项目里新增 `docs/status/INDEX.md`
- 在每个正式 `AGENTS.md` 中加入 `Navigation Surface`
- 对已 `passed` 但不再是默认续接面的 handoff 做轮转
- 若当前确实没有新 active task，就在 `status_index` 明写“当前无新 active task”

#### Stage C - Governance Hardening

- 定义 tool-specific shim 的归位规则：
  - 若它是长期必要入口，就进入 `Navigation Surface`
  - 若只是局部工具提示，就只能作为 path-scoped 补充，不得凌驾于主入口
- 增加轻量检查清单：
  - `AGENTS` 是否有 `Navigation Surface`
  - `docs/status/INDEX.md` 是否存在
  - `current_task_handoff` 的 status 是否与 `status_index` 一致
  - 是否存在多个“看起来像当前 task”的文件

### Reviewer 挑战

- 只改蓝本不改已落地仓库，不足以解决使用中的问题。
- 只新增 `INDEX.md` 但不约束 handoff 内容，也会继续膨胀。
- 只讲“状态轮转”但不解释 `passed / accepted / archived` 差异，仍会误导后续 agent。

### Host 判定

- 方案成立，且属于 `no-regret`：
  - 它不会把更多动态细节重新塞回 `AGENTS`
  - 它不会引入新的概念洪水，只是把已有隐含对象正式化
  - 即使未来继续演化，这几层也仍然稳定成立

## 最终结论

当前架构在使用中的不完善点，已经收敛为以下六项：

1. 已落地 `AGENTS.md` 缺 `Navigation Surface`
2. 已落地仓库缺 `status_index`
3. `current_task_handoff` 有膨胀成 report 的趋势
4. `passed` 与项目级 blocker / lane 状态之间缺少显式状态解释
5. tool-specific shim 参与续接，但没有被正式纳入入口治理
6. 缺少“当前无新 active task”的显式表达方式

## 建议执行顺序

1. 先把本轮蓝本改动作为新标准
2. 在 `VLM_Bench`、`CGen`、`Cangjie` 中各补一个 `docs/status/INDEX.md`
3. 给三者的正式 `AGENTS.md` 加入 `Navigation Surface`
4. 轮转已 `passed` 的旧 handoff，避免它们继续充当默认续接面
5. 统一 `passed / accepted / archived` 的状态语义
6. 清理或归位 `claude.md`、`.claude/status/current-phase.md` 这类 shim 的入口位置

## 待拍板项

- 是否要求每个正式仓库都必须有 `docs/status/INDEX.md`
- `current_task_handoff` 是否只允许保留最近一个默认续接 task
- tool-specific shim 是否必须在 `Navigation Surface` 明示，还是允许继续只在局部 handoff 出现
