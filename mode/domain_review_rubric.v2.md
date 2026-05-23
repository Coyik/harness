# Domain Review Rubric v2

更新时间：`YYYY-MM-DD`

本文件是蓝本仓库的 reviewer 词义与 gate 占位面。
下游新项目必须把它实例化为该仓库自己的 `docs/domain_review_rubric.v2.md`，不得保留其它项目的术语、promotion ladder、gate truth 或 artifact 路径。

## 0. Glossary / Object Model / State Semantics

### Repo-specific canonical terms

#### `canonical_term`

- object / scope：
- canonical meaning：
- authority or anchor：
- not_equal_to：
- reviewer consequence：

### Recommended starter pack

#### `task / lane / checkpoint / authority_surface`

- `task` means：
- `lane` means：
- `checkpoint` means：
- `authority_surface` means：
- not_equal_to：
- reviewer consequence：

#### `consume_surface / evidence_only_surface / legacy_history_surface`

- `consume_surface` means：
- `evidence_only_surface` means：
- `legacy_history_surface` means：
- resume semantics：
- not_equal_to：
- reviewer consequence：

#### `passed / accepted / archived`

- `passed` means：task 级 `done_when` 已满足；不等于项目级 blocker 消失。
- `accepted` means：该 task 已正式吸收到当前状态面；不再作为默认续接面。
- `archived` means：只保留追溯价值；只能通过 `status_index` / archive 读取。
- not_equal_to：
- reviewer consequence：

## 1. Canonical Boundary Pairs

### `A / B`

- 一句话定义：
- 正证据长什么样：
- 什么还不足以支持这个判断：
- 最常见混淆：
- 判错后果：

### `planning_freeze_passed / execution_ready`

- 一句话定义：
- 正证据长什么样：
- 什么还不足以支持这个判断：
- 最常见混淆：
- 判错后果：

### `raw_truth / effective_truth / reviewer_truth`

- 一句话定义：
- 正证据长什么样：
- 什么还不足以支持这个判断：
- 最常见混淆：
- 判错后果：

## 2. Promotion Ladder

### `exploratory`

- 进入条件：
- 还不够进入下一层的伪证据：
- 对下游意味着什么：

### `bounded_smoke_passed`

- 进入条件：
- 常见误写：
- 对下游意味着什么：

### `review_ready`

- 进入条件：
- 常见误写：
- 对下游意味着什么：

### `authoritative_cleared`

- 进入条件：
- promotion 必须依赖的 authority：
- 对下游意味着什么：

## 3. Reviewer Gates

- 一票否决型 blocker：
  - 任何把 evidence-only surface 写成 active runtime input 的叙事。
  - 任何把 preview / smoke / baseline / partial result 提升为正式 reviewer 放行的叙事。
  - 任何在 authority surface 未变化时抬高 gate truth 的动作。
- 可后置但必须显式说明的风险：
  - 当前验证未覆盖的主要风险面。
  - 下游 consumer 仍需自行拼装的缺口。
- 只影响叙述质量、不影响主线推进的问题：
  - 便利性 memo 或说明文档，只要不自称 canonical entrypoint。

## 4. Common Narrative Traps

- 把 task passed 写成 lane promoted。
- 把 baseline / compare / preview / smoke 写成正式 reviewer 放行。
- 把部分落盘 / 初步可读 artifact 写成 fully closed。
- 把 legacy history surface 写成当前真值。
- 把 current task handoff 写成 repo 级 allowed moves。

## 5. Common Failure Modes

- 词义混写：
- 证据错位：
- runtime boundary 漂移：
- 当前主线与旧路线混写：
- failure taxonomy 塌缩：

## 更新规则

只有当仓库特有词义、阶段定义、promotion ladder 或 reviewer gate 真正变化时才更新本文件。
详细骨架见 `mode/agent_system/domain_review_rubric_template.md`。
