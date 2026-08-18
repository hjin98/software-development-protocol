#!/usr/bin/env python3
"""Build self-contained role skills from the canonical protocol source."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED = ROOT / "shared"
ROLES = ROOT / "roles"
PROTOCOL_VERSION = (ROOT / "PROTOCOL_VERSION").read_text(encoding="utf-8").strip()

ROLE_SPECS = {
    "software-design-review": {
        "role": "design-review",
        "references": [
            "architecture-and-design.md",
            "workplans-and-agent-handoff.md",
            "repository-intake.md",
            "git-and-version-control.md",
            "debugging-and-state-recovery.md",
            "scientific-software.md",
            "performance-and-parallelism.md",
            "storage-and-io.md",
            "concurrency-and-orchestration.md",
            "configuration-and-policy.md",
            "security-and-trust-boundaries.md",
            "specification-and-implementation.md",
            "testing-and-qualification.md",
            "documentation-and-evidence.md",
            "release-and-distribution.md",
            "mdstats-validation-case-study.md",
        ],
        "scripts": ["repo_inventory.py"],
        "templates": ["implementation_workplan_template.md"],
    },
    "software-implementation": {
        "role": "implementation",
        "references": [
            "workplans-and-agent-handoff.md",
            "repository-intake.md",
            "git-and-version-control.md",
            "specification-and-implementation.md",
            "testing-and-qualification.md",
            "scientific-software.md",
            "performance-and-parallelism.md",
            "storage-and-io.md",
            "concurrency-and-orchestration.md",
            "configuration-and-policy.md",
            "security-and-trust-boundaries.md",
            "debugging-and-state-recovery.md",
            "documentation-and-evidence.md",
            "release-and-distribution.md",
        ],
        "scripts": ["repo_inventory.py", "render_markdown_pdfs.py"],
        "templates": ["implementation_workplan_template.md"],
    },
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def source_entries(skill_name: str, spec: dict) -> list[tuple[str, Path]]:
    entries: list[tuple[str, Path]] = [
        ("SKILL.md", ROLES / skill_name / "SKILL.md"),
        ("PROTOCOL_VERSION", ROOT / "PROTOCOL_VERSION"),
    ]
    entries.extend((f"references/{name}", SHARED / "references" / name) for name in spec["references"])
    entries.extend((f"scripts/{name}", SHARED / "scripts" / name) for name in spec["scripts"])
    entries.extend((f"templates/{name}", SHARED / "templates" / name) for name in spec["templates"])
    return entries


def validate_sources(entries: list[tuple[str, Path]]) -> None:
    missing = [str(src) for _, src in entries if not src.is_file()]
    if missing:
        raise SystemExit("Missing canonical source files:\n  " + "\n  ".join(missing))


def build_one(skill_name: str, spec: dict, out_root: Path) -> Path:
    entries = source_entries(skill_name, spec)
    validate_sources(entries)
    dst_root = out_root / skill_name
    if dst_root.exists():
        shutil.rmtree(dst_root)
    dst_root.mkdir(parents=True)

    source_hashes: dict[str, str] = {}
    for rel, src in entries:
        dst = dst_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        source_hashes[rel] = sha256(src)

    canonical = {
        "protocol_version": PROTOCOL_VERSION,
        "skill_name": skill_name,
        "role": spec["role"],
        "canonical_source_sha256": dict(sorted(source_hashes.items())),
    }
    canonical_bytes = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode("utf-8")
    manifest = {
        **canonical,
        "source_manifest_sha256": hashlib.sha256(canonical_bytes).hexdigest(),
        "generated_policy": "Do not hand-edit generated skill packages; rebuild from canonical protocol source.",
    }
    (dst_root / "protocol-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return dst_root


def deterministic_zip(src_root: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    if zip_path.exists():
        zip_path.unlink()
    base = src_root.parent
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in src_root.rglob("*") if p.is_file()):
            rel = path.relative_to(base).as_posix()
            info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if path.suffix == ".py" else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            zf.writestr(info, path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--no-zip", action="store_true")
    args = parser.parse_args()

    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)

    built = []
    for skill_name, spec in ROLE_SPECS.items():
        root = build_one(skill_name, spec, out)
        built.append(root)
        if not args.no_zip:
            deterministic_zip(root, out / f"{skill_name}.zip")

    index = {
        "protocol_version": PROTOCOL_VERSION,
        "skills": [p.name for p in built],
        "source": "canonical shared protocol + role SKILL.md",
    }
    (out / "BUILD_INDEX.json").write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for p in built:
        print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
