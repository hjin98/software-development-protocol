#!/usr/bin/env python3
"""Cheap semantic invariants for the canonical Protocol v3 source."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROLES = ROOT / "roles"
REFS = ROOT / "shared" / "references"
TEMPLATES = ROOT / "shared" / "templates"


def require(path: Path, needles: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [f"{path}: missing {needle!r}" for needle in needles if needle not in text]


def forbid(path: Path, needles: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [f"{path}: forbidden current-contract text {needle!r}" for needle in needles if needle in text]


def main() -> int:
    errors: list[str] = []

    expected_roles = {
        "software-design",
        "software-implementation",
        "software-qualification",
        "software-verification",
    }
    actual_roles = {
        p.name for p in ROLES.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    }
    if actual_roles != expected_roles:
        errors.append(f"role registry mismatch: expected={sorted(expected_roles)} actual={sorted(actual_roles)}")

    errors += require(
        REFS / "protocol-versioning-and-compatibility.md",
        [
            "candidate_commit",
            "candidate_content_identity",
            "EPHEMERAL_QUALIFICATION_OUTPUT",
            "TRACKED_CANDIDATE_OUTPUT",
            "IDENTICAL_RETRY",
            "CLEAN_RETRY",
            "RESUME_RETRY",
            "invalidate by default",
        ],
    )
    errors += require(
        REFS / "workplans-and-agent-handoff.md",
        [
            "Only verification",
            "candidate_content_identity",
            "mandatory_for_current_acceptance",
            "verifier_context",
            "TRACKED_CANDIDATE_OUTPUT",
        ],
    )

    qskill = ROLES / "software-qualification" / "SKILL.md"
    errors += require(
        qskill,
        [
            "product_source_mutation: FORBIDDEN",
            "candidate_content_identity",
            "TRACKED_CANDIDATE_OUTPUT",
            "RETURN_TO_IMPLEMENTATION",
        ],
    )
    errors += forbid(
        qskill,
        [
            "final acceptance belongs to qualification",
            "qualification may edit product source",
        ],
    )

    vskill = ROLES / "software-verification" / "SKILL.md"
    errors += require(
        vskill,
        [
            "MERGE_READY",
            "candidate_content_identity",
            "verifier_context",
            "does not repair substantial product source",
        ],
    )

    iskill = ROLES / "software-implementation" / "SKILL.md"
    errors += require(
        iskill,
        [
            "candidate_content_identity",
            "Qualification Handoff",
            "Ambiguous dependency",
            "Do not mark the workplan `COMPLETE`",
        ],
    )

    for template_name in (
        "implementation_workplan_template.md",
        "qualification_handoff_template.md",
        "qualification_report_template.md",
        "verification_report_template.md",
    ):
        errors += require(TEMPLATES / template_name, ["REPLACE_WITH_SKILL_PROTOCOL_VERSION"])

    errors += require(
        TEMPLATES / "qualification_handoff_template.md",
        [
            "candidate_commit",
            "candidate_content_identity",
            "candidate_identity_policy",
            "Evidence dependencies",
            "Retry policy",
            "EPHEMERAL_QUALIFICATION_OUTPUT",
        ],
    )
    errors += require(
        TEMPLATES / "qualification_report_template.md",
        [
            "candidate_content_identity",
            "Candidate preflight",
            "Per-check execution provenance",
            "Retry history",
            "Evidence reuse",
            "Candidate postflight",
        ],
    )
    errors += require(
        TEMPLATES / "verification_report_template.md",
        [
            "candidate_content_identity",
            "independence:",
            "Evidence reuse audit",
            "MERGE_READY",
        ],
    )

    if errors:
        print("FAIL: protocol semantic invariant check")
        for error in errors:
            print(f"  {error}")
        return 2

    print("PASS: Protocol v3 semantic invariants")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
