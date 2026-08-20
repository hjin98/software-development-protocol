#!/usr/bin/env python3
"""Build Protocol 4 role-skill ZIP packages from canonical source."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED = ROOT / "shared"
ROLES = ROOT / "roles"
PROTOCOL_VERSION = (ROOT / "PROTOCOL_VERSION").read_text(encoding="utf-8").strip()

CORE = [
    "workflow-and-workplans.md",
    "testing-and-validation.md",
    "protocol-versioning-and-compatibility.md",
]

ROLE_SPECS = {
    "software-design": {
        "role": "design",
        "references": CORE + [
            "architecture-and-design.md",
            "documentation-and-evidence.md",
            "specification-and-implementation.md",
        ],
        "templates": ["implementation_workplan_template.md"],
    },
    "software-implementation": {
        "role": "implementation",
        "references": CORE + [
            "debugging-and-state-recovery.md",
            "documentation-and-evidence.md",
            "specification-and-implementation.md",
            "release-and-distribution.md",
        ],
        "templates": [],
    },
}

NAME_RE = re.compile(r"(?m)^name:\s*([A-Za-z0-9_.-]+)\s*$")


def entries(skill_name: str, spec: dict) -> list[tuple[str, Path]]:
    out = [
        ("SKILL.md", ROLES / skill_name / "SKILL.md"),
        ("PROTOCOL_VERSION", ROOT / "PROTOCOL_VERSION"),
    ]
    out += [
        (f"references/{name}", SHARED / "references" / name)
        for name in spec["references"]
    ]
    out += [
        (f"templates/{name}", SHARED / "templates" / name)
        for name in spec["templates"]
    ]
    return out


def validate() -> None:
    actual = {p.name for p in ROLES.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    expected = set(ROLE_SPECS)
    if actual != expected:
        raise SystemExit(f"role registry mismatch: expected={sorted(expected)} actual={sorted(actual)}")

    for skill_name, spec in ROLE_SPECS.items():
        skill = ROLES / skill_name / "SKILL.md"
        match = NAME_RE.search(skill.read_text(encoding="utf-8"))
        if match is None or match.group(1) != skill_name:
            raise SystemExit(f"{skill}: frontmatter name mismatch")
        for _, path in entries(skill_name, spec):
            if not path.is_file():
                raise SystemExit(f"missing package source: {path}")


def build_one(skill_name: str, spec: dict, stage: Path) -> Path:
    root = stage / skill_name
    root.mkdir(parents=True, exist_ok=True)

    for rel, src in entries(skill_name, spec):
        dst = root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8").replace(
            "REPLACE_WITH_SKILL_PROTOCOL_VERSION", PROTOCOL_VERSION
        )
        dst.write_text(text, encoding="utf-8")

    (root / "protocol-manifest.json").write_text(
        json.dumps(
            {
                "protocol_version": PROTOCOL_VERSION,
                "skill_name": skill_name,
                "role": spec["role"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return root


def zip_tree(src_root: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        base = src_root.parent
        for path in sorted(p for p in src_root.rglob("*") if p.is_file()):
            zf.write(path, path.relative_to(base).as_posix())


def build(output: Path) -> None:
    validate()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    with tempfile.TemporaryDirectory(prefix="protocol4-") as tmp:
        stage = Path(tmp)
        for skill_name, spec in ROLE_SPECS.items():
            root = build_one(skill_name, spec, stage)
            zip_tree(root, output / f"{skill_name}.zip")

    (output / "BUILD_INDEX.json").write_text(
        json.dumps(
            {
                "protocol_version": PROTOCOL_VERSION,
                "skills": list(ROLE_SPECS),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT.parent / "dist")
    args = parser.parse_args()
    build(args.output.resolve())
    for skill_name in ROLE_SPECS:
        print(args.output.resolve() / f"{skill_name}.zip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
