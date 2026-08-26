from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").lower()


class HistoricalFailureModeScenarios(unittest.TestCase):
    def setUp(self) -> None:
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")
        self.workflow = read("source/shared/references/workflow-and-workplans.md")
        self.testing = read("source/shared/references/testing-and-validation.md")

    def test_green_tests_plus_omitted_obligation_is_incomplete(self) -> None:
        self.assertIn("green tests never prove an omitted obligation was implemented", self.workflow)
        self.assertIn("silent omission is not an accepted state", self.implementation)

    def test_downstream_helper_cannot_replace_required_production_caller(self) -> None:
        self.assertIn("directly invokes a downstream helper", self.testing)
        self.assertIn("cannot close the owner claim", self.testing)

    def test_expensive_dependency_can_be_faked_below_real_owner(self) -> None:
        self.assertIn("expensive ml/scientific training or prediction", self.testing)
        self.assertIn("not a global ban on mocks or fakes", self.testing)

    def test_equivalent_local_realization_is_reconciliation_not_redesign(self) -> None:
        self.assertIn("local reconciliation", self.implementation)
        self.assertIn("equivalent local realization", self.implementation)
        self.assertIn("suggested realization is not automatically frozen", self.workflow)

    def test_invalidated_frozen_premise_triggers_bounded_redesign(self) -> None:
        self.assertIn("representative measurement invalidating a premise", self.implementation)
        self.assertIn("reopen only the affected", self.workflow)
        self.assertIn("earliest materially affected stage", self.implementation)

    def test_acceptance_signal_cannot_be_repaired_by_weakening_fixture_or_spec(self) -> None:
        self.assertIn("deleting/weakening its assertion", self.testing)
        self.assertIn("removing known failing inputs", self.testing)
        self.assertIn("rewriting specification/documentation", self.testing)

    def test_self_correction_invalidates_unsound_work(self) -> None:
        self.assertIn("invalidate it and repair/retest", self.implementation)
        self.assertIn("truthful non-closure", self.implementation)

    def test_small_local_change_does_not_require_micro_gating(self) -> None:
        self.assertIn("small/local executable work may look like", self.workflow)
        self.assertIn("a local coherent behavior change is normally one material implementation stage", self.implementation)

    def test_tightly_coupled_edits_form_one_stage_without_independent_risk_boundary(self) -> None:
        self.assertIn("several tightly coupled edits may close under one stage", self.workflow)
        self.assertIn("do not become separate stages merely because", self.implementation)

    def test_newly_discovered_affected_surface_is_incorporated_without_unrelated_redesign(self) -> None:
        self.assertIn("newly discovered affected behavior", self.workflow)
        self.assertIn("do not reopen unrelated design", self.implementation)

    def test_removal_or_unique_authority_claim_needs_structural_evidence(self) -> None:
        self.assertIn("removal, uniqueness, ownership, or no-legacy-path claims", self.testing)
        self.assertIn("structural/source", self.testing)

    def test_literal_contract_pass_that_defeats_stakeholder_outcome_is_rejected(self) -> None:
        self.assertIn("literal compliance actually realizes the protected stakeholder outcome", self.design)
        self.assertIn("workplan/design deficiency", self.design)
        self.assertIn("independent-evaluator counterfactual", self.testing)


if __name__ == "__main__":
    unittest.main()
