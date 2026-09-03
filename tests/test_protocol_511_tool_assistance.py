from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(SOURCE))

import build_skills  # noqa: E402


REFERENCE = "tool-assisted-engineering.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class Protocol511ToolAssistanceTests(unittest.TestCase):
    def test_lifecycle_entrypoints_route_conditionally_to_tool_reference(self) -> None:
        for rel in (
            "source/roles/software-design/SKILL.md",
            "source/roles/software-implementation/SKILL.md",
        ):
            text = read(rel)
            line = next(line for line in text.splitlines() if "](references/tool-assisted-engineering.md)" in line)
            self.assertIn("material", line.lower(), rel)
            self.assertNotIn("MUST read", line, rel)

    def test_tool_reference_is_packaged_only_for_lifecycle_roles(self) -> None:
        for spec in build_skills.ROLE_SPECS.values():
            self.assertIn(REFERENCE, spec["references"])
        for spec in build_skills.SPECIALIST_SPECS.values():
            self.assertNotIn(REFERENCE, spec["references"])

        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            for role in build_skills.ROLE_SPECS:
                self.assertTrue((dist / "skills" / role / "references" / REFERENCE).is_file())
            for specialist in build_skills.SPECIALIST_SPECS:
                self.assertFalse((dist / "skills" / specialist / "references" / REFERENCE).exists())

    def test_tool_selection_is_optional_and_composition_is_not_ceremonial(self) -> None:
        text = read("source/shared/references/tool-assisted-engineering.md").lower()
        self.assertIn("tool availability alone is not a reason", text)
        self.assertIn("tool unavailability is not an acceptance failure", text)
        self.assertIn("mandatory three-tool pipeline", text)
        self.assertIn("do not invoke another tool merely to duplicate evidence", text)
        self.assertIn("defect diagnosis and variant analysis", text)
        self.assertIn("independent review", text)

    def test_serena_guidance_protects_backend_completeness_mutation_and_memory(self) -> None:
        text = read("source/shared/references/tool-assisted-engineering.md").lower()
        for phrase in (
            "backends and languages expose different capabilities",
            "cross-check semantic results",
            "ambiguous repository state",
            "inspect current file/diff/status before retrying",
            "derived/advisory context by default",
            "explicitly promote",
        ):
            self.assertIn(phrase, text)
        self.assertIn(".serena", text)

    def test_semgrep_guidance_bounds_rules_engine_scope_and_suppressions(self) -> None:
        text = read("source/shared/references/tool-assisted-engineering.md").lower()
        for phrase in (
            "community edition-compatible",
            "known-positive and known-negative",
            "0 findings",
            ".gitignore",
            ".semgrepignore",
            "nosemgrep",
            "explicit project/user authorization",
            "autofix",
        ):
            self.assertIn(phrase, text)

    def test_hypothesis_guidance_preserves_oracle_durability_and_isolation(self) -> None:
        text = read("source/shared/references/tool-assisted-engineering.md").lower()
        for phrase in (
            "not an independent oracle",
            "health-check suppression",
            "isolated/reset test-owned state",
            "example database",
            "@example",
            "settings profile",
            "seeds and failure-replay mechanisms are debugging aids",
        ):
            self.assertIn(phrase, text)

    def test_tool_content_is_not_instruction_authority_or_acceptance_substitute(self) -> None:
        text = read("source/shared/references/tool-assisted-engineering.md").lower()
        self.assertIn("not an instruction-authority channel", text)
        self.assertIn("not product truth", text)
        self.assertIn("affected regression", text)
        self.assertIn("integration", text)
        self.assertIn("re-derive the final affected surface", text)

    def test_portability_keeps_external_tooling_optional(self) -> None:
        text = read("PORTABILITY.md").lower()
        self.assertIn("optional environment capabilities", text)
        self.assertIn("not part of generic agent skill validity", text)
        self.assertIn("direct-directory installation contract", text)
        self.assertIn("protocol 5.9 routing qualification", text)
        self.assertIn("named harness/tool configuration", text)


if __name__ == "__main__":
    unittest.main()
