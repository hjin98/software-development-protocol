from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProxyProofAcceptanceContractTests(unittest.TestCase):
    def test_testing_reference_defines_real_owner_and_counterfactual(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        for phrase in (
            "semantic owner under acceptance",
            "allowed test-double boundary",
            "proxy-proof acceptance",
            "could this evidence remain green",
            "cannot close the owner claim",
        ):
            self.assertIn(phrase, text)

    def test_owner_mock_and_bypass_cannot_establish_owner_claim(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("mocks, stubs, monkeypatches", text)
        self.assertIn("directly invokes a downstream helper", text)
        self.assertIn("seeds post-decision or post-transition state", text)
        self.assertIn("reimplements production compatibility", text)
        self.assertIn("helper-produced plan/result", text)

    def test_real_persistence_is_required_when_restart_is_the_claim(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("replaces durable/project persistence", text)
        self.assertIn("persistence, restart, or recovery semantics are the claim", text)

    def test_bounded_fakes_below_owner_remain_valid(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("not a global ban on mocks or fakes", testing)
        self.assertIn("bounded deterministic fixtures remain preferred", testing)
        self.assertIn("below/outside the owner boundary", implementation)
        self.assertIn("expensive external computation", implementation)
        self.assertIn("production-scale execution", testing)

    def test_unavailable_real_boundary_is_not_proxy_passed(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        for text in (testing, implementation):
            self.assertIn("unavailable/blocking", text)
            self.assertIn("silently", text)
            self.assertIn("proxy", text)

    def test_implementation_audits_acceptance_path_and_frozen_boundary(self) -> None:
        text = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("protect the semantic owner under acceptance", text)
        self.assertIn("which production owner/path", text)
        self.assertIn("which functions/components", text)
        self.assertIn("every replacement lies below or outside", text)
        self.assertIn("could remain green", text)
        self.assertIn("not a suggested fixture mechanic", text)
        self.assertIn("must not be weakened as local reconciliation", text)

    def test_design_and_workplan_preserve_material_acceptance_boundary(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        for text in (design, workflow, template):
            self.assertIn("required real owner/path", text)
            self.assertIn("allowed test doubles", text)
            self.assertIn("forbidden substitutions", text)
        self.assertIn("observable acceptance evidence", design)
        self.assertIn("ordinary unit tests", design)
        self.assertIn("ordinary unit tests", template)

    def test_independent_review_routes_proxy_failure_correctly(self) -> None:
        text = read("source/roles/software-design/SKILL.md").lower()
        self.assertIn("could the evidence remain green", text)
        self.assertIn("implementation nonconformance", text)
        self.assertIn("workplan/design deficiency", text)
        self.assertIn("semantic owner", text)

    def test_targeted_guardrail_does_not_create_global_anti_mock_bureaucracy(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("robust inexpensive structural/negative check", text)
        self.assertIn("do not require universal ast scanning", text)
        self.assertIn("global monkeypatch ban", text)
        self.assertIn("new anti-mocking framework", text)

    def test_root_agents_is_compact_authority_router(self) -> None:
        agents = read("AGENTS.md")
        implementation = read("source/roles/software-implementation/SKILL.md")
        lower = agents.lower()
        self.assertIn("`source/` is the canonical protocol source", lower)
        self.assertIn("source/roles/software-design/skill.md", lower)
        self.assertIn("source/roles/software-implementation/skill.md", lower)
        self.assertIn("testing-and-validation.md", lower)
        self.assertIn("workflow-and-workplans.md", lower)
        self.assertIn("protocol-versioning-and-compatibility.md", lower)
        self.assertIn("do not assume every file under `workplans/active/` governs every task", lower)
        self.assertIn("semantic owner", lower)
        self.assertIn("protocol-check.yml", lower)
        self.assertLess(len(agents), len(implementation) // 3)
        self.assertNotIn("## governing doctrine", lower)
        self.assertNotIn("## product design", lower)

    def test_protocol_56_versioning_is_backward_compatible_and_version_bound(self) -> None:
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        self.assertEqual("5.6.0", read("source/PROTOCOL_VERSION").strip())
        self.assertIn("protocol 5.6 is a backward-compatible", versioning)
        self.assertIn("proxy-proof acceptance", versioning)
        self.assertIn("do not automatically adopt protocol 5.6", versioning)
        self.assertIn("declared version", versioning)


if __name__ == "__main__":
    unittest.main()
