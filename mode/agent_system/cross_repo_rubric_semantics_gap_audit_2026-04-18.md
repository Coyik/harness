# Cross-Repo Rubric Semantics Gap Audit

更新时间：`2026-04-18 UTC`

## 1. 范围

本页只审计四个仓库的 `domain_review_rubric` 语义层，不重复评估协作模式、恢复链或 legacy 降级。

对照对象：

- `VLM_Bench/docs/domain_review_rubric.v2.md`
- `Cangjie/docs/domain_review_rubric.v2.md`
- `CGen/docs/domain_review_rubric.v2.md`
- `harness/mode/agent_system/domain_review_rubric_template.md`

## 2. 目标问题

要回答的不是“这些 rubric 能不能用”，而是：

1. 它们是否已经和蓝本模板在 `Glossary / Object Model / State Semantics` 这一层同构。
2. 如果还没有，同构缺口会不会影响跨仓恢复、reviewer 复核和代理检索稳定性。
3. 下一步应先改蓝本、还是先改实例仓。

## 3. 审计结论

- 结论一：四仓在 `Canonical Boundary Pairs / Promotion Ladder / Reviewer Gates / Common Narrative Traps` 这一层已经整体可用。
- 结论二：真实缺口不在 boundary pair，而在 `Section 0` 语义层。蓝本模板已经要求显式定义 `canonical terms / object model / state semantics`，三个实例仓仍大多依赖读者从上下文自行推断。
- 结论三：这类缺口更像“语义显式化不足”，不是“reviewer 规则错误”。因此当前最优动作是先把缺口冻结成蓝本审计结论，并用测试防止模板回退；实例仓再分批补。

## 4. 对照矩阵

| 维度 | blueprint target | VLM_Bench | Cangjie | CGen | 影响判断 |
| --- | --- | --- | --- | --- | --- |
| `## 0. Glossary / Object Model / State Semantics` | 必须存在 | 缺失 | 缺失 | 缺失 | 三个实例仓都还没把术语层显式化 |
| `consume_surface / evidence_only_surface / legacy_history_surface` starter pack | 若仓库存在相关对象，需显式定义 | 有 `consume_surface / evidence_only_audit_surface`，但没有 `legacy_history_surface` 显式层 | 未显式定义 | 未显式定义 | VLM 最接近目标；另外两仓仍主要靠上下文理解 |
| `task_status / lane_status` | 推荐显式定义 | 缺失 | 缺失 | 缺失 | reviewer 仍能工作，但跨仓迁移时词义不够稳定 |
| `passed / accepted / archived` | 推荐显式定义 | 缺失 | 缺失 | 缺失 | “passed” 等词还没有统一成稳定语义层 |
| `planning_freeze_passed / execution_ready` | 推荐显式定义 | 缺失 | 缺失 | 已有 boundary pair，但不是 state semantics section | CGen 最接近目标，但仍未上升到模板要求的显式语义层 |
| `raw_truth / effective_truth / reviewer_truth` | 推荐显式定义 | 有 dual truth 实际语义，但未显式命名为 state semantics | 缺失 | 缺失 | VLM 的 reviewer 词义强，但对跨仓读者不够直接 |
| `promotion 必须依赖的 authority` | 至少一条 ladder 需显式 authority | 已满足 | 已满足 | 未显式写出 | CGen 在 promotion authority 这一项仍弱于蓝本目标 |

## 5. 仓库级判断

### `VLM_Bench`

- 强项：
  - `raw_release_ready / release_ready`、`consume_surface / evidence_only_audit_surface`、`authoritative_scale_out_cleared` 这些 pair 与 ladder 定义已经很强。
  - reviewer 实际上能读出 `dual truth`、authority split、active input 边界。
- 缺口：
  - 缺少 `Section 0`，导致 `dual truth`、`consume vs audit`、`legacy/explainer` 这些词义没有被提升成统一对象模型。
  - `task_status / lane_status / accepted` 等通用状态语义还没单独显式化。
- 审计判断：
  - 它是“业务边界很强、通用术语层偏隐式”的代表仓。

### `Cangjie`

- 强项：
  - boundary pairs 与 ladder 足够具体，promotion gate 和 continuation lane 边界清楚。
  - `P22 / P23 / Phase07 / Staging-Core / Staging-Full` 这些 repo-specific boundary 读起来是稳定的。
- 缺口：
  - 缺少显式的 `consume_surface / evidence_only_surface / legacy_history_surface` 语义层。
  - 缺少 `task_status / lane_status`、`passed / accepted / archived` 这类跨仓通用状态面。
- 审计判断：
  - 它是“repo-specific reviewer 词义强，但缺少跨仓通用语义桥接”的代表仓。

### `CGen`

- 强项：
  - 最早显式写出了 `planning_freeze_passed / execution_ready` 这一组关键 boundary。
  - reviewer gates 已能稳定压住“planning 通过不等于 execution ready”。
- 缺口：
  - `planning_freeze_passed / execution_ready` 还停留在 boundary pair，尚未进入 `State Semantics` 层。
  - 当前 rubric 没有显式写出 promotion authority 依赖。
  - `consume_surface / evidence_only_surface / legacy_history_surface` 也未显式建模。
- 审计判断：
  - 它是“主线 blocker 语义强，但模板要求的公共语义层尚未实例化”的代表仓。

## 6. 这类缺口是否真实影响项目

- 会影响人类可读性。
  - reviewer 能看懂当前仓库，但换仓时要重新猜“passed / hold / landed / ready”分别落在哪一层。
- 也会影响代理检索稳定性。
  - 当 `Section 0` 缺失时，代理更容易从 boundary pair 中局部抽词，而不是先绑定该仓库的对象模型和状态语义。
- 但它不会立刻推翻现有架构。
  - 当前三个实例仓的 rubric 仍然是“可用但未完全同构”，不是“不可用”。

## 7. 推荐推进顺序

1. 先保持蓝本模板为目标架构，不回退。
2. 用测试锁住蓝本 rubric template 的 `Section 0 + minimal requirements`。
3. 之后再按 repo-specific 风险顺序补实例仓：
   - 第一优先：`CGen`
     - 因为它已经有 `planning_freeze_passed / execution_ready`，最容易补齐成完整 state semantics。
   - 第二优先：`VLM_Bench`
     - 因为它已有最强的 dual truth / consume boundary，只差把隐式词义抬升成显式结构。
   - 第三优先：`Cangjie`
     - 因为它的 repo-specific boundary 已足够稳，风险更偏“跨仓迁移摩擦”，不是当前主线误判。

## 8. 不建议在本页之后立即做的事

- 不建议因为模板更完整，就立刻把三个实例仓 rubric 全部重写成同一套字面结构。
- 不建议把 repo-specific boundary pair 压扁成抽象术语，导致业务细节变弱。
- 不建议把这份审计当成 live truth；它只是迁移与对齐依据，不是项目当前状态页。

## 9. 下一步

- 蓝本侧：
  - 保留本页作为 `rubric semantics` 对齐基线。
  - 为 `domain_review_rubric_template.md` 补最小防回退测试。
  - 运行 `pytest -q tests/test_blueprint_agent_architecture_docs.py tests/test_cross_repo_rubric_semantics_compliance.py`，把四仓 rubric 同构检查从人工审计收成可重复执行的自动化检查。
- 实例仓侧：
  - 后续逐仓补 `Section 0`，但只做显式化，不改写既有 repo-specific reviewer truth。
