#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "tests/test_protocol_contracts.py"
text = path.read_text(encoding="utf-8")

old = '''    def test_protocol_58_identity_and_two_role_lifecycle(self) -> None:\n        self.assertEqual("5.8.0", read("source/PROTOCOL_VERSION").strip())\n        source_readme = read("source/README.md").lower()\n        root_readme = read("README.md").lower()\n        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()\n        self.assertIn("software development protocol 5.8", source_readme)\n        self.assertIn("protocol 5.8", root_readme)\n        self.assertIn("protocol 5.8 is a backward-compatible", versioning)\n        for text in (source_readme, root_readme, versioning):\n            self.assertIn("software-design", text)\n            self.assertIn("software-implementation", text)\n'''
new = '''    def test_protocol_59_identity_and_two_role_lifecycle(self) -> None:\n        self.assertEqual("5.9.0", read("source/PROTOCOL_VERSION").strip())\n        source_readme = read("source/README.md").lower()\n        root_readme = read("README.md").lower()\n        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()\n        self.assertIn("software development protocol 5.9", source_readme)\n        self.assertIn("protocol 5.9", root_readme)\n        self.assertIn("protocol 5.9 is a backward-compatible", versioning)\n        for text in (source_readme, root_readme, versioning):\n            self.assertIn("software-design", text)\n            self.assertIn("software-implementation", text)\n'''
if text.count(old) != 1:
    raise SystemExit("release identity test anchor mismatch")
text = text.replace(old, new, 1)

old = '''        for text in (design, implementation):\n            self.assertIn("inspect progressively", text)\n            self.assertIn("ownership, dependency, contract, or behavioral impact", text)\n            self.assertIn("load a reference when a material question enters its ownership domain", text)\n            self.assertIn("references/repository-intake.md", text)\n'''
new = '''        for text in (design, implementation):\n            self.assertIn("inspect progressively", text)\n            self.assertIn("ownership, dependency, contract, or behavioral impact", text)\n            self.assertIn("## reference routing", text)\n            self.assertIn("](references/repository-intake.md)", text)\n            self.assertIn("progressive disclosure is preserved", text)\n'''
if text.count(old) != 1:
    raise SystemExit("progressive routing test anchor mismatch")
text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
