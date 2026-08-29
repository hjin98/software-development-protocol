from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(SOURCE))

import validate_packages  # noqa: E402


class FrontmatterSchemaTests(unittest.TestCase):
    def validate(self, frontmatter: str):
        text = f"---\n{frontmatter}\n---\nbody\n"
        return validate_packages.validate_frontmatter(text, "sample-skill")[0]

    def test_valid_nested_metadata_and_allowed_tools(self) -> None:
        errors = self.validate('name: sample-skill\ndescription: Portable sample.\ncompatibility: Requires git.\nmetadata:\n  owner: test\n  version: "1"\nallowed-tools: Bash(git:*) Read')
        self.assertEqual([], errors)

    def test_malformed_yaml_is_rejected(self) -> None:
        errors = self.validate('name: sample-skill\ndescription: Sample.\nmetadata: [unterminated')
        self.assertTrue(any("invalid YAML" in error for error in errors), errors)

    def test_compatibility_type_and_length_are_rejected(self) -> None:
        errors = self.validate('name: sample-skill\ndescription: Sample.\ncompatibility: [linux]')
        self.assertTrue(any("compatibility must be" in error for error in errors), errors)
        errors = self.validate('name: sample-skill\ndescription: Sample.\ncompatibility: "' + ('x' * 501) + '"')
        self.assertTrue(any("exceeds 500" in error for error in errors), errors)

    def test_metadata_requires_string_keys_and_values(self) -> None:
        errors = self.validate('name: sample-skill\ndescription: Sample.\nmetadata:\n  owner: [team]')
        self.assertTrue(any("metadata keys and values" in error for error in errors), errors)
        errors = self.validate('name: sample-skill\ndescription: Sample.\nmetadata:\n  7: seven')
        self.assertTrue(any("metadata keys and values" in error for error in errors), errors)

    def test_allowed_tools_must_be_scalar_string(self) -> None:
        errors = self.validate('name: sample-skill\ndescription: Sample.\nallowed-tools:\n  - Read')
        self.assertTrue(any("allowed-tools must be" in error for error in errors), errors)


class ResourceRouteSafetyTests(unittest.TestCase):
    def assert_unsafe(self, target: str) -> None:
        errors = validate_packages.validate_resource_routes(f"Read [resource]({target}).", {})
        self.assertTrue(any("unsafe or non-portable" in error for error in errors), errors)

    def test_parent_traversal_from_reference_namespace_is_rejected(self) -> None:
        self.assert_unsafe("references/../outside.md")

    def test_parent_traversal_into_reference_namespace_is_rejected(self) -> None:
        self.assert_unsafe("../references/outside.md")

    def test_backslash_resource_path_is_rejected(self) -> None:
        self.assert_unsafe(r"references\outside.md")

    def test_safe_but_missing_resource_still_fails(self) -> None:
        errors = validate_packages.validate_resource_routes("Read [resource](references/missing.md).", {})
        self.assertTrue(any("routed resource is not packaged" in error for error in errors), errors)


class WorkplanLifecycleTests(unittest.TestCase):
    def test_protocol_58_workplan_is_archived_completed(self) -> None:
        active = ROOT / "workplans/active/PROTOCOL-5.8-EFFECTIVE-COMPRESSION.md"
        archived = ROOT / "workplans/archive/PROTOCOL-5.8-EFFECTIVE-COMPRESSION.md"
        self.assertFalse(active.exists())
        self.assertTrue(archived.is_file())
        text = archived.read_text(encoding="utf-8")
        self.assertIn("status: completed", text)
        self.assertIn("completed_date: 2026-08-29", text)
        active_names = {path.name for path in (ROOT / "workplans/active").glob("*.md")}
        self.assertTrue(active_names)
        self.assertTrue(all(name.startswith("PROTOCOL-5.9-") for name in active_names), active_names)


if __name__ == "__main__":
    unittest.main()
