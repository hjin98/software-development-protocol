#!/usr/bin/env python3
"""Synthetic lifecycle cases for materiality-first Protocol v3.1."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    required: bool
    executed: bool
    passed: bool


def check_passes(check: Check) -> bool:
    return check.required and check.executed and check.passed


def correction_requires_requalification(
    *,
    product_changed: bool = False,
    material_input_changed: bool = False,
    material_environment_changed: bool = False,
    acceptance_semantics_changed: bool = False,
    interpretation_changed: bool = False,
) -> bool:
    return any(
        (
            product_changed,
            material_input_changed,
            material_environment_changed,
            acceptance_semantics_changed,
            interpretation_changed,
        )
    )


def harness_correction_allowed(*, material_conditions_unchanged: bool) -> bool:
    return material_conditions_unchanged


def broad_failure_blocks(*, candidate_caused: bool, globally_green_policy: bool) -> bool:
    return candidate_caused or globally_green_policy


def qualification_may_change(*, product_semantics: bool, harness_only: bool) -> bool:
    return harness_only and not product_semantics


def resource_outcome(
    *,
    hard_limit_hit: bool = False,
    material_product_measurement: bool = False,
    product_requirement_violated: bool = False,
    minimum_material_workload_fits: bool = True,
) -> str:
    if material_product_measurement and product_requirement_violated:
        return "PRODUCT_FAIL"
    if not minimum_material_workload_fits:
        return "BLOCKED"
    if hard_limit_hit:
        return "HARNESS_ADAPT"
    return "CONTINUE"


def optional_defect_blocks(*, needed_for_safety_or_interpretation: bool) -> bool:
    return needed_for_safety_or_interpretation


def production_scale_required(*, bounded_representative_evidence_sufficient: bool) -> bool:
    return not bounded_representative_evidence_sufficient


def cleanup_policy(*, owned_transient: bool, compact_failure_evidence_saved: bool) -> str:
    if owned_transient and compact_failure_evidence_saved:
        return "CLEAN"
    if not owned_transient:
        return "DO_NOT_DELETE"
    return "PRESERVE_UNTIL_COMPACTED"


def main() -> int:
    # Mandatory missing execution never passes.
    assert not check_passes(Check(required=True, executed=False, passed=True))
    assert not check_passes(Check(required=True, executed=True, passed=False))
    assert check_passes(Check(required=True, executed=True, passed=True))

    # Product/material changes invalidate affected evidence.
    assert correction_requires_requalification(product_changed=True)
    assert correction_requires_requalification(material_input_changed=True)
    assert correction_requires_requalification(material_environment_changed=True)
    assert correction_requires_requalification(acceptance_semantics_changed=True)
    assert correction_requires_requalification(interpretation_changed=True)

    # Administrative/harness corrections do not by themselves invalidate evidence.
    assert not correction_requires_requalification()
    assert harness_correction_allowed(material_conditions_unchanged=True)
    assert not harness_correction_allowed(material_conditions_unchanged=False)

    # Qualification may repair harnesses but not product semantics.
    assert qualification_may_change(product_semantics=False, harness_only=True)
    assert not qualification_may_change(product_semantics=True, harness_only=True)

    # Broad-suite failures block by attribution or explicit globally-green policy.
    assert broad_failure_blocks(candidate_caused=True, globally_green_policy=False)
    assert broad_failure_blocks(candidate_caused=False, globally_green_policy=True)
    assert not broad_failure_blocks(candidate_caused=False, globally_green_policy=False)

    # Oversized qualification adapts; it is not automatically a product failure.
    assert resource_outcome(hard_limit_hit=True) == "HARNESS_ADAPT"

    # Minimum material workload that cannot safely fit is an environment blocker.
    assert resource_outcome(minimum_material_workload_fits=False) == "BLOCKED"

    # A genuine frozen product resource requirement remains enforceable.
    assert resource_outcome(
        material_product_measurement=True,
        product_requirement_violated=True,
    ) == "PRODUCT_FAIL"

    # Secondary/advisory observability does not block unless materially needed.
    assert not optional_defect_blocks(needed_for_safety_or_interpretation=False)
    assert optional_defect_blocks(needed_for_safety_or_interpretation=True)

    # Do not demand production replay when bounded representative evidence suffices.
    assert not production_scale_required(bounded_representative_evidence_sufficient=True)
    assert production_scale_required(bounded_representative_evidence_sufficient=False)

    # Preserve compact failure evidence, then clean only clearly owned transient data.
    assert cleanup_policy(owned_transient=True, compact_failure_evidence_saved=True) == "CLEAN"
    assert cleanup_policy(owned_transient=True, compact_failure_evidence_saved=False) == "PRESERVE_UNTIL_COMPACTED"
    assert cleanup_policy(owned_transient=False, compact_failure_evidence_saved=True) == "DO_NOT_DELETE"

    print("PASS: Protocol v3.1 materiality/resource lifecycle cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
