# Task Handoff Template

此文件保留为兼容别名。

正式拆分后的模板位于：

- `current_task_handoff_template.md`
- `execution_routing_template.md`
- `mode/status/current_committed_plan_template.md`

迁移原因：

- 让 `current_task_handoff` 只承载 task 状态
- 把长期执行路线迁到 `execution_routing`
- 把当前批准执行步迁到 `current_committed_plan`
- 避免 `task_handoff` 这个泛称继续吞掉 routing / wake / anti-stall

若继续维护这套架构，默认请使用：

- `current_task_handoff_template.md`
- `execution_routing_template.md`
- `mode/status/current_committed_plan_template.md`
