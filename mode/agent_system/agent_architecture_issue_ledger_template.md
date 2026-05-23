# Agent Architecture Issue Ledger Template

这个文件承载“架构问题账本”。
它用来记录可重复观察的路由失配、层级漂移、承载面缺口与后续重构触发条件。
它不是默认恢复入口，不是项目真值层，也不承载当前 task 的执行细节。

## 推荐结构

```markdown
# Agent Architecture Issue Ledger

更新时间：`YYYY-MM-DD`
状态：`append-only`
角色：`architecture issue ledger`

## Purpose

- 保留架构问题的持续证据
- 让重复出现的偏差有统一落点
- 为后续重构触发条件提供可追踪依据

## Non-Goals

- 不是默认 resume surface
- 不是项目真值层
- 不覆写 `AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`
- 不承载当前任务的执行细节
- 不承载长周报、命令输出洪水或一次性返工叙事

## Current Open Issues

### 1. short title

- trigger：
- observed gap：
- evidence：
- impact：
- mitigation：
- status：`open | monitoring | mitigated | redesign_candidate`

## Redesign Triggers

- 同类路由失配在多个 task 中重复出现
- 某条补充路线从设计备忘变成可执行实现面
- 默认恢复链长期无法定位用户实际要求的 continuation lane
- 架构反馈条目开始累积到需要独立分流、分类或归档

## Feedback Append Protocol

新增反馈只追加，不覆盖历史判断。

### YYYY-MM-DD - short title

- trigger：
- observed gap：
- evidence：
- impact：
- mitigation：
- status：`open | monitoring | mitigated | redesign_candidate`
```

## 使用原则

- 只记录架构层问题，不记录普通 bug 或 task 进度。
- 每条记录必须指向证据面，例如 `AGENTS.md`、`current_committed_plan`、`current_state`、`status_index`、`current_task_handoff`、`execution_routing`、report 或 artifact。
- 若需要更正旧判断，优先追加一条更正记录，不回头重写旧条目。
- 每条记录尽量短，只保留足以支持后续判断的证据锚点。

## 什么时候更新

- 用户目标与默认恢复链反复错位。
- routing / handoff / status index 出现同类冲突。
- 某个能力从“设计 note”变成“可执行实现面”，需要重新评估路由。
- 发现顶层宪法正在吸收本该落到局部规则、task handoff、runtime contract 或 archive 的内容。

## 不该放进来什么

- 当前 task 的逐步执行记录
- 当前批准计划六字段正文
- 项目级 active lane / blocker / allowed moves
- 长报告正文
- 全量命令输出
- 明文密钥、token 或凭据
