#!/usr/bin/env python3
"""Synthetic lifecycle cases for the materiality-first Protocol v3."""

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

    print("PASS: Protocol v3 materiality lifecycle cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
