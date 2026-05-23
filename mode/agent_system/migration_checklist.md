# Migration Checklist

更新时间：`2026-04-18`

## 1. 范围与前提

本文件是 `harness` agent-system 重构进入真正实施前的 adoption gate 清单。

它负责回答：

- 什么时候允许从冻结设计进入实施
- 先改什么，后改什么
- 哪些情况必须 stop-ship
- 三个目标项目应按什么顺序进入迁移

本文件不负责：

- 代替具体 patch 方案
- 承载项目业务状态
- 充当 `status_index` 或 `current_task_handoff`

## 2. 全局放行前提

以下前提未满足，迁移不得开始：

- `blueprint_migration_mapping.md` 已冻结，且 P0 锚点无未归属项
- 旧高价值信息已逐条标记 `mapped-to / archived-to / discarded-because`
- 明文凭据、错误 repo 内容、旧“唯一 SSOT + 强制进化日志”口径已被识别
- blueprint 已明确 `Navigation Surface`、`status_index`、`discard policy`、`prompt parity`
- blueprint 已把协作模式显式收口为 `Debate`、`Reviewer + Planner / Executor`、`Conductor`、`单窗口执行`，并把 `AGENT TEAM` 降回 capability
- README / rolling worklog / legacy 页面已具备 `resume_surface=false` 或等价降级语义，不再与 live truth 竞争默认入口
- 迁移后验收指标与前测基线已定义

## 3. Stop-Ship 条件

出现以下任一项，立即停止迁移：

- 任一 P0 高价值锚点未映射或多归属
- `Navigation Surface` 或 `status_index` 缺失，却已开始删除旧入口
- 首跳读序没有缩短，反而变长
- 术语混写率不降反升
- 产生多套 `current task`、多套 canonical entrypoint、或第二真值层
- 任何 partial / baseline / preview / close-ready evidence 被写成正式放行
- 新发现明文密钥、错误 repo 口径、或 shim 自立规则
- 任何 README / rolling worklog / legacy 页面重新被抬升成默认 resume 首跳

## 4. 阶段门总览

| gate_id | objective | outputs | owner | release_to_next |
| --- | --- | --- | --- | --- |
| `G0` | blueprint freeze | mapping + checklist 冻结 | planner | 所有 P0 锚点已定义 |
| `G1` | source inventory / triage | 旧入口分类完成 | planner + reviewer | 所有 legacy 段落都有动作标签 |
| `G2` | target surface bootstrap | 缺失承载面补齐 | implementer | `Navigation Surface` / `status_index` / rubric 缺口存在明确目标 |
| `G3` | stable-knowledge extraction | repo-local 知识迁移清单 | implementer + reviewer | 高价值知识未丢失 |
| `G4` | security / wrong-repo purge | 安全污染隔离 | reviewer | 所有密钥与错仓内容已退出迁移路径 |
| `G5` | navigation / status wiring | `AGENTS`、`INDEX`、handoff 接线完成 | implementer | clean-context 续接链可用 |
| `G6` | prompt read-path alignment | prompts 对齐新读序 | planner | 角色读法一致 |
| `G7` | cross-doc consistency review | 多层口径一致性通过 | analyst + reviewer | 无 duplicate truth / 无 lifecycle 漂移 |
| `G8` | repo freeze signoff | 实施阶段准入判定 | reviewer + planner | 允许进入真正 patch 阶段 |

## 5. 逐门执行清单

### G0 Blueprint Freeze

- `objective`
  - 冻结 canonical target，而不是直接写 patch
- `inputs`
  - `AGENTS.refactor.md`
  - `README.md`
  - `architecture_explained.md`
  - `status_index_template.md`
  - `current_task_handoff_template.md`
  - `blueprint_migration_mapping.md`
- `required_actions`
  - 冻结 P0 锚点
  - 冻结目标承载层与 discard policy
  - 冻结后测指标
- `blocking_conditions`
  - 仍存在“以后再看”的核心承载缺口
- `release_conditions`
  - 目标层与字段都可直接进入实施
- `outputs`
  - 两份冻结文档可供后续 patch 使用
- `cross_project_dependency`
  - 无
- `owner`
  - `planner`

### G1 Source Inventory / Triage

- `objective`
  - 给所有旧入口与旧段落打动作标签
- `inputs`
  - 旧 `AGENTS`
  - 当前 `AGENTS`
  - 旧报告 / 旧 shim / 旧 prompt
- `required_actions`
  - 标记 `keep/split/rewrite/create/drop/escalate`
  - 标记 `security contamination` 与 `wrong-repo content`
- `blocking_conditions`
  - 任一 legacy 段落没有去向
- `release_conditions`
  - 所有来源均有明确动作与目标承载
- `outputs`
  - source inventory register
- `cross_project_dependency`
  - blueprint 冻结完成
- `owner`
  - `planner + reviewer`

### G2 Target Surface Bootstrap

- `objective`
  - 先补缺失承载层，再谈压缩旧入口
- `inputs`
  - mapping 文档
  - 各模板与现有项目结构
- `required_actions`
  - 在 blueprint 中补 `Navigation Surface`
  - 补 `status_index` 能力
  - 在 `domain_review_rubric_template` 中补 `glossary/object model/state semantics` 模板骨架
  - 在骨架层补 `Lightweight Soft Constraints`
  - 在 execution/prompt 层补 `协作模式显式命名 + AGENT TEAM capability` 边界
- `blocking_conditions`
  - 仍需靠口头说明补入口
- `release_conditions`
  - 所有 `create` 类缺口都有可写入模板
  - blueprint 层已经具备 `glossary / object model / state semantics` 模板，不再把这类语义缺口留给实例仓临场发挥
- `outputs`
  - target surface ready
- `cross_project_dependency`
  - `G1`
- `owner`
  - `implementer`

### G3 Stable-Knowledge Extraction

- `objective`
  - 保住旧 AGENTS 里真正有价值的 repo-local 知识
- `inputs`
  - 旧 `AGENTS`
  - 当前 `AGENTS`
  - 项目 repo-local 文档
- `required_actions`
  - 抽取回归规则、skill 路由、模块教训、authority split
  - 为每类知识指定承载层
- `blocking_conditions`
  - 任何 P0 知识只能在旧文里找到
- `release_conditions`
  - 高价值知识都已在新承载层有归宿
- `outputs`
  - stable-knowledge register
- `cross_project_dependency`
  - `G2`
- `owner`
  - `implementer + reviewer`

### G4 Security / Wrong-Repo Purge

- `objective`
  - 把不应进入新架构的内容隔离出去
- `inputs`
  - source inventory register
  - 安全污染条目
- `required_actions`
  - 隔离明文密钥
  - 标记错误 repo 作用域内容
  - 明确哪些旧口径直接丢弃
- `blocking_conditions`
  - 安全污染仍可被默认入口命中
- `release_conditions`
  - 所有敏感与错仓内容已退出迁移路径
- `outputs`
  - security quarantine complete
- `cross_project_dependency`
  - `G1`
- `owner`
  - `reviewer`

### G5 Navigation / Status Wiring

- `objective`
  - 建立真正可用的 clean-context 续接链
- `inputs`
  - blueprint 模板
  - 目标项目当前结构
- `required_actions`
  - 接通 `AGENTS -> current_committed_plan -> current_state -> status_index -> current_task_handoff`
  - 保证 `Navigation Surface` 只做入口图，不自立第二真值层
  - 下游实例仓的 `INDEX` 明确 `why current default` 与 `fallback`
  - 所有 handoff 补 `lane`、`Why This Task Exists`、`Proof Snapshot`
- `blocking_conditions`
  - index 存在但不被 `AGENTS` 或模式路由读取
- `release_conditions`
  - 新代理能在 `<= 3` 个 artifact 内定位当前默认续接 task
- `outputs`
  - navigation chain ready
- `cross_project_dependency`
  - `G2` + `G4`
- `owner`
  - `implementer`

### G6 Prompt Read-Path Alignment

- `objective`
  - 让角色 prompt 真正读取新结构
- `inputs`
  - `planner_reviewer.md`
  - `executor.md`
  - `conductor.md`
- `required_actions`
  - 删除“最近20条进化日志”默认读法与旧 mode labels
  - 对齐 `Resume-First`
  - 对齐统一输出收口
  - 补齐 `中文默认`、`绝对日期绑定`、`README/legacy 非真值面` 这三类轻量软约束
- `blocking_conditions`
  - prompt 仍默认扫长历史
- `release_conditions`
  - 角色首跳与 `AGENTS` / `status_index` 一致
- `outputs`
  - prompt parity
- `cross_project_dependency`
  - `G5`
- `owner`
  - `planner`

### G7 Cross-Doc Consistency Review

- `objective`
  - 验证多层没有重新混写
- `inputs`
  - `AGENTS`
  - `current_state`
  - `runtime_contract`
  - `domain_review_rubric`
  - `current_task_handoff`
  - `status_index`
- `required_actions`
  - 检查 duplicate truth
  - 检查 lifecycle 漂移
  - 检查 forbidden narrative
  - 检查 `README / rolling worklog / legacy current-phase` 是否仍处于显式降级语义
- `blocking_conditions`
  - 同一事实需要三层以上重复同步
- `release_conditions`
  - 术语混写率下降，且没有新真值层
- `outputs`
  - consistency review passed
- `cross_project_dependency`
  - `G6`
- `owner`
  - `analyst + reviewer`

### G8 Repo Freeze Signoff

- `objective`
  - 决定是否允许进入真正 patch 阶段
- `inputs`
  - 所有 gate 的 pass/fail
  - 实施前后基线
- `required_actions`
  - reviewer 给出放行或阻断
  - planner 确认下一轮 patch 顺序
- `blocking_conditions`
  - 任一 P0 gate 未通过
- `release_conditions`
  - 下述五个总门全部通过
- `outputs`
  - implementation go / no-go
- `cross_project_dependency`
  - `G7`
- `owner`
  - `reviewer + planner`

## 6. 五个总门

| gate | pass_rule | evidence_path | blocking_reason | next_action |
| --- | --- | --- | --- | --- |
| 高价值信息保真通过 | `P0` 锚点 `0` 丢失、`0` 多归属 | mapping 文档 + source inventory | 旧高价值规则无唯一归位 | 回到 `G1/G3` |
| 首跳读序缩短通过 | `<=3` 个 artifact 内定位默认续接面；token 或行数下降 `>=30%` | blind resume dry-run | clean-context 续接未改善 | 回到 `G5/G6` |
| 术语混写下降通过 | `P0` 术语对 `0` 处混写；整体混写率下降 `>=50%` | rubric 词表抽样 | reviewer gate 仍易误写 | 回到 `G2/G7` |
| 实施后基线已落盘 | 七项核心指标均已记录 | baseline record | 无法做前后对照 | 回到 `G0` |
| 无中止条件触发 | 未命中任何 stop-ship 条件 | gate review | 存在安全、真值层或叙事升级问题 | 停止迁移并升级 |

## 7. 跨项目执行顺序

### 7.1 顺序原则

- `harness` blueprint 永远先于项目迁移
- `CGen` 可作为参考样板，但不是必须最先改写的目标仓库
- `VLM_Bench` 是第一优先级结构试点，但只有在 blueprint 冻结完成后才允许进入
- `Cangjie` 在 lifecycle 规则明确后做补齐

### 7.2 推荐顺序

1. `harness`
   - 冻结模板、prompt、mapping、checklist
2. `VLM_Bench`
   - 先补成 `6` 件套闭环：
     - `AGENTS`
     - `current_state`
     - `runtime_contract`
     - `domain_review_rubric`
     - `current_task_handoff`
     - `status_index`
3. `CGen`
   - 以现有结构为主，只补 prompt 对齐、index 字段、repo-local 知识归位
4. `Cangjie`
   - 只补 lifecycle 与 index fallback，不重写主叙事

## 8. 项目级最小通过标准

### harness

- 模板、prompts、mapping、checklist 已对齐
- `Navigation Surface`、`status_index`、discard policy、rubric 语义模板都已存在

### VLM_Bench

- 新增 [docs/status/INDEX.md](/volume/wzhang/cky-workspace/my_projects/VLM_Bench/docs/status/INDEX.md)
- `AGENTS` 写入 `默认续接入口`
- 模式路由与 prompts 不再默认扫“最近20条日志”
- 旧 `AGENTS copy` 不再作为默认可命中入口

### CGen

- `INDEX` 补 `why current default` 与 `fallback`
- handoff 补模板缺项
- prompts 与 blueprint 新读序一致

### Cangjie

- `passed` task 不再继续伪装成 active task
- `INDEX`、handoff、prompts 的 lifecycle 语义一致

## 9. 实施后基线记录

实施后至少记录以下七项：

- `resume_hops`
- `resume_token_budget`
- `time_to_current_task`
- `mixed_write_rate`
- `unmapped_anchor_count`
- `duplicate_truth_entrypoints`
- `shim_only_entrypoints`

## 10. 完成定义

只有当以下条件同时成立，才允许进入真正实施阶段：

1. mapping 文档与 checklist 文档都已冻结
2. 五个总门全部通过
3. 所有 stop-ship 条件均未命中
4. `reviewer + planner` 明确给出 `go`
5. 下一轮 patch 已按 `harness -> VLM_Bench -> CGen -> Cangjie` 的顺序排定
