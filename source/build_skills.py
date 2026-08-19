#!/usr/bin/env python3
"""Build and verify deterministic Protocol v3 role skill packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED = ROOT / "shared"
ROLES = ROOT / "roles"
PROTOCOL_VERSION = (ROOT / "PROTOCOL_VERSION").read_text(encoding="utf-8").strip()

CORE = [
    "workplans-and-agent-handoff.md",
    "protocol-versioning-and-compatibility.md",
    "testing-and-qualification.md",
]

ROLE_SPECS = {
    "software-design": {
        "role": "design",
        "references": CORE + [
            "documentation-and-evidence.md",
            "specification-and-implementation.md",
        ],
        "templates": ["implementation_workplan_template.md"],
    },
    "software-implementation": {
        "role": "implementation",
        "references": CORE + [
            "documentation-and-evidence.md",
            "specification-and-implementation.md",
            "release-and-distribution.md",
        ],
        "templates": [
            "implementation_workplan_template.md",
            "qualification_handoff_template.md",
        ],
    },
    "software-qualification": {
        "role": "qualification",
        "references": CORE + ["release-and-distribution.md"],
        "templates": ["qualification_report_template.md"],
    },
    "software-verification": {
        "role": "verification",
        "references": CORE + [
            "documentation-and-evidence.md",
            "release-and-distribution.md",
        ],
        "templates": ["verification_report_template.md"],
    },
}

FRONTMATTER_NAME_RE = re.compile(r"(?m)^name:\s*([A-Za-z0-9_.-]+)\s*$")
HARDCODED_PROTOCOL_RE = re.compile(
    r"(?m)^protocol_version:\s*[\"']?\d+\.\d+\.\d+(?:[-+][A-Za-z0-9_.-]+)?[\"']?\s*$"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def source_entries(skill_name: str, spec: dict) -> list[tuple[str, Path]]:
    entries = [
        ("SKILL.md", ROLES / skill_name / "SKILL.md"),
        ("PROTOCOL_VERSION", ROOT / "PROTOCOL_VERSION"),
    ]
    entries += [
        (f"references/{name}", SHARED / "references" / name)
        for name in spec["references"]
    ]
    entries += [
        (f"templates/{name}", SHARED / "templates" / name)
        for name in spec["templates"]
    ]
    return entries


def validate_sources() -> None:
    actual_roles = {
        p.name for p in ROLES.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    }
    if actual_roles != set(ROLE_SPECS):
        raise SystemExit(
            f"role registry mismatch: expected={sorted(ROLE_SPECS)} actual={sorted(actual_roles)}"
        )

    for skill_name, spec in ROLE_SPECS.items():
        skill = ROLES / skill_name / "SKILL.md"
        match = FRONTMATTER_NAME_RE.search(skill.read_text(encoding="utf-8"))
        if match is None or match.group(1) != skill_name:
            raise SystemExit(f"{skill}: frontmatter name mismatch")
        for _, path in source_entries(skill_name, spec):
            if not path.is_file():
                raise SystemExit(f"missing canonical package source: {path}")

    for template in (SHARED / "templates").glob("*.md"):
        text = template.read_text(encoding="utf-8")
        if HARDCODED_PROTOCOL_RE.search(text):
            raise SystemExit(
                f"{template}: hard-coded protocol version; use REPLACE_WITH_SKILL_PROTOCOL_VERSION"
            )


def build_one(skill_name: str, spec: dict, stage: Path) -> Path:
    root = stage / skill_name
    root.mkdir(parents=True, exist_ok=True)
    source_hashes: dict[str, str] = {}
    for rel, src in source_entries(skill_name, spec):
        dst = root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        data = src.read_bytes()
        dst.write_bytes(data)
        source_hashes[rel] = sha256_bytes(data)

    canonical = {
        "protocol_version": PROTOCOL_VERSION,
        "skill_name": skill_name,
        "role": spec["role"],
        "canonical_source_sha256": dict(sorted(source_hashes.items())),
    }
    canonical_bytes = json.dumps(
        canonical, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    manifest = {
        **canonical,
        "source_manifest_sha256": sha256_bytes(canonical_bytes),
        "generated_policy": "Generated from canonical protocol source; do not hand-edit dist packages.",
    }
    (root / "protocol-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return root


def deterministic_zip(src_root: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    base = src_root.parent
    with zipfile.ZipFile(
        zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as zf:
        for path in sorted(p for p in src_root.rglob("*") if p.is_file()):
            rel = path.relative_to(base).as_posix()
            info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if path.suffix == ".py" else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            zf.writestr(info, path.read_bytes())


def build_distribution(out: Path) -> None:
    validate_sources()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    with tempfile.TemporaryDirectory(prefix="protocol-stage-") as td:
        stage = Path(td)
        for skill_name, spec in ROLE_SPECS.items():
            root = build_one(skill_name, spec, stage)
            deterministic_zip(root, out / f"{skill_name}.zip")

    index = {
        "protocol_version": PROTOCOL_VERSION,
        "skills": list(ROLE_SPECS),
        "artifacts": {name: f"{name}.zip" for name in ROLE_SPECS},
        "source": "canonical materiality-first protocol source",
    }
    (out / "BUILD_INDEX.json").write_text(
        json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def file_hashes(root: Path) -> dict[str, str]:
    return {
        p.relative_to(root).as_posix(): sha256(p)
        for p in sorted(root.rglob("*")) if p.is_file()
    } if root.exists() else {}


def check_distribution(out: Path) -> int:
    with tempfile.TemporaryDirectory(prefix="protocol-check-") as td:
        expected = Path(td) / "dist"
        build_distribution(expected)
        expected_hashes = file_hashes(expected)
    actual_hashes = file_hashes(out)
    if actual_hashes == expected_hashes:
        print(f"PASS: {out} matches canonical protocol source ({PROTOCOL_VERSION})")
        return 0
    print("FAIL: generated distribution drift detected")
    for path in sorted(set(expected_hashes) | set(actual_hashes)):
        if expected_hashes.get(path) != actual_hashes.get(path):
            print(f"  changed: {path}")
    return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT.parent / "dist")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    out = args.output.resolve()
    if args.check:
        return check_distribution(out)
    build_distribution(out)
    for skill_name in ROLE_SPECS:
        print(out / f"{skill_name}.zip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
