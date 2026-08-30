from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProtocolContractTests(unittest.TestCase):
    def test_protocol_510_identity_and_two_role_lifecycle(self) -> None:
        self.assertEqual("5.10.0", read("source/PROTOCOL_VERSION").strip())
        source_readme = read("source/README.md").lower()
        root_readme = read("README.md").lower()
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        self.assertIn("software development protocol 5.10", source_readme)
        self.assertIn("protocol 5.10", root_readme)
        self.assertIn("protocol 5.10 is a backward-compatible", versioning)
        self.assertIn("protocol 5.9 is a backward-compatible", versioning)
        self.assertIn("protocol 5.4-5.9 guarantees unchanged", source_readme)
        for text in (source_readme, root_readme, versioning):
            self.assertIn("software-design", text)
            self.assertIn("software-implementation", text)

    def test_governing_hierarchy_and_product_truth_remain_entrypoint_critical(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        hierarchy = "product engineering fitness > minimum justified product/system complexity > development economy"
        for text in (design, implementation):
            self.assertIn(hierarchy, text)
            self.assertIn("stakeholder", text)
            self.assertIn("durable", text)
            self.assertIn("truthful non-closure", text)
        self.assertIn("non-adversarially", design)
        self.assertIn("counterfeit completion", implementation)

    def test_progressive_inspection_and_reference_loading_are_explicit(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        intake = read("source/shared/references/repository-intake.md").lower()
        for text in (design, implementation):
            self.assertIn("inspect progressively", text)
            self.assertIn("ownership, dependency, contract, or behavioral impact", text)
            self.assertIn("## reference routing", text)
            self.assertIn("](references/repository-intake.md)", text)
            self.assertIn("progressive disclosure is preserved", text)
        self.assertIn("lowest-cost next inspection", intake)
        self.assertIn("reuse repository facts", intake)
        self.assertIn("context minimization is never permission", intake)

    def test_workplan_authority_is_detailed_in_canonical_workflow(self) -> None:
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        for phrase in (
            "accepted-workplan authority",
            "frozen",
            "delegated",
            "reopen only on evidence",
            "minimum known contract, not a ceiling",
            "later protocol releases do not silently reinterpret",
        ):
            self.assertIn(phrase, workflow)
        self.assertIn("implementation realization", implementation)
        self.assertIn("local reconciliation", implementation)
        self.assertIn("material redesign", implementation)
        self.assertIn("minimum known contract, not a ceiling", implementation)

    def test_lossless_handoff_is_preserved_without_template_boilerplate(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        for phrase in (
            "protected concern",
            "required end state",
            "required implementation consequence",
            "suggested realization",
            "acceptance evidence",
        ):
            self.assertIn(phrase, workflow)
            self.assertIn(phrase, design)
        self.assertIn("known material consequences must not disappear", template)
        self.assertIn("handoff closure", template)
        self.assertIn("generic functional-acceptance requirements are inherited", template)
        self.assertIn("attach only when material", template)

    def test_snapshot_complete_handoff_survives_history_loss(self) -> None:
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        documentation = read("source/shared/references/documentation-and-evidence.md").lower()
        for phrase in (
            "snapshot-complete",
            "supplied artifact set",
            "snapshot-loss counterfactual",
            "workplan/design deficiency",
        ):
            self.assertIn(phrase, workflow)
        self.assertIn("git history", workflow)
        self.assertIn("not sufficient normative storage", workflow)
        self.assertIn("snapshot-loss counterfactual", template)
        self.assertIn("supplied current artifact set", template)
        self.assertIn("not sufficient normative storage", template)
        self.assertIn("current protocol/specification/architecture/package composition remains valid", template)
        self.assertIn("snapshot-complete", design)
        self.assertIn("supplied current authority", design)
        self.assertIn("complete task-specific authority", implementation)
        self.assertIn("workplan/design deficiency", implementation)
        self.assertIn("not the normal source of normative task requirements", implementation)
        self.assertIn("current normative document", documentation)
        self.assertIn("supplied current artifact set", documentation)
        self.assertIn("current cross-document composition remains valid", documentation)
        self.assertIn("non-current authority", documentation)

    def test_stage_proportionality_preserves_dual_closure_and_regression(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("a local coherent behavior change is normally one material implementation stage", implementation)
        self.assertIn("several tightly coupled edits", workflow)
        for text in (implementation, workflow, testing):
            self.assertIn("semantic/conformance closure", text)
            self.assertIn("stage-local affected regression", text)
        self.assertIn("functional closure", workflow)
        self.assertIn("functional closure", testing)

    def test_final_acceptance_remains_complete(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        for phrase in (
            "reconcile the complete accepted contract",
            "re-derive the complete affected behavioral surface",
            "complete affected-surface regression",
            "integration/end-to-end",
        ):
            self.assertIn(phrase, implementation)
        self.assertIn("final assembled acceptance", testing)
        self.assertIn("structural/source", testing)
        self.assertIn("negative/absence", testing)

    def test_production_qualification_remains_separate(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        testing = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("production qualification is separate", implementation)
        self.assertIn("distinct from functional testing", testing)
        self.assertIn("production run never substitutes", implementation)

    def test_independent_review_remains_two_pass_and_evidence_directed(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        self.assertIn("contract/outcome conformance", design)
        self.assertIn("independent engineering challenge", design)
        self.assertIn("highest-information current evidence", design)
        self.assertIn("implementation nonconformance", design)
        self.assertIn("workplan/design deficiency", design)
        self.assertIn("new independent issue", design)
        self.assertIn("equivalent preferences without material engineering benefit", workflow)

    def test_compact_working_state_does_not_create_new_bureaucracy(self) -> None:
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        self.assertIn("compact task-local state", workflow)
        self.assertIn("not a required persistent artifact", workflow)
        self.assertIn("do not create a ledger", workflow)
        self.assertIn("do not create a mandatory handoff manifest", workflow)

    def test_optional_specialists_remain_supporting_capabilities(self) -> None:
        source_readme = read("source/README.md").lower()
        docs = read("source/specialists/software-documentation/SKILL.md").lower()
        hygiene = read("source/specialists/repository-hygiene/SKILL.md").lower()
        self.assertIn("optional specialists", source_readme)
        self.assertIn("not approval gates", source_readme)
        self.assertIn("product engineering fitness first", docs)
        self.assertIn("not a lifecycle role", hygiene)


if __name__ == "__main__":
    unittest.main()
