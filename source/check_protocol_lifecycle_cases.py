#!/usr/bin/env python3
"""Synthetic lifecycle cases for Protocol v3 authority/identity rules.

This is a protocol regression model, not a project-specific qualification runner.
"""

from __future__ import annotations

from dataclasses import dataclass


BLOCKING_QUAL = {"NOT_RUN", "FAIL", "BLOCKED"}
RETRY_MODES = {"NONE", "IDENTICAL_RETRY", "CLEAN_RETRY", "RESUME_RETRY"}


@dataclass(frozen=True)
class CheckState:
    status: str
    mandatory_for_current_acceptance: bool = True


def ready_for_verification(checks: list[CheckState]) -> bool:
    for check in checks:
        if not check.mandatory_for_current_acceptance:
            continue
        if check.status in BLOCKING_QUAL:
            return False
        if check.status == "DEFERRED":
            return False
        if check.status not in {"PASS", "NOT_REQUIRED"}:
            return False
    return True


def evidence_reusable(*, dependency_known: bool, dependency_intersects_change: bool) -> bool:
    return dependency_known and not dependency_intersects_change


def qualification_candidate_valid(
    *,
    head_matches: bool,
    content_identity_matches: bool,
    tracked_dirty: bool,
    undeclared_untracked_affects_execution: bool,
) -> bool:
    return (
        head_matches
        and content_identity_matches
        and not tracked_dirty
        and not undeclared_untracked_affects_execution
    )


def verification_candidate_valid(
    *,
    content_identity_matches: bool,
    later_commits_only_declared_evidence_coordination: bool,
) -> bool:
    """Verification may inspect a later HEAD if qualified candidate content is unchanged."""
    return content_identity_matches and later_commits_only_declared_evidence_coordination


def output_allowed(*, output_class: str, declared_write_path: bool) -> bool:
    return output_class == "EPHEMERAL_QUALIFICATION_OUTPUT" and declared_write_path


def retry_allowed(
    *,
    mode: str,
    candidate_changed: bool,
    policy_changed: bool,
    cleanup_declared: bool = True,
    resume_state_declared: bool = True,
) -> bool:
    if mode not in RETRY_MODES or mode == "NONE":
        return False
    if candidate_changed or policy_changed:
        return False
    if mode == "CLEAN_RETRY" and not cleanup_declared:
        return False
    if mode == "RESUME_RETRY" and not resume_state_declared:
        return False
    return True


def main() -> int:
    # Qualification preflight requires exact candidate commit plus clean content state.
    assert qualification_candidate_valid(
        head_matches=True,
        content_identity_matches=True,
        tracked_dirty=False,
        undeclared_untracked_affects_execution=False,
    )
    assert not qualification_candidate_valid(
        head_matches=True,
        content_identity_matches=True,
        tracked_dirty=True,
        undeclared_untracked_affects_execution=False,
    )
    assert not qualification_candidate_valid(
        head_matches=True,
        content_identity_matches=True,
        tracked_dirty=False,
        undeclared_untracked_affects_execution=True,
    )
    assert not qualification_candidate_valid(
        head_matches=True,
        content_identity_matches=False,
        tracked_dirty=False,
        undeclared_untracked_affects_execution=False,
    )
    assert not qualification_candidate_valid(
        head_matches=False,
        content_identity_matches=True,
        tracked_dirty=False,
        undeclared_untracked_affects_execution=False,
    )

    # Verification after qualification may see later evidence-only commits.
    assert verification_candidate_valid(
        content_identity_matches=True,
        later_commits_only_declared_evidence_coordination=True,
    )
    assert not verification_candidate_valid(
        content_identity_matches=False,
        later_commits_only_declared_evidence_coordination=True,
    )
    assert not verification_candidate_valid(
        content_identity_matches=True,
        later_commits_only_declared_evidence_coordination=False,
    )

    # Output classes.
    assert output_allowed(
        output_class="EPHEMERAL_QUALIFICATION_OUTPUT", declared_write_path=True
    )
    assert not output_allowed(
        output_class="EPHEMERAL_QUALIFICATION_OUTPUT", declared_write_path=False
    )
    assert not output_allowed(
        output_class="TRACKED_CANDIDATE_OUTPUT", declared_write_path=True
    )

    # Evidence dependency reuse.
    assert evidence_reusable(
        dependency_known=True, dependency_intersects_change=False
    )
    assert not evidence_reusable(
        dependency_known=True, dependency_intersects_change=True
    )
    assert not evidence_reusable(
        dependency_known=False, dependency_intersects_change=False
    )

    # Retry boundaries.
    assert retry_allowed(
        mode="IDENTICAL_RETRY", candidate_changed=False, policy_changed=False
    )
    assert retry_allowed(
        mode="CLEAN_RETRY",
        candidate_changed=False,
        policy_changed=False,
        cleanup_declared=True,
    )
    assert not retry_allowed(
        mode="CLEAN_RETRY",
        candidate_changed=False,
        policy_changed=False,
        cleanup_declared=False,
    )
    assert retry_allowed(
        mode="RESUME_RETRY",
        candidate_changed=False,
        policy_changed=False,
        resume_state_declared=True,
    )
    assert not retry_allowed(
        mode="RESUME_RETRY",
        candidate_changed=False,
        policy_changed=False,
        resume_state_declared=False,
    )
    assert not retry_allowed(
        mode="IDENTICAL_RETRY", candidate_changed=True, policy_changed=False
    )
    assert not retry_allowed(
        mode="IDENTICAL_RETRY", candidate_changed=False, policy_changed=True
    )

    # Derived lifecycle / deferred semantics.
    assert ready_for_verification(
        [CheckState("PASS"), CheckState("NOT_REQUIRED")]
    )
    assert not ready_for_verification([CheckState("NOT_RUN")])
    assert not ready_for_verification([CheckState("FAIL")])
    assert not ready_for_verification([CheckState("BLOCKED")])
    assert not ready_for_verification(
        [CheckState("DEFERRED", mandatory_for_current_acceptance=True)]
    )
    assert ready_for_verification(
        [CheckState("DEFERRED", mandatory_for_current_acceptance=False)]
    )

    print("PASS: Protocol v3 synthetic lifecycle cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
