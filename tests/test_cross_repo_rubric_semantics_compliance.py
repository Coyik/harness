from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


MY_PROJECTS_ROOT = Path(__file__).resolve().parents[2]


COMMON_SEMANTICS_ANCHORS = (
    "## 0. Glossary / Object Model / State Semantics",
    "`consume_surface / evidence_only_surface / legacy_history_surface`",
    "`task_status / lane_status`",
    "`passed / accepted / archived`",
    "`planning_freeze_passed / execution_ready`",
    "`raw_truth / effective_truth / reviewer_truth`",
    "promotion 必须依赖的 authority",
    "## 6. Update Rules",
)


@dataclass(frozen=True)
class RubricCase:
    repo_name: str
    relative_path: tuple[str, ...]
    repo_specific_anchors: tuple[str, ...]
    forbidden_template_tokens: tuple[str, ...] = ()

    @property
    def path(self) -> Path:
        return MY_PROJECTS_ROOT.joinpath(self.repo_name, *self.relative_path)


RUBRIC_CASES = (
    RubricCase(
        repo_name="VLM_Bench",
        relative_path=("docs", "domain_review_rubric.v2.md"),
        repo_specific_anchors=(
            "`dual truth`",
            "`reservoir sidecar`",
            "`reviewer_hold + not_cleared_for_control_based_scale_out`",
        ),
        forbidden_template_tokens=(
            "#### `canonical_term`",
            "#### `object_name`",
        ),
    ),
    RubricCase(
        repo_name="CGen",
        relative_path=("docs", "domain_review_rubric.v2.md"),
        repo_specific_anchors=(
            "`pilot_execution_gate`",
            "`teacherB supplement`",
            "`archivally_closed fail-hold`",
        ),
        forbidden_template_tokens=(
            "#### `canonical_term`",
            "#### `object_name`",
        ),
    ),
    RubricCase(
        repo_name="Cangjie",
        relative_path=("docs", "domain_review_rubric.v2.md"),
        repo_specific_anchors=(
            "`P22 / 311-311 frozen-pass checkpoint`",
            "`Phase07 Telegram UI Incubation`",
            "`Linux Staging-Core / Windows Staging-Full`",
        ),
        forbidden_template_tokens=(
            "#### `canonical_term`",
            "#### `object_name`",
        ),
    ),
    RubricCase(
        repo_name="harness",
        relative_path=("mode", "agent_system", "domain_review_rubric_template.md"),
        repo_specific_anchors=(
            "## 最小落地要求",
            "至少 `3` 个 repo-specific canonical terms 已定义。",
            "只在仓库特有词义或 reviewer gate 真正变化时更新",
        ),
    ),
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_cross_repo_rubric_paths_exist() -> None:
    missing = [str(case.path) for case in RUBRIC_CASES if not case.path.exists()]
    assert not missing, f"missing rubric files: {missing}"


def test_cross_repo_rubrics_share_semantics_layer_and_repo_specific_instantiation() -> None:
    failures: list[str] = []

    for case in RUBRIC_CASES:
        text = _read(case.path)

        for anchor in COMMON_SEMANTICS_ANCHORS:
            if anchor not in text:
                failures.append(f"{case.repo_name}: missing common anchor {anchor}")

        for anchor in case.repo_specific_anchors:
            if anchor not in text:
                failures.append(f"{case.repo_name}: missing repo-specific anchor {anchor}")

        for token in case.forbidden_template_tokens:
            if token in text:
                failures.append(f"{case.repo_name}: still contains uninstantiated template token {token}")

    assert not failures, "\n".join(failures)
