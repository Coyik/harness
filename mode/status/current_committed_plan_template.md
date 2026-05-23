# Current Committed Plan Template

这个文件承载“当前唯一已批准执行步”。
它不是 backlog，不是路线图，也不是 task handoff。
正文字段必须严格固定为下面六项，不得额外增删 key。

## 固定结构

```markdown
# Current Committed Plan

- `approved_on`：
- `approved_by`：
- `current_step`：
- `why_this_step`：
- `do_not_do_now`：
- `exit_condition`：
```

## 维护规则

- 只有在当前批准执行步被明确批准、替换或撤销时才更新。
- 默认恢复首链为 `AGENTS.md -> current_committed_plan -> current_state -> INDEX -> current_task_handoff`；本文件是读完 `AGENTS.md` 后的第一份结构化状态面。
- 若执行方向变化，先更新本文件，再同步 `current_task_handoff` 与 `status_index`。
- 本文件只描述当前这一步，不承担长期恢复顺序；长期路线写在 `execution_routing`。
- repo-local actual path wins；在这个模板仓库里，实际路径是 `mode/status/current_committed_plan_template.md`。

## 不该放进来什么

- 额外字段
- 多步 backlog
- 默认恢复顺序
- task 级 checkpoint
- 报告正文
