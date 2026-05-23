from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def read_text(*parts: str) -> str:
    return PROJECT_ROOT.joinpath(*parts).read_text(encoding="utf-8")


def test_agents_refactor_has_mode_and_soft_constraint_surfaces() -> None:
    text = read_text("mode", "AGENTS.refactor.md")
    assert "### 1.3 Lightweight Soft Constraints" in text
    assert "### 2.1 Collaboration Mode Matrix" in text
    assert "### 2.5 AGENT TEAM Capability Matrix" in text
    assert "### 2.8 Mode Boundary Rules" in text
    assert "默认全程使用中文" in text
    assert "先绑定绝对日期" in text
    assert "不得以未加限定的 live header" in text


def test_readme_is_demoted_and_uses_blueprint_source_paths() -> None:
    text = read_text("mode", "agent_system", "README.md")
    assert "`role`: `architecture_explainer`" in text
    assert "`resume_surface`: `false`" in text
    assert "`default_live_truth_in_downstream_repo`:" in text
    assert "`repo_local_blueprint_source`:" in text
    assert "mode/AGENTS.refactor.md" in text


def test_execution_routing_template_uses_collaboration_mode_language() -> None:
    text = read_text("mode", "agent_system", "execution_routing_template.md")
    assert "# Execution Routing / Collaboration Modes Template" in text
    assert "## 2. Collaboration Mode Routing" in text
    assert "Reviewer + Planner / Executor" in text
    assert "## 3. Mode Boundaries And AGENT TEAM Capability" in text


def test_prompts_share_resume_first_chain() -> None:
    expected_chain = [
        "current_committed_plan",
        "current_state",
        "status_index",
        "current_task_handoff",
    ]
    for relative_path in [
        ("mode", "agent_system", "prompts", "planner_reviewer.md"),
        ("mode", "agent_system", "prompts", "executor.md"),
        ("mode", "agent_system", "prompts", "conductor.md"),
    ]:
        text = read_text(*relative_path)
        indices = [text.index(item) for item in expected_chain]
        assert indices == sorted(indices)
        assert "全程使用中文" in text
        assert "不是默认真值面" in text
        assert "先绑定绝对日期" in text


def test_executor_uses_agent_team_as_capability_only() -> None:
    text = read_text("mode", "agent_system", "prompts", "executor.md")
    assert "AGENT TEAM Matrix" not in text
    assert "AGENT TEAM Working Flow" not in text
    assert "`AGENT TEAM` 只是条件化协作能力" in text


def test_mapping_checklist_and_freeze_are_aligned() -> None:
    mapping = read_text("mode", "agent_system", "blueprint_migration_mapping.md")
    checklist = read_text("mode", "agent_system", "migration_checklist.md")
    freeze = read_text("mode", "agent_system", "blueprint_runtime_alignment_freeze_2026-04-16.md")

    assert "Reviewer + Planner / Executor" in mapping
    assert "AGENT TEAM capability" in mapping
    assert "resume_surface=false" in mapping
    assert "AGENT TEAM` 降回 capability" in checklist or "AGENT TEAM` 降回 capability" in checklist.replace("`", "")
    assert "Resume-First" in checklist
    assert "README / rolling worklog / legacy 页面" in checklist
    assert "docs/status/current_committed_plan.md -> docs/current_state.v2.md -> docs/status/INDEX.md -> docs/status/current_task_handoff.md" in freeze
    assert "AGENT TEAM` 不是协作模式本身" in freeze or "AGENT TEAM 不是协作模式本身" in freeze
    assert "resume_surface=false" in freeze


def test_domain_review_rubric_template_has_semantics_layer_and_minimum_requirements() -> None:
    text = read_text("mode", "agent_system", "domain_review_rubric_template.md")

    assert "## 0. Glossary / Object Model / State Semantics" in text
    assert "`consume_surface / evidence_only_surface / legacy_history_surface`" in text
    assert "`task_status / lane_status`" in text
    assert "`passed / accepted / archived`" in text
    assert "`planning_freeze_passed / execution_ready`" in text
    assert "`raw_truth / effective_truth / reviewer_truth`" in text
    assert "promotion 必须依赖的 authority" in text
    assert "## 最小落地要求" in text
    assert "至少 `3` 个 repo-specific canonical terms 已定义。" in text
