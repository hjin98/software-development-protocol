#!/usr/bin/env python3
"""Cheap semantic invariants for materiality-first Protocol v3 source."""

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
    return [f"{path}: forbidden blocking doctrine {needle!r}" for needle in needles if needle in text]


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

    workplans = REFS / "workplans-and-agent-handoff.md"
    errors += require(
        workplans,
        [
            "Materiality rule",
            "Acceptance-critical requirements",
            "No administrative, secondary diagnostic, or evidence-format defect may by itself require product requalification",
            "Harness/record defect",
            "MERGE_READY",
        ],
    )

    testing = REFS / "testing-and-qualification.md"
    errors += require(
        testing,
        [
            "mandatory check that did not execute cannot be called PASS",
            "smallest materially sufficient",
            "full production scale only when production scale itself is materially required",
            "hard-limit hit caused by an oversized harness is not by itself a product failure",
            "Broad regression policy",
            "If no trustworthy baseline exists",
        ],
    )

    resource = REFS / "resource-bounded-execution.md"
    errors += require(
        resource,
        [
            "hard safety ceiling",
            "planned operating envelope",
            "Smallest materially sufficient workload",
            "Automatic adaptation",
            "Adaptive execution mechanics are allowed. Adaptive acceptance semantics are forbidden.",
            "Autonomous external execution",
            "Transient-state ownership and cleanup",
            "startup scavenging",
            "Do not turn observability into an acceptance system.",
            "minimum materially sufficient workload cannot be executed safely",
        ],
    )

    versioning = REFS / "protocol-versioning-and-compatibility.md"
    errors += require(
        versioning,
        [
            "candidate_commit = <Git commit SHA>",
            "real boundary",
            "report typo or evidence-only wording change -> rerun nothing",
        ],
    )

    qskill = ROLES / "software-qualification" / "SKILL.md"
    errors += require(
        qskill,
        [
            "Harness correction authority",
            "smallest materially sufficient",
            "Prefer autonomous one-command execution",
            "clean owned large intermediates",
            "RETURN_TO_IMPLEMENTATION",
            "DESIGN_REVISION_REQUIRED",
            "BLOCKED",
            "Do **not** silently change product code",
        ],
    )

    iskill = ROLES / "software-implementation" / "SKILL.md"
    errors += require(iskill, ["standalone one-command qualifier", "automatically cleans run-owned large transient state"])

    vskill = ROLES / "software-verification" / "SKILL.md"
    errors += require(vskill, ["MERGE_READY", "NOT_READY", "DESIGN_REVISION_REQUIRED", "did not merely rely on hard-limit termination"])

    handoff = TEMPLATES / "qualification_handoff_template.md"
    errors += require(handoff, ["Resource-bounded execution", "smallest materially sufficient", "cleanup/scavenging", "Optional telemetry/secondary diagnostics are advisory"])

    for template_name in (
        "implementation_workplan_template.md",
        "qualification_handoff_template.md",
        "qualification_report_template.md",
        "verification_report_template.md",
    ):
        errors += require(TEMPLATES / template_name, ["REPLACE_WITH_SKILL_PROTOCOL_VERSION"])

    # The default templates/roles must not reinstate discarded mandatory machinery.
    for path in [
        ROLES / "software-implementation" / "SKILL.md",
        ROLES / "software-qualification" / "SKILL.md",
        ROLES / "software-verification" / "SKILL.md",
        TEMPLATES / "qualification_handoff_template.md",
        TEMPLATES / "qualification_report_template.md",
    ]:
        errors += forbid(
            path,
            [
                "candidate_content_identity:",
                "candidate_identity_policy:",
                "workplan_sha256:",
                "qualification_handoff_sha256:",
                "Evidence dependencies:",
                "Retry policy:",
            ],
        )

    if errors:
        print("FAIL: protocol semantic invariant check")
        for error in errors:
            print(f"  {error}")
        return 2

    print("PASS: Protocol v3.1 materiality/resource semantic invariants")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
