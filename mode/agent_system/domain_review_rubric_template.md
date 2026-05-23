# Domain Review Rubric Template

这个文件承载“仓库特有的审查词表、对象模型、状态语义与 reviewer gate”。
它不是通用角色模板，也不是战略周报。

## 推荐结构

```markdown
# Domain Review Rubric

更新时间：`YYYY-MM-DD`

## 0. Glossary / Object Model / State Semantics

### Repo-specific canonical terms

#### `canonical_term`

- object / scope：
- canonical meaning：
- authority or anchor：
- not_equal_to：
- reviewer consequence：

### Recommended starter pack

以下几类如果在仓库里存在，就必须显式定义，而不是留给审查者脑补：

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

### Object model

#### `object_name`

- lifecycle / ownership：
- canonical role：
- visible to whom：
- not_equal_to：
- reviewer consequence：

### State semantics

#### `task_status / lane_status`

- `task_status` means：
- `lane_status` means：
- not_equal_to：
- reviewer consequence：

#### `passed / accepted / archived`

- `passed` means：
- `accepted` means：
- `archived` means：
- not_equal_to：
- reviewer consequence：

#### `planning_freeze_passed / execution_ready`

- `planning_freeze_passed` means：
- `execution_ready` means：
- not_equal_to：
- reviewer consequence：

#### `raw_truth / effective_truth / reviewer_truth`

- `raw_truth` means：
- `effective_truth` means：
- `reviewer_truth` means：
- not_equal_to：
- reviewer consequence：

## 1. Canonical Boundary Pairs

### `A / B`

- 一句话定义：
- 正证据长什么样：
- 什么还不足以支持这个判断：
- 最常见混淆：
- 判错后果：

### `consume_surface / evidence_only_surface`

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

## 2. Promotion Ladder

### `exploratory`

- 进入条件：
- 还不够进入下一层的伪证据：
- 对下游意味着什么：

### `landed` 或 repo-local 等价层

- 进入条件：
- 常见误写：
- 对下游意味着什么：

### `mechanical-ready`

- 进入条件：
- 常见误写：
- 对下游意味着什么：

### `live`

- 进入条件：
- 还不够构成 live 的证据：
- 对下游意味着什么：

### `promoted`

- 进入条件：
- promotion 必须依赖的 authority：
- 对下游意味着什么：

## 3. Reviewer Gates

- 一票否决型 blocker：
- 可后置但必须显式说明的风险：
- 只影响叙述质量、不影响主线推进的问题：

## 4. Common Narrative Traps

- 把局部结果误写成阶段闭合：
- 把 evidence-only artifact 误写成 consumer contract：
- 把 baseline / compare / smoke 误写成正式放行：
- 把 partial handoff 误写成 downstream-ready：
- 把历史页面或解释页重新抬升成 live truth：

## 5. Common Failure Modes

- 词义混写：
- 证据错位：
- path / schema / runtime boundary 混写：
- 当前主线与旧路线混写：
- `task_status / lane_status / checkpoint_status` 混写：

## 6. Update Rules

- only_update_when：
- do_not_record_here：
- required_review_when_terms_change：
```

## 使用原则

- 仓库特有术语放这里，不放进通用 `planner` / `executor` 模板。
- 这层只放 repo-specific reviewer 词义、object model、state semantics、boundary 与 gate。
- 这里可以定义 `task status vs lane status`、`passed / accepted / archived`、`planning_freeze_passed / execution_ready`、`raw / effective / reviewer truth` 这类语义，但不记录当前 run / task / project 的动态状态值。
- 它不替代 `runtime_contract`、`task_handoff` 或 `project snapshot` 一类状态文档。
- 每个 canonical term 都要同时写清：
  - 它是什么
  - 它不等于什么
  - 它依赖哪个 authority
  - 判错之后会误导哪一层
- 每个 boundary pair 都必须写“什么还不足以支持这个判断”，否则模板不算闭合。
- 若仓库保留 README、rolling worklog、legacy `current-phase` 一类历史 / 解释页面，这里必须显式写清它们不是 live truth，必要时给出 `legacy_history_surface` 定义。
- reviewer gate 要能直接用于判 blocker / 非 blocker，而不是只给抽象定义。

## 最小落地要求

如果一个仓库要声称自己已经完成了 rubric 落地，至少要满足：

1. 至少 `3` 个 repo-specific canonical terms 已定义。
2. 至少 `2` 组 canonical boundary pairs 已定义，其中一组必须是 `consume_surface / evidence_only_surface` 或等价对。
3. 至少 `1` 条 promotion ladder 已写出明确 authority 依赖。
4. 至少 `1` 组 state semantics 已显式区分 `task_status / lane_status` 或 `passed / accepted / archived`。
5. 已写出至少 `3` 条 common narrative traps。

## 什么时候更新

只在仓库特有词义或 reviewer gate 真正变化时更新，例如：

- promotion ladder 的进入条件改变
- boundary pair 定义改变
- 某类误判已反复出现，需要成为稳定审查规则
- 某个 legacy / explain surface 被正式降级或重新定义

## 不该放进来什么

- 通用协作礼仪
- 单轮 task 过程
- 当前 run / task / lane / project snapshot 的动态状态值
- 长 why-not 报告
- 与词义 / gate 无关的运行参数
- 没有 authority anchor 的口头偏好
