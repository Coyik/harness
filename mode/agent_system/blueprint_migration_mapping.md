# Blueprint Migration Mapping

更新时间：`2026-04-18`

## 1. 目的与冻结边界

本文件是 `harness` agent-system 重构进入实施前的冻结映射表。

它回答三个问题：

- 旧承载面中的高价值信息，应该迁到哪一层
- 哪些内容只能归档或丢弃，不能继续回灌
- 后续实施如何证明“信息没丢、入口更短、没有制造第二真值层”

本文件不是：

- 逐文件 diff 清单
- run 级日志归档
- 项目业务状态页
- 替代 `AGENTS.md`、`current_state`、`status_index` 的第二真值层

冻结边界：

- 当前只冻结蓝本迁移规则，不直接修改 `harness` 以外项目的业务状态
- 当前只定义 canonical target，不定义具体逐行 patch
- 当前只允许把旧信息归位到正确承载层，不允许借迁移回退到“单巨型 AGENTS”

## 2. 源面清点原则

### 2.1 迁移优先级

1. 保住高价值规则与 repo-local 稳定知识
2. 修复 resume / navigation / status wiring 缺口
3. 统一 prompt 的读序与输出契约
4. 最后才删除旧入口或旧冗余段落

### 2.2 源面处理动作

- `keep`
  - 原承载层正确，保留并轻量收口
- `split`
  - 一段内容混有多层信息，拆到多个承载层
- `rewrite`
  - 语义应保留，但旧写法已与新架构冲突
- `create`
  - 目标承载面目前不存在，必须先补
- `drop`
  - 明确不应迁移，直接丢弃或归档
- `escalate`
  - 触及安全、错误 repo 边界、或 authority 冲突，先升级再处理

补充规则：

- 若旧页面仍保留历史追溯价值，但不应继续作为默认入口，必须显式标成 `archived-to` 或 `legacy_history_surface`，而不是继续保留未加限定的 live header。
- 若旧协作说明仍把 `AGENT TEAM` 写成主模式，必须改写为 capability 语义；不得继续把“用户提到多人 / 并行”当成自动全面并行。

### 2.3 P0 高价值锚点

以下锚点在迁移后必须保持 `0 丢失 + 0 多归属`：

- 热区读取顺序与 resume-first 规则
- 证据纪律与 narrative red lines
- reviewer / executor / `Reviewer + Planner / Executor` / `AGENT TEAM capability` 角色边界
- 层级分工：`AGENTS / current_state / runtime_contract / domain_review_rubric / current_task_handoff / status_index`
- task 生命周期与 `passed != accepted != archived`
- repo-local reviewer gate 与 authority split
- tool shim / path-scoped 规则的归位原则

## 3. Canonical Mapping Matrix

| legacy_source | source_anchor | content_class | current_problem | new_surface | migration_action | discard_condition | acceptance_criteria | owner | priority | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 旧 `AGENTS` / 现 `AGENTS` | `Session Header` | 项目入口 headline | 容易混入 task 级动态状态 | `AGENTS.md` | `rewrite` | 若含 run 级细节或 exact artifact 洪水则移出 | 只保留项目 / 阶段 / active lane / blocker / 当前状态页 / 默认续接入口 / allowed move | planner | P0 | 下游仓实例化后应保持同一高密度 headline 形状 |
| 旧 `AGENTS` / 现 `AGENTS` | `Navigation Surface` | canonical 入口图 | 若缺失，resume 首跳会退回人工读长文 | `AGENTS.md` | `create` | 不得退化成文件总目录 | 至少包含 `current_state`、`runtime_contract`、`domain_review_rubric`、`current_task_handoff`、`status_index` 及 fallback | planner | P0 | 这是 clean-context 续接的首要缺口 |
| 旧 `AGENTS` / 现 `AGENTS` | `Hard Rules` / `Git 宪法` | 跨任务稳定规则 | 旧版夹带项目态与进化日志 | `AGENTS.md` | `split` | 任务进度、run 细节不得继续留顶层 | 只保留跨任务规则、证据纪律、Git 授权、层级纪律 | planner | P0 | 高价值规则必须保留 |
| 旧 `AGENTS` / prompts | `Mode Routing` / 角色边界 | 协作骨架 | prompt 与蓝本读序不一致，且旧命名容易把 `AGENT TEAM` 写成主模式 | `AGENTS.md` + `prompts/*.md` | `split` | 若角色视角不稳定则不得放入顶层 | 模式读序与角色提示一致；显式收口为 `Debate`、`Reviewer + Planner / Executor`、`Conductor`、`单窗口执行`，且 `AGENT TEAM` 只保留为 capability | planner | P0 | prompts 不得再残留旧 routing labels 或自动并行口径 |
| 旧 `AGENTS` / 状态页段落 | `active lane` / `blocker` / `allowed moves` | 项目快照 | 常与 task 状态混写 | `docs/current_state.v2.md` | `rewrite` | 不得带 task 返工细节 | 只保留项目级当前快照、非目标、待决项 | implementer | P0 | `VLM_Bench` 当前该层过载明显 |
| 旧 `AGENTS` / repo 文档 | `entrypoints` / `env` / `consume boundary` / `fail-closed` / `failure taxonomy` | 运行合同 | 常被塞进 AGENTS 或 handoff | `docs/runtime_contract.v2.md` | `split` | 若只是 reviewer 词义，不得写进 runtime | 运行入口、合同边界、失败分类唯一归位 | implementer | P1 | 当前蓝本模板已具备，但项目迁移不整齐 |
| 旧 `AGENTS` / reviewer 说明 / 当前 rubric | `repo-local 词义` / `promotion ladder` / `narrative traps` | reviewer gate | glossary / object model / state semantics 尚未模板化 | `docs/domain_review_rubric.v2.md` + `domain_review_rubric_template.md` | `rewrite` | 抽象方法论不应回灌这里 | 每个词义都包含“定义 / 还不算 / 常见混淆 / 判错后果” | reviewer | P0 | 必须新增 `glossary/object model/state semantics` |
| 蓝本缺口 | `raw/effective/reviewer truth`、`task status vs lane status`、`Gate A/B/C` 等 | 状态语义 | 目前常回流到 `current_state` / `handoff` | `domain_review_rubric_template.md` | `create` | 若 repo 无此类复杂术语，可留最小占位 | 模板支持 repo-specific 状态语义，不再挤占其他层 | reviewer | P0 | 这是术语混写的主因之一 |
| 旧 `AGENTS` / task 状态文案 | `task slice` / `done_when` / `next start` / `proof snapshot` | 当前 task 持续态 | 常被状态页或 AGENTS 吞掉 | `docs/status/current_task_handoff.md` | `rewrite` | 项目级 blocker 不得整段复制到 handoff | 具备 `lane`、`Why This Task Exists`、`Proof Snapshot`、生命周期状态 | implementer | P1 | `CGen/Cangjie` 也应补齐模板字段 |
| 旧长文 / README / 报告入口 | `default resume` / `latest_report` / `raw_log_root` / `archive` / `path-scoped resume` | 索引导航 | 历史面、解释面、模板面容易与真值层抢入口 | `docs/status/INDEX.md` | `create` | 不得塞正文，不得复制 task 细节 | 能回答“当前默认从哪续接、为什么、失效后去哪”；`README` / rolling worklog / legacy 页面都必须显式降级为 `resume_surface=false` | implementer | P0 | `status_index` 是蓝本必需层，不是可选附加件 |
| 旧 `AGENTS` / tool-specific 文件 | `path-scoped rules` / `shim-only entrypoints` | 局部规则 | 现易散落或与顶层冲突 | path-scoped docs / 工具 shim | `split` | 若仅是旧工具残影且无实际价值，归档 | shim 只做导向，不制造第二套宪法 | planner | P1 | `CLAUDE/GEMINI/copilot` 只应做薄 shim |
| 旧 `AGENTS` / evolution log / 周报 | `长 why-not` / `exact run` / 命令输出 | 历史与证据 | 噪声高、易被误读为当前真相 | `docs/reports/*` / `docs/status/*` / archive | `split` | 若仅剩重复噪声，可丢弃 | 当前层文档不再承载长日志；索引能回跳到历史 | analyst | P1 | 历史追溯路径不得替代当前执行路径 |
| `AGENTS copy.md` 等 legacy 文档 | 明文 key / 错仓路径 / 旧“唯一 SSOT + 强制进化日志”口径 | 安全污染 / 错误作用域 | 不能继续作为迁移内容 | security incident + archive note | `drop` 或 `escalate` | 永不迁回新架构 | 敏感信息单独隔离；错误 repo 内容不再出现在新入口 | reviewer | P0 | `VLM_Bench/AGENTS copy.md` 是显式安全事件 |
| 现有 prompts | “最近20条进化日志” / 旧读序 / 缺少语言和日期守卫 | 过时读序 | 与 `Resume-First`、轻量软约束和真值层分工冲突 | `prompts/{planner_reviewer,executor,conductor}.md` | `rewrite` | 若角色无该读取需求，不得保留 | 首跳改为 `AGENTS -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`；并补 `中文默认`、`绝对日期绑定`、`README/legacy 非真值面` | planner | P0 | 读序不改，导航层就会失效 |

## 4. Missing Surface Register

| missing_target_surface | where_missing_now | required_action | why_it_blocks_migration | owner | priority |
| --- | --- | --- | --- | --- | --- |
| `repo-specific instantiation of glossary/object model/state semantics` | 下游项目 `domain_review_rubric.v2.md` | 基于已补齐的 blueprint 模板在复杂仓库落地实例 | 若只停在模板层，术语仍会回流到 `current_state/handoff` | reviewer | P0 |
| `discard policy` | `AGENTS` / 迁移文档 | 明确 `mapped-to / archived-to / discarded-because / escalated-because` | 假迁移时最容易把旧噪声带回 | reviewer | P0 |
| prompt read-path parity | `planner_reviewer/executor/conductor` | 统一读序、输出收口与轻量软约束 | 文件存在但模型不读，形成假迁移 | planner | P0 |
| `legacy_history_surface` demotion language | `rolling worklog / current-phase / README` | 统一 `resume_surface=false`、`superseded_by` 与历史字段改写规则 | 历史面会继续和 live truth 抢入口 | planner | P0 |
| `AGENT TEAM capability` naming parity | `AGENTS` / prompts / `execution_routing` | 统一从 mode 级命名到 prompt 级边界 | 下游容易从蓝本学回旧“并行=主模式” | planner | P0 |
| `Why This Task Exists` / `Proof Snapshot` / lifecycle 字段 | 多项目 `current_task_handoff` | 对齐模板字段 | task 态与项目态继续混写 | implementer | P1 |

## 5. Project Migration Register

| project | current_state | key_gap | pilot_role | minimum_target |
| --- | --- | --- | --- | --- |
| `harness` | blueprint source | 需保证 mapping / checklist / freeze 与蓝本骨架同构 | blueprint owner | 完成模板、prompt、checklist、mapping、freeze 五面冻结 |
| `VLM_Bench` | 已完成首轮 structural pilot | 需维持与蓝本同构，防止后续 drift | first structural pilot | 持续保持 `AGENTS + current_state + runtime_contract + domain_review_rubric + current_task_handoff + status_index` 六件套闭环 |
| `CGen` | 已完成 prompt / README / routing / rolling worklog 对齐 | 需维持 `claude.md` 的历史语义降级不回退 | reference repo | 保持现有结构，只做增量 parity 检查 |
| `Cangjie` | 已完成 prompt / README / routing / legacy current-phase 对齐 | 需维持 lifecycle 与 legacy demotion 不回退 | alignment repo | 保持现有结构，只做增量 parity 检查 |

## 6. Discard And Escalation Rules

### 6.1 必须保留并映射

- 热区读取顺序
- 证据纪律与 narrative red lines
- reviewer / executor / `Reviewer + Planner / Executor` / `AGENT TEAM capability` 边界
- Git 授权与风险提示规则
- repo-local 稳定知识
- 状态层 / task 层 / 索引层的边界

### 6.2 必须迁出归档

- 长 why-not 报告
- run 级 exact artifact 细节
- 历史阶段的长演化日志
- 仅用于追历史的旧 handoff

### 6.3 必须直接丢弃或升级

- 明文密钥、token、cookie
- 错仓路径或错误 repo 作用域
- 旧“唯一 SSOT + 强制进化日志”口径
- 会制造第二真值层的重复入口

### 6.4 升级触发条件

出现以下任一项，迁移不得继续推进，必须先升级：

- 任一 P0 高价值锚点未找到唯一归属
- `Navigation Surface` 或 `status_index` 缺失却计划删除旧入口
- 发现新的明文凭据或错误 repo 内容
- 新文档把 partial / baseline / preview / close-ready evidence 误写为正式放行
- 迁移后出现多套 `current task` 或多套 canonical entrypoint
- README / rolling worklog / legacy 页面重新被抬升为默认 resume 首跳

## 7. 验收与风险骨架

### 7.1 Anchor Preservation Table

| source_anchor | target_carrier | why_high_value | pass_rule | check_method | loss_risk | owner | abort_if_missing |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 热区读取顺序 | `AGENTS` + prompts + `status_index` | 决定 clean-context 续接效率 | `0` 丢失、`0` 多归属 | blind resume dry-run | 首跳变长 | planner | yes |
| 证据纪律 | `AGENTS` + reviewer prompt | 防止乐观外推 | 所有核心 red lines 仍可在首层定位 | 逐条核对 | narrative drift | reviewer | yes |
| repo-local 词义 | `domain_review_rubric` | 防止术语混写 | 每个 canonical pair 都有“还不算” | 抽样审查 | gate 误判 | reviewer | yes |
| task 生命周期 | `current_task_handoff` + `status_index` | 防止 `passed`/`accepted` 混写 | 状态语义唯一 | 生命周期核对 | resume 误判 | implementer | yes |
| tool shim 治理 | path-scoped docs / shim | 防止多套宪法 | shim 只导向，不自立规则 | 入口检查 | duplicate truth | planner | yes |
| legacy / explain surfaces demotion | `README` / rolling worklog / legacy current-phase | 防止历史面抢入口 | 均带 `resume_surface=false` 或等价语义，且指向 live truth | 抽样读取 | live-truth drift | planner | yes |

### 7.2 量化基线

- 首跳基线
  - `before_path`：`AGENTS -> current_state -> runtime_contract -> domain_review_rubric -> current_task_handoff`
  - `before_hops`：`5`
  - `before_tokens`：实施前记录
- 目标态
  - `after_path`：`AGENTS -> current_committed_plan -> current_state -> status_index -> current_task_handoff`
  - `after_hops`：默认 `<= 3` 个 artifact 内定位当前默认续接面
  - `after_tokens`：较实施前下降 `>= 30%`
- 术语治理
  - `canonical_pair`：由 `domain_review_rubric` 维护
  - `forbidden_mix`：由 `domain_review_rubric` 维护
  - `baseline_mix_rate`：实施前记录
  - `target_mix_rate`：较实施前下降 `>= 50%`

### 7.3 实施后基线指标

- `resume_hops`
- `resume_token_budget`
- `time_to_current_task`
- `mixed_write_rate`
- `unmapped_anchor_count`
- `duplicate_truth_entrypoints`
- `shim_only_entrypoints`

## 8. 最终验收口径

迁移映射表通过，必须同时满足：

1. 所有 P0 高价值锚点都已唯一归位
2. 所有 `create` 类缺口都已在 blueprint 或目标项目中显式补齐
3. 所有 `drop/escalate` 项都有去向，不存在“先删后想”
4. 不需要依赖长报告正文，也能回答“当前从哪继续”
5. 新增的 `mapping` / `checklist` / `status_index` 不构成第二真值层
