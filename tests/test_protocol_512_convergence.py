from __future__ import annotations

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
