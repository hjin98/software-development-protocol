#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"{label}: expected one match, found {text.count(old)}")
    return text.replace(old, new, 1)


def insert_after(text: str, anchor: str, insertion: str, label: str) -> str:
    return replace_once(text, anchor, anchor + "\n" + insertion.rstrip() + "\n", label)


def remove_section(text: str, heading: str, next_heading: str | None, label: str) -> str:
    start_marker = f"\n## {heading}\n"
    if text.count(start_marker) != 1:
        raise SystemExit(f"{label}: expected one {heading!r} section")
    start = text.index(start_marker)
    if next_heading is None:
        return text[:start].rstrip() + "\n"
    end_marker = f"\n## {next_heading}\n"
    end = text.find(end_marker, start + len(start_marker))
    if end < 0:
        raise SystemExit(f"{label}: missing next section {next_heading!r}")
    return text[:start] + text[end:]


def update_skill(path: Path, anchor: str, routing: str, old_heading: str, next_heading: str | None) -> None:
    text = path.read_text(encoding="utf-8")
    text = remove_section(text, old_heading, next_heading, str(path))
    text = insert_after(text, anchor, routing, str(path))
    path.write_text(text, encoding="utf-8")


DESIGN_ROUTING = r'''## Reference routing

Before substantive role reasoning, apply these explicit routes. A **MUST read** route is a precondition to the named decision or closure; other routes remain conditional so progressive disclosure is preserved.

### Role-critical routes

- Before creating or amending a workplan, closing a Design -> Implementation handoff, reviewing implementation for Pass/No Pass, reasoning about stages/gates, or routing rework/redesign, **MUST read** [Workflow and workplans](references/workflow-and-workplans.md).
- Before designing or reviewing testing, affected regression, integration, evidence reuse, proxy-proof acceptance, or qualification claims, **MUST read** [Testing and validation](references/testing-and-validation.md).
- Before a nontrivial architecture, ownership, algorithm, product-complexity, or redesign decision, or an independent engineering challenge, **MUST read** [Architecture and design](references/architecture-and-design.md).
- Before deciding protocol/workplan version binding, compatibility, or release-version semantics, **MUST read** [Protocol versioning and compatibility](references/protocol-versioning-and-compatibility.md).

### Domain-conditional routes

- When repository inspection strategy or context economy becomes material, read [Repository intake](references/repository-intake.md).
- When specification/API/schema ownership or implementation fidelity becomes material, read [Specification and implementation](references/specification-and-implementation.md).
- When documentation authority or evidence communication becomes material, read [Documentation and evidence](references/documentation-and-evidence.md).
- When packaging, installation, compatibility distribution, or release mechanics become material, read [Release and distribution](references/release-and-distribution.md).
- When configuration or policy surfaces become material, read [Configuration and policy](references/configuration-and-policy.md).
- When concurrency, scheduling, or orchestration becomes material, read [Concurrency and orchestration](references/concurrency-and-orchestration.md).
- When security or trust boundaries become material, read [Security and trust boundaries](references/security-and-trust-boundaries.md).
- When latency, throughput, scaling, parallelism, or hardware effectiveness becomes material, read [Performance and parallelism](references/performance-and-parallelism.md).
- When storage, filesystem, checkpoint, cache, or I/O behavior becomes material, read [Storage and I/O](references/storage-and-io.md).
- When scientific/numerical fidelity becomes material, read [Scientific software](references/scientific-software.md).
- When producing a substantial implementation workplan, use the [Implementation workplan template](templates/implementation_workplan_template.md).'''

IMPLEMENTATION_ROUTING = r'''## Reference routing

Before substantive implementation reasoning, apply these explicit routes. A **MUST read** route is a precondition to the named decision or closure; other routes remain conditional so progressive disclosure is preserved.

### Role-critical routes

- Before implementing from an accepted workplan, closing a material stage, performing local reconciliation, or routing a material redesign, **MUST read** [Workflow and workplans](references/workflow-and-workplans.md).
- Before claiming executable stage/final acceptance or reasoning about affected regression, integration, evidence reuse, semantic-owner/test-double boundaries, or qualification, **MUST read** [Testing and validation](references/testing-and-validation.md).
- Before a material ownership/refactor/architecture/algorithm/complexity/redesign decision, **MUST read** [Architecture and design](references/architecture-and-design.md).
- Before deciding protocol/workplan version binding, compatibility, or release-version semantics, **MUST read** [Protocol versioning and compatibility](references/protocol-versioning-and-compatibility.md).

### Domain-conditional routes

- When repository inspection strategy or context economy becomes material, read [Repository intake](references/repository-intake.md).
- When debugging, recovery, or state reconstruction becomes material, read [Debugging and state recovery](references/debugging-and-state-recovery.md).
- When specification/API/schema ownership or implementation fidelity becomes material, read [Specification and implementation](references/specification-and-implementation.md).
- When documentation authority or evidence communication becomes material, read [Documentation and evidence](references/documentation-and-evidence.md).
- When packaging, installation, compatibility distribution, or release mechanics become material, read [Release and distribution](references/release-and-distribution.md).
- When Git state, commits, branches, or repository version-control operations become material, read [Git and version control](references/git-and-version-control.md).
- When configuration or policy surfaces become material, read [Configuration and policy](references/configuration-and-policy.md).
- When concurrency, scheduling, or orchestration becomes material, read [Concurrency and orchestration](references/concurrency-and-orchestration.md).
- When security or trust boundaries become material, read [Security and trust boundaries](references/security-and-trust-boundaries.md).
- When latency, throughput, scaling, parallelism, or hardware effectiveness becomes material, read [Performance and parallelism](references/performance-and-parallelism.md).
- When storage, filesystem, checkpoint, cache, or I/O behavior becomes material, read [Storage and I/O](references/storage-and-io.md).
- When scientific/numerical fidelity becomes material, read [Scientific software](references/scientific-software.md).'''

DOCUMENTATION_ROUTING = r'''## Reference routing

Before substantive documentation reasoning, apply these explicit routes; load only the reference whose trigger is material.

- Before substantive documentation maintenance, reconciliation, refactoring, or current-state authority decisions, **MUST read** [Documentation maintenance](references/documentation-maintenance.md).
- Before deciding documentation/evidence authority or durable evidence presentation, **MUST read** [Documentation and evidence](references/documentation-and-evidence.md).
- When lifecycle/workplan state affects documentation, read [Workflow and workplans](references/workflow-and-workplans.md).
- When testing, acceptance, qualification, or evidence boundaries affect documentation, read [Testing and validation](references/testing-and-validation.md).
- When protocol/candidate compatibility or version binding affects documentation, read [Protocol versioning and compatibility](references/protocol-versioning-and-compatibility.md).
- When architecture/ownership is being explained or reconciled, read [Architecture and design](references/architecture-and-design.md).
- When specification/API/schema contracts are being explained or reconciled, read [Specification and implementation](references/specification-and-implementation.md).
- When scientific exposition or technical method writing is material, read [Scientific technical writing](references/scientific-technical-writing.md).
- When scientific/numerical semantics are material, read [Scientific software](references/scientific-software.md).
- When security or trust boundaries affect docs, rendering, credentials, or external resources, read [Security and trust boundaries](references/security-and-trust-boundaries.md).
- When documented performance/scaling/parallelism claims are material, read [Performance and parallelism](references/performance-and-parallelism.md).
- When documented storage/I/O behavior is material, read [Storage and I/O](references/storage-and-io.md).
- When generated/shipped documentation or release packaging is material, read [Release and distribution](references/release-and-distribution.md).'''

HYGIENE_ROUTING = r'''## Reference routing

Before substantive repository-hygiene reasoning, apply these explicit routes; load only the reference whose trigger is material.

- Before branch deletion or other material Git/ref operations, **MUST read** [Git and version control](references/git-and-version-control.md).
- Before archiving/closing workplans or reasoning about lifecycle closure, **MUST read** [Workflow and workplans](references/workflow-and-workplans.md).
- When cleanup can affect required regression/integration evidence, read [Testing and validation](references/testing-and-validation.md).
- When protocol/candidate compatibility or evidence invalidation is material, read [Protocol versioning and compatibility](references/protocol-versioning-and-compatibility.md).
- When broad repository inspection or context economy is material, read [Repository intake](references/repository-intake.md).
- When secrets, unsafe artifacts, or trust boundaries are material, read [Security and trust boundaries](references/security-and-trust-boundaries.md).
- When cache/checkpoint/scratch ownership or recovery value is material, read [Storage and I/O](references/storage-and-io.md).
- When tracked/generated/release artifact boundaries are material, read [Release and distribution](references/release-and-distribution.md).
- When distinguishing durable records/evidence from disposable coordination material, read [Documentation and evidence](references/documentation-and-evidence.md).'''

update_skill(
    SOURCE / "roles/software-design/SKILL.md",
    "Use this role when a change needs real design reasoning or independent review.\n",
    DESIGN_ROUTING,
    "Progressive-disclosure references",
    "Completion",
)
update_skill(
    SOURCE / "roles/software-implementation/SKILL.md",
    "Implement the accepted behavior as the globally best justified realization of the material requirements and design for the target environment.\n",
    IMPLEMENTATION_ROUTING,
    "Progressive-disclosure references",
    None,
)
update_skill(
    SOURCE / "specialists/software-documentation/SKILL.md",
    "Use this optional specialist when documentation needs substantive reconciliation, restructuring, theory/method explanation, user-oriented synthesis, or publication maintenance.\n",
    DOCUMENTATION_ROUTING,
    "Supporting references",
    "Completion",
)
update_skill(
    SOURCE / "specialists/repository-hygiene/SKILL.md",
    "Use this optional specialist **after a development stage is formally closed**, or when the user explicitly requests a repository-hygiene pass.\n",
    HYGIENE_ROUTING,
    "Supporting references",
    "Completion report",
)

# P1: build one canonical directory bundle tree and derive ZIPs from it.
build_path = SOURCE / "build_skills.py"
build = build_path.read_text(encoding="utf-8")
build = build.replace('"""Build skill ZIP packages from canonical protocol source."""', '"""Build portable skill directory bundles and ZIPs from canonical protocol source."""')
build = build.replace("import tempfile\n", "")
build = replace_once(
    build,
    'NAME_RE = re.compile(r"(?m)^name:\\s*([A-Za-z0-9_.-]+)\\s*$")',
    'NAME_RE = re.compile(r"(?m)^name:\\s*([a-z0-9]+(?:-[a-z0-9]+)*)\\s*$")',
    "build name regex",
)
start = build.index("def build(output: Path) -> None:\n")
end = build.index("\ndef main() -> int:\n", start)
new_build = '''def build(output: Path) -> None:\n    validate()\n    if output.exists():\n        shutil.rmtree(output)\n    output.mkdir(parents=True)\n    skills_output = output / "skills"\n    skills_output.mkdir()\n\n    for skill_name, spec, kind in all_specs():\n        root = build_one(skill_name, spec, kind, skills_output)\n        zip_tree(root, output / f"{skill_name}.zip")\n\n    all_names = [name for name, _, _ in all_specs()]\n    (output / "BUILD_INDEX.json").write_text(\n        json.dumps(\n            {\n                "protocol_version": PROTOCOL_VERSION,\n                "runtime_root": "skills",\n                "skills": all_names,\n                "lifecycle_roles": list(ROLE_SPECS),\n                "specialists": list(SPECIALIST_SPECS),\n            },\n            indent=2,\n            sort_keys=True,\n        )\n        + "\\n",\n        encoding="utf-8",\n    )\n'''
build = build[:start] + new_build + build[end:]
build = build.replace(
    '        print(args.output.resolve() / f"{skill_name}.zip")',
    '        print(args.output.resolve() / "skills" / skill_name)\n        print(args.output.resolve() / f"{skill_name}.zip")',
)
build_path.write_text(build, encoding="utf-8")

# P1/P2: independent validation of generic core, direct routes, vendor adapter, and directory/ZIP parity.
validator = r'''#!/usr/bin/env python3
"""Independently validate generated Protocol skill bundles and compatibility adapters."""

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
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TOP_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$")
RESOURCE_MENTION_RE = re.compile(r"(?<![A-Za-z0-9_.-])((?:references|templates)/[A-Za-z0-9_.-]+\.md)")
DIRECT_LINK_RE = re.compile(r"\[[^\]]+\]\(((?:references|templates)/[A-Za-z0-9_.-]+\.md)\)")
STANDARD_FRONTMATTER_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


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
        if not line.strip() or line[0].isspace():
            continue
        match = TOP_KEY_RE.fullmatch(line)
        if not match:
            raise ValueError(f"invalid top-level frontmatter line: {line!r}")
        key, value = match.groups()
        if key in values:
            raise ValueError(f"duplicate frontmatter key: {key}")
        values[key] = (value or "").strip().strip('"').strip("'")
    return values, "\n".join(lines[end + 1 :])


def validate_frontmatter(text: str, skill_name: str) -> tuple[list[str], str]:
    errors: list[str] = []
    try:
        frontmatter, body = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)], ""
    unknown = set(frontmatter) - STANDARD_FRONTMATTER_KEYS
    if unknown:
        errors.append(f"unsupported non-portable frontmatter keys: {sorted(unknown)}")
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not name:
        errors.append("frontmatter name is missing")
    elif len(name) > 64 or not NAME_RE.fullmatch(name):
        errors.append("frontmatter name violates portable kebab-case/64-character constraint")
    elif name != skill_name:
        errors.append("frontmatter name mismatch")
    if not description:
        errors.append("frontmatter description is empty")
    elif len(description) > 1024:
        errors.append("frontmatter description exceeds 1024 characters")
    return errors, body


def validate_agent_yaml(text: str) -> list[str]:
    errors: list[str] = []
    if not re.search(r"(?m)^interface:\s*$", text):
        errors.append("missing interface mapping")
    if not re.search(r"(?m)^\s+display_name:\s*.+$", text):
        errors.append("missing display_name")
    if not re.search(r"(?m)^\s+short_description:\s*.+$", text):
        errors.append("missing short_description")
    return errors


def directory_files(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(p for p in root.rglob("*") if p.is_file())
    }


def zip_files(path: Path, skill_name: str) -> tuple[dict[str, bytes], list[str]]:
    errors: list[str] = []
    files: dict[str, bytes] = {}
    try:
        with zipfile.ZipFile(path, "r") as zf:
            names = zf.namelist()
            if len(names) != len(set(names)):
                errors.append("duplicate ZIP members")
            prefix = f"{skill_name}/"
            for name in names:
                posix = PurePosixPath(name)
                if posix.is_absolute() or ".." in posix.parts:
                    errors.append(f"unsafe ZIP member {name!r}")
                    continue
                if not name.startswith(prefix):
                    errors.append(f"ZIP member is outside single {skill_name}/ root: {name!r}")
                    continue
                rel = name[len(prefix):]
                if rel and not name.endswith("/"):
                    files[rel] = zf.read(name)
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(f"invalid ZIP: {exc}")
    return files, errors


def expected_canonical_bytes(rel: str, source_root: Path) -> bytes | None:
    if rel == "SKILL.md":
        path = source_root / "SKILL.md"
    elif rel == "agents/openai.yaml":
        path = source_root / "agents/openai.yaml"
    elif rel.startswith("references/") or rel.startswith("templates/"):
        path = SOURCE / "shared" / rel
    else:
        return None
    if not path.is_file():
        return None
    return path.read_bytes().replace(
        b"REPLACE_WITH_SKILL_PROTOCOL_VERSION", PROTOCOL_VERSION.encode("utf-8")
    )


def validate_core_bundle(files: dict[str, bytes], skill_name: str, kind: str, source_root: Path) -> list[str]:
    errors: list[str] = []
    required = {"SKILL.md", "PROTOCOL_VERSION", "protocol-manifest.json"}
    for rel in sorted(required - set(files)):
        errors.append(f"generic core missing required member {rel}")
    if required - set(files):
        return errors

    try:
        skill_text = files["SKILL.md"].decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"SKILL.md is not UTF-8: {exc}"]
    fm_errors, body = validate_frontmatter(skill_text, skill_name)
    errors.extend(f"SKILL.md: {error}" for error in fm_errors)

    canonical_skill = expected_canonical_bytes("SKILL.md", source_root)
    if canonical_skill is None or files["SKILL.md"] != canonical_skill:
        errors.append("SKILL.md differs from canonical source")

    try:
        packaged_version = files["PROTOCOL_VERSION"].decode("utf-8").strip()
    except UnicodeDecodeError as exc:
        errors.append(f"PROTOCOL_VERSION is not UTF-8: {exc}")
        packaged_version = ""
    if packaged_version != PROTOCOL_VERSION:
        errors.append("protocol version mismatch")

    try:
        manifest = json.loads(files["protocol-manifest.json"].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"invalid protocol manifest: {exc}")
        manifest = {}
    if manifest.get("protocol_version") != PROTOCOL_VERSION:
        errors.append("manifest protocol_version mismatch")
    if manifest.get("skill_name") != skill_name:
        errors.append("manifest skill_name mismatch")
    if kind == "role" and not manifest.get("role"):
        errors.append("role package missing manifest role")
    if kind == "specialist" and manifest.get("kind") != "specialist":
        errors.append("specialist package missing manifest kind")

    mentions = set(RESOURCE_MENTION_RE.findall(body))
    direct_links = set(DIRECT_LINK_RE.findall(body))
    for rel in sorted(mentions):
        if rel not in files:
            errors.append(f"routed resource is not packaged: {rel}")
    packaged_routes = {
        rel for rel in files
        if (rel.startswith("references/") or rel.startswith("templates/")) and rel.endswith(".md")
    }
    for rel in sorted(packaged_routes - direct_links):
        errors.append(f"packaged resource is not directly Markdown-linked from SKILL.md: {rel}")

    for rel in sorted(packaged_routes):
        expected = expected_canonical_bytes(rel, source_root)
        if expected is None:
            errors.append(f"packaged resource has no canonical source: {rel}")
        elif files[rel] != expected:
            errors.append(f"packaged resource differs from canonical source: {rel}")
    return errors


def validate_openai_adapter(files: dict[str, bytes], source_root: Path) -> list[str]:
    rel = "agents/openai.yaml"
    if rel not in files:
        return ["OpenAI adapter missing agents/openai.yaml"]
    expected = expected_canonical_bytes(rel, source_root)
    if expected is None or files[rel] != expected:
        return ["OpenAI adapter differs from canonical source"]
    try:
        return [f"OpenAI adapter {error}" for error in validate_agent_yaml(files[rel].decode("utf-8"))]
    except UnicodeDecodeError as exc:
        return [f"OpenAI adapter is not UTF-8: {exc}"]


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
    if index.get("runtime_root") != "skills":
        errors.append("BUILD_INDEX runtime_root must be 'skills'")
    if set(index.get("skills", [])) != set(skills):
        errors.append("BUILD_INDEX skill set does not match canonical source")

    expected_top_files = {"BUILD_INDEX.json", *(f"{name}.zip" for name in skills)}
    actual_top_files = {path.name for path in dist.iterdir() if path.is_file()}
    if actual_top_files != expected_top_files:
        errors.append(
            f"distribution top-level file set mismatch: expected={sorted(expected_top_files)} actual={sorted(actual_top_files)}"
        )
    actual_top_dirs = {path.name for path in dist.iterdir() if path.is_dir()}
    if actual_top_dirs != {"skills"}:
        errors.append(f"distribution top-level directory set mismatch: expected=['skills'] actual={sorted(actual_top_dirs)}")

    skills_root = dist / "skills"
    if not skills_root.is_dir():
        return errors + ["unpacked runtime root dist/skills is missing"]
    runtime_dirs = {path.name for path in skills_root.iterdir() if path.is_dir()}
    if runtime_dirs != set(skills):
        errors.append(f"runtime skill set mismatch: expected={sorted(skills)} actual={sorted(runtime_dirs)}")

    for skill_name, (kind, source_root) in skills.items():
        dir_root = skills_root / skill_name
        dir_files = directory_files(dir_root) if dir_root.is_dir() else {}
        for error in validate_core_bundle(dir_files, skill_name, kind, source_root):
            errors.append(f"skills/{skill_name}: {error}")
        for error in validate_openai_adapter(dir_files, source_root):
            errors.append(f"skills/{skill_name}: {error}")

        package = dist / f"{skill_name}.zip"
        if not package.is_file():
            errors.append(f"{skill_name}.zip is missing")
            continue
        if package.stat().st_size > MAX_SKILL_ZIP_BYTES:
            errors.append(f"{package.name}: exceeds 25 MB skill package limit")
        zip_map, zip_errors = zip_files(package, skill_name)
        errors.extend(f"{package.name}: {error}" for error in zip_errors)
        for error in validate_core_bundle(zip_map, skill_name, kind, source_root):
            errors.append(f"{package.name}: {error}")
        for error in validate_openai_adapter(zip_map, source_root):
            errors.append(f"{package.name}: {error}")
        if dir_files != zip_map:
            missing = sorted(set(dir_files) - set(zip_map))
            extra = sorted(set(zip_map) - set(dir_files))
            changed = sorted(rel for rel in set(dir_files) & set(zip_map) if dir_files[rel] != zip_map[rel])
            errors.append(f"{skill_name}: unpacked/ZIP bundle mismatch: missing={missing} extra={extra} changed={changed}")
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
    print("all generated Protocol skill directory bundles and ZIPs are structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''
(SOURCE / "validate_packages.py").write_text(validator, encoding="utf-8")

check_dist = r'''#!/usr/bin/env python3
"""Compare a fresh protocol build with the committed distribution semantically."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def zip_contents(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path, "r") as zf:
        return {name: zf.read(name) for name in sorted(zf.namelist()) if not name.endswith("/")}


def relative_files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in sorted(p for p in root.rglob("*") if p.is_file())
    }


def compare(expected: Path, committed: Path) -> list[str]:
    errors: list[str] = []
    if not expected.is_dir():
        return [f"expected distribution directory is missing: {expected}"]
    if not committed.is_dir():
        return [f"committed distribution directory is missing: {committed}"]

    exp_files = relative_files(expected)
    got_files = relative_files(committed)
    if set(exp_files) != set(got_files):
        return [
            "dist recursive file set mismatch: "
            f"missing={sorted(set(exp_files) - set(got_files))} "
            f"extra={sorted(set(got_files) - set(exp_files))}"
        ]

    for rel in sorted(exp_files):
        exp = exp_files[rel]
        got = got_files[rel]
        if rel.endswith(".zip"):
            try:
                exp_tree = zip_contents(exp)
                got_tree = zip_contents(got)
            except (OSError, zipfile.BadZipFile) as exc:
                errors.append(f"invalid ZIP while comparing {rel}: {exc}")
                continue
            if got_tree != exp_tree:
                exp_keys = set(exp_tree)
                got_keys = set(got_tree)
                detail: list[str] = []
                detail.extend(f"missing {item}" for item in sorted(exp_keys - got_keys))
                detail.extend(f"extra {item}" for item in sorted(got_keys - exp_keys))
                detail.extend(
                    f"content differs {item}"
                    for item in sorted(exp_keys & got_keys)
                    if exp_tree[item] != got_tree[item]
                )
                errors.append(f"semantic package mismatch: {rel}: " + "; ".join(detail))
        elif rel.endswith(".json"):
            try:
                if json.loads(got.read_text(encoding="utf-8")) != json.loads(exp.read_text(encoding="utf-8")):
                    errors.append(f"JSON distribution mismatch: {rel}")
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON while comparing {rel}: {exc}")
        else:
            try:
                if got.read_bytes() != exp.read_bytes():
                    errors.append(f"distribution mismatch: {rel}")
            except OSError as exc:
                errors.append(f"failed to compare {rel}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected", type=Path, required=True)
    parser.add_argument("--committed", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    errors = compare(args.expected.resolve(), args.committed.resolve())
    if errors:
        for error in errors:
            print(error)
        return 1
    print("committed dist matches the fresh canonical build semantically")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''
(SOURCE / "check_dist.py").write_text(check_dist, encoding="utf-8")

# Version history: add only the routing/portability release description; doctrine remains untouched.
versioning_path = SOURCE / "shared/references/protocol-versioning-and-compatibility.md"
versioning = versioning_path.read_text(encoding="utf-8")
needle = "Protocol 5.8 is a backward-compatible **effective-compression and canonical-ownership refinement**. It intentionally preserves the material engineering semantics and historical failure-mode defenses of Protocols 5.4-5.7 while reducing always-loaded duplication. Lifecycle entrypoints retain high-salience invariants and role decision loops; detailed generic doctrine has one canonical owner where practical and is loaded when its material surface becomes relevant. Task workplans inherit generic protocol rules and preserve task-specific intent without copying protocol manuals. Stage proportionality reduces micro-gating ceremony without weakening affected-surface regression, semantic-owner acceptance, final assembled acceptance, or product-truth safeguards.\n"
addition = needle + "\nProtocol 5.9 is a backward-compatible **agent-portable deterministic-routing refinement**. It preserves the Protocol 5 hierarchy, two-role lifecycle, and all Protocol 5.4-5.8 hardening semantics unchanged while making progressive disclosure more reliable across Agent-Skills-style harnesses: role-critical task triggers route explicitly to exact linked references, domain references remain conditional, exported skill directories are first-class runtime bundles, and generic Agent Skill conformance is separated from vendor-adapter validation. The release changes reference reachability and distribution mechanics, not engineering doctrine.\n"
versioning = replace_once(versioning, needle, addition, "protocol versioning history")
versioning = versioning.replace("Protocol 5.8 or any other later release", "Protocol 5.9 or any other later release")
versioning_path.write_text(versioning, encoding="utf-8")

# Release version.
(SOURCE / "PROTOCOL_VERSION").write_text("5.9.0\n", encoding="utf-8")

# Documentation maintenance: preserve doctrine text, update only release/routing/distribution statements.
readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace(
    "Protocol 5.8 preserves the complete two-role lifecycle and the material engineering guarantees accumulated through Protocols 5.4-5.7 while reducing always-loaded instruction duplication:",
    "Protocol 5.9 preserves the complete two-role lifecycle and every material Protocol 5.4-5.8 engineering safeguard while making Protocol 5.8 progressive disclosure deterministic and portable across Agent-Skills-style harnesses:",
)
readme = readme.replace(
    "Protocol 5.8 uses **canonical detailed ownership + progressive disclosure**: lifecycle skills retain high-salience invariants and loading triggers, while detailed generic workflow/testing/architecture/intake/version rules live in their canonical references and are loaded when their material surface becomes relevant. This preserves Protocol 5.4 development economy without weakening Protocol 5.5 lossless handoff, Protocol 5.6 proxy-proof semantic-owner acceptance, or Protocol 5.7 engineering stewardship and acceptance integrity.",
    "Protocol 5.9 keeps Protocol 5.8 **canonical detailed ownership + progressive disclosure** unchanged, but makes routing explicit: role-critical task triggers require exact linked references before the corresponding decision or closure, while domain references remain conditional. This changes how reliably agents reach the doctrine, not what the doctrine means.",
)
readme = readme.replace(
    "`source/` is canonical and `dist/` contains committed generated skill packages. Before a protocol revision is complete:",
    "`source/` is canonical. `dist/skills/<skill-name>/` contains first-class ready-to-install directory bundles and the existing top-level ZIPs remain backward-compatible transport artifacts generated from the same bundle tree. See `PORTABILITY.md` for installation and real-harness routing qualification. Before a protocol revision is complete:",
)
readme_path.write_text(readme, encoding="utf-8")

source_readme_path = SOURCE / "README.md"
sreadme = source_readme_path.read_text(encoding="utf-8")
sreadme = sreadme.replace("# Software Development Protocol 5.8", "# Software Development Protocol 5.9")
sreadme = sreadme.replace("This directory is the canonical Protocol 5.8 source.", "This directory is the canonical Protocol 5.9 source.")
sreadme = sreadme.replace(
    "Protocol 5.8 preserves all material Protocol 5.4-5.7 guarantees while reducing control-plane duplication. High-salience invariants remain directly visible in lifecycle skills; detailed generic rules have one canonical reference owner where practical and are loaded when their material surface becomes relevant.",
    "Protocol 5.9 preserves all material Protocol 5.4-5.8 guarantees unchanged. It strengthens only routing and distribution: high-salience entrypoint triggers now link directly to exact canonical references, role-critical routes are mandatory under their named conditions, and domain references remain progressively disclosed.",
)
sreadme = sreadme.replace(
    "Load a reference when a material question enters its ownership domain; start with the relevant section and broaden only when cross-cutting evidence requires it. Context minimization never permits omission of plausible affected behavior or material evidence.",
    "Each packaged `SKILL.md` now maps material triggers directly to linked references. Role-critical routes are mandatory before the corresponding decision or closure; domain references remain conditional. Context minimization never permits omission of plausible affected behavior or material evidence.",
)
sreadme = sreadme.replace(
    "`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for distribution.",
    "`source/` is canonical. `dist/skills/<skill-name>/` contains generated ready-to-install directory bundles; top-level ZIPs are generated from the same bundles for backward-compatible transport. `agents/openai.yaml` is a separately validated OpenAI adapter, not part of generic Agent Skill validity. See `../PORTABILITY.md` for harness installation and live routing qualification.",
)
source_readme_path.write_text(sreadme, encoding="utf-8")

portability = r'''# Agent portability and routing qualification

Protocol 5.9 preserves Protocol 5.8 engineering doctrine and changes only skill routing, packaging, validation, and compatibility mechanics. The runtime installation unit is the self-contained directory under `dist/skills/<skill-name>/`; the top-level ZIP with the same skill name contains identical files under one enclosing skill directory.

## Installation contract

Install each skill as a direct child of a harness skill root so the entrypoint is exactly `<skills-root>/<skill-name>/SKILL.md`. Do not install `source/roles/...` or `source/specialists/...` directly: canonical source references live under `source/shared/` and become self-contained only in the generated bundles.

Use a harness-supported shared `.agents/skills` root when available, or the harness-native skill root when required. Current commonly supported locations include project `.agents/skills` for Pi, Gemini/Antigravity, GitHub Copilot, and DeepSeek Harness; Claude Code also supports `.claude/skills`, Copilot supports `.github/skills`, Pi supports `.pi/skills`, and DeepSeek Harness supports `.dsh/skills`. Harness-specific paths are integration guidance, not protocol doctrine; verify them against the harness version being qualified.

ZIPs are transport artifacts: extract the enclosing `<skill-name>/` directory before placing it under a runtime skill root. A symlinked/shared installation is a separate harness capability and must be qualified on that harness; direct-directory installation is the portability baseline.

## Why deterministic routing exists

Skill activation proves only that the harness/model obtained `SKILL.md`. Protocol 5.9 therefore makes role-critical routing explicit in each entrypoint: a material task trigger names the exact linked reference and states when reading it is mandatory. Domain references remain conditional so Protocol 5.8 progressive disclosure and context economy are preserved.

Static validation proves that references are packaged, directly linked, and structurally reachable. It cannot prove that a real harness/model actually performs the follow-up read, so live qualification is a separate evidence class.

## Bounded live qualification

Use `qualification/reference-routing/protocol-routing-sentinel/` as a tiny independent Agent Skill. The required answer token exists only in its bundled reference; `SKILL.md` deliberately does not contain the token.

For each harness/model/install mode being claimed:

1. copy the sentinel skill directory as a direct child of that harness's skill root;
2. start a fresh session so skill discovery is not inherited from an earlier context;
3. ask: `Use protocol-routing-sentinel and return the routing sentinel.`;
4. verify that the final answer equals the token in `references/sentinel.md`;
5. when the harness exposes a tool/file trajectory, verify an actual read of `references/sentinel.md` after skill activation;
6. classify failures separately as discovery, activation, resource-access/path-canonicalization, route-selection, or model-compliance failures.

A simulated parser or local file loader cannot establish a real-harness claim. If the harness does not expose file-read traces, a correct sentinel answer is behavioral evidence with lower confidence; report that limitation rather than claiming an observed read.

## Compatibility matrix

Record actual qualification results here or in a release/PR closeout. Do not infer a pass from static validation.

| Harness | Direct-directory routing | Read trace observed | Notes |
| --- | --- | --- | --- |
| Codex/OpenAI | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| Claude Code | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| Pi | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| Gemini CLI / Antigravity | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| GitHub Copilot | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |
| DeepSeek Harness | unqualified | — | Run the bounded sentinel scenario on the target harness/model. |

Ordinary repository CI intentionally does not call external agents. Live qualification may be promoted into CI only if credentials, harness/model versions, cost, and stochastic behavior become stable enough to make it a reliable release signal.
'''
(ROOT / "PORTABILITY.md").write_text(portability, encoding="utf-8")

fixture_root = ROOT / "qualification/reference-routing/protocol-routing-sentinel"
(fixture_root / "references").mkdir(parents=True, exist_ok=True)
(fixture_root / "SKILL.md").write_text(r'''---
name: protocol-routing-sentinel
description: Qualify whether an Agent-Skills-style harness follows an explicit SKILL.md route into a bundled reference. Use only for bounded skill-routing compatibility checks.
---

# Protocol Routing Sentinel

When asked for the routing sentinel, **MUST read** [Sentinel](references/sentinel.md) before answering. Return exactly the sentinel token defined there and nothing else. Do not guess or synthesize a token.
''', encoding="utf-8")
(fixture_root / "references/sentinel.md").write_text("# Routing sentinel\n\nThe exact sentinel token is `PROTOCOL_ROUTING_REFERENCE_5927`.\n", encoding="utf-8")

# Tooling tests: distinguish generic core, OpenAI adapter, direct routing, and recursive dist parity.
tooling_test = r'''from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(SOURCE))

import build_skills  # noqa: E402
import check_dist  # noqa: E402
import validate_packages  # noqa: E402


def rewrite_zip(path: Path, transform) -> None:
    with zipfile.ZipFile(path, "r") as zf:
        members = [(info.filename, zf.read(info.filename)) for info in zf.infolist()]
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, data in transform(members):
            zf.writestr(name, data)


class ProtocolToolingTests(unittest.TestCase):
    def test_build_and_validate_packages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            self.assertEqual([], validate_packages.validate(dist))

    def test_build_emits_unpacked_and_zip_runtime_forms(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            for skill in build_skills.ROLE_SPECS | build_skills.SPECIALIST_SPECS:
                self.assertTrue((dist / "skills" / skill / "SKILL.md").is_file())
                self.assertTrue((dist / f"{skill}.zip").is_file())

    def test_implementation_package_contains_cross_cutting_references_and_openai_adapter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            with zipfile.ZipFile(dist / "software-implementation.zip", "r") as zf:
                names = set(zf.namelist())
            prefix = "software-implementation/"
            required = {
                prefix + "agents/openai.yaml",
                prefix + "references/configuration-and-policy.md",
                prefix + "references/concurrency-and-orchestration.md",
                prefix + "references/security-and-trust-boundaries.md",
                prefix + "references/repository-intake.md",
                prefix + "references/git-and-version-control.md",
            }
            self.assertTrue(required <= names, required - names)

    def test_generic_core_validation_does_not_require_openai_adapter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            root = dist / "skills" / "software-design"
            files = validate_packages.directory_files(root)
            files.pop("agents/openai.yaml")
            errors = validate_packages.validate_core_bundle(
                files, "software-design", "role", SOURCE / "roles/software-design"
            )
            self.assertEqual([], errors)

    def test_repository_adapter_validation_rejects_missing_openai_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            package = dist / "software-design.zip"

            def without_agent(members):
                return [(name, data) for name, data in members if not name.endswith("agents/openai.yaml")]

            rewrite_zip(package, without_agent)
            errors = validate_packages.validate(dist)
            self.assertTrue(any("OpenAI adapter missing" in error for error in errors), errors)

    def test_validator_rejects_broken_direct_reference_route(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            package = dist / "software-design.zip"

            def add_bad_route(members):
                out = []
                for name, data in members:
                    if name.endswith("/SKILL.md"):
                        data += b"\nRead [missing](references/not-packaged.md).\n"
                    out.append((name, data))
                return out

            rewrite_zip(package, add_bad_route)
            errors = validate_packages.validate(dist)
            self.assertTrue(any("routed resource is not packaged" in error for error in errors), errors)

    def test_validator_rejects_packaged_unlinked_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            package = dist / "software-design.zip"

            def add_unlinked(members):
                members.append(("software-design/references/unlinked.md", b"sentinel\n"))
                return members

            rewrite_zip(package, add_unlinked)
            errors = validate_packages.validate(dist)
            self.assertTrue(any("not directly Markdown-linked" in error for error in errors), errors)

    def test_frontmatter_accepts_standard_optional_field(self) -> None:
        text = "---\nname: sample-skill\ndescription: Portable sample.\nlicense: MIT\nmetadata:\n  owner: test\n---\nbody\n"
        errors, _ = validate_packages.validate_frontmatter(text, "sample-skill")
        self.assertEqual([], errors)

    def test_frontmatter_rejects_nonportable_name(self) -> None:
        text = "---\nname: Bad_Name\ndescription: Sample.\n---\nbody\n"
        errors, _ = validate_packages.validate_frontmatter(text, "Bad_Name")
        self.assertTrue(any("kebab-case" in error for error in errors), errors)

    def test_dist_parity_detects_modified_zip_member(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            expected = Path(tmp) / "expected"
            committed = Path(tmp) / "committed"
            build_skills.build(expected)
            shutil.copytree(expected, committed)
            package = committed / "software-implementation.zip"

            def modify_skill(members):
                out = []
                for name, data in members:
                    if name.endswith("/SKILL.md"):
                        data += b"\n# tampered\n"
                    out.append((name, data))
                return out

            rewrite_zip(package, modify_skill)
            errors = check_dist.compare(expected, committed)
            self.assertTrue(any("semantic package mismatch" in error for error in errors), errors)

    def test_dist_parity_detects_modified_unpacked_member(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            expected = Path(tmp) / "expected"
            committed = Path(tmp) / "committed"
            build_skills.build(expected)
            shutil.copytree(expected, committed)
            skill = committed / "skills/software-design/SKILL.md"
            skill.write_text(skill.read_text(encoding="utf-8") + "\n# tampered\n", encoding="utf-8")
            errors = check_dist.compare(expected, committed)
            self.assertTrue(any("distribution mismatch" in error for error in errors), errors)

    def test_dist_parity_ignores_zip_metadata_when_contents_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            expected = Path(tmp) / "expected"
            committed = Path(tmp) / "committed"
            build_skills.build(expected)
            shutil.copytree(expected, committed)
            package = committed / "software-design.zip"
            rewrite_zip(package, lambda members: members)
            self.assertEqual([], check_dist.compare(expected, committed))

    def test_build_index_matches_protocol_version_and_runtime_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            build_skills.build(dist)
            index = json.loads((dist / "BUILD_INDEX.json").read_text(encoding="utf-8"))
            version = (SOURCE / "PROTOCOL_VERSION").read_text(encoding="utf-8").strip()
            self.assertEqual(version, index["protocol_version"])
            self.assertEqual("skills", index["runtime_root"])


if __name__ == "__main__":
    unittest.main()
'''
(ROOT / "tests/test_protocol_tooling.py").write_text(tooling_test, encoding="utf-8")

portability_test = r'''from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
HIERARCHY = "product engineering fitness > minimum justified product/system complexity > development economy"
LINK_RE = re.compile(r"\[[^\]]+\]\((references/[A-Za-z0-9_.-]+\.md)\)")

EXPECTED_REFERENCES = {
    "roles/software-design": {
        "workflow-and-workplans.md", "testing-and-validation.md", "protocol-versioning-and-compatibility.md",
        "architecture-and-design.md", "documentation-and-evidence.md", "specification-and-implementation.md",
        "release-and-distribution.md", "repository-intake.md", "configuration-and-policy.md",
        "concurrency-and-orchestration.md", "security-and-trust-boundaries.md", "performance-and-parallelism.md",
        "storage-and-io.md", "scientific-software.md",
    },
    "roles/software-implementation": {
        "workflow-and-workplans.md", "testing-and-validation.md", "protocol-versioning-and-compatibility.md",
        "architecture-and-design.md", "debugging-and-state-recovery.md", "documentation-and-evidence.md",
        "specification-and-implementation.md", "release-and-distribution.md", "repository-intake.md",
        "git-and-version-control.md", "configuration-and-policy.md", "concurrency-and-orchestration.md",
        "security-and-trust-boundaries.md", "performance-and-parallelism.md", "storage-and-io.md", "scientific-software.md",
    },
    "specialists/software-documentation": {
        "workflow-and-workplans.md", "testing-and-validation.md", "protocol-versioning-and-compatibility.md",
        "architecture-and-design.md", "documentation-and-evidence.md", "documentation-maintenance.md",
        "scientific-technical-writing.md", "specification-and-implementation.md", "release-and-distribution.md",
        "security-and-trust-boundaries.md", "performance-and-parallelism.md", "storage-and-io.md", "scientific-software.md",
    },
    "specialists/repository-hygiene": {
        "workflow-and-workplans.md", "testing-and-validation.md", "protocol-versioning-and-compatibility.md",
        "git-and-version-control.md", "documentation-and-evidence.md", "release-and-distribution.md",
        "repository-intake.md", "security-and-trust-boundaries.md", "storage-and-io.md",
    },
}


class ProtocolPortabilityTests(unittest.TestCase):
    def test_doctrine_hierarchy_remains_verbatim_in_lifecycle_entrypoints(self) -> None:
        for rel in ("roles/software-design", "roles/software-implementation"):
            text = (SOURCE / rel / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(HIERARCHY, text, rel)

    def test_reference_sets_are_preserved_and_directly_linked(self) -> None:
        for rel, expected in EXPECTED_REFERENCES.items():
            text = (SOURCE / rel / "SKILL.md").read_text(encoding="utf-8")
            linked = {Path(path).name for path in LINK_RE.findall(text)}
            self.assertEqual(expected, linked, rel)

    def test_design_role_critical_routes_are_mandatory(self) -> None:
        text = (SOURCE / "roles/software-design/SKILL.md").read_text(encoding="utf-8")
        for path in (
            "references/workflow-and-workplans.md",
            "references/testing-and-validation.md",
            "references/architecture-and-design.md",
            "references/protocol-versioning-and-compatibility.md",
        ):
            line = next(line for line in text.splitlines() if f"]({path})" in line)
            self.assertIn("MUST read", line, path)

    def test_implementation_role_critical_routes_are_mandatory(self) -> None:
        text = (SOURCE / "roles/software-implementation/SKILL.md").read_text(encoding="utf-8")
        for path in (
            "references/workflow-and-workplans.md",
            "references/testing-and-validation.md",
            "references/architecture-and-design.md",
            "references/protocol-versioning-and-compatibility.md",
        ):
            line = next(line for line in text.splitlines() if f"]({path})" in line)
            self.assertIn("MUST read", line, path)

    def test_sentinel_value_is_reference_only(self) -> None:
        root = ROOT / "qualification/reference-routing/protocol-routing-sentinel"
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        reference = (root / "references/sentinel.md").read_text(encoding="utf-8")
        token = re.search(r"`(PROTOCOL_ROUTING_REFERENCE_[0-9]+)`", reference)
        self.assertIsNotNone(token)
        self.assertNotIn(token.group(1), skill)
        self.assertIn("](references/sentinel.md)", skill)
        self.assertIn("MUST read", skill)


if __name__ == "__main__":
    unittest.main()
'''
(ROOT / "tests/test_protocol_portability.py").write_text(portability_test, encoding="utf-8")

# Build-index contract: explicitly retain the first-class runtime root.
idx_test_path = ROOT / "tests/test_build_index_contract.py"
idx = idx_test_path.read_text(encoding="utf-8")
idx = replace_once(
    idx,
    '            index = json.loads((dist / "BUILD_INDEX.json").read_text(encoding="utf-8"))\n',
    '            index = json.loads((dist / "BUILD_INDEX.json").read_text(encoding="utf-8"))\n            self.assertEqual("skills", index["runtime_root"])\n',
    "build-index test",
)
idx_test_path.write_text(idx, encoding="utf-8")

print("Protocol 5.9 source, routing, validation, qualification fixture, and documentation changes applied.")
