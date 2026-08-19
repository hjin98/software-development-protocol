#!/usr/bin/env python3
"""Build and verify self-contained role skills from canonical protocol source."""

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

ROLE_SPECS = {
    "software-design": {
        "role": "design",
        "references": [
            "architecture-and-design.md",
            "workplans-and-agent-handoff.md",
            "protocol-versioning-and-compatibility.md",
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
        ],
        "scripts": ["repo_inventory.py"],
        "templates": ["implementation_workplan_template.md"],
    },
    "software-implementation": {
        "role": "implementation",
        "references": [
            "workplans-and-agent-handoff.md",
            "protocol-versioning-and-compatibility.md",
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
        "templates": [
            "implementation_workplan_template.md",
            "qualification_handoff_template.md",
        ],
    },
    "software-qualification": {
        "role": "qualification",
        "references": [
            "workplans-and-agent-handoff.md",
            "protocol-versioning-and-compatibility.md",
            "git-and-version-control.md",
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
        "scripts": ["render_markdown_pdfs.py"],
        "templates": ["qualification_report_template.md"],
    },
    "software-verification": {
        "role": "verification",
        "references": [
            "architecture-and-design.md",
            "workplans-and-agent-handoff.md",
            "protocol-versioning-and-compatibility.md",
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
        ],
        "scripts": ["repo_inventory.py"],
        "templates": ["verification_report_template.md"],
    },
}

_RESOURCE_RE = re.compile(r"\b(references|scripts|templates)/([A-Za-z0-9_.-]+)")
_FRONTMATTER_NAME_RE = re.compile(r"(?m)^name:\s*([A-Za-z0-9_.-]+)\s*$")
_HARDCODED_PROTOCOL_RE = re.compile(
    r"(?m)^protocol_version:\s*[\"']?\d+\.\d+\.\d+(?:[-+][A-Za-z0-9_.-]+)?[\"']?\s*$"
)


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
    entries.extend(
        (f"references/{name}", SHARED / "references" / name)
        for name in spec["references"]
    )
    entries.extend(
        (f"scripts/{name}", SHARED / "scripts" / name)
        for name in spec["scripts"]
    )
    entries.extend(
        (f"templates/{name}", SHARED / "templates" / name)
        for name in spec["templates"]
    )
    return entries


def validate_sources(entries: list[tuple[str, Path]]) -> None:
    missing = [str(src) for _, src in entries if not src.is_file()]
    if missing:
        raise SystemExit("Missing canonical source files:\n  " + "\n  ".join(missing))


def validate_role_registry() -> None:
    actual = sorted(
        p.name for p in ROLES.iterdir()
        if p.is_dir() and (p / "SKILL.md").is_file()
    )
    expected = sorted(ROLE_SPECS)
    if actual != expected:
        raise SystemExit(
            "Role registry/source directory mismatch:\n"
            f"  ROLE_SPECS={expected}\n  source/roles={actual}"
        )

    for skill_name, spec in ROLE_SPECS.items():
        skill = ROLES / skill_name / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        match = _FRONTMATTER_NAME_RE.search(text)
        if match is None or match.group(1) != skill_name:
            raise SystemExit(
                f"{skill}: frontmatter name must be exactly {skill_name!r}"
            )
        allowed = {
            "references": set(spec["references"]),
            "scripts": set(spec["scripts"]),
            "templates": set(spec["templates"]),
        }
        for kind, name in _RESOURCE_RE.findall(text):
            if name not in allowed[kind]:
                raise SystemExit(
                    f"{skill}: references {kind}/{name} but ROLE_SPECS does not package it"
                )

    for template in (SHARED / "templates").glob("*.md"):
        text = template.read_text(encoding="utf-8")
        if _HARDCODED_PROTOCOL_RE.search(text):
            raise SystemExit(
                f"{template}: hard-codes a protocol version; use "
                "REPLACE_WITH_SKILL_PROTOCOL_VERSION"
            )


def build_one(skill_name: str, spec: dict, stage_root: Path) -> Path:
    entries = source_entries(skill_name, spec)
    validate_sources(entries)
    dst_root = stage_root / skill_name
    dst_root.mkdir(parents=True)

    source_hashes: dict[str, str] = {}
    package_hashes: dict[str, str] = {}
    for rel, src in entries:
        dst = dst_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        source_hashes[rel] = sha256(src)
        package_hashes[rel] = sha256(dst)

    canonical = {
        "protocol_version": PROTOCOL_VERSION,
        "skill_name": skill_name,
        "role": spec["role"],
        "canonical_source_sha256": dict(sorted(source_hashes.items())),
        "package_file_sha256": dict(sorted(package_hashes.items())),
    }
    canonical_bytes = json.dumps(
        canonical, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    manifest = {
        **canonical,
        "source_manifest_sha256": hashlib.sha256(canonical_bytes).hexdigest(),
        "generated_policy": (
            "Do not hand-edit generated skill packages; "
            "rebuild from canonical protocol source."
        ),
    }
    (dst_root / "protocol-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return dst_root


def deterministic_zip(src_root: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    if zip_path.exists():
        zip_path.unlink()
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


def build_distribution(
    out: Path, *, no_zip: bool = False, keep_expanded: bool = False
) -> None:
    validate_role_registry()

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    stage = out if no_zip or keep_expanded else Path(
        tempfile.mkdtemp(prefix="protocol-skill-stage-")
    )
    try:
        built: list[Path] = []
        for skill_name, spec in ROLE_SPECS.items():
            root = build_one(skill_name, spec, stage)
            built.append(root)
            if not no_zip:
                deterministic_zip(root, out / f"{skill_name}.zip")

        index = {
            "protocol_version": PROTOCOL_VERSION,
            "skills": [p.name for p in built],
            "artifacts": {
                p.name: (
                    f"{p.name}/" if no_zip else f"{p.name}.zip"
                )
                for p in built
            },
            "source": "canonical shared protocol + role SKILL.md",
        }
        (out / "BUILD_INDEX.json").write_text(
            json.dumps(index, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        if keep_expanded and stage != out:
            for role_root in built:
                shutil.copytree(role_root, out / role_root.name)
    finally:
        if stage != out:
            shutil.rmtree(stage, ignore_errors=True)


def file_hashes(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in sorted(p for p in root.rglob("*") if p.is_file())
    }


def check_distribution(out: Path) -> int:
    with tempfile.TemporaryDirectory(prefix="protocol-dist-check-") as td:
        expected = Path(td) / "dist"
        build_distribution(expected)
        expected_hashes = file_hashes(expected)
        actual_hashes = file_hashes(out)

    if actual_hashes == expected_hashes:
        print(f"PASS: {out} matches canonical protocol source ({PROTOCOL_VERSION})")
        return 0

    paths = sorted(set(expected_hashes) | set(actual_hashes))
    print("FAIL: generated distribution drift detected")
    for path in paths:
        e = expected_hashes.get(path)
        a = actual_hashes.get(path)
        if e != a:
            if e is None:
                label = "unexpected"
            elif a is None:
                label = "missing"
            else:
                label = "changed"
            print(f"  {label}: {path}")
    return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT.parent / "dist")
    parser.add_argument("--no-zip", action="store_true")
    parser.add_argument("--keep-expanded", action="store_true")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Rebuild in a temporary directory and compare against --output.",
    )
    args = parser.parse_args()

    out = args.output.resolve()
    if args.check:
        if args.no_zip or args.keep_expanded:
            parser.error("--check uses the canonical zipped distribution; "
                         "do not combine it with --no-zip/--keep-expanded")
        validate_role_registry()
        return check_distribution(out)

    build_distribution(
        out, no_zip=args.no_zip, keep_expanded=args.keep_expanded
    )
    for skill_name in ROLE_SPECS:
        artifact = (
            out / skill_name
            if args.no_zip
            else out / f"{skill_name}.zip"
        )
        print(artifact)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
