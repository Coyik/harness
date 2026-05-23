# Copilot Instructions

This file is a shim only. Do not treat it as a second ruleset, task log, project guide, or status snapshot.

## Standard Resume Order

Downstream repos should replace these paths with their repo-local actual paths:

1. `AGENTS.md`
2. `docs/status/current_committed_plan.md`
3. `docs/current_state.v2.md`
4. `docs/status/INDEX.md`
5. `docs/status/current_task_handoff.md`
6. Follow the `INDEX` pointer for task-specific authority / reports only when needed.
7. Read `docs/agent_system/execution_routing.md` only when mode routing, wake / anti-stall, or escalation rules are needed.

Authoritative blueprint surfaces live at:

- `mode/AGENTS.refactor.md`
- `mode/agent_system/execution_routing_template.md`
- `mode/status/current_committed_plan_template.md`
- `mode/current_state.v2.md`
- `mode/agent_system/status_index_template.md`
- `mode/agent_system/current_task_handoff_template.md`
- `mode/agent_system/agent_architecture_issue_ledger_template.md` when architecture feedback is needed; it is not a default resume surface.

Do not let rolling worklogs or legacy logs override `current_committed_plan`, `current_state`, or `current_task_handoff`.

Repo-local actual path wins. Downstream repos should replace these `mode/...` paths with their own actual locations.
