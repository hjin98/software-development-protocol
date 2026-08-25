from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class EngineeringStewardshipContractTests(unittest.TestCase):
    def test_shared_product_objective_is_explicit_without_reordering_hierarchy(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        for text in (design, implementation):
            self.assertIn("engineering stewardship", text)
            self.assertIn("stakeholder", text)
            self.assertIn("durable", text)
            self.assertIn("not", text)
            self.assertIn("green", implementation)
        self.assertIn(
            "product engineering fitness > minimum justified product/system complexity > development economy",
            design,
        )

    def test_acceptance_integrity_rejects_signal_gaming_but_preserves_legitimate_changes(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        for phrase in (
            "measurement instruments",
            "deleting/weakening",
            "removing known failing inputs",
            "buggy implementation output",
            "warning/success",
            "making a required check optional",
            "relaxing a material threshold",
            "rewriting specification/documentation",
            "test, fixture, threshold, and specification changes remain legitimate",
        ):
            self.assertIn(phrase, testing)
        self.assertIn("not a global ban on mocks or fakes", testing)

    def test_non_adversarial_compliance_and_owning_layer_repair_are_explicit(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("non-adversarially", design)
        self.assertIn("fix the owning layer", implementation)
        self.assertIn("minimum known engineering contract, not a scoreboard", implementation)

    def test_truthful_nonclosure_requires_genuine_blocker_not_easy_escape(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("truthful non-closure", implementation)
        self.assertIn("reasonable in-scope engineering path remains", implementation)
        self.assertIn("counterfeit completion", implementation)

    def test_self_correction_invalidates_bad_prior_evidence(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("invalidate", implementation)
        self.assertIn("self-correction is engineering progress", implementation)
        self.assertIn("unsound", implementation)

    def test_long_horizon_stewardship_is_bounded_against_scope_creep(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        architecture = read("source/shared/references/architecture-and-design.md").lower()
        self.assertIn("accepted scope", design)
        self.assertIn("bounded by explicit stakeholder requirements", workflow)
        self.assertIn("accepted engineering envelope", workflow)
        self.assertIn("accepted scope", architecture)
        self.assertIn("speculative gold-plating", design)
        self.assertIn("unrelated enhancements", workflow)

    def test_hotfix_mitigation_cannot_masquerade_as_durable_closure(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("emergency/hotfix", implementation)
        self.assertIn("temporary mitigation", implementation)
        self.assertIn("do not misrepresent", implementation)

    def test_independent_review_challenges_outcome_not_only_literal_contract(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        self.assertIn("contract/outcome conformance challenge", design)
        self.assertIn("stakeholder outcome", design)
        self.assertIn("workplan/design deficiency", design)
        self.assertIn("short-term workarounds", design)

    def test_workplans_and_gates_are_not_terminal_objectives(self) -> None:
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        self.assertIn("not terminal objectives", workflow)
        self.assertIn("must never create pressure to manufacture a pass", workflow)
        self.assertIn("stakeholder-relevant product outcome", template)
        self.assertIn("anti-shortcut / integrity constraint", template)
        self.assertIn("do not create a mandatory matrix or traceability ledger", workflow)

    def test_optional_specialists_share_product_truth_without_new_gate(self) -> None:
        docs = read("source/specialists/software-documentation/SKILL.md").lower()
        hygiene = read("source/specialists/repository-hygiene/SKILL.md").lower()
        self.assertIn("truthful stakeholder", docs)
        self.assertIn("never rewrite product truth", docs)
        self.assertIn("long-term repository safety", hygiene)
        self.assertIn("not cosmetic closure", hygiene)
        self.assertIn("not a lifecycle role", hygiene)

    def test_agents_remains_compact_but_primes_stewardship(self) -> None:
        agents = read("AGENTS.md")
        implementation = read("source/roles/software-implementation/SKILL.md")
        lower = agents.lower()
        self.assertIn("engineering steward", lower)
        self.assertIn("durable product outcome", lower)
        self.assertIn("constraints and evidence, not the objective", lower)
        self.assertIn("truthful non-closure", lower)
        self.assertLess(len(agents), len(implementation) // 3)
        self.assertNotIn("## governing doctrine", lower)

    def test_protocol_57_versioning_and_old_workplan_binding(self) -> None:
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        self.assertEqual("5.7.0", read("source/PROTOCOL_VERSION").strip())
        self.assertIn("protocol 5.7 is a backward-compatible", versioning)
        self.assertIn("engineering-stewardship", versioning)
        self.assertIn("older workplans", versioning)
        self.assertIn("declared version", versioning)

    def test_completed_55_workplan_is_not_left_active(self) -> None:
        self.assertFalse((ROOT / "workplans/active/PROTOCOL-5.5-IMPLEMENTATION-FIDELITY.md").exists())
        archived = ROOT / "workplans/archive/PROTOCOL-5.5-IMPLEMENTATION-FIDELITY.md"
        self.assertTrue(archived.exists())
        text = archived.read_text(encoding="utf-8").lower()
        self.assertIn("status: completed", text)
        self.assertIn("completion record", text)


if __name__ == "__main__":
    unittest.main()
