from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(SOURCE))

import build_skills  # noqa: E402


class BuildIndexContractTests(unittest.TestCase):
    def test_build_index_classifies_roles_and_specialists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            index = json.loads((dist / "BUILD_INDEX.json").read_text(encoding="utf-8"))
            self.assertEqual(set(build_skills.ROLE_SPECS), set(index["lifecycle_roles"]))
            self.assertEqual(set(build_skills.SPECIALIST_SPECS), set(index["specialists"]))
            self.assertEqual(
                set(build_skills.ROLE_SPECS) | set(build_skills.SPECIALIST_SPECS),
                set(index["skills"]),
            )


if __name__ == "__main__":
    unittest.main()
