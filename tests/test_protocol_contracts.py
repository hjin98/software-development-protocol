from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProtocolContractTests(unittest.TestCase):
    def test_two_role_lifecycle_remains_explicit(self) -> None:
        text = read("source/README.md")
        self.assertIn("software-design", text)
        self.assertIn("software-implementation", text)
        self.assertIn("two-role lifecycle", text)

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

    def test_progressive_repository_inspection_remains_required(self) -> None:
        text = read("source/shared/references/repository-intake.md").lower()
        self.assertIn("progressive inspection", text)
        self.assertIn("expand on evidence", text)

    def test_optional_specialists_do_not_become_lifecycle_gates(self) -> None:
        text = read("source/README.md").lower()
        self.assertIn("optional specialists", text)
        self.assertIn("not lifecycle roles", text)

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


if __name__ == "__main__":
    unittest.main()
