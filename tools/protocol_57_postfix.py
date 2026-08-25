from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"expected one anchor in {path}: {old!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "source/shared/references/architecture-and-design.md",
    "material operational and maintenance horizon of the accepted stakeholder scope",
    "material operational and maintenance horizon of the accepted scope",
)
replace_once(
    "tests/test_protocol_proxy_proof_acceptance.py",
    "self.assertIn(\"do not automatically adopt protocol 5.6\", versioning)",
    "self.assertIn(\"do not automatically adopt protocol 5.7\", versioning)",
)
replace_once(
    "tests/test_protocol_engineering_stewardship.py",
    "        for text in (design, workflow, architecture):\n            self.assertIn(\"accepted scope\", text)\n        self.assertIn(\"speculative gold-plating\", design)\n        self.assertIn(\"unrelated enhancements\", workflow)\n",
    "        self.assertIn(\"accepted scope\", design)\n        self.assertIn(\"bounded by explicit stakeholder requirements\", workflow)\n        self.assertIn(\"accepted engineering envelope\", workflow)\n        self.assertIn(\"accepted scope\", architecture)\n        self.assertIn(\"speculative gold-plating\", design)\n        self.assertIn(\"unrelated enhancements\", workflow)\n",
)
replace_once(
    "source/roles/software-design/SKILL.md",
    "1. **Contract/outcome conformance challenge**",
    "1. **Contract/outcome conformance challenge (preserving contract conformance)**",
)

print("Protocol 5.7 stage-local test-contract reconciliation applied")
