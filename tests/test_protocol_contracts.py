from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProtocolContractTests(unittest.TestCase):
    # Protocol 5.4 guarantees retained as regression contracts.
    def test_two_role_lifecycle_remains_explicit(self) -> None:
        text = read("source/README.md")
        self.assertIn("software-design", text)
        self.assertIn("software-implementation", text)
        self.assertIn("two-role lifecycle", text)
        self.assertIn("not a third lifecycle role", read("README.md").lower())

    def test_engineering_fitness_precedes_product_simplicity(self) -> None:
        text = read("source/roles/software-design/SKILL.md").lower()
        self.assertIn("product engineering fitness", text)
        self.assertIn("product/system complexity", text)
        self.assertIn("do not weaken a material requirement", text)
        self.assertIn("development economy", text)

    def test_stage_local_and_final_functional_acceptance_remain_required(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        for text in (implementation, testing):
            self.assertIn("stage-local", text)
            self.assertIn("affected", text)
            self.assertIn("regression", text)
            self.assertIn("integration", text)
        self.assertIn("final assembled acceptance", implementation)
        self.assertIn("re-derive", implementation)

    def test_production_qualification_remains_separate(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("production qualification is separate", implementation)
        self.assertIn("production qualification", testing)
        self.assertIn("distinct from functional testing", testing)
        self.assertIn("bounded benchmarks", testing)

    def test_progressive_repository_inspection_remains_required(self) -> None:
        text = read("source/shared/references/repository-intake.md").lower()
        self.assertIn("progressive inspection", text)
        self.assertIn("expand on evidence", text)

    def test_optional_specialists_do_not_become_lifecycle_gates(self) -> None:
        text = read("source/README.md").lower()
        self.assertIn("optional specialists", text)
        self.assertIn("not approval gates", text)

    def test_accepted_workplan_governs_without_blind_obedience(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        for text in (design, implementation, workflow):
            self.assertIn("accepted workplan", text)
            self.assertIn("reopen", text)
        self.assertIn("repository evidence", implementation)
        self.assertIn("higher-priority", implementation)

    def test_material_redesign_is_bounded_to_invalidated_surface(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        architecture = read("source/shared/references/architecture-and-design.md").lower()
        self.assertIn("local reconciliation", implementation)
        self.assertIn("material redesign", implementation)
        self.assertIn("earliest materially affected", implementation)
        self.assertIn("reopen only the affected", architecture)

    def test_workplan_inheritance_is_bound_to_declared_protocol_version(self) -> None:
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        self.assertIn("workplan protocol binding", versioning)
        self.assertIn("declared `protocol_version`", versioning)
        self.assertIn("later protocol releases do not silently change", template)
        self.assertIn("implementation authority", template)
        self.assertIn("### frozen", template)
        self.assertIn("### delegated", template)
        self.assertIn("### reopen only on evidence", template)

    def test_repository_intake_optimizes_information_gain_not_coverage(self) -> None:
        intake = read("source/shared/references/repository-intake.md").lower()
        self.assertIn("information gain and context economy", intake)
        self.assertIn("lowest-cost next inspection", intake)
        self.assertIn("reuse repository facts", intake)
        self.assertIn("targeted symbol/search/range", intake)
        self.assertIn("context minimization is never permission", intake)

    def test_testing_reuses_valid_evidence_without_weakening_final_acceptance(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        self.assertIn("coherent stage granularity", testing)
        self.assertIn("cheapest high-signal", workflow)
        self.assertIn("evidence reuse and invalidation", testing)
        self.assertIn("never removes final assembled acceptance", testing)
        self.assertIn("coherent behavior/risk boundary", workflow)
        self.assertIn("final assembled affected-surface regression", workflow)

    def test_long_gated_work_preserves_compact_state_without_new_bureaucracy(self) -> None:
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        self.assertIn("compact task-local state", workflow)
        self.assertIn("accepted frozen decisions", workflow)
        self.assertIn("still-valid evidence", workflow)
        self.assertIn("not a required persistent artifact", workflow)
        self.assertIn("do not create a ledger", workflow)
        self.assertIn("final acceptance still re-derives", workflow)

    def test_implementation_performance_and_resource_guardrails_remain(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("eliminating redundant work/i/o", implementation)
        self.assertIn("algorithmic scaling", implementation)
        self.assertIn("compiled/vectorized kernels", implementation)
        self.assertIn("cpu/ram/vram/storage/i/o/wall-time", implementation)
        self.assertIn("measure enough to establish the claim", implementation)
        self.assertIn("retain intentional duplication", implementation)

    def test_lifecycle_entrypoints_route_references_by_material_surface(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        for text in (design, implementation):
            self.assertIn("reference routing", text)
            self.assertIn("packaging a reference does not make reading it mandatory", text)
            self.assertIn("material surface", text)
            self.assertIn("references/testing-and-validation.md", text)
            self.assertIn("references/repository-intake.md", text)
        self.assertIn("references/git-and-version-control.md", implementation)
        self.assertNotIn("references/git-and-version-control.md", design)

    def test_independent_review_is_evidence_directed_but_not_scope_limited(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        self.assertIn("highest-information current evidence", design)
        self.assertIn("not acceptance of the implementation agent's summary", design)
        self.assertIn("do not automatically replay the original architecture search", design)
        self.assertIn("retains authority to inspect any surface", design)

    # Protocol 5.5 implementation-fidelity contracts.
    def test_lossless_design_handoff_preserves_material_intent(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        for text in (design, template):
            self.assertIn("protected concern", text)
            self.assertIn("required end state", text)
            self.assertIn("required implementation consequence", text)
            self.assertIn("suggested realization", text)
            self.assertIn("acceptance evidence", text)
        self.assertIn("design handoff closure", template)
        self.assertIn("no material requirement or known design consequence may disappear", workflow)

    def test_required_consequence_is_distinct_from_suggestion_and_delegation(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        for text in (design, implementation, template):
            self.assertIn("required implementation consequence", text)
            self.assertIn("suggested realization", text)
            self.assertIn("delegated", text)

    def test_implementation_intake_and_discovered_consequences_are_explicit(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        self.assertIn("protected concern", implementation)
        self.assertIn("before material editing", implementation)
        self.assertIn("minimum known contract, not a ceiling", implementation)
        self.assertIn("necessary local consequence", implementation)
        self.assertIn("newly affected", implementation)
        self.assertIn("minimum known contract, not a ceiling", workflow)

    def test_material_stage_requires_semantic_and_functional_closure(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        for text in (implementation, workflow, testing):
            self.assertIn("semantic/conformance closure", text)
            self.assertIn("functional closure", text)
        self.assertIn("green tests never prove", workflow)
        self.assertIn("stage-local affected regression", testing)

    def test_final_contract_reconciliation_precedes_functional_acceptance(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("reconcile the complete accepted contract", implementation)
        self.assertIn("silent omission is not an accepted state", implementation)
        self.assertIn("final accepted-contract reconciliation", testing)
        self.assertIn("structural/source", testing)
        self.assertIn("negative/absence", testing)

    def test_independent_review_is_two_pass_and_rework_is_lossless(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        for text in (design, workflow):
            self.assertIn("contract conformance", text)
            self.assertIn("independent engineering challenge", text)
            self.assertIn("implementation nonconformance", text)
            self.assertIn("workplan/design deficiency", text)
            self.assertIn("new independent issue", text)
        self.assertIn("required corrected end state", design)
        self.assertIn("equivalent implementation preferences", design)

    def test_protocol_55_identity_and_specialist_hierarchy_are_reconciled(self) -> None:
        self.assertEqual("5.7.0", read("source/PROTOCOL_VERSION").strip())
        source_readme = read("source/README.md")
        root_readme = read("README.md")
        docs = read("source/specialists/software-documentation/SKILL.md").lower()
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md")
        self.assertIn("Software Development Protocol 5.7", source_readme)
        self.assertIn("Protocol 5.7 preserves the two-role lifecycle", source_readme)
        self.assertIn("Protocol 5.7", root_readme)
        self.assertIn("Protocol 5.6", versioning)
        self.assertIn("Protocol 5.7", versioning)
        self.assertIn("product engineering fitness first", docs)
        self.assertIn("development economy third", docs)


if __name__ == "__main__":
    unittest.main()
