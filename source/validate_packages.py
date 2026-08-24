#!/usr/bin/env python3
"""Independently validate generated Protocol skill packages as shipped artifacts."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
PROTOCOL_VERSION = (SOURCE / "PROTOCOL_VERSION").read_text(encoding="utf-8").strip()
MAX_SKILL_ZIP_BYTES = 25 * 1024 * 1024
REFERENCE_RE = re.compile(r"references/([A-Za-z0-9_.-]+\.md)")
TEMPLATE_RE = re.compile(r"templates/([A-Za-z0-9_.-]+\.md)")


def canonical_skills() -> dict[str, tuple[str, Path]]:
    found: dict[str, tuple[str, Path]] = {}
    for kind, parent in (("role", SOURCE / "roles"), ("specialist", SOURCE / "specialists")):
        if not parent.is_dir():
            continue
        for path in sorted(parent.iterdir()):
            if path.is_dir() and (path / "SKILL.md").is_file():
                found[path.name] = (kind, path)
    return found


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not terminated") from exc
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values, "\n".join(lines[end + 1 :])


def validate_agent_yaml(text: str) -> list[str]:
    errors: list[str] = []
    if not re.search(r"(?m)^interface:\s*$", text):
        errors.append("agents/openai.yaml missing interface mapping")
    if not re.search(r"(?m)^\s+display_name:\s*.+$", text):
        errors.append("agents/openai.yaml missing display_name")
    if not re.search(r"(?m)^\s+short_description:\s*.+$", text):
        errors.append("agents/openai.yaml missing short_description")
    return errors


def validate_package(path: Path, skill_name: str, kind: str, source_root: Path) -> list[str]:
    errors: list[str] = []
    if path.stat().st_size > MAX_SKILL_ZIP_BYTES:
        errors.append(f"{path.name}: exceeds 25 MB skill package limit")
    try:
        with zipfile.ZipFile(path, "r") as zf:
            names = zf.namelist()
            if len(names) != len(set(names)):
                errors.append(f"{path.name}: duplicate ZIP members")
            for name in names:
                posix = PurePosixPath(name)
                if posix.is_absolute() or ".." in posix.parts:
                    errors.append(f"{path.name}: unsafe ZIP member {name!r}")
            prefix = f"{skill_name}/"
            if any(not name.startswith(prefix) for name in names):
                errors.append(f"{path.name}: package must contain exactly one {skill_name}/ root")

            required = {
                f"{skill_name}/SKILL.md",
                f"{skill_name}/PROTOCOL_VERSION",
                f"{skill_name}/protocol-manifest.json",
                f"{skill_name}/agents/openai.yaml",
            }
            for member in sorted(required - set(names)):
                errors.append(f"{path.name}: missing required member {member}")
            if required - set(names):
                return errors

            skill_bytes = zf.read(f"{skill_name}/SKILL.md")
            canonical_skill = (source_root / "SKILL.md").read_bytes()
            if skill_bytes != canonical_skill:
                errors.append(f"{path.name}: packaged SKILL.md differs from canonical source")
            try:
                frontmatter, body = parse_frontmatter(skill_bytes.decode("utf-8"))
            except (UnicodeDecodeError, ValueError) as exc:
                errors.append(f"{path.name}: invalid SKILL.md: {exc}")
                body = ""
                frontmatter = {}
            if set(frontmatter) != {"name", "description"}:
                errors.append(
                    f"{path.name}: SKILL.md frontmatter keys must be exactly name, description"
                )
            if frontmatter.get("name") != skill_name:
                errors.append(f"{path.name}: frontmatter name mismatch")
            if not frontmatter.get("description", "").strip():
                errors.append(f"{path.name}: frontmatter description is empty")

            packaged_version = zf.read(f"{skill_name}/PROTOCOL_VERSION").decode("utf-8").strip()
            if packaged_version != PROTOCOL_VERSION:
                errors.append(f"{path.name}: protocol version mismatch")

            try:
                manifest = json.loads(
                    zf.read(f"{skill_name}/protocol-manifest.json").decode("utf-8")
                )
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                errors.append(f"{path.name}: invalid protocol manifest: {exc}")
                manifest = {}
            if manifest.get("protocol_version") != PROTOCOL_VERSION:
                errors.append(f"{path.name}: manifest protocol_version mismatch")
            if manifest.get("skill_name") != skill_name:
                errors.append(f"{path.name}: manifest skill_name mismatch")
            if kind == "role" and not manifest.get("role"):
                errors.append(f"{path.name}: role package missing manifest role")
            if kind == "specialist" and manifest.get("kind") != "specialist":
                errors.append(f"{path.name}: specialist package missing manifest kind")

            agent_member = f"{skill_name}/agents/openai.yaml"
            canonical_agent = (source_root / "agents" / "openai.yaml").read_bytes()
            agent_bytes = zf.read(agent_member)
            if agent_bytes != canonical_agent:
                errors.append(f"{path.name}: packaged agents/openai.yaml differs from source")
            try:
                errors.extend(
                    f"{path.name}: {message}"
                    for message in validate_agent_yaml(agent_bytes.decode("utf-8"))
                )
            except UnicodeDecodeError as exc:
                errors.append(f"{path.name}: agents/openai.yaml is not UTF-8: {exc}")

            referenced = set(REFERENCE_RE.findall(body))
            referenced_templates = set(TEMPLATE_RE.findall(body))
            for ref_name in sorted(referenced):
                member = f"{skill_name}/references/{ref_name}"
                if member not in names:
                    errors.append(f"{path.name}: routed reference is not packaged: {ref_name}")
            for template_name in sorted(referenced_templates):
                member = f"{skill_name}/templates/{template_name}"
                if member not in names:
                    errors.append(f"{path.name}: routed template is not packaged: {template_name}")

            for member in names:
                rel = member[len(prefix) :] if member.startswith(prefix) else ""
                if rel.startswith("references/"):
                    source_path = SOURCE / "shared" / rel
                elif rel.startswith("templates/"):
                    source_path = SOURCE / "shared" / rel
                else:
                    continue
                if not source_path.is_file():
                    errors.append(f"{path.name}: packaged resource has no canonical source: {rel}")
                elif zf.read(member) != source_path.read_bytes():
                    errors.append(f"{path.name}: packaged resource differs from canonical source: {rel}")
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(f"{path.name}: invalid ZIP: {exc}")
    return errors


def validate(dist: Path) -> list[str]:
    errors: list[str] = []
    skills = canonical_skills()
    if not dist.is_dir():
        return [f"distribution directory is missing: {dist}"]

    index_path = dist / "BUILD_INDEX.json"
    if not index_path.is_file():
        return ["BUILD_INDEX.json is missing"]
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"BUILD_INDEX.json is invalid: {exc}"]

    if index.get("protocol_version") != PROTOCOL_VERSION:
        errors.append("BUILD_INDEX protocol_version mismatch")
    if set(index.get("skills", [])) != set(skills):
        errors.append("BUILD_INDEX skill set does not match canonical source")

    expected_files = {"BUILD_INDEX.json", *(f"{name}.zip" for name in skills)}
    actual_files = {path.name for path in dist.iterdir() if path.is_file()}
    if actual_files != expected_files:
        errors.append(
            f"distribution file set mismatch: expected={sorted(expected_files)} "
            f"actual={sorted(actual_files)}"
        )

    for skill_name, (kind, source_root) in skills.items():
        agent = source_root / "agents" / "openai.yaml"
        if not agent.is_file():
            errors.append(f"canonical skill metadata missing: {agent}")
        package = dist / f"{skill_name}.zip"
        if package.is_file() and agent.is_file():
            errors.extend(validate_package(package, skill_name, kind, source_root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path, required=True)
    args = parser.parse_args()
    errors = validate(args.dist.resolve())
    if errors:
        for error in errors:
            print(error)
        return 1
    print("all generated Protocol skill packages are structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
