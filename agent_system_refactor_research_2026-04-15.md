# Agent System Refactor Research Notes

更新时间：`2026-04-15`
用途：给本轮 agent system 重构提供外部写法依据，避免只靠本地直觉改文档。

## 1. 研究问题

这轮需要回答的不是“别人有没有 `AGENTS.md`”，而是：

1. 主流 agent tooling 如何承载仓库级规则
2. 是否支持继续拆分到路径级 / 主题级规则
3. 任务级动态变量通常该写在哪里
4. 优秀的公共示例更像“短口号”还是“repo-specific 可执行规则”

## 2. 冻结来源

### Anthropic Claude Code Memory

- 来源：<https://docs.anthropic.com/en/docs/claude-code/memory>
- 访问日期：`2026-04-15`
- 用途：确认官方如何建议组织项目级指令与路径级规则
- 关键结论：
  - `CLAUDE.md` 是项目记忆入口
  - 鼓励在子目录放 path-specific memory
  - 官方建议 instructions 要具体、简洁、可执行；单文件过大时继续拆分

### GitHub Copilot Custom Instructions

- 来源：<https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot>
- 访问日期：`2026-04-15`
- 用途：确认另一套主流 tooling 如何区分仓库级、路径级、agent级指令
- 关键结论：
  - GitHub 区分 repository custom instructions、path-specific instructions、agent-specific instructions
  - 说明“顶层一份大文档解决一切”不是主流共识

### OpenAI Codex `AGENTS.md`

- 来源：<https://raw.githubusercontent.com/openai/codex/main/AGENTS.md>
- 访问日期：`2026-04-15`
- 用途：看公开仓库中的 `AGENTS.md` 实际长什么样
- 关键结论：
  - 内容非常 repo-specific
  - 强调目录结构、构建命令、测试规则、前后端约束
  - 风格不是“概念宣言”，而是能直接指导代理做事的操作约束

### Google Gemini CLI `GEMINI.md`

- 来源：<https://raw.githubusercontent.com/google-gemini/gemini-cli/main/GEMINI.md>
- 访问日期：`2026-04-15`
- 用途：确认另一种项目入口文件的典型写法
- 关键结论：
  - 同样采用 repo-specific 规则、命令和行为边界
  - 说明不同工具入口文件并存是常态

### AGENTS.md 标准站点

- 来源：<https://agents.md/>
- 访问日期：`2026-04-15`
- 用途：确认社区层面对 `AGENTS.md` 的定位
- 关键结论：
  - 核心目标是给 coding agents 一致的、可发现的仓库说明入口
  - 强调开放格式和可组合性

### Apache Airflow `AGENTS.md`

- 来源：<https://raw.githubusercontent.com/apache/airflow/main/AGENTS.md>
- 访问日期：`2026-04-15`
- 用途：观察较成熟开源仓库怎么写 agent instructions
- 关键结论：
  - 依然是 repo-specific、命令导向、流程导向
  - 不追求“极短”，而是追求“能直接指导执行”

## 3. 外部共识提炼

从这些来源里，能稳定提炼出四条共识：

1. 顶层规则文件必须存在，但不应该承担全部上下文
2. 路径级 / 主题级规则继续拆分，是主流做法
3. 文件内容必须偏 repo-specific、偏执行约束，而不是抽象口号
4. 工具特定入口可以并存，但应尽量指向同一套核心事实

## 4. 对本地蓝本的直接含义

这意味着当前蓝本不能只满足“有 `AGENTS.refactor.md` + 几个 prompt 文件”。

还必须满足：

1. `current_state`、`runtime_contract`、`domain_review_rubric` 不是标题，而是结构化 schema
2. 要有专门承接 task 级持续状态的承载面，不再把这部分塞回顶层 `AGENTS`
3. `Conductor` 和 `Debate` 角色模板必须写到足够可执行，而不是留在摘要级
4. 若未来某个子目录有自己独立稳定规则，应继续拆 path-scoped 文档，而不是顶层继续膨胀

## 5. 与本地图片方法论的对齐

外部资料解决的是“别人怎么分层”。
本地图片补的是“这套系统究竟怎样高质量推进问题与落地”。

两者结合后的结论是：

- 顶层文档应该继续分层
- 但不能因为分层而把 `Debate` 的 Layer 2 底层定义删掉
- 也不能因为分层而把 `Conductor` 的增量 task 闭环删掉
- `task_handoff` / clean-context 续接是这轮本地蓝本必须补上的缺口

## 6. 当前建议

本轮蓝本应重点补强：

- `README.md`
- `architecture_explained.md`
- `current_state_template.md`
- `runtime_contract_template.md`
- `domain_review_rubric_template.md`
- `window_init_template.md`
- `task_handoff_template.md`
- `prompts/conductor.md`
- `prompts/debate_*.md`

而不是继续只围绕 `planner_reviewer.md` 和 `executor.md` 微调。
