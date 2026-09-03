#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
workflow = ROOT / "source/shared/references/workflow-and-workplans.md"
text = workflow.read_text(encoding="utf-8")

old_revision = "Ordinary implementation attempts and review cycles do **not** require a new numbered authority revision."
new_revision = "Ordinary implementation attempts and review cycles do not require a new numbered authority revision."
if old_revision in text:
    text = text.replace(old_revision, new_revision, 1)
elif new_revision not in text:
    raise SystemExit("Protocol 5.12 revision-economy sentence not found")

old_saturation = (
    "When a blocker implicates a material family, the reviewer should continue cheap, high-information "
    "read-only inspection of the directly implicated family far enough to characterize obvious sibling "
    "variants/equivalence classes before routing it back."
)
new_saturation = (
    "When a blocker implicates a material family, the reviewer must, to the degree proportionate and practical "
    "in the current review, continue cheap, high-information read-only inspection of the directly implicated "
    "family far enough to characterize obvious sibling variants/equivalence classes before routing it back."
)
if old_saturation in text:
    text = text.replace(old_saturation, new_saturation, 1)
elif new_saturation not in text:
    raise SystemExit("Protocol 5.12 reviewer-saturation sentence not found")

force_sentence = (
    "No recurrence count, review count, cycle budget, or convergence target can force acceptance; "
    "escalation changes the engineering method, not the pass threshold."
)
anchor = (
    "If the same material family survives or reappears after a genuine family closure, or the census itself "
    "demonstrates duplicated/contradictory ownership, uncontrolled entry points, proliferating exceptional paths, "
    "or another structural redesign trigger, stop another ordinary sibling-patch cycle and route to **bounded "
    "Software Design reconsideration**. Reconsideration is mandatory, but a normative design change is not "
    "predetermined: Design may keep frozen product/architecture semantics and require stronger implementation "
    "consolidation/refactoring/canonicalization, or reopen only the affected frozen decision when evidence shows "
    "that decision itself must change."
)
if force_sentence not in text:
    if anchor not in text:
        raise SystemExit("Protocol 5.12 escalation anchor not found")
    text = text.replace(anchor, anchor + "\n\n" + force_sentence, 1)

unrelated_sentence = (
    "An unrelated pre-existing issue does not block current closure merely because review discovered it; "
    "it becomes current-scope material only when evidence shows that the active change exposes, depends on, "
    "or materially interacts with it."
)
route_anchor = (
    "Route findings by engineering meaning, not cycle count: an already-binding requirement/invariant/acceptance "
    "miss is implementation nonconformance under the same authority; a genuinely missing or incorrect still-binding "
    "task semantic requires reconciliation of current workplan/design before the next handoff; a newly affected material "
    "issue that preserves frozen design is incorporated as a necessary implementation consequence and grouped into an "
    "existing family when semantics match; an unrelated pre-existing issue with no material dependency on the active "
    "claim is routed separately."
)
if unrelated_sentence not in text:
    if route_anchor not in text:
        raise SystemExit("Protocol 5.12 finding-routing anchor not found")
    text = text.replace(route_anchor, route_anchor + "\n\n" + unrelated_sentence, 1)

workflow.write_text(text, encoding="utf-8")

TEST = '''from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").lower()


class Protocol512ConvergenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workflow = read("source/shared/references/workflow-and-workplans.md")
        self.testing = read("source/shared/references/testing-and-validation.md")
        self.architecture = read("source/shared/references/architecture-and-design.md")
        self.intake = read("source/shared/references/repository-intake.md")
        self.tooling = read("source/shared/references/tool-assisted-engineering.md")
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")
        self.template = read("source/shared/templates/implementation_workplan_template.md")

    def test_identity_and_preservation(self) -> None:
        self.assertEqual("5.12.0", read("source/PROTOCOL_VERSION").strip())
        hierarchy = "product engineering fitness > minimum justified product/system complexity > development economy"
        self.assertIn(hierarchy, self.design)
        self.assertIn(hierarchy, self.implementation)
        self.assertIn("software-design -> software-implementation", read("source/README.md"))
        self.assertIn("truthful non-closure", self.design)
        self.assertIn("truthful non-closure", self.implementation)

    def test_escalation_and_semantic_family_boundary(self) -> None:
        for phrase in (
            "a first clean local defect",
            "family closure after recurrence",
            "genuine family closure",
            "bounded software design reconsideration",
            "do not fragment",
            "do not overaggregate",
            "protected invariant / required product claim",
            "semantic owner or authority class",
            "state / transition / lifecycle class",
            "materially equivalent failure mechanism",
        ):
            self.assertIn(phrase, self.workflow)

    def test_incomplete_family_closure_does_not_force_redesign(self) -> None:
        self.assertIn("incomplete family closure", self.workflow)
        self.assertIn("remains implementation nonconformance", self.workflow)
        self.assertIn("normative design change is not predetermined", self.workflow)
        self.assertIn("does not automatically mean architecture churn", self.architecture)
        self.assertIn("complete/correct that family closure", self.implementation)

    def test_genuine_post_family_recurrence_requires_design_reconsideration(self) -> None:
        self.assertIn("after a genuine family closure", self.workflow)
        self.assertIn("same family materially fails after an adequate family closure", self.implementation)
        self.assertIn("triggers bounded design reconsideration", self.design)
        self.assertIn("same authority", self.architecture)

    def test_no_cycle_or_review_count_can_force_acceptance(self) -> None:
        self.assertIn(
            "no recurrence count, review count, cycle budget, or convergence target can force acceptance",
            self.workflow,
        )
        self.assertIn("not the pass threshold", self.workflow)

    def test_census_is_bounded_and_conditional(self) -> None:
        self.assertIn("progressive evidence-directed inspection remains the default", self.intake)
        self.assertIn("switch to a bounded census only when", self.intake)
        self.assertIn("whole-repository inventory remains unnecessary", self.workflow)
        self.assertIn("not universal persistent traceability artifacts", self.intake)

    def test_acceptance_liveness_keeps_real_owner_and_runtime_evidence(self) -> None:
        for phrase in (
            "patched seam, failpoint, callback",
            "trigger actually fired",
            "real semantic owner",
            "not a universal requirement to check out historical commits",
            "known-positive and known-negative",
            "structural/negative scans complement runtime acceptance",
        ):
            self.assertIn(phrase, self.testing)

    def test_review_readiness_is_not_a_refusal_or_design_revision_mechanism(self) -> None:
        for phrase in (
            "exact candidate identity",
            "final complete affected-surface regression",
            "real-boundary integration",
            "not review-ready",
            "not an automatic design revision",
            "explicitly requested review still proceeds",
        ):
            self.assertIn(phrase, self.workflow)
        self.assertIn("do not refuse an explicitly requested review", self.design)
        self.assertIn("review readiness is not a mechanism for refusing review", self.testing)

    def test_review_saturates_family_proportionately_and_has_stopping_rule(self) -> None:
        self.assertIn("reviewer must, to the degree proportionate and practical", self.workflow)
        self.assertIn("review characterizes and batches the family", self.workflow)
        self.assertIn("implementation owns the systematic family closure", self.workflow)
        self.assertIn("reviewer expansion stops", self.workflow)
        self.assertIn("not proof that no conceivable repository defect exists", self.workflow)
        self.assertIn("proportionately saturate the directly implicated family", self.design)
        self.assertIn("evidence-directed sufficiency", self.design)

    def test_revision_economy_preserves_snapshot_complete_current_authority(self) -> None:
        for phrase in (
            "do not require a new numbered authority revision",
            "reconcile that semantic into canonical current authority",
            "snapshot completeness is preserved",
            "concrete new sites",
        ):
            self.assertIn(phrase, self.workflow)
        self.assertIn(
            "ordinary implementation misses and review cycles do not require numbered authority revisions",
            self.design,
        )

    def test_unrelated_preexisting_issue_is_not_automatically_a_blocker(self) -> None:
        self.assertIn("unrelated pre-existing issue", self.workflow)
        self.assertIn("does not block current closure merely because review discovered it", self.workflow)
        self.assertIn("materially interacts with it", self.workflow)

    def test_closure_horizon_and_template_remain_nonbureaucratic(self) -> None:
        self.assertIn("closure horizon", self.workflow)
        self.assertIn("it is not a scope ceiling", self.workflow)
        self.assertIn("conditional convergence guidance", self.template)
        self.assertIn("does not require a family matrix", self.template)
        self.assertIn("do not require ids, ledgers, persistent closure maps", self.template)

    def test_tools_remain_optional(self) -> None:
        self.assertIn("convergence-oriented composition", self.tooling)
        self.assertIn("optional tools", self.tooling)
        self.assertIn("tool absence does not relax family closure", self.tooling)
        self.assertIn("three-tool sequence mandatory", self.tooling)
        self.assertIn("tool availability alone is not a reason", self.tooling)

    def test_regression_integration_and_qualification_semantics_are_preserved(self) -> None:
        self.assertIn("stage-local affected regression", self.testing)
        self.assertIn("stage-local affected regression", self.implementation)
        self.assertIn("final complete affected-surface regression", self.testing)
        self.assertIn("integration/end-to-end", self.testing)
        self.assertIn("production qualification is separate", self.implementation)
        self.assertIn("distinct from functional testing", self.testing)


if __name__ == "__main__":
    unittest.main()
'''

(ROOT / "tests/test_protocol_512_convergence.py").write_text(TEST, encoding="utf-8")
