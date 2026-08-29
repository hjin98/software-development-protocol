from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(SOURCE))

import validate_packages  # noqa: E402


class ResourceRouteUriSafetyTests(unittest.TestCase):
    def assert_unsafe(self, target: str) -> None:
        errors = validate_packages.validate_resource_routes(f"Read [resource]({target}).", {})
        self.assertTrue(any("unsafe or non-portable" in error for error in errors), errors)

    def test_windows_backslash_absolute_resource_path_is_rejected(self) -> None:
        self.assert_unsafe(r"C:\references\outside.md")

    def test_windows_forward_slash_absolute_resource_path_is_rejected(self) -> None:
        self.assert_unsafe("C:/references/outside.md")

    def test_file_uri_resource_path_is_rejected(self) -> None:
        self.assert_unsafe("file:///tmp/references/outside.md")

    def test_external_https_resource_like_path_is_not_treated_as_local_bundle_route(self) -> None:
        errors = validate_packages.validate_resource_routes(
            "Read [external](https://example.com/references/guide.md).", {}
        )
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
