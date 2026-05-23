# Runtime Contract v2

更新时间：`YYYY-MM-DD`

本文件是蓝本仓库的运行合同占位面。
下游新项目必须把它实例化为该仓库自己的 `docs/runtime_contract.v2.md`，不得保留其它项目的命令、环境变量、模型配置、artifact 路径或 failure taxonomy。

## 1. Canonical Entrypoints

- 主入口命令：
- 辅助入口命令：
- 不再推荐的旧入口：

## 2. Required Inputs

- 必需输入文件 / manifest：
- 必需目录结构：
- 输入前置校验：

## 3. Required Environment

- 必需 env：
- 必需 PATH / toolchain：
- 缺失时的失败信号：
- 凭据处理规则：不得写入 `AGENTS.md`、日志、runbook 或状态页；只引用环境变量名。

## 4. Runtime Boundary

- 明确会消费的字段 / 路径：
- 明确不会消费的字段 / 路径：
- 哪些只是 evidence-only，不是 runtime blocker：
- 哪些 override 必须 fail-closed：

## 5. Verification Ladder

- 最小 smoke：
- 有代表性的 bounded verification：
- 必做回归：
- 通过标准：

## 6. Consumer-Facing Outputs

- 产物路径：
- 字段级合同：
- 下游可依赖的最小面：
- 不可被下游依赖的临时 / debug 输出：

## 7. Failure Taxonomy And Escalation

- 输入 / 合同漂移：
- provider / 外部依赖失败：
- runtime / harness 失败：
- synthesis / contract 失败：
- 哪些可以本地重试：
- 哪些必须升级给 reviewer / 用户：

## 更新规则

只有当运行入口、必需环境、runtime boundary、consume boundary、smoke gate 或 failure taxonomy 变化时才更新本文件。
详细骨架见 `mode/agent_system/runtime_contract_template.md`。
