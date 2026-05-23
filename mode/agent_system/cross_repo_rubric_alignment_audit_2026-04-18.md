# Cross-Repo Rubric Alignment Audit

更新时间：`2026-04-18 UTC`

## 1. 范围

本页记录截至 `2026-04-18` 对以下四个仓库做的协作架构 / reviewer 语义面对照：

- `VLM_Bench`
- `Cangjie`
- `CGen`
- `harness`

它只回答一件事：蓝本和实例仓在“模式命名、恢复顺序、legacy 降级、`AGENT TEAM` capability 语义、rubric 骨架”上是否已经同构。

## 2. 对照矩阵

| surface | VLM_Bench | Cangjie | CGen | harness |
| --- | --- | --- | --- | --- |
| `Lightweight Soft Constraints` | yes | yes | yes | yes |
| `Collaboration Mode Matrix` naming | yes | yes | yes | yes |
| `AGENT TEAM Capability Matrix` naming | yes | yes | yes | yes |
| `Mode Boundary Rules` | yes | yes | yes | yes |
| README / architecture explainer demoted | yes | yes | yes | yes |
| execution routing uses `Collaboration Modes` language | yes | yes | yes | yes |
| prompts use `Resume-First` chain | yes | yes | yes | yes |
| `AGENT TEAM` treated as capability, not main mode | yes | yes | yes | yes |
| legacy / rolling history explicitly demoted | n/a | yes | yes | blueprint-only |
| rubric template includes `glossary / object model / state semantics` starter pack | repo instance | repo instance | repo instance | yes |

## 3. 当前结论

- 蓝本与三个实例仓在主协作模式命名上已无分叉。
- `AGENT TEAM` 已在四个仓库里统一降回 capability 语义，不再被写成主模式。
- `README`、rolling worklog 与 legacy 页面不再与 live truth 抢默认 resume 入口。
- 蓝本现在已经具备 `domain_review_rubric_template` 的最小公共骨架，后续实例仓只需要做 repo-specific instantiation，而不是自己再发明对象模型和状态语义结构。

## 4. 仍需持续防回退的点

- 实例仓的 `domain_review_rubric.v2.md` 仍然是 repo-specific 的，后续新增复杂术语时要继续保持 `term / authority / not_equal_to / consequence` 这组完整定义。
- 任何新加的 README、rolling worklog、legacy current-phase 页面都必须带 `resume_surface=false` 或等价降级语义。
- 若后续有人把 `多人 / 并行` 再写回主模式，必须视为架构回退，而不是普通文案问题。

## 5. 审计方式

本轮对照采用的是锚点匹配而不是业务状态审查，核对点包括：

- 主模式命名
- `AGENT TEAM` capability 语义
- README / legacy demotion
- `Resume-First` prompt 读序
- execution routing 标题与边界语言
- rubric 模板中的 `glossary / object model / state semantics` 骨架
